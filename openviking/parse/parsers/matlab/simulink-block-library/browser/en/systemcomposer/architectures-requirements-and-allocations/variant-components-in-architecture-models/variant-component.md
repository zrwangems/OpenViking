---
type: simulink-block
title: 'Variant Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Variant Components in Architecture Models'
documentation_page: 'variantcomponent'
documentation_source_path: 'ref/variantcomponent.html'
language: en
---

# Variant Component

## Ports

### Input

### **Source** — Input connection from another component interface

If you connect to a source component, the interfaces on the ports are
shared.
### Output

### **Destination** — Output connection to another component interface

If you connect to a destination component, the interfaces on the ports are
shared.

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

Add components with alternative designs

Use a Variant Component block to create multiple design alternatives for a
component.

Add ports to the block to connect to other components. Define
an interface for the ports, add properties associated with the component using stereotypes, and
define parameters.

Variant Component block

To add or connect System Composer™ components:

- Add an architecture Variant Component block from the
  **Modeling** tab or the palette. You can also click and drag a box on
  the canvas, then select the Variant Component block. You can also create
  a variant component from a Component block or Reference
  Component block. Right-click on the component and select **Add Variant
  Choice**.
- To add a port, select an edge of the component and choose a direction from the menu:
  `Input` or `Output`
- Click and drag the port to create a connection. Connect to another component. You
  can also create a new component to complete the connection.
- To connect Variant Component blocks to architecture or composition
  model root ports, drag from the component ports to the containing model boundary. When
  you release the connection, a root port is created at the boundary.

**Note**

You can add a mask icon to your component to illustrate the system represented by your component. For more information, see Add Mask Icon on Component.

To manage Variant Component choices:

- By default, two variant choices are created when you create a Variant
  Component block. Right-click the Variant Component block and
  select **Variant** > **Label Mode Active Choice**, then select the active choice.
- To add an additional variant choice, right-click on the Variant
  Component block and select **Variant** > **Add Variant Choice**.
- Double-click into the Variant Component block to design the variants
  within it.
- Use the Variant Manager to easily switch between variant choices in a
  complex model hierarchy. Right-click on the Variant Component block and
  select **Variant** > **Open in Variant Manager**. For more information, see Variant Manager for Simulink.
