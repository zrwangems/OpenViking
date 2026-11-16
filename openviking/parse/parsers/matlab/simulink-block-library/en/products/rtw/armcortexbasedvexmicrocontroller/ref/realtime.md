---
type: simulink-block
title: 'Real Time'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'realtime'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/realtime.html'
language: en
---

# Real Time

## Ports

Not documented in R2025b.

## Parameters

**Time Scaling Factor**
:   Enter the time scaling factor to slow down the simulation speed to be close to the
    real-time.

    For example, when you a enter a time scaling factor as 1, one simulation second
    runs in 1 second of real time. The simulation time is the same as real time.

    When you enter a time scaling factor as 5, one simulation second runs in 5 seconds
    of real time. The simulation time is five times slower than real time.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Slow down simulation time close to real time

Place this block in your model to slow down the simulation time close to the real time.
To specify the ratio between the actual time and the simulation time, use the time scaling
factor parameter in the block.

**Note**

The Real Time block will be deprecated in the next release of Simulink®
Coder™ Support Package for ARM®
Cortex®-based VEX® Microcontroller. Instead, you can use the Simulation Pacing option in the Simulink Editor.
