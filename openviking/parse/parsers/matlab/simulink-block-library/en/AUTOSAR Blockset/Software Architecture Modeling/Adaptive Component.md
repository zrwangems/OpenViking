---
type: simulink-block
title: 'Adaptive Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'adaptivecomponent'
documentation_source_path: 'ref/adaptivecomponent.html'
language: en
---

# Adaptive Component

## Ports

### Input

### **Input port** — Component require port scalar | vector | matrix

Require port in the AUTOSAR software component port interface.

If you link the component block to an implementation model, the port interfaces of
the block and model, including the number of ports, match.

### **Client port** — Component client port on a service interface scalar | vector | matrix

Client port on a service interface for AUTOSAR method communication, implementing
a service consumer.

If you link the component block to an implementation model, the port interfaces of
the block and model, including the number of ports, match.
### Output

### **Output port** — Component provide port scalar | vector | matrix

Provide port in the AUTOSAR software component port interface.

If you link the component block to an implementation model, the port interfaces of
the block and model, including the number of ports, match.

### **Server port** — Component server port on a service interface scalar | vector | matrix

Server port on a service interface for AUTOSAR method communication, implementing
a service provider.

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

**Introduced in R2023a**

## Description

Model adaptive software component in AUTOSAR architecture model

In an AUTOSAR architecture model, you use the composition editor and the Simulink® Toolstrip **Modeling** tab to add and connect compositions and
components. Use the Adaptive Component block to add an adaptive software
component to an AUTOSAR adaptive software design.

To add and connect AUTOSAR components:

- From the **Modeling** tab, configure the platform kind for the
  architecture model by setting **Platform** to
  `Adaptive`.
- For each component required by the design, from the **Modeling** tab
  or the palette to the left of the canvas, add an Adaptive Component block.
  You can view the component **Kind** in the Property Inspector. For
  adaptive components, the component kind is
  `AdaptiveApplication`.
- Add component require ports and provide ports. To add each component port, click an
  edge of a Adaptive Component block. When port controls appear, select
  **Input** or **Client** for a require port, or
  **Output** or **Server** for a provide port.
- To connect the Adaptive Component blocks to other blocks, connect the
  block ports with signal lines.
- To connect the Adaptive Component blocks to architecture or composition
  model root ports, drag a line from the component ports to the containing model boundary.
  Releasing the connection creates a root port at the boundary.
- Configure additional AUTOSAR properties using the Property Inspector.

After you add and connect AUTOSAR components, add Simulink behavior to the AUTOSAR components by creating, importing, or linking
models.

If you have Requirements Toolbox™ software, you can link components in an AUTOSAR architecture model to
Simulink requirements.

Each Adaptive Component block represents an adaptive application. Upon
deployment, each adaptive component is treated as an executable.
