---
type: simulink-block
title: 'Display'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customdisplay'
---

# Display

Display signal value during simulation with customizable appearance

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

The Display block connects to a signal in your model and displays the
signal value during simulation. The Display block can display scalar signals.
When you use the Display block in the Customizable Blocks library, you can customize the
appearance of the block to look like a real display in your system. Use the
Display block with other dashboard blocks to build an interactive dashboard
of controls and indicators for your model.

### Customize Display Blocks

When you add a Display block to your model, the block is preconfigured
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

In design mode, you can use the toolbar above the block to customize the display. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Display block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the font. Choose from a list of WYSIWYG (what you see is what you get) fonts that look the same on all platforms. | Yes | Yes |
| Change the font size. | Yes | Yes |
| Change the text color. | Yes | Yes |
| Make the text bold, italic, or underlined. | Yes | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |
| Change the position of the text within the block. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also reposition the text interactively in the
canvas.

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

An unconnected Display block connects to the signal that a Sine Wave block sends to
an Outport block.

An unconnected Half Gauge block connects to the signal that a Sine Wave block sends to a Display block.

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

When you connect the Display block to the signal output
by a String Constant block, the format for displaying signal values is
`string`, regardless of the value of the
**Format** parameter. Similarly, when you connect the
Display block to the signal output by an Enumerated
Constant block, the format for displaying signal values is
`enum`, regardless of the value of the **Format** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character array | string |
| **Values:** `'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **Default:** `'short'` |

### **Format String** — Custom string to format data `'%d'` (default) | string

Specify a custom string to format displayed signal data. The format string
consists of text and format operators, which start with a `%` sign
and end with a conversion character. Use the format operators at the place in the
string where you want the signal data to display. For more information about supported
formatting operators, see the `formatSpec` input of the `compose` function.

**Example:** `The value of pi is %.2f` displays the value of the
connected signal within a sentence.

**Example:** `$%.2f` displays the value of the connected signal with a
dollar sign and two decimal places.

#### Dependencies

To enable this parameter, set **Format** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |
| **Type:** character array | string |
| **Default:** `'%d'` |

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

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Display

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

#### Text

### **Font** — Font `Courier Prime` | `DSEG7-Classic` | `Noto Sans` | `Noto Serif` | `Roboto` | `Ubuntu`

Choose from a list of WYSIWYG (what you see is what you get) fonts that look the
same on all platforms.

### **Size** — Font size scalar

Choose from a list of font sizes between `6` and
`72`.

### **Text Color** — Text color `[r g b]` vector

Choose a text color from the palette of standard colors, or specify a custom
color.

### **X Offset** — Horizontal offset of center of text from center of block scalar

Specify the horizontal offset of the center of the text from the center of the
block as a ratio of the block width. Relative to the position of the text when the
offset is `0`, an offset with a negative value moves the text left,
and an offset with a positive value moves the text right.

### **Y Offset** — Vertical offset of center of text from center of block scalar

Specify the vertical offset of the center of the text from the center of the block
as a ratio of the block height. Relative to the position of the text when the offset
is `0`, an offset with a negative value moves the text up, and an
offset with a positive value moves the text down.

### **Width** — Width of text bounding box scalar

Specify the width of the bounding box of the text as a ratio of the block
width.

### **Height** — Height of text bounding box scalar

Specify the height of the bounding box of the text as a ratio of the block
height.

### **Lock Aspect Ratio** — Option to maintain text bounding box aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the bounding box
of the text in the Simulink canvas.

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

**Introduced in R2023b**

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

### R2024a: Display block from Customizable Blocks library can display strings

Starting in R2024a, the Display block from the
Customizable Blocks library can connect to and display signals that are strings.

### R2023b: Open Panel in New Window

Starting in R2023b, you can open a dashboard panel in a new window. To do so, select the
panel and pause on the ellipsis that appears. In the action menu that expands, click Open in
New Window .

You can minimize and restore the new window containing the panel separately from the
model window. From the panel window, you can run, pause, stop, and step through the
simulation. In the panel window, you can edit the panel and the blocks it contains.

To return the panel to the model canvas, in the panel window toolstrip, click Open in
canvas .

For more information about opening a panel in a new window, see Open Panels in New Window.
