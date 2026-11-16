---
type: simulink-block
title: 'Serial Configuration'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'serialconfiguration'
documentation_source_path: 'ref/serialconfiguration.html'
language: en
---

# Serial Configuration

## Ports

Not documented in R2025b.

## Parameters

### **Port** — Serial communication port available communication ports

Serial port on your machine that you want to configure. Use this configured port to
send and receive data with your Serial Send and Serial
Receive blocks. If you have not configured a port, the block returns an error
when you run your model.

**Note**

Each Serial Send and Serial Receive block must have
a configured Serial Configuration block. If you use multiple serial
ports in your simulation, you must configure each port using a separate Serial
Configuration block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Port` |
| **Type:** character vector, string |

### **Baud rate** — Communication speed 9600 (default) | positive integer

Rate at which bits are transmitted for the serial interface, in bits per
second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BaudRate` |
| **Type:** character vector, string |
| **Values:** positive integer |
| **Default:** `'9600'` |

### **Data bits** — Number of bits to represent one character of data `8` (default) | `5` | `6` | `7`

Number of data bits to transmit over the serial interface.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataBits` |
| **Type:** character vector, string |
| **Values:** `'5'` | `'6'` | `'7'` | `'8'` |
| **Default:** `'8'` |

### **Parity** — Parity bit type `none` (default) | `even` | `odd`

Parity bit type added to data transmitted by serial port. You can use this parameter
to add a parity bit (also referred to as a check bit) to your data. Adding a parity bit
to a string of binary code is a method of detecting errors in data transmission by
ensuring that the total number of 1-bits is even or odd.

The value of the parity bit is determined by the number of 1s in a given set of bits
and is set as follows.

| Parity Bit Type | Parity Bit Value | |
| --- | --- | --- |
| If number of 1s is even | If number of 1s is odd |
| `none` | No parity bit set | No parity bit set |
| `even` | 0 | 1 |
| `odd` | 1 | 0 |

**Note**

Starting in R2021a, the **Parity** parameter no longer supports
`mark` or `space`. For more
information, see Parity parameter no longer supports mark or space in Serial Configuration block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Parity` |
| **Type:** character vector, string |
| **Values:** `'none'` | `'even'` | `'odd'` |
| **Default:** `'none'` |

### **Stop bits** — Pattern of bits that indicates the end of a character `1` (default) | positive scalar

Number of bits used to indicate the end of a byte. This parameter depends on the
value you select for the **Data bits** parameter. If you select data
bits `6`, `7`, or
`8`, the default value is `1` and the other
available choice is `2`. If you select data bit
`5`, the default value is `1` and the other
available choice is `1.5`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StopBits` |
| **Type:** character vector, string |
| **Values:** positive scalar |
| **Default:** `'1'` |

### **Byte order** — Sequential order of bytes `little-endian` (default) | `big-endian`

Sequential order in which bytes are arranged into larger numerical values. If the
byte order is `little-endian`, then the instrument stores the
first byte in the first memory address. If the byte order is
`big-endian`, then the instrument stores the last byte in the
first memory address.

Configure the byte order to the appropriate value for your instrument before
performing a read or write operation. Refer to your instrument documentation for
information about the order in which it stores bytes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ByteOrder` |
| **Type:** character vector, string |
| **Values:** `'little-endian'` | `'big-endian'` |
| **Default:** `'little-endian'` |

### **Flow control** — Mode for managing data transmission rate `none` (default) | `hardware`

Process of managing the rate of data transmission on your serial port. Select
`none` to have no flow control or
`hardware` to let your hardware determine the flow
control.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FlowControl` |
| **Type:** character vector, string |
| **Values:** `'none'` | `'hardware'` |
| **Default:** `none` |

### **Timeout** — Allowed time to complete operations 10 (default) | positive scalar

Amount of time that the model waits for data during each simulation time
step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Timeout` |
| **Type:** character vector, string |
| **Values:** positive scalar |
| **Default:** `'10'` |

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

### R2021a: **Parity** parameter no longer supports `mark` or `space` in Serial Configuration block

The `mark` and `space` options for the
**Parity** parameter are no longer supported in the Serial
Configuration block. Valid values for **Parity** are
`none` (default), `even`, and
`odd`.

If you try to open an existing model that has the **Parity** value set
to `mark` or `space`, MATLAB® returns a warning and changes the parameter to the default value
`none`.

## Description

Configure parameters for serial port

The Serial Configuration block configures parameters for a serial port that
you can use to send and receive data. Use this block to set the parameters of your serial port
before you set up the Serial Receive and the Serial Send
blocks.

**Note**

You must configure your serial port parameters using the Serial
Configuration block before you specify the Serial Receive and
Serial Send block parameters.

### Other Supported Features

- The Serial Configuration block supports the use of Simulink® Accelerator mode, but not Rapid Accelerator.
  This feature speeds up the execution of Simulink models.
- The Serial Configuration block supports the use of model referencing.
  This feature lets your model include other Simulink models as modular components.
- The Serial Configuration block supports C/C++ code generation. This
  feature allows you to generate C and C++ code using Simulink
  Coder™.

For more information on these features, see the Simulink
documentation.
