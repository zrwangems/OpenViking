---
type: simulink-block
title: 'P-Channel JFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pchanneljfet'
documentation_source_path: 'ref/pchanneljfet.html'
language: en
---

# P-Channel JFET

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

Electrical conserving port associated with the transistor gate terminal.

### **D** — Drain terminal electrical

Electrical conserving port associated with the transistor drain terminal.

### **S** — Source terminal electrical

Electrical conserving port associated with the transistor source terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Parameterization
  summary: Block parameterization Specify from a datasheet (default) | Specify using equation parameters directly
  group: Main
- name: Gate reverse current, I_gss
  summary: Gate reverse current 5 nA (default)
  group: Main
- name: Saturated drain current, I_dss
  summary: Saturated drain current -3 mA (default)
  group: Main
- name: I_dss measurement point, [V_gs V_ds]
  summary: I_dss measurement point [ 0 -15 ] V (default)
  group: Main
- name: Small-signal parameters, [g_fs g_os]
  summary: Small-signal parameters [ 2.5e+3 75 ] uS (default)
  group: Main
- name: Small-signal measurement point [V_gs V_ds]
  summary: Small-signal measurement point [ 0 -15 ] V (default)
  group: Main
- name: Transconductance parameter
  summary: Transconductance parameter 1e-04 A/V2 (default)
  group: Main
- name: Saturation current
  summary: Saturation current 1e-14 A (default)
  group: Main
- name: Threshold voltage
  summary: Threshold voltage 2 V (default)
  group: Main
- name: Channel-length modulation
  summary: Channel-length modulation 0 1/V (default)
  group: Main
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Main
- name: Source ohmic resistance
  summary: Source ohmic resistance 0.0001 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Drain ohmic resistance
  summary: Drain ohmic resistance 0.01 Ohm (default) | nonnegative scalar
  group: Ohmic Resistance
- name: Parameterization
  summary: Junction capacitance parameterization Specify from a datasheet (default) | Specify using equation parameters directly
  group: Junction Capacitance
- name: Input capacitance, Ciss
  summary: Input capacitance 5 pF (default)
  group: Junction Capacitance
- name: Reverse transfer capacitance, Crss
  summary: Reverse transfer capacitance 1 pF (default)
  group: Junction Capacitance
- name: Gate-source junction capacitance
  summary: Gate-source junction capacitance 4 pF (default)
  group: Junction Capacitance
- name: Gate-drain junction capacitance
  summary: Gate-drain junction capacitance 1 pF (default)
  group: Junction Capacitance
- name: Parameterization
  summary: Temperature dependence parameterization None — Simulate at parameter measurement temperature (default) | Model
    temperature dependence
  group: Temperature Dependence
- name: Gate reverse current, I_gss, at second measurement temperature
  summary: Gate reverse current, I_gss, at second measurement temperature 950 nA (default)
  group: Temperature Dependence
- name: Saturated drain current, I_dss, at second measurement temperature
  summary: Saturated drain current, I_dss, at second measurement temperature -2.3 mA (default)
  group: Temperature Dependence
- name: Second measurement temperature
  summary: Second measurement temperature 125 degC (default)
  group: Temperature Dependence
- name: Energy gap, EG
  summary: Energy gap 1.11 eV (default)
  group: Temperature Dependence
- name: Saturation current temperature exponent, XTI
  summary: Saturation current temperature exponent 3 (default)
  group: Temperature Dependence
- name: Gate threshold voltage temperature coefficient, dVt0/dT
  summary: Gate threshold voltage temperature coefficient 1 mV/K (default)
  group: Temperature Dependence
- name: Mobility temperature exponent, BEX
  summary: Mobility temperature exponent -1.5 (default)
  group: Temperature Dependence
- name: Device simulation temperature
  summary: Device simulation temperature 25 degC (default)
  group: Temperature Dependence
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Parameterization** — Block parameterization `Specify from a datasheet` (default) | `Specify using equation parameters directly`

Select one of the following methods for block parameterization:

- `Specify from a datasheet` — Provide parameters that
  the block converts to equations that describe the transistor. This is the default
  method.
- `Specify using equation parameters directly` —
  Provide equation parameters *β*, *IS*,
  *Vt0*, and *λ*.

### **Gate reverse current, I\_gss** — Gate reverse current `5` `nA` (default)

The reverse current that flows in the diode when the drain and source are
short-circuited and a large positive gate-source voltage is applied.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter.

### **Saturated drain current, I\_dss** — Saturated drain current `-3` `mA` (default)

The current that flows when a large negative drain-source voltage is applied for a
specified gate-source voltage. For a depletion-mode device, this gate-source voltage may be
zero, in which case *I\_dss* may be referred to as the zero-gate voltage
drain current.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter.

### **I\_dss measurement point, [V\_gs V\_ds]** — I\_dss measurement point `[ 0 -15 ]` `V` (default)

A vector of the values of *VGS* and
*VDS* at which *I\_dss* is
measured. Normally *VGS* is zero.
*VDS* should be less than zero.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter.

### **Small-signal parameters, [g\_fs g\_os]** — Small-signal parameters `[ 2.5e+3 75 ]` `uS` (default)

A vector of the values of *g\_fs* and *g\_os*.
*g\_fs* is the forward transfer conductance, that is, the conductance for a
fixed drain-source voltage. *g\_os* is the output conductance, that is, the
conductance for a fixed gate-source voltage.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter.

### **Small-signal measurement point [V\_gs V\_ds]** — Small-signal measurement point `[ 0 -15 ]` `V` (default)

A vector of the values of *VGS* and
*VDS* at which *g\_fs* and
*g\_os* are measured. *VDS* should
be less than zero. For depletion-mode devices, *VGS*
is typically zero.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter.

### **Transconductance parameter** — Transconductance parameter `1e-04` `A/V2` (default)

The derivative of drain current with respect to gate voltage.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization**
parameter.

### **Saturation current** — Saturation current `1e-14` `A` (default)

The magnitude of the current that the ideal diode equation approaches asymptotically for
very large reverse bias levels.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization**
parameter.

### **Threshold voltage** — Threshold voltage `2` `V` (default)

The gate-source voltage above which the transistor produces a nonzero drain current. For
an enhancement device, Vt0 should be negative. For a depletion mode device, Vt0 should be
positive.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization**
parameter.

### **Channel-length modulation** — Channel-length modulation `0` `1/V` (default)

The channel-length modulation.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization**
parameter.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

The temperature for which the datasheet parameters are quoted.

### Ohmic Resistance

### **Source ohmic resistance** — Source ohmic resistance `0.0001` `Ohm` (default) | nonnegative scalar

The transistor source resistance.

### **Drain ohmic resistance** — Drain ohmic resistance `0.01` `Ohm` (default) | nonnegative scalar

The transistor drain resistance.

### Junction Capacitance

### **Parameterization** — Junction capacitance parameterization `Specify from a datasheet` (default) | `Specify using equation parameters directly`

Select one of the following methods for block parameterization:

- `Specify from a datasheet` — Provide parameters that
  the block converts to junction capacitance values. This is the default method.
- `Specify using equation parameters directly` —
  Provide junction capacitance parameters directly.

### **Input capacitance, Ciss** — Input capacitance `5` `pF` (default)

The gate-source capacitance with the drain shorted to the source.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter in the
**Junction Capacitance** tab.

### **Reverse transfer capacitance, Crss** — Reverse transfer capacitance `1` `pF` (default)

The drain-gate capacitance with the source connected to ground.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter in the
**Junction Capacitance** tab.

### **Gate-source junction capacitance** — Gate-source junction capacitance `4` `pF` (default)

The value of the capacitance placed between the gate and the source.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization** parameter
in the **Junction Capacitance** tab.

### **Gate-drain junction capacitance** — Gate-drain junction capacitance `1` `pF` (default)

The value of the capacitance placed between the gate and the drain.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization** parameter
in the **Junction Capacitance** tab.

### Temperature Dependence

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter measurement
  temperature` — Temperature dependence is not modeled. This is the
  default method.
- `Model temperature dependence` — Model
  temperature-dependent effects. You also have to provide a set of additional parameters
  depending on the block parameterization method. If you parameterize the block from a
  datasheet, you have to provide values for *I\_gss* and
  *I\_dss* at second measurement temperature. If you parameterize by
  directly specifying equation parameters, you have to provide the values for
  *EG*, *XTI*, and the gate threshold voltage temperature
  coefficient,
  *d**Vt0*/*d**T*.
  Regardless of the block parameterization method, you also have to provide values for
  *BEX* and for the simulation temperature,
  *Ts*.

### **Gate reverse current, I\_gss, at second measurement temperature** — Gate reverse current, I\_gss, at second measurement temperature `950` `nA` (default)

The value of the gate reverse current, *I\_gss*, at the second
measurement temperature and when the *I\_gss* measurement point is the same
as defined by the **Gate reverse current, I\_gss** parameter on the
**Main** tab.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter on the
**Main** tab.

### **Saturated drain current, I\_dss, at second measurement temperature** — Saturated drain current, I\_dss, at second measurement temperature `-2.3` `mA` (default)

The value of the saturated drain current, *I\_dss*, at the second
measurement temperature, and when the *I\_dss* measurement point is the same
as defined by the **I\_dss measurement point, [V\_gs V\_ds]** parameter on the
**Main** tab.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter on the
**Main** tab.

### **Second measurement temperature** — Second measurement temperature `125` `degC` (default)

Second temperature *Tm2* at which **Gate
reverse current, I\_gss, at second measurement temperature** and **Saturated
drain current, I\_dss, at second measurement temperature** are measured.

#### Dependencies

This parameter is visible only when you select `Specify from a
datasheet` for the **Parameterization** parameter on the
**Main** tab.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Energy gap value.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization** parameter
on the **Main** tab.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Saturation current temperature coefficient value.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization** parameter
on the **Main** tab.

### **Gate threshold voltage temperature coefficient, dVt0/dT** — Gate threshold voltage temperature coefficient `1` `mV/K` (default)

The rate of change of gate threshold voltage with temperature.

#### Dependencies

This parameter is visible only when you select `Specify using equation
parameters directly` for the **Parameterization** parameter
on the **Main** tab.

### **Mobility temperature exponent, BEX** — Mobility temperature exponent `-1.5` (default)

Mobility temperature coefficient value. You can use the default value for most JFETs.
See the Assumptions and Limitations section for additional considerations.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default)

Temperature *Ts* at which the device is
simulated.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2019b: Thermal network simlog paths

From R2019b forward, it is possible to model the thermal network of this block either
internally or externally.

As a result, the simlog paths corresponding to the thermal network have changed. If you
have a script that programmatically access the simlog, you have to manually update it to reflect
these changes.

## Description

P-Channel junction field-effect transistor

The P-Channel JFET block uses the Shichman and Hodges
equations to represent a P-Channel JFET using a model with the following structure:

G is the transistor gate, D is the transistor drain and S is the transistor source. The
drain current, *ID*, depends on the region of operation
and whether the transistor is operating in normal or inverse mode.

- In normal mode (–*VDS* ≥ 0), the block provides
  the following relationship between the drain current
  *ID* and the drain-source voltage
  *VDS*.

  | Region | Applicable Range of *VGS* and *VDS* Values | Corresponding *ID* Equation |
  | --- | --- | --- |
  | Off | –*VGS* ≤ –*Vt0* | *ID* = 0 |
  | Linear | 0 < –*VDS* < –*VGS* + *Vt0* | *ID* = *β**VDS*(2(–*VGS* + *Vt0*) + *VDS*)(1 – *λ**VDS*) |
  | Saturated | 0 < –*VGS* + *Vt0* ≤ –*VDS* | *ID* = –*β*(–*VGS* + *Vt0*)2 (1 – *λ**VDS*) |
- In inverse mode (–*VDS* < 0), the block provides the following relationship between the drain current
  *ID* and the drain-source voltage
  *VDS*.

  | Region | Applicable Range of *VGS* and *VDS* Values | Corresponding *ID* Equation |
  | --- | --- | --- |
  | Off | –*VGD* ≤ –*Vt0* | *ID* = 0 |
  | Linear | 0 < *VDS* < – *VGD* + *Vt0* | *ID* = *β**VDS*(2(–*VGD* + *Vt0*) – *VDS*)(1 + *λ**VDS*) |
  | Saturated | 0 < –*VGD* + t0*V* ≤*VDS* | *ID* = *β*(–*VGD* + *Vt0*)2 (1 + *λ**VDS*) |

In the preceding equations:

- *VGS* is the gate-source voltage.
- *VGD* is the gate-drain voltage.
- *Vt0* is the threshold voltage. If you select
  `Specify using equation parameters directly` for the
  **Parameterization** parameter,
  *Vt0* is the **Threshold voltage**
  parameter value. Otherwise, the block calculates *Vt0*
  from the datasheet parameters you specify.
- *β* is the transconductance parameter. If you select
  `Specify using equation parameters directly` for the
  **Parameterization** parameter, *β* is the
  **Transconductance parameter** parameter value. Otherwise, the block
  calculates *β* from the datasheet parameters you specify.
- *λ* is the channel-length modulation parameter. If you select
  `Specify using equation parameters directly` for the
  **Parameterization** parameter, *λ* is the
  **Channel-length modulation** parameter value. Otherwise, the block
  calculates *λ* from the datasheet parameters you specify.

The currents in each of the diodes satisfy the exponential diode equation

IGD=−IS⋅(e−qVGD/kTm1−1)

IGS=−IS⋅(e−qVGS/kTm1−1)

where:

- *IS* is the saturation current. If you select `Specify using
  equation parameters directly` for the **Parameterization**
  parameter, **IS** is the **Saturation
  current** parameter value. Otherwise, the block calculates
  **IS** from the datasheet parameters you specify.
- *q* is the elementary charge on an electron (1.602176e–19
  Coulombs).
- *k* is the Boltzmann constant (1.3806503e–23 J/K).
- *Tm1* is the measurement temperature. The value
  comes from the **Measurement temperature** parameter.

The block models gate junction capacitance as a fixed gate-drain capacitance
*CGD* and a fixed gate-source capacitance
*CGS*. If you select `Specify using
equation parameters directly` for the **Parameterization**
parameter, you specify these values directly using the **Gate-drain junction
capacitance** and **Gate-source junction capacitance** parameters.
Otherwise, the block derives them from the **Input capacitance Ciss** and
**Reverse transfer capacitance Crss** parameter values. The two
parameterizations are related as follows:

- *CGD* = *Crss*
- *CGS* = *Ciss* –
  *Crss*

### Modeling Temperature Dependence

The default behavior is that dependence on temperature is not modeled, and the device is
simulated at the temperature for which you provide block parameters. You can optionally include
modeling the dependence of the transistor static behavior on temperature during simulation.
Temperature dependence of the junction capacitances is not modeled, this being a much smaller
effect.

When including temperature dependence, the transistor defining equations remain the same.
The measurement temperature value, *Tm1*, is replaced
with the simulation temperature, *Ts*. The
transconductance, *β*, and the threshold voltage,
*Vt0*, become a function of temperature according to
the following equations:

βTs=βTm1(TsTm1)BEX

*Vt0s* =
*Vt01* + *α* (
*Ts* – *Tm1*)

where:

- *Tm1* is the temperature at which the transistor
  parameters are specified, as defined by the **Measurement temperature**
  parameter value.
- *Ts* is the simulation temperature.
- *βTm1* is JFET transconductance at the
  measurement temperature.
- *βTs* is JFET transconductance at the simulation
  temperature. This is the transconductance value used in the JFET equations when temperature
  dependence is modeled.
- *Vt01* is the threshold voltage at measurement
  temperature.
- *Vt0s* is the threshold voltage at simulation
  temperature. This is the threshold voltage value used in the JFET equations when temperature
  dependence is modeled.
- *BEX* is the mobility temperature exponent. A typical value of
  *BEX* is -1.5.
- *α* is the gate threshold voltage temperature coefficient,
  *d**V*th/*d**T*.

For most JFETS, you can use the default value of `-1.5` for
*BEX*. Some datasheets quote the value for *α*, but most
typically they provide the temperature dependence for the saturated drain current,
*I\_dss*. Depending on the block parameterization method, you have two ways of
specifying *α*:

- If you parameterize the block from a datasheet, you have to provide
  *I\_dss* at a second measurement temperature. The block then calculates the
  value for *α* based on this data.
- If you parameterize by specifying equation parameters, you have to provide the value for
  *α* directly.

If you have more data comprising drain current as a function of gate-source voltage for
fixed drain-source voltage plotted at more than one temperature, then you can also use
Simulink®
Design Optimization™ software to help tune the values for *α* and
*BEX*.

In addition, the saturation current term, *IS*, in the gate-drain and
gate-source current equations depends on temperature

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

where:

- *ISTm1* is the saturation current at the
  measurement temperature.
- *ISTs* is the saturation current at the
  simulation temperature. This is the saturation current value used in the gate diode equations
  when temperature dependence is modeled..
- *EG* is the energy gap.
- *k* is the Boltzmann constant (1.3806503e–23 J/K).
- *XTI* is the saturation current temperature exponent.

Similar to *α*, you have two ways of specifying *EG* and
*XTI*:

- If you parameterize the block from a datasheet, you have to specify the gate reverse
  current, *I\_gss*, at a second measurement temperature. The block then
  calculates the value for *EG* based on this data and assuming a p-n junction
  nominal value of `3` for *XTI*.
- If you parameterize by specifying equation parameters, you have to provide the values for
  *EG* and *XTI* directly. This option gives you most
  flexibility to match device behavior, for example, if you have a graph of
  *I\_gss* as a function of temperature. With this data you can use Simulink
  Design Optimization software to help tune the values for *EG* and
  *XTI*.

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

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Plot Basic I-V Characteristics

You can plot the basic I-V characteristics of the P-Channel JFET block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
P-Channel JFET block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
