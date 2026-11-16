---
type: simulink-block
title: 'ASCII Decode V2'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'asciidecodev2'
documentation_source_path: 'io_ref/asciidecodev2.html'
language: en
---

# ASCII Decode V2

## Ports

### Input

### **Data** — Input vector to parse `character vector`

The input vector can be either 8-bit or 16-bit and signed or unsigned.
If the data format is 16-bit, the block ignores the upper 8 bits of each
entry.

**Data Types:** `int8` | `uint8` | `int16` | `uint16`
### Output

### **cnt** — Number of format specifiers satisfied by input integer

`cnt` receives the number of format specifiers
satisfied by the input character vector.

### **Value** — Inlined ports that send Simulink values numeric

Output ports corresponding to items in
**Format**.

This block generates inline code for the target computer. You cannot
use it for Simulink simulation.

**Data Types:** `single` | `double` | `int8` | `uint8` | `uint16` | `int16` | `int32` | `uint32`

## Parameters

### **Format** — Format specifier for parsing input vector `'%f\n'` (default) | `%c` | `%d` | `%i` | `%o` | `%u` | `%x` | `%e` | `%g`

Enter a `scanf` like format string. Each format
specifier such as `%d` must match a corresponding part of
the input vector. Literal strings in the format must match the characters in
the input vector. The format specifiers follow the normal description for
`scanf`. The specifiers must be enclosed in single
quotes. Failure to include these quotes causes simulation failures.

An example format string is:

```
'alpha %d bravo %f\n'
```

In this example, the data from the FIFO read is `'alpha
5'`. In this case, `cnt` is
`1` and the second output is unchanged from the last
time both were found in a character vector. If the model expects
`2` values, and `cnt` is less than
`2`, the model detects an error in the data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `format` |

## Libraries

Simulink Real-Time / RS232

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Parse ASCII character vector into Simulink values

The ASCII Decode block parses an input vector produced by one of the
following:

- Serial port Receive block
- Serial port FIFO Read block
- ASCII Encode block

This block makes the converted values available to a real-time
application. It assumes that the
input vector was prepared using an output format specifier similar to
`printf` and uses an input format specifier similar to
`scanf`.

This block generates inline code for the Speedgoat® target computer. You
cannot use it for Simulink® simulation.

For more information, see RS-232 Serial Communication and
RS-232 Legacy Drivers.
