---
type: simulink-block
title: 'Analog Input AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/analoginputadvancedavr.html'
language: en
---

# Analog Input AVR

## Ports

### Output

### **ADC\_Ch1(A0)** — ADC output data scalar

The block outputs the digitally converted voltage data received by the analog
input pin of the Arduino board. The number of output ports depends on the number of analog input
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

Enter the Arduino board analog input pin number. To open the Arduino pin mapping table, click **View pin map**. For more
information on how to assign pins for the Analog Input block, see Pin Mapping for Arduino Timer-Independent Blocks.

The number of **Pin Number** parameters depends on the number of
analog input pins you specify in the **Number of analog input pins**
parameter. For example, if you set the **Number of analog input pins**
parameter to `3`, the block enables the **Pin number
2** and **Pin number 3** parameters. You can enter the
analog pin numbers for the Arduino board accordingly.

### **ADC trigger** — Select a trigger to start ADC conversion `Free running mode` (default) | `Timer/Counter 0 Compare Match A` | `Timer/Counter 0 Overflow` | `Timer/Counter 1 Compare Match B` | `Timer/Counter 1 Overflow` | `Timer/Counter 4 Overflow` | `Timer/Counter 4 Compare Match A` | `Timer/Counter 4 Compare Match B` | `Timer/Counter 4 Compare Match D`

Select a timer/counter trigger to start the ADC conversion on the positive edge of
the trigger. Connect the Arduino hardware board pin to the PWM input signal using the PWM block to
enable the timer/counter.

- `Free running mode` — Operates independently of the
  clock and triggers an ADC conversion by the end of the previous conversion.
- `Timer/Counter 0 Compare Match A` — Trigger an ADC
  conversion once the value of the Timer/Counter 0 matches the value stored in the
  output compare register (OCR) A.
- `Timer/Counter 0 Overflow` — Triggers an ADC
  conversion when the value set in the Timer/Counter 0 register reaches its maximum
  value.
- `Timer/Counter 1 Compare Match B` — Trigger an ADC
  conversion once the value of the Timer/Counter 0 matches the value stored in OCR
  B.
- `Timer/Counter 1 Overflow` — Triggers an ADC
  conversion when the value set in the Timer/Counter 1 register reaches its maximum
  value.
- `Timer/Counter 4 Overflow` — Triggers an ADC
  conversion when the value set in the Timer/Counter 4 register reaches its maximum
  value.
- `Timer/Counter 4 Compare Match A` — Trigger an ADC
  conversion once the value of the Timer/Counter 4 matches the value stored in OCR
  A.
- `Timer/Counter 4 Compare Match B` — Trigger an ADC
  conversion once the value of the Timer/Counter 4 matches the value stored in OCR
  B.
- `Timer/Counter 4 Compare Match D` — Trigger an ADC
  conversion once the value of the Timer/Counter 4 matches the value stored in OCR
  D.

### **Enable ADC conversion complete interrupt** — Enable interrupt after ADC conversion is complete `on` (default) | `off`

Select this option to generate an interrupt after the analog voltage at the pin of
the Arduino hardware is converted to its equivalent digital voltage.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / AVR

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Read ADC register value after ADC conversion at analog pin of Arduino AVR core

Use the Analog Input block to read the value from an ADC register after
analog to digital conversion on the Arduino® AVR analog pin. You can use the block to read up to three analog voltage outputs simultaneously.

**Note**

The Analog Input block supports C/C++ code generation. This feature
allows you to generate C and C++ code using Embedded Coder®.
