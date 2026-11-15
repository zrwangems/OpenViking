---
type: simulink-block
title: 'Magnetic Rotor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / System-Level Modeling'
documentation_page: 'magneticrotor'
documentation_source_path: 'ref/magneticrotor.html'
language: en
---

# Magnetic Rotor

## Ports

### Conserving

### **N** — Magnetic stator connection magnetic | array

Magnetic conserving port associated with the stator.

The value at this port is an array of magnetic ports with a length
equal to the value of the **Number of stator teeth**
parameter.

### **S** — Magnetic rotor connection magnetic | array

Magnetic conserving port associated with the rotor.

The value at this port is an array of magnetic ports with a length
equal to the value of the **Number of stator teeth**
parameter.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor
case.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor
rotor.

## Parameters

### Main

### **Number of rotor pole pairs** — Rotor pole pairs `5` (default) | positive scalar

Number of pole pairs of the rotor. This parameter must be equal to or
greater than `1` and less than the value of the
**Number of stator teeth** parameter.

### **Number of stator teeth** — Number of stator teeth `9` (default) | positive scalar

Number of teeth of the stator. This parameter must be equal to or
greater than `2`.

### **Peak magnet flux density** — Peak flux density of magnet rotor `0.4` `T` (default) | positive scalar

Peak flux density associated with the permanent magnet rotor. The flux
density is sinusoidal with the rotor angle.

### **Permanent magnet length (in direction of flux)** — Magnet length in radial machine direction `5` `mm` (default) | positive scalar

Length of the magnet in the radial machine direction or, equivalently,
in the direction of the magnetic flux. This parameter must be less than
the value of the **Rotor radius** parameter.

### **Permanent magnet relative permeability** — Permanent magnet relative permeability `1.05` (default) | scalar

Relative permeability of the permanent magnets. Typically, you set
this parameter to a value a little greater than `1` to
reflect that the magnetic dipoles are already aligned in a permanent
magnet.

### **Air gap** — Air gap in radial direction `1` `mm` (default) | positive scalar

Length of the air gap in the radial direction.

### **Rotor radius** — Rotor radius `65` `mm` (default) | positive scalar

Radius of the rotor.

### **Tooth depth (in direction of shaft)** — Stator tooth depth `50` `mm` (default) | positive scalar

Length of a stator tooth in the direction of the rotating
shaft.

### Faults

### **Rotor poles fault** — Option to fault rotor poles `Add fault` (default)

Option to add a fault to the rotor poles.

To add a fault, click the **Add fault**
hyperlink.

### **Flux multipliers for faulted rotor poles** — Multipliers to reduce rotor pole flux `ones(1,10)` (default) | vector

Multipliers used to reduce the rotor pole magnetic density when the
rotor poles are faulted. The value of this parameter must be a vector
with length equal to twice the value of the **Number of rotor
pole pairs** parameter. Each element of the vector
corresponds to one rotor pole.

The default value of `ones(1,10)` results in the same
behavior as the unfaulted scenario.

#### Dependencies

To enable this parameter, add a fault to the Magnetic Rotor block by
clicking the **Add fault** hyperlink in the
**Rotor poles fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Duration of transition to faulted** — Duration after which block fully faults `100` `s` (default) | positive scalar

Duration after which the block applies the full effect of the faulted
multipliers on the peak magnet flux density of each rotor pole. When the
block enters the faulted state, the software gradually modifies the peak
magnetic flux densities of each rotor pole using the faulted
multipliers.

#### Dependencies

To enable this parameter, add a fault to the Magnetic Rotor block by
clicking the **Add fault** hyperlink in the
**Rotor poles fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

## Libraries

Simscape / Electrical / Electromechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Air gaps between stator teeth and rotating permanent magnet rotor

The Magnetic Rotor block represents the magnetic and
mechanical characteristics of a rotor component in a permanent magnet synchronous
machine (PMSM). In particular, this block models the air gaps between the stator teeth
and a rotating permanent magnet rotor as an array of Rotating Air
Gap blocks.

The **Number of stator teeth** parameter specifies the number of
Rotating Air Gap blocks that comprise the
Magnetic Rotor block. This figure shows the
equivalent circuit of the block when you set the **Number of stator
teeth** parameter to `9`:

If the rotor angle is zero, one of the rotor magnets perfectly aligns with the middle
of the first stator tooth. The orientation of this permanent magnet opposes the flux
flow from port **N** to port **S**.

The magnetic port **N** is an array of magnetic ports with a length
equal to the value of the **Number of stator teeth** parameter. To
connect the individual magnetic ports corresponding to each stator tooth, you need a
Magnetic Demux block. You can write your own Magnetic Demux block using Simscape code,
or use the block from the Faulted PMSM example model.

This figure shows the relationship between the parameters of the
Magnetic Rotor block and their physical values inside
a permanent magnet motor.

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

### Faults

To model a fault in the Magnetic Rotor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Magnetic Rotor block supports faulting the
rotor poles. This faulted behavior corresponds to one or more magnets (poles) in the
rotor having a weakened magnetic field. You can apply a reduction factor to the flux
density of any of the rotor poles by specifying the **Flux multipliers for
faulted rotor poles** parameter.

The transition to the faulted values linearly interpolates over the time period
that you specify in the **Duration of transition to faulted**
parameter. Use this parameter to emulate how an overheated permanent magnet
gradually loses its magnetization over time.
