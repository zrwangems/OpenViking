---
type: simulink-block
title: 'Torque Converter'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'torqueconverter'
documentation_source_path: 'ref/torqueconverter.html'
language: en
---

# Torque Converter

## Ports
```yaml
ports:
- name: I
  summary: Impeller mechanical rotational
  direction: conserving
- name: T
  summary: Turbine mechanical rotational
  direction: conserving
```

### Conserving

### **I** — Impeller mechanical rotational

Mechanical rotational conserving port associated with the impeller.

### **T** — Turbine mechanical rotational

Mechanical rotational conserving port associated with turbine.
## Parameters
```yaml
parameters:
- name: Coast mode modeling
  summary: Coast transition simulation option Two-mode (default) | Continuous
  group: Torque Characteristics
- name: Drive mode speed ratio vector
  summary: Turbine speed to impeller speed ratios [0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1] (default) | vector
  group: Torque Characteristics
- name: Drive mode torque ratio vector
  summary: Turbine torque to impeller torque ratios [2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, 1, 1, 1, 1] (default)
    | vector
  group: Torque Characteristics
- name: Drive mode capacity factor vector
  summary: Capacity factors of drive mode 1e-4 * [.72558, .66322, .63463, .59042, .51331, .4144, .29287, .22444, .12186, .04386,
    0] m*N/rpm^2 (default) | vector
  group: Torque Characteristics
- name: Coast mode speed ratio vector
  summary: Impeller speed to turbine speed ratios [0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1] (default) | vector
  group: Torque Characteristics
- name: Coast mode capacity factor vector
  summary: Capacity factors of coast mode 1e-4 * [.5079, .4643, .4442, .4133, .3593, .2901, .205, .1571, .0853, .0307, 0]
    m*N/rpm^2 (default) | vector
  group: Torque Characteristics
- name: Initial mode
  summary: Initial mode of simulation Drive mode (default) | Coast mode
  group: Torque Characteristics
- name: Mode transition threshold
  summary: Threshold of mode transition 1 rpm (default) | positive scalar
  group: Torque Characteristics
- name: Speed ratio vector
  summary: Turbine speed to impeller speed ratios [0, .5, .6, .7, .8, .87, .92, .94, .96, .97] (default) | vector of ascending
    nonnegative elements
  group: Torque Characteristics
- name: Torque ratio vector
  summary: Turbine torque to impeller torque ratios [2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, .9983, .9983,
    .9983, .9983] (default) | vector of ascending positive elements
  group: Torque Characteristics
- name: Capacity factor parameterization
  summary: Capacity factor definition Ratio of speed to square root of impeller torque (default) | Ratio of impeller torque
    to square of speed
  group: Torque Characteristics
- name: Capacity factor reference speed
  summary: Capacity factor reference speed option Always impeller speed (default) | Turbine speed for speed ratios greater
    than one
  group: Torque Characteristics
- name: Capacity factor vector
  summary: Capacity factors [12.2938, 12.8588, 13.1452, 13.6285, 14.6163, 16.2675, 19.3503, 22.1046, 29.9986, 50] rad/(N^(1/2)*m^(1/2)*s)
    (default) | vector
  group: Torque Characteristics
- name: Model transmission lag
  summary: Transmission lag setting No lag – Suitable for HIL simulation (default) | Specify time constant and initial value
  group: Dynamics
- name: Torque transmission time constant
  summary: Time constant of torque transmission .02 s (default) | positive scalar
  group: Dynamics
- name: Initial turbine-to-impeller torque ratio
  summary: Initial torque ratio of turbine to impeller 0 (default) | nonnegative scalar
  group: Dynamics
- name: Interpolation method
  summary: Interpolation method of lookup function Linear (default) | Smooth
  group: Dynamics
- name: Extrapolation method
  summary: Extrapolation method of lookup function Linear (default) | Nearest | Error
  group: Dynamics
```

### Torque Characteristics

### **Coast mode modeling** — Coast transition simulation option `Two-mode` (default) | `Continuous`

Coast mode transition method. When you select
`Continuous`, the block smoothly transitions between drive
and coast mode but has reduced accuracy and robustness when modeling near the
transition. When you select `Two-mode`, the block uses mode
charts, which promote better robustness and accuracy when the mode transitions.

### **Drive mode speed ratio vector** — Turbine speed to impeller speed ratios `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]` (default) | vector

Speed ratios, Rω, of the drive mode. The vector elements must be in ascending order,
start at 0, and end at 1.

Rω=ωT/ωI

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Drive mode torque ratio vector** — Turbine torque to impeller torque ratios `[2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, 1, 1, 1, 1]` (default) | vector

Torque ratios, Rτ, of the drive mode. Each element of the vector must be greater than
or equal to 1, and the last element must be 1. The block defines the torque ratio of
the drive mode as:

Rτ=τT/τI

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Drive mode capacity factor vector** — Capacity factors of drive mode `1e-4 * [.72558, .66322, .63463, .59042, .51331, .4144, .29287, .22444, .12186, .04386, 0]` `m*N/rpm^2` (default) | vector

Capacity factors,K\*, of the drive mode. Each element of the vector must be nonnegative,
and the last element must be 0. The block defines the capacity factory of the drive
mode as:

K\*=τI/ωI2

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Coast mode speed ratio vector** — Impeller speed to turbine speed ratios `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]` (default) | vector

Speed ratios, R^ω, of the coast mode. The vector elements must be in ascending order,
start at 0, and end at 1. The block defines the speed ratio of the coast mode
as:

R^ω=ωI/ωT

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Coast mode capacity factor vector** — Capacity factors of coast mode `1e-4 * [.5079, .4643, .4442, .4133, .3593, .2901, .205, .1571, .0853, .0307, 0]` `m*N/rpm^2` (default) | vector

Capacity factors, K^\*, of the coast mode. Each element of the vector must be nonnegative,
and the last element must be 0. The block defines the capacity factor of the coast
mode as:

K^\*=τT/ωT2

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Initial mode** — Initial mode of simulation `Drive mode` (default) | `Coast mode`

Initial mode of the simulation, specified as either `Drive
mode` or `Coast mode`.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Mode transition threshold** — Threshold of mode transition `1` `rpm` (default) | positive scalar

Mode transition threshold of the simulation. Setting a threshold for the mode
transition can increase the simulation robustness by avoiding high-frequency mode
switching.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Two-mode`.

### **Speed ratio vector** — Turbine speed to impeller speed ratios `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97]` (default) | vector of ascending nonnegative elements

Speed ratios, Rω, of the torque converter. Each element of the vector must be in
ascending order and nonnegative. The block defines the speed ratio as Rω=ωT/ωI. If *Rω* exceeds the last
element, the block extrapolates according to the **Extrapolation
method** parameter.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Continuous`.

### **Torque ratio vector** — Turbine torque to impeller torque ratios `[2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, .9983, .9983, .9983, .9983]` (default) | vector of ascending positive elements

Torque ratios, Rτ, of the torque converter. Each element of the vector must be
positive. The block defines the torque ratio as Rτ=τT/τI. If *Rω* exceeds the last
element of the **Speed ratio vector** parameter, the block
extrapolates according to the **Extrapolation method**
parameter.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Continuous`.

### **Capacity factor parameterization** — Capacity factor definition `Ratio of speed to square root of impeller torque` (default) | `Ratio of impeller torque to square of speed`

Definition of the capacity factor.

| `Ratio of speed to square root of impeller torque` | `Ratio of impeller torque to the square of the speed` |
| --- | --- |
| K=ω/τI | K\*=τI/ω2 |

When you select `Ratio of impeller torque to square of
speed`, the default value is `1e-3 * [6.616, 6.048, 5.787,
5.384, 4.681, 3.779, 2.671, 2.047, 1.111, .4]`
`N*m/(rad/s)^2`.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Continuous`.

### **Capacity factor reference speed** — Capacity factor reference speed option `Always impeller speed` (default) | `Turbine speed for speed ratios greater than one`

Whether to always use the impeller speed as the reference speed or to use the
turbine speed when speed ratios are greater than one.

- `Always impeller speed`: Use impeller speed ωI for all values of Rω.
- `Turbine speed for speed ratios greater than one`:
  Use impeller speed ωI for all values of Rω < 1, and use turbine speed ωT when Rω > 1.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Continuous`.

### **Capacity factor vector** — Capacity factors `[12.2938, 12.8588, 13.1452, 13.6285, 14.6163, 16.2675, 19.3503, 22.1046, 29.9986, 50]` `rad/(N^(1/2)*m^(1/2)*s)` (default) | vector

Capacity factors of the torque converter. The block defines the capacity factor
according to the table:

**Note**

If you do not specify capacity factor data for a speed ratio of 1, the block
uses a capacity factor value of 10\**KMax*, where *K*Max is the
maximum value in the specified capacity factor vector. The corresponding torque
ratio is assumed to be 0. For all other speed ratio values not explicitly
specified in the lookup table data, the block uses the interpolation or
extrapolation method specified by the **Interpolation method**
or **Extrapolation method** parameter, respectively.

#### Dependencies

To enable this parameter, set **Coast mode modeling** to
`Continuous`.

### Dynamics

To enable these parameters, set **Coast mode modeling** parameter to
`Continuous`

### **Model transmission lag** — Transmission lag setting `No lag – Suitable for HIL simulation` (default) | `Specify time constant and initial value`

Whether to include transmission lag in the simulation. When you select:

- `No lag – Suitable for HIL simulation`, torque
  transfer is instantaneous. When there is no time lag, the input impeller torque, τI, and output turbine torque, τT, are:

  τI=sgn(1−ωT/ωI)(ωI/K)2

  τT=τTRτ
- `Specify time constant and initial value`, the
  block transfers torque with a time lag. If you select this option, you can
  specify the **Torque transmission time constant** and
  **Initial turbine-to-impeller torque ratio**
  parameters.

### **Torque transmission time constant** — Time constant of torque transmission `.02` `s` (default) | positive scalar

Torque transmission time. The time lag increases model fidelity and computational
cost. See Adjust Model Fidelity for more information.

#### Dependencies

To enable this parameter, set **Model transmission lag** to
`Specify time constant and initial value`.

### **Initial turbine-to-impeller torque ratio** — Initial torque ratio of turbine to impeller `0` (default) | nonnegative scalar

Initial torque ratio of the turbine to the impeller.

#### Dependencies

To enable this parameter, set **Model transmission lag** to
`Specify time constant and initial value`.

### **Interpolation method** — Interpolation method of lookup function `Linear` (default) | `Smooth`

Interpolation method of the lookup function, specified as either
`Linear` or `Smooth`. The method
interpolates torque ratio and capacity factor functions between the discrete relative
velocity values in the definition range. For more information about
`Linear` and `Smooth`, see `tablelookup`.

### **Extrapolation method** — Extrapolation method of lookup function `Linear` (default) | `Nearest` | `Error`

Extrapolation method of the lookup function, specified as
`Linear`, `Smooth`, or
`Error`. The method extrapolates torque ratio and capacity
factor functions. For more information about, see `tablelookup`.
## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2020b: Simulate Coast Mode with Mode Charts

To use mode charts to improve simulation robustness during mode transitions, set
**Coast mode modeling** to `Two-mode`.

## Description

Torque converter coupling between two drive shafts

The Torque Converter block represents an automotive torque
converter that comprises an impeller, a turbine, and a stator. The impeller and the turbine
make up the fluid coupling, and the stator increases torque by redirecting the flow returning
to the impeller. As the shaft turns the impeller, centrifugal force flings the fluid outward
toward the turbine blades, which causes the turbine to spin as the fluid proceeds to the
center and out toward the stator. Use the block to connect an engine to an automatic
transmission. Connect port **I** to the engine and port **T** to the transmission.

Cross-section of a torque converter. The flow moves continuously from the impeller blades to the turbine blades and then back to the impeller blades via the stator.

By default, the block constrains τT, the torque at port **T**, and τI, the torque at port **I**, to one another for a given time step.
You can optionally include the effect of torque transmission time lag that is caused by
internal fluid flow and compressibility. To include transmission lag, set **Model
transmission lag** to `Specify time constant and initial
value`. The block introduces the lag and finds the steady state torque at port
**I** such that

tc(dτI/dt)+τI=τI(steadystate).

The instantaneous function of the capacity factor *K*
determines the steady-state value of *τI*. The block
operates in drive mode when power flows from port **I** to port **T**. The
block operates in coast mode when power flows in reverse. You can simulate the coast mode
transition continuously or by using mode charts. The block uses the capacity factor for the
torque converter to calculate torque from angular speed.

### Two Mode Coast Transition

When you set **Coast mode modeling** to `Two
mode`, the block uses separate modes for coasting or driving. The block
computes the torque from angular speed such that

τ=K\*ω2,

where *K\** is the
**Drive mode capacity factor vector** parameter and
*ω* is the angular speed for either port **I** or port
**T**. The capacity factor is a function of the speed ratio. When in drive mode,
the block defines the speed ratio as

Rω=ωT/ωI,

where *ωT* and
*ωI* represent the speeds at ports
**T** and **I**, respectively. When in coast mode, the block defines the
speed ratio as

R^ω=ωI/ωT.

Because of the different speed ratio definitions, the block also uses a
separate capacity factor for the coast mode, K^\*, which is the **Coast mode capacity factor vector**
parameter. The **Mode transition parameter** determines the speed at
which the block changes modes. The graphic illustrates the two modes.Mode chart diagram where the drive mode and coast mode share a transition region. The turbine and impeller speeds match. At the coast mode extreme, the impeller speed is zero. At the drive mode extreme, the turbine speed is zero.

### Continuous Coast Transition

When you set **Coast mode modeling** to
`Continuous`, the block smoothly transitions between drive and
coast mode. You can also add dynamics. The block simulation is less accurate when operating
near the transition region.

The block defines the speed ratio as Rω=ωT/ωI and the torque ratio as Rτ=τT/τI. The **Capacity factor parameterization** parameter
controls how the block defines the capacity factor. When you select:

- `Ratio of speed to square root of impeller torque`, the
  block uses K=ω/τI.
- `Ratio of impeller torque to square of speed`, the block
  uses K\*=τI/ω2.

To improve fidelity, you can include lag due to the transmission in your
simulation. When you set **Model transmission lag** to
`Specify time constant and initial value`, the block adds a
constant time delay to the torque transfer.

When you set **Coast mode modeling** to
`Continuous`:

- The impeller shaft must always rotate in a positive direction. Simulation is not
  valid for ωI < 0.
- If you drive the Torque Converter block by using a
  torque source, such as the Generic Engine block, you must include an inertia in the source to
  represent the engine, shaft inertia, or other source components. To ensure that the
  impeller starts by rotating in a positive direction, set the initial speed for this
  inertia to a positive value.
