# 智能家居控制板与嵌入式程序汇总表（2025年版）

| 品牌 / 平台 | 典型控制板型号 | 嵌入式平台/主控 | 开源/闭源代码 | 核心功能示例 | 通信协议 | 生态特色 |
|-------------|-----------------|------------------|----------------|--------------|-----------|-----------|
| **小米 / 米家** | 多功能网关板 V3 | ESP32-S2 | 闭源（可配 Home Assistant 插件） | 红外转发、Zigbee3.0 路由、本地场景 | Wi-Fi + Zigbee3.0 + BLE | 小米 IoT 云、米家 APP、小爱同学 |
| **华为 / 鸿蒙智家** | Hi-3861 开发板 | Hi3861（RISC-V，160 MHz） | OpenHarmony 开源 | 全屋调光、分布式联动、碰一碰配网 | Wi-Fi 2.4 GHz | 鸿蒙分布式软总线、HarmonyOS Connect |
| **绿米 Aqara** | M2 网关板 | EFR32MG21（ARM Cortex-M33） | 闭源 | 支持 Matter over Thread、场景联动 | Zigbee3.0 + Thread + BLE | 本地化场景、Apple HomeKit 认证 |
| **欧瑞博** | MixPad S 中控屏 | RK3566（ARM Cortex-A55）+ STM32 | Linux+FreeRTOS 双系统 | 10 cm 近场语音、无感触屏、地暖控制 | Wi-Fi + Zigbee3.0 + BLE | HomeAI OS、地产前装方案 |
| **海尔智家** | 云芯 Smart Hub | 海思 Hi3861V100 | 闭源 | 多联机空调、安防、水系统联动 | Wi-Fi + BLE | 海尔智家云、U+ 协议 |
| **萤石** | CS-HP 网关板 | RTL8197FS | 闭源 | 摄像头联动、老人跌倒检测、门铃 | Wi-Fi + BLE | 萤石云、视频 AI |
| **飞利浦 Hue** | Hue Bridge v3 | Marvell 88MC200 | 闭源（官方开放 REST API） | 1600 万色调光、音乐律动、掌静脉识别 | Zigbee3.0 + Ethernet | Hue App、Matter 升级 |
| **涂鸦智能** | Tuya Zigbee SoC | EFR32MG13 | 基于 TuyaOS 开源框架 | 快速量产、跨品牌互联 | Zigbee3.0 + Wi-Fi | Tuya Cloud、免开发面板 |
| **ST 意法半导体** | Nucleo-F103RB 快速原型板 | STM32F103RBT6 | 开源（STM32CubeMX + FreeRTOS） | 温湿度-光感-风扇-LED 本地联动 | Wi-Fi 扩展（ESP8266 UART） | 社区/教育市场 |
| **乐鑫 Espressif** | ESP32-C6 开发板 | ESP32-C6（RISC-V） | 开源（ESP-IDF、Matter SDK） | Thread/Matter 边界路由、BLE Mesh | Wi-Fi 6 + BLE 5 + Thread | 官方 OTA、RainMaker 云 |
| **Nordic** | nRF5340 DK | nRF5340（M33+FPU） | 开源（Zephyr + nRF Connect SDK） | BLE Mesh 灯控、Thread 路由器 | BLE + Thread + NFC | Nordic Thingy 生态 |
| **Silicon Labs** | EFR32MG24-BRD2703A | EFR32MG24 | 开源（Zephyr + Matter SDK） | 低功耗 Matter 节点、本地场景 | Zigbee + Thread + BLE | Simplicity Studio |
| **清华大学课程板** | QHNU 智能家居板 | S3C2440 (ARM9) + Linux | 教学开源 | 温湿度、光感、烟雾、声感检测网页展示 | Ethernet + Wi-Fi Dongle | 教学/实验 |

## 使用建议
1. **DIY/学习**：选 STM32、ESP32-C6、nRF5340 DK，资料全、代码开源。  
2. **全屋装修**：欧瑞博 MixPad、绿米 M2 网关，支持地产前装与 Matter 协议。  
3. **快速量产**：涂鸦 Zigbee SoC + TuyaOS，免开发 15 天出样。  
4. **云生态优先**：华为鸿蒙、小米米家、海尔智家，云端联动最成熟。

###智能家居控制板与手机 APP 的连接流程
可以概括为“三步走”：  
1. 建立网络通道（局域网或云）；  
2. 完成设备发现与身份绑定；  
3. 通过双向协议实时收发指令/状态。  
下面把常用 5 种技术路径整理成一览表，并给出示例代码片段，方便直接落地。

| 连接方式 | 典型硬件/模组 | 手机端流程（用户视角） | 控制板端关键代码/AT 指令 | 优缺点 | 适用场景 |
| --- | --- | --- | --- | --- | --- |
| 品牌官方 APP | 小米 V3 网关、ESP32-S2 模组 | ①商店下载“米家”→②注册→③按提示配网→④控制 | 模组上电后主动连接预设的 `miio` 云域名，无需用户代码 | 零开发、功能全；必须原厂生态 | 大众消费级产品 |
| 通用 MQTT 云 | 任意 ESP8266/ESP32 | ①APP 扫描 QR 绑定设备→②APP 通过阿里云/腾讯云 MQTT 发布 `{"power":1}`→③设备订阅主题并执行 | 设备端： <br>`client.publish("device/12345/report",json)` <br>`client.subscribe("device/12345/control")` | 跨平台、云联动；需服务器 | 快速量产、海外部署 |
| 本地局域网 HTTP | STM32 + ESP8266（AT 固件） | ①手机连同一 Wi-Fi→②APP 扫描 UDP 广播发现设备→③HTTP GET `http://192.168.1.88/relay?on=1` | `AT+CIPSERVER=1,80` <br>`AT+CIPSEND=...` 回传 JSON | 无需云、响应快；仅限局域网 | 别墅/机房/隐私场景 |
| BLE Mesh | nRF5340 DK | ①打开“HomeKit”/“nRF Mesh”→②靠近设备→③配对→④控制 | Zephyr： <br>`bt_mesh_init(&prov, &comp)` <br>`bt_mesh_model_msg_handler` | 低功耗、断网可用；需 BLE 4.2+ 手机 | 灯具/电池传感器 |
| 红外/射频转发 | 米家空调伴侣 P2（ESP8266+红外） | ①APP 选空调品牌→②APP 下发红外码→③伴侣发射 38 kHz 红外 | 伴侣内部： <br>`ir_send(NEC,0x20DF10EF)` | 老家电秒变智能；单向无状态 | 空调、电视存量市场 |

## 快速上手示例（以“ESP8266 + MQTT + uni-app”为例，阿里云物联网平台）  
### 1. 设备端（Arduino 框架）  
```cpp
#include <PubSubClient.h>
WiFiClient espClient;
PubSubClient client(espClient);
void callback(char* topic, byte* payload, unsigned int len){
  String msg = "";
  for(int i=0;i<len;i++) msg += (char)payload[i];
  if(msg == "1") digitalWrite(RELAY_PIN, LOW);   //开灯
  else            digitalWrite(RELAY_PIN, HIGH);  //关灯
}
void setup(){
  WiFi.begin("SSID","PWD");
  client.setServer("a1xxxxxx.iot-as-mqtt.cn-shanghai.aliyuncs.com",1883);
  client.setCallback(callback);
  while(!client.connected()){
    client.connect("ESP8266|securemode=2,signmethod=hmacsha1,timestamp=...","用户名","密码");
  }
  client.subscribe("/sys/a1xxxxxx/设备名/thing/service/property/set");
}
void loop(){ client.loop(); }
```
### 2. 手机端（uni-app 片段）  
```js
mqtt = require('mqtt.min.js')
client = mqtt.connect('wxs://a1xxxxxx.iot-as-mqtt.cn-shanghai.aliyuncs.com')
client.on('connect', ()=>{ client.publish('/设备名/thing/service/property/set','{"power":1}') })
```

### 常见坑 & 对策  
- 路由器 5 GHz/2.4 GHz 同名导致配网失败 → 强制热点分开。  
- iOS 14+ 本地网络权限 → 在 `info.plist` 加 `NSLocalNetworkUsageDescription`。  
- 云价格敏感 → 使用开源的 EMQX 或 mosquitto 自建 MQTT。

