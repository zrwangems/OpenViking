---
type: simulink-block
title: 'F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x DAC'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Analog System'
documentation_page: 'c28xdac'
documentation_source_path: 'ref/c28xdac.html'
language: en
---

# F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x DAC

## Ports

### Input

### **Port\_1** — Input signal `real` | `scalar`

The input port through which the block accepts the digital input value to convert
it to analog signal.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `double`

## Parameters

### **DAC channel** — The DAC channel to generate analog output `12` (default)

Enter the DAC channel on which to generate the analog signal. The DAC channels that
you can select are A, B, or C.

### **Saturate on input overflow (>4095)** — The option to saturate the input value on input overflow `off` | `on`

Select this check box to saturate the input value to 4095 when there is an input
value is higher than 4095.

#### Compatibility Considerations

Earlier to R2021b, when **Saturate on input overflow (>4095)**
parameter is deselected, an input value to the DAC greater than
`65536` results the output to saturate at `65535`.
Starting R2021b, the output wraps around i.e., for an input of
`65580`, results in output `44
(65580-65536)`.

## Libraries

C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Configures the DAC to generate an analog output on the specified DAC channel A/B/C (12-bit)

Generate an analog output on the specified DAC channel A, B, or C for
F2837x/F2807x/F28004x and F2838x/C28x processors. The block accepts a 12–bit value as an input
in the range 0 to 4095. You can saturate a value higher than 4095 to 4095 with the
**Saturate on input outflow** option.

The output pins of this block are multiplexed with the ADC block input. When you use a DAC
block in your model, the corresponding channels of the ADC cannot be used as input. If used,
the ADC samples the DAC output.

The pins that are shared between ADC and DAC are DACOUTA/ADCINA0, DACOUTB/ADCINA1, and
DACOUTC/ADCINB1. The input to the DAC block can be double, float, int, and uint. The block
typecasts the input to uint16.
