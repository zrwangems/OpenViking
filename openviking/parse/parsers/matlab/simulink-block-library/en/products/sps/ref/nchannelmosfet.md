---
type: simulink-block
title: 'N-Channel MOSFET'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'nchannelmosfet'
documentation_source_path: 'ref/nchannelmosfet.html'
language: en
---

# N-Channel MOSFET

## Ports

### Conserving

### **G** — Gate terminal electrical

Electrical conserving port associated with the transistor gate terminal.

### **D** — Drain terminal electrical

Electrical conserving port associated with the transistor drain terminal.

### **S** — Source terminal electrical

Electrical conserving port associated with the transistor source terminal.

### **B** — Body terminal electrical

Electrical conserving port associated with the transistor body terminal.

#### Dependencies

To enable this port, set **Parameterization** to
`Four`.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Threshold-based with thermal` or
`Surface-potential-based with thermal`.

## Parameters

### **Modeling Option** — MOSFET representation `Threshold-based` (default) | `Threshold-based with thermal` | `Surface-potential-based` | `Surface-potential-based with thermal`

Select the MOSFET representation:

- `Threshold-based` — Basic model, which represents the
  device using the Shichman-Hodges equation (based on threshold voltage) and does not
  simulate thermal effects. This is the default.
- `Threshold-based with thermal` — Model based on
  threshold voltage and with exposed thermal port.
- `Surface-potential-based` — Model based on surface
  potential. This model does not simulate thermal effects.
- `Surface-potential-based with thermal` —
  Thermal modeling option of the model based on surface potential.

### Main (Threshold-Based Modeling Option)

This configuration of the **Main** parameters corresponds to the
threshold-based block modeling option, which is the default. If you are using the
surface-potential-based modeling option of the block, see Main (Surface-Potential-Based Modeling Option).

### **Number of terminals** — Terminal parameterization `Three` (default) | `Four`

Number of terminals of the block.

### **Parameterization** — Block parameterization `Specify from a datasheet` (default) | `Specify using equation parameters directly` | `Lookup table (2-D, temperature independent)` | `Lookup table (3-D, temperature dependent)`

Select one of the following methods for block parameterization:

- `Specify from a datasheet` — Provide the drain-source
  on resistance and the corresponding drain current and gate-source voltage. The block
  calculates the transistor gain for the Shichman and Hodges equations from this
  information.
- `Specify using equation parameters directly` —
  Provide the transistor gain.
- `Lookup table (2-D, temperature independent)` — Use
  2-D table lookup for drain-source current as a function of gate-source voltage and
  drain-source voltage.
- `Lookup table (3-D, temperature dependent)` — Use 3-D
  table lookup for drain-source current as a function of gate-source voltage, drain-source
  voltage, and temperature.

### **Drain-source on resistance, R\_DS(on)** — Drain-source on resistance `0.025` `Ohm` (default)

Ratio of the drain-source voltage to the drain current for specified values of drain
current and gate-source voltage. *RDS(on)* should
have a positive value.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify from a datasheet`.

### **Drain current, Ids, for R\_DS(on)** — Drain current `6``A` (default)

Drain current the block uses to calculate the value of the drain-source resistance.
*IDS* should have a positive value.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify from a datasheet`.

### **Gate-source voltage, Vgs, for R\_DS(on)** — Gate-source voltage, Vgs `10` `V` (default)

Gate-source voltage the block uses to calculate the value of the drain-source
resistance. *VGS* should have a positive
value.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify from a datasheet`.

### **Gain, K** — Positive constant gain coefficient `5.0` `A/V2` (default)

Positive constant gain coefficient for the Shichman and Hodges equations.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify using equation parameters directly`.

### **Gate-source threshold voltage, Vth** — Gate-source threshold voltage `1.7` `V` (default)

Gate-source threshold voltage *Vth* in the
Shichman and Hodges equations. For an enhancement device,
*Vth* should be positive. For a depletion mode
device, *Vth* should be negative.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Three` and **Parameterization** to
`Specify from a datasheet` or `Specify using equation
parameters directly`.

### **Gate-source threshold voltage at zero bulk-source voltage, Vth0** — Gate-source threshold voltage at zero bulk-source voltage `1.7` `V` (default)

Gate-source threshold voltage at zero bulk-source voltage
*Vth0* in the Shichman and Hodges equations.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify from a datasheet` or `Specify using equation
parameters directly`.

### **Channel modulation, L** — Channel modulation `0` `1/V` (default)

The channel-length modulation, usually denoted by the mathematical symbol
*λ*. When in the saturated region, it is the rate of change of drain
current with drain-source voltage. The effect on drain current is typically small, and the
effect is neglected if calculating transistor gain *K* from drain-source
on-resistance, *RDS(on)*. A typical value is 0.02,
but the effect can be ignored in most circuit simulations. However, in some circuits a small
nonzero value may help numerical convergence.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify from a datasheet` or `Specify using equation
parameters directly`.

### **Gate-source threshold voltage at first non-zero bulk-source voltage, Vth1** — Gate-source threshold voltage at first non-zero bulk-source voltage `1.9071` `V` (default)

Gate-source threshold voltage at first non-zero bulk-source voltage
*Vth1* in the Shichman and Hodges equations.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify from a datasheet`.

### **First bulk-source voltage, Vbs1** — First bulk-source voltage `-1` `V` (default)

First bulk-source voltage, *Vbs1*

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify from a datasheet`.

### **Gate-source threshold voltage at second non-zero bulk-source voltage, Vth2** — Gate-source threshold voltage at second non-zero bulk-source voltage `2.066` `V` (default)

Gate-source threshold voltage at second non-zero bulk-source voltage
*Vth2* in the Shichman and Hodges equations.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify from a datasheet`.

### **Second bulk-source voltage, Vbs2** — Second bulk-source voltage `-2` `V` (default)

Second bulk-source voltage, *Vbs2*

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify from a datasheet`.

### **Body factor** — Body factor `0.5` `V^0.50000` (default)

Body factor, *γ*.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify using equation parameters directly`.

### **Surface potential** — Surface potential `0.5` `V` (default)

Surface potential.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Specify using equation parameters directly`.

### **Measurement temperature** — Measurement temperature `25` `°C` (default)

Temperature *Tm1* at which
**Drain-source on resistance, R\_DS(on)** is measured.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Specify from a datasheet` or `Specify using equation
parameters directly`.

### **Vector of gate-source voltages, Vgs** — Vector of gate-source voltages `[-.5, 2, 3, 4, 5]` `V` (default)

Vector of gate-source voltages.

#### Dependencies

To enable this parameter, set **Parameterization** to either
`Lookup table (2-D, temperature independent)` or
`Lookup table (3-D, temperature dependent)`.

### **Vector of drain-source voltages, Vds** — Vector of drain-source voltages `[0, 2, 4, 8, 12, 16, 20]` `V` (default)

Vector of drain-source voltages, to be used for table lookup. The vector values must be
strictly increasing.

#### Dependencies

To enable this parameter, set **Parameterization** to either
`Lookup table (2-D, temperature independent)` or
`Lookup table (3-D, temperature dependent)`.

### **Vector of bulk-source voltages, Vbs** — Vector of drain-source voltages `[0, -4, -6, -12]` `V` (default)

Vector of bulk-source voltages, to be used for table lookup.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to either
`Lookup table (2-D, temperature independent)` or
`Lookup table (3-D, temperature dependent)`.

### **Tabulated drain-source currents, Ids(Vgs,Vds)** — Tabulated drain-source currents temperature independent `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (default)

Tabulated values for drain-source currents as a function of gate-source voltage and
drain-source voltage, to be used for 2-D table lookup. Each value in the matrix specifies the
drain-source current for a specific combination of gate-source voltage and drain-source
voltage. The matrix size must match the dimensions defined by the gate-source voltage and
drain-source voltage vectors.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Three` and **Parameterization** to
`Lookup table (2-D, temperature independent)`.

### **Vector of temperatures, T** — Vector of temperatures `[25 125]` `degC` (default)

Vector of temperatures, to be used for table lookup. The vector values must be strictly
increasing. The values can be nonuniformly spaced.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Lookup table (3-D, temperature dependent)`.

### **Tabulated drain-source currents, Ids(Vgs,Vds,T)** — Tabulated drain-source currents temperature dependent `zeros(5, 7, 2)` `A` (default)

Tabulated values for drain-source currents as a function of gate-source voltage,
drain-source voltage, and temperature, to be used for 2-D table lookup. Each value in the
matrix specifies the drain-source current for a specific combination of gate-source voltage
and drain-source voltage. The matrix size must match the dimensions defined by the
gate-source voltage, drain-source voltage, and temperature vectors.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Three` and **Parameterization** to
`Lookup table (3-D, temperature dependent)`.

### **Tabulated gate-source threshold voltage, Vth(Vbs)** — Vector of gate-source threshold voltage temperature independent `[.4, 1.2, 1.4, 1.45]` `V` (default)

Tabulated values for gate-source threshold voltage as a function of bulk-source voltage,
to be used for 2-D table lookup The vector values must be strictly increasing.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Lookup table (2-D, temperature independent)`.

### **Tabulated drain-source currents at zero bulk-source voltage, Ids(Vgs,Vds)** — Tabulated drain-source currents at zero bulk-source voltage, temperature independent `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (default)

Tabulated values for drain-source currents at zero bulk-source voltage, as a function of
gate-source voltage and drain-source voltage, to be used for 2-D table lookup. Each value in
the matrix specifies the drain-source current for a specific combination of gate-source
voltage and drain-source voltage. The matrix size must match the dimensions defined by the
gate-source voltage and drain-source voltage vectors.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Lookup table (2-D, temperature independent)`.

### **Tabulated gate-source threshold voltage, Vth(Vbs,T)** — Vector of gate-source threshold voltage temperature dependent `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V` (default)

Tabulated values for gate-source threshold voltage as a function of bulk-source voltage
and temperature, to be used for 3-D table lookup The vector values must be strictly
increasing.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Lookup table (3-D, temperature dependent)`.

### **Tabulated drain-source currents at zero bulk-source voltage, Ids(Vgs,Vds,T)** — Tabulated drain-source currents at zero bulk-source voltage, temperature dependent `zeros(5, 7, 2)` `A` (default)

Tabulated values for drain-source currents at zero bulk-source voltage, as a function of
gate-source voltage, drain-source voltage, and temperature, to be used for 3-D table lookup.
Each value in the matrix specifies the drain-source current for a specific combination of
gate-source voltage, drain-source voltage, and temperature. The matrix size must match the
dimensions defined by the gate-source voltage, drain-source voltage, and temperature
vectors.

#### Dependencies

To enable this parameter, set **Number of terminals** to
`Four` and **Parameterization** to
`Lookup table (3-D, temperature dependent)`.

### **Ids-Vds parameterization** — Ids-Vds table data as symmetric data `Provide negative and positive Vds data` (default) | `Provide positive Vds data only`

Whether to provide Ids-Vds table data as symmetric data. If you choose
`Provide negative and positive Vds data`, the data is not
symmetric. If you choose `Provide positive Vds data only`, the block
rotates and flips the positive data to obtain the negative data.

#### Dependencies

To enable this parameter, set **Parameterization** to either
`Lookup table (2-D, temperature independent)` or
`Lookup table (3-D, temperature dependent)`.

### Main (Surface-Potential-Based Modeling Option)

This configuration of the **Main** setting corresponds to the
surface-potential-based block modeling option. If you are using the threshold-based modeling
option of the block, based on the Shichman and Hodges equations, see Main (Threshold-Based Modeling Option).

### **Number of terminals** — Terminal parameterization `Three` (default) | `Four`

Number of terminals of the block.

### **Gain** — MOSFET gain `18` `A/V 2` (default) | positive scalar

MOSFET gain, *β*. This parameter primarily defines the linear region of
operation on an
*ID*–*VDS*
characteristic.

### **Flatband voltage** — Flatband voltage `-1.1` `V` (default)

Flatband voltage, *VFB*, defines the gate bias
that must be applied in order to achieve the flatband condition at the surface of the
silicon. The default value is `-1.1` V. You can also use this parameter to
arbitrarily shift the threshold voltage due to material work function differences, and to
trapped interface or oxide charges. In practice, however, it is usually recommended to modify
the threshold voltage by using the **Body factor** and **Surface
potential at strong inversion** parameters first, and only use this parameter for
fine-tuning.

### **Body factor** — Body factor `3.5` `V1/2` (default)

Body factor, *γ*, in the surface-potential equation. This parameter
primarily impacts the threshold voltage.

### **Surface potential at strong inversion** — Surface potential at strong inversion `1` `V` (default)

2*ϕB* term in the surface-potential equation.
This parameter also primarily impacts the threshold voltage.

### **Velocity saturation factor** — Velocity saturation factor `0.4` `1/V` (default)

Velocity saturation, *θsat*, in the
drain-current equation. Use this parameter in cases where a good fit to linear operation
leads to a saturation current that is too high. By increasing this parameter value, you
reduce the saturation current. For high-voltage devices, it is often the case that a good fit
to linear operation leads to a saturation current that is too low. In such a case, either
increase both the gain and the drain ohmic resistance or use an N-Channel
LDMOS FET block instead.

### **Channel-length modulation factor** — Channel-length modulation factor `0` (default)

Factor, α, multiplying the logarithmic term in the
*GΔL* equation. This parameter describes the onset
of channel-length modulation. For device characteristics that exhibit a positive conductance
in saturation, increase the parameter value to fit this behavior. The default value is
`0`, which means that channel-length modulation is off by default.

### **Channel-length modulation voltage** — Channel-length modulation voltage `5e-2` `V` (default)

Voltage *Vp* in the
*GΔL* equation. This parameter controls the
drain-voltage at which channel-length modulation starts to become active

### **Surface roughness scattering factor** — Surface roughness scattering factor `0` `1/V` (default)

Strength of the mobility reduction. The mobility is *μ* =
*μ0*/*Gmob*, where *μ0* is the low-field
mobility without the effect of surface scattering. The mobility reduction factor,
*Gmob*, is given by Gmob=1+(θsrVeff)4, where *θsr* is the surface
roughness scattering factor and *Veff* is a voltage
that is indicative of the effective vertical electric field strength in the channel,
*Eeff*. For high vertical electric fields, the
mobility is roughly proportional to *Eeff*^2 for
electrons.

### **Linear-to-saturation transition coefficient** — Linear-to-saturation transition coefficient `8` (default)

Smoothness of the MOSFET transitions from linear into saturation, particularly when
velocity saturation is enabled. This parameter can usually be left at its default value, but
you can use it to fine-tune the knee of the
*ID*–*VDS*
characteristic. The expected range for this parameter value is between 2 and 8.

### **Measurement temperature** — Measurement temperature `25` `°C` (default)

Temperature *Tm1* at which the block parameters
are measured. If the **Device simulation temperature** parameter on the
**Temperature Dependence** setting differs from this value, then device
parameters will be scaled from their defined values according to the simulation and reference
temperatures. For more information, see Temperature Dependence (Surface-Potential-Based Modeling Option).

### Ohmic Resistance

If you set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`, to enable this setting set **Parameterization** to
`Specify from a datasheet` or `Specify using equation
parameters directly`.

### **Source ohmic resistance, Rs** — Transistor source resistance `0.0001` `Ohm` (default) | nonnegative scalar

Transistor source resistance, that is, the series resistance associated with the source
contact. The default value for threshold-based variants is `1e-4` Ohm. The
default value for surface-potential-based variants is `2e-3` Ohm.

### **Drain ohmic resistance, Rd** — Transistor drain resistance `0.01` `Ohm` (default) | nonnegative scalar

Transistor drain resistance, that is, the series resistance associated with the drain
contact. The value must be greater than or equal to `0`. The default value
for threshold-based variants is `0.01` Ohm. The default value for
surface-potential-based variants is `0.17` Ohm.

### **Gate ohmic resistance, Rg** — Transistor gate resistance `8.4` `Ohm` (default) | nonnegative scalar

Transistor gate resistance, that is, the series resistance associated with the gate
contact.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Surface-potential-based` or
`Surface-potential-based with thermal`.

### **Body ohmic resistance, Rb** — Transistor body resistance `0.001` `Ohm` (default) | nonnegative scalar

Transistor body resistance, that is, the series resistance associated with the body
contact.

#### Dependencies

To enable this parameter, set:

- **Number of terminals** to `Four`.
- **Modeling option** to
  `Threshold-based` or `Threshold-based
  with thermal`.

### **Bulk ohmic resistance** — Transistor bulk resistance `2e-3` `Ohm` (default) | nonnegative scalar

Transistor body resistance, that is, the series resistance associated with the bulk
contact.

#### Dependencies

To enable this parameter, set:

- **Number of terminals** to `Four`.
- **Modeling option** to
  `Surface-potential-based` or
  `Surface-potential-based with thermal`.

### Packaging

### **Source lead resistance** — Source lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Source lead resistance of the transistor, that is, the series lead resistance
associated with the source contact. Use this parameter to model parasitic effects in
the transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Drain lead resistance** — Drain lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Drain lead resistance of the transistor, that is, the series lead resistance
associated with the drain contact. Use this parameter to model parasitic effects in
the transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Gate lead resistance** — Gate lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Gate lead resistance of the transistor, that is, the series lead resistance
associated with the gate contact. Use this parameter to model parasitic effects in the
transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Body lead resistance** — Body lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Body lead resistance of the transistor, that is, the series lead resistance
associated with the body contact. Use this parameter to model parasitic effects in the
transistor.

#### Dependencies

To enable this parameter, set:

- **Number of terminals** to
  `Four`.
- **Modeling option** to
  `Threshold-based` or `Threshold-based
  with thermal`.

### **Source lead inductance** — Source lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Source lead inductance of the transistor, that is, the series lead inductance
associated with the source contact. Use this parameter to model parasitic effects in
the transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Drain lead inductance** — Drain lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Drain lead inductance of the transistor, that is, the series lead inductance
associated with the drain contact. Use this parameter to model parasitic effects in
the transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Gate lead inductance** — Gate lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Gate lead inductance of the transistor, that is, the series lead inductance
associated with the gate contact. Use this parameter to model parasitic effects in the
transistor.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Body lead inductance** — Body lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Body lead inductance of the transistor, that is, the series lead inductance
associated with the body contact. Use this parameter to model parasitic effects in the
transistor.

#### Dependencies

To enable this parameter, set:

- **Number of terminals** to
  `Four`.
- **Modeling option** to
  `Threshold-based` or `Threshold-based
  with thermal`.

### Capacitance

To enable this setting, set **Modeling option** to
`Threshold-based` or `Threshold-based with
thermal`.

### **Parameterization** — Capacitance parameterization `Specify fixed input, reverse transfer, and output capacitance` (default) | `Specify fixed gate-source, gate-drain, and drain-source capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-source, gate-drain, and drain-source capacitance`

Select one of the following methods for capacitance parameterization:

- `Specify fixed input, reverse transfer, and output
  capacitance` — Provide fixed parameter values from
  datasheet and let the block convert the input, output, and reverse transfer
  capacitance values to capacitance values, as described in Charge Model for Threshold-Based Modeling Option.
- `Specify fixed gate-source, gate-drain, and drain-source
  capacitance` — Provide fixed values for capacitance
  parameters directly.
- `Specify tabulated input, reverse transfer, and output
  capacitance` — Provide tabulated capacitance and
  drain-source voltage values based on datasheet plots. The block converts the
  input, output, and reverse transfer capacitance values to capacitance values, as
  described in Charge Model for Threshold-Based Modeling Option.
- `Specify tabulated gate-source, gate-drain, and drain-source
  capacitance` — Provide tabulated values for capacitances
  and drain-source voltage.

### **Input capacitance, Ciss** — Input gate-source capacitance `350` `pF` (default)

Gate-source capacitance with the drain shorted to the source.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed input, reverse
transfer, and output capacitance`.

### **Input capacitance, Ciss(Vds)** — Input gate-source capacitance with tabulated input `[720 700 590 470 390 310]` `pF` (default)

Gate-source capacitance with the drain shorted to the source, tabulated with
drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated input, reverse
transfer, and output capacitance`.

### **Reverse transfer capacitance, Crss** — Reverse transfer capacitance `80` `pF` (default)

Drain-gate capacitance with the source connected to ground, also known as the Miller
capacitance.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed input, reverse
transfer, and output capacitance`.

### **Reverse transfer capacitance, Crss(Vds)** — Reverse transfer capacitance with tabulated inputs `[450 400 300 190 95 55]` `pF` (default)

Drain-gate capacitance with the source connected to ground, also known as the Miller
capacitance, tabulated with drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated input, reverse
transfer, and output capacitance`.

### **Output capacitance, Coss** — Output capacitance `0` `pF` (default)

Drain-source capacitance with the gate and source shorted.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed input, reverse
transfer, and output capacitance`.

### **Output capacitance, Coss(Vds)** — Output capacitance with tabulated inputs `[900 810 690 420 270 170]` `pF` (default)

Drain-source capacitance with the gate and source shorted, tabulated with drain-source
voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated input, reverse
transfer, and output capacitance`.

### **Gate-source capacitance, Cgs** — Gate-source capacitance `270` `pF` (default)

Capacitance placed between the gate and the source.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed gate-source,
gate-drain, and drain-source capacitance`.

### **Gate-source capacitance, Cgs(Vgs, Vds)** — Gate-source capacitance with tabulated values `[270 300 290 280 295 255]` `pF` (default)

Capacitance placed between the gate and the source, tabulated with gate-source
voltage and drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`.

### **Gate-drain capacitance, Cgd** — Gate-drain capacitance `80` `pF` (default)

Capacitance placed between the gate and the drain.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed gate-source,
gate-drain, and drain-source capacitance`.

### **Gate-drain capacitance, Cgd(Vgs,Vds)** — Gate-drain capacitance with tabulated values `[450 400 300 190 95 55]` `pF` (default)

Capacitance placed between the gate and the drain, tabulated with gate-source
voltage and drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`.

### **Gate-bulk capacitance, Cgb** — Gate-bulk capacitance `0` `pF` (default)

Capacitance placed between the gate and the bulk.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed gate-source,
gate-drain, and drain-source capacitance` and **Gate-bulk and
gate-source charge-voltage linearity** to `Separate gate-bulk
and gate-source capacitance`.

### **Gate-bulk capacitance, Cgb(Vgs,Vds)** — Gate-bulk capacitance with tabulated values `[450 400 300 190 95 55]` `pF` (default)

Capacitance placed between the gate and the bulk, tabulated with gate-source
voltage and drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated
gate-source, gate-drain, and drain-source capacitance` and
**Gate-bulk and gate-source charge-voltage linearity** to
`Separate gate-bulk and gate-source capacitance`.

### **Corresponding gate-source voltages, Vgs** — Corresponding gate-source voltages `0` `V` (default)

Gate-source voltages corresponding to the tabulated capacitance values.

If this value is a scalar, then **Gate-source capacitance,
Cgs(Vgs,Vds)** and **Gate-drain capacitance,
Cgd(Vgs,Vds)** are vectors of scalars. If this value is a vector, then
**Gate-source capacitance, Cgs(Vgs,Vds)** and **Gate-drain
capacitance, Cgd(Vgs,Vds)** are matrices of scalars.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated gate-source,
gate-drain, and drain-source capacitance`.

### **Drain-source capacitance, Cds** — Drain-source capacitance `0` `pF` (default)

Capacitance placed between the drain and the source.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed gate-source,
gate-drain, and drain-source capacitance`.

### **Drain-source capacitance, Cds(vds)** — Drain-source capacitance with tabulated values `[450 410 390 230 175 115]` `pF` (default)

Capacitance placed between the drain and the source, tabulated with the
drain-source voltage.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`.

### **Corresponding drain-source voltages, Vds** — Corresponding drain-source voltages `[.1, .3, 1, 3, 10, 30]` `V` (default)

Drain-source voltages corresponding to the tabulated capacitance values.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated input, reverse
transfer, and output capacitance` or to `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`.

### **Gate-source voltage, Vgs, for tabulated capacitances** — Gate-source voltage for tabulated capacitances `0` `V` (default)

For tabulated capacitance models, this parameter controls the voltage dependence of the
**Reverse transfer capacitance, Crss** or the **Gate-drain
capacitance, Cgd** parameter (depending on the selected parameterization
option). These capacitances are a function of the drain-gate voltage. The block
calculates drain-gate voltages by subtracting this gate-source voltage value from the
values specified for the **Corresponding drain-source voltages**
parameter.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify tabulated input, reverse
transfer, and output capacitance`.

### **Gate-drain charge-voltage linearity** — Charge-voltage linearity `Gate-drain capacitance is constant` (default) | `Gate-drain charge function is nonlinear`

The two fixed capacitance options let you model gate capacitance as a fixed gate-source
capacitance *CGS* and either a fixed or a
nonlinear gate-drain capacitance *CGD*. Select
whether the gate-drain capacitance is fixed or nonlinear:

- `Gate-drain capacitance is constant` — The
  capacitance value is constant and defined according to the selected
  parameterization option, either directly or derived from a datasheet.
- `Gate-drain charge function is nonlinear` —
  The gate-drain charge relationship is defined according to the
  piecewise-nonlinear function described in Charge Model for Threshold-Based Modeling Option. Two additional parameters appear to let you define the
  gate-drain charge function.

#### Dependencies

To enable this parameter, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed input, reverse transfer
and output capacitance` or to `Specify fixed gate-source,
gate-drain and drain-source capacitance`.

### **Gate-drain oxide capacitance** — Gate-drain oxide capacitance `200` `pF` (default)

Gate-drain capacitance when the drain-gate voltage is less than the **Drain-gate
voltage at which oxide capacitance becomes active** parameter value.

#### Dependencies

To enable this parameter, set **Gate-drain charge-voltage linearity**
to `Gate-drain charge function is nonlinear`.

### **Drain-gate voltage at which oxide capacitance becomes active** — Drain-gate voltage at which oxide capacitance becomes active `-0.5` `V` (default)

Drain-gate voltage at which the drain-gate capacitance switches between off-state
(*CGD*) and on-state
(*Cox*) capacitance values.

#### Dependencies

To enable this parameter, set **Gate-drain charge-voltage linearity**
to `Gate-drain charge function is nonlinear`.

### **Gate-bulk and gate-source charge-voltage linearity** — Gate-bulk and gate-source charge-voltage linearity `Gate-bulk and gate-source capacitance change instantly` (default) | `Gate-bulk and gate-source capacitance change gradually` | `Separate gate-bulk and gate-source capacitance`

Gate-bulk and gate-source charge-voltage linearity.

#### Dependencies

To enable this parameter, in the **Main** setting, set
**Number of terminals** to `Four`.

To enable the `Separate gate-bulk and gate-source capacitance`
option, in the **Capacitance** setting, set
**Parameterization** to `Specify fixed gate-source,
gate-drain, and drain-source capacitance` or `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`

### Channel Capacitances

To enable this setting, set **Modeling option** to
`Surface-potential-based` or `Surface-potential-based with
thermal`.

### **Oxide capacitance** — Oxide capacitance `1500` `pF` (default)

The parallel plate gate-channel capacitance.

### **Gate-source overlap capacitance** — Gate-source overlap capacitance `100` `pF` (default)

The fixed, linear capacitance associated with the overlap of the gate electrode with the
source well.

### **Gate-drain overlap capacitance** — Gate-drain overlap capacitance `14` `pF` (default)

The fixed, linear capacitance associated with the overlap of the gate electrode with the
drain well.

### Body Diode

### **Model body diode** — Body diode modeling option `No` (default) | `Exponential` | `Tabulated I-V curve`

Whether to model the body diode.

### **Table type** — Tabulated function `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

Whether to tabulate the current as a function of temperature and voltage or the voltage
as a function of temperature and current.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Tabulated I-V curve`.

### **Reverse saturation current, Is** — Reverse saturation current `0` `A` (default)

The current designated by the *Is* symbol in the
body-diode equations. The default value for threshold-based modeling option is
`0` A. The default value for surface-potential-based modeling
option is `5.2e-13` A.

To enable conduction through the body diode, for applications where the MOSFET current
changes sign during the simulation, such as when the MOSFET is driving an inductive load, set
this parameter to a non-zero value.

For applications where the MOSFET current never changes sign, such as in a small-signal
amplifier, set this parameter to 0 to improve simulation speed.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential`.

### **Built-in voltage, Vbi** — Built-in voltage `0.6` `V` (default)

The built-in voltage of the diode, designated by the
*Vbi* symbol in the body-diode equations. Built-in
voltage has an impact only on the junction capacitance equation. It does not affect the
conduction current.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential`.

### **Ideality factor, n** — Ideality factor `1` (default)

The factor designated by the *n* symbol in the body-diode
equations.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential`.

### **Zero-bias junction capacitance, Cj0** — Zero-bias junction capacitance `0` `pF` (default)

The capacitance between the drain and bulk contacts at zero-bias due to the body diode
alone. It is designated by the *Cj0* symbol in
the body-diode equations. The default value for threshold-based modeling option is
`0` pF. The default value for surface-potential-based modeling
option is `480` pF.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential`.

### **Transit time, TT** — Transit time `50e-9` `s` (default)

The time designated by the *τ* symbol in the body-diode
equations.

When the **Reverse saturation current** and **Transit
time** parameters are both non-zero, this block includes the reverse recovery
inside the body diode model.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential`.

### **Measurement temperature** — Measurement temperature `25` `°C` (default)

Temperature at which the block parameters are measured.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Exponential` and, in the **Main** setting, set
**Parameterization** to either `Lookup table (2-D, temperature
independent)` or `Lookup table (3-D, temperature
dependent)`

### **Diode forward voltages, Vf(If)** — Diode forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V` (default)

Tabulated values of the minimum voltage that needs to be applied for the diode to become
forward-biased.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Specify from a datasheet`, `Specify from
  equation parameters directly`, or `Lookup table (2-D,
  temperature independent)`.
- In the **Body diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.

    **Table type** to `Table in Vf(If)
    form`.

### **Diode forward currents, If** — Diode forward currents temperature independent `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

Tabulated values of the forward currents.

#### Dependencies

To enable this parameter, in the **Body diode** setting, set
**Model body diode** to `Tabulated I-V curve` and
**Table type** to `Table in Vf(If) form` or
`Table in Vf(Tj,If) form`.

### **Diode forward currents, If(Vf)** — Diode forward currents tabulated with forward voltages `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A` (default)

Tabulated values of the forward current, as a function of the forward voltages.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Specify from a datasheet`, `Specify from
  equation parameters directly`, or `Lookup table (2-D,
  temperature independent)`.
- In the **Body diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.

    **Table type** to `Table in If(Vf)
    form`.

### **Diode forward voltages, Vf** — Diode forward voltages temperature independent `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

Tabulated values of the forward voltages.

#### Dependencies

To enable this parameter, in the **Body diode** setting, set
**Model body diode** to `Tabulated I-V curve` and
**Table type** to `Table in If(Vf) form` or
`Table in If(Tj,Vf) form`.

### **Diode junction temperatures, Tj** — Diode junction temperatures `[25, 125]` `degC` (default)

Vector of junction temperatures.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Tabulated I-V curve` and, in the **Main**
setting, set **Parameterization** to `Lookup table (3-D,
temperature dependent)`.

### **Diode forward currents, If(Tj,Vf)** — Diode forward currents temperature dependent `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default)

Tabulated values of the forward current, as a function of the forward voltages and
junction temperatures.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Lookup table (3-D, temperature dependent)`.
- In the **Body diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.

    **Table type** to `Table in If(Tj,Vf)
    form`.

### **Diode forward voltages, If(Tj,Vf)** — Diode forward voltages temperature dependent `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default)

Tabulated values of the forward voltage, as a function of the forward currents and
junction temperatures.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Lookup table (3-D, temperature dependent)`.
- In the **Body diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.

    **Table type** to `Table in Vf(Tj,If)
    form`.

### **Diode off conductance** — Conductance of diode when reverse biased `1e-12` `1/Ohm` (default) | positive scalar

*Since R2024a*

Conductance of the diode when it is reverse biased.

#### Dependencies

To enable this parameter, set **Model body diode** to
`Tabulated I-V curve`.

### Temperature Dependence (Threshold-Based Modeling Option)

This configuration of the **Temperature Dependence** setting corresponds
to the threshold-based block modeling option, which is the default. If you are using the
surface-potential-based modeling option of the block, see Temperature Dependence (Surface-Potential-Based Modeling Option)

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter measurement
  temperature` — Temperature dependence is not modeled. This
  is the default method.
- `Model temperature dependence` — Model
  temperature-dependent effects. Provide a value for simulation temperature,
  *Ts*, a value for
  *BEX*, and a value for the measurement temperature
  *Tm1* (using the
  **Measurement temperature** parameter on the
  **Main** setting). You also have to provide a value for
  *α* using one of two methods, depending on the value of the
  **Parameterization** parameter on the
  **Main** setting. If you parameterize the block from a
  datasheet, you have to provide *RDS(on)*
  at a second measurement temperature, and the block will calculate
  *α* based on that. If you parameterize by specifying equation
  parameters, you have to provide the value for *α*
  directly.

### **Drain-source on resistance, R\_DS(on), at second measurement temperature** — Drain-source on resistance at second measurement temperature `0.037` `Ohm` (default)

The ratio of the drain-source voltage to the drain current for specified values of drain
current and gate-source voltage at second measurement temperature. It must be quoted for the
same working point (drain current and gate-source voltage) as the **Drain-source on
resistance, R\_DS(on)** parameter on the **Main** setting.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter on the
**Main** setting.

### **Second measurement temperature** — Second temperature `125` `°C` (default)

Second temperature *Tm2* at which
**Drain-source on resistance, R\_DS(on), at second measurement temperature**
is measured.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter on the
**Main** setting.

### **Gate threshold voltage temperature coefficient, dVth/dT** — Gate-source voltage, Vgs `-6` `mV/K` (default)

The rate of change of gate threshold voltage with temperature.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization**
parameter on the **Main** setting.

### **Mobility temperature exponent, BEX** — Mobility temperature exponent `-1.5` (default)

Mobility temperature coefficient value. You can use the default value for most MOSFETs.
See the Assumptions and Limitations section for additional considerations.

### **Body diode reverse saturation current temperature exponent** — Body diode reverse saturation current temperature exponent `3` (default)

The reverse saturation current for the body diode is assumed to be proportional to the
square of the intrinsic carrier concentration, *ni* =
*NC*
exp(–*EG*/2*kB**T*). *NC* is the temperature-dependent
effective density of states and *EG* is the
temperature-dependent bandgap for the semiconductor material. To avoid introducing another
temperature-scaling parameter, the block neglects the temperature dependence of the bandgap
and uses the bandgap of silicon at 300K (1.12eV) for all device types. Therefore, the
temperature-scaled reverse saturation current is given by

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* is the value of the **Reverse
saturation current** parameter from the **Body Diode** setting,
*kB* is Boltzmann’s constant
(8.617x10-5eV/K), and
*ηIs* is the **Body diode reverse saturation
current temperature exponent**. The default value is `3`, because
*NC* for silicon is roughly proportional to
*T3/2*. You can remedy the effect of neglecting
the temperature-dependence of the bandgap by a pragmatic choice of
*ηIs*.

### **Device simulation temperature** — Device simulation temperature `25` `°C` (default)

Temperature *Ts* at which the device is
simulated.

### Temperature Dependence (Surface-Potential-Based Modeling Option)

This configuration of the **Temperature Dependence** setting corresponds
to the surface-potential-based block modeling option. If you are using the threshold-based
modeling option of the block, see Temperature Dependence (Threshold-Based Modeling Option)

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter measurement
  temperature` — Temperature dependence is not modeled.
- `Model temperature dependence` — Model
  temperature-dependent effects. Provide a value for the device simulation temperature,
  *Ts*, and the temperature-scaling coefficients
  for other block parameters.

### **Gain temperature exponent** — Gain temperature exponent `1.3` (default)

The MOSFET gain, *β*, is assumed to scale exponentially with
temperature, *β* = *β*
m1(*Tm1*/*Ts*)^*ηβ*. *βm1* is the value of the
**Gain** parameter from the **Main** setting and
*ηβ* is the **Gain temperature
exponent**.

### **Flatband voltage temperature coefficient** — Flatband voltage temperature coefficient `5e-4` `V/K` (default)

The flatband voltage, *V*FB, is assumed to scale
linearly with temperature, *V*FB =
*VFBm1* +
(*Ts* –
*Tm1*)*ST,VFB*. *VFBm1* is the value of the
**Flatband voltage** parameter from the **Main** setting
and *ST,VFB* is the
**Flatband voltage temperature coefficient**.

### **Surface potential at strong inversion temperature coefficient** — Surface potential at strong inversion temperature coefficient `-8.5e-4` `V/K` (default)

The surface potential at strong inversion,
2*ϕB*, is assumed to scale linearly with temperature, *2ϕB* =
2*ϕBm1* +
(*Ts* –
*Tm1*)*ST,ϕB*. 2*ϕBm1* is the value of the
**Surface potential at strong inversion** parameter from the
**Main** setting and
*ST,ϕB* is the
**Surface potential at strong inversion temperature coefficient**.

### **Velocity saturation temperature exponent** — Velocity saturation temperature exponent `1.04` (default)

The velocity saturation, *θsat*, is assumed to
scale exponentially with temperature, *θsat* =
*θsat,m1*
(*Tm1*/*Ts*)^*ηθ*. *θsat,m1* is the value of the
**Velocity saturation factor** parameter from the **Main**
setting and *ηθ* is the **Velocity saturation
temperature exponent**.

### **Surface roughness scattering temperature exponent** — Surface roughness scattering temperature exponent `0.65` (default)

This parameter leads to a temperature-dependent reduction in the MOSFET transconductance
at high gate voltage. The surface roughness scattering,
*θsr*, is assumed to scale exponentially with
temperature, *θsr* =
*θsr,m1*
(*Tm1*/*Ts*)^*ηsr*. *θsr,m1* is the value of the
**Surface roughness scattering factor** parameter from the
**Main** setting and *ηsr* is the
**Surface roughness scattering temperature exponent**.

### **Resistance temperature exponent** — Resistance temperature exponent `0.95` (default)

The series resistances are assumed to correspond to semiconductor resistances.
Therefore, they decrease exponentially with increasing temperature. *Ri* =
*Ri,m1*
(*Tm1*/*Ts*)^*ηR*, where *i* is S, D, or G, for the source, drain, or gate
series resistance, respectively. *Ri,m1* is the value
of the corresponding series resistance parameter from the **Ohmic
Resistance** setting and *ηR* is the
**Resistance temperature exponent**.

### **Body diode reverse saturation current temperature exponent** — Body diode reverse saturation current temperature exponent `3` (default)

The reverse saturation current for the body diode is assumed to be proportional to the
square of the intrinsic carrier concentration, *ni* =
*NC*
exp(–*EG*/2*kB**T*). *NC* is the temperature-dependent
effective density of states and *EG* is the
temperature-dependent bandgap for the semiconductor material. To avoid introducing another
temperature-scaling parameter, the block neglects the temperature dependence of the bandgap
and uses the bandgap of silicon at 300K (1.12eV) for all device types. Therefore, the
temperature-scaled reverse saturation current is given by

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* is the value of the **Reverse
saturation current** parameter from the **Body Diode** setting,
*kB* is Boltzmann’s constant
(8.617x10-5eV/K), and
*ηIs* is the **Body diode reverse saturation
current temperature exponent**. The default value is `3`, because
*N*C for silicon is roughly proportional to
*T3/2*. You can remedy the effect of neglecting
the temperature-dependence of the bandgap by a pragmatic choice of
*ηIs*.

### **Device simulation temperature** — Device simulation temperature `25` `°C` (default)

Temperature *Ts* at which the device is
simulate.

### Faults

The fault interface includes the **Fault Inspector** window
and the **Faults** section of the **Blocks** tab for blocks that support faults. You define what triggers the fault
and how the fault behaves when that trigger occurs. When you create and edit the fault, you
parameterize the fault behavior.

To add a fault, click the **Add fault**
hyperlink.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **NMOS fault** — Option to add fault `Add fault` (default)

Option to add a fault in the N-Channel MOSFET block.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible gate-source voltage** — Gate-source voltage threshold to fault transition `inf` `V` (default) | positive scalar

Maximum permissible gate-source voltage value, above which a fault might be
triggered.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible drain-source voltage** — Drain-source voltage threshold to fault transition `inf` `V` (default) | positive scalar

Maximum permissible drain-source voltage value, above which a fault might be
triggered.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible drain-bulk voltage** — Drain-bulk voltage threshold to fault transition `inf` `V` (default) | positive scalar

Maximum permissible drain-bulk voltage value, above which a fault might be
triggered.

#### Dependencies

To enable this parameter:

- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.
- In the **Main** setting, set **Number of
  terminals** to `Four`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Maximum permissible drain-source current** — Current threshold to fault transition `inf` `A` (default) | positive scalar

Maximum permissible drain-source current value. If the current exceeds this value for
longer than the value of the **Time to fail when exceeding drain-source
current** parameter, then the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding drain-source current** — Time to fail when exceeding drain-source current `1` `s` (default) | positive scalar

Amount of time that the drain-source current must continuously exceed the maximum
permissible drain-source current before a behavioral fault is triggered.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible body diode current** — Body diode current threshold to fault transition `inf` `A` (default) | positive scalar

Maximum permissible body diode current value. If the current exceeds this value
for longer than the value of the **Time to fail when exceeding body diode
current** parameter, then the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Set **Model body diode** to either
  `Exponential` or `Tabulated I-V
  curve`.
- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Time to fail when exceeding body diode current** — Time to fail when exceeding body diode current `1` `s` (default) | positive scalar

Amount of time that the body diode current must continuously exceed the maximum
permissible body diode current before a behavioral fault is triggered.

#### Dependencies

To enable this parameter:

- Set **Model body diode** to either
  `Exponential` or `Tabulated I-V
  curve`.
- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Maximum diode recovery, dV/dt** — Maximum diode recovery `inf` `V/s` (default) | positive scalar

Maximum amount of diode recovery per second.

#### Dependencies

To enable this parameter:

- Set **Model body diode** to either
  `Exponential` or `Tabulated I-V
  curve`.
- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Maximum permissible temperature** — Temperature threshold to fault transition `inf` `K` (default) | positive scalar

Maximum permissible temperature value. If the temperature exceeds this value for
longer than the value of the **Time to fail when exceeding
temperature** parameter, then the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Set **Modeling option** to `Threshold-based
  with thermal`.
- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Time to fail when exceeding temperature** — Time to fail when exceeding temperature `1` `s` (default) | positive scalar

Amount of time that the temperature must continuously exceed the maximum
permissible temperature before a behavioral fault is triggered.

#### Dependencies

To enable this parameter:

- Set **Modeling option** to `Threshold-based
  with thermal`.
- In the **Fault Inspector** window, set **Trigger Type** to
  `Behavioral`.

This parameter appears in the **Trigger**
section of the **Fault Inspector** window. For more information, see Set Fault Triggers.

### **Fault transition time constant, tau** — Fault transition time constant `1e-3` `s` (default)

Time constant for transitioning to faulted state.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter.

### **Failure mode** — Failure category `Open circuit` (default) | `Drain-source short` | `Drain-bulk short or source-bulk short` | `Gate oxide short` | `Parameter shift`

Type of failure. You can set this parameter to:

- `Open circuit` — Failure due to metallization
  burnout.
- `Drain-source short` — Failure due to avalanche
  breakout on drain-source channel.
- `Drain-bulk short or source-bulk short` — Failure due
  to avalanche breakout on drain-bulk or source-bulk channels.
- `Gate oxide short` — Failure of the gate oxide
  dielectric layer.
- `Parameter shift` — Failure due to aging.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter.

To enable the `Drain-source short` option, in the
**Main** setting, set **Number of terminals** to
`Three`.

To enable the `Drain-bulk short or source-bulk short`
option, in the **Main** setting, set **Number of
terminals** to `Four`.

### **Faulted series gate resistance, Rg** — Faulted series gate resistance `1e6` `Ohm` (default)

Series gate resistance in faulted state.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Open
circuit`.

### **Faulted series drain resistance, Rd** — Faulted series drain resistance `1000` `Ohm` (default)

Series drain resistance in faulted state.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Open
circuit`.

### **Faulted series source resistance, Rs** — Faulted series source resistance `1000` `Ohm` (default)

Series source resistance in faulted state.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Open
circuit`.

### **Faulted series bulk resistance, Rb** — Faulted series source resistance `1000` `Ohm` (default)

Series source resistance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Open
  circuit`.

### **Faulted parallel drain-source conductance, Gds** — Faulted parallel drain-source conductance `1000` `1/Ohm` (default)

Parallel drain-source conductance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Three`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Drain-source
  short`.

### **Faulted parallel drain-bulk conductance, Gdb** — Faulted parallel drain-bulk conductance `1000` `1/Ohm` (default)

Parallel drain-bulk conductance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Drain-bulk short or
  source-bulk short`.

### **Faulted parallel source-bulk conductance, Gsb** — Faulted parallel source-bulk conductance `1000` `1/Ohm` (default)

Parallel source-bulk conductance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Drain-bulk short or
  source-bulk short`.

### **Location of fault node (percentage of total channel length from source)** — Fault node location `0` (default)

Location of the fault node, as a percentage of the total channel length from the
source.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Gate oxide
short`.

### **Gate oxide short conductance, G** — Gate oxide short conductance `1000` `1/Ohm` (default)

Gate oxide short conductance.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Gate oxide
short`.

### **Model gate oxide short diode** — Model option for gate oxide short diode `No` (default) | `Yes`

Whether to model the gate oxide short diode.

#### Dependencies

To enable this parameter, add a fault to the N-Channel MOSFET block by clicking the
**Add fault** hyperlink in the **NMOS fault**
parameter and set **Failure mode** to `Gate oxide
short`.

### **Gate oxide short diode reverse saturation current, Is** — Reverse saturation current of gate oxide short diode `0` `A` (default)

Reverse saturation current of the gate oxide short diode.

#### Dependencies

To enable this parameter:

- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Gate oxide
  short`.
- Set **Model gate oxide short diode** to
  `Yes`.

### **Gate oxide short diode built-in voltage, Vbi** — Built-in voltage of gate oxide short diode `0.6` `V` (default)

Built-in voltage of the gate oxide short diode.

#### Dependencies

To enable this parameter:

- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Gate oxide
  short`.
- Set **Model gate oxide short diode** to
  `Yes`.

### **Gate oxide short diode ideality factor, n** — Ideality factor of gate oxide short diode `1` (default)

Ideality factor of the gate oxide short diode.

#### Dependencies

To enable this parameter:

- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Gate oxide
  short`.
- Set **Model gate oxide short diode** to
  `Yes`.

### **Gate oxide short diode zero-bias junction capacitance, Cj0** — Zero-bias junction capacitance of gate oxide short diode `0` `pF` (default)

Zero-bias junction capacitance of the gate oxide short diode.

#### Dependencies

To enable this parameter:

- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Gate oxide
  short`.
- Set **Model gate oxide short diode** to
  `Yes`.

### **Gate oxide short diode transit time, TT** — Transit time of gate oxide short diode `50e-9` `s` (default)

Transit time of the gate oxide short diode.

#### Dependencies

To enable this parameter:

- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Gate oxide
  short`.
- Set **Model gate oxide short diode** to
  `Yes`.

### **Shifted gain as percentage of unshifted** — Shifted gain as percentage of unshifted `100` (default)

Shifted gain as percentage of unshifted.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Threshold voltage shift value, dVth** — Threshold voltage shift value `0` `V` (default)

Shift value of threshold voltage.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted channel modulation, L** — Faulted channel modulation `0` `1/V` (default)

Channel modulation in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Shifted body factor as percentage of unshifted** — Shifted body factor as percentage of unshifted `100` (default)

Shifted body factor as percentage of unshifted.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Surface potential shift value, dPhib** — Surface potential shift value `0` `V` (default)

Shift value of surface potential.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted source ohmic resistance, Rs** — Faulted source ohmic resistance `0.0001` `Ohm` (default)

Transistor source resistance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted drain ohmic resistance, Rd** — Faulted drain ohmic resistance `0.01` `Ohm` (default)

Transistor drain resistance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted body ohmic resistance, Rb** — Faulted body ohmic resistance `0.001` `Ohm` (default)

Transistor body resistance in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Specify from a
  datasheet` or `Specify using equation parameters
  directly`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted vector of gate-source voltages, Vgs** — Faulted vector of gate-source voltages `[-.5, 2, 3, 4, 5]` `V` (default)

Gate-source voltages in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)` or `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted vector of drain-source voltages, Vds** — Faulted vector of drain-source voltages `[0, 2, 4, 8, 12, 16, 20]` `V` (default)

Drain-source voltages in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)` or `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted vector of bulk-source voltages, Vbs** — Faulted vector of bulk-source voltages `[0, -4, -6, -12]` `V` (default)

Bulk-source voltages in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)` or `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated gate-source threshold voltage, Vth(Vbs)** — Faulted tabulated gate-source threshold voltage `[.4, 1.2, 1.4, 1.45]` `V` (default)

Tabulated gate-source threshold voltage in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated gate-source threshold voltage, Vth(Vbs,T)** — Faulted tabulated gate-source threshold voltage dependent on temperature `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V` (default)

Gate-source threshold voltage in faulted state, tabulated on bulk-source voltage and
temperature.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated drain-source currents, Ids(Vgs,Vds)** — Faulted tabulated drain-source currents `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (default)

Tabulated drain-source currents in faulted state.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Three`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated drain-source currents, Ids(Vgs,Vds,T)** — Faulted tabulated drain-source currents, dependent on temperature `zeros(5, 7, 2)` `A` (default)

Drain-source currents in faulted state, tabulated on gate-source voltage, drain-source
voltage, and temperature.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Three`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated drain-source currents at zero bulk-source voltage, Ids(Vgs,Vds)** — Faulted tabulated drain-source currents at zero bulk-source voltage `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (default)

Tabulated drain-source currents in faulted state, when the bulk-source voltage is
zero.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (2-D,
  temperature independent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted tabulated drain-source currents at zero bulk-source voltage, Ids(Vgs,Vds,T)** — Faulted tabulated drain-source currents at zero bulk-source voltage, dependent on temperature `zeros(5, 7, 2)` `A` (default)

Tabulated drain-source currents in faulted state, when the bulk-source voltage is zero,
tabulated on gate-source voltage, drain-source voltage, and temperature.

#### Dependencies

To enable this parameter:

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Main** setting, set
  **Parameterization** to `Lookup table (3-D,
  temperature dependent)`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted gate-source capacitance as percentage of unfaulted** — Faulted gate-source capacitance as percentage of unfaulted `100` (default)

Gate-source capacitance in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter, meet one of these sets of conditions:

**Condition Set One**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify fixed input,
  reverse transfer, and output capacitance` or
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.

**Condition Set Two**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance` or `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Open
  circuit`, `Drain-source short`,
  `Drain-bulk short or source-bulk short`, or
  `Gate oxide short`.

### **Faulted gate-drain capacitance as percentage of unfaulted** — Faulted gate-drain capacitance as percentage of unfaulted `100` (default)

Gate-drain capacitance in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter, meet one of these sets of conditions:

**Condition Set One**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify fixed input,
  reverse transfer, and output capacitance` or
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.

**Condition Set Two**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance` or `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Open
  circuit`, `Drain-source short`,
  `Drain-bulk short or source-bulk short`, or
  `Gate oxide short`.

### **Faulted gate-bulk capacitance as percentage of unfaulted** — Faulted gate-bulk capacitance as percentage of unfaulted `100` (default)

Gate-bulk capacitance in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter, meet one of these sets of conditions:

**Condition Set One**

- In the **Main** setting, **Number of terminals**
  to `Four`.
- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify fixed gate-source,
    gate-drain, and drain-source capacitance`.
  - **Gate-bulk and gate-source charge-voltage linearity** to
    `Separate gate-bulk and gate-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.

**Condition Set Two**

- In the **Main** setting, **Number of terminals**
  to `Four`.
- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify tabulated
    gate-source, gate-drain, and drain-source capacitance`.
  - **Gate-bulk and gate-source charge-voltage linearity** to
    `Separate gate-bulk and gate-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Open
  circuit`, `Drain-bulk short or source-bulk
  short`, or `Gate oxide short`.

### **Faulted drain-source capacitance as percentage of unfaulted** — Faulted drain-source capacitance as percentage of unfaulted `100` (default)

Drain-source capacitance in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter, meet one of these sets of conditions:

**Condition Set One**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify fixed input,
  reverse transfer, and output capacitance` or
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.

**Condition Set Two**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance` or `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Open
  circuit`, `Drain-source short`,
  `Drain-bulk short or source-bulk short`, or
  `Gate oxide short`.

### **Faulted gate-drain oxide capacitance as percentage of unfaulted** — Faulted gate-drain oxide capacitance as percentage of unfaulted `100` (default)

Gate-drain oxide capacitance in faulted state as percentage of unfaulted.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify fixed input,
    reverse transfer, and output capacitance` or `Specify fixed
    gate-source, gate-drain, and drain-source capacitance`.
  - **Gate-drain charge-voltage linearity** to
    `Gate-drain charge function is non linear`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted drain-gate voltage at which oxide capacitance becomes active** — Faulted drain-gate voltage at which oxide capacitance becomes active `-0.5` `V` (default)

Drain-gate voltage in faulted state at which oxide capacitance becomes active.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify fixed input,
    reverse transfer, and output capacitance` or `Specify fixed
    gate-source, gate-drain, and drain-source capacitance`.
  - **Gate-drain charge-voltage linearity** to
    `Gate-drain charge function is non linear`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted input capacitance, Ciss(Vds)** — Faulted input capacitance `[720, 700, 590, 470, 390, 310]` `pF` (default)

Input capacitance in faulted state.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted reverse transfer capacitance, Crss(Vds)** — Faulted reverse transfer capacitance `[450, 400, 300, 190, 95, 55]` `pF` (default)

Reverse transfer capacitance in faulted state.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted output capacitance, Coss(Vds)** — Faulted output capacitance `[900, 810, 690, 420, 270, 170]` `pF` (default)

Output capacitance in faulted state.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted corresponding drain-source voltages, Vds** — Faulted corresponding drain-source voltages `[.1, .3, 1, 3, 10, 30]` `V` (default)

Corresponding drain-source voltages in faulted state.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance` or `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted gate-source voltages, Vgs, for tabulated capacitances** — Faulted gate-source voltages for tabulated capacitances `0` `V` (default)

Gate-source voltages for tabulated capacitances, in faulted state.

#### Dependencies

To enable this parameter, meet one of these sets of conditions:

**Condition Set One**

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated input, reverse
  transfer, and output capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

**Condition Set Two**

- In the **Main** setting, **Number of terminals**
  to `Four`.
- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify tabulated
    gate-source, gate-drain, and drain-source capacitance`.
  - **Gate-bulk and gate-source charge-voltage linearity** to
    `Gate-bulk and gate-source capacitance change instantly` or
    `Gate-bulk and gate-source capacitance change
    gradually`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted gate-source capacitance, Cgs(Vgs,Vds)** — Faulted gate-source capacitance `[270, 300, 290, 280, 295, 255]` `pF` (default)

Gate-source capacitance in faulted state, tabulated with gate-source voltage and
drain-source voltage.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted gate-drain capacitance, Cgd(Vgs,Vds)** — Faulted gate-source capacitance `[450, 400, 300, 190, 95, 55]` `pF` (default)

Gate-drain capacitance in faulted state, tabulated with gate-source voltage and
drain-source voltage.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set
  **Parameterization** to `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted gate-bulk capacitance, Cgb(Vgs,Vds)** — Faulted gate-source capacitance `[270, 300, 290, 280, 295, 255]` `pF` (default)

Gate-bulk capacitance in faulted state, tabulated with gate-source voltage and
drain-source voltage.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Number of
  terminals** to `Four`.
- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify
    tabulated gate-source, gate-drain, and drain-source
    capacitance`.
  - **Gate-bulk and gate-source charge-voltage
    linearity** to `Separate gate-bulk and
    gate-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted corresponding gate-source voltages, Vgs** — Faulted corresponding gate-source voltages `0` `V` (default)

Corresponding gate-source voltages in faulted state.

#### Dependencies

To enable this parameter,

- In the **Capacitance** setting, set:

  - **Parameterization** to `Specify tabulated
    gate-source, gate-drain, and drain-source capacitance`.
  - **Gate-bulk and gate-source charge-voltage linearity** to
    `Separate gate-bulk and gate-source capacitance`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode reverse saturation current, Is** — Faulted diode reverse saturation current `0` `A` (default)

Reverse saturation current of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Exponential`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode built-in voltage, Vbi** — Faulted diode built-in voltage `0.6` `V` (default)

Built-in voltage of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Exponential`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode ideality factor, n** — Faulted diode ideality factor `1` (default)

Ideality factor of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Exponential`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode zero-bias junction capacitance as percentage of unfaulted** — Faulted diode zero-bias junction capacitance as percentage of unfaulted `100` (default)

Faulted diode zero-bias junction capacitance as percentage of unfaulted.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Exponential`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode transit time, TT** — Faulted diode transit time `50e-9` `s` (default)

Transit time of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Exponential`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward currents, If(Vf)** — Faulted diode forward currents `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A` (default)

Forward currents of the diode in faulted state, tabulated with the forward
voltages.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Specify from a datasheet`, `Specify using
  equation parameters directly`, or `Lookup table (2-D,
  temperature independent)`.
- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in If(Vf)
    form`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward voltages, Vf** — Faulted diode forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

Forward voltages of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in If(Vf)
    form` or `Table in If(Tj,Vf) form`
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward voltages, Vf(If)** — Faulted diode forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V` (default)

Forward voltages of the diode in faulted state, tabulated with the forward
currents.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Specify from a datasheet`, `Specify using
  equation parameters directly`, or `Lookup table (2-D,
  temperature independent)`.
- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in Vf(If)
    form`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward currents, If** — Faulted diode forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

Forward currents of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in Vf(If)
    form` and `Table in Vf(Tj,If) form`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward currents, If(Tj,Vf)** — Faulted diode forward currents with tabulated inputs `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default)

Forward currents of the diode in faulted state, tabulated with the forward voltages and
junction temperatures.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Lookup table (3-D, temperature dependent)`.
- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in If(Tj,Vf)
    form`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode forward voltages, Vf(Tj,If)** — Faulted diode forward voltages with tabulated inputs `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default)

Forward voltages of the diode in faulted state, tabulated with the forward currents and
junction temperatures.

#### Dependencies

To enable this parameter,

- In the **Main** setting, set **Parameterization**
  to `Lookup table (3-D, temperature dependent)`.
- In the **Body Diode** setting, set:

  - **Model body diode** to `Tabulated I-V
    curve`.
  - **Table type** to `Table in Vf(Tj,If)
    form`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

### **Faulted diode off conductance** — Faulted diode off conductance `1e-12` `1/Ohm` (default)

*Since R2024a*

Off conductance of the diode in faulted state.

#### Dependencies

To enable this parameter,

- In the **Body Diode** setting, set **Model body
  diode** to `Tabulated I-V curve`.
- Add a fault to the N-Channel MOSFET block by clicking the **Add
  fault** hyperlink in the **NMOS fault**
  parameter.
- Set **Failure mode** to `Parameter
  shift`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2024b: Model the parasitic lead resistances and inductances in each transistor terminal

You can now model parasitic effects in each terminal of the N-Channel MOSFET block by
specifying lead resistances and inductances using these parameters:

- **Source lead resistance**
- **Drain lead resistance**
- **Gate lead resistance**
- **Body lead resistance**
- **Source lead inductance**
- **Drain lead inductance**
- **Gate lead inductance**
- **Body lead inductance**

### R2024a: Specify the off conductance value of the tabulated diode

You can now specify the value of the off conductance of the tabulated diode by using the
**Diode off conductance** parameter.

Before R2024a, to specify the off conductance of the tabulated diode, you must connect
an Environment Parameters block to the electrical network. Then, set the minimum conductance
of the N-Channel MOSFET block and other SPICE-compatible blocks by setting the **GMIN** parameter of the Environment Parameters block.

## Description

N-Channel metal-oxide-semiconductor field-effect transistor using either Shichman-Hodges equation or surface-potential-based model

The N-Channel MOSFET block provides two main modeling
options:

- Based on threshold voltage — Uses the Shichman-Hodges equation to represent the
  device. This modeling approach, based on threshold voltage, has the benefits of simple
  parameterization and simple current-voltage expressions. However, these models have difficulty
  in accurately capturing transitions across the threshold voltage and lack some important
  effects, such as velocity saturation. For details, see Threshold-Based Model.

  This modeling option provides four ways of parameterizing an N-Channel MOSFET:

  - By specifying parameters from a datasheet.
  - By specifying equation parameters directly.
  - By a 2-D lookup table approximation to the I-V (current-voltage) curve. For details, see
    Representation by 2-D Lookup Table.
  - By a 3-D lookup table approximation to the I-V (current-voltage) curve that includes
    temperature data. For details, see Representation by 3-D Lookup Table.
- Based on surface potential — Uses the surface-potential equation to represent
  the device. This modeling approach provides a greater level of model fidelity than the
  simple square-law (threshold-voltage-based) models can provide. The tradeoff is that there
  are more parameters that require extraction. For details, see Surface-Potential-Based Model.

Together with the thermal port options (see Thermal Port), the block therefore provides you with four choices. To select the desired option, set the
**Modeling option** parameter to either:

- **Threshold-based** — Basic model, which represents
  the device using the Shichman-Hodges equation (based on threshold voltage) and does not
  simulate thermal effects. This is the default.
- **Threshold-based with thermal** — Model based on
  threshold voltage and with exposed thermal port.
- **Surface-potential-based** — Model based on surface
  potential. This model does not simulate thermal effects.
- **Surface-potential-based with thermal** — Thermal
  modeling option of the model based on surface potential.

### Threshold-Based Model

The threshold-based option of the block uses the Shichman and Hodges equations [1] for an insulated-gate field-effect transistor to represent an N-Channel MOSFET.

The drain-source current, *IDS*, depends on the
region of operation:

- In the off region (*VGS* <
  *Vth*), the drain-source current is:

  IDS=0
- In the linear region (0 < *VDS* <
  *VGS*
  –*Vth*), the drain-source current is:

  IDS=K((VGS−Vth)VDS−VDS2/2)(1+λ|VDS|)
- In the saturated region (0 < *VGS*
  –*Vth* <
  *VDS*), the drain-source current is:

  IDS=(K/2)(VGS−Vth)2(1+λ|VDS|)

In the preceding equations:

- *K* is the transistor gain.
- *VDS* is the positive drain-source
  voltage.
- *VGS* is the gate-source voltage.
- *Vth* is the threshold voltage. For the four
  terminal parameterization, *Vth* is obtained using
  these equations:

  | *VBS* Range | *Vth* Equation |
  | --- | --- |
  | VBS≤0 | Vth=VT0+γ(−2ϕB)+γ(2ϕB−VBS) |
  | 0<VBS≤4ϕB | Vth=VT0−γVBS2ϕB |
  | VBS>4ϕB | Vth=VT0+γ(−2ϕB) |
- *λ* is the channel modulation.

To specify the parallel conductance of the channel, connect an Environment Parameters block to the electrical network. Then, set the
minimum conductance of the N-Channel MOSFET block and other
SPICE-compatible blocks by setting the **GMIN** parameter of
the Environment Parameters block.

### Charge Model for Threshold-Based Modeling Option

The block models capacitances either by fixed capacitance values, or by tabulated values as
a function of the drain-source voltage. In either case, you can either directly specify the
gate-source and gate-drain capacitance values, or let the block derive them from the input
and reverse transfer capacitance values. Therefore, the
**Parameterization** options for charge model on the
**Capacitance** setting are:

- `Specify fixed input, reverse transfer and output
  capacitance` — Provide fixed parameter values from datasheet and
  let the block convert the input and reverse transfer capacitance values to capacitance
  values, as described below. This is the default method.
- `Specify fixed gate-source, gate-drain and drain-source
  capacitance` — Provide fixed values for capacitance parameters
  directly.
- `Specify tabulated input, reverse transfer and output
  capacitance` — Provide tabulated capacitance and drain-source
  voltage values based on datasheet plots. The block converts the input and reverse
  transfer capacitance values to capacitance values, as described below.
- `Specify tabulated gate-source, gate-drain and drain-source
  capacitance` — Provide tabulated values for capacitances and
  drain-source voltage.

Use one of the tabulated capacitance options (`Specify tabulated input, reverse
transfer and output capacitance` or `Specify tabulated
gate-source, gate-drain and drain-source capacitance`) when the datasheet
provides a plot of capacitances as a function of drain-source voltage. Using tabulated
capacitance values gives more accurate dynamic characteristics and avoids the need for
interactive tuning of parameters to fit the dynamics.

If you use the `Specify fixed gate-source, gate-drain and drain-source
capacitance` or `Specify tabulated gate-source, gate-drain and
drain-source capacitance` option, the **Capacitance**
setting lets you specify the **Gate-drain capacitance, Cgd**,
**Gate-source capacitance, Cgs**, and **Drain-source capacitance,
Cds** parameter values (fixed or tabulated) directly. Otherwise, the block
derives them from the **Input capacitance, Ciss**, **Reverse
transfer capacitance, Crss**, and **Output capacitance, Coss**
parameter values. These two parameterization methods are related as follows:

- *CGD* = *Crss*
- *CGS* = *Ciss* –
  *Crss*
- *CDS* = *Coss* –
  *Crss*

For the four terminals parameterization, the **Input capacitance, Ciss**,
**Reverse transfer capacitance, Crss**, and **Output capacitance,
Coss** are obtained using these equations:

- *CGD* = *Crss*
- *CGS* +
  *CGB* = *Ciss* –
  *Crss*
- *CDB* = *Coss* –
  *Crss*

A simplified Meyer's capacitance model describes the gate-source capacitance,
*CGS*, the gate-bulk capacitance,
*CGB*, and the gate-drain capacitance,
*CGD*.

This figure shows how *CGB* and
*CGS* change, when the gate-source voltage
*Vgs* reaches the threshold voltage
*Vth*, if you set the **Gate-bulk and
gate-source charge-voltage linearity** parameter to `Gate-bulk and
gate-source capacitance change instantly`.

This figure shows how *CGB* and
*CGS* change, when
*Vgs* is between *Vth*
–2*ΦB* and *Vth*, if you set the
**Gate-bulk and gate-source charge-voltage linearity** parameter to
`Gate-bulk and gate-source capacitance change gradually`.

The two fixed capacitance options (`Specify fixed input, reverse transfer and
output capacitance` or `Specify fixed gate-source, gate-drain and
drain-source capacitance`) let you model gate capacitance as a fixed
gate-source capacitance *CGS* and either a fixed or
a nonlinear gate-drain capacitance *CGD*. If you
select the `Gate-drain charge function is nonlinear` option for the
**Gate-drain charge-voltage linearity** parameter, then the gate-drain
charge relationship is defined by the piecewise-linear function shown in the following
figure.

For instructions on how to map a time response to device capacitance values, see the
N-Channel IGBT block reference page. However, this mapping is only approximate
because the Miller voltage typically varies more from the threshold voltage than in the case for
the IGBT.

**Note**

Because this block implementation includes a charge model, you must model the impedance of
the circuit driving the gate to obtain representative turn-on and turn-off dynamics. Therefore,
if you are simplifying the gate drive circuit by representing it as a controlled voltage
source, you must include a suitable series resistor between the voltage source and the
gate.

### Representation by 2-D Lookup Table

For the lookup table representation of the detailed block modeling option, you provide
tabulated values for drain-source currents as a function of gate-source voltage and
drain-source voltage. The main advantage of using this option is simulation speed. It also
lets you parameterize the device from either measured data or from data obtained from
another simulation environment.

This figure shows the implementation of the 2-D lookup table option when you set
**Ids-Vds parameterization** to `Provide negative and positive Vds
data`:

This figure shows the implementation of the 2-D lookup table option when you set
**Ids-Vds parameterization** to `Provide positive Vds data
only`:

For the four terminal MOSFET, the surface potential and body factor values are calculated
based on the nearest threshold voltage as shown in this picture:

**Note**

To ensure that the signs of the drain-source current and drain-source voltage are consistent:

- If the drain-source voltage is equal to `0`, the value of the
  **Tabulated drain-source currents, Ids(Vgs,Vds)** parameter must
  be equal to `0`.
- The tabulated power, which is the product of the **Tabulated
  drain-source currents, Ids(Vgs,Vds)** parameter and the drain-source
  voltage, must be greater than or equal to `0`.
- The tabulated conductance, which is the gradient of the **Tabulated
  drain-source currents, Ids(Vgs,Vds)** parameter with respect to the
  drain-source voltage *Vds*, must be greater
  than or equal to `0`.
- The first gradient of the **Tabulated drain-source currents,
  Ids(Vgs,Vds)** parameter, with respect to gate-source voltage
  *Vgs*, must be equal to
  `0`.

### Representation by 3-D Lookup Table

For the temperature-dependent lookup table representation of the detailed block modeling
option, you provide tabulated values for drain-source currents as a function of gate-source
voltage, drain-source voltage, and temperature.

**Note**

To ensure that the signs of the drain-source current and drain-source voltage are consistent:

- If the drain-source voltage is equal to `0`, the value of the
  **Tabulated drain-source currents, Ids(Vgs,Vds,T)** parameter
  must be equal to `0`.
- The tabulated power, which is the product of the **Tabulated
  drain-source currents, Ids(Vgs,Vds,T)** parameter and the drain-source
  voltage, must be greater than or equal to `0`.
- The tabulated conductance, which is the gradient of the **Tabulated
  drain-source currents, Ids(Vgs,Vds,T)** parameter with respect to the
  drain-source voltage *Vds*, must be
  greater than or equal to `0`.
- The first gradient of the **Tabulated drain-source currents,
  Ids(Vgs,Vds,T)** parameter, with respect to gate-source voltage
  *Vgs*, must be equal to
  `0`.

### Surface-Potential-Based Model

The surface-potential-based modeling option of the block provides a greater level of model
fidelity than the simple square-law (threshold-voltage-based) model. The
surface-potential-based block modeling option includes the following effects:

- Fully nonlinear capacitance model (including the nonlinear Miller capacitance)
- Charge conservation inside the model, so you can use the model for charge sensitive
  simulations
- Velocity saturation and channel-length modulation
- The intrinsic body diode
- Reverse recovery in the body diode model
- Temperature scaling of physical parameters
- For the thermal modeling option, dynamic self-heating (that is, you can simulate the
  effect of self-heating on the electrical characteristics of the device)

This model is a minimal version of the world-standard PSP model (see https://briefs.techconnect.org/papers/introduction-to-psp-mosfet-model/),
including only certain effects from the PSP model in order to strike a balance between model
fidelity and complexity. For details of the physical background to the phenomena included in
this model, see [2].

The basis of the model is Poisson equation:

∂2ψ∂x2+∂2ψ∂y2=qNAεSi[1−exp(−ψϕT)+exp(ψ−2ϕB−VCBϕT)]

ϕT=kBTq

where:

- *ψ* is the electrostatic potential.
- *q* is the magnitude of the electronic charge.
- *NA* is the density of acceptors in the
  substrate.
- *ɛSi* is the dielectric permittivity of the
  semiconductor material (for example, silicon).
- *ϕB* is the difference between the intrinsic
  Fermi level and the Fermi level in the bulk silicon.
- *VCB* is the quasi-Fermi potential of the
  surface layer referenced to the bulk.
- *ϕT* is the thermal voltage.
- *kB* is Boltzmann’s constant.
- *T* is temperature.

Poisson equation is used to derive the surface-potential equation:

(VGB−VFB−ψs)2=γ2[ψs+ϕT(exp(−ψsϕT)−1)+ϕTexp(−2ϕB+VCBϕT)(exp(ψsϕT)−1)]

where:

- *VGB* is the applied gate-body voltage.
- *VFB* is the flatband voltage.
- *ψs* is the surface potential.
- *γ* is the body factor,

γ=2qεSiNACox

- *Cox* is the capacitance per unit area.

The block uses an explicit approximation to the surface-potential equation, to avoid the
need for numerical solution to this implicit equation.

Once the surface potential is known, the drain current
*ID* is given by

ID=Wμ0LGΔLGmob1+(θsatΔψ)2[−Q¯invΔψ+ϕT(QinvL−Qinv0)]

where:

- *W* is the device width.
- *L* is the channel length.
- *μ0* is the low-field mobility.
- *θsat* is the velocity saturation.
- *Δψ* is the difference in the surface potential between the drain and
  the source.
- *Qinv0* and
  *QinvL* are the inversion charge densities at the
  source and drain, respectively.
- Q¯inv is the average inversion charge density across the channel.
- *Gmob* is the mobility reduction factor. For
  more information, see the **Surface roughness scattering factor** parameter
  description in the Main (Surface-Potential-Based Modeling Option) section.
- *GΔL* is the channel-length modulation.

GΔL=1−ΔLL=1−αln[VDB−VDB,eff+(VDB−VDB,eff)2+Vp2Vp]

where:

- *α* is the channel-length modulation factor.
- *VDB* is the drain-body voltage.
- *VDB,eff* is the drain-body voltage clipped to a
  maximum value corresponding to velocity saturation or pinch-off (whichever occurs
  first).
- *Vp* is the channel-length modulation
  voltage.

The block computes the inversion charge densities directly from the surface
potential.

The block also computes the nonlinear capacitances from the surface potential. Source and
drain charge contributions are assigned via a bias-dependent Ward-Dutton charge-partitioning
scheme, as described in [3]. These charges are computed explicitly, so this model is charge-conserving. The capacitive
currents are computed by taking the time derivatives of the relevant charges. In practice, the
charges within the simulation are normalized to the oxide capacitance and computed in units of
volts.

The MOSFET gain, β, is given by

β=Wμ0CoxL

The threshold voltage for a short-circuited source-bulk connection is approximately given
by

VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

where:

- 2*ϕB* is the surface potential at strong
  inversion.

The overall three and four terminal models consist of an intrinsic MOSFET defined by the
surface-potential formulation, a body diode, series resistances, and fixed overlap capacitances,
as shown in the schematics.

### Modeling Body Diode

The block models the body diode either as an ideal, exponential diode or as a tabulated
diode.

**Exponential Diode**

When you set **Model body diode** to
`Exponential`, the junction and diffusion capacitances are:

Idio=Is[exp(−VDBnϕT)−1]

Cj=Cj01+VDBVbi

Cdiff=τIsnϕTexp(−VDBnϕT)

where:

- *Idio* is the current through the diode.
- *Is* is the reverse saturation current.
- *VDB* is the drain-body voltage.
- *n* is the ideality factor.
- *ϕT* is the thermal voltage.
- *Cj* is the junction capacitance of the
  diode.
- *Cj0* is the zero-bias junction
  capacitance.
- *Vbi* is the built-in voltage.
- *Cdiff* is the diffusion capacitance of the
  diode.
- *τ* is the transit time.

The capacitances are defined through an explicit calculation of charges, which are then
differentiated to give the capacitive expressions above. The block computes the capacitive
diode currents as time derivatives of the relevant charges, similar to the computation in the
surface-potential-based MOSFET model.

**Tabulated Diode**

To model a tabulated diode, set the **Model body diode** parameter to
`Tabulated I-V curve`. This figure shows the implementation of the
tabulated diode option:

When choosing this parameterization, you must provide the data for the forward bias
only.

The block implements the diode using a smooth interpolation option. If the diode exceeds
the provided tabulated data range, the block uses a linear extrapolation technique at the last
voltage-current data point.

To specify the off conductance of the tabulated
diode, set the **Diode off conductance** parameter. *(since R2024a)*

**Note**

The tabulated diode does not model the reverse breakdown.

### Modeling Temperature Dependence

The default behavior is that dependence on temperature is not modeled, and the device is
simulated at the temperature for which you provide block parameters. To model the dependence on
temperature during simulation, select `Model temperature dependence`
for the **Parameterization** parameter in the **Temperature
Dependence** setting.

**Threshold-Based Model**

For threshold-based modeling option, you can include modeling the dependence of the
transistor static behavior on temperature during simulation. Temperature dependence of the
capacitances is not modeled, this being a much smaller effect.

When including temperature dependence, the transistor defining equations remain the same.
The gain, *K*, and the threshold voltage,
*Vth*, become a function of temperature according to
the following equations:

KTs=KTm1(TsTm1)BEX

*Vths* =
*Vth1* + *α*
(*Ts* –
*Tm1*)

where:

- *Tm1* is the temperature at which the transistor
  parameters are specified, as defined by the **Measurement temperature**
  parameter value.
- *Ts* is the simulation temperature.
- *KTm1* is the transistor gain at the measurement
  temperature.
- *KTs* is the transistor gain at the simulation
  temperature. This is the transistor gain value used in the MOSFET equations when temperature
  dependence is modeled.
- *Vth1* is the threshold voltage at the
  measurement temperature.
- *Vths* is the threshold voltage at the
  simulation temperature. This is the threshold voltage value used in the MOSFET equations when
  temperature dependence is modeled.
- *BEX* is the mobility temperature exponent. A typical value of
  *BEX* is -1.5.
- *α* is the gate threshold voltage temperature coefficient,
  *d**Vth*/*d**T*.

For the four terminals parameterization, *Vth* is
obtained using these equations:

| *VBS* Range | *Vth* Equation |
| --- | --- |
| VBS≤0 | dVthdT=dVT0dT−γ22ϕBd2ϕBdT+γ22ϕB−VBSd2ϕBdT |
| 0<VBS≤4ϕB | dVthdT=dVT0dT−γVBS4(2ϕB)−32d2ϕBdT |
| VBS>4ϕB | dVthdT=dVT0dT−γ22ϕBd2ϕBdT |

Where:

- ϕB=kTqln(NBni) is the surface potential and d2ϕBdT=1T[2ϕB−(Eg(0)q+3kTq)].
- *Eg(0)* is the extrapolated zero degree
  band-gap, which is equal to `1.16`
  `eV` for silicon.
- *VBS* is the bulk-source voltage.

For most MOSFETS, you can use the default value of `-1.5` for
*BEX*. Some datasheets quote the value for *α*, but most
typically they provide the temperature dependence for drain-source on resistance,
*RDS(on)*. Depending on the block parameterization
method, you have two ways of specifying *α*:

- If you parameterize the block from a datasheet, you have to provide
  *RDS(on)* at a second measurement temperature. The
  block then calculates the value for *α* based on this data.
- If you parameterize by specifying equation parameters, you have to provide the value for
  *α* directly.

If you have more data comprising drain current as a function of gate-source voltage for
more than one temperature, then you can also use Simulink®
Design Optimization™ software to help tune the values for *α* and
*BEX*.

**Surface-Potential-Based Model**

The surface-potential-based model includes temperature effects on the capacitance
characteristics, as well as modeling the dependence of the transistor static behavior on
temperature during simulation.

The **Measurement temperature** parameter on the **Main**
setting specifies temperature *T*m1 at which the other
device parameters have been extracted. The **Temperature Dependence** setting
provides the simulation temperature, *T*s, and the
temperature-scaling coefficients for the other device parameters. For more information, see
Temperature Dependence (Surface-Potential-Based Modeling Option).

### Faults

To model a fault in the N-Channel MOSFET block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The N-Channel MOSFET block models five types of
fault:

- `Open circuit` — Failure due to metallization
  burnout
- `Drain-source short` — Failure due to avalanche
  breakdown on drain-source channel
- `Drain-bulk short or source-bulk short` — Failure
  due to avalanche breakdown on drain-bulk or source-bulk channels
- `Gate oxide short` — Failure of the gate oxide
  dielectric layer
- `Parameter shift` — Failure due to aging

The block can trigger fault events at a specific time or when the current or voltage
exceed the limit for longer than a specific time interval.

**Parameter Shift Fault**

If, in the **Faults** settings, you set the **Failure
mode** parameter to `Parameter shift`, the MOSFET
fails due to the aging of its components. This equation defines the value of the shifted
parameters:

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

where *tth* is the time
threshold when the fault is triggered and *τ* is the value of the
**Fault transition time constant, tau** parameter.

**Gate Oxide Short Fault**

If, in the **Faults** settings, you set the **Failure
mode** parameter to `Gate oxide short`, the gate oxide
dielectric layer fails. These figures show the equivalent circuits for the three-terminal
MOSFET in the unfaulted and faulted state:

These figures show the equivalent circuits for the four-terminal MOSFET
in the unfaulted and faulted state:

### Thermal Port

The block has an optional thermal port, hidden by default. To expose the thermal port, set the
**Modeling option** parameter to:

- `Threshold-based with thermal` — Model based
  on threshold voltage and with exposed thermal port
- `Surface-potential-based with thermal` —
  Model based on surface potential and with exposed thermal
  port

This action displays the thermal port **H** on the block icon, and exposes
the **Thermal Port** parameters.

Use the thermal port to simulate the effects of generated heat and device temperature. For
more information on using thermal ports and on the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

This table shows the relationship between the capacitances of the block and the initial targets:

| Defined Capacitance | Initial Targets |
| --- | --- |
| Gate-emitter capacitance, *Cge* | Set the initial target for the gate-emitter capacitance voltage only. Set the initial target of the collector-emitter capacitance voltage to `0` or set its priority to `None`. |
| Collector-emitter capacitance, *Cce* | Set the initial target for the collector-emitter capacitance voltage only. Set the initial target of the gate-emitter capacitance voltage to `0` or set its priority to `None`. |
| Gate-collector capacitance, *Cgc* | Set the initial targets for the gate-collector voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and collector-emitter. |
| Gate-emitter capacitance, *Cge*, and gate-collector capacitance, *Cgc* | Set the initial targets for the gate-emitter and gate-collector voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |
| Gate-emitter capacitance, *Cge*, and collector-emitter capacitance, *Cce* | Set the initial target for the gate-emitter and the collector-emitter capacitance. |
| Gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | Set the initial targets for the gate-collector and collector-emitter voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |
| Gate-emitter capacitance, *Cge*, gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | Set the initial targets for the gate-emitter, gate collector and collector-emitter capacitances by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |

**Note**

Inside your model, the number of initial targets with **Priority** equal to `Low` or `High` must match the number of differential variables. The differential variables come from the inductors and the capacitances in the model.

### Plot Device Characteristics

You can plot the basic I-V characteristics of the N-Channel MOSFET block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
N-Channel MOSFET block to `Threshold Based` or `Surface
potential based`. To plot the basic characteristics, right-click the block
and select **Electrical** > **Basic
characteristics** from the context menu. For more information about the
**Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.

The N-Channel MOSFET blocks also supports the
**Explore characteristics** option. Use this option to perform an
in-depth study of block characteristics and match the block behavior to a set of target
characteristics. To enable this option, set the **Modeling option**
parameter of the block to `Surface potential based`. Then,
right-click the block and select **Electrical** >
**Explore characteristics** from the context menu. For more
information about this option, see MOSFET Characteristics Viewer.
