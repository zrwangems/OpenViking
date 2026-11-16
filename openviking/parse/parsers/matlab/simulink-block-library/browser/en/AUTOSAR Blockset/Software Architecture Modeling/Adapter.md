---
type: simulink-block
title: 'Adapter'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'adapter'
documentation_source_path: 'ref/adapter.html'
language: en
---

# Adapter

## Ports

### Input

### **Source** — Input connection from a component interface

If you connect to a source component, the interfaces on the ports should be
compatible.
### Output

### **Destination** — Output connection to a component interface

If you connect to a destination component, the interfaces on the ports should be
compatible.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Connect components with different interfaces

The Adapter block allows you to connect the source and destination ports of
components that have different interface definitions.

Adapter block

To add or connect System Composer™ components:

- Add an Adapter block from the **Modeling** tab or
  the palette. The Adapter block has `In` and
  `Out` ports.
- Click and drag a port to create a connection. Connect each port to another
  component. You can also create a new component to complete the connection.
- Insert an Adapter block between two ports with different interfaces.
  You can create mappings between interface elements on each port.

To map between interfaces, apply interface conversions, and enter bus creation mode for
architecture models:

- Double-click the Adapter block to open the Interface Adapter dialog. In
  the dialog box, you can create and edit mappings between input and output interfaces,
  and set the **Apply Interface conversion** parameter to
  `UnitDelay` to break an algebraic loop or
  `RateTransition` to reconcile different sample time rates for
  reference models. When output interfaces are undefined, you can use input interfaces in
  bus creation mode to author owned output interfaces.

When you have Simulink® component behaviors with signal or message lines, then to merge message
connections for architecture models and signal or message connections for software
architecture models:

- Manually configure the Adapter block by double-clicking the block to
  open the Interface Adapter. Set the
  **Apply Interface conversion** parameter to
  `Merge`.
- For software architecture models, from the toolstrip, add a Merge
  block, which is a preconfigured Adapter block for merging.
