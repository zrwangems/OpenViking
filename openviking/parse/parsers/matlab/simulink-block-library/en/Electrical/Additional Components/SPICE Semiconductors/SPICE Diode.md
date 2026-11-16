---
type: simulink-block
title: 'SPICE Diode'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicediode'
documentation_source_path: 'ref/spicediode.html'
language: en
---

# SPICE Diode

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with positive voltage.

### **-** — Negative voltage electrical

Electrical conserving port associated with negative voltage.

## Parameters

### Main

### **Device area, AREA** — Device area `1.0` `m^2` (default) | positive scalar

Diode area. The value must be greater than `0`.

### **Number of parallel devices, SCALE** — Number of parallel devices `1` (default) | positive scalar

Number of parallel diodes that the block represents. The value must be greater than
`0`.

### **Saturation current, IS** — Saturation current `1e-14` `A/m^2` (default) | nonnegative scalar

Magnitude of the current that the ideal diode equation approaches asymptotically for
very large reverse bias levels. The value must be greater than or equal
to `0`.

### **High-injection knee current, IKF** — High-injection knee current `Inf` `A/m^2` (default) | scalar

Current value at which forward-beta high-current roll-off occurs. The
value must be greater than or equal to `0`.

### **Recombination current parameter, ISR** — Recombination current `0` `A/m^2` (default) | scalar

Magnitude of the current generated from the process of the
recombination of electrons and holes inside the junction.

### **Emission coefficient, N** — Emission coefficient `1` (default) | positive scalar

Diode emission coefficient or ideality factor. The value must be
greater than `0`.

### **Emission coefficient for ISR, NR** — Emission coefficient for ISR `2` (default) | positive scalar

Diode emission coefficient for the recombination current. The value
must be greater than `0`.

### **Grading coefficient, M** — Grading coefficient `0.5` (default) | 0 < *M* < 0.9 | scalar

Grading coefficient, *M*. The value must be greater
than `0` and less than `0.9`.

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

### **Ohmic resistance, RS** — Series resistance `0.01` `m^2*Ohm` (default) | nonnegative scalar

Series diode connection resistance. The value must be greater than or equal to
`0`.

### Junction Capacitance

### **Model junction capacitance** — Junction capacitance model `No` (default) | `Yes`

Options for modeling the junction capacitance:

- `No` — Do not include
  junction capacitance in the model.
- `Yes` — Specify zero-bias
  junction capacitance, junction potential, grading
  coefficient, forward-bias depletion capacitance coefficient,
  and transit time.

### **Zero-bias junction capacitance, CJO** — Zero-bias junction capacitance `0` `F/m^2` (default) | nonnegative scalar

Value of the capacitance placed in parallel with the exponential diode term. The value
must be greater than or equal to `0`.

#### Dependencies

To enable this parameter, set **Model junction capacitance** to
`Yes`.

### **Capacitance coefficient, FC** — Capacitance coefficient `0.5` (default) | 0 ≤ *FC* < 0.95 | scalar

Fitting coefficient,, *FC*, that quantifies the decrease of the
depletion capacitance with applied voltage. The value must be greater
than or equal to `0` and less than
`0.95`.

#### Dependencies

To enable this parameter, set **Model junction
capacitance** to `Yes`.

### **Transit time, TT** — Transit time `0` `s` (default) | nonnegative scalar

Transit time, *TT*, of the carriers that cause diffusion capacitance.
The value must be greater than or equal to `0`.

#### Dependencies

To enable this parameter, set **Model junction
capacitance** to `Yes`.

### **Specify initial condition** — Initial condition model `No` (default) | `Yes`

Options for specifying initial conditions:

- `No` — Do not specify an
  initial condition for the model.
- `Yes` — Specify the
  initial diode voltage.

  **Note**

  The SPICE Diode block
  applies the initial diode voltage across the junction
  capacitors and not across the ports.

#### Dependencies

To enable this parameter, set **Model junction
capacitance** to `Yes`.

### **Initial condition voltage, V0** — Initial voltage `0` `V` (default) | scalar

Diode voltage at the start of the simulation.

**Note**

The block applies the initial condition across the diode junction,
so the initial condition is only effective when charge storage is
included, that is, when one or both of the **Zero-bias
junction capacitance, CJO** and **Transit time,
TT** parameters are greater than zero.

#### Dependencies

To enable this parameter, set **Model junction
capacitance** and **Specify initial
condition** to `Yes`.

### Reverse Breakdown

### **Model reverse breakdown** — Reverse breakdown model `No` (default) | `Yes`

Options for modeling reverse breakdown:

- `No` — Do not model
  reverse breakdown.
- `Yes` — Introduce a second
  exponential term to the diode I-V relationship, thereby
  modeling a rapid increase in conductance as the breakdown
  voltage is exceeded.

### **Reverse breakdown voltage, BV** — Reverse breakdown threshold voltage `Inf` `V` (default) | nonnegative scalar

If voltage drops below this value, the block models the rapid increase
in conductance that occurs at diode breakdown. The value must be greater
than or equal to `0`.

#### Dependencies

To enable this parameter, set **Model reverse breakdown** to
`Yes`.

### **Reverse breakdown current, IBV** — Reverse breakdown current `1e-10` `A/m^2` (default) | positive scalar

Diode current that corresponds to the voltage specified for the
**Reverse breakdown voltage, BV** parameter. The
value must be greater than `0`.

#### Dependencies

To enable this parameter, set **Model reverse
breakdown** to `Yes`.

### **Low-level reverse breakdown knee current, IBVL** — Low-level reverse breakdown knee current `0` `A/m^2` (default) | positive scalar

Low-level reverse breakdown knee current.

#### Dependencies

To enable this parameter, set **Model reverse
breakdown** to `Yes`.

### **Reverse breakdown ideality factor, NBV** — Reverse breakdown ideality factor `1` (default) | positive scalar

Ideality factor for the **Reverse breakdown voltage,
BV**.

#### Dependencies

To enable this parameter, set **Model reverse
breakdown** to `Yes`.

### **Low-level reverse breakdown ideality factor, NBVL** — Low-level reverse breakdown ideality factor `1` (default) | positive scalar

Ideality factor for the **Low-level reverse breakdown knee
current, IBVL**

#### Dependencies

To enable this parameter, set **Model reverse
breakdown** to `Yes`.

### Temperature

### **Model temperature dependence using** — Temperature dependence model `Device temperature` (default) | `Fixed temperature`

Select one of these options for modeling the diode temperature dependence:

- `Device temperature` — Use
  the device temperature to model temperature
  dependence.
- `Fixed temperature` — Use
  a temperature that is independent of the circuit temperature
  to model temperature dependence.

For more information, see Diode Temperature.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3.0` (default) | positive scalar

Order of the exponential increase in the saturation current as
temperature increases. The value must be greater than
`0`.

### **Activation energy, EG** — Activation energy `1.11` `eV` (default) | *EG* *≥* 0.1 | scalar

Diode activation energy. The value must be greater than or equal to
`0.1`
`eV`.

### **IKF temperature coefficient (linear), TIKF** — Temperature coefficient for IKF `0` `1/K` (default) | positive scalar

Linear temperature coefficient for the **High-injection knee
current, IKF**.

### **RS temperature coefficient (linear), TRS1** — Temperature coefficient for RS `0` `1/K` (default) | positive scalar

Linear temperature coefficient for the **Ohmic resistance,
RS**.

### **RS temperature coefficient (quadratic), TRS2** — Temperature coefficient for RS `0` `1/K^2` (default) | positive scalar

Quadratic temperature coefficient for the **Ohmic resistance,
RS**.

### **BV temperature coefficient (linear), TBV1** — Temperature coefficient for BV `0` `1/K` (default) | positive scalar

Linear temperature coefficient for the **Breakdown voltage,
BV**.

### **BV temperature coefficient (quadratic), TBV2** — Temperature coefficient for BV `0` `1/K^2` (default) | positive scalar

Quadratic temperature coefficient for the **Breakdown voltage,
BV**.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default) | positive scalar

Diode simulation temperature. The value must be greater than `0`
`K`.

#### Dependencies

To enable this parameter, set **Model temperature dependence using**
to `Fixed temperature`.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default) | positive scalar

Temperature at which the diode parameters are measured. The value must be greater than
`0`
`K`.

### **Offset local circuit temperature, TOFFSET** — Local circuit temperature offset `0` `K` (default) | scalar

Amount by which the diode temperature differs from the circuit temperature.

#### Dependencies

To enable this parameter, set **Model temperature
dependence using** to `Device
temperature`.

## Libraries

Simscape / Electrical / Additional Components / SPICE Semiconductors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

SPICE-compatible diode

The SPICE Diode block represents a SPICE-compatible
diode.

SPICE, or Simulation Program with Integrated Circuit Emphasis,
is a simulation tool for electronic circuits. You can convert some SPICE subcircuits into
equivalent Simscape™
Electrical™ models using the Environment Parameters block and
SPICE-compatible blocks from the Additional Components library. For more
information, see `subcircuit2ssc`.

### Equations

Variables for the SPICE Diode block equations include:

- Variables that you define by specifying parameters for the
  SPICE Diode block. The visibility of
  some of the parameters depends on the value that you set for other
  parameters. For more information, see Parameters.
- Geometry-adjusted variables, which depend on several values that you
  specify using parameters for the SPICE
  Diode block. For more information, see Geometry-Adjusted Variables.
- Temperature, *T*, which is `300.15`
  `K` by default. You can use a different value
  by specifying parameters for the SPICE
  Diode block or by specifying parameters for both the
  SPICE Diode block and an
  Environment
  Parameters block. For more information, see Diode Temperature.
- Temperature-dependent variables. For more information, see Temperature Dependence.
- Minimal conductance, *GMIN*, which is
  `1e–12`
  `1/Ohm` by default. You can use a different
  value by specifying a parameter for an Environment
  Parameters block. For more information, see Minimal Conduction.
- Thermal voltage, *Vt*. For
  more information, see Thermal Voltage.

**Geometry-Adjusted Variables**

Several variables in the equations for the SPICE diode model consider the geometry of the
device that the block represents. These geometry-adjusted variables depend on
variables that you define by specifying SPICE
Diode block parameters. The geometry-adjusted variables
depend on these variables:

- *AREA* — Area of the device
- *SCALE* — Number of parallel connected
  devices
- The associated unadjusted variable

The table includes the geometry-adjusted variables and the
defining equations.

| Variable | Description | Equation |
| --- | --- | --- |
| *CJOd* | Geometry-adjusted zero-bias junction capacitance | CJOd=CJO\*AREA\*SCALE |
| *IBVd* | Geometry-adjusted reverse breakdown current | IBVd=IBV\*AREA\*SCALE |
| *ISd* | Geometry-adjusted saturation current | ISd=IS\*AREA\*SCALE |
| *RSd* | Geometry-adjusted series resistance | RSd=RSAREA\*SCALE |

**Diode Temperature**

You can use these options to define diode temperature, *T*:

- Fixed temperature — The block uses a temperature that is
  independent from the circuit temperature when the **Model
  temperature dependence using** parameter in the
  **Temperature** settings of the
  Spice Diode block is set to
  `Fixed temperature`. For this model,
  the block sets *T* equal to
  *TFIXED*.
- Device temperature — The block uses a temperature that
  depends on circuit temperature when the **Model temperature
  dependence using** parameter in the
  **Temperature** settings of the
  Spice Diode block is set to
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
    **Spice** settings of the
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
   Parameters block in the diode circuit, add
   one.
2. In the **Spice** settings of the
   Environment Parameters block,
   specify the desired *GMIN* value for the
   **GMIN** parameter.

**Thermal Voltage**

Thermal voltage, *Vt*, is defined by
the equation

Vt=Nk\*Tq

Where:

- *N* is the emission
  coefficient.
- *T* is the diode temperature. For
  more information, see Diode Temperature.
- *k* is the Boltzmann constant.
- *q* is the elementary charge on an
  electron.

**Current-Voltage Equations**

These equations define the relationship between the diode current,
*Id*, and the diode voltage,
*Vd*. As applicable, the model
parameters are first adjusted for temperature. For more information, see Temperature Dependence.

Id=AREA\*(Ifwd−Irev)

Ifwd=Inrm\*Kinj+Irec\*Kgen

Irev=Irevh+Irevl

Inrm=ISeVd/(N\*Vt)−1

Irec=ISReVd/(NR\*Vt)−1

Kinj=(IKFIKF+Inrm)0.5

Kgen=[(1−VdVJ)2+0.005]M2

Irevh=IBV\*e−Vd+BVNBV\*Vt

Irevl=IBVL\*e−Vd+BVNBVL\*Vt

Where:

- *Ifwd* is the forward
  current.
- *Irev* is the reverse
  current.
- *Inrm* is the normal
  current.
- *Irec* is the
  recombination current.
- *Kinj* is the
  high-injection factor.
- *Kgen* is the generation
  factor.
- *Irevh* is the high-level
  breakdown current.
- *Irevl* is the low-level
  breakdown current.
- *Vt* is thermal voltage.
  For more information, see Thermal Voltage.
- *IS* is the saturation
  current.
- *ISR* is the recombination
  current.
- *IKF* is the forward knee current.
- *VJ* is the junction potential.
- *N* is the emission coefficient.
- *NR* is the reverse emission coefficient.
- *NBV* is the reverse breakdown emission
  coefficient.
- *NBVL* is the low-level reverse breakdown
  ideality factor.
- *M* is the grading coefficient.
- *BV* is the reverse breakdown voltage.
- *IBV* is the reverse breakdown current.
- *IBVL* is the low-level reverse breakdown knee
  current.

**Junction Charge Model**

The table shows the equations that define the relationship between the diode charge
*Qd*, and the diode voltage,
*Vd*. As applicable, the model
parameters are first adjusted for temperature. For more information, see Temperature Dependence.

| *Vd* Range | *Qd* Equation |
| --- | --- |
| Vd<FC\*VJ | Qd=TT\*AREA\*Ifwd+CJOd\*VJ\*1−(1−VdVJ)1−M1−M |
| Vd≥FC\*VJ | Qd=TT\*AREA\*Ifwd+          CJOd\*(F1+F3\*(Vd-FC\*VJ)+(M2\*VJ)\*(Vd2-(FC\*VJ)2)F2)​ |

Where:

- *FC* is the forward bias depletion capacitance
  coefficient.
- *VJ* is the junction potential.
- *TT* is the transit time.
- *CJOd* is the
  geometry-adjusted zero-bias junction capacitance. For more
  information, see Geometry-Adjusted Variables.
- *M* is the grading coefficient.
- F1=VJ\*(1-(1-FC)(1-M))/(1-M)
- F2=(1-FC)(1+M)
- F3=1-FC\*(1+M)

**Temperature Dependence**

The relationship between the geometry-adjusted saturation current and the
diode temperature is

ISd(T)=ISd\*(T/TMEAS)XTIN\*e(TTMEAS−1)\*EGN\*Vt

Where:

- *ISd* is the
  geometry-adjusted saturation current. For more information, see
  Geometry-Adjusted Variables.
- *T* is the diode temperature. For more
  information, see Diode Temperature.
- *TMEAS* is the parameter extraction
  temperature.
- *XTI* is the saturation current temperature
  exponent.
- *N* is the emission coefficient.
- *EG* is the activation energy.
- *Vt* is thermal voltage.
  For more information, see Thermal Voltage.

The relationship between the recombination current and the diode temperature is

ISR(T)=ISR\*(TTMEAS)XTINR\*e(TTMEAS−1)\*EGNR\*Vt

Where:

- *ISR* is the recombination current.
- *NR* is the reverse emission coefficient.

The relationship between the forward knee current and the diode temperature is

IKF(T)=IKF\*[1+TIKF\*(T−TMEAS)]

Where:

- *IKF* is the forward knee current.
- *TIKF* is the linear IKF temperature
  coefficient.

The relationship between the breakdown voltage and the diode temperature is

BV(T)=BV\*[1+TBV1\*(T−TMEAS)+TBV2\*(T−TMEAS)2]

Where:

- *BV* is the breakdown voltage.
- *TBV1* is the linear BV temperature
  coefficient.
- *TBV2* is the quadratic BV temperature
  coefficient.

The relationship between the ohmic resistance and the diode temperature is

RS(T)=RS\*[1+TRS1\*(T−TMEAS)+TRS2\*(T−TMEAS)2]

Where:

- *RS* is the ohmic resistance.
- *TRS1* is the linear RS temperature
  coefficient.
- *TRS2* is the quadratic RS temperature
  coefficient.

The relationship between the junction potential and the diode temperature is

VJ(T)=VJ\*(TTMEAS)-3\*Vt\*ln(TTMEAS)-(TTMEAS)\*EGTMEAS+EGT

Where:

- *VJ* is the junction potential.
- *EGTMEAS* is the
  activation energy for the temperature at which the diode parameters
  were measured. The defining equation is EGTMEAS=1.16eV-(7.02e-4\*TMEAS2)/(TMEAS+1108).
- *EGT* is the activation
  energy for the diode temperature. The defining equation is EGT=1.16eV-(7.02e-4\*T2)/(T+1108).

The relationship between the geometry-adjusted diode zero-bias junction
capacitance and the diode temperature is

CJOd(T) = CJOd\*[1+M\*(400e−6\*(T-TMEAS)-VJ(T)-VJVJ)]

Where:

- *CJOd* is the
  geometry-adjusted zero-bias junction capacitance. For more
  information, see Geometry-Adjusted Variables.
- *M* is the grading coefficient.
