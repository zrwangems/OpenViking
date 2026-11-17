---
type: simulink-block
title: 'Half Gauge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customhalfgauge'
documentation_source_path: 'slref/customhalfgauge.html'
language: en
---

# Half Gauge

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Connection
  summary: Signal to connect and display signal connection options
  group: Parameters
  block_parameter: Binding
  type: Simulink.HMI.SignalSpecification
  default: '[]'
- name: Minimum
  summary: Minimum tick mark value 0 (default) | scalar
  group: Parameters
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Maximum
  summary: Maximum tick mark value 100 (default) | scalar
  group: Parameters
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Tick Interval
  summary: Interval between major tick marks auto (default) | scalar
  group: Parameters
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Direction
  summary: Direction of increasing scale values Clockwise (default) | Counterclockwise
  group: Parameters
  block_parameter: ScaleDirection
  type: character vector
  values: '''Clockwise'' | ''Counterclockwise'''
  default: '''Clockwise'''
- name: Label
  summary: Position of label displaying name of connected element Hide (default) | Bottom | Top
  group: Parameters
  block_parameter: LabelPosition
  type: character vector
  values: '''Hide'' | ''Bottom'' | ''Top'''
  default: '''Hide'''
- name: Lock Aspect Ratio
  summary: Option to maintain block aspect ratio on (default) | off
  group: Parameters
- name: Scale Colors
  summary: Color indications on gauge scale colors for scale ranges
  group: Parameters
  block_parameter: ScaleColors
  type: structure array
  default: 0x1 struct array
- name: Lock Aspect Ratio
  summary: Option to maintain block aspect ratio on (default) | off
  group: Design
- name: Minimum
  summary: Minimum tick mark value 0 (default) | scalar
  group: Design
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Maximum
  summary: Maximum tick mark value 100 (default) | scalar
  group: Design
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Tick Interval
  summary: Interval between major tick marks auto (default) | scalar
  group: Design
  block_parameter: Limits
  type: 1x3 vector
  default: '[0 -1 100]'
- name: Origin
  summary: Value on scale from which needle moves and value bar grows auto (default) | scalar
  group: Design
- name: Direction
  summary: Direction of increasing scale values Clockwise (default) | Counterclockwise
  group: Design
  block_parameter: ScaleDirection
  type: character vector
  values: '''Clockwise'' | ''Counterclockwise'''
  default: '''Clockwise'''
- name: Arc
  summary: Arc length of scale 180 (default) | scalar
  group: Design
- name: Start Angle
  summary: Angular location of scale minimum 180 (default) | scalar
  group: Design
- name: Inner Radius
  summary: Radius of free end of scale tick marks scalar
  group: Design
- name: Outer Radius
  summary: Span line radius scalar
  group: Design
- name: X Offset
  summary: Horizontal offset of left edge of scale bounding box from left edge of block scalar
  group: Design
- name: Y Offset
  summary: Vertical offset of top edge of scale bounding box from top edge of block scalar
  group: Design
- name: Width
  summary: Scale width scalar
  group: Design
- name: Height
  summary: Scale height scalar
  group: Design
- name: Lock Aspect Ratio
  summary: Option to maintain scale aspect ratio on (default) | off
  group: Design
- name: Tick Color
  summary: Color of scale tick marks, span line, and block name [r g b] vector
  group: Design
  block_parameter: ForegroundColor
  type: character vector | string
  values: '[r g b] vector'
- name: Minor Tick Height
  summary: Height of minor tick marks on scale 1 (default) | scalar
  group: Design
- name: Label Color
  summary: Scale label font color [r g b] vector
  group: Design
- name: Label Radius
  summary: Distance of scale labels from scale center scalar
  group: Design
- name: Width
  summary: Needle image width scalar
  group: Design
- name: Height
  summary: Needle image height scalar
  group: Design
- name: Lock Aspect Ratio
  summary: Option to maintain image aspect ratio on (default) | off
  group: Design
- name: Rotate Image
  summary: Rotation of needle image 180 (default) | scalar
  group: Design
- name: Offset from Center
  summary: Offset of needle image center from scale center 0 (default) | scalar
  group: Design
- name: Use Background Color
  summary: Option to specify solid block background color off (default) | on
  group: Design
- name: Color
  summary: Block background color [r g b] vector
  group: Design
  block_parameter: BackgroundColor
  type: character vector | string
  values: '[r g b] vector'
- name: Opacity
  summary: Block background opacity 1 (default) | scalar
  group: Design
- name: Corner radius
  summary: Offset of outer edge of area with block background color from tick marks scalar
  group: Design
- name: X Offset
  summary: Horizontal offset of left edge of foreground image from left edge of block scalar
  group: Design
- name: Y Offset
  summary: Vertical offset of top edge of foreground image from top edge of block scalar
  group: Design
- name: Width
  summary: Foreground image width scalar
  group: Design
- name: Height
  summary: Foreground image height scalar
  group: Design
- name: Lock Aspect Ratio
  summary: Option to maintain foreground image aspect ratio on (default) | off
  group: Design
```

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

### **Direction** — Direction of increasing scale values `Clockwise` (default) | `Counterclockwise`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Label** — Position of label displaying name of connected element `Hide` (default) | `Bottom` | `Top`

You can display the name of the element to which the dashboard block connects in a
label positioned at the top or bottom of the block, or you can hide the label. If you
want the label to be visible, specify the position of the label. If you do not want the
label to be visible, select `Hide`.

**Note**

When the dashboard block is not connected to an element, the label is
blank.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

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

#### Circular Gauge

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

### **Direction** — Direction of increasing scale values `Clockwise` (default) | `Counterclockwise`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Arc** — Arc length of scale `180` (default) | scalar

Specify the arc length of the scale as a scalar value, measured in degrees.

**Example:** `90`

### **Start Angle** — Angular location of scale minimum `180` (default) | scalar

Specify the angular location of the minimum scale value, measured in degrees
clockwise from the horizontal axis pointing right.

**Example:** `0`

### **Inner Radius** — Radius of free end of scale tick marks scalar

Specify the radius of the free end of the scale tick marks as a ratio of the
smaller of the two dimensions of the bounding box of the scale, width or
height. The `Inner Radius` can be larger than the
`Outer Radius`.

**Example:** `0.5`

### **Outer Radius** — Span line radius scalar

Specify the span line radius as a ratio of the smaller of the two dimensions
of the bounding box of the scale, width or height. The `Outer
Radius` can be smaller than the `Inner
Radius`.

**Example:** `0.5`

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

### **Minor Tick Height** — Height of minor tick marks on scale `1` (default) | scalar

Specify the height of the minor tick marks on the scale as a ratio of the height to
the difference between the outer and inner radii.

**Example:** `0.5`

### **Label Color** — Scale label font color `[r g b]` vector

Choose a font color for the scale label from the palette of standard
colors, or specify a custom color.

**Tip**

To specify the color of the scale, use the **Tick
Color** parameter.

### **Label Radius** — Distance of scale labels from scale center scalar

Specify the distance of the scale labels from the center of the scale as a ratio
of the radius of the scale.

**Example:** `0.5`

#### Needle

### **Width** — Needle image width scalar

Specify the width of the needle image as a ratio of the smaller of the two
dimensions of the bounding box of the scale, width or length.

**Example:** `1`

### **Height** — Needle image height scalar

Specify the height of the needle image as a ratio of the smaller of the two
dimensions of the bounding box of the scale, width or length.

**Example:** `1`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Rotate Image** — Rotation of needle image `180` (default) | scalar

Rotate the needle image about its center in 90 degree increments.

**Example:** `90`

### **Offset from Center** — Offset of needle image center from scale center `0` (default) | scalar

Specify the distance from the center of the needle image to the center of the
scale as a ratio of the diameter of the scale.

**Example:** `1`

#### Background Image

### **Use Background Color** — Option to specify solid block background color `off` (default) | `on`

For the block background, you can provide a background image or select a solid
color. To select a solid background color, turn **Use Background
Color** on. To provide a background image, turn **Use Background
Color** off.

**Note**

Changing the background color using the toolstrip removes the background image
and enables the **Use Background Color** option.

When you use a solid background with the Half Gauge block, you
can design gauges that cover with angular spans other than the default 180° of the
half gauge. When the scale arc angle is 180° or smaller, the background shape
conforms to the scale.

Half Gauge block with noncircular orange background area

**Example:** `on`

### **Color** — Block background color `[r g b]` vector

To select a solid background color, enable the **Use Background
Color** parameter. Then, choose a background color from the palette of
standard colors, or specify a custom color.

**Note**

When you use a solid background with the Half Gauge block, you
can design gauges that cover with angular spans other than the default 180° of the
half gauge. When the scale arc angle is 180° or smaller, the background shape
conforms to the scale.

Half Gauge block with noncircular orange background area

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1` that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner radius** — Offset of outer edge of area with block background color from tick marks scalar

Specify the offset of the outer edge of the area covered by the block background
color from tick marks as a scalar value from `0` to
`1`.

**Example:** `0.1`

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

**Introduced in R2024a**

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

## Description

Display signal value during simulation on gauge shaped as half-circle with customizable appearance

The Half Gauge block displays the value of the connected signal on a gauge
with a half-circle shape. You can design the block to look like a gauge in a real
system.

The Half Gauge block displays the instantaneous value of the connected
signal throughout simulation. You can modify the range and tick values on the Half
Gauge block to fit your data. Use the Half Gauge block with other
dashboard blocks to build an interactive dashboard of controls and indicators for your
model.

### Customize Half Gauge Blocks

When you add a Half Gauge block to your model, the block is preconfigured
with a default design. You can use the block with the default design or customize the
appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the half gauge. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Half Gauge block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a needle image. | Yes | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |
| Change the arc length of the scale. | No | Yes |
| Specify the location of the origin from which the value bar grows. | No | Yes |
| Change the color and opacity of the scale tick marks, scale labels, or value bar. | Yes | Yes |
| Specify the scale direction as clockwise or counterclockwise. | No | Yes |
| Change the size of the scale and needle. | No | Yes |
| Change the position the scale and needle. | No | Yes |

To change the color and opacity of the scale tick marks, scale labels, or value bar
using the toolbar, in the second section of the toolbar from the left, select the component
whose color you want to change. To change the color, click the color wheel. To change the
opacity, move the slider.

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. The movement of the needle is limited to the line that passes
through the center of the block and the minimum value on the scale.

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

This animation shows how to connect the Half Gauge block to your
model.

An unconnected Half Gauge block connects to the signal that a Sine Wave block sends to an Outport block.
