---
type: simulink-block
title: 'ADC Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Other'
documentation_page: 'adcinterface'
documentation_source_path: 'ref/adcinterface.html'
language: en
---

# ADC Interface

## Ports

### Input

### **start** — Start analog to digital conversion start an analog to digital conversion event

Specify an event signal to start the sampling and measurement of the
**analog** input port signal.

**Data Types:** `rteEvent`

### **analog** — Analog voltage signal scalar

Input analog voltage signal to convert into a digital measurement.

**Data Types:** `double` | `single`
### Output

### **digital** — SoC message data scalar

This port sends the ADC Interface input signal data as a message to
the **msg** input port of the ADC Read block.

**Data Types:** `SoCData`

### **wd event** — Analog watchdog task event signal scalar

This port sends a message at whenever the analog voltage signal exceeds the
specified **Lower threshold** and **Upper
threshold** property values. This output connects to the input of the Task
Manager block to execute the associated event-driven task to react to the over- or
under-voltage input event.

#### Dependencies

To enable this port, enable the **Enable analog watchdog**
parameter.

**Data Types:** `rteEvent`

### **event** — Task event signal scalar

This port sends a message at each analog to digital signal conversion event. This
output connects to the input of the Task Manager block to execute the associated
event-driven task after executing the ADC event.

#### Dependencies

To enable this port, enable the  **Enable interrupt**
parameter.

**Data Types:** `rteEvent`

## Parameters

### Single Channel

### **Resolution (bits)** — Resolution of digital measurement `12` (default) | `16`

An input analog signal can be represented in digital values in the form of 12 or
16 bits. The minimum value of an analog signal that can be represented in 1 bit is
called *resolution*. One bit represents the minimum voltage
resolution measurable by the ADC. The minimum voltage resolution can be determined
using the following equation:

where `n` is the **Resolution
(bits)** and `Vref` is the **Voltage reference
(V)** parameter values.

**Example:** `16`

### **Voltage reference (V)** — Reference voltage in ADC `3` (default) | `3.3`

The reference voltage determines the total voltage range that the ADC can convert
into a digital value without saturating. Any voltage signal higher than this value
produces the maximum possible value that can represented by the **Resolution
(bits)** parameter.

**Example:** `3.3`

### **Acquisition time (s)** — Time required for ADC to capture input voltage `320e-9` (default) | positive scalar

Specify the time required for the ADC to capture the input voltage during
sampling.

**Example:** `200e-9`

### **Conversion time (s)** — Time to convert physical voltage sample to digital value `240e-9` (default) | positive scalar

Specify the required time to convert the physical voltage sample to the digital
representation and output the value.

**Example:** `20e-9`

### **Charge/dischard time constant (s)** — Charge or discharge time constant of the ADC acquisition circuit `0` (default) | nonnegative scalar

Specify the charge or discharge time constant of the ADC sample acquisition
circuitry.

### Multichannel

### **Number of channel** — Number of channels used in multichannel sampling `1` (default) | integer in the range 1 to 16

Specify the number of channels used by the ADC module. Specifying 2 or more
channels allows for either more efficient or precise measurements of the input
signal.

### **Conversion type** — Type multichannel conversion `Sequential` (default) | `Simultaneous` | `Oversampling`

Select the type of multichannel conversion.

- `Sequential` — Take sequential measurements on each
  ADC channel. At a new ADC event, the next channel in the sequence of channels
  takes a new measurement of the input signal. All other previous channel values
  remain unchanged. Sequential measurement improves sampling by allowing for
  individual conversion times of each channel to exceed the sample rate of the ADC
  module.
- `Simultaneous` — Take simultaneous measurements on
  each ADC channel. At a new ADC event, all channels take a new measurement of the
  input signal, replacing the previously captured value. Simultaneous measurement
  allows for noise to be removed from the measurement using an average value or
  other filter.
- `Oversampling` — Take oversampled measurements across
  the channels of the ADC. Between two timer-driven ADC events, each channel takes a
  time offset ADC measurement, resulting in the channels sampling the input signal
  evenly between the two ADC events. The resulting channel output provides an
  oversampled measurement of the input signal at each sample. Oversampling
  measurement allows for the ADC module to exceed the theoretical Nyquist sample
  rate of the individual channel and ADC hardware.

### Event

### **Enable interrupt** — Option to enable interrupt event generation enable (default) | disable

Select this parameter for the ADC Interface block to generate an interrupt
following an ADC acquisition and to enable the **event** output port.
You can connect this **event** port to a Task Manager block to
simulate asynchronous ADC operation.

### **Condition** — Condition on when to trigger interrupt `Acquisition time` (default) | `Acquisition + Conversion time`

Select the timing condition for when to generate the ADC interrupt event. Using
`Acquisition + Conversion time`, the interrupt is generated
when the complete measurement is available. Using `Acquisition
time`, the interrupt is generated prior to the measurements
availability. Allowing for the associated task to start during the conversion and
reduce execution delay in the total measurement cycle.

### **Enable analog watchdog** — Option to enable analog watchdog interrupt event generation off (default) | on

Select this parameter for the ADC Interface block to generate an analog watchdog
interrupt following an ADC acquisition where the input voltage exceeds the specified
**Lower threshold** and **Upper threshold**
parameter values. Selecting this parameter also enables the **wd
event** output port, which you can connect to a Task Manager block to
simulate task action on an over-or under-voltage event on the ADC input signal.

### **Lower threshold** — Lower threshold watchdog trigger `0.1` (default) | real-valued scalar

Specify the lower threshold value of the analog input signal on which to trigger
an analog watchdog interrupt event.

**Example:** `0.2`

### **Upper threshold** — Upper threshold watchdog trigger `2.9` (default) | real-valued scalar

Specify the upper threshold value of the analog input signal on which to trigger
an analog watchdog interrupt event.

**Example:** `3.0`

### **Interrupt latency (s)** — Interrupt generation latency `0` (default) | positive scalar

Specify the time required by the ADC hardware module from the completion of the
conversion to the generation of the interrupt in software.

**Example:** `0.00001`

## Libraries

SoC Blockset / Peripherals C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

## Version History

**Introduced in R2020b**

## Description

Convert analog signal on ADC input pin to digital signal

The ADC Interface block simulates the analog-to-digital conversion (ADC) of
a hardware board. The input analog signal gets sampled and converted into a representative
digital value. A start event message signals the block to sample the input analog voltage
signal. When the conversion completes, the block emits the digital representation of the
analog signal and sends an event to a Task Manager block. At this point, a connected task can
execute with the new ADC sample.
