---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'analogoutput'
documentation_source_path: 'freedomboard/ref/analogoutput.html'
language: en
---

# Analog Output

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Send an analog output signal to PTE30 pin

Send an analog output signal to the pin PTE30 on the FRDM-KL25Z board. When you give a
value between 0.0-1.0, this block emits an analog signal to the pin PTE30, such
that:

Vout = 3.3\*(1 + input\*4095)/4096

Make sure to use only one Analog Output block within the same model.

During simulations without the hardware, this block does nothing.
