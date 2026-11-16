---
type: simulink-block
title: 'Diode'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: en
---

# Diode

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the anode.

### **-** — Negative terminal electrical

Electrical conserving port associated with the cathode.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### Main

### **Fidelity level** — Level of fidelity `Include capacitance and charge dynamics` (default) | `Ideal switching`

Level of detail of the dynamics model of the diode. If you select `Ideal
switching`, the block only models the reverse recovery losses. If you select
`Include capacitance and charge dynamics`, the block models both
junction capacitance and charge dynamics.

#### Dependencies

To enable this parameter, set **Modeling option** to `Show
thermal port`.

### **Diode model** — Diode model `Piecewise Linear` (default) | `Exponential` | `Tabulated I-V curve`

Select one of these diode models:

- `Piecewise Linear` — Use a piecewise linear model for
  the diode, as described in Piecewise Linear Diode. This is the default method.
- `Exponential` — Use a standard exponential model for
  the diode, as described in Exponential Diode.
- `Tabulated I-V curve` — Use tabulated forward bias
  I-V data plus fixed reverse bias off conductance, as described in Tabulated Diode.

### **Table type** — Tabulated function `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

Whether to tabulate the current as a function of temperature and voltage or the voltage
as a function of temperature and current.

#### Dependencies

To enable this parameter, set **Diode model** to
`Tabulated I-V curve`.

### **Forward voltage** — Forward voltage `0.6` `V` (default)

Minimum voltage that needs to be applied for the diode to become forward-biased.

#### Dependencies

To enable this parameter, set **Diode model** to
`Piecewise linear`.

### **On resistance** — On resistance `0.3` `Ohm` (default)

Resistance of the diode when it is forward biased.

#### Dependencies

To enable this parameter, set **Diode model** to
`Piecewise linear`.

### **Off conductance** — Off conductance `1e-8` `1/Ohm` (default)

Conductance of the diode when it is reverse biased. The block uses this value to
determine the reverse I-V characteristics when the **Model Zener diode**
parameter is cleared.

#### Dependencies

To enable this parameter, set **Diode model** to
`Piecewise linear` or `Tabulated I-V
curve`.

### **Parameterization** — Model parameterization `Use two I-V curve data points` (default) | `Use parameters IS and N` | `Use an I-V data point and IS` | `Use an I-V data point and N`

Select one of the following methods for model parameterization:

- `Use two I-V curve data points` — Specify measured
  data at two points on the diode I-V curve. This is the default method.
- `Use parameters IS and N` — Specify saturation current
  and emission coefficient.
- `Use an I-V data point and IS` — Specify measured data
  at a single point on the diode I-V curve in combination with the saturation current.
- `Use an I-V data point and N` — Specify measured data
  at a single point on the diode I-V curve in combination with the emission
  coefficient.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential`.

### **Currents [I1 I2]** — Vector of current values at two points `[.0137, .545]` `A` (default)

Vector of the current values at the two points on the diode I-V curve that the block
uses to calculate *IS* and *N*.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use two I-V curve data points`.

### **Voltages [V1 V2]** — Vector of voltage values at two points `[.6, .7]` `V` (default)

Vector of the voltage values at the two points on the diode I-V curve that the block
uses to calculate *IS* and *N*.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use two I-V curve data points`.

### **Saturation current, IS** — Saturation current `1e-12` `A` (default)

Magnitude of the current that the ideal diode equation approaches asymptotically for
very large reverse bias levels.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use parameters IS and N` or `Use an I-V data point
and IS`.

### **Emission coefficient, N** — Diode emission coefficient `1` (default)

Diode emission coefficient or ideality factor.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use parameters IS and N` or `Use an I-V data point
and N`.

### **Current I1** — Current value `0.0137` `A` (default)

Current value at the point on the diode I-V curve that the block uses for calculations.
Depending on the **Parameterization** value, the block uses this parameter
to calculate either *N* or *IS*.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use an I-V data point and IS` or `Use an I-V data
point and N`.

### **Voltage V1** — Voltage value `0.6` `V` (default)

Voltage value at the point on the diode I-V curve that the block uses for
calculations.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential` and **Parameterization** to
`Use an I-V data point and IS` or `Use an I-V data
point and N`.

### **Ohmic resistance, RS** — Ohmic resistance `0` `Ohm` (default)

Series diode connection resistance.

#### Dependencies

To enable this parameter, set **Diode model** to
`Exponential`.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

Temperature *Tm1* at which IS or the I-V curve
was measured.

### **Forward currents, If(Tj,Vf)** — Vector of forward currents `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default) | nonnegative vector

Forward currents. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional (*If(Tj,Vf)* = 0A).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
If(Tj,Vf) form`.

### **Forward voltages, Vf(Tj,If)** — Vector of forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default) | nonnegative vector

Forward voltages. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional (*Vf(Tj,If)* = 0V).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
Vf(Tj,If) form`.

### **Junction temperatures, Tj** — Vector of junction temperatures `[25, 125]` `degC` (default)

Vector of junction temperatures.

If the size of the vector is equal to `1`, the diode characteristics
does not depend on the temperature.

#### Dependencies

To enable this parameter, set **Diode model** to
`Tabulated I-V curve`.

### **Forward voltages, Vf** — Vector of forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

Vector of forward voltages. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional (*Vf* =
0V).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
If(Tj,Vf) form`.

### **Forward currents, If** — Vector of forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

Vector of forward currents. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional (*If* =
0A).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
Vf(Tj,If) form`.

### **Reverse currents, Ir(Tj,Vr)** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A` (default) | nonnegative vector

*Since R2024a*

Reverse currents. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional (*Ir(Tj,Vr)* = 0A).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
If(Tj,Vf) form` and select the **Model Zener diode**
parameter.

### **Reverse voltages, Vr** — Vector of reverse voltages `[10, 20, 40, 50, 70, 80, 100]` `V` (default)

*Since R2024a*

Vector of reverse voltages. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional (*Vr* =
0V).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
If(Tj,Vf) form` and select the **Model Zener diode**
parameter.

### **Reverse voltages, Vr(Tj,Ir)** — Vector of reverse voltages `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V` (default) | nonnegative vector

*Since R2024a*

Reverse voltages. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional (*Vr(Tj,Ir)* = 0V).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
Vf(Tj,If) form` and select the **Model Zener diode**
parameter.

### **Reverse currents, Ir** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A` (default)

*Since R2024a*

Vector of reverse currents. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional (*Ir* =
0A).

#### Dependencies

To enable this parameter, set **Table type** to `Table in
Vf(Tj,If) form` and select the **Model Zener diode**
parameter.

### **Number of series diodes** — Number of diodes connected in series `1` (default)

Number of diodes connected in series between the **+** and
**–** block ports. Multiple diodes are not modeled. Rather, each diode has
all voltage-related quantities scaled by the factor that you specify.

### **Number of parallel diodes** — Number of parallel diodes `1` (default)

Number of parallel diodes, or number of parallel paths formed by series-connected
diodes, between the **+** and **–** block ports. Multiple
diodes are not modeled. Rather, each diode has all current-related quantities scaled by the
factor that you specify.

### **Model Zener diode** — Option to model a Zener diode `Off` (default) | `On`

*Since R2023b*

Option to model a Zener diode.

Select this parameter to model a Zener diode that conducts in the forward and reverse
biased directions. The block icon shows the electronic symbol for a Zener diode and you
enable the parameters in the **Breakdown** tab. You must specify a finite
value for the **Reverse breakdown voltage** parameter.

When you select this option, you can model the
reverse I-V characteristics for the Diode block by specifying the new **Reverse
voltages, Vr(Tj,Ir)**, **Reverse currents, Ir(Tj,Vr)**,
**Reverse voltages, Vr** and **Reverse currents, Ir**
parameters. *(since R2024a)*

Clear this parameter to model a standard diode that conducts in a single direction only.
The block assumes that the reverse breakdown voltage is infinite, which effectively omits
reverse breakdown from the model. The block icon shows the electronic symbol for a standard
diode.

### Breakdown

To enable these parameters, select the **Model Zener diode**
parameter.

### **Zener resistance** — Zener resistance `0.3` `Ohm` (default) | positive scalar

Resistance of the diode when the voltage is less than the **Reverse breakdown
voltage** value.

#### Dependencies

To enable this parameter, set **Diode model** to
`Piecewise linear`.

### **Reverse breakdown voltage** — Reverse breakdown voltage `inf` `V` (default) | positive scalar

Reverse voltage below which to model the rapid increase in conductance that occurs at
diode breakdown.

#### Dependencies

To enable this parameter, set **Diode model** to
`Piecewise linear` or
`Exponential`.

### Capacitance

To enable these parameters, set **Modeling option** to `No
thermal port` or **Fidelity level** to `Include
capacitance and charge dynamics`.

### **Parameterization** — Modeling junction capacitance `Fixed or zero junction capacitance` (default) | `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

Method for modeling the junction capacitance:

- `Fixed or zero junction capacitance` — Model the
  junction capacitance as a fixed value.
- `Use C-V curve data points` — Specify measured data
  at three points on the diode C-V curve.
- `Use parameters CJ0, VJ, M & FC` — Specify
  zero-bias junction capacitance, junction potential, grading coefficient, and forward-bias
  depletion capacitance coefficient.

### **Junction capacitance** — Junction capacitance `0` `pF` (default)

Fixed junction capacitance value.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Fixed or zero junction capacitance`.

### **Reverse bias voltages [VR1 VR2 VR3]** — Vector of reverse bias voltage values `[.1, 10, 100]` `V` (default)

Vector of the reverse bias voltage values at the three points on the diode C-V curve
that the block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
C-V curve data points`.

### **Corresponding capacitances [C1 C2 C3]** — Vector of capacitance values `[3.5, 1, .4]` `pF` (default)

Vector of the capacitance values at the three points on the diode C-V curve that the
block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
C-V curve data points`.

### **Zero-bias junction capacitance, CJ0** — Zero-bias junction capacitance `5` `pF` (default)

Value of the capacitance placed in parallel with the conduction current term.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
parameters CJ0, VJ, M & FC`.

### **Junction potential, VJ** — Junction potential `1` `V` (default)

The junction potential.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
parameters CJ0, VJ, M & FC`.

### **Grading coefficient, M** — Grading coefficient `0.5` (default)

Grading coefficient.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
parameters CJ0, VJ, M & FC`.

### **Capacitance coefficient, FC** — Capacitance coefficient `0.5` (default)

Fitting coefficient that quantifies the decrease of the depletion capacitance with
applied voltage.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
parameters CJ0, VJ, M & FC`.

### **Charge dynamics** — Charge dynamics parameterization `Do not model charge dynamics` (default) | `Use peak reverse current and stretch factor` | `Use peak reverse current and reverse recovery time` | `Use peak reverse current and reverse recovery charge` | `Use peak reverse current and reverse recovery energy` | `Use transit time and carrier lifetime`

Select one of the following methods for charge dynamics parameterization:

- `Do not model charge dynamics` — Do not include charge
  dynamics modeling. This is the default method.
- `Use peak reverse current and stretch factor` — Model
  charge dynamics by providing values for peak reverse current
  *iRM* and stretch factor *λ*
  plus information on the initial forward current and rate of change of current used in the
  test circuit when measuring *iRM* and
  *trr*.
- `Use peak reverse current and reverse recovery time` —
  Model charge dynamics by providing values for peak reverse current
  *iRM* and reverse recovery time
  *trr* plus information on the initial forward
  current and rate of change of current used in the test circuit when measuring
  *iRM* and
  *trr*. Use this option if the manufacturer
  datasheet does not provide values for transit time *TT* and carrier
  lifetime *τ*.
- `Use peak reverse current and reverse recovery charge`
  — Model charge dynamics by providing values for peak reverse current
  *iRM* and reverse recovery charge
  *Qrr* plus information on the initial forward current and rate of change
  of current used in the test circuit when measuring
  *iRM* and
  *trr*.
- `Use peak reverse current and reverse recovery energy`
  — Model charge dynamics by providing values for peak reverse current
  *iRM* and reverse recovery energy
  *Erec* plus information on the initial forward current and rate of change
  of current used in the test circuit when measuring
  *iRM*.
- `Use transit time and carrier lifetime` — Model charge
  dynamics by providing values for transit time *TT* and carrier lifetime
  *τ*.

### **Peak reverse current, iRM** — Peak reverse current `-7.15` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit. This value must be less than
zero.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and stretch factor`, `Use peak reverse
current and reverse recovery time`, `Use peak reverse current and
reverse recovery charge`, or `Use peak reverse current and reverse
recovery energy`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `4` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current. This value must be greater
than zero.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and stretch factor`, `Use peak reverse
current and reverse recovery time`, `Use peak reverse current and
reverse recovery charge`, or `Use peak reverse current and reverse
recovery energy`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-750` `A/μs` (default) | negative scalar

Rate of change of current when measuring peak reverse current. This value must be less
than zero.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and stretch factor`, `Use peak reverse
current and reverse recovery time`, `Use peak reverse current and
reverse recovery charge`, or `Use peak reverse current and reverse
recovery energy`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default)

Value that the block uses to calculate **Reverse recovery time, trr**.
This value must be greater than `1`. The default value is
`3`.

Specifying the stretch factor is an easier way to parameterize the reverse recovery time
than specifying the reverse recovery charge. The larger the value of the stretch factor, the
longer it takes for the reverse recovery current to dissipate.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and stretch factor`.

### **Reverse recovery time, trr** — Reverse recovery time `115` (default)

Time between the point where the current initially goes to zero when the diode turns
off, and the point where the current falls to less than ten percent of the peak reverse
current. The default value is `115`
`ns`.

The value of the **Reverse recovery time, trr** parameter must be
greater than the value of the **Peak reverse current, iRM** parameter
divided by the value of the **Rate of change of current when measuring iRM**
parameter.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and reverse recovery time`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `s*μA` (default)

Value that the block uses to calculate **Reverse recovery time, trr**.
Use this parameter if the data sheet for your diode device specifies a value for the reverse
recovery charge instead of a value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to dissipate when the
diode turns off. The value must be less than −i2RM2a,

where:

- *iRM* is the value specified for
  **Peak reverse current, iRM**.
- *a* is the value specified for **Rate of change of current when
  measuring iRM**.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and reverse recovery charge`.

### **Diode turn-off voltage when measuring Erec** — Diode turn-off voltage when measuring Erec `-600` `V` (default)

Voltage between the diode in steady-state.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and reverse recovery energy`.

### **Stray inductance when measuring Erec** — Stray inductance when measuring Erec `150` `nH` (default)

Total unintended inductance in the measurement circuit. The block uses this value to
calculate **Reverse recovery energy, Erec**.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and reverse recovery energy`.

### **Reverse recovery energy, Erec** — Reverse recovery energy `0.03` `J` (default)

Total switching losses due to the diode reverse recovery.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
peak reverse current and reverse recovery energy`.

### **Transit time, TT** — Transit time `50` `ns` (default)

Measure of how long it takes carriers to cross the diode junction.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
transit time and carrier lifetime`.

### **Carrier lifetime, tau** — Carrier lifetime `100` `ns` (default)

Measure of how long it takes for the carriers to dissipate once the diode is no longer
conducting. The default value is `100`
`ns`.

#### Dependencies

To enable this parameter, set **Charge dynamics** to `Use
transit time and carrier lifetime`.

### Reverse Recovery Loss

To enable these parameters, set **Modeling option** to `Show
thermal port` and **Fidelity level** to `Ideal
switching`.

### **Reverse recovery loss model** — Model for reverse recovery loss `Fixed loss` (default) | `Tabulated loss`

Whether to model fixed or tabulated reverse recovery losses.

### **Reverse recovery loss** — Reverse recovery loss `0` `J` (default) | nonnegative scalar

Dissipated energy in each turn-off event, regardless of the state of the diode before or
after the switching event.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Fixed loss`.

### **Scale reverse recovery loss with current and voltage** — Option to scale reverse recovery loss `On` (default) | `Off`

*Since R2023b*

Option to scale reverse recovery loss with current and voltage.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Fixed loss`.

### **Forward current when measuring recovery loss, Irec** — Forward current when block measures recovery loss `10` `A` (default) | positive scalar

*Since R2023b*

Forward current through the diode before the reverse recovery event that the block
uses to measure recovery loss.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Fixed loss` and select the **Scale reverse
recovery loss with current and voltage** parameter.

### **Turn-off voltage when measuring recovery loss, Vrec** — Turn-off voltage when measuring recovery loss `10` `V` (default) | positive scalar

Voltage across the diode after the reverse recovery event used to measure recovery
loss.

#### Dependencies

To enable this parameter, choose from one of these options:

- Set **Reverse recovery loss model** to `Fixed
  loss` and select the **Scale reverse recovery loss with current and
  voltage** parameter.
- Set the **Reverse recovery loss model** parameter to
  `Tabulated loss`.

### **Filter time constant for voltage and current values** — Filter time constant for voltage and current values `1 / 1000 / 100` `s` (default) | positive scalar

Filter time constant for the voltage and current values that the block uses to calculate
reverse recovery loss. Set this parameter to a value that is lower than the fastest switching
period.

#### Dependencies

To enable this parameter, choose from one of these options:

- Set **Reverse recovery loss model** to `Fixed
  loss` and select the **Scale reverse recovery loss with current and
  voltage** parameter.
- Set the **Reverse recovery loss model** parameter to
  `Tabulated loss`.

### **Reverse recovery loss table, Erec(Tj, If)** — Reverse recovery loss `zeros(2, 3)` `J` (default) | vector of nonnegative scalars

Dissipated energy as a function of the forward current *If* just before
the switching event, and final off-state voltage once the diode is in off state.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Tabulated loss`.

### **Temperature vector for recovery loss table, Tj** — Temperature vector for recovery loss table `[298.15, 398.15]` `K` (default) | vector

Temperature vector that the block uses to tabulate the reverse recovery loss.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Tabulated loss`.

### **Forward current vector for recovery loss table, If** — Forward current vector for recovery loss table `[.1, 1, 10]` `A` (default) | vector of nonnegative scalars

Forward current vector that the block uses to tabulate reverse recovery loss.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Tabulated loss`.

### Temperature Dependence

This section is applicable to `Exponential` and
`Tabulated I-V curve` diode models only.

This table shows how the visibility of **Temperature Dependence** setting
depends on how you configure the **Diode model** parameter in the
**Main** setting and whether you expose the thermal port. To learn how to read
this table, see Parameter Dependencies

**Visibility of the Temperature Dependence Setting**

| Parameters, options, and visibility of the setting | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Diode model** | | | | | | | |
| *`Piecewise linear`* | | | | *`Exponential`* | | *`Tabulated I-V curve`* | |
| **Thermal Port** | | | | **Thermal Port** | | **Thermal Port** | |
| *`Not exposed`* | *`Exposed`* | | | *`Not exposed`* | *`Exposed`* | *`Not exposed`* | *`Exposed`* |
| Hidden | Hidden | | | Visible | Visible | Visible | Hidden |

### **Parameterization** — Temperature dependence parameterization `None - Use characteristics at parameter measurement temperature` (default) | `Use an I-V data point at second measurement temperature` | `Specify saturation current at second measurement temperature` | `Specify the energy gap EG`

Select one of the following methods for temperature dependence parameterization:

- `None - Use characteristics at parameter measurement
  temperature` — Temperature dependence is not modeled, or the model is
  simulated at the measurement temperature *T*m1 (as
  specified by the **Measurement temperature** parameter on the
  **Main** tab). This is the default method.
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

### **Current I1 at second measurement temperature** — Current I1 at second measurement temperature `0.0245` `A` (default)

Specify the diode current *I1* value when the voltage is
*V1* at the second measurement temperature.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
an I-V data point at second measurement temperature`.

### **Voltage V1 at second measurement temperature** — Voltage V1 at second measurement temperature `0.5` `V` (default)

Specify the diode voltage *V1* value when the current is
*I1* at the second measurement temperature.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
an I-V data point at second measurement temperature`.

### **Saturation current, IS, at second measurement temperature** — Saturation current, IS, at second measurement temperature `1.25e-7` `A` (default)

Specify the saturation current *IS* value at the second measurement
temperature.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify saturation current at second measurement
temperature`.

### **Second measurement temperature** — Second measurement temperature `125` `°C` (default)

Specify the value for the second measurement temperature.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use an I-V data point at second measurement temperature` or
`Specify saturation current at second measurement
temperature`.

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

To enable this parameter, set **Parameterization** to
`Specify the energy gap EG`.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Specify a custom value for the energy gap, *EG*.

#### Dependencies

To enable this parameter, set **Energy gap parameterization** to
`Specify a custom value`.

### **Saturation current temperature exponent parameterization** — Saturation current temperature exponent parameterization `Use nominal value for pn-junction diode (XTI=3)` (default) | `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

Select one of the following options to specify the saturation current temperature
exponent value:

- `Use nominal value for pn-junction diode (XTI=3)` —
  This is the default.
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — If you select this option,
  the **Saturation current temperature exponent, XTI** parameter appears in
  the dialog box, to let you specify a custom value for *XTI*.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
an I-V data point at second measurement temperature`, `Specify
saturation current at second measurement temperature`, or `Specify
the energy gap, EG`.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Specify a custom value for the saturation current temperature exponent,
*XTI*.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
an I-V data point at second measurement temperature`, `Specify
saturation current at second measurement temperature`, or `Specify
the energy gap, EG` and **Saturation current temperature exponent
parameterization** to `Specify a custom value`.

### **Reverse breakdown voltage temperature coefficient, dBV/dT** — Reverse breakdown voltage temperature coefficient `0` `V/K` (default)

Modulate the reverse breakdown voltage *BV*. If you define the reverse
breakdown voltage *BV* as a positive quantity, a positive value for
*TCV* implies that the magnitude of the reverse breakdown voltage decreases
with temperature.

#### Dependencies

To enable this parameter, select the **Model Zener diode** parameter
and set **Parameterization** to `Use an I-V data point at
second measurement temperature`, `Specify saturation current at
second measurement temperature`, or `Specify the energy gap,
EG`.

### **Device simulation temperature** — Device simulation temperature `25` `°C` (default)

Specify the value for the temperature *T*s, at
which the device is to be simulated.

#### Dependencies

To enable this parameter, set **Parameterization** to `Use
an I-V data point at second measurement temperature`, `Specify
saturation current at second measurement temperature`, or `Specify
the energy gap, EG`.

### Faults

### **Diode fault** — Option to model fault in diode `Add fault` (default)

Option to model a fault in the Diode block.

To add a fault, click the **Add fault**
hyperlink.

### **Failure mode** — Failure category `Open` (default) | `Short` | `Parameter shift`

Specify the failure mode of the Diode block:

- `Open` — Once the fault is triggered, the series
  resistance increases instantaneously. You can use this type of fault to model a diode that
  fails due to metallization burnout.
- `Short` — Once the fault is triggered, the parallel
  conductance increases instantaneously. You can use this option to model a diode that fails
  due to punch-through.
- `Parameter shift` — The block parameters change over
  time starting from the moment that the fault is triggered. You can use this option to
  model a diode that fails due to aging.

#### Dependencies

To enable this parameter, add a fault to the Diode block by clicking the
**Add fault** hyperlink in the **Diode fault**
parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Fault transition time constant** — Fault transition time constant `1e-3` `s` (default) | positive scalar

Time constant for transitioning to faulted state.

#### Dependencies

To enable this parameter, add a fault to the Diode block by clicking the
**Add fault** hyperlink in the **Diode fault**
parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted series resistance** — Faulted series resistance `1000` `Ohm` (default) | finite nonnegative scalar

Series resistance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Failure mode** to `Open`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted parallel conductance** — Faulted parallel conductance `1000` `1/Ohm` (default) | finite nonnegative scalar

Parallel conductance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Failure mode** to `Short`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted forward voltage** — Faulted forward voltage `0.6` `V` (default) | positive scalar

Forward voltage in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Piecewise
  linear`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted on resistance** — Faulted on resistance `0.3` `Ohm` (default) | positive scalar

On resistance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Piecewise
  linear`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted off conductance** — Faulted off conductance `1e-8` `S` (default) | positive scalar

Off conductance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Piecewise
  linear`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted zener resistance** — Faulted zener resistance `0.3` `Ohm` (default) | positive scalar

Off conductance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Piecewise
  linear`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted reverse breakdown voltage** — Faulted reverse breakdown voltage `inf` `V` (default) | positive scalar

Reverse breakdown voltage in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Piecewise
  linear`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted currents, [I1 I2]** — Faulted currents `[.0137, .545]` `A` (default) | 2-D vector of positive scalars

*I1* and *I2* currents in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use two I-V curve data
  points`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted voltages, [V1 V2]** — Faulted voltages `[.6, .7]` `V` (default) | 2-D vector of positive scalars

*V1* and *V2* voltages in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use two I-V curve data
  points`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted ohmic resistance, RS** — Faulted voltages `0` `Ohm` (default) | nonnegative scalar

Ohmic resistance in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted saturation current, IS** — Faulted saturation current `1e-12` `A` (default) | positive scalar

Saturation current in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use parameters IS and
  N` or `Use an I-V data point and IS`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted emission coefficient, N** — Faulted emission coefficient `1` (default) | positive scalar

Emission coefficient in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use parameters IS and
  N` or `Use an I-V data point and N`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted current, I1** — Faulted current `0.0137` `A` (default) | positive scalar

Current in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use an I-V data point and
  IS` or `Use an I-V data point and N`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted voltage, V1** — Faulted voltage `0.6` `V` (default) | positive scalar

Voltage in faulted state.

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to
  `Exponential`.
- Set **Parameterization** to `Use an I-V data point and
  IS` or `Use an I-V data point and N`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted forward currents, If(Tj,Vf)** — Faulted forward currents `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default) | matrix of nonnegative scalars

Forward currents, *If(Tj,Vf)*, in faulted state. This parameter must be
a vector of at least three nonnegative elements in ascending order. The zero point is
optional (*Ir(Tj,Vr)* = 0A).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in If(Tj,Vf)
  form`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted forward voltages, Vf** — Faulted forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default) | vector of nonnegative scalars

Forward voltages, *Vf*, in faulted state. This parameter must be a
vector of at least three nonnegative elements in ascending order. The zero point is optional
(*Vf* = 0V).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in If(Tj,Vf)
  form`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted reverse currents, Ir(Tj,Vr)** — Faulted reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A` (default) | matrix of nonnegative scalars

*Since R2024a*

Reverse currents, *Ir(Tj,Vr)*, in faulted state. This parameter must be
a vector of at least three nonnegative elements in ascending order. The zero point is
optional (*Ir(Tj,Vr)* = 0A).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in If(Tj,Vf)
  form`.
- Select the **Model Zener diode** parameter.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted reverse voltages, Vr** — Faulted reverse voltages `[1, 2, 4, 5, 7, 8, 10]` `V` (default) | vector of nonnegative scalars

*Since R2024a*

Reverse voltages, *Vr*, in faulted state. This parameter must be a
vector of at least three nonnegative elements in ascending order. The zero point is optional
(*Vr* = 0V).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in If(Tj,Vf)
  form`.
- Select the **Model Zener diode** parameter.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted forward voltages, Vf(Tj,If)** — Faulted forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default) | matrix of nonnegative scalars

Forward voltages, *Vf(Tj,If)*, in faulted state. This parameter must be
a vector of at least three nonnegative elements in ascending order. The zero point is
optional (*Vf(Tj,If)* = 0V).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in Vf(Tj,If)
  form`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted forward currents, If** — Faulted forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default) | vector of nonnegative scalars

Forward currents, *If*, in faulted state. This parameter must be a
vector of at least three nonnegative elements in ascending order. The zero point is optional
(*If* = 0A).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in Vf(Tj,If)
  form`.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted reverse voltages, Vr(Tj,Ir)** — Faulted reverse voltages `[1, 10, 20, 25, 30, 32.5, 35; 1, 5, 10, 20, 25, 30, 32]` `V` (default) | matrix of nonnegative scalars

*Since R2024a*

Reverse voltages, *Vr(Tj,Ir)*, in faulted state. This parameter must be
a vector of at least three nonnegative elements in ascending order. The zero point is
optional (*Vr(Tj,ir)* = 0V).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in Vf(Tj,If)
  form`.
- Select the **Model Zener diode** parameter.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted reverse currents, Ir** — Faulted reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A` (default) | vector of nonnegative scalars

*Since R2024a*

Reverse currents, *Vr*, in faulted state. This parameter must be a
vector of at least three nonnegative elements in ascending order. The zero point is optional
(*Ir* = 0A).

#### Dependencies

To enable this parameter:

- Add a fault to the Diode block by clicking the **Add fault**
  hyperlink in the **Diode fault** parameter.
- Set **Diode model** to `Tabulated I-V
  curve`.
- Set **Table type** to `Table in Vf(Tj,If)
  form`.
- Select the **Model Zener diode** parameter.
- Set **Failure mode** to `Parameter
  shift`.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted capacitance and charge as percentage of unfaulted** — Faulted capacitance and charge as percentage of unfaulted `100` (default) | finite positive scalar

Capacitance and charge in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter, add a fault to the Diode block by clicking the
**Add fault** hyperlink in the **Diode fault**
parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible reverse voltage** — Maximum permissible reverse voltage `inf` `V` (default) | positive scalar

Maximum reverse voltage above which a fault may be triggered.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Number of events to fail when exceeding voltage** — Number of events to fail when exceeding voltage `1` (default) | positive scalar integer

Number of times the diode must exceed the reverse voltage threshold before a fault is
triggered.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible current** — Current threshold to fault transition `inf` `A` (default) | positive scalar

Current threshold to a fault transition. If the current exceeds this value for longer
than the **Time to fail when exceeding current** parameter value, then the
block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Maximum length of time that the current can exceed the maximum permissible value without
triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum diode recovery, dV/dt** — Diode recovery threshold `inf` `V/s` (default) | positive scalar

Maximum diode recovery.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible temperature** — Temperature threshold to fault transition `inf` `K` (default) | positive scalar

Maximum permissible temperature value. If the temperature exceeds this value for longer
than the value of the **Time to fail when exceeding temperature** parameter,
then the block enters the faulted state.

#### Dependencies

To enable this parameter:

- In the **Fault Inspector** window, set **Trigger Type** to `Behavioral`.
- Set **Diode model** to `Piecewise
  Linear`.

This parameter appears in the **Trigger** section of the
**Fault Inspector** window.

### **Time to fail when exceeding temperature** — Time to fail when exceeding current `1` `s` (default) | positive scalar

Amount of time that the temperature must continuously exceed the maximum permissible
temperature before a behavioral fault is triggered.

#### Dependencies

To enable this parameter:

- In the **Fault Inspector** window, set **Trigger Type** to `Behavioral`.
- Set **Diode model** to `Piecewise
  Linear`.

This parameter appears in the **Trigger** section of the
**Fault Inspector** window.

### Thermal Port

To enable these parameters, set **Modeling option** to `Show
thermal port`.

For more information about using thermal ports and the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

### **Thermal network** — Options for thermal network modeling `External` (default) | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

Options for modeling the thermal network of the block.

### **Thermal mass parameterization** — Option to parameterize thermal mass `By thermal time constants` (default) | `By thermal mass`

Options to parameterize the thermal mass:

- `By thermal time constants` — Parameterize the thermal
  masses in terms of thermal time constants.
- `By thermal mass` — Specify the thermal mass values
  directly.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`, `Cauer
model`, or `Cauer model parameterized with Foster
coefficients`.

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances `[0, 10]` `K/W` (default) | vector of nonnegative values

Row vector, [ *R\_JC*
*R\_CA* ], of two thermal resistance values, represented by two Conductive
Heat Transfer blocks. The first value, *R\_JC*, is the thermal resistance
between the junction and the case. The second value, *R\_CA*, is the thermal
resistance between port **H** and the device case.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`.

### **Junction and case thermal time constants, [t\_J t\_C]** — Junction and case thermal time constants `[0, 10]` `s` (default) | vector of nonnegative values

Row vector, [ *t\_J*
*t\_C* ], of two thermal time constant values. The first value,
*t\_J*, is the junction time constant. The second value,
*t\_C*, is the case time constant.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters` and
**Thermal mass parameterization** to `By thermal time
constants`.

### **Junction and case thermal masses, [M\_J M\_C]** — Junction and case thermal masses `[0, 1]` `J/K` (default) | vector of positive values

Row vector, [ *M\_J*
*M\_C* ], of two thermal mass values. The first value,
*M\_J*, is the junction thermal mass. The second value,
*M\_C*, is the case thermal mass.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters` and
**Thermal mass parameterization** to `By thermal
mass`.

### **Junction and case initial temperatures, [T\_J T\_C]** — Junction and case initial temperatures `[25, 25]` `degC` (default) | vector of positive values

Row vector, [ *T\_J* *T\_C* ], of two temperature
values. The first value, *T\_J*, is the junction initial temperature. The
second value, *T\_C*, is the case initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[1, 3, 10]` `K/W` | `[4, 6]` `K/W` | vector of positive values

Row vector of *n* thermal resistance values, represented by the Cauer
elements used in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[1, 3, 10]`. If you set
**Thermal network** to `Cauer model parameterized with Foster
coefficients`, the default value is `[4, 6]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model parameterized with
Foster coefficients`.

### **Thermal masses, [M1 M2 … Mn]** — Thermal masses `[.1, .3, 1]` `J/K` | `[1.5, 3]` `J/K` | vector of positive values

Row vector of *n* thermal mass values, where *n* is
the number of Cauer elements in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.1, .3, 1]`. If you set
**Thermal network** to `Cauer model parameterized with Foster
coefficients`, the default value is `[1.5, 3]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model parameterized with
Foster coefficients` and **Thermal mass parameterization** to
`By thermal mass`.

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — Initial temperatures of thermal masses `[25, 25, 25]` `degC` (default) | vector of positive values

Row vector of temperature values that correspond to the temperature drop across each
thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[1, 3, 10]` `s` | `[6, 18]` `s` | vector of positive values

Row vector of *n* thermal time constant values, where
*n* is the number of Cauer elements in the thermal network. The length of
this vector must match the length of **Thermal resistances, [R1 R2 … Rn]**.
With this parameterization, the block computes the thermal masses as
`Mi =
ti/Ri`, where
`Mi`, `ti`
and `Ri` are the thermal mass, thermal time, and
thermal resistance for the ith Cauer element (if you set
**Thermal network** to `Cauer model`) or Foster
element (if you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is `[1, 3, 10]`. If you set
**Thermal network** to `Cauer model parameterized with Foster
coefficients`, the default value is `[6, 18]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model parameterized with
Foster coefficients`and **Thermal mass parameterization** to
`By thermal time constants`.

### **Initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures `[25, 25, 25, 25]` `degC` (default) | vector of positive values

Row vector of the temperature values of each node starting from the junction.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model parameterized with Foster coefficients`.

### **Junction thermal mass** — Thermal mass of junction `0.01` `J/K` (default) | positive scalar

Thermal mass of the junction.

#### Dependencies

To enable this parameter, set **Fidelity level** to `Ideal
switching` and **Thermal network** to
`External`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2024a: Model tabulated reverse I-V characteristics

You can now model the tabulated reverse I-V characteristics for the Diode block.

To model the reverse I-V characteristics, select the **Model Zener diode**
parameter and then specify the new **Reverse voltages, Vr(Tj,Ir)**,
**Reverse currents, Ir(Tj,Vr)**, **Reverse voltages, Vr** and
**Reverse currents, Ir** parameters.

Before R2024a, you can only model the reverse I-V characteristics by specifying the off
conductance of the reverse-biased diode.

### R2024a: **Junction capacitance voltage** variable replaced with **Charge of junction capacitance** variable

If, in the **Capacitance** section, you set
**Parameterization** to `Use C-V curve data points`
or `Use parameters Cj0, VJ, M & FC`, you now specify
**Initial Targets** and **Nominal Values** for capacitance
and charge modeling using the **Charge of junction capacitance** variable. The
**Junction capacitance voltage** variable is no longer enabled.

If a model you created in an earlier release uses these values for
**Parameterization** and specifies **Initial Targets** or
**Nominal Values** for the **Junction capacitance voltage**
variable, you must update the model. For more information on how to calculate the charge of
junction capacitance, see Junction Capacitance.

### R2023b: Show the electronic symbol for a Zener diode in the block icon

The Diode block icon now shows different electronic symbols
depending on whether you are modeling a standard diode or a Zener diode. To model a Zener diode,
select the **Model a Zener diode** parameter and specify a finite value for the
**Reverse breakdown voltage** parameter.

Before R2023b, you can model a Zener diode by specifying a finite value for the
**Reverse breakdown voltage** parameter, but the block icon shows the
electronic symbol for a standard diode. To enable the **Reverse breakdown
voltage** parameter, set **Diode model** to `Piecewise
linear` or `Exponential`.

If you create a model before R2023b and specify a finite value for the **Reverse
breakdown voltage** parameter, the block now enables the **Model a Zener
diode** parameter by default for backward compatibility.

### R2023b: Scale reverse recovery loss with current and voltage

You can now scale a fixed reverse recovery loss value with current and voltage. To enable
this option, select the **Scale reverse recovery loss with current and
voltage** parameter.

Models you create in R2023a or earlier default to no scaling for backward
compatibility.

### R2023b: Model a specific diode using built-in parameterizations

You can now parameterize the Diode block by using built-in parameterizations that represent
components from specific suppliers. The parameterizations of these diodes match the manufacturer
data sheets. Use these parameterizations to set up this block to replicate the V-I curve for
forward voltage from datasheets of specific suppliers. To load a predefined parameterization,
double-click the Diode block, click the **<click to select>**
hyperlink of the **Selected part** parameter, and, in the Block
Parameterization Manager window, select the part you want to use from the list of available
components.

### R2023a: Implement temporal or behavioral triggers for faults using a single parameter

The **Enable temporal trigger** and **Enable behavioral trigger** parameters have been removed and are replaced with the **Fault
trigger** parameter. You can set the **Fault trigger**
parameter to `Temporal` or `Behavioral`.
You can enable only one trigger.

If you created a model in an earlier release and enabled both temporal and behavioral
triggers, now only the temporal trigger is enabled. Therefore, the simulation results are
different if the behavioral trigger causes the fault in your model.

If you want to trigger a fault at a specific time, set the **Fault trigger**
parameter to `Temporal`. If you want to determine whether a system
fails and, if so, when it fails, set the **Fault Trigger** parameter to
`Behavioral`.

## Description

Piecewise linear, exponential, or tabulated diode

The Diode block can represent either a piecewise linear
diode, an exponential diode, or a diode with tabulated I-V curve. Use the **Fidelity
level** parameter to select the level of detail in the dynamics model.

### Piecewise Linear Diode

The piecewise linear diode model is the same model as the **Simscape™** > **Foundation Library** > **Electrical** > **Electrical Elements** > **Diode** block, with the addition of a fixed junction capacitance and optional charge
dynamics. If the diode forward voltage exceeds the value specified in the **Forward
voltage** parameter, the diode behaves as a linear resistor with the resistance
specified in the **On resistance** parameter. Otherwise, the diode behaves as a
linear resistor with the small conductance specified in the **Off conductance**
parameter. Zero voltage across the diode results in zero current flowing.

For more information about the Diode block in the Simscape Foundation library, see Diode.

### Exponential Diode

The exponential diode model represents the following relationship between the diode current
*I* and the diode voltage *V*:

I=IS⋅(eqVNkTm1−1)   V>−BVI=−IS⋅(e−q(V+Vz)kTm1−eqVNkTm1)  V≤−BV

where:

- *q* is the elementary charge on an electron (1.602176e–19
  coulombs).
- *k* is the Boltzmann constant (1.3806503e–23 J/K).
- *BV* is the **Reverse breakdown voltage** parameter
  value.
- *N* is the emission coefficient.
- *IS* is the saturation current.
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

When you select `Use parameters IS and N` for the
**Parameterization** parameter, you specify the diode in terms of the
**Saturation current IS** and **Emission coefficient N**
parameters. When you select `Use two I-V curve data points` for the
**Parameterization** parameter, you specify two voltage and current
measurement points on the diode I-V curve and the block derives the *IS* and
*N* values. The block then calculates *IS* and
*N* as follows:

- N=((V1−V2)/Vt)/(log(I1)−log(I2))
- IS=(I1/(exp(V1/(NVt))−1)+I2/(exp(V2/(NVt))−1))/2

where:

- *Vt* =
  *k**Tm1* /
  *q*.
- *V1* and
  *V2* are the values in the **Voltages [V1
  V2]** vector.
- *I1* and
  *I2* are the values in the **Currents [I1
  I2]** vector.

When you select `Use an I-V data point and IS` for the
**Parameterization** parameter, then the block calculates *N*
as follows:

N=V1/(Vtlog(I1IS+1))

When you select `Use an I-V data point and N` for the
**Parameterization** parameter, then the block calculates
*IS* as follows:

IS=I1/(exp(V1/(NVt)−1))

### Tabulated Diode

To model a tabulated diode, set the **Diode model** parameter to
`Tabulated I-V curve`. This figure shows the implementation of the
tabulated diode option:

If you select the **Model Zener
Diode** parameter, you can also model the tabulated reverse I-V
characteristics. *(since R2024a)*

If you do not select the **Model Zener Diode** parameter, the block models
the reverse characteristics by using the **Off conductance** parameter:

- If the voltage is less than -1 V, the block models the I-V relationship with a constant
  off-state conductance equal to the value of the **Off conductance**
  parameter. The value you specify must be less than the gradient of the forward I-V curve for
  small positive voltages.
- If the voltage is between -1 V and 0 V, the block uses makima interpolation so that the
  I-V curves for forward and reverse bias overlap smoothly.

The block uses `makima` interpolation to find
intermediate values. If the voltage or current exceed the tabulated data range, the block uses
linear extrapolation after the last voltage-current data point.

### Junction Capacitance

The Diode block models the junction capacitance only if you
set the **Modeling option** parameter to `No thermal
port` or the **Fidelity level** parameter to `Include
capacitance and charge dynamics`. To include a junction capacitance:

- Select `Include fixed or zero junction capacitance` for the
  **Parameterization** parameter. The capacitance is fixed.
- Select `Use parameters CJO, VJ, M & FC` for the
  **Parameterization** parameter. The block uses the coefficients
  *CJO*, *VJ*, *M*, and
  *FC* to calculate a junction capacitance that depends on the junction
  voltage.
- Select `Use C-V curve data points` for the
  **Parameterization** parameter. The block uses three capacitance values on
  the C-V capacitance curve to estimate *CJO*, *VJ*, and
  *M* and uses these values with the specified value of *FC*
  to calculate a junction capacitance that depends on the junction voltage. The block
  calculates *CJO*, *VJ*, and *M* as follows:

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  where:

  - *VR1*,
    *VR2*, and
    *VR3* are the values in the **Reverse
    bias voltages [VR1 VR2 VR3]** vector.
  - *C1*,
    *C2*, and
    *C3* are the values in the
    **Corresponding capacitances [C1 C2 C3]** vector.

  The reverse bias voltages (defined as positive values) should satisfy
  *VR3* >
  *VR2* >
  *VR1*. This means that the capacitances should
  satisfy *C1* >
  *C2* >
  *C3* as reverse bias widens the depletion region and
  hence reduces capacitance. Violating these inequalities results in an error. Voltages
  *VR2* and
  *VR3* should be well away from the Junction
  potential *VJ*. Voltage *VR1* should
  be less than the Junction potential *VJ*, with a typical value for
  *VR1* being 0.1 V.

The voltage-dependent junction capacitance is defined in terms of the charge of junction
capacitance *Qj* as:

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

These equations are the same as used in [2], except that the
temperature dependence of *VJ* and *FC* is not modeled.

### Charge Dynamics

The Diode block models the charge dynamics only if you set
the **Modeling option** parameter to `No thermal port`
or the **Fidelity level** parameter to `Include capacitance and
charge dynamics`. For applications such as commutation diodes it can be important
to model diode charge dynamics. When a forward-biased diode has a reverse voltage applied across
it, it takes time for the charge to dissipate and hence for the diode to turn off. The time
taken for the diode to turn off is captured primarily by the transit time parameter. Once the
diode is off, any remaining charge then dissipates, the rate at which this happens being
determined by the carrier lifetime.

The Diode block uses the model of Lauritzen and Ma [3] to capture these effects. These are the defining equations.

|  |  |
| --- | --- |
| i=qE−qMTM | **(1)** |

|  |  |
| --- | --- |
| dqMdt+qMτ−qE−qMTM=0 | **(2)** |

|  |  |
| --- | --- |
| qE=(τ+TM)i | **(3)** |

where:

- *i* is the diode current.
- *qE* is the junction charge.
- *qM* is the total stored charge.
- *TM* is the transit time.
- *τ* is the carrier lifetime.
- *vD* is the voltage across the diode.
- *vF* is the diode forward voltage.
- *R* is the diode on resistance.
- *G* is the diode off conductance.

This graphic shows a typical reverse-mode current characteristic for a diode device.

where:

- *iRM* is the peak reverse current.
- *iF* is the starting forward current when
  measuring *iRM*.
- *a* is the rate of change of current when measuring
  *iRM*.
- *trr* is the reverse recovery time.

Data sheets for diodes quote values for peak reverse current for an initial forward current
and a steady rate of change of current. The data sheet might also provide values for reverse
recovery time and total recovery charge.

**How the Block Calculates *TM* and Tau**

The block calculates transit time *TM* and carrier
lifetime *τ* based on the values you enter for the **Charge
Dynamics** parameters. The block uses *TM*
and *τ* to solve the charge dynamics equations 1, 2, and 3.

During initial current drop in reverse mode, the diode is still on, and the rate of change
of current is determined by an external test circuit.

First, the block uses equation 1 to perform this calculation.

|  |  |
| --- | --- |
| iF+at=qE−qMTM | **(4)** |

Then, it substitutes equation 4 into equation 2.

|  |  |
| --- | --- |
| dqMdt+qMτ=iF+at | **(5)** |

Then, it solves equation 5 for *qM*,

|  |  |
| --- | --- |
| qM=iFτ−aτ2+kexp(tτ)+aτt, | **(6)** |

where *k* is a constant.

When *t* is zero, *i* =
*iF* and *qM*
= *τiF* because the system is in steady state.

Substituting these relationships into equation 6 and solving the equation gives
*k* = *aτ2*.

Therefore,

|  |  |
| --- | --- |
| qM=iFτ+aτ2(1exp(tτ)−1)+aτt. | **(7)** |

At time *t* = *ts*, the
current is *iRM* and the junction charge
*qE* is zero.

The block substitutes these values into equation 1.

|  |  |
| --- | --- |
| iRM=−qMTM | **(8)** |

The block rearranges equation 8 to solve for
*qM* and substitutes the result into equation
7.

|  |  |
| --- | --- |
| −TMiRM=iFτ+aτ2(1exp(tsτ)−1)+aτts | **(9)** |

Then, the block expresses time *ts* in terms of
*iRM*, *iF*,
and *a*.

|  |  |
| --- | --- |
| ts=iRM−iFa | **(10)** |

Consider the diode recovery, that is, when *t* >
*ts*. The diode is reverse biased, and current and
junction charge are effectively zero.

The current is defined by this equation.

|  |  |
| --- | --- |
| i=iRMexp[−(t−ts)τrr], | **(11)** |

where:

|  |  |
| --- | --- |
| 1τrr=1τ+1TM. | **(12)** |

The block now relates the expression in equation 12 to the reverse recovery time
*trr*.

When t=iFa+trr, the current is iRM10.

Therefore,

|  |  |
| --- | --- |
| exp(−t−tsτrr)=0.1 | **(13)** |

and

|  |  |
| --- | --- |
| trr=τrrlog(10)+iRMa. | **(14)** |

The block uses equations 9 and 14 to calculate values for
*TM* and *τ*. The calculation uses
an iterative scheme because of the exponential term in Equation 9.

**Alternatives to Specifying *trr* Directly**

In addition to allowing you to specify reverse recovery time
*trr* directly, the block supports three alternative
parameterizations. The block can derive *trr* from
either of these parameters:

- Reverse recovery time stretch factor *λ*
- Reverse recovery charge *Qrr*, when the data
  sheet specifies this value instead of the reverse recovery time.
- Reverse recovery energy *Erec*, when the data
  sheet specifies this value instead of the reverse recovery time.

The relationship between reverse recovery time stretch factor *λ* and
*trr* is expressed by the equation

λ=trraiRM.

Reverse recovery time must be greater than iRMa and a typical value is 3(iRMa).

Therefore, a typical value for *λ* is 3. *λ* must be
greater than 1.

Reverse recovery charge *Qrr* is the integral over
time of the reverse current from the point where the current goes negative until it decays back
to zero.

The initial charge, to time ts (as shown in the figure), is
expressed by this equation:

|  |  |
| --- | --- |
| Qs=12(−iRM)iRMa. | **(15)** |

Integrating equation 11 gives the charge between times ts and inf.
This charge is equal to

τrriRM.

Therefore, total reverse recovery charge is given by this equation:

|  |  |
| --- | --- |
| Qrr=−iRM22a−τrriRM. | **(16)** |

Rearranging equation 16 to solve for *τrr* and
substituting the result into equation 14 gives an equation that expresses
*trr* in terms of
*Qrr*:

trr=(QrriRM+iRM2a)log(10)+iRMa.

Alternatively, the block calculates *τrr* by using
the reverse recovery energy, *Erec*. This equation
defines the diode voltage curve:

|  |  |
| --- | --- |
| vd=vR−(vR−vRM)exp(−(t−t1)/τrr), | **(17)** |

where vRM=vR−iRM(R−Lτrr) is the maximum diode reverse voltage.

If Lτrr≫R, which is a common condition for the reverse recovery test circuit, the block
calculates the maximum diode reverse voltage as:

vRM=vR+iRMLτrr.

Since the drop time value is small, the block assumes that the diode current drop is
linear:

|  |  |
| --- | --- |
| iF+didt · t = qE−qMTM. | **(18)** |

Then, it substitutes equation 18 into equation 5:

|  |  |
| --- | --- |
| dqMd+qMτ=iF+didt · t. | **(19)** |

To obtain the total stored charge, it solves equation 19 :

|  |  |
| --- | --- |
| qM=iFτ+didt · τ2(1exp(tτ)−1)+didt · τt, | **(20)** |

where *didt* is the gradient of the current.

When t=t1=iRM−iFdidt, the peak reverse current is:

|  |  |
| --- | --- |
| iRM=−qMTM. | **(21)** |

The block now substitutes equation 21 into equation 20:

|  |  |
| --- | --- |
| −iRMTM=iFτ+ didt · τ2(exp(−iRM−iFdidt · τ)−1)+τ(iRM−iF)−(TM+τ)iRM=didt · τ2(exp(−iRM−iFdidt · τ)−1)iRM=F(didt,iF,TM,τ). | **(22)** |

Finally, the block solves equation 22 to obtain the reverse recovery energy:

|  |  |
| --- | --- |
| Erec=∫t1t2idvddtErec=τrriRM(vR+vRM)2Erec=iRM(2vRτrr+iRML)2. | **(23)** |

**Charge dynamics with faults**

When the device is faulted, the Diode block calculates the
junction charge as

qE=(τ+TM)idiode,

where:

- *idiode* is the diode current without the
  charge model.
- *qE* is the junction charge.
- *TM* is the transit time.
- *τ* is the carrier lifetime.

This equation then defines the value of the diode current:

dqMdt+qMτ−qE−qMTM=0i=qE−qMTMQscale−(Qscale−1)idiode

where:

- *i* is the diode current.
- *qM* is the total stored charge.
- *Qscale* is the current value of the charge
  ratio.

### Temperature Dependence

The default behavior for the Diode block is that dependence
on temperature is not modeled, and the device is simulated at the temperature for which you
provide block parameters. The exponential diode model contains several options for modeling the
dependence of the diode current-voltage relationship on temperature during simulation.
Temperature dependence of the junction capacitance is not modeled because it has a much smaller
effect.

When including temperature dependence, the diode defining equation remains the same. The
measurement temperature value, *Tm1*, is replaced with
the simulation temperature, *Ts*. The saturation
current, *IS*, becomes a function of temperature according to the following
equation:

ISTs=ISTm1⋅(Ts/Tm1)XTI/N⋅exp(−EGNkTs(1−Ts/Tm1))

where:

- *Tm1* is the temperature at which the diode
  parameters are specified, as defined by the **Measurement temperature**
  parameter value.
- *Ts* is the simulation temperature.
- *ISTm1* is the saturation current at measurement
  temperature.
- *ISTs* is the saturation current at simulation
  temperature. This is the saturation current value used in the standard diode equation when
  temperature dependence is modeled.
- *EG* is the energy gap for the semiconductor type measured in
  joules(J). The value for silicon is usually taken to be 1.11 eV, where 1 eV is
  1.602e-19.
- *XTI* is the saturation current temperature exponent. This is usually
  set to 3.0 for pn-junction diodes, and 2.0 for Schottky barrier diodes.
- *N* is the emission coefficient.
- *k* is the Boltzmann constant (1.3806503e–23 J/K).

Appropriate values for *XTI* and *EG* depend on the type
of diode and the semiconductor material used. Default values for particular material types and
diode types capture approximate behavior with temperature. The block provides default values for
common types of diode.

In practice, the values of *XTI* and *EG* need tuning to
model the exact behavior of a particular diode. Some manufacturers quote these tuned values in a
SPICE Netlist, and you can read off the appropriate values. Otherwise, you can determine
improved estimates for *EG* by using a datasheet-defined current-voltage data
point at a higher temperature. The block provides a parameterization option for this. It also
gives the option of specifying the saturation current at a higher temperature
*ISTm2* directly.

You can also tune the values of *XTI* and *EG* yourself,
to match lab data for your particular device. You can use Simulink®
Design Optimization™ software to help tune the values for *XTI* and
*EG*.

**Caution**

Device temperature behavior is also dependent on the emission coefficient. An
inappropriate value for the emission coefficient can give incorrect temperature dependence,
because saturation current is a function of the ratio of *EG* to
*N*.

If defining a finite reverse breakdown voltage (*BV*), then the value of
the reverse *BV* is modulated by the reverse breakdown temperature coefficient
*TCV* (specified using the **Reverse breakdown voltage temperature
coefficient, dBV/dT** parameter):

|  |  |
| --- | --- |
| *BVTs* = *BVTm1* – *TCV*· (*Ts* – *Tm1*) | **(24)** |

### Ideal Switching

You can use the ideal switching option with these ideal switching semiconductor blocks:

- GTO
- Half-Bridge (Ideal,
  Switching)
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

You can model the diode in these blocks internally, or you can model the diode
externally using a separate Diode block.

To enable the ideal switching option, set the **Fidelity level** parameter
to `Ideal Switching`.

This figure shows the voltage and current of the diode in a switching regime inside a half-bridge.

Reverse recovery loss is one of the main sources of thermal loss in diodes. The diode
dissipates energy every time it turns off, from its conducting state to the open-circuit state.

With ideal switching, the block does not use a physics-based charge model. The block
represents the losses that the charge creates during reverse recovery as an instantaneous
loss.

The block applies reverse recovery losses by stepping up the junction temperature with a
value equal to the reverse recovery loss divided by the total thermal mass at the junction.

If you set the **Reverse recovery loss model** parameter to
`Tabulated loss`, the value of the **Reverse recovery loss
table, Erec(Tj, If)** parameter specifies the dissipated energy as a function of the
junction temperature and the forward current just before the switching event. The off-state
voltage linearly scales the losses relative to the **Turn-off voltage when measuring
recovery loss, Vrec** parameter value. The table uses delayed values for the current
and voltage. To use a value in the lookup table that is close to the instantaneous value, set
the **Filter time constant for voltage and current values**
parameter to a value that is lower than the fastest switching period.

If you set the **Reverse recovery loss model** parameter to
`Fixed loss`, the value of the **Reverse recovery
loss** parameter specifies the energy dissipated during each turn-off event. If you
select the **Scale reverse recovery loss with current and voltage** parameter,
then the block scales this loss value linearly by the on-state current and the off-state
voltage. To use scaling values that are close to the instantaneous values, set **Filter time constant for voltage and current values** to a value that is
lower than the fastest switching period.

**Note**

The `lastReverseRecoveryLoss` variable in the logged simulation data
includes the reverse recovery losses as a pulse with an amplitude equal to the energy loss. If
you use a script to sum the total losses over a defined simulation period, you must sum the
pulse values at each pulse rising edge. Alternatively, you can extract conduction and switching
losses from logged data using the `ee_getPowerLossSummary` and `ee_getPowerLossTimeSeries` functions. To learn how to log and plot simulation data,
see the Log and Plot Simulation Data example.

The `power_dissipated` variable in the logged simulation data does not
include switching losses because the block models the losses as instantaneous events. The
`power_dissipated` variable reports ohmic on-state losses.

### Faults

To model a fault in the Diode block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Diode block allows you to model three types of faults:

- `Open` — Once the fault is triggered, the series
  resistance increases instantaneously. You can use this type of fault to model a diode that
  fails due to metallization burnout.
- `Short` — Once the fault is triggered, the parallel
  conductance increases instantaneously. You can use this option to model a diode that fails
  due to punch-through.
- `Parameter shift` — The block parameters shift over time
  starting from the moment that the fault is triggered. You can use this option to model a
  diode that fails due to aging.

The block can trigger fault events:

- At a specific time.
- When a current limit, a voltage limit, or a temperature limit are exceeded for longer
  than a specific time interval.

If you want to trigger a fault at a specific time, in the
**Fault Inspector** window, set **Trigger type** to
`Timed`. If you want to determine whether a system fails and, if
so, when it fails, in the **Fault Inspector** window, set **Trigger
type** to `Behavioral`.

If you select the behavioral trigger, the component fails as soon as one of the trigger
conditions is true.

**Parameter Shift Fault**

If, in the **Faults** settings, you set the **Failure
mode** parameter to `Parameter shift`, the diode fails due
to the aging of its components. This equation defines the value of the shifted parameters:

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

where *tth* is the time threshold
when the fault is triggered and *τ* is the value of the **Fault
transition time constant** parameter.

### Modeling Thermal Effects

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

### Modeling a Zener Diode

*Since R2023b*

To model a Zener diode that conducts in the forward and reverse biased directions, select
the **Model Zener diode** parameter and specify a finite value for
the **Reverse breakdown voltage** parameter.

When you select this option, you can model the
reverse I-V characteristics for the Diode block by specifying the new **Reverse
voltages, Vr(Tj,Ir)**, **Reverse currents, Ir(Tj,Vr)**,
**Reverse voltages, Vr** and **Reverse currents, Ir**
parameters. *(since R2024a)*

The Diode block icon depends on whether you model a Zener
diode and whether you expose the thermal port. For more information about exposing the thermal
port, see Modeling Thermal Effects.

| **Modeling option** Parameter Value | **Model a Zener diode** Parameter Value | Block Icon |
| --- | --- | --- |
| `No thermal port` | `Off` |  |
| `On` |  |
| `Show thermal port` | `Off` |  |
| `On` |  |

### Parameterization

*Since R2023b*

The Diode block supports multiple predefined
parameterizations.

Use this parameterization data to replicate the V-I curve for forward voltage from
datasheets of specific suppliers. To load a predefined parameterization, double-click the Diode
block, click the **<click to select>** hyperlink of the
**Selected part** parameter, and, in the Block Parameterization Manager
window, select the part you want to use from the list of available components.

**Note**

The predefined parameterizations of Simscape components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about predefined parameterization and a list of the available
components, see List of Pre-Parameterized Components.

You can also use the `ee_importDeviceParameters` function to extract the device parameters from an XML
file and import them into the block. The XML file must be on the MATLAB® path and must use a parameterization format supported by Hitachi or Infineon®.

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

You can plot the basic I-V characteristics of the Diode block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
Diode block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
