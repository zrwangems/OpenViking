---
type: simulink-block
title: 'Vertical Gauge'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'verticalgauge'
language: en
---

# Vertical Gauge

## Ports

Not documented in R2025b.

## Parameters

Use the Property Inspector and the Block Parameters dialog box
to specify the values of the block parameters. To set the core parameters of the dashboard
block, use the Block Parameters dialog box or the **Parameters** tab in the
Property Inspector. To customize the block, use the **Design** tab in the
Property Inspector. To open the Block Parameters dialog box for a block, double-click the block.
To open the Property Inspector, on the **Modeling** tab, under
**Design**, select **Property Inspector**.

### Parameters

To set the core parameters of the dashboard block, open the
Property Inspector and click the **Parameters** tab.

#### Signal

### **Connection** — Signal to connect and display signal connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink Toolstrip, or the **Connection** table in the Block
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

#### Main

### **Minimum** — Minimum tick mark value `0` (default) | scalar

Finite, real, double, scalar value specifying the minimum tick mark value for the
scale. The parameter value must be less than the value of the
**Maximum** parameter.

#### Programmatic Use

To programmatically set the `Minimum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — Maximum tick mark value `100` (default) | scalar

Finite, real, double, scalar value specifying the maximum tick mark value for the
scale. The parameter value must be greater than the value of the
**Minimum** parameter.

#### Programmatic Use

To programmatically set the `Maximum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — Interval between major tick marks `auto` (default) | scalar

Finite, real, positive, whole, scalar value specifying the interval of major tick
marks on the scale. When set to `auto`, the block automatically adjusts
the tick interval based on the values of the **Maximum** and
**Minimum** parameters.

#### Programmatic Use

To programmatically set the `Tick Interval` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Scale Direction** — Direction of increasing scale values `'Bottom to top'` (default) | `'Top to bottom'`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Label** — Position of label displaying name of connected element `Top` (default) | `Bottom` | `Hide`

You can display the name of the element to which the dashboard block connects in a
label positioned at the top or at the bottom of the block, or you can hide the label. If
you want the label to be visible, specify the position of the label. If you do not want
the label to be visible, specify `Hide`.

**Note**

When the dashboard block is not connected to an element, the label is
blank.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match the aspect ratio of the background image. When the aspect
ratio is unlocked, adding a new background image does not change the aspect ratio of the
block, but instead changes the aspect ratio of the background image to fit the size of
the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block temporarily unlocks the aspect ratio. When you release the
**Shift** key, the aspect ratio locks. When the aspect ratio is
unlocked, pressing the **Shift** key while resizing a block temporarily
locks the aspect ratio. When you release the **Shift** key, the aspect
ratio unlocks.

### **Scale Colors** — Color indications on gauge scale colors for scale ranges

Color specifications for value ranges on the scale. Click the **+**
button to add a scale color. For each color added, specify the minimum and maximum
values of the range in which you want to display that color.

#### Programmatic Use

To programmatically specify the `Scale Colors` parameter, use an
array of structures with these fields:

- `Min` — Minimum value for the color range on the
  scale
- `Max` — Maximum value for the color range on the
  scale
- `Color` —
  `1`-by-`3` vector of
  `double` values between `0` and
  `1` that specify the color for the range in the
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

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Linear Gauge

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match that of the background image. When the aspect ratio is
unlocked, adding a new background image does not change the proportions of the block but
instead stretches or scales the background image to fit the size of the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block unlocks the aspect ratio. When you release the **Shift**
key, the aspect ratio locks. When the aspect ratio is unlocked, pressing the
**Shift** key while resizing a block locks the aspect ratio. When you
release the **Shift** key, the aspect ratio unlocks.

#### Scale

### **Minimum** — Minimum tick mark value `0` (default) | scalar

Finite, real, double, scalar value specifying the minimum tick mark value for the scale. The
parameter value must be less than the value of the **Maximum**
parameter.

#### Programmatic Use

To programmatically set the `Minimum` parameter, use a
`1`-by-`3`
vector containing values for the
`Minimum`, `Tick
Interval`, and `Maximum`
parameters, in that order. To use the
`auto` value for the
`Tick Interval`, leave the
`Tick Interval` position in the
vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — Maximum tick mark value `100` (default) | scalar

Finite, real, double, scalar value specifying the maximum tick mark value for the scale. The
parameter value must be greater than the value of the **Minimum**
parameter.

#### Programmatic Use

To programmatically set the `Maximum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — Interval between major tick marks `auto` (default) | scalar

Finite, real, positive, whole, scalar value specifying the interval of major tick marks on the scale. When set to `auto`, the block automatically adjusts the tick interval based on the values of the **Maximum** and **Minimum** parameters.

#### Programmatic Use

To programmatically set the `Tick Interval` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Origin** — Value on scale from which needle moves and value bar grows `auto` (default) | scalar

Specify the value on the scale from which the needle moves and the value bar grows.
When set to `auto`, the `Origin` is the minimum of
the scale.

**Example:** `0`

### **Scale Direction** — Direction of increasing scale values `'Bottom to top'` (default) | `'Top to bottom'`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **X Offset** — Horizontal offset of left edge of scale bounding box from left edge of block scalar

Specify the horizontal offset of the left edge of the bounding box of
the scale from the left edge of the block as a ratio of the
block width. Relative to the position of the scale when the
offset is `0`, an offset with a negative value
moves the scale left, and an offset with a positive value moves
the scale right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of scale bounding box from top edge of block scalar

Specify the vertical offset of the top edge of the bounding box of the scale from the
top edge of the block as a ratio of the block height. Relative to the position of the
scale when the offset is `0`, an offset with a negative value moves the
scale up, and an offset with a positive value moves the scale down.

**Example:** `1`

### **Width** — Scale width scalar

Specify the width of the bounding box of the scale as a ratio of the
block width.

**Example:** `2`

### **Height** — Scale height scalar

Specify the height of the bounding box of the scale as a ratio of the
block height.

**Example:** `2`

### **Lock Aspect Ratio** — Option to maintain scale aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the scale using the
Property Inspector.

### **Tick Color** — Color of scale tick marks, span line, and block name `[r g b]` vector

Set the color of the scale tick marks, the span line, and the block name. Choose a
color from the palette of standard colors, or specify a custom color.

**Tip**

You can also set the **Tick Color** by choosing a
**Foreground Color** on the **Format** tab of
the Simulink Toolstrip.

To specify the color of the block text, use the **Label Color**
parameter.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the block as a string
or a character vector that defines a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Label Color** — Scale label font color `[r g b]` vector

Choose a font color for the scale label from the palette of standard
colors, or specify a custom color.

**Tip**

To specify the color of the scale, use the **Tick
Color** parameter.

### **Label Offset** — Horizontal distance of scale labels from free end of scale tick marks `0.3` (default) | scalar

Specify the horizontal distance from the scale labels to the free end of their
corresponding tick marks on the scale as a ratio of the width of the bounding box of the
scale.

**Example:** `0.5`

#### Needle

### **Width** — Needle image width scalar

Specify the width of the needle image as a ratio of the block width.

**Example:** `1`

### **Height** — Needle image height scalar

Specify the height of the needle image as a ratio of the block height.

**Example:** `1`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **X Offset** — Horizontal offset of left edge of needle image from scale span line scalar

Specify the horizontal offset of the left edge of the needle image from the span
line of the scale as a ratio of the needle image width. Relative to the position of
the needle image when the offset is `0`, an offset with a negative
value moves the image left, and an offset with a positive value moves the image
right.

**Example:** `1`

### **Y Offset** — Vertical offset of needle image center from scale origin scalar

Specify the vertical offset of the needle image center from the scale origin as a
ratio of the needle image height. Relative to the position of the needle image when
the offset is `0`, an offset with a negative value moves the image
up, and an offset with a positive value moves the image down.

**Example:** `1`

#### Value Bar

### **Offset from Scale** — Distance of left edge of value bar from span line `0` (default) | scalar

Specify the distance from the left edge of the value bar to the span
line as a ratio of the width of the bounding box of the scale.
Relative to the position of the value bar when the offset is
`0`, an offset with a negative
value moves the value bar left, and an offset with a positive
value moves the value bar right.

**Example:** `0.25`

### **Size** — Value bar thickness scalar

Specify the thickness of the value bar as a ratio of the width of the bounding box of
the scale.

**Example:** `0.3`

#### Background Image

### **Use Background Color** — Option to specify solid block background color `off` (default) | `on`

For the block background, you can provide a background image or select a solid color.
To select a solid background color, select this parameter. To provide a background
image, clear this parameter.

**Note**

Changing the background color using the **Format** tab of the
Simulink Toolstrip removes the background image and enables the **Use
Background Color** parameter.

**Example:** `on`

### **Color** — Block background color `[r g b]` vector

To use a solid background color, select the **Use Background Color**
parameter. Then, choose a background color from the palette of standard colors, or
specify a custom color.

**Tip**

You can also specify the **Background Color** in the
**Format** tab of the Simulink Toolstrip.

To specify the color of the block text, use the **Font Color**
parameter.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1` that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner Radius** — Corner radius of area with block background color scalar

Specify the corner radius of the area covered by the block background color as a ratio
of half of the smaller of the two block dimensions, width or height.

**Example:** `0.25`

#### Foreground Image

### **X Offset** — Horizontal offset of left edge of foreground image from left edge of block scalar

Specify the horizontal offset of the left edge of the image from the left edge of the
block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of foreground image from top edge of block scalar

Specify the vertical offset of the top edge of the image from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Width** — Foreground image width scalar

Specify the width of the foreground image as a ratio of the block width.

**Example:** `0.5`

### **Height** — Foreground image height scalar

Specify the height of the foreground image as a ratio of the block height.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain foreground image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

## Libraries

Simulink / Dashboard / Customizable Blocks

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

**Introduced in R2020a**

### R2024b: Unlock dashboard block aspect ratio with keyboard

If the aspect ratio of a block from the Dashboard library is locked, you can temporarily
unlock the aspect ratio by pressing **Shift**. When you release the
**Shift** key, the aspect ratio locks.

If the aspect ratio is unlocked, pressing **Shift** temporarily locks the
aspect ratio. When you release the **Shift** key, the aspect ratio
unlocks.

### R2024a: Deploy dashboard panel as web app or standalone desktop app

With a Simulink
Compiler™ license, you can now deploy a dashboard panel, packaged with the model to
which the panel connects, as a standalone desktop app or as a web app. You can use the app
to operate the controls and monitor the displays on the panel independent of Simulink.

To learn how to deploy panels, see Deploy Dashboard Panel as App.

### R2024a: Dock dashboard panels

Starting in R2024a, you can dock dashboard panels to the Simulink Editor window. You can use the docked panel to monitor signals and control
parameters during simulation without covering the model diagram in the canvas.

For more information, see Dock Panels.

### R2023b: Open panel in new window

Starting in R2023b, you can open a dashboard panel in a new window. To do so, select the
panel and pause on the ellipsis that appears. In the action menu that expands, click Open In
New Window .

You can minimize and restore the new window containing the panel separately from the
model window. From the panel window, you can run, pause, stop, and step through the
simulation. In the panel window, you can edit the panel and the blocks it contains.

To return the panel to the model canvas, in the panel window toolstrip, click Open in
canvas .

For more information about opening a panel in a new window, see Open Panels in New Window.

### R2023a: Persistent panels tab in Simulink Toolstrip

When you add a dashboard panel to a model, the **Panels** tab appears
in the Simulink Toolstrip and shows options for managing and editing panels.

Previously, the **Panels** tab was only visible when a panel was
selected. Starting in R2023a, the **Panels** tab stays visible when no
panel is selected.

The **Panels** tab also contains these new options:

- You can add an empty panel.
- You can rename the selected panel.
- You can hide the selected panel.

### R2022b: Undo and redo support for customizable dashboard blocks in panel

Starting in R2022b, you can undo and redo the changes you make to customizable dashboard
blocks that are in a panel.

To undo or redo a change:

1. Click the panel or a block in the panel.
2. Press **Ctrl+Z** to undo the change, or press **Ctrl+Y**
   to redo the change.

**Note**

The keyboard shortcuts are based on Windows®. On a Mac, press **command** (⌘) instead of
**Ctrl**.

### R2022b: Toolstrip support for panels

Starting in R2022b, you can use the Simulink Toolstrip to manage and edit panels and the dashboard blocks that they
contain.

When you click a dashboard block in a panel, the toolstrip tab for the block appears.
For example, when you click a Circular Gauge block, the
**Gauge** tab appears in the toolstrip.

When you click a panel, the **Panel** tab appears in the toolstrip. The
tab provides these options:

- Manage the visibility of panels in the model.
- Fit all unhidden panels within the current view.
- Collapse the selected panel.
- Customize the size and the contents of the panel.
- Set a custom background image for the selected panel.
- Add a new tab to the selected panel.

### R2022b: Extended support for customizable Dashboard blocks on Raspberry Pi boards

Starting in R2022b, the Simulink Support Package for Raspberry Pi® Hardware supports deploying these blocks from the **Customizable
Blocks** library on your Raspberry Pi boards:

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

You can customize the visual aspects of the blocks in a Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on a
web browser you launch from a Raspberry Pi terminal.

### R2022b: Extended support for customizable Dashboard blocks on Android devices

Starting in R2022b, the Simulink Support Package for Android® Devices supports deploying these blocks from the **Customizable
Blocks** library on your Android devices:

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

You can customize the visual aspects of the blocks in a Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on
your Android device as well as on your web browser.

### R2022a: Change scale direction

Starting in R2022a, you can change the direction of the scale of these blocks from the
**Customizable Blocks** library:

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: Specify origin for value bar and needle

The origin of a scale is the value on the scale from which the needle moves and the
value bar grows. Starting in R2022a, you can specify an origin for the scales of these
blocks from the **Customizable Blocks** library:

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.

### R2021a: Customizable dashboard block gauges move to Customizable Blocks library

In prior releases, the Dashboard library contained the Circular Gauge,
Horizontal Gauge, and Vertical Gauge blocks. Starting in
R2021a, these blocks are in the Customizable Blocks sublibrary within the Dashboard
library.

### R2021a: Dashboard gauge blocks support foreground, background, and font color

Starting in R2021a, you can change the foreground, background, and font color of these
blocks:

- Gauge
- Half Gauge
- Linear Gauge
- Quarter Gauge
- Circular Gauge
- Horizontal Gauge
- Vertical Gauge

### R2020b: Simulink toolstrip support for dashboard blocks

Starting in R2020b, the Simulink Toolstrip opens a block-specific tab when you select a block in your model
from the Simulink Dashboard library or from the Flight Instruments library in the Aerospace Blockset™ Flight Control Analysis Library. From the toolstrip, you can connect,
disconnect, and modify connections for the selected block. You can also jump to the model
element connected to the selected block and add the selected block to a panel.

### R2020b: Add a foreground image to the Horizontal Gauge, Vertical Gauge, and Circular Gauge blocks

Starting in R2020b, you can add a foreground image to a Horizontal Gauge, Vertical
Gauge, or Circular Gauge block in your model.

## Description

Display signal value during simulation on vertical gauge with customizable appearance

During simulation, the Vertical Gauge block displays the value of the
connected signal on a linear gauge that you can customize to look like a gauge in a real
system. You can modify the range and tick values on the Vertical Gauge block to
fit your data. Use the Vertical Gauge block with other dashboard blocks to
build an interactive dashboard of controls and indicators for your model.

### Customize Vertical Gauge Blocks

When you add a Vertical Gauge block to your model, the block is
preconfigured with a default design. You can use the block with the default design or
customize the appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the circular gauge.
To access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Vertical Gauge block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a needle image. | Yes | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |
| Specify the location of the origin from which the value bar grows. | No | Yes |
| Change the color and opacity of the scale tick marks, scale labels, or value bar. | Yes | Yes |
| Specify the scale direction as left to right or right to left. | No | Yes |
| Change the size of the scale and needle. | No | Yes |
| Change the position the scale and needle. | No | Yes |

To change the color and opacity of the scale tick marks, scale labels, or value bar
using the toolbar, in the second section of the toolbar from the left, select the component
whose color you want to change. To change the color, click the color wheel. To change the
opacity, move the slider.

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas.

When you finish editing the design, to exit design mode, click the
**X** in the upper right of the canvas.

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

This animation shows how to connect the Vertical Gauge block to your
model.

An unconnected Vertical Gauge block connects to the signal that a Sine Wave block sends to an Outport block.
