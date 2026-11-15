---
type: simulink-block
title: 'Environment'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'environment'
documentation_source_path: 'ref/environment.html'
language: en
---

# Environment

## Ports

### Input

### **ExtEnv** — External driver reference `Bus`

External environment signals.

#### Dependencies

To create this port, select **Environment**.

### **ExtGrd** — External driver commands `Bus`

External ground signals.

#### Dependencies

To create this port, select **Ground**.
### Output

### **Env** — Environment signals `Bus`

Bus containing the environment signals.

## Parameters

### **Environment** — Enable external environment input `off` (default) | `on`

Specify to create an external environment inport, `ExtEnv`.

### **Ground** — Enable external ground input `off` (default) | `on`

Specify to create an external ground inport, `ExtGnd`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Configure environment

The Environment block implements the environment model, including road
grade, wind velocity, and ambient temperature and pressure. The subsystem contains variants
that generate environment- and terrain-specific signals. Select
**Environment** to input external environment signals. Select
**Ground** to input external ground signals.

Additionally, you can control external or internally generated signals by setting the
workspace variables `ExtEnvSwitch` and `ExtGndSwitch` to
`true` or `false` during runtime. Consider using the
switch values when running multiple simulations that require both external and internal
maneuvers or when overriding nominal model-generated ones.
