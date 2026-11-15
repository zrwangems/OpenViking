---
type: simulink-block
title: 'Hardware Interrupt AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Event Scheduling and Interrupt Handling'
documentation_page: 'hardwareinterruptadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedavr.html'
language: en
---

# Hardware Interrupt AVR

## Ports

### Output

### **Default event** — Generate interrupt request scalar

The block outputs a function call.

## Parameters

### **Interrupt group** — Select peripheral ISR `Timer 0` (default) | `Timer 1` | `Timer 2` | `Timer 3` | `Timer 4` | `Timer 5` | `Analog to digital converter (ADC)`

This parameter lists all the available ISRs for a particular type of peripheral in
an Arduino board. The values available in the **Interrupt name**
parameter change depending on the interrupt group you select in this parameter.

### **Interrupt name** — Select ISR `Timer0_COMPA` (default) | `Timer0_COMPB` | `Timer1_COMPA` | `Timer1_COMPB` | `Timer1_COMPC` | `Timer1_OVF` | `Timer2_COMPA` | `Timer2_COMPB` | `Timer2_OVF` | `Timer3_COMPA` | `Timer3_COMPB` | `Timer3_COMPC` | `Timer3_OVF` | `Timer4_COMPA` | `Timer4_COMPB` | `Timer4_COMPC` | `Timer4_COMPD` | `Timer4_OVF` | `Timer5_COMPA` | `Timer5_COMPB` | `Timer5_COMPC` | `Timer5_OVF` | `Analog to digital converter (ADC)`

The interrupt name specifies the ISR for the Hardware Interrupt
block. This parameter corresponds to the specific entry in the interrupt vector table of
the Arduino board. The available ISRs depend on the **Interrupt
group**.

#### Dependencies

- To enable the `Timer0_COMPA` and
  `Timer0_COMPB` interrupts, set **Interrupt
  group** to `Timer 0`.
- To enable the `Timer1_COMPA` and
  `Timer1_COMPB`,
  `Timer1_COMPC`, and `Timer1_OVF`
  interrupts, set **Interrupt group** to `Timer
  1`.
- To enable the `Timer2_COMPA` and
  `Timer2_COMPB`, and
  `Timer1_OVF` interrupts, set **Interrupt
  group** to `Timer 2`.
- To enable the `Timer3_COMPA` and
  `Timer3_COMPB`,
  `Timer3_COMPC`, and `Timer3_OVF`
  interrupts, set **Interrupt group** to `Timer
  3`.
- To enable the `Timer4_COMPA` and
  `Timer4_COMPB`,
  `Timer4_COMPC`, `Timer4_COMPC`,
  and `Timer4_OVF` interrupts, set **Interrupt
  group** to `Timer 4`.
- To enable the `Timer5_COMPA` and
  `Timer5_COMPB`,
  `Timer5_COMPC`, and `Timer5_OVF`
  interrupts, set **Interrupt group** to `Timer
  5`.
- To enable the `Analog to digital converter (ADC)`
  interrupt, set **Interrupt group** to
  `ADC`.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / AVR

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Trigger downstream function-call subsystems from interrupt service routine for Arduino AVR core

Use the Hardware Interrupt block to create an interrupt service routine
(ISR) automatically in the generated code of your Simulink® model for the selected interrupts. The ISR executes the downstream function-call
subsystem associated with the event ports of the block.

This block generates code only for the ISR that you select or specify. To change the
configuration, enable the interrupt, and specify triggering options, use the settings of the
selected peripherals. For example, to create an ISR for the ADC peripheral on the
Hardware Interrupt block:

- Your Simulink model must have an Analog Input
  block. In the block, select the **Enable ADC conversion complete
  interrupt** parameter.
- In the Hardware Interrupt block, set these parameters:

  - **Interrupt group** to `Analog to digital
    converter (ADC)`
  - **Interrupt name** to `ADC`

Similarly, to create an ISR for the PWM peripheral on the Hardware
Interrupt block:

- Your Simulink model must have a PWM block. In
  the block, select the **Enable compare match (MCx) interrupt** or
  **Enable overflow/underflow (OVF) interrupt** parameter or both the
  parameters.
- In the Hardware Interrupt block, set these parameters:

  - **Interrupt group** to either `Timer
    0`, `Timer 1`, `Timer
    2`, `Timer 2`, `Timer
    3`, `Timer 4`, or `Timer
    5`.
  - **Interrupt name** to the available ISRs depend on the
    **Interrupt group**.

**Note**

The Hardware Interrupt block supports C/C++ code generation. This
feature allows you to generate C and C++ code using Embedded Coder®.

### Supported Arduino Boards

- Arduino® Uno
- Arduino Mega 2560
- Arduino Mega ADK
- Arduino Leonardo
- Arduino Micro
