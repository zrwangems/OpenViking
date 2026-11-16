---
type: simulink-block
title: 'Wind Turbine (Mechanical)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / System-Level Modeling'
documentation_page: 'windturbinemechanical'
documentation_source_path: 'ref/windturbinemechanical.html'
language: en
---

# Wind Turbine (Mechanical)

## Ports

### Inputs

### **V** — Incident wind velocity, m/s physical signal

Physical signal input associated with the incident wind velocity, in
m/s.

### **β** — Pitch angle, deg physical signal

Physical signal input associated with the pitch angle of the turbine
blades, in deg.
### Conserving

### **R** — Turbine shaft mechanical rotational

Mechanical rotational conserving port associated with the wind turbine
shaft.

## Parameters

### Main

### **Turbine radius** — Blade tip radius `80` `m` (default) | positive scalar

Distance from the turbine hub center to the blade tips.

### **Pitch angle vector, β** — Reference pitch angle `[0, 3, 5, 10, 20, 90]` `deg` (default) | vector of length *M*

Reference collective blade pitch angle. The length of this vector
defines the number of rows in the **Power
coefficient table, Cp(β,TSR)** parameter.

### **Tip speed ratio vector, TSR** — Reference tip speed ratio `[0, 2, 4, 6, 8, 10, 12, 14, 15]` (default) | vector of length *N*

Reference tip speed ratio (TSR). TSR is the ratio of the blade tip
speed to wind speed. The length of this vector defines the number of
columns in the **Power coefficient table,
Cp(β,TSR)** parameter. The block supports negative TSR
values. The values must be strictly monotonically increasing.

### **Power coefficient table, Cp(β,TSR)** — Power coefficient table *M*-by-*N* (default)

Power coefficients for a given pitch angle and tip speed ratio. Each
row corresponds to an element in the **Pitch angle
vector, β** parameter, and each column corresponds to an
element in the **Tip speed ratio vector,
TSR** parameter. The default parameter value is
`[0.0010, 0.0161, 0.1446, 0.3865, 0.5009, 0.4404, 0.2545,
0.0002, -0.1384; 0.0016, 0.0173, 0.1079, 0.2676, 0.3779, 0.4111,
0.3838, 0.3176, 0.2753; 0.0027, 0.0197, 0.1151, 0.2606, 0.3469,
0.3558, 0.3069, 0.2222, 0.1718; 0.0054, 0.0283, 0.1315, 0.2364,
0.2589, 0.2022, 0.0929, -0.0455, -0.1204; 0.0109, 0.0536, 0.1320,
0.1256, 0.0120, -0.1752, -0.4017, -0.6435, -0.7655; -0.01 * ones(1,
9)]`.

### **Wind speed threshold** — Velocity smoothing threshold `0.01` `m/s` (default) | positive scalar

Threshold velocity smoothing location. This parameter smooths the
torque, thrust, and power when the rotational speed approaches or
crosses 0. The block applies more smoothing over greater velocity ranges
as you increase the value of this parameter.

### **Rotational velocity threshold** — Velocity smoothing threshold `0.01` `rad/s` (default) | positive scalar

Threshold velocity smoothing location. This parameter smooths the
torque, thrust, and power when the rotational speed approaches or
crosses 0. The block applies more smoothing over greater velocity ranges
as you increase the value of this parameter.

### **Air density** — Air density `1.225` `kg/m^3` (default) | positive scalar

Constant density of air.

### Mechanical

### **Include inertia** — Whether to model rotor inertia `Off` (default) | `On`

Whether to model the rotor inertia of the mechanical translational
port **R**.

### **Rotor Inertia** — Rotor moment of inertia `0.1` `kg*m^2` (default) | positive scalar

Inertia of the rotor attached to mechanical translational port
**R**.

#### Dependencies

To enable this parameter, select the **Include
inertia** parameter.

### **Rotor damping** — Damping of rotor `0` `N*m*s/rad` (default) | positive scalar

Damping of the rotor.

## Libraries

Simscape / Electrical / Electromechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Turbine that converts wind kinetic energy into mechanical power

The Wind Turbine (Mechanical) block represents a wind
turbine that converts the kinetic energy of the wind into mechanical power. The power of
the turbine depends on the nondimensional power coefficient *Cp*. You
can tabulate this coefficient with blade pitch angle and tip speed ratio by specifying
the **Power coefficient table, Cp(β,TSR)** parameter.

The values at the physical signal ports **V** and
**β** represent the wind speed and the collective blade pitch. Port
**R** models the mechanical rotational conserving port associated
with the shaft.

### Equations

The block calculates the coefficients of power by using a table lookup such that

Cp=tablelookup(βRef,λRef,Cp,Ref,β,λsmooth,interpolation = linear, extrapolation = nearest),

where:

- *βRef* is the
  reference pitch angle.
- *λRef* is the
  reference tip speed ratio.
- *CP,Ref* is the
  **Power coefficient table** parameter.
- *λSmooth* is the
  smoothed tip speed ratio.

The block uses this equation as the basis for the instantaneous tip speed ratio

λ=RωV,

where:

- *R* is the **Turbine radius**
  parameter.
- *ɷ* is the differential angular velocity between the
  shaft and the case.
- *V* is the incident air velocity on the rotor. This
  value is the physical signal input port **V**.

The block uses this equation to describe the smoothed version of the instantaneous
tip speed ratio equation

λSmooth=RωV(V2+VThr2),

where *VThr* is the
**Wind speed threshold** parameter. The block uses this
equation as a basis for the power

Power=12CpρAV3=Torque⋅ω,

where:

- *ρ* is the **Air density**
  parameter.
- *A* is the area of the circle swept by the turbine
  blades, and *A =
  πr2*.

To relate the block parameters to the wind turbine mechanical power rating,
determine the wind turbine power at the peak power coefficient and the rated wind
speed. The rated power corresponds to the block parameters using the equation

Powerrated=12CP,maxρAVrated3,

where:

- *CP,max* is the peak power
  coefficient. This is the maximum value in the **Power coefficient
  table, Cp(β,TSR)** parameter.
- *Vrated* is the rated wind speed.
  Rated wind speeds are typically 10 to 15 m/s. The designs of wind turbine
  controller can alter strategy at this wind speed to maintain the rated
  power.
- *A* is the rotor swept area, where *A =
  πr2*.

The block uses numerically smoothed equations for the power, such that

PowerSmooth=CPρA(V2+Vthr2)3/22.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
