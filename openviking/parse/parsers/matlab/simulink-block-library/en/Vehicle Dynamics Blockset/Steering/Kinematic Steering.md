---
type: simulink-block
title: 'Kinematic Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'kinematicsteering'
documentation_source_path: 'ref/kinematicsteering.html'
language: en
---

# Kinematic Steering

## Ports

### Input

### **AngIn** — Steering angle `scalar`

Steering angle, *δin*, in
rad.

Use the **Steering range, StrgRng** parameter to
specify a steering angle range. By default, the value is set to 1.25\*pi,
which limits the steering angle to a range of -1.25\*pi to
1.25\*pi.

### **PctAckIn** — Ackerman percentage `scalar`

Ackerman percentage, *δin*, in
percent.

#### Dependencies

To create this input port:

- Set **Type** to
  `Ackerman`.
- On the **Ackerman Steering** pane,
  select **Input percent
  Ackerman**.
### Output

### **Info** — Bus signal bus

Bus signal contains this block calculation.

| Signal | Description | Variable | Unit |
| --- | --- | --- | --- |
| `InstStrgRatio` | Instantaneous steering ratio | *γ* | NA |

### **AngLft** — Left wheel angle `scalar`

Left wheel angle, *δL*, in
rad.

### **AngRght** — Right wheel angle `scalar`

Right wheel angle, *δR*, in
rad.

## Parameters

### **Type** — Select steering type `Ackerman` (default) | `Rack and pinion` | `Parallel`

To specify the steering
type, use the **Type** parameter.

| Setting | Block Implementation |
| --- | --- |
| `Ackerman` | Ideal Ackerman steering. Wheel angles have a common turning circle center. |
| `Rack and pinion` | Ideal rack-and-pinion steering. Gears convert the steering rotation into linear motion. |
| `Parallel` | Parallel steering. Wheel angles are equal. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgType` |
| **Values:** | `Ackerman` (default) | `Rack and pinion` | `Parallel` |
| **Data Types:** | `character vector` |

### **Parametrized by** — Select parameterization `Constant` (default) | `Lookup table`

To specify the type of
data for the steering mechanism, use the **Parametrized by**
parameter.

| Setting | Block Implementation |
| --- | --- |
| `Constant` | Steering mechanism uses constant parameter data. |
| `Lookup table` | Steering mechanism implements tables for parameter data. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgRatioType` |
| **Values:** | `Constant` (default) | `Lookup table` |
| **Data Types:** | `character vector` |

### **Location** — Select location **Front** (default) | **Rear**

Use the **Steered axle** parameter to
specify whether the front or rear axle is steered.

| Setting | Implementation |
| --- | --- |
| **Front** | Front axle steering  Figure of front steering turning right |
| **Rear** | Rear axle steering  Figure of rear steering turning right |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Loc` |
| **Values:** | `Front` (default) | `Rear` |
| **Data Types:** | `character vector` |

### **Normalization factor, NrmlFctr** — Adjust the steering angle `scalar`

Factor, *NrmFctr*, that the block
uses to adjust the steering ratio, *γ* or pinion radius,
*r*. The block can only normalize if you have
**Parametrized by** set to
`Constant`.

To adjust the steering ratio or pinion radius, click
**Normalize**.

| Steering Type | Normalization |
| --- | --- |
| `Ackerman`  `Parallel` | Block updates the **Steering ratio, StrgRatio** parameter to the normalized value, *γnrm*, specified by this equation.  γnrm=1NrmFctr |
| `Rack and pinion` | Block updates the **Pinion radius, PnnRadius** parameter to using the normalization factor, *NrmFctr*. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NrmlFctr` |
| **Values:** | `scalar` |
| **Data Types:** | `double` |

#### General

### **Track width, TrckWdth** — Width `1` (default) | `scalar`

Track width, *TW*, in m.

#### Dependencies

To create this parameter, set **Type** to
`Ackerman` or `Rack and
pinion`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrckWdth` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Wheel base, WhlBase** — Base `1.524` (default) | `scalar`

Wheel base, *WB*, in m.

#### Dependencies

To create this parameter, set **Type** to
`Ackerman`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WhlBase` |
| **Values:** | `1.524` (default) | `scalar` |
| **Data Types:** | `double` |

### **Deadband, Db** — Deadband `0` (default) | `scalar`

Deadband steering angle before pinion engages the gear, in rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Db` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Steering range, StrgRng** — Steering wheel angle input range `1.25*pi` (default) | `scalar`

Steering wheel angle input range, in rad. The block limits the steering
wheel input angles to remain within the steering range.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgRng` |
| **Values:** | `1.25*pi` (default) | `scalar` |
| **Data Types:** | `double` |

### **Steering ratio, StrgRatio** — Ratio `100` (default) | `scalar`

Steering ratio, *γ*, dimensionless.

#### Dependencies

To create this parameter:

- Set **Type** to `Ackerman` or
  `Parallel`.
- Set **Parametrized by** to
  `Constant`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgRatio` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

### **Steering angle breakpoints, StrgAngBpts** — Breakpoints `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | `vector`

Steering angle breakpoints, in rad.

#### Dependencies

To create this parameter, set **Parametrized by** to
`Lookup table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgAngBpts` |
| **Values:** | `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | `vector` |
| **Data Types:** | `double` |

### **Steering ratio table, StrgRatioTbl** — Table `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]` (default) | `vector`

Steering ratio table, *γ*, dimensionless.

#### Dependencies

To create this parameter:

- Set **Type** to `Ackerman` or
  `Parallel`.
- Set **Parametrized by** to `Lookup
  table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgRatioTbl` |
| **Values:** | `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]` (default) | `vector` |
| **Data Types:** | `double` |

#### Rack-and-Pinion

### **Steering arm length, StrgArmLngth** — Length `0.1` (default) | `scalar`

Steering arm length, *larm*, in m.

#### Dependencies

To create this parameter, set **Type** to `Rack and
pinion`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgArmLngth` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Rack casing length, RckCsLngth** — Length `0.5` (default) | `scalar`

Rack casing length, *lrack*, in m.

#### Dependencies

To create this parameter, set **Type** to `Rack and
pinion`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RckCsLngth` |
| **Values:** | `0.5` (default) | `scalar` |
| **Data Types:** | `double` |

### **Tie rod length, TieRodLngth** — Length `0.248` (default) | `scalar`

Tie rod length, *lrod*, in m.

#### Dependencies

To create this parameter, set **Type** to `Rack and
pinion`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TieRodLngth` |
| **Values:** | `0.248` (default) | `scalar` |
| **Data Types:** | `double` |

### **Distance between axis and rack, D** — Distance `0.2` (default) | `scalar`

Distance between axis and rack, *D*, in m.

#### Dependencies

To create this parameter, set **Type** to `Rack and
pinion`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `D` |
| **Values:** | `0.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Pinion radius, PnnRadius** — Radius `0.0057` (default) | `scalar`

Pinion radius, *r*, in m.

#### Dependencies

To create this parameter:

- Set **Type** to `Rack and
  pinion`.
- Set **Parametrized by** to
  `Constant`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PnnRadius` |
| **Values:** | `0.0057` (default) | `scalar` |
| **Data Types:** | `double` |

### **Pinion radius table, PnnRadiusTbl** — Table `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]` (default) | `vector`

Pinion radius table, *r*, in m.

#### Dependencies

To create this parameter:

- Set **Type** to `Rack and
  pinion`.
- Set **Parametrized by** to `Lookup
  table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PnnRadiusTbl` |
| **Values:** | `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]` (default) | `vector` |
| **Data Types:** | `double` |

#### Ackerman Steering

### **Input Percent Ackerman** — Create `PctAckIn` input port `off` (default) | `on`

Select to create `PctAckIn` input port.

#### Dependencies

To enable this parameter, set **Type** to
`Ackerman`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `PctAckIn` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Percent Ackerman, PctAck** — Percent Ackerman constant `100` (default) | `scalar`

Constant value of percent Ackerman, in percent.

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Ackerman`
- Set **Parametrized by** to
  `Constant`
- Clear **Input Percent Ackerman**

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `PctAck` |
| **Values:** | `100` (default) | `scalar` |
| **Data Types:** | `double` |

### **Percent Ackerman table, PctAckTbl** — Percent Ackerman table `ones(1,11)*100` (default) | `vector`

Table of percent Ackerman values as a function of the steering angle,
*δin*, in percent.

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Ackerman`
- Set **Parametrized by** to
  `Constant`
- Clear **Input Percent Ackerman**

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `PctAckTbl` |
| **Values:** | `ones(1,11)*100` (default) | `vector` |
| **Data Types:** | `double` |

## Libraries

Vehicle Dynamics Blockset / Steering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Kinematic steering for Ackerman, rack-and-pinion, and parallel steering mechanisms

The Kinematic Steering block implements a steering model to determine
the left and right wheel angles for Ackerman, rack-and-pinion, and parallel steering
mechanisms. The block uses the vehicle coordinate system.

To specify the steering type, use the
**Type** parameter.

| Setting | Block Implementation |
| --- | --- |
| `Ackerman` | Ideal Ackerman steering, adjusted by percentage Ackerman. Wheel angles have a common turning circle center. |
| `Rack and pinion` | Ideal rack-and-pinion steering. Gears convert the steering rotation into linear motion. |
| `Parallel` | Parallel steering. Wheel angles are equal. |

To specify the type of
data for the steering mechanism, use the **Parametrized by**
parameter.

| Setting | Block Implementation |
| --- | --- |
| `Constant` | Steering mechanism uses constant parameter data. |
| `Lookup table` | Steering mechanism implements tables for parameter data. |

Use the **Steered axle** parameter to
specify whether the front or rear axle is steered.

| Setting | Implementation |
| --- | --- |
| **Front** | Front axle steering  Figure of front steering turning right |
| **Rear** | Rear axle steering  Figure of rear steering turning right |

### Steering Types

**Ackerman**

For ideal Ackerman steering, the wheel angles have a common turning circle.

Figure of Ackerman steering turning right around turning circle

To calculate the ideal wheel angles, the block uses these equations.

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

After the block calculates the ideal wheel angles, it uses the Ackerman
percentage to adjust the outside wheel angle.

δo=δi−pAck(δi−δAck)

The outside wheel angle depends on the turn direction.

- Right turn

  - Outside angle,
    *δo*, is left
    wheel angle,
    *δL*
  - Inside angle,
    *δi*, is right wheel
    angle, *δR*
- Left turn

  - Outside angle,
    *δo*, is right
    wheel angle,
    *δR*
  - Inside angle,
    *δi*, is left wheel
    angle, *δL*

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Steering angle |
| *δL* | Left wheel angle |
| *δR* | Right wheel angle |
| *δo* | Outside wheel angle |
| *δi* | Inside wheel angle |
| *pAck* | Ackerman percentage |
| *TW* | Track width |
| *WB* | Wheel base |
| *γ* | Steering ratio |

**Rack-and-Pinion**

For ideal rack-and-pinion steering, the gears convert the steering rotation
into linear motion.

Figure of rack, rod, and arm in rack and pinion steering mechanism

Figure of rod in rack and pinion steering mechanism

To calculate the steering angles, the block uses these equations.

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Steering wheel angle |
| *δL* | Left wheel angle |
| *δR* | Right wheel angle |
| *TW* | Track width |
| *r* | Pinion radius |
| *ΔP* | Linear change in rack position |
| *D* | Distance between front axis and rack |
| *lrack* | Rack casing length |
| *larm* | Steering arm length |
| *lrod* | Tie rod length |

**Parallel**

For parallel steering, the wheel angles are equal.

Figure parallel steering where wheel angles are equal

To calculate the steering angles, the block uses this equation.

δR=δL=δinγ

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Steering wheel angle |
| *δL* | Left wheel angle |
| *δR* | Right wheel angle |
| *γ* | Steering ratio |
