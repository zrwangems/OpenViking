---
type: simulink-block
title: 'Lamp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customlamp'
documentation_source_path: 'slref/customlamp.html'
language: en
---

# Lamp

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
- name: Specify State Values as Ranges
  summary: Option to specify ranges of values that activate states off (default) | on
  group: Parameters
  block_parameter: StateValueType
  type: character vector | string
  values: '"Discrete" | "Range"'
  default: '"Discrete"'
- name: States
  summary: Pairings of lamp color with signal value scalar and [r g b] vector
  group: Parameters
  block_parameter: ColorDefault
  type: '[r g b] vector'
  default: '[0.7529 0.7529 0.7529]'
- name: Lock Aspect Ratio
  summary: Option to maintain block aspect ratio on (default) | off
  group: Design
- name: Select State
  summary: Selection of state to configure scalar and [r g b] vector
  group: Design
  block_parameter: ColorDefault
  type: '[r g b] vector'
  default: '[0.7529 0.7529 0.7529]'
- name: Apply Default Settings to All States
  summary: Option to apply settings of default state to all other states off (default) | on
  group: Design
- name: Specify State Values as Ranges
  summary: Option to specify ranges of values that activate states off (default) | on
  group: Design
  block_parameter: StateValueType
  type: character vector | string
  values: '"Discrete" | "Range"'
  default: '"Discrete"'
- name: Value
  summary: State value scalar
  group: Design
- name: Color
  summary: State color [r g b] vector
  group: Design
- name: Opacity
  summary: State color opacity 1 (default) | scalar
  group: Design
- name: Style
  summary: Shape and icon combination style Intersect (default) | Simple | Subtract
  group: Design
- name: Shape
  summary: State shape image
  group: Design
- name: Icon
  summary: Lamp block appearance SVG image
  group: Design
  block_parameter: Icon
  type: string | character vector
  default: '''Default'''
- name: X Offset
  summary: Horizontal offset of left edge of shape icon combination bounding box from left edge of block scalar
  group: Design
- name: Y Offset
  summary: Vertical offset of top edge of shape icon combination bounding box from top edge of block scalar
  group: Design
- name: Width
  summary: Width of shape icon combination scalar
  group: Design
- name: Height
  summary: Height of shape icon combination scalar
  group: Design
- name: Icon Size
  summary: Icon image zoom level scalar
  group: Design
- name: Use Background Color
  summary: Option to specify solid block background color off (default) | on
  group: Design
- name: Color
  summary: Block background color [r g b] vector
  group: Design
  block_parameter: BackgroundColor
  type: string | character vector
  values: '[r g b] vector'
- name: Opacity
  summary: Block background opacity 1 (default) | scalar
  group: Design
- name: Corner Radius
  summary: Corner radius of area with block background color scalar
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

#### States

### **Specify State Values as Ranges** — Option to specify ranges of values that activate states `off` (default) | `on`

You can specify ranges of signal values that activate the Lamp
block states. Select **Specify State Values as Ranges** and specify
the minimum and maximum of the value range that activates each state.

#### Programmatic Use

To programmatically specify whether the states are each activated by a signal
value or by a range of signal values, specify the `StateValueType`
parameter as a string or a character vector. To activate each state with a signal
value, set `StateValueType` to `"Discrete"`. To
activate each state with a range of signal values, set
`StateValueType` to `"Range"`.

|  |
| --- |
| **Block Parameter:** `StateValueType` |
| **Type:** character vector | string |
| **Values:** `"Discrete"` | `"Range"` |
| **Default:** `"Discrete"` |

### **States** — Pairings of lamp color with signal value scalar and `[r g b]` vector

States pair a lamp color with a value of the connected signal. Each state consists
of a **Value** and a **Color**.

- **Value** — Connected signal value or range of signal
  values that cause the Lamp block to display the specified color.
  To specify a range of values, select **Specify State Values as
  Ranges** and specify the minimum and maximum of the range of values
  that activates each state.
- **Color** — Lamp color when the connected signal value
  matches the corresponding **State** value. You can select from
  a palette of standard colors or specify a custom color with
  `RGB` values.

The `[undefined]` state specifies the color of the
Lamp block when the connected signal value does not match any of the
values specified in the **States** table. Click the
**+** button to add another state.

#### Programmatic Use

To programmatically specify the `Value` and
`Color` parameter values for a Lamp block, use an
array of structures that contain these fields:

- `Value` — Scalar `double` signal value
  or vector specifying the minimum and maximum of a range of
  `double` signal values that cause the Lamp
  block to display the specified color indication.

  **Note**

  Specifying a vector enables the **Specify State Values as
  Ranges** option.
- `Color` — `1`-by-`3`
  `[r g b]` vector with values between `0` and
  `1` that specifies the color for the Lamp
  block to display.

```
lampState1.Value = [1 2];
lampState1.Color = [0 0 1];
lampState2.Value = [2 3];
lampState2.Color = [1 0 0];
lampStates = [lampState1 lampState2];
```

|  |
| --- |
| **Block Parameter:** `StateColors` |
| **Type:** structure array |
| **Default:** structure |

The `ColorDefault` parameter specifies the color for the
Lamp block when the value of the connected signal does not match
any of the specified state values. Specify the `ColorDefault`
parameter as a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ColorDefault` |
| **Type:** `[r g b]` vector |
| **Default:** `[0.7529 0.7529 0.7529]` |

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Lamp

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

### **Select State** — Selection of state to configure scalar and `[r g b]` vector

Select a state that you want to configure from the drop-down menu in the
**Select State** section of the **States**
component. You can use a customizable Lamp block to design a lamp with
any number of states greater than or equal to 1. Click **+** to add
another state. Click **X** to delete the current state.

States match a display color to the value of the connected signal. Each state
consists of a **State** and a **Color**.

- **State** — Connected signal value or range of signal
  values that cause the Lamp block to display the specified color.
  To specify a range of values, select **Specify State Values as
  Ranges** and specify the minimum and maximum of the range of values
  that activates each state.
- **Color** — Lamp color when the connected signal value
  matches the corresponding **State** value. You can select from
  a palette of standard colors or specify a custom color with
  `RGB` values.

The `[default]` state specifies the color of the
Lamp block when the connected signal value does not match any of the
values specified in the **States** table.

**Note**

You can configure more than the value and color of a state: you can configure
all of the parameters in the **States** component of the
**Design** tab for a state. For example, you can select an icon
that will appear on the lamp when it is in the state. When you configure any of the
parameters in the **States** component, the changes are applied to
the state that is selected in the **Select State** section of the
**States** component.

#### Tips

You can also configure the values and colors of the states for the block using
the **Parameters** tab in the Property Inspector.

#### Programmatic Use

To programmatically specify the `State` and
`Color` parameter values for a Lamp block, use an
array of structures that contain these fields:

- `Value` — Scalar `double` signal value
  or vector specifying the minimum and maximum of a range of
  `double` signal values that cause the Lamp
  block to display the specified color indication.

  **Note**

  Specifying a vector enables the **Specify State Values as
  Ranges** option.
- `Color` — `1`-by-`3`
  `[r g b]` vector with values between `0` and
  `1` that specifies the color for the Lamp
  block to display.

```
lampState1.Value = [1 2];
lampState1.Color = [0 0 1];
lampState2.Value = [2 3];
lampState2.Color = [1 0 0];
lampStates = [lampState1 lampState2];
```

|  |
| --- |
| **Block Parameter:** `StateColors` |
| **Type:** structure array |
| **Default:** structure |

The `ColorDefault` parameter specifies the color for the
Lamp block when the value of the connected signal does not match
any of the specified state values. Specify the `ColorDefault`
parameter as a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ColorDefault` |
| **Type:** `[r g b]` vector |
| **Default:** `[0.7529 0.7529 0.7529]` |

### **Apply Default Settings to All States** — Option to apply settings of default state to all other states `off` (default) | `on`

Apply the settings of the default state to all other states. This option applies
to all settings in the **States** component except for the settings
in the **Value and Color** section.

### **Specify State Values as Ranges** — Option to specify ranges of values that activate states `off` (default) | `on`

You can specify ranges of signal values that activate the states. Select **Specify
State Values as Ranges** and specify the minimum and maximum of the value
range that activates each state.

#### Programmatic Use

To programmatically specify whether the states are each activated by a signal value or by a range of signal values, specify the `StateValueType` parameter as a string or a character vector. To activate each state with a signal value, set `StateValueType` to `"Discrete"`. To activate each state with a range of signal values, set `StateValueType` to `"Range"`.

|  |
| --- |
| **Block Parameter:** `StateValueType` |
| **Type:** character vector | string |
| **Values:** `"Discrete"` | `"Range"` |
| **Default:** `"Discrete"` |

### **Value** — State value scalar

Each state pairs a **Value** with a **Color**.
Specify the **Value** that activates the state selected in the
**Design** tab.

**Note**

When the **Specify State Values as Ranges** option is enabled,
the **Value** parameter changes to the parameters
`Minimum` and `Maximum`, which allow you to
define a range by specifying its minimum and maximum values.

**Example:** `0`

### **Color** — State color `[r g b]` vector

Each state pairs a **Value** with a **Color**.
Choose the **Color** of the state selected in the
**Design** tab from the palette of standard colors, or specify a
custom color.

**Example:** `[1 0 0]`

### **Opacity** — State color opacity `1` (default) | scalar

Specify the opacity of the state **Color** as a scalar value from
0 to 1.

**Example:** `0.5`

### **Style** — Shape and icon combination style `Intersect` (default) | `Simple` | `Subtract`

A lamp can show up to three different colors:

- State **Color**
- Color of the selected icon in the Property Inspector
- Background color or the background image, depending on which is
  activated

The colors that show on the lamp depend on how the shape and icon layers of the
Lamp block are combined. Select how to combine the layers:

- In the `Intersect` style, the area where the shape
  and icon overlap has the state **Color**. The area where the
  shape and icon do not overlap has the background color or image.
- In the `Simple` style, the area of the shape that
  is not covered by the icon has the state **Color**. The icon on
  the lamp has the same colors as its counterpart in the Property Inspector. The
  remaining area has the background color or image.
- In the `Subtract` style, the area of the shape that
  is not covered by the icon has the state **Color**. The
  remaining area has the background color or image.

Three Lamp blocks, each configured for one of the three ways you can combine the shape and icon: simple, intersect, or subtract.

**Example:** `'Simple'`

### **Shape** — State shape image

Select a shape that, in combination with the icon, determines the area on the lamp
to which the state **Color** is applied. Choose a circle, a square,
or a triangle.

### **Icon** — Lamp block appearance SVG image

Use an icon to configure the appearance of the Lamp block in the
model. You can choose from built-in shape, automotive, and wireless icons, or you can
upload your own custom SVG file as an icon.

To view icon options, in the **Icon** section, select an
**Icon Type**. To use your own SVG file as the block icon, in the
**Icon** section, select `Custom` as the
**Icon Type**, and in the **Custom Icon** section,
click the plus button to upload the SVG file.

**Shape Icons**

| Icon | Icon Name | Programmatic Use Value |
| --- | --- | --- |
| Lamp icon: a solid gray circle | Lamp | `Default` |
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
| Frown1 icon: the outline of a face with an open frowning mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed frowning mouth | Frown2 | `Frown2` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| L-shaped membrane icon: the silhouette of the L-shaped membrane | L-shaped Membrane | `Membrane` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open frowning mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed frowning mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |

**Automotive Icons**

| Icon | Icon Name | Programmatic Use Value |
| --- | --- | --- |
| Adaptive Cruise Control icon: a speedometer with an arrow pointing to a tick mark, and the silhouette of a car in the background | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure icon: a speedometer with an exclamation mark next to it, and the silhouette of a car in the background | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| ABS icon: a circle labeled "ABS" in a set of parentheses | Antilock Brake System | `AntilockBrakeSystem` |
| Battery icon: the outline of a battery, with a + symbol on the positive pole, and a - symbol on the negative pole | Battery | `Battery` |
| Check Engine icon: the outline of an engine labeled "Check Engine" | Check Engine | `CheckEngine` |
| Check Engine2 icon: the outline of an engine with the silhouette of a lightning rod on it, and the word "CHECK" underneath it | Check Engine2 | `CheckEngine2` |
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
| Headlamp Leveling icon: the outline of a lamp emitting rays of light with an arrow pointing clockwise above them and an arrow pointing counterclockwise below them to indicate that the lamp can be turned to level the light rays | Headlamp Leveling | `HeadlampLeveling` |
| High Beams icon: the outline of a lamp emitting horizontal rays of light | High Beams | `HighBeams` |
| Hill Descent Control icon: the outline of a car driving down a slope | Hill Descent Control | `HillDescentControl` |
| Lighting Switch icon: the silhouette of a glowing light bulb | Lighting Switch | `LightingSwitch` |
| High Beams icon: the outline of a lamp emitting rays of light that run diagonally downward | Low Beams | `LowBeams` |
| Parking Assistance icon: the letter "P" next to a solid triangle that represents an obstacle, and the "P" emits a detection signal represented as three curved lines aimed at the triangle | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light icon: the outline of a fog light lamp emitting rays of light to the right that are depicted as horizontal lines on top of a wavy vertical line that represents the fog | Rear Fog Light | `RearFogLight` |
| Side Lights icon: the outline two lamps emitting rays of light to the left and right | Side Lights | `SideLights` |
| Stability Control icon: the silhouette of a car with wavy lines behind it to represent the car slipping | Stability Control | `StabilityControl` |
| Stability Control Off icon: the silhouette of a car with wavy lines behind it to represent the car slipping, and the word "OFF" underneath | Stability Control Off | `StabilityControlOff` |
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
| Network No Signal icon: the wireless internet connection icon grayed out, with a crossed-out circle next to it | Network No Signal | `NetworkNoSignal` |
| Network Transmission icon: a wireless internet tower | Network Transmission | `NetworkTransmission` |
| Network3G icon: the wireless internet connection icon with "3G" next to it | Network3G | `Network3G` |
| Network4G icon: the wireless internet connection icon with "4G" next to it | Network4G | `Network4G` |
| Network5G icon: the wireless internet connection icon with "4G" next to it | Network5G | `Network5G` |

**Tip**

The Dashboard library has libraries with a preconfigured Lamp
block for each icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Icon` |
| **Type:** string | character vector |
| **Default:** `'Default'` |

### **X Offset** — Horizontal offset of left edge of shape icon combination bounding box from left edge of block scalar

Specify the horizontal offset of the left edge of the bounding box of the shape
and icon combination from the left edge of the block as a ratio of the block width.
Relative to the position of the shape and icon combination when the offset is
`0`, an offset with a negative value moves the combination left and
an offset with a positive value moves the combination right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of shape icon combination bounding box from top edge of block scalar

Specify the vertical offset of the top edge of the bounding box of the shape and
icon combination from the top edge of the block as a ratio of the block height.
Relative to the position of the shape and icon combination when the offset is
`0`, an offset with a negative value moves the combination up and
an offset with a positive value moves the combination down.

**Example:** `1`

### **Width** — Width of shape icon combination scalar

Specify the width of the bounding box of the shape and icon combination as a ratio
of the block width.

**Example:** `0.5`

### **Height** — Height of shape icon combination scalar

Specify the height of the bounding box of the shape and icon combination as a
ratio of the block height.

**Example:** `0.5`

### **Icon Size** — Icon image zoom level scalar

You can modify how the icon is shown on the lamp by zooming in or out on its
center. Specify the zoom level as a scalar value from `0` to
`2`. When the **Icon Size** is
`1`, the icon is zoomed to show the whole image as large as is
possible within the limits of the bounding box of the shape and icon combination. When
the **Icon Size** is larger than `1`, the image is
cut off at the limits of the bounding box.

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
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2021b**

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

### R2022a: View and edit each state in design mode

Starting in R2022a, you can view and edit each state for the customizable Lamp block in
design mode. You can modify more aspects of the block appearance for each state. For
example, you can now design a lamp that uses a different icon for each state.

### R2022a: Lamp block supports specifying state values as ranges

In previous releases, the Lamp block would only enter a state if the
connected signal had a single unique value that you specified for that state. Starting in
R2022a, you can specify a range of signal values that activate each state.

### R2022a: Change opacity of state colors

Starting in R2022a, for the customizable Lamp block, you can change the opacity of the
state color.

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.

## Description

Display color that reflects signal value on lamp with customizable appearance

The Lamp block displays a color that reflects the value of the connected
signal. When you use the Lamp block in the Customizable Blocks library, you can
modify the appearance of the block so it looks like a real indicator lamp in your system. Use
the Lamp block with other dashboard blocks to build an interactive dashboard of
controls and indicators for your model.

To configure the Lamp block, specify one or more states. A state pairs a
state value with a color for the Lamp block to display. When the value of the
connected signal is the same as the state value, the Lamp block displays the
color. You can also specify the state value as a range, such that the block displays the color
when the value of the connected signal falls into the specified range.

### Customize Lamp Blocks

When you add a Lamp block to your model, the block is preconfigured with
a default design. You can use the block with the default design or customize the appearance
of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the lamp. To access
additional customization options or to enter exact values for design settings, use the
**Design** tab in the Property Inspector.

Customizable Lamp block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Lamp block, you configure the block appearance for
each state. To select a state to customize, use the drop-down list in the toolbar.
Alternatively, on the **Design** tab, select the
**States** component, and then select from the **Select
State** list. To add a state, in the toolbar, click the Add State button
. To delete a state, click the Remove State button
.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state value as a number or a range. | No | Yes |
| Add or remove states. | Yes | Yes |
| Select a shape for the region whose color reflects the signal value. | Yes | Yes |
| Select the color of the shape. | Yes | Yes |
| Select from an icon set that includes wireless icons and automotive indicator lamps, or upload a custom icon. | Yes | Yes |
| Specify how to combine the shape and the icon. | Yes | Yes |
| Change the size of the shape and icon. | No | Yes |
| Change the position of the shape and icon. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. To resize a component specific to a state, such as the icon,
select the state in the toolbar, and then resize or reposition the component.

To combine the shape and icon, in the third section of the toolbar from the left, choose
one of these combination styles:

- Simple — Overlay the icon on top of the shape.
- Intersect — Retain the intersection of the shape and icon as the area whose color
  reflects the signal value.
- Subtract — Retain the shape with the icon cut out of it as the area that changes
  color.

Three Lamp blocks, each configured for one of the three ways you can combine the shape and icon: simple, intersect, or subtract.

**Tip**

The intersect and subtract combination styles use transparency in the icon asset to
produce the area that changes color. For custom icons, consider using image formats that
support transparency, such as SVG or PNG.

**Design Mode Actions that Apply to All States**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a background image. | No | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

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

This animation shows how to connect the Lamp block to your model.

An unconnected Lamp block connects to the signal that a Constant block sends to an Outport block.
