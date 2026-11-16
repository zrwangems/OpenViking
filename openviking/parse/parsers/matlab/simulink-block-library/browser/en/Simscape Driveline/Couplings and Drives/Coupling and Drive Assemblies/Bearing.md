---
type: simulink-block
title: 'Bearing'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Coupling and Drive Assemblies'
documentation_page: 'bearing'
documentation_source_path: 'ref/bearing.html'
language: en
---

# Bearing

## Ports

### Input

### **Load** — Variable load input, N physical signal

Physical signal input port associated with the load on the bearing, in
N.

#### Dependencies

To enable this port, set **Radial load
specification** to
`Variable`.
### Conserving

### **B** — Base mechanical rotational

Mechanical rotational conserving port associated with the base end of
the shaft.

### **F** — Follower mechanical rotational

Mechanical rotational conserving port associated with the follower end
of the shaft. This port maintains the same angular velocity as port
**B**.

#### Dependencies

To enable this port, select **Enable follower
port**.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the bearing casing. When this port
is enabled, the block assumes the casing reference is stationary.

#### Dependencies

To enable this port, select **Enable case
port**.

## Parameters

### Mechanical Properties

### **Bearing type** — Bearing option `Ball or Roller` (default) | `Journal`

Type of bearing that the block behaves as during the
simulation.

### **Enable follower port** — Follower port option `off` (default) | `on`

Whether to enable the follower port.

### **Enable case port** — Case port option `off` (default) | `on`

Whether to enable the case port.

### **Radius** — Bearing interface radius `30` `mm` (default) | positive scalar

Radius of the interface between the bearing and the shaft.

### **Length** — Bearing interface length `100` `mm` (default) | positive scalar

Length of the interface between the bearing and the shaft.

### **Radial load specification** — Option to control radial load `Constant` (default) | `Variable`

Whether the block uses a constant load or you specify a variable load using the
**Load** port.

### **Load on bearing** — Constant bearing load `10` `N` (default) | positive scalar

Constant load that the shaft imparts on the bearing.

#### Dependencies

To enable this parameter, set **Radial load
specification** to
`Constant`.

### **Force threshold** — Load threshold `0.001` `N` (default)

Load threshold above which the block applies a load to the
bearing.

#### Dependencies

To enable this parameter, set **Radial load
specification** to
`Variable`.

### **Angular velocity threshold** — Angular velocity threshold `0.001` `rev/s` (default)

Angular velocity threshold above which the block applies bearing
friction.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Ball or Roller`.

### **Coefficient of friction specification** — Option to specify coefficient of friction `Constant` (default) | `Variable`

Whether the block coefficient is constant or varies with the bearing speed.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Ball or Roller` and
**Coefficient of friction specification** to
`Constant`.

### **Coefficient of friction** — Coefficient of friction `0.002` (default) | positive scalar

Constant coefficient of friction.

#### Dependencies

To enable this parameter, set **Coefficient of friction
specification** to
`Constant`.

### **Interpolation method** — Method of interpolation between breakpoint values `Linear` (default) | `Smooth`

Method to use for lookup table breakpoint interpolation. The block
uses the `tablelookup` function to model nonlinearity
by using array data to map input values to output values:

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to
  produce a continuous curve with continuous first-order
  derivatives.

For more information, see `tablelookup`.

### **Extrapolation method** — Method of handling input values that fall outside range of breakpoint data set `Linear` (default) | `Nearest` | `Error`

Method to use for lookup table breakpoint extrapolation. This method
determines the output value when the input value is outside the range
specified in the argument list. The block uses the
`tablelookup` function to model nonlinearity by
using array data to map input values to output values:

- `Linear` — Select this option to
  produce a curve with continuous first-order derivatives in
  the extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Select this option to
  produce an extrapolation that does not go above the highest
  point in the data or below the lowest point in the
  data.
- `Error` — Select this option to
  avoid extrapolating when you want your data to be within the
  table range. If the input signal is outside the range of the
  table, the simulation stops and generates an error.

### **Bearing angular speed vector, ω** — Bearing angular velocity `[10, 2500, 5000, 10000, 25000]` `rpm` (default) | vector of length *N*

Bearing angular velocity.

### **Coefficient of friction, f(ω)** — Coefficient of friction `[.004, .001, .0005, .00025, .000125]` (default) | vector of length *N*

Coefficient of friction for a given bearing angular velocity. The
elements in this vector must correspond one-to-one with the
**Bearing angular speed vector, ω**
parameter.

### Fluid Properties

To enable these parameters, set **Bearing type** to
`Journal`.

### **Customize friction curve** — Option to customize bearing friction curve `off` (default) | `on`

Whether to customize the bearing friction curve.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal`.

### **Dynamic viscosity** — Lubricant dynamic viscosity `0.29` `Pa*s` (default) | positive scalar

Dynamic viscosity of the bearing lubricant.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal`.

### **Minimum coefficient of friction** — Minimum coefficient of friction `0.002` (default) | positive scalar

Lowest coefficient of friction the block uses for any angular
velocity.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal`.

### **Bearing Modulus** — Journal bearing modulus `7.2519e-08` `rev` (default) | positive scalar

Journal bearing modulus.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal` and select
**Customize friction curve**.

### **Normalized Hersey number vector** — Normalized Hersey number `[.4306, .6124, .6651, .7512, .866, 1, 1.1962, 1.4354, 3.8517]` (default) | vector of length *M*

Normalized Hersey number.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal` and select
**Customize friction curve**.

### **Normalized viscous coefficient vector** — Normalized viscous friction coefficient `[3.6621, 1.672, 1.3397, 1.1811, 1.0743, 1, 1.0358, 1.1173, 2.2792]` (default) | vector of length *M*

Normalized viscous friction coefficients. The elements in this vector
correspond one-to-one with the **Normalized Hersey number
vector** parameter.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal` and select
**Customize friction curve**.

### **Interpolation method** — Method of interpolation between breakpoint values `Linear` (default) | `Smooth`

Method to use for lookup table breakpoint interpolation. The block
uses the `tablelookup` function to model nonlinearity
by using array data to map input values to output values:

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to
  produce a continuous curve with continuous first-order
  derivatives.

For more information, see `tablelookup`.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal` and select
**Customize friction curve**.

### **Extrapolation method** — Method of handling input values that fall outside range of breakpoint data set `Linear` (default) | `Nearest` | `Error`

Method to use for lookup table breakpoint extrapolation. This method
determines the output value when the input value is outside the range
specified in the argument list. The block uses the
`tablelookup` function to model nonlinearity by
using array data to map input values to output values:

- `Linear` — Select this option to
  produce a curve with continuous first-order derivatives in
  the extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Select this option to
  produce an extrapolation that does not go above the highest
  point in the data or below the lowest point in the
  data.
- `Error` — Select this option to
  avoid extrapolating when you want your data to be within the
  table range. If the input signal is outside the range of the
  table, the simulation stops and generates an error.

#### Dependencies

To enable this parameter, set **Bearing type** to
`Journal` and select
**Customize friction curve**.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Damping fault** — Option to model bearing failure `Add fault`

Whether to model a fault in the bearing. To add a fault, click the
**Add fault** hyperlink.

### **Faulted damping coefficient multiplier** — Damping multiplier `5` (default) | positive scalar

Damping coefficient when a fault is triggered.

#### Dependencies

To enable this parameter, enable faults for the block by clicking the **Add
fault** hyperlink.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

## Version History

**Introduced in R2023a**

### R2024a: Model faults with the Simscape faults interface

The Bearing block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Bearing that provides trans-axial support to freely rotating shaft

The Bearing block represents a ball- or roller-type bearing
or a journal bearing. These bearings constrain a shaft in the transverse plane so the
shaft may only rotate axially in the bearing. Bearings also contribute torque to the
system due to friction. You can add bearing friction to a mechanical rotational network
by connecting the network to only port **B** or by connecting the
bearing in series with other components using ports **B** and
**F**.

You can use either a constant or variable load on the bearing, *F*.
When you set **Radial load specification** to
`Constant`, the block uses the value of the **Load
on bearing** parameter. When you set **Radial load
specification** to `Variable`, the block takes a
physical signal input from port **Load** and smooths the signal such that

F=(Finput2+FThr2)1/2,

where:

- *Finput* is the physical signal
  input at the **Load** port.
- *FThr* is the **Force
  threshold** parameter.

The block calculates the torque due to friction such that

Tf=μ⋅F⋅r,

where:

- *μ* is the coefficient of friction.
- *Ff* is the friction force acting
  on the bearing.
- *r* is the **Bearing radius**
  parameter.

How the block calculates *μ* depends on the type of
bearing that you simulate.

### Ball- or Roller-Type Bearings

When you set **Bearing type** to `Ball or
Roller`, the block calculates the overall friction coefficient
depending on the **Coefficient of friction specification**
parameter. When you set this parameter to `Constant`, the
block calculates a constant coefficient of friction throughout the simulation. The
block uses a hyperbolic tangent function to smooth the zero-crossing transition.
When you set **Coefficient of friction specification** to
`Variable`, the block uses a 1-D lookup table where
*μ* functions with the angular velocity, *ɷ*
such that

μ=tablelookup(ω⇀,μ⇀,ω,interpolation=interp\_method\_1,extrapolation=extrap\_method\_1),

where:

- ω⇀ is the **Bearing angular speed vector,
  N** parameter.
- μ⇀ is the **Coefficient of friction,
  f(N)** parameter.

The block uses linear interpolation and extrapolation by default. You
can use the **Interpolation method** and **Extrapolation
method** parameters to change the interpolation and extrapolation,
respectively.

### Journal Bearings

When you set **Bearing type** to `Journal`, the
block uses the Hersey number a lookup table to define the coefficient of friction,
such that

μ=tablelookup(H⇀⋅K,μ⇀⋅μmin,H,interpolation=interp\_method\_2,extrapolation=extrap\_method\_2),

where:

- H⇀ is the optional **Normalized Hersey number
  vector** parameter.
- μ⇀ is the optional **Normalized viscous
  coefficient vector** parameter.
- *K* is the bearing modulus, which is the value of
  *H* where
  *μmin* occurs.
- *μmin* is the
  **Minimum coefficient of friction**
  parameter.

The block defines the bearing characteristic number, or Hersey
number, as

H=μωP,

where *P* is the bearing lubricant pressure such that

P=F2rl,

where *r* is the **Radius**
parameter and *l* is the **Length**
parameter.

### Faults

To model a fault in the Bearing block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When the block experiences a fault, it increases the bearing friction using the value of
the **Faulted damping coefficient multiplier** parameter. When
you trigger a fault, the block calculates the friction coefficient such that

μfault=μ⋅fault factor,

where *fault factor* is the **Faulted
damping coefficient multiplier** parameter.

### Assumptions and Limitations

The block assumes that the bearing lubricant is a Newtonian fluid with zero-slip
boundary conditions.
