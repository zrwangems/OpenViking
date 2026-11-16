---
type: simulink-block
title: 'Photodiode'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'photodiode'
documentation_source_path: 'ref/photodiode.html'
language: en
---

# Photodiode

## Ports

### Output

### **W** — Incident flux physical signal

Physical signal port associated with the incident flux.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the anode.

### **-** — Negative terminal electrical

Electrical conserving port associated with the cathode.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Sensitivity parameterization** — Sensitivity parameterization `Specify measured current for given flux density` (default) | `Specify current per unit flux density`

Select one of the following methods for sensitivity parameterization:

- `Specify measured current for given flux density` —
  Specify the measured current and the corresponding flux density. This is the default
  method.
- `Specify current per unit flux density` — Specify the
  device sensitivity directly.

### **Measured current** — Measured current `25` `uA` (default)

The current the block uses to calculate the device sensitivity.

#### Dependencies

This parameter is visible only when you select `Specify measured current
for given flux density` for the **Sensitivity
parameterization** parameter.

### **Flux density** — Flux density `5` `W/m^2` (default)

The flux density the block uses to calculate the device sensitivity.

#### Dependencies

This parameter is visible only when you select `Specify measured current
for given flux density` for the **Sensitivity
parameterization** parameter.

### **Device sensitivity** — Device sensitivity `5e-06` `m^2*A/W` (default)

The current per unit flux density.

#### Dependencies

This parameter is visible only when you select `Specify current per unit
flux density` for the **Sensitivity parameterization**
parameter.

### **Diode parameterization** — Diode parameterization `Use dark current plus a forward bias I-V data point` (default) | `Use dark current and N`

Select one of the following methods for diode model parameterization:

- `Use dark current plus a forward bias I-V data point`
  — Specify the dark current and a point on the diode I-V curve. This is the default
  method.
- `Use dark current and N` — Specify dark current and
  emission coefficient.

### **Current I1** — Current at the forward-biased point `0.1` `A` (default)

The current at the forward-biased point on the diode I-V curve that the block uses to
calculate *IS* and *N*.

#### Dependencies

This parameter is visible only when you select `Use dark current plus a
forward bias I-V data point` for the **Diode
parameterization** parameter.

### **Voltage V1** — Voltage at the forward-biased point `1.3` `V` (default)

The corresponding voltage at the forward-biased point on the diode I-V curve that the
block uses to calculate *IS* and *N*.

#### Dependencies

This parameter is visible only when you select `Use dark current plus a
forward bias I-V data point` for the **Diode
parameterization** parameter.

### **Dark current** — Dark current `5e-9` `A` (default)

The current through the diode when it is not exposed to light.

### **Emission coefficient, N** — Emission coefficient `3` (default)

The diode emission coefficient or ideality factor.

#### Dependencies

This parameter is visible only when you select `Use dark current and
N` for the **Diode parameterization** parameter.

### **Ohmic resistance, RS** — Series diode connection resistance `0.1` `Ohm` (default)

The series diode connection resistance.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

The temperature at which the I-V curve or dark current was measured.

### Junction Capacitance

### **Parameterization** — Junction capacitance parameterization `Fixed or zero junction capacitance` (default) | `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

Select one of the following options for modeling the junction capacitance:

- `Fixed or zero junction capacitance` — Model
  the junction capacitance as a fixed value.
- `Use C-V curve data points` — Specify
  measured data at three points on the diode C-V curve.
- `Use parameters CJ0, VJ, M & FC` —
  Specify zero-bias junction capacitance, junction potential, grading coefficient,
  and forward-bias depletion capacitance coefficient.

### **Junction capacitance** — Junction capacitance `60` `pF` (default)

Fixed value of the junction capacitance.

#### Dependencies

This parameter is visible only when you select `Fixed or zero
junction capacitance` for the **Parameterization**
parameter.

### **Zero-bias junction capacitance, CJ0** — Zero-bias junction capacitance `60` `pF` (default)

Value of the capacitance placed in parallel with the exponential diode term.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Parameterization**
parameter.

### **Reverse bias voltages [VR1 VR2 VR3]** — Reverse bias voltages `[ 0.1 10 100 ]` `V` (default)

A vector of the reverse bias voltage values at the three points on the diode C-V curve
that the block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` for the **Parameterization**
parameter.

### **Corresponding capacitances [C1 C2 C3]** — Corresponding capacitances `[ 45 3 6 ]` `pF` (default)

A vector of the capacitance values at the three points on the diode C-V curve that the
block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` for the **Parameterization**
parameter.

### **Junction potential, VJ** — Junction potential `1` `V` (default)

Junction potential.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Parameterization**
parameter.

### **Grading coefficient, M** — Grading coefficient `0.5` (default)

The grading coefficient.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Parameterization**
parameter.

### **Capacitance coefficient, FC** — Capacitance coefficient `0.5` (default)

Fitting coefficient that quantifies the decrease of the depletion capacitance with
applied voltage.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` or `Use parameters CJ0, VJ, M &
FC` for the **Parameterization** parameter.

### Temperature Dependence

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Use an I-V data point at second measurement temperature T2` | `Specify saturation current at second measurement temperature T2` | `Specify the energy gap EG`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter measurement temperature`
  — Temperature dependence is not modeled, or the model is simulated at the
  measurement temperature *T*m1 (as specified by the
  **Measurement temperature** parameter on the **Main**
  tab). This is the default method.
- `Use an I-V data point at second measurement temperature T2`
  — If you select this option, you specify a second measurement temperature
  *T*m2, and the current and voltage values at this
  temperature. The model uses these values, along with the parameter values at the first
  measurement temperature *T*m1, to calculate the
  energy gap value.
- `Specify saturation current at second measurement temperature
  T2` — If you select this option, you specify a second measurement
  temperature *T*m2, and saturation current value at
  this temperature. The model uses these values, along with the parameter values at the first
  measurement temperature *T*m1, to calculate the
  energy gap value.
- `Specify the energy gap EG` — Specify the energy gap
  value directly.

### **Current I1 at second measurement temperature** — Current I1 at second measurement temperature `0.07` `A` (default)

Specify the diode current *I1* value when the voltage is
*V1* at the second measurement temperature.

#### Dependencies

This parameter is visible only when you select `Use an I-V data point at
second measurement temperature T2` for the
**Parameterization** parameter.

### **Voltage V1 at second measurement temperature** — Voltage V1 at second measurement temperature `1.3` `V` (default)

Specify the diode voltage *V1* value when the current is
*I1* at the second measurement temperature.

#### Dependencies

This parameter is visible only when you select `Use an I-V data point at
second measurement temperature T2` for the
**Parameterization** parameter.

### **Saturation current, IS, at second measurement temperature** — Saturation current, IS, at second measurement temperature `2.5e-7` `A` (default)

Specify the saturation current *IS* value at the second measurement
temperature.

#### Dependencies

This parameter is visible only when you select `Specify saturation current
at second measurement temperature T2` for the
**Parameterization** parameter.

### **Second measurement temperature** — Second measurement temperature `125` `degC` (default)

Specify the value for the second measurement temperature.

#### Dependencies

This parameter is visible only when you select  `Use an I-V data point at
second measurement temperature T2` or `Specify saturation current
at second measurement temperature T2` for the
**Parameterization** parameter.

### **Energy gap parameterization** — Energy gap parameterization `Use nominal value for silicon (EG=1.11eV)` (default) | `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

Select a value for the energy gap from a list of predetermined options, or specify a
custom value:

- `Use nominal value for silicon (EG=1.11eV)` — This is
  the default.
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — If you select this option,
  the **Energy gap, EG** parameter appears in the dialog box, to let you
  specify a custom value for *EG*.

#### Dependencies

This parameter is visible only when you select `Specify the energy gap
EG` for the **Parameterization** parameter.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Specify a custom value for the energy gap, *EG*.

#### Dependencies

This parameter is visible only when you select `Specify a custom
value` for the **Energy gap parameterization**
parameter.

### **Saturation current temperature exponent parameterization** — Saturation current temperature exponent parameterization `Use nominal value for pn-junction diode (XTI=3)` (default) | `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

Select one of the following options to specify the saturation current temperature
exponent value:

- `Use nominal value for pn-junction diode (XTI=3)` —
  This is the default.
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — If you select this option,
  the **Saturation current temperature exponent, XTI** parameter appears in
  the dialog box, to let you specify a custom value for *XTI*.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Specify a custom value for the saturation current temperature exponent,
*XTI*.

#### Dependencies

This parameter is visible only when you select `Specify a custom
value` for the **Saturation current temperature exponent
parameterization** parameter.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default)

Specify the value for the temperature *T*s, at
which the device is to be simulated.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2024a: **Junction capacitance voltage** variable replaced with **Charge of junction capacitance** variable

If, in the **Capacitance** section, you set
**Parameterization** to `Use C-V curve data
points` or `Use parameters Cj0, VJ, M & FC`, you
now specify **Initial Targets** and **Nominal Values** for
capacitance and charge modeling using the **Charge of junction
capacitance** variable. The **Junction capacitance voltage**
variable is no longer enabled.

If a model you created in an earlier release uses these values for
**Parameterization** and specifies **Initial Targets**
or **Nominal Values** for the **Junction capacitance
voltage** variable, you must update the model. For more information on how to
calculate the charge of junction capacitance, see Description.

## Description

Photodiode with incident flux input port

The Photodiode block represents a photodiode as a controlled
current source and an exponential diode connected in parallel. The controlled current source
produces a current *Ip* that is proportional to the
radiant flux density:

|  |  |
| --- | --- |
| *Ip* = *DeviceSensitivity* · *RadiantFluxDensity* | **(1)** |

where:

- *DeviceSensitivity* is the ratio of the current produced to the incident
  radiant flux density.

  - If you select `Specify measured current for given flux
    density` for the **Sensitivity parameterization** parameter,
    the block calculates this variable by converting the **Measured current**
    parameter value to units of amps and dividing it by the **Flux density**
    parameter values.
  - If you select `Specify current per unit flux density` for the
    **Sensitivity parameterization** parameter, this variable is defined by
    the **Device sensitivity** parameter value.
- *RadiantFluxDensity* is the incident radiant flux density.

To model dynamic response time, use the **Parameterization** parameter in
the **Junction capacitance** tab to include the diode junction capacitance in
the model.

The exponential diode model provides the following relationship between the diode current
*I* and the diode voltage *V*:

I=IS⋅(eqVNkTm1−1)

where:

- *q* is the elementary charge on an electron (1.602176e–19
  Coulombs).
- *k* is the Boltzmann constant (1.3806503e–23 J/K).
- *N* is the emission coefficient.
- *IS* is the saturation current, which is equal to the **Dark
  current** parameter value.
- *Tm1* is the temperature at which the diode
  parameters are specified, as defined by the **Measurement temperature**
  parameter value.

When (*q**V* /
*N**k**Tm1*) >
80, the block replaces eqVNkTm1 with (*q**V* /
*N**k**Tm1* –
79)e80, which matches the gradient of the diode current at (*q**V* /
*N**k**Tm1*) =
80 and extrapolates linearly. When (*q**V* /
*N**k**Tm1*) <
–79, the block replaces eqVNkTm1 with (*q**V* /
*N**k**Tm1* +
80)e–79, which also matches the gradient and extrapolates linearly. Typical electrical
circuits do not reach these extreme values. The block provides this linear extrapolation to help
convergence when solving for the constraints during simulation.

When you select `Use dark current and N` for the **Diode
parameterization** parameter, you specify the diode in terms of the **Dark
current** and **Emission coefficient N** parameters. When you select
`Use dark current plus a forward bias I-V data point` for the
**Diode parameterization** parameter, you specify the **Dark
current** parameter and a voltage and current measurement point on the diode I-V curve.
The block calculates *N* from these values as follows:

N=VF/(Vtlog(IF/IS+1))

where:

- *VF* is the **Forward voltage
  VF** parameter value.
- *Vt* =
  *k**Tm1* /
  *q*.
- *IF* is the **Current IF at forward
  voltage VF** parameter value.

The exponential diode model provides the option to include a junction capacitance:

- When you select `Fixed or zero junction capacitance` for
  the **Parameterization** parameter, the capacitance is fixed.
- When you select `Use parameters CJO, VJ, M & FC` for
  the **Parameterization** parameter, the block uses the coefficients
  *CJO*, *VJ*, *M*, and
  *FC* to calculate a junction capacitance that depends on the junction
  voltage.
- When you select `Use C-V curve data points` for the
  **Parameterization** parameter, the block uses three capacitance
  values on the C-V capacitance curve to estimate *CJO*,
  *VJ*, and *M* and uses these values with the
  specified value of *FC* to calculate a junction capacitance that
  depends on the junction voltage. The block calculates *CJO*,
  *VJ*, and *M* as follows:

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  where:

  - *VR1*,
    *VR2*, and
    *VR3* are the values in the
    **Reverse bias voltages [VR1 VR2 VR3]** vector.
  - *C1*,
    *C2*, and
    *C3* are the values in the
    **Corresponding capacitances [C1 C2 C3]** vector.

  It is not possible to estimate *FC* reliably from
  tabulated data, so you must specify its value using the **Capacitance
  coefficient FC** parameter. In the absence of suitable data for this
  parameter, use a typical value of 0.5.

  The reverse bias voltages (defined as positive values) should satisfy
  *VR3* >
  *VR2* >
  *VR1*. This means that the capacitances should
  satisfy *C1* >
  *C2* >
  *C3* as reverse bias widens the depletion region and
  hence reduces capacitance. Violating these inequalities results in an error. Voltages
  *VR2* and
  *VR3* should be well away from the Junction potential
  *VJ*. Voltage *VR1* should be less
  than the Junction potential *VJ*, with a typical value for
  *VR1* being 0.1 V.

The voltage-dependent junction is defined in terms of the charge of junction capacitance
*Qj* as:

- For *V* <
  *FC*·*VJ*:

  Qj=CJ0⋅(VJ/(M−1))⋅((1−V/VJ)1−M−1)
- For *V* ≥
  *FC*·*VJ*:

  Qj=CJ0⋅F1+(CJ0/F2)⋅(F3⋅(V−FC⋅VJ)+0.5(M/VJ)⋅(V2−(FC⋅VJ)2))

where:

- F1=(VJ/(1−M))⋅(1−(1−FC)1−M))
- F2=(1−FC)1+M))
- F3=1−FC⋅(1+M)
- *V* is the junction capacitance voltage.

These equations are the same as used in [2], except that the temperature dependence of *VJ* and
*FC* is not modeled. This model does not include the diffusion
capacitance term that affects performance for high frequency switching applications.

The Photodiode block contains several options for modeling the dependence of
the diode current-voltage relationship on the temperature during simulation. Temperature
dependence of the junction capacitance is not modeled, this being a much smaller effect. For
details, see the Diode reference page.

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

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

**Note**

To satisfy all your initial targets, do not set the priority to `High` for more initial targets than the total number of differential variables in the block equations.

- If in the **Capacitance** section, you set
  **Parameterization** to `Fixed or zero junction
  capacitance` and **Junction capacitance** to
  `0`, the total number of differential variables in the
  block equations is zero. Do not set the priority of any variables in the
  **Initial Targets** section to
  `High`.
- If in the **Capacitance** section, you set
  **Parameterization** to `Fixed or zero junction
  capacitance` and you set the **Junction
  capacitance** parameter to a nonzero value, the total number of
  differential variables in the block equations is one. Set the priority to
  `High` for no more than one variable in the
  **Initial Targets** section.
- If in the **Capacitance** section, you set
  **Parameterization** to `Use C-V curve data
  points` or `Use parameters Cj0, VJ, M &
  FC`, the total number of differential variables in the block
  equations is one. Set the priority to `High` for no
  more than one variable in the **Initial Targets**
  section.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Plot Basic I-V Characteristics

You can plot the basic I-V characteristics of the Photodiode block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
Photodiode block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
