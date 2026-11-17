---
type: simulink-block
title: 'SPICE-Imported MOSFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'spiceimportedmosfet'
documentation_source_path: 'ref/spiceimportedmosfet.html'
language: en
---

# SPICE-Imported MOSFET

## Ports
```yaml
ports:
- name: g
  summary: Gate terminal electrical
  direction: conserving
- name: d
  summary: Drain terminal electrical
  direction: conserving
- name: tj
  summary: Junction temperature electrical
  direction: conserving
- name: tc
  summary: Case temperature electrical
  direction: conserving
- name: s
  summary: Source terminal electrical
  direction: conserving
```

### Conserving

### **g** — Gate terminal electrical

Electrical conserving port associated with the gate terminal of the
chosen pre-parameterized MOSFET.

### **d** — Drain terminal electrical

Electrical conserving port associated with the drain terminal of the
chosen pre-parameterized MOSFET.

### **tj** — Junction temperature electrical

Electrical conserving port associated with the junction temperature of
the chosen pre-parameterized MOSFET.

The voltage measured at this port corresponds to the temperature of
the junction. For example, if the value at this port is equal to 25V,
then the junction temperature is equal to 25 degrees Celsius.

**Tj** is usually a monitoring node and it is not
connected.

### **tc** — Case temperature electrical

Electrical conserving port associated with the case temperature of the
chosen pre-parameterized MOSFET.

The voltage measured at this port corresponds to the temperature of
the case. For example, if the value at this port is equal to 25V, then
the case temperature is equal to 25 degrees Celsius.

**Tc** is connected either to a voltage source that
represents the ambient temperature or to a heat-sink thermal network
represented by electrical resistors and capacitors.

### **s** — Source terminal electrical

Electrical conserving port associated with the source of the chosen
pre-parameterized MOSFET.
## Parameters
```yaml
parameters:
- name: Series
  summary: MOSFET series Infineon OptiMOS6 40V (default) | Infineon OptiMOS5 80V | Infineon OptiMOS4 60V | Infineon OptiMOST
    120V
  group: ''
- name: Device
  summary: Device name IPB015N08N5 | IAUC120N04S6N009 | IAUC120N04S6N010 | IAUC120N04S6N013 | IAUC100N04S6N015 | ...
  group: ''
```

### **Series** — MOSFET series `Infineon OptiMOS6 40V` (default) | `Infineon OptiMOS5 80V` | `Infineon OptiMOS4 60V` | `Infineon OptiMOST 120V`

Series of the pre-parameterized MOSFET, specified as either
`Infineon OptiMOS6 40V`, `Infineon
OptiMOS5 80V`, `Infineon OptiMOS4
60V`, or `Infineon OptiMOST
120V`.

### **Device** — Device name `IPB015N08N5` | `IAUC120N04S6N009` | `IAUC120N04S6N010` | `IAUC120N04S6N013` | `IAUC100N04S6N015` | ...

Name of the device, specified as one of the options listed in the Available Parameterizations
table.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Predefined MOSFET parameterized by external SPICE subcircuit

The SPICE-Imported MOSFET block models a
metal-oxide-semiconductor field-effect transistor (MOSFET) that has been parameterized
using an external SPICE subcircuit.

You can use this block to model the MOSFET devices listed in the table. These
parameterizations have already been imported to Simscape using the `subcircuit2ssc` function, and they have been numerically validated
against results generated using a SPICE simulation tool.

**Available Parameterizations**

| Series | Device |
| --- | --- |
| **Infineon OptiMOS6 40V** | `IAUC120N04S6N009` |
| `IAUC120N04S6N010` |
| `IAUC120N04S6N013` |
| `IAUC100N04S6N015` |
| `IAUC100N04S6N022` |
| `IAUC100N04S6N028` |
| `IAUC80N04S6N036` |
| `IAUC60N04S6N036` |
| `IAUC120N04S6L008` |
| `IAUC120N04S6L009` |
| `IAUC120N04S6L012` |
| `IAUC100N04S6L014` |
| `IAUC100N04S6L020` |
| `IAUC100N04S6L025` |
| `IAUC80N04S6L032` |
| `IAUC60N04S6L039` |
| **Infineon OptiMOS5 80V** | `IPB015N08N5` |
| `IPB017N08N5` |
| `IPP020N08N5` |
| `IPT012N08N5` |
| `IPB020N08N5` |
| `IPP023N08N5` |
| `IPB024N08N5` |
| `IPP027N08N5` |
| `IPB031N08N5` |
| `IPP034N08N5` |
| `IPB049N08N5` |
| `IPP052N08N5` |
| `IAUT300N08S5N012` |
| `IAUT165N08S5N029` |
| `IAUT300N08S5N014` |
| `IAUT240N08S5N019` |
| `IAUT200N08S5N023` |
| `IAUS300N08S5N013T` |
| `IAUS300N08S5N015T` |
| `IAUC100N08S5N031` |
| `IAUC100N08S5N043` |
| `IAUC70N08S5N074` |
| **Infineon OptiMOS4 60V** | `IPB180N06S4_H1` |
| `IPB120N06S4_H1` |
| `IPI120N06S4_H1` |
| `IPP120N06S4_H1` |
| `IPB120N06S4_02` |
| `IPI120N06S4_02` |
| `IPP120N06S4_02` |
| `IPB120N06S4_03` |
| `IPI120N06S4_03` |
| `IPP120N06S4_03` |
| `IPB90N06S4_04` |
| `IPD90N06S4_04` |
| `IPD100N06S4_03` |
| `IPI90N06S4_04` |
| `IPP90N06S4_04` |
| `IPB80N06S4_05` |
| `IPD90N06S4_05` |
| `IPI80N06S4_05` |
| `IPP80N06S4_05` |
| `IPB80N06S4_07` |
| `IPD90N06S4_07` |
| `IPI80N06S4_07` |
| `IPP80N06S4_07` |
| `IPB45N06S4_09` |
| `IPD50N06S4_09` |
| `IPI45N06S4_09` |
| `IPP45N06S4_09` |
| `IPG20N06S4_15` |
| `IPB90N06S4L_04` |
| `IPD90N06S4L_03` |
| `IPI90N06S4L_04` |
| `IPP90N06S4L_04` |
| `IPB80N06S4L_05` |
| `IPD90N06S4L_05` |
| `IPI80N06S4L_05` |
| `IPP80N06S4L_05` |
| `IPB80N06S4L_07` |
| `IPD90N06S4L_06` |
| `IPI80N06S4L_07` |
| `IPP80N06S4L_07` |
| `IPB45N06S4L_08` |
| `IPD50N06S4L_08` |
| `IPI45N06S4L_08` |
| `IPP45N06S4L_08` |
| `IPD50N06S4L_12` |
| `IPD30N06S4L_23` |
| `IPD25N06S4L_30` |
| `IPG20N06S4L_11` |
| `IPG20N06S4L_14` |
| `IPG20N06S4L_26` |
| **Infineon OptiMOST 120V** | `IPB100N12S3_05` |
| `IPI100N12S3_05` |
| `IPP100N12S3_05` |
| `IPB70N12S3_11` |
| `IPI70N12S3_11` |
| `IPP70N12S3_11` |
| `IPD70N12S3_11` |
| `IPD70N12S3L_12` |
| `IPB70N12S3L_12` |
| `IPI70N12S3L_12` |
| `IPP70N12S3L_12` |
| `IPB50N12S3L_15` |
| `IPD50N12S3L_15` |
| `IPI50N12S3L_15` |
| `IPP50N12S3L_15` |
| `IPB35N12S3L_26` |
| `IPD35N12S3L_24` |
| `IPD30N12S3L_31` |
