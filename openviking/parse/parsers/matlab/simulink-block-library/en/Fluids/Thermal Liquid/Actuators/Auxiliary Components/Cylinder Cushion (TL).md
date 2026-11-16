---
type: simulink-block
title: 'Cylinder Cushion (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylindercushiontl'
documentation_source_path: 'ref/cylindercushiontl.html'
language: en
---

# Cylinder Cushion (TL)

## Ports

### Conserving

### **A** — Liquid entry port thermal liquid

Thermal liquid conserving port associated with the liquid entry port
to the cushion chamber.

### **B** — Liquid exit port thermal liquid

Thermal liquid conserving port associated with the exit liquid port of
the cushion chamber.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the piston plunger velocity and
force.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the cylinder reference
structure.

## Parameters

### Cushion Plunger

### **Cushion plunger cross-sectional area** — Cross-sectional area of cushion plunger `1e-4 m^2` (default) | positive scalar

Area of the cross-section of the cushion plunger. The area is πDplunger2/4, where
*Dplunger* is the diameter
of the circular plunger.

### **Cushion plunger length** — Length of cushion plunger `1e-3 m` (default) | positive scalar

Length of the cushion plunger.

### **Initial actuator piston displacement** — Initial displacement of attached piston `0 m` (default) | scalar

Displacement of the piston in the cylinder at the start of simulation.
This displacement determines the initial area of the variable orifice
that models the variable gap between the plunger and the end cap.

If the **Actuator mechanical orientation** parameter
is `Pressure at A causes positive displacement of R relative
to C`, the value of the **Actuator piston
initial displacement** parameter must be positive or
zero.

If the **Actuator mechanical orientation** parameter
is `Pressure at A causes negative displacement of R relative
to C`, the value of the **Actuator piston
initial displacement** parameter must be negative or
zero.

### **Actuator mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Piston displacement direction of the connected actuator block. If this parameter is
`Pressure at A causes positive displacement of R
relative to C`, the piston extends when the value of
the signal at port **R** minus the value of the signal
at port **C** is positive. If this parameter is
`Pressure at A causes negative displacement of R
relative to C`, the piston retracts when the value of
the signal at port **R** minus the value of the signal
at port **C** is positive.

### **Piston cross-sectional area** — Cross-sectional area of piston `0.01 m^2` (default) | positive scalar

Cross-sectional area of the cylinder piston.

### Valves

### **Cushion orifice area** — Orifice area of cushioning valve `1e-6 m^2` (default) | positive scalar

Constant orifice area of the valve through which the fluid flows. The fluid flows from
the cylinder chamber to the cap chamber when the plunger is inside the
opening in the cap.

### **Leakage area between plunger and cushion sleeve** — Total leakage area when plunger is inside cap opening `1e-7 m^2` (default) | positive scalar

Total area of possible leaks when the plunger is inside the cap opening or the cushion
sleeve. When the displacement of the piston is less than or equal to the
value of the **Cushion plunger length** parameter, the
area of the variable orifice that models the gap between the plunger and
the cushion sleeve equals the value of this parameter.

### **Check valve cracking pressure differential** — Pressure differential at which check valve starts to open `0.01 MPa` (default) | positive scalar

Minimum pressure differential across the check valve at which the valve starts to open.
The check valve allows free flow of the liquid from the cushion chamber
to the piston chamber, but does not allow flow in the opposite
direction.

### **Check valve maximum pressure differential** — Pressure differential needed to fully open check valve `0.1 MPa` (default) | positive scalar

Pressure differential across the check valve needed to fully open the valve. The value
of this parameter must be greater than the **Check valve
cracking pressure differential** parameter. The check valve
allows free flow of the liquid from the cushion chamber to the piston
chamber, but does not allow flow in the opposite direction.

### **Check valve maximum area** — Opening area when check valve is fully open `1e-4 m^2` (default) | positive scalar

Passage area of the check valve when the valve is fully open.

### **Check valve leakage area** — Total leakage area when check valve is fully closed `1e-10 m^2` (default) | positive scalar

Total area of possible leaks when the check valve is fully
closed.

### **Smoothing factor** — Amount of smoothing to apply to check valve and variable orifice opening area functions `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

## Libraries

Simscape / Fluids / Thermal Liquid / Actuators / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Cylinder cushion in a thermal liquid network

The Cylinder Cushion (TL) block models a cylinder cushion in a thermal
liquid network. The cushion decelerates the cylinder rod as it approaches the end of a
stroke by restricting the flow rate leaving the cylinder chamber. This figure below
shows a typical cylinder cushion design [1].

Diagram of cylinder cushion

As the piston moves toward the cap, which is to the left in the figure, the cushioning bush,
or plunger, enters the chamber in the cap and creates an additional resistance to the
fluid leaving the cylinder chamber. The piston deceleration starts when the plunger
enters the opening in the cap and closes the main fluid exit. In this state, the fluid
flows through a check valve in the gap between the cylinder and the cap. The valve
restricts the flow rate leaving the cylinder chamber and reduces the initial speed of
the piston.

The cylinder cushion is a composite of a variable orifice, a local restriction, and a check
valve. The variable orifice provides a variable opening between the plunger and end cap
cavity. The local restriction connects the piston chamber to the cushion chamber. The
check valve provides a flow path between the cushion chamber and the piston chamber only
during piston retraction.

The Cylinder Cushion (TL) block is a composite component that consists of
these blocks:

- A Local Restriction (TL)
  block that models the cushioning valve.
- A Check Valve (TL) block that
  models the check valve.
- An Orifice (TL) block that
  models the variable gap between the plunger and the end cap.
- An Ideal Translational Motion Sensor block that converts the separation
  between the plunger and the cavity in the end cap into a physical signal. This
  signal controls the opening of the Orifice (TL) block.

You can use the Cylinder Cushion (TL) block to model
actuators. A single-acting or double-acting actuator can include cylinder cushions to
slow piston motion near the ends of the stroke. The cylinder cushion prevents extreme
impacts when the piston is stopped by the end caps.

Ports **A** and **B** are thermal liquid conserving ports
associated with the chamber inlet and outlet, respectively. Port **R**
is a mechanical translational conserving port connected with the piston plunger. Port
**C** is a mechanical translational conserving port that
corresponds to the cylinder clamping structure. The block cushions the flow rate from
port **B** to port **A**. The check valve in the block
is oriented from port **A** to port **B**.

### Variable Orifice Area

In the variable orifice, the block assumes that when the plunger is far away from the
cushion, the orifice area is fully open and equal to πDplunger2/4, where *Dplunger* is the
diameter of the circular plunger. When the plunger is in the cushion, the orifice is
fully closed and the orifice area is equal to the leakage area. As the plunger moves
towards the cushion, the fluid flows radially from the cylinder chamber to the cap
chamber through the gap between the plunger and the opening in the cap. The block
assumes that the orifice area changes linearly with the piston displacement between
the maximum area and the leakage area. The orifice area for a given position of the
piston is

S={Sleak,εxpiston≤LplungerSmax,εxpiston≥Lplunger+Dplunger4Smax−SleakDplunger4(εxpiston−Lplunger)+Sleak,Lplunger<εxpiston<Lplunger+Dplunger4

where:

- *S* is the orifice area for a given position of the
  piston.
- *Sleak* is the value of the
  **Leakage area between plunger and cushion
  sleeve** parameter.
- *Smax* is the maximum size of
  the orifice, which is equal to the value of the **Cushion
  plunger cross-sectional area** parameter.
- *xpiston* is the displacement
  of the piston. The initial displacement of the piston
  *x0,piston* is the value
  of the **Actuator piston initial displacement**
  parameter.
- *ε* is `1` when the
  **Actuator mechanical orientation** parameter is
  `Pressure at A causes positive displacement of R
  relative to C` and is `-1` when the
  **Actuator mechanical orientation** parameter is
  `Pressure at A causes negative displacement of R
  relative to C`.
- *Lplunger* is the value of the
  **Cushion plunger length** parameter.
- *Dplunger* is the value of the
  **Cushion plunger diameter** parameter.

### Numerically-Smoothed Area and Pressure

You can maintain numerical robustness in your simulation
by adjusting the **Smoothing factor** parameter. If the
**Smoothing factor** parameter is nonzero, the block smooths
the orifice area and the check valve pressure range. The block smoothly saturates
the orifice area between the **Leakage area between plunger and cushion
sleeve** and **Cushion plunger cross-sectional
area** parameters. The valve pressure is saturated between the
**Check valve cracking pressure differential** and
**Check valve maximum pressure differential** parameters. For
more information, see Numerical Smoothing.
