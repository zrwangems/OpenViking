---
type: simulink-block
title: 'Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'component'
documentation_source_path: 'ref/component.html'
language: en
---

# Component

## Ports

### Input

### **Source** — Input connection from another component interface

If you connect to a source component, the interfaces on the ports are
shared.
### Output

### **Destination** — Output connection to another component interface

If you connect to a destination component, the interfaces on the ports are
shared.
### Physical

### **Physical** — Physical connection to another component physical interface

If you connect to another component, the physical interfaces on the ports are
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

Add components to architecture model

Use a Component block to represent a structural or behavioral element at
any level of an architecture model hierarchy.

Add ports to the block to connect to other components. Define
an interface for the ports, add properties associated with the component using stereotypes, and
define parameters.

Component block

To add or connect System Composer™ components:

- Add an architecture Component block from the
  **Modeling** tab or the palette. You can also click and drag a box on
  the canvas, then select the Component block.
- To add a port, select an edge of the component and choose a direction from the menu:
  `Input`, `Output`, or
  `Physical`
- Click and drag the port to create a connection. Connect to another component. You
  can also create a new component to complete the connection.
- To connect Component blocks to architecture or composition model root
  ports, drag from the component ports to the containing model boundary. When you release
  the connection, a root port is created at the boundary.
- To add component-level parameters, use the Parameter
  Editor tool.

**Note**

You can add a mask icon to your component to illustrate the system represented by your component. For more information, see Add Mask Icon on Component.
