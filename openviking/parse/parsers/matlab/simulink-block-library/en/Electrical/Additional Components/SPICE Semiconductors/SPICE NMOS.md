---
type: simulink-block
title: 'SPICE NMOS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicenmos'
documentation_source_path: 'ref/spicenmos.html'
language: en
---

# SPICE NMOS

## Ports

### Conserving

### **gx** — Gate terminal electrical

Electrical conserving port associated with the transistor gate
terminal.

### **dx** — Drain terminal electrical

Electrical conserving port associated with the transistor drain
terminal.

### **sx** — Source terminal electrical

Electrical conserving port associated with the transistor source
terminal.

### **bx** — Bulk terminal electrical

Electrical conserving port associated with the transistor bulk
terminal.

## Parameters

### Model Selection

### **MOS model** — Drain current model `Level 1 MOS` (default) | `Level 3 MOS`

MOSFET drain current model options:

- `Level 1 MOS` — Use the
  Level 1 Drain Current Model. This is the
  default option.
- `Level 3 MOS` — Use the
  Level 3 Drain Current Model.

#### Dependencies

The setting that you select for the **MOS model**
affects the visibility of certain parameters in the **DC
Currents** and **Process**
settings.

### Dimensions

### **Device area factor, AREA** — Device area `1.0` (default) | positive scalar

Transistor area factor for scaling. The value must be greater than
`0`.

### **Number of parallel devices, SCALE** — Number of parallel devices `1` (default) | positive integer

The number of parallel MOS instances that the block represents. This
parameter multiplies the output current and device charge. The value
must be greater than `0`.

### **Length of channel, LENGTH** — Source-to-drain channel length `1e-4` `m` (default) | positive scalar

Length of the channel between the source and drain.

### **Width of channel, WIDTH** — Source-to-drain channel width `1e-4` `m` (default) | positive scalar

Width of the channel between the source and drain.

### **Area of drain, AD** — Drain area `0` `m^2` (default) | nonnegative scalar

Area of the transistor drain diffusion. The value must be greater than
or equal to `0`.

### **Area of source, AS** — Source area `0` `m^2` (default) | nonnegative scalar

Area of the transistor source diffusion. The value must be greater
than or equal to `0`.

### **Perimeter of drain, PD** — Drain perimeter `0` `m` (default) | nonnegative scalar

Perimeter of the transistor drain diffusion. The value must be greater
than or equal to `0`.

### **Perimeter of source, PS** — Source perimeter `0` `m` (default) | nonnegative scalar

Perimeter of the transistor source diffusion. The value must be
greater than or equal to `0`.

### Resistors

### **Number of drain squares, NRD** — Number of drain diffusion resistance squares `0` (default) | nonnegative scalar

Number of squares of resistance that make up the transistor drain diffusion. The value
must be greater than or equal to `0`. The block only
uses this parameter value if you do not specify one or both of the
**Drain resistance, RD** and **Source
resistance, RS** parameter values, as described in Parameters Calculations.

### **Number of source squares, NRS** — Number of transistor source diffusion squares of resistance `1` (default) | nonnegative scalar

Number of squares of resistance that make up the transistor source diffusion. The value
must be greater than or equal to `0`. The block only
uses this parameter value if you do not specify one or both of the
**Drain resistance, RD** and **Source
resistance, RS** parameter values, as described in Parameters Calculations.

### **Drain resistance, RD** — Series resistance `0` `Ohm` (default) | nonnegative scalar

Transistor drain resistance. The value must be greater than or equal
to `0`.

### **Source resistance, RS** — Series resistance `0` `Ohm` (default) | nonnegative scalar

Transistor source resistance. The value must be greater than or equal to
`0`.

### **Sheet resistance, RSH** — Per square resistance `0` `Ohm` (default) | nonnegative scalar

Resistance per square of the transistor source and drain. Check Parameters Calculations to see when the block uses this
parameter. The value must be greater than or equal to
`0`.

### DC Currents

### **Threshold voltage, VTO** — Threshold voltage `0` `V` (default) | scalar

The gate-source voltage above which the transistor produces a nonzero drain current. If
you assign this parameter a value of `NaN`, the block
calculates the value from the specified values of the **Oxide
thickness, TOX** and **Substrate doping,
NSUB** parameters. For more information about this
calculation, see Temperature Dependence.

### **Transconductance, KP** — Transconductance `2e-5` `A/V^2` (default) | nonnegative scalar

The derivative of drain current with respect to gate voltage. The
value must be greater than or equal to `0`. If you
assign this parameter a value of `NaN`, the block
calculates the value from the specified values of the **Oxide
thickness, TOX** and **Substrate doping,
NSUB** parameters. For more information about this
calculation, see Level 1 Drain Current Model or Level 3 Drain Current Model as
appropriate for the selected value of the **MOS model**
parameter.

### **Bulk threshold, GAMMA** — Bulk threshold `0` `V^0.50000` (default) | nonnegative scalar

Body effect parameter, which relates the threshold voltage, VTH, to
the body bias, VBS, as described in Level 1 Drain Current Model and Level 3 Drain Current Model. The
value must be greater than or equal to `0`. If you
assign this parameter a value of `NaN`, the block
calculates the value from the specified values of the **Oxide
thickness, TOX** and **Substrate doping,
NSUB** parameters. For more information about this
calculation, see Level 1 Drain Current Model or Level 3 Drain Current Model as
appropriate for the selected value of the **MOS model**
parameter.

### **Surface potential, PHI** — Surface potential `0.6` `V` (default) | nonnegative scalar

Twice the voltage at which the surface electron concentration becomes
equal to the intrinsic concentration and the device transitions between
depletion and inversion conditions. The value must be greater than or
equal to `0`. If you assign this parameter a value of
`NaN`, the block calculates the value from the
specified values of the **Oxide thickness, TOX** and
**Substrate doping, NSUB** parameters. For more
information about this calculation, see Level 1 Drain Current Model or Level 3 Drain Current Model as
appropriate for the selected value of the **MOS model**
parameter.

### **Channel modulation, LAMBDA** — Channel-length modulation `0` `1/V` (default) | scalar

Channel-length modulation.

#### Dependencies

This parameter is only visible when you select `Level
1 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Bulk saturation current, IS** — Bulk saturation current magnitude `1e-14` `A` (default) | nonnegative scalar

Magnitude of the current that the junction approaches asymptotically
for very large reverse bias levels. The value must be greater than or
equal to `0`.

### **Emission coefficient, N** — Emission coefficient `1` (default) | nonnegative scalar

Transistor emission coefficient or ideality factor. The value must be
greater than `0`.

### **Bulk jct sat current density, JS** — Bulk junction saturation current density `0` `A/m^2` (default) | nonnegative scalar

Magnitude of the current per unit area that the junction approaches
asymptotically for very large reverse bias levels. The value must be
greater than or equal to `0`.

### **Width effect on threshold, DELTA** — Width factor `0` (default) | scalar

Factor that controls the effect of transistor width on threshold
voltage.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Max carrier drift velocity, VMAX** — Maximum drift velocity `0` `m/s` (default) | scalar

Maximum drift velocity of the carriers.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Fast surface state density, NFS** — Fast surface state density `0` `1/cm^2` (default) | scalar

Fast surface state density adjusts the drain current for the mobility
reduction caused by the gate voltage.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Vds dependence threshold volt, ETA** — Drain-source voltage threshold `0` (default) | scalar

The coefficient that controls how the drain voltage affects the mobility in the drain
current calculation.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Vgs dependence on mobility, THETA** — Mobility dependence coefficient `0` `1/V` (default) | scalar

The coefficient that controls how the gate voltage affects the mobility in the drain
current calculation.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### **Mobility modulation, KAPPA** — Mobility modulation coefficient `0.2` (default) | scalar

Coefficient of channel-length modulation for the level 3 MOS model.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### C-V

### **Model gate capacitance (CGS, CGD, CGB)** — Gate capacitance model `No intrinsic capacitance` (default) | `Meyer gate capacitances` | `Charge conservation capacitances`

Options for modeling the gate capacitance:

- `No intrinsic capacitance`
  — Do not include gate capacitance in the
  model.
- `Meyer gate capacitances`
  —
- `Charge conservation
  capacitances` —

### **Model gate overlap capacitance (CGSO, CGDO, CGBO)** — Gate overlap model `No` (default) | `Yes`

Options for modeling the gate overlap capacitance:

- `No` — Do not include gate
  overlap capacitance in the model.
- `Yes` — Specify the
  gate-source, gate-drain, and gate-bulk capacitances.

#### Dependencies

Selecting `Yes` exposes related
parameters.

### **G-S overlap capacitance, CGSO** — Gate-source overlap capacitance `0` `F/m` (default) | scalar | `0` or ≥ `1e-18`

Gate-source capacitance due to lateral diffusion of the source. The
value must be equal to `0` or greater than or equal to
*Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model gate
overlap capacitance (CGSO, CGDO, CGBO)** parameter.

### **G-D overlap capacitance, CGDO** — Gate-drain overlap capacitance `0` `F/m` (default) | scalar | `0` or ≥ `1e-18`

Gate-drain capacitance due to lateral diffusion of the drain. The
value must be equal to `0` or greater than or equal to
*Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model gate
overlap capacitance (CGSO, CGDO, CGBO)** parameter.

### **G-B overlap capacitance, CGBO** — Gate-bulk overlap capacitance `0` `F/m` (default) | scalar | `0` or ≥ `1e-18`

Gate-bulk capacitance due to gate extending beyond the channel width.
The value must be equal to `0` or greater than or equal
to *Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model gate
overlap capacitance (CGSO, CGDO, CGBO)** parameter.

### **Model junction capacitance (CBD, CBS)** — Junction capacitance model `No` (default) | `Yes`

Options for modeling the junction capacitance:

- `No` — Do not include
  junction capacitance in the model.
- `Yes` — Specify zero-bias
  junction capacitance, junction potential, grading
  coefficient, forward-bias depletion and capacitance
  coefficient.

#### Dependencies

Selecting `Yes` exposes related
parameters.

### **Zero-bias BD capacitance, CBD** — Zero-bias junction capacitance `0` `F` (default) | `0` or ≥ `1e-18`

Capacitance between the bulk and the drain. The value must be equal to
`0` or greater than or equal to
*Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Zero-bias BS capacitance, CBS** — Zero-bias bulk-source capacitance `0` `F` (default) | scalar | `0` or ≥ `1e-18`

Capacitance between the bulk and the source. The value must be equal
to `0` or greater than or equal to
*Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Bulk junction potential, PB** — Bulk junction potential `0.8` `V` (default) | scalar | `0` or ≥ `0.01`

Potential across the bulk junction. This parameter is only visible
when you select `Yes` for the **Model
junction capacitance (CBD, CBS)** parameter. The value must
be equal to `0` or greater than or equal to
*VJmin*. *VJmin* is a built-in
model constant whose value is `0.01`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Bottom junction cap per area, CJ** — Zero-bias bulk junction bottom capacitance per junction area `0` `F/m^2` (default) | scalar | `0` or ≥ `1e-18`

Zero-bias bulk junction bottom capacitance per junction area. The
value must be equal to `0` or greater than or equal to
*Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Bottom grading coefficient, MJ** — Bottom grading coefficient `0.5` (default) | scalar | 0 or < 0.9

Transistor bottom grading coefficient. The value must be equal to
`0` or less than *MGmax*.
*MGmax* is a built-in model constant whose value is
`0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Side jct cap/area of jct perimeter, CJSW** — Zero-bias bulk junction sidewall capacitance per junction perimeter `0` `F/m` (default) | scalar | `0` or ≥ `1e-18`

Zero-bias bulk junction sidewall capacitance per junction perimeter.
The value must be equal to `0` or greater than or equal
to *Cmin*. *Cmin* is a built-in model
constant whose value is `1e-18`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Side grading coefficient, MJSW** — Sidewall grading coefficient `0.5` (default) | scalar | 0 < *MJSW* < 0.9

Transistor sidewall grading coefficient. The value must be equal to
`0` or less than *MGmax*.
*MGmax* is a built-in model constant whose value is
`0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Capacitance coefficient, FC** — Capacitance coefficient `0.5` (default) | 0 or ≤ 0.95 | scalar

Fitting coefficient that quantifies the decrease of the depletion
capacitance with applied voltage. The value must be equal to
`0` or less than or equal to
*FCmax*. *FCmax* is a built-in
model constant whose value is `0.95`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance (CBD, CBS)** parameter.

### **Specify initial condition** — Initial condition model `No` (default) | `Yes`

Options for specifying initial conditions:

- `No` — Do not specify an
  initial condition for the model.
- `Yes` — Specify the
  initial transistor voltage.

  **Note**

  The block applies the initial transistor voltage
  across the junction capacitors and not across the
  ports.

#### Dependencies

To enable this parameter, set either:

- **Model gate capacitance (CGS, CGD,
  CGB)** to `No intrinsic
  capacitance` and either or both
  **Model gate overlap capacitance (CGSO,
  CGDO, CGBO)** and **Model junction
  capacitance (CBD, CBS)** to
  `Yes`.
- **Model gate capacitance (CGS, CGD,
  CGB)** to `Meyer gate
  capacitances` or `Charge
  conservation capacitances`.

### **Initial condition voltage, ICVDS** — Initial voltage `0` `V` (default) | scalar

Drain-source voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Specify initial
condition** parameter.

### **Initial condition voltage, ICVGS** — Initial voltage `0` `V` (default) | scalar

Gate-source voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Specify initial
condition** parameter.

### **Initial condition voltage, ICVBS** — Initial voltage `0` `V` (default) | scalar

Bulk-source voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Specify initial
condition** parameter.

### Process

### **Oxide thickness, TOX** — Gate oxide thickness `1e-7` `m` (default) | nonegative scalar

Thickness of the gate oxide. The value must be greater than or equal to
`0`.

### **Lateral diffusion, LD** — Length of lateral diffusion `0` `m` (default) | scalar

Length of lateral diffusion.

### **Surface mobility, U0** — Zero-bias surface mobility coefficient `600` `cm^2/s/V` (default)

Zero-bias surface mobility coefficient.

### **Substrate doping, NSUB** — Substrate doping `NaN` `1/cm^3` (default) | scalar ≥ `1.45e10`

Substrate doping. The value must be greater than or equal to
`1.45e10` (the carrier concentration of intrinsic
silicon).

### **Gate type, TPG** — Gate type `Opposite of substrate (1)` (default) | `Same as substrate (-1)` | `Aluminum (0)`

MOSFET gate materials (as compared to the substrate):

- `Opposite of substrate` — The gate
  material is the opposite of the substrate. This means that
  TPG = 1 in the device equations. This is the default
  option.
- `Same as substrate` — The
  gate material is the same as the substrate. This means that
  TPG = –1 in the device equations.

- `Aluminum` — The gate
  material is aluminum. This means that TPG = 0 in the device
  equations.

### **Surface state density, NSS** — Surface state density `NaN` `1/cm^2` (default) | scalar

Surface state density.

### **Junction depth, XJ** — Junction depth `0``m` (default)

Junction depth.

#### Dependencies

This parameter is only visible when you select `Level
3 MOS` for the **MOS model**
parameter in the **Model Selection**
settings.

### Temperature

### **Model temperature dependence using** — Temperature dependence model `Device temperature` (default) | `Fixed temperature`

Select one of these options for modeling the transistor temperature dependence:

- `Device temperature` — Use
  the device temperature to model temperature
  dependence.
- `Fixed temperature` — Use
  a temperature that is independent of the circuit temperature
  to model temperature dependence.

For more information, see Temperature Dependence.

#### Dependencies

Selecting `Device temperature` exposes
the **Offset local circuit temperature, TOFFSET**
parameter. Selecting `Fixed temperature`
exposes the **Fixed circuit temperature, TFIXED**
parameter.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default) | positive scalar

Transistor simulation temperature. The value must be greater than
`0`
`K`.

#### Dependencies

This parameter is only visible when you select `Fixed
temperature` for the **Model temperature
dependence using** parameter.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default) | positive scalar

The temperature at which the transistor parameters are measured. The
value must be greater than `0`
`K`.

### **Offset local circuit temperature, TOFFSET** — Local circuit temperature offset `0` `K` (default) | scalar

The amount by which the transistor temperature differs from the circuit
temperature.

#### Dependencies

This parameter is only visible when you select `Device
temperature` for the **Model temperature
dependence using** parameter.

## Libraries

Simscape / Electrical / Additional Components / SPICE Semiconductors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

SPICE-compatible N-Channel MOSFET

The SPICE NMOS block represents a SPICE-compatible
negative-channel (N-Channel) metal-oxide semiconductor (MOS) field-effect transistor
(FET). If the gate-source voltage increases the channel conductance increases. If the
gate-source voltage is decreased, the channel conductance decreases.

SPICE, or Simulation Program with Integrated Circuit Emphasis,
is a simulation tool for electronic circuits. You can convert some SPICE subcircuits into
equivalent Simscape™
Electrical™ models using the Environment Parameters block and
SPICE-compatible blocks from the Additional Components library. For more
information, see `subcircuit2ssc`.

### Equation Variables

Variables for the SPICE NMOS block equations include:

- Variables that you define by specifying parameters for the
  SPICE NMOS block. The visibility of
  some of the parameters depends on the value that you set for other
  parameters. For more information, see Parameters.
- Geometry-adjusted variables, which depend on several of the values
  that you specify using parameters for the SPICE
  NMOS block. For more information, see Geometry-Adjusted Variables.
- Temperature, *T*, which is `300.15`
  `K` by default. You can use a different value
  by specifying parameters for the SPICE
  NMOS block or by specifying parameters for both the
  SPICE NMOS block and an
  Environment
  Parameters block. For more information, see Transistor Temperature.
- Minimal conductance, *GMIN*, which is
  `1e-12`
  `1/Ohm` by default. You can use a different
  value by specifying a parameter for an Environment
  Parameters block. For more information, see Minimal Conduction.
- Thermal voltage, *Vtn*. For
  more information, see Thermal Voltage.

**Geometry-Adjusted Variables**

Several variables in the equations for the SPICE N-channel MOSFET model
consider the geometry of the device that the block represents. These
geometry-adjusted variables depend on variables that you define by specifying
SPICE NMOS block parameters. The
geometry-adjusted variables depend on these variables:

- *AREA* — Area of the device
- *SCALE* — Number of parallel connected
  devices
- The associated unadjusted variable

The table includes the geometry-adjusted variables and the
defining equations.

| Variable | Description | Equation |
| --- | --- | --- |
| *KPd* | Geometry-adjusted transconductance | KPd=KP\*AREA\*SCALE |
| *ISd* | Geometry-adjusted bulk saturation current | ISd=IS\*AREA\*SCALE |
| *JSd* | Geometry-adjusted bulk junction saturation current density | JSd=JS\*AREA\*SCALE |
| *CBDd* | Geometry-adjusted zero-bias bulk-drain capacitance | CBDd=CBD\*AREA\*SCALE |
| *CBSd* | Geometry-adjusted zero-bias bulk-source capacitance | CBSd=CBS\*AREA\*SCALE |
| *CGSOd* | Geometry-adjusted gate-source overlap capacitance | CGSOd=CGSO\*AREA\*SCALE |
| *CGDOd* | Geometry-adjusted gate-drain overlap capacitance | CGDOd=CGDO\*AREA\*SCALE |
| *CGBOd* | Geometry-adjusted gate-bulk overlap capacitance | CGBOd=CGBO\*AREA\*SCALE |
| *CJ* | Geometry-adjusted bottom capacitance per junction area | CJd=CJ\*AREA\*SCALE |
| *CJSW* | Geometry-adjusted sidewall capacitance per junction perimeter | CJSWd=CJSW\*AREA\*SCALE |
| *RDd* | Geometry-adjusted drain resistance | RDd=RDAREA\*SCALE |
| *RSd* | Geometry-adjusted source resistance | RSd=RSAREA\*SCALE |
| *RSHd* | Geometry-adjusted sheet resistance | RSHd=RSHAREA\*SCALE |

**Transistor Temperature**

There are two different options for defining transistor temperature,
*T*:

- Fixed temperature — The block uses a temperature that is
  independent of the circuit temperature when the **Model
  temperature dependence using** parameter in the
  **Temperature** settings of the
  SPICE NMOS block is set to
  `Fixed temperature`. For this model,
  the block sets *T* equal to
  *TFIXED*.
- Device temperature — The block uses a temperature that depends on circuit
  temperature when the **Model temperature dependence
  using** parameter in the
  **Temperature** settings of the
  SPICE NMOS block is set to
  `Device temperature`. For this model,
  the block defines temperature as

  T=TC+TOFFSET

  Where:

  - *TC* is the
    circuit temperature.

    If there is not an Environment
    Parameters block in the circuit,
    *TC* is
    equal to 300.15 K.

    If there is an Environment
    Parameters block in the circuit,
    *TC* is
    equal to the value that you specify for the
    **Temperature** parameter in the
    **SPICE** settings of the
    Environment
    Parameters block. The default value
    for the **Temperature** parameter is
    `300.15`
    `K`.
  - *TOFFSET* is the offset local circuit
    temperature.

**Minimal Conduction**

Minimal conductance, *GMIN*, has a default value of
`1e–12`
`1/Ohm`. To specify a different value:

1. If there is not already an Environment
   Parameters block in the circuit, add one.
2. In the **SPICE** settings of the
   Environment Parameters block,
   specify the desired *GMIN* value for the
   **GMIN** parameter.

**Thermal Voltage**

*Vtn* is the thermal voltage, which is defined as

Vtn=Nk\*Tq

Where:

- *N* is the emission
  coefficient.
- *T* is the transistor temperature.
  For more information, see Transistor Temperature.
- *k* is the Boltzmann constant.
- *q* is the elementary charge on an
  electron.

### Parameters Calculations

The tables show how the SPICE NMOS block determines some of
its parameters based on values that you specify.

**Drain Resistance**

| Parameter Values | | | Geometry-Adjusted Transistor Drain Resistance |
| --- | --- | --- | --- |
| **Drain resistance, RD** | **Sheet resistance, RSH** | **Number of drain squares, NRD** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRD* | 0 |
| *RD* | `NaN` or *RSH* | `NaN` or *NRD* | *RDd* |
| `NaN` | *RSH* | *NRD* | *RSHd*\**NRD* |

**Source Resistance**

| Parameter Values | | | Geometry-Adjusted Transistor Source Resistance |
| --- | --- | --- | --- |
| **Source resistance, RS** | **Sheet resistance, RSH** | **Number of source squares, NRS** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRS* | 0 |
| *RS* | `NaN` or *RSH* | `NaN` or *NRS* | *RSd* |
| `NaN` | *RSH* | *NRS* | *RSHd*\**NRS* |

**Transconductance and Surface Mobility**

| Parameter Values | | | Geometry-Adjusted Transconductance (level 1), in A/V2 | Geometry-Adjusted Transconductance (level 3), in A/V2 | Surface mobility (level 3), in cm2/s/V |
| --- | --- | --- | --- | --- | --- |
| **Oxide thickness, TOX** | **Surface mobility, U0** | **Transconductance, KP** |
| `NaN` | `NaN` | `NaN` | `2e-5` (default value) | `2e-5` (default value) | `600` (default value) |
| `NaN` | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| `NaN` | `U0` | `NaN` | `2e-5` | *UO*\**EPXox*/`1e-7` | `U0` |
| `NaN` | `U0` | `KP` | `KPd` | `KPd` | `U0` |
| *TOX* | `NaN` | `NaN` | `600`\**EPXox*/*TOX* | `600`\**EPXox*/*TOX* | `600` |
| *TOX* | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| *TOX* | `U0` | `NaN` | *UO*\**EPXox*/*TOX* | *UO*\**EPXox*/*TOX* | `U0` |
| *TOX* | `U0` | `KP` | `KPd` | `KPd` | `U0` |

**Oxide Thickness and Threshold Voltage**

| Parameter Values | | | | Surface potential, PHI (level 1), in V | Threshold voltage, VTO (level 1), in V | Surface potential, PHI (level 3), in V | Threshold voltage, VTO (level 3), in V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Oxide thickness, TOX** | **Substrate doping, NSUB** | **Surface potential, PHI** | **Threshold voltage, VTO** |
| `NaN` | `NaN` | `NaN` | `NaN` | `0.6` (default value) | 0 (default value) | `0.6` (default value) | 0 (default value) |
| `NaN` | `NaN` | `NaN` | `VTO` | `0.6` | `VTO` | `0.6` | `VTO` |
| `NaN` | `NaN` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | 0 |
| `NaN` | `NaN` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `NaN` | `NSUB` | `NaN` | `NaN` | `0.6` | 0 | `PHI (1e-7, NSUB)` | `VTO (1e-7, NSUB)` |
| `NaN` | `NSUB` | `NaN` | `VTO` | `0.6` | `VTO` | `PHI (1e-7, NSUB)` | `VTO` |
| `NaN` | `NSUB` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | `VTO (1e-7, NSUB)` |
| `NaN` | `NSUB` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `TOX` | `NaN` | `NaN` | `NaN` | `0.6` | 0 | `0.6` | 0 |
| `TOX` | `NaN` | `NaN` | `VTO` | `0.6` | `VTO` | `0.6` | `VTO` |
| `TOX` | `NaN` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | 0 |
| `TOX` | `NaN` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `TOX` | `NSUB` | `NaN` | `NaN` | `PHI (NSUB, TOX)` | `VTO (NSUB, TOX)` | `PHI (NSUB, TOX)` | `VTO (NSUB, TOX)` |
| `TOX` | `NSUB` | `NaN` | `VTO` | `PHI (NSUB, TOX)` | `VTO` | `PHI (NSUB, TOX)` | `VTO` |
| `TOX` | `NSUB` | `PHI` | `NaN` | `PHI` | `VTO (NSUB, TOX)` | `PHI` | `VTO (NSUB, TOX)` |
| `TOX` | `NSUB` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |

Where `PHI (NSUB, TOX)`, `PHI (1e-7,
NSUB)`, `VTO (NSUB, TOX)`, and `VTO (1e-7,
NSUB)` are obtained using these equations:

PHI=2kTqln(NSUBni)

GAMMA=2qεsiNSUBCox

VFB=φMS−qNSSCoxVTO=VFB+PHI+GAMMA\*PHI.

### Bulk-Source Diode Model

The table shows the equations that define the relationship between the bulk-source current,
*Ibs*, and the bulk-source voltage,
*Vbs*. As applicable, the model
parameters are first adjusted for temperature. For more information, see Temperature Dependence.

| Applicable Range of *Vbs* Values | Corresponding *Ibs* Equation |
| --- | --- |
| Vbs>80\*Vtn | Ibs=ISbs\*((VbsVtn−79)e80−1)+Vbs\*Gmin |
| 80Vtn≥Vbs | Ibs=ISbs\*(eVbs/Vtn−1)+Vbs\*Gmin |

Where:

- *ISbs* is the bulk saturation
  current, such that, if:

  - JSd≠0 and AS≠0, ISbs=JSd\*AS.

    Where:

    - *JSd*
      is the geometry-adjusted bulk junction saturation
      current density.
    - *AS* is the source
      area.
  - If JSd=0 or AS=0, ISbs=ISd, where
    *ISd* is the
    geometry-adjusted bulk saturation current.
- *Vtn* is the thermal voltage.
  For more information, see Thermal Voltage.
- *Gmin* is the minimal
  conductance. For more information, see Minimal Conduction.

### Bulk-Drain Diode Model

The table shows the equations that define the relationship between the bulk-drain current
*Ibd*, and the bulk-drain voltage,
*Vbd*. As applicable, the model
parameters are first adjusted for temperature. For more information, see Temperature Dependence.

| Applicable Range of *Vbd* Values | Corresponding *Ibd* Equation |
| --- | --- |
| Vbd>80\*Vtn | Ibd=ISbd\*((VbdVtn−79)e80−1)+Vbd\*Gmin |
| 80Vtn≥Vbd | Ibd=ISbd\*(eVbd/Vtn−1)+Vbd\*Gmin |

Where:

- *ISbd* is the bulk drain
  current, such that:

  - If JSd≠0 and AD≠0, ISbd=JSd\*AD.

    Where:

    - *JSd*
      is the geometry-adjusted bulk junction saturation
      current density.
    - *AD* is the drain
      area.
  - If JSd=0 or AD=0, ISbd=ISd, where
    *ISd* is the
    geometry-adjusted bulk saturation current.
- *Vtn* is the thermal voltage.
  For more information, see Thermal Voltage.
- *Gmin* is the minimal
  conductance. For more information, see Minimal Conduction.

### Level 1 Drain Current Model

This table shows relationship between the drain current,
*Id*, and the drain-source voltage,
*Vds*, in normal mode
(*Vds* ≥ 0). As applicable, model
parameters are first adjusted for temperature.

**Normal Mode**

| Applicable Range of *Vgs* and *Vds* Values | Corresponding *Id* Equation |
| --- | --- |
| Vgs-Von≤0 | Id=0 |
| 0<Vgs-Von≤Vds | Id=BETA\*(Vgs−Von)2(1+LAMBDA\*Vds)2 |
| 0<Vds<Vgs-Von | Id=BETA\*Vds((Vgs-Von)-Vds2)(1+LAMBDA\*Vds) |

Where:

- *Von* depends on
  *Vbs* and
  *PHI*.

  | Applicable Relationship of *Vbs* and *PHI* Values | Corresponding *Von* Equation |
  | --- | --- |
  | Vbs≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbs |
  | 0<Vbs≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
  | Vbs>2\*PHI | Von=MTYPE\*VBI |
- *MTYPE* is 1.
- *BETA* is BETA=(KPd\*WIDTH)/(LENGTH−2\*LD)
- *KP* is:

  - The **Transconductance, KP**, if this
    parameter has a numerical value.
  - U0\*3.9\*ε0/TOX, if **Transconductance,
    KP** is `NaN` and you specify
    values for both the **Oxide thickness,
    TOX** and **Substrate doping,
    NSUB** parameters.
- *WIDTH* is the channel width.
- *LENGTH* is the channel length.
- *LD* is the lateral diffusion.
- *VBI* is a built-in voltage value the block uses in
  calculations. The value is a function of temperature. For a detailed
  definition, see Temperature Dependence.
- *PHI* is:

  - The **Surface potential, PHI**, if this
    parameter has a numerical value.
  - 2\*kTmeas/q\*log(NSUB/ni), if **Surface potential,
    PHI** is `NaN` and you specify
    values for both the **Oxide thickness,
    TOX** and **Substrate doping,
    NSUB** parameters.
- *LAMBDA* is the channel modulation.
- *GAMMA* is:

  - The **Bulk threshold, GAMMA**, if this
    parameter has a numerical value.
  - TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0), if **Bulk threshold,
    GAMMA** is `NaN` and you
    specify values for both the **Oxide thickness,
    TOX** and **Substrate doping,
    NSUB** parameters.
- *ε0* is the permittivity of
  free space, 8.854214871e-12 F/m.
- *ni* is the carrier
  concentration of intrinsic silicon, 1.45e10
  cm-3.

This table shows relationship between the drain current
*Id* and the drain-source voltage
*Vds* in inverse mode (*Vds* < 0). As applicable, model parameters are first adjusted for
temperature.

**Inverse Mode**

| Applicable Range of *Vgd* and *Vds* Values | Corresponding *Id* Equation |
| --- | --- |
| Vgd-Von≤0 | Id=0 |
| 0<Vgd-Von≤−Vds | Id=−BETA(Vgd−Von)2(1−LAMBDA\*Vds)/2 |
| 0<−Vds<Vgd−Von | Id=BETA\*Vds((Vgd-Von)+Vds/2)(1−LAMBDA\*Vds) |

*Von* depends on
*Vbd* and
*PHI*.

| Applicable Relationship of *Vbs* and *PHI* Values | Corresponding *Von* Equation |
| --- | --- |
| Vbd≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbd |
| 0<Vbd≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
| Vbd>2\*PHI | Von=MTYPE\*PHI |

### Level 3 Drain Current Model

The block provides the following model for drain current
*Ids* in normal mode (Vds≥0) after adjusting the applicable model parameters for temperature.

IDS=IDS0\*ScaleVMAX\*ScaleLChan\*ScaleINV

Where:

- *IDS0* is the Basic Drain Current
  Model.
- *ScaleVMAX* is the Velocity Saturation
  Scaling.
- *ScaleLChan* is the Channel Length
  Modulation Scaling.
- *ScaleINV* is the Weak Inversion
  Scaling.

The block uses the same model for drain current in inverse mode (Vds<0), with the following substitutions:

Vbs≡Vbs−Vds

Vgs≡Vgs−Vds

Vds≡−Vds

**Basic Drain Current Model**

The relationship between the drain current, *Ids*,
and the drain-source voltage, *Vds* is

IDS0=BETA\*Fgate\*(VGSX−VTH−1+FB2\*VDSX)\*VDSX

Where:

- *BETA* is calculated as described in Level 1 Drain Current Model.
- *FGATE* is calculated as

  Fgate=11+THETA\*(Vgsx−VTH)

  Where:

  - *THETA* models the dependence of the
    mobility on the gate-source voltage.
  - Vgsx=max(VGS,Von)
- If you specify a nonzero value for the **Fast surface
  state density, NFS** parameter, the block calculates
  *Von* using this equation:

  Von=VTH+xnVT

  Otherwise,

  Von=VTH
- The block calculates *xn* as

  xn=1+q\*NFSCOX+(GAMMA\*Fs\*Vbulk+Fn\*VbulkWIDTH)2\*Vbulk
- The block calculates
  *Vbulk* as follows:

  - If

    VBS≤0,

    Vbulk=PHI−VBS.
  - Otherwise, the block calculates
    *Vbulk* as

    Vbulk=PHI(1+VBS2\*PHI)2
- Thermal voltage such that

  VT=kTq
- The block calculates *VTH*
  using the following equation:

  VTH=VBI−8.15e−22\*ETACOX\*(LENGTH−2\*LD)3\*VDS​​​​​​​​​​            +GAMMA\*Fs\*Vbulk+Fn\*Vbulk

  For information about how the block calculates
  *VBI*, see Temperature Dependence.
- *ETA* is the **Vds dependence threshold
  volt, ETA**.
- COX=εoxTOX,

  Where
  *εox* is the
  permittivity of the oxide and *TOX* is the
  **Oxide thickness, TOX**.
- If you specify a nonzero value for the **Junction depth,
  XJ** parameter and a value for the **Substrate
  doping, NSUB** parameter, the block calculates
  *Fs* using these equations:

  α=2εsiqNSUB

  XD=α

  wc=.0631353+.8013292\*XD\*VbulkXJ−.01110777\*(XD\*VbulkXJ)2+LDXJ

  Fs=1−(wc\*1−(XD\*VbulkXJ+XD\*Vbulk)2−LDXJ)

  Where
  *εsi* is the
  permittivity of silicon.

  Otherwise,

  Fs=1
- The block calculates *FB* as

  FB=GAMMA\*Fs4\*Vbulk+Fn
- The block calculates *Fn* as

  Fn=DELTA\*π\*εsi2\*COX\*WIDTH
- *DELTA* is the width effect on threshold.
- *VDSX* is the lesser of
  *VDS* and the
  saturation voltage,
  *Vdsat*.

  - If you specify a positive value for the **Max
    carrier drift velocity, VMAX** parameter, the
    block calculates
    *Vdsat* using
    the following equation:

    Vdsat=Vgsx−VTH1+FB+(LENGTH−2\*LD)\*VMAXUO\*Fgate             −(Vgsx−VTH1+FB)2+((LENGTH−2\*LD)\*VMAXUO\*Fgate)2

    Otherwise, the block calculates
    *Vdsat* as

    Vdsat=Vgsx−VTH1+FB

**Velocity Saturation Scaling**

If you specify a positive value for the **Max carrier drift velocity,
VMAX** parameter, the block calculates
*ScaleVMAX* as

ScaleVMAX=11+UO\*Fgate(LENGTH−2\*LD)\*VMAX\*VDSX

Otherwise,

ScaleVMAX=1

**Channel Length Modulation Scaling**

The block scales the drain current to account for channel length modulation if
the block meets all of the following criteria:

- VDS>Vdsat
- The **Max carrier drift velocity, VMAX** is less than or equal to zero
  or *α* is nonzero.

The block scales the drain current using the following equation:

ScaleLChan=11−Δl(LENGTH−2\*LD)

To calculate Δl the block:

1. Calculates the intermediate value Δl0.

   - If you specify a positive value for the **Max carrier drift velocity,
     VMAX** parameter, the block computes the
     intermediate value
     *gdsat* as the
     greater of 1e-12 and the result of the following equation:

     IDS0\*(1−11+Scalegdsat\*VDSX)\*Scalegdsat

     Where:

     Scalegdsat=UO\*Fgate(LENGTH−2\*LD)\*VMAX

     Then, the block uses the following equation to calculate the intermediate value
     Δ*l0*:

     Δl0=(KA\*IDS2\*(LENGTH−2\*LD)\*gdsat)2+KA\*(VDS−Vdsat)            −KA\*IDS2\*(LENGTH−2\*LD)\*gdsat

     Where

     KA=KAPPA\*α.
   - Otherwise, the block uses the following equation to
     calculate the intermediate value Δl0 as

     Δl=KA\*(VDS−Vdsat)
2. The block checks for punch through and calculates Δl.

   - If

     Δl0>(LENGTH−2\*LD)/2,

     the block calculates Δl using the following equation:

     Δl=(1−(LENGTH−2\*LD)4\*Δl0)\*(LENGTH−2\*LD)
   - Otherwise,

     Δl=Δl0.

**Weak Inversion Scaling**

If *VGS* is less than
*Von*, the block calculates
*ScaleINV* using the following equation:

ScaleINV=eVgs−Vonxn\*VT

Otherwise,

ScaleINV=1

### Junction Charge Model

The block models Junction Overlap Charges and Bulk Junction Charges.

**Junction Overlap Charges**

The block calculates the following junction overlap charges:

- QGS=CGSOd\*WIDTH\*Vgs

  Where:

  - *QGS* is the
    gate-source overlap charge.
  - *CGSOd* is the
    geometry adjusted gate-source overlap
    capacitance.
  - *WIDTH* is the channel width.
- QGD=CGDOd\*WIDTH\*Vgd

  Where:

  - *QGD* is the
    gate-drain overlap charge.
  - *CGDOd* is the
    geometry adjusted gate-drain overlap capacitance.
- QGB=CGBOd\*(LENGTH−2\*LD)\*Vgb

  Where:

  - *QGB* is the
    gate-bulk overlap charge.
  - *CGBOd* is the
    geometry adjusted gate-bulk overlap capacitance.
  - *LENGTH* is the channel
    length.
  - *LD* is the lateral diffusion.

**Bulk Junction Charges**

This table shows relationship between the bulk-drain bottom junction charge
*Qbottom* and the junction
voltage, *Vbd*. As applicable, model
parameters are first adjusted for temperature.

| Applicable Range of *Vbd* Values | Corresponding *Qbottom* Equation |
| --- | --- |
| Vbd<FC\*PB | Qbottom=CBDd\*PB\*(1-(1-VbdPB)1−MJ)1−MJ if CBDd>0  Qbottom=CJd\*AD\*PB\*(1-(1-VbdPB)1−MJ)1−MJ otherwise. |
| Vbd≥FC\*PB | Qbottom=CBDd\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) if CBDd>0  Qbottom=CJd\*AD\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) otherwise. |

Where:

- *PB* is the bulk junction potential.
- *FC* is the capacitance coefficient.
- *CBDd* is the
  geometry-adjusted zero-bias bulk-drain capacitance.
- *CJd* is the
  geometry-adjusted bottom capacitance per junction area.
- *AD* is the drain area.
- *MJ* is the bottom grading coefficient.
- F1=PB\*(1-(1-FC)1−MJ)1−MJ
- F2=(1-FC)1+MJ
- F3=1-FC\*(1+MJ)

To calculate the bulk-source bottom junction charge, the block substitutes
variables in the equations in the preceding table. The block substitutes:

- *Vbs* for
  *Vbd*
- *AS* for *AD*
- *CBSd* for
  *CBDd*

This table shows relationship between the bulk-drain sidewall junction charge
*Qsidewall* and the junction
voltage *Vbd*. As applicable, model
parameters are first adjusted for temperature.

| Applicable Range of *Vbd* Values | Corresponding *Qsidewall* Equation |
| --- | --- |
| Vbd<FC\*PB | Qsidewall=CJSWd\*PD\*PB\*(1-(1-VbdPB)1−MGSW)1−MGSW |
| Vbd≥FC\*PB | Qsidewall=CJSWd\*PD\*                      (F1+F3\*(Vbd-FC\*PB)+MGSW\*(Vbd2-(FC\*PB)2)2\*PBF2) |

Where:

- *CJSWd* is the geometry
  adjusted sidewall capacitance per junction perimeter.
- *PD* is the drain perimeter.
- *MGSW* is the side grading coefficient.
- F1=PB\*(1-(1-FC)1−MJSW)1−MJSW
- F2=(1-FC)1+MJSW
- F3=1-FC\*(1+MJSW)

To calculate the bulk-source sidewall junction charge and the sidewall
junction voltage, the block substitutes variables in the equations in the
preceding table. The block substitutes:

- *Vbs* for
  *Vbd*
- *PS* for *PD*

### Capacitance Model

The SPICE NMOS block allows you to model the
transistor capacitance model in three different ways:

- No intrinsic capacitance model
- Meyer Gate Capacitance Model
- Charge Conservation Capacitance Model

**Meyer Gate Capacitance Model**

This table shows the relationship between the operational regions of the
transistor and the gate-bulk, gate-drain, and gate-source capacitances.

| Operational region | Gate-Bulk, *Cgb*, Gate-Drain, *Cgd*, and Gate-Source, *Cgs*, Equations | |
| --- | --- | --- |
| Accumulation region, Vgb<VFB | Cgb=CoxtCgd=0Cgs=0 | |
| Depletion region, Vgs<VTH | Cgb=Coxt1+4GAMMA2\*(Vgb−VFB)Cgd=0Cgs=0 | |
| Saturation region, Vgs−VTH<Vds | if Vds<Vsatmin then: | if Vds≥Vsatmin then: |
| Cgb=0Cgd=23(Coxt−Cgb)(1−(Vsatmin)2(2Vsatmin−Vds)2)Cgs=23(Coxt−Cgb)(1−(Vsatmin−Vds)2(2Vsatmin−Vds)2) | Cgb=0Cgd=0Cgs=23(Coxt−Cgb) |
| Linear region, Vgs−VTH>Vds | Cgb=0Cgd=23(Coxt−Cgb)\*(1−(Vgs−VTH)2(2\*(Vgs−VTH)−Vds)2)Cgs=23(Coxt−Cgb)\*(1−(Vgs−VTH−Vds)2(2\*(Vgs−VTH)−Vds)2) | |

where:

- Coxt=WIDTH\*(LENGTH−2\*LD)\*COX\*AREA\*SCALE
- VFB=VBI\*MTYPE−PHI is the flat-band voltage.
- *Vsatmin* is the minimum
  saturation voltage. It is a predefined parameter equal to
  `1`
  `V`.

These equations are continuous between the depletion region and the
accumulation region, and discontinuous between the depletion and the inversion
region. Other SPICE tools apply smoothing functions between the inversion and
depletion regions.

Cgb=WIDTH\*LENGTH\*COX(1+4GAMMA2\*(VTH−Vbs−VFB))m\*smoothingsmoothing=1(1+4GAMMA2\*(Vgs−VTH))m

where *m* is a predefined smoothing
constant.

**Charge Conservation Capacitance Model**

This table shows the relationship between the operational regions of the
transistor and the gate, bulk, channel, drain, and source charges for a level 1
MOS.

| Operational region | Level-1 Charges Equations |
| --- | --- |
| Accumulation region, Vgb<VFB | Qg=Coxt\*(Vgb−VFB)Qb=−Coxt\*(Vgb−VFB)Qc=0Qd=0Qs=Qc−Qd |
| Depletion region, Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qc=0Qd=0Qs=Qc−Qd |
| Saturation region, Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vgs−VTH3)Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vgs−VTH3)Qd=0Qs=Qc−Qd |
| Linear region, Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vds2+Vds212(Vgs−VTH−0.5Vds))Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vds2+Vds212(Vgs−VTH−0.5Vds))Qd=−Coxt\*(Vgs−VTH2−3Vds4+Vds28(Vgs−VTH−0.5Vds))Qs=Qc−Qd |

where:

- Qc=−(Qg+Qb)=Qd+Qs is the charge in channel.
  *Qc* needs to be
  partitioned between *Qd* and
  *Qs*.

where:

- *Qg* is the gate
  charge.
- *Qb* is the bulk
  charge.
- *Qd* is the drain
  charge.
- *Qs* is the source
  charge.
- Qc=−(Qg+Qb)=Qd+Qs is the charge in channel.
  *Qc* needs to be
  partitioned between *Qd* and
  *Qs*.

This table shows the relationship between the operational regions of the
transistor and the gate, bulk, channel, drain, and source charges for a level-3
MOS.

| Operational region | Level-3 Charges Equations |
| --- | --- |
| Accumulation region, Vgb<VFB | Qg=Coxt\*(Vgb−VFB)−SF1+SF2Qb=−Coxt\*(Vgb−VFB)−SF1+SF2Qc=0Qd=0Qs=Qc−Qd |
| Depletion region, Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))−SF1+SF2Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))+SF1−SF2Qc=0Qd=0Qs=Qc−Qd |
| Saturation region, Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vdsat−Vdsat2+1+FB12\*Fi\*Vdsat2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vdsat−Fb2\*Vds−FB\*(1+FB)12\*Fi\*Vdsat2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vdsat+(1+FB)212\*Fi\*Vdsat2)Qd=0Qs=Qc−Qd |
| Linear region, Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vds−Vds2+1+FB12\*Fi\*Vds2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vds+FB2\*Vds−FB\*(1+FB)12\*Fi\*Vds2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vds+(1+FB)212\*Fi\*Vds2)Qd=−Coxt\*(Vgs−VTH2−3(1+FB)2\*Vds+(1+FB)28\*Fi\*Vds2)Qs=Qc−Qd |

where:

- *Vdsat* is the saturation
  voltage
- *FB* is the body effect
  coefficient
- *ETA* is the drain-source voltage threshold
  coefficient
- Fi=Vgs−VTH−1+FB2\*Vds
- SF1=−0.5\*Coxt\*GAMMA2\*(1−(1+4GAMMA2\*2(VTH−Vbs−VFB))0.5) and SF2=Coxt\*(VTH−VFB−PHI) are smoothing factors between depletion and
  accumulation regions to help with convergence.

### Temperature Dependence

The transconductance as a function of the transistor temperature is

KP(T)=KPd(TTmeas)3/2

Where:

- *KPd* is the geometry-adjusted
  transconductance.
- *T* is the transistor temperature. For more
  information, see Transistor Temperature.
- *Tmeas* is the parameter
  extraction temperature.

The surface potential as a function of the transistor temperature is

PHI(T)=TTmeas(PHI+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasTmeas)))                          −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

Where:

- *PHI* is the surface potential.
- *k* is the Boltzmann constant.
- *q* is the elementary charge on an
  electron, 1.6021918e-19 C.
- *EG* is the activation energy, such that:

  - EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
  - EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

The built-in voltage as a function of the transistor temperature is

VBI(T)=VTO+MTYPE\*(PHI(T)−PHI2−GAMMAPHI)                               +EGTmeas−EGT2

Where:

- *VBI* is the built-in voltage.
- *VTO* is the threshold voltage.
  *VTO* depends on the value that you specify for the
  **Threshold voltage, VTO** parameter in the
  **DC currents** settings. If you specify a
  numerical value, *VTO* is evaluated as that value. If
  you specify a nonnumerical value (`NAN`) and you
  specify numerical values for both the **Oxide thickness,
  TOX** and **Substrate doping, NSUB**
  parameters in the **Process** settings, then
  *VTO* is evaluated as Φ−3.25+EGTmeas/2+MTYPE\*PHI/2−NSS\*q\*TOX/(3.9\*ε0)+MTYPE\*(GAMMA\*PHI+PHI), Where:

  - *Φ* depends on the gate type, which you
    specify using the **Gate type, TPG**
    parameter. If you specify `Aluminum
    (0)`, Φ=3.2. Otherwise, Φ=3.25+EGTmeas/2−MTYPE\*TPG\*EGTmeas/2, Where:

    - *MTYPE* is the transistor
      type. For an N-channel MOSFET,
      *MTYPE* = 1.
    - *TPG* represents the gate
      type and also depends on the option that you
      specify for the **Gate type,
      TPG** parameter in the
      **Process** settings. If you specify

      - `Opposite of substrate
        (1)` — *TPG*
        = 1
      - `Same as substrate
        (-1)` — *TPG*
        = -1
  - *NSS* is the surface state
    density.
  - *TOX* is the oxide thickness.
  - *ε0* is the
    permittivity of free space.
  - *GAMMA* is the bulk threshold.
    *GAMMA* depends on the value that you
    specify for the **Bulk threshold, GAMMA**
    parameter in the **DC currents** settings.
    If you specify a numerical value, *GAMMA*
    is evaluated as that value. If you specify a nonnumerical
    value (`NAN`) and you specify numerical
    values for both the **Oxide thickness,
    TOX** and **Substrate doping,
    NSUB** parameters in the
    **Process** settings, then
    *VTO* is evaluated as TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0), where *NSUB* is the
    substrate doping.

The bulk saturation current as a function of the transistor temperature is

IS(T)=ISd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

Where:

- *ISd* is the geometry-adjusted
  bulk saturation current.
- *ND* is the emission coefficient.

The bulk junction saturation current density as a function of the transistor temperature is

JS(T)=JSd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

Where *JSd* is the
geometry-adjusted bulk junction saturation current density.

The bulk junction potential as a function of the transistor temperature is

PB(T)=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))TmeasT                         −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

Where *PB* is the bulk junction
potential.

The bulk-drain junction capacitance as a function of the transistor temperature is

CBD(T)=CBDdpbo+MJ\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJ\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

Where:

- *CBDd* is the geometry
  adjusted zero-bias bulk-drain capacitance.
- *MJ* is the bottom grading coefficient.
- pbo=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))Tmeas300.15

The block uses the *CBD(T)* equation to calculate:

- The bulk-source junction capacitance by substituting
  *CBSd*, the
  geometry-adjusted zero-bias bulk-source capacitance, for
  *CBDd*.
- The bottom junction capacitance by substituting
  *CJd*, the
  geometry-adjusted bottom capacitance per junction area for
  *CBDd*.

The relationship between the sidewall junction capacitance *CJSW* and the
transistor temperature, *T*, is

CJSW(T)=CJSWdpbo+MJSW\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJSW\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

Where:

- *CJSWd* is the side
  geometry-adjusted sidewall capacitance per junction perimeter.
- *MJSW* is the side grading coefficient.
