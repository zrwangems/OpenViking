---
type: simulink-block
title: 'MultiStateImage'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'multistateimage'
language: en
---

# MultiStateImage

Display image reflecting input value

## Libraries

Simulink / Dashboard

## Description

The MultiStateImage block displays an image to indicate the value of
the input signal. You can use the MultiStateImage block with other
Dashboard blocks to build an interactive dashboard of controls and indicators for your
model. You can specify pairs of input values and images to provide the information you
want during simulation.

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

This animation shows how to connect the MultiStateImage block to
your model.

An unconnected MultiStateImage block connects to the signal that a Pulse Generator block sends to a Display block.

## Parameters

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

### **Scale Mode** — Specify how to scale image `Fill with fixed aspect ratio` (default) | `Fixed` | `Fill`

Specify how to scale the image.

**Fill with fixed Aspect Ratio** scales the image
to the size of the block while retaining its original aspect ratio.

**Fixed** displays the image with its fixed true
size.

**Fill** adjusts the image to fill the
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleMode` |
| **Type:** string or character vector |
| **Values:** `'Fill with fixed aspect ratio'` | `'Fixed'` | `'Fill'` |
| **Default:** `'Fill with fixed aspect ratio'` |

### **States** — Match values with images to display scalar and image

States match an image to display with a value of the connected variable or
parameter. Each state consists of a **State** and an image,
displayed as a **Thumbnail** in the
**States** table for the MultiStateImage block.

- **State** — Connected variable or parameter
  value that causes the MultiStateImage block to
  display the corresponding image.
- **Thumbnail** — Image to display when the
  connected variable or parameter value matches the corresponding
  **State**.

Click the **+** button to add another state.

#### Programmatic Use

To programmatically configure `State` and
`Thumbnail` parameter values for the
MultiStateImage block, use the
`States` parameter. Specify the value for the
`States` parameter as an array of structures with
the fields:

- `State` — State value.
- `Size` —
  `1`-by-`2` vector
  containing the width and height for the image in that order,
  in pixels, specified as a `uint64`.
- `Image` — Character array of Base64
  encoded image data.
- `Thumbnail` — Character array of Base64
  encoded image data for the thumbnail image to display in the
  **States** table in the block dialog
  box.

Include a structure in the array for each state you want to specify
for the block. In the example, the `myBase64Image` and
`myBase64Thumbnail` variables contain character
vectors of the Base64 image data for the block image and
thumbnail.

```
state1.State = 1;
state1.Size = [uint64(400) uint64(400)];
state1.Image = myBase64Image;
state1.Thumbnail = myBase64Thumbnail;
state2.State = 2;
state2.Size = uint64(400) uint64(400)];
state2.Image = myBase64Image2;
state2.Thumbnail = myBase64Thumbnail2;
msiStates = [state1 state2];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** structure array |

The block displays the default image when the connected signal value
does not correspond to any of the specified states. Specify the
`DefaultImage` parameter as a structure containing
the fields:

- `Size` —
  `1`-by-`2` vector
  containing the width and height for the image in that order,
  in pixels, specified as `uint64`.
- `Image` — Character array of Base64
  encoded image data.
- `Thumbnail` — Character array of Base64
  encoded image data for the thumbnail image to display in the
  **States** table in the block dialog
  box.

|  |
| --- |
| **Block Parameter:** `DefaultImage` |
| **Type:** structure |

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

**Introduced in R2016b**
