---
type: simulink-block
title: 'Passive Harmonic Filter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'passiveharmonicfilterthreephase'
documentation_source_path: 'ref/passiveharmonicfilterthreephase.html'
language: en
---

# Passive Harmonic Filter (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase voltage electrical

Expandable three-phase
port associated with the voltage.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Rated reactive power** — Reactive power `100e6` `V*A` (default)

Reactive power at rated frequency and voltage, in V\*A.

### **Rated voltage (phase-to-phase RMS)** — Phase-to-phase RMS Voltage `4160` `V` (default)

Rated phase-to-phase root mean squared (RMS) voltage, in V.

### **Rated frequency** — Rated frequency `60` `Hz` (default)

Fundamental frequency, in Hz.

### **Quality factor** — Quality factor `10` (default)

Index of the sharpness of the tuned frequency.

### **Filter type** — Filter model `Band-pass filter, single-tuned` (default) | `Band-pass filter, double-tuned` | `High-pass filter, second-order` | `High-pass filter, C-type`

Type of harmonic filter.

#### Dependencies

The **Tuned frequency** parameter becomes visible if you select
`Band-pass filter, single-tuned`,
`High-pass filter, second-order`, or
`High-pass filter, C-type` for the
**Filter type** parameter.

If you select `Band-pass filter,
double-tuned` for the **Filter type**
parameter, the **Tuned frequency 1** and
**Tuned frequency 2** parameters become
visible.

### **Filter connection** — Connection type `Wye with floating neutral` (default) | `Wye with neutral port` | `Wye with grounded neutral` | `Delta`

Type of connection

### **Tuned frequency** — Tuned frequency `5 * 60` `Hz` (default)

Tuned frequency for the filter, in Hz.

#### Dependencies

This parameter is visible only when you select `Band-pass filter,
single-tuned`, `High-pass filter,
second-order`, or `High-pass filter,
C-type` for the **Filter type**
parameter.

### **Tuned frequency 1** — First tuned frequency `7 * 60` `Hz` (default)

First tuned frequency, in Hz.

#### Dependencies

This parameter is visible only when you select `Band-pass
filter, double-tuned` for the **Filter
type** parameter.

### **Tuned frequency 2** — Second tuned frequency `11 * 60` `Hz` (default)

Second tuned frequency, in Hz.

#### Dependencies

This parameter is visible only when you select `Band-pass
filter, double-tuned` for the **Filter
type** parameter.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Harmonic current filter

The Passive Harmonic Filter (Three-Phase) block suppresses
system harmonic currents and decreases voltage distortion by providing low-impedance
paths for the harmonics. At the rated frequency, the passive shunt filters are
capacitive and provide reactive power, which can improve electrical power factor.

Each of the four models for the block corresponds to an option for the **Filter
type** parameter:

- Band-Pass Filter, Single Tuned
- Band-Pass Filter, Double Tuned
- High-Pass Filter, Second-Order
- High-Pass Filter, C-type

### Band-Pass Filter, Single Tuned

At the tuned frequency, LC resonance occurs and the impedance of the filter
reaches its minimum, which equals the value of the resistance.

The filter tuned frequency is defined by this equation:

f1=nf0=12πLC,

where *f1* and
*f0* are the tuned and fundamental
frequency, *n* is the harmonic order of the tuned frequency,
*L* is the inductance and *C* is the
capacitance.

The quality factor is defined as the ratio between the inductive or capacitive
reactance at the tuned frequency and the resistance, as described by this equation:

Qf=XLNR=XCNR,

where:

- R is the resistance.
- `XLN` is the impedance of the
  inductor at the tuned frequency XLN=2πf1L.
- `XCN` is the impedance of the
  capacitor at the tuned frequency XCN=12πf1C.

Higher quality factor values result in sharper frequencies. However, this produces
high-power dissipation at the base frequency due to a relative low resistance.

The rated reactive power is given by:

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

where *Qr* is the rated
reactive power for one phase and *V* is the branch voltage in root
mean square.

### Band-Pass Filter, Double Tuned

A double-tuned filter has two tuned frequencies,
*f1* and
*f2*, where f1=n1f0 and f2=n2f0.

The double-tuned filter comprises a series LC and a parallel RCL circuit, each
tuned at frequencies *fs* and
*fp*, close to the mean geometric
frequency of *f1* and
*f2*, which are represented by the equation:

fm=f1f2=fsfp,

where

fs=12πLC

fp=12πL2C2.

The quality factor of this filter is defined as the quality factor of the parallel
`R` and `L` elements at the mean geometric
frequency, *fm*:

Qf=R2πfmL2.

### High-Pass Filter, Second-Order

The second order high-pass filter shunts a large percentage of the harmonics at
and above the tuned frequency. The filter is designed to have a flat impedance for
high-order harmonics.

The tuned frequency is described by this equation:

f1=nf0=12πLC.

The quality factor is the reciprocal of the band-pass, single-tuned filter:

Qf=RXLN=RXCN.

The rated reactive power is the same of the band-pass, single-tuned filter:

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

### High-Pass Filter, C-type

Compared to the single-tuned version, the C-type, high-pass filter has lower
losses at the fundamental frequency, because the capacitor and inductor are parallel
with the resistor.

To prevent fundamental currents from passing through the resistor, the resonance
frequency of *L2* and
*C2* is tuned to the fundamental frequency:

f0=12πL2C2.

The quality factor is calculated using this equation:

Qf=R2πf0nL2.

### Values of RCL Filter Components

|  | Single-Tuned | Double-Tuned | Second-Order, High-Pass | C-type, High-Pass |
| --- | --- | --- | --- | --- |
| R | 12πf0CQf | 2πfmL2Qf | 2πnf0LQf | Qf(2π n f0 L2) |
| L | 1C(2πnf0)2 | V2Qrπf0(n12+n22−2) | 1C(2πnf0)2 | None |
| C | Qr2πf0V2⋅n2−1n2 | Qr4πf0V2(n12−1n12+n22−1n22) | Qr2πf0V2⋅n2−1n2 | Qr2πf0V2 |
| L2 | None | (1−f12fs2)(1−f12fp2)C(2πf12)where  fs=12πLC, fp=f1f2fs | None | 1C2(2πnf0)2 |
| C2 | None | 1L2(2πfp)2 | None | C(n2−1) |
