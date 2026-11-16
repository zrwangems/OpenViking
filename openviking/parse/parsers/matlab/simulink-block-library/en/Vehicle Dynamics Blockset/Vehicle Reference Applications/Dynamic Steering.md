---
type: simulink-block
title: 'Dynamic Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'dynamicsteering'
documentation_source_path: 'ref/dynamicsteering.html'
language: en
---

# Dynamic Steering

## Ports

### Input

### **TrqIn** — Torque `scalar`

Torque, *τin*, in N·m.

### **TrqLft** — Left wheel torque `scalar`

Left wheel torque, *τL*, in
N·m.

### **TrqRght** — Right wheel torque `scalar`

Right wheel torque, *τR*, in
N·m.

### **VehSpd** — Vehicle speed `scalar`

Vehicle speed, *v*, in m/s.

#### Dependencies

To create a `VehSpd` port, select **Power
assist**.
### Output

### **Info** — Bus signal bus

Bus signal contains these block calculations.

| Signal | Description | Unit |
| --- | --- | --- |
| `StrgWhlAng` | Steering wheel angle | rad |
| `StrgWhlSpd` | Steering wheel angular velocity | rad/s |
| `ShftAng` | Shaft angle | rad |
| `ShftSpd` | Shaft angular velocity | rad/s |
| `AngLft` | Left wheel angle | rad |
| `SpdLft` | Left wheel angular velocity | rad/s |
| `AngRght` | Right wheel angle | rad |
| `SpdRght` | Right wheel angular velocity | rad/s |
| `TrqAst` | Torque assist | N·m |
| `PwrAst` | Power assist | W |
| `PwrLoss` | Power loss | W |
| `InstStrgRatio` | Instantaneous steering ratio | NA |

### **AngLft** — Left wheel angle `scalar`

Left wheel angle, *δL*, in
rad.

### **AngRght** — Right wheel angle `scalar`

Right wheel angle, *δR*, in
rad.

## Parameters

### **Type** — Select steering type `Rack and pinion` (default) | `Ackerman` | `Parallel`

To specify the steering
type, use the **Type** parameter.

| Setting | Block Implementation |
| --- | --- |
| `Ackerman` | Ideal Ackerman steering. Wheel angles have a common turning circle center. |
| `Rack and pinion` | Ideal rack-and-pinion steering. Gears convert the steering rotation into linear motion. |
| `Parallel` | Parallel steering. Wheel angles are equal. |

#### Dependencies

This table summarizes the **Type** and **Parametrized
by** parameter dependencies.

| Type | Parameterized By | Creates Parameters |
| --- | --- | --- |
| `Ackerman` | `Constant` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |
| `Rack and pinion` | `Constant` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius, PnnRadius** |
| `Lookup table` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius table, PnnRadiusTbl** |
| `Parallel` | `Constant` | **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |

### **Parametrized by** — Select parameterization `Lookup table` (default) | `Constant`

To specify the type of
data for the steering mechanism, use the **Parametrized by**
parameter.

| Setting | Block Implementation |
| --- | --- |
| `Constant` | Steering mechanism uses constant parameter data. |
| `Lookup table` | Steering mechanism implements tables for parameter data. |

#### Dependencies

This table summarizes the **Type** and **Parametrized
by** parameter dependencies.

| Type | Parameterized By | Creates Parameters |
| --- | --- | --- |
| `Ackerman` | `Constant` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |
| `Rack and pinion` | `Constant` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius, PnnRadius** |
| `Lookup table` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius table, PnnRadiusTbl** |
| `Parallel` | `Constant` | **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |

### **Power assist** — Specify power assist `on` (default) | `off`

If you select **Power assist**, you can specify a torque
assist lookup table, *ƒtrq*, that is
a function of the vehicle speed, *v*, and steering wheel
input torque, *τin*.

τast=ftrq(v,τin)

The block uses the steering wheel input torque and torque
assist to calculate the steering dynamics.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Location** — Select location **Front** (default) | **Rear**

Use the **Steered axle** parameter to
specify whether the front or rear axle is steered.

| Setting | Implementation |
| --- | --- |
| **Front** | Front axle steering  Figure of front steering turning right |
| **Rear** | Rear axle steering  Figure of rear steering turning right |

#### General

### **Track width, TrckWdth** — Width `1` | `scalar`

Track width, *TW*, in m.

#### Dependencies

To create this parameter, set **Type** to
`Ackerman` or `Rack and
pinion`.

### **Wheel base, WhlBase** — Base `1.524` (default) | `scalar`

Wheel base, *WB*, in m.

#### Dependencies

To create this parameter, set **Type** to
`Ackerman`.

### **Steering range, StrgRng** — Range `1.25*pi` (default) | `scalar`

Steering range, in rad. The block limits the wheel angles to remain within the
steering range.

### **Steering ratio, StrgRatio** — Ratio `13.5` (default) | `scalar`

Steering ratio, *γ*, dimensionless.

#### Dependencies

To create this parameter:

- Set **Type** to `Ackerman` or
  `Parallel`.
- Set **Parametrized by** to
  `Constant`.

### **Steering angle breakpoints, StrgAngBpts** — Breakpoints `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | `vector`

Steering angle breakpoints, in rad.

#### Dependencies

To create this parameter, set **Parametrized by** to
`Lookup table`.

### **Steering ratio table, StrgRatioTbl** — Table `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]` (default) | `vector`

Steering ratio table, *γ*, dimensionless.

#### Dependencies

To create this parameter:

- Set **Type** to `Ackerman` or
  `Parallel`.
- Set **Parametrized by** to `Lookup
  table`.

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

#### Dynamics

### **Steering wheel inertia, J1** — Inertia `0.1` (default) | `scalar`

Steering wheel inertia, *J1*, in
kg\*m^2.

### **Steering mechanism inertia, J2** — Inertia `0.01` (default) | `scalar`

Steering mechanism inertia, *J2*,
in kg\*m^2.

### **Upper hysteresis modifier, beta\_u** — Upper hysteresis modifier `0.1` (default) | `scalar`

Upper hysteresis modifier, *βu*,
dimensionless.

### **Lower hysteresis modifier, beta\_l** — Lower hysteresis modifier `0.1` (default) | `scalar`

Lower hysteresis modifier, *βl*,
dimensionless.

### **Hysteresis viscous damping, b1** — Damping `0.001` (default) | `scalar`

Hysteresis damping, *b1*, in
N·m·s/rad.

### **Hysteresis stiffness, k1** — Stiffness `30` (default) | `scalar`

Hysteresis stiffness, *k1*,in
N·m/rad.

### **Steering wheel damping, b2** — Damping `1` (default) | `scalar`

Steering wheel damping, *b2*, in
N·m·s/rad.

### **Steering mechanism damping, b3** — Damping `0.001` (default) | `scalar`

Steering mechanism damping, *b3*,
in N·m·s/rad.

### **Initial steering angle, theta\_o** — Angle `0` (default) | `scalar`

Initial steering angle, *θ0*, in
rad.

### **Initial steering angular velocity, omega\_o** — Angular velocity `0` (default) | `scalar`

Initial steering angular velocity,
*ωo*, in rad/s.

### **Friction torque, FricTrq** — Torque `0` (default) | `scalar`

Friction torque, *τfric*, in
N·m.

#### Power Assist

### **Steering wheel torque breakpoints, TrqBpts** — Breakpoints `[-100 0 100]` (default) | `1`-by-`M` vector

Steering wheel torque breakpoints, in N·m.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Vehicle speed breakpoints, VehSpdBpts** — Breakpoints `[0 20]` (default) | `1`-by-`N` vector

Vehicle speed breakpoints, in m/s.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque table, TrqTbl** — 2D torque table `[0 -100;0 0;0 100]` (default) | `M`-by-`N` matrix

Assisting torque table, *ƒtrq*, in
N·m.

The torque assist lookup table is a function of the vehicle speed,
*v*, and steering wheel input torque,
*τin*.

τast=ftrq(v,τin)

The block uses the steering wheel input torque and torque
assist to calculate the steering dynamics.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque limit, TrqLmt** — Torque limit `100` (default) | `scalar`

Assisting torque limit, in N·m.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting power limit, PwrLmt** — Power limit `1000` (default) | `scalar`

Assisting power limit, in N·m/s.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque efficiency, Eta** — Efficiency `1` (default) | `scalar`

Assisting torque efficiency, dimensionless.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Cutoff frequency, omega\_c** — Cutoff frequency `200` (default) | `scalar`

Cutoff frequency, in rad/s.

#### Dependencies

Selecting **Power assist** creates the `VehSpd` input
port and these parameters.

| Power Assist | Parameters |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

## Libraries

Vehicle Dynamics Blockset / Steering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024a: Removed

The Dynamic Steering is removed. Use the Steering
System block instead.

### R2023b: To be removed

The Dynamic Steering will be removed in a future release. Instead,
use the Steering
System block.

### R2023a: Not recommended

The Dynamic Steering is not recommended. Instead, use the Steering
System block to implement dynamic steering, including:

- Ackerman percentage that adjusts the ideal Ackerman outside wheel
  angle. You can use an input port or parameters to specify a constant or
  table of Ackerman percentages.
- Single or double Cardan joint to model the intermediate steering
  shaft.
- Friction and compliance effects.
- Input ports for power assistance, Ackerman steering, and kingpin
  moments.

## Description

(Removed) Dynamic steering for Ackerman, rack-and-pinion, and parallel steering mechanisms

The Dynamic Steering block implements dynamic steering to calculate the
wheel angles for Ackerman, rack-and-pinion, and parallel steering mechanisms. The block
uses the steering wheel input torque, right wheel torque, and left wheel torque to
calculate the wheel angles. The block uses the vehicle coordinate system.

If you select **Power assist**, you can specify a torque assist
lookup table that is a function of the vehicle speed and steering wheel input torque.
The block uses the steering wheel input torque and torque assist to calculate the
steering dynamics.

To specify the steering
type, use the **Type** parameter.

| Setting | Block Implementation |
| --- | --- |
| `Ackerman` | Ideal Ackerman steering. Wheel angles have a common turning circle center. |
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

### Dynamics

To calculate the steering dynamics, the Dynamic Steering block
models the steering wheel, shaft, steering mechanism, hysteresis, and, optionally,
power assist.

Figure of steering wheel, spring damper, and steering mechanism

| Calculation | Equations |
| --- | --- |
| Steering column and steering shaft dynamics | J1θ¨1=τin−b2θ˙1−τhys      J2θ¨2=τeq−b3θ˙2+τhys−τfric |
| Hysteresis spring damper | δ=θ1−θ2Δδ=δcurrent−δpreviousτhys=(b1δ˙−k1δ)(1+exp(−|Δδ|β))β={βu   when  δ>0βl    when  δ≤0 |
| Optional power assist | τast=ftrq(v,τin)J1θ¨1=τin+τast−b2θ˙1−τhysJ2θ¨2=τeq+τast−b3θ˙2+τhys−τfric |

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *J1* | Steering wheel inertia |
| *J2* | Steering mechanism inertia |
| θ1,θ˙1,θ¨1 | Steering wheel angle, angular velocity, and angular acceleration, respectively |
| θ2,θ˙2,θ¨2 | Shaft angle, angular velocity, and angular acceleration, respectively |
| *b1*, *k1* | Hysteresis spring and viscous damping coefficients, respectively |
| *b2* | Steering wheel viscous damping coefficient |
| *b3* | Steering mechanism damping coefficient |
| *τhys* | Hysteresis spring damping torque |
| *τfric* | Steering mechanism friction torque |
| *τeq* | Wheel equivalent torque |
| *τast* | Torque assist |
| *βu*, *βl* | Upper and lower hysteresis modifiers, respectively |
| *v* | Vehicle speed |
| *ƒtrq* | Torque assist lookup table |

### Steering Types

**Ackermann Steering**

For 100% (ideal) Ackermann steering, all wheels follow circular arcs with the same center point.

Figure of Ackermann steering turning right around turning circle

To calculate the steered wheel angles, the Steering System block uses these equations:

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

This table defines variables used in the equations:

|  |  |
| --- | --- |
| *δin* | Pinion angle (steering shaft angle into pinion) |
| *δL* | Left wheel steer angle |
| *δR* | Right wheel steer angle |
| *δAck* | Ackermann steer angle |
| *TW* | Track width |
| *WB* | Wheel base |
| *γ* | Steering ratio: Ratio of pinion angle to Ackermann angle |

**Rack-and-Pinion**

For rack-and-pinion steering, pinion rotation causes linear motion of the rack, which
steers the wheels through the tie rods and steering arms.

Figure of rack, rod, and arm in rack and pinion steering mechanism

Figure of rod in rack and pinion steering mechanism

To calculate the steered wheel angles, the block uses these equations.

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Pinion angle (steering shaft angle into pinion) |
| *δL* | Left wheel steer angle |
| *δR* | Right wheel steer angle |
| *TW* | Track width |
| *r* | Pinion radius |
| *ΔP* | Linear change in rack position from "straight ahead" position |
| *D* | Longitudinal distance between rack and steered axle |
| *lrack* | Rack length (distance between inner tie-rod ends) |
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
