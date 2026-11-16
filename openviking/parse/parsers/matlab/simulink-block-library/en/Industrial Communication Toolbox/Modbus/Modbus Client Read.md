---
type: simulink-block
title: 'Modbus Client Read'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'Modbus'
documentation_page: 'modbusclientread'
documentation_source_path: 'ug/modbusclientread.html'
language: en
---

# Modbus Client Read

## Ports

### Output

### **Reg\_*`x`*** — Current values of registers vector

Values read from Modbus TCP/IP or serial server. The number of output ports
(*x*) corresponds to the number of rows you add in the Registers parameter. The data
at each port is of size 1-by-*N*, where *N*
corresponds to the number of consecutive registers to read. The value of
*N* is specified in the `Count` field of the
**Registers** parameter. The block reads the values
from *N* consecutive registers starting with the register address
specified in the `Address` field of the **Registers** parameter.

#### Dependencies

To enable this port, specify one or more registers in the
**Registers** parameter.

**Data Types:** `double`

## Parameters

### **Client** — Select Modbus client drop-down list

Select the Modbus client to associate with the block. The block updates the
**Connection endpoint** parameter once you select a client.

- To add the clients using the **Modbus** pane,
  click **Configure clients**. For more information, see Configure Modbus Client in Simulink.
- To update the client list and to show the latest Modbus clients, click
  **Refresh**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ClientList` |
| **Values:** | Modbus client name |
| **Data Types:** | `character vector` | `string` |

### **Server ID** — Address of the server 1 (default) | nonnegative integer in the range [0, 255]

Server address to read from, specified as a nonnegative integer in the range [0,
255]. The default value is 1. The server address refers to the unit identifier for the
Modbus TCP/IP server.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ServerId` |
| **Values:** | 1 (default) | nonnegative integer in the range [0, 255] |
| **Data Types:** | `double` |

### **Registers** — List of Modbus registers table

Add registers to read from the specified client.

- To add a register, click **Add**. This action adds a row in
  the **Registers** table with `Name`,
  `Register Type`, `Precision` and
  `Count` set to the default values of `Reg_1`,
  `Holding Register`, `uint16` and
  `1`, respectively. You must specify an address for the register
  to read from in the `Address` column. Each time you click
  **Add**, the block adds a new row in the
  **Registers** table and increments the name by 1.

  - `Sl`. `no`. : This field is
    noneditable and specifies the serial number of the register. The serial
    number determines the order in which the block outputs the signals at the
    output ports.
  - `Name`: This is an editable text field that specifies a
    name for the register. This field also defines the names for the output
    ports.
  - `Address`: This is an editable text field that
    specifies a starting address for the Modbus read operation.
  - `Register Type`: This is a drop-down list that
    specifies the target area to read. You can perform a Modbus read operation
    on four types of targets: coils, inputs, input registers, and holding
    registers.
  - `Precision`: This is a drop-down list that specifies
    the data format of the read register. Note that the
    `Precision` field does not refer to the data type of the
    block output. The data type of the output is always
    `double`. `Precision` specifies how the
    block interprets the register data.

    - For coils and inputs, set this field to
      `bit`.
    - For holding registers and input registers, set this field to
      `int16`, `uint16`,
      `int32`, `uint32`,
      `single`, `double`,
      `int64` or `uint64`.
  - `Count`: This is an editable text field that specifies
    the number of registers to read starting from the address specified in the
    corresponding `Address` field.
- To delete registers, select the registers and click
  **Delete**.
- To import a register table saved as a MAT file, click
  **Import**. This action opens the Load register table dialog
  box for the current workspace. Using this browser, you can select the MAT file
  with the register information. The MAT file that you select must have a table
  named `ModbusRegisterTable`.

  **Note**

  The Modbus Explorer app exports the contents of the register table as a
  MAT file. You can import this MAT file into the Modbus Client Simulink blocks to reuse the register table. For more information, see
  Use the Modbus Explorer App.
- To save the register table as a MAT file, click **Export**.
  This action opens the Save register table dialog box for the current workspace.
  Using this browser, you can save the register table as a MAT file in the location
  of your choice. The default filename is
  `ModbusRegisterTable.mat`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RegisterTable` |
| **Values:** | register name and information |
| **Data Types:** | `character vector` | `string` |

### **Block sample time** — Sample time for read operation -1 (default) | nonnegative scalar

Define the sample time of the block in seconds. The block reads the data from the
server synchronously at the specified sample time. For more information, see Specify Sample Time (Simulink).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | -1 (default) | nonnegative scalar |
| **Data Types:** | `double` |

## Libraries

Industrial Communication Toolbox / Modbus

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Limitations:

- This block generates platform-specific code for the host machine's platform only
  (Windows®, macOS, Linux®).
- You cannot have more than one Modbus Client block (Read or Write) in a model
  connected to the same serial port of a Modbus serial
  server.

## Version History

**Introduced in R2024b**

## Description

Read data from Modbus server

The Modbus Client Read block reads data from one or more registers on a
Modbus® TCP/IP or serial server.

Each output port returns data from a corresponding register specified in the
**Registers** parameter of the block. The data at the output ports is of
size 1-by-*N*, where *N* corresponds to the number of
consecutive registers to read specified in the **Registers**
table.

**Note**

You need a license for Industrial Communication Toolbox™ and Simulink® to use this block.

**Note**

You must connect the Modbus Client Read block to a Modbus TCP/IP or serial server. You
can create the client to connect to the Modbus TCP/IP or serial server using the
**Modbus** pane in the Configuration Parameters dialog box of the model.
You must add at least one Modbus Client Read or Modbus Client Write
block in the model to enable this pane. For more information, see Configure Modbus Client in Simulink.

### Other Supported Features

The Modbus Client Read block supports the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution of
Simulink models by using these modes. For more information on these simulation modes,
see Acceleration (Simulink).
