---
type: simulink-block
title: 'Linear Gauge'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'lineargauge'
language: en
---

# Linear Gauge

## Ports

Not documented in R2025b.

## Parameters

### Signal

### **Connection** — Signal to connect and display signal connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink® Toolstrip, or the **Connection** table in the Block
Parameters dialog box. For information about connect mode and how to connect using the
toolstrip, see Connect Dashboard Blocks to Simulink Model.

To connect a display block or change the connection of a display block using the **Connection** table:

1. Select the block.
2. To connect the block, in the Property Inspector, on the **Parameters** tab, click **Connect**. To change the connection of the block, click **Change** instead.
3. Select the signal line to which you want to connect.
4. In the table, select the signal to which you want to connect.
5. Click **Apply**.

You can also connect dashboard blocks to a Stateflow chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.SignalSpecification` |
| **Default:** `[]` |

### Main

### **Minimum** — Minimum tick mark value `0` (default) | scalar

Finite, real, double, scalar value specifying the minimum tick mark value for the
scale. The minimum must be less than the value of the **Maximum**
parameter.

#### Programmatic Use

To programmatically set the `Minimum` parameter, use a
`1`-by-`3` vector containing values for
the `Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`,
leave the `Tick Interval` position in the vector empty or
specify `-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — Maximum tick mark value `100` (default) | scalar

Finite, real, double, scalar value specifying the maximum tick mark value for the
scale. The maximum must be greater than the value of the
**Minimum** parameter.

#### Programmatic Use

To programmatically set the `Maximum` parameter, use a
`1`-by-`3` vector containing values for
the `Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`,
leave the `Tick Interval` position in the vector empty or
specify `-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — Interval between major tick marks `auto` (default) | scalar

Finite, real, positive, whole, scalar value specifying the interval of major tick
marks on the scale. When set to `auto`, the block automatically
adjusts the tick interval based on the values of the **Maximum**
and **Minimum** parameters.

#### Programmatic Use

To programmatically set the `Tick Interval` parameter, use a
`1`-by-`3` vector containing values for
the `Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`,
leave the `Tick Interval` position in the vector empty or
specify `-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Scale Colors** — Color indications on gauge scale colors for scale ranges

Color specifications for value ranges on the scale. Press the
**+** button to add a scale color. For each color added,
specify the minimum and maximum values of the range in which you want to display
that color.

#### Programmatic Use

To programmatically specify the `Scale Colors` parameter, use
an array of structures with the fields:

- `Min` — Minimum value for the color range on the
  scale
- `Max` — Maximum value for the color range on the
  scale
- `Color` —
  `1`-by-`3` vector of
  `double` values between `0`
  and `1` that specify the color for the range in the
  form `[r g b]`

Include a structure in the array for each scale range for which you want to
specify a color.

```
range1.Min = 0;
range1.Max = 10;
range1.Color = [0 0 1];
range2.Min = 10;
range2.Max = 15;
range2.Color = [0 1 0];
scaleRanges = [range1 range2];
```

|  |
| --- |
| **Block Parameter:** `ScaleColors` |
| **Type:** structure array |
| **Default:** `0x1` struct array |

### **Label** — Block label position `Top` (default) | `Bottom` | `Hide`

Position of the block label. When the block is connected to an element in the
model, the label is the name of the connected element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

### Format

### **Opacity** — Block background opacity `1` (default) | scalar

Block background opacity, specified as a scalar value between 0 and 1.

**Example:** `0.5`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Opacity` |
| **Type:** scalar |
| **Default:** `1` |

### **Foreground Color** — Block foreground color `[r g b]` vector

Block foreground color, excluding the text. The **Foreground
Color** applies to the scale and the block name. You can select a color
from a palette of standard colors or specify a custom color. To specify the color
for the block text, use the **Font Color**.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the block as a
string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Background Color** — Block background color `[r g b]` vector

Block background color. You can select a color from a palette of standard colors or specify a custom color.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a string or a
character vector that defines a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Font Color** — Block font color `[r g b]` vector

Block font color. The **Font Color** applies to the tick labels on the scale.
You can select a color from a palette of standard colors or specify a custom
color.

#### Programmatic Use

Specify the `FontColor` parameter for the block as a `1`-by-`3` `[r g b]` vector with values between `0` and `1`.

|  |
| --- |
| **Block Parameter:** `FontColor` |
| **Type:** `[r g b]` vector |

## Libraries

Simulink / Dashboard

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2015a**

## Description

Display input value on linear scale

The Linear Gauge block displays the connected signal on a straight
linear scale during simulation. Use the Linear Gauge block with other
Dashboard blocks to build an interactive dashboard of controls and indicators for your
model. The Linear Gauge block provides an indication of the instantaneous
value of the connected signal throughout simulation. You can modify the range of the
Linear Gauge block to fit your data. You can also customize the
appearance of the Linear Gauge block to provide more information about
your signal. For example, you can color-code in-specification and out-of-specification
ranges.

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard block,
use connect mode. To enter connect mode on an unconnected block, pause on the block you want
to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a display block to a signal in your model or change the connection of a display
block, enter connect mode. Select the signal line to which you want to connect. From the
list that appears, select the signal to which you want to connect. Then, pause on the
dashboard block and click the Done Connecting button . To see the dashboard block display the value of the
connected block, run the simulation.

For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

This animation shows how to connect the Linear Gauge block to your
model.

An unconnected Linear Gauge block connects to the signal that a Sine Wave block sends to a Display block.
