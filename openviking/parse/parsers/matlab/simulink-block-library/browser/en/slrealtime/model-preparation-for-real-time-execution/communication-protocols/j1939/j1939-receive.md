---
type: simulink-block
title: 'J1939 Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / J1939'
documentation_page: 'j1939receive'
documentation_source_path: 'io_ref/j1939receive.html'
language: en
---

# J1939 Receive

## Ports

### Output

### **Data** — Data output double

Depending on the J1939 parameter group defined in the J1939 database file,
the block can have multiple data output signal ports. The block output data
type is double.

### **Msg Status** — Message received status 0 | 1

When you select the **Output New Message Received status**
check box in the parameters dialog, this port outputs `1` when a new
message is received from the CAN bus. Otherwise, this port outputs
`0`.

## Parameters

### **Config name** — Name of the J1939 network configuration to associate `ConfigX` (default) | character vector

The name of the J1939 network configuration to associate. This value is used to
access the corresponding J1939 database. Only the nodes defined in the model and
associated with the specified J1939 network configuration appear in the Node name list.
The option shows `none` if no J1939 network configuration is
found.

### **Node name** — Name of the J1939 node `NodeX` (default) | character vector

The name of the J1939 node. The drop-down list includes all the nodes in the model,
both custom nodes and nodes from the database.

### **Parameter Group** — Parameter group number (PGN) and name from database character vector

The parameter group number (PGN) and name from the database. The contents of this
list vary depending on the parameter groups that the J1939 database file specifies. The
default is the first parameter group for the selected node.

If you change any parameter group settings within your J1939 database file, open the
J1939 Receive block dialog box and select the same **Parameter Group**
and click **OK** or **Apply**.

### **Signals** — Signals defined in the parameter group array of character vectors

Signals that are defined in the parameter group. The **Min** and
**Max** settings are read from the database, but by default the block
does not clip signal values that exceed this range.

### **Source Address Filter** — Filter messages based on source address `Allow all` (default) | `Allow only`

Filter messages based on source address are:

- `Allow only` — Specify a single source address.
- `Allow all` — Accepts messages from any source address.
  This option is the default.

### **Destination Address Filter** — Filter out message based on destination address `global and node specific` (default) | `global only` | `node specific only`

Filter out a message based on the destination address:

- `global only` — Receive only broadcast messages.
- `node specific only` — Receive only messages addressed
  to this node.
- `global and node specific` — Receive all broadcast and
  node-addressed messages. This option is the default.

### **Sample time** — Simulation refresh rate `0.01` (default) | double

The simulation refresh rate. Specify the sampling time of the block during
simulation. This value defines the frequency at which the J1939 Receive
block updates its output ports. If the block is inside a triggered subsystem or inherits
a sample time, specify a value of `-1`. You can also specify a
MATLAB® variable for sample time. The default value is `0.01`
simulation seconds. For information about simulation sample timing, see What Is Sample Time?.

### **Output New Message Received status** — Create a Msg Status output 0 (default) | 1

Select this check box to create a **Msg Status** output port. Its
output signal indicates a new incoming message, showing 1 for a new message received, or
0 when there is no new message.

## Libraries

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Receive J1939 parameter group messages

The J1939 Receive block receives a J1939 message from the configured CAN device. The J1939
database file defines the nodes and parameter groups. You specify the J1939 database by using
the J1939 Network Configuration block.

To use this block, you must have a license for both Vehicle Network Toolbox™ and Simulink® software.

The J1939 communication blocks support the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution of
Simulink models by using these modes. For more information on these modes, see Acceleration.

The J1939 communication blocks also support code generation that have limited deployment
capabilities. Code generation requires a C++ compiler that is compatible with the code
generation target. For the current list of supported compilers, see Supported and Compatible Compilers.
