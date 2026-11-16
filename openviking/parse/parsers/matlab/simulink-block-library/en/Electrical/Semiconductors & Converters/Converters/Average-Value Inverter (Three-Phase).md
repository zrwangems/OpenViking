---
type: simulink-block
title: 'Average-Value Inverter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevalueinverterthreephase'
documentation_source_path: 'ref/averagevalueinverterthreephase.html'
language: en
---

# Average-Value Inverter (Three-Phase)

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal

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

## Parameters

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Rated AC frequency** — AC frequency in Hz `60``Hz` (default)

AC frequency, specified in Hz (where Hz is defined as 1/s). For example, kHz and MHz are valid units, but rad/s is
not.

### **Phase shift** — Phase shift `0``deg` (default)

Phase shift in angular units.

### **Ratio of rated AC voltage to rated DC voltage** — Ratio of rated AC voltage to rated DC voltage `sqrt(6) / pi` (default)

The table shows ratios for common three-phase two-level inverter control
modes. The default value is 6/π.

For 180° and 120° conduction modes, the listed voltages are the
fundamental RMS values of line-line voltages. For other methods, the listed
voltages are the maximum fundamental RMS values of line-line voltages.

You can control the output voltage of the inverter according to specific
requirements. DPWM includes 30° DPWM, 60° DPWM, and 120°
DPWM. For details, see references [3] and [4].

| **Control Method** | ***V RMS  (line-line)*** | **Ratio of  *V RMS (line-line)*  to  *v DC*** |
| --- | --- | --- |
| 180° conduction mode [1] | 6πVDC | 0.7797 |
| 120° conduction mode [1] | 32πVDC | 0.6752 |
| Hysteresis current control [2] | (32)(2VDCπ) | 0.7797 |
| Sinusoidal PWM (SPMW) [2] | (32)(VDC2) | 0.6124 |
| Space vector modulation (SVM) [2] | (32)(VDC3) | 0.7071 |
| Discontinuous PWM (DPWM) [3], [4] | (32)(VDC3) | 0.7071 |
| Convert to the original AC voltage of the average-value rectifier | (π2)(VDC3) | 0.7405 |

### **Fixed power loss** — Fixed power loss `1e3``W` (default)

Minimum power drawn on the DC side. The default value is
`1e3`.

### **DC voltage for turn on** — DC voltage for turn on `100``V` (default)

When the DC supply voltage rises above this value, the inverter produces
an AC output voltage.

### **DC voltage for turn off** — DC voltage for turn off `75``V` (default)

When the DC supply voltage falls below this value, the inverter turns off
and the block sets the output AC currents to zero.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Average-value DC Voltage to three-phase AC voltage converter with fixed power loss

The Average-Value Inverter (Three-Phase) block models
an average-value, full-wave inverter. It converts DC voltage to three-phase AC voltages
and converts three-phase AC power demand to DC power demand. The corresponding DC power
demand is equal to the sum of the fixed power loss and the AC power demand.

You can use the Average-Value Inverter (Three-Phase)
block only as a full-wave inverter. It behaves as a DC-voltage-controlled AC voltage
source. The ratio you specify determines the ratio between the DC voltage and the AC
voltage.

The figure shows the equivalent circuit for the inverter as a full-wave inverter. The
Average-Value Inverter (Three-Phase) block does not
yield the harmonics that are typically associated with the detailed representation,
however, because it performs an average-value power conversion.

### Electrical Defining Equations

The voltages are defined by

vDC=vp−vn,

vref=vp+vn2,

vRMS=vratiovDC,

V0=23VRMS,

va=V0sin(2πft+φ)+vref,

vb=V0sin(2πft+φ−120∘)+vref,

and

vc=V0sin(2πft+φ+120∘)+vref,

where:

- *vp* and
  *vn* are the voltages at
  the positive and negative terminals of the inverter.
- *vDC* is the voltage
  difference between the positive and negative terminals of the
  inverter.
- *vref* is the DC
  offset.
- *Vratio* is the ratio of rated
  AC voltage to rated DC voltage for the inverter. See the **Ratio
  of rated AC voltage to rated DC voltage** parameter in
  Parameters for the
  *Vratio* values for
  common inverter control modes.
- *VRMS* is the RMS AC line-line
  voltage.
- *V0* is the peak phase
  voltage.
- *f* is the frequency.
- *t* is the time.
- *φ* is the phase shift.
- *va*,
  *vb*,
  *vc* are the respective
  AC phase voltages.

The power, resistance, and currents are defined by

PAC=−vaia−vbib−vcic,

RDC=vDC2PAC+Pfixed,

and

i=vDCRDC,

where:

- *ia*,
  *ib*, and
  *ic* are the respective
  AC phase currents flowing into the inverter.
- *PAC* is the power output on
  the AC side. *PAC* has a minimum
  limit of `0` W.
- *Pfixed* is the fixed power
  loss that you specify on the block.
- *RDC* is the resistance on the
  DC side.
- *i* is the current flowing from the positive to the
  negative terminals of the inverter.

The inverter starts to create an AC voltage, that is turns on, when the DC supply
voltage is above the value that you specify for **DC voltage for turn
on** parameter. It stops inverting, that is turns off, when the DC
supply voltage falls below the value that you specify for **DC voltage for
turn off** parameter. When the inverter turns off, the block sets the
output AC current to zero.
