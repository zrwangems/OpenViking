---
type: simulink-block
title: 'Pipe (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'pipetl'
documentation_source_path: 'ref/pipetl.html'
language: en
---

# Pipe (TL)

## Ports
```yaml
ports:
- name: EL
  summary: Port elevation difference, m physical signal
  direction: input
- name: G
  summary: Gravitational acceleration, m/s^2 physical signal
  direction: input
- name: A
  summary: Pipe opening thermal liquid
  direction: conserving
- name: B
  summary: Pipe opening thermal liquid
  direction: conserving
- name: H
  summary: Pipe wall thermal
  direction: conserving
```

### Input

### **EL** — Port elevation difference, m physical signal

Variable elevation differential between port **A**
and **B**, specified as a physical signal. The block
bounds the signal value at **EL** between
*-L* and *L*, where
*L* is the value of the **Pipe
length** parameter.

#### Dependencies

To enable this port, set **Elevation gain
specification** to
`Variable`.

### **G** — Gravitational acceleration, m/s^2 physical signal

Variable gravitational acceleration, specified as a physical
signal.

#### Dependencies

To enable this port, set **Gravitational acceleration
specification** to
`Variable`.
### Conserving

### **A** — Pipe opening thermal liquid

Liquid entry or exit port to the pipe.

### **B** — Pipe opening thermal liquid

Liquid entry or exit port to the pipe.

### **H** — Pipe wall thermal

Pipe wall temperature.
## Parameters
```yaml
parameters:
- name: Enable dynamic compressibility
  summary: Whether to model fluid dynamic compressibility on (default) | off
  group: Configuration
- name: Enable fluid inertia
  summary: Whether to model fluid acceleration off (default) | on
  group: Configuration
- name: Number of segments
  summary: Pipe discretization 1 (default) | positive unitless scalar
  group: Configuration
- name: Pipe total length
  summary: Total pipe length 5 m (default) | positive scalar in units of length
  group: Configuration
- name: Cross-sectional geometry
  summary: Pipe geometry Circular (default) | Annular | Rectangular | Elliptical | Isosceles triangular | Custom
  group: Configuration
- name: Pipe diameter
  summary: Pipe diameter 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe inner diameter
  summary: Pipe inner diameter 0.05 m (default) | positive scalar
  group: Configuration
- name: Pipe outer diameter
  summary: Pipe outer diameter 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe width
  summary: Rectangular pipe width 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe height
  summary: Rectangular pipe height 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe major axis
  summary: Elliptical pipe major axis 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe minor axis
  summary: Elliptical pipe minor axis 0.05 m (default) | positive scalar
  group: Configuration
- name: Pipe side length
  summary: Triangular pipe side length 0.1 m (default) | positive scalar
  group: Configuration
- name: Pipe vertex angle
  summary: Triangular pipe vertex angle 30 deg (default) | positive scalar
  group: Configuration
- name: Cross-sectional area
  summary: Cross-sectional pipe area without deformation 0.01 m^2 (default) | positive scalar
  group: Configuration
- name: Hydraulic diameter
  summary: Effective diameter of noncircular pipes 0.1128 m (default) | positive scalar in units of length
  group: Configuration
- name: Elevation gain specification
  summary: Set pipe elevation property Constant (default) | Variable
  group: Configuration
- name: Elevation gain from port A to port B
  summary: Change in elevation from port A to port B 0 m (default) | positive scalar in units of length
  group: Configuration
- name: Gravitational acceleration specification
  summary: Acceleration specification Constant (default) | Variable
  group: Configuration
- name: Gravitational acceleration
  summary: Acceleration due to gravity at mean pipe elevation 9.81 m/s^2 (default) | scalar
  group: Configuration
- name: Viscous friction parameterization
  summary: Friction model Haaland correlation (default) | Nominal pressure drop vs. nominal mass flow rate | Tabulated data
    - Darcy friction factor vs. Reynolds number
  group: Viscous Friction
- name: Local resistances specification
  summary: Method for quantifying pressure losses in the Haaland correlation Aggregate equivalent length (default) | Local
    loss coefficient
  group: Viscous Friction
- name: Total local loss coefficient
  summary: Defines loss coefficient over the pipe 0.1 (default) | positive scalar
  group: Viscous Friction
- name: Aggregate equivalent length of local resistances
  summary: Minor pressure loss in the pipe expressed as a length 1 m (default) | positive scalar
  group: Viscous Friction
- name: Surface roughness specification
  summary: 'Pipe material for roughness specification Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um (default)
    | Steel and wrought iron : 46 um | Galvanized iron or steel : 152 um | Cast iron : 259 um | Custom'
  group: Viscous Friction
- name: Internal surface absolute roughness
  summary: Pipe wall absolute roughness 1.5e-5 m (default) | positive scalar in units of length
  group: Viscous Friction
- name: Laminar friction constant for Darcy friction factor
  summary: Friction constant for laminar flows 64 (default) | positive scalar
  group: Viscous Friction
- name: Laminar flow upper Reynolds number limit
  summary: Reynolds number below which the flow is laminar 2e+3 (default) | positive scalar
  group: Viscous Friction
- name: Turbulent flow lower Reynolds number limit
  summary: Reynolds number above which the flow is turbulent 4e+3 (default) | positive scalar
  group: Viscous Friction
- name: Nominal mass flow rate
  summary: Pipe mass flow rate [0.1 1] kg/s (default) | scalar or vector of numbers in units of mass/time
  group: Viscous Friction
- name: Nominal pressure drop
  summary: Pressure drop over the pipe [0.001 0.01] MPa (default) | scalar or vector of numbers in units of pressure
  group: Viscous Friction
- name: Mass flow rate threshold for flow reversal
  summary: Threshold below which numerical smoothing is applied 1e-6 kg/s (default) | positive scalar in units of mass/time
  group: Viscous Friction
- name: Reynolds number vector for turbulent Darcy friction factor
  summary: Reynolds numbers at which to tabulate the Darcy friction factor [ 400 1000 1.5e+3 3e+3 4e+3 6e+3 1e+4 2e+4 4e+4
    6e+4 1e+5 1e+8 ] (default) | vector of positive numbers
  group: Viscous Friction
- name: Darcy friction factor vector
  summary: Darcy friction factors at the tabulated Reynolds numbers [ 0.264 0.112 0.07099999999999999 0.0417 0.0387 0.0268
    0.025 0.0232 0.0226 0.022 0.0214 0.0214 ] (default) | vector of positive numbers
  group: Viscous Friction
- name: Pipe wall specification
  summary: Pipe wall flexibility Rigid (default) | Flexible
  group: Pipe Wall
- name: Volumetric expansion specification
  summary: Linear expansion correlation Cross-sectional area vs. pressure (default) | Cross-sectional area vs. pressure -
    Tabulated | Hydraulic diameter vs. pressure | Based on material properties
  group: Pipe Wall
- name: Static gauge pressure to cross-sectional area gain
  summary: Coefficient for area-dependent pipe deformation 1e-6 m^2/MPa (default) | positive scalar
  group: Pipe Wall
- name: Static gauge pressure vector
  summary: Vector of gauge pressures [.1,1] MPa (default) | vector
  group: Pipe Wall
- name: Cross sectional area gain vector
  summary: Vector of pipe cross-sectional areas [1e-05, 1.1e-05] m^2 (default) | vector
  group: Pipe Wall
- name: Static gauge pressure to hydraulic diameter gain
  summary: Coefficient for diameter-dependent pipe deformation 1e-6 m/MPa (default) | positive scalar
  group: Pipe Wall
- name: Material behavior
  summary: Method to specify material behavior Linear Elastic (default) | Multilinear Elastic
  group: Pipe Wall
- name: Pipe wall thickness
  summary: Width of pipe wall 0.05 m (default) | positive scalar
  group: Pipe Wall
- name: Young's modulus
  summary: Young's modulus of pipe wall material 69 GPa (default) | positive scalar
  group: Pipe Wall
- name: Poisson's ratio
  summary: Poisson's ratio of pipe wall material 0.33 (default) | positive scalar
  group: Pipe Wall
- name: Stress vector
  summary: Stress vector of pipe wall material [276, 310] MPa (default) | vector
  group: Pipe Wall
- name: Strain vector
  summary: Strain vector of pipe wall material [.004, .02] (default) | vector
  group: Pipe Wall
- name: Check if stress exceeds specified allowable level
  summary: Notification when stress is above specified max None (default) | Warning | Error
  group: Pipe Wall
- name: Maximum allowable stress
  summary: Maximum allowed stress on pipe wall 400 MPa (default) | positive scalar
  group: Pipe Wall
- name: Volumetric expansion time constant
  summary: Pipe deformation time constant 0.01 s (default) | positive scalar
  group: Pipe Wall
- name: Pipe thermal expansion
  summary: Whether to model thermal expansion off (default) | on
  group: Pipe Wall
- name: Coefficient of thermal expansion
  summary: Pipe coefficient of thermal expansion 24 um/(deltaK*m) (default) | positive scalar
  group: Pipe Wall
- name: Thermal expansion reference temperature
  summary: Reference temperature for pipe thermal expansion 293.15 K (default) | positive scalar
  group: Pipe Wall
- name: Heat transfer parameterization
  summary: Method by which to capture the convective heat transfer with the pipe wall Gnielinski correlationNominal temperature
    differential vs. nominal mass flow rate (default) | Dittus-Boelter correlation | Tabulated data - Colburn factor vs. Reynolds
    number | Tabulated data - Nusselt number vs. Reynolds number & Prandtl number
  group: Heat Transfer
- name: Nusselt number for laminar flow heat transfer
  summary: Nusselt number to use in the heat transfer calculations for laminar flows 3.66 (default)
  group: Heat Transfer
- name: Nominal mass flow rate
  summary: Pipe mass flow rate [0.1 1] kg/s (default) | scalar or vector of numbers in units of mass/time
  group: Heat Transfer
- name: Nominal inflow temperature
  summary: Pipe inlet temperature [293.15 293.15] K (default) | scalar or vector of numbers in units of temperature
  group: Heat Transfer
- name: Nominal outflow temperature
  summary: Pipe outlet temperature [300 300] K (default) | scalar or vector of numbers in units of temperature
  group: Heat Transfer
- name: Nominal inflow pressure
  summary: Pipe inlet pressure [0.101325 0.101325] MPa (default) | scalar or vector of numbers in units of pressure
  group: Heat Transfer
- name: Nominal wall temperature
  summary: Pipe wall temperature [303.15 303.15] K (default) | scalar or vector of numbers in units of temperature
  group: Heat Transfer
- name: Coefficient a
  summary: Empirical constant *a* of the Dittus-Boelter correlation 0.023 (default) | positive scalar
  group: Heat Transfer
- name: Exponent b
  summary: Empirical constant *b* of the Dittus-Boelter correlation 0.8 (default) | positive scalar
  group: Heat Transfer
- name: Exponent c
  summary: Empirical constant *c* of the Dittus-Boelter correlation 0.4 (default) | positive scalar
  group: Heat Transfer
- name: Reynolds number vector for Colburn factor
  summary: Reynolds numbers at which to tabulate the Colburn factor [100 150 1000] (default) | vector of positive numbers
  group: Heat Transfer
- name: Colburn factor vector
  summary: Colburn factors at which the tabulated Reynolds numbers [0.019 0.013 0.002] (default) | vector of positive numbers
  group: Heat Transfer
- name: Reynolds number vector for Nusselt number
  summary: Reynolds number at which to tabulate the Nusselt number [100 150 100] (default) | vector of positive numbers
  group: Heat Transfer
- name: Prandtl number vector for Nusselt number
  summary: Prandtl numbers at which to tabulate the Nusselt number [1 10] (default) | vector of positive numbers
  group: Heat Transfer
- name: Nusselt number table
  summary: Nusselt numbers at the tabulated Reynolds and Prandtl numbers [ 3.72 4.21; 3.75 4.44; 4.21 7.15 ] (default) | matrix
    of positive numbers
  group: Heat Transfer
- name: Initial liquid temperature
  summary: Liquid temperature at start of simulation 293.15 K (default)
  group: Initial Conditions
- name: Initial liquid pressure
  summary: Pipe pressure at beginning of simulation 0.101325 MPa (default) | positive scalar
  group: Initial Conditions
- name: Nominal liquid temperature
  summary: Temperature at nominal operating conditions 293.15 K (default) | scalar
  group: Initial Conditions
- name: Nominal liquid pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Initial Conditions
```

### Configuration

### **Enable dynamic compressibility** — Whether to model fluid dynamic compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid
compressibility. When you select **Fluid
compressibility**, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure.

### **Enable fluid inertia** — Whether to model fluid acceleration `off` (default) | `on`

Whether to account for acceleration in the mass flow rate due to the
mass of the fluid.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Number of segments** — Pipe discretization `1` (default) | positive unitless scalar

Number of pipe divisions. Each division represents an individual
segment over which pressure is calculated, depending on the pipe inlet
pressure, fluid compressibility, and wall flexibility, if applicable.
The fluid volume in each segment remains fixed.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Pipe total length** — Total pipe length `5` `m` (default) | positive scalar in units of length

Total pipe length across all pipe segments.

### **Cross-sectional geometry** — Pipe geometry `Circular` (default) | `Annular` | `Rectangular` | `Elliptical` | `Isosceles triangular` | `Custom`

Cross-sectional pipe geometry. A nominal hydraulic diameter and
nominal cross-sectional area is calculated based on the cross-sectional
geometry.

### **Pipe diameter** — Pipe diameter `0.1 m` (default) | positive scalar

Diameter for circular cross-sectional pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Circular`.

### **Pipe inner diameter** — Pipe inner diameter `0.05 m` (default) | positive scalar

Inner diameter for annular pipe flow, or flow between two concentric
pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Annular`.

### **Pipe outer diameter** — Pipe outer diameter `0.1 m` (default) | positive scalar

Outer diameter for annular pipe flow, or flow between two concentric
pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Annular`.

### **Pipe width** — Rectangular pipe width `0.1 m` (default) | positive scalar

Width of rectangular pipe.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Rectangular`.

### **Pipe height** — Rectangular pipe height `0.1 m` (default) | positive scalar

Height of rectangular pipe.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Rectangular`.

### **Pipe major axis** — Elliptical pipe major axis `0.1 m` (default) | positive scalar

Major axis for elliptical pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Elliptical`.

### **Pipe minor axis** — Elliptical pipe minor axis `0.05 m` (default) | positive scalar

Minor axis for elliptical pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Elliptical`.

### **Pipe side length** — Triangular pipe side length `0.1 m` (default) | positive scalar

Length of the two equal sides of isosceles-triangular pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Isosceles
triangular`.

### **Pipe vertex angle** — Triangular pipe vertex angle `30 deg` (default) | positive scalar

Vertex angle for triangular pipes. The value must be less than 180
degrees.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Isosceles
triangular`.

### **Cross-sectional area** — Cross-sectional pipe area without deformation `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the pipe without deformations.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Custom`.

### **Hydraulic diameter** — Effective diameter of noncircular pipes `0.1128` `m` (default) | positive scalar in units of length

Effective diameter used in heat transfer, momentum balance, and pipe
flexibility equations. For noncircular pipes, the hydraulic diameter is
the effective diameter of the fluid in the pipe. For circular pipes, the
hydraulic diameter and pipe diameter are the same.

#### Dependencies

To enable this parameter, either:

- Clear the **Enable dynamic
  compressibility** check box and set
  **Cross-sectional geometry** to
  `Custom`.
- Select **Enable dynamic
  compressibility**, set the **Pipe
  wall specification** parameter to
  `Rigid` and set
  **Cross-sectional geometry** to
  `Custom`.

### **Elevation gain specification** — Set pipe elevation property `Constant` (default) | `Variable`

Set the pipe elevation as either `Constant`
or `Variable`. Selecting
`Variable` exposes the physical signal port
**EL**.

### **Elevation gain from port A to port B** — Change in elevation from port A to port B `0 m` (default) | positive scalar in units of length

Elevation differential for constant-elevation pipes.

#### Dependencies

To enable this parameter, set **Elevation gain
specification** to
`Constant`.

### **Gravitational acceleration specification** — Acceleration specification `Constant` (default) | `Variable`

Whether the gravitational acceleration is constant or variable.

### **Gravitational acceleration** — Acceleration due to gravity at mean pipe elevation `9.81` `m/s^2` (default) | scalar

Constant of the gravitational acceleration at the mean elevation of
the pipe.

#### Dependencies

To enable this parameter, set **Gravitational acceleration
specification** to
`Constant`.

### Viscous Friction

### **Viscous friction parameterization** — Friction model `Haaland correlation` (default) | `Nominal pressure drop vs. nominal mass flow rate` | `Tabulated data - Darcy friction factor vs. Reynolds number`

Parameterization of pressure losses due to wall friction. Both
analytical and tabular formulations are available.

### **Local resistances specification** — Method for quantifying pressure losses in the Haaland correlation `Aggregate equivalent length` (default) | `Local loss coefficient`

Method for quantifying pressure losses due to pipe
nonuniformities.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation`.

### **Total local loss coefficient** — Defines loss coefficient over the pipe `0.1` (default) | positive scalar

Loss coefficient associated with each pipe nonuniformity. You can
input a single loss coefficient or the sum of all loss coefficients
along the pipe.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Local resistance
specifications** to `Local loss
coefficient`.

### **Aggregate equivalent length of local resistances** — Minor pressure loss in the pipe expressed as a length `1` `m` (default) | positive scalar

Length of pipe that would produce the equivalent hydraulic losses as
would a pipe with bends, area changes, or other nonuniformities. The
effective length of the pipe is the sum of the **Pipe length** and the **Aggregate
equivalent length of local resistances**.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Local resistances
specification** to `Aggregate equivalent
length`.

### **Surface roughness specification** — Pipe material for roughness specification `Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um` (default) | `Steel and wrought iron : 46 um` | `Galvanized iron or steel : 152 um` | `Cast iron : 259 um` | `Custom`

Absolute surface roughness based on pipe material. The provided values
are ASHRAE standard roughness values. You can also input your own value
by setting **Surface roughness specification** to
`Custom`.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation`.

### **Internal surface absolute roughness** — Pipe wall absolute roughness `1.5e-5` `m` (default) | positive scalar in units of length

Pipe wall absolute roughness. This parameter is used to determine the
Darcy friction factor, which contributes to pressure loss in the
pipe.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Surface roughness
specification**
`Custom`.

### **Laminar friction constant for Darcy friction factor** — Friction constant for laminar flows `64` (default) | positive scalar

Friction constant for laminar flows. The Darcy friction factor
captures the contribution of wall friction in pressure loss
calculations. If **Cross-sectional geometry** is not
set to `Custom`, this parameter is internally
set to 64.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Custom`.

### **Laminar flow upper Reynolds number limit** — Reynolds number below which the flow is laminar `2e+3` (default) | positive scalar

Reynolds number below which the flow is laminar. Above this threshold,
the flow transitions to turbulent, reaching the turbulent regime at the
**Turbulent flow lower Reynolds number limit**
setting.

### **Turbulent flow lower Reynolds number limit** — Reynolds number above which the flow is turbulent `4e+3` (default) | positive scalar

Reynolds number above which the flow is turbulent. Below this
threshold, the flow gradually transitions to laminar, reaching the
laminar regime at the **Laminar flow upper Reynolds number
limit** setting.

### **Nominal mass flow rate** — Pipe mass flow rate `[0.1 1]` `kg/s` (default) | scalar or vector of numbers in units of mass/time

Pipe nominal mass flow rate used to calculate the pressure loss
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal pressure drop** parameter. When this
parameter is supplied as a vector, the scalar value *K*p is determined as
a least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Nominal pressure drop** — Pressure drop over the pipe `[0.001 0.01]` `MPa` (default) | scalar or vector of numbers in units of pressure

Pipe nominal pressure drop used to calculate the pressure loss
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal mass flow rate** parameter. When this
parameter is supplied as a vector, the scalar value *K*p is determined as
a least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Mass flow rate threshold for flow reversal** — Threshold below which numerical smoothing is applied `1e-6` `kg/s` (default) | positive scalar in units of mass/time

Mass flow rate threshold for reversed flow. A transition region is
defined around 0 kg/s between the positive and negative values of the
mass flow rate threshold. Within this transition region, numerical
smoothing is applied to the flow response. The threshold value must be
greater than 0.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Reynolds number vector for turbulent Darcy friction factor** — Reynolds numbers at which to tabulate the Darcy friction factor `[ 400 1000 1.5e+3 3e+3 4e+3 6e+3 1e+4 2e+4 4e+4 6e+4 1e+5 1e+8 ]` (default) | vector of positive numbers

Vector of Reynolds numbers for the tabular parameterization of the
Darcy friction factor. The vector elements form an independent axis with
the **Darcy friction factor vector**
parameter. The vector elements must be listed in ascending order and
must be greater than 0.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Tabulated data -
Darcy friction factor vs. Reynolds number`.

### **Darcy friction factor vector** — Darcy friction factors at the tabulated Reynolds numbers `[ 0.264 0.112 0.07099999999999999 0.0417 0.0387 0.0268 0.025 0.0232 0.0226 0.022 0.0214 0.0214 ]` (default) | vector of positive numbers

Vector of Darcy friction factors for the tabular parameterization of
the Darcy friction factor. The vector elements must correspond
one-to-one with the elements in the **Reynolds
number vector for turbulent Darcy friction factor**
parameter, and must be unique and greater than or equal to 0.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Tabulated data -
Darcy friction factor vs. Reynolds number`.

### Pipe Wall

### **Pipe wall specification** — Pipe wall flexibility `Rigid` (default) | `Flexible`

Wall flexibility of the pipe. This parameter is independent of pipe
cross-sectional geometry. The `Flexible`
setting preserves the initial pipe shape and applies equal expansion of
the cross-sectional area. The `Flexible`
setting may not be accurate for non-circular cross-sectional geometry
under high deformation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Volumetric expansion specification** — Linear expansion correlation `Cross-sectional area vs. pressure` (default) | `Cross-sectional area vs. pressure - Tabulated` | `Hydraulic diameter vs. pressure` | `Based on material properties`

Linear expansion correlation. The settings correlate the new
cross-sectional area or hydraulic diameter to the pipe pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to
`Flexible`.

### **Static gauge pressure to cross-sectional area gain** — Coefficient for area-dependent pipe deformation `1e-6 m^2/MPa` (default) | positive scalar

Coefficient for calculating pipe deformation. The block multiplies the
value of this parameter by the pressure differential between the segment
pressure and atmospheric pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Cross-sectional area vs.
pressure`.

### **Static gauge pressure vector** — Vector of gauge pressures `[.1,1] MPa` (default) | vector

Vector that contains the gauge pressures. The block uses this vector
in a table lookup to calculate the pipe cross-sectional area. The vector
entries must be strictly positive and monotonically increasing and the
vector must be the same length as the **Cross sectional area
gain vector** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Cross-sectional area vs. pressure -
Tabulated`.

### **Cross sectional area gain vector** — Vector of pipe cross-sectional areas `[1e-05, 1.1e-05] m^2` (default) | vector

Vector that contains the pipe cross-sectional areas. The block uses
this vector in a table lookup to calculate the pipe cross sectional-area
at other pressures. The vector entries must be strictly positive and
monotonically increasing and the vector must be the same length as the
**Static gauge pressure vector** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Cross-sectional area vs. pressure -
Tabulated`.

### **Static gauge pressure to hydraulic diameter gain** — Coefficient for diameter-dependent pipe deformation `1e-6 m/MPa` (default) | positive scalar

Coefficient for calculating the pipe deformation. The block multiplies
the value of this parameter by the pressure differential between the
segment pressure and atmospheric pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Hydraulic diameter vs.
pressure`.

### **Material behavior** — Method to specify material behavior `Linear Elastic` (default) | `Multilinear Elastic`

Method the block uses to calculate the material behavior.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Based on material properties`.

### **Pipe wall thickness** — Width of pipe wall `0.05 m` (default) | positive scalar

Thickness of the pipe wall. The block uses this value to calculate
stress.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Based on material properties`.

### **Young's modulus** — Young's modulus of pipe wall material `69 GPa` (default) | positive scalar

Young's modulus of the material that makes up the pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, and set **Pipe wall
specification** to `Flexible`,
**Volumetric expansion specification** to
`Based on material properties`, and
**Material behavior** to `Linear
Elastic`.

### **Poisson's ratio** — Poisson's ratio of pipe wall material `0.33` (default) | positive scalar

Poisson's ratio of the material that makes up the pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and set **Volumetric expansion specification** to
`Based on material properties`.

### **Stress vector** — Stress vector of pipe wall material `[276, 310] MPa` (default) | vector

Vector containing the stress values for the material that makes up the
pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to `Flexible`,
**Volumetric expansion specification** to
`Based on material properties`, and
**Material behavior** to
`Multilinear Elastic`.

### **Strain vector** — Strain vector of pipe wall material `[.004, .02]` (default) | vector

Vector containing the strain values for the material that makes up the
pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to `Flexible`,
**Volumetric expansion specification** to
`Based on material properties`, and
**Material behavior** to
`Multilinear Elastic`.

### **Check if stress exceeds specified allowable level** — Notification when stress is above specified max `None` (default) | `Warning` | `Error`

Whether the block does nothing, generates a warning, or generates an
error when the stress is above the maximum stress specified by the
**Maximum allowable stress** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to `Flexible`,
**Volumetric expansion specification** to
`Based on material properties`, and
**Material behavior** to
`Multilinear Elastic`.

### **Maximum allowable stress** — Maximum allowed stress on pipe wall `400 MPa` (default) | positive scalar

Maximum stress the block allows on the pipe wall. Control what the
block does if the stress exceeds this value with the **Check if
stress exceeds specified allowable level**
parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to `Flexible`,
**Volumetric expansion specification** to
`Based on material properties`,
**Material behavior** to
`Multilinear Elastic` and
**Check if stress exceeds specified allowable
level** to `Warning` or
`Error`.

### **Volumetric expansion time constant** — Pipe deformation time constant `0.01 s` (default) | positive scalar

Time required for the wall to reach steady-state after pipe
deformation. This parameter impacts the dynamic change in pipe
volume.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to
`Flexible`.

### **Pipe thermal expansion** — Whether to model thermal expansion `off` (default) | `on`

Whether to account for expansion in the pipe due to temperature
changes.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility** and set **Pipe wall
specification** to
`Flexible`.

### **Coefficient of thermal expansion** — Pipe coefficient of thermal expansion `24 um/(deltaK*m)` (default) | positive scalar

Coefficient of linear thermal expansion for the pipe material. This
value is the fractional change in size per degree change in temperature
at a constant pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and select **Pipe thermal expansion**.

### **Thermal expansion reference temperature** — Reference temperature for pipe thermal expansion `293.15 K` (default) | positive scalar

Reference temperature the block uses when calculating the thermal
expansion of the pipe.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**, set **Pipe wall
specification** to `Flexible`,
and select **Pipe thermal expansion**.

### Heat Transfer

### **Heat transfer parameterization** — Method by which to capture the convective heat transfer with the pipe wall `Gnielinski correlation``Nominal temperature differential vs. nominal mass flow rate` (default) | `Dittus-Boelter correlation` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`

Method of calculating the heat transfer coefficient between the fluid
and the pipe wall. Analytical and tabulated data parameterizations are
available.

### **Nusselt number for laminar flow heat transfer** — Nusselt number to use in the heat transfer calculations for laminar flows `3.66` (default)

Ratio of convective to conductive heat transfer in the laminar flow
regime. The fluid Nusselt number influences the heat transfer
rate.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Custom` and set
**Heat transfer parameterization** to either:

- `Gnielinski
  correlation`.
- `Nominal temperature differential vs.
  nominal mass flow rate`.
- `Dittus-Boelter
  correlation`.

### **Nominal mass flow rate** — Pipe mass flow rate `[0.1 1]` `kg/s` (default) | scalar or vector of numbers in units of mass/time

Pipe nominal mass flow rate used to calculate the heat transfer
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal inflow temperature** parameter. When
this parameter is supplied as a vector, the scalar value
*h*p is determined as a
least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Nominal temperature
differential vs. nominal mass flow rate`.

### **Nominal inflow temperature** — Pipe inlet temperature `[293.15 293.15]` `K` (default) | scalar or vector of numbers in units of temperature

Nominal fluid inlet temperature used to calculate the heat transfer
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal mass flow rate** parameter. When this
parameter is supplied as a vector, the scalar value *h*
is determined as a least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Nominal temperature
differential vs. nominal mass flow rate`.

### **Nominal outflow temperature** — Pipe outlet temperature `[300 300]` `K` (default) | scalar or vector of numbers in units of temperature

Nominal fluid outlet temperature used to calculate the heat transfer
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal mass flow rate** parameter. When this
parameter is supplied as a vector, the scalar value *h*
is determined as a least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Nominal temperature
differential vs. nominal mass flow rate`.

### **Nominal inflow pressure** — Pipe inlet pressure `[0.101325 0.101325]` `MPa` (default) | scalar or vector of numbers in units of pressure

Nominal fluid inlet pressure used to calculate the heat transfer
coefficient, specified as a scalar or a vector. All nominal values must
be greater than 0 and have the same number of elements as the **Nominal mass flow rate** parameter. When this
parameter is supplied as a vector, the scalar value *h*
is determined as a least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Nominal temperature
differential vs. nominal mass flow rate`.

### **Nominal wall temperature** — Pipe wall temperature `[303.15 303.15]` `K` (default) | scalar or vector of numbers in units of temperature

Pipe wall temperature used to calculate the heat transfer coefficient,
specified as a scalar or a vector. All nominal values must be greater
than 0 and have the same number of elements as the **Nominal mass flow rate** parameter. When this parameter is
supplied as a vector, the scalar value *h* is
determined as a least-squares fit of the vector elements.

#### Dependencies

To enable this temperature, set **Heat transfer
parameterization** to `Nominal temperature
differential vs. nominal mass flow rate`.

### **Coefficient a** — Empirical constant *a* of the Dittus-Boelter correlation `0.023` (default) | positive scalar

Empirical constant *a* to use in the Dittus-Boelter
correlation. The correlation relates the Nusselt number in turbulent
flows to the heat transfer coefficient.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Dittus-Boelter
correlation`.

### **Exponent b** — Empirical constant *b* of the Dittus-Boelter correlation `0.8` (default) | positive scalar

Empirical constant *b* to use in the Dittus-Boelter
correlation. The correlation relates the Nusselt number in turbulent
flows to the heat transfer coefficient.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Dittus-Boelter
correlation`.

### **Exponent c** — Empirical constant *c* of the Dittus-Boelter correlation `0.4` (default) | positive scalar

Empirical constant *c* to use in the Dittus-Boelter
correlation. The correlation relates the Nusselt number in turbulent
flows to the heat transfer coefficient. The default value reflects heat
transfer to the fluid.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Dittus-Boelter
correlation`.

### **Reynolds number vector for Colburn factor** — Reynolds numbers at which to tabulate the Colburn factor `[100 150 1000]` (default) | vector of positive numbers

Vector of Reynolds numbers for the tabular parameterization of the
Colburn factor. The vector elements form an independent axis with the
**Colburn factor vector** parameter.
The vector elements must be listed in ascending order and must be
greater than 0. This parameter must have the same number of elements as
the **Colburn factor vector**. For reversed
flows, or flows from **B** to **A**,
the same data is applied in the opposite direction.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Tabulated data -
Colburn factor vs. Reynolds number`.

### **Colburn factor vector** — Colburn factors at which the tabulated Reynolds numbers `[0.019 0.013 0.002]` (default) | vector of positive numbers

Vector of Colbrun factors for the tabular parameterization of the
Colburn factor. The vector elements form an independent axis with the
**Reynolds number vector for Colburn
factor** parameter. This parameter must have the same
number of elements as the **Reynolds number vector
for Colburn factor**.

#### Dependencies

This parameter is active when the **Heat transfer
parameterization** block parameter is set to
`Tabulated data - Colburn factor vs. Reynolds
number`.

### **Reynolds number vector for Nusselt number** — Reynolds number at which to tabulate the Nusselt number `[100 150 100]` (default) | vector of positive numbers

Vector of Reynolds numbers for the tabular parameterization of Nusselt
number. This vector forms an independent axis with the **Prandtl
number vector for Nusselt number** parameter for the 2-D
dependent **Nusselt number table**. The vector elements
must be listed in ascending order and must be greater than 0.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Tabulated data -
Nusselt number vs. Reynolds number & Prandtl
number`.

### **Prandtl number vector for Nusselt number** — Prandtl numbers at which to tabulate the Nusselt number `[1 10]` (default) | vector of positive numbers

Vector of Prandtl numbers for the tabular parameterization of Nusselt
number. This vector forms an independent axis with the
**Reynolds number vector for Nusselt number**
parameter for the 2-D dependent **Nusselt number
table**. The vector elements must be listed in ascending
order.

#### Dependencies

To enable this parameter, set **Heat transfer
parameterization** to `Tabulated data -
Nusselt number vs. Reynolds number & Prandtl
number`.

### **Nusselt number table** — Nusselt numbers at the tabulated Reynolds and Prandtl numbers `[ 3.72 4.21; 3.75 4.44; 4.21 7.15 ]` (default) | matrix of positive numbers

*M*-by-*N* matrix of Nusselt numbers
at the specified Reynolds and Prandtl numbers. Linear interpolation is
employed between table elements. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of vector elements in
  the **Reynolds number vector for Nusselt
  number** parameter.
- *N* is the number of vector elements in
  the **Prandtl number vector for Nusselt
  number** parameter.

#### Dependencies

To enable this parameter, **Heat transfer
parameterization** to `Tabulated data -
Nusselt number vs. Reynolds number & Prandtl
number`.

### Initial Conditions

### **Initial liquid temperature** — Liquid temperature at start of simulation `293.15` `K` (default)

Liquid temperature at the beginning of the simulation.

### **Initial liquid pressure** — Pipe pressure at beginning of simulation `0.101325 MPa` (default) | positive scalar

Pipe pressure at the beginning of the simulation.

#### Dependencies

To enable this parameter, set select **Enable dynamic
compressibility**.

### **Nominal liquid temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Liquid temperature at nominal operating conditions. The block uses
this value to calculate the nominal density to use in the mass and
energy conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy
conservation equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.
## Libraries

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2023b: Model a flexible pipe wall or variable gravitational acceleration

Set the **Pipe wall specification** parameter to
`Flexible` to model flexible pipe walls. This
parameterization also accounts for pipe wall deformation due to temperature
changes.

Set the **Gravitational acceleration specification** parameter to
`Variable` to enable port **G** and
provide gravitational acceleration as a physical signal.

### R2023b: Model pipe with length shorter than elevation gain

You can now model a pipe with length shorter than the elevation change when
**Elevation gain specification** is
`Constant`. The block issues a warning rather than an
error if the value of the **Elevation gain from port A to port B**
parameter is greater than the value of the **Pipe length**
parameter.

### R2023a: Model pipe characteristics

You can now use new parameters for the Pipe (TL) block to
control pipe attributes. Use the **Cross-sectional geometry**
parameter to specify the cross-sectional pipe shape. Use the **Surface
roughness specification** parameter to use the pipe wall material to
determine surface roughness.

## Description

Closed conduit that transports fluid between thermal liquid components

The Pipe (TL) block represents thermal liquid flow through a pipe. The
block finds the temperature across the pipe from the differential between ports, pipe
elevation, and any additional heat transfer at port **H**.

The pipe can have a constant or varying elevation between ports **A**
and **B**. For a constant elevation differential, use the
**Elevation gain from port A to port B** parameter. You can specify
a variable elevation by setting **Elevation gain specification** to
`Variable`. This exposes physical signal port
**EL**.

You can choose to include the effects of fluid dynamic compressibility, inertia, and
wall flexibility. When the block includes these phenomena, it calculates the flow
properties for each number of pipe segments that you specify.

### Pipe Geometry

Use the **Cross-sectional geometry** parameter to specify the
shape of the pipe.

**Circular**

The nominal hydraulic diameter, *DN*,
and the pipe diameter, *dcircle*, are
both equal to the is the value of the **Pipe diameter**
parameter. The pipe cross-sectional area is SN=π4dcircle2.

**Annular**

The nominal hydraulic diameter is the difference between the **Pipe
outer diameter** and **Pipe inner diameter**
parameters *DN* =
*douter* –
*dinner*. The pipe
cross-sectional area is SN=π4(douter2−dinner2).

**Rectangular**

The nominal hydraulic diameter is

DN=2hwh+w,

where:

- *h* is the is the value of the **Pipe
  height** parameter.
- *w* is the is the value of the **Pipe
  width** parameter.

The pipe cross-sectional area is SN=wh.

**Elliptical**

The nominal hydraulic diameter is

DN=2amajbmin(64-16(amaj-bminamaj+bmin)2)(amaj+bmin)(64-3(amaj-bminamaj+bmin)4),

where:

- *amaj* is the is the value
  of the **Pipe major axis** parameter.
- *bmin* is the is the value
  of the **Pipe minor axis** parameter.

The pipe cross-sectional area is SN=π4amajbmin.

**Isosceles Triangular**

The nominal hydraulic diameter is

DN=lsidesin(θ)1+sin(θ2),

where:

- *lside* is the is the
  value of the **Pipe side length** parameter.
- *θ* is the is the value of the **Pipe
  vertex angle** parameter.

The pipe cross-sectional area is SN=lside22sin(θ).

**Custom**

When the **Cross-sectional geometry** parameter is
`Custom`, you can specify the pipe cross-sectional
area with the **Cross-sectional area** parameter. The nominal
hydraulic diameter is the value of the **Hydraulic diameter**
parameter.

### Pipe Flexibility

You can model flexible walls for all cross-sectional geometries. When you set
**Pipe wall specification** to
`Flexible`, the block assumes uniform expansion along
all directions and preserves the defined cross-sectional shape. This setting may not
result in physical results for noncircular cross-sectional areas undergoing high
pressure relative to atmospheric pressure. When you model flexible walls, you can
use the **Volumetric expansion specification** parameter to specify
the volumetric expansion of the pipe cross-sectional area.

When the **Volumetric expansion specification** parameter is
`Cross-sectional area vs. pressure`, the change in
volume is

V˙=L(A−Sτ),

where:

- A=SN+Kps(p−patm).
- *L* is the **Pipe length**
  parameter.
- *SN* is the nominal pipe
  cross-sectional area defined for each shape.
- *S* is the current pipe cross-sectional area.
- *p* is the internal pipe pressure.
- *patm* is the atmospheric
  pressure.
- *K*ps is the **Static
  gauge pressure to cross-sectional area gain**
  parameter.

  To calculate *Kps* assuming
  uniform elastic deformation of a thin-walled, open-ended cylindrical
  pipe, use

  Kps=ΔDΔp=πDN34tE,

  where *t* is the pipe wall thickness
  and *E* is Young's modulus.
- *τ* is the **Volumetric expansion time
  constant**.

When the **Volumetric expansion specification** parameter is
`Cross-sectional area vs. pressure - Tabulated`, the
block uses the same equation for V˙ as the `Cross-sectional area vs.
pressure` setting. The block calculates *A* with
the table lookup function

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear),

where *pps* is the **Static gauge
pressure vector** parameter and
*Aps* is the **Cross sectional
area gain vector** parameter.

When the **Volumetric expansion specification** parameter is
`Hydraulic diameter vs. pressure`, the change in volume is

V˙=π2DL(Dstatic−Dτ),

where:

- Dstatic=DN+Kpd(p−patm).
- *DN* is the nominal hydraulic
  diameter defined for each shape.
- *D* is the current pipe hydraulic diameter.
- *Kpd* is the **Static
  gauge pressure to hydraulic diameter gain** parameter. To
  calculate *Kps* assuming uniform
  elastic deformation of a thin-walled, open-ended cylindrical pipe,
  use

  Kpd=ΔDΔp=DN22tE.

When the **Volumetric expansion specification** parameter is
`Based on material properties`, the block uses the same
equation for V˙ as the `Hydraulic diameter vs. pressure`
setting but calculates *Dstatic* depending
on the value of the **Material behavior** parameter

Dstatic=DN(1+ϵhoop).

This parameterization assumes a cylindrical thin-walled pressure vessel where σradial=0.

When the **Material behavior** parameter is `Linear
elastic`,

ϵhoop=1E[σhoop−vσlongitudinal],

where:

- *E* is the value of the **Young's
  modulus** parameter.
- *v* is the value of the  **Poisson's
  ratio** parameter.
- σhoop=pD2t, where *t* is the value of the
  **Pipe wall thickness** parameter.
- σlongitudinal=pD4t.

When the **Material behavior** parameter is
`Multilinear elastic`, the block calculates the von
Mises stress, *σv*, which simplifies to σv=34pD2t, to determine the equivalent strain. The hoop strain is

ϵhoop=ϵhoopelastic+ϵhoopplastic

ϵhoopelastic=1E[σhoop−vσlongitudinal]ϵhoopi,jplastic=32(1Es−1E)Si,j

where:

- The block calculates the Young's Modulus, *E*, from
  the first elements of the **Stress vector** and
  **Strain vector** parameters.
- ES=σtotalϵtotal, where
  *σtotal* and
  *εtotal* are the
  equivalent total stress and the equivalent total strain, respectively.
  The block calculates the equivalent total strain from the von Mises
  stress and the stress-strain curve.
- Si,j=σi,j−[σhoop+σlongitudinal+σradial3]δi,j, where *σi,j*
  are the elements of the Cauchy stress tensor.

If you do not model flexible walls, *SN*
= *S* and *DN* =
*D*.

**Pipe Wall Thermal Expansion**

If you select **Pipe thermal expansion**, the block models
the thermal expansion of the pipe wall using these assumptions:

- The pipe material is isotropic.
- The Biot number of the pipe is less than 0.1 and the pipe can be
  modeled with lumped thermal capacitance.
- The temperature change and pipe deformations are small enough that
  a first order approximation for area expansion is accurate.

When the **Material behavior** parameter is
`Cross-sectional area vs. pressure`,
`Cross-sectional area vs. pressure - Tabulated`, or
`Hydraulic diameter vs. pressure` and you select
**Pipe thermal expansion**, the block adds a thermal
expansion term when calculating area or diameter.

When **Material behavior** is `Cross-sectional
area vs. pressure`,

A=SN+Kps(p−patm)+SN2αΔT,

where:

- *ɑ* is the value of the **Coefficient of
  thermal expansion** parameter.
- ΔT=TI−Tref.
- *TI* is the fluid
  temperature at the internal node of the block.
- *Tref* is the value of the
  **Thermal expansion reference temperature**
  parameter.

When **Material behavior** is `Cross-sectional
area vs. pressure - Tabulated`,

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear)+SN2αΔT.

When **Material behavior** is `Hydraulic diameter
vs. pressure` ,

Dstatic=DN+Kpd(p−patm)+DNαΔT.

When the **Material behavior** parameter is
`Multilinear elastic` and you select **Pipe
thermal expansion**, the block calculates
*Dstatic* as

Dstatic=DN(1+ϵhoop+ϵthermal),

where ϵthermal=αΔT.

### Heat Transfer at the Pipe Wall

You can include heat transfer to and from the pipe walls in multiple ways. There
are two analytical models: the `Gnielinski correlation`,
which models the Nusselt number as a function of the Reynolds and Prandtl numbers
with predefined coefficients, and the `Dittus-Boelter correlation -
Nusselt = a*Re^b*Pr^c`, which models the Nusselt number as a
function of the Reynolds and Prandtl numbers with user-defined coefficients.

The `Nominal temperature differential vs. nominal mass flow
rate`, `Tabulated data - Colburn factor vs. Reynolds
number`, and `Tabulated data - Nusselt number vs.
Reynolds number & Prandtl number` are lookup table
parameterizations based on user-supplied data.

Heat transfer between the fluid and pipe wall occurs through convection,
*QConv* and conduction,
*QCond*, where the net heat flow
rate, *QH* is
*QH*=*QConv*+*QCond*.

Heat transfer due to conduction is:

QCond=kISHD(TH−TI),

where:

- *D* is the nominal hydraulic diameter,
  *DN*, if the pipe walls
  are rigid, and is the pipe steady-state diameter,
  *DS*, if the pipe walls
  are flexible.
- *kI* is the thermal
  conductivity of the thermal liquid, defined internally for each pipe
  segment.
- *SH* is the surface area of
  the pipe wall.
- *TH* is the pipe wall
  temperature.
- *TI* is the fluid temperature
  at the internal node of the block.

Heat transfer due to convection is:

QConv=cp,Avg|m˙Avg|(TH−TIn)[1−exp(−hSHcp,Avg|m˙Avg|)],

where:

- *c*p, Avg is the average fluid
  specific heat which the block calculates using a lookup table.
- m˙Avg is the average mass flow
  rate through the pipe.
- *TIn* is the fluid inlet port
  temperature.
- *h* is the pipe heat transfer coefficient.

The heat transfer coefficient *h* is:

h=NukAvgD,

except when parameterizing by `Nominal temperature
differential vs. nominal mass flow rate`, where
*kAvg* is the average thermal
conductivity of the thermal liquid over the entire pipe and *Nu* is
the average Nusselt number in the pipe.

**Analytical Parameterizations**

When **Heat transfer parameterization** is set to
`Gnielinski correlation` and the flow is turbulent,
the average Nusselt number is calculated as:

Nu=f8(Re−1000)Pr1+12.7( f8)1/2(Pr2/3−1),

where:

- *f* is the average Darcy friction factor,
  according to the Haaland correlation:

  f={−1.8log10[6.9Re+(ϵR3.7D)1.11]}-2,

  where
  *ε*R is the pipe
  **Internal surface absolute roughness**.
- *Re* is the Reynolds number.
- *Pr* is the Prandtl number.

When the flow is laminar, the data from [1]
determines how the Nusselt number depends on the **Cross-sectional
geometry** parameter:

- When **Cross-sectional geometry** is
  `Circular`, the Nusselt number is
  3.66.
- When **Cross-sectional geometry** is
  `Annular`, the block calculates the
  Nusselt number from tabulated data using a lookup table with linear
  interpolation and nearest extrapolation.

  | DinnerDouter | Nusselt number |
  | --- | --- |
  | 1/20 | 17.46 |
  | 1/10 | 11.56 |
  | 1/4 | 7.37 |
  | 1/2 | 5.74 |
  | 1 | 4.86 |

  The block adjusts the calculated Nusselt number with
  a correction factor F = 0.86(DouterDinner)0.16.
- When **Cross-sectional geometry** is
  `Rectangular`, the block calculates the
  Nusselt number from tabulated data using a lookup table with linear
  interpolation and nearest extrapolation.

  | min(h,w)max(h,w) | Nusselt number |
  | --- | --- |
  | 0 | 7.54 |
  | 1/8 | 5.60 |
  | 1/6 | 5.14 |
  | 1/4 | 4.44 |
  | 1/3 | 3.96 |
  | 1/2 | 3.39 |
  | 1 | 2.98 |
- When **Cross-sectional geometry** is
  `Elliptical`, the block calculates the
  Nusselt number from tabulated data using a lookup table with linear
  interpolation and nearest extrapolation.

  | bminamaj | Nusselt number |
  | --- | --- |
  | 1/16 | 3.65 |
  | 1/8 | 3.72 |
  | 1/4 | 3.79 |
  | 1/2 | 3.74 |
  | 1 | 3.66 |
- When **Cross-sectional geometry** is
  `Isosceles triangular`, the block
  calculates the Nusselt number from tabulated data using a lookup
  table with linear interpolation and nearest
  extrapolation.

  | θ | Nusselt number |
  | --- | --- |
  | 10π/180 | 1.61 |
  | 30π/180 | 2.26 |
  | 60π/180 | 2.47 |
  | 90π/180 | 2.34 |
  | 120π/180 | 2.00 |
- When **Cross-sectional geometry** is
  `Custom`, the Nusselt number is the
  value of the **Nusselt number for laminar flow heat
  transfer** parameter.

When **Heat transfer parameterization** is set to
`Dittus-Boelter correlation` and the flow is
turbulent, the average Nusselt number is calculated as:

Nu=aRebPrc,

where:

- *a* is the value of the **Coefficient
  a** parameter.
- *b* is the value of the **Exponent
  b** parameter.
- *c* is the value of the **Exponent
  c** parameter.

The block default Dittus-Boelter correlation is:

Nu=0.023Re0.8Pr0.4.

When the flow is laminar, the Nusselt number depends on the
**Cross-sectional geometry** parameter.

**Parameterization By Tabulated Data**

When the **Heat transfer parameterization** parameter is set
to `Tabulated data - Colburn factor vs. Reynolds
number`, the average Nusselt number is calculated as:

Nu=JM(Re)RePr1/3.

where *J*M is the
Colburn-Chilton factor.

When the **Heat transfer parameterization** parameter is set
to `Tabulated data - Nusselt number vs. Reynolds number &
Prandtl number`, the Nusselt number is interpolated from the
three-dimensional array of average Nusselt number as a function of both average
Reynolds number and average Prandtl number:

Nu=Nu(Re,Pr).

When the **Heat transfer parameterization** parameter is set
to `Nominal temperature difference vs. nominal mass flow
rate` and the flow is turbulent, the heat transfer coefficient
is calculated as:

h=hNDN1.8m˙N0.8m˙Avg0.8D1.8,

where:

- m˙N is the value of the
  **Nominal mass flow rate** parameter.
- m˙Avg is the average mass flow rate:

  m˙Avg=m˙A−m˙B2.
- *h*N is the nominal heat
  transfer coefficient, which is calculated as:

  hN=m˙Ncp,NSH,Nln(TH,N−TIn, NTH,N−TOut,N),

  where:

  - *SH,N* is the
    nominal wall surface area.
  - *TH,N* is the
    value of the **Nominal wall
    temperature** parameter.
  - *TIn,N* is the
    value of the **Nominal inflow
    temperature** parameter.
  - *TOut,N* is
    the value of the **Nominal outflow
    temperature** parameter.

This relationship is based on the assumption that the Nusselt
number is proportional to the Reynolds number:

hDk∝(m˙DSμ)0.8.

If the pipe walls are rigid, the expression for the heat
transfer coefficient becomes:

h=hNm˙N0.8m˙Avg0.8.

### Pipe Effects

The block lets you include dynamic compressibility and fluid inertia effects.
Turning on each of these effects can improve model fidelity at the cost of increased
equation complexity and potentially increased simulation cost:

- When you disable dynamic compressibility, the liquid is assumed to spend
  negligible time in the pipe volume. Therefore, there is no accumulation of
  mass in the pipe, and mass inflow equals mass outflow. This is the simplest
  option. It is appropriate when the liquid mass in the pipe is a negligible
  fraction of the total liquid mass in the system.
- When you enable dynamic compressibility, an imbalance of mass inflow and
  mass outflow can cause liquid to accumulate or diminish in the pipe. As a
  result, pressure in the pipe volume can rise and fall dynamically, which
  provides some compliance to the system and modulates rapid pressure changes.
  This is the default option.
- If dynamic compressibility is enabled, you can also turn on fluid inertia.
  This effect results in additional flow resistance, besides the resistance
  due to friction. This additional resistance is proportional to the rate of
  change of mass flow rate. Accounting for fluid inertia slows down rapid
  changes in flow rate but can also cause the flow rate to overshoot and
  oscillate. This option is appropriate in a very long pipe. Turn on fluid
  inertia and connect multiple pipe segments in series to model the
  propagation of pressure waves along the pipe, such as in the water hammer
  phenomenon.

### Pressure Loss Due to Friction

**Haaland Correlation**

The analytical Haaland correlation models losses due to wall friction either
by *aggregate equivalent length*, which accounts for
resistances due to nonuniformities as an added straight-pipe length that results
in equivalent losses, or by *local loss coefficient*, which
directly applies a loss coefficient for pipe nonuniformities.

When the **Local resistances specification** parameter is set
to `Aggregate equivalent length` and the flow in the
pipe is lower than the **Laminar flow upper Reynolds number
limit**, the pressure loss over all pipe segments is:

Δpf,A=υλ2D2SL+Ladd2m˙A,

Δpf,B=υλ2D2SL+Ladd2m˙B,

where:

- *ν* is the fluid kinematic viscosity.
- *λ* is the value of the **Laminar
  friction constant for Darcy friction factor**
  parameter, which you can define when the **Cross-sectional
  geometry** parameter is
  `Custom` and is otherwise equal to
  64.
- *D* is the pipe hydraulic diameter.
- *L*add is the value of the
  **Aggregate equivalent length of local
  resistances** parameter.
- m˙A is the mass flow rate at
  port **A**.
- m˙B is the mass flow rate at
  port **B**.

When the Reynolds number is greater than the **Turbulent
flow lower Reynolds number limit**, the pressure loss in the pipe is:

Δpf,A=f2ρIDS2L+Ladd2m˙A|m˙A|,

Δpf,B=f2ρIDS2L+Ladd2m˙B|m˙B|,

where:

- *f* is the Darcy friction factor. This is
  approximated by the empirical Haaland equation and is based on the
  **Surface roughness specification**,
  *ε*, and pipe hydraulic diameter:

  f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

  Pipe roughness for brass, lead, copper, plastic,
  steel, wrought iron, and galvanized steel or iron are provided as
  ASHRAE standard values. You can also supply your own
  **Internal surface absolute roughness** with
  the `Custom` setting.
- *ρ*I is the internal fluid
  density.

When the **Local resistances specification** parameter is set
to `Local loss coefficient` and the flow in the pipe is
lower than the **Laminar flow upper Reynolds number limit**,
the pressure loss over all pipe segments is:

Δpf,A=υλ2D2SL2m˙A.

Δpf,B=υλ2D2SL2m˙B.

When the Reynolds number is greater than the
**Turbulent flow lower Reynolds number limit**, the
pressure loss in the pipe is:

Δpf,A=(fL2D+Closs,total)12ρIS2m˙A|m˙A|,

Δpf,B=(fL2D+Closs,total)12ρIS2m˙B|m˙B|,

where *C*loss,total
is the loss coefficient, which can be defined in the **Total local loss
coefficient** parameter as either a single coefficient or the sum
of all loss coefficients along the pipe.

**Nominal Pressure Drop vs. Nominal Mass Flow Rate**

The Nominal Pressure Drop vs. Nominal Mass Flow Rate parameterization
characterizes losses with a loss coefficient for rigid or flexible walls. When
the fluid is incompressible, the pressure loss over the entire pipe due to wall
friction is:

Δpf,A=Kpm˙Am˙A2+m˙th2,

where *K*p is:

Kp=ΔpNm˙N2,

where:

- *Δp*N is the
  **Nominal pressure drop**, which can be defined
  either as a scalar or a vector.
- m˙N is the **Nominal mass flow
  rate**, which can be defined either as a scalar or a
  vector.

When you supply the **Nominal pressure drop**
and **Nominal mass flow rate** parameters as vectors, the
scalar value *Kp* is determined from a
least-squares fit of the vector elements.

**Tabulated Data – Darcy Friction Factor vs. Reynolds Number**

Pressure losses due to viscous friction can also be determined from
user-provided tabulated data of the **Darcy friction factor
vector** and the **Reynolds number vector for turbulent
Darcy friction factor** parameters. Linear interpolation is
employed between data points.

### Momentum Balance

The pressure differential over the pipe is due to the pressure at the pipe ports,
friction at the pipe walls, and hydrostatic changes due to any change in elevation:

pA−pB=Δpf+ρIgΔz,

where:

- *pA* is the pressure at a port
  **A**.
- *pB* is the pressure at a port
  **B**.
- *Δpf* is the pressure
  differential due to viscous friction,
  *Δpf,A+Δpf,B*.
- *g* is the value of the **Gravitational
  acceleration** parameter or the signal at port
  **G**.
- *Δz* the elevation differential between port
  **A** and port **B**.
- *ρI* is the internal fluid
  density, which is measured at each pipe segment. If fluid dynamic
  compressibility is not modeled, this is:

  pI=pA+pB2.

When fluid inertia is not modeled, the momentum balance between port
**A** and internal node I is:

pA−pI=Δpf,A+ρIgΔz2.

When fluid inertia is not modeled, the momentum balance between port
**B** and internal node I is:

pB−pI=Δpf,B−ρIgΔz2.

When fluid inertia is modeled, the momentum balance between port
**A** and internal node I is:

pA−pI=Δpf,A+ρIgΔz2+m¨ASL2,

where:

- m¨A is the fluid inertia at port
  **A**.
- *L* is the value of the **Pipe
  length** parameter.
- *S* is the value of the **Nominal
  cross-sectional area** parameter.

When fluid inertia is modeled, the momentum balance between port
**B** and internal node I is:

pB−pI=Δpf,B−ρIgΔz2+m¨BSL2,

where

m¨B is the fluid inertia at port
**B**.

### Pipe Discretization

You can divide the pipe into multiple segments. If a pipe has more than one
segment, the mass flow, energy flow, and momentum balance equations are calculated
for each segment. Having multiple pipe segments can allow you to track changes to
variables such as fluid density when fluid dynamic compressibility is
modeled.

If you would like to capture specific phenomena in your application, such as water
hammer, choose a number of segments that provides sufficient resolution of the
transient. The following formula, from the Nyquist sampling theorem, provides a rule
of thumb for pipe discretization into a minimum of *N* segments:

N=2Lfc,

where:

- *L* is the **Pipe length**.
- *f* is the transient frequency.
- *c* is the speed of sound.

For some applications, you may need to connect Pipe
(TL) blocks in series. For example, you may require multiple
pipe segments to define a thermal boundary condition along the length of a pipe. In
this case, model the pipe segments by using a Pipe
(TL) block for each segment and use the thermal ports to set the
thermal boundary condition.

### Mass Balance

For a rigid pipe with an incompressible fluid, the pipe mass conversation equation is:

m˙A+m˙B=0,

where:

- m˙A is the mass flow rate at port
  **A**.
- m˙B is the mass flow rate at port
  **B**.

For a flexible pipe with an incompressible fluid, the pipe mass conservation
equation is:

m˙A+m˙B=ρIV˙,

where:

- *ρI* is the thermal liquid
  density at internal node I. Each pipe segment has an internal
  node.
- V˙ is the rate of deformation of the pipe volume.

For a flexible pipe with a compressible fluid, the mass within the
pipe can change with pressure and temperature. The bulk modulus and thermal
expansion coefficient of the thermal liquid account for this dependence and the pipe
mass conservation equation is:

m˙A+m˙B=ρIV˙+ρIV(p˙IβI+αIT˙I),

where:

- *pI* is the thermal liquid
  pressure at the internal node I.
- T˙I is the rate of change of the
  thermal liquid temperature at the internal node I.
- *βI* is the thermal liquid
  bulk modulus.
- *αI* is the liquid thermal
  expansion coefficient.

### Energy Balance

The energy accumulation rate in the pipe at internal node I is defined as:

E.=ϕA+ϕB+QH−m˙AvggΔz,

where:

- *ϕA* is the energy flow rate
  at port **A**.
- *ϕB* is the energy flow rate
  at port **B**.
- *QH* is the heat transfer
  through the pipe wall.

If the fluid is incompressible, the expression for energy accumulation rate is

E˙=ρ0cpIVdTIdt,

where:

- *cpI*
  is the fluid specific heat at the internal node of the block.
- *V* is the pipe volume.
- *ρ0* is the constant fluid
  density. The block calculates this value from the **Nominal
  liquid temperature** and **Nominal liquid
  pressure** parameters.

If the fluid is compressible, the expression for energy accumulation rate is

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV,

where:

∂(ρIuI)∂p|T=(ρIhIβI−TIαI)V∂(ρIuI)∂T|p=(cpI−hIαI)V

and *hI* is the specific
enthalpy at the internal node of the block.

If the fluid is compressible and the pipe walls are flexible, the expression for
energy accumulation rate is

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV+ρIhIdVdt.
