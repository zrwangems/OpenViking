---
type: simulink-block
title: 'BLE Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / BLE'
documentation_page: 'blereceive'
documentation_source_path: 'supportpkg/arduino_ref/blereceive.html'
language: zh-CN
chinese_source: worker-translation
---

# BLE Receive

## 端口

### 输出

### **data** — BLE 设备接收的数据 N-by-1 数组

该模块将其从 BLE 设备接收的数据输出为 *N*-by-1 数组。

**注意**

BLE Receive 模块在输出从 BLE 设备接收的数据之前不会处理这些数据。有关数据数组内容的详细信息，请参阅 GATT Characteristics。

**数据类型：** `int8`

### **size** — BLE 设备接收的数据大小 2（默认）| 非负整数

该模块以字节为单位输出其从 BLE 设备接收的数据大小。

**数据类型：** `uint8`

## 参数

### **Mode** — BLE 模式 `Peripheral (Server)`（默认）| `Central (Client)`

将 BLE 设备的硬件设置为以下模式之一。

- `Peripheral (Server)` — 选择此模式时，指定 Bluetooth 设备的服务和特征。然后其他 Bluetooth 设备接收从您的 Arduino 板发送的、具有相同服务和特征的数据。
- `Central (Client)` — 选择此模式时，在 Peripheral device 参数中选择外围设备之前，先扫描并检测附近的 BLE 设备，并在 Characteristic 参数中选择其特征。

### **Specify using UUID** — 使用 UUID 指定服务和特征 `off`（默认）| `on`

启用此参数以使用通用唯一标识符 (UUID) 值指定 BLE 服务和特征。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Peripheral (Server)`。

### **Service** — BLE 服务名称 `Heart Rate`（默认）| `...`

选择 BLE 设备在 `Peripheral (Server)` 模式下运行时广播的服务。可用服务列于下表中。启用 Specify using UUID 后，您可以将特征的特定 UUID 值写为字符数组。

| Service | Characteristic |
| --- | --- |
| Generic Access | Device Name |
| Appearance |
| Peripheral Privacy Flag |
| Reconnection Address |
| Peripheral Preferred Connection Parameters |
| Generic Attribute | Service Changed |
| Glucose service | Glucose Measurement |
| Glucose Measurement Context |
| Glucose Feature |
| Record Access Control Point |
| Health Thermometer service | Temperature Measurement |
| Temperature Type |
| Intermediate Temperature |
| Measurement Interval |
| Heart Rate service | Heart Rate Measurement |
| Body Sensor Location |
| Heart Rate Control Point |
| Blood pressure service | Blood Pressure Measurement |
| Intermediate Cuff Pressure |
| Blood Pressure Feature |
| Running Speed and Cadence | RSC Measurement |
| RSC Feature |
| SC Control Point |
| Sensor Location |
| Cycling Power service | Sensor Location |
| Cycling Power Measurement |
| Cycling Power Vector |
| Cycling Power Feature |
| Cycling Power Control Point |
| Location and Navigation | Location and Navigation Characteristic |
| Navigation |
| Position Quality |
| LN Feature |
| LN Control Point |
| Environmental Sensing | Magnetic Declination |
| Elevation |
| Pressure |
| Temperature |
| Humidity |
| True Wind Speed |
| True Wind Direction |
| Apparent Wind Speed |
| Apparent Wind Direction |
| Gust Factor |
| Pollen Concentration |
| UV Index |
| Irradiance |
| Rainfall |
| Wind Chill |
| Heat Index |
| Dew Point |
| Magnetic Flux Density - 2-D |
| Magnetic Flux Density - 3-D |
| Barometric pressure Trend |
| Body Composition service | Body Composition Feature |
| Body Composition Measurement |
| Weight Scale | Weight Scale Measurement |
| Weight Scale Feature |
| Continuous Glucose Monitoring Service | CGM Measurement |
| CGM Feature |
| CGM Status |
| CDM Session start Time |
| Indoor Positioning | Indoor Positioning Configuration |
| Latitude |
| Longitude |
| Local North Coordinate |
| Local East Coordinate |
| Altitude |
| Uncertainty |
| Location Name |
| Pulse Oximeter Service | Record Access Control Point |
| PLX Spot-Check Measurement |
| PLX Continuous Measurement |
| PLX Features |
| Fitness Machine Service | Treadmill Data |
| Cross Trainer Data |
| Step Climber |
| Stair Climber |
| Rower Data |
| Indoor Bike Data |
| Supported Speed Range |
| Supported Inclination Range |
| Supported Resistance Level Range |
| Supported Heart Range |
| Supported Power Range |

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Peripheral (Server)`。

### **Characteristic** — 外围设备的 BLE 特征 `Heart Rate Measurement`（默认）| `...`

选择外围设备的 BLE 特征。可用特征取决于您在 **Service** 参数中选择的服务。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Peripheral (Server)`。

### **Scan** — 打开 BLE Setup 向导以扫描附近启用 Bluetooth 的设备的按钮

点击此按钮以打开 BLE Setup 向导。使用该向导发现附近启用 Bluetooth 的设备及其特征。您可以使用主机计算机或 Arduino 板扫描设备。要打开并配置 BLE Setup 向导：

1. 将 Mode 设置为 `Central (Client)`。BLE Setup 向导允许您扫描附近的 Bluetooth 设备。
2. 按照屏幕上的说明导入设备名称及其特征，以分别显示在模块参数对话框中的 Peripheral device 和 Characteristic 参数下。
3. 关闭 BLE Setup 向导。重新打开 BLE Receive 模块对话框，并从可用的外围设备和特征中进行选择。

#### 依赖关系

要启用此按钮，请将 **Mode** 设置为 `Central (Client)`。

### **Peripheral device** — 可通过 BLE Setup 向导使用的设备 `No Devices`（默认）

从可用的外围设备或传感器中进行选择。如果看不到任何设备，请点击 Scan 以检测主机计算机或 Arduino 板范围内的新 BLE 设备。

**注意**

外围设备名称不得包含数值大于 255 的字符。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Central (Client)`。

### **Characteristic** — 外围设备可用的 BLE 特征 `No Characteristic`（默认）

从可用的特征中为外围设备选择一个特征。有关每个 BLE 服务下可用的特征的完整列表，请参阅 Service 参数。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Central (Client)`。

### **Data size (N)** — 模块接收的数据大小 `2`（默认）| 标量

输入模块可从 BLE 设备接收的数据大小。

### **Sample time** — 模块接收数据的时间间隔 `0.1`（默认）| 标量

输入 BLE Receive 模块从 BLE 设备接收数据的时间间隔（以秒为单位）。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

使用 Bluetooth Low Energy (BLE) 协议接收数据

使用 BLE Receive 模块使您的 Arduino® 板能够使用 Bluetooth® Low Energy (BLE) 协议从附近的设备或传感器接收数据或指令。

### 支持的 Arduino 板

- Arduino Nano 33 IoT
- Arduino Nano 33 BLE Sense
- Arduino MKR Wi-Fi® 1010
- Arduino compatible ESP32 – WROOM
- Arduino compatible ESP32 – WROVER

### Central 模式

配置为 `Central (Client)` 模式的 BLE 设备可以扫描并检测附近的 BLE 设备，并确定其可用的服务。当您将 **Mode** 参数设置为 `Central (Client)` 时，使用模块上的 **Scan** 按钮设置 BLE Setup 向导。BLE Setup 向导会扫描附近的 BLE 设备，并确定这些设备上可用的服务和特征。一旦向导检测到附近的 BLE 设备，请使用 **Peripheral Device** 和 **Characteristic** 参数选择外围设备及其特征。

### Peripheral 模式

配置为 `Peripheral (Server)` 模式的 BLE 设备会向其他设备通告其存在，广播有关其支持的服务和设备身份的少量信息。这允许配置为 central 模式的 BLE 设备扫描并检测附近的 BLE 设备，并确定其可用的服务。当您将设备的 **Mode** 设置为 `Peripheral (Server)` 时，必须指定设备的 **Service** 和 **Characteristic**。具有相同服务和特征的其他设备随后接收从您的 Arduino 板发送的数据。

### Service 和 Characteristic

BLE 数据交换基于 Generic Attributes (GATT) 配置文件，该配置文件定义了分层数据结构。GATT 由一个服务（例如 Heart Rate service）组成，该服务可以包含多个特征（例如 Heart Rate Measurement 或 Body Sensor Location）。通用唯一标识符 (UUID) 同时定义服务和特征，允许不同的 BLE 设备识别所连接设备的服务和特征。

当 BLE 设备在 peripheral 模式下运行时，该设备提供的可用服务会通告给任何正在侦听的、在 central 模式下运行的 BLE 设备。只有当 BLE central 设备与 BLE peripheral 设备建立连接后，服务内的特征才可用。许多服务和关联特征已作为标准提供，包括 Heart Rate service。

您可以选择使用自己的服务 UUID 和特征 UUID 来指定自己的或自定义的服务和特征。要启用自定义 UUID 指定，请选中 **Specify using UUID** 参数。
