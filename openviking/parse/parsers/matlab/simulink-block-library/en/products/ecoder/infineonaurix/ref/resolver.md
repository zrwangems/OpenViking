---
type: simulink-block
title: 'Resolver'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'resolver'
documentation_source_path: 'infineonaurix/ref/resolver.html'
language: en
---

# Resolver

## Ports

### Output

### **θₘ** — Angle of the resolver sensor `scalar` | `vector`

The block outputs the position of the resolver sensor in radians (default)
or degrees. The size of θₘ output depends on the **Enable
timestamp** parameter.

Selecting the **Enable timestamp** parameter results in θₘ
of size 2x1 and disabling **Enable timestamp** parameter
results in θₘ of size 1x1.

**Data Types:** `single`

### **timestamp** — Timestamp of 16-bit counter value `scalar`

The port outputs the timestamp indicating the time elapsed in seconds from
the last conversion.

#### Dependencies

To enable this port, select the **Enable timestamp**
parameter.

**Data Types:** `single`

## Parameters

### **Angle in** — Measuring unit of angle `Radians` (default) | `Degrees`

Select the position measurement unit for the resolver sensor.

### **Enable timestamp** — Select to enable the timestamp `off` (default) | `on`

Select to enable the timestamp.

When you select the `Enable timestamp` parameter, the block
configures an additional output port  **timestamp**.

Selecting of this parameter enables options in the
**Timestamp** tab and Timestamp event (under
**Events** tab) in the Resolver
Peripheral Configuration window.

### **Sample time** — Frequency at which block reads the position `-1` (default) | `scalar`

Specify in seconds how often the block must read the position of the resolver
sensor.

When you specify this parameter as -1, Simulink® determines the best sample time for the block based on the block
context within the model.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Measure position of resolver sensor

The Resolver block measures the position of a resolver sensor and also capable of
generating the excitation carrier signal for the resolver sensor.

The Resolver block outputs the angle of the resolver sensor in either radians (default)
or degrees. The block outputs a measurement based on the sensed sine and cosine voltages of
the resolver sensor.

Enabling the timestamp option creates an additional output port that outputs the
timestamp in seconds from the last conversion as a signed value.
