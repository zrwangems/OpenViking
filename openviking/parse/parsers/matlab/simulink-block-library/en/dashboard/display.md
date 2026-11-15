---
type: simulink-block
title: 'Display'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboarddisplay'
language: en
---

# Display

Display signal value during simulation

## Libraries

Simulink / Dashboard

## Description

The Display block connects to a signal in your model and displays its
value during simulation. You can configure the appearance and format of the
Display block to make intuitive sense for the value it displays. You
can edit the parameters of the Display block during simulation. The
Display block can display complex, vector, and 2-D matrix signals.
Use the Display block with other dashboard blocks to build an interactive
dashboard of controls and indicators for your model.

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

This animation shows how to connect the Display block to your
model.

An unconnected Display block connects to the signal that a Ramp block sends to a Terminator block.

## Parameters

### Connection

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

### **Format** — Format for displaying signal values `short` (default) | `long` | `shortE` | `longE` | ...

Specify a format for displaying signal values.

| If You Select... | The Block Displays... |
| --- | --- |
| `short` | Scaled fixed-decimal format with four digits after the decimal point. |
| `long` | Scaled fixed-decimal format with fifteen digits after the decimal point for `double` values and seven digits after the decimal point for `single` values. |
| `shortE` | Scientific notation format with four digits. |
| `longE` | Scientific notation format with fifteen digits after the decimal point for `double` values and seven digits after the decimal point for `single` values. |
| `shortG` | Data takes the more compact format between fixed-decimal or scientific notation, with a total of five digits. |
| `longG` | Data takes the more compact format between fixed-decimal or scientific notation, with a total of fifteen digits for `double` values and seven digits for `single` values. |
| `shortEng` | Engineering notation where the exponent is a multiple of three, with four digits after the decimal point. |
| `longEng` | Engineering notation where the exponent is a multiple of three, with fifteen significant digits. |
| `+-` | Positive/negative format. `+`, `-`, and blank characters are displayed for positive, negative, and zero values, respectively. |
| `bank` | Currency format with two digits after the decimal point. |
| `hex` | Hexadecimal representation. |
| `rat` | Ratio. |
| `Custom` | Custom string format. Data is displayed in a custom string that you specify using the **Format String** parameter. |
| `Integer` | Data rounded to the nearest whole number. |

When you connect the Display block to the
signal output by a String Constant block, the format for
displaying signal values is `string`, regardless of the
value of the **Format** parameter. Similarly, when you
connect the Display block to the signal output by an
Enumerated Constant block, the format for displaying
signal values is `enum`, regardless of the value of the
**Format** parameter.

Display blocks show example outputs for these formats: short, long, shortE, longE, shortG, longG, Custom, shortEng, longEng, bank, plus, hex, rat, Integer, string, and enum.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character array | string |
| **Values:** `'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **Default:** `'short'` |

### **Format String** — Custom string to format data `'%d'` (default) | string

Custom string to format displayed signal data, specified as a string.
The format string consists of text and format operators, which start
with a `%` sign and end with a conversion character.
Use the format operators at the place in the string where you want the
signal data to display. For more information about supported formatting
operators, see the `formatSpec` input of the `compose` function.

**Example:** `The value of pi is %.2f` displays the value
of the connected signal within a sentence.

**Example:** `$%.2f` displays the value of the connected
signal with a dollar sign and two decimal places.

#### Dependencies

To enable this parameter, set the **Format**
parameter to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |
| **Type:** character array | string |
| **Default:** `'%d'` |

### **Alignment** — Text alignment in block `Center` (default) | `Left` | `Right`

Text alignment in the Display block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Alignment` |
| **Type:** character array |
| **Values:** `'Left'` | `'Center'` | `'Right'` |
| **Default:** `'Center'` |

### **Label** — Block label position `Hide` (default) | `Bottom` | `Top`

Position of the block label. When the block is connected to an element in the
model, the label is the name of the connected element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

### **Layout** — How to arrange elements of non-scalar data `Preserve dimensions` (default) | `Fill available space`

How to arrange elements of non-scalar data, specified as one of these options:

- `Preserve dimensions` — Display elements
  arranged to match signal dimensions.
- `Fill available space` — Display as many
  elements as possible within available space.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layout` |
| **Type:** character array | string |
| **Values:** `'Preserve dimensions'` | `'Fill available space'` |
| **Default:** `'Preserve dimensions'` |

### Format

### **Show grid for non-scalar signals** — Whether to show grid on (default) | off

Whether to show a grid on the block when the block displays non-scalar
data. Specify the color of the grid using the **Grid
Color** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowGrid` |
| **Type:** character array | string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

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

Block foreground color, including the text. You can select a color from a palette
of standard colors or specify a custom color.

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

### **Grid Color** — Block grid color `[r g b]` vector

Block grid color. The grid shows when the block displays non-scalar
data. You can select a color from a palette of standard colors or
specify a custom color.

#### Programmatic Use

Specify the `GridColor` parameter for the block
as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `GridColor` |
| **Type:** `[r g b]` vector |
| **Default:** `[0.502 0.502 0.502]` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2017b**
