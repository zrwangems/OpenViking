---
type: simulink-block
title: 'Spark Ignition Engine'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'sparkignitionengine'
documentation_source_path: 'ref/sparkignitionengine.html'
language: en
---

# Spark Ignition Engine

## Ports

### Inputs

### **IgSw** — Ignitor switch, binary physical signal

Physical signal output associated with the ignitor, where
`0` turns off the ignitor and `1`
turns on the ignitor.

#### Dependencies

To enable this port, set **Spark input type** to
`Fixed` or `Spark
angle`.

### **Pim** — Intake manifold pressure input, kPa physical signal

Physical signal input associated with the intake manifold, in kPa.
When you clear **Compute air intake dynamics**, you
supply the intake manifold pressure using this port. You can use this
port as an alternative to providing the throttle command to port
**Thr**.

#### Dependencies

To enable this port, clear **Compute air intake
dynamics**.

### **Thr** — Throttle command input, unitless physical signal

Physical signal input associated with the normalized throttle command,
where `0` represents a fully closed throttle, and
`1` represents a fully open throttle. The block
maps this input to a throttle-open angle between `0`
and `90` degrees.

#### Dependencies

To enable this port, select **Compute air intake
dynamics**.

### **InVT** — Intake Variable Valve Timing input, deg physical signal

Physical signal input associated with the angle to shift the intake
valve open and close timings, in degrees. Positive values advance the
timing and negative values delay the timing.

#### Dependencies

To enable this port, select **Intake Variable Valve
Timing**.

### **ExVT** — Exhaust Variable Valve Timing input, deg physical signal

Physical signal input associated with angle to shift the exhaust valve
open and close timings, in degrees. Negative values advance the timing
and positive values delay the timing.

#### Dependencies

To enable this port, set **Exhaust Variable Valve
Timing**.

### **AfrCmd** — Air-fuel ratio command input, unitless physical signal

Physical signal input associated with the unitless air-fuel ratio
command. Note that this is different from the stoichiometric air-fuel
ratio for gasoline, which the block fixes at
`14.6`.

#### Dependencies

To enable this port, select **Input air-fuel
ratio** and clear **Input injector pulse
width**.

### **InjPw** — Injector pulse width input, ms physical signal

Physical signal input associated with the duration during which the
injector is open to inject fuel, in ms. The block multiplies this signal
by the value of the **Injector slope** parameter to
calculate the amount of fuel that the injector releases during one
pulse.

#### Dependencies

To enable this port, select **Input air-fuel
ratio** and **Input injector pulse
width**.

### **SA** — Spark angle input, deg physical signal

Physical signal input associated with the spark angle before top dead
center, in deg.

#### Dependencies

To enable this port, set **Spark input type** to
`Spark angle`.

### **IgTrig** — Ignition trigger input, unitless physical signal

Physical signal input associated with the ignition trigger. The block
treats a rise from `0` to `1` as a
trigger. The input must return to `0` before the block
accepts another trigger.

#### Dependencies

To enable this port, set **Spark input type** to
`Spark trigger event`.

### **Pback** — Exhaust back pressure input, kPa physical signal

Physical signal input associated with the exhaust back pressure, in
kPa.

#### Dependencies

To enable this port, select **Input back
pressure**.
### Outputs

### **AvrTrq** — Cycle-average net indicated torque output, N\*m physical signal

Physical signal output associated with the cycle-average net indicated torque in
Nm.

#### Dependencies

To enable this port, select **Cycle-average net indicated
torque**.

### **AvrSpd** — Cycle-average speed output, rad/s physical signal

Physical signal output associated with the cycle-average speed output, in rad/s.

#### Dependencies

To enable this port, select **Cycle-average speed**.

### **Pim** — Intake manifold pressure output, kPa physical signal

Physical signal output associated with the intake manifold pressure, in kPa.

#### Dependencies

To enable this port, select **Intake manifold pressure**.

### **crkpos** — Crank position output, deg physical signal

Physical signal output associated with the crank position, in degrees.

#### Dependencies

To enable this port, select **Crank position**.

### **AirMassFlow** — Cylinder air mass flow output, g/s physical signal

Physical signal output associated with the air mass flow, in g/s.

#### Dependencies

To enable this port, select **Cylinder air mass flow** .

### **FuelMassFlow** — Cylinder fuel mass flow output, g/s physical signal

Physical signal output associated with the fuel mass flow, in g/s.

#### Dependencies

To enable this port, select **Cylinder fuel mass flow**.

### **AFR** — Air-fuel ratio output, unitless physical signal

Physical signal output associated with the unitless air-fuel ratio response that the
block attains during operation. Note that this is different from the
stoichiometric air-fuel ratio for gasoline, which the block fixes at
`14.6`.

#### Dependencies

To enable this port, select **Air-fuel ratio**.

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
### Conserving

### **F** — Crank shaft driveline connection mechanical rotational

Mechanical rotational conserving port associated with the crankshaft
connection to the driveline. Include friction and inertia here to
simulate engine load or directly connect other driveline
elements.

## Parameters

### Mechanical

### **Number of cylinders** — Total cylinder count `Single Cylinder` (default) | `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

Number of spark ignition cylinders.

### **Spark angle difference** — Two-cylinder engine spark angle phase `270` `deg` (default) | positive scalar

Spark angle difference for two-cylinder engines.

#### Dependencies

To enable this parameter, set **Number of
cylinders** to `Two
Cylinders`.

### **Firing order** — Ignition order for four cylinder engines `1-3-4-2` (default) | `1-3-2-4`

Firing order for four-cylinder engines. Firing order is engine
specific, but your selection for this parameter will not affect the
block performance. Controller development requires this
information.

#### Dependencies

To enable this parameter, set **Number of
cylinders** to `Four
Cylinders`.

### **Bore** — Cylinder diameter `72.5` `mm` (default) | positive scalar

Diameter of the piston cylinder.

### **Stroke** — Piston travel distance `80.5` `mm` (default) | positive scalar

Distance the piston head travels within the cylinder.

### **Connecting-rod length** — Length of connecting rod `141` `mm` (default) | positive scalar

Length of the piston connecting rod from hole center to hole
center.

### **Compression ratio** — Static compression ratio `11.0` (default) | positive scalar

Ratio of the maximum to minimum cylinder volume.

### Ambient

### **Ambient pressure** — Reference air pressure `101.325` `kPa` (default) | positive scalar

Pressure of the air entering the intake.

### **Ambient temperature** — Reference temperature `298.15` `K` (default) | positive scalar

Temperature of the air entering the intake.

### **Ambient air density** — Reference density `1.225` `mg/cm^3` (default) | positive scalar

Density of the air entering the intake.

### **Specific gas constant of dry air** — Specific gas constant of dry air `288.1965` `J/(K*kg)` (default) | positive scalar

Specific gas constant of dry air.

### Air Intake

### **Compute air intake dynamics** — Option to compute air intake dynamics `on` (default) | `off`

Whether to compute the air intake dynamics. Selecting this parameter
enables these parameters:

- **Throttle response time
  constant**
- **Throttle rest angle**
- **Throttle plate diameter**
- **Throttle leakage area**
- **Intake manifold volume**

### **Throttle response time constant** — Throttle response time constant `0.1` `s` (default) | positive scalar

Time constant associated with the response rate of the engine to the
throttle command.

#### Dependencies

To enable this parameter, select **Compute air intake
dynamics**.

### **Throttle rest angle** — Released throttle position `3` `deg` (default) | positive scalar

Radial distance from the resting throttle position to
`0` degrees.

#### Dependencies

To enable this parameter, select **Compute air intake
dynamics**.

### **Throttle plate diameter** — Throttle plate diameter `5` `cm` (default) | positive scalar

Diameter of the butterfly valve disc in the throttle body.

#### Dependencies

To enable this parameter, select **Compute air intake
dynamics**.

### **Throttle leakage area** — Throttle leakage area `1` `cm^2` (default) | nonnegative scalar

Cumulative area of the throttle leakage.

#### Dependencies

To enable this parameter, select **Compute air intake
dynamics**.

### **Intake manifold volume** — Intake manifold volume `1000` `cm^3` (default) | positive scalar

Volumetric capacity of the intake manifold.

#### Dependencies

To enable this parameter, select **Compute air intake
dynamics**.

### Valves

### **Discharge coefficient for intake valve** — Intake valve discharge coefficient `0.9` (default) | positive scalar

Ratio of actual discharge to ideal discharge for the intake
valve.

### **Intake valve open before TDC** — IVO crank position `15` `deg` (default) | scalar in the range [-360,360]

Crank position before top dead center at which the intake valve opens.
Measure from top dead center to the crank position in the opposite
direction of the crank rotation.

### **Intake valve close after BDC** — IVC crank position `50` `deg` (default) | scalar in the range [-360,360]

Crank position after bottom dead center at which the intake valve
closes. Measure from bottom dead center to the crank position in the
same direction of the crank rotation.

### **Exhaust valve open before BDC** — EVO crank position `55` `deg` (default) | scalar in the range [-360,360]

Crank position before bottom dead center at which the exhaust valve
opens. Measure from bottom dead center to the crank position in the
opposite direction of the crank rotation.

### **Exhaust valve close after TDC** — EVC crank position `10` `deg` (default) | scalar in the range [-360,360]

Crank position after top dead center at which the exhaust valve
closes. Measure from top dead center to the crank position in the same
direction of the crank rotation.

### **Intake Variable Valve Timing** — Intake variable valve timing option `on` (default) | `off`

Whether to control the intake valve timing. Selecting this parameter
enables the **InVT** port.

### **Exhaust Variable Valve Timing** — Exhaust variable valve timing option `on` (default) | `off`

Whether to control the exhaust valve timing. Selecting this port
enables the **ExVT** port.

### Fuel

### **Lower heating value for gasoline** — Fuel net calorific value `44.3` `MJ/kg` (default) | positive scalar

Lower heating value for gasoline. This value is also known as the fuel
net calorific value.

### **Input air-fuel ratio** — Air-fuel ratio parameter option `on` (default) | `off`

Whether to specify the air-fuel ratio by using the **Air-fuel
ratio** parameter or the **AfrCmd**
port.

### **Air-fuel ratio** — Air-fuel ratio `14.6` (default) | positive scalar

Mixture ratio of air to fuel.

#### Dependencies

To enable this parameter, clear **Input air-fuel
ratio**.

### **Input injector pulse width** — Pulse width parameterization `on` (default) | `off`

Whether to specify the injector pulse width.

#### Dependencies

To enable this parameter, select **Input air-fuel
ratio**.

### **Injector slope** — Injector slope `6.5` `mg/ms` (default) | positive scalar

Slope of the fuel injector mass flow rate.

#### Dependencies

To enable this parameter, select **Input air-fuel
ratio** and **Input injector pulse
width**.

### Combustion

### **Spark input type** — Spark input type `Fixed` (default) | `Spark angle` | `Spark trigger event`

Whether to parameterize the spark input using a fixed value, spark
angle, or spark trigger events.

### **Spark advance BTDC** — Spark advance before top dead center `20` `deg` (default) | positive scalar

Spark advance before top dead center.

### **Combustion duration** — Combustion duration `50` `deg` (default) | positive scalar

Duration of combustion as a portion of the crank shaft
rotation.

### **Cylinder pressure slow decay time constant** — Cylinder pressure slow decay rate `60` `s` (default) | positive scalar

Time constant for the cylinder pressure slow decay.

### **Cylinder temperature slow decay time constant** — Cylinder temperature slow decay rate `600` `s` (default) | positive scalar

Time constant for the cylinder temperature slow decay.

### Exhaust

### **Exhaust gas temperature decay time constant** — Exhaust temperature decay rate `5` `ms` (default) | positive scalar

Time constant for the exhaust gas temperature decay.

### **Input back pressure** — Back pressure input option `on` (default) | `off`

Option to input the back-pressure pressure constant and speed
constant.

### **Back-pressure pressure constant** — Pressure constant for back pressure `50` `kPa` (default) | positive scalar

Back-pressure pressure constant.

#### Dependencies

To enable this parameter, clear **Input back
pressure**.

### **Back-pressure speed constant** — Speed constant for back-pressure `6000` `rpm` (default) | positive scalar

Back-pressure speed constant.

#### Dependencies

To enable this parameter, clear **Input back
pressure**.

### **Compute exhaust manifold temperature** — Option to compute exhaust manifold temperature `on` (default) | `off`

Whether the block computes the exhaust manifold temperature. Selecting
this parameter enables these parameters:

- **Surface area of exhaust wall**
- **Mass of exhaust wall**
- **Heat capacity of exhaust wall**
- **Time constant of exhaust heat
  flow**
- **Convective heat transfer coefficient for the
  outer side of exhaust**
- **Radiation constant**
- **Stefan-Boltzmann constant**

### **Surface area of exhaust wall** — Exhaust wall surface area `1` `m^2` (default) | positive scalar

Surface area of the exhaust
wall.
This wall is only the surface area of the internal wall that makes
contact with the exhaust.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Mass of exhaust wall** — Exhaust wall total mass `5` `kg` (default)

Mass of the exhaust wall.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Heat capacity of exhaust wall** — Exhaust wall heat capacity `100` `J/(K*kg)` (default) | positive scalar

Heat capacity of the exhaust wall.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Time constant of exhaust heat flow** — Exhaust heat flow time constant `10` `s` (default) | positive scalar

Time constant for the rate of exhaust heat flow.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Convective heat transfer coefficient for the outer side of exhaust** — Exhaust external convective heat transfer coefficient `100` `W/(K*m^2)` (default) | positive scalar

Convective heat transfer coefficient for the outer side of the
exhaust.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Radiation constant** — Exhaust radiation constant `0.3` (default) | positive scalar

Radiation constant of the exhaust.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### **Stefan-Boltzmann constant** — Stefan-Boltzmann constant of exhaust `5.7e-8` `W/(K^4*m^2)` (default) | positive scalar

Stefan-Boltzmann constant for the total exhaust.

#### Dependencies

To enable this parameter, select **Compute exhaust
manifold temperature**.

### Simulation

### **Initial intake manifold pressure** — Initial pressure inside intake manifold `101.325` `kPa` (default) | positive scalar

Intake manifold pressure at the start of the simulation.

### **Initial crank position (0-720 CAdeg)** — Initial crank position `0` `deg` (default) | scalar in the range [0,720]

Crank position at the start of the simulation.

### **Initial engine speed** — Initial engine speed `0` `rpm` (default) | nonnegative scalar

Rotational speed of the engine at the start of the simulation.

### **Engine speed simulation limit** — Maximum engine speed `8500` `rpm` (default) | positive scalar

Maximum engine speed allowed during the simulation. If the block
exceeds this value, it will generate an error and stop the
simulation.

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

### **Input air/fuel ratio** — Option to output the air-to-fuel ratio `on` (default) | `off`

Whether to output the air-to-fuel ratio from physical signal port
**AFR**.

### **Air mass flow** — Option to output cylinder air mass flow `on` (default) | `off`

Whether to output the intake manifold pressure from physical signal
port **AirMassFlow**.

### **Fuel mass flow** — Option to output fuel mass flow `on` (default) | `off`

Whether to output the fuel mass flow from physical signal port
**FuelMassFlow**.

## Libraries

Simscape / Driveline / Engines & Motors

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
- **Compute exhaust manifold temperature**
- **Crank position**
- **Cycle-average net indicated torque**
- **Cycle-average speed**
- **Cylinder air mass flow**
- **Cylinder fuel mass flow**
- **Cylinder pressure**
- **Cylinder temperature**
- **Cylinder volume**
- **Engine outlet gas energy flow**
- **Exhaust Variable Valve Timing**
- **Fuel mass flow**
- **Input air/fuel ratio**
- **Input back pressure**
- **Input injector pulse width**
- **Intake manifold pressure**
- **Intake Variable Valve Timing**

These parameters used drop downs in previous releases.

### R2024b: Simulate an Atkinson cycle

When you adjust the intake and exhaust valve timings to align with the Atkinson
cycle, the block demonstrates the expected engine behavior.

## Description

Spark ignition engine

The Spark Ignition Engine block represents a naturally
aspirated, spark-ignited internal combustion engine. The engine can be an arbitrary
configuration of one to four cylinders. This block is a composite block that uses a
subcomponent implementation of these blocks:

- The SI Combustion Cylinder block represents
  an individual spark ignited combustion cylinder. The Spark
  Ignition Engine block controls how many
  SI Combustion Cylinder blocks it uses in
  the subcomponent implementation based on the value of the **Number
  of cylinders** parameter. You can adjust the valve timing to
  suit traditional gasoline engine applications as well as hybrid electric and
  plug-in hybrid electric vehicle applications.
- The Ignition Trigger block controls the
  igniter timing for the SI Combustion Cylinder
  blocks.
- The Air Intake block provides the intake
  manifold pressure to the SI Combustion
  Cylinder block. To enable the air intake implementation,
  select **Compute air intake dynamics**.
- The Crank Shaft block connects to each
  SI Combustion Cylinder block to report
  the crank-angle-resolved instantaneous torque.
- The Exhaust Manifold Thermal block
  abstracts the thermodynamics of the exhaust manifold and reports the
  temperature of the exhaust manifold. To compute the exhaust manifold thermal
  effects, select **Compute exhaust manifold
  temperature**.

Many of the Spark Ignition Engine
parameters are identical to the parameters in the subcomponent blocks, and when the
block implements subcomponent blocks, it uses the equations from those blocks. You can
learn more about how the Spark Ignition Engine block uses
each parameter by visiting the reference pages for the subcomponent blocks. You can use
this block to learn how to create your own implementations of the subcomponent blocks by
viewing the source code.

### Equations

The block derives performance information about the engine components using their
respective relationship with the crank position, *θ*, where 0 degrees ≤ *θ* < 720 degrees. The block defines the crank starting position as the intake
stroke at top dead center. For a four-stroke engine, each cylinder is uniquely
affiliated with a crank position, where the crank position for a given cylinder
*i* is *θi*. The block
derives the angular velocity from *θ* as

ω=ddxθ.

The block sets the first cylinder *θ1* =
*θ* regardless of how many cylinders you simulate. When you set
**Number of cylinders** to `Two
cylinders`, the block calculates
*θ2* as

θ2=θ1+Δ,

where *Δ* is the **Spark angle
difference** parameter.

When you set **Number of cylinders** to `Three
cylinders`, the block assumes that the cylinders are evenly phased
such that

θ2=θ1+(1⋅720°3)θ3=θ1+(2⋅720°3)

When you set **Number of cylinders** to `Four
cylinders`, the block assumes that the spark angle difference is
180 degrees. You can select the firing order using the **Firing
order** parameter.

### Assumptions and Limitations

- The block ignores knocking and other combustion instabilities.
- The block ignores internal and external exhaust gas recirculation.
