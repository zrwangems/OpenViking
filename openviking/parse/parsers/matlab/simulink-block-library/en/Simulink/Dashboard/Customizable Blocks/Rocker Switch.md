---
type: simulink-block
title: 'Rocker Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customrockerswitch'
documentation_source_path: 'slref/customrockerswitch.html'
language: en
---

# Rocker Switch

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

#### Connection

### **Connection** — Block parameter value to connect parameter value connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink Toolstrip, or the **Connection** table in the Block
Parameters dialog box. To open the Block Parameters dialog box from the Property
Inspector, to the right of **Connected to**, click
**Connect** or **Change**. You can connect to a
parameter with a scalar value, or to an element of a matrix. For information about
connect mode and how to connect using the toolstrip, see Connect Dashboard Blocks to Simulink Model.

To connect a control block to a parameter with a scalar value or change the connection
of a control block to a parameter with a scalar value using the
**Connection** table:

1. Select the block.
2. To connect the block, in the Property Inspector, on the
   **Parameters** tab, click **Connect**.
   To change the connection of the block, click **Change**
   instead.
3. Select the block to whose parameter value you want to connect.
4. In the table, select the parameter to which you want to connect.
5. Click **Apply**.

The control block cannot connect to a parameter defined by a variable until you update
the model diagram. To connect to a parameter defined by a variable or to modify the
value of a variable that defines the value of a connected parameter when the simulation
is not running, update the model diagram by pressing **Ctrl+D**.

You can also connect dashboard blocks to a Stateflow chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

#### Programmatic Use

To programmatically connect a dashboard block to a tunable parameter, use a
`Simulink.HMI.ParamSourceInfo` object. The
`Simulink.HMI.ParamSourceInfo` object contains four properties.
Some properties apply to connecting dashboard blocks to parameters defined by
values, and some apply to connecting dashboard blocks to parameters defined by
variables. Not all fields have a value for a connection because a given dashboard
block connects to either to a parameter defined by a value or to a parameter defined
by a variable.

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

#### Main

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

### **States** — Pairings of value with label scalar and character vector

Each state pairs a **State Value** with a **State
Label**. When the block is in a given state, it assigns the **State
Value** for that state to the connected variable or parameter. You can use
the **State Label** to display the value assigned to the connected
variable or parameter on the block or to provide a descriptive text label.

By default, the switch has two states, one corresponding to each switch position:

- In the `Off` state, the block assigns the connected
  variable or parameter a value of `0`.
- In the `On` state, the block assigns the connected
  variable or parameter a value of `1`.

You can use a customizable switch block to design a switch with any number of states
greater than or equal to 1. To add a new state, click the **+**
button. To delete the current state, click the **-** button.

**Tip**

You can configure a variety of other parameters for a state besides the value and
label in design mode. For example, you can select an image that will appear on the
switch when it is in the state. To configure parameters in design mode:

1. Select the switch block.
2. Enter design mode. In the Property Inspector, on the
   **Design** tab, click the **Edit**
   button.
3. On the **Design** tab, open the
   **States** component, expand the **Select
   State** section, and select the state that you want to
   configure from the drop-down menu.
4. Configure the parameter values for the selected state, either using the
   toolbar above the block, or in the **States** component on
   the **Design** tab in the Property Inspector.

#### Programmatic Use

To configure the **States** for the block programmatically,
specify the value of the `States` parameter as a structure array
containing two elements with fields:

- `Value` — Scalar double value for the state.
- `Label` — String or character array to use as the
  label for the switch position.

```
leftState.Value = 0;
leftState.Label = 'Off';
rightState.Value = 1;
rightState.Label = 'On';
switchStates = [leftState rightState];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** two element array of structures |

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Switch

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

### **Select State** — Management and configuration of states scalar and character vector

Each state pairs a **State Value** with a **State
Label**. When the block is in a given state, it assigns the **State
Value** for that state to the connected variable or parameter. You can use
the **State Label** to display the value assigned to the connected
variable or parameter on the block or to provide a descriptive text label.

By default, the switch has two states, one corresponding to each switch position:

- In the `Off` state, the block assigns the connected
  variable or parameter a value of `0`.
- In the `On` state, the block assigns the connected
  variable or parameter a value of `1`.

You can use a customizable switch block to design a switch with any number of states
greater than or equal to 1. To add a new state, click the **+**
button. To delete the current state, click the **X** button.

To configure a state, in the **States** component, expand the
**Select State** section and select the state.

You can configure the value, label text, and a variety of other parameters for the
selected state in the **States** component on the
**Design** tab in the Property Inspector. For example, you can
select an image that will appear on the switch when it is in the state.

All changes that you make to parameter values in the **States**
component are applied only to the selected state. To configure a different state, in the
**Select State** section, select the state in the drop-down menu.
Then, configure the parameter values of that state in the **States**
component.

**Tip**

Alternatively, you can:

- Configure the parameters for the selected state using the toolbar that
  appears above the switch block in design mode
- Configure the values and label text of the states for the block using the
  **Parameters** tab in the Property Inspector

#### Programmatic Use

To configure the **States** for the block programmatically,
specify the value of the `States` parameter as a structure array
containing two elements with fields:

- `Value` — Scalar double value for the state.
- `Label` — String or character array to use as the
  label for the switch position.

```
leftState.Value = 0;
leftState.Label = 'Off';
rightState.Value = 1;
rightState.Label = 'On';
switchStates = [leftState rightState];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** two element array of structures |

### **Value** — State value scalar

Each state pairs a **State Value** with a **State
Label**. Specify the **State Value** of the state selected
in the **Design** tab.

### **Text** — State label text string | character array

Each state pairs a **State Value** with a **State
Label**. Specify the text for the **State Label** of the
state selected in the **Design** tab.

### **Color** — Label font color `[r g b]` vector

Choose a font color for the label text from the palette of standard colors, or specify
a custom color. The color is applied to the label text for the state that is selected in
the **Select State** section of the **States**
component on the **Design** tab.

### **Label X Offset** — Horizontal offset of text center from left edge of block `scalar`

Specify the horizontal offset of the center of the **State Label**
from the left edge of the block as a ratio of the block width. Relative to the position
of the text when the offset is `0`, an offset with a negative value
moves the text left, and an offset with a positive value moves the text right.

### **Label Y Offset** — Vertical offset of text center from top edge of block `scalar`

Specify the vertical offset of the center of the **State Label** from
the top edge of the block as a ratio of the block height. Relative to the position of
the text when the offset is `0`, an offset with a negative value moves
the text up, and an offset with a positive value moves the text down.

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

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Enable this option to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Click Area X Offset** — Horizontal offset of left edge of click area from left edge of block scalar

Specify the horizontal offset of the left edge of the click area from the left edge of
the block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Click Area Y Offset** — Vertical offset of top edge of click area from top edge of block scalar

Specify the vertical offset of the top edge of the click area from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Click Area Width** — Click area width scalar

Specify the click area width as a ratio of the block width.

**Example:** `0.5`

### **Click Area Height** — Click area height scalar

Specify the click area height as a ratio of the block height.

**Example:** `0.5`

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
| **Data Types** | `double` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2021b**

### R2025a: Select dashboard block and open Block Parameters dialog box during simulation

When a Simulink block from the Dashboard or Customizable Blocks library is
*active*, you can interact with the gadget the block represents. For
example, you can push a button or flip a switch. When a block is inactive, you can only
interact with the block. For example, you can move or resize the block. By default, all
blocks from the Dashboard and Customizable Blocks libraries are active during simulation.
Blocks promoted to a dashboard panel are also active when the panel is open in its own
window or docked and unlocked. Callback Button blocks for which at least one
of the callbacks triggered by pushing the button has a nonempty value are always active. To
interact with the gadget represented by an inactive block, you can temporarily activate a
block by clicking the block. When you deselect the block, the block becomes inactive
again.

Clicking an active Callback Button block or an active block from the
Dashboard or Customizable Blocks library that is connected to a parameter or variable value
both selects the block and interacts with the gadget the block represents. For example,
clicking an unselected active connected Push Button block both selects the
block and pushes the button. Starting in R2025a, you can select the block without
interacting with the gadget by pressing **Shift** and then clicking the block.
Similarly, you can open the Block Parameters dialog box by pressing **Shift**
and then double-clicking the block.

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

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.

## Description

Change parameter or variable value using switch with customizable appearance

Use the Rocker Switch block to change the value of the connected variable
or parameter before or during simulation. When you use the Rocker Switch block
in the Customizable Blocks library, you can customize the appearance of the block to look like
a real switch in your system. You can configure the switch with any number of states to
customize the behavior. For example, you could design a three-way toggle switch or a gearbox.
Use the Rocker Switch block with other dashboard blocks to create an
interactive dashboard for your model.

A real rocker switch has multiple settings. The Rocker Switch block treats
these settings as different states. A state pairs a state value with an image, a click area,
and a state label that is displayed on the click area.

To activate a state during simulation, click the click area of the state. To activate a
state when the simulation is not running, click the Rocker Switch block to
select the block, and then click the click area of the state. When you activate the state, the
state value is assigned to the Simulink® block diagram element to which the Rocker Switch block
connects.

**Note**

- Double-clicking a connected Rocker Switch block during simulation or
  after clicking the block does not open the Block Parameters dialog box. To open the
  Block Parameters dialog box, press **Shift**, then double-click the
  block.
- Clicking a connected Rocker Switch block during simulation both
  selects the block and moves the switch. To select the block without moving the switch,
  press **Shift**, then click the block.

### Customize Rocker Switch Blocks

When you add a Rocker Switch block to your model, the block is
preconfigured with a default design. You can use the block with the default design or
customize the appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the rocker switch.
To access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Rocker Switch block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Rocker Switch block, you configure the block
appearance for each state. To select a state to customize, use the drop-down list in the
toolbar. Alternatively, on the **Design** tab, select the
**States** component, and then select from the **Select
State** list. To add a state, in the toolbar, click the Add State button
. To delete a state, click the Remove State button
.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state value. | No | Yes |
| Specify the state label text and color. | No | Yes |
| Add or remove states. | Yes | Yes |
| Upload a state image that defines the appearance of the block in the state. | Yes | Yes |
| Change the size of the state image and click area. | No | Yes |
| Change the position the state label, state image, and click area. | No | Yes |

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

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard
block, use connect mode. To enter connect mode on an unconnected block, pause on the block
you want to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a control block to a parameter in your model or to change the connection of a
control block, enter connect mode. Select the block to whose parameter you want to connect.
From the list that appears, select the parameter to which you want to connect. Then, pause
on the dashboard block and click the Done Connecting button .

The control block cannot connect to a parameter defined by a variable until you update the
model diagram. To connect to a parameter defined by a variable or to modify the value of a
variable that defines the value of a connected parameter when the simulation is not running,
update the model diagram by pressing **Ctrl+D**.

You can connect to a parameter with a scalar value or to an element of a matrix or structure.
For more information, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

This animation shows how to connect the Rocker Switch block to your
model.

An unconnected Rocker Switch block connects to a Constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB® workspace by exporting the parameter data from the Simulation Data Inspector
by using the UI or the `Simulink.sdi.exportRun` function. For more information about exporting
data using the Simulation Data Inspector UI, see Export Data to Workspace or File. The
parameter data is stored in a `Simulink.SimulationData.Parameter` object, accessible as an element in the
exported `Simulink.SimulationData.Dataset`.
