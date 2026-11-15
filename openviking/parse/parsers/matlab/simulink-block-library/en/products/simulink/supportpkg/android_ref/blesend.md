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
language: en
---

# BLE Send

## Ports

### Input

### **Port1** — Input data N-by-1 array

The block accepts data as an N-by-1 array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Mode** — Set the BLE mode of your device `Peripheral (Server)` (default) | `Central (Client)`

Set the BLE hardware of your device to either peripheral or central mode. In the
`Peripheral (Server)` mode, you must specify the
**Service** and **Characteristic** of your device.
Other devices then receive the data sent from your Android mobile device with the same
service and characteristic.

When you set the `Mode` of the devices to Central (Client), you
must scan and detect nearby BLE devices before selecting the peripheral device and
characteristic.

### **Service** — BLE service name `Heart Rate Service` (default) | ...

Select the service broadcast by the BLE device when operating in the
`Peripheral (Server)` mode. Available services that can be broadcast
from the device are listed in the following table. When **Specify by
UUID** is enabled, you can write a specific UUID value for the characteristic
as a character array.

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

### **Characteristic** — BLE characteristic from selected service `Heart Rate Measurement` (default) | ...

Select the characteristic for a given BLE service when operating in the peripheral
(server) mode. See **Service** for the available characteristics, and
their parent services, provided by the BLE Send block. When
`Specify by UUID` is enabled, you can write a specific UUID value
for the characteristic as a character array.

### **Specify using UUID** — Specify service and characteristic using UUID off (default) | on

When enabled, specify the BLE service and characteristic using Universally Unique ID
(UUID) values.

### **Peripheral Device** — Devices available through BLE no devices (default)

Select an available peripheral device or sensor found using the BLE scan app. If you
cannot see any devices listed, click **Scan** to detect new BLE
devices within range of your mobile device.

### **Scan** — Discover devices and characteristics button (default)

Discover devices and characteristics of nearby Bluetooth Low Energy (BLE) devices and sensors and connect them to your Android mobile device.

1. Connect your Android device to your development computer. If you have not previously
   connected and configured your Android device, see Hardware Setup.
2. Configure the model to use your connected Android. For more information, see Run Model on Android Devices.
3. Set the **Mode** of the BLE Receive block to
   `Central (Client)`.
4. To open the BLE Setup wizard, click the **Scan**
   button.
5. The BLE Setup wizard allows you to upload the BLE Scanner Android app onto your
   Android device. The BLE Scanner Android app then scans for nearby BLE
   devices.
6. Follow the instructions provided in the BLE Scanner Android app to scan for BLE
   devices. The BLE Scanner Android app temporarily connects to the devices to gather
   their available services and characteristics as part of the scanning process.
7. After exiting the BLE Scanner Android app, confirm you can see BLE devices in
   the BLE Setup wizard. Close the wizard.
8. Re-open the BLE Send block mask and select from the available
   peripheral devices and characteristics.

### **Characteristic** — BLE characteristic from peripheral device no characteristic (default)

Select the characteristic available from the selected **Peripheral
Device**. See **Service** for the available characteristics,
and their parent services, provided by the BLE Send block.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Send data using Bluetooth Low Energy (BLE) protocol

The BLE Send block transmits data or instructions from your Android® mobile device to a nearby device or sensor using the Bluetooth® Low Energy (BLE) protocol.

### Central Mode

A BLE device configured in the central mode scans and detects nearby BLE devices and
determines their available services. After scanning, a BLE device operating in the central
mode can connect to any of the discovered BLE devices.

When you set the **Mode** of the devices to `Central
(Client)`, you must scan and detect nearby BLE devices. To start BLE Setup
wizard, click **Scan**. When the wizard completes, select a
**Peripheral Device** and **Characteristic** found
during the scan and detection.

### Peripheral Mode

A BLE device configured in the peripheral mode advertises its presence to other devices,
broadcasting minimal information on the service supported and identity of the device. This
allows BLE devices configured in the central mode to scan and detect nearby BLE devices and
determine their available services.

When you set the **Mode** of the device to `Peripheral
(Server)`, you must specify the **Service** and
**Characteristic** of your device. Other devices with the same service
and characteristic then receive the data sent from your Android mobile device.

### Service and Characteristic

BLE data exchange is based on the Generic Attributes (GATT) profile, which defines a
hierarchical data structure. GATT consists of a service, such as Heart Rate service, that
can contain several characteristics, such as Heart Rate Measurement or Body Sensor Location.
Universally Unique ID (UUID) defines both services and characteristics allowing different
BLE devices to identify the services and characteristics of the connected device.

When a BLE device operates in peripheral mode, the available services provided by the
device are advertised to any listening BLE devices operating in the central mode. Only when
the BLE central device establishes the connection to the BLE peripheral device are the
characteristics within the service made available. Many services and associated
characteristics are already available as standards, including the Heart Rate service.

You can optionally specify your own or custom services and characteristics using your
own UUIDs for the service and characteristics. To enable custom UUID specification, select
the **Specify using UUID** parameter.
