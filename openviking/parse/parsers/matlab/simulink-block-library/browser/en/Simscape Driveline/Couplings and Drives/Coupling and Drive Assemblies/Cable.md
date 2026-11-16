---
type: simulink-block
title: 'Cable'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Coupling and Drive Assemblies'
documentation_page: 'cable'
documentation_source_path: 'ref/cable.html'
language: en
---

# Cable

## Ports

### Input

### **L** — Length physical signal

Physical signal input port associated with the length between the
instantaneous contact points at either end of the cable segment.

#### Dependencies

To enable this port, select **Model variable rest
length**.
### Conserving

### **B** — Base contact location of cable mechanical translational

Mechanical translational conserving port associated with the base
instantaneous contact location of the cable segment.

### **F** — Follower contact location of cable mechanical translational

Mechanical translational conserving port associated with the follower
instantaneous contact location of the cable segment.

## Parameters

### **Model variable rest length** — Variable rest length option `off` (default) | `on`

Whether to model variable rest length. Variable length affects stiffness
and damping. When you select **Model mass**, variable
length affects the mass of the cable. When you select **Model
gravity**, variable length affects the force acting on the
cable due to gravity.

### **Minimum rest length** — Minimum rest length `0.01` `m` (default) | positive scalar

Minimum rest length of the cable. The value of the **Minimum rest
length** parameter represents the lower-bound of the cable
length when simulating variable rest length. The block smoothly transitions
to and from this value and saturates inputs below this value.

#### Dependencies

To enable this parameter, select **Model variable rest
length**.

### **Stretch parameterization** — Constant or tabulated parameterization `Constant stiffness and damping` (default) | `Tabulated stiffness and damping`

Whether to parameterize the cable using constants or tabulated stiffness
and damping values.

### **Rigidity** — Cable rigidity `1000` `N` (default) | positive scalar

Effective rigidity of the cable segment. The value of this parameter is
equivalent to the axial stiffness when the cable stretch motion is purely
longitudinal.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and set **Stretch
parameterization** to `Constant stiffness and
damping`.

### **Stiffness** — Resistance to deformation `1000` `N/m` (default) | positive scalar

Effective translational spring stiffness of the cable segment.

#### Dependencies

To enable this parameter, clear **Model variable rest
length** and set **Stretch
parameterization** to `Constant stiffness and
damping`.

### **Damping** — Tendency to dissipate energy `100` `N/(m/s)` (default) | positive scalar

Effective translational damping of the cable segment. When you select the
**Model slack** parameter and xs<0, the block ignores damping.

#### Dependencies

To enable this parameter, set **Stretch parameterization** to
`Constant stiffness and damping`.

### **Stretch vector** — Stretch displacement `[.1, .2, .5, 1]` `m` (default) | vector

Stretch displacement of a given point along the cable. The vector must have a minimum
length of two and must be strictly increasing. The block determines the
displacement as a function of the cable velocity.

#### Dependencies

To enable this parameter, clear **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Stiffness vector** — Tabular energy dissipation `[500, 520, 540, 540]` `N/m` (default) | vector of nonnegative values

Cable stiffness for a given stretch displacement. The elements in this
parameter correspond one-to-one with the **Stretch
vector** parameter.

#### Dependencies

To enable this parameter, clear **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Damping vector** — Tabular damping `[50, 60, 80, 80]` `N*s/m` (default) | vector of nonnegative values

Cable damping for a given stretch displacement. The elements in this
parameter correspond one-to-one with the **Stretch
vector** parameter.

#### Dependencies

To enable this parameter, clear **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Rest length vector, Lr** — Tabulated rest length `[.25, .5, 1]` `m` (default) | vector of length *M*

Vector of rest length values,
*LRest*.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Stretch per rest length vector, s/Lr** — Tabulated stretch per rest length `[.01, .02, .1, .25]` (default) | vector of length *N*

Vector of stretch values for a given rest length,
*s/LRest*. The elements
correspond one-to-one with the **Rest length vector, Lr**
parameter.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Stiffness table (Lr, s/Lr)** — Tabulated stiffness `[500, 600, 600, 500; 250, 300, 300, 250; 125, 150, 150, 125]` `N/m` (default) | *M*x*N* matrix

Table of stiffness values for a given rest length,
*LRest*, and stretch,
*s/LRest*.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Damping table (Lr, s/Lr)** — Tabulated damping `[50, 60, 60, 50; 50, 60, 60, 50; 50, 60, 60, 50]` `N*s/m` (default) | *M*x*N* matrix

Table of damping values for a given rest length,
*LRest*, and stretch,
*s/LRest*.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and set **Stretch
parameterization** to `Tabulated stiffness and
damping`.

### **Model slack** — Slack parameterization option `off` (default) | `on`

Whether to model slack. The block does not transfer spring force when the
cable is not in tension. When you select this parameter, the
Cable block is equivalent to a
Translational Hard Stop block with
**Upper bound** set to `0` and
**Lower bound** set to `-inf`. For
more information, see Translational Hard Stop.

### **Slack model** — Slack transition behavior `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | ...

Stiffness and rebound options for the slack model. The slack model is
equivalent to a Translational Hard Stop
block. You can choose from these options:

- `Stiffness and damping applied smoothly through
  transition region, damped rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`

#### Dependencies

To enable this parameter, select **Model
slack**.

### **Linear density** — Linear density `0.2` `kg/m` (default) | positive scalar

Linear density of the cable segment, *μ*.

#### Dependencies

To enable this parameter, select **Model variable rest
length** and select either **Model
mass** or **Model slack**.

### **Transition region** — Region of partial slack effects `0.1` `mm` (default) | positive scalar

Distance from full compression or full extension where the effects of
stiffness and damping are partially applied. When you set **Slack
model** to `Stiffness and damping applied smoothly
through transition region, damped rebound`, the block
smoothly transitions the onset of stiffness and damping as the spring
approaches full extension or full compression.

#### Dependencies

To enable this parameter, select **Model variable rest length** or
clear **Model variable rest length** and select
**Model slack** and set **Slack
model** to `Stiffness and damping applied
smoothly through transition region`.

### **Model mass** — Mass parameterization option `Off` (default) | `On`

Whether to model mass. When you select **Model mass**, the block
considers the mass of the cable segment that it represents. Including mass
can help initialize some models but can also be more computationally
costly.

#### Dependencies

To enable this parameter, clear the **Model slack**
parameter.

### **Mass** — Cable segment mass `1` `kg` (default) | positive scalar

Mass of the cable segment that the block represents. The block distributes
half of the total mass to each end of the cable.

#### Dependencies

To enable this parameter, clear **Model variable rest
length**select **Model mass** or
**Model slack**.

### **Model gravity** — Gravity option `off` (default) | `on`

Whether to model gravity.

#### Dependencies

To enable this parameter, select **Model mass** or **Model
slack**.

### **Gravitational acceleration, g** — Gravitational acceleration `9.81` `m/s^2` (default) | positive scalar

Acceleration due to gravity. You can specify the direction of positive
acceleration with the **Angle of gravity relative to positive
direction, θ** parameter.

#### Dependencies

To enable this parameter, select **Model mass** or **Model
slack** and **Model gravity**.

### **Angle of gravity relative to positive direction, θ** — Positive gravity angle `0` `deg` (default) | scalar

Angle at which the value of the **Gravitational acceleration,
g** parameter is positive, *θ*. A value of
`0` represents downward acceleration.

#### Dependencies

To enable this parameter, select **Model mass** or
**Model slack** and **Model
gravity**.

### **Warn if cable loses tension** — Lost tension warning option `off` (default) | `on`

Whether to generate a warning when the cable segment is no longer in tension. Use this
parameter to identify if your system experiences instances of slack.

### **Error if cable exceeds maximum tension** — Maximum tension error option `off` (default) | `on`

Whether to generate an error when the cable segment exceeds the value of
the **Cable maximum tension** parameter.

### **Cable maximum tension** — Maximum allowable tension force in cable segment `1e5` `N` (default) | positive scalar

Tension value error target. When the tension in the cable segment exceeds
this parameter, the block generates an error.

#### Dependencies

To enable this parameter, select **Error if cable exceeds
maximum tension**.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2024b: Variable rest length

Represent a connection with variable rest length. When you select **Model variable
rest length**, the block generates results with higher accuracy for
travelling pulley applications.

Additionally, you can now include the force of gravity. To enable the
**Model gravity** parameter, select the **Model
mass** parameter.

### R2023b: Tabular stiffness and damping

You can set the new **Stretch parameterization** parameter to
`Tabulated` to specify tabulated data for the cable
behavior. The associated **Stretch vector**, **Stiffness
vector**, and **Damping vector** parameters are
also new. These parameters have been updated to support block
enhancements:

| Old Parameter | New Parameter |
| --- | --- |
| **Rope model** | **Model slack** |
| **Maximum tension** | **Specify maximum tension** |
| **Tension warning** | **Warn if cable loses tension** |

### R2023b: Name change

The Rope block was renamed to the
Cable block.

## Description

Cable connection that enables tension transfer

The Cable block represents an element that transfers tension
between two contact points. You can treat the block as an arbitrary tension transfer
device to simulate a variety of situations, including pulley networks, cable drives, and
serpentine belts. You can choose whether the cable exhibits slack upon loss of tension.
The block has a base port, **B**, and a follower port,
**F**. The cable stretches in tension when the base port leads the
follower port.

The block considers only the longitudinal translational motion and force exerted at the
cable ends. The first figure shows a Translational Spring
and Translational Damper block in parallel, which is
functionally equivalent to the Cable block with zero
mass. The second figure shows the same spring and damper blocks but with an additional
Mass block on either side, which is functionally
equivalent to the Cable block with a nonzero mass.

Parallel spring and damper with an in port and an out port.Parallel spring and damper with an in port, an out port, and mass at both ends.

These figures only apply when the cable is in tension.

**Tip**

Confirm that your model operates as expected before you select the **Model
slack** and **Model mass** parameters. Verify that
the **B** and **F** ports are oriented properly by
viewing the tension plots of each cable in the **Simscape Results
Viewer** and looking for unexpected negative values.

The Cable block can act as a rope, belt, cable, or any other
device that has tensile strength and transmits tension between two contact points. A
contact point can be a pulley, a drum, or an ideal source. You can use the
**Stretch parameterization** parameter to control whether the
block acts as a constant or tabulated connection.

You can use this block to model stationary or travelling pulley networks. You can drive the
Cable block with sources like the
Ideal Translational Velocity Source block, or a
Rope Drum block attached to an Ideal
Force Source block.

For greater fidelity or numerical stability, you can choose to model the effect of mass on
the system. When you select **Model mass**, the block distributes
half of the total mass to either end of the cable. Adding a small amount of mass can
improve the initialization of your model. You can also specify the initial conditions of
the cable. If you choose to simulate slack, the block does not apply stiffness and
damping when the cable is in slack. Selecting **Model slack** or
**Model mass** enables the **Model gravity**
parameter. Including the effect of gravity improves accuracy for heavy cable
segments.

For cable segments with variable rest length, use the **Model variable rest
length** parameter to improve results for travelling pulley applications.
The block supports these examples of variable rest length scenarios:

- One end of the cable is stationary, and the other end connects to a
  travelling pulley.
- A cable is connected to a travelling pulley at each end.

You must use the correct orientation for the block when you select
**Model variable rest length**. To learn more, see Best Practices for Modeling Pulley Networks.

### Equations

The block equations refer to these quantities:

- *F* is the tension force, where F=FB=−FF.
- *xs* is the deformation due to
  stretching, which you specify by using the **Stretch**
  variable. Simscape Results Explorer displays this quantity as
  `s`.
- *K* is the spring stiffness coefficient. K(xs)=0 when you select **Model slack** and xs<0.
- *D* is the damping coefficient.
- *m* is the total mass, which you specify by using the
  **Mass** parameter. The block distributes half of
  the total mass to each end.
- *xB* is the position of the
  base node.
- *xF* is the position of the
  follower node.
- *ẋs* is the stretch
  velocity.
- *LRest* is the rest length of
  the cable segment.
- *Lmin* is the
  **Minimum rest length** parameter.
- *μ* is the **Linear density**
  parameter.

The Cable block responds to external load at the port
**B** as

FB(xs(t),t)=m2x¨B(t)+Dx˙s(t)+Kxs(t),

and port **F** as,

FF(xs(t),t)=m2x¨F(t)−Dx˙s(t)−Kxs(t),

where xs(t)=xB(t)−xF(t). The definitions of *D* and *V*
depend on the parameterization.

- *D* and *K* are constant when you
  set **Stretch parameterization** to
  `Constant stiffness and damping` and clear
  **Model variable rest length**.
- *D* is constant and *K =
  EA/LRest* when you set
  **Stretch parameterization** to
  `Constant stiffness and damping` and select
  **Model variable rest length**, where EA is the
  value of the **Rigidity** parameter.
- *D = TLU(xs)* and *K =
  TLU(xs)* when you set
  **Stretch parameterization** to
  `Tabulated stiffness and damping` and clear
  **Model variable rest length**.
- *D = TLU(xs,
  xs/LRest)*
  and *K = TLU(LRest,
  xs/LRest)*
  when you set **Stretch parameterization** to
  `Tabulated stiffness and damping` and
  select **Model variable rest length**.

The block overrides the value of *K* to
`0` when you select **Model slack** and
*xs < 0*.

The forces vary as functions of time and the stretch deformation,
*xs*. *K* and
*B* are functions of
*xs*, such that K(xs)=K when there is no slack or you are not simulating slack. Otherwise, K(xs)=0 when slack occurs at xs<0. The same logic applies for *B*. The terms that
involve mass only apply when you select the **Model mass**
parameter.

When you select **Model variable rest length**, takes the length as an
input at port **L**. To input the rest length, use a
Translational Motion Sensor block to determine
the motion of the cable segment. The block saturates the rest length such that

Lrest=max(L−xs,Lmin)

When you select **Model variable rest length**
and **Model mass**, the block uses the value of the
**Linear density** parameter to determine the mass of the
cable segment such that

m= μLRestfMass,B=m2v˙BfMass,F=m2v˙F

When you select **Model variable rest
length**, **Model mass**, and **Model
gravity**, the block applies gravity to each end of the cable segment,
such that

fGravity=mgcos(θ)fGravity,B=fGravity2fGravity,F=fGravity2

Positive cable velocity acts from port **B** to port
**F**. Positive gravity acts downward according to the cable orientation.Gravity applies to the block depending on the orientation of the B and F ports.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Limitations

When you select the **Model mass** and **Model variable rest
length** parameters, the block uses a quasi-static model to calculate
force due to mass. The block does not account for the rate of change in the cable
segment mass. You can use a Variable Mass block to
include the effect of the varying mass on the tension due to mass.
