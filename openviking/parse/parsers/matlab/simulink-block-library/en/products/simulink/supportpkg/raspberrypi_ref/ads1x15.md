---
type: simulink-block
title: 'ADS1x15'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'ads1x15'
documentation_source_path: 'supportpkg/raspberrypi_ref/ads1x15.html'
language: en
---

# ADS1x15

## Ports

### Output

### **data** — ADC digital data scalar

The block outputs the converted digital data of analog channel. For ADS1015
converter, the digital output values are in the range 0 to 4095 while, for ADS1115
converter, the digital output values are in the range 0 to 65535.

**Data Types:** `int16`

## Parameters

### Basic

### **ADC chip** — ADC converter IC `ADS1015` (default) | `ADS1115`

Select an ADC converter integrated circuit (IC) for performing analog to digital
conversion. The ADS1015 IC is a 12-bit ADC while, the ADS1115 IC is a 16-bit
ADC.

### **I2C address** — I2C address for ADS1x15 IC `0x48` (default) | `0x49` | `0x4A` | `0x4B`

Select the I2C address for ADS1x15 ADC for communicating with the Raspberry Pi board. The ADS1x15 ADC can have four I2C addresses depending on the
logic level on pins SCL and SDA.

| I2C Address | ADC Address Pin |
| --- | --- |
| 0x48 | GND |
| 0x49 | VIN |
| 0x4A | SDA |
| 0x4B | SCL |

### **Conversion mode** — ADC conversion mode `Single-shot` (default) | `Continuous`

- `Single-shot` — In this mode, the ADC performs only
  one analog-to-digital conversion at the specified sample time and writes to the
  ADC result data registers.
- `Continuous` — In this mode, the analog input is
  continually converted to its digital equivalent and written to the ADC result
  data registers.

### **Input channel** — Analog input channel of ADC converter `A0 - A1 (Differential)` (default) | `A0 - A3 (Differential)` | `A1 - A3 (Differential)` | `A2 - A3 (Differential)` | `A0 - GND (Single-ended)` | `A1 - GND (Single-ended)` | `A2 - GND (Single-ended)` | `A3 - GND (Single-ended)`

Select the analog input channel of the ADC converter.

- `A0 - A1 (Differential)` — Measure the voltage
  difference between A0 and A1 input channels of the sensor.
- `A0 - A3 (Differential)` — Measure the voltage
  difference between A0 and A3 input channels of the sensor.
- `A1 - A3 (Differential)` — Measure the voltage
  difference between A1 and A3 input channels of the sensor.
- `A2 - A3 (Differential)` — Measure the voltage
  difference between A2 and A3 input channels of the sensor.
- `A0 - GND (Single-ended)` — Measure analog voltage
  on A0 input channel with respect to the GND pin of the sensor.
- `A1 - GND (Single-ended)` — Measure analog voltage
  on A1 input channel with respect to the GND pin of the sensor.
- `A2 - GND (Single-ended)` — Measure analog voltage
  on A2 input channel with respect to the GND pin of the sensor.
- `A3 - GND (Single-ended)` — Measure analog voltage
  on A3 input channel with respect to the GND pin of the sensor.

### **Gain** — Amplify input analog signal `+/-2.048V` (default) | `+/-6.144V` | `+/-4.096V` | `+/-1.024V` | `+/-0.512V` | `+/-0.256V`

Select the gain of the ADC converter to amplify the weak input analog
signal.

### **Data rate** — Data conversion rate `1600SPS` (default) | `128SPS` | `250SPS` | `490SPS` | `920SPS` | `2400SPS` | `3300SPS`

Select the analog-to-digital conversion rate of the ADC converter in samples per
second (SPS).

### **Sample time** — Interval at which block reads data `0.01` (default) | scalar

Enter the time in seconds between consecutive sets of samples that are converted
for the selected input channel. This is the rate at which values are read from the
result registers.

### Advanced

### **Enable comparator** — Enable advanced ADC options `off` (default) | `on`

Select this option to enable advanced functions useful for ADC
applications.

### **Mode** — ADC comparator mode `Traditional with hysteresis` (default) | `Window`

Select the comparator mode of operation for ALERT pin on ADC chip.

- `Traditional with hysteresis` — In this mode, the
  ALERT pin on the ADC chip asserts when conversion data exceeds the limit set in
  the high threshold register. The comparator then de-asserts when the input
  signal falls below the low threshold register value.
- `Window` — In this mode, the ALERT pin asserts is
  the conversion data exceeds the high threshold register or falls below the low
  threshold register.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

### **Polarity configuration** — ADC comparator polarity configuration `Active low` (default) | `Active high`

Select the comparator polarity for the ALERT pin on ADC chip.

- `Active low` — Assert on the ALERT pin of the ADC
  chip on the falling edge of the digital output signal.
- `Active high` — Assert on the ALERT pin of the ADC
  chip on the rising edge of the digital output signal.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

### **Latching configuration** — ADC comparator latching configuration `Non-latching` (default) | `Latching`

Select the latching configuration of the ALERT pin on the ADC chip.

- `Non-latching` — Select this option to clear away
  the assertion on the ALERT ping of the ADC chip when the input analog signal is
  not beyond the low and high threshold values.
- `Latching` — Select this option for the assertion
  to continue on the ALERT pin of the ADC chip even if the input analog signal is
  not beyond the low and high threshold values.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

### **Queue configuration** — Queue configuration before asserting ALERT pin of ADC chip `Assert after 1 conversion` (default) | `Assert after 2 conversions` | `Assert after 4 conversions`

Select the option to control the number of successive conversions exceeding the
upper or lower thresholds required before asserting the ALERT pin of the ADC
chip.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

### **Low threshold** — Low threshold for queue configuration `0` (default) | scalar

Enter the lower threshold value for queue configuration before asserting the ALERT
pin of the ADC chip.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

### **High threshold** — High threshold for queue configuration `0` (default) | scalar

Enter the higher threshold value for queue configuration before asserting the
ALERT pin of the ADC chip.

#### Dependencies

- To enable this parameter, select **Enable
  comparator**.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Read digital output data from ADS1015 and ADS1115 ADCs

Use the ADS1x15 analog-to-digital converter block to perform
analog-to-digital conversion of signals connected to the selected ADC input pins. The block
outputs digital values representing the analog input signal and stores the converted values in
the result register of your digital signal processor. You use this block to capture and
digitize analog signals from external sources such as signal generators, frequency generators,
or audio devices. With the ADS1x15 block, you can configure for ADS1015 and
ADS1115 converter, that provides a 12-bit and 16-bit precision digital output, respectively.

### Hardware Connections

When you select A0 - A1 as the differential input channel for the ADS1x15 sensor, use
the following table to set up the connections between a Raspberry Pi® board, ADS1x15 sensor, and an analog source device. For any other input
channels that you select, make the hardware connections accordingly.

| Raspberry Pi | ADS1x15 Sensor | Device |
| --- | --- | --- |
| VCC | VCC |  |
| GPIO 2 | SDA |
| GPIO 3 | SCL |
| GND | GND | GND |
|  | A0 | Sig + |
| A1 | Sig - |
