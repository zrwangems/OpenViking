---
type: simulink-block
title: 'Angle-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'angletimeintensityscope'
documentation_source_path: 'ref/angletimeintensityscope.html'
language: en
---

# Angle-Time Intensity Scope

## Ports

### Input

### **X** — Input data real-valued length-*M* vector

Input data, specified as a real-valued length-*M* vector of angle
responses. Each vector corresponds to a line of data. The block can accept single
precision data type input, but converts the data to double precision for
display.

**Data Types:** `double` | `single`

## Parameters

### **Angle offset (degree)** — Angle offset `0.0` (default) | scalar

Angle offset, specified as a scalar. This property defines the angle value of the
first column of the display. Units are in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`AngleOffset` |
| **Type:**double |
| **Values:**`scalar` | |
| **Default:**0.0 |

**Data Types:** `double`

### **Angle resolution (degree)** — Angle difference between samples `1.0` (default) | positive scalar

Angle separation between samples, specified as a positive scalar. This property
defines the angle difference between columns of the scope. Units are in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`AngleResolution` |
| **Type:**double |
| **Values:**`positive scalar` | |
| **Default:**0.0 |

**Data Types:** `double`

### **Time span (s)** — Time span of display `Auto` (default)

Time span of the intensity display, specified as a positive scalar. When the
**Time span (s)** is set to `Auto` the simulation
stops at the default **stop time** of the simulation. Units are in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeSpan` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`0.1` |

**Data Types:** `double`

### **Time resolution (s)** — Time difference between rows `Auto` (default)

Time interval between rows, specified as a positive scalar. This property defines
the time duration between rows of the scope. When the **Time resolution (s)** parameter is set to `Auto` the block uses the
**Compiled Sample Time**  value during simulation. At all other
times, the block uses the value specified by this parameter. Units are in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeResolution` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`0.001` |

**Data Types:** `double`

### **Grid** — Show Cartesian grid overlay on (default) | off

Show Cartesian grid overlay. To show the grid, select the check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ShowGrid` |
| **Type:**logical |
| **Values:**1 | 0 |
| **Default:**`1` |

### **Ticks** — Show tick value labels on (default) | off

Show value labels on tick marks. To display the labels, select the check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ShowTicks` |
| **Type:**logical |
| **Values:**1 | 0 |
| **Default:**`1` |

#### Labels

### **Angle label** — Angle-axis label `'Angle (degree)'` (default) | character vector | string

Angle-axis label, specified as a character vector or a string.

**Example:** `'Angle (rad)'`

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`AngleLabel` |
| **Type:**string |
| **Values:**string |
| **Default:**`'Angle (degree)'` |

**Data Types:** `char` | `string`

### **Time label** — Time axis label `'Time History (s)'` (default) | string

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

### **Title** — Window title `Angle vs. Time'` (default) | string

Window title, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Title` |
| **Type:**string |
| **Values:**string |
| **Default:**`'Doppler vs. Time'` |

**Data Types:** `char`

### **Colorbar label** — Color bar label `'dB'` (default) | string

Color bar label, specified as a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ColorBarLabel` |
| **Type:**string |
| **Values:**string |
| **Default:**`'dB'` |

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

This block can be used for simulation visibility in systems that generate code but is
not included in the generated code.

## Version History

**Introduced in R2022b**

## Description

Angle-time intensity scope

The Angle-Time Intensity Scope block creates a scrolling display of angle
response intensities as a function of time. The input consists of angle responses for a pulse
or FMCW signal. Each frame of data creates a new line on the scope. The scope serves as a
display of the angle response.
