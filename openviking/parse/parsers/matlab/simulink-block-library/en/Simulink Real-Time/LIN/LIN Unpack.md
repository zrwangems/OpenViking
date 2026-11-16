---
type: simulink-block
title: 'LIN Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'LIN'
documentation_page: 'linunpack'
documentation_source_path: 'io_ref/linunpack.html'
language: en
---

# LIN Unpack

## Ports

### Input

### **message\_updated** — indicates message update 0 (logical false) | 1 (logical true)

When the `message_updated` value is 1 (logical true), there is a
message coming in from the LIN bus. This block outputs the unpacked signals. When the
`message_updated` value is 0 (logical false), there is no message
updated on the LIN bus, and this block outputs the default value for each signal
defined in the LDF file.

### **Lin\_data\_8\_bytes** — input LIN data to unpack LIN data

Receives LIN data to unpack.
### Output

### **out** — output data data

Sends unpacked data. The number of the output ports is allocated based on the
number of signals in the selected frame. When a frame is selected, the port name is
assigned to each port.

## Parameters

### **LDF File Name** — File path of LDF empty (default) | character vector | string scalar

Provides the file path of the LDF. If you do not set this parameter, you cannot use
the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LDFFileName` |

### **Select Frame** — LIN frame `None` (default) | character vector | string scalar

Selects the LIN frame from selections available in LDF. If you do not select an LDF,
the block uses `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `selectedFrameName` |

### **Frame ID** — LIN frame ID `1` (default) | uint8

Selects LIN frame ID from selections available in LDF. If you do not select an LDF,
the block uses `1`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `frameId` |

## Libraries

Simulink Real-Time / LIN

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Unpack signals from data frame by using configuration in LIN description file

The LIN Unpack block unpacks the data frame by using the configuration in
the LIN description file (LDF) and outputs signal data. You can use the unpacked local
interconnect network (LIN) bus data as signal data in the model. The LIN Unpack
block supports LDF version 2.2 and previous.
