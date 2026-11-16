---
type: simulink-block
title: 'N-Channel LDMOS FET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'nchannelldmosfet'
documentation_source_path: 'ref/nchannelldmosfet.html'
language: en
---

# N-Channel LDMOS FET

## Ports

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

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Gain, [channel drift\_region]** — Gain `[11.6, .01]` `A/V` (default) | positive vector

The gain, *β*, of the MOSFET regions. The parameter
value is a two-element vector, with the first element corresponding to
the channel, and the second — to the drift region. This parameter
primarily defines the linear region of operation on an
*I*D–*VDS*
characteristic.

### **Flatband voltage, [channel drift\_region]** — Flatband voltage `[-1.05, -.1]` `V` (default)

The flatband voltage, *VFB*,
defines the gate bias that must be applied in order to achieve the
flatband condition at the surface of the silicon. The parameter value is
a two-element vector, with the first element corresponding to the
channel, and the second — to the drift region. The default value
is `[-1.05, -0.1]` V. You can also use this parameter
to arbitrarily shift the threshold voltage due to material work function
differences, and to trapped interface or oxide charges. In practice,
however, it is usually recommended to modify the threshold voltage by
using the **Body factor** and **Surface
potential at strong inversion** parameters first, and only
use this parameter for fine-tuning.

The threshold voltage for the channel region, for a short-circuited
source-bulk connection, is approximately

VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

where 2*ϕB* is the surface
potential at strong inversion and *γ* is the body
factor, both at the channel region.

### **Body factor, [channel drift\_region]** — Body factor `[3.4, 2.5]` `V1/2` (default)

Body factor, *γ*, in the surface-potential equation.
The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region.

For the channel region, the body factor is

γ=2qεSiNACox

See the N-Channel MOSFET
block reference page for details on this equation. The drift region
equation is similar, except that
*NA* is replaced by the
doping density, *N*D. The
channel-region parameter value primarily impacts the threshold voltage.
For the drift region, this parameter primarily affects the charge model,
and also has a minor effect on the pinch-off behavior of the bulk
current through the drift region.

### **Surface potential at strong inversion, [channel drift\_region]** — Surface potential at strong inversion `[.95, .95]` `V` (default)

The 2*ϕB* term in the
surface-potential equation. The parameter value is a two-element vector,
with the first element corresponding to the channel, and the second
— to the drift region.

The channel-region parameter value also primarily impacts the
threshold voltage. For the drift region, this parameter affects the
charge model only.

### **Velocity saturation factor, [channel drift\_region]** — Velocity saturation factor `[0, .1]` `1/V` (default)

Velocity saturation, *θ*sat,
in the drain-current equation. Use this parameter in cases where a good
fit to linear operation leads to a saturation current that is too high.
By increasing this parameter value, you reduce the saturation current.
The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. The default value is `[0.0, 0.1]` 1/V, which
means that velocity saturation in the channel region is off by default.

### **Drift region surface scattering factor** — Drift region surface scattering factor `0` `V` (default)

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
N-Channel MOSFET block
reference page for details on this equation. This parameter controls the
drain-voltage at which channel-length modulation starts to become
active. This parameter applies to the channel region only.

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
associated with the source contact.

### **Drain ohmic resistance** — Drain ohmic resistance `0.07` `Ohm` (default) | nonnegative scalar

The transistor drain resistance, that is, the series resistance
associated with the drain contact and with the LOCOS part of the drift
region, which is not heavily impacted by the applied gate
voltage.

### **Gate ohmic resistance** — Gate ohmic resistance `8.4` `Ohm` (default) | nonnegative scalar

The transistor gate resistance, that is, the series resistance
associated with the gate contact.

### **Drift region low-bias resistance for gated region** — Drift region low-bias resistance for gated region `0.1` `Ohm` (default) | nonnegative scalar

Resistance *RD* in the
drain-current equation. It represents the resistance of the bulk part of
the drift region in the absence of depletion from the top and bottom
interfaces.

### **Drift region depletion layer thickness factor** — Drift region depletion layer thickness factor `0.2` (default)

Parameter *λD* in the
drain-current equation. It is the ratio of vertical depths
*y1* and
*y2* at zero bias, where
*y1* represents the
space-charge region and *y2*
represents the undepleted part of the drift region.

### Capacitances

### **Oxide capacitance, [channel drift\_region]** — Oxide capacitance `[1600, 1000]` `pF` (default)

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

### **Transit time** — Transit time `50e-9` `s` (default)

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
device is simulated

### **Gain temperature exponent, [channel drift\_region]** — Gain temperature exponent `[1.3, 1.3]` (default)

The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. Both in the channel and the drift region, the MOSFET gain,
*β*, is assumed to scale exponentially with
temperature, *β* =
*βm1*
(*Tm1*/*T*s)^*ηβ*. *βm1* is the
value of the channel or drift region gain, as specified by the
**Gain, [channel drift\_region]** parameter from the
**Main** tab.
*η*β is the corresponding
element of the **Gain temperature exponent, [channel
drift\_region]** parameter.

### **Flatband voltage temperature coefficient, [channel drift\_region]** — Flatband voltage temperature coefficient `[.0005, .0005]` `V/K` (default)

The parameter value is a two-element vector, with the first element
corresponding to the channel, and the second — to the drift
region. The flatband voltage,
*V*FB, is assumed to scale
linearly with temperature, *V*FB =
*V*
FBm1 +
(*Ts* –
*Tm1*)*S*T,VFB. *VFBm1* is
the value of the channel or drift region flatband voltage, as specified
by the **Flatband voltage, [channel drift\_region]**
parameter from the **Main** tab.
*ST,VFB*
is the corresponding element of the **Flatband voltage
temperature coefficient, [channel drift\_region]**
parameter.

### **Surface potential at strong inversion temperature coefficient** — Surface potential `-8.5e-4` `V/K` (default)

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
*η*θ is the corresponding
element of the **Velocity saturation temperature exponent,
[channel drift\_region]** parameter.

### **Ohmic resistance temperature exponent** — Ohmic resistance temperature exponent `0.95` (default)

The series resistances are assumed to correspond to semiconductor
resistances. Therefore, they decrease exponentially with increasing
temperature. *Ri* =
*Ri,m1*
(*T*/*T*s)^*ηR*, where *i* is
*Sm1*,
*D*, or *G*, for the source,
drain, or gate series resistance, respectively.
*Ri,m1* is the value of
the corresponding series resistance parameter from the **Ohmic
Resistance** tab and
*ηR* is the **Ohmic
resistance temperature exponent**.

### **Drift region low-bias resistance temperature exponent for gated portion** — Drift region low-bias resistance temperature exponent for gated portion `0.95` (default)

Resistance *R*D, the low-bias
resistance of the bulk part of the drift region, scales similarly to the
other series resistances. A separate value of the temperature exponent
for this resistance provides an extra degree of freedom.

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
roughly proportional to
*T3/2*. You can remedy
the effect of neglecting the temperature-dependence of the bandgap by a
pragmatic choice of
*ηIs*.

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

N-Channel laterally-diffused metal-oxide-semiconductor or vertically-diffused metal-oxide-semiconductor transistors suitable for high voltage

The N-Channel LDMOS FET block models LDMOS (or VDMOS)
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
- For the option with exposed thermal ports (see Thermal Port), dynamic self-heating

This figure shows the physical structure of the model:

The channel region is in the p+ region, from the heavily n-doped source well to the
end of the p+ region. The drift region is a lightly doped drain extension. Further down,
there is a p-type epi-layer, and then the entire structure is on a heavily p-doped
substrate. The gate oxide is thin over the entire channel region and over part of the
drift region. Further into the drift region, the gate oxide has a greater thickness in
the local-oxidation-of-silicon (LOCOS) region.

This figure shows the equivalent circuit of the model.

The modeling approach is similar to [1]. The overlaps of the gate contact with the source and drain n-wells are modeled as
lumped linear capacitances. The channel (p+) region is modeled using the
surface-potential-based MOSFET model. The pn-junction between the source/bulk and drain
is modeled using an ideal diode, including both junction and diffusion capacitances. The
drift region underneath the thin gate oxide is modeled according to a surface-potential
formulation, which includes:

- The current due to the accumulation layer at the semiconductor-oxide
  interface
- The current due to the electrons flowing towards the drain deeper inside the
  drift region

The space-charge region between the epi-layer and the drift region is represented
using a pinching effect on the current flowing through the bulk of the drift region. The
LOCOS part of the drift region is modeled as a lumped, series resistor, and there are
also series resistances added to the source and gate contacts.

For detailed description of the channel model, see the surface-potential-based model
of the N-Channel MOSFET block. The drift region
model is similarly derived from the surface potential using the Poisson equation. For an
n-type semiconductor under the gradual-channel approximation, the defining equations
are:

∂2ψ∂y2≈qNDεSi[−1−exp(−ψ−2ϕBϕT)+exp(ψ−VCBϕT)]

ϕT=kBTq

where:

- *ψ* is the electrostatic potential.
- *q* is the magnitude of the electronic charge.
- *ND* is the doping density of the
  drift region.
- *ɛSi* is the dielectric
  permittivity of the semiconductor material (for example, silicon).
- *ϕB* is the difference between the
  intrinsic Fermi level and the Fermi level deep in the drift region.
- *VCB* is the quasi-Fermi potential
  of the drift region referenced to the bulk.
- *ϕT* is the thermal
  voltage.
- *kB* is Boltzmann’s
  constant.
- *T* is temperature.

Neglect the inversion for the DC current model to obtain this current
expression,

ID=11+θsatVDK[flinRDVDK+β2⋅VGK2−VGD21+θsurf2(VGK+VGD)]

where:

- *ID* is the drain current.
- *θsat* is the velocity
  saturation.
- *Vij* is the voltage difference
  between nodes *i* and *j*, where
  subscripts D and K refer to the drain and to the junction of the channel and
  drift regions, respectively, and subscript G refers to the gate with a
  correction due to the flatband voltage being applied.
- *flin*/*RD*
  represents the conductance of the bulk of the drift region, including the
  effect of pinching due to depletion from the epi-drift interface.
- *β* is the gain of the accumulation layer at the
  interface between the drift region and the thin gate oxide.
- *θsurf* is the parameter that
  accounts for scattering in the accumulation layer due to the vertical
  electric field.

This equation describes the pinching off of the bulk part of the drift region,

flin=1−λDVbi+VSB−VbiVbi

where:

- *λD* is the parameter representing
  the n-side vertical depth of the space-charge region along the epi-drift
  interface at zero bias divided by the vertical depth of the undepleted part
  of the drift region at zero bias.

  In the figure, the top solid line is the semiconductor surface. The lower
  solid line is the junction between the drift region and the epi layer. The
  dashed lines show the extent of the space-charge region around the drift-epi
  interface. *λD* is
  *y1*/*y2*
  at zero bias.
- *Vbi* is the built-in voltage for
  the epi-drift diode.
- *VSB* is the source-body voltage,
  used as an approximation to the bias applied across the epi-drift diode.
  Using this voltage instead of *VKB*
  is more numerically stable, and is justified because most of the
  drain-source voltage drops across the drift region in the transistor
  on-state.

The charge model is similar to that of the surface-potential-based MOSFET model, with
additional expressions to account for the charge in the drift region. The block uses the
derived equations as described in [1], which include both inversion and accumulation in the drift region.

### Modeling Body Diode

The block models the body diode as an ideal, exponential diode with both junction
and diffusion capacitances:

Idio=Is[exp(−VDBnϕT)−1]

Cj=Cj01+VDBVbi

Cdiff=τIsnϕTexp(−VDBnϕT)

where:

- *Idio* is the current through
  the diode.
- *Is* is the reverse saturation
  current.
- *VDB* is the drain-body
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
parameters have been extracted. The **Temperature Dependence**
parameters provides the simulation temperature,
*Ts*, and the temperature-scaling
coefficients for the other device parameters. For more information, see Temperature Dependence.

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

The thermal option of this block includes dynamic self-heating. This lets you
simulate the effect of self-heating on the electrical characteristics of the
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

You can plot the basic I-V characteristics of the N-Channel LDMOS FET block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
N-Channel LDMOS FET block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
