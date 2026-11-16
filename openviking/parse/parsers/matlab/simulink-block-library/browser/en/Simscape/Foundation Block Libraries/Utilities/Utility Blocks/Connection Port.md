---
type: simulink-block
title: 'Connection Port'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'connectionport'
documentation_source_path: 'ref/connectionport.html'
language: en
---

# Connection Port

## Ports

### Conserving

### **Port\_1** — Connection port untyped connection port

Physical modeling connection port. By default, this port is untyped.

You define the type of the port by connecting it to a conserving port or a
physical signal port of another block, or to a Simscape Bus port. Once
you establish a connection, the port appearance on the parent Subsystem
block changes accordingly, the port becomes typed and can be connected only to the
same type of port.

## Parameters

### **Port number** — Subsystem connector label `1` (default) | string that represents an integer number

Labels the subsystem connector port that this block creates. Each connector port
requires a unique number as a label. If you do not mask the parent subsystem and use the
default block name, the value of this parameter appears as a label next to the
corresponding port on the parent Subsystem block icon. If you change the
name of the Connection Port block, then the block name appears as a label
next to the corresponding port on the parent Subsystem block icon. You
can also use masking to change the subsystem port names. For more information, see Masking Fundamentals.

The default value for the first port is `1`. As you create more
ports, the software labels them incrementally. If you move the ports to a different
location on the Subsystem block icon, the Simulink Editor may renumber the ports, according to its rules. In this case, the
value of the **Port number** parameter of the corresponding
Connection Port block automatically changes to match the new port
number.

### **Port location on parent subsystem** — Connector port location on the subsystem block icon `Left` (default) | `Right`

Choose which side of the parent subsystem block the port is located:
`Left` or `Right`. If you move the port to a
different location on the Subsystem block icon, the parameter value
automatically changes to reflect the new placement. For more information, see Port Naming and Location on Subsystem Block.

### **Connection type** — Specify or remove rigid interface `Inherit: auto` (default) | `Bus: <object name>` | `CompositeConnection: <domain name>` | list of `ConnectionBus` objects, Foundation domains, and Simscape Multibody connection types

Specify a rigid interface by selecting a port type from the drop-down list. The list
contains the names of Foundation domains, Simscape
Multibody connection types, and `ConnectionBus` objects present in
the base workspace or a data dictionary. For more granularity, click the **Show
type assistant** button next to the drop-down list to display the
**Type Assistant** panel. You can also use the **Type
Assistant** panel to specify a rigid connection to a composite domain.

For more information, see Specifying Rigid Interfaces and Example of a Custom Composite Domain.

To remove the rigid interface specification, set the **Connection
type** parameter to `Inherit: auto`.

### **Mode** — Specify connection mode `Inherit` (default) | `Connection Bus object` | `Connection` | `Composite domain`

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
  `ConnectionBus` object. In this case, the Connection
  Port block can be connected only to a bus (bundle) port of a
  Simscape Bus block.
- `Connection` — Specify a rigid connection type by
  selecting a domain name or Simscape
  Multibody connection type from the drop-down list. The **Simscape
  Domains** link at the bottom of the dialog box lets you view the list of
  Foundation domain names and domain-specific line styles.
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

## Libraries

Simulink / Signal Routing Simscape / Utilities Powertrain Blockset / Utilities / Simscape RF Blockset / Equivalent Baseband / Input RF Blockset / Circuit Envelope / Utilities Vehicle Dynamics Blockset / Utilities / Simscape

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Physical Modeling connector port for subsystem

The Connection Port block transfers a physical connection or signal across
subsystem boundaries. Physical connections include Simscape™ conserving and physical signal connections, Simscape
Multibody™ connections, and Vehicle Dynamics Blockset™ two-way connection ports, among others. This block is similar in function to the
Inport and Outport blocks in the Simulink® library.

A subsystem needs a Connection Port block for each physical connection line
that crosses its boundary. You can manually place a Connection Port block
inside a subsystem, or Simulink can automatically insert a Connection Port block when you create
a subsystem within an existing network.

### Port Appearance on Subsystem Block

The Connection Port block adds a port to the parent
Subsystem block. The port type depends on the connection or signal it
transfers. The port appearance on the Subsystem block matches the port to
which the Connection Port block connects inside the subsystem. For example,
if the port transfers a Simscape conserving connection, then it appears on the Subsystem block
as a Simscape conserving port.

Consider a subsystem with Simulink input and output ports labeled **In** and
**Out**, respectively. If you place a Connection Port
block inside this subsystem and leave it unconnected, the connection port on the parent
Subsystem block appears as a white circle.

Block diagram with Connection Port block added to subsystem

Appearance of connection port on subsystem icon

However, if you connect the Connection Port block to a
Mass block, the appearance of the connection port on the
parent Subsystem block changes to a conserving port.

Block diagram with Connection Port block connected to Mass block

Changed appearance of connection port on subsystem icon

The connection port becomes typed as mechanical translational, that is, you can connect
only mechanical translational ports on other blocks to this subsystem port.

### Port Naming and Location on Subsystem Block

Similar to the Simulink input and output ports, the connection port on the subsystem icon displays the
port number instead of the block name when the port block has the default name. If you add a
Connection Port block with default name and parameters to a subsystem, the
connection port is labeled with the **Port number** parameter value and
located on the left side of the parent Subsystem block icon.

Connection port appears on the left side of subsystem icon

To switch the port to display on the right side of the icon, change the **Port
location on the parent subsystem** parameter value to
`Right`.

Connection port appears on the right side of subsystem icon

Flexible port placement in Simulink Editor lets you move ports by clicking and dragging the port along the block
icon outline, and this way you can put ports on any side of a Subsystem
block, including top and bottom. The **Port location on the parent
subsystem** parameter does not have separate values for top or bottom. If you
drag a port to a different location on the Subsystem block icon, the
parameter value automatically changes to reflect the new placement:

- `Left` — The port appears on the left or top side of the
  subsystem icon.
- `Right` — The port appears on the right or bottom side of
  the subsystem icon.

If there are multiple connection ports, the port index is automatically renumbered after
each move, as necessary, to reflect the new port location. For example, if a
Subsystem block has three connection ports, as shown, and you move port
**2** to the bottom of the block icon, ports **2** and
**3** are renumbered. The value of the **Port number**
parameter of these two Connection Port blocks automatically changes to match
the new port number.

Connection ports renumbered according to location on the subsystem block icon

The orientation of the parent Subsystem block can also affect the port
location. For example, if you flip the parent Subsystem block, the connection
port **1** appears on the opposite side to what its **Port location
on the parent subsystem** parameter indicates.

Connection port side flips when the subsystem block is flipped

### Specifying Rigid Interfaces

You can lock down the connection type for the block port by applying a rigid interface
specification. For example, you can restrict the block to accept connections only from the
mechanical translational ports on other blocks. For a list of Foundation domain types, see
Domain-Specific Line Styles. If you apply a rigid interface using a `ConnectionBus` object, the
Connection Port block can be connected only to a bus port of a
Simscape Bus block.

Use the **Connection type** parameter to specify a rigid interface,
such as a particular domain type or a `ConnectionBus` object. When you apply
a rigid interface definition, the block appearance changes, as shown:

1. Flexible connection
2. Rigid domain connection
3. Rigid bus connection

Connection port block appearance in model diagrams for different connection types

To remove the rigid interface specification, set the **Connection
type** parameter to `Inherit: auto`.
