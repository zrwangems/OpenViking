---
type: simulink-block
title: 'J1939 Node Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939nodeconfiguration'
documentation_source_path: 'ug/j1939nodeconfiguration.html'
language: en
---

# J1939 Node Configuration

## Ports

### Output

### **Address** — Returns the effective address of the node int8

This optional output port exists when you select the **Output current node
address** check box in the dialog box.

### **AC Status** — Indicates the success (1) or failure (0) of the node’s address claim 0 | 1

This optional output port exists when you select the **Output address claim
status** check box in the dialog box.

## Parameters

### **Config name** — ID of the J1939 network configuration to associate with this node `ConfigX` (default) | character vector

To access the corresponding J1939 database, use this ID.

### **Node name** — name of this J1939 node `NodeX` (default) | character vector

The available list shows `none` if no J1939 network configuration
is found or no node is defined in the associated database. If you are creating a custom
node, the node name must be unique within its J1939 network configuration.

### **Message** — Nine network attributes as defined by the database file consistent with the J1939 protocol vector array

Unless you are defining a custom node, these parameters are read-only:

- **Allow arbitrary address** — Allow/disallow the node to
  switch to an arbitrary address if the station address is not available. If this
  option is off and the node loses its address claim, the node goes silent.

  **Node Address** — Station address, decimal,
  8-bit.
- **Industry Group** — Decimal, 3-bit.
- **Vehicle System** — Decimal, 7-bit.
- **Vehicle System Instance** — Identifies one particular
  occurrence of a given vehicle system in a given network. If only one instance of a
  certain vehicle system exists in a network, then this field must be set to 0 to
  define it as the first instance. Decimal, 4-bit.
- **Function ID** — Decimal, 8-bit.
- **Function Instance** — Identifies the particular
  occurrence of a given function in a vehicle system and given network. If only one
  instance of a certain function exists in a network, then this field must be set to 0
  to define it as the first instance. Decimal, 5-bit.
- **ECU Instance** — This 3-bit field is used when
  multiple electronic control units (ECU) are involved in performing a single
  function. If only one ECU is used for a particular controller application (CA), then
  this field must be set to 0 to define it as the first instance.
- **Manufacturer Code** — Decimal, 11-bit.
- **Identity Number** — Decimal, 21-bit.

### **Sample time** — Simulation refresh rate 0.01 (default) | double

Specify the sampling time of the block during simulation. This value defines the
frequency at which the J1939 Node Configuration updates its optional output ports. If
the block is inside a triggered subsystem or inherits a sample time, specify a value of
`-1`. You can also specify a MATLAB® variable for sample time. The default value is `0.01`
simulation seconds. For information about simulation sample timing, see Timing in Hardware Interface Models.

### **Output current node address** — Enable or disable the Address port display `off` (default) | `on`

Enable or disable the **Address** output port to show the effective
address. The effective address is different from the predefined station address. If
**Allow arbitrary address** is selected, a name conflict occurs, and
the current node has lower priority. The output signal is a double value from 0 to 253.
This port is disabled by default.

### **Output address claim status** — Enable or disable the address claim AC Status display `off` (default) | `on`

Enable or disable the address claim **AC Status** output port to
show the success of an address claim. The output value is binary, 1 for success or 0 for
failure. This port is disabled by default.

## Libraries

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Configure J1939 node with address and network management attributes

The J1939 Node Configuration block is where you define a node and associate it with a
specific network configuration. Its Message information is read from the database for that
configuration, unless you are creating and configuring a custom node.

To use this block, you must have a license for both Vehicle Network Toolbox™ and Simulink® software.

The J1939 communication blocks support the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution of
Simulink models by using these modes. For more information on these modes, see Acceleration (Simulink).

The J1939 communication blocks also support code generation that have limited deployment
capabilities. Code generation requires a C++ compiler that is compatible with the code
generation target. For the current list of supported compilers, see Supported and Compatible Compilers.
