---
type: simulink-block
title: 'Analog Input SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/analoginputadvancedsamd.html'
language: en
---

# Analog Input SAMD

## Ports

### Output

### **ADC\_Ch1(A0)** — ADC output data scalar

The block outputs the digitally converted voltage data that is received on the
analog input pin of the Arduino board. The number of output ports depends on the number of analog input
pins you specify in the **Number of analog input pins** parameter.
For example, if you set the **Number of analog input pins** parameter
to `3`, the block enables three output ports with port names
**ADC\_Ch1(A0)**, **ADC\_Ch2(A1)**, and
**ADC\_Ch3(A2)**.

**Data Types:** `double`

## Parameters

### **Number of analog input pins** — Select number of analog inputs `1` (default) | `2` | `3`

Select the number of inputs for analog to digital conversion.

### **Pin number 1** — Arduino pin number `0` (default) | Arduino board pin number

Enter the Arduino board analog input pin number. To open the Arduino pin mapping table, click **View pin map**. To know how
to assign pins for the Analog Input block, see Pin Mapping for Arduino Timer-Independent Blocks.

The number of **Pin Number** parameters depends on the number of
analog input pins you specify in the **Number of analog input pins**
parameter. For example, if you set the **Number of analog input pins**
parameter to `3`, the block enables the **Pin number
2** and **Pin number 3** parameters. You can enter the
analog pin numbers for the Arduino board accordingly.

### **Enable end of conversion interrupt** — Enable interrupt after ADC conversion is complete `on` (default) | `off`

Select this option to generate an interrupt after the analog voltage at the pin of
the Arduino hardware is converted to its equivalent digital voltage.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Read ADC register value after ADC conversion at the analog pin of Arduino SAMD21 core

Use the Analog Input block to read the value from an ADC register after
analog to digital conversion on the Arduino® SAMD21 analog pin. You can use the block to read up to three analog voltage
outputs simultaneously.

Use the block inside a downstream function call subsystem that executes the ADC conversion
operation based on an interrupt service routine (ISR) trigger. You specify the ISR trigger
using a Hardware Interrupt block.

**Note**

The Analog Input block supports C/C++ code generation. This feature
allows you to generate C and C++ code using Embedded Coder®.

### Supported Arduino Boards

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
