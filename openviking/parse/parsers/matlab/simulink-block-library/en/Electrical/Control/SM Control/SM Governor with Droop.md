---
type: simulink-block
title: 'SM Governor with Droop'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smgovernorwithdroop'
documentation_source_path: 'ref/smgovernorwithdroop.html'
language: en
---

# SM Governor with Droop

## Ports

### Input

### **P\_ref** — Desired per-unit generator load scalar

Reference generator load expressed as a per-unit quantity. The
steady-state output of the governor running at its reference speed is
equivalent to this value.

**Data Types:** `single` | `double`

### **speed\_ref** — Desired per-unit generator speed scalar

Reference generator speed expressed as a per-unit quantity.

**Data Types:** `single` | `double`

### **speed** — Actual per-unit generator speed scalar

Measured generator speed expressed as a per-unit quantity.

**Data Types:** `single` | `double`
### Output

### **throttle** — Throttle position scalar

Throttle position of the governor, expressed as a per-unit quantity.

**Data Types:** `single` | `double`

## Parameters

### **Percentage droop, (%)** — Droop `5` `%` (default)

Percent change in governor speed from `0`% to `100`%
load. If multiple governor-driven generators are connected in parallel,
those with lower droop percentages are more sensitive to load
changes.

### **Time constant of governor, (s)** — First-order lag time constant `0.2` (default)

Time constant of the governor first-order lag representing the throttle
inertia dynamics.

### **Initial throttle position, (pu)** — Initial throttle output `0.5` (default)

Initial state of the throttle.

## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Synchronous machine governor with droop

The SM Governor with Droop block implements a synchronous machine (SM)
governor with a droop characteristic. Use this block to regulate or control the throttle
input to a prime mover driving a synchronous generator.

The block uses the error between the measured and desired generator speeds to set the
prime mover throttle position. For example, when the prime mover is rotating too slowly,
the throttle is opened to increase the energy input to the generator and increase its
speed.

### Operation

When multiple governor-driven generators are connected in parallel, droop characteristics
ensure overall stability of the grid. Droop is defined as percent change in speed
from no load to full load of the generator. This figure shows the speed-load
relationship for a governor with 5% droop.

Here,

- *ωref* is the reference speed of the governor.
  Set this value as a per-unit quantity using the
  **speed\_ref** port.
- *Pref* is the reference load of the governor.
  Set this value as a per-unit quantity using the
  **P\_ref** port.
- `droop` is the droop percentage of the governor. Set
  this value as a percentage using the **Percentage droop,
  (%)** parameter.

The block calculates the reference throttle position, expressed as a per-unit quantity, as:

uthrottle,ref=Pref−100droop(ω−ωref)

where *ω* is the actual, per-unit generator
speed.

The inertia of the valve introduces a delay between this reference throttle
position and the actual throttle position, which is modeled as a first-order lag:

uthrottle=(1Tss+1)uthrottle,ref

Here, *Ts* is the time
constant. Set this value using the **Time constant of governor,
(s)** parameter.
