---
type: simulink-block
title: 'LIS3DH Accelerometer Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'lis3dhaccelerometersensor'
documentation_source_path: 'nucleo/ref/lis3dhaccelerometersensor.html'
language: en
---

# LIS3DH Accelerometer Sensor

## Ports

### Output

### **Acceleration** — Acceleration along each axis as measured by accelerometer vector

The block outputs acceleration as a
`1`-by-`3` vector when FIFO is disabled.
When FIFO is enabled, the block outputs
`n`-by-`3` vector, where
`n` is the number of samples. Each value represents the
measurement of acceleration in `m/s^2` along the X, Y, and Z
axes.

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `single` | `double` | `int16`

### **ADC1 Voltage** — Voltage on external pin ADC1 vector

The block outputs voltage applied on the external pin ADC1 of the LIS3DH
sensor.

#### Dependencies

This output port appears only if you select the **Voltage (external
input at ADC1)** parameter.

**Data Types:** `single` | `double` | `int16`

### **ADC2 Voltage** — Voltage on external pin ADC2 vector

The block outputs voltage applied on the external pin ADC2 of the LIS3DH
sensor.

#### Dependencies

This output port appears only if you select the **Voltage (external
input at ADC2)** parameter.

**Data Types:** `single` | `double` | `int16`

### **ADC3 Voltage** — Voltage on external pin ADC3 vector

The block outputs voltage applied on the external pin ADC3 of the LIS3DH
sensor.

#### Dependencies

This output port appears only if you select `Voltage (external
input)` for **ADC3 input** parameter.

**Data Types:** `single` | `double` | `int16`

### **Temperature** — Temperature measured by LIS3DH sensor scalar

Temperature (in ℃) measured by LIS3DH sensor connected to Arduino board.

#### Dependencies

This output port appears only if you select
`Temperature` for **ADC3 input**
parameter.

**Data Types:** `single` | `double` | `int16`

### **Acceleration status** — Status of acceleration measurement `2` | `0` | `1`

The block outputs the status of acceleration measured as a value
`0`, `1`, or `2`. The value
`0` indicates that the data read is new, `1`
indicates that the data read is not new, and `2` indicates that the
data is overwritten.

If **Enable FIFO** is selected, then `0`
indicates that the specified samples are collected, `1` indicates
that specified number of samples are not collected, and `2` indicates
that the data is overwritten.

#### Dependencies

This output port appears only if you select the **Acceleration data
ready status** parameter.

**Data Types:** `uint8`

### **Samples pending** — Number of pending samples scalar

The block outputs the number of pending samples to be read as a value ranging from
`0-32`.

#### Dependencies

This output port appears only if you select the **Enable FIFO**
parameter.

**Data Types:** `uint8`

### **Click status [X,Y,Z]** — Click detection status `0` | `1`

The block outputs the Click status of axes as a
`1`-by-`3` vector (x,y,z) indicating on which axis
the click has been detected. The axis value `1` indicates that the
click is detected on that axis and `0` indicates that the click is
not detected.

#### Dependencies

This output port appears only if you select the **click
status** parameter.

**Data Types:** `uint8`

### **Inertial wake-up status [X,Y,Z]** — Status of inertial wake-up interrupt `0` | `1`

The block outputs inertial wake-up status as a
`1`-by-`3` vector. This provides information of
the axis, on which inertial wake-up is detected. The value `1`
indicates that the inertial wake-up event is detected on the selected axis and value
`0` indicates the event is not detected.

#### Dependencies

This parameter appears only if you select `Inertial
wake-up` from **Detect** parameter and select
**Detection status** parameter.

**Data Types:** `uint8`

### **Free-fall status** — Status of free-fall `0` | `1`

The block outputs free-fall status. The value `1` indicates that
the free-fall is detected on the selected axis and `0` indicates the
interrupt is not detected.

#### Dependencies

This parameter appears only if you select `Free-fall`
from **Detect** parameter and select **Detection
status** parameter.

**Data Types:** `uint8`

### **6D position status [X, -X, Y, -Y, Z, -Z]** — Status of 6D position `0` | `1`

The block outputs 6D position status as a
`1`-by-`6` vector. The value `1`
indicates that the 6D position interrupt is detected on the selected axis and
`0` indicates the interrupt is not detected.

#### Dependencies

This parameter appears only if you select `6D position`
from **Detect** parameter and select **Detection
status** parameter.

**Data Types:** `uint8`

### **6D movement status [X, -X, Y, -Y, Z, -Z]** — Status of 6D movement `0` | `1`

The block outputs 6D movement status as a
`1`-by-`6` vector. The value `1`
indicates that the 6D movement interrupt is detected on the selected axis and
`0` indicates the interrupt is not detected.

#### Dependencies

This parameter appears only if you select `6D movement`
from **Detect** parameter and select **Detection
status** parameter.

**Data Types:** `uint8`

### **4D position status [X, -X, Y, -Y]** — Status of 4D position `0` | `1`

The block outputs 4D position status as a
`1`-by-`4` vector. The value `1`
indicates that the 4D position interrupt is detected on the selected axis and
`0` indicates the interrupt is not detected.

#### Dependencies

This parameter appears only if you select `4D position`
from **Detect** parameter and select **Detection
status** parameter.

**Data Types:** `uint8`

### **4D movement status [X, -X, Y, -Y]** — Status of 4D movement `0` | `1`

The block outputs 4D movement status as a
`1`-by-`4` vector. The value `1`
indicates that the 4D movement interrupt is detected on the selected axis and
`0` indicates the interrupt is not detected.

#### Dependencies

This parameter appears only if you select `4D movement`
from **Detect** parameter and select **Detection
status** parameter.

**Data Types:** `uint8`

## Parameters

### Main

### **I2C address** — I2C addresses to communicate with sensor peripherals `0x18` (default) | `0x19`

The I2C addresses to communicate with the accelerometer peripheral on the LIS3DH
sensor are decided by the state of the SA0 pin on the hardware board. This table
provides the I2C addresses corresponding to the pin and their state.

| Pin Name | Pin State | I2C address |
| --- | --- | --- |
| SA0 | 0 | 0x18 |
| 1 | 0x19 |

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the
output ports.

### **ADC3 input** — Select output port for reading temperature or voltage `None` (default) | `Temperature` | `Voltage (external input)`

Select `Temperature` to set
**Temperature** as one of the output ports or select
`Voltage (external input)` to set **ADC3
Voltage** as one of the output port.

### **Voltage (external input at ADC1)** — Select output port for reading voltage `off` (default) | `on`

Select this parameter to set **ADC1 Voltage** as one of the
output ports.

### **Voltage (external input at ADC2)** — Select output port for reading voltage `off` (default) | `on`

Select this parameter to set **ADC2 Voltage** as one of the
output ports.

### **Acceleration data ready status** — Set output port for obtaining acceleration status `on` (default) | `off`

Select this parameter to set **Acceleration status** as one of
the output ports.

### **Accelerometer resolution** — Data register bit resolution `12bit` (default) | `10bit` | `8bit`

Select the data register bit resolution for the sensor.

### **Accelerometer output data rate (Hz)** — Rate at which accelerometer data is sampled `400 Hz` (default) | `1 Hz` | `10 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `1344 Hz`

Select the output data rate at which accelerometer data is sampled.

### **Accelerometer range** — Full scale for measuring linear acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the full scale for measuring linear acceleration (the range of acceleration
that the sensor needs to measure).

### **Enable FIFO** — Enable number of samples to read `off` (default) | `on`

Select this option to enable the option **Number of samples to read
from FIFO (1-32)**, which allows you to set the number of samples
to be read. When FIFO is enabled, the oldest set of samples from the buffer is
read first and newest set of samples is read last.

### **Number of samples to read from FIFO (1-32)** — Number of samples to read `2` (default)

Enter a value for number of samples (1-32) to be read from FIFO.

#### Dependencies

This parameter appears only if you select the **Enable FIFO**
parameter.

**Note**

For AVR targets, if the value for **Number of samples to read from FIFO
(1-32)** parameter is set to more than `29`, then the Display
Sample values might show as zeros. To avoid this issue, set the baud rate of External Mode
to a value less than `921600`. To change the baud rate, select
**Hardware** > **Hardware Settings** >
**Hardware Implementation** > **Target hardware
resources** > **Host-board connection** and change the value
for **Baudrate** under **External Mode over Serial
communication** to `115200` (recommended
value).

### **Generate FIFO overrun interrupt on INT1 pin** — Generate interrupt when FIFO buffer is full `off` (default) | `on`

Select this option to receive an interrupt if the FIFO buffer gets filled and the
first sample is overwritten.

#### Dependencies

This parameter appears only if you select the **Enable FIFO**
parameter.

### **Enable high pass filter** — Enable high pass filter for accelerometer data `off` (default) | `on`

Enable the high pass filter for reading accelerometer values.

### **HPF cutoff frequency (Hz)** — Bandwidth of high pass filter `100 Hz` (default) | `12 Hz` | `25 Hz` | `50 Hz`

Select the required bandwidth of the high pass filter for reading accelerometer
values. The HPF cutoff frequency depends on the Accelerometer output data rate (Hz).
The HPF cutoff frequencies for the selected Accelerometer output data rate (Hz) are
shown in this table. The values `00`, `01`,
`10`, and `11` are the HPF mode configurations.

**HPF cutoff frequency**

| HPF cutoff frequency[2:1] | Acceleration output data rate - 1 Hz | Acceleration output data rate - 10 Hz | Acceleration output data rate - 25 Hz | Acceleration output data rate - 50 Hz | Acceleration output data rate - 100 Hz | Acceleration output data rate - 200 Hz | Acceleration output data rate - 400 Hz | Acceleration output data rate - 1600 Hz | Acceleration output data rate - 5376 Hz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `0.02` | `0.2` | `0.5` | `1` | `2` | `4` | `8` | `32` | `100` |
| `01` | `0.008` | `0.08` | `0.2` | `0.5` | `1` | `2` | `4` | `16` | `50` |
| `10` | `0.004` | `0.04` | `0.1` | `0.2` | `0.5` | `1` | `2` | `8` | `25` |
| `11` | `0.002` | `0.02` | `0.05` | `0.1` | `0.2` | `0.5` | `1` | `4` | `12` |

#### Dependencies

This parameter appears only if you select the **Enable high pass
filter** parameter.

### **Generate data ready interrupt on INT1 pin** — Generate interrupt when data is ready `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 of the sensor
when data is ready, allowing you to trigger other subsystems to perform any
action.

### **Data type** — Output data type for values from lis3dh sensor `single` (default) | `double` | `int16`

Specify the output data type for the values read from lis3dh sensor. The default
data type for Arduino hardware is `single`. Use this parameter to change the
values to `double` or `int16`, if required.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LIS3DH sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

### Click detection

### **Enable click detection** — Option for enabling click detection `off` (default) | `on`

Select this parameter to enable click detection.

### **Type** — Select type of click to be detected `Single click` (default) | `Double click`

Select the type of click to be detected. The available options are
`Single click` and `Double
click`.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Threshold (m/s2)** — Threshold for detecting single or double click `1.5` (default)

Specify the threshold for detecting single click or double click. When the value
crosses the specified threshold value, click is detected.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Time limit (s)** — Time limit duration `0.3` (default) | `positive integer`

Specify the time limit value in seconds for detecting single click or double
click. The click must occur during the specified time limit for detecting single click
or double click.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Time latency (s)** — Time latency duration `0.3` (default) | `positive integer`

Specify the time latency value in seconds for detecting double click. The second
click must occur after the specified time latency period for detecting a double
click.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter and select `Double click`
option for **Type** parameter.

### **Time window (s)** — Time window duration `0.3` (default) | `positive integer`

Specify the time window value in seconds for detecting double click. The second
click must occur before the time window period expires for detecting double
click.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter and select `Double click`
option for **Type** parameter.

### **X axis** — Click detection in X axis `on` (default) | `off`

Select this option to enable click detection along X axis. The value
`1` indicates that the click is detected and
`0` indicates that the click is not detected.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Y axis** — Click detection in Y axis `on` (default) | `off`

Select this option to enable click detection along Y axis. The value
`1` indicates that the click is detected and
`0` indicates that the click is not detected.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Z axis** — Click detection in Z axis `off` (default) | `on`

Select this option to enable click detection along Z axis. The value
`1` indicates that the click is detected and
`0` indicates that the click is not detected.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Generate click interrupt** — Generate interrupt when click is detected `off` (default) | `on`

Select the option to generate an interrupt, if a click is detected.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### **Interrupt pin** — Pin to generate click interrupt `INT1` (default) | `INT2`

If this option is selected, an interrupt is generated on pin INT1 or IN2 of the
sensor when data is ready, allowing you to trigger other subsystems to perform any
action.

#### Dependencies

This parameter appears only if you select **Generate click
interrupt** parameter.

### **Click status** — Set output port for obtaining click detection status `off` (default) | `on`

Select this parameter to set **Click status [X,Y,Z]** as one of
the output ports.

#### Dependencies

This parameter appears only if you select **Enable click
detection** parameter.

### Configurable detections

### **Configurable detections** — Set number of configurable detections `0` (default) | `1` | `2`

Select the required option for the number of configurable detections.

#### Configurable detections 1

### **Detect** — Select configurable event `Inertial wake-up` (default) | `Free-fall` | `6D position` | `6D movement` | `4D position` | `4D movement`

Select the required feature of the sensor. (Inertial wake-up, Free-fall, 6D
position, 6D movement, 4D position, 4D movement).

#### Dependencies

This parameter appears only if you select `1` or
`2` from **Configurable detections**
parameter.

### **X axis** — Configurable detection in X axis `on` (default) | `off`

Select this option to enable the configurable event detection status on X axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `Inertial
wake-up` or `6D position` or `6D
movement` or `4D position` or
`4D movement` from **Detect**
parameter.

### **Y axis** — Configurable detection in Y axis `on` (default) | `off`

Select this option to enable the configurable event detection status on Y axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `Inertial
wake-up` or `6D position` or `6D
movement` or `4D position` or
`4D movement` from **Detect**
parameter.

### **Z axis** — Configurable detection in Z axis `on` (default) | `off`

Select this option to enable the configurable event detection status on Z axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `Inertial
wake-up` or `6D position` or `6D
movement` from **Detect** parameter.

### **-X axis** — Configurable detection in -X axis `off` (default) | `on`

Select this option to enable the configurable event detection status on -X axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `6D position`
or `6D movement` or `4D position`
or `4D movement` from **Detect**
parameter.

### **-Y axis** — Configurable detection in -Y axis `off` (default) | `on`

Select this option to enable the configurable event detection status on -Y axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `6D position`
or `6D movement` or `4D position`
or `4D movement` from **Detect**
parameter.

### **-Z axis** — Configurable detection in -Z axis `off` (default) | `on`

Select this option to enable the configurable event detection status on -Z axis.
The value `1` indicates that the event is detected and
`0` indicates that the event is not detected.

#### Dependencies

This parameter appears only if you select `6D position`
or `6D movement` from **Detect**
parameter.

### **Threshold (m/s2** — Acceleration threshold for detecting selected configurable detection `1.5` (default)

Specify the threshold for detecting the selected configurable detection. When the
acceleration value crosses the specified threshold value, the event is
detected.

#### Dependencies

This parameter appears only if you select `1` or
`2` from **Configurable detections**
parameter.

### **Duration (s)** — Time limit duration `0.3` (default) | `positive integer`

Specify the time limit for detecting the configurable event. To detect an event,
the Threshold criteria must be satisfied for a minimum time equal to Duration.

#### Dependencies

This parameter appears only if you select `1` or
`2` from **Configurable detections**
parameter.

### **Generate interrupt** — Generate interrupt `off` (default) | `on`

If this option is selected, an interrupt is generated for the selected
configurable detection.

#### Dependencies

This parameter appears only if you select `1` or
`2` from **Configurable detections**
parameter.

### **Interrupt pin** — Pin to generate interrupt `INT1` (default) | `INT2`

If this option is selected, an interrupt is generated on pin INT1 or IN2 of the
sensor when the configurable event is detected, allowing you to trigger other
subsystems to perform any action.

#### Dependencies

This parameter appears only if you select the **Generate
interrupt** parameter.

**Note**

Parameters for **Configuration detections 2** are similar
to **Configuration detections 1**. For information to configure
these parameters, see Configurable detections.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Measure linear acceleration, voltage, and temperature from LIS3DH sensor

The LIS3DH Accelerometer Sensor block measures linear acceleration,
voltages on external input pins (ADC1, ADC2 and ADC3) of the sensor, and temperature using the
LIS3DH Accelerometer sensor interfaced with the Arduino® hardware.

The block also provides the option to enable the high pass filter, FIFO and FIFO
interrupt. An interrupt is generated if **Generate data ready interrupt** is
selected. After selecting **Generate data ready interrupt**, if FIFO is
disabled data ready interrupt is generated and if FIFO is enabled FIFO interrupt is
generated.

The block outputs status of acceleration measurement, specified as a value
`0`, `1`, or `2`. The value
`0` indicates that the data read is new, `1` indicates
that the data read is not new, and `2` indicates that the data is
overwritten.

The block outputs single / double click axis as a
`1`-by-`3` vector. The click axis provides information of
the axis, on which click is detected. The axis value displays `1` when a
click is detected otherwise it displays `0`.

The block supports inertial wake-up, free-fall, 6D position, 6D movement, 4D position and
4D movement recognition. The block outputs inertial wake-up axis as a
`1`-by-`3` vector. This provides information of the axis,
on which inertial wake-up is detected. The 6D position axis and 6D movement axis are of size
`1`-by-`6`. The 4D position and 4D movement axis are of
size `1`-by-`4`. The status contains the information about
the axis, on which the detection is recognized. The status value displays `1`
when the configured detection is recognized on the selected axis, otherwise it displays
`0`.

**Note**

Always ensure to connect the sensor to the board, when performing monitor and tune
with sensor block available in the model.
