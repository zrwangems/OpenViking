---
type: simulink-block
title: 'DIP Switch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'dipswitch'
documentation_source_path: 'freedomboard/ref/dipswitch.html'
language: en
---

# DIP Switch

## Ports

Not documented in R2025b.

## Parameters

**Sample time**
:   Specify how often this block reads the dip switch states.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read the state of a DIP switch

Read the four individual switch statuses. Each block output emits 0 when the
corresponding switch state is Off and emits 1 when the switch state is On.

During simulations without the hardware, this block emits zeroes.
