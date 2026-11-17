---
type: simulink-block
title: 'Connection Label'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'connectionlabel'
documentation_source_path: '../simrf/ref/connectionlabel.html'
language: en
---

# Connection Label

## Ports
```yaml
ports:
- name: Port_1
  summary: Connection port untyped circuit envelope port
  direction: input
```

### Input

### **Port\_1** — Connection port untyped circuit envelope port

Circuit envelope connection port. By default, this port is untyped.

You define the port type by connecting this port to a circuit envelope port of
another block in the subsystem. Once you establish a connection, other
Connection Label blocks that are in the same
subsystem and have the same label can be connected only to the same type of
port.
## Parameters
```yaml
parameters:
- name: Label
  summary: Name of connection label Label1 (default) | character vector | string
  group: ''
```

### **Label** — Name of connection label `Label1` (default) | character vector | string

Label name, which establishes the virtual connection. If two or more
Connection Label blocks in the same subsystem of a
model have the same label, then the circuit envelope ports of the blocks connected to
them behave as though they are physically connected.

The value of this parameter appears as a label next to the block icon on the model
canvas.
## Libraries

RF Blockset / Circuit Envelope / Utilities Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Virtual connection between circuit envelope ports

The Connection Label block lets you specify virtual
connections between circuit envelope ports, similar to the Goto and From blocks in Simulink® diagrams. These connection lines are nondirectional, which means that all sides
of the virtual connection use the same type of block.

Virtual connectivity is established by the label name. If two or more
Connection Label blocks in a model subsystem have the same
label, then the circuit envelope ports of other blocks connected to them behave as though they
were physically connected. Virtual connections cannot cross subsystem boundaries. The label
name is displayed next to the block icon on the model canvas.

You specify the label name by using the **Label** parameter.

Use the Connection Label block to reduce diagram clutter by
breaking off tangled connection lines.

You can select a Connection Label block to highlight blocks
related to it. To show a related block in an open diagram or new tab, pause on the ellipsis.
Then, select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond to the
selected block, a list of related blocks opens. You can filter the list of related blocks by
entering a search term in the text box. After you select a related block from the list, window
focus changes to the open diagram or new tab that shows the related block.
