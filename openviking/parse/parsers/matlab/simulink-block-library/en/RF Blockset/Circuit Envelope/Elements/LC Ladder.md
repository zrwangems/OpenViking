---
type: simulink-block
title: 'LC Ladder'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'lcladder'
documentation_source_path: 'ref/lcladder.html'
language: en
---

# LC Ladder

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Ladder topology
  summary: Type of ladder topology LC Lowpass Tee (default)
  group: ''
- name: Inductance
  summary: inductance values [1.3324e-5 1.3324e-5] H (default) | real number
  group: ''
- name: Capacitance
  summary: Capacitance value 1.1327e-9 F (default) | real number
  group: ''
- name: Ground and hide negative terminals
  summary: Internally ground and hide the negative terminals on (default) | off
  group: ''
```

### **Ladder topology** — Type of ladder topology `LC Lowpass Tee` (default)

Type of ladder topology, specified as one of the following:

**Ladder Topology**

|  |  |
| --- | --- |
| LC Lowpass Tee | LC Lowpass Tee |
| LC Lowpass Pi | LC Lowpass pi |
| LC Highpass Tee | LC highpass tee |
| LC Highpass Pi | LC highpass pi |
| LC Bandpass Tee | LC bandpass Tee |
| LC Bandpass Pi | LC Bandpass pi |
| LC Bandstop Tee | LC Bandstop Tee |
| LC Bandstop Pi | LC Bandstop pi |

### **Inductance** — inductance values `[1.3324e-5 1.3324e-5] H` (default) | real number

Inductance value, specified as a real number in Henries. Specify the units
of the inductance from the corresponding drop-down menu.

**Data Types:** `double`

### **Capacitance** — Capacitance value `1.1327e-9 F` (default) | real number

Capacitance value, specified as a real number in Farads. Specify the units
of the capacitance from the corresponding drop-down menu.

### **Ground and hide negative terminals** — Internally ground and hide the negative terminals `on` (default) | `off`

Select this option to internally ground and hide the negative terminals.
Clear this to expose the negative terminals. By exposing these terminals,
you can connect them to other parts of your model.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Model LC ladder networks

The LC Ladder block models common two-port LC lossless networks. To
learn how you can use LC Ladder to compare the input and output signal
amplitudes to study the signal attenuation, see Model RF Filter Using Circuit Envelope.
