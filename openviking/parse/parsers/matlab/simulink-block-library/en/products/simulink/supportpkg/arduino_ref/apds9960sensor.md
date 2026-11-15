---
type: simulink-block
title: 'APDS9960 Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Proximity Sensors'
documentation_page: 'apds9960sensor'
documentation_source_path: 'supportpkg/arduino_ref/apds9960sensor.html'
language: en
---

# APDS9960 Sensor

## Ports

### Output

**Proximity**

### **Proximity** — Proximity data positive scalar in the range [`0`, `255`]

The block outputs the proximity data as a positive scalar in the range
[`0`, `255`], where `0`
represents an object that is farthest from the sensor and `255`
represents an object that is closest to the sensor.

#### Dependencies

To enable this port:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

**Data Types:** `uint8`

**Gesture**

### **GFIFO\_U** — Gesture data detected in upward direction vector

The block outputs the data for gestures in the upward direction detected by the
sensor as a `1`-by-*N* vector, where
*N* is the threshold for number of gestures in the upward
direction.

#### Dependencies

To enable this port:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint8`

### **GFIFO\_D** — Gesture data detected in downward direction vector

The block outputs the data for gestures in the downward direction detected by the
sensor as a `1`-by-*N* vector, where
*N* is the threshold for number of gestures in the downward
direction.

#### Dependencies

To enable this port:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint8`

### **GFIFO\_L** — Gesture data detected towards left vector

The block outputs the data for gestures detected by the sensor towards the left as
a `1`-by-*N* vector, where *N* is
the threshold for number of gestures towards the left.

#### Dependencies

To enable this port:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint8`

### **GFIFO\_R** — Gesture data detected towards right vector

The block outputs the data for gestures detected by the sensor towards the right
as a `1`-by-*N* vector, where *N*
is the threshold for number of gestures towards the right.

#### Dependencies

To enable this port:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint8`

**Ambient light and Color**

### **Ambient** — Ambient light data positive scalar in the range [`0`, `65535`]

The block outputs the ambient light intensity data as a positive scalar in the
range [`0`, `65535`], where `0`
represents the lowest ambient light intensity and `65535` represents
the highest ambient light intensity.

#### Dependencies

To enable this port:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint16`

### **RGB** — Color intensity data vector

The block outputs the color light intensity data as a 3-by-1 vector.

#### Dependencies

To enable this port:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Data Types:** `uint16`

**Status**

### **Status** — Availability of new data at output port scalar

The block outputs the status of new data availability depending on the Sensor mode that you select, as either a scalar or as a
`1`-by-`2` vector of values `0`
and `1`.

- `0`: Indicates that there is no new data available at the
  output port of the sensor since the last read cycle.
- `1`: Indicates that there is new data available at the
  output port of the sensor since the last read cycle.

For example, if you select the Sensor mode as `Proximity`, the block outputs a scalar
value at the port. Similarly, if you select the Sensor mode as `Proximity, Ambient light and Color`,
the block outputs a `1`-by-`2` vector, where, the
first element corresponds to the `Proximity` sensor mode and
the later element corresponds to the `Ambient light and
Color`sensor mode.

This table lists the status output available at the output port depending on the
Sensor mode you select.

| Sensor Mode | Status Port Outputs |
| --- | --- |
| `Proximity` | Proximity |
| `Gesture` | Gesture |
| `Ambient light and Color` | Ambient light and Color |
| `Proximity, Ambient light and Color` | - Proximity - Ambient light and Color |
| `Gesture, Ambient light and Color` | - Gesture - Ambient light and Color |

#### Dependencies

To enable this port, select **Enable status output**.

**Data Types:** `uint8`

## Parameters

Every APDS9960 IMU Sensor mode has
both Basic and Advanced parameters. You can
configure the parameters in both the tabs of the **Block Parameters** dialog
box for every sensor mode you select to suit your requirement and functional area.

For example, if you select the Sensor mode as
`Proximity, Ambient light and Color`, both the Basic and Advanced tabs of the
**Block Parameters** dialog box will contain the parameters that are
applicable for both the `Proximity, Ambient light and Color` sensor
mode. You can configure the parameters in both the tabs.

### Basic

**Common**

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Sensor mode** — Type of sensor mode `Proximity` (default) | `Gesture` | `Ambient light and Color` | `Proximity, Ambient light and Color` | `Gesture, Ambient light and Color`

Select the operating mode of the sensor.

### **Data acquisition mode** — Data acquisition mode `Polling` (default) | `Interrupt`

Select the data acquisition mode.

**Note**

In the `Gesture` mode, the sensor can acquire data in
the `Interrupt` mode only, with a new gesture input
acting as a source of interrupt.

### **Enable status output** — Availability of data at output port off (default) | on

Select the parameter to enable the Status output
port.

### **Sample time** — Interval at which block reads data `0.1` (default) | scalar

Enter the time interval in seconds at which the block reads values from the
APDS9960 IMU sensor.

**Proximity**

### **Interrupt thresholds [low, high]** — Proximity thresholds to generate interrupt `[0, 50]` (default) | 1-by-2 vector in the range `[0, 255]`

Generate an interrupt when the proximity value exceeds above or falls below the
high and low interrupt threshold levels, respectively.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity` and **Data acquisition
  mode** to `Interrupt`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color` and **Data acquisition mode**
  to `Interrupt`.

### **Interrupt persistence** — Control rate of proximity interrupts `2` (default) | positive integer

Assert proximity interrupts only if consecutive proximity values are outside the
range specified in the Interrupt thresholds [low, high] parameter. This prevents the block from generating
false interrupts. Use this parameter to specify after how many consecutive proximity
values outside the interrupt threshold should the block generate a proximity
interrupt. For example, when you set this parameter to `2`, the block
generates an interrupt when two consecutive proximity values are outside the range you
set in the Interrupt thresholds [low, high] parameter.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity` and **Data acquisition
  mode** to`Interrupt`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color` and **Data acquisition mode**
  to `Interrupt`.

**Gesture**

### **Enter and exit thresholds [enter, exit]** — Gesture thresholds to generate interrupt `[40, 30]` (default) | 1-by-2 vector in the range `[0, 255]`

Set the threshold values to determine the start and end points of a
gesture.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

### **FIFO threshold for interrupt** — Gesture FIFO threshold `4 datasets` (default) | `1 dataset` | `8 datasets` | `16 datasets`

Generate a gesture interrupt after the value selected in this parameter is equal
to the number of data set available in the FIFO. For example, if you set this
parameter is set to `4 datasets`, the block generates a
gesture interrupt after four data sets are available in the FIFO.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

### **Exit persistence** — Control rate of gesture exits `1st gesture end` (default) | `2nd gesture end` | `4th gesture end` | `7th gesture end`

Assert gesture interrupts only if consecutive gesture values are outside the range
specified in the Enter and exit thresholds [enter, exit] parameter. This prevents the block from
generating false interrupts. Use this parameter to specify after how many consecutive
gesture values outside the interrupt threshold should the block generate a gesture
interrupt. For example, when you select `4th gesture end`,
the block generates an interrupt after four consecutive gesture values are outside the
range you set in the Enter and exit thresholds [enter, exit] parameter.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient
  light and Color`.

**Ambient light and Color**

### **Interrupt thresholds [low, high]** — Ambient light threshold to generate interrupt `[65535, 0]` (default) | 1-by-2 vector in the range `[0, 65535]`

Generate an interrupt when the ambient light and color intensity data exceeds or
falls below the high and low interrupt threshold levels, respectively.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color` and **Data acquisition mode** to
  `Interrupt`.
- Set **Sensor mode** to`Proximity, Ambient
  light and Color` and **Data acquisition mode**
  to `Interrupt`, and **Interrupt
  source** to `Ambient light and
  Color`.

### **Interrupt persistence** — Control rate of ambient light and color interrupts `2` (default) | positive scalar

Assert ambient light and color interrupts to the sensor only if the consecutive
out of Interrupt thresholds [low, high] values is equal to or greater than the value set
in this parameter. This prevents the block from generating false interrupts. For
example, when you set this parameter to `2`, the block generates an
interrupt when two consecutive ambient light and color values are outside the range
you set in the Interrupt thresholds [low, high] parameter.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color` and **Data acquisition mode** to
  `Interrupt`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color` and **Data acquisition mode**
  to `Interrupt`, and **Interrupt
  source** as `Ambient light and
  Color`.

**Proximity, Ambient light and Color**

### **Interrupt source** — Source of interrupt `Proximity` (default) | `Ambient light and Color`

Select the source of interrupt for the sensor.

#### Dependencies

To enable this parameter, set **Sensor mode** to
`Proximity, Ambient light and Color`, and **Data
acquisition mode** to `Interrupt`.

### Advanced

**Proximity**

### **Gain** — Proximity gain control `4x` (default) | `1x` | `2x` | `8x`

Select gain for the proximity data value.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

### **Pulse length** — Time period of each proximity pulse length `16 μs` (default) | `4 μs` | `8 μs` | `32 μs`

Select the ON time of each pulse in the IR LED emitted pulse train.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

### **Pulse count** — Number of proximity pulses generated by LDR `8` (default) | positive scalar in the range [`1` to `64`]

Specify the number of pulses that the light-dependent resistor (LDR) should
generate. The number of pulses that the LDR generates is the pulse count value plus
one. For example, if you set the pulse count value to `8`, the LDR
generates nine pulses.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

### **Offsets [UR, DL]** — Proximity offsets for up-right and down-left photodiodes `[0, 0]` (default) | 1-by-2 vector in the range `[255, 255]`

Set a scalable internal offset correction factor for the up-right and down-left
photodiode pairs.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

**Proximity, Ambient light and Color**

### **LED drive strength** — Control intensity of LED IR emission `100 mA` (default) | `50 mA` | `25 mA` | `12.5 mA`

Select current levels for the LED IR emission to control the intensity
levels.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

**Proximity and Gesture**

### **LED boost current** — Additional intensity boost for LED IR emission `100%` (default) | `150%` | `200%` | `300%`

Specify additional current boost levels for the LED IR emission to detect
long-range devices.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Proximity`.
- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.

**Gesture**

### **Offsets [U, D, L, R]** — Gesture offsets for up, down, left, and right photodiodes `[0, 0, 0, 0]` (default) | 1-by-4 vector `[255, 255, 255, 255]`

Set a scalable internal offset correction factor for the up, down, left, and right
photodiodes.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **LED drive strength** — Control intensity of LED IR emission `100 mA` (default) | `50 mA` | `25 mA` | `12.5 mA`

Select current levels for the LED IR emission to control the intensity
levels.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **Gain** — Gesture gain control `4x` (default) | `1x` | `2x` | `8x`

Select gain for the gesture data value.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **Pulse length** — Time period of each gesture pulse length `32 μs` (default) | `4 μs` | `8 μs` | `16 μs`

Select the ON time of each pulse in the IR LED emitted pulse train.

#### Dependencies

To enable this parameter,

- Set **Sensor mode** as
  `Gesture`.
- Set **Sensor mode** as `Gesture, Ambient light
  and Color`.

### **Pulse count** — Number of gesture pulses generated by LDR `10` (default) | positive scalar

Specify the number of pulses that the light-dependent resister (LDR) should
generate. The number of pulses that the LDR generates is the pulse count value plus
one. For example, if you set the pulse count value `10`, the LDR
generates `11` pulses.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **Wait time** — Time between gesture detection cycles `2.8 ms` (default) | `0 ms` | `5.6 ms` | `8.4 ms` | `14 ms` | `22.4 ms` | `30.8 ms` | `39.2 ms`

Delay pulse train repetition by selecting a gesture waiting time. This parameter
controls the amount of time the sensor spends in a low-power mode between the gesture
detection cycles. Include a wait time to reduce power consumption by the sensor and to
make data acquisition more efficient.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to
  `Gesture`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

**Ambient light and Color**

### **Gain** — Ambient light and color gain control `4x` (default) | `1x` | `16x` | `64x`

Select gain for the ambient light and color data value.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **ADC integration time (ms)** — Control integration time of ambient light and color analog to digital converters `219` (default) | positive scalar

Use this parameter to specify the time for data from the color and ambient light
photodiodes to accumulate.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **Enable wait before Ambient light sensing** — Activate wait feature before the sensor starts reading ambient light and color off (default) | on

Activate wait feature before the sensor begins reading ambient light and
color.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

### **Wait time (ms)** — Waiting time before sensor starts reading ambient light and color `246` (default) | positive scalar

Enter the wait time before the sensor begins reading ambient light and
color.

#### Dependencies

To enable this parameter, select **Enable wait before Ambient light
sensing**.

### **Enable wait long (12x)** — Increase wait time by 12x off (default) | on

Enable the parameter to increase the wait time set in the Wait time (ms) parameter by a factor of 12x.

#### Dependencies

To enable this parameter:

- Set **Sensor mode** to `Ambient light and
  Color`.
- Set **Sensor mode** to `Proximity, Ambient
  light and Color`.
- Set **Sensor mode** to `Gesture, Ambient light
  and Color`.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Read proximity, gesture, ambient light, and RGB color data from APDS9960 I2C sensor

The APDS9960 Sensor block detects proximity, provides directional data to
decode gesture, and measures ambient and color (RGB) values from the APDS9960 sensor
interfaced with Arduino® hardware with interrupt driven I2C communication. You can acquire data from the
APDS9960 I2C sensor using either the polling or the interrupt mode.

**Note**

For the `Interrupt` data acquisition mode, place the block in
the function call subsystem of the External
Interrupt block.

**Note**

If you are using Arduino Nano 33 BLE Sense hardware, which always includes an embedded
sensor, reading data from a breakout board containing APDS9960 sensor is not supported.
