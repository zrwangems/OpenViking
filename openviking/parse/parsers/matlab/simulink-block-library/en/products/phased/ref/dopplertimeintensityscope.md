---
type: simulink-block
title: 'Doppler-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Visualization'
documentation_page: 'dopplertimeintensityscope'
documentation_source_path: 'ref/dopplertimeintensityscope.html'
language: en
---

# Doppler-Time Intensity Scope

## Ports

### Input

### **X** — Input data real-valued length-*M* vector

Input data, specified as a real-valued length-*M* vector of
Doppler responses. Each vector corresponds to a line of data. The block accepts single
precision data type input, but converts the data to double precision for
display.

**Data Types:** `double` | `single`

## Parameters

### **Doppler Output** — Doppler output domain `'Frequency'` (default) | `'Speed'`

Doppler output domain, specified as `'Frequency'` or
`'Speed'`. If you set this property to
`'Frequency'`, the Doppler domain is Doppler shift. Units are in Hz. If
you set this property to `'Speed'`', the Doppler domain is radial
speed. Units are in m/s.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`DopplerOutput` |
| **Type:**character vector |
| **Values:**`'Frequency'` | `'Speed'` |
| **Default:**`'Frequency'` |

**Data Types:** `string`

### **Propagation Speed (m/s)** — Signal propagation speed `physconst("LightSpeed")` (default) | positive scalar

Signal propagation speed, specified as a positive scalar. To obtain the speed of
light in SI units, use `physconst`. Units are in
meters/second.

**Example:** `3e8`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PropagationSpeed` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`physconst("LightSpeed")` |

**Data Types:** `double`

### **Doppler Offset (Hz)** — Doppler axis offset `0.0` (default) | scalar

Doppler axis offset, specified as a scalar. This property applies a frequency offset
to the Doppler axis. Units are in Hz.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`DopplerOffset` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`0` |

**Data Types:** `double`

### **Time Span (s)** — Time span of display `0.100` (default) | positive scalar

Time span of the intensity display, specified as a positive scalar. Units are in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeSpan` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`0.1` |

**Data Types:** `double`

### **Operating Frequency (Hz)** — Operating frequency `300e6` (default) | positive scalar

Operating frequency, specified as a positive scalar. Units are in Hz.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OperatingFrequency` |
| **Type:**double |
| **Values:**scalar |
| **Default:**`300000000` |

**Data Types:** `double`

### **Doppler Resolution (Hz)** — Doppler interval between samples `1.0` (default) | positive scalar

Doppler interval between samples, specified as a positive scalar. This property
defines the Doppler frequency difference between the scope columns. Units are in
Hz.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`DopplerResolution` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1` |

**Data Types:** `double`

### **Time Resolution (s)** — Time difference between rows `0.001` (default) | positive scalar

Time interval between samples, specified as a positive scalar. This property defines
the time duration between rows of scope. Units are in seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TimeResolution` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`0.001` |

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

### **Time Label** — Time axis label `'Time (s)'` (default) | string

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

### **Colorbar Label** — Color bar label `'dB'` (default) | string

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

### **Title** — Window title `'Doppler vs. Time'` (default) | string

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

**Introduced in R2022a**

## Description

Doppler-time intensity scope

The Doppler-Time Intensity Scope block creates a scrolling display of
Doppler response intensities as a function of time. The input consists of Doppler responses
for a pulse or FMCW signal. Each frame of data creates a new line on the scope. The scope
serves only as a display of the Doppler response. Using the response as input corresponds to
setting the `IQDataInput` property of the `phased.DTIScope`
System object™ to `false`.
