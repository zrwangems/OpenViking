---
type: simulink-block
title: 'FEM-Parameterized Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechatronic Actuators\u200b'
documentation_page: 'femparameterizedrotaryactuator'
documentation_source_path: 'ref/femparameterizedrotaryactuator.html'
language: en
---

# FEM-Parameterized Rotary Actuator

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the actuator
positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the actuator
negative terminal.

### **C** — Case mechanical

Mechanical rotational conserving port associated with the
actuator case.

### **R** — Rotor mechanical

Mechanical rotational conserving port associated with the
rotor.

### **H** — Thermal port thermal

Thermal port.

#### Dependencies

To enable this port, set **Modeling
option** to `Show thermal
port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of losses that convert
power to heat.

### Magnetic Force

### **Electrical model** — Electrical model parameterization `Define in terms of dPhi(i,theta)/dtheta and dPhi(i,theta)/di` (default) | `Define in terms of Phi(i,theta)`

Select one of the following parameterization options,
based on the underlying electrical model:

- `Define in terms of
  dPhi(i,theta)/dtheta and
  dPhi(i,theta)/di` — Define the
  current through the block in terms of partial
  derivatives of the magnetic flux with respect to
  distance and current.
- `Define in terms of
  Phi(i,theta)` — Define the
  voltage across the block terminals directly in
  terms of the flux.

### **Current vector, i** — Current vector `[0, .2, .4, .6, .8, 1]` `A` (default)

Specify a vector of monotonically increasing current
values corresponding to your torque-flux data. If you
specify positive currents only, the first element must be
zero.

### **Angle vector, theta** — Angle vector `[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]` `deg` (default)

Specify a vector of monotonically increasing rotor angle
values corresponding to your torque-flux data.

### **Flux partial derivative wrt current, dPhi(i,theta)/di** — Flux partial derivative with respect to current `[.002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002; .002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002; .002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002; .002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002; .002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002; .002, .0024, .0035, .0052, .0074, .0096, .0118, .0135, .0146, .015, .0146, .0135, .0118, .0096, .0074, .0052, .0035, .0024, .002]` `Wb/A` (default)

Specify a matrix of the flux partial derivatives with
respect to current. This parameter is visible only if
**Electrical model** is set to
`Define in terms of dPhi(i,theta)/dtheta
and dPhi(i,theta)/di`. The default
value, in Wb/A, is:

```
[ 0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002;
  0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002;
  0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002;
  0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002;
  0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002;
  0.002 0.0024 0.0035 0.0052 0.0074 0.0096 0.0118 0.0135 0.0146 ...
        0.015 0.0146 0.0135 0.0118 0.0096 0.0074 0.0052 0.0035 0.0024 0.002; ]
```

#### Dependencies

This parameter is visible only when you set the
**Electrical model** parameter to
`Define in terms of
dPhi(i,theta)/dtheta and
dPhi(i,theta)/di`.

### **Flux partial derivative wrt angle, dPhi(i,theta)/dtheta** — Flux partial derivative with respect to angle `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, .0009, .0017, .0023, .0026, .0026, .0023, .0017, .0009, 0, -.0009, -.0017, -.0023, -.0026, -.0026, -.0023, -.0017, -.0009, 0; 0, .0018, .0033, .0045, .0051, .0051, .0045, .0033, .0018, 0, -.0018, -.0033, -.0045, -.0051, -.0051, -.0045, -.0033, -.0018, 0; 0, .0027, .005, .0068, .0077, .0077, .0068, .005, .0027, 0, -.0027, -.005, -.0068, -.0077, -.0077, -.0068, -.005, -.0027, 0; 0, .0036, .0067, .009, .0102, .0102, .009, .0067, .0036, 0, -.0036, -.0067, -.009, -.0102, -.0102, -.009, -.0067, -.0036, 0; 0, .0044, .0084, .0113, .0128, .0128, .0113, .0084, .0044, 0, -.0044, -.0084, -.0113, -.0128, -.0128, -.0113, -.0084, -.0044, 0]` `Wb/rad` (default)

Specify a matrix of the flux partial derivatives with
respect to rotor angle. This parameter is visible only if
**Electrical model** is set to
`Define in terms of dPhi(i,theta)/dtheta
and dPhi(i,theta)/di`. The default
value, in Wb/rad, is:

```
[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
  0 9e-4 0.0017 0.0023 0.0026 0.0026 0.0023 0.0017 9e-4 ...
         0 -9e-4 -0.0017 -0.0023 -0.0026 -0.0026 -0.0023 -0.0017 -9e-4 0;
  0 0.0018 0.0033 0.0045 0.0051 0.0051 0.0045 0.0033 0.0018 ...
         0 -0.0018 -0.0033 -0.0045 -0.0051 -0.0051 -0.0045 -0.0033 -0.0018 0;
  0 0.0027 0.005 0.0068 0.0077 0.0077 0.0068 0.005 0.0027 ...
         0 -0.0027 -0.005 -0.0068 -0.0077 -0.0077 -0.0068 -0.005 -0.0027 0;
  0 0.0036 0.0067 0.009 0.0102 0.0102 0.009 0.0067 0.0036 ...
         0 -0.0036 -0.0067 -0.009 -0.0102 -0.0102 -0.009 -0.0067 -0.0036 0;
  0 0.0044 0.0084 0.0113 0.0128 0.0128 0.0113 0.0084 0.0044 ...
         0 -0.0044 -0.0084 -0.0113 -0.0128 -0.0128 -0.0113 -0.0084 -0.0044 0 ]
```

#### Dependencies

This parameter is visible only when you set the
**Electrical model** parameter to
`Define in terms of
dPhi(i,theta)/dtheta and
dPhi(i,theta)/di`.

### **Flux linkage matrix, Phi(i,theta)** — Flux linkage matrix `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; .0004, .00048, .0007, .00105, .00147, .00193, .00235, .0027, .00292, .003, .00292, .0027, .00235, .00193, .00147, .00105, .0007, .00048, .0004; .0008, .00096, .00141, .0021, .00295, .00385, .0047, .00539, .00584, .006, .00584, .00539, .0047, .00385, .00295, .0021, .00141, .00096, .0008; .0012, .00144, .00211, .00315, .00442, .00578, .00705, .00809, .00876, .009, .00876, .00809, .00705, .00578, .00442, .00315, .00211, .00144, .0012; .0016, .00191, .00282, .0042, .0059, .0077, .0094, .01078, .01169, .012, .01169, .01078, .0094, .0077, .0059, .0042, .00282, .00191, .0016; .002, .00239, .00352, .00525, .00737, .00963, .01175, .01348, .01461, .015, .01461, .01348, .01175, .00963, .00737, .00525, .00352, .00239, .002]` `Wb` (default)

Specify a matrix of the total flux linkage, that is, flux
times the number of turns. This parameter is visible only
if **Electrical model** is set to
`Define in terms of
Phi(i,theta)`. The default value, in
Wb, is:

```
[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
  4e-4 4.8e-4 7e-4 0.00105 0.00147 0.00193 0.00235 0.0027 0.00292 ...
        0.003 0.00292 0.0027 0.00235 0.00193 0.00147 0.00105 7e-4 4.8e-4 4e-4;
  8e-4 9.6e-4 0.00141 0.0021 0.00295 0.00385 0.0047 0.00539 0.00584 ...
        0.006 0.00584 0.00539 0.0047 0.00385 0.00295 0.0021 0.00141 9.6e-4 8e-4;
  0.0012 0.00144 0.00211 0.00315 0.00442 0.00578 0.00705 0.00809 0.00876 ...
        0.009 0.00876 0.00809 0.00705 0.00578 0.00442 0.00315 0.00211 0.00144 0.0012;
  0.0016 0.00191 0.00282 0.0042 0.0059 0.0077 0.0094 0.01078 0.01169 ...
        0.012 0.01169 0.01078 0.0094 0.0077 0.0059 0.0042 0.00282 0.00191 0.0016;
  0.002 0.00239 0.00352 0.00525 0.00737 0.00963 0.01175 0.01348 0.01461 ...
        0.015 0.01461 0.01348 0.01175 0.00963 0.00737 0.00525 0.00352 0.00239 0.002 ]
```

#### Dependencies

This parameter is visible only when you set the
**Electrical model** parameter to
`Define in terms of
Phi(i,theta)`.

### **Calculate torque matrix?** — Electromagnetic torque data specification `No` (default) | `Yes`

Specify the way of providing the electromagnetic torque data:

- `No` — Enter
  the electromagnetic torque data directly, by using
  the **Torque matrix, T(i,theta)**
  parameter.
- Yes — The block calculates the torque
  from the flux linkage information, as a function
  of current and rotor angle.

### **Torque matrix, T(i,theta)** — Torque matrix `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, .0889, .1671, .2252, .2561, .2561, .2252, .1671, .0889, 0, -.0889, -.1671, -.2252, -.2561, -.2561, -.2252, -.1671, -.0889, 0; 0, .3557, .6685, .9007, 1.0242, 1.0242, .9007, .6685, .3557, 0, -.3557, -.6685, -.9007, -1.0242, -1.0242, -.9007, -.6685, -.3557, 0; 0, .8003, 1.5041, 2.0265, 2.3045, 2.3045, 2.0265, 1.5041, .8003, 0, -.8003, -1.5041, -2.0265, -2.3045, -2.3045, -2.0265, -1.5041, -.8003, 0; 0, 1.4228, 2.674, 3.6027, 4.0968, 4.0968, 3.6027, 2.674, 1.4228, 0, -1.4228, -2.674, -3.6027, -4.0968, -4.0968, -3.6027, -2.674, -1.4228, 0; 0, 2.2231, 4.1781, 5.6292, 6.4013, 6.4013, 5.6292, 4.1781, 2.2231, 0, -2.2231, -4.1781, -5.6292, -6.4013, -6.4013, -5.6292, -4.1781, -2.2231, 0]` `mN*m` (default)

Specify a matrix of the electromagnetic torque applied to
the rotor. This parameter is visible only if
**Calculate torque matrix?** is set
to `No`. The default value, in
mN\*m, is:

```
[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
  0 0.0889 0.1671 0.2252 0.2561 0.2561 0.2252 0.1671 0.0889 ...
        0 -0.0889 -0.1671 -0.2252 -0.2561 -0.2561 -0.2252 -0.1671 -0.0889 0;
  0 0.3557 0.6685 0.9007 1.0242 1.0242 0.9007 0.6685 0.3557 ...
        0 -0.3557 -0.6685 -0.9007 -1.0242 -1.0242 -0.9007 -0.6685 -0.3557 0;
  0 0.8003 1.5041 2.0265 2.3045 2.3045 2.0265 1.5041 0.8003 ...
        0 -0.8003 -1.5041 -2.0265 -2.3045 -2.3045 -2.0265 -1.5041 -0.8003 0;
  0 1.4228 2.674 3.6027 4.0968 4.0968 3.6027 2.674 1.4228 ...
        0 -1.4228 -2.674 -3.6027 -4.0968 -4.0968 -3.6027 -2.674 -1.4228 0;
  0 2.2231 4.1781 5.6292 6.4013 6.4013 5.6292 4.1781 2.2231 ...
        0 -2.2231 -4.1781 -5.6292 -6.4013 -6.4013 -5.6292 -4.1781 -2.2231 0 ]
```

#### Dependencies

This parameter is visible only when you set the
**Calculate torque matrix?**
parameter to `No`.

### **Flux dependence on displacement** — Flux pattern `Unique` (default) | `Cyclic`

Specify the flux pattern:

- `Unique` —
  No flux pattern present.
- `Cyclic` —
  Select this option to model a linear motor with a
  repeated flux pattern. The force and flux (or
  force and flux partial derivatives, depending on
  the **Electrical model** option
  chosen) must have identical first and last
  columns.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Select one of the following interpolation methods for
approximating the output value when the input value is
between two consecutive grid points:

- `Linear` —
  Select this option to get the best
  performance.
- `Smooth` —
  Select this option to produce a continuous surface
  with continuous first-order derivatives.

For more information on interpolation algorithms, see the
PS Lookup Table
(2D) block reference page.

### **Extrapolation method** — Extrapolation method `Linear` (default) | `Nearest` | `Error`

Select one of the following extrapolation methods for
determining the output value when the input value is
outside the range specified in the argument list:

- `Linear` —
  Select this option to produce a surface with
  continuous first-order derivatives in the
  extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` —
  Select this option to produce an extrapolation
  that does not go above the highest point in the
  data or below the lowest point in the data.
- `Error` —
  Issues an error if the input signal is outside the
  range of the table. Select this option to avoid
  going into the extrapolation mode when you want
  your data to be within the table range.

For more information on extrapolation algorithms, see the
PS Lookup Table
(2D) block reference page.

#### Dependencies

This parameter is visible only when you set the
**Flux dependence on
displacement** parameter to
`Unique`.

### **Winding resistance** — Electrical winding total resistance `14` `Ohm` (default)

Total resistance of the electrical winding.

### **Magnetizing resistance** — Magnetizing resistance for iron losses `inf` `Ohm` (default)

Magnetizing resistance. The value must be greater than
zero. The default value is `inf`, which
implies that there are no iron losses.

### Mechanical

### **Damping** — Rotary damping `0.0001` `N*m/(rad/s)` (default)

Rotary damping. The value can be zero.

### **Rotor inertia** — Rotor inertia `0.00005` `kg*m^2` (default)

Inertia of the rotor attached to mechanical translational
port **R**. The value can be zero.

### **Minimum rotor angle** — Minimum rotor angle `-Inf` `deg` (default)

The rotor angle at which the lower mechanical end stop is
applied.

### **Maximum rotor angle** — Maximum rotor angle `Inf` `deg` (default)

The rotor angle at which the upper mechanical end stop is
applied.

### **Contact stiffness** — Contact stiffness `1e8` `N*m/rad` (default)

Contact stiffness between rotor and end stops.

### **Contact damping** — Contact damping `1e4` `N*m/(rad/s)` (default)

Contact damping between rotor and end stops.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Resistance temperature coefficient.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

Temperature for which the actuator parameters are
defined.

### Thermal Port

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Thermal mass** — Thermal mass `100` `J/K` (default)

Thermal mass is the energy required to raise the
temperature by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Rotary actuator defined in terms of magnetic flux

The FEM-Parameterized Rotary Actuator block
implements a model of a rotary actuator defined in terms of magnetic flux. Use
this block to model custom rotary actuators and motors where magnetic flux depends
on both rotor angle and current. You parameterize the block using data from a
third-party Finite Element Magnetic (FEM) package.

The block has two options for the electrical equation. The first,
`Define in terms of dPhi(i,theta)/dtheta and
dPhi(i,theta)/di`, defines the current in terms of partial
derivatives of the magnetic flux (Φ) with respect to rotor angle (θ) and current
(*i*), the equations for which are:

didt=(v−iR−∂Φ∂θdθdt)/∂Φ∂i

The second option, `Define in terms of Phi(i,theta)`,
defines the voltage across the component directly in terms of the flux, the
equation for which is:

v=iR+ddtΦ(θ,i)

Numerically, defining the electrical equation in terms of flux partial derivatives
is better because the back-emf is piecewise continuous. If using the flux
directly, using a finer grid size for current and position will improve results,
as will selecting cubic or spline interpolation.

In both cases, you have an option to either directly specify the torque as a
function of current and rotor angle, by using the **Torque matrix,
T(i,theta)** parameter, or have the block automatically calculate
the torque matrix.

If entering the electromagnetic torque data directly, you can either use data
supplied by the finite element magnetic package (which you used to determine the
flux) or calculate the torque from the flux with following equation:

T=∫0i∂Φ(θ,i)∂θdi

See the Solenoid Parameterized with FEM Data example model for an example
of how to implement this type of integration in MATLAB®.

Alternatively, the block can automatically calculate the torque matrix from the
flux information that you provide. To select this option, set the
**Calculate torque matrix?** parameter to
`Yes`. The torque matrix calculation occurs at
model initialization based on current block flux linkage information. The torque
is calculated by numerically integrating the rate of change of flux linkage with
respect to angle over current, according to the preceding equation. If the
**Electrical model** parameter is set to
`Define in terms of Phi(i,theta)`, then the block
must first estimate the **Flux partial derivative wrt angle,
Phi(i,theta)/dtheta** parameter value from the flux linkage data.
When doing this, the block uses the interpolation method specified by the
**Interpolation method** parameter. Typically, the
`Smooth` option is most accurate, but the
`Linear` option is most robust.

You can define Φ and its partial derivatives for just positive, or positive and
negative currents. If defining for just positive currents, then the block assumes
that Φ(–*i*,*x*) =
–Φ(*i*,*x*). Therefore, if the current
vector is positive only:

- The first current value must be zero.
- The flux corresponding to zero current must be zero.
- The partial derivative of flux with respect to rotor angle must be
  zero for zero current.

To model a rotary motor with a repeated flux pattern, set the **Flux
dependence on displacement** parameter to
`Cyclic`. When selecting this option, the torque
and flux (or torque and flux partial derivatives depending on the option chosen)
must have identical first and last columns.

### Model Thermal Effects

You can expose the thermal port to model the effects of losses that convert power to heat.
To expose the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a
  thermal port.
- `Show thermal port` — The block contains one thermal
  conserving port.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
