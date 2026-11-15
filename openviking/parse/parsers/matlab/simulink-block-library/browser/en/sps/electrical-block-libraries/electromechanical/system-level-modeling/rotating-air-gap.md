---
type: simulink-block
title: 'Rotating Air Gap'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / System-Level Modeling'
documentation_page: 'rotatingairgap'
documentation_source_path: 'ref/rotatingairgap.html'
language: en
---

# Rotating Air Gap

## Ports

### Conserving

### **N** — Magnetic stator connection magnetic

Magnetic conserving port associated with the stator.

### **S** — Magnetic rotor connection magnetic

Magnetic conserving port associated with the rotor.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor case.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor rotor.

## Parameters

### Main

### **Number of rotor pole pairs** — Rotor pole pairs `5` (default) | positive scalar

Number of the pole pairs of the rotor. This parameter must be equal to
or greater than `1` and less than the value of the
**Number of stator teeth** parameter.

### **Number of stator teeth** — Number of stator teeth `9` (default) | positive scalar

Number of teeth of the stator. This parameter must be equal to or
greater than `2`.

### **Stator tooth reference index** — Stator tooth reference index `1` (default) | positive scalar

Reference index of the stator tooth of the motor. This parameter must
be between `1` and the value of the **Number of
stator teeth** parameter.

For example, if you want to model a motor with nine stator poles,
create nine copies of this block and set the **Stator tooth
reference index** parameter for each of the Rotating Air
Gap blocks to `1`, `2`,
`3`, `4`, `5`,
`6`, `7`, `8`,
and `9`, respectively.

### **Peak magnet flux density** — Peak flux density of magnet rotor `0.4` `T` (default) | positive scalar

Peak flux density associated with the permanent magnet rotor. The flux
density is sinusoidal with the rotor angle.

### **Permanent magnet length (in direction of flux)** — Magnet length in radial machine direction `5` `mm` (default) | positive scalar

Length of the magnet in the radial machine direction or, equivalently,
in the direction of the magnetic flux. This parameter must be less than
the value of the **Rotor radius** parameter.

### **Permanent magnet relative permeability** — Permanent magnet relative permeability `1.05` (default) | scalar

Relative permeability of the permanent magnets. Typically, you should
set this value a little greater than `1` to reflect
that the magnetic dipoles are already aligned in a permanent
magnet.

### **Air gap** — Air gap in radial direction `1` `mm` (default) | positive scalar

Length of the air gap in the radial direction.

### **Rotor radius** — Rotor radius `65` `mm` (default) | positive scalar

Radius of the rotor.

### **Tooth depth (in direction of shaft)** — Stator tooth depth `50` `mm` (default) | positive scalar

Length of the stator tooth in the direction of the rotating
shaft.

### Faults

### **Enable faults** — Fault option `off` (default) | `on`

Whether to simulate the effect of a degraded rotor magnet
strength.

### **Flux multipliers for faulted rotor poles** — Multipliers to reduce rotor pole flux `ones(1,10)` (default) | vector

Multipliers used to reduce the rotor pole magnetic density when
faulted. The value of this parameter must be a vector of length equal to
twice the value of the **Number of rotor pole pairs**
parameter. Each element of the vector corresponds to one rotor
pole.

The default value is equal to `ones(1,10)` and
results in the same behavior as the unfaulted scenario.

#### Dependencies

To enable this parameter, select the **Enable
faults** parameter.

### **Duration of transition to faulted** — Amount of time after which block fully faults `100` `s` (default) | positive scalar

Amount of time after which the block applies the full effect of the
faulted multipliers on the peak magnet flux density of each rotor pole.
When the block enters the fault state, the peak magnet flux densities of
each rotor pole are gradually modified using the faulted
multipliers.

#### Dependencies

To enable this parameter, select the **Enable
faults** parameter.

### **Simulation time for fault event** — Simulation time at which block faults `1` `s` (default) | positive scalar

Simulation time at which the block starts to apply the faulted
multipliers for the peak magnet flux density on each rotor pole.

#### Dependencies

To enable this parameter, select the **Enable
faults** parameter.

## Libraries

Simscape / Electrical / Electromechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Air gap between stator tooth and rotating permanent magnet rotor

The Rotating Air Gap block models an air gap between a
stator tooth and a rotating permanent magnet rotor. This block assumes that the rotor
magnets are surface mounted and that the associated induced voltage is
sinusoidal.

This figure shows the relationship between the parameters of the Rotating Air
Gap block and their physical values inside a permanent magnet motor

where:

- *r* is the value of the **Rotor radius**
  parameter.
- *g* is the value of the **Air gap**
  parameter.
- *lm* is the value of the
  **Permanent magnet length (in direction of flux)**
  parameter.
- *l* is the value of the **Tooth depth (in
  direction of shaft)** parameter.

The rotor circumference is equal to 2πr. Then, the width of a permanent magnet on the rotor is equal to 2πr2N, where *N* is the **Number of rotor pole
pairs**.

If the rotor angle is zero, specified by the **Rotor angle** variable in
the **Variables** section, then the rotor magnet perfectly aligns with
the middle of the first stator tooth. The permanent magnet is then orientated to oppose
the flux flow from port **N** to port **S**.

Use this block to create a magnetic representation of a permanent magnet synchronous motor
(PMSM). For example, if you want to model a motor with nine stator poles, create nine
copies of this block and set each of the **Stator tooth reference
index** parameters to `1`, `2`,
`3`, `4`, `5`,
`6`, `7`, `8`, and
`9`, respectively.

### Equations

This figure shows the equivalent circuit for the air gap and the adjacent permanent
magnet

where:

- *ϕg* is the magnetic flux that
  flows from the external magnetic circuit to port
  **N**.
- *Rg* is the air gap
  reluctance.
- *mmf* is the magnetomotive force across the rotating
  air gap component.
- *Rm* is the permanent magnet
  reluctance.
- *ϕr* is the magnetic flux
  generated by the rotor permanent magnets in the angle range subtended by
  the stator tooth.

This equation defines the relationship between
*ϕg*, *mmf*, and
*ϕr*:

ϕg=mmf−RmϕrRm+Rg.

If the back EMF is sinusoidal, the flux density of the permanent magnet rotor is defined by
this equation

Br=B0cos(Nθs−Nθr)

where:

- *N* is the **Number of rotor pole
  pairs**.
- *θr* is the rotor
  angle.
- *θs* is the stator
  angle.
- *B0* is the **Peak
  magnet flux density**, in Tesla.

Then, to obtain the permanent magnet flux linkage, integrate over the stator angle
subtended by the stator tooth

ϕr(θr)=rl∫−θtooth2θtooth2[B0cos(Nθs−Nθr)]dθs

where:

- *r* is the **Rotor radius**.
- *l* is the **Tooth depth (in direction of
  shaft)**.

For an ideal PMSM, the *θtooth* must be equal to
*2π/Ns*, where
*Ns* is the value of the
**Number of stator teeth** parameter. Then the equation of the
flux that flows through the equivalent circuit is obtained by solving the integral:

ϕr(θr)=2B0lr/Nsin(πNNs)cos(Nθr).

To obtain the torque generated across the air gap, first calculate the total
energy stored by the component:

E=12ϕg2Rg+12(ϕr(θr))2Rm.

Then, to obtain the torque, differentiate with respect to the
rotor angle:

τ=∂E∂θr=−2B0Rmlrsin(πNNs)sin(Nθr)(ϕg+ϕr(θr))/N.

Finally, calculate *Rg* and
*Rm* in terms of geometry:

Rg=gμ0AgRm=lmμrμ0Ag

where:

- *μ0* is the permittivity of
  free space.
- *μr* is the relative
  permittivity of the permanent magnet.
- *g* is the **Air gap**.
- *lm* is the magnet
  length.

### Faults

You can fault the Rotating Air Gap block. To enable
faults, in the **Faults** section, select the **Enable
faults** parameter.

**Note**

The Rotating Air Gap block does not support
non-intrusive fault modeling. To model non-intrusive faults, use the
Magnetic
Rotor.

A fault is defined as a reduction in the peak magnet flux density. The flux density
associated with each rotor magnet remains sinusoidal in shape. When the Rotating Air
Gap block is in the faulted state, you can apply a reduction factor to the flux
density of any of the rotor poles by specifying the **Flux multipliers for
faulted rotor poles** parameter.

The unfaulted flux density in the airgap of a perfect PMSM with a sinusoidal back EMF is
equal to:

Br=B0cos(Nθs−Nθr)

When the faulted magnet interacts with the tooth, the block uses
this equation to define the flux density

Br=λB0cos(Nθs−Nθr),

where *λ* is the factor that maps peak
*B0* to the faulted
*B0*, and is defined in the
**Flux multipliers for faulted rotor poles** parameter.

The transition to the faulted values linearly blends over the time period that you
specify in the **Duration of transition to faulted** parameter. Use
this parameter to emulate how an overheated permanent magnet gradually loses its
magnetization over time.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
