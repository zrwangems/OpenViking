---
type: simulink-block
title: 'Pixy2 Vision Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'pixy2visionsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/pixy2visionsensor.html'
language: en
---

# Pixy2 Vision Sensor

## Ports

### Output

### **X** — *x*-location of the center of the detected object pixels | scalar

The *x*-location of the center of the most significant object
(color blob) based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Signature`, `Color Code
Signature`, or `Color and Color Code Signature
(Mixed)`.

**Data Types:** `uint16`

### **Y** — *y*-location of the center of the detected object pixels | scalar

The *y*-location of the center of the most significant object
(color blob) based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Signature`, `Color Code
Signature`, or `Color and Color Code Signature
(Mixed)`.

**Data Types:** `uint16`

### **Width** — Width of detected object pixels | scalar

The width of the most significant object (color blob) based on the field of view,
as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Signature`, `Color Code
Signature`, or `Color and Color Code Signature
(Mixed)`.

**Data Types:** `uint16`

### **Height** — Height of detected object pixels | scalar

The height of the most significant object (color blob) based on the field of view,
as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Signature`, `Color Code
Signature`, or `Color and Color Code Signature
(Mixed)`.

**Data Types:** `uint16`

### **Object Count** — Number of detected objects positive integer in the range [1, 255]

The number of objects (color blobs) based on the field of view, as detected by the
Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Signature`, `Color Code
Signature`, or `Color and Color Code Signature
(Mixed)`.

**Data Types:** `uint8`

### **Signature** — Color or color code signature of detected objects positive integer in the range [1, 7]

The signature of the color or color-coded objects (color blobs) based on the field
of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
either `Color Code Signature` or `Color and
Color Code Signature (Mixed)`.

**Data Types:** `uint16`

### **Angle** — Angle of detected object integer in the range [-180, +180]

The angle of the color or color-coded signature of objects (color blobs) based on
the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Color and Color Code Signature (Mixed)`.

**Data Types:** `int16`

### **Xstart** — Start point of *x*-coordinate for detected line pixels | scalar

The starting point of the *x*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Line`.

**Data Types:** `uint16`

### **Ystart** — Start point of *y*-coordinate for detected line pixels | scalar

The starting point of the *y*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Line`.

**Data Types:** `uint16`

### **Xend** — End point of *x*-coordinate for detected line pixels | scalar

The ending point of the *x*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Line`.

**Data Types:** `uint16`

### **Yend** — End point of *y*-coordinate for detected line pixels | scalar

The ending point of the *y*-coordinate of the most significant
line based on the field of view, as detected by the Pixy2 vision sensor.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Line`.

**Data Types:** `uint16`

### **Intersection Flag** — Presence of intersecting lines 1 (true) or 0 (false)

The presence of intersecting lines in the field of view of the Pixy2 vision
sensor. `1` indicates the presence of intersecting lines.

#### Dependencies

To enable this port , set the **Tracking mode** parameter to
`Line`.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port** — Input port connected to Pixy2 vision sensor `4` (default) | positive integer in the range [1, 4]

Select the input port on the LEGO
MINDSTORMS EV3 hardware to which the Pixy2 vision sensor is connected. There are four
ports on the hardware and you can select any one of the ports. Specify a unique input
port for each Pixy2 Vision Sensor block in the model.

### **I2C address** — I2C bus identifier `0x54` (default) | address in the range [`0x54`, `0x57`]

Enter the hexadecimal address of the I2C bus connected to the Pixy2 vision Sensor.
Ensure that the same I2C address is configured in the PixyMon utility.

### **Tracking mode** — Select tracking mode `Color Signature` (default) | `Color Code Signature` | `Color and Color Code Signature (Mixed)` | `Line`

Select the tracking mode to detect the object that matches the configured color or
color-coded signature in the PixyMon utility. The *xy*-coordinates,
width, and height of the detected object remain the same for the `Color
Signature`, `Color Code Signature`, and
`Color and Color Code Signature (Mixed)` tracking
modes.

### **Color Signature** — Color signature of object to be tracked `1` (default) | positive integer in the range [1, 7] | `ALL`

Select the color signature of the object to be tracked as configured in the PixyMon
utility. Select `ALL` to track all the configured color
signatures.

### **Sample time** — Time sample interval `0.1` (default) | positive scalar in the range [`0.001`, `1`]

Enter the time interval at which the block reads values from the Pixy2 vision
sensor.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Represent connected CMUcam5 Pixy2 vision sensor and tracks object (color blob)

The Pixy2 Vision Sensor block allows you to extend the capabilities of the
LEGO®
MINDSTORMS® EV3 hardware and reads the coordinates of object (color blobs) detected by the
Pixy2 vision sensor.

**Note**

This block supports Pixy2 LEGO firmware version 3.0.14.

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

If you have already installed the support package for LEGO
MINDSTORMS EV3 hardware and followed the additional hardware setup as mentioned in Install Support for LEGO MINDSTORMS EV3 Hardware, the PixyMon utility will launch
automatically.
