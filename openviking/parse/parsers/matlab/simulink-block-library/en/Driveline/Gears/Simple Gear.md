---
type: simulink-block
title: 'Simple Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'simplegear'
documentation_source_path: 'ref/simplegear.html'
language: en
---

# Simple Gear

## Ports
```yaml
ports:
- name: B
  summary: Base rotational mechanical
  direction: conserving
- name: F
  summary: Follower mechanical rotational
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Conserving

### **B** — Base rotational mechanical

Mechanical rotational conserving port associated with the base shaft.

### **F** — Follower mechanical rotational

Mechanical rotational conserving port associated with the follower shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects
gear temperature, and therefore, power transmission efficiency.

#### Dependencies

To enable this port, set **Friction model** to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`
## Parameters
```yaml
parameters:
- name: Follower (F) to base (B) teeth ratio (NF/NB)
  summary: Gear ratio 2 (default) | positive scalar
  group: Main
- name: Output shaft rotates
  summary: Shaft rotation direction In opposite direction to input shaft (default) | In same direction as input shaft
  group: Main
- name: Friction model
  summary: Default friction model No meshing losses - Suitable for HIL simulation (default) | Constant efficiency | Load-dependent
    efficiency | Temperature-dependent efficiency | Temperature and load-dependent efficiency
  group: Meshing Losses
- name: Efficiency
  summary: Torque transfer efficiency, *η* 0.8 (default) | 0≤ *η* < 1
  group: Meshing Losses
- name: Follower power threshold
  summary: Efficiency factor power basis 0.001 W (default) | positive scalar
  group: Meshing Losses
- name: Input shaft torque at no load
  summary: No-load torque 0.1 N*m (default) | positive scalar
  group: Meshing Losses
- name: Nominal output torque
  summary: Nominal torque 5 N*m (default) | positive scalar
  group: Meshing Losses
- name: Efficiency at nominal output torque
  summary: Nominal efficiency, *η* 0.8 (default) | 0 ≤ *η* < 1 | scalar
  group: Meshing Losses
- name: Follower angular velocity threshold
  summary: Efficiency factor angular velocity basis 0.01 rad/s (default) | positive scalar
  group: Meshing Losses
- name: Temperature
  summary: Temperature [280, 300, 320] K (default) | positive array
  group: Meshing Losses
- name: Efficiency
  summary: Efficiency, *η* [.95, .9, .85] (default) | 0 ≤ *η* < 1 | array
  group: Meshing Losses
- name: Follower power threshold
  summary: Efficiency factor power basis 0.001 W (default) | positive array
  group: Meshing Losses
- name: Load at base gear
  summary: Base gear load [1, 5, 10] N*m (default) | positive array
  group: Meshing Losses
- name: Efficiency matrix
  summary: Efficiency [.85, .8, .75; .95, .9, .85; .85, .8, .7] (default) | numerical array with positive elements in the
    range of [0,1)
  group: Meshing Losses
- name: Follower angular velocity threshold
  summary: Efficiency factor angular velocity basis 0.01 rad/s (default) | positive scalar
  group: Meshing Losses
- name: Enable backlash
  summary: Backlash option off (default) | on
  group: Backlash
- name: Hard stop model
  summary: Hard stop transition behavior Stiffness and damping applied smoothly through transition region, damped rebound
    (default) | ...
  group: Backlash
- name: Linear backlash
  summary: Translational backlash distance 1e-3 mm (default) | positive scalar
  group: Backlash
- name: Base (B) gear radius
  summary: Base gear pitch radius 0.1 m (default) | positive scalar
  group: Backlash
- name: Transition region
  summary: Region of gradual hard stop effects 1e-4 mm (default) | positive scalar
  group: Backlash
- name: Linear stiffness
  summary: Resistance to translational deformation 1e6 N/m (default) | positive scalar
  group: Backlash
- name: Linear damping
  summary: Tendency to dissipate translational energy 1e3 N/(m/s) (default) | positive scalar
  group: Backlash
- name: Coefficient of restitution
  summary: Collision energy loss coefficient 0.7 (default) | positive scalar
  group: Backlash
- name: Static contact speed threshold
  summary: Threshold relative speed between gear teeth before collision 0.001 m/s (default) | nonnegative scalar
  group: Backlash
- name: Static contact release force threshold
  summary: Threshold force needed to transition from contact mode to free mode 0.001 N (default) | positive scalar
  group: Backlash
- name: Viscous friction coefficients at base (B) and follower (F)
  summary: Coefficients of viscous friction [0, 0] N*m/(rad/s) (default) | positive array
  group: Viscous Losses
- name: Gear fault
  summary: Option to model gear fault Add fault
  group: Faults
- name: Faulted efficiency
  summary: Faulted efficiency 0.05 (default) | scalar in the range [0,1]
  group: Faults
- name: Faulted angle range
  summary: Fault angle range pi / 12 rad (default) | nonnegative scalar
  group: Faults
- name: Thermal mass
  summary: Thermal mass 50 J/K (default) | positive scalar
  group: Thermal Port
- name: Initial temperature
  summary: Temperature 300 K (default) | positive scalar
  group: Thermal Port
```

### Parameter Dependencies Table

The table shows how the visibility of some **Meshing Losses** parameters
and **Faults** parameters depend on the thermal model and the
option that you choose for other parameters.

| Default Model — For nonthermal models, thermal port **H** is not visible. | | | | | | Thermal Model — For thermal models, thermal port **H** is visible. | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Meshing Losses | | | | | | Meshing Losses | |
| Friction model — Choose `No meshing losses - Suitable for HIL simulation`, `Constant efficiency`, or `Load-dependent efficiency` | | | | | | Friction model — Choose `Temperature-dependent efficiency` or `Temperature and load-dependent efficiency` | |
| **No meshing losses - Suitable for HIL simulation** | **Constant efficiency** | | | **Load-dependent efficiency** | | **Temperature-dependent efficiency** | **Temperature and load-dependent efficiency** |
| Efficiency | | | Input shaft torque at no load | | Temperature | Temperature |
| Follower power threshold | | | Nominal output torque | | Efficiency | Load at base gear |
|  | | | Efficiency at nominal output torque | | Follower power threshold | Efficiency matrix |
|  | | | Follower angular velocity threshold | | Follower angular velocity threshold |

### Main

### **Follower (F) to base (B) teeth ratio (NF/NB)** — Gear ratio `2` (default) | positive scalar

Fixed ratio *gFB* of the
follower axis to the base axis. The gear ratio must be strictly
positive.

### **Output shaft rotates** — Shaft rotation direction `In opposite direction to input shaft` (default) | `In same direction as input shaft`

Direction of motion of the follower (output) driveshaft relative to
the motion of the base (input) driveshaft.

### Meshing Losses

Meshing losses parameters depend on the thermal model. For more information, see
Parameter Dependencies Table.

### **Friction model** — Default friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Load-dependent efficiency` | `Temperature-dependent efficiency` | `Temperature and load-dependent efficiency`

Friction models at various precision levels for estimating power
losses due to meshing.

- `No meshing losses - Suitable for HIL
  simulation` — Neglect friction
  between gear cogs. Meshing is ideal.
- `Constant efficiency` —
  Reduce torque transfer by a constant efficiency factor. This
  factor falls in the range 0 < *η* ≤ 1 and is independent from load.
- `Load-dependent efficiency`
  — Reduce torque transfer by a variable efficiency
  factor. This factor falls in the range 0 < *η* <
  1 and varies with the torque load.
- `Temperature-dependent
  efficiency` — Reduce torque transfer
  by a constant efficiency factor that is dependent on
  temperature but does not consider the gear load. This factor
  falls in the range 0 < *η* ≤ 1 and is independent from load. Torque
  transfer is determined from user-supplied data for gear
  efficiency and temperature.
- `Temperature and load-dependent
  efficiency` — Reduce torque transfer
  by a variable efficiency factor that is dependent on
  temperature and load. This factor falls in the range 0 < *η* <
  1 and varies with the torque load. Torque
  transfer efficiency is determined from user-supplied data
  for gear loading and temperature.

### **Efficiency** — Torque transfer efficiency, *η* `0.8` (default) | `0`≤ *η* < `1`

Torque transfer efficiency, *η*, between base and
follower shafts. Efficiency is inversely proportional to the meshing
power losses.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

For more information, see Parameter Dependencies Table.

### **Follower power threshold** — Efficiency factor power basis `0.001` `W` (default) | positive scalar

Absolute value of the follower shaft power above which the full
efficiency factor is in effect. Below this value, a hyperbolic tangent
function smooths the efficiency factor to 1, lowering the efficiency
losses to 0 when no power is transmitted.

As a guideline, the power threshold should be lower than the expected
power transmitted during simulation. Higher values might cause the block
to underestimate efficiency losses. Very low values tend to raise the
computational cost of simulation.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

For more information, see Parameter Dependencies Table.

### **Input shaft torque at no load** — No-load torque `0.1` `N*m` (default) | positive scalar

Net torque,*τidle*, acting on
the input shaft in idle mode, that is, when torque transfer to the
output shaft equals zero. For nonzero values, the power input in idle
mode completely dissipates due to meshing losses.

#### Dependencies

To enable this parameter, set **Friction model**
to `Load-dependent efficiency`.

For more information, see Parameter Dependencies Table.

### **Nominal output torque** — Nominal torque `5` `N*m` (default) | positive scalar

Output torque, *τ*F, at which
to normalize the load-dependent efficiency.

#### Dependencies

To enable this parameter, set **Friction model**
to `Load-dependent efficiency`.

For more information, see Parameter Dependencies Table.

### **Efficiency at nominal output torque** — Nominal efficiency, *η* `0.8` (default) | `0` ≤ *η* < `1` | scalar

Torque transfer efficiency, *η*, at the nominal
output torque. Larger efficiency values correspond to greater torque
transfer between the input and output shafts.

#### Dependencies

To enable this parameter, set **Friction model**
to `Load-dependent efficiency`.

For more information, see Parameter Dependencies Table.

### **Follower angular velocity threshold** — Efficiency factor angular velocity basis `0.01` `rad/s` (default) | positive scalar

Absolute value of the follower shaft angular velocity above which the
full efficiency factor is in effect,
*ωF*. Below this value, a
hyperbolic tangent function smooths the efficiency factor to one,
lowering the efficiency losses to zero when at rest.

As a guideline, the angular velocity threshold should be lower than
the expected angular velocity during simulation. Higher values might
cause the block to underestimate efficiency losses. Very low values tend
to raise the computational cost of simulation.

#### Dependencies

To enable this parameter, set **Friction model**
to `Load-dependent efficiency`.

For more information, see Parameter Dependencies Table.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | positive array

Array of temperatures used to construct an efficiency lookup table.
The array values must increase from left to right. The temperature array
must be the same size as the efficiency array in temperature-dependent
models. The array must be the same size as a single row of the
efficiency matrix in temperature and load dependent models.

#### Dependencies

To enable this parameter, set **Friction model**
to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

For more information, see Parameter Dependencies Table.

### **Efficiency** — Efficiency, *η* `[.95, .9, .85]` (default) | `0` ≤ *η* < `1` | array

Array of efficiencies used to construct a 1-D temperature-efficiency
lookup table for temperature-dependent efficiency models. The array
values are the efficiencies at the temperatures in the
**Temperature** array. The number of elements must
be the same as the number of elements in the
**Temperature** array.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

For more information, see Parameter Dependencies Table.

### **Follower power threshold** — Efficiency factor power basis `0.001` `W` (default) | positive array

Absolute value of the follower shaft power above which the full
efficiency factor is in effect,
*pF*. Below this value, a
hyperbolic tangent function smooths the efficiency factor to 1, lowering
the efficiency losses to 0 when no power is transmitted.

As a guideline, the power threshold should be lower than the expected
power transmitted during simulation. Higher values might cause the block
to underestimate efficiency losses. Very low values tend to raise the
computational cost of simulation.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

For more information, see Parameter Dependencies Table.

### **Load at base gear** — Base gear load `[1, 5, 10]` `N*m` (default) | positive array

Array of base-gear loads used to construct a 2-D temperature load
efficiency lookup table for temperature and load dependent efficiency
models. The array values must increase left to right. The load array
must be the same size as a single column of the efficiency
matrix.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature and load-dependent
efficiency`.

For more information, see Parameter Dependencies Table.

### **Efficiency matrix** — Efficiency `[.85, .8, .75; .95, .9, .85; .85, .8, .7]` (default) | numerical array with positive elements in the range of [0,1)

Matrix of component efficiencies used to construct a 2-D temperature
load efficiency lookup table. The matrix elements are the efficiencies
at the temperatures given by the **Temperature** array
and at the loads given by the **Load at base gear**
array.

The number of rows must be the same as the number of elements in the
**Temperature** array. The number of columns must
be the same as the number of elements in the **Load at base
gear** array.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature and load-dependent
efficiency`.

For more information, see Parameter Dependencies Table.

### **Follower angular velocity threshold** — Efficiency factor angular velocity basis `0.01` `rad/s` (default) | positive scalar

Absolute value of the follower shaft angular velocity above which the
full efficiency factor is in effect,
*ωF*. Below this value, a
hyperbolic tangent function smooths the efficiency factor to one,
lowering the efficiency losses to zero when at rest.

As a guideline, the angular velocity threshold should be lower than
the expected angular velocity during simulation. Higher values might
cause the block to underestimate efficiency losses. Very low values tend
to raise the computational cost of simulation.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature and load-dependent
efficiency`.

For more information, see Parameter Dependencies Table.

### Backlash

### **Enable backlash** — Backlash option `off` (default) | `on`

Whether to enable backlash.

### **Hard stop model** — Hard stop transition behavior `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | ...

Stiffness and rebound options for the hard stop model. You can choose
from these options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

For more information, see Translational Hard
Stop.

#### Dependencies

To enable this parameter, select **Enable
backlash**.

### **Linear backlash** — Translational backlash distance `1e-3` `mm` (default) | positive scalar

Translational distance that a gear tooth can travel between meshing
teeth.

#### Dependencies

To enable this parameter, select **Enable
backlash**.

### **Base (B) gear radius** — Base gear pitch radius `0.1` `m` (default) | positive scalar

Base gear distance from the center to the meshing point on the gear
tooth.

#### Dependencies

To enable this parameter, select **Enable
backlash**.

### **Transition region** — Region of gradual hard stop effects `1e-4` `mm` (default) | positive scalar

Distance where the block gradually applies effects of stiffness and
damping. When you set **Hard stop model** to
`Stiffness and damping applied smoothly through
transition region, damped rebound`, the block smoothly
transitions the onset of stiffness and damping as the hard stop
approaches full stiffness.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to `Stiffness and damping applied smoothly through
transition region, damped rebound`.

### **Linear stiffness** — Resistance to translational deformation `1e6` `N/m` (default) | positive scalar

Effective translational spring stiffness of the gear collision.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to one of these options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Linear damping** — Tendency to dissipate translational energy `1e3` `N/(m/s)` (default) | positive scalar

Effective translational damping of the gear collision.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to one of these options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Coefficient of restitution** — Collision energy loss coefficient `0.7` (default) | positive scalar

Loss of translational kinetic energy during collisions. A value of
`0` represents an inelastic collision, and a value
of `1` represents a perfectly elastic collision where
the gear retains all kinetic energy. The default of `0`
is equivalent to simulating gear torque when the gears are in contact,
and removing torque when the gear changes direction and the tooth
travels the backlash distance.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact speed threshold** — Threshold relative speed between gear teeth before collision `0.001` `m/s` (default) | nonnegative scalar

Velocity, *vtol*, below which
the gear tooth becomes locked with the meshing teeth. The block sets
*vTooth = 0* when
*|vTooth| <
vtol*.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact release force threshold** — Threshold force needed to transition from contact mode to free mode `0.001` `N` (default) | positive scalar

Minimum force needed to release the gear from a static contact
mode.

#### Dependencies

To enable this parameter, select **Enable
backlash** and set **Hard stop model**
to `Based on coefficient of
restitution`.

### Viscous Losses

### **Viscous friction coefficients at base (B) and follower (F)** — Coefficients of viscous friction `[0, 0]` `N*m/(rad/s)` (default) | positive array

Two-element array with the viscous friction coefficients in effect at
the base and follower shafts. To neglect viscous losses, use the default
setting, `[0, 0]`.

### Faults

To enable the **Faults** tab, set **Friction
model** to

- `Constant efficiency`
- `Load-dependent efficiency`
- `Temperature-dependent efficiency`
- `Temperature and load-dependent
  efficiency`

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Gear fault** — Option to model gear fault `Add fault`

Whether to model a fault in the block. When you trigger a fault, the
block applies the value of the **Faulted efficiency**
parameter to the range of the gear specified in the **Faulted
angle range** parameter. To add a fault, click the
**Add fault** hyperlink.

#### Dependencies

To enable this parameter, set **Meshing
Losses** to:

- `Constant efficiency`
- `Load-dependent
  efficiency`
- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

### **Faulted efficiency** — Faulted efficiency `0.05` (default) | scalar in the range [0,1]

Efficiency when a fault triggers.

#### Dependencies

To enable this parameter, enable faults for the block by clicking the **Add
fault** hyperlink.

### **Faulted angle range** — Fault angle range `pi / 12` `rad` (default) | nonnegative scalar

Rotational angle range for the faulted efficiency. For multiples of `2π
rad`, the block applies the value of the **Faulted
efficiency** parameter throughout rotation.

#### Dependencies

To enable this parameter, enable faults for the block by clicking the **Add
fault** hyperlink.

### Thermal Port

### **Thermal mass** — Thermal mass `50` `J/K` (default) | positive scalar

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set **Friction model**
to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

### **Initial temperature** — Temperature `300` `K` (default) | positive scalar

Temperature at simulation start.

#### Dependencies

To enable this parameter, set **Friction model**
to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`
## Libraries

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2024a: Model faults with the Simscape faults interface

The Simple Gear block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

### R2023a: Backlash updates

Due to updates in the Translational Hard Stop
block, the Simple Gear block provides new options
when modeling backlash. Previously, the block used the **Backlash
model** drop down parameter. Now, you can enable backlash when you
select **Enable backlash**.

The updated **Hard stop model** parameter provides the same
options as the Translational Hard Stop block. The
parameter names align with new options introduced in theTranslational
Hard Stop block.

## Description

Simple gear of base and follower wheels with adjustable gear ratio, friction losses, and triggered faults

The Simple Gear block represents a gearbox that
constrains the connected driveline axes of the base gear, *B*, and the
follower gear, *F*, to corotate with a fixed ratio that you specify.
You choose whether the follower axis rotates in the same or opposite direction as the
base axis. If they rotate in the same direction, the angular velocity of the follower,
*ωF*, and the angular velocity of the
base, *ωB*, have the same sign. If they rotate
in opposite directions, *ωF* and
*ωB* have opposite signs. You can easily
add and remove backlash, faults, and thermal effects.

### Ideal Gear Constraint and Gear Ratio

The kinematic constraint that the Simple Gear block
imposes on the two connected axes is

rFωF=rBωB

where:

- *rF* is the radius of the
  follower gear.
- *ωF* is the angular velocity
  of the follower gear.
- *rB* is the radius of the base
  gear.
- *ωB* is the angular velocity
  of the base gear.

The follower-base gear ratio is

gFB=rFrB=NFNB

where:

- *NB* is the number of teeth in
  the base gear.
- *NBF* is the number of teeth
  in the follower gear.

Reducing the two degrees of freedom to one independent degree of freedom yields
the torque transfer equation

gFBτB+τF−τloss=0

where:

- *τB* is the input
  torque.
- *τF* is the output
  torque.
- *τloss* is the torque loss due
  to friction.

For the ideal case, τloss=0.

### Nonideal Gear Constraint and Losses

In the nonideal case, τloss≠0. For general considerations on nonideal gear modeling, see Model Gears with Losses.

In a nonideal gear pair (B,F), the angular velocity, gear radii, and gear teeth
constraints are unchanged. But the transferred torque and power are reduced
by:

- Coulomb friction between teeth surfaces on gears *B* and
  *F*, characterized by efficiency,
  *η*
- Viscous coupling of driveshafts with bearings, parametrized by viscous
  friction coefficients, *μ*

**Constant Efficiency**

In the constant efficiency case, *η* is constant, independent
of load or power transferred.

**Load-Dependent Efficiency**

In the load-dependent efficiency case, *η* depends on the
load or power transferred across the gears. For either power flow,

τCoul=gFBτidle+kτF

where:

- *τCoul* is the Coulomb
  friction dependent torque.
- *k* is a proportionality constant.
- *τidle* is the net torque
  acting on the input shaft in idle mode.

Efficiency, *η*, is related to
*τCoul* in the standard,
preceding form but becomes dependent on load:

η=τFgFBτidle+(k+1)τF

### Backlash

You can incorporate the effects of backlash in your model. *Backlash* is
the excess space between a gear tooth and the mating gear teeth. Increasing the backlash
compensates for lowering manufacturing tolerances and allows the free motion of lubricants
in the gears to prevent jamming. However, excess backlash can cause premature wear on your
system components and can affect measurements that rely on gear position. The block applies
backlash for start-ups and reversals using an implementation of the Translational Hard Stop block.

When you select **Enable backlash**, the block relates gear rotation to
linear backlash as:

vTooth=rBωB−βrFωF,

where:

- *vTooth* is the relative linear
  velocity of the gear tooth.
- *rB* is the **Base (B) gear
  radius** parameter.
- *rF* is the follower gear radius,
  where *rF =
  NF/NB·**rB*,
  and the **Follower (F) to base (B) teeth ratio (NF/NB)**
  parameter represents
  *NF/NB*.
- *ωB* and
  *ωF* are the angular velocities
  of the base and follower gears, respectively.
- *β* is the gear direction sign. When you set:

  - **Output shaft rotates** to `In same
    direction as input shaft`, *β =
    1*.
  - **Output shaft rotates** to `In
    opposite direction as input shaft`, *β =
    -1*.

The block treats the meshing gear tooth as a position,
*xTooth*, with respect to the linear backlash,
*Backlash*, where *-1/2·Backlash <
xTooth < 1/2·Backlash*.
*Backlash* is equivalent to the **Linear backlash**
parameter. The initial value of the **Backlash position** variable is
equivalent to the initial position of
*xTooth*.

When you set **Hard stop model** to `Based on coefficient of
restitution`, the hard stop can incorporate a nonzero value for the
**Coefficient of restitution** parameter,
*coeffrest*, into the momentum balance
equation. During a collision,

coeffrest=vBacklash,t−vBacklash,t+,

where *t-* and *t+* are the instants
before and after the collision, respectively. The block asserts
*coeffrest* is in the range [0, 1]. For more
information, see State Reset Modeling. Simscape™ logs the mode state of the gear as the intermediate
**M**.

| State | Value |
| --- | --- |
| *M = 0* | Disengaged |
| *M = 1* | Forwards engaged with *xtooth = 1/2·Backlash* |
| *M = -1* | Backwards engaged with *xtooth = -1/2·Backlash* |
| *M = 2* | Instantaneous mode transition between forward engaged and forward disengaged |
| *M = -2* | Instantaneous mode transition between backward engaged and backward disengaged |
| *M = 3* | Instantaneous impact mode |

The hard stop simulates static contact at the bounds. The gear locks when a collision occurs
and *|vTooth| < vtol*.
Once the gear locks, *vTooth* = 0. Once *fTooth* >
*fTol*, the gear unlocks, where

- *fTol* is the **Static contact
  release force threshold** parameter.
- *vtol* is the **Static contact
  speed threshold** parameter.
- *fTooth* is the meshing force between
  the gear teeth such that *fTooth* =
  *TB/rB*
  =
  *TF/rF*.

### Faults

To model a fault in the Simple Gear block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block applies the value of the **Faulted
efficiency** parameter to the range of the gear specified in the
**Faulted angle range** parameter.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

Additionally, you can choose to model efficiency that varies with loading and
temperature by setting **Friction model** to
`Temperature and load-dependent efficiency`. Selecting
a thermal variant:

- Exposes port **H**, a conserving port in the thermal
  domain.
- Enables the **Thermal mass** parameter, which allows
  you to specify the ability of the component to resist changes in
  temperature.
- Enables the **Initial Temperature** parameter, which
  allows you to set the initial temperature.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.
