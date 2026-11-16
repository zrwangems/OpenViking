---
type: simulink-block
title: 'Analog Input'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'analoginput'
documentation_source_path: 'beaglebone/ref/analoginput.html'
language: en
---

# Analog Input

## Ports

### Output

### **Port\_1** — Voltage of analog input pin scalar

The block outputs the voltage level of an analog pin relative to the analog input
reference voltage on the BeagleBone hardware. The block outputs a voltage value between 0 (GND\_ADC) and 1.8
(VDD\_ADC). The units of the output are volts.

**Data Types:** `double`

## Parameters

### **Pin** — Analog input pin number `P9_39` (default) | `P9_40` | `P9_37` | `P9_38` | `P9_33` | `P9_36` | `P9_35`

Specify the BeagleBone board analog input pin number. To open the BeagleBone pin mapping table, click **View pin map**.

### **Sample time** — Time interval at which the blocks read input pin value `0.1` (default) | scalar

Specify how often the block measures voltage of the analog input pin, in seconds.
Enter a value greater than zero. When you specify this parameter as
`–1`, Simulink® determines the best sample time for the block based on the block context
within the model. Smaller values require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Measure voltage of analog input pin

Use the Analog Input block to measure the voltage of a BeagleBone® board analog input pin.
