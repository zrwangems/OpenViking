---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'pwmoutput'
documentation_source_path: 'freescalefrdmk64fboard/ref/pwmoutput.html'
language: en
---

# PWM Output

## Ports

Not documented in R2025b.

## Parameters

**Pin**
:   Select the output pin to generate the pulse waveform. To view the
    pin mapping, click **View pin map**.

**Initial frequency (Hz)**
:   Specify the initial frequency in Hertz. The default initial
    frequency is 2000 Hz.

**Initial duty cycle (0 – 100)**
:   Specify the initial duty cycle between 0 to 100. The default
    initial duty cycle is 0.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Generate pulse waveform on specified output pin

Generate pulse waveform on the specified output pin. You can provide a value
between 0 to 100 as the block input. The input value that you provide controls
the duty cycle of the pulse waveform. For an input ‘0’, the block produces ‘0’
percent duty cycle and for an input ‘100’, the block produces 100 duty
cycle.
