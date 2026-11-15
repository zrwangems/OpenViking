---
type: simulink-block
title: 'Serial Receive'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Interface-Based Instrument Communication / Serial Port Interface'
documentation_page: 'serialreceive'
documentation_source_path: 'serialreceive.html'
language: en
---

# Serial Receive

## Ports

### Output

### **Data** — Data received vector | matrix | array

Data received by the block from the serial port, returned as a vector, matrix, or
array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — New data available `false` or `0` (default) | `true` or `1`

New data available status, returned as numeric or logical `1`
(`true`) or `0` (`false`). If
this port returns `1`, new data is available to be read.

#### Dependencies

To enable this port, unselect the **Enable blocking mode**
parameter.

**Data Types:** `Boolean`

## Parameters

### **Port** — Serial communication port available communication ports

Serial port on your machine that you want to receive data from. Select a port from
the available ports and then configure the port using the Serial
Configuration block. If you have not configured a port, the block returns an
error when you run your model.

**Note**

Each Serial Receive block must have a configured Serial
Configuration block. If you use multiple serial ports in your simulation,
you must configure each port using a separate Serial Configuration
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |

### **Data type** — Output data type `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32`

Data type that the block receives from the serial port, specified as a MATLAB® numeric data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector, string |
| **Values:** `'uint8'` | `'single'` | `'double'` | `'int8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **Default:** `'uint8'` |

### **Header** — Header numeric array | integer from 0 to 255, inclusive

If this parameter is selected, you can specify the header that indicates the
beginning of your data block. The simulation disregards data that occurs before the
header. The header data is not sent to the output port. By default, this parameter is
not selected and no header is specified.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

You can also specify this parameter using the hexadecimal representation
of the ASCII
characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ToggleHeader` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `Header` |
| **Type:** character vector, string |
| **Values:** integer array |

### **End token** — Terminator `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

If this parameter is selected, you can specify the end token or terminator that
indicates the end of your data block. The simulation considers any data that occurs
after the end token as a new data block. The end token data is not sent to the output
port. This end token must match the one in the data you are reading from your serial
port, if it has one.

If you select `Custom Terminator`, you can specify your own
end token value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ToggleTerminator` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `Terminator` |
| **Type:** character vector, string |
| **Values:** `'<none>'` | `'CR ('\r')'` | `'LF ('\n')'` | `'CR/LF ('\r\n')'` | `'NULL ('\0')'` | `'Custom Terminator'` |
| **Default:** `'<none>'` |

### **Custom terminator** — Custom terminator numeric array | integer from 0 to 255, inclusive

Custom terminator that indicates the end of your data block, used when **End
token** is set to `'Custom Terminator'`. The simulation
considers any data that occurs after the terminator as a new data block. The terminator
data is not sent to the output port.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"End"` | `uint8('End')` | `[69 110 100]` |

You can also specify this parameter using the hexadecimal representation
of the ASCII characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomTerminator` |
| **Type:** character vector, string |
| **Values:** integer array |

### **Input Format** — Format of data read `Column major` (default) | `Row major`

Format of the data that the block receives from the serial port, specified as
`Row major` or `Column
major`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputFormat` |
| **Type:** character vector, string |
| **Values:** `'Row major'` | `'Column major'` |
| **Default:** `'Column major'` |

### **Data size** — Number of values read `[1 1]` (default) | numeric array

Output data size, or the number of values that should be read at each simulation
time step. This parameter is specified as a multidimensional numeric array. The data
size does not include the header or terminator values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataSize` |
| **Type:** character vector, string |
| **Values:** integer array |
| **Default:** `'[1 1]'` |

### **Enable blocking mode** — Simulation waits while receiving data `on` (default) | `off`

This parameter has the simulation wait while the block receives data. When new data
becomes available, the simulation continues from the next time step. Unselect the check
box if you do not want the read operation to cause the simulation to wait.

If you enable blocking mode, the simulation waits for the requested data to become
available. The model waits for up to the amount of time specified by the
**Timeout** parameter in the Serial Configuration
block. If new data does not become available during a simulation, you can return an
error by selecting the `Error` option for the **Action
when data is not available** parameter.

If you do not enable blocking mode, the simulation runs continuously and the block
has two output ports, **Status** and **Data**. The
**Data** port contains the requested set of data at each time step.
The **Status** port contains 0 or 1 based on whether it received new
data at the given time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableBlockingMode` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Action when data is not available** — Action to take when data not available `Output last received value` (default) | `Output custom value` | `Error`

Action the block should take when data is not available. Available options are:

- `Output last received value` — Block returns the
  value it received at the preceding time step when it does not receive data at
  current time step.
- `Output custom value` — Block returns any
  user-defined value when it does not receive current data. Define the custom value
  in the **Custom value** field.
- `Error` — Block returns an error when it does not
  receive current data. You must select **Enable blocking mode** to
  use this option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ActionDataUnavailable` |
| **Type:** character vector, string |
| **Values:** `'Output last received value'` | `'Output custom value'` | `'Error'` |
| **Default:** `'Output last received value'` |

### **Custom value** — Custom output value when data unavailable 0 (default) | numeric

Custom value for the block to output when it does not receive new data. The custom
value can be a scalar or value equal to the size of data that it receives (specified by
**Data size** parameter). You must select `Output custom
value` as the **Action when data is unavailable** to set
this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomValue` |
| **Type:** character vector, string |
| **Values:** numeric |
| **Default:** `'0'` |

### **Block sample time** — Sampling time 0.01 (default) | positive numeric

Sampling time of the block during the simulation. This is the rate at which the
block is executed during simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector, string |
| **Values:** positive numeric |
| **Default:** `'0.01'` |

## Libraries

Instrument Control Toolbox Motor Control Blockset / Protection and Diagnostics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block generates platform-specific code for the host machine's platform only
(Windows®, macOS, Linux®).

## Version History

**Introduced in R2008a**

## Description

Receive binary data over serial port

The Serial Receive block configures and opens an interface to the specified
serial port. The configuration and initialization occur once at the start of the model's
execution. The block acquires data from the serial port during the model's run time. You can
use only one Serial Receive block at a time to receive data from a specific
serial port.

**Note**

You must configure your serial port parameters using the Serial
Configuration block before you specify the Serial Receive block
parameters.

This block has no input ports. It has one or two output ports based on whether you select
blocking or non-blocking mode. If you select blocking mode, the block has one output port,
**Data**, corresponding to the data it receives. If you do not select
blocking mode, the block has two output ports, **Data** and
**Status**.

This block uses a First In, First Out (FIFO) buffer to receive data from the serial port.
At each time step, the **Data** port returns the requested values from the
buffer. In non-blocking mode, the **Status** port indicates if the block has
received new data. If the **Status** port displays `1`, new
data is available and if the **Status** port displays
`0`, no new data is available.

### Other Supported Features

- The Serial Receive block supports the use of Simulink® Accelerator mode, but not Rapid Accelerator. This feature speeds up the
  execution of Simulink models.
- The Serial Receive block supports the use of model referencing. This
  feature lets your model include other Simulink models as modular components.
- The Serial Receive block supports C/C++ code generation. This feature
  allows you to generate C and C++ code using Simulink
  Coder™.

For more information on these features, see the Simulink
documentation.
