---
type: simulink-block
title: 'Battery'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Automotive Indicator Lamps'
documentation_page: 'battery'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/battery.html'
language: en
---

# Battery

## Ports

### Output

### **voltage** — EV3 brick battery voltage scalar

The block outputs the battery voltage from the LEGO
MINDSTORMS EV3 brick in millivolts.

**Data Types:** `uint16`

## Parameters

### **Sample time** — Time interval at which block reads EV3 brick battery voltage `0.1` (default) | positive integer

Specify the frequency of how often the block reads battery values of EV3 brick.
Shorter sample times, such as `0.01`, may produce unreliable
measurements.

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

Measure voltage level of battery in EV3 brick

Use the Battery block to measure voltage of the battery in the LEGO®
MINDSTORMS® EV3 brick, in millivolts. For example, when the six 1.5-volt batteries are fully
charged, the output value is approximately `9000` millivolts.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
