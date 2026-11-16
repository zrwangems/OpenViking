---
type: simulink-block
title: 'SPICE PNP'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicepnp'
documentation_source_path: 'ref/spicepnp.html'
language: en
---

# SPICE PNP

## Ports

### Conserving

### **bx** — Base terminal electrical

Electrical conserving port associated with the transistor base
terminal.

### **cx** — Collector terminal electrical

Electrical conserving port associated with the transistor collector
terminal.

### **ex** — Emitter terminal electrical

Electrical conserving port associated with the transistor emitter
terminal.

### **sx** — Substrate terminal electrical

Electrical conserving port associated with the transistor substrate
terminal.

## Parameters

### Main

### **Device area, AREA** — Device area `1.0` `m^2` (default) | positive scalar

Device area. The value must be greater than
`0`.

### **Number of parallel devices, SCALE** — Number of parallel devices `1` (default) | positive scalar

Number of parallel transistors that the block represents. The value
must be greater than `0`.

### Forward Gain

### **Transport saturation current, IS** — Saturation current magnitude `1e-16` `A/m^2` (default) | positive scalar

Magnitude of the current at which the transistor saturates. The value
must be greater than `0`.

### **Forward beta, BF** — Ideal maximum forward beta `100` (default) | positive scalar

Ideal maximum forward beta. The value must be greater than
`0`.

### **Forward emission coefficient, NF** — Forward emission coefficient `1` (default) | positive scalar

Forward emission coefficient or ideality factor. The value must be
greater than `0`.

### **Forward Early voltage, VAF** — Forward Early voltage `Inf` `V` (default) | nonnegative scalar

Forward Early voltage. The value must be greater than or equal to
`0`.

### **Forward knee current, IKF** — Forward-beta high-current roll-off current `Inf` `A/m^2` (default) | nonnegative scalar

Current value at which forward-beta high-current roll-off occurs. The
value must be greater than or equal to `0`.

### **B-E leakage current, ISE** — Base-emitter leakage current `0` `A/m^2` (default) | nonnegative scalar

Base-emitter leakage current. The value must be greater than or equal
to `0`.

### **B-E emission coefficient, NE** — Base-emitter emission coefficient `1.5` (default) | positive scalar

Base-emitter emission coefficient or ideality factor. The value must
be greater than `0`.

### Reverse Gain

### **Reverse beta, BR** — Ideal maximum reverse beta `1` (default) | positive scalar

Ideal maximum reverse beta. The value must be greater than
`0`.

### **Reverse emission coefficient, NR** — Reverse emission coefficient `1` (default) | positive scalar

Reverse emission coefficient or ideality factor. The value must be
greater than `0`.

### **Reverse Early voltage, VAR** — Reverse Early voltage `Inf` `V` (default) | nonnegative scalar

Reverse Early voltage. The value must be greater than or equal to
`0`.

### **Reverse knee current, IKR** — Reverse-beta high-current roll-off current `Inf` `A/m^2` (default) | nonnegative scalar

Current value at which reverse-beta high-current roll-off occurs. The
value must be greater than or equal to `0`.

### **B-C leakage current, ISC** — Base-collector leakage current `0` `A/m^2` (default) | nonnegative scalar

Base-collector leakage current. The value must be greater than or
equal to `0`.

### **B-C emission coefficient, NC** — Base-collector emission coefficient `2` (default) | positive scalar

Base-collector emission coefficient or ideality factor. The value must
be greater than `0`.

### Resistors

### **Zero-bias base resistance, RB** — Base resistance `1` `m^2*Ohm` (default) | nonnegative scalar

Maximum resistance of the base. The value must be greater than or equal to
`0`.

### **Half base resistance cur, IRB** — Base resistance half zero-bias drop current `Inf` `A/m^2` (default) | nonnegative scalar

Base current at which the base resistance has dropped to half of its
zero-bias value. The value must be greater than or equal to
`0`. If you do not want to model the change in base
resistance as a function of base current, use the default value of
`Inf`.

### **Minimum base resistance, RBM** — Minimum base resistance `0` `m^2*Ohm` (default) | scalar < *RB*

Minimum resistance of the base. The value must be less than or equal
to the **Zero-bias base resistance, RB** parameter
value.

### **Emitter resistance, RE** — Emitter resistance `1e-4` `m^2*Ohm` (default) | nonnegative scalar

Resistance of the emitter. The value must be greater than or equal to
`0`.

### **Collector resistance, RC** — Collector resistance `0.01` `m^2*Ohm` (default) | nonnegative scalar

Resistance of the collector. The value must be greater than or equal
to `0`.

### Capacitance

### **Model junction capacitance** — Junction capacitance model `No` (default) | `Yes`

Options for modeling the junction capacitance:

- `No` — Do not include
  junction capacitance in the model. This is the default
  option.
- `Yes` — Include junction
  capacitance in the model.

#### Dependencies

Selecting `Yes` for the **Model
junction capacitance** parameter exposes other
**Capacitance** parameters and these
capacitance junction settings:

- **B-E Capacitance** —
  Base-emitter parameters
- **B-C Capacitance** —
  Base-collector parameters
- **C-S Capacitance** —
  Collector-substrate parameters

### **Capacitance coefficient, FC** — Capacitance coefficient `0.5` (default) | 0 ≤ *FC* < 0.95 | scalar

Fitting coefficient, *FC*, that quantifies the decrease of the
depletion capacitance with applied voltage. The value must be greater
than or equal to `0` and less than
`0.95`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Specify initial condition** — Initial condition model `No` (default) | `Yes`

Options for specifying initial conditions:

- `No` — Do not specify an initial
  condition for the model. This is the default option.
- `Yes` — Specify the
  initial transistor conditions.

  **Note**

  The block applies the initial transistor voltages
  across the junction capacitors and not across the
  ports.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

Selecting `Yes` for the **Specify
initial condition** parameter exposes related
parameters.

### **Initial condition voltage ICVBE** — Initial base-emitter voltage `0` `V` (default) | scalar

Base-emitter voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** and `Yes` for
the **Specify initial condition** parameter.

### **Initial condition voltage ICVCE** — Initial base-collector voltage `0` `V` (default) | scalar

Base-collector voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** and `Yes` for
the **Specify initial condition** parameter.

### B-E Capacitance

These settings are exposed if you select `Yes` for the
**Model junction capacitance** parameter in the
**Capacitance** settings.

### **B-E depletion capacitance, CJE** — Base-emitter junction depletion capacitance `0` `F/m^2` (default) | nonnegative scalar

Depletion capacitance across the base-emitter junction. The value must
be greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **B-E built-in potential, VJE** — Base-emitter junction potential `0.75` `V` (default) | scalar | 0.01 ≤ *VJE*

Base-emitter junction potential. The value must be greater than or
equal to `0.01`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **B-E exponential factor, MJE** — Base-emitter junction grading coefficient `0.33` (default) | scalar | 0 ≤ *MJC* ≤ 0.9

Grading coefficient for the base-emitter junction. The value must be
greater than or equal to `0` and less than or equal to
`0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Forward transit time, TF** — Minority carrier transit time `0` `s` (default) | nonnegative scalar

Transit time of the minority carriers that cause diffusion capacitance
when the base-emitter junction is forward-biased. The value must be
greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Coefficient of TF, XTF** — Base-emitter transit time bias dependence coefficient `0` (default) | nonnegative scalar

Coefficient for the base-emitter bias dependence of the transit time, which produces a
charge across the base-emitter junction. The value must be greater than
or equal to `0`. If you do not want to model the effect
of base-emitter bias on transit time, use the default value of
`0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **VBC dependence of TF, VTF** — Base-collector transit time bias dependence coefficient `Inf` `V` (default) | nonnegative scalar

Coefficient for the base-collector bias dependence of the transit time. The value must
be greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Coefficient of TF, ITF** — Collector current transit time dependence coefficient `0` `A/m^2` (default) | nonnegative scalar

Coefficient for the dependence of the transit time on collector current. The value must
be greater than or equal to `0`. If you do not want to
model the effect of collector current on transit time, use the default
value of `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### B-C Capacitance

These settings are exposed if you select `Yes` for the
**Model junction capacitance** parameter in the
**Capacitance** settings.

### **B-C depletion capacitance, CJC** — base-collector junction depletion capacitance `0` `F/m^2` (default) | positive scalar

Depletion capacitance across the base-collector junction. The value
must be greater than `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **B-C built-in potential, VJC** — Base-collector junction potential `0.75` `V` (default) | scalar | 0.01 ≤ *VJC*

Base-collector junction potential. The value must be greater than or
equal to `0.01`
`V`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **B-C exponential factor, MJC** — Base-collector junction grading coefficient `0.33` (default) | 0 ≤ *MJC* ≤ 0.9

Grading coefficient for the base-collector junction. The value must be greater than or
equal to `0` and less than or equal to
`0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **B-C capacitance fraction, XCJC** — Base-collector depletion capacitance fraction `1` (default) | scalar | 0 ≤ *XCJC* ≤ 1

Fraction of the base-collector depletion capacitance that is connected
between the internal base and the internal collector. The rest of the
base-collector depletion capacitance is connected between the external
base and the internal collector. The value must be greater than or equal
to `0` and less than or equal to
`1`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Reverse transit time, TR** — Minority carrier transit time `0` `s` (default) | nonnegative scalar

Transit time of the minority carriers that cause diffusion capacitance
when the base-collector junction is forward-biased. The value must be
greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### C-S Capacitance

These settings are exposed if you select `Yes` for the
**Model junction capacitance** parameter in the
**Capacitance** settings.

### **C-S junction capacitance, CJS** — Collector-substrate junction capacitance `0``F/m^2` (default) | nonnegative scalar

Collector-substrate junction capacitance. The value must be greater
than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Substrate built-in potential, VJS** — Substrate potential `0.75` `V` (default) | scalar | 0.01 ≤ *VJS*

Potential of the substrate. The value must be greater than or equal to
`0.01`
`V`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Substrate exponential factor, MJS** — Collector-substrate junction grading coefficient `0` (default) | scalar | 0 ≤ *MJS* ≤ 0.9

Grading coefficient for the collector-substrate junction. The value
must be greater than or equal to `0` and less than or
equal to `0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### Temperature

### **Model temperature dependence using** — Temperature dependence model `Device temperature` (default) | `Fixed temperature`

Select one of these options for modeling the transistor temperature dependence:

- `Device temperature` — Use
  the device temperature to model temperature
  dependence.
- `Fixed temperature` — Use
  a temperature that is independent of the circuit temperature
  to model temperature dependence.

For more information, see Transistor Temperature.

#### Dependencies

Selecting `Device temperature` exposes
the **Offset local circuit temperature, TOFFSET**
parameter. Selecting `Fixed temperature`
exposes the **Fixed circuit temperature, TFIXED**
parameter.

### **Beta temperature exponent, XTB** — Forward and reverse beta temperature exponent `0` (default) | nonnegative scalar

Forward and reverse beta temperature exponent that models base current
temperature dependence. The value must be greater than or equal to
`0`.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default) | *EG* ≥ 0.1 | scalar

Energy gap that affects the increase in the saturation current as
temperature increases. The value must be greater than or equal to
`0.1`.

### **Temperature exponent for IS, XTI** — Saturation current exponential increase order `3` (default) | nonnegative scalar

Order of the exponential increase in the saturation current as
temperature increases. The value must be greater than or equal to
`0`.

### **Offset local circuit temperature, TOFFSET** — Local circuit temperature offset `0` `K` (default) | scalar

Amount by which the transistor temperature differs from the circuit
temperature.

#### Dependencies

This parameter is only visible when you select `Device
temperature` for the **Model temperature
dependence using** parameter.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default) | positive scalar

Transistor simulation temperature. The value must be greater than
`0`
`K`.

#### Dependencies

This parameter is only visible when you select `Fixed
temperature` for the **Model temperature
dependence using** parameter.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default) | positive scalar

Temperature at which the transistor parameters are measured. The value
must be greater than `0`
`K`.

## Libraries

Simscape / Electrical / Additional Components / SPICE Semiconductors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

SPICE-compatible Gummel-Poon PNP Transistor

The SPICE PNP block represents a SPICE-compatible
four-terminal Gummel-Poon PNP bipolar junction transistor. A capacitor connects the
substrate port, **sx**, to the transistor base,
**bx**. Therefore, the device is equivalent to a three-terminal
transistor when you use the default value of `0` for the **C-S
junction capacitance, CJS** parameter and connect the substrate port to any
other port, including the emitter port, **ex**, or the collector port,
**cx**.

SPICE, or Simulation Program with Integrated Circuit Emphasis,
is a simulation tool for electronic circuits. You can convert some SPICE subcircuits into
equivalent Simscape™
Electrical™ models using the Environment Parameters block and
SPICE-compatible blocks from the Additional Components library. For more
information, see `subcircuit2ssc`.

### Equations

Variables for the SPICE PNP block equations include:

- Variables that you define by specifying parameters for the
  SPICE PNP block. The visibility of
  some of the parameters depends on the value that you set for other
  parameters. For more information, see Parameters.
- Geometry-adjusted variables, which depend on several values that you
  specify using parameters for the SPICE
  PNP block. For more information, see Geometry-Adjusted Variables.
- Temperature, *T*, which is `300.15`
  `K` by default. You can use a different value
  by specifying parameters for the SPICE
  PNP block or by specifying parameters for both the
  SPICE PNP block and an Environment
  Parameters block. For more information, see Transistor Temperature.
- Temperature-dependent variables. For more information, see Temperature Dependence.
- Minimal conductance, *GMIN*, which is
  `1e–12`
  `1/Ohm` by default. You can use a different
  value by specifying a parameter for an Environment
  Parameters block. For more information, see Minimal Conduction.

**Geometry-Adjusted Variables**

Several variables in the equations for the SPICE PNP bipolar junction
transistor model consider the geometry of the device that the block represents.
These geometry-adjusted variables depend on variables that you define by
specifying SPICE PNP block parameters. The
geometry-adjusted variables depend on these variables:

- *AREA* — Area of the device
- *SCALE* — Number of parallel connected
  devices
- The associated unadjusted variable

The table includes the geometry-adjusted variables and the
defining equations.

| Variable | Description | Equation |
| --- | --- | --- |
| *ISd* | Geometry-adjusted transport saturation current | ISd=IS\*AREA\*SCALE |
| *IKFd* | Geometry-adjusted forward knee current | IKFd=IKF\*AREA\*SCALE |
| *ISd* | Geometry-adjusted base-emitter leakage current | ISEd=ISE\*AREA\*SCALE |
| *IKRd* | Geometry-adjusted reverse knee current | IKRd=IKR\*AREA\*SCALE |
| *ISCd* | Geometry-adjusted base-collector leakage current | ISCd=ISC\*AREA\*SCALE |
| *IRBd* | Geometry-adjusted half base resistance current | IRBd=IRB\*AREA\*SCALE |
| *CJEd* | Geometry-adjusted base-emitter depletion capacitance | CJEd=CJE\*AREA\*SCALE |
| *ITFd* | Geometry-adjusted forward transit time coefficient | ITFd=ITF\*AREA\*SCALE |
| *CJCd* | Geometry-adjusted base-collector depletion capacitance | CJCd=CJC\*AREA\*SCALE |
| *CJSd* | Geometry-adjusted collector-substrate junction capacitance | CJSd=CJS\*AREA\*SCALE |
| *RBd* | Geometry-adjusted zero-bias base resistance | RBd=RBAREA\*SCALE |
| *RBMd* | Geometry-adjusted minimum base resistance | RBMd=RBMAREA\*SCALE |
| *REd* | Geometry-adjusted emitter resistance | REd=REAREA\*SCALE |
| *RCd* | Geometry-adjusted collector resistance | RCd=RCAREA\*SCALE |

**Transistor Temperature**

You can use these options to define transistor temperature,
*T*:

- Fixed temperature — The block uses a temperature that is
  independent from the circuit temperature when the **Model
  temperature dependence using** parameter in the
  **Temperature** settings of the
  SPICE PNP block is set to
  `Fixed temperature`. For this model,
  the block sets *T* equal to
  *TFIXED*.
- Device temperature — The block uses a temperature that depends on circuit
  temperature when the **Model temperature dependence
  using** parameter in the
  **Temperature** settings of the
  SPICE PNP block is set to
  `Device temperature`. For this model,
  the block defines temperature as

  T=TC+TOFFSET

  Where:

  - *TC* is the
    circuit temperature.

    If there is no Environment
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

1. If there is not an Environment
   Parameters block in the circuit, add one.
2. In the **SPICE** settings of the
   Environment Parameters block,
   specify the desired *GMIN* value for the
   **GMIN** parameter.

**Current-Voltage and Base Charge Model**

The current-voltage relationships and base charge relationships for the transistor are
described in terms of Base-Emitter and Base-Collector Junction Currents, Terminal Currents, and Base Charge Model. As applicable, the model parameters are first
adjusted for temperature.

**Base-Emitter and Base-Collector Junction Currents**

The base-emitter junction current depends on the emitter-base voltage,
*VEB* such that:

- When VEB>80\*VTF:

  Ibef = ISd\*((VEBVTF-79)\*e80 - 1)+Gmin\*VEB

  Ibee = ISEd\*((VEB-80\*VTF+VTE)\*e(80\*VTF/VTE)VTE - 1)
- When VEB≤80\*VTF:

  Ibef = ISd\*(e(VEB/VTF)-1)+ Gmin\*VEB

  Ibee = ISEd\*(e(VEB/VTE)-1)

The base-collector junction current depends on the collector-base
voltage, *VCB*, such that:

- When VCB>80\*VTR:

  Ibcr = ISd\*((VCBVTR-79)\*e80 - 1)+Gmin\*VCB

  Ibcc = ISCd\*((VCB-80\*VTR+VTC)\*e(80\*VTR/VTC)VTC - 1)
- When VCB≤80\*VTR:

  Ibcr = ISCd\*(e(VCB/VTR)−1)+Gmin\*VCB

  Ibcc = ISCd\*(e(VCB/VTC)-1)

Where:

- *VEB* is the emitter-base
  voltage.
- *VCB* is the
  collector-base voltage.
- *VTE* is the emitter
  thermal voltage, such that VTE=NE\*k\*T/q.
- *VTC* is the collector
  thermal voltage, such that VTC=NC\*k\*T/q.
- *VTF* is the forward
  thermal voltage, such that VTF=NF\*k\*T/q.
- *VTR* is the reverse
  thermal voltage, such that VTR=NR\*k\*T/q.
- *ISCd* is the
  geometry-adjusted base-collector leakage current.
- *ISEd* is the
  geometry-adjusted base-emitter leakage current.
- *NE* is the base-emitter emission
  coefficient.
- *NC* is the base-collector emission
  coefficient.
- *NF* is the forward emission coefficient.
- *NR* is the reverse emission coefficient.
- *q* is the elementary charge on an
  electron.
- *k* is the Boltzmann constant.
- *T* is the transistor temperature. For more
  information, see Transistor Temperature.
- *Gmin* is the minimum
  conductance. For more information, see Minimal Conduction.

**Terminal Currents**

The terminal currents are calculated as:

IB =− (IbefBF+Ibee+IbcrBR+Ibcc)

IC = −(Ibef-Ibcrqb-IbcrBR-Ibcc)

Where:

- *IB* is the base terminal
  current.
- *IC* is the collector
  terminal current.
- *BF* is the forward beta.
- *BR* is the reverse beta.

**Base Charge Model**

The base charge, *qb*, is calculated using these equations:

qb=q12(1+0.5((1+4q2 - eps)2 + eps2 + 1+4q2-eps)+eps)

q1=(1−VCBVAF−VEBVAR)−1

q2= IbefIKFd+IbcrIKRd

Where:

- *qb* is the base
  charge.
- *VAF* is the forward Early voltage.
- *VAR* is the reverse Early voltage.
- *IKFd* is the
  geometry-adjusted forward knee current.
- *IKRd* is the
  geometry-adjusted reverse knee current.
- *eps* is 1e-4.

**Base Resistance Model**

You can use these options to model base resistance,
*rbb*:

- If you use the default value of infinity for the **Half base resistance cur,
  IRB** parameter, the block calculates the base
  resistance as

  rbb = RBMd+RBd-RBMdqb

  Where:

  - *rbb* is base
    resistance.
  - *RBMd* is the
    geometry-adjusted minimum base resistance.
  - *RBd* is the
    geometry-adjusted zero-bias base resistance.
- If you specify a finite value for the **Half base resistance cur,
  IRB** parameter, the block calculates the base
  resistance as

  rbb = RBMd+3\*(RBd-RBMd)\*(tan z -zz\*tan2z)

  Where

  z=1+144IB/(π2IRBd)−1(24/π2)(IB/IRBd)

**Transit Charge Modulation Model**

If you specify nonzero values for the **Coefficient of TF, XTF**
parameter, the block models transit charge modulation by scaling the forward
transit time as

TFmod=TF\*[1+XTF\*eVCB/(1.44VTF)(IEBIEB+ITFd)2]qb

Where *ITFd* is the
geometry-adjusted coefficient of the forward transit time.

**Junction Charge Model**

The block lets you model junction charge. The base-collector charge,
*Qbc*, and the base-emitter
charge, *Qbe*, depend on an intermediate
value, *Qdep*. As applicable, the model
parameters are first adjusted for temperature.

- For the internal base-emitter junctions

  Qbe=TFmod\*Ibe+Qdep
- For the internal base-collector junctions

  Qbc=TR\*Ibc+XCJC\*Qdep
- For the external base-collector junctions

  Qbextc=(1−XCJC)\*Qdep

*Qdep* depends on the
junction voltage, *Vjct*
(*VBE* for the base-emitter
junction and *VBC* for the
base-collector junction), as follows.

| Applicable Range of *Vjct* Values | Corresponding *Qdep* Equation |
| --- | --- |
| Vjct<FC\*VJ | Qdep=Cjct\*VJ\*1-(1-Vjct/VJ)(1−MJ)1−MJ |
| Vjct≥FC\*VJ | Qdep=Cjct\*[F1+F3\*(Vjct-FC\*VJ)+MJ\*[Vjct2-(FC\*VJ)2]2\*VJF2] |

Where:

- *FC* is the capacitance coefficient.
- *VJ* is:

  - The base-emitter built-in potential,
    *VJE*, for the base-emitter
    junction.
  - The base-collector built-in potential,
    *VJC*, for the base-collector
    junction.
- *MJ* is:

  - The base-emitter exponential factor,
    *MJE*, for the base-emitter
    junction.
  - The base-collector exponential factor,
    *MJC*, for the base-collector
    junction.
- *Cjct* is:

  - The geometry-adjusted base-emitter depletion
    capacitance,
    *CJEd*, for
    the base-emitter junction.
  - The geometry-adjusted base-collector depletion
    capacitance,
    *CJCd*, for
    the base-collector junction.
- F1=VJ\*(1-(1-FC)(1−MJ))/(1−MJ)
- F2=(1-FC)(1+MJ)
- F3=1-FC\*(1+MJ)

The collector-substrate charge, *Qcs*, depends on
the substrate-collector voltage, *Vsc*.
As applicable, the model parameters are first adjusted for
temperature.

| Applicable Range of *Vsc* Values | Corresponding *Qcs* Equation |
| --- | --- |
| Vsc<0 | Qcs=CJSd\*VJS\*(1-(1-Vsc/VJS)(1−MJS)1−MJS) |
| Vsc≥0 | Qcs=CJSd\*(1+MJS\*Vsc/(2\*VJS))\*Vsc |

Where:

- *CJSd* is the
  geometry-adjusted collector-substrate junction capacitance.
- *VJS* is the substrate built-in potential.
- *MJS* is the substrate exponential factor.

**Temperature Dependence**

The relationship between the saturation current,
*ISd*, and the transistor
temperature, *T*, is

IS(T)=ISd\*(T/Tmeas)XTI\*e(TTmeas−1)\*EGVt

Where:

- *ISd* is the
  geometry-adjusted transport saturation current.
- *Tmeas* is the parameter
  extraction temperature.
- *XTI* is the transport saturation current
  temperature exponent.
- *EG* is the energy gap.
- *Vt = kT/q*.

The relationship between the base-emitter junction potential, *VJE*, and
the transistor temperature, *T*, is

VJE(T)=VJE\*(TTmeas)-3\*k\*Tq\*log(TTmeas)-(TTmeas)\*EGTmeas+EGT

Where:

- *VJE* is the base-emitter built-in
  potential.
- EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
- EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

The block uses the *VJE(T)* equation to
calculate the base-collector junction potential by substituting
*VJC*, the base-collector built-in potential, for
*VJE*.

The relationship between the base-emitter junction capacitance, *CJE*,
and the transistor temperature, *T*, is

CJE(T) = CJEd\*[1+MJE\*(400e−6\*(T-Tmeas)-VJE(T)-VJEVJE)]

Where:

- *CJEd* is the
  geometry-adjusted base-emitter depletion capacitance.
- *MJE* is the base-emitter exponential
  factor.

The block uses the *CJE(T)* equation to
calculate the base-collector junction capacitance by substituting
*CJCd*, geometry-adjusted
base-collector depletion capacitance, for
*CJEd* and *MJC*,
base-collector exponential factor, for *MJE*.

The relationship between the forward and reverse beta and the transistor temperature,
*T*, is

β(T)=β\*(TTmeas)XTB

Where:

- *β* is the forward beta or reverse beta.
- *XTB* is the beta temperature exponent.

The relationship between the base-emitter leakage current, *ISE*, and the
transistor temperature, *T*, is

ISE(T)=ISEd\*(TTmeas)-XTB \* (IS(T)ISd)1/NE

Where:

- *ISEd* is the
  geometry-adjusted base-emitter leakage current.
- *NE* is the base-emitter emission
  coefficient.

The block uses this equation to calculate the base-collector
leakage current by substituting, *ISCd*,
the geometry-adjusted base-collector leakage current for
*ISEd* and
*NC*, the base-collector emission coefficient, for
*NE*.
