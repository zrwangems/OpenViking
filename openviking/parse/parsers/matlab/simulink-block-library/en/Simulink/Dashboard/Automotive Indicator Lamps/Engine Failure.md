---
type: simulink-block
title: 'Lamp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'lamp'
documentation_source_path: 'slref/lamp.html'
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
  group: ''
  block_parameter: Binding
  type: Simulink.HMI.SignalSpecification
  default: '[]'
- name: States
  summary: Signal value and color pairs scalar and RGB vector
  group: ''
  block_parameter: ColorDefault
  type: '[r g b] vector'
  default: '[0.7529 0.7529 0.7529]'
- name: Icon
  summary: Lamp block appearance SVG image
  group: ''
  block_parameter: Icon
  type: string | character vector
  default: '''Default'''
- name: Label
  summary: Block label position Top (default) | Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
- name: Opacity
  summary: Block opacity 1 (default) | scalar
  group: ''
  block_parameter: Opacity
  type: scalar
  default: '1'
```

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

### **States** — Signal value and color pairs scalar and `RGB` vector

States match a display color to the value of the connected signal. Each state
consists of a **State** and a **Color**.

- **State** — Connected signal value that causes the
  Lamp block to display the specified color.
- **Color** — Lamp color when the connected signal
  value matches the corresponding **State** value. You
  can select from a palette of standard colors or specify a custom color
  with `RGB` values.

The `[undefined]` state specifies the color of the
Lamp block when the connected signal value does not match any of
the values specified in the **States** table. Click the
**+** button to add another state.

#### Programmatic Use

To programmatically specify the `State` and
`Color` parameter values for a Lamp block,
use an array of structures that contain these fields:

- `Value` — Scalar `double` signal
  value that causes the Lamp block to display the
  specified color indication.
- `Color` —
  `1`-by-`3`
  `[r g b]` vector with values between
  `0` and `1` that specifies the
  color for the Lamp block to display.

```
lampState1.Value = 1;
lampState1.Color = [0 0 1];
lampState2.Value = 2;
lampState2.Color = [1 0 0];
lampStates = [lampState1 lampState2];
```

|  |
| --- |
| **Block Parameter:** `StateColors` |
| **Type:** structure array |
| **Default:** structure |

The `ColorDefault` parameter specifies the color for the
Lamp block when the value of the connected signal does not
match any of the specified state values. Specify the
`ColorDefault` parameter as a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ColorDefault` |
| **Type:** `[r g b]` vector |
| **Default:** `[0.7529 0.7529 0.7529]` |

### **Icon** — Lamp block appearance SVG image

Use an icon to configure the appearance of the Lamp block
in the model. You can choose from built-in shape, automotive, and wireless
icons, or you can upload your own custom SVG file as an icon.

To view icon options, on the **Icon** tab, select an
**Icon Type**. To use your own SVG file as the block
icon, select `Custom` as the **Icon
Type** and upload the SVG file. The state colors for the
Lamp block can apply to these SVG elements:

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

**Shape Icons**

| Icon | Basic Shapes Library Block Name | Programmatic Use Value |
| --- | --- | --- |
| Lamp icon: a solid gray circle | Lamp | `Default` |
| Circle icon: a solid black circle | Circle | `Circle` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |
| Check1 icon: a check mark | Check1 | `Check1` |
| Check2 icon: a check mark with slightly curved lines | Check2 | `Check2` |
| Check3 icon: the outline of a check mark | Check3 | `Check3` |
| Check4 icon: a check mark with a divot along its outline | Check4 | `Check4` |
| Ex1 icon: a cross mark | Ex1 | `Ex1` |
| Ex2 icon: a cross mark with one curved line | Ex2 | `Ex2` |
| Ex3 icon: the outline of a cross mark | Ex3 | `Ex3` |
| Ex4 icon: a cross mark with a divot along the outline | Ex4 | `Ex4` |
| Face icon: the outline of a face with a closed mouth in a straight line | Face | `Face` |
| Frown1 icon: the outline of a face with an open downturned mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed downturned mouth | Frown2 | `Frown2` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open downturned mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed downturned mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |

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

- You can change the icon for a Lamp block using
  the block tab in the toolstrip.
- The Dashboard library has libraries with a preconfigured
  Lamp block for each icon.
- If you want to customize the appearance of the
  Lamp block beyond the ability to select an
  icon, consider designing your own indicator lamp using the
  Lamp block in the Customizable Blocks
  library.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Icon` |
| **Type:** string | character vector |
| **Default:** `'Default'` |

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

### **Opacity** — Block opacity `1` (default) | scalar

Block opacity, specified as a scalar value between 0 and 1.

**Example:** `0.5`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Opacity` |
| **Type:** scalar |
| **Default:** `1` |
## Libraries

Simulink / Dashboard

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

**Introduced in R2015a**

## Description

Display color that reflects signal value on lamp

The Lamp block displays a color that indicates the value of the
connected signal. To configure the Lamp block to provide the information
you need during simulation, specify one or more states, which pair a signal value with a
color for the Lamp block to display. You can use the Lamp
block with other Dashboard blocks to build an interactive dashboard of controls and
indicators for your model.

### Lamp Icons

You can change the appearance of the Lamp block by selecting one of
the built-in icons or uploading your own custom icon. The built-in icons include
basic shapes, automotive indicator lamps, and wireless icons. You can change the
icon for a Lamp block by using the **Icon**
parameter or by using the block tab in the toolstrip. The Dashboard library also
includes libraries that have a preconfigured version of the Lamp
block for each icon. For complete details, see Icon.

Lamp Icon drop-down menu showing basic shape icons, automotive indicator lamps, wireless icons, and the option to choose a custom icon

If you want to customize the appearance of the Lamp block beyond
the ability to select an icon, consider designing your own indicator lamp using the
Lamp
block in the Customizable Blocks library.

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

This animation shows how to connect the Lamp block to your
model.

An unconnected Lamp block connects to the signal that a Ramp block sends to a Terminator block.
