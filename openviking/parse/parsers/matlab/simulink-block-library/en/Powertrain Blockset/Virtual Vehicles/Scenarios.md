---
type: simulink-block
title: 'Scenarios'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'scenarios'
documentation_source_path: 'ref/scenarios.html'
language: en
---

# Scenarios

## Ports

### Input

### **ExtDrvRef** — External driver reference `Bus`

External driver reference signals.

#### Dependencies

To create this port, select **Driver reference**.

### **ExtDrvCmd** — External driver commands `Bus`

External driver commands signals.

#### Dependencies

To create this port, select **Driver reference**.

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.
### Output

### **Vis** — Visualization reference signals `Bus`

Bus containing the visualization reference signals, including longitudinal and
lateral displacement, and steering.

### **VehRef** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

### **Fdbk** — Vehicle location feedback signals `Bus`

Bus containing vehicle displacement feedback signals.

## Parameters

### **Driver reference** — Enable external driver input `off` (default) | `on`

Specify to create an external driver reference inport,
`ExtDrvRef`.

### **Driver commands** — Enable external driver commands `off` (default) | `on`

Specify to create an external driver commands inport,
`ExtDrvCmd`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Configure scenarios

The Scenarios block implements the driver
scenario. The subsystem contains variants that generate maneuver-specific driver reference
velocity, path, and action signals. Select **Driver reference** to input
external driver reference signals. Select **Driver commands** to input
external driver signals.

Additionally, you can control external or internally generated signals by setting the
workspace variables `ExtDrvRefSwitch` and `ExtDrvCmdsSwitch`
to `true` or `false` during runtime. Consider using the
switch values when running multiple simulations that require both external and internal
maneuvers or when overriding nominal model-generated ones.
