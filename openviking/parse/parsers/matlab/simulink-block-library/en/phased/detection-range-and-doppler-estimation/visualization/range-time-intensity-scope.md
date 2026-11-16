---
type: simulink-block
title: 'Range-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Visualization'
documentation_page: 'rangetimeintensityscope'
documentation_source_path: 'ref/rangetimeintensityscope.html'
language: en
---

# Range-Time Intensity Scope

## Ports

### Input

### **X** — Input data real-valued length-*M* vector

Input data, specified as a real-valued length-*M* vector of range
responses. Each vector corresponds to a line of data. The block accepts single
precision data type input, but converts the data to double precision for
display.

**Data Types:** `double` | `single`

## Parameters

#### Data and Axes

### **Range Offset (m)** — Range offset `0.0` (default) | positive scalar

Range offset, specified as a positive scalar. This parameter defines the range value
of the first column of the display. Units are in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`RangeOffset` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`0` |

**Data Types:** `double`

### **Time Span (s)** — Time span of display `0.1` (default) | positive scalar

Time span of the intensity display, specified as a positive scalar. Units are in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeSpan` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`1` |

**Data Types:** `double`

### **Range Resolution (m)** — Range difference between samples `1` (default) | positive scalar

Range distance between samples, specified as a positive scalar. This parameter
defines the distance between columns of the scope. Units are in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`RangeResolution` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`25` |

**Data Types:** `double`

### **Time Resolution (s)** — Time difference between rows `0.001` (default) | positive scalar

Time interval between samples, specified as a positive scalar. This parameter
defines the time interval between the rows of the scope. Units are in seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeResolution` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`0.00033356` |

**Data Types:** `double`

### **Show Grid** — Show Cartesian grid overlay on (default) | off

Show Cartesian grid overlay. To show the grid, select the check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ShowGrid` |
| **Type:**logical |
| **Values:**1 | 0 |
| **Default:**`1` |

### **Show Ticks** — Show tick value labels on (default) | off

Show value labels on tick marks. The display the labels on, select the check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ShowTicks` |
| **Type:**logical |
| **Values:**1 | 0 |
| **Default:**`1` |

#### Labels

### **Range Label** — Range axis label `'Range (m)'` (default) | string

Range-axis label, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`RangeLabel` |
| **Type:**string |
| **Values:**string |
| **Default:**`'Range (m)'` |

**Data Types:** `char`

### **Time Label** — Time axis label `Time History (s)'` (default) | string

Time-axis label, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeLabel` |
| **Type:**string |
| **Values:**string |
| **Default:**`'Time History (s)'` |

**Data Types:** `string`

### **Title** — Window title `'Range vs. Time'` (default) | string

Window title, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Title` |
| **Type:**string |
| **Values:**string |
| **Default:**`Range vs. Time'` |

**Data Types:** `char`

### **Colorbar Label** — Color bar `'mag'` (default) | string

Color bar label, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ColorBarLabel` |
| **Type:**string |
| **Values:**string |
| **Default:**`'mag'` |

**Data Types:** `string`

## Libraries

Phased Array System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code but

## Version History

**Introduced in R2022a**

## Description

Range-time intensity scope

The Range-Tine Intensity Scope block creates a scrolling display of range
response intensities as a function of time. The input consists of range responses for a pulse
or FMCW signal. Each frame of data creates a new line on the scope. The scope serves only as a
display of the range response. Using the response as input corresponds to setting the
`IQDataInput` property of the `phased.RTIScope`
System object™ to `false`.
