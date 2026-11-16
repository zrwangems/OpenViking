---
type: simulink-block
title: 'BMI160 IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'bmi160imusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/bmi160imusensor.html'
language: en
---

# BMI160 IMU Sensor

## Ports

### Output

### **Acceleration** — Linear acceleration measured by BMI160 sensor row vector

Linear acceleration (in m/s2) measured by BMI160
sensor connected to STM32 Processors, along the x-, y- and z- axes, specified
as a row vector [x,y,z].

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double`

### **Angular Rate** — Angular rate measured by BMI160 sensor row vector

Angular rate (in rad/s) measured by BMI160 sensor connected to STM32
Processors, along the x-, y- and z- axes, specified as a row vector
[x,y,z].

#### Dependencies

This output port appears only if you select the **Angular rate
(rad/s)** parameter.

**Data Types:** `double`

### **Magnetic Field** — Magnetic field strength measured by a secondary BMM150 sensor row vector

Magnetic field strength (in µT) measured by a BMM150 sensor that is
connected as a secondary sensor to BMI160 sensor, along the x-, y- and z- axes,
specified as a row vector [x,y,z].

#### Dependencies

This output port appears only if you select the **Enable
secondary magnetometer** and **Magnetic Field
(µT)** parameters.

**Data Types:** `double`

### **Temperature** — Temperature measured by BMI160 sensor scalar

Temperature (in ℃) measured by BMI160 sensor connected to STM32
Processors.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Acceleration Status** — Status of acceleration value `0` | `1`

Status of acceleration `0` indicates that the data read is
new and `1` indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Acceleration
Status** parameter.

**Data Types:** `int8`

### **Angular Rate Status** — Status of angular rate value `0` | `1`

Status of angular rate `0` indicates that the data read is
new and `1` indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Angular Rate
Status** parameter.

**Data Types:** `int8`

### **Magnetic Field Status** — Status of magnetic field value `0` | `1`

Status of magnetic field `0` indicates that the data read
is new and `1` indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Magnetic Field
Status** parameter.

**Data Types:** `int8`

### **Interrupt Source** — Status of interrupt source `0` | `1` | `-1`

Interrupt source is a `1`-by-`7` vector
which represents Single tap, Double tap, High g detection, Any motion, Slow
motion, Flat detection, and Data ready interrupts.

Status of interrupt source `1` indicates that the interrupt
enabled and it is the source of the generated interrupt, `0`
indicates that the interrupt is enabled and it is not the source of the
generated interrupt, and `-1` indicates that the interrupt is
not enabled.

#### Dependencies

This output port appears only if you select one of these
parameters.

- **Single tap**
- **Double tap**
- **High g detection**
- **Any motion**
- **Flat detection**
- **Data ready**

**Data Types:** `double`

### **Tap event Source** — Status of tap event source row vector

Tap event source is a `1`-by-`4` vector
which represents Single tap or Double tap interrupt. The first three elements
indicates if the interrupt occurred in X, Y and Z axis, and the fourth element
indicates if it is on positive or negative direction of the axis. For
direction, byte `0` denotes negative side,
`1` denotes positive side and for other bytes
`1` denotes that axis is the source and
`0` denotes that axis is not the source.

#### Dependencies

This output port appears only if you select the **Interrupt
source** parameter.

**Data Types:** `int8`

### **High g event Source** — Status of high g event source row vector

High g event source is a `1`-by-`4` vector
which represents High g interrupt. The first three elements indicates if the
interrupt occurred in X, Y and Z axis, and the fourth element indicates if it
is on positive or negative direction of the axis. For direction, byte
`0` denotes negative side, `1` denotes
positive side and for other bytes `1` denotes that axis is the
source and `0` denotes that axis is not the source.

#### Dependencies

This output port appears only if you select the **Interrupt
source** parameter.

**Data Types:** `int8`

### **Any motion event Source** — Status of any motion event source row vector

Any motion event source is a `1`-by-`4`
vector which represents Any motion interrupt. The first three elements
indicates if the interrupt occurred in X, Y and Z axis, and the fourth element
indicates if it is on positive or negative direction of the axis. For
direction, byte `0` denotes negative side,
`1` denotes positive side and for other bytes
`1` denotes that axis is the source and
`0` denotes that axis is not the source.

#### Dependencies

This output port appears only if you select the **Interrupt
source** parameter.

**Data Types:** `int8`

## Parameters

### **I2C module** — Module for communication `I2C1` (default)

The I2C module to be used for communication to the BMI160 sensor. The number of
I2C modules supported varies across different STM32 Processors. You can find the
supported I2C modules corresponding to the processor (which you selected for the
Hardware Board parameter in the Simulink® model) by opening the Configuration Parameters dialog box and
checking the I2C specific tabs under **Target hardware
resources**.

### **BMI160 I2C address** — I2C address of BMI160 sensor `0x69` (default) | `0x68`

The I2C address used by BMI160 sensor communicating with the STM32 Processors.
The default parameter value (`0x69`) corresponds to the value
mentioned in the `Schematics` section of the BOOSTXL-SENSORS
BoosterPackTM Plug-in Module User's Guide.

### **Enable secondary magnetometer** — Enable read data from BMM150 connected as a secondary sensor to BMI160 `on` (default) | `off`

If this option is selected, the block can read magnetometer data from a BMM150
sensor that is connected as a secondary sensor to BMI160.

### **BMM150 I2C address** — I2C address of BMM150 sensor `0x10` (default) | `0x11` | `0x12` | `0x13`

The I2C address used by BMM150 sensor connected as a secondary sensor to BMI160
sensor. The default parameter value (`0x13`) corresponds to the
value mentioned in the `Schematics` section of the
BOOSTXL-SENSORS BoosterPackTM Plug-in Module User's
Guide.

#### Dependencies

This parameter appears only if you select the **Enable secondary
magnetometer** parameter.

#### Select outputs

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the
output ports.

### **Angular rate (rad/s)** — Set output port for reading angular rate `on` (default) | `off`

Select this parameter to set **Angular Rate** as one of the
output ports.

### **Magnetic Field (µT)** — Set output port for reading magnetic field `on` (default) | `off`

Select this parameter to set **Magnetic Field** as one of the
output ports.

### **Temperature (℃)** — Set output port for reading temperature `off` (default) | `on`

Select this parameter to set **Temperature** as one of the
output ports.

### **Acceleration status** — Set output port for obtaining acceleration status `off` (default) | `on`

Select this parameter to set **Acceleration Status** as one of
the output ports.

### **Angular rate status** — Set output port for obtaining angular rate status `off` (default) | `on`

Select this parameter to set **Angular Rate Status** as one of
the output ports.

### **Magnetic Field Status** — Set output port for obtaining magnetic field status `off` (default) | `on`

Select this parameter to set **Magnetic Field Status** as one
of the output ports.

### **Interrupt source** — Set output port for obtaining interrupt source status `off` (default) | `on`

Select this parameter to set **Interrupt source** as one of
the output ports.

### **Tap source** — Set output port for obtaining tap event status `off` (default) | `on`

Select this parameter to set **Tap event source** as one of
the output ports.

### **High g source** — Set output port for obtaining high g event status `off` (default) | `on`

Select this parameter to set **High g event source** as one of
the output ports.

### **Any motion source** — Set output port for obtaining any motion event status `off` (default) | `on`

Select this parameter to set **Any motion event source** as
one of the output ports.

#### Accelerometer Settings

### **Accelerometer range** — Full scale for measuring linear acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the full scale for measuring linear acceleration (the range of
acceleration that the sensor needs to measure).

### **Accelerometer output data rate** — Rate at which accelerometer data is sampled `12.5 Hz` (default) | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

Select the output data rate at which accelerometer data is sampled, which also
determines the bandwidth.

### **Enable low pass filter** — Enable low pass filter to read accelerometer data from BMI160 sensor `off` (default) | `on`

Select this option to enable the low-pass filter for the acceleration values
read from BMI160 sensor.

### **Accelerometer filter mode** — Select the filter mode for low pass filter for accelerometer values `Normal` (default) | `OSR2` | `OSR4`

Select the filter mode for low pass filter for accelerometer values. The 3dB
Cutoff frequency of the accelerometer depends on the value of this parameter and
the ODR that you selected using the **Accelerometer output data
rate** parameter.

#### Gyroscope settings

### **Gyroscope range** — Full scale for measuring angular rate `125 dps` (default) | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

Select the full scale for measuring angular rate (the range of angular rate
that the sensor needs to measure).

### **Gyroscope output data rate** — Rate at which gyroscope data is sampled `25 Hz` (default) | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz` | `3200 Hz`

Select the output data rate at which gyroscope data is sampled, which also
determines the bandwidth.

### **Enable low pass filter** — Enable low pass filter to read gyroscope data from BMI160 sensor `off` (default) | `on`

Select this option to enable the low-pass filter for the angular rate values
read from BMI160 sensor.

### **Gyroscope filter mode** — Select the filter mode for low pass filter for gyroscope values `Normal` (default) | `OSR2` | `OSR4`

Select the filter mode for low pass filter for gyroscope values. The 3dB Cutoff
frequency of the gyroscope depends on the value of this parameter and the ODR that
you selected using the **Gyroscope output data rate**
parameter.

#### Magnetometer settings

### **Magnetometer output data rate** — Rate at which magnetometer data is sampled `25 Hz` (default) | `0.78125 Hz` | `1.5625 Hz` | `3.125 Hz` | `6.25 Hz` | `12.5 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

Select the output data rate at which magnetometer data is sampled.

**Note**

Selecting one of these parameters (**Single tap**, **Double
tap**, **High g detection**, **Any
motion**, **Slow motion**, **Flat
detection**, **Data ready**) overrides the availability of
other status values at the output. The selection of parameters for other status outputs
(`Acceleration status`, `Angular rate status`, and
`Magnetic field status`) is disabled.

### **Single tap** — Enable interrupt when single tap is triggered `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when single tap is triggered and following conditions are valid.

- The tap occurs during the Shock Time threshold.
- No tap occurs during the Quiet Time threshold.

### **Quiet Time threshold** — Quiet time duration `30 ms` (default) | `20 ms`

Select the quiet time threshold for generating single tap or double tap
interrupt. The tap must not occur during the specified quiet time threshold for
generating single tap or double tap interrupt.

#### Dependencies

This parameter appears only if you select the **Single
tap** parameter or **Double tap**
parameter.

### **Shock Time threshold** — Shock time duration `50 ms` (default) | `75 ms`

Select the shock time threshold for single tap or double tap interrupt. The tap
must occur during the specified shock time threshold for generating single tap or
double tap interrupt.

#### Dependencies

This parameter appears only if you select **Single tap**
parameter or **Double tap** parameter.

### **Amplitude threshold (0.03125g - 1.96875g)** — Amplitude threshold for detecting a tap `0.1` (default)

Specify the amplitude threshold value ranging from 0.03125g - 1.96875g for
detecting a single tap or double tap. When the value crosses the specified
amplitude threshold value, a tap occurs. Amplitude threshold has minimum and
maximum range which depends on the accelerometer range.

#### Dependencies

This parameter appears only if you select the **Single
tap** parameter or **Double tap**
parameter.

### **Interrupt generate pin** — Pin to generate single tap interrupt `INT1` (default) | `INT2`

Select the pin on which the single tap interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Single
tap** parameter.

### **Double tap** — Enable interrupt when double tap is triggered `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when double tap is triggered and following conditions are valid.

- The first tap occurs during the Shock Time threshold.
- No tap occurs during the Quiet Time threshold.
- The second tap occurs during the Duration Time threshold.

### **Duration Time threshold** — Time threshold for second tap `50 ms` (default) | `100 ms` | `150 ms` | `200 ms` | `250 ms` | `375 ms` | `500 ms` | `700 ms`

Select the duration time threshold for double tap interrupt. The second tap
must occur during the specified duration time threshold for generating double tap
interrupt.

#### Dependencies

This parameter appears only if you select **Double tap**
parameter.

### **Interrupt generate pin** — Pin to generate double tap interrupt `INT1` (default) | `INT2`

Select the pin on which the double tap interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Double
tap** parameter.

### **High g detection** — Enable interrupt when high g detection is triggered `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when high g interrupt is detected.

### **Time threshold(2.5 ms to 640 ms)** — Time duration for high g detection `2.5` (default) |

Specify the time threshold value ranging from 2.5 ms to 640 ms for high g
interrupt. The high g detection must occur during the specified time threshold for
generating high g interrupt.

#### Dependencies

This parameter appears only if you select **High g
detection** parameter.

### **Amplitude threshold (0.00391g - 1.99546g)** — Amplitude threshold for detecting high g interrupt `0.1` (default)

Specify the amplitude threshold value ranging from 0.00391g - 1.99546g for
detecting a high g interrupt. When the value crosses the specified amplitude
threshold value, high g interrupt is detected. Amplitude threshold has minimum and
maximum range which depends on the accelerometer range.

#### Dependencies

This parameter appears only if you select the **High g
detection** parameter.

### **Interrupt generate pin** — Pin to generate high g interrupt `INT1` (default) | `INT2`

Select the pin on which the high g interrupt, which can be used by the STM32
Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **High g
detection** parameter.

### **Any motion** — Enable interrupt when any motion interrupt is triggered `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when any motion interrupt is detected.

### **Time threshold** — Time duration for any motion detection `1` (default) | `2` | `3` | `4`

Select the time threshold value for any motion interrupt. The any motion
detection must occur during the specified time threshold.

#### Dependencies

This parameter appears only if you select **Any motion**
parameter.

### **Amplitude threshold (0.00195g - 0.999g)** — Amplitude threshold for detecting any motion interrupt `0.1` (default)

Specify the amplitude threshold value ranging from 0.00195g - 0.999g for
detecting any motion interrupt. When the value crosses the specified amplitude
threshold value, any motion interrupt is detected. Amplitude threshold has minimum
and maximum range which depends on the accelerometer range.

#### Dependencies

This parameter appears only if you select **Any motion**
parameter.

### **Interrupt generate pin** — Pin to generate any motion interrupt `INT1` (default) | `INT2`

Select the pin on which the any motion interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Any
motion** parameter.

### **Slow motion** — Enable interrupt when slow motion interrupt is triggered `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when slow motion interrupt is detected.

### **Time threshold** — Time duration for slow motion detection `1` (default) | `2` | `3` | `4`

Select the time threshold value for slow motion interrupt. The slow motion
detection must occur during the specified time threshold.

#### Dependencies

This parameter appears only if you select **Slow motion**
parameter.

### **Amplitude threshold (0.00195g - 0.999g)** — Amplitude threshold for detecting slow motion interrupt `0.1` (default)

Specify the amplitude threshold value ranging from 0.00195g - 0.999g for
detecting slow motion interrupt. When the value crosses the specified amplitude
threshold value, slow motion interrupt is detected.

#### Dependencies

This parameter appears only if you select **Slow motion**
parameter.

### **Interrupt generate pin** — Pin to generate slow motion interrupt `INT1` (default) | `INT2`

Select the pin on which the slow motion interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Slow
motion** parameter.

### **Flat detection** — Enable interrupt when flat detection interrupt is triggered `-1` (default) | positive integer

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when flat detection interrupt is detected.

### **Theta threshold (0.7° to 44.8°)** — Theta threshold for detecting flat detection interrupt `5` (default)

Specify the amplitude threshold value ranging from 0.7° - 44.8° for detecting
flat detection interrupt. When the value crosses the specified amplitude threshold
value, flat detection interrupt is detected.

#### Dependencies

This parameter appears only if you select **Flat
detection** parameter.

### **Time threshold** — Time duration for flat detection interrupt `640` (default) | `0` | `1280` | `2560`

Select the time threshold value for flat detection interrupt. The flat
detection interrupt must occur during the specified time threshold.

#### Dependencies

This parameter appears only if you select **Flat
detection** parameter.

### **Interrupt generate pin** — Pin to generate flat detection interrupt `INT1` (default) | `INT2`

Select the pin on which the flat detection interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Flat
detection** parameter.

### **Data ready** — Enable interrupt when data is ready `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or INT2 of
the sensor when data is ready, allowing you to trigger other subsystems to perform
any action.

### **Interrupt generate pin** — Pin to generate data ready interrupt `INT1` (default) | `INT2`

Select the pin on which the data ready interrupt, which can be used by the
STM32 Processors, gets generated on the sensor.

#### Dependencies

This parameter appears only if you select the **Enable data ready
interrupt** parameter.

### **Data type** — Output data type for values from BMI160 sensor `single` (default) | `double`

Specify the output data type for the values read from BMI160 sensor. The
default data type for STM32 Processors is `single`. Use this
parameter to change the values to `double`, if required.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the BMI160 sensor. When you
set this parameter to `-1`, Simulink determines the best sample
time for the block based on the block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Measure linear acceleration, angular rate, and temperature from BMI160 sensor

The BMI160 IMU Sensor block outputs the values of linear acceleration and
angular rate along x-, y- and z- axes as measured by the BMI160 sensor connected to
STMicroelectronics® STM32 Processors. The block also outputs the temperature as read by the
BMI160 sensor. If you connect the BMM150 as a secondary sensor to BMI160, the BMI160 block
also outputs magnetic field along x-, y- and z- axes as measured by the BMM150
sensor.

The block supports Single tap, Double tap, High g detection, Any motion, Slow motion,
Flat detection, and Data ready interrupts.

Interrupt source output is a `1`-by-`7` vector with
elements corresponding to the source of single tap, double tap, high g detection, any
motion, slow motion, flat detection, and data ready interrupts respectively.
`1` indicates that it is the source, `0` indicates
that it is not a source, and `-1` indicates that the interrupt is not
active.

Tap source output is a `1`-by-`4` vector, with the
first three elements indicating whether the single tap / double tap occurred in X, Y and Z
axis, and the fourth element indicating whether it is on positive or negative direction of
the axis. High g source output is a `1`-by-`4` vector,
with the first three elements indicating whether the High g interrupt occurred in X,Y and Z
axis and the fourth element indicating whether it is on positive or negative direction of
the axis. Any motion source output is a `1`-by-`4` vector
which shows on which of the X,Y and Z axis did Any motion interrupt occur and whether it is
on positive or negative direction of the axis. First byte denotes whether the event
occurred on X axis, second byte denotes whether the event occurred on Y axis, third byte
denotes whether the event occurred on Z axis and fourth byte denotes the direction. For
direction byte `0` denotes negative side and `1` denotes
positive and for other bytes 1 denotes that axis is the source and `0`
denotes that axis is not the source.

When interrupts are enabled use external interrupt block and develop respective function
call subsystem.
