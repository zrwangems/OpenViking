---
type: simulink-block
title: 'Serial Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Blocks for Embedded Targets'
documentation_page: 'serialsend'
documentation_source_path: 'ref/serialsend.html'
language: en
---

# Serial Send

## Ports

### Input

### **Data** — Data values to send vector | matrix | array

Data values to send from the block over your serial port, specified as a vector,
matrix, or array. Set the parameters for this block before you send data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Port** — Serial communication port available communication ports

Serial ports on your machine that you want to send data to. Select a port from the
available ports and then configure the port using the Serial
Configuration block. If you have not configured a port, the block returns an
error when you run your model.

**Note**

Each Serial Send block must have a configured Serial
Configuration block. If you use multiple serial ports in your simulation,
you must configure each port using a separate Serial Configuration
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |

### **Header** — Header numeric array | integer from 0 to 255, inclusive

Header that indicates the beginning of your data block. The Serial
Send block adds the header in front of the data before sending it over the
serial port. By default, no header is specified.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

You can also specify this parameter using the hexadecimal representation
of the ASCII characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Header` |
| **Type:** character vector, string |
| **Values:** integer array |

### **Terminator** — Terminator `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

Terminator that indicates the end of your data block. The Serial Send
block appends the terminator to the data before sending it over the serial port.

If you select `Custom Terminator`, you can specify your own
terminator value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Terminator` |
| **Type:** character vector, string |
| **Values:** `'<none>'` | `'CR ('\r')'` | `'LF ('\n')'` | `'CR/LF ('\r\n')'` | `'NULL ('\0')'` | `'Custom Terminator'` |
| **Default:** `'<none>'` |

### **Custom terminator** — Custom terminator numeric array | integer from 0 to 255, inclusive

Custom terminator that indicates the end of your data block. The Serial
Send block appends the terminator to the data before sending it over the
serial port.

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

### **Enable blocking mode** — Simulation waits while sending data `on` (default) | `off`

This parameter has the simulation wait while the block sends data. Unselect the
check box if you do not want the write operation to cause the simulation to wait.

If you enable blocking mode, the simulation waits for the data to be sent. If you do
not enable blocking mode, the simulation runs continuously.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableBlockingMode` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

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

Send binary data over serial port

The Serial Send block configures and opens an interface to the specified
serial port. The configuration and initialization occur once at the start of the model's
execution. The block sends data from the model to the serial port during the model's run time.
You can use multiple Serial Send blocks at a time to send data to a specific
serial port.

**Note**

You must configure your serial port parameters using the Serial
Configuration block before you specify the Serial Send block
parameters.

The Serial Send block has one input port that accepts both 1-D vector and
matrix data. This block has no output ports. The block inherits the data type from the signal
at the input port. Valid data types are `single`, `double`,
`int8`, `uint8`, `int16`,
`uin16`, `int32`, and `uint32`.

### Other Supported Features

- The Serial Send block supports the use of Simulink® Accelerator mode, but not Rapid Accelerator.
  This feature speeds up the execution of Simulink models.
- The Serial Send block supports the use of model referencing. This
  feature lets your model include other Simulink
  models as modular components.
- The Serial Send block supports C/C++ code generation. This feature
  allows you to generate C and C++ code using Simulink
  Coder™.

For more information on these features, see the Simulink
documentation.
