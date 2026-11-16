---
type: simulink-block
title: 'ADC Type 3-5'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Analog System'
documentation_page: 'adctype35'
documentation_source_path: 'ref/adctype35.html'
language: en
---

# ADC Type 3-5

## Ports

### Output

### **Data** — ADC data vector

The output of the ADC is a vector of `uint16` values.

**Data Types:** `uint16`

## Parameters

### SOC Trigger

### **ADC Module** — Select module to use `A` (default) | `B` | `A and B`

Select ADC Module 1 or ADC Module 2 for conversion.

Select ADC Module A through D for the processors that support Type 4 ADC.

**Note**

The **ADC Module** parameter is available only
for Texas Instruments C2000 processors that support Type 3, Type 4, or Type 5
ADC.

### **ADC Resolution** — Select 12 bit or 16 bit resolution `12-bit (Single-ended input)` (default) | `16-bit (Differential inputs)`

Select 12-bit (Single-ended input) or 16-bit (Differential inputs) ADC
resolution options.

In 12-bit mode, only single-ended input is supported. In 16-bit mode, the input
voltage to the converter is sampled through a pair of input pins, that means the
differential inputs between the two channels is converted.

**Note**

- This parameter is supported only for Texas Instruments C2000 F2837xD,
  F2838x, F2837xS, and F28p55x processors.
- The 16-bit (Differential inputs) ADC mode is not enabled by default in
  most of the processors.
- For TI F29H85x processor, you can select either 12-bit or 16-bit
  resolution for single-ended or differential ADC inputs.

### **ADC mode** — Select ADC mode `Single-ended input` (default) | `Differential inputs`

Select `Single-ended input` or `Differential
inputs` as ADC mode. This parameter is supported only for Texas
Instruments F29H85x processor.

### **Sampling mode** — Select sampling type `Single` (default) | `Simultaneous`

Type of sampling to use for the signals:

- `Single` — Samples the selected channels
  sequentially.
- `Simultaneous` — Samples the corresponding
  channels of modules 1 and 2 at the same time. The hardware allows each signal of
  a pair to be sampled at the same time.

**Note**

This parameter is supported only for Texas Instruments C2000 F28M3x
processors.

### **SOC trigger number** — Start of conversion number `SOC0` (default) | `SOC1` | `SOC2` | `…`

Identify the start-of-conversion trigger by number. In single sampling mode, you
can select an individual trigger. In simultaneous sampling mode, you can select
triggers in pairs.

### **SOCx acquisition window** — Length of the acquisition period `7` (default) | `8` | `...`

Define the length of the acquisition period in ADC clock cycles. The value of
this parameter depends on the SYSCLK and the minimum ADC sample time. The value of
SOC acquisition window is subtracted by 1 and set to ACQPS field in ADC register.
For more information, see the ADC Acquisition (Sample and Hold) Window section of
the *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter
(ADC) and Comparator Reference Guide*.

### **SOCx trigger source** — Source that triggers the start of conversion `Software` (default) | `EVA` | `External pin`

Select the source that triggers the start of conversion. The following types of
inputs are available:

- `Software`.
- `CPU Timers 0/1/2 interrupts`.
- `XINT2 SOC`.
- `ePWMx SOCA and SOCB`.

If you set **SOCx trigger source** to
`XINT2_XINT2SOC`, use the **Input5 pin
assignment** parameter at **Hardware
Implementation** > **Target hardware
resources** to define the external GPIO pin that triggers the start of
conversion.

**Note**

The SOCx trigger source input **ePWMx SOCA and
SOCB** range will vary according the processor selected.

### **ADCINT will trigger SOCx** — Use ADC interrupt to trigger SOC `No ADCINT` (default) | `ADCINT1` | `ADCINT2`

At the end of conversion, use the ADCINT1 or ADCINT2 interrupt to trigger a
start of conversion (SOC). This loop creates a continuous sequence of conversions.
The default selection, No ADCINT disables this parameter. To set the interrupt,
select the Post interrupt at EOC trigger option, and choose the appropriate
interrupt.

### **Sample time** — Interval at which block reads data `0.1` (default)

Time in seconds between consecutive sets of samples that are converted for the
selected ADC channel(s). This is the rate at which values are read from the result
registers. To execute this block asynchronously, set **Sample
Time** to `-1`, check the **Post
interrupt at the end of conversion** box.

### **Data type** — Select the output data type `uint16` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

Date type of the output data.

### **Post interrupt at EOC trigger** — Post interrupts when ADC triggers `Off` (default) | `on`

Post interrupts when the ADC triggers EOC pulses. When you select this option,
the dialog box displays the **Interrupt selection** and
**ADCINT# continuous mode** options.

**Note**

For new processors, the Interrupt selection provides option **ADCA#, ADCB#** and so on.

### **Interrupt selection** — ADC interrupt selection `ADCINT1` (default) | `ADCINT2`

Select which interrupt the ADC posts after triggering an EOC pulse.

#### Dependencies

To enable this parameter, select **Post interrupt at EOC
trigger** parameter.

### **ADC# continuous mode** — Generate ADC interrupt `ADCINT1` (default) | `ADCINT2`

When the ADC generates an end of conversion (EOC) signal, generate an ADCINT#
interrupt, whether the previous interrupt flag has been acknowledged or not.

#### Dependencies

To enable this parameter, select **Post interrupt at EOC
trigger** parameter.

### Input channels

### **Conversions channel** — Select ADC channel to which this ADC conversion applies `ADCINA0` (default) | `ADCINA1` | `ADCINA2` | `…`

Select the input channel to which this ADC conversion applies. For Type 4 ADC,
if you select 16-bit (differential inputs) mode, the differential voltage between
the two channels is converted.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Configure ADC to sample analog pins and output digital data

Configures the Type 3 to Type 5 ADC to output a constant stream of data collected from
the ADC pins on the DSP. For more information on ADC types, refer to C2000 Real-Time Control
Peripheral Reference Guide.

An ADC block allows for reading one ADC channel. Use multiple ADC blocks to read
multiple ADC channels.
