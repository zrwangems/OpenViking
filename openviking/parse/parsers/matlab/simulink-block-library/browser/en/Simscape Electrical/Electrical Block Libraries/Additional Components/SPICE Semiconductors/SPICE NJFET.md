---
type: simulink-block
title: 'SPICE NJFET'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Semiconductors'
documentation_page: 'spicenjfet'
documentation_source_path: 'ref/spicenjfet.html'
language: en
---

# SPICE NJFET

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

## Parameters

### Main

### **Device area, AREA** — Device area `1.0` `m^2` (default) | positive scalar

Transistor area. The value must be greater than `0`.

### **Number of parallel devices, SCALE** — Number of parallel devices `1` (default) | positive integer

Number of parallel transistors the block represents. The value must be an integer
greater than `0`.

### **Threshold voltage, VTO** — Threshold voltage `-2` `V` (default) | scalar

Gate-source voltage above which the transistor produces a nonzero drain current.

### **Transconductance, BETA** — Channel modulation `1e-4` `A/m^2/V^2` (default) | nonnegative scalar

Derivative of drain current with respect to gate voltage. The value must be greater than
or equal to `0`.

### **Channel modulation, LAMBDA** — Channel modulation `0` `1/V` (default) | scalar

Channel modulation.

### **Saturation current, IS** — Saturation current `1e-14` `A/m^2` (default) | nonnegative scalar

Magnitude of the current that the gate-current equation approaches asymptotically for
very large reverse bias levels. The value must be greater than or equal
to `0`.

### **Drain resistance, RD** — Series resistance `0.01` `m^2*Ohm` (default) | nonnegative scalar

Transistor drain resistance. The value must be greater than or equal to
`0`.

### **Source resistance, RS** — Series resistance `0.0001` `m^2*Ohm` (default) | nonnegative scalar

Transistor source resistance. The value must be greater than or equal to
`0`.

### **Emission coefficient, N** — Emission coefficient `1` (default) | positive scalar

Transistor emission coefficient or ideality factor. The value must be
greater than `0`.

### Junction Capacitance

### **Model junction capacitance** — Junction capacitance model `No` (default) | `Yes`

Options for modeling the junction capacitance:

- `No` — Do not include
  junction capacitance in the model.
- `Yes` — Specify zero-bias
  junction capacitance, junction potential, grading
  coefficient, forward-bias depletion capacitance coefficient,
  and transit time.

#### Dependencies

Selecting `Yes` exposes related
parameters.

### **Zero-bias GS capacitance, CGS** — Zero-bias junction capacitance `0` `F/m^2` (default) | nonnegative scalar

Value of the capacitance placed between the gate and the source. The value must be
greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Zero-bias GD capacitance, CGD** — Zero-bias junction capacitance `0` `F/m^2` (default) | nonnegative scalar

Value of the capacitance placed between the gate and the drain. The value must be
greater than or equal to `0`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Junction potential, VJ** — Junction potential `1` `V` (default) | *VJ* > 0.01 | scalar

Junction potential, *VJ*. The value must be greater
than `0.01`
`V`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

### **Grading coefficient, M** — Grading coefficient `0.5` (default) | 0 < *M* < 0.9 | scalar

Grading coefficient, *M*. The value must be greater
than `0` and less than `0.9`.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

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

- `No` — Do not specify an
  initial condition for the model.
- `Yes` — Specify the
  initial transistor voltage.

  **Note**

  The SPICE NJFET block
  applies the initial transistor voltage across the
  junction capacitors and not across the ports.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** parameter.

Selecting `Yes` for this parameter exposes the
**Initial condition voltage, ICVDS** and
**Initial condition voltage, ICVGS**
parameters.

### **Initial condition voltage, ICVDS** — Initial voltage `0` `V` (default) | scalar

Drain-source voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** and `Yes` for
the **Specify initial condition** parameter.

### **Initial condition voltage, ICVGS** — Initial voltage `0` `V` (default) | scalar

Gate-source voltage at the start of the simulation.

#### Dependencies

This parameter is only visible when you select
`Yes` for the **Model junction
capacitance** and `Yes` for
the **Specify initial condition** parameter.

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

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `0` (default) | positive scalar

Order of the exponential increase in the saturation current as
temperature increases. The value must be greater than
`0`.

### **Activation energy, EG** — Activation energy `1.11` `eV` (default) | *EG* *≥* 0.1 | scalar

Transistor activation energy. The value must be greater than or equal
to `0.1`.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default) | positive scalar

Transistor simulation temperature. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when you select `Fixed
temperature` for the **Model temperature
dependence using** parameter.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default) | positive scalar

Temperature at which the transistor parameters are measured. The value must be greater
than `0`.

### **Offset local circuit temperature, TOFFSET** — Local circuit temperature offset `0` `K` (default) | scalar

Amount by which the transistor temperature differs from the circuit temperature.

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

**Introduced in R2008a**

## Description

SPICE-compatible N-Channel JFET

The SPICE NJFET block represents a SPICE-compatible N-channel
junction field-effect transistor (NJFET). If the voltage applied to the gate port,
**gx**, is less than the voltage applied to the source port,
**sx**, the current between the source port and drain port,
**dx**, is reduced.

SPICE, or Simulation Program with Integrated Circuit Emphasis,
is a simulation tool for electronic circuits. You can convert some SPICE subcircuits into
equivalent Simscape™
Electrical™ models using the Environment Parameters block and
SPICE-compatible blocks from the Additional Components library. For more
information, see `subcircuit2ssc`.

### Equations

Variables for the SPICE NJFET block equations include:

- Variables that you define by specifying parameters for the
  SPICE NJFET block. The visibility of
  some of the parameters depends on the value that you set for other
  parameters. For more information, see Parameters.
- Geometry-adjusted variables, which depend on several values that you
  specify using parameters for the SPICE
  NJFET block. For more information, see Geometry-Adjusted Variables.
- Temperature, *T*, which is `300.15`
  `K` by default. You can use a different value
  by specifying parameters for the SPICE
  NJFET block or by specifying parameters for both the
  SPICE NJFET block and an
  Environment
  Parameters block. For more information, see Transistor Temperature.
- Temperature-dependent variables. For more information, see Temperature Dependence.
- Minimal conductance, *GMIN*, which is
  `1e-12`
  `1/Ohm` by default. You can use a different
  value by specifying a parameter for an Environment
  Parameters block. For more information, see Minimal Conduction.

**Geometry-Adjusted Variables**

Several variables in the equations for the N-channel junction field-effect transistor
model consider the geometry of the device that the block represents. These
geometry-adjusted variables depend on variables that you define by specifying
SPICE NJFET block parameters. The
geometry-adjusted variables depend on these variables:

- *AREA* — Area of the device
- *SCALE* — Number of parallel connected
  devices
- The associated unadjusted variable

The table includes the geometry-adjusted variables and the
defining equations.

| Variable | Description | Equation |
| --- | --- | --- |
| *BETAd* | Geometry-adjusted transconductance | BETAd=BETA\*AREA\*SCALE |
| *CGDd* | Geometry-adjusted zero-bias gate-drain capacitance | CGDd=CGD\*AREA\*SCALE |
| *CGSd* | Geometry-adjusted zero-bias gate-source capacitance | CGSd=CGS\*AREA\*SCALE |
| *ISd* | Geometry-adjusted saturation current | ISd=IS\*AREA\*SCALE |
| *RSd* | Geometry-adjusted source resistance | RSd=RSAREA\*SCALE |
| *RDd* | Geometry-adjusted drain resistance | RDd=RDAREA\*SCALE |

**Transistor Temperature**

You can use these options to define transistor temperature, *T*:

- Fixed temperature — The block uses a temperature that is
  independent of the circuit temperature when the **Model
  temperature dependence using** parameter in the
  **Temperature** settings of the
  SPICE NJFET block is set to
  `Fixed temperature`. For this model,
  the block sets *T* equal to
  *TFIXED*.
- Device temperature — The block uses a temperature that depends on circuit
  temperature when the **Model temperature dependence
  using** parameter in the
  **Temperature** settings of the
  SPICE NJFET block is set to
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

1. If there is not an Environment
   Parameters block in the transistor circuit, add
   one.
2. In the **SPICE** settings of the
   Environment Parameters block,
   specify the desired *GMIN* value for the
   **GMIN** parameter.

**Gate-Source Current-Voltage Model**

This table shows the equations that define the relationship between the gate-source
current, *Igs*, and the gate-source
voltage, *Vgs*. As applicable, the model
parameters are first adjusted for temperature. For more information, see Temperature Dependence.

| Applicable Range of *Vgs* Values | Corresponding *Igs* Equation |
| --- | --- |
| Vgs>80\*Vt | Igs=ISd\*((VgsVt−79)e80−1)+Vgs\*Gmin |
| 80\*Vt≥Vgs | Igs=ISd\*(eVgs/Vt−1)+Vgs\*Gmin |

Where:

- *ISd* is the
  geometry-adjusted saturation current.
- *Vt* is the thermal
  voltage, such that Vt=ND\*k\*T/q.
- *ND* is the emission
  coefficient.
- *q* is the elementary charge on an
  electron.
- *k* is the Boltzmann constant.
- *T* is the transistor temperature. For more
  information, see Transistor Temperature
- *GMIN* is the transistor minimum conductance. or
  more information, see Minimal Conduction

**Gate-Drain Current-Voltage Model**

This table shows the relationship between the gate-drain current,
*Igd*, and the gate-drain
voltage, *Vgd*. As applicable, model
parameters are first adjusted for temperature.

| Applicable Range of *Vgd* Values | Corresponding *Igd* Equation |
| --- | --- |
| Vgd>80\*Vt | Igd=ISd\*((VgdVt−79)e80−1)+Vgd\*Gmin |
| 80\*Vt≥Vgd | Igd=ISd\*(eVgd/Vt−1)+Vgd\*Gmin |

**Drain-Source Current-Voltage Model**

This table shows the relationship between the drain-source current,
*Ids*, and the drain-source
voltage, *Vds*, in normal mode (Vds≥0). As applicable, model parameters are first adjusted for
temperature.

| Applicable Range of *Vgs* and *Vgd* Values | Corresponding *Ids* Equation |
| --- | --- |
| Vgs-Vto≤0 | Ids=0 |
| 0<Vgs-Vto≤Vds | Ids=βd(Vgs−Vto)2(1+λVds) |
| 0<Vds<Vgs-Vto | Ids=βdVds(2(Vgs-Vto)-Vds)(1+λVds) |

Where:

- *Vto* is the threshold
  voltage.
- *βd* is the
  geometry-adjusted transconductance.
- *λ* is the channel modulation.

This table shows the relationship between the drain-source current,
*Ids*, and the drain-source
voltage, *Vds*, in inverse mode (Vds<0). As applicable, model parameters are first adjusted for
temperature.

| Applicable Range of *Vgs* and *Vgd* Values | Corresponding *Ids* Equation |
| --- | --- |
| Vgd-Vto≤0 | Ids=0 |
| 0<Vgd-Vto≤−Vds | Ids=−βd(Vgd−Vto)2(1−λVds) |
| 0<−Vds<Vgd-Vto | Ids=βdVds(2(Vgd-Vto)+Vds)(1−λVds) |

**Junction Charge Model**

This table shows the relationship between the gate-source charge,
*Qgs*, and the gate-source
voltage, *Vgs*. As applicable, model
parameters are first adjusted for temperature.

| Applicable Range of *Vgs* Values | Corresponding *Qgs* Equation |
| --- | --- |
| Vgs<FC\*VJ | Qgs=CGSd\*VJ\*(1-(1-VgsVJ)1−MG)1−MG |
| Vgs≥FC\*VJ | Qgs=CGSd\*(F1+F3\*(Vgs-FC\*VJ)+MG\*(Vgs2-(FC\*VJ)2)2\*VJF2) |

Where:

- *FC* is the capacitance coefficient.
- *VJ* is the junction potential.
- *CGSd* is the zero-bias
  gate-source capacitance.
- *MG* is the grading coefficient.
- F1=VJ\*(1-(1-FC)1−MG)1−MG
- F2=(1-FC)1+MG
- F3=1-FC\*(1+MG)

This table shows the relationship between the gate-drain charge,
*Qgd*, and the gate-drain
voltage, *Vgd*. As applicable, model
parameters are first adjusted for temperature.

| Applicable Range of *Vgd* Values | Corresponding *Qgd* Equation |
| --- | --- |
| Vgd<FC\*VJ | Qgd=CGDd\*VJ\*(1-(1-VgdVJ)1−MG)1−MG |
| Vgd≥FC\*VJ | Qgd=CGDd\*(F1+F3\*(Vgd-FC\*VJ)+MG\*(Vgd2-(FC\*VJ)2)2\*VJF2) |

Where *CGDd* is the
geometry-adjusted zero-bias gate-drain capacitance.

**Temperature Dependence**

The block provides this relationship between the saturation current *IS*
and the transistor temperature *T*:

IS(T)=ISd\*(T/Tmeas)XTIND\*e(TTmeas−1)\*EGVt

Where:

- *ISd* is the
  geometry-adjusted saturation current.
- *Tmeas* is the parameter
  extraction temperature.
- *XTI* is the saturation current temperature
  exponent.
- *EG* is the energy gap.
- *Vt* is the thermal
  voltage, such that Vt=ND\*k\*T/q.
- *ND* is the emission
  coefficient.

The relationship between the junction potential, *VJ*, and the transistor
temperature *T* is

VJ(T)=VJ\*(TTmeas)-3\*k\*Tq\*log(TTmeas)-(TTmeas)\*EGTmeas+EGT

Where:

- *VJ* is the junction potential.
- EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
- EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

The relationship between the gate-source junction capacitance, *CGS*, and
the transistor temperature, *T*:

CGS(T) = CGSd\*[1+MG\*(400e−6\*(T-Tmeas)-VJ(T)-VJVJ)]

Where *CGSd* is the
geometry-adjusted zero-bias gate-source capacitance.

The block uses the *CGS(T)* equation to calculate the
gate-drain junction capacitance by substituting
*CGDd*, the zero-bias gate-drain
capacitance, for *CGSd*.

The relationship between the transconductance, *β*, and the transistor
temperature *T* is

β(T)=βd\*(TTmeas)

Where *βd* is the
geometry-adjusted transconductance.
