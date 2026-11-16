---
type: simulink-block
title: 'Average-Value Rectifier (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluerectifierthreephase'
documentation_source_path: 'ref/averagevaluerectifierthreephase.html'
language: en
---

# Average-Value Rectifier (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
port

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

## Parameters

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **AC frequency** — AC frequency `Variable` (default) | `Constant`

Whether to have a variable or constant AC frequency:

- `Variable` — If the frequency
  at the AC side varies, this option only works in time simulation
  mode.
- `Constant` — If the frequency
  at the AC side is constant, this option works in both time and
  frequency-and-time simulation modes.

### **Rated AC voltage** — Rated AC voltage `4160``V` (default)

Rated voltage of the AC system.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` | scalar

Rated electrical frequency. The value of this parameter must be equal to
the value of the rated electrical frequencies of other sinusoidal sources in
your model, if present.

#### Dependencies

To enable this parameter, set **AC frequency** to
`Constant`.

### **Fixed power loss** — Fixed power loss `1e3``W` (default)

Minimum power drawn on the AC side at rated AC voltage. When the
instantaneous AC voltage is equal to the value you specify for the
**Rated AC voltage**, the AC power demand equals the
value you specify for the **Fixed power loss** plus DC
power demand.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Average-value three-phase AC voltage to DC voltage converter with fixed power loss

The Average-Value Rectifier (Three-Phase) block models
an average-value, full-wave, six-pulse rectifier. It converts instantaneous three-phase
AC voltages to DC voltage and DC power demand to three-phase AC power demand. The
corresponding AC power demand is equal to the sum of the fixed power loss and the DC
power demand.

You can use the Average-Value Rectifier (Three-Phase)
block only as a six-pulse rectifier. You cannot combine two Average-Value
Rectifier blocks to represent a twelve-pulse rectifier.

The figure shows the equivalent circuit for the rectifier as a full-wave, six-pulse
rectifier. The Average-Value Rectifier (Three-Phase)
block does not yield the harmonics that are typically associated with the detailed
representation, however, because it performs an average-value power conversion.

This block can work in both time and frequency-and-time simulation modes. If you set
the **AC frequency** parameter to `Variable`,
this block works only in time simulation mode. If you select
`Constant`, this block works in both time and
frequency-time simulation modes. For more information, see Frequency and Time Simulation Mode.

### Electrical Defining Equations

The voltages are defined by:

vref=va+vb+vc3,

VRMS=(va−vb)2+(vb−vc)2+(vc−va)23,

vDC=32πVRMS,

vp=vref+vDC2,

and

vn=vref−vDC2,

where:

- *va*,
  *vb*,
  *vc* are the respective AC
  phase voltages.
- *vref* is the DC offset on the AC
  side. In a balanced AC power system with no DC bias,
  *vDC* is
  `0` V.
- *VRMS* is the RMS AC line-line
  voltage.
- *v*DC is the voltage difference
  between the positive and negative terminals of the rectifier.
- 32/π is the *vDC*/*VRMS*
  ratio for a full-wave, six-pulse rectifier.
- *vp*,
  *vn* are the voltages at the
  positive and negative terminals of the rectifier.

The resistance, power, and currents are defined by

Rfixed=VRated2Pfixed,

PDC=−vpip−vnin,

RAC=VRMS2PDC+VRMS2Rfixed,

and

[iaibic]=[vavbvc]−vrefRAC,

where:

- *VRated* is the rated AC
  voltage that you specify on the block mask.
- *Pfixed* is the fixed power
  loss that you specify on the block mask.
- *Rfixed* is the fixed
  per-phase series resistance in an equivalent wye-connected load.
- *ip*,
  *in* are the currents
  flowing into the positive and negative terminals of the
  rectifier.
- *PDC* is the power output on
  the DC side. *PDC* has a minimum
  limit of `0` W.
- *RAC* is the per-phase series
  resistance in an equivalent wye-connected load.
- *ia*,
  *ib*,
  *ic* are the respective
  AC phase currents flowing into the rectifier.
