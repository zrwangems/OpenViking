---
type: simulink-block
title: 'LIN Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'LIN'
documentation_page: 'linpack'
documentation_source_path: 'io_ref/linpack.html'
language: en
---

# LIN Pack

## Ports

### Input

### **in** — input data to pack data

Receives data to pack for the LIN. The number of input ports is allocated based on
the selected frame. The port name is assigned to each port.
### Output

### **lin\_data** — output LIN data LIN data

Sends packed LIN data.

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

Selects the LIN frame ID from selections available in LDF. If you do not select an
LDF, the block uses `1`.

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

Pack signals into data frame by using configuration in LIN description file

The LIN Pack block packs signals into the data frame by using the
configuration in the LIN description file (LDF). A local interconnect network (LIN) bus can
use the packed data. The LIN Pack block supports LDF version 2.2 and
previous.
