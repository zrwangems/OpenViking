---
type: simulink-block
title: 'Software Composition'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'softwarecomposition'
documentation_source_path: 'ref/softwarecomposition.html'
language: en
---

# Software Composition

## Ports

### Input

### **Input port** — Composition require port scalar | vector | matrix

Require port in the AUTOSAR software composition port interface.

### **Client port** — Composition client port on a service interface scalar | vector | matrix

Client port in the AUTOSAR software composition port interface. Client ports are
supported when you model method communication in an AUTOSAR adaptive architecture.
### Output

### **Output port** — Composition provide port scalar | vector | matrix

Provide port in the AUTOSAR software composition port interface.

### **Server port** — Composition server port on a service interface scalar | vector | matrix

Server port in the AUTOSAR software composition port interface. Server ports are
supported when you model method communication in an AUTOSAR adaptive architecture.

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

### R2023a: Client and server ports for adaptive component modeling

Client and server ports are available and supported when you model method communication
in an AUTOSAR adaptive architecture.

## Description

Model software composition in AUTOSAR architecture model

In an AUTOSAR architecture model, you use the composition editor and the Simulink® Toolstrip **Modeling** tab to add and connect compositions and
components. Use the Software Composition block to add a nested software
composition to an AUTOSAR software design. Compositions are supported for classic and adaptive
modeling.

To add and connect a nested AUTOSAR composition:

- From the **Modeling** tab or the palette to the left of the canvas,
  add a Software Composition block.
- Add composition require ports and provide ports. To add each composition port, click
  an edge of the Software Composition block. When port controls appear:

  - For classic modeling, select **Input** for a require port or
    **Output** for a provide port.
  - For adaptive modeling, select **Input** or
    **Client** for a require port, or **Output** or
    **Server** for a provide port.

  Alternatively, open the Software Composition block. To add each
  composition port, click the boundary of the composition diagram and select require and
  provide ports as needed.
- To connect the Software Composition block to other blocks, connect the
  block ports with signal lines.
- To connect the Software Composition block to architecture or
  composition model root ports, drag a line from the composition ports to the containing
  model boundary. Releasing the connection creates a root port at the boundary.
- Configure additional AUTOSAR properties using the Property Inspector.

An AUTOSAR composition contains a set of AUTOSAR components and compositions with a shared
purpose. To populate a composition, open the Software Composition block and
begin adding more Software Composition blocks and Classic
Component or Adaptive Component blocks. Mixing classic and adaptive
components is not supported.
