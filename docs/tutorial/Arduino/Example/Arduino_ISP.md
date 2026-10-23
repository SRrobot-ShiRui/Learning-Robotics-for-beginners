# ArduinoISP
这段代码是一个Arduino程序，用于将Arduino转换为一个AVR ISP（In-System Programmer），可以用来编程和操作AVR微控制器。
```cpp
// ArduinoISP version 04m3
// Copyright (c) 2008-2011 Randall Bohn
// If you require a license, see
//     http://www.opensource.org/licenses/bsd-license.php
//
// This sketch turns the Arduino into a AVRISP
// using the following arduino pins:
//
// pin name:    not-mega:         mega(1280 and 2560)
// slave reset: 10:               53
// MOSI:        11:               51
// MISO:        12:               50
// SCK:         13:               52
//
// Put an LED (with resistor) on the following pins:
// 9: Heartbeat   - shows the programmer is running
// 8: Error       - Lights up if something goes wrong (use red if that makes sense)
// 7: Programming - In communication with the slave
//
// 23 July 2011 Randall Bohn
// -Address Arduino issue 509 :: Portability of ArduinoISP
// http://code.google.com/p/arduino/issues/detail?id=509
//
// October 2010 by Randall Bohn
// - Write to EEPROM > 256 bytes
// - Better use of LEDs:
// -- Flash LED_PMODE on each flash commit
// -- Flash LED_PMODE while writing EEPROM (both give visual feedback of writing progress)
// - Light LED_ERR whenever we hit a STK_NOSYNC. Turn it off when back in sync.
// - Use pins_arduino.h (should also work on Arduino Mega)
//
// October 2009 by David A. Mellis
// - Added support for the read signature command
//
// February 2009 by Randall Bohn
// - Added support for writing to EEPROM (what took so long?)
// Windows users should consider WinAVR's avrdude instead of the
// avrdude included with Arduino software.
//
// January 2008 by Randall Bohn
// - Thanks to Amplificar for helping me with the STK500 protocol
// - The AVRISP/STK500 (mk I) protocol is used in the arduino bootloader
// - The SPI functions herein were developed for the AVR910_ARD programmer
// - More information at http://code.google.com/p/mega-isp

#include "pins_arduino.h"
#define RESET     SS

#define LED_HB    9
#define LED_ERR   8
#define LED_PMODE 7
#define PROG_FLICKER true

#define HWVER 2
#define SWMAJ 1
#define SWMIN 18

// STK Definitions
#define STK_OK      0x10
#define STK_FAILED  0x11
#define STK_UNKNOWN 0x12
#define STK_INSYNC  0x14
#define STK_NOSYNC  0x15
#define CRC_EOP     0x20 //ok it is a space...

void pulse(int pin, int times);

void setup() {
  Serial.begin(19200);
  pinMode(LED_PMODE, OUTPUT);
  pulse(LED_PMODE, 2);
  pinMode(LED_ERR, OUTPUT);
  pulse(LED_ERR, 2);
  pinMode(LED_HB, OUTPUT);
  pulse(LED_HB, 2);
}

int error = 0;
int pmode = 0;
// address for reading and writing, set by 'U' command
int here;
uint8_t buff[256]; // global block storage

#define beget16(addr) (*addr * 256 + *(addr+1) )
typedef struct param {
  uint8_t devicecode;
  uint8_t revision;
  uint8_t progtype;
  uint8_t parmode;
  uint8_t polling;
  uint8_t selftimed;
  uint8_t lockbytes;
  uint8_t fusebytes;
  int flashpoll;
  int eeprompoll;
  int pagesize;
  int eepromsize;
  int flashsize;
}
parameter;

parameter param;

// this provides a heartbeat on pin 9, so you can tell the software is running.
uint8_t hbval = 128;
int8_t hbdelta = 8;
void heartbeat() {
  if (hbval > 192) hbdelta = -hbdelta;
  if (hbval < 32) hbdelta = -hbdelta;
  hbval += hbdelta;
  analogWrite(LED_HB, hbval);
  delay(20);
}


void loop(void) {
  // is pmode active?
  if (pmode) digitalWrite(LED_PMODE, HIGH);
  else digitalWrite(LED_PMODE, LOW);
  // is there an error?
  if (error) digitalWrite(LED_ERR, HIGH);
  else digitalWrite(LED_ERR, LOW);

  // light the heartbeat LED
  heartbeat();
  if (Serial.available()) {
    avrisp();
  }
}

uint8_t getch() {
  while (!Serial.available());
  return Serial.read();
}
void fill(int n) {
  for (int x = 0; x < n; x++) {
    buff[x] = getch();
  }
}

#define PTIME 30
void pulse(int pin, int times) {
  do {
    digitalWrite(pin, HIGH);
    delay(PTIME);
    digitalWrite(pin, LOW);
    delay(PTIME);
  }
  while (times--);
}

void prog_lamp(int state) {
  if (PROG_FLICKER)
    digitalWrite(LED_PMODE, state);
}

void spi_init() {
  uint8_t x;
  SPCR = 0x53;
  x = SPSR;
  x = SPDR;
}

void spi_wait() {
  do {
  }
  while (!(SPSR & (1 << SPIF)));
}

uint8_t spi_send(uint8_t b) {
  uint8_t reply;
  SPDR = b;
  spi_wait();
  reply = SPDR;
  return reply;
}

uint8_t spi_transaction(uint8_t a, uint8_t b, uint8_t c, uint8_t d) {
  uint8_t n;
  spi_send(a);
  n = spi_send(b);
  //if (n != a) error = -1;
  n = spi_send(c);
  return spi_send(d);
}

void empty_reply() {
  if (CRC_EOP == getch()) {
    Serial.print((char)STK_INSYNC);
    Serial.print((char)STK_OK);
  }
  else {
    error++;
    Serial.print((char)STK_NOSYNC);
  }
}

void breply(uint8_t b) {
  if (CRC_EOP == getch()) {
    Serial.print((char)STK_INSYNC);
    Serial.print((char)b);
    Serial.print((char)STK_OK);
  }
  else {
    error++;
    Serial.print((char)STK_NOSYNC);
  }
}

void get_version(uint8_t c) {
  switch (c) {
    case 0x80:
      breply(HWVER);
      break;
    case 0x81:
      breply(SWMAJ);
      break;
    case 0x82:
      breply(SWMIN);
      break;
    case 0x93:
      breply('S'); // serial programmer
      break;
    default:
      breply(0);
  }
}

void set_parameters() {
  // call this after reading paramter packet into buff[]
  param.devicecode = buff[0];
  param.revision   = buff[1];
  param.progtype   = buff[2];
  param.parmode    = buff[3];
  param.polling    = buff[4];
  param.selftimed  = buff[5];
  param.lockbytes  = buff[6];
  param.fusebytes  = buff[7];
  param.flashpoll  = buff[8];
  // ignore buff[9] (= buff[8])
  // following are 16 bits (big endian)
  param.eeprompoll = beget16(&buff[10]);
  param.pagesize   = beget16(&buff[12]);
  param.eepromsize = beget16(&buff[14]);

  // 32 bits flashsize (big endian)
  param.flashsize = buff[16] * 0x01000000
                    + buff[17] * 0x00010000
                    + buff[18] * 0x00000100
                    + buff[19];

}

void start_pmode() {
  spi_init();
  // following delays may not work on all targets...
  pinMode(RESET, OUTPUT);
  digitalWrite(RESET, HIGH);
  pinMode(SCK, OUTPUT);
  digitalWrite(SCK, LOW);
  delay(50);
  digitalWrite(RESET, LOW);
  delay(50);
  pinMode(MISO, INPUT);
  pinMode(MOSI, OUTPUT);
  spi_transaction(0xAC, 0x53, 0x00, 0x00);
  pmode = 1;
}

void end_pmode() {
  pinMode(MISO, INPUT);
  pinMode(MOSI, INPUT);
  pinMode(SCK, INPUT);
  pinMode(RESET, INPUT);
  pmode = 0;
}

void universal() {
  int w;
  uint8_t ch;

  fill(4);
  ch = spi_transaction(buff[0], buff[1], buff[2], buff[3]);
  breply(ch);
}

void flash(uint8_t hilo, int addr, uint8_t data) {
  spi_transaction(0x40 + 8 * hilo,
                  addr >> 8 & 0xFF,
                  addr & 0xFF,
                  data);
}
void commit(int addr) {
  if (PROG_FLICKER) prog_lamp(LOW);
  spi_transaction(0x4C, (addr >> 8) & 0xFF, addr & 0xFF, 0);
  if (PROG_FLICKER) {
    delay(PTIME);
    prog_lamp(HIGH);
  }
}

//#define _current_page(x) (here & 0xFFFFE0)
int current_page(int addr) {
  if (param.pagesize == 32)  return here & 0xFFFFFFF0;
  if (param.pagesize == 64)  return here & 0xFFFFFFE0;
  if (param.pagesize == 128) return here & 0xFFFFFFC0;
  if (param.pagesize == 256) return here & 0xFFFFFF80;
  return here;
}


void write_flash(int length) {
  fill(length);
  if (CRC_EOP == getch()) {
    Serial.print((char) STK_INSYNC);
    Serial.print((char) write_flash_pages(length));
  }
  else {
    error++;
    Serial.print((char) STK_NOSYNC);
  }
}

uint8_t write_flash_pages(int length) {
  int x = 0;
  int page = current_page(here);
  while (x < length) {
    if (page != current_page(here)) {
      commit(page);
      page = current_page(here);
    }
    flash(LOW, here, buff[x++]);
    flash(HIGH, here, buff[x++]);
    here++;
  }

  commit(page);

  return STK_OK;
}

#define EECHUNK (32)
uint8_t write_eeprom(int length) {
  // here is a word address, get the byte address
  int start = here * 2;
  int remaining = length;
  if (length > param.eepromsize) {
    error++;
    return STK_FAILED;
  }
  while (remaining > EECHUNK) {
    write_eeprom_chunk(start, EECHUNK);
    start += EECHUNK;
    remaining -= EECHUNK;
  }
  write_eeprom_chunk(start, remaining);
  return STK_OK;
}
// write (length) bytes, (start) is a byte address
uint8_t write_eeprom_chunk(int start, int length) {
  // this writes byte-by-byte,
  // page writing may be faster (4 bytes at a time)
  fill(length);
  prog_lamp(LOW);
  for (int x = 0; x < length; x++) {
    int addr = start + x;
    spi_transaction(0xC0, (addr >> 8) & 0xFF, addr & 0xFF, buff[x]);
    delay(45);
  }
  prog_lamp(HIGH);
  return STK_OK;
}

void program_page() {
  char result = (char) STK_FAILED;
  int length = 256 * getch();
  length += getch();
  char memtype = getch();
  // flash memory @here, (length) bytes
  if (memtype == 'F') {
    write_flash(length);
    return;
  }
  if (memtype == 'E') {
    result = (char)write_eeprom(length);
    if (CRC_EOP == getch()) {
      Serial.print((char) STK_INSYNC);
      Serial.print(result);
    }
    else {
      error++;
      Serial.print((char) STK_NOSYNC);
    }
    return;
  }
  Serial.print((char)STK_FAILED);
  return;
}

uint8_t flash_read(uint8_t hilo, int addr) {
  return spi_transaction(0x20 + hilo * 8,
                         (addr >> 8) & 0xFF,
                         addr & 0xFF,
                         0);
}

char flash_read_page(int length) {
  for (int x = 0; x < length; x += 2) {
    uint8_t low = flash_read(LOW, here);
    Serial.print((char) low);
    uint8_t high = flash_read(HIGH, here);
    Serial.print((char) high);
    here++;
  }
  return STK_OK;
}

char eeprom_read_page(int length) {
  // here again we have a word address
  int start = here * 2;
  for (int x = 0; x < length; x++) {
    int addr = start + x;
    uint8_t ee = spi_transaction(0xA0, (addr >> 8) & 0xFF, addr & 0xFF, 0xFF);
    Serial.print((char) ee);
  }
  return STK_OK;
}

void read_page() {
  char result = (char)STK_FAILED;
  int length = 256 * getch();
  length += getch();
  char memtype = getch();
  if (CRC_EOP != getch()) {
    error++;
    Serial.print((char) STK_NOSYNC);
    return;
  }
  Serial.print((char) STK_INSYNC);
  if (memtype == 'F') result = flash_read_page(length);
  if (memtype == 'E') result = eeprom_read_page(length);
  Serial.print(result);
  return;
}

void read_signature() {
  if (CRC_EOP != getch()) {
    error++;
    Serial.print((char) STK_NOSYNC);
    return;
  }
  Serial.print((char) STK_INSYNC);
  uint8_t high = spi_transaction(0x30, 0x00, 0x00, 0x00);
  Serial.print((char) high);
  uint8_t middle = spi_transaction(0x30, 0x00, 0x01, 0x00);
  Serial.print((char) middle);
  uint8_t low = spi_transaction(0x30, 0x00, 0x02, 0x00);
  Serial.print((char) low);
  Serial.print((char) STK_OK);
}
//////////////////////////////////////////
//////////////////////////////////////////


////////////////////////////////////
////////////////////////////////////
int avrisp() {
  uint8_t data, low, high;
  uint8_t ch = getch();
  switch (ch) {
    case '0': // signon
      error = 0;
      empty_reply();
      break;
    case '1':
      if (getch() == CRC_EOP) {
        Serial.print((char) STK_INSYNC);
        Serial.print("AVR ISP");
        Serial.print((char) STK_OK);
      }
      break;
    case 'A':
      get_version(getch());
      break;
    case 'B':
      fill(20);
      set_parameters();
      empty_reply();
      break;
    case 'E': // extended parameters - ignore for now
      fill(5);
      empty_reply();
      break;

    case 'P':
      start_pmode();
      empty_reply();
      break;
    case 'U': // set address (word)
      here = getch();
      here += 256 * getch();
      empty_reply();
      break;

    case 0x60: //STK_PROG_FLASH
      low = getch();
      high = getch();
      empty_reply();
      break;
    case 0x61: //STK_PROG_DATA
      data = getch();
      empty_reply();
      break;

    case 0x64: //STK_PROG_PAGE
      program_page();
      break;

    case 0x74: //STK_READ_PAGE 't'
      read_page();
      break;

    case 'V': //0x56
      universal();
      break;
    case 'Q': //0x51
      error = 0;
      end_pmode();
      empty_reply();
      break;

    case 0x75: //STK_READ_SIGN 'u'
      read_signature();
      break;

      // expecting a command, not CRC_EOP
      // this is how we can get back in sync
    case CRC_EOP:
      error++;
      Serial.print((char) STK_NOSYNC);
      break;

      // anything else we will return STK_UNKNOWN
    default:
      error++;
      if (CRC_EOP == getch())
        Serial.print((char)STK_UNKNOWN);
      else
        Serial.print((char)STK_NOSYNC);
  }
}

```

## 1. **程序功能概述**

#### **功能**：
将Arduino变成一个ISP（In-System Programmer），用于编程和操作AVR微控制器。
#### **硬件要求**：

- Arduino Leonardo、Micro、Due或其他支持SPI通信的Arduino开发板。

- 一个目标AVR微控制器，通过SPI接口连接到Arduino。

- 三个LED（带电阻）分别连接到数字引脚9（心跳）、8（错误）、7（编程模式）。
#### **输出**：
通过串口与主机通信，执行编程和读取操作。
#### **警告**：
当使用`Mouse.move()`命令时，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

## 2. **代码结构**

#### **全局变量**

```cpp
#define RESET     SS
#define LED_HB    9
#define LED_ERR   8
#define LED_PMODE 7
#define PROG_FLICKER true

#define HWVER 2
#define SWMAJ 1
#define SWMIN 18

// STK Definitions
#define STK_OK      0x10
#define STK_FAILED  0x11
#define STK_UNKNOWN 0x12
#define STK_INSYNC  0x14
#define STK_NOSYNC  0x15
#define CRC_EOP     0x20 //ok it is a space...
```

- 定义了重置引脚、LED引脚、硬件版本号、软件版本号等。

- 定义了STK协议的状态码和特殊字符。

#### **`setup()` 函数**

```cpp
void setup() {
  Serial.begin(19200);
  pinMode(LED_PMODE, OUTPUT);
  pulse(LED_PMODE, 2);
  pinMode(LED_ERR, OUTPUT);
  pulse(LED_ERR, 2);
  pinMode(LED_HB, OUTPUT);
  pulse(LED_HB, 2);
}
```

- 初始化串口通信，波特率设置为19200。

- 设置LED引脚为输出模式，并闪烁两次以确认程序启动。

#### **`loop()` 函数**

```cpp
void loop(void) {
  // is pmode active?
  if (pmode) digitalWrite(LED_PMODE, HIGH);
  else digitalWrite(LED_PMODE, LOW);
  // is there an error?
  if (error) digitalWrite(LED_ERR, HIGH);
  else digitalWrite(LED_ERR, LOW);

  // light the heartbeat LED
  heartbeat();
  if (Serial.available()) {
    avrisp();
  }
}
```

- 根据编程模式和错误状态点亮或熄灭相应的LED。

- 调用`heartbeat()`函数闪烁心跳LED。

- 如果串口有数据可用，调用`avrisp()`函数处理串口命令。

#### **`avrisp()` 函数**

```cpp
int avrisp() {
  uint8_t ch = getch();
  switch (ch) {
    case '0': // signon
      error = 0;
      empty_reply();
      break;
    case '1':
      if (getch() == CRC_EOP) {
        Serial.print((char) STK_INSYNC);
        Serial.print("AVR ISP");
        Serial.print((char) STK_OK);
      }
      break;
    case 'A':
      get_version(getch());
      break;
    case 'B':
      fill(20);
      set_parameters();
      empty_reply();
      break;
    case 'E': // extended parameters - ignore for now
      fill(5);
      empty_reply();
      break;

    case 'P':
      start_pmode();
      empty_reply();
      break;
    case 'U': // set address (word)
      here = getch();
      here += 256 * getch();
      empty_reply();
      break;

    case 0x60: //STK_PROG_FLASH
      low = getch();
      high = getch();
      empty_reply();
      break;
    case 0x61: //STK_PROG_DATA
      data = getch();
      empty_reply();
      break;

    case 0x64: //STK_PROG_PAGE
      program_page();
      break;

    case 0x74: //STK_READ_PAGE 't'
      read_page();
      break;

    case 'V': //0x56
      universal();
      break;
    case 'Q': //0x51
      error = 0;
      end_pmode();
      empty_reply();
      break;

    case 0x75: //STK_READ_SIGN 'u'
      read_signature();
      break;

    case CRC_EOP:
      error++;
      Serial.print((char) STK_NOSYNC);
      break;

    default:
      error++;
      if (CRC_EOP == getch())
        Serial.print((char)STK_UNKNOWN);
      else
        Serial.print((char)STK_NOSYNC);
  }
}
```

#### **处理串口命令**：
`avrisp()`函数通过读取串口命令并根据命令类型执行不同的操作。
#### 支持的命令包括：

- `0`：签名（signon）。

- `1`：确认连接。

- `A`：获取版本信息。

- `B`：设置参数。

- `E`：扩展参数（目前忽略）。

- `P`：进入编程模式。

- `U`：设置地址。

- `0x60`：编程闪存。

- `0x61`：编程数据。

- `0x64`：编程页面。

- `0x74`：读取页面。

- `V`：通用命令。

- `Q`：退出编程模式。

- `0x75`：读取签名。

- `CRC_EOP`：同步失败。

- 默认：未知命令。

#### **其他辅助函数**

- **`getch()`**：从串口读取一个字节。

- **`fill()`**：从串口读取多个字节并存储到缓冲区。

- **`pulse()`**：闪烁LED。

- **`prog_lamp()`**：控制编程模式LED。

- **`spi_init()`**：初始化SPI通信。

- **`spi_wait()`**：等待SPI通信完成。

- **`spi_send()`**：发送一个字节通过SPI。

- **`spi_transaction()`**：执行一个SPI事务。

- **`empty_reply()`**：发送一个空的回复。

- **`breply()`**：发送一个带参数的回复。

- **`get_version()`**：处理版本信息请求。

- **`set_parameters()`**：设置编程参数。

- **`start_pmode()`**：进入编程模式。

- **`end_pmode()`**：退出编程模式。

- **`universal()`**：处理通用命令。

- **`flash()`**：写入闪存。

- **`commit()`**：提交编程。

- **`current_page()`**：计算当前页面地址。

- **`write_flash()`**：写入闪存页面。

- **`write_eeprom()`**：写入EEPROM。

- **`write_eeprom_chunk()`**：写入EEPROM块。

- **`program_page()`**：编程页面。

- **`flash_read()`**：读取闪存。

- **`flash_read_page()`**：读取闪存页面。

- **`eeprom_read_page()`**：读取EEPROM页面。

- **`read_page()`**：读取页面。

- **`read_signature()`**：读取签名。

## 3. **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将目标AVR微控制器通过SPI接口连接到Arduino。

3. 上传代码到Arduino开发板。

4. 使用支持AVR ISP的工具（如avrdude）与Arduino通信，执行编程和读取操作。

## 4. **注意事项**

- **硬件限制**：此代码适用于支持SPI通信的Arduino开发板。

- **安全警告**：确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

- **编程模式**：进入编程模式后，Arduino会接管目标AVR微控制器的编程操作。

- **错误处理**：程序通过LED指示错误状态，确保在出现错误时及时处理。

- **版本信息**：程序支持获取硬件和软件版本信息。



## 视频讲解
**BiliBili：** [视睿网络-哔哩哔哩视频 (bilibili.com)](https://space.bilibili.com/1985904092/lists/1497284)

<iframe
  width=auto
  height=auto
  src="//player.bilibili.com/player.html?isOutside=true&aid=230442258&bvid=BV19h411w7rf&cid=1183170164&p=1" 
  scrolling="no" 
  border="0" 
  frameborder="no" 
  framespacing="0" 
  allowfullscreen="true"></iframe>

