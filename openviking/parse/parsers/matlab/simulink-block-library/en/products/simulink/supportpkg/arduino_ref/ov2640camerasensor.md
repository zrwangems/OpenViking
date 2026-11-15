---
type: simulink-block
title: 'OV2640 Camera Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Vision Sensors'
documentation_page: 'ov2640camerasensor'
documentation_source_path: 'supportpkg/arduino_ref/ov2640camerasensor.html'
language: en
---

# OV2640 Camera Sensor

## Ports

### Input

### **Capture trigger** — Initiate image capture `0` | `1`

Signal input to block that initiates image capture.

**Data Types:** `uint8`
### Output

### **Data** — Raw JPEG image data vector

Raw JPEG image data with values ranging from 0—255. The size of the image depends
on the JPEG encoding compression ratio and is less than the actual resolution.

**Data Types:** `uint8`

### **Data length** — Size of data scalar

Size of the raw JPEG image data.

**Data Types:** `uint16`

### **Status** — Capture outcome status scalar

The **Status** port outputs the status of the capture operation.
Each value corresponds to a specific data output.

| Scenario | Status Value | Data Output |
| --- | --- | --- |
| Valid output | `0` | Valid raw image data |
| Size of actual image data exceeds the maximum image buffer size | `1` | `0` |
| Invalid output | `2` | `0` |
| Incorrect sensor initialization | `3` | `0` |
| Capture timeout | `4` | `0` |

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — Peripheral address to communicate with camera sensor `0x30` (default) | scalar

The peripheral address of the OV2640 camera sensor to communicate with the
Arduino hardware.

### **SPI module** — SPI communication module `0` (default) | scalar

Specify the SPI module on the Arduino hardware to communicate with SPI peripherals. For more information on
Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Chip select pin** — Chip select pin of Arduino board `10` (default) | target hardware pin

To connect an ArduCam Mini 2MP Plus camera module with an OV2640 sensor to an
Arduino board, enter the chip select pin of the Arduino board. For more information on chip select pins for Arduino boards, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Product ID** — Product ID of sensor `0x41` (default) | `0x42`

Select the Product ID of the sensor.

### **Image Resolution** — Image dimensions `160x120` (default) | `176x144` | `320x240` | `352x288` | `640x480` | `800x600` | `1024x768` | `1280x1024` | `1600x1200`

Select the dimensions of the image that you want to capture in pixels.

For the list of image resolutions available for the supported boards, see Supported
Boards.

### **Max image buffer size** — Maximum size of image `3500` (default) | any nonnegative value

Enter the maximum size of the image in bytes. The image size must be supported by
the hardware you are using for the chosen resolution.

**Note**

The `max image buffer size` must not be greater than the product
of selected `image resolution`.

### **Capture timeout** — Duration of Capture timeout `1` (default) | any nonnegative value

Specify capture timeout in seconds. Capture timeout allows the sensor block to
capture image data at a rate dependent on this value. This parameter also ensures that
capture operation times out once this duration has elapsed. During this duration, the
camera is busy and cannot carry out any other action.

**Note**

To avoid overruns, set the `capture timeout` input to a value
that is smaller than the sample time of the block that you select when determining the
`capture trigger` input.

### Supported Boards

This list shows the supported board and the corresponding image resolutions.

| Arduino Board | Supported resolutions |
| --- | --- |
| Arduino Mega 2560a | `160x120`, `176x144`, `320x240` |
| Arduino Mega ADK | `160x120`, `176x144`, `320x240` |
| Arduino Due | `160x120`, `176x144`, `320x240` |
| Arduino MKR1000 | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino MKR WiFi1010 | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino MKR Zero | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino Nano 33 IoT | `160x120`, `176x144` |
| Arduino Nano 33 BLE SENSE | `160x120`, `176x144` |
| ESP32-DevKitV1 | `160x120`, `176x144`, `320x240`, `352x288`, `640x480`, `800x600` |
| ESP32-DevKitC | `160x120`, `176x144`, `320x240`, `352x288`, `640x480`, `800x600` |
| a Arduino Mega 2560 board supports the `176x144` and `320x240` resolutions only while doing 'Build, Deploy and Start' in Simulink whereas not to 'Monitor and Tune'. | |

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Capture JPEG images using ArduCam 2MP Mini Plus camera module with OV2640 sensor

The OV2640 Camera Sensor block captures images in the JPEG format using the
ArduCam Mini 2MP Plus camera module with an OV2640 sensor. The camera is attached to an
Arduino® board. This block is a composite sensor block and uses both the SPI and I2C
modules.

For a list of boards that support the OV2640 Camera Sensor block, see Supported
Boards.

**Note**

You cannot add multiple OV2640 Camera Sensor blocks to a model.
