---
type: simulink-block
title: 'Classic Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'classiccomponent'
documentation_source_path: 'ref/classiccomponent.html'
language: en
---

# Classic Component

## Ports

### Input

### **Input port** — Component require port scalar | vector | matrix

Require port in the AUTOSAR software component port interface.

If you link the component block to an implementation model, the port interfaces of
the block and model, including the number of ports, match.
### Output

### **Output port** — Component provide port scalar | vector | matrix

Provide port in the AUTOSAR software component port interface.

If you link the component block to an implementation model, the port interfaces of
the block and model, including the number of ports, match.

## Parameters

Not documented in R2025b.

## Libraries

AUTOSAR Blockset

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

### R2023a: Software Component block name changed to Classic Component

The Software Component block is renamed to the Classic
Component block.

## Description

Model classic software component in AUTOSAR architecture model

In an AUTOSAR architecture model, you use the composition editor and the Simulink® Toolstrip **Modeling** tab to add and connect compositions and
components. Use the Classic Component block to add a classic software component
to an AUTOSAR classic software design.

To add and connect AUTOSAR components:

- From the **Modeling** tab, configure the platform kind for the
  architecture model by setting **Platform** to
  `Classic`.
- For each component required by the design, from the **Modeling** tab
  or the palette to the left of the canvas, add a Classic Component block.
  You can use the Property Inspector to set the component **Kind** —
  `Application`, `ComplexDeviceDriver`,
  `EcuAbstraction`, `SensorActuator`, or
  `ServiceProxy`. (`Application` and
  `SensorActuator` are common.)
- Add component require ports and provide ports. To add each component port, click an
  edge of a Classic Component block. When port controls appear, select
  **Input** for a require port or **Output** for a
  provide port.
- To connect Classic Component blocks to other blocks, connect the block
  ports with signal lines.
- To connect Classic Component blocks to architecture or composition
  model root ports, drag a line from the component ports to the containing model boundary.
  Releasing the connection creates a root port at the boundary.
- Configure additional AUTOSAR properties using the Property Inspector.

After you add and connect AUTOSAR components, add Simulink behavior to the AUTOSAR components by creating, importing, or linking
models.

If you have Requirements Toolbox™ software, you can link components in an AUTOSAR architecture model to
Simulink requirements.

*Before R2023a: The Classic Component block was
named Software Component. The block was renamed to differentiate it from the
Adaptive Component block, which was introduced in R2023a.*
