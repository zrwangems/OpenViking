---
type: simulink-block
title: 'Waveform From Wireless Waveform Generator App'
family: 'wlan'
product_id: 'wlan'
product_name: 'WLAN Toolbox'
documentation_release: R2025b
official_category: 'Test and Measurement'
documentation_page: 'waveformfromwirelesswaveformgeneratorapp'
documentation_source_path: 'ref/waveformfromwirelesswaveformgeneratorapp.html'
language: en
---

# Waveform From Wireless Waveform Generator App

## Ports

### Output

### **wf** — Time-domain wireless waveform complex matrix

Time-domain wireless waveform, returned as a complex matrix. The number of matrix
columns corresponds to the number of transmit antennas. The waveform type you select
in the app determines the output waveform type. To access waveform configuration
parameters, use the `WaveformConfig` structure field of the
`UserData` common block property.

**Data Types:** `double`
**Complex Number Support:** Yes

## Parameters

### Read-Only Waveform Parameters

The block automatically updates these parameters based on the waveform configuration in
the **Code** tab.

### **Waveform sample rate (Fs)** — Waveform sample rate numeric scalar

This parameter is read-only.

To access this parameter, use the `Fs` structure field of the
`UserData` common block property. Units of the
`Fs` structure field are in Hz.

### **Waveform length** — Waveform length positive integer

This parameter is read-only.

To access this parameter, use the `WaveformLength` structure
field of the `UserData` common block property. Units of the
`WaveformLength` structure field are in samples.

### Simulation Parameters

These parameters control how the block outputs the waveform during simulation.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

This parameter specifies the number of samples to buffer into each output
frame.

### **Form output after final data value by** — Output values after last waveform sample `Cyclic repetition` (default) | `Setting to zero`

This parameter specifies the output values after the block has output all
available waveform samples.

- When you select `Cyclic Repetition`, the block
  repeats the waveform from the beginning after reaching the last sample in the
  waveform.
- When you select `Setting To Zero`, the block
  generates zero-valued outputs for the duration of the simulation after generating
  the last frame of the waveform.

## Libraries

None

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Wireless waveform source exported to Simulink

The Waveform From Wireless Waveform Generator App block is generated using the Wireless Waveform
Generator app. You can use the generated block as a wireless waveform source in a
Simulink® model.

**Note**

The actual block name and output waveform depend on the waveform that you configure in
the app before generating the block.

For
an overview of the waveform types that you can export to Simulink using the WLAN Toolbox™ software, see the WLAN Waveform Generator
app.

To generate a block:

1. On the app toolstrip, in the **Waveform Type** section,
   click the waveform that you want to configure and export to Simulink.
2. Set the parameters of the selected waveform.
3. On the app toolstrip, in the **Export** section, click
   **Export** and select **Export to
   Simulink**.

The **Code** tab of the Mask Editor window contains the
MATLAB® code that the block executes to output the configured waveform. To access
read-only block parameters and waveform configuration parameters, use the
`UserData` common block property, which is a structure with these fields.

- `WaveformConfig` — Waveform configuration parameters
- `WaveformLength` — Waveform length
- `Fs` — Waveform sample rate

For more information on how to use the generated block, see
Generate Wireless Waveform in Simulink Using App-Generated Block.
