---
type: simulink-block
title: 'Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'transmissionline'
documentation_source_path: 'ref/transmissionline.html'
language: en
---

# Transmission Line

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Model type** — Transmission line model `Delay-based and lossless` (default) | `Delay-based and lossy` | `Lumped parameter L-section` | `Lumped parameter Pi-section` | `Coaxial` | `Coplanar waveguide` | `Microstrip` | `Stripline` | `Two-wire` | `Parallel-plate` | `Equation-based` | `RLCG` | ...

Type of transmission line model, specified as one of these.

| Transmission Line Types | Description |
| --- | --- |
| `Delay-based and lossless` | Model transmission line with delay but no loss.  Delay-based transmission line |
| `Delay-based and lossy` – | Model transmission line with delay and loss.    Delay-based and lossy transmission line |
| `Lumped parameter L-section` | Model transmission line with RLGC L-sections.    R,L,G.C is connected as L-section. |
| `Lumped parameter Pi-section` | Model transmission line with RLGC pi-sections.    R,L,G.C is connected as Pi-section. |
| `Coaxial` | Model transmission line as a coaxial transmission line. The cross section of a coaxial transmission line is shown in the following figure. Its physical characteristics include the radius of the inner conductor *a*, and the radius of the outer conductor *b*.    Coaxial transmission line layers: Inner conductor, dielectric, outer conductor |
| `Coplanar waveguide` | Model transmission line as a coplanar waveguide. The cross section of a coplanar waveguide transmission line is shown in the following figure. Its physical characteristics include conductor width *w*, conductor thickness *t*, slot width *s*, substrate height *d*, and relative permittivity constant *ε*.  Cross-section of a coplanar waveguide with and without conductor-backed ground plane |
| `Microstrip` | Model transmission line as a standard, embedded, inverted, or suspended microstrip transmission line. The cross-sections of standard, embedded, inverted, and suspended microstrip transmission lines are shown here. The physical characteristics of such a transmission line include microstrip width *w*, microstrip thickness *t*, dielectric thickness *d*, and relative permittivity constant *ε*.    Cross-section of standard, embedded, inverted, and suspended microstrip transmission lines |
| `Stripline` | Model transmission line as stripline transmission line. The cross-section of a stripline transmission line is shown in this figure. Its physical characteristics include strip width *w*, strip thickness *t*, dielectric thickness *h*, and relative permittivity constant *ε*.    Stripline transmission line |
| `Two-wire` | Model transmission line as two-wire transmission line. The cross-section of a two-wire transmission line is shown in the following figure. Its physical characteristics include the radius of wires *a*, separation or physical distance between the wire centers *S*, and relative permittivity and permeability of the wires.    Cross-section of a two-wire transmission line |
| `Parallel plate` | Model transmission line as a parallel-plate transmission line. The cross-section of a parallel-plate transmission line is shown in the following figure. Its physical characteristics include plate width *w*, and plate separation *d*.    Cross-section of a parallel plate transmission line |
| `Equation based` | Model transmission line as an equation-based transmission line. The transmission line, which can be lossy or lossless, is treated as a two-port linear network.  Equation based transmission line |
| `RLCG` | Model transmission line as an RLCG transmission line. This line is defined in terms of its frequency-dependent resistance, inductance, capacitance, and conductance. The transmission line, which can be lossy or lossless, is treated as a two-port linear network.    Cross-section of RLGC transmission line |

### **Transmission delay** — Delay in transmission line `4.7e-9 s` (default) | real scalar | `s` | `ms` | `us` | `ns`

Delay in the transmission line, specified as a real scalar in
`s`, `ms`,
`us`, or `ns`.

#### Dependencies

To enable this parameter, choose one of the following:

- `Delay-based and lossless` in
  **Model type**.
- `Delay-based and lossy` in
  **Model type**.

### **Characteristic impedance** — Impedance of transmission line `50 ohm` (default) | real scalar | `Ohm` | `kOhm` | `MOhm` | `GOhm`

Impedance of the transmission line, specified as a real scalar in
`Ohm`, `kOhm`,
`MOhm`, or
`GOhm`.

#### Dependencies

To enable this parameter, choose one of the following:

- `Delay-based and lossless`,
  `Delay-based and lossy`, or
  `Equation-based` in
  **Model type**.
- `Lumped parameter L-section`
  or `Lumped parameter
  Pi-section` in **Model
  type** and `By characterisitc
  impedance and capacitance` in
  **Parameterization**.

### **Resistance per unit length** — Resistance per unit length of transmission line `0.3 Ohm/m` (default) | positive scalar | `Ohm/m` | `kOhm/m` | `MOhm/m` | `GOhm/m`

Resistance per unit length of the transmission line, specified as a
positive scalar in `Ohm/m`,
`kOhm/m`,
`MOhm/m`, or
`GOhm/m`.

#### Dependencies

To enable this parameter, choose one of the following:

- `Delay-based and lossy` or
  `RLCG` in **Model
  type**.
- `Lumped parameter L-section`
  or `Lumped parameter
  Pi-section` in **Model
  type** and `By characterisitc
  impedance and capacitance` in
  **Parameterization**.

### **Number of segments** — Number of segments in transmission line `10` (default) | positive scalar

Number of segments in the transmission line, specified as a positive
scalar.

#### Dependencies

To enable this parameter, choose one of the following:

- `Delay-based and lossy` in
  **Model type**.
- `Lumped parameter L-section`
  or `Lumped parameter
  Pi-section` in **Model
  type** and `By characterisitc
  impedance and capacitance` or `By
  inductance and capacitance` in
  **Parameterization**.

### **Parameterization** — Type of parameters to model segments in transmission line `By characterisitc impedance and capacitance` (default) | `By inductance and capacitance`

Type of parameters to model segments in transmission line, specified
as `By characterisitc impedance and capacitance` or
`By inductance and capacitance`.

#### Dependencies

To enable this parameter, select `Lumped parameter
L-section` or `Lumped parameter
Pi-section` in **Model
type**.

### **Capacitance per unit length** — Capacitance per unit length of transmission line `94e-12 F/m` (default) | positive scalar

Capacitance per unit length of the transmission line, specified as a
positive scalar in `F/m`,
`mF/m`, `uF/m`,
`nF/m`, or
`pF/m`.

#### Dependencies

To enable this parameter, choose `Lumped parameter
L-section`, `Lumped parameter
Pi-section`, or `RLCG` in
**Model type**.

### **Conductance per unit length** — Conductance per unit length of transmission line `5e-6 S/m` (default) | positive scalar | `S/m` | `mS/m` | `uS/m` | `nS/m`

Conductance per unit length of the transmission line, specified as a
positive scalar in `S/m`,
`mS/m`, `uS/m`, or
`nS/m`.

#### Dependencies

To enable this parameter, choose `Lumped parameter
L-section`, `Lumped parameter
Pi-section`, or `RLCG` in
**Model type**.

### **Inductance per unit length** — Inductance per unit length of transmission line `235e-9 H/m` (default) | positive scalar | `H/m` | `mH/m` | `uH/m` | `nH/m`

Inductance per unit length of the transmission line, specified as a
positive scalar in `H/m`,
`mH/m`, `uH/m`, or
`nH/m`.

#### Dependencies

To enable this parameter, choose one of the following:

- `Lumped parameter L-section`,
  or `Lumped parameter
  Pi-section` in **Model
  type** and `By inductance and
  capacitance` in
  **Parameterization**.
- `RLCG` in **Model
  type**

### **Outer radius** — Outer radius of coaxial transmission line `2.57 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Outer radius of coaxial transmission line, specified as a positive
scalar in `m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Coaxial` in **Model
type**.

### **Inner radius** — Inner radius of coaxial transmission line `2.57 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Inner radius of coaxial transmission line, specified as a positive
scalar in `m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Coaxial` in **Model
type**.

### **Conductor width** — Physical width of conductor `0.6 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Physical width of the conductor, specified as a positive scalar in
`m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose `Coplanar
waveguide` in **Model
type**.

### **Slot width** — Physical width of slot `0.2 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Physical width of the slot, specified as a positive scalar in
`m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose `Coplanar
waveguide` in **Model
type**.

### **Conductor backed** — Infinite bottom conductor `off` (default) | `on`

Select this parameter to add an infinite-bottom conductor to your
coplanar waveguide transmission line.

#### Dependencies

To enable this parameter, set **Model type** to
`Coplanar waveguide`.

### **Structure** — Type of microstrip transmission line `Standard` (default) | `Embedded` | `Inverted` | `Suspended`

Type of microstrip transmission line, specified as Standard, Embedded,
Inverted, or Suspended.

#### Dependencies

To enable this parameter, set **Model type** to
`Microstrip`.

### **Strip Width** — Width of microstrip transmission line `0.6 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Width of the microstrip transmission line, specified as a positive
scalar in `m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, set **Model type**
to`Microstrip`.

### **Strip thickness** — Physical thickness of conductor `5 um` (default) | nonnegative scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Physical thickness of the conductor, specified as a nonnegative scalar
in `m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose `Coplanar
waveguide` or `Microstrip`
in **Model type**.

### **Strip Height** — Strip height of microstrip transmission line `0.635 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Strip height of the inverted, suspended, or embedded microstrip
transmission line, specified as a positive scalar in
`m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Microstrip` in **Model
type** and choose `Inverted`,
`Suspended`, or
`Embedded` in
**Structure**.

### **Wire radius** — Radius of conducting wires of two-wire transmission line `0.67 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Radius of the conducting wires of the two-wire transmission line,
specified as a positive scalar in `m`,
`cm`, `mm`,
`um`, `in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Two-wire` in **Model
type**.

### **Wire separation** — Physical distance between conducting wires of two-wire transmission line `1.62 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Physical distance between the conducting wires of the two-wire
transmission line, specified as a positive scalar in
`m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Two-wire` in **Model
type**.

### **Plate width** — Width of parallel-plate transmission line `5 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Width of the parallel-plate transmission line, specified as a positive
scalar in `m`, `cm`,
`mm`, `um`,
`in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Parallel-plate` in **Model
type**.

### **Plate separation** — Thickness of dielectric separating plates `1 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Thickness of the dielectric separating the plates, specified as a
positive scalar in `m`,
`cm`, `mm`,
`um`, `in`, or
`ft`.

#### Dependencies

To enable this parameter, choose
`Parallel-plate` in **Model
type**.

### **Phase velocity (m/s)** — Propagation velocity of a uniform plane wave on transmission line `299792458` (default) | positive scalar

Propagation velocity of a uniform plane wave on the transmission line,
specified as a positive scalar in meters per second.

#### Dependencies

To enable this parameter, choose
`Equation-based` in **Model
type**.

### **Loss (dB/m)** — Reduction in strength of signal as it travels over transmission line `0` (default) | positive scalar

Reduction in strength of the signal as it travels over the
transmission line, specified as a positive scalar in meters per
second.

#### Dependencies

To enable this parameter, choose
`Equation-based` in **Model
type**.

### **Frequency** — Modeling frequencies `1e9 Hz` (default) | positive scalar | `Hz` | `kHz` | `MHz` | `GHz`

Modeling frequencies, specified as a positive scalar or vector in
`Hz`, `kHz`,
`MHz`, or
`GHz`.

#### Dependencies

To enable this parameter, choose
`Equation-based` or
`RLCG` in **Model
type**.

### **Interpolation method** — Interpolation method used to calculate values at the modeling frequencies `Linear` (default) | `Spline` | `Cubic`

Interpolation method used to calculate the values at the modeling
frequencies, specified as `Linear`,
`Spline`, or
`Cubic`.

#### Dependencies

To enable this parameter, choose
`Equation-based` or
`RLCG` in **Model
type**.

### **Conductivity of conductor** — Conductivity of conductor `inf` (default) | scalar | `S/m` | `mS/m` | `uS/m` | `nS/m`

Conductivity of conductor, specified as a scalar in
`S/m`, `mS/m`,
`uS/m`, or
`nS/m`.

#### Dependencies

To enable this parameter, choose
`Coaxial`, `Coplanar
waveguide`, `Microstrip`,
`Two-wire` or
`Parallel-plate` in **Model
type**.

### **Dielectric Thickness** — Thickness of dielectric on which conductor resides `0.635 mm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Thickness of the dielectric on which the conductor resides, specified
as a positive scalar in `m`,
`cm`, `mm`,
`um`, `in`, or
`ft`.

Default values of the dielectric thickness of coplanar waveguide,
standard, embedded, inverted, and suspended microstrip transmission
lines are listed in this table.

| Model Type | Structure | Default Dielectric Thickness in mm |
| --- | --- | --- |
| `Coplanar waveguide` | N.A. | `0.635` |
| `Microstrip` | `Standard` and `Inverted` | `0.635` |
| `'Suspended'` | `0.3175` |
| `'Embedded'` | `1.37` |

#### Dependencies

To enable this parameter, set **Model type** to
`Microstrip` or `Coplanar
waveguide`.

### **Relative permeability of dielectric** — Relative permeability of dielectric `1` (default) | scalar

Relative permeability of the dielectric, specified as a scalar.

#### Dependencies

To enable this parameter, set **Model type** to
`Coaxial`,
`Two-wire`, or
`Parallel-plate`.

### **Relative permittivity of dielectric** — Relative permittivity of dielectric `2.2` (default) | scalar

Relative permittivity of the dielectric, specified as a scalar.

#### Dependencies

To enable this parameter, set **Model type** to
`Coaxial`, `Coplanar
waveguide`, `Microstrip`,
`Two-wire`, or
`Parallel-plate`.

### **Loss tangent of dielectric** — Loss tangent of dielectric `0` (default) | scalar

Loss tangent of the dielectric, specified as a scalar.

#### Dependencies

To enable this parameter, set **Model type** to
`Coaxial`, `Coplanar
waveguide`, `Microstrip`,
`Two-wire`, or
`Parallel-plate`.

### **Line length** — Physical length of transmission line `1 cm` (default) | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

Physical length of the transmission line or *l*,
specified as a positive scalar in `m`,
`cm`, `mm`,
`um`, `in`, or
`ft`.

#### Dependencies

To enable this parameter, choose one of the following:

- `Delay-based and lossy`,
  `Coaxial`,
  `Coplanar waveguide`,
  `Microstrip`, or
  `Two-wire`,
  `Parallel-plate`,
  `Equation-based`, or
  `RLCG` in **Model
  type**.
- `Lumped parameter L-section`
  or `Lumped parameter
  Pi-section` in **Model
  type** and `By characterisitc
  impedance and capacitance` or `By
  inductance and capacitance` in
  **Parameterization**.

### **Stub mode** — Type of stub `Not a stub` (default) | `Shunt` | `Series`

Type of stub, specified as `Not a stub`,
`Shunt`, or
`Series`. See Parameter Calculations for Transmission Line with Stub.

#### Dependencies

To enable this parameter, choose
`Coaxial`, `Coplanar
waveguide`, `Microstrip`
`Two-wire`,
`Parallel-plate`,
`Equation-based`, or
`RLCG` in **Model
type**.

### **Termination of stub** — Type of termination for stub `Open` (default) | `Short`

Type of termination for stub, specified as
`Open` or
`Short`.

#### Dependencies

To enable this parameter, choose `Series`
or `Shunt` in **Stub
mode**.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to internally ground and hide the negative
terminals. To expose the negative terminals, clear this parameter. By
exposing these terminals, you can connect them to other parts of your
model.

By default, this option is selected.

### Modeling

### **Modeling Options** — Options to model S-parameters `Frequency domain` (default) | `Time domain`

Options to model S-parameters, specified as:

- `Frequency domain` – Computes the baseband
  impulse response for each carrier frequency independently. This technique is
  based on convolution. There is an option to specify the duration of the
  impulse response. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.
- `Time domain` – Computes the analytical rational
  model that approximates the whole range of the data.

For the Amplifier, Antenna, and S-Parameters blocks, the default
value is `Time domain`. For the Transmission
Line block, the default value is `Frequency
domain`.

### **Automatically estimate impulse response duration** — Calculate impulse response duration automatically `off` (default) | `on`

Select **Automatically estimate impulse response duration**  to
calculate impulse response duration automatically. Clear the selection to specify
impulse response duration.

#### Dependencies

To enable this parameter, choose `Frequency domain` in
**Modeling options**.

### **Impulse response duration** — Manually specify impulse response duration `0 s` (default) | positive scalar | `s` | `ms` | `us` | `ns`

Manually specify impulse response duration, specified as a positive scalar in
`s`, `ms`,
`us`, or `ns`.

#### Dependencies

To enable this parameter, clear **Automatically estimate impulse response
duration**.

### **Fitting options** — Fitting options for rationalfit `Share all poles` (default) | `Share poles by columns` | `Fit individually`

Fitting options for rationalfit, specified as `Share all
poles`, `Share poles by columns`, or
`Fit individually`.

For the Amplifier block, the default value is `Fit
individually`. For the S-parameters block and
Transmission Line block, the default value is `Share all
poles`.

#### Dependencies

To enable this parameter, choose `Time domain` in
**Modeling options**.

### **Relative error desired (dB)** — Relative error acceptable in rational fit output `-40` (default) | real scalar

Relative error acceptable in rational fit output, specified as a real scalar in
decibels.

#### Dependencies

To enable this parameter, choose `Time domain` in
**Modeling options**.

### **Rational fitting results** — Values of rationalfit calculations read-only (default)

Shows values of **Number of independent fits**, **Number of
required poles**, and **Relative error achieved
(dB)**.

When modeling using `Time domain`, the **Plot** in
`Visualization` tab plots the data defined in `Data
Source` and the values in the `rationalfit`
function.

#### Dependencies

To enable this parameter, choose `Time domain` in
**Modeling options**.

**Note**

Modeling tab is enabled for all transmission line types except
`Delay-based and lossless`,
`Delay-based and lossy`, `Lumped
parameter L-section`, and `Lumped parameter
pi-section`.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

### R2024b: `Time domain (rationalfit)` parameter renamed

The `Time domain (rationalfit)` parameter value in the
**Modeling options** parameter has been renamed to
`Time domain` in the Transmission Line
block.

When you open a model created before R2024b containing an Transmission
Line block, the parameter name displays as `Time
domain`.

### R2022a: Three block parameters renamed

The **Substrate height**, **Relative permittivity
constant**, and **Relative permeability constant**
parameters in the Transmission Line block have been renamed to
**Dielectric thickness**, **Relative permittivity of
dielectric**, and **Relative permeability of
dielectric**, respectively.

When you open a model created before R2022a containing the Transmission
Line block, the software replaces the old parameters names with the new
ones.

### R2022a: Model transmission lines

Use the Transmission Line block to model:

- Embedded, inverted, and suspended microstrip transmission lines
- Conductor-backed coplanar waveguide transmission lines
- Stripline transmission lines

## Description

Model transmission line

Use the Transmission Line block to model delay-based, lumped, and
distributed transmission lines. Mask dialog box options change automatically to
accommodate model type selection.
