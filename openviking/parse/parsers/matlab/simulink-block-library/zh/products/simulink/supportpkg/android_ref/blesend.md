---
type: simulink-block
title: 'BLE Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'blesend'
documentation_source_path: 'supportpkg/android_ref/blesend.html'
language: zh-CN
chinese_source: worker-translation
---

# BLE Send

## 端口

### 输入

### **Port1** — 输入数据 N×1 数组

该模块接受 N×1 数组形式的数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Mode** — 设置设备的 BLE 模式 `Peripheral (Server)`（默认）| `Central (Client)`

将设备的 BLE 硬件设置为外设模式或中央模式。在 `Peripheral (Server)` 模式下，您必须指定设备的 **Service** 和 **Characteristic**。然后，其他具有相同服务和特征的设备会接收从您的 Android 移动设备发送的数据。

当您将设备的 `Mode` 设置为 Central (Client) 时，必须先扫描并检测附近的 BLE 设备，然后才能选择外设设备和特征。

### **Service** — BLE 服务名称 `Heart Rate Service`（默认）| ...

选择 BLE 设备在 `Peripheral (Server)` 模式下广播的服务。设备可广播的可用服务列在下表中。当 **Specify by UUID** 启用时，您可以将特征的特定 UUID 值写为字符数组。

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

### **Characteristic** — 来自所选服务的 BLE 特征 `Heart Rate Measurement`（默认）| ...

选择在 peripheral (server) 模式下给定 BLE 服务的特征。有关 BLE Send 模块提供的可用特征及其父服务，请参阅 **Service**。当 `Specify by UUID` 启用时，您可以将特征的特定 UUID 值写为字符数组。

### **Specify using UUID** — 使用 UUID 指定服务和特征 off（默认）| on

启用后，使用通用唯一标识符 (UUID) 值指定 BLE 服务和特征。

### **Peripheral Device** — 可通过 BLE 使用的设备 no devices（默认）

选择使用 BLE 扫描应用找到的可用外设设备或传感器。如果看不到列出的任何设备，请点击 **Scan**，以检测移动设备范围内新的 BLE 设备。

### **Scan** — 发现设备和特征按钮（默认）

发现附近 Bluetooth Low Energy (BLE) 设备和传感器的设备与特征，并将它们连接到您的 Android 移动设备。

1. 将您的 Android 设备连接到开发计算机。如果您之前尚未连接并配置 Android 设备，请参阅 Hardware Setup。
2. 配置模型以使用已连接的 Android。有关详细信息，请参阅 Run Model on Android Devices。
3. 将 BLE Receive 模块的 **Mode** 设置为 `Central (Client)`。
4. 要打开 BLE Setup 向导，请点击 **Scan** 按钮。
5. BLE Setup 向导允许您将 BLE Scanner Android 应用上传到您的 Android 设备。然后，BLE Scanner Android 应用会扫描附近的 BLE 设备。
6. 按照 BLE Scanner Android 应用中提供的说明扫描 BLE 设备。作为扫描过程的一部分，BLE Scanner Android 应用会临时连接到设备，以收集其可用的服务和特征。
7. 退出 BLE Scanner Android 应用后，确认您可以在 BLE Setup 向导中看到 BLE 设备。关闭该向导。
8. 重新打开 BLE Send 模块封装，并从可用的外设设备和特征中进行选择。

### **Characteristic** — 来自外设的 BLE 特征 no characteristic（默认）

选择所选 **Peripheral Device** 可用的特征。有关 BLE Send 模块提供的可用特征及其父服务，请参阅 **Service**。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

使用 Bluetooth Low Energy (BLE) 协议发送数据

BLE Send 模块使用 Bluetooth® Low Energy (BLE) 协议将数据或指令从您的 Android® 移动设备传输到附近的设备或传感器。

### 中央模式

配置为中央模式的 BLE 设备会扫描并检测附近的 BLE 设备，并确定其可用服务。扫描后，运行在中央模式的 BLE 设备可以连接到任何已发现的 BLE 设备。

当您将设备的 **Mode** 设置为 `Central (Client)` 时，必须扫描并检测附近的 BLE 设备。要启动 BLE Setup 向导，请点击 **Scan**。向导完成后，选择在扫描和检测期间找到的 **Peripheral Device** 和 **Characteristic**。

### 外设模式

配置为外设模式的 BLE 设备会向其他设备通告其存在，广播有关所支持服务和设备身份的最少信息。这允许配置为中央模式的 BLE 设备扫描并检测附近的 BLE 设备，并确定其可用服务。

当您将设备的 **Mode** 设置为 `Peripheral (Server)` 时，必须指定设备的 **Service** 和 **Characteristic**。然后，具有相同服务和特征的其他设备会接收从您的 Android 移动设备发送的数据。

### 服务和特征

BLE 数据交换基于 Generic Attributes (GATT) 配置文件，该配置文件定义了一种分层数据结构。GATT 由服务（例如 Heart Rate service）组成，服务可包含多个特征（例如 Heart Rate Measurement 或 Body Sensor Location）。通用唯一标识符 (UUID) 定义了服务和特征，使不同的 BLE 设备能够识别已连接设备的服务和特征。

当 BLE 设备运行在外设模式时，该设备提供的可用服务会通告给任何正在监听且运行在中央模式的 BLE 设备。只有当 BLE 中央设备与 BLE 外设设备建立连接后，服务内的特征才可用。许多服务及相关特征已作为标准提供，包括 Heart Rate service。

您可以选择使用自己的服务 UUID 和特征 UUID 来指定自己的或自定义的服务和特征。要启用自定义 UUID 指定，请选择 **Specify using UUID** 参数。
