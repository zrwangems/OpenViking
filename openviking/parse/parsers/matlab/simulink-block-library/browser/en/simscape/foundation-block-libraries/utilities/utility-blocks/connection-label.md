---
type: simulink-block
title: 'Connection Label'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'connectionlabel'
documentation_source_path: 'ref/connectionlabel.html'
language: en
---

# Connection Label

## Ports

### Conserving

### **Port\_1** — Connection port untyped conserving port

Conserving connection port. By default, this port is untyped.

You define the type of the port by connecting it to a conserving port of another
block in the subsystem, or to a Simscape Bus port. Once
you establish a connection, other Connection Label
blocks that are in the same subsystem and have the same label can be connected only to
the same type of port.

## Parameters

### **Label** — Name of connection label `Label1` (default) | character vector | string

Label name, which establishes the virtual connection. If two or more
Connection Label blocks in the same subsystem of a
model have the same label, then the conserving ports of the blocks connected to them
behave as though they were physically connected.

The value of this parameter appears as a label next to the block icon on the model
canvas.

## Libraries

Simscape / Utilities RF Blockset / Circuit Envelope / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Virtual connection between conserving ports

The Connection Label block lets you specify virtual
connections between Simscape™ conserving ports, similar to the Goto and From blocks in Simulink® diagrams. These connection lines are nondirectional, which means that all sides
of the virtual connection use the same type of block.

You can also use the Connection Label block to specify
virtual connections between other types of nondirectional ports, such as Simscape Bus ports or
Simscape
Multibody™ frame, geometry, and belt-cable ports.

Virtual connectivity is established by the label name. If two or more
Connection Label blocks in a model subsystem have the same
label, then the conserving ports of other blocks connected to them behave as though they were
physically connected. Virtual connections cannot cross subsystem boundaries.

The label name is displayed next to the block icon on the model canvas. You specify the
label name by using the **Label** parameter.

Use the Connection Label block to reduce diagram clutter by
breaking off tangled connection lines.

You can select a Connection Label block to highlight blocks
related to it. To show a related block in an open diagram or new tab, pause on the ellipsis.
Then, select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond to the
selected block, a list of related blocks opens. You can filter the list of related blocks by
entering a search term in the text box. After you select a related block from the list, window
focus goes to the open diagram or new tab that shows the related block.
