---
type: simulink-block
title: 'BLE Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'blereceive'
documentation_source_path: 'supportpkg/android_ref/blereceive.html'
language: zh-CN
chinese_source: worker-translation
---

# BLE Receive

## 端口

### 输出

### **Data** — 接收的数据，N×1 数组

该模块将数据输出为 N×1 数组。

**注**

BLE Receive 模块输出的数据未经处理。有关数据数组内容的信息，请参阅 GATT 特征。

**数据类型：** `int8`

### **Size** — 接收数据的大小 2（默认） | nonnegative integer

此端口以 bytes 为单位显示从 BLE 连接接收的数据大小。

**数据类型：** `uint8`

## 参数

### **Mode** — 设置设备的 BLE `Peripheral (server)`（默认） | `Central (client)`

将设备的 BLE 硬件设置为外设模式或中央模式。在 `Peripheral (server)` 模式下，必须指定设备的 `Service` 和 `Characteristic`。然后，具有相同服务和特征的其他设备会接收从您的 Android® 移动设备发送的数据。

当您将设备的 `Mode` 设置为 `Central (Client)` 时，必须先扫描并检测附近的 BLE 设备，然后才能选择外设设备和特征。

### **Scan** — 发现设备和特征按钮（默认）

发现附近的 Bluetooth Low Energy (BLE) 设备和传感器的设备与特征，并将它们连接到您的 Android 移动设备。

1. 将您的 Android 设备连接到开发计算机。如果您之前未连接并配置 Android 设备，请参阅硬件设置。
2. 配置模型以使用您连接的 Android 设备。有关更多信息，请参阅在 Android 设备上运行模型。
3. 将 BLE Receive 模块的 **Mode** 设置为 `Central (Client)`。
4. 要打开 BLE Setup 向导，请点击 **Scan** 按钮。
5. BLE Setup 向导允许您将 BLE Scanner Android 应用上传到您的 Android 设备。然后，BLE Scanner Android 应用会扫描附近的 BLE 设备。
6. 按照 BLE Scanner Android 应用中提供的说明扫描 BLE 设备。作为扫描过程的一部分，BLE Scanner Android 应用会临时连接到设备，以收集其可用服务和特征。
7. 退出 BLE Scanner Android 应用后，确认您可以在 BLE Setup 向导中看到 BLE 设备。关闭向导。
8. 重新打开 BLE Receive 模块封装，并从可用的外设设备和特征中进行选择。

### **Service** — BLE 服务名称 `Heart Rate service`（默认） | ...

选择 BLE 设备在 `Peripheral (Server)` 模式下运行时广播的服务。设备可广播的可用服务列于下表中。启用 **Specify by UUID** 时，可以将自定义服务 UUID 值指定为字符数组。

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

### **Characteristic** — 来自所选服务的 BLE 特征 `Heart Rate Measurement`（默认） | ...

选择在 `Peripheral (Server)` 模式下运行时，给定 BLE 服务的特征。有关可通过 BLE Send 模块访问的可用特征及其父服务（取决于连接的 BLE 设备和可用服务），请参阅 **Service**。

启用 **Specify by UUID** 时，可以将自定义特征 UUID 指定为字符数组。

### **Specify using UUID** — 使用 UUID 指定服务和特征 off（默认） | on

启用后，使用通用唯一标识符（UUID）值指定 BLE 服务和特征。

### **Peripheral Device** — 通过 BLE 可用的设备 no devices（默认）

选择通过 BLE 扫描和检测向导找到的可用外设设备或传感器。如果您看不到列出的任何设备，请点击 **Scan** 以检测您移动设备范围内的新 BLE 设备。

### **Characteristic** — 来自外设设备的可用 BLE 特征 no characteristic（默认）

从所选 **Peripheral Device** 中选择可用特征。有关可通过 BLE Send 模块访问的可用特征及其父服务（取决于连接的 BLE 设备和可用服务），请参阅 **Service**。

### **Data size (N)** — 要接收的数据大小 `2`（默认） | scalar

输入要从远程设备接收的数据大小。

### **Sample time** — 接收数据的频率 `0.1`（默认） | scalar

输入接收数据的时间频率。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017b 中引入**

## 描述

使用 Bluetooth Low Energy (BLE) 协议接收数据

BLE Receive 模块允许您的 Android 移动设备使用 Bluetooth® Low Energy (BLE) 协议从附近的设备或传感器接收数据或指令。

### 中央模式

配置为中央模式的 BLE 设备会扫描并检测附近的 BLE 设备，并确定其可用服务。扫描后，运行在中央模式的 BLE 设备可以连接到任何已发现的 BLE 设备。

当您将设备的 **Mode** 设置为 `Central (Client)` 时，必须扫描并检测附近的 BLE 设备。要启动 BLE Setup 向导，请点击 **Scan**。向导完成后，选择在扫描和检测期间找到的 **Peripheral Device** 和 **Characteristic**。

### 外设模式

配置为外设模式的 BLE 设备会向其他设备通告其存在，广播有关所支持服务和设备标识的最少信息。这允许配置为中央模式的 BLE 设备扫描并检测附近的 BLE 设备，并确定其可用服务。

当您将设备的 **Mode** 设置为 `Peripheral (Server)` 时，必须指定设备的 **Service** 和 **Characteristic**。具有相同服务和特征的其他设备随后会接收从您的 Android 移动设备发送的数据。

### 服务和特征

BLE 数据交换基于 Generic Attributes (GATT) 配置文件，它定义了分层数据结构。GATT 由服务（例如 Heart Rate service）组成，该服务可以包含若干特征（例如 Heart Rate Measurement 或 Body Sensor Location）。通用唯一标识符 (UUID) 同时定义服务和特征，使不同的 BLE 设备能够识别所连接设备的服务和特征。

当 BLE 设备运行在外设模式时，设备提供的可用服务会通告给任何正在监听的、运行在中央模式的 BLE 设备。只有当 BLE 中央设备建立与 BLE 外设设备的连接后，服务中的特征才可用。许多服务和关联特征已经作为标准提供，包括 Heart Rate service。

您可以选择使用自己的服务 UUID 和特征 UUID 来指定自己的或自定义的服务和特征。要启用自定义 UUID 指定，请选择 **Specify using UUID** 参数。
