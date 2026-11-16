---
type: simulink-block
title: 'Battery Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'batteryread'
documentation_source_path: 'freedomboard/ref/batteryread.html'
language: en
---

# Battery Read

## Ports

Not documented in R2025b.

## Parameters

**Sample time**
:   Specify how often the block reads the battery voltage level, in seconds.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read the battery voltage of a battery connected to the TFC Shield

Read the voltage of the battery connected to the TFC shield. The block output emits a
value in the range 0.0 –1.0 to indicate the current voltage level of the battery as a
percentage of an assumed 7.2 Volt battery.

During simulations without the hardware, this block emits zeroes.
