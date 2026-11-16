---
type: simulink-block
title: 'Rotating Cylinder Force (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'rotatingcylinderforceil'
documentation_source_path: 'ref/rotatingcylinderforceil.html'
language: en
---

# Rotating Cylinder Force (IL)

## Ports

### Conserving

### **X** — Liquid density port isothermal liquid

Liquid port associated with fluid density. There is no mass flow
through port **X**. Connect port **X**
to port **A** of the Single-Acting Actuator (IL) or
Translational Mechanical Converter (IL)
blocks.

### **C** — Cylinder casing mechanical translational

Mechanical translational conserving port associated with the cylinder
casing reference velocity and force.

### **R** — Piston mechanical translational

Mechanical translational conserving port associated with the piston
velocity and force induced by the pressure differential.
### Input

### **W** — Angular velocity, rad/s physical signal

Angular velocity in rad/s, specified as a physical signal.

## Parameters

### **Piston outer radius** — Piston outer radius `0.1` m (default) | positive scalar

Piston outer radius.

### **Piston inner radius** — Piston inner radius `0.05` m (default) | positive scalar

Piston inner radius.

### **Fluid entry radius** — Fluid channel radius `0.06` m (default) | positive scalar

Radius of the fluid opening in the cylinder casing, measured from the
rotational axis. This value must be greater than or equal to the
**Piston inner radius** and less than or equal to the
**Piston outer radius**.

### **Actuator mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Piston displacement direction of the connected actuator block. `Pressure at A
causes positive displacement of R relative to C`
corresponds to positive displacement, or actuator shaft extension, when
**R** – **C** is positive.
`Pressure at A causes negative displacement of R relative to
C` corresponds to negative displacement, or actuator shaft
retraction, when **R** – **C** is
positive.

## Libraries

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Centripetal pressure gradient for components in an isothermal liquid system

The Rotating Cylinder Force (IL) block models the axial force due to a centripetal
pressure gradient in a rotating shaft about its symmetry axis, which is found in
applications such as friction clutches, square-jaw positive clutches, dog clutches, and
brakes. Connect this block in parallel to a Single-Acting Actuator (IL) or a Translational Mechanical Converter (IL) block to model a
rotating actuator. The fluid density is recorded at the isothermal liquid port
**X**. The angular velocity is received as a physical signal at
port **W**. Port **R** is associated with the piston
velocity, relative to the case at port **C**.

The angular velocity of the shaft is assumed to be constant or nearly-constant, and
therefore the fluid is considered to be in rigid-body rotation.

The centripetal force is due solely to the fluid angular momentum induced by shaft
rotation. Removing the contribution of the static pressure in the fluid channel, the
contribution of the rotation of the shaft to the axial force is:

Frotational=ρπW24(ro4−ri4−2rp2(ro2−ri2)),

where:

- *ρ* is the fluid density at port
  **X**.
- *W* is the angular velocity of the rotating pipe,
  received as a physical signal at port **W**.
- *r*o is the **Piston outer
  radius**.
- *r*i is the **Piston inner
  radius**.
- *r*p is the **Fluid entry
  radius**.
