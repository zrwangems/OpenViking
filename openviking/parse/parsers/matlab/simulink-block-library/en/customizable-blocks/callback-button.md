---
type: simulink-block
title: 'Callback Button'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customcallbackbutton'
language: en
---

# Callback Button

Execute MATLAB code using button with customizable appearance

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

The Callback Button block runs MATLAB® code in response to a click (immediate release of the pointer) or a press
(delayed release of the pointer). You can specify different code for the click than the press.
When you press the button, the code either executes after a time span or at time intervals
that you specify. You can customize the appearance of the Callback Button block
to look like a button in a real system. Use the Callback Button block with
other dashboard blocks to create an interactive dashboard to control your model.

When a Callback Button block is *active*, you can
interact with the gadget the block represents. Clicking an active Callback
Button block pushes a virtual button. While you press your pointer, the button is
pushed. When you release your pointer, you release the button. Callback Button
blocks are active when the simulation is running, the block is in a panel that is open in its
own window or docked and unlocked, or at least one of the callbacks triggered by a click or
press has a nonempty value. To select an active Callback Button block without
pushing the button, press **Shift**, and then click the block. To open the Block
Parameters dialog box of an active Callback Button block, press
**Shift**, and then double-click the block.

When a block is inactive, you can only interact with the block, for example, taking
actions such as resizing or dragging the block. To temporarily activate an inactive
Callback Button block, click the block. When you deselect the Callback
Button block, the block becomes inactive again.

Specify what you want pushing the button to do using callback functions:

- `PressFcn` functions run while the button is pushed. You can
  configure the button to run the `PressFcn` function only once while the
  button is pushed, or you can specify a repeat interval. To run the function only once,
  specify a repeat interval of `0`.
- `ClickFcn` functions run when you release the button.

You can configure the button to remain pushed when you release the pointer by setting the
**Button Type** to `Latched`. When you choose the
latched button type:

- To latch the button, click the button.
- To unlatch the button, click the button again.

The `PressFcn` function runs while the button is latched. The
`ClickFcn` function runs once when you latch the button and once when you
unlatch the button.

You can use states to specify how the appearance of the Callback Button
block changes when you interact with the button:

- While you push the button, the block is in the `Pressed`
  state.
- When the button is latched and you are not pushing it, the block is in the
  `Latched` state.
- When the button is latched and you are pushing it, the block is in the
  `Latched and Pressed` state.
- When the block is not in any of these three states, it is in the
  `Default` state.

A state pairs pointer actions with:

- A state label
- A state icon
- A state image

### Customize Callback Button Blocks

When you add a Callback Button block to your model, the block is
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

In design mode, you can use the toolbar above the block to customize the callback
button. To access additional customization options or to enter exact values for design
settings, use the **Design** tab in the Property Inspector.

Customizable Callback Button block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Callback Button block, you configure the block
appearance for each state. When you configure the **Block Type** as
`Momentary`, the block has two states. When you configure the
**Block Type** as `Latch`, the block has four.
To select a state to customize, use the drop-down list in the toolbar. Alternatively, on
the **Design** tab, select the **States** component and
then select from the **Select State** list.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state label text. | No | Yes |
| Specify the color and opacity of the state label text. | Yes | Yes |
| Upload a state image. | Yes | Yes |
| Upload a state icon. | Yes | Yes |
| Change the size of the state image and state icon. | No | Yes |
| Change the position of the state label, state image, and state icon. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. To resize a component specific to a state, such as the state
image, select the state in the toolbar, and then resize or reposition the component.

**Design Mode Actions that Apply to All States**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a background image. | No | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

When you finish editing the design, to exit design mode, click the
**X** in the upper right of the canvas.

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

#### Main

### **Button Type** — Button response to click `Momentary` (default) | `Latch`

Specify how the block responds to a click.

- `Momentary` — The button changes state only while
  pressed. When you release the click, the button returns to its default
  state.
- `Latch` — The button latches the state change
  when clicked. The button remains in the pressed state until you click it
  again.

When you configure **Button Type** as
`Momentary`, the block has these states:

- `Default` — Default state for the block when it
  is not pressed
- `Pressed` — Block state when the block is
  pressed

When you configure **Button Type** as
`Latch`, the block has these states:

- `Default` — Default state for the block when it
  is not pressed.
- `Pressed` — Transitional state when you press the
  button while it is in the `Default` state. The
  block transitions to the `Latched` state when you
  release the click.
- `Latched` — Latched state for the block when it
  is not pressed.
- `Latched and Pressed` — Transitional state when
  you press the button while it is in the `Latched`
  state. The block transitions to the `Default` state
  when you release the click.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ButtonType` |
| **Type:** string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

### **Button Text** — Button label text `'Callback Button'` (default) | string | character array

Specify the text for the button label. The label is applied to the button for the
state that is selected in the **Select State** section of the
**States** component on the **Design** tab.

#### Programmatic Use

Specify the `ButtonText` parameter for the block as a string or
a character vector.

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

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

#### Callbacks

### **ClickFcn** — MATLAB code that executes in response to click MATLAB code

MATLAB code that executes in response to a click of the button.

Every time you click the button, the `ClickFcn` code executes
once, at the point in time when you release the click.

To specify code for the `ClickFcn`, select
`ClickFcn` from the drop-down menu. Enter the code in the
text box below the menu.

#### Programmatic Use

Specify the `ClickFcn` parameter for the block as MATLAB code that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `ClickFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

### **PressFcn** — MATLAB code that executes in response to press MATLAB code

MATLAB code that executes in response to a press of the button.

While the button is in the pressed state, the `PressFcn` code
executes once when the **Press Delay** time has elapsed and
periodically at every **Repeat Interval**.

To specify code for the `PressFcn`, select
`PressFcn` from the drop-down menu. Enter the code in the
text box below the menu.

How you press the button to execute the `PressFcn` code
depends on the **Button Type**.

- If the **Button Type** is
  `Momentary`, hold down your click for the duration
  that you want to press the button.
- If the **Button Type** is `Latch`,
  click to press the button, but do not hold down your click. The button remains
  pressed until you click it again.

**Note**

Every time that you click on the button, even when you do so as part of the
process for pressing the button, the `ClickFcn` code
executes once, at the point in time when you release the click.

#### Programmatic Use

Specify the `PressFcn` parameter for the block as MATLAB code that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `PressFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

### **Press Delay (ms)** — Time to hold button for press `500` (default) | scalar

Amount of time required to cause the `PressFcn` code to
execute.

#### Dependencies

**Press Delay (ms)** is visible only when
`PressFcn` is selected as the callback.

#### Programmatic Use

Specify the `PressDelay` parameter for the block as a positive
scalar value.

|  |
| --- |
| **Block Parameter:** `PressDelay` |
| **Type:** scalar |

### **Repeat Interval (ms)** — Time interval to repeat `PressFcn` code `0` (default) | scalar

Time interval after which the `PressFcn` code executes again
if the Callback Button block is still pressed.

#### Dependencies

**Repeat Interval (ms)** is visible only when
`PressFcn` is selected as the callback.

#### Programmatic Use

Specify the `RepeatInterval` parameter for the block as a
positive scalar value.

|  |
| --- |
| **Block Parameter:** `RepeatInterval` |
| **Type:** scalar |

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Button

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

#### States

### **Select State** — Selection of state to configure `Default` (default) | `Pressed` | `Latched` | `Latched and Pressed`

Select a state that you want to configure from the drop-down menu in the
**Select State** section of the **States**
component. When the **Button Type** is
`Momentary`, you can select these states:

- `Default` — Default state for the block when it
  is not pressed
- `Pressed` — Block state when the block is
  pressed

When the **Button Type** is `Latch`, you can
select these states:

- `Default` — Default state for the block when it
  is not pressed.
- `Pressed` — Transitional state when you press the
  button while it is in the `Default` state. The
  block transitions to the `Latched` state when you
  release the click.
- `Latched` — Latched state for the block when it
  is not pressed.
- `Latched and Pressed` — Transitional state when
  you press the button while it is in the `Latched`
  state. The block transitions to the `Default` state
  when you release the click.

**Note**

You can configure all of the parameters in the **States**
component of the **Design** tab for a state. For example, you can
select an icon that will appear on the button when it is in the state. When you
configure any of the parameters in the **States** component, the
changes are applied to the state that is selected in the **Select
State** section of the **States** component.

**Example:** `Pressed`

### **Text** — Button label text `'Callback Button'` (default) | string | character array

Specify the text for the button label. The label is applied to the button for the
state that is selected in the **Select State** section of the
**States** component on the **Design** tab.

#### Programmatic Use

Specify the `ButtonText` parameter for the block as a string or
a character vector.

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

### **Color** — Label font color `[r g b]` vector

Choose a font color for the label text from the palette of standard colors, or specify
a custom color. The color is applied to the label text for the state that is selected in
the **Select State** section of the **States**
component on the **Design** tab.

### **Horizontal Alignment** — Horizontal alignment of label and icon pair with block `Left` (default) | `Center` | `Right`

Set the alignment of the label and icon pair in the horizontal direction. The table
lists the horizontal position of the label and icon pair when the **X
Offset** is zero. A nonzero **X Offset** moves the label
and icon pair from the position listed in the table.

| Alignment | Position of the Label and Icon Pair |
| --- | --- |
| `Left` | The left edge of the label and icon pair is at the left edge of the block. |
| `Center` | The horizontal middle of the label and icon pair is at the horizontal middle of the block. |
| `Right` | The right edge of the label and icon pair is at the right edge of the block. |

### **Vertical Alignment** — Vertical alignment of label and icon pair with block `Center` (default) | `Bottom` | `Top`

Set the alignment of the label and icon pair in the vertical direction. The table
lists the vertical position of the label and icon pair when the **Y
Offset** is zero. A nonzero **Y Offset** moves the label
and icon pair from the position listed in the table.

| Alignment | Position of the Label and Icon Pair |
| --- | --- |
| `Top` | The top edge of the label and icon pair is at the top edge of the block. |
| `Center` | The vertical middle of the label and icon pair is at the vertical middle of the block. |
| `Bottom` | The bottom edge of the label and icon pair is at the bottom edge of the block. |

### **Icon and Label X Offset** — Horizontal offset of icon and label pair from block `0` (default) | scalar

How the **X Offset** is measured depends on the value of the
**Horizontal Alignment**. The table lists how the offset is
measured for each **Horizontal Alignment** value. Relative to the
position when the offset is `0`, an offset with a negative value moves
the text left, and an offset with a positive value moves the text right.

| **Horizontal Alignment** | Offset |
| --- | --- |
| `Left` | Specify the horizontal offset of the left edge of the label and icon pair from the left edge of the block as a ratio of the block width. |
| `Center` | Specify the horizontal offset of the horizontal middle of the label and icon pair from the horizontal middle of the block as a ratio of the block width. |
| `Right` | Specify the horizontal offset of the right edge of the label and icon pair from the right edge of the block as a ratio of the block width. |

### **Icon and Label Y Offset** — Vertical offset of icon and label pair from block `0` (default) | `scalar`

How the **Y Offset** is measured depends on the value of the
**Vertical Alignment**. The table lists how the offset is measured
for each **Vertical Alignment** value. Relative to the position of the
text when the offset is `0`, an offset with a negative value moves the
text up, and an offset with a positive value moves the text down.

| **Vertical Alignment** | Offset |
| --- | --- |
| `Top` | Specify the vertical offset of the top edge of the label and icon pair from the top edge of the block as a ratio of the block width. |
| `Center` | Specify the vertical offset of the vertical middle of the label and icon pair from the vertical middle of the block as a ratio of the block width. |
| `Bottom` | Specify the vertical offset of the bottom edge of the label and icon pair from the bottom edge of the block as a ratio of the block width. |

### **Icon Placement** — Placement of icon relative to label `Left` (default) | `Top` | `Right` | `Bottom`

Specify the placement of the icon relative to the label.

**Note**

Changing the placement of the icon moves the label, but does not change the offset
or alignment of the label.

### **Icon Width** — Icon width scalar

Specify the icon width as a ratio of the font height of the label text.

**Example:** `0.5`

### **Icon Height** — Icon height scalar

Specify the icon height as a ratio of the font height of the label text.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Enable this option to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Image X Offset** — Horizontal offset of left edge of image from left edge of block scalar

Specify the horizontal offset of the left edge of the image from the left edge of the
block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Image Y Offset** — Vertical offset of top edge of image from top edge of block scalar

Specify the vertical offset of the top edge of the image from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Image Width** — Image width scalar

Specify the image width as a ratio of the block width.

**Example:** `0.5`

### **Image Height** — Image height scalar

Specify the image height as a ratio of the block height.

**Example:** `0.5`

#### Background Image

### **Use Background Color** — Option to specify solid background color for button `off` (default) | `on`

You can provide a background image for the block or select a solid background
color for the button. To select a solid background color for the button, select this
parameter. To provide a background image for the block, clear this parameter.

**Note**

- The state images are not visible when you set a solid background color for
  the button. To make the state images visible, turn off **Use Background
  Color**.
- Changing the background color using the **Format** tab of
  the Simulink Toolstrip removes the background image and turns on the
  **Use Background Color** parameter.

**Example:** `on`

### **Color** — Button background color `[r g b]` vector

To select a solid background color for the button, enable the **Use
Background Color** parameter. Then, choose a background color from the
palette of standard colors, or specify a custom color.

**Note**

The state images are not visible when you set a solid background color. To make
the state images visible, in the Property Inspector, on the
**Design** tab, in the **Background Image**
component, turn off **Use Background Color**.

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
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the opacity of the solid background color as a scalar value from 0 to
1.

**Example:** `0.5`

### **Corner Radius** — Corner radius of area with block background color scalar

Specify the corner radius of the area covered by the solid background
color.

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
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2021b**

### R2025a: Push callback button with one click instead of two when simulation is not running

When a Simulink block from the Dashboard or Customizable Blocks library is
*active*, you can interact with the gadget the block represents. For
example, you can push a button or flip a switch. When a block is inactive, you can only
interact with the block. For example, you can move or resize the block. To interact with the
gadget when a block is inactive, you can temporarily activate the block by clicking the
block. When you deselect the block, the block becomes inactive again.

By default, all blocks from the Dashboard and Customizable Blocks libraries are active
during simulation. Blocks promoted to a dashboard panel are also active when the panel is
open in its own window or docked and unlocked. In previous releases, the blocks are inactive
in all other cases. Specifically, when the simulation is not running, a Callback
Button block in the model canvas or in a panel that is neither open in its own
window nor docked and unlocked is inactive. To push the button, you must click the block
twice: once to temporarily activate the block, and once to push the button.

Starting in R2025a, Callback Button blocks for which at least one of the
callbacks triggered by pushing the button has a nonempty value are always active, regardless
of whether the simulation is running. This change means when the simulation is not running,
you can push callback buttons with a single click. When the simulation is not running, you
can move and resize active Callback Button blocks.

There is also a new keyboard shortcut for interacting with active blocks. Clicking an
active Callback Button block or an active block from the Dashboard or
Customizable Blocks library that is connected to a parameter or variable value both selects
the block and interacts with the gadget the block represents. For example, clicking an
unselected active connected Push Button block both selects the block and
pushes the button. Starting in R2025a, you can select the block without interacting with the
gadget by pressing **Shift** and then clicking the block. Similarly, you can
open the Block Parameters dialog box by pressing **Shift** and then
double-clicking the block.

### R2024b: Unlock dashboard block aspect ratio with keyboard

If the aspect ratio of a block from the Dashboard library is locked, you can temporarily
unlock the aspect ratio by pressing **Shift**. When you release the
**Shift** key, the aspect ratio locks.

If the aspect ratio is unlocked, pressing **Shift** temporarily locks the
aspect ratio. When you release the **Shift** key, the aspect ratio
unlocks.

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

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.
