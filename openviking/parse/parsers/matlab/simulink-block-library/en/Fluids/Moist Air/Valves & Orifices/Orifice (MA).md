---
type: simulink-block
title: 'Orifice (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices'
documentation_page: 'orificema'
documentation_source_path: 'ref/orificema.html'
language: en
---

# Orifice (MA)

## Ports
```yaml
ports:
- name: A
  summary: Fluid entry or exit moist air
  direction: conserving
- name: B
  summary: Fluid entry or exit moist air
  direction: conserving
- name: S
  summary: Control member position, m physical signal
  direction: input
```

### Conserving

### **A** — Fluid entry or exit moist air

Moist air conserving port associated with the fluid entry or exit
port.

### **B** — Fluid entry or exit moist air

Moist air conserving port associated with the fluid entry or exit
port.
### Input

### **S** — Control member position, m physical signal

Control member position that sets the orifice opening.

#### Dependencies

To enable this port, set **Orifice type** to
`Variable`.
## Parameters
```yaml
parameters:
- name: Orifice type
  summary: Constant or variable orifice Variable (default) | Constant
  group: ''
- name: Orifice parameterization
  summary: Variable or constant orifice parameterization Cv flow coefficient (default) | Kv flow coefficient | Sonic conductance
    | Orifice area
  group: ''
- name: Opening characteristic
  summary: Method to convert from control signal to measure of flow capacity Linear (default) | Tabulated
  group: ''
- name: Control member position at closed orifice
  summary: Control member offset 0 m (default) | positive scalar
  group: ''
- name: Control member travel between closed and open orifice
  summary: Control member stroke 5e-3 m (default) | positive scalar
  group: ''
- name: Opening orientation
  summary: Direction of displacement that opens the orifice Positive control member displacement opens orifice (default) |
    Negative control member displacement opens orifice
  group: ''
- name: Cv flow coefficient
  summary: Flow coefficient 4 (default) | positive scalar
  group: ''
- name: Maximum Cv flow coefficient
  summary: '*Cv* coefficient that corresponds to maximally open component 4 (default) | positive scalar'
  group: ''
- name: Control member position vector
  summary: Vector of control member positions [0, .002, .004, .007, .017] m (default) | 1-by-*n* vector
  group: ''
- name: Cv flow coefficient vector
  summary: '*Cv* coefficients that correspond to values in member position vector [1e-06, .8, 1.6, 2.4, 3.2, 4] (default)
    | 1-by-*n* vector'
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7 (default) | positive scalar
  group: ''
- name: Kv flow coefficient
  summary: Flow coefficient 3.6 (default) | positive scalar
  group: ''
- name: Maximum Kv flow coefficient
  summary: '*Kv* coefficient that corresponds to maximally open component 3.6 (default) | positive scalar'
  group: ''
- name: Kv flow coefficient vector
  summary: '*Kv* coefficients that correspond to values in member position vector [1e-06, .72, 1.44, 2.16, 2.88, 3.6] (default)
    | 1-by-*n* vector'
  group: ''
- name: Sonic conductance
  summary: Measure of flow rate capacity in choked flow regime 12 l/(bar*s) (default) | positive scalar
  group: ''
- name: Maximum sonic conductance
  summary: Sonic conductance corresponding to maximally open component 12 l/(bar*s) (default) | positive scalar
  group: ''
- name: Critical pressure ratio
  summary: Ratio of downstream and upstream pressures at which the flow first chokes 0.3 (default) | positive scalar
  group: ''
- name: Subsonic index
  summary: Exponent used to characterize mass flow in subsonic flow regime 0.5 (default) | positive scalar
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 reference temperature 293.15 K (default) | scalar
  group: ''
- name: ISO reference density
  summary: ISO 8778 reference density 1.185 kg/m^3 (default) | positive scalar
  group: ''
- name: Sonic conductance vector
  summary: Sonic conductances corresponding to values in control member position vector [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)
    (default) | vector of positive values
  group: ''
- name: Critical pressure ratio vector
  summary: Critical pressure ratios corresponding to values in control member position vector 0.3 * ones(1,6) (default) |
    vector of positive numbers
  group: ''
- name: Orifice area
  summary: Area of orifice opening 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Orifice area vector
  summary: Vector of orifice opening area values [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: ''
- name: Leakage flow fraction
  summary: Ratio of flow rates 1e-6 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Laminar flow pressure ratio
  summary: Laminar-turbulent transition pressure ratio 0.999 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Valve port areas 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Orifice type** — Constant or variable orifice `Variable` (default) | `Constant`

Type of orifice. When you set this parameter to
`Variable`, the orifice area varies according
to the input signal received at port **S**.

### **Orifice parameterization** — Variable or constant orifice parameterization `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

Method the block uses to calculate the mass flow rate from the pressure
difference across the orifice or the pressure difference from the mass flow
rate.

### **Opening characteristic** — Method to convert from control signal to measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to convert the control signal specified at port **S** to the chosen measure of flow capacity.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`.

### **Control member position at closed orifice** — Control member offset `0` m (default) | positive scalar

Control member offset, or the value at **S** when the
orifice is fully closed.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Opening
characteristic** to
`Linear`.

### **Control member travel between closed and open orifice** — Control member stroke `5e-3` m (default) | positive scalar

Distance the control member travels between a closed and open orifice.
When you set **Opening orientation** to
`Positive control member displacement opens
orifice`, the orifice is fully open at the sum of the
**Control member position at closed orifice** and
**Control member travel between closed and open
orifice** parameters. When you set **Opening
orientation** to `Negative control member
displacement opens orifice`, the orifice is fully open at
the difference between the **Control member position at closed
orifice** and **Control member travel between closed
and open orifice** parameters.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, and **Opening
characteristic** to `Linear`.

### **Opening orientation** — Direction of displacement that opens the orifice `Positive control member displacement opens orifice` (default) | `Negative control member displacement opens orifice`

Direction of the member displacement that opens the variable orifice. A
positive orientation means that an increase in the signal at
**S** opens the orifice. A negative orientation means
that a decrease in the signal at **S** opens the
orifice.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv* flow
coefficient. This parameter measures the ease with which the vapor traverses
the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Cv flow
coefficient`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the orifice is fully open and the area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Cv flow
coefficient`, and **Opening
characteristic** to
`Linear`.

### **Control member position vector** — Vector of control member positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for the tabulated orifice
parameterizations. The vector elements correspond one-to-one to the values
in the **Orifice area vector**, **Cv flow
coefficient vector**, or **Kv flow coefficient
vector** parameters.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Opening
characteristic** to
`Tabulated`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow coefficients.
Each coefficient corresponds to a value in the **Control member
position vector** parameter. This parameter measures the ease
with which the vapor traverses the resistive element when driven by a
pressure differential. The size of the vector must be the same as the
**Control member position vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Cv flow
coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet pressure,
*pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, **Orifice
parameterization** to `Cv flow
coefficient` or `Kv flow
coefficient`.

### **Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv* flow
coefficient. This parameter measures the ease with which the vapor traverses
the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Kv flow
coefficient`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow coefficient
when the orifice is fully open and the area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Kv flow
coefficient`, and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow coefficients.
Each coefficient corresponds to a value in the **Control member
position vector** parameter. This parameter measures the ease
with which the vapor traverses the resistive element when driven by a
pressure differential. The size of the vector must be the same as the
**Control member position vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Kv flow
coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **Sonic conductance** — Measure of flow rate capacity in choked flow regime `12 l/(bar*s)` (default) | positive scalar

Ratio, measured at the onset of choking, of the mass flow rate through the
resistive element to the product of the upstream pressure and mass density
at standard conditions as defined in ISO 8778. This parameter determines the
maximum flow rate allowed at a given upstream pressure.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Sonic
conductance`.

### **Maximum sonic conductance** — Sonic conductance corresponding to maximally open component `12 l/(bar*s)` (default) | positive scalar

Value of the sonic conductance when the control signal specified at port
**S** is `1` and
cross-sectional area available for flow is at a maximum.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Sonic
conductance`, and **Opening
characteristic** to
`Linear`.

### **Critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes `0.3` (default) | positive scalar

Pressure ratio at which flow first begins to choke and the flow velocity
reaches its maximum, given by the local speed of sound. The pressure ratio
is the outlet pressure divided by inlet pressure.

#### Dependencies

To enable this parameter, set either:

- **Orifice type** to
  `Constant` and
  **Orifice parameterization** to
  `Sonic conductance`.
- **Orifice type** to
  `Variable`, **Orifice
  parameterization** to `Sonic
  conductance`, and **Opening
  characteristic** to
  `Linear`.

### **Subsonic index** — Exponent used to characterize mass flow in subsonic flow regime `0.5` (default) | positive scalar

Empirical value used to more accurately calculate the mass flow rate in
the subsonic flow regime.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Sonic
conductance`.

### **ISO reference temperature** — ISO 8778 reference temperature `293.15 K` (default) | scalar

Temperature at standard reference atmosphere, defined as 293.15 K in ISO
8778.

You only need to adjust the ISO reference parameter values if you are
using sonic conductance values that are obtained at difference reference
values.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Sonic
conductance`.

### **ISO reference density** — ISO 8778 reference density `1.185 kg/m^3` (default) | positive scalar

Density at standard reference atmosphere, defined as 1.185 kg/m3 in ISO
8778.

You only need to adjust the ISO reference parameter values if you are
using sonic conductance values that are obtained at difference reference
values.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Sonic
conductance`.

### **Sonic conductance vector** — Sonic conductances corresponding to values in control member position vector `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)` (default) | vector of positive values

Vector of sonic conductances inside the resistive element. Each
conductance corresponds to a value in the **Control member position
vector** parameter. The size of the vector must be the same as
the **Control member position vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Sonic
conductance`, and **Opening
characteristic** to
`Tabulated`.

### **Critical pressure ratio vector** — Critical pressure ratios corresponding to values in control member position vector `0.3 * ones(1,6)` (default) | vector of positive numbers

Vector of critical pressure ratios at which the flow first chokes, with
each critical pressure ratio corresponding to a value in the
**Control member position vector** parameter. The
critical pressure ratio is the fraction of downstream-to-upstream pressures
at which the flow velocity reaches the local speed of sound. The size of the
vector must be the same as the **Control member position
vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Sonic
conductance`, and **Opening
characteristic** to
`Tabulated`.

### **Orifice area** — Area of orifice opening `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the orifice opening.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Orifice
area`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Orifice area when it is fully open.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Orifice
area`, and **Opening characteristic**
to `Linear`.

### **Orifice area vector** — Vector of orifice opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the
orifice area. The values in this vector correspond one-to-one with the
elements in the **Control member position vector**
parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`, **Orifice
parameterization** to `Orifice
area`, and **Opening characteristic**
to `Tabulated`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate. This parameter accounts for
real-world losses that are not captured in the orifice equation.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Orifice
area`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Opening
characteristic** to `Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the orifice is in near-open or near-closed positions.
Set this parameter to a nonzero value less than one to increase the
stability of your simulation in these regions.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Opening
characteristic** to `Linear`.

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the orifice outlet pressure to orifice inlet pressure at which
the fluid transitions between the laminar and turbulent regimes. The
pressure loss corresponds to the mass flow rate linearly in laminar flows
and quadratically in turbulent flows.

### **Cross-sectional area at ports A and B** — Valve port areas `0.01` m^2 (default) | positive scalar

Area of the orifice ports **A** and
**B**.
## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Orifice in a moist air network

The Orifice (MA) block models pressure loss due to a constant or variable area orifice
in a moist air network. The block calculates fluid properties inside the valve from
inlet conditions. There is no heat exchange between the fluid and the environment, and
therefore phase change inside the orifice only occurs due to a pressure drop or a
propagated phase change from another part of the model.

The orifice can be constant or variable. When the **Orifice type**
parameter is `Variable`, the physical signal at port
**S** sets the position of the control member, which opens and
closes the orifice.

### Orifice Parameterizations

The block behavior depends on the **Orifice parametrization**
parameter:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  determines the block parameterization. The flow coefficient measures the
  ease with which the moist air can flow when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *K*v, where Kv=0.865Cv, determines the block parameterization. The flow
  coefficient measures the ease with which the moist air can flow when driven
  by a certain pressure differential.
- `Sonic conductance` — The sonic conductance of
  the resistive element at steady state determines the block parameterization.
  The sonic conductance measures the ease with which the moist air can flow
  when *choked*, which is a condition in which the flow
  velocity is at the local speed of sound. Choking occurs when the ratio
  between downstream and upstream pressures reaches a critical value known as
  the *critical pressure ratio*.
- `Orifice area` — The size of the flow restriction
  determines the block parametrization.

### Variable Orifice

When you set **Orifice type** to
`Variable` and **Opening
characteristic** to `Linear`, the block
uses the input at port **S** to calculate the
orifice opening,

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

where *S* is the value of the signal at port
**S**, and *Smin*
and *ΔS* are the values of the **Control member
position at closed orifice** and **Control member travel
between closed and open orifice** parameters, respectively.

When you set **Orifice type** to
`Variable` and **Opening
characteristic** to `Tabulated`, the block
interpolates the orifice characteristics from the **Control member
position vector** parameter and the input at port **S**.

For a variable orifice, the flow rate in the orifice depends on the
**Opening characteristic** parameter:

- `Linear` — The measure of flow capacity is
  proportional to the control signal at port **S**. As the control signal increases, the measure of flow
  capacity scales from the specified minimum to the specified
  maximum.

  When you set **Orifice parameterization** to
  `Cv flow coefficient` or `Kv
  flow coefficient`, the block treats the parameter
  **xT pressure differential ratio factor at choked
  flow** as a constant independent of the control signal.
- `Tabulated` — The block calculates the
  measure of flow capacity as a function of the control signal at port
  **S**. This function uses a
  one-dimensional lookup table.

  When you set **Orifice parameterization** to
  `Cv flow coefficient` or `Kv
  flow coefficient`, the block treats the parameter
  **xT pressure differential ratio factor at choked
  flow** as a function of the control signal.

### Momentum Balance

The block equations depend on the **Orifice parametrization**
parameter.

**Cv Flow Coefficient Parameterization**

When you set **Orifice parametrization** to `Cv
flow coefficient`, the mass flow rate is

m˙=CvN6Y(pin−pout)vin,

where:

- *Cv* is the flow
  coefficient.
- *N6* is a constant equal
  to 27.3 when mass flow rate is in kg/hr, pressure is in bar, and
  density is in kg/m3.
- *Y* is the expansion factor.
- *pin* is the inlet
  pressure.
- *pout* is the outlet
  pressure.
- *vin* is the inlet
  specific volume.

The expansion factor is

Y=1−pin−pout3pinFγxT,

where:

- *Fγ* is the ratio of the
  isentropic exponent to 1.4.
- *xT* is the value of the
   **xT pressure differential ratio factor at choked
  flow** parameter.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter,
*Blam*,

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

where:

Ylam=1−1−Blam3FγxT.

When the pressure ratio, pout/pin, falls below 1−FγxT, the orifice becomes choked and the block uses the equation

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

When you set **Orifice parametrization** to `Kv
flow coefficient`, the block uses the same equations as the
`Cv flow coefficient` parametrization, but replaces
*Cv* with
*Kv* using the relation Kv=0.865Cv.

**Sonic Conductance Parameterization**

When you set **Orifice parametrization** to `Sonic
conductance`, the mass flow rate is

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

where:

- *C* is the sonic conductance.
- *Bcrit* is the critical
  pressure ratio.
- *m* is the value of the **Subsonic
  index** parameter.
- *Tref* is the value of the
  **ISO reference temperature** parameter.
- *ρref* is the value of the
  **ISO reference density** parameter.
- *Tin* is the inlet
  temperature.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter
*Blam*,

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

When the pressure ratio, pout/pin, falls below the critical pressure ratio,
*Bcrit*, the orifice becomes
choked and the block switches to the equation

m˙=CρrefpinTrefTin.

The `Sonic conductance` setting of the
**Orifice parameterization** parameter is for pneumatic
applications. If you use this setting for moist air with high levels of trace
gasses or are modeling a fluid other than air, you may need to scale the sonic
conductance by the square root of the mixture specific gravity.

**Orifice Area Parameterization**

When you set **Orifice parametrization** to
`Orifice area`, the mass flow rate is

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ],

where:

- *Cd* is the value of
  the **Discharge coefficient** parameter.
- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when
the pressure ratio, pout/pin, rises above the value of the **Laminar flow
pressure ratio** parameter,
*Blam*,

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the orifice becomes choked and the block uses the
equation

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2.

### Mass Balance

The block conserves mass through the valve

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where *ṁ* is the mass flow rate and the
subscript *w* denotes water vapor, the subscript
*g* denotes trace gas, and the subscript *d*
denotes water droplets.

### Energy Balance

Energy is conserved in the orifice,

ΦA+ΦB=0,

where:

- *ΦA* is the energy flow at
  port **A**.
- *ΦB* is the energy flow at
  port **B**.

### Assumptions and Limitations

- There is no heat exchange between the valve and the
  environment.
