---
type: simulink-block
title: 'IEEE 1588 Read Parameter'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'PTP'
documentation_page: 'ieee1588readparameter'
documentation_source_path: 'io_ref/ieee1588readparameter.html'
language: en
---

# IEEE 1588 Read Parameter

## Ports

### Output

### **Output** — Output selected by Parameter to read parameter `double` | `[uint32]`

The current parameter to read.

## Parameters

### **Parameter to read** — Parameter to display at output `System time (nanosecond)` (default) | `Calendar time (time_t)` | `Offset from Client` | `Client to Server Delay` | `One Way Delay`

Specify the parameter to read. Select one of:

| Parameter | Data Type | Description |
| --- | --- | --- |
| `System time (nanosecond)` | `uint64` | Current SLRT system time number of nanoseconds, counting from the current epoch. |
| `Calendar time (time_t)` | `int32` vector | Current SLRT calendar time in `time_t`. |
| `Offset from Client` | `double` | Time offset in seconds. |
| `Client to Server Delay` | `double` | Time delay in seconds. |
| `One Way Delay` | `double` | Time delay in seconds. |

**Note**

These parameter options will be
removed in a future release and generate a warning message during model
build: `Offset from Client`,
`Client to Server Delay`, and
`One Way Delay`.

The `Calendar time (time_t)` vector contains
these components:

- Seconds after the minute — 0 to 61 (until C99) and 0 to 60 (since
  C99)
- Minutes after the hour — 0 to 59
- Hours since midnight — 0 to 23
- Day of the month — 1 to 31
- Months since January — 0 to 11
- Years since 1900
- Days since Sunday — 0 to 6
- Days since January 1 — 0 to 365
- Daylight Saving Time flag. The value is positive if DST is in
  effect, zero if not and negative if no information is
  available

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `param` |

### **Sample time (-1 for inherited)** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample
time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sample_time` |

## Libraries

Simulink Real-Time / PTP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Output Precision Time Protocol status parameter values such as target computer system time, calendar time, and delays

The IEEE 1588 Read Parameter block reads the parameter that you select
and send its value to the block output. The block label changes based on the parameter
that you select. You can use the IEEE 1588 Read Parameter block to read
the Speedgoat® target computer system time even without a PTP process running.

**Note**

The IEEE 1588 Read Parameter block outputs the system time,
which is updated every 1 ms. This output is independent of the sample time
of the block and the nanosecond precision of the block output. For more
information, see  `clock_gettime()` in the QNX® Neutrino® documentation.
