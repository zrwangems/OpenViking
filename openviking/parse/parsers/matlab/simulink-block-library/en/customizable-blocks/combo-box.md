---
type: simulink-block
title: 'Combo Box'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customcombobox'
language: en
---

# Combo Box

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

### **Enumerated Data Type** — Option to specify state values and labels using enumerated data type `off` (default) | `on`

To configure the state labels and values for the block, you can use an enumerated
data type that pairs each enumeration with a numeric value. First, select
**Enumerated Data Type**. Then, specify the name of the enumerated
data type in the text box. The definition for the specified enumerated data type must
be saved on the MATLAB path or in the base workspace.

**Note**

You can define an enumerated data type using the `Simulink.defineIntEnumType`
function. For example, to define the enumerated data type
`myEnumType` for a set of Roman numerals from one to five, use
this command.

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

Then, in the Property Inspector, on the **Parameters** tab, in
the **Enumerated Data Type** text box, enter
`myEnumType`.

### **States** — Management and configuration of states scalar and character vector

Each option in the combo box drop-down list corresponds to a state of the
Combo Box block. The state has a label and a value. The
**State Label** value is the text in the drop-down list that
identifies the option. When you select an option, the Combo Box block
enters the associated state and assigns the **State Value** value to
the connected parameter.

By default, the block has three combo box options and three corresponding
states.

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

You can design a Combo Box block with any number of states greater
than or equal to 1. To add a new state, click the **+** button. To
delete a state, click the label text in the **State Label** column or
the value in the **State Value** column, and then click the
**-** button.

**Note**

When **Enumerated Data Type** is turned on, you cannot add or
delete states. You can turn off this option in the **Parameters**
tab of the Property Inspector.

To configure the label text or value of a state, click the label text in the
**State Label** column or the value in the **State
Value** column, delete the current value, enter a new value, and press
**Enter**.

**Tip**

You can also configure the parameters for a state in design mode:

1. Select the Combo Box block.
2. Enter design mode. In the Property Inspector, on the
   **Design** tab, click **Edit**.
3. On the **Design** tab, open the
   **States** component, expand the **Select
   State** section, and from the drop-down menu, select the state that
   you want to configure.
4. Configure the label text and value of the selected state in the
   **Text** and **Value** text boxes.

### Design

To customize the dashboard block, open the Property
Inspector, click the **Design** tab, and click **Edit**.
Changes you make to the values of the parameters in this section are applied to all combo
box options.

#### Combo Box

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

### **Dropdown Background Color** — Background color of drop-down list `[r g b]` vector

Choose a background color for the drop-down list from the palette of standard
colors, or specify a custom color.

### **Dropdown Border Color** — Color of border around drop-down list `[r g b]` vector

Choose a color for the border around the drop-down list from the palette of
standard colors, or specify a custom color.

### **Visible Entries** — Maximum number of options visible in drop-down list scalar

By default, when you expand the drop-down list a maximum of five combo box options
are visible. You can access any options that are not visible by scrolling. Specify the
maximum number of options that are visible when you expand the drop-down list.

### **Highlight Background Color** — Background color of highlighted option in drop-down list `[r g b]` vector

Choose a background color for the highlighted option in the drop-down list from
the palette of standard colors, or specify a custom color.

### **Highlight Border Color** — Color of border around highlighted option in drop-down list `[r g b]` vector

Choose a color for the border around the highlighted option in the drop-down list
from the palette of standard colors, or specify a custom color.

### **Highlight Font Color** — Font color of highlighted option in drop-down list `[r g b]` vector

Choose a font color for the highlighted option in the drop-down list from the
palette of standard colors, or specify a custom color.

### **Width** — Chevron width scalar

Specify the width of the chevron as a ratio of the font height of the label
text.

**Example:** `0.5`

### **Height** — Chevron height scalar

Specify the height of the chevron as a ratio of the font height of the label
text.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain chevron aspect ratio `on` (default) | `off`

Turn on this option to maintain the aspect ratio when resizing the chevron using
the Property Inspector.

#### States

### **Select State** — State label and value scalar and character vector

Each option in the combo box drop-down list corresponds to a state of the
Combo Box block. The state has a label and a value. The
**State Label** value is the text in the drop-down list that
identifies the option. When you select an option, the Combo Box block
enters the associated state and assigns the **State Value** value to
the connected parameter.

By default, the block has three combo box options and three corresponding
states.

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

You can design a Combo Box block with any number of states greater
than or equal to 1. To add a new state, click the **+** button. To
delete a state, in the **Select State** section, select the state.
Then, click the **X** button.

**Note**

When **Enumerated Data Type** is enabled, you cannot add or
delete states. You can disable this option in the **Parameters**
tab of the Property Inspector.

To configure the label text or value of a state, in the **Select
State** section, select the state. Then, enter new values in the
**Value** and **Text** boxes.

**Tip**

You can also configure the states for the block using the
**Parameters** tab in the Property Inspector.

### **Value** — State value scalar

Specify the **State Value** of the state selected in the
**Select State** section.

**Note**

When **Enumerated Data Type** is turned on, you cannot change
the value. You can turn off this option in the **Parameters** tab
of the Property Inspector.

### **Text** — State label text string | character array

Specify the **State Label** text of the state selected in the
**Select State** section.

**Note**

When **Enumerated Data Type** is turned on, you cannot change
the text. You can turn off this option in the **Parameters** tab of
the Property Inspector.

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

**Introduced in R2025a**

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

## Description

Change parameter or variable value during simulation using combo box with customizable appearance

Use the Combo Box block to change the value of the connected parameter or
variable before or during simulation. When you use the Combo Box block in the
Customizable Blocks library, you can customize the appearance of the block, for example, to
make the block look like a combo box in a digital user interface you are designing. Use the
Combo Box block with other dashboard blocks to build an interactive dashboard
of controls and indicators for your model.

Each option in the combo box drop-down list corresponds to a state of the Combo
Box block. The state has a label and a value. The state label is the text in the
drop-down list that identifies the option. When you select an option, the Combo
Box block enters the associated state and assigns the state value to the connected
parameter. To select an option during simulation, click the Combo Box block to
expand the drop-down list, and then select the option. To select an option when the simulation
is not running, click the Combo Box block to select the block, click the block
again to expand the drop-down list, and then select the option.

To customize the state label or value, open the **Parameters** tab of the
Property Inspector or the Block Parameters dialog box.

**Note**

- Double-clicking a connected Combo Box block during simulation or
  after clicking the block does not open the Block Parameters dialog box. To open the
  Block Parameters dialog box, press **Shift**, then double-click the
  block.
- Clicking a connected Combo Box block during simulation both selects
  the block and expands the combo box drop-down list. To select the block without
  expanding the list, press **Shift**, then click the block.

### Customize Combo Box Blocks

When you add a Combo Box block to your model, the block is preconfigured
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

In design mode, you can use the toolbar above the block to customize the combo box. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Combo Box block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the value each option assigns to the connected parameter. | No | Yes |
| Change the text of the option labels. | No | Yes |
| Add or remove options. | Yes | Yes |
| Change the chevron icon of the drop-down list. | No | Yes |
| Change the number of visible entries in the drop-down list. | No | Yes |
| Change the background and border color of the drop-down list. | No | Yes |
| Change the background, border, and font color of the highlighted entry in the drop-down list. | No | Yes |
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

This animation shows how to connect the Combo Box block to your
model.

An unconnected Combo Box block connects to a Constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB® workspace by exporting the parameter data from the Simulation Data Inspector
by using the UI or the `Simulink.sdi.exportRun` function. For more information about exporting
data using the Simulation Data Inspector UI, see Export Data to Workspace or File. The
parameter data is stored in a `Simulink.SimulationData.Parameter` object, accessible as an element in the
exported `Simulink.SimulationData.Dataset`.
