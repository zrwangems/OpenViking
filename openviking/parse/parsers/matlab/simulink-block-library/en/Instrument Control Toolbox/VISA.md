---
type: simulink-block
title: 'VISA'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'visablock'
documentation_source_path: 'visablock.html'
language: en
---

# VISA

## Ports

### Input

### **Input** — Data to send vector | matrix | array

Data values to send from the block to your VISA resource, specified as a vector,
matrix, or array.

#### Dependencies

- To enable this port, set **Send command type** to
  **Compose command from input data** or **Send input
  port data as is** in the **Send or Query**
  tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Data** — Data received vector | matrix | array

Data received by the block from your VISA resource, returned as a vector, matrix,
or array.

#### Dependencies

- To enable this port, set **Use block to** to
  **Query instrument** or **Receive response**
  in the **Send or Query** tab.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Status** — Instrument status `1` | `0`

Instrument status, returned as `1` or `0`, where
`1` represents success and `0` represents
failure.

#### Dependencies

- To enable this port, set **Action when error occurs** to
  `Continue simulation` in the **Handle
  Error** tab.

**Data Types:** `double`

### **Instrument error** — Error message from instrument string

Error message from instrument, returned as a string.

#### Dependencies

- To enable this port, set **Action when error occurs** to
  `Continue simulation` and select the **Check
  instrument error** parameter in the **Handle
  Error** tab.

**Data Types:** `string`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block parameters

### **Block sample time** — Time interval between samples -1 (default) | numeric

Sampling time of the block during the simulation. This is the rate at which the
block is executed during simulation. For more information, see Timing in Hardware Interface Models.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | number in quotes |

**Example:** `set_param(gcb,"SampleTime","1")`

### Hardware Configuration

#### Select from resource list

### **Resource name** — VISA resource name available VISA resources

VISA resource on your machine that you want to connect to and communicate with.
Each type of VISA interface has a different format. For more information, see
ResourceName.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ResourceName` |
| **Values:** | resource name |

**Example:** `set_param(gcb,"ResourceName","ASRL4::INSTR")`

### **Vendor** — Instrument manufacturer Read-only: instrument manufacturer name

This parameter is read-only.

Instrument manufacturer. This parameter is empty if the VISA interface type does
not provide information about the manufacturer.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `VendorName` |
| **Values:** | Read-only: vendor name |

**Example:** `get_param(gcb,"VendorName")`

### **Model** — Instrument model Read-only: instrument model name

This parameter is read-only.

Instrument model. This parameter is empty if the VISA interface type does not
provide information about the model.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ModelName` |
| **Values:** | Read-only: model name |

**Example:** `get_param(gcb,"ModelName")`

### **Serial Number** — Unique serial number associated with instrument Read-only: instrument serial number

This parameter is read-only.

Unique serial number associated with instrument. This parameter is empty if the
VISA interface type does not provide information about the serial number.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SlNumber` |
| **Values:** | Read-only: serial number |

**Example:** `get_param(gcb,"SlNumber")`

#### Configure new VISA resource

### **VISA resource type** — Type of VISA resource to configure `TCP/IP Socket` (default) | `TCP/IP HiSLIP` | `TCP/IP VXI-11`

Type of VISA resource to manually configure to make a connection to. After you
select a VISA resource type for the resource you want to connect to, you can specify
the parameters for that resource and create a connection to it.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Interface` |
| **Values:** | `"TCP/IP Socket"` (default) | `"TCP/IP HiSLIP"` | `"TCP/IP VXI-11"` |

**Example:** `set_param(gcb,"Interface","TCP/IP
VXI-11")`

### **Board index** — Board index to connect to positive integer

Board index of VISA resource that you want to connect to. For VISA-TCP/IP
resources, this is the index number of the network board associated with an
instrument.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `BoardNumber` |
| **Values:** | positive number in quotes |

**Example:** `set_param(gcb,"BoardNumber","5")`

### **IP address** — IP address to connect to IP address

IP address of VISA resource that you want to connect to. For VISA-TCP/IP
resources, this is the TCP/IP address of the socket in dot-decimal notation.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `IPAddress` |
| **Values:** | IP address in dot-decimal notation in quotes |

**Example:** `set_param(gcb,"IPAddress","127.0.0.1")`

### **Port number** — Port number to use for connection `4880` (default) | positive integer

Port number that your VISA-TCP/IP resource is connected through, specified as a
number between 1 and 65535, inclusive.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.
- To enable this parameter, **VISA resource type** must be
  `TCP/IP Socket` or `TCP/IP HiSLIP`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `"4880"` (default) | positive number in quotes |

**Example:** `set_param(gcb,"Port","80")`

### **Device ID** — ID of device to connect to positive integer

Device ID number of the VISA-TCP/IP resource that you want to connect to.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.
- To enable this parameter, **VISA resource type** must be
  `TCP/IP HiSLIP` or `TCP/IP VXI-11`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DeviceID` |
| **Values:** | positive number in quotes |

**Example:** `set_param(gcb,"DeviceID","1")`

#### Specify resource name

### **Resource name** — VISA resource name VISA resource name

VISA resource on your machine that you want to connect to and communicate with.
Each type of VISA interface has a different format. For more information, see
ResourceName.

#### Dependencies

- To enable this parameter, select the **Specify resource
  name** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ResourceString` |
| **Values:** | resource name in quotes |

**Example:** `set_param(gcb,"ResourceString","GPIB0::5::INSTR")`

#### Configure connection

### **EOI Mode** — EOI mode `on` (default) | `off`

Whether the EOI (end or identify) line is asserted at the end of a write
operation.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `EOIMode` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param(gcb,"EOIMode","off")`

### **Byte order** — Sequential order of bytes `little-endian` (default) | `big-endian`

Sequential order in which bytes are arranged into larger numerical values.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** or **Specify resource name** option
  from **Select and configure hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ByteOrder` |
| **Values:** | `"little-endian"` (default) | `"big-endian"` |

**Example:** `set_param(gcb,"ByteOrder","big-endian")`

### **Read terminator** — Terminator character for reading data `off` (default) | `LF` | `CR` | `CR/LF` | 0 to 255

Terminator character for reading ASCII-terminated data, specified as
`off`, `LF`, `CR`,
`CR/LF`, or a number from 0 to 255, inclusive. When reading from
the remote host with a terminator value of `CR/LF`, the read
terminates on an occurrence of `CR` and `LF`
together. If the terminator value is `off`, read operations ignore
terminator characters.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ReadTerminator` |
| **Values:** | `"off"` (default) | `"LF"` | `"CR"` | `"CR/LF"` | 0 to 255 in quotes |

**Example:** `set_param(gcb,"ReadTerminator","CR")`

### **Write terminator** — Terminator character for writing data `LF` (default) | `CR` | `CR/LF` | 0 to 255

Terminator character for writing ASCII-terminated data, specified as
`LF`, `CR`, `CR/LF`, or a number
from 0 to 255, inclusive. When writing to the remote host with a terminator value of
`CR/LF`, the write terminates by adding both `CR`
and `LF`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `WriteTerminator` |
| **Values:** | `"LF"` (default) | `"CR"` | `"CR/LF"` | 0 to 255 in quotes |

**Example:** `set_param(gcb,"WriteTerminator","CR")`

### **Data bits** — Number of bits to represent one character of data `8` (default) | `5` | `6` | `7`

Number of data bits to transmit over your VISA resource.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DataBits` |
| **Values:** | `"8"` (default) | `"5"` | `"6"` | `"7"` |

**Example:** `set_param(gcb,"DataBits","5")`

### **Parity** — Parity bit type `none` (default) | `even` | `odd`

Parity bit type added to data transmitted by your VISA resource. You can use this
parameter to add a parity bit (also referred to as a check bit) to your data. Adding a
parity bit to a string of binary code is a method of detecting errors in data
transmission by ensuring that the total number of 1-bits is even or odd.

The value of the parity bit is determined by the number of 1s in a given set of
bits and is set as follows.

| Parity Bit Type | Parity Bit Value | |
| --- | --- | --- |
| If number of 1s is even | If number of 1s is odd |
| `none` | No parity bit set | No parity bit set |
| `even` | 0 | 1 |
| `odd` | 1 | 0 |

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Parity` |
| **Values:** | `"none"` (default) | `"even"` | `"odd"` |

**Example:** `set_param(gcb,"Parity","even")`

### **Stop bits** — Pattern of bits that indicates the end of a character `1` (default) | positive scalar

Number of bits used to indicate the end of a byte. This parameter depends on the
value you select for the **Data bits** parameter. If you select data
bits `6`, `7`, or
`8`, the default value is `1` and the
other available choice is `2`. If you select data bit
`5`, the default value is `1` and the
other available choice is `1.5`.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `StopBits` |
| **Values:** | `"1"` (default) | positive scalar |

**Example:** `set_param(gcb,"StopBits","2")`

### **Flow control** — Mode for managing data transmission rate `none` (default) | `hardware` | `software`

Process of managing the rate of data transmission on your VISA resource. Select
`none` to have no flow control,
`hardware` to let your hardware determine the flow control,
or `software` to let your software determine the flow
control.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FlowControl` |
| **Values:** | `"none"` (default) | `"hardware"` | `"software"` |

**Example:** `set_param(gcb,"FlowControl","hardware")`

### **Baud rate** — Communication speed 9600 (default) | positive integer

Rate at which bits are transmitted for your VISA resource, in bits per
second.

#### Dependencies

- To enable this parameter, select the **Select from resource
  list** option from **Select and configure
  hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `BaudRate` |
| **Values:** | `"9600"` (default) | positive integer |

**Example:** `set_param(gcb,"BaudRate",14400)`

### **Timeout** — Allowed time to complete operations 10 (default) | numeric

Allowed time in seconds to complete read and write operations.

#### Dependencies

- To enable this parameter, select the **Configure new VISA
  resource** or **Specify resource name** option
  from **Select and configure hardware**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `TimeOut` |
| **Values:** | 10 (default) | numeric |

**Example:** `set_param(gcb,20)`

#### Validate and test connection

### **Instrument identification command** — SCPI command to send to your instrument `*IDN?` (default) | SCPI command

Instrument identification SCPI command that you send to your instrument to see its
response. Use this command to test that you are able to successfully establish a
connection with your VISA resource.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `TestCommand` |
| **Values:** | `"*IDN?"` (default) | SCPI command in quotes |

**Example:** `set_param(gcb,"TestCommand","*IDN?")`

### **Validate and test connection** — VISA resource connection verification button

Click this button to send your VISA resource the SCPI command specified in
**Instrument identification command** and return a value in
**Response**.

### **Response** — Instrument query response Read-only: string scalar

This parameter is read-only.

Instrument response to SCPI command specified in **Instrument
identification command**. This field is populated after you click
**Validate and test connection**.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Response` |
| **Values:** | Read-only: instrument response in quotes |

**Example:** `get_param(gcb,"Response")`

### Instrument Initialization

#### Initialization commands

### **Initialization commands** — SCPI command to send to your instrument `*RST;*CLS` (default) | SCPI command

Instrument initialization SCPI commands that you send to your instrument. If you
have multiple commands, separate each with a semicolon (`;`). Each
command is sent one after another. These commands are executed once during simulation.
Click the **Upload initialization commands and check instrument error
status** button to send these commands to your instrument.

#### Dependencies

- To enable this parameter, select the **Initialization
  commands** option from **Send initialization
  commands**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SendString` |
| **Values:** | `"*RST;*CLS"` (default) | SCPI command in quotes |

**Example:** `set_param(gcb,"SendString","SOURce1:FUNCtion
SQU")`

#### MATLAB Code

### **MATLAB Code** — MATLAB® code to send to your instrument MATLAB code

Instrument initialization MATLAB script to send to your instrument. When writing this code, use
`visaObj` as the VISA object that represents a connection to your
instrument. You can use the `write` function to send your
instrument ASCII initialization commands. Click the **Upload initialization
commands and check instrument error status** button to send this code to
your instrument.

#### Dependencies

- To enable this parameter, select the **MATLAB Code**
  option from **Send initialization commands**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ExecuteFunction` |
| **Values:** | MATLAB code in quotes |

**Example:** `set_param(gcb,"ExecuteFunction","write(visaObj,'SOURce1:FUNCtion
SQU')")`

#### Test instrument initialization commands

### **Instrument error check command** — SCPI command to send to your instrument `SYSTem:ERRor?` (default) | SCPI command

Instrument error check SCPI command that you send to your instrument to see its
response. If you have specified any initialization SCPI commands or MATLAB code, this command is sent after them.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InitTestCommand` |
| **Values:** | `"SYSTem:ERRor?"` (default) | SCPI command in quotes |

**Example:** `set_param(gcb,"InitTestCommand","SYSTem:ERRor?")`

### **Upload initialization commands and check instrument error status** — Initialization and error check commands upload button

Click this button to send your instrument any initialization commands that you
specified in either **Initialization commands** or
**MATLAB Code**, followed by the error check command specified in
**Instrument error check command**. Depending on the status of
the instrument, the instrument sends a response that is displayed in the
**Instrument status** field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

### **Instrument status** — Instrument initialization response Read-only: string scalar

This parameter is read-only.

Instrument response to the initialization commands specified in either
**Initialization commands** or **MATLAB
Code**. If the commands are accepted by the instrument this field displays a
success message. If the instrument is in an error state, the status reflects
that.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `initStatus` |
| **Values:** | Read-only: instrument response in quotes |

**Example:** `get_param(gcb,"initStatus")`

### Send or Query

#### Send command

### **SCPI Command** — SCPI command to send to your instrument SCPI command

Data to send to your instrument as a SCPI command. The SCPI command you send must
be supported by your instrument.

#### Dependencies

- To enable this parameter, select the **SCPI command**
  option from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `StaticCommand` |
| **Values:** | SCPI command in quotes |

**Example:** `set_param(gcb,"StaticCommand","SYST:PON:TIME?")`

### **Binary command** — Binary command to send to your instrument binary values

Data to send to your instrument as binary data. The values must be between 0 and
256.

#### Dependencies

- To enable this parameter, select the **Binary** option
  from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `StaticBinary` |
| **Values:** | binary values in quotes |

**Example:** `set_param(gcb,"StaticBinary","[83 89 83 84 58 80 79 78 58 84
73 77 69 63]")`

### **Binblock data** — Binblock command to send to your instrument binblock values

Data to send to your instrument as a binblock.

#### Dependencies

- To enable this parameter, select the **Binblock** option
  from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `BinBlockCommand` |
| **Values:** | binblock values in quotes |

**Example:** `set_param(gcb,"BinBlockCommand","[83 89 83 84 58 80 79 78 58
84 73 77 69 63]")`

### **Data type** — Size and format of each value `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `uint64` | `int64`

Data type to send data as to your instrument. This parameter determines the number
of bytes to write for each value and the interpretation of those bytes as a
MATLAB data type.

#### Dependencies

- To enable this parameter, select the **Binary** or
  **Binblock** option from **Send command
  type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DataType` |
| **Values:** | `"uint8"` (default) | `"single"` | `"double"` | `"int8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` |

**Example:** `set_param(gcb,"DataType","double")`

### **Command header** — SCPI command header to send with input port data SCPI command

SCPI command header that is prepended to the input port data to send to your
instrument.

#### Dependencies

- To enable this parameter, select the **Compose command from input
  data** option from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Header` |
| **Values:** | SCPI command in quotes |

**Example:** `set_param(gcb,"Header","SOUR1:VOLT")`

### **Numeric format** — Format of numeric data `Integer, signed (%d)` (default) | `Integer, unsigned (%u)` | `Floating-point (%f)` | `Characters (%c)` | `Enter numeric format`

Format of the input port data. You can specify a format other than the options
provided if you select `Enter numeric format`.

#### Dependencies

- To enable this parameter, select the **Compose command from input
  data** option from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `NumFormat` |
| **Values:** | `"Integer, signed (%d)"` (default) | `"Integer, unsigned (%u)"` | `"Floating-point (%f)"` | `"Characters (%c)"` | `"Enter numeric format"` |

**Example:** `set_param(gcb,"NumFormat","Characters
(%c)")`

### **Enter numeric format** — Custom format of numeric data `%2f` (default) | numeric formats

Customized format of input port data.

#### Dependencies

- To enable this parameter, select the `Enter numeric
  format` option from **Numeric format**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CustomNumericFormat` |
| **Values:** | `"%2f"` (default) | numeric format in quotes |

**Example:** `set_param(gcb,"CustomNumericFormat","%2f")`

### **delimiter** — Delimiting character `,` (default)

Delimiting character that is appended to the numeric format to create the command
string to send to your instrument.

#### Dependencies

- To enable this parameter, select the **Compose command from input
  data** option from **Send command type**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `delimiter` |
| **Values:** | `","` (default) | delimiting character in quotes |

**Example:** `set_param(gcb,"delimiter",",")`

#### Receive response

### **Data type** — Size and format of each value `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `uint64` | `int64`

Data type to read data as from your instrument. This parameter determines the
number of bytes to read for each value and the interpretation of those bytes as a
MATLAB data type.

#### Dependencies

- To enable this parameter, select the **Read numeric
  data** option from **Data format**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ReceiveDatatype` |
| **Values:** | `"uint8"` (default) | `"single"` | `"double"` | `"int8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` |

**Example:** `set_param(gcb,"ReceiveDatatype","double")`

### **Determine data size automatically** — Allow block to automatically detect data size on (default) | off

Select this parameter to let the block determine the size of the received data. If
you want to manually specify the data size, clear this parameter, and set the value of
the **Data size** parameter accordingly.

#### Dependencies

- To enable this parameter, select the **Read string response and
  convert to numeric value** or **Binblock** option
  from **Data format**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `AutoSize` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param(gcb,"AutoSize","off")`

### **Data size** — Number of values read `[1,1]` (default) | `[10000,1]` (default) | numeric array

Manually specify the number of values that should be read at each simulation time
step. Define the size as a multidimensional numeric array. The data size does not
include the header or terminator values.

#### Dependencies

To enable this parameter, either:

- Select the **Read numeric data** option from
  **Data format**. This case uses the `Size`
  programmatic parameter with a default value of `[1,1]`.
- Select the **Read string response and convert to numeric
  value** or **Binblock** option from
  **Data format**, and clear **Determine data size
  automatically**. This case uses the `OutputSize`
  programmatic parameter with a default value of
  `[10000,1]`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Size` |
| **Values:** | `"[1,1]"` (default) |

**Example:** `set_param(gcb,"Size","[1,2]")`

|  |  |
| --- | --- |
| **Parameter:** | `OutputSize` |
| **Values:** | `"[10000,1]"` (default) |

**Example:** `set_param(gcb,"OutputSize","[10000,2]")`

### Handle Error

### **Action when error occurs** — Action to take when instrument errors `Stop simulation` (default) | `Continue simulation`

Action the block should take when your instrument returns an error during
simulation. If you select `Stop simulation`, the diagnostic
viewer window displays the error. This error can be a `visadev` error
or an instrument error. If you select `Continue simulation`,
and a read error occurs, then the status bits are set to 1. If an instrument error
occurs, the instrument error port outputs the error message text as a string.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ActionWhenerror` |
| **Values:** | `"Stop simulation"` (default) | `"Continue simulation"` |

**Example:** `set_param(gcb,"ActionWhenerror","Continue
simulation")`

### **Check instrument error** — Output error message `off` (default) | `on`

Select this option to output any error to the instrument error port of the block
at each timestep using the SCPI command specified in **Error check
command**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Checkerror` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,"Checkerror","on")`

### **Error check command** — SCPI command to send to your instrument `SYSTem:ERRor?` (default) | SCPI command

Instrument error check SCPI command that you send to your instrument to see its
response.

#### Dependencies

- To enable this parameter, set the **Check instrument
  error** parameter to `on`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CheckCommand` |
| **Values:** | `"SYSTem:ERRor?"` (default) | SCPI command in quotes |

**Example:** `set_param(gcb,"InitTestCommand","SYSTem:ERRor?")`

## Libraries

Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Communicate with VISA resources

The VISA block communicates with a VISA resource. You can use this block to
send or receive data, as well as query the VISA resource, depending on the
configuration.
