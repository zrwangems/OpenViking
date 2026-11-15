---
type: simulink-block
title: 'Push Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'pushbutton'
documentation_source_path: 'slref/pushbutton.html'
language: en
---

# Push Button

## Ports

Not documented in R2025b.

## Parameters

### Connection

### **Connection** — Block parameter value to connect parameter value connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink® Toolstrip, or the **Connection** table in the Block
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

### Main

### **Button Text** — Text label for button `Button` (default) | string | character vector

The text displayed on the Push Button block in your
model.

#### Tips

To design a button that displays different text depending on the
state of the block, use the Push Button block in the Customizable Blocks
library.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** string or character array |
| **Default:** `'Button'` |

### **On Value** — Value assigned to connected parameter when button is pressed or latched `1` (default) | scalar

The value assigned to the connected block parameter when the button is pressed or latched.

#### Tips

Use the **Block Type** parameter to configure how the block responds to a click:

- `Momentary` — The button applies the **On Value** only while you press it.
- `Latch` — The button latches the state change when you click it and applies the **On value** until you click it again.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OnValue` |
| **Type:** string or character array |
| **Default:** `'1'` |

### **Button Type** — Button response to click `Momentary` (default) | `Latch`

Specify how the button responds to a click.

- `Momentary` — The button applies
  the **On Value** only while you press
  it.
- `Latch` — The button latches the
  state change when you click it and applies the **On
  value** until you click it again.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ButtonType` |
| **Type:** string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

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

### Icon

### **Icon** — Icon to display on button SVG file | PNG file | JPEG file

You can add an icon to the Push Button block to display
alongside or instead of the button text. You can choose from built-in
shape, automotive, and wireless icons, or you can upload your own custom
SVG, PNG, or JPEG file to use as the icon.

To view icon options, on the **Icon** tab of the
block dialog box, select an **Icon Type**. To use your
own custom icon, select `Custom` as the
**Icon Type** and upload the image file.

When you add an icon, you can configure the icon appearance using
these parameters:

- **Icon Alignment** — Alignment of icon
  relative to button text
- **On Color** — Icon color when block is
  pressed or latched and applying the **On
  value** to the connected parameter
- **Off Color** — Icon color when the block
  is not pressed or latched and is not applying the
  **On value** to the connected
  parameter

To specify an **On Color** and **Off
Color** for the icon, you must select **Customize
Icon Color**.

**Shape Icons**

| Icon | Basic Shapes Library Block Name | Programmatic Use Value |
| --- | --- | --- |
| Check1 icon: a check mark | Check1 | `Check1` |
| Check2 icon: a check mark with slightly curved lines | Check2 | `Check2` |
| Check3 icon: the outline of a check mark | Check3 | `Check3` |
| Check4 icon: a check mark with a divot along its outline | Check4 | `Check4` |
| Circle icon: a solid black circle | Circle | `Circle` |
| Ex1 icon: a cross mark | Ex1 | `Ex1` |
| Ex2 icon: a cross mark with one curved line | Ex2 | `Ex2` |
| Ex3 icon: the outline of a cross mark | Ex3 | `Ex3` |
| Ex4 icon: a cross mark with a divot along the outline | Ex4 | `Ex4` |
| Face icon: the outline of a face with a closed mouth in a straight line | Face | `Face` |
| Frown1 icon: the outline of a face with an open downturned mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed downturned mouth | Frown2 | `Frown2` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open downturned mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed downturned mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |

**Automotive Icons**

| Icon | Automotive Indicator Lamps Library Block Name | Programmatic Use Value |
| --- | --- | --- |
| Adaptive Cruise Control icon: a speedometer with an arrow pointing to a tick mark and the silhouette of a car in the background | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure icon: a speedometer with an exclamation mark next to it and the silhouette of a car in the background | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| Anti-Lock Brake System icon: a circle labeled "ABS" in a set of parentheses | Antilock Brake System | `AntilockBrakeSystem` |
| Battery icon: the outline of a battery with a plus symbol on the positive pole, and a negative symbol on the negative pole | Battery | `Battery` |
| Check Engine icon: the outline of an engine labeled "Check Engine" | Check Engine | `CheckEngine` |
| Check Engine2 icon: the outline of an engine with the silhouette of a lightning rod on it and the word "CHECK" underneath it | Check Engine2 | `CheckEngine2` |
| Cruise Control icon: a speedometer with an arrow pointing to one of the tick marks | Cruise Control | `CruiseControl` |
| Eco Mode icon: a solid leaf shape labeled "ECO" | Eco Mode | `EcoMode` |
| Electronic Stability icon: a circle labeled "ESP" in a set of parentheses | Electronic Stability | `ElectronicStability` |
| Engine icon: the silhouette of an engine | Engine | `Engine` |
| Engine Coolant Temp icon: a thermometer with waves in the background | Engine Coolant Temp | `EngineCoolantTemp` |
| Engine Failure icon: the silhouette of an engine with an exclamation mark on it | Engine Failure | `EngineFailure` |
| Engine Heating icon: the silhouette of an engine with three wavy arrows pointing upwards on it | Engine Heating | `EngineHeating` |
| Engine Oil icon: the silhouette of an oil can | Engine Oil | `EngineOil` |
| Exterior Bulb Failure icon: the silhouette of a glowing light bulb with an exclamation mark on it | Exterior Bulb Failure | `ExteriorBulbFailure` |
| Front Fog Light icon: the outline of a fog light lamp emitting rays of light to the left that are depicted as diagonal lines on top of a wavy vertical line that represents the fog | Front Fog Light | `FrontFogLight` |
| Fuel icon: the silhouette of a gas pump with an arrow pointing left on it | Fuel | `Fuel` |
| Hazards icon: the outline of a warning triangle | Hazards | `Hazards` |
| Headlamp Leveling icon: the outline of a lamp emitting rays of light with an arrow pointing clockwise above them and an arrow pointing counterclockwise below them | Headlamp Leveling | `HeadlampLeveling` |
| High Beams icon: the outline of a lamp emitting horizontal rays of light | High Beams | `HighBeams` |
| Hill Descent Control icon: the outline of a car driving down a slope | Hill Descent Control | `HillDescentControl` |
| Lighting Switch icon: the silhouette of a glowing light bulb | Lighting Switch | `LightingSwitch` |
| High Beams icon: the outline of a lamp emitting rays of light that run diagonally downward | Low Beams | `LowBeams` |
| Parking Assistance icon: the letter "P" next to a solid triangle, and the "P" emits a detection signal represented as three curved lines aimed at the triangle | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light icon: the outline of a fog light lamp emitting rays of light to the right that are depicted as horizontal lines on top of a wavy vertical line that represents the fog | Rear Fog Light | `RearFogLight` |
| Side Lights icon: the outline two lamps emitting rays of light to the left and right | Side Lights | `SideLights` |
| Stability Control icon: the silhouette of a car with wavy lines behind it | Stability Control | `StabilityControl` |
| Stability Control Off icon: the silhouette of a car with wavy lines behind it and the word "OFF" underneath | Stability Control Off | `StabilityControlOff` |
| Tire Monitor icon: the outline of the cross-section of a tire with an exclamation mark on it | Tire Monitor | `TireMonitor` |
| Traction Control icon: the outline of the cross-section of a tire with the label "TC" | Traction Control | `TractionControl` |
| Traction Control Off icon: the outline of the cross-section of a tire with the label "TC" and a diagonal slash through the whole image | Traction Control Off | `TractionControlOff` |
| Traction Control Failure icon: the outline of the cross-section of a tire with the label "TC" and an exclamation mark next to it | Traction Control Failure | `TractionControlFailure` |
| Turn Signal Left icon: a solid arrow pointing left | Turn Signal Left | `TurnSignalLeft` |
| Turn Signal Right icon: a solid arrow pointing right | Turn Signal Right | `TurnSignalRight` |

**Wireless Icons**

| Icon | Icon Name | Programmatic Use Value |
| --- | --- | --- |
| Network icon: the wireless internet connection icon | Network | `Network` |
| Network No Signal icon: the wireless internet connection icon grayed out,with a crossed-out circle next to it | Network No Signal | `NetworkNoSignal` |
| Network Transmission icon: a wireless internet tower | Network Transmission | `NetworkTransmission` |
| Network3G icon: the wireless internet connection icon with "3G" next to it | Network3G | `Network3G` |
| Network4G icon: the wireless internet connection icon with "4G" next to it | Network4G | `Network4G` |
| Network5G icon: the wireless internet connection icon with "4G" next to it | Network5G | `Network5G` |

#### Tips

- You can change the icon for a Push Button
  block using the **Button** tab in the
  toolstrip.
- If you want to customize the appearance of the Push
  Button block further, consider designing your
  own button using the Push Button block in the Customizable Blocks
  library.

  The Push Button block in the Customizable
  Blocks library supports adding a custom icon but does not
  include any built-in icons.
- The on and off colors for the icon can apply to these SVG elements:

  - `altGlyph`
  - `circle`
  - `ellipse`
  - `path`
  - `polygon`
  - `rect`
  - `text`
  - `textPath`
  - `tref`
  - `tspan`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Icon` |
| **Type:** string | character vector |
| **Default:** `'Default'` |

### **Icon Alignment** — Icon alignment relative to button text `Left` (default) | `Right` | `Top` | `Bottom` | `Center`

Alignment of the icon relative to the button text. When you do not
specify button text, the icon is always in the center of the
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconAlignment` |
| **Type:** string | character vector |
| **Value:** `'Left'` | `'Right'` | `'Top'` | `'Bottom'` | `'Center'` |
| **Default:** `'Left'` |

### **Customize Icon Color** — Whether to use icon on and off colors `Off` (default) | `On`

When you add an icon to the Push Button block, you can
specify on and off colors so the icon color changes to reflect the state
of the block. To use and specify the **On Color** and
**Off Color** for an icon, select
**Customize Icon Color**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconColor` |
| **Type:** string | character vector |
| **Value:** `'On'` | `'Off'` |
| **Default:** `'Off'` |

### **On Color** — Icon color when block is pressed or latched `[r g b]` vector

When you add an icon to the Push Button block, you can
specify on and off colors so the icon color changes to reflect the state
of the block. The **On Color** specifies the color of
the icon when the block is pressed or latched and is applying the
**On value** to the connected parameter. You can
select a color from a palette of standard colors or specify a custom
color.

#### Dependencies

To enable the **On Color** parameter, select
**Customize Icon Color**.

#### Programmatic Use

Specify the `IconOnColor` parameter for the block
as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `IconOnColor` |
| **Type:** `[r g b]` vector |

### **Off Color** — Icon color when block is not pressed or latched `[r g b]` vector

When you add an icon to the Push Button block, you can
specify on and off colors so the icon color changes to reflect the state
of the block. The **Off Color** specifies the color of
the icon when the block is not pressed or latched and is not applying
the **On value** to the connected parameter. You can
select a color from a palette of standard colors or specify a custom
color.

#### Dependencies

To enable the **On Color** parameter, select
**Customize Icon Color**.

#### Programmatic Use

Specify the `IconOffColor` parameter for the
block as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `IconOffColor` |
| **Type:** `[r g b]` vector |

## Libraries

Simulink / Dashboard

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

**Introduced in R2015a**

### R2023b: Open panel in new window

Starting in R2023b, you can open a dashboard panel in a new window. To do so,
select the panel and pause on the ellipsis that appears. In the action menu that
expands, click the **Open In New Window** button
.

You can minimize and restore the new window containing the panel separately from
the model window. From the panel window, you can run, pause, stop, and step through
the simulation. In the panel window, you can edit the panel and the blocks it
contains.

To return the panel to the model canvas, in the panel window toolstrip, click
**Open in canvas**
.

For more information about opening a panel in a new window, see Open Panels in New Window.

### R2023a: Persistent panels tab in Simulink Toolstrip

When you add a dashboard panel to a model, the **Panels** tab
appears in the Simulink Toolstrip and shows options for managing and editing panels.

Previously, the **Panels** tab was only visible when a panel was
selected. Starting in R2023a, the **Panels** tab stays visible when
no panel is selected.

The **Panels** tab also contains these new options:

- You can add an empty panel.
- You can rename the selected panel.
- You can hide the selected panel.

### R2022b: Undo and redo support for customizable dashboard blocks in panel

Starting in R2022b, you can undo and redo the changes you make to customizable
dashboard blocks that are in a panel.

To undo or redo a change:

1. Click the panel or a block in the panel.
2. Press **Ctrl+Z** to undo the change, or press
   **Ctrl+Y** to redo the change.

**Note**

The keyboard shortcuts are based on Windows®. On a Mac, press **command** (⌘) instead of
**Ctrl**.

### R2022b: Toolstrip support for panels

Starting in R2022b, you can use the Simulink Toolstrip to manage and edit panels and the dashboard blocks that they
contain.

When you click a dashboard block in a panel, the toolstrip tab for the block
appears. For example, when you click a Circular Gauge block, the
**Gauge** tab appears in the toolstrip.

When you click a panel, the **Panel** tab appears in the
toolstrip. The tab provides these options:

- Manage the visibility of panels in the model.
- Fit all unhidden panels within the current view.
- Collapse the selected panel.
- Customize the size and the contents of the panel.
- Set a custom background image for the selected panel.
- Add a new tab to the selected panel.

### R2021b: Push Button Block Can Apply Value After You Release Click

Starting in R2021b, you can configure the behavior of the Push
Button block to latch or momentarily apply the **On
Value** when you click the block.

### R2021b: Push Button Block Can Display Icons

Starting in R2021b, you can add an icon to display on the Push
Button block alongside or instead of the button text. Choose an icon for
the block from a predefined set or upload your own custom icon using the block
dialog box or the **Button** tab of the
toolstrip.

You can also specify an on color and an off color so the icon color changes with
the state of the block and specify the alignment of the icon relative to the button
text.

### R2021a: Tune matrix and structure elements using dashboard blocks

Starting in R2021a, you can connect a block from the Dashboard library to a scalar
element of a matrix or structure that defines the value of a tunable block
parameter. When you connect a dashboard block to a tunable parameter, you first
select one or more blocks. Then, in a dialog box, you select the parameter to which
you want to connect. When you select a parameter that has a nonscalar value, specify
the element you want to tune using the text box in the dialog box.

### R2020b: **Background Color**, **Foreground Color**, and **Opacity** properties added for several dashboard blocks

Starting in R2020b, you can specify a background color, a foreground color, and
opacity for these blocks from the Dashboard library:

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b: Simulink Toolstrip support for dashboard blocks

Starting in R2020b, the **Block** tab in the Simulink Toolstrip turns into a block-specific tab when you select a block in
your model that is from the Dashboard library in the Simulink library or from the Flight Instruments library in the Aerospace Blockset™ Flight Control Analysis library. From the toolstrip, you can connect,
disconnect, and modify connections for the selected block. You can jump to the model
element connected to the selected block, and you can add the selected block to a
panel.

### R2019a: Programmatically add and configure dashboard blocks

Starting in R2019a, you can use functions such as `add_block`
and `set_param` to create and configure blocks from the Dashboard
library in your model.

## Description

Change parameter or variable value using button

Use the Push Button block to change the value of the connected variable
or parameter before or during simulation. You can configure the button to change the
value only while you press the button or to latch the value change until you click the
button again. Use the Push Button block with other Dashboard blocks to
create an interactive dashboard to control your model.

Double-clicking the Push Button block does not open its dialog box
during simulation or when the block is selected. To edit the block parameters, you can
use the **Property Inspector** or open the block dialog box by:

- Double-clicking the block when the block is not selected and the model is
  not simulating.
- Right-clicking the block and selecting **Block
  Parameters** from the context menu.

### Push Button Icons

You can add an icon to the Push Button block that is displayed
alongside the button text. You can choose an icon from a predefined set that
includes basic shapes, automotive indicators, and wireless icons, or you can upload
your own custom icon. For more information, including a complete list of the
built-in icons, see Icon.

When you add an icon to the Push Button block, you can configure an
on color and an off color for the icon so its color changes with the state of the
block and specify the alignment of the icon relative to the button text. For
example, this Push Button block is configured to use a circle icon
with the on color specified as bright green, aligned to the left of the button
text.

Push button block with a green circle icon to the left of the button text.

The icon settings for the Push Button block allow you to configure
the appearance of the block in your model. When you want to customize the appearance
of the block further, consider using the Push
Button block in the Customizable Blocks library. The Push
Button block in the Customizable Blocks library supports adding a custom
icon but does not include any built-in icons.

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

This animation shows how to connect the Push Button block to your
model.

An unconnected Push Button block connects to the Value parameter of a constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB® workspace by exporting the parameter data from the Simulation Data Inspector
by using the UI or the `Simulink.sdi.exportRun` function. For more information about exporting
data using the Simulation Data Inspector UI, see Export Data to Workspace or File. The
parameter data is stored in a `Simulink.SimulationData.Parameter` object, accessible as an element in the
exported `Simulink.SimulationData.Dataset`.
