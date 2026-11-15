---
type: simulink-block
title: 'ASCII Encode'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'asciiencode'
documentation_source_path: 'io_ref/asciiencode.html'
language: en
---

# ASCII Encode

## Ports

### Input

### **1** — Numbered ports that receive values to encode numeric

Values that the block encodes as a null-terminated character
vector.

**Data Types:** `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

### **D** — Null-terminated character vector `character vector`

Generated `uint8` output vector that contains a
NULL-terminated character vector.

## Parameters

### **Format string** — Format specifiers for converting values to ASCII `%d\r` (default) | `%c` | `%i` | `%o` | `%u` | `%x` | `%e` | `%f` | `%g`

Enter a `printf` like format string. For each format
specifier such as `%d`, the block replaces the format
specifier by the converted value in the corresponding input variable. The
format specifiers follow the normal description for
`printf`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `format` |

### **Number of variables** — Number of block inputs `1` (default) | integer

The value on each port is inserted into the output character vector with
the format specified in **Format string**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nvars` |

### **Max output string length** — Maximum length of converted character vector, in bytes `128` (default) | integer

The block allocates enough memory to support this length for the output
port. When specifying this length, include the NULL termination on the
character vector.

If the converted character vector exceeds this length, the block returns
an error and does not write that character vector to the output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxlength` |

### **Variable types** — Simulink® data types allowed for input ports `{'double'}` (default) | `{'int8'}` | `{'uint8'}` | `{'int16}` | `{'uint16'}` | `{'int32'}` | `{'uint32'}`

A cell vector with the same number of elements as specified in
**Number of variables** can specify a different data
type for each input port. A single element is replicated. For
example:

```
nvars=3
```

`{ }` — The three inputs are doubles.

`{'uint8'}` — The three inputs are
`uint8`.

`{'uint16', 'double', 'uint8'}` — The first input
is a `uint16`, the second input is a
`double`, and the third input is a
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vartypes` |

## Libraries

Simulink Real-Time / RS232

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Convert Simulink values into uint8 character vector

The ASCII Encode block generates a `uint8` output
vector that contains a NULL-terminated character vector based on a
`printf` like format string. The data comes from the input
ports.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
