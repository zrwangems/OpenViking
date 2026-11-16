---
type: simulink-block
title: 'Interface (H-IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Upgrading Hydraulic Models to Use Isothermal Liquid Blocks'
documentation_page: 'interfacehil'
documentation_source_path: 'ref/interfacehil.html'
language: en
---

# Interface (H-IL)

## Ports

### Conserving

### **H** — Hydraulic port hydraulic

Hydraulic conserving port representing a passage point through the interface.
Connect this port to a block network built on the Simscape hydraulic domain.

### **IL** — Isothermal liquid port isothermal liquid

Isothermal liquid conserving port representing a passage point through the
interface. Connect this port to a block network built on the Simscape isothermal liquid domain.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Hydraulic / Hydraulic Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Flow connection between hydraulic and isothermal liquid networks

The Interface (H-IL) block represents a cross-domain flow
connection between hydraulic and isothermal liquid networks:

- Pressure and mass flow rates are equal at the interface.
- Fluid properties are not shared across the interface. Each network has its own fluid
  properties.

Use this block in existing models with blocks from the Foundation > Hydraulic library, or
from the Fluids > Hydraulics (Isothermal) library, to implement parts of the model using
Isothermal Liquid library blocks, without converting the whole model. The Fluids > Hydraulics
(Isothermal) library is available if you have a Simscape™
Fluids™ license.

The `hydraulicToIsothermalLiquid` conversion tool replaces Hydraulic
blocks in your model with equivalent Isothermal Liquid blocks. If your model contains
references or links to other libraries, models, or subsystems, you can use the
Interface (H-IL) to restore the broken connections between
the converted parts of the block diagram and the libraries, models, or subsystems that still
need to be converted.
