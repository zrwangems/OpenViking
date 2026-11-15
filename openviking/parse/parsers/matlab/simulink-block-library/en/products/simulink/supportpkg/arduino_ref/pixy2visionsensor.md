---
type: simulink-block
title: 'Pixy2 Vision Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Vision Sensors'
documentation_page: 'pixy2visionsensor'
documentation_source_path: 'supportpkg/arduino_ref/pixy2visionsensor.html'
language: en
---

# Pixy2 Vision Sensor

## Ports

### Output

### **X** — *x*-location of the center of the detected object pixels | scalar

The *x*-location of the center of the most significant object
(color blob) based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Signature`, `Color Code
  Signature`, or `Color and Color Code Signature
  (Mixed)`.

**Data Types:** `uint16`

### **Y** — *y*-location of the center of the detected object pixels | scalar

The *y*-location of the center of the most significant object
(color blob) based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Signature`, `Color Code
  Signature`, or `Color and Color Code Signature
  (Mixed)`.

**Data Types:** `uint16`

### **Width** — Width of detected object pixels | scalar

The width of the most significant object (color blob) based on the field of view,
as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Signature`, `Color Code
  Signature`, or `Color and Color Code Signature
  (Mixed)`.

**Data Types:** `uint16`

### **Height** — Height of detected object pixels | scalar

The height of the most significant object (color blob) based on the field of view,
as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Signature`, `Color Code
  Signature`, or `Color and Color Code Signature
  (Mixed)`.

**Data Types:** `uint16`

### **Object Count** — Number of detected objects positive integer in the range [1, 255]

The number of objects (color blobs) based on the field of view, as detected by the
Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Signature`, `Color Code
  Signature`, or `Color and Color Code Signature
  (Mixed)`.

**Data Types:** `uint8`

### **Signature** — Color or color code signature of detected objects positive integer in the range [1, 7]

The signature of the color or color-coded objects (color blobs) based on the field
of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to either `Color Code Signature` or `Color
  and Color Code Signature (Mixed)`.

**Data Types:** `uint16`

### **Angle** — Angle of detected object integer in the range [-180, +180]

The angle of the color or color-coded signature of objects (color blobs) based on
the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Color and Color Code Signature (Mixed)`.

**Data Types:** `int16`

### **X0** — Start point of *x*-coordinate for detected line pixels | scalar

The starting point of the *x*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Line`.

**Data Types:** `uint16`

### **Y0** — Start point of *y*-coordinate for detected line pixels | scalar

The starting point of the *y*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Line`.

**Data Types:** `uint16`

### **X1** — End point of *x*-coordinate for detected line pixels | scalar

The ending point of the *x*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Line`.

**Data Types:** `uint16`

### **Y1** — End point of *y*-coordinate for detected line pixels | scalar

The ending point of the *y*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Line`.

**Data Types:** `uint16`

### **IntFlag** — Presence of intersecting lines `1` (true) or `0` (false)

The presence of intersecting lines in the field of view of the Pixy2 vision
sensor. `1` indicates the presence of intersecting lines.

#### Dependencies

- To enable this port , set the **Tracking mode** parameter
  to `Line`.

**Data Types:** `uint8`

## Parameters

### **Interface** — Interface type `I2C` (default) | `SPI with CS` | `Serial`

Select the type of interface on the Arduino board to establish a connection with the Pixy2 vision sensor.

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

#### Dependencies

To enable this parameter, set **Interface** to
`I2C`.

### **Pixy2 I2C address** — I2C address of Arduino board `0x54` (default) | address in the range [`0` to `127`]

To connect a Pixy2 vision sensor to an Arduino board using I2C communication protocol, enter the I2C address of the
Arduino board.

#### Dependencies

To enable this parameter, set **Interface** to
`I2C`.

### **SPI module** — SPI communication module `0` (default) | scalar

Specify the SPI module on the Arduino hardware to communicate with SPI peripherals. For more information on
Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

#### Dependencies

To enable this parameter, set **Interface** to `SPI
with CS`.

### **Chip select pin** — Chip select pin of Arduino board `4` (default) | target hardware pin

To connect a Pixy2 vision sensor to an Arduino board using SPI communication protocol, enter the chip select pin of the
Arduino board. For more information on chip select pins for Arduino boards, see Pin Mapping for Arduino Timer-Independent Blocks.

#### Dependencies

- To enable this parameter, set **Interface** to
  `SPI with CS`.

### **Serial** — Serial port number of Arduino board `0` (default) | target hardware port

To connect a Pixy2 vision sensor to an Arduino board using serial communication, enter the serial port number of the
Arduino board. For more information on serial port numbers for Arduino boards, see Pin Mapping for Arduino Timer-Independent Blocks.

#### Dependencies

- To enable this parameter, set **Interface** to
  `Serial`.

### **Tracking mode** — Select tracking mode `Color Signature` (default) | `Color Code Signature` | `Color and Color Code Signature (Mixed)` | `Line`

Select the tracking mode to detect the object that matches the configured color or
color-coded signature in the PixyMon utility. The *xy*-coordinates,
width, and height of the detected object remain the same for the `Color
Signature`, `Color Code Signature`, and
`Color and Color Code Signature (Mixed)` tracking
modes.

### **Color signature** — Color signature of object to be tracked `1` (default) | positive integer in the range [1, 7] | `ALL`

Select the color signature of the object to be tracked as configured in the PixyMon
utility. Select `ALL` to track all the configured color
signatures.

### **Sample time** — Time sample interval `0.1` (default) | positive scalar in the range [0.001, 1]

Enter the time interval at which the block reads values from the Pixy2 vision
sensor.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Represent connected CMUcam5 Pixy2 vision sensor and tracks object (color blob)

Use the Pixy2 Vision Sensor block to read the coordinates of object (color
blobs) detected by the Pixy2 vision sensor interfaced with an Arduino® board. You can use either SPI, I2C, or serial communication protocol to connect
the Pixy2 vision sensor to an Arduino board.

### Functional Modes

Pixy2 Vision Sensor block has four functional modes:

- Color Signature: Detects object that matches the configured color signature in the
  PixyMon utility.
- Color Code Signature: Detects object that matches the configured color-coded
  signature in the PixyMon utility.
- Color and Color Code Signature (Mixed): Detects object that matches the configured
  color and color-coded signature in the PixyMon utility.
- Line: Detects and tracks the line.

### Launch PixyMon

If you have already installed the support package for Arduino hardware and followed the additional hardware setup as mentioned in Install Support for Arduino Hardware, the
PixyMon utility will launch automatically.
