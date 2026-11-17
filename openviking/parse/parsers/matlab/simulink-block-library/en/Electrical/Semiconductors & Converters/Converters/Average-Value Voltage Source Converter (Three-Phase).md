---
type: simulink-block
title: 'Average-Value Voltage Source Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluevoltagesourceconverterthreephase'
documentation_source_path: 'ref/averagevaluevoltagesourceconverterthreephase.html'
language: en
---

# Average-Value Voltage Source Converter (Three-Phase)

## Ports
```yaml
ports:
- name: ModWave
  summary: Modulation wave vector
  direction: input
- name: Vt
  summary: Phase-to-phase RMS voltage scalar
  direction: input
- name: ph
  summary: Phase shift scalar
  direction: input
- name: '~'
  summary: Voltage electrical
  direction: conserving
- name: a
  summary: '*a*-phase electrical'
  direction: conserving
- name: b
  summary: '*b*-phase electrical'
  direction: conserving
- name: c
  summary: '*c*-phase electrical'
  direction: conserving
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Input

### **ModWave** — Modulation wave vector

Physical signal input port associated with the normalized modulation
wave.

#### Dependencies

To enable this port, set **Input type** to
`Modulation wave`.

### **Vt** — Phase-to-phase RMS voltage scalar

*Since R2024a*

Physical signal input port associated with the phase-to-phase RMS
voltage.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase
shift`.

### **ph** — Phase shift scalar

*Since R2024a*

Physical signal input port associated with the phase shift.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase
shift`.
### Conserving

### **~** — Voltage electrical

Expandable electrical conserving port associated with voltage. For
more information, see three-phase
port.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
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
- name: Electrical connection
  summary: Electrical connection Composite three-phase ports (default) | Expanded three-phase ports
  group: ''
- name: AC frequency
  summary: AC frequency Variable (default) | Constant
  group: ''
- name: Input type
  summary: Type of input Modulation wave (default) | Sinusoidal magnitude and phase shift
  group: ''
- name: Rated electrical frequency
  summary: Rated electrical frequency 60 Hz | scalar
  group: ''
- name: Losses parameterization
  summary: 'Losses parameterization Fixed (default) | Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2 | Profile:
    loss=f(Irms,vdc_nom)'
  group: ''
- name: Fixed power loss
  summary: Power loss 1 W (default)
  group: ''
- name: Switching losses coefficient, ks
  summary: Coefficient of switching losses 0.01 (default)
  group: ''
- name: Conduction losses coefficient, kc1
  summary: First coefficient of conduction losses 1.7 V (default)
  group: ''
- name: Conduction losses coefficient, kc2
  summary: Second coefficient of conduction losses 0.01 Ohm (default)
  group: ''
- name: Converter losses
  summary: Converter losses vector [100, 800, 1870, 3250, 4900] W (default)
  group: ''
- name: RMS current for converter losses
  summary: RMS currents vector [10, 100, 200, 300, 400] A (default)
  group: ''
- name: Nominal dc-link voltage
  summary: Nominal dc-link voltage 300 V (default)
  group: ''
- name: Thermal mass
  summary: Thermal mass 30000 J/K (default)
  group: ''
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model thermal parameters.

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **AC frequency** — AC frequency `Variable` (default) | `Constant`

Whether to have a variable or constant AC frequency:

- `Variable` — If the frequency
  of generated AC voltage varies, this option supports both
  variable-voltage variable-frequency (VVVF) and variable-voltage
  constant-frequency (VVCF) applications but the block only works
  in time simulation mode.
- `Constant` — If the frequency
  of generated AC voltage is constant, this option supports
  variable-voltage constant-frequency (VVCF) application and the
  block works in both time and frequency-and-time simulation
  modes. You can also choose between a three-phase modulation wave
  input or a magnitude and phase modulation input.

### **Input type** — Type of input `Modulation wave` (default) | `Sinusoidal magnitude and phase shift`

*Since R2024a*

Option to specify the input of the block as a three-phase modulation wave
or through sinusoidal magnitude and phase shift.

#### Dependencies

To enable this parameter, set **AC frequency** to
`Constant`.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` | scalar

Rated electrical frequency. The value of this parameter must be equal to
the value of the rated electrical frequencies of other sinusoidal sources in
your model, if present.

#### Dependencies

To enable this parameter, set **AC frequency** to
`Constant`.

### **Losses parameterization** — Losses parameterization `Fixed` (default) | `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2` | `Profile: loss=f(Irms,vdc_nom)`

Parameterization option for the power losses. You can choose one of these options:

- `Fixed` — Power loss is fixed and
  equal to the value of the **Fixed power loss**
  parameter.
- `Coefficients:
  loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2` —
  The total power losses are obtained by summing up the switching,
  the conduction, and quiescent losses.
- `Profile: loss=f(Irms,vdc_nom)` — The
  power loss is a function of the RMS current and the nominal
  dc-link voltage, and is obtained from the power losses
  profile.

,

### **Fixed power loss** — Power loss `1` `W` (default)

Fixed power loss on semiconductor components, in W. The input power is
equal to the fixed power loss plus output power.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to either
`Fixed` or `Coefficients:
loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`.

### **Switching losses coefficient, ks** — Coefficient of switching losses `0.01` (default)

Proportionality constant that depends on the turn-on and turn-off
intervals and switching frequency.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Coefficients:
loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`.

### **Conduction losses coefficient, kc1** — First coefficient of conduction losses `1.7` `V` (default)

Coefficient of the conduction losses that depends on the on-state zero
current collector-emitter voltage of the transistor and on the forward
voltage drop of the diode.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Coefficients:
loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`.

### **Conduction losses coefficient, kc2** — Second coefficient of conduction losses `0.01` `Ohm` (default)

Coefficient of the conduction losses that depends on the state resistance
of the transistor and on the anti-parallel diode.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Coefficients:
loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`.

### **Converter losses** — Converter losses vector `[100, 800, 1870, 3250, 4900]` `W` (default)

Vector of power losses values.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Profile:
loss=f(Irms,vdc_nom)`.

### **RMS current for converter losses** — RMS currents vector `[10, 100, 200, 300, 400]` `A` (default)

Vector of root mean square currents associated to the values of the
**Converter losses** parameter.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Profile:
loss=f(Irms,vdc_nom)`.

### **Nominal dc-link voltage** — Nominal dc-link voltage `300` `V` (default)

Nominal voltage.

#### Dependencies

To enable this parameter, set **Losses
parameterization** to `Profile:
loss=f(Irms,vdc_nom)`.

### **Thermal mass** — Thermal mass `30000` `J/K` (default)

Thermal mass.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024a: Specify magnitude and phase modulation input

You can now use phasor quantities such as magnitude and phase shift as input to the block.
To specify a magnitude and phase modulation input, set the **AC
frequency** parameter to `Constant` and the
**Input type** parameter to `Sinusoidal magnitude
and phase shift`.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Three-phase average-value bidirectional AC/DC voltage source converter

The Average-Value Voltage Source Converter (Three-Phase)
block converts electrical energy from AC to DC voltage or from DC to AC voltage
according to an input three-phase modulation wave. You can specify the modulation wave
directly or through phasor quantities such as the magnitude and phase shift. The
corresponding input power is equal to the sum of the fixed power loss and the output
power.

This block can work in both time and frequency-and-time simulation modes. If you set the
**AC frequency** parameter to `Variable`,
this block works only in time simulation mode. If you select
`Constant`, this block works in both time and
frequency-time simulation modes. For more information, see Frequency and Time Simulation Mode.

### Losses Parameterization

Switching losses, conduction losses, and quiescent losses are the main heat
sources for a converter.

The switching losses are defined by this equation:

Pswitching=ksvdcIrms

where:

- *ks* is the proportionality
  constant that depends on the turn-on and turn-off intervals and
  switching frequency. Specify this value by setting the
  **Switching losses coefficient, ks**
  parameter.
- *vdc* is the dc-link
  voltage.
- Irms=(ia−idc)2+(ib−idc)2+(ic−idc)23 is the root mean square (RMS) phase current, where idc=ia+ib+ic3.

The conduction losses are defined by this equation:

Pconduction=kc1Irms+kc2Irms2

where:

- *kc1* is the coefficient of
  the conduction losses that depends on the on-state zero current
  collector-emitter voltage of the transistor and on the forward voltage
  drop of the diode. Specify this value by setting the
  **Conduction losses coefficient, kc1**
  parameter.
- *kc2* is the coefficient of
  the conduction losses that depends on the state resistance of the
  transistor and on the anti-parallel diode. Specify this value by setting
  the **Conduction losses coefficient, kc2**
  parameter.

The quiescent losses are defined by the **Fixed power loss**
parameter, *Pfixed*.

The sum of the switching, conduction, and quiescent losses define the total power
losses of the converter:

Ploss=Pswitching+Pconduction+Pfixed.

If not available, you can also obtain the
*ks*,
*kc1*,
*kc2* and
*Pfixed* parameters values from the
power losses profile, by setting the **Losses parameterization**
parameter to `Profile: loss=f(Irms,vdc_nom)`. The block
then solves this equation and calculates the values of the parameters:

[P1⋮Pn]=[1vdc\_nomIrms,1Irms,1Irms,12⋮⋮⋮⋮1vdc\_nomIrms,nIrms,nIrms,n2][Pfixedkskc1kc2]

where [P1⋮Pn] is the vector of power loss values, **Converter
losses**, corresponding to the **RMS current for converter
losses** parameter, [Irms,1⋮Irms,n], and the **Nominal dc-link voltage**,
*vdc\_nom*.

### Model Thermal Effects

This block has one optional thermal port. To control the
visibility of the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a thermal
  port.
- `Show thermal port` — The block contains one thermal
  conserving port.
