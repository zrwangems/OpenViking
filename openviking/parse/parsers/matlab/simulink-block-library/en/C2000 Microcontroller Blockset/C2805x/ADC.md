---
type: simulink-block
title: 'ADC Type 1-2'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'adctype12'
documentation_source_path: 'ref/adctype12.html'
language: en
---

# ADC Type 1-2

## Ports
```yaml
ports:
- name: Data
  summary: ADC data vector
  direction: output
  data_types: uint16
```

### Output

### **Data** — ADC data vector

The output of the C281x ADC is a vector of `uint16`
values. The output values are in the range 0 to 4095 because the C281x ADC is 12-bit
converter.

**Data Types:** `uint16`
## Parameters
```yaml
parameters:
- name: Module
  summary: Select module to use A (default) | B | A and B
  group: ADC Control
- name: Conversion mode
  summary: Select conversion type Sequential (default) | Simultaneous
  group: ADC Control
- name: Start of conversion
  summary: Select start of conversion Software (default) | ePWMxA | ePWMxB | XINT1_ADCSOC
  group: ADC Control
- name: Sample time
  summary: Interval at which block reads data 0.1 (default)
  group: ADC Control
- name: Data type
  summary: Select the output data type uint16 (default) | double | single | int8 | uint8 | int16 | int32 | uint32
  group: ADC Control
- name: Post interrupt at end of conversion
  summary: Enable to post an asynchronous interrupt Off (default) | on
  group: ADC Control
- name: Use DMA (with C28x3x)
  summary: Enable to post an asynchronous interrupt Off (default) | on
  group: ADC Control
- name: 'Conversions no. #'
  summary: Select ADC channel for each conversion number ADCINA# and ADCINB# (default) | ADCINA# | …
  group: Input channels
- name: Use multiple output ports
  summary: Enable to output multiple ports on (default) | off
  group: Input channels
```

### ADC Control

### **Module** — Select module to use `A` (default) | `B` | `A and B`

Specify which DSP module to use:

- `A` — Displays the ADC channels in module A
  (ADCINA0 through ADCINA7).
- `B` — Displays the ADC channels in module B
  (ADCINB0 through ADCINB7).
- `A and B` — Displays the ADC channels in
  both modules A and B (ADCINA0 through ADCINA7 and ADCINB0 through
  ADCINB7)

### **Conversion mode** — Select conversion type `Sequential` (default) | `Simultaneous`

Type of sampling to use for the signals:

- `Sequential` — Samples the selected channels
  sequentially
- `Simultaneous` — Samples the corresponding
  channels of modules A and B at the same time

### **Start of conversion** — Select start of conversion `Software` (default) | `ePWMxA` | `ePWMxB` | `XINT1_ADCSOC`

Specify the type of signal that triggers the conversion:

Type of signal that triggers conversions to begin:

- `Software` — Signal from software.
  Conversion values are updated at each sample time.
- `ePWM#A` / `ePWM#B` /
  `ePWM#A_ePWM#B` — Start of conversion is
  controlled by user-defined PWM events.
- `XINT2_ADCSOC` — Start of conversion is
  controlled by the `XINT2_ADCSOC` external signal pin.

The choices available in **Start of
conversion** depend on the
**Module** setting. The following table summarizes the available
choices. For each set of **Start of
conversion** choices, the default is given
first.

| Module Setting | Start of Conversion Choices |
| --- | --- |
| `A` | `Software`, `ePWM#A`, `XINT2_ADCSOC` |
| `B` | `ePWM#B`, `Software` |
| `A and B` | `Software`, `ePWM#A`, `ePWM#B`, `ePWM#A_ePWM#B`, `XINT2_ADCSOC` |

### **Sample time** — Interval at which block reads data `0.1` (default)

Time in seconds between consecutive sets of samples that are converted for the
selected ADC channel(s). This is the rate at which values are read from the result
registers. To execute this block asynchronously, set **Sample
Time** to `-1`, check the **Post
interrupt at the end of conversion** box.

To set different sample times for different groups of ADC channels, you must add
separate C281x ADC blocks to your model and set the desired sample times for each
block.

### **Data type** — Select the output data type `uint16` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

Date type of the output data.

### **Post interrupt at end of conversion** — Enable to post an asynchronous interrupt `Off` (default) | `on`

Enable this check box to post an asynchronous interrupt at the end of each
conversion. The interrupt is posted at the end of conversion.

To execute this block asynchronously, set **Sample
Time** to `-1`.

### **Use DMA (with C28x3x)** — Enable to post an asynchronous interrupt `Off` (default) | `on`

Enable this check box to post an asynchronous interrupt at the end of each
conversion. The interrupt is posted at the end of conversion.

To execute this block asynchronously, set **Sample
Time** to `-1`.

### Input channels

### **Conversions no. #** — Select ADC channel for each conversion number `ADCINA# and ADCINB#` (default) | `ADCINA#` | `…`

Specific ADC channel to associate with each conversion number.

In oversampling mode, a signal at a given ADC channel can be sampled multiple
times during a single conversion sequence. To oversample, specify the same channel
for more than one conversion. Converted samples are output as a single vector.

### **Use multiple output ports** — Enable to output multiple ports `on` (default) | `off`

If more than one ADC channel is used for conversion, you can use separate ports
for each output and show the output ports on the block. If you use more than one
channel and do not use multiple output ports, the data is output in a single
vector.
## Libraries

C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Analog-to-digital converter (ADC)

The ADC block configures the ADC to perform analog-to-digital conversion of
signals connected to the selected ADC input pins. The ADC block outputs digital values
representing the analog input signal and stores the converted values in the result register
of your digital signal processor. You use this block to capture and digitize analog signals
from external sources such as signal generators, frequency generators, or audio devices.
With the C2833x, you can configure the ADC to use the processor DMA module to move data
directly to memory without using the CPU. This frees the CPU to perform other tasks and
increases overall system capacity.
