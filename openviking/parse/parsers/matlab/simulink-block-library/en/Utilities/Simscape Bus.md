---
type: simulink-block
title: 'Simscape Bus'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'simscapebus'
documentation_source_path: '../simscape/ref/simscapebus.html'
language: en
---

# Simscape Bus

## Ports

### Conserving

### **Bus** — Simscape Bus port bus

Port connected to a Simscape Bus line, which represents a bundle of conserving
connection lines. The bundle contains all the lines connected to the block on the
opposite side.

This opposite side, by default, does not have ports. You add ports by dragging the
connection lines to that side of the block, or by using the block dialog box. Elements
coming into the block on the children side can be either conserving connection lines
or Simscape Bus lines. Every time you add a port on the children side, the
corresponding connection is added to the connections list inside the block.

## Parameters

### **Connection type** — Specify or remove rigid interface `Inherit: auto` (default) | `Bus: <object name>` | `CompositeConnection: <domain name>` | list of `ConnectionBus` objects

Specify a rigid interface by selecting a port type from the drop-down list. The list
contains the names of `ConnectionBus` objects present in the base
workspace or a data dictionary. If you add a new `ConnectionBus` object
to the base workspace or data dictionary, click **Refresh data types**
in the drop-down list to make the new object available for selection. To create or
modify `ConnectionBus` objects, click the **Show type
assistant** button next to the drop-down list to display the **Type
Assistant** panel. For more information, see Specifying Rigid Interfaces.

To specify a rigid connection to a composite domain, select
`CompositeConnection: <domain name>` and click the
**Show type assistant** button next to the drop-down list. In the
**Type Assistant** panel, set **Mode** to
`Composite domain` and type the name of an existing composite
domain in the `<domain name>` field.

To remove the rigid interface specification, set the **Connection
type** parameter to `Inherit: auto`.

### **Mode** — Specify connection mode `Inherit` (default) | `Connection Bus object` | `Composite domain`

Works in conjunction with the **Connection type** parameter and
provides additional options for specifying a rigid interface:

- `Inherit` — Indicates flexible interface. The only
  drop-down option available is `auto`. Corresponds to the
  **Connection type** parameter setting `Inherit:
  auto`.
- `Connection Bus object` — Specify a rigid bus
  connection. Type the name of an existing `ConnectionBus` object in
  the `<object name>` field or use the
  **Edit** button to open the Type Editor and create or modify a
  `ConnectionBus` object. Corresponds to the **Connection
  type** parameter setting `Bus: <object
  name>`.
- `Composite domain` — Specify a rigid connection to a
  composite domain. Type the name of an existing composite domain in the
  `<domain name>` field. Corresponds to the
  **Connection type** parameter setting
  `CompositeConnection: <domain name>`.

#### Dependencies

To enable this selection, click the **Show type assistant**
button next to the **Connection type** parameter. As you select
values in the **Type Assistant** panel, the **Connection
type** parameter setting updates accordingly.

### **Hierarchy Strings** — List of connection names empty (default) | connection names

List of connection names corresponding to the conserving lines that are connected to
the Simscape Bus block. By default, this list is empty.
Every time you add a connection, a conserving port appears on the children side of the
block. Use the  or  buttons in the block dialog box to add or remove
connections.

You can also add and remove connections directly on the model canvas, as described
in Working with the Block on Model Canvas.

## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Bus for conserving connection lines

The Simscape Bus block bundles conserving connections into
a Simscape Bus line. You can also use this block to access one or more connections from an
existing Simscape Bus line. Physical connection lines are nondirectional, therefore, the block
can serve as both a bus creator and a bus selector. Typically, a model would have two
Simscape Bus blocks, facing each other, with their bus ports
connected.

However, a model can also contain a hierarchy of Simscape
Bus blocks.

Conserving connections bundled into a Simscape Bus line can belong to different
domains.

The block bundles only the Simscape™ conserving connections, that is, nondirectional connection lines between
Simscape conserving ports or Simscape
Multibody™ ports. It does not work with other types of connections, such as physical signal
lines.
For more information on conserving connections, see Physical Conserving Ports.

The Simscape Bus block can have ports on two sides:

- Parent (bundle) side, indicated by the black ribbon. This side contains a single bus
  port, which bundles all the connections coming into the block on the children side.
- Children (elements) side, opposite the parent side. This side does not have any ports
  by default. You add ports by dragging the connection lines to that side of the block, or
  by using the block dialog box. Elements coming into the block on the children side can be
  either conserving connection lines or Simscape Bus lines. Every time you add a port on the
  children side, the corresponding connection is added to the connections list inside the
  block.

The names of the connections are shown on the block icon, next to the corresponding ports
on the children side, and in the **Hierarchy Strings** list in the block
dialog box. You can edit these names in the dialog box or directly on the icon, if needed, by
clicking and typing a new name.

The block dialog box contains these buttons:

|  |  |
| --- | --- |
|  | Add a new connection name to the **Hierarchy Strings** list. The default connection names are `Connection1`, `Connection2`, and so on. You can edit these names, as needed, by selecting a row, then clicking it again and typing the new name. When you add a connection using this button, a round conserving port appears on the children side of the block, similar to that of a Connection Port block. The domain type of this conserving port is defined once you connect it to a conserving port on another block. After that, you can connect only the same type of port to the corresponding connection on the second bus. You can also add connections directly on the canvas, by dragging a connection line from a conserving port on another block to the children side of the Simscape Bus block. |
|  | Delete the selected connection from the **Hierarchy Strings** list. For unconnected ports, you can also delete them or edit their names directly on the canvas. |
|  | Refresh the **Hierarchy Strings** list after adding or removing connections on the canvas. |

### Working with the Block on Model Canvas

To add connections to a Simscape Bus block:

1. Select a conserving port on another block. Or, to create a hierarchy of
   Simscape Bus blocks, select a bus port on the parent
   side of another Simscape Bus block.
2. Drag a connection line from the selected port to the children side of the first
   Simscape Bus block.
3. A new connection with the default name is automatically added to the block
   connection list. You can edit the connection name, as needed, in the upper blue field.
   When done editing, select the connection name in the lower blue field to create the
   connection.

**Note**

- A Simscape Bus block cannot have multiple children
  connections to the same port. In other words, you cannot connect a conserving port on
  another block to the same Simscape Bus block more than
  once.
- You can create a hierarchy of Simscape Bus blocks
  by connecting a bus port on the parent side of a Simscape
  Bus block to a child port of another Simscape
  Bus block, but child connections between different
  Simscape Bus blocks are prohibited. In other words,
  you cannot connect a conserving port on a block to more than one
  Simscape Bus block.

When you delete a connection line, the corresponding port on the children side of the
block is not deleted. You can reuse it by connecting another block.

To delete unused ports:

- Select a round conserving port on the children side of a Simscape
  Bus block. Make sure to select just the port, not the whole block.
- From the ellipsis menu, select **Delete Port**. Deleting a port
  also deletes the corresponding name in the block connection list.

### Specifying Rigid Interfaces

You can lock down connection types for a Simscape Bus block by defining a
rigid interface specification. Design a rigid interface specifications for conserving
connections by using `Simulink.ConnectionBus` and
`Simulink.ConnectionElement` objects or by declaring composite domains.
When you apply such rigid specification to a Simscape Bus block, the block
ports become typed by the interface and do not accept connections to a different domain
type. This functionality helps you ensure the correct connection types within your model
architecture.

Use the **Connection type** parameter to apply a rigid interface
specification. For detailed information, see Apply a Rigid Interface Specification to a Simscape Bus Block and Example of a Custom Composite Domain.

When you apply a rigid interface specification to a Simscape Bus block:

- If the block previously had no ports on the children side, the block automatically
  adds children ports corresponding to the interface definition. In case of a nested bus
  definition, only the children ports in first level of the top bus appear
  automatically.
- If the block already had ports on the children side, these ports are not
  overwritten and the new ports do not appear automatically. Instead, the block
  validates the names and types of existing ports against the interface definition and
  reports connection errors, if found.

When you apply a rigid interface specification to a Simscape Bus block,
the block appearance changes to indicate a rigid bus. The bus (parent) port has a white
center and the block icon has a Refresh badge in the bottom-left corner.

Rigid Simscape Bus block appearance in model diagrams

When applying rigid interfaces, you can connect the bus (parent) ports of two
Simscape Bus blocks if they are both rigid and use the same interface
definition, or if one of the blocks is a rigid bus that uses a
`ConnectionBus` object and the other one is flexible (with
**Connection type** parameter set to `Inherit:
auto`). In both of these cases, the connection line style (double line)
indicates a rigid bus connection.

Connection line between two rigid Simscape Bus blocks

You cannot connect bus ports of a rigid bus that uses a composite domain interface and a
flexible bus.

To remove the rigid interface specification, set the **Connection
type** parameter to `Inherit: auto`.
