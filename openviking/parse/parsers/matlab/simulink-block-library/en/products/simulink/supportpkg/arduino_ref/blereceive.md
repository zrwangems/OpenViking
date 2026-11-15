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
language: en
---

# BLE Receive

## Ports

### Output

### **data** — Data received by BLE device N-by-1 array

The block outputs the data it receives from a BLE device as an
*N*-by-1 array.

**Note**

The BLE Receive block does not process the data it receives
from a BLE device before outputting it. For more information about the content of
the data array, see GATT
Characteristics.

**Data Types:** `int8`

### **size** — Size of data received by BLE device 2 (default) | nonnegative integer

The block outputs size of the data it receives from a BLE device in bytes.

**Data Types:** `uint8`

## Parameters

### **Mode** — BLE mode `Peripheral (Server)` (default) | `Central (Client)`

Set the hardware of your BLE device to one of these modes.

- `Peripheral (Server)` — When you select this mode,
  specify the Service and Characteristic of the
  Bluetooth device. Other Bluetooth devices then receive the data sent from your Arduino board that has the same service and characteristic.
- `Central (Client)` — When you select this mode, scan
  and detect nearby BLE devices before selecting the peripheral device in the Peripheral device parameter and
  its characteristic in the Characteristic
  parameter.

### **Specify using UUID** — Specify service and characteristic using UUID `off` (default) | `on`

Enable this parameter to specify the BLE service and
characteristic
using the universal unique ID (UUID) values.

#### Dependencies

To enable this parameter, set **Mode** to `Peripheral
(Server)`.

### **Service** — BLE service name `Heart Rate` (default) | `...`

Select the service that the BLE device broadcasts when operating in the
`Peripheral (Server)` mode. Available services are listed in the
following table. When you enable the Specify using UUID, you can write a
specific UUID value for the characteristic as a character array.

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

#### Dependencies

To enable this parameter, set **Mode** to `Peripheral
(Server)`.

### **Characteristic** — BLE characteristic of peripheral device `Heart Rate Measurement` (default) | `...`

Select the BLE characteristic of the peripheral device. The available
characteristics vary depending on the service you select in the
**Service** parameter.

#### Dependencies

To enable this parameter, set **Mode** to `Peripheral
(Server)`.

### **Scan** — Open BLE Setup wizard to scan nearby Bluetooth enabled devices button

Click this button to open the BLE Setup wizard. Use the wizard to discover nearby
Bluetooth enabled devices and their characteristics. You can scan for the devices
using the host computer or the Arduino board. To open and configure the BLE Setup wizard:

1. Set Mode to
   `Central (Client)`. The BLE Setup wizard allows you to
   scan nearby Bluetooth devices.
2. Follow the instructions on the screen to import the device name and its
   characteristics to show in the Block Parameters dialog box under the Peripheral device and Characteristic parameters,
   respectively.
3. Close the BLE Setup wizard. Reopen the BLE Receive block dialog
   box and select from the available peripheral devices and characteristics.

#### Dependencies

To enable this button, set **Mode** to `Central
(Client)`.

### **Peripheral device** — Devices available through BLE Setup wizard `No Devices` (default)

Select from the available peripheral devices or sensors. If you cannot see any
devices, click Scan to detect new BLE
devices within the range of your host computer or Arduino board.

**Note**

Peripheral device name must not contain characters with numeric values greater
than 255.

#### Dependencies

To enable this parameter, set **Mode** to `Central
(Client)`.

### **Characteristic** — Available BLE characteristic for peripheral device `No Characteristic` (default)

Select a characteristic for the peripheral device from the available
characteristics. For a complete list of characteristics available under each BLE
service, see the Service parameter.

#### Dependencies

To enable this parameter, set **Mode** to `Central
(Client)`.

### **Data size (N)** — Size of data received by block `2` (default) | scalar

Enter the size of data that the block can receive from the BLE device.

### **Sample time** — Time interval at which block receives data `0.1` (default) | scalar

Enter the time interval (in seconds) at which the BLE Receive block
receives data from the BLE device.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Receive data using Bluetooth Low Energy (BLE) protocol

Use the BLE Receive block to enable your Arduino® board to receive data or instructions from a nearby device or sensor using the
Bluetooth® Low Energy (BLE) protocol.

### Supported Arduino Boards

- Arduino Nano 33 IoT
- Arduino Nano 33 BLE Sense
- Arduino MKR Wi-Fi® 1010
- Arduino compatible ESP32 – WROOM
- Arduino compatible ESP32 – WROVER

### Central Mode

A BLE device configured in the Central (Client) mode can scan and detect nearby BLE
devices and determine their available services. When you set the **Mode**
parameter to `Central (Client)`, use the **Scan** button
on the block to set up the BLE Setup wizard. The BLE Setup wizard scans for nearby BLE
devices and determines the services and characteristics available on these devices. Once
wizard detects nearby BLE devices, select a peripheral device and its characteristic using
the **Peripheral Device** and **Characteristic**
parameters.

### Peripheral Mode

A BLE device configured in the Peripheral (Server) mode advertises its presence to other
devices, broadcasting minimal information on the services it supports and the identity of
the device. This allows BLE devices configured in the central mode to scan and detect nearby
BLE devices and determine their available services. When you set the
**Mode** of the device to `Peripheral (Server)`, you
must specify the **Service** and **Characteristic** of
your device. Other devices with the same service and characteristic then receive the data
sent from your Arduino board.

### Service and Characteristic

BLE data exchange is based on the Generic Attributes (GATT) profile, which defines a
hierarchical data structure. GATT consists of a service, such as Heart Rate service, that
can contain several characteristics, such as Heart Rate Measurement or Body Sensor Location.
Universal unique ID (UUID) defines both services and characteristics allowing different BLE
devices to identify the services and characteristics of the connected device.

When a BLE device operates in the peripheral mode, the available services provided by
the device are advertised to any listening BLE devices operating in the central mode. Only
when the BLE central device establishes a connection to the BLE peripheral device are the
characteristics within the service made available. Many services and associated
characteristics are already available as standards, including the Heart Rate service.

You can optionally specify your own or custom services and characteristics using your
own UUIDs for the service and characteristics. To enable custom UUID specification, select
the **Specify using UUID** parameter.
