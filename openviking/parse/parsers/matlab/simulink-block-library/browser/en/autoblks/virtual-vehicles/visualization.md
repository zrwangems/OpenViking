---
type: simulink-block
title: 'Visualization'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'visualization'
documentation_source_path: 'ref/visualization.html'
language: en
---

# Visualization

## Ports

### Input

### **Vis** — Visualization reference signals `Bus`

Bus containing the visualization reference signals, including longitudinal and
lateral displacement, and steering.

### **VehRef** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

### **Fdbk** — Vehicle location feedback signals `Bus`

Bus containing vehicle displacement feedback signals.
### Output

### **ExtVehFdbk** — Command signals `Bus`

Bus containing the commands, including steering, acceleration, braking, and gear
commands.

#### Dependencies

To create this port, select **Vehicle feedback**.

## Parameters

### **Vehicle feedback** — Enable vehicle feedback outport `off` (default) | `on`

Specify to create a top-level model non-virtual bus port feedback outport,
`ExtVehFdbk`, with vehicle system signals. Consider selecting to make
signals available when the model is simulated with other systems.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Configure visualization

The Visualization subsystem contains
signal logging, scopes, and other visualization features. Selecting **Vehicle
feedback** creates a top-level model non-virtual bus port, making commonly used
vehicle system signals available when the model is simulated with other systems.
