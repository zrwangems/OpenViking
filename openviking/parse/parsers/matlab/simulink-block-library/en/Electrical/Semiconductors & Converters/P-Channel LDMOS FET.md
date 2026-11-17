---
type: simulink-block
title: 'P-Channel LDMOS FET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pchannelldmosfet'
documentation_source_path: 'ref/pchannelldmosfet.html'
language: en
---

# P-Channel LDMOS FET

## Ports
```yaml
ports:
- name: G
  summary: Gate terminal electrical
  direction: conserving
- name: D
  summary: Drain terminal electrical
  direction: conserving
- name: S
  summary: Source terminal electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **G** — Gate terminal electrical

Electrical conserving port associated with the transistor gate
terminal.

### **D** — Drain terminal electrical

Electrical conserving port associated with the transistor drain
terminal.

### **S** — Source terminal electrical

Electrical conserving port associated with the transistor source
terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Gain, [channel drift_region]
  summary: Gain [11.6, .01] A/V2 (default)
  group: Main
- name: Flatband voltage, [channel drift_region]
  summary: Flatband voltage [-1.05, -0.1] V (default)
  group: Main
- name: Body factor, [channel drift_region]
  summary: Body factor [3.4, 2.5] V1/2 (default)
  group: Main
- name: Surface potential at strong inversion, [channel drift_region]
  summary: Surface potential at strong inversion [0.95, 0.95] V (default)
  group: Main
- name: Velocity saturation factor, [channel drift_region]
  summary: Velocity saturation factor [0.0, 0.1] 1/V (default)
  group: Main
- name: Drift region surface scattering factor
  summary: Drift region surface scattering factor 0 1/V (default)
  group: Main
- name: Channel-length modulation factor
  summary: Channel-length modulation factor 0 (default)
  group: Main
- name: Channel-length modulation voltage
  summary: Channel-length modulation voltage 5e-2 V (default)
  group: Main
- name: Linear-to-saturation transition coefficient
  summary: Linear-to-saturation transition coefficient 8 (default)
  group: Main
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Main
- name: Source ohmic resistance
  summary: Source ohmic resistance 1e-4 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Drain ohmic resistance
  summary: Drain ohmic resistance 0.07 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Gate ohmic resistance
  summary: Gate ohmic resistance 8.4 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Drift region low-bias resistance for gated region
  summary: Drift region low-bias resistance for gated region 0.1 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Drift region depletion layer thickness factor
  summary: Drift region depletion layer thickness factor 0.2 (default)
  group: Ohmic Resistance
- name: Oxide capacitance, [channel drift_region]
  summary: Oxide capacitance [1600.0, 1000.0] pF (default)
  group: Capacitances
- name: Gate-source overlap capacitance
  summary: Gate-source overlap capacitance 15 pF (default)
  group: Capacitances
- name: Gate-drain overlap capacitance
  summary: Gate-drain overlap capacitance 15 pF (default)
  group: Capacitances
- name: Reverse saturation current
  summary: Reverse saturation current 1e-13 A (default)
  group: Body Diode
- name: Built-in voltage
  summary: Built-in voltage 0.6 V (default)
  group: Body Diode
- name: Ideality factor
  summary: Ideality factor 1 (default)
  group: Body Diode
- name: Zero-bias junction capacitance
  summary: Zero-bias junction capacitance 1800 pF (default)
  group: Body Diode
- name: Transit time
  summary: Transit time 50 ns (default)
  group: Body Diode
- name: Parameterization
  summary: Temperature dependence parameterization None — Simulate at parameter measurement temperature (default) | Model
    temperature dependence
  group: Temperature Dependence
- name: Device simulation temperature
  summary: Device simulation temperature 25 degC (default)
  group: Temperature Dependence
- name: Gain temperature exponent, [channel drift_region]
  summary: Gain temperature exponent [1.3, 1.3] (default)
  group: Temperature Dependence
- name: Flatband voltage temperature coefficient, [channel drift_region]
  summary: Flatband voltage temperature coefficient [0.0005, 0.0005] V/K (default)
  group: Temperature Dependence
- name: Surface potential at strong inversion temperature coefficient
  summary: Surface potential at strong inversion temperature coefficient -8.5e-4 V/K (default)
  group: Temperature Dependence
- name: Velocity saturation temperature exponent, [channel drift_region]
  summary: Velocity saturation temperature exponent [1.04, 1.04] (default)
  group: Temperature Dependence
- name: Ohmic resistance temperature exponent
  summary: Ohmic resistance temperature exponent 0.95 (default)
  group: Temperature Dependence
- name: Drift region low-bias resistance temperature exponent for gated portion
  summary: Drift region low-bias resistance temperature exponent for gated portion 0.95 (default)
  group: Temperature Dependence
- name: Body diode reverse saturation current temperature exponent
  summary: Body diode reverse saturation current temperature exponent 3 (default)
  group: Temperature Dependence
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Gain, [channel drift\_region]** — Gain `[11.6, .01]` `A/V2` (default)

The gain, *β*, of the MOSFET regions. The parameter
value is a two-element vector, with the first element corresponding to
the channel, and the second — to the drift region. This parameter
primarily defines the linear region of operation on an
*ID*–*VDS*
characteristic. The values of both elements must be greater than
0.

### **Flatband voltage, [channel drift\_region]** — Flatband voltage `[-1.05, -0.1]` `V` (default)

The flatband voltage, *VFB*,
defines the gate bias that must be applied in order to achieve the
flatband condition at the surface of the silicon. The parameter value is
a two-element vector, with the first element corresponding to the
channel, and the second — to the drift region. You can also use
this parameter to arbitrarily shift the threshold voltage due to
material work function differences, and to trapped interface or oxide
charges. In practice, however, it is usually recommended to modify the
threshold voltage by using the **Body factor, [channel
drift\_region]** and **Surface potential at strong
inversion, [channel drift\_region]** parameters first, and
only use this parameter for fine-tuning.

The threshold voltage for the channel region, for a short-circuited
source-bulk connection, is approximately

−VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

where 2*ϕB* is the surface
potential at strong inversion and *γ* is the body
factor, both at the channel region.

### **Body factor, [channel drift\_region]** — Body factor `[3.4, 2.5]` `V1/2` (default)

Body factor, *γ*, in the surface-potential equation.
The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region.

For the channel region, the body factor is

γ=2qεSiNDCox

See the N-Channel MOSFET
block reference page for details on this equation. The drift region
equation is similar, except that
*ND* is replaced by the
doping density, *NA*. The
channel-region parameter value primarily impacts the threshold voltage.
For the drift region, this parameter primarily affects the charge model,
and also has a minor effect on the pinch-off behavior of the bulk
current through the drift region.

### **Surface potential at strong inversion, [channel drift\_region]** — Surface potential at strong inversion `[0.95, 0.95]` `V` (default)

The 2*ϕB* term in the
surface-potential equation. The parameter value is a two-element vector,
with the first element corresponding to the channel, and the second
— to the drift region.

The channel-region parameter value also primarily impacts the
threshold voltage. For the drift region, this parameter affects the
charge model only.

### **Velocity saturation factor, [channel drift\_region]** — Velocity saturation factor `[0.0, 0.1]` `1/V` (default)

Velocity saturation, *θsat*,
in the drain-current equation. Use this parameter in cases where a good
fit to linear operation leads to a saturation current that is too high.
By increasing this parameter value, you reduce the saturation current.
The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. The default value is `[0.0, 0.1]` 1/V, which
means that velocity saturation in the channel region is off by default.

### **Drift region surface scattering factor** — Drift region surface scattering factor `0` `1/V` (default)

Surface scattering factor,
*θsurf*, in the
drain-current equation. This parameter applies to the drift region only
and accounts for scattering in the accumulation layer due to the
vertical electric field.

### **Channel-length modulation factor** — Channel-length modulation factor `0` (default)

The factor, α, multiplying the logarithmic term in the
*GΔL* equation. See the
N-Channel MOSFET
block reference page for details on this equation. This parameter
describes the onset of channel-length modulation. For device
characteristics that exhibit a positive conductance in saturation,
increase the parameter value to fit this behavior. This parameter
applies to the channel region only. The default value is
`0`, which means that channel-length modulation is
off by default.

### **Channel-length modulation voltage** — Channel-length modulation voltage `5e-2` `V` (default)

The voltage *Vp* in the
*GΔL* equation. See the
N-Channel MOSFET
block reference page for details on this equation. This parameter
controls the drain-voltage at which channel-length modulation starts to
become active. This parameter applies to the channel region only.

### **Linear-to-saturation transition coefficient** — Linear-to-saturation transition coefficient `8` (default)

This parameter controls how smoothly the MOSFET transitions from
linear into saturation, particularly when velocity saturation is
enabled. This parameter can usually be left at its default value, but
you can use it to fine-tune the knee of the
*ID*–*VDS*
characteristic. This parameter applies both to the channel and drift
regions. The expected range for this parameter value is between 2 and
8.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

Temperature *Tm1* at which the
block parameters are measured. If the **Device simulation
temperature** parameter on the **Temperature
Dependence** tab differs from this value, then device
parameters will be scaled from their defined values according to the
simulation and reference temperatures. For more information, see Temperature Dependence.

### Ohmic Resistance

### **Source ohmic resistance** — Source ohmic resistance `1e-4` `Ohm` (default) | nonnegative scalar

The transistor source resistance, that is, the series resistance
associated with the source contact. The value must be greater than or
equal to `0`.

### **Drain ohmic resistance** — Drain ohmic resistance `0.07` `Ohm` (default) | nonnegative scalar

The transistor drain resistance, that is, the series resistance
associated with the drain contact and with the LOCOS part of the drift
region, which is not heavily impacted by the applied gate voltage. The
value must be greater than or equal to `0`.

### **Gate ohmic resistance** — Gate ohmic resistance `8.4` `Ohm` (default) | nonnegative scalar

The transistor gate resistance, that is, the series resistance
associated with the gate contact. The value must be greater than or
equal to `0`.

### **Drift region low-bias resistance for gated region** — Drift region low-bias resistance for gated region `0.1` `Ohm` (default) | nonnegative scalar

Resistance *RD* in the
drain-current equation. It represents the resistance of the bulk part of
the drift region in the absence of depletion from the top and bottom
interfaces. The value must be greater than or equal to
`0`.

### **Drift region depletion layer thickness factor** — Drift region depletion layer thickness factor `0.2` (default)

Parameter *λD* in the
drain-current equation. It is the ratio of vertical depths
*y1* and
*y2* at zero bias, where
*y1* represents the
space-charge region and *y2*
represents the undepleted part of the drift region. See the
N-Channel LDMOS FET
block reference page for an illustration.

### Capacitances

### **Oxide capacitance, [channel drift\_region]** — Oxide capacitance `[1600.0, 1000.0]` `pF` (default)

The parallel plate gate-channel and gate-drift-region capacitance. The
parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region.

### **Gate-source overlap capacitance** — Gate-source overlap capacitance `15` `pF` (default)

The fixed, linear capacitance associated with the overlap of the gate
electrode with the source well.

### **Gate-drain overlap capacitance** — Gate-drain overlap capacitance `15` `pF` (default)

The fixed, linear capacitance associated with the overlap of the gate
electrode with the drain well.

### Body Diode

### **Reverse saturation current** — Reverse saturation current `1e-13` `A` (default)

The current designated by the
*Is* symbol in the
body-diode equations.

### **Built-in voltage** — Built-in voltage `0.6` `V` (default)

The built-in voltage of the diode, designated by the
*Vbi* symbol in the
body-diode equations.

### **Ideality factor** — Ideality factor `1` (default)

The factor designated by the *n* symbol in the
body-diode equations.

### **Zero-bias junction capacitance** — Zero-bias junction capacitance `1800` `pF` (default)

The capacitance between the drain and bulk contacts at zero-bias due
to the body diode alone. It is designated by the
*Cj0* symbol in the
body-diode equations.

### **Transit time** — Transit time `50` `ns` (default)

The time designated by the *τ* symbol in the
body-diode equations.

### Temperature Dependence

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter
  measurement temperature` —
  Temperature dependence is not modeled. This is the default
  method.
- `Model temperature dependence`
  — Model temperature-dependent effects. Provide a
  value for the device simulation temperature,
  *Ts*, and
  the temperature-scaling coefficients for other block
  parameters.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default)

Temperature *Ts* at which the
device is simulated.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Gain temperature exponent, [channel drift\_region]** — Gain temperature exponent `[1.3, 1.3]` (default)

The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. Both in the channel and the drift region, the MOSFET gain,
*β*, is assumed to scale exponentially with
temperature, *β* =
*βm1*
(*Tm1*/*Ts*)^*ηβ*. *βm1* is the
value of the channel or drift region gain, as specified by the
**Gain, [channel drift\_region]** parameter from the
**Main** tab.
*ηβ* is the corresponding
element of the **Gain temperature exponent, [channel
drift\_region]** parameter.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Flatband voltage temperature coefficient, [channel drift\_region]** — Flatband voltage temperature coefficient `[0.0005, 0.0005]` `V/K` (default)

The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. The flatband voltage,
*VFB*, is assumed to scale
linearly with temperature, *VFB* =
*VFBm1* +
(*Ts* –
*Tm1*)*ST,VFB*. *VFBm1* is
the value of the channel or drift region flatband voltage, as specified
by the **Flatband voltage, [channel drift\_region]**
parameter from the **Main** tab.
*ST,VFB*
is the corresponding element of the **Flatband voltage
temperature coefficient, [channel drift\_region]**
parameter.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Surface potential at strong inversion temperature coefficient** — Surface potential at strong inversion temperature coefficient `-8.5e-4` `V/K` (default)

The surface potential at strong inversion,
2*ϕB*, is assumed to
scale linearly with temperature, *2ϕB* =
2*ϕBm1* +
(*Ts* –
*Tm1*)*ST,ϕB*. 2*ϕBm1* is
the value of the **Surface potential at strong
inversion** parameter from the **Main**
tab and
*ST,ϕB*
is the **Surface potential at strong inversion temperature
coefficient**.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Velocity saturation temperature exponent, [channel drift\_region]** — Velocity saturation temperature exponent `[1.04, 1.04]` (default)

The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. The velocity saturation,
*θsat*, is assumed to scale
exponentially with temperature, *θsat* =
*θsat,m1*
(*Tm1*/*Ts*)^*ηθ*. *θsat,m1* is
the value of the channel or drift region velocity saturation factor, as
specified by the **Velocity saturation factor, [channel
drift\_region]** parameter from the
**Main** tab.
*ηθ* is the corresponding
element of the **Velocity saturation temperature exponent,
[channel drift\_region]** parameter.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Ohmic resistance temperature exponent** — Ohmic resistance temperature exponent `0.95` (default)

The series resistances are assumed to correspond to semiconductor
resistances. Therefore, they decrease exponentially with increasing
temperature. *Ri* =
*Ri,m1*
(*Tm1*/*Ts*)^*ηR*, where *i* is S, D, or G, for the
source, drain, or gate series resistance, respectively.
*Ri,m1* is the value of
the corresponding series resistance parameter from the **Ohmic
Resistance** tab and
*ηR* is the **Ohmic
resistance temperature exponent**.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Drift region low-bias resistance temperature exponent for gated portion** — Drift region low-bias resistance temperature exponent for gated portion `0.95` (default)

Resistance *RD*, the low-bias
resistance of the bulk part of the drift region, scales similarly to the
other series resistances. A separate value of the temperature exponent
for this resistance provides an extra degree of freedom.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.

### **Body diode reverse saturation current temperature exponent** — Body diode reverse saturation current temperature exponent `3` (default)

The reverse saturation current for the body diode is assumed to be
proportional to the square of the intrinsic carrier concentration, *ni* =
*NC*
exp(–*EG*/2*kB**T*). *NC* is the
temperature-dependent effective density of states and
*EG* is the
temperature-dependent bandgap for the semiconductor material. To avoid
introducing another temperature-scaling parameter, the block neglects
the temperature dependence of the bandgap and uses the bandgap of
silicon at 300K (1.12eV) for all device types. Therefore, the
temperature-scaled reverse saturation current is given by

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* is the value of the
**Reverse saturation current** parameter from the
**Body Diode** tab,
*kB* is Boltzmann’s
constant (8.617x10-5eV/K), and
*ηIs* is the **Body
diode reverse saturation current temperature exponent**.
The default value is `3`, because
*NC* for silicon is
roughly proportional to T3/2. You can remedy
the effect of neglecting the temperature-dependence of the bandgap by a
pragmatic choice of
*ηIs*.

#### Dependencies

This parameter is visible only when you select `Model
temperature dependence` for the
**Parameterization** parameter.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2019b: Thermal network simlog paths

From R2019b forward, it is possible to model the thermal network of this block
either internally or externally.

As a result, the simlog paths corresponding to the thermal network have changed.
If you have a script that programmatically access the simlog, you have to manually
update it to reflect these changes.

## Description

P-Channel laterally-diffused metal-oxide-semiconductor or vertically-diffused metal-oxide-semiconductor transistors suitable for high voltage

The P-Channel LDMOS FET block models LDMOS (or VDMOS)
transistors suitable for high voltage. The model is based on surface potential and
includes effects due to an extended drain (drift) region:

- Nonlinear capacitive effects associated with the drift region
- Surface scattering and velocity saturation in the drift region
- Velocity saturation and channel-length modulation in the channel region
- Charge conservation inside the model, so you can use the model for charge
  sensitive simulations
- The intrinsic body diode
- Reverse recovery in the body diode model
- Temperature scaling of physical parameters
- For the option with exposed thermal port (see Thermal Port), dynamic self-heating

For information on physical background and defining equations, see the N-Channel LDMOS FET block reference page. Both the p-type and
n-type versions of the LDMOS model use the same underlying code with appropriate voltage
transformations, to account for the different device types.

The charge model is similar to that of the surface-potential-based MOSFET model, with
additional expressions to account for the charge in the drift region. The block uses the
derived equations as described in [1], which include both inversion and accumulation in the drift region.

### Modeling Body Diode

The block models the body diode as an ideal, exponential diode with both junction
and diffusion capacitances:

Idio=Is[exp(−VBDnϕT)−1]

Cj=Cj01+VBDVbi

Cdiff=τIsnϕTexp(−VBDnϕT)

where:

- *Idio* is the current through
  the diode.
- *Is* is the reverse saturation
  current.
- *VBD* is the body-drain
  voltage.
- *n* is the ideality factor.
- *ϕT* is the thermal
  voltage.
- *Cj* is the junction
  capacitance of the diode.
- *Cj0* is the zero-bias
  junction capacitance.
- *Vbi* is the built-in
  voltage.
- *Cdiff* is the diffusion
  capacitance of the diode.
- *τ* is the transit time.

The capacitances are defined through an explicit calculation of charges, which are
then differentiated to give the capacitive expressions above. The block computes the
capacitive diode currents as time derivatives of the relevant charges, similar to
the computation in the surface-potential-based MOSFET model.

### Modeling Temperature Dependence

The default behavior is that dependence on temperature is not modeled, and the
device is simulated at the temperature for which you provide block parameters. To
model the dependence on temperature during simulation, select `Model
temperature dependence` for the
**Parameterization** parameter on the **Temperature
Dependence** tab.

The model includes temperature effects on the capacitance characteristics, as well
as modeling the dependence of the transistor static behavior on temperature during
simulation.

The **Measurement temperature** parameter on the
**Main** tab specifies temperature
*Tm1* at which the other device
parameters have been extracted. The **Temperature Dependence** tab
provides the simulation temperature, *Ts*,
and the temperature-scaling coefficients for the other device parameters. For more
information, see Temperature Dependence.

### Thermal Port

You can expose the thermal port to model the effects of generated heat and device
temperature. To expose the thermal port, set the **Modeling option**
parameter to either:

- `No thermal port` — The block does not contain a
  thermal port and does not simulate heat generation in the device.
- `Show thermal port` — The block contains a thermal
  port that allows you to model the heat that conduction losses generate. For
  numerical efficiency, the thermal state does not affect the electrical behavior
  of the block.

For more information on using thermal ports and on the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

If you expose the thermal port, the block includes dynamic self-heating. This lets
you simulate the effect of self-heating on the electrical characteristics of the
device.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Plot Basic I-V Characteristics

You can plot the basic I-V characteristics of the P-Channel LDMOS FET block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
P-Channel LDMOS FET block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
