---
type: simulink-block
title: 'Dog Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'dogclutch'
documentation_source_path: 'ref/dogclutch.html'
language: en
---

# Dog Clutch

## Ports

### Input

### **S** — Logical shift linkage, unitless physical signal

Physical signal input port associated with the shift linkage,
unitless. A logical `true` allows the clutch to engage
if the relative speeds of the hub and ring are within tolerance. A
logical `false` causes the clutch to disengage.

#### Dependencies

To enable this port, set **Torque transmission
model** to:

- `Two-mode`
- `Friction clutch approximation - Suitable
  for HIL and linearization`, and set
  **Shift linkage control** to
  `Physical signal`
- `Dynamic with backlash`, and
  set **Shift linkage control** to
  `Physical signal`
### Output

### **X** — Clutch position, m or unitless physical signal

Physical signal output port associated with the clutch position, in
*m* or unitless. When you set **Torque
transmission model** to
`Two-mode`, the port outputs a logical
value `true` for engaged or `false`
for disengaged. Otherwise, the port outputs the position of the
clutch.
### Conserving

### **H** — Clutch hub mechanical rotational

Mechanical rotational conserving port associated with the clutch
hub

### **R** — Clutch ring mechanical rotational

Mechanical rotational conserving port associated with the clutch
ring.

### **S** — Shift linkage mechanical translational

Mechanical translational conserving port associated with shift
linkage.

#### Dependencies

To enable this port, set **Torque transmission
model** to:

- `Friction clutch approximation - Suitable
  for HIL and linearization`
- `Dynamic modal`
- `Dynamic with backlash` and
  set **Shift linkage control** to
  `Conserving port`

### **T** — Heat flow thermal

Thermal conserving port associated with heat flow.

#### Dependencies

To enable this port, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

## Parameters

### Clutch

### **Torque transmission model** — Torque transmission model `Two-mode` (default) | `Friction clutch approximation - Suitable for HIL and linearization` | `Dynamic with backlash` | `Dynamic modal`

Method to model the behavior of the dog clutch:

- `Two-mode` — Fully abstracted
  torque transmission model based on mode charts. This setting
  is fast enough for real time simulation and does not require
  knowledge of the clutch dimensions. You can control the
  shift linkage only with a physical or logic-controlled
  signal.
- `Friction clutch approximation - Suitable for
  HIL and linearization` — Medium- to
  high-fidelity composite implementation of the Fundamental Friction
  Clutch block. This setting supports thermal
  modeling. You can control the shift linkage by using either
  a physical signal or a mechanical translational conserving
  connection.
- `Dynamic with backlash` —
  High-fidelity clutch engagement model, that accounts for
  phenomena such as backlash, torsional compliance, and
  contact forces between the ring and hub teeth.
- `Dynamic modal` — System-level
  clutch engagement model that captures the effects of
  engagement blocking due to the speed differential.

### **Engagement speed threshold** — Engagement speed threshold `5` `rpm` (default) | positive scalar

Minimum rotational speed at which the clutch delivers power.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Two-mode` or
`Dynamic modal`.

### **Thermal port** — Option to enable thermal port `Omit` (default) | `Model`

Whether to enable the thermal conserving port, **T**.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`.

### **Clutch teeth mean radius** — Clutch teeth mean radius `50` `mm` (default) | positive scalar

Distance from the ring or hub center to the corresponding tooth
center. The mean tooth radius determines the normal contact forces
between the ring and hub teeth given the transmission torque between the
two components. The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash`.

### **Maximum transmitted torque** — Maximum transmitted torque `1000` `N*m` (default) | positive scalar

Largest torque that the clutch can transmit. This value corresponds to
a nonslip engaged configuration. If the torque transmitted between the
ring and the hub exceeds this value, the two components begin to slip
with respect to each other. This torque determines the static friction
limit in the friction clutch approximation.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Omit`.

### **Temperature vector** — Temperature `[280, 300, 320]` `K` (default) | vector

Temperature values. The minimum number of values depends on the
interpolation method that you select. For linear interpolation, provide
at least two values per dimension. For smooth interpolation, provide at
least three values per dimension. The values in the vector must increase
from left to right.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

### **Maximum transmitted torque vector** — Maximum transmitted torque `[1000, 1050, 1000]` `N*m` (default) | vector

Maximum transmitted torque for a given temperature in the
**Temperature vector** parameter.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation method for approximating the output value when the input
value is between two consecutive grid points:

- `Linear` — Select this option for the
  best performance.
- `Smooth` — Select this option to
  produce a continuous curve with continuous first-order
  derivatives.

For more information on interpolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

### **Extrapolation method** — Extrapolation method `Linear` (default) | `Nearest` | `Error`

Extrapolation method for determining the output value when the input
value is outside the range specified in the argument list:

- `Linear` — Select this option to
  produce a curve with continuous first-order derivatives in
  the extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Select this option to
  produce an extrapolation that does not go above the highest
  point in the data or below the lowest point in the
  data.
- `Error` — Select this option to
  avoid going into the extrapolation mode. If the input signal
  is outside the range of the table, the simulation stops and
  generates an error.

For more information on extrapolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

### **Number of teeth** — Number of ring or hub teeth `6` (default) | positive nonzero scalar integer

Total number of teeth in the ring or the hub. The two components have
equal tooth numbers. The value must be greater than or equal to
one.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic with
backlash`.

### **Rotational backlash** — Rotational backlash `10` `deg` (default) | positive scalar

Allowable angular motion, or play, between the ring and hub teeth when
the clutch is engaged. The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic with
backlash`.

### **Torsional stiffness** — Torsional stiffness `10e6` `N*m/rad` (default) | positive scalar

Linear torsional stiffness coefficient at the contact interface
between the ring and hub teeth. This coefficient characterizes the
restoring component of the contact force between the two sets of teeth.
Greater stiffness values correspond to greater contact forces. The value
must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic with
backlash`.

### **Torsional damping** — Torsional damping `100` `N*m*s/rad` (default) | positive scalar

Linear torsional damping coefficient at the contact interface between
the ring and hub teeth. This coefficient characterizes the dissipative
component of the contact force between the two sets of teeth. Greater
damping values correspond to greater energy dissipation during contact.
The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic with
backlash`.

### Shift Linkage

### **Abstract shift linkage control** — Two-mode linkage control option `Logic-controlled` (default) | `Physical signal`

Abstract shift linkage control to use for two-mode torque transmission.

- `Logic-controlled` — Input the
  shift linkage as a Boolean operator using the physical
  signal port **S**.
- `Physical signal` — Input shift
  linkage position directly through the physical signal port
  **S**.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Two-mode`.

### **Shift linkage control** — Shift linkage control port `Physical signal` (default) | `Conserving port`

Port type for shift linkage control:

- `Physical signal` — Input shift
  linkage position directly through the physical signal port,
  **S**.
- `Conserving port` — Input the
  shift linkage position dynamically through the translational
  conserving port, **S**.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash`.

### **Tooth height** — Tooth height `10` `mm` (default) | positive scalar

Distance between the base and crest of a tooth. The ring and hub teeth
share the same height. The tooth height and the ring-hub clearance when
fully disengaged determine the maximum travel span of the shift linkage.
The value of this parameter must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to:

- `Friction clutch approximation - Suitable
  for HIL and linearization`
- `Dynamic with
  backlash`
- `Dynamic modal`
- `Two-mode`, and set
  **Abstract shift linkage
  control** to `Physical
  signal`

### **Ring-hub clearance when disengaged** — Ring-hub clearance when disengaged `3` `mm` (default) | positive scalar

Maximum open gap between the ring and hub tooth crests along the shift
linkage translation axis. This gap corresponds to the fully disengaged
clutch state. The tooth height and the ring-hub clearance when fully
disengaged determine the maximum travel span of the shift linkage. The
value of this parameter must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to:

- `Friction clutch approximation - Suitable
  for HIL and linearization`
- `Dynamic with
  backlash`
- `Dynamic modal`
- `Two-mode`, and set
  **Abstract shift linkage
  control** to `Physical
  signal`

### **Hard stop at back of shift linkage** — Hard stop backing option `on` (default) | `off`

Whether to enable a hard stop when the shift linkage travels beyond
the fully disengaged position.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to:

- `Dynamic modal`
- `Friction clutch approximation - Suitable
  for HIL and linearization`, and set
  **Shift linkage control** to
  `Conserving port`
- `Dynamic with backlash` and
  set **Shift linkage control** to
  `Conserving port`

### **Ring stop stiffness** — Ring stop stiffness `10e5` `N/m` (default) | positive scalar

Linear stiffness coefficient of the ring end stop. This coefficient
characterizes the restoring component of the contact force that resists
translational motion past the end stops. Greater stiffness values
correspond to greater contact forces and a smaller end stop compliance.
The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash` and set
**Shift linkage control** to
`Conserving port`.

### **Ring stop damping** — Ring stop damping `1e3` `N*s/m` (default) | nonegative scalar

Linear damping coefficient of the ring end stop. This coefficient
characterizes the dissipative component of the contact force that
resists translational motion past the end stops. Greater damping values
correspond to greater energy dissipation during contact. The value must
be greater than or equal to zero

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash` and set
**Shift linkage control** to
`Conserving port`.

### **Shift linkage viscous friction coefficient** — Shift linkage viscous friction coefficient `100` `N*s/m` (default) | positive scalar

Linear damping coefficient acting on the shift linkage. This
coefficient characterizes the dissipative force that resists shift
linkage motion due to viscous damping. Greater coefficient values
correspond to greater energy dissipation during shift linkage motion.
The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash` and set
**Shift linkage control** to
`Conserving port`.

### **Tooth-tooth friction coefficient** — Tooth-tooth contact kinetic friction coefficient `0.05` (default) | positive scalar

Kinetic friction coefficient at the contact interface between the ring
and hub teeth. This coefficient characterizes the dissipative force that
resists shift linkage motion due to tooth-to-tooth contact during clutch
engagement and disengagement.

Greater coefficient values correspond to greater energy dissipation
during shift linkage motion. The value must be greater than zero.

#### Dependencies

To enable this parameter, set:

- **Torque transmission model** to
  `Dynamic with
  backlash`
- **Shift linkage control** to
  `Conserving port`

### **Shift linkage engaged friction coefficient** — Engaged friction coefficient `100` `N*s/m` (default) | positive scalar

Friction coefficient at the shift linkage when the ring and hub are
engaged. This value is the friction between the shift linkage and its
support.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### **Shift linkage disengaged friction coefficient** — Disengaged friction coefficient `50` `N*s/m` (default) | positive scalar

Friction coefficient at the shift linkage when the ring and hub are
disengaged. This value is the friction between the shift linkage and its
support.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### **Static contact speed threshold** — Static contact speed threshold `0.1` `m/s` (default) | positive scalar

t

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### **Static contact release force threshold** — Release force threshold `0.001` `N` (default) | positive scalar

Force threshold above which the ring and hub can unlock and
disengage.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### Engagement Conditions

### **Linkage travel direction** — Engagement condition travel direction `Positive shift linkage displacement engages clutch` (default) | `Negative shift linkage displacement engages clutch`

Direction the shift linkage must travel in to engage the
clutch.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to:

- `Friction clutch approximation - Suitable
  for HIL and linearization`
- `Dynamic with
  backlash`
- `Dynamic modal`

### **Maximum engagement speed** — Engagement speed upper velocity threshold `inf` (default) | positive scalar

Relative angular velocity between the ring and the hub above which the
clutch cannot engage. The value is specific to the specific gearbox or
transmission. Minimizing the value helps avoid high dynamic impact
during engagement. The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization` or
`Dynamic with backlash`.

### **Tooth overlap to engage** — Tooth overlap engagement threshold `3` `mm` (default) | positive scalar

Overlap length between the ring and hub teeth along the common
longitudinal axis. The clutch engages when the tooth overlap is greater
than this value. The clutch remains disengaged until the meshing gear
teeth overlap by at least this length. The value must be greater than
zero.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to

- `Dynamic modal`
- `Friction clutch approximation - Suitable
  for HIL and linearization`, and set
  **Shift linkage control** to
  `Conserving port`
- `Dynamic with backlash` and
  set **Shift linkage control** to
  `Conserving port`

### **Engagement block stiffness** — Engagement blocking stiffness coefficient `10e6` `N/m` (default) | positive scalar

Stiffness coefficient during engagement blocking.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### **Engagement block damping** — Engagement blocking damping coefficient `300` `N*s/m` (default) | positive scalar

Damping coefficient when during engagement blocking.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic
modal`.

### Initial Conditions

### **Clutch locked** — Initial clutch state `off` (default) | `on`

Clutch state at the start of simulation:

- `off` — Clutch transmits zero
  torque between the ring and the hub.
- `on` — Clutch transmits torque
  between the ring and the hub.

### **Initial shift linkage position** — Initial shift linkage position `0` `mm` (default) | scalar

Shift linkage position at simulation time zero. The clutch is
disengaged when this value is between zero and the sum of the ring-hub
clearance.

#### Dependencies

To enable this parameter, set:

- **Torque transmission model** to
  `Dynamic with
  backlash`
- **Thermal model** to
  `Omit`
- **Shift linkage control** to
  `Conserving port`

### **Initial ring-hub offset angle** — Initial ring-hub offset angle `0` `deg` (default) | scalar

Rotation angle between the ring and the hub at simulation time zero.
This angle determines whether the ring and hub teeth can engage. The
initial offset angle must satisfy these conditions:

- If the clutch initial state is disengaged, the initial
  offset angle must fall in the range

  −180°N≤ϕ0≤+180°N,

  where *N* is the number
  of teeth present in the ring or the hub. The two components
  contain the same number of teeth.
- If the clutch initial state is engaged, the initial offset
  angle must fall in the range

  −δ2≤ϕ0≤+δ2,

  where *δ* is the
  backlash angle between the ring and hub teeth.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Dynamic with
backlash`, and set **Thermal
port** to `Omit`.

### Thermal Port

### **Thermal mass** — Resistance to temperature change `50` `kJ/K` (default) | scalar

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

Component temperature at the start of simulation. The initial
temperature alters the component efficiency by adjusting the starting
meshing or friction losses.

#### Dependencies

To enable this parameter, set **Torque transmission
model** to `Friction clutch approximation
- Suitable for HIL and linearization`, and set
**Thermal port** to
`Model`.

## Libraries

Simscape / Driveline / Clutches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2024a: Capture effects of engagement blocking due to speed differentials

You can now capture the effects of engagement blocking due to the speed
differential at the system level when **Torque transmission
model** is `Dynamic modal`.

### R2023b: Two-mode support

The Dog Clutch block can now model abstract
behavior when **Torque transmission model** is
`Two-mode`. Use this option for system-level design or
where speed is a priority over precision.

## Description

Clutch with toothed plates that engage when plate teeth become enmeshed

The Dog Clutch block represents a nonslip clutch that
uses the positive engagement of interlocking teeth to transfer torque between drive
shafts. Dog clutches are common in applications that require high-speed and frequent
gear shifts. Dog clutches are typical for motorcycle manual transmissions, and some
industrial machinery.

The ring and hub are the primary components of a dog clutch. The input shaft turns the
ring, which has slots or teeth. The hub connects to an output shaft that has protruding
"dogs" that fit into the slots of the ring. When you shift the transmission,the dogs and
slots engage and lock the two components and transmitting power. You shift again to
disengage the clutch, which causes the dogs to disengage from the slots and allows the
transmission to spin freely. The ring and the hub spin together as a unit.

To control engagement, the dog clutch contains a shift linkage that governs the
position of the ring with respect to the hub. You can choose to control the shift
linkage with a physical signal or a mechanical translational conserving port by using
the **Torque transmission model** parameter. Choose the parameter
setting according to your performance, fidelity, and the clutch behavior:

- `Two-mode` — Fully abstracted torque transmission
  model based on mode charts. This setting is fast enough for real-time
  simulation and does not require knowledge of the clutch dimensions. You can
  control the shift linkage only with a physical or logic-controlled
  signal.
- `Friction clutch approximation - Suitable for HIL and
  linearization` — Medium- to high-fidelity composite
  implementation of the Fundamental Friction Clutch block.
  This setting supports thermal modeling. You can control the shift linkage
  with either a physical signal or a mechanical translational conserving
  port.
- `Dynamic with backlash` — High-fidelity clutch
  engagement model that accounts for phenomena such as backlash, torsional
  compliance, and contact forces between the ring and hub teeth.
- `Dynamic modal` — Medium to high-fidelity mode
  chart implementation that simulates engagement blocking and determines the
  shift linkage position from a mechanical translational conserving port.

Moving the ring toward the hub so that the teeth interlock changes the clutch state to
engaged. Tooth overlap must exceed a minimum value for engagement. Moving the ring in
reverse so that the two sets of teeth no longer interlock changes the clutch state back
to disengaged. Port **S** specifies the shift linkage position. When
the clutch is fully disengaged, the shift linkage position is zero. When the clutch is
fully engaged, the shift linkage position equals the sum of the tooth height and the
ring-hub clearance of the fully disengaged state,

z=h+zGap,

where:

- *z* is the shift linkage position.
- *h* is the tooth height.
- *zGap* is the ring hub clearance
  when disengaged.

The figure shows side and front views of the dog clutch and some of its
relevant variables.

### Torque Transmission Models

You can choose from these torque transmission models.

**Two-Mode**

To simulate an abstracted dog clutch, set **Torque transmission model** to `Two-mode`. The two-mode torque transmission model uses mode charts to control whether the clutch is engaged or disengaged. You can control the shift linkage position using logic-based commands or a linkage position physical signal. When you use logic-based commands, `false` at port **X** represents a disengaged clutch, and `true` represents an engaged clutch.

**Friction Clutch Approximate Model**

When you set **Torque transmission model** to `Friction clutch approximation - Suitable for HIL and`, the block treats the clutch engagement as a friction phenomenon between the ring and the hub. This setting is better suited for linearization, fixed-step simulation, and hardware-in-loop (HIL) simulation. The block uses a composite implementation of the Fundamental Friction Clutch block.

When you use this setting, the clutch has three possible configurations: disengaged, engaged, and locked. When disengaged, the contact force between the ring and the hub is zero. This force remains zero until the shift linkage reaches the minimum position for engagement.

When the ring-hub tooth overlap, *h*, exceeds the minimum value for engagement, the contact force between the two components begins to increase linearly with the shift linkage position, *z*.

At full engagement, the contact force reaches its maximum value and the clutch state switches to locked. In this state, the ring and the hub spin as a unit without slip. To unlock the clutch, the transmitted torque must exceed the value of the **Maximum transmitted torque** parameter.

**Dynamic with Backlash**

When you set **Torque transmission model** to `Dynamic with backlash`, the block simulates clutch phenomena such as backlash, torsional compliance, and contact forces between ring and hub teeth. This model provides greater accuracy than the friction clutch approximation.

When you use this setting, the clutch has two possible configurations: disengaged and engaged. When disengaged, the contact force between the ring and the hub is zero. This force remains zero until the shift linkage reaches the minimum position for engagement.

When the ring-hub tooth overlap, *h*, exceeds the engagement threshold value,
the clutch transmits torque. This torque is the sum of torsional spring and damper
components, including backlash between the ring and hub teeth, such thatTC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2,where:

- *kRH* is the torsional stiffness
  of the ring-hub coupling.
- *ϕ* is the relative angle, about the common rotation
  axis, between the ring and the hub.
- *δ* is the backlash between ring and hub teeth.
- *ω* is the relative angular velocity between the ring and
  the hub. This variable describes how fast the two components slip past each
  other.

Compliant end stops limit the translational motion of the clutch shift linkage and the ring. The compliance model treats the end stops as linear spring-damper sets. The location of the end stops depends on the relative angle and angular velocity between the ring and hub teeth:

- If the teeth align and the relative angular velocity is smaller than the maximum value for clutch engagement, the end stop location is the sum of the ring-hub clearance when fully disengaged and the tooth height. The clutch can engage in this end stop position.
- If the teeth do not align or the relative angular velocity exceeds the maximum value for clutch engagement, the end-stop location is set to prevent the ring from engaging the hub. The clutch does not engage in this end stop position.

Translational friction opposes shift linkage and ring motion. This friction is the sum of
Coulomb and viscous components, such thatFZ=−kK·FN·tanh(4vvth)−μTv,where:

- *FZ* is the net translational
  friction force acting on the shift linkage and ring.
- *kK* is the kinetic friction
  coefficient between ring and hub teeth.
- *FN* is the normal force between
  ring and hub teeth, where *FN* =
  *TC*/*Rm*.
- *v* is the translational velocity of the shift linkage
  and the ring.
- *vth* is the translational
  velocity threshold. Below this threshold, a hyperbolic tangent function
  smooths the Coulomb friction force to zero as the shift linkage and ring
  velocity tends to zero.
- *μT* is the viscous damping
  coefficient acting on the shift linkage and the ring.

**Dynamic Modal**

When you set **Torque transmission model** to `Dynamic
modal`, the block determines the discrete clutch modal behavior by
taking the shift linkage position from the mechanical translational conserving port
**S**. This setting captures more complex clutch dynamics than the
`Two-mode` parameterization and is faster than the
`Friction clutch approximation` and `Dynamic
with backlash` settings.

You can use the `Dynamic modal` setting to simulate
engagement blocking when the speed difference is too large for the clutch plates to
engage. The block represents engagement blocking as a spring-damper system where you can
parameterize the spring and damping coefficients. The engagement modes overlap, which
prevents the mode from changing until the shift linkage position is beyond the
engagement overlap region. You define the engagement overlap region using the
**Tooth overlap to engage** parameter.

Diagram depicting the mode transitions between engaged and disengage. The z variable represents the shift linkage position. The Engaged and Disengaged modal regions overlap, which attenuates the mode transition rate.

The linkage position constrains are:

- *z* is the shift linkage position at port
  **S**.
- *h* is the **Tooth height**
  parameter.
- *zGap* is the **Ring hub
  clearance when disengaged** parameter.
- *zOverlap* is the **Tooth
  overlap to engage** parameter.
- *ωthr* is the
  **Engagement speed threshold** parameter.

The engagement mode positions are:

- *z* = 0 — The clutch is fully disengaged.
- 0 < *z* <
  *zGap* — The clutch is disengaged when the shift linkage position
  is in the region defined by *zGap*.
  The clutch can transition from disengaged to engaged at *x* =
  *zGap* +
  *zOverlap*.
- *zGap* <
  *z* < *h* — The clutch is engaged when *z* is in
  the region defined by *h*. The clutch can transition from
  engaged to disengaged when *z* =
  *zGap*.
- *z* =
  *zGap* +
  *h* — The clutch is fully engaged.
- *z* =
  *zGap* +
  *zOverlap* — When *z* is in the engagement overlap
  region, the clutch engages only when the speed difference is less than the
  value of the *ωthr*
  parameter.

### Rotational Power Dissipation

When the clutch slips under an applied torque, it dissipates power. The power loss
equals the product of the slip angular velocity and the contact torque between the
ring and the hub, such that

Ploss=ω · TC,

where:

- *Ploss* is the dissipated
  power due to slipping.
- *TC* is the kinetic contact
  torque.

### Thermal Modeling

When you set **Torque transmission model** to
`Friction clutch approximation - Suitable for HIL and
linearization`, you can model the effects of heat flow and
temperature change by using the optional thermal conserving port,
**T**.

### Linearization

To optimize your model for linearization, use the **Clutch** > **Torque transmission model** parameter default setting, `Friction clutch approximation -
Suitable for HIL and linearization`.

### Hardware-in-the-Loop Simulation

For optimal simulation performance, use the **Clutch** > **Torque transmission model** parameter default setting, `Friction clutch approximation -
Suitable for HIL and linearization`.
