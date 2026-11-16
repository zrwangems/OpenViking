---
type: simulink-block
title: 'J1939 Transmit'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939transmit'
documentation_source_path: 'io_ref/j1939transmit.html'
language: en
---

# J1939 Transmit

## Ports

### Input

### **Data** — Input data signal

Depending on the J1939 parameter group and signals defined in the J1939
database file, the block can have multiple data input ports.

### **Trigger** — Enables the transmission of message 0 | 1

Enables the transmission of the message for that sample. A value of
`1` specifies to send, a value of `0`
specifies not to send.

## Parameters

### **Config name** — Name of the J1939 network configuration to associate `ConfigX` (default) | character vector

The name of the J1939 network configuration to associate with. This is used to
access the corresponding J1939 database. Only the nodes defined in the model and
associated with the specified J1939 network configuration appear in the Node name
list. The option shows `none` if no J1939 network configuration
is found.

### **Node name** — Name of the J1939 node `NodeX` (default) | character vector

The name of the J1939 node. The drop-down list includes all the nodes in the
model, both custom nodes and nodes from the database.

### **Parameter Group** — Group number (PGN) and name int8

The parameter group number (PGN) and name from the database. The contents of
this list vary depending on the parameter groups that the J1939 database file
specifies. The default is the first parameter group for the selected node.

If you change any parameter group settings within your J1939 database file, you
must then open the J1939 Transmit block dialog box and select the same
**Parameter Group**, then click **OK** or
**Apply** to update the parameter group information in the
block.

### **Signals** — Signals defined in parameter group array of character vectors

Signals defined in the parameter group. The **Min** and
**Max** settings are read from the database, but by default
the block does not clip signal values that exceed this range.

### **PG Priority** — Priority of the parameter group int8

Priority of the parameter group, read from the database. This priority setting
resolves clashes of multiple parameter groups transmitting on the same bus at the
same time. If a conflict occurs, the priority group with lower priority (higher
value) will refrain from transmitting. The value can range from 0 (highest
priority) to 7 (lowest).

### **Destination Address** — Name of the destination node int8

The name of the destination node. The default is the first node defined in the
database, otherwise `Custom`.

For a custom destination address, you can specify 0–253 for the address of the
destination node. For broadcasting to all nodes, use the `Custom`
**Destination Address** setting with an address of
`255`.

### **Sample time** — Simulation transmit rate `-1` (default) | double

The simulation transmit rate, specified as the sampling time of the block
during simulation. This value defines the frequency at which the J1939
Transmit block transmits messages. The default value of
`-1` is used when the block is inside a triggered subsystem or
inherits a sample time. You can also specify a MATLAB® variable for sample time. For information about simulation sample
timing, see What Is Sample Time?.

## Libraries

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Transmit J1939 message

The J1939 Transmit block transmits a J1939 message. The J1939 database file defines the
nodes and parameter groups. You specify the J1939 database by using the J1939 Network
Configuration block.

To use this block, you must have a license for both Vehicle Network Toolbox™ and Simulink® software.

The J1939 communication blocks support the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution of
your models by using these modes. For more information, see Acceleration.

The J1939 communication blocks also support code generation that have limited deployment
capabilities. Code generation requires a C++ compiler that is compatible with the code
generation target. For the current list of supported compilers, see Supported and Compatible Compilers.
