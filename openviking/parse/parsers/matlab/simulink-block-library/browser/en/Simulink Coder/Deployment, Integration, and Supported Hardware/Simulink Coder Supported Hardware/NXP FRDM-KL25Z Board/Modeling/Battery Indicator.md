---
type: simulink-block
title: 'Battery Indicator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'batteryindicator'
documentation_source_path: 'freedomboard/ref/batteryindicator.html'
language: en
---

# Battery Indicator

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

Display the battery voltage level with LEDs on the TFC shield

This block controls the four LEDs on the TFC Shield to indicate the present level of
the battery voltage. Each LED represents 25% of the battery voltage. When the input is
between 0.75 and 1.0, all the four LEDs are on and when the input reduces to a value
between 0.0 and 0.25, only one of the LEDs is on.

During simulations without the hardware, this block does nothing.
