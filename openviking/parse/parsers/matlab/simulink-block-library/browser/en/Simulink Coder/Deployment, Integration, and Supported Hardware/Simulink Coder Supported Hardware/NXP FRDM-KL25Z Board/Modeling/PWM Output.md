---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'pwmoutput'
documentation_source_path: 'freedomboard/ref/pwmoutput.html'
language: en
---

# PWM Output

## Ports

### Input

### **Port\_1** — Duty cycle value scalar

The range of valid input values is `0` to `100`.
The input controls the duty cycle (width of the square wave) of the
square waveform.

An input value of `0` produces a 0% duty cycle
and an input value of `100` produces a 100% duty
cycle. Any out-of-range values, such as `500` or `-500`,
at the block input port has the same effect as the maximum or minimum
input values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Pin** — Output pin at which the block generates the square-wave pulse waveform `PTA5 (D5)` (default) | `LED_RED` | `LED_GREEN` | `LED_BLUE` | `PTA1 (D0)` | `PTA2 (D1)` | `PTD4 (D2)` | `PTA12 (D3)` | `PTA4 (D4)` | `PTC8 (D6)` | `PTC9 (D7)` | `PTA13 (D8)` | `PTD5 (D9)` | `PTD0 (D10)` | `PTD2 (D11)` | `PTD3 (D12)` | `PTD1 (D13)` | `PTB0 (A0)` | `PTB1 (A1)` | `PTB2 (A2)` | `PTB3 (A3)` | `PTC2 (A4)` | `PTC1 (A5)` | `PTE20` | `PTE21` | `PTE22` | `PTE23` | `PTE29` | `PTE30` | `PTE31` | `PTC3` | `PTC4`

To view the pin mapping on the board, click **View
Pin Map**. On the board, each PWM pin is connected to either
of the three timers, TPM0 (Timer PWM Module), TPM1, or TPM2. To learn
about the Timer Channel Pin combination, see the Timer to Pin Mapping
table in the **Timer/PWM module** parameter description
section.

### **Timer/PWM module** — Timers that generate the PWM signal `TPM0` (default) | `TPM1` | `TPM2`

The board has three timers, TPM0, TPM1, and TPM2. Each PWM pin
is connected to one of these three timers. When you select a pin in
the **Pin** list, this parameter is populated with
the timer to which the pin is connected. For example, if you select
the `PTA1 (D0)` pin, this parameter is set
to `TPM2`.

The following table shows timer to pin mapping.

In your model, if you have more than one instance of the PWM
Output block, use a different Timer Channel combination for
every block instance. Otherwise, you receive an error message indicating
you to use GPIO Pins from different Timer Channel combination for
all the block instances.

For example, suppose that in one PWM Output block
instance you select the `PTC3` pin to generate
the output. The `PTC3` pin is connected to
the CH2 channel of the TPM0 timer. When selecting a pin for the other
instances of the PWM Output block, select a pin that
belongs to a timer channel combination other than TPM0 CH2.

#### Dependencies

This parameter appears dimmed.

### **Initial duty cycle (0 - 100)** — Initial duty cycle `0` (default) | `integer between 0 and 100`

When initializing, the block sets its duty cycle to the value
that you specify in this parameter.

### Example

This example shows how to use the PWM Output block
to control the brightness of the blue LED connected to the `D13` pin
on the board.

1. Connect the FRDM-KL25Z hardware to your computer.
2. In the Simulink® Editor, open a new model window.
   From the Library Browser, copy a Constant block and
   a PWM Output block and connect them.
3. Set the value of the Constant block
   to `50`. This value represents the duty cycle of
   the output square wave in percentage.
4. In the Block Parameter dialog box, set the Pin to `D13` and
   the Initial duty cycle to `0`.
5. In the Simulink Editor, select **Simulation** > **Model Configuration
   Parameters**.
6. In the Configuration Parameters dialog box, click **Hardware
   Implementation**.
7. Set the **Hardware board** parameter
   to NXP FRDM-KL25Z.
8. To set the frequency of the output signal, identify
   the timer to which the `D13` pin is connected.

   To identify the timer, in the Block Parameter dialog box, click **View
   Pin Map**. In the pin map, search for the `D13` pin
   and the timer name next to it. The `D13` pin
   is connected to the `TMP0` pin.
9. In the Configuration Parameters dialog box, set the **TPM0
   Frequency (in Hz)** to `50`. Using the frequency
   value, the block calculates the period of the square wave.

   Period = 1/50 = 0.02 seconds

When you build the model and load it on the hardware, the PWM
Output block generates square-wave pulses with the pulse width
of (50\* 0.02)/100 = 0.01 seconds. The blue LED turns on for 0.01 seconds,
and then it turns off for the next 0.01 seconds. You can blink an
LED on and off quickly to control its brightness with the PWM
Output block.

## Libraries

Simulink Coder Support Package for NXP FRDM-KL25Z Board/FRDM-KL25Z

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Generate square wave on the specified output pin

The PWM Output block generates square-wave pulses
and outputs to the specified pin on the board. You can provide a value
between 0–100 as the block input. The input value that you
provide controls the duty cycle of the pulse waveform. An input value
of `0` produces a 0% duty cycle and an input value
of `100` produces a 100% duty cycle.
