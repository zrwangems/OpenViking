---
type: simulink-block
title: 'Timer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'timer'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/timer.html'
language: en
---

# Timer

## Ports

### Output

### **time** — Time elapsed from running a Simulink model scalar

The block outputs the time elapsed in milliseconds when the EV3 brick starts
running the Simulink model.

**Data Types:** `uint32`

## Parameters

### **Sample time** — Time interval at which block reads timer values `0.1` (default) | positive integer

Specify the frequency of how often the block the timer values. Shorter sample times,
such as `0.01`, may produce unreliable measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Measure elapsed time from timer in EV3 brick

Use the Timer block measure the elapsed time in milliseconds when the EV3
brick starts running the Simulink® model.

You can see when the EV3 brick starts running a model by observing the LCD on the EV3
brick. For Simulink models that do not use the Display block, the LCD on the EV3 brick
displays `I am running` followed by the model name. For models that use the
Display block, the model displays
whatever output is sent to it.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
