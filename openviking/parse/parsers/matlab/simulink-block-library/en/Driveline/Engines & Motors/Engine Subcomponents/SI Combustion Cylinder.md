---
type: simulink-block
title: 'SI Combustion Cylinder'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'sicombustioncylinder'
documentation_source_path: 'ref/sicombustioncylinder.html'
language: en
---

# SI Combustion Cylinder

## Ports

### Input

### **IgTrig** — Ignition trigger input, unitless physical signal

Physical signal input associated with the ignition trigger. The block
treats a rise from `0` to `1` as a
trigger. The input must return to `0` before the block
accepts another trigger.

### **InjPw** — Injector pulse width input, ms physical signal

Physical signal input associated with the duration during which the
injector is open to inject fuel, in milliseconds. The block multiplies
this signal by the value of the **Injector slope**
parameter to calculate the amount of fuel that the injector releases
during one pulse.

#### Dependencies

To enable this port, select **Input injector pulse
width**.

### **AfrCmd** — Air-fuel ratio command input, unitless physical signal

Physical signal input associated with the unitless air-fuel ratio
command. Note that this is different from the stoichiometric air-fuel
ratio for gasoline, which the block fixes at
`14.6`.

#### Dependencies

To enable this port, clear **Input injector pulse
width**.

### **Pim** — Intake manifold pressure input, kPa physical signal

Physical signal input associated with the intake manifold, in kPa.
When you clear **Compute air intake dynamics**, you
supply the intake manifold pressure using this port. You can use this
port as an alternative to providing the throttle command to port
**Thr**.

### **InVT** — Intake variable valve timing input, deg physical signal

Physical signal input associated with the angle to shift the intake
valve open and close timings, in degrees. Positive values advance the
timing and negative values delay the timing.

#### Dependencies

To enable this port, select **Intake Variable Valve
Timing**.

### **ExVT** — Exhaust variable valve timing input, deg physical signal

Physical signal input associated with angle to shift the exhaust valve
open and close timings, in degrees. Negative values advance the timing
and positive values delay the timing.

#### Dependencies

To enable this port, select **Exhaust Variable Valve
Timing**.

### **Pback** — Exhaust back pressure input, kPa physical signal

Physical signal input associated with the exhaust back pressure, in
kPa.

#### Dependencies

To enable this port, select **Input back
pressure**.

### **CrkPos** — Crank position, deg physical signal

Physical signal input associated with the crank position, in
degrees.

### **Spd** — Engine rotational speed, rad/s physical signal

Physical signal input associated with the engine rotational speed, in
rad/s.
### Output

### **CylPwr** — Cylinder power, W physical signal

Physical signal output associated with the cylinder power, in W.

### **Weo** — Engine outlet gas energy flow, W physical signal

Physical signal output associated with the engine outlet gas energy flow, in W.

#### Dependencies

To enable this port, select **Engine outlet gas energy flow**.

### **Vcyl** — Cylinder volume output, cm^3 physical signal

Physical signal output associated with the cylinder volume, in
cm3.

#### Dependencies

To enable this port, select **Cylinder volume**.

### **Pcyl** — Cylinder pressure output, MPa physical signal

Physical signal output associated with the cylinder pressure, in MPa.

#### Dependencies

To enable this port, select **Cylinder pressure**.

### **Tcyl** — Cylinder temperature output, K physical signal

Physical signal output associated with the cylinder temperature, in K.

#### Dependencies

To enable this port, select **Cylinder temperature**.

### **AFR** — Air-fuel ratio output, unitless physical signal

Physical signal output associated with the unitless air-fuel ratio response that the
block attains during operation. Note that this is different from the
stoichiometric air-fuel ratio for gasoline, which the block fixes at
`14.6`.

#### Dependencies

To enable this port, select **Air-fuel ratio**.

### **AirMassFlow** — Cylinder air mass flow output, g/s physical signal

Physical signal output associated with the air mass flow, in g/s.

#### Dependencies

To enable this port, select **Air mass flow** .

### **FuelMassFlow** — Cylinder fuel mass flow output, g/s physical signal

Physical signal output associated with the fuel mass flow, in g/s.

#### Dependencies

To enable this port, select **Fuel mass flow**.

## Parameters

### Mechanical

### **Number of cylinders as a system** — Total combustion cylinder count in series `1` (default) | positive scalar

Total number of combustion cylinders connected to a single
Crank Shaft block. The value of this
parameter should be the same as the number of SI
Combustion Cylinder blocks in the system.

### **Cylinder number** — Cylinder number in series `1` (default) | positive scalar

Assignment number for this SI Combustion
Cylinder block. Each SI Combustion
Cylinder block must use a unique value for
**Cylinder number**.

### **Bore** — Cylinder diameter `75.0` `mm` (default) | positive scalar

Diameter of the piston cylinder.

### **Stroke** — Piston travel distance `84.7` `mm` (default) | positive scalar

Distance the piston head travels within the cylinder.

### **Connecting-rod length** — Length of connecting rod `141` `mm` (default) | positive scalar

Length of the piston connecting-rod from hole center to hole
center.

### **Compression ratio** — Static compression ratio `11.0` (default) | positive scalar

Ratio of the maximum to minimum cylinder volume.

### Ambient

### **Ambient pressure** — Reference air pressure `101.325` `kPa` (default) | positive scalar

Pressure of the air entering the intake.

### **Ambient temperature** — Reference temperature `(273.15 + 25)` `K` (default) | positive scalar

Temperature of the air entering the intake.

### **Ambient air density** — Reference density `1.225` `mg/cm^3` (default) | positive scalar

Density of the air entering the intake.

### **Specific gas constant of dry air** — Specific gas constant of dry air `288.1965` `J/(K*kg)` (default) | positive scalar

Specific gas constant of dry air.

### Valves

### **Discharge coefficient for intake valve** — Intake valve discharge coefficient `0.5` (default) | positive scalar

Ratio of actual discharge to ideal discharge for the intake
valve.

### **Intake valve open before TDC** — IVO crank position before TDC `15` `deg` (default) | scalar in the range [-360,360]

Crank position before TDC at which the intake valve opens. Measure
from TDC to the crank position in the opposite direction of the crank
rotation.

### **Intake valve close after BDC** — IVC crank position after BDC `50` `deg` (default) | scalar in the range [-360,360]

Crank position after BDC at which the intake valve closes. Measure
from BDC to the crank position in the same direction of the crank
rotation.

### **Exhaust valve open before BDC** — EVO crank position before BDC `55` `deg` (default) | scalar in the range [-360,360]

Crank position before BDC at which the exhaust valve opens. Measure
from BDC to the crank position in the opposite direction of the crank
rotation.

### **Exhaust valve close after TDC** — EVC crank position after TDC `10` `deg` (default) | scalar in the range [-360,360]

Crank position after TDC at which the exhaust valve closes. Measure
from TDC to the crank position in the same direction of the crank
rotation.

### **Intake Variable Valve Timing** — Option to control intake VVT `on` (default) | `off`

Option to control the intake valve timing. Selecting this parameter
enables the **InVT** port.

### **Exhaust Variable Valve Timing** — Option to control exhaust VVT `on` (default) | `off`

Option to control the exhaust valve timing. Selecting this parameter
enables the **ExVT** port.

### Combustion

### **Lower heating value for gasoline** — Fuel net calorific value `44.3e+6` `J/kg` (default)

Lower heating value for gasoline. This value is also known as the fuel
net calorific value.

### **Input injector pulse width** — Option to input injector pulse width `on` (default) | `off`

Option to specify the injector pulse width. Selecting this parameter
enables the **InjPw** port.

### **Injector slope** — Injector slope `6.5` `mg/ms` (default) | positive scalar

Slope of the fuel injector mass flow rate.

#### Dependencies

To enable this parameter, select **Input injector pulse
width**.

### **Combustion duration** — Combustion duration `50` `deg` (default) | positive scalar

Duration of combustion as a segment of the crank shaft
rotation.

### **Cylinder pressure slow decay time constant** — Cylinder pressure slow decay rate `60` `s` (default) | positive scalar

Time constant for the cylinder pressure slow decay.

### **Cylinder temperature slow decay time constant** — Cylinder temperature slow decay rate `600` `s` (default) | positive scalar

Time constant for the cylinder temperature slow decay.

### Exhaust

### **Exhaust gas temperature decay time constant** — Exhaust temperature decay rate `5` `ms` (default) | positive scalar

Time constant to specify the exhaust gas temperature decay.

### **Input back pressure** — Back pressure input option `on` (default) | `off`

Option to input the back-pressure pressure constant and speed
constant. Selecting this parameter enables the
**Pback** port.

### **Back-pressure pressure constant** — Pressure constant for back-pressure `50` `kPa` (default) | positive scalar

Back-pressure pressure constant.

#### Dependencies

To enable this parameter, clear **Input back
pressure**.

### **Back-pressure speed constant** — Speed constant for back-pressure `6000` `rpm` (default) | positive scalar

Back-pressure speed constant.

#### Dependencies

To enable this parameter, clear **Input back
pressure**.

### Simulation

### **Engine speed simulation limit** — Maximum engine speed `8500` `rpm` (default) | positive scalar

Maximum engine speed allowed during the simulation. If the engine
speed exceeds this value, the block prevents combustion.

### **Initial crank position (0-720 deg)** — Initial crank position `0` `deg` (default) | scalar in the range [0,720]

Crank position at the start of the simulation.

### **Initial engine speed** — Initial engine speed `0` `rpm` (default) | nonnegative scalar

Rotational speed of the engine at the start of the simulation.

### Output

### **Engine outlet gas energy flow** — Option to output engine outlet gas energy flow `off` (default) | `on`

Whether to output engine outlet gas energy flow from physical signal
port **Weo**.

### **Cylinder volume** — Option to output the cylinder volume `on` (default) | `off`

Whether to output the cylinder volume from physical signal port
**Vcyl**.

### **Cylinder pressure** — Option to output cylinder pressure `on` (default) | `off`

Whether to output the cylinder pressure from physical signal port
**Pcyl**.

### **Cylinder temperature** — Option to output cylinder temperature `on` (default) | `off`

Whether to output the cylinder temperature from physical signal port
**Tcyl**.

### **Air/fuel ratio** — Option to output the air-to-fuel ratio `on` (default) | `off`

Whether to output the air-to-fuel ratio from physical signal port
**AFR**.

### **Air mass flow** — Option to output cylinder air mass flow `on` (default) | `off`

Whether to output the intake manifold pressure from physical signal
port **AirMassFlow**.

### **Fuel mass flow** — Option to output fuel mass flow `on` (default) | `off`

Whether to output the fuel mass flow from physical signal port
**FuelMassFlow**.

## Libraries

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

### R2025a: Enumeration Updates

These parameters now use a checkbox.

- **Air-fuel ratio**
- **Air mass flow**
- **Compute air intake dynamics**
- **Cylinder pressure**
- **Cylinder temperature**
- **Cylinder volume**
- **Engine outlet gas energy flow**
- **Exhaust Variable Valve Timing**
- **Fuel mass flow**
- **Input back pressure**
- **Input injector pulse width**
- **Intake Variable Valve Timing**

These parameters used drop downs in previous releases.

### R2024b: Simulate an Atkinson cycle

When you adjust the intake and exhaust valve timings to align with the Atkinson
cycle, the block demonstrates the expected engine behavior.

## Description

Spark-ignited, four-stroke internal combustion cylinder

The SI Combustion Cylinder block represents the
crank-angle-resolved, instantaneous pressure production dynamics of a spark-ignited,
four-stroke internal combustion engine cylinder. You can use this block as a
subcomponent in a composite internal combustion engine block, such as the
Spark Ignition Engine block. The block computes the
instantaneous cylinder pressure and also provides optional outputs to collect additional
information. To obtain the instantaneous torque, connect one or more of these blocks
with the Crankshaft block. This page uses these common
industry abbreviations:

- TDC — Top dead center
- BDC — Bottom dead center
- IVO — Intake valve open
- IVC — Intake valve close
- EVO — Exhaust valve open
- EVC — Exhaust valve close
- VVT — Variable valve timing

### Equations

The block depends on the angular position of the crank, *θ*, where TDC is
0°, and the crank position can range from 0° to 720°. Using this definition, 0° is
the intake TDC, and 360° is the combustion TDC. The block calculates the
instantaneous cylinder volume as a function of the crank position such that

V(θ)=Vcl+Vdispl⋅12(la+1−cosθ−(la)2−sin2θ),

where:

- *Vcl* is the clearance
  volume.
- *Vdispl* is the displacement
  volume, which the block finds from the **Bore** and
  **Stroke** parameters.
- *l* is the **Connecting-rod length**
  parameter.
- *a* is the crank radius.

The block calculates *Vcl* as

Vcl=Vdisplrc−1,

where *rc* is the
**Compression ratio** parameter. The time derivative of
*V(θ)* scales the instantaneous power that the cylinder
generates, *Q(θ)*, such that

Qcyl(θ)=(Pcyl(θ)−Pamb)⋅ddtV(θ),

where *Pcyl(θ)* is the
cylinder pressure as a function of the crank position, and
*Pamb* is the **Ambient
pressure** parameter. The block formulation to compute
*Pcyl(θ)* depends on which part of
the stroke cycle is active in the cylinder.

**Valve Timing and Stroke Cycle**

These plots show the stroke status with respect to the crank position. The spiral line
represents the crank rotation. The spiral begins at IVO and ends at EVC.
Depending on timing, there may be overlapping times where both the intake and
exhaust valves have the same condition. Positive overlap happens when IVO occurs
before EVC. Negative overlap happens when EVC occurs before IVO. Using this
definition, there can be six unique modes depending on whether the overlap
occurs before, during, or after TDC. The block approximates these modes.

An example plot of valve timings showing 25 degrees of positive overlap

This plot shows a typical valve timing scenario where IVO
occurs 15 degrees before TDC, and IVC occurs 50 degrees after BDC. EVO occurs at
55 degrees before BDC, and EVC occurs at 10 degrees after TDC. Note the 25
degrees of positive overlap where the intake valves open before the exhaust
valves close. The table demonstrates the six valve overlap modes.

|  | Before TDC | During TDC | After TDC |
| --- | --- | --- | --- |
| Positive Overlap |  |  |  |
| Negative Overlap |  |  |  |

You adjust the parameters in the **Valves**
section to represent either an Otto cycle or an Atkinson cycle. Gasoline engines
typically use the Otto cycle due to its balance of power and efficiency. Hybrid
engines and some modern gasoline engines use the Atkinson cycle to enhance fuel
efficiency by sacrificing power output. Using Atkinson cycle timings for either
the Spark Ignition
Engine or SI Combustion
Cylinder blocks results in:

- A smaller effective compression ratio and larger expansion
  ratio
- Improved fuel efficiency
- Reduced torque and power for a given displacement

The figure shows a comparison of typical timings for the Otto
cycle and the Atkinson cycle :

Examples of valve timings between the Otto and Atkinson cycle. The Otto cycle has a 25 degree overlap, while the Atkinson cycle has a -5 degree overlap.

**Cylinder Modes**

During normal operation, the engine cylinders require a minimum engine speed to maintain
stable combustion. However, during transient operations, such as using the
starter motor to turn the crank, the cylinder completes stroke cycles without
attaining stable combustion. The block takes these slow engine speed
interactions into account such that the block considers 18 possible modes. These
are the slow engine operation modes:

1. Slow Intake
2. Slow Compression-Expansion
3. Slow Exhaust
4. Slow Positive Overlap Before TDC
5. Slow Positive Overlap During TDC
6. Slow Positive Overlap After TDC
7. Slow Negative Overlap Before TDC
8. Slow Negative Overlap During TDC
9. Slow Negative Overlap After TDC

These are the regular engine operation modes:

10. Intake
11. Compression-Expansion
12. Exhaust
13. Positive Overlap Before TDC
14. Positive Overlap During TDC
15. Positive Overlap After TDC
16. Negative Overlap Before TDC
17. Negative Overlap During TDC
18. Negative Overlap After TDC

The block gives each discrete mode a transition constraint by using the mode
chart feature. The table shows which transitions the block allows.

| Mode Transition | Allowed Modes |
| --- | --- |
| Slow ↣ Slow | - 1 ↣ 2 - 2 ↣ 3 - 3 ↣ 4, 5, 6, 7, 8, 9 - 4, 5, 6, 7, 8, 9 ↣ 1 |
| Slow ↣ Regular | - 4, 5, 6, 7, 8, 9 ↣ 10 |
| Regular ↣ Regular | - 10 ↣ 11 - 11 ↣ 12 - 12 ↣ 13, 14, 15, 16, 17, 18 - 13, 14, 15, 16, 17, 18 ↣ 10 |
| Regular ↣ Slow | - 10 ↣ 2 - 11 ↣ 3 - 12 ↣ 4, 5, 6, 7, 8, 9 - 13, 14, 15, 16, 17, 18 ↣ 1 |

The flow chart in the figure visually depicts how the block
steps through the modes.

**Mode Transition Flowchart**

Transition flowchart that illustrates the steps in the table.

The block captures the effect of the valve timings on the effective
compression ratio and considers the effect of IVC much later than BDC which can
reduce the amount of air charged in the combustion cylinder. However, the block
ignores internal exhaust gas recirculation.

### Assumptions and Limitations

- The block ignores knocking and other combustion instabilities.
- The block ignores internal and external exhaust gas recirculation.
