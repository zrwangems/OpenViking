---
type: simulink-block
title: 'Potentiometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'potentiometer'
documentation_source_path: 'freedomboard/ref/potentiometer.html'
language: en
---

# Potentiometer

## Ports

Not documented in R2025b.

## Parameters

**Potentiometer**
:   Select potentiometer A or B.

**Sample time**
:   Specify how often this block reads the potentiometer value, in seconds.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read the state of a potentiometer

The NXP TFC shield comes with two on board potentiometers (POTA and POTB).

The block output emits values from -1.0 to 1.0 based on the current angular position
of the potentiometer. These values correspond to the potentiometer being turned fully
counter clockwise or fully clockwise respectively.

During simulations without the hardware, this block emits zeroes.
