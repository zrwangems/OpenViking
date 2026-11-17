---
type: simulink-block
title: 'PWM Generator (Multilevel)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratormultilevel'
documentation_source_path: 'ref/pwmgeneratormultilevel.html'
language: en
---

# PWM Generator (Multilevel)

## Ports
```yaml
ports:
- name: ref
  summary: Reference signal vector
  direction: input
- name: PWM
  summary: PWM signal vector
  direction: output
  data_types: single | double
```

### Input

### **ref** — Reference signal vector

Reference signal to calculate the PWM for each power submodule of the
multilevel converter, specified as a vector.
### Output

### **PWM** — PWM signal vector

Pulse width modulation signal for each submodule, returned as a
vector.

If you set the **Converter topology** parameter to
`Half-bridge`, the output is a vector
specified as:

G={G1\_SM1, G2\_SM1, G1\_SM2, G2\_SM2, … , G1\_SMN, G2\_SMN}.

If you set the **Converter topology** parameter to
`Full-bridge`, the output is a vector
specified as:

G={G1\_SM1, G2\_SM1, G3\_SM1, G4\_SM1, G1\_SM2, G2\_SM2, G3\_SM2, G4\_SM2, … , G1\_SMN, G2\_SMN, G3\_SMN, G4\_SMN},

where *Gi\_SMj* is the reference signal controlling the
*i*-th gate of the *j*-th
power submodule. *i* ranges from `1`
to `2` in a half-bridge topology and from
`1` to `4` in a full-bridge
topology. *j* ranges from `1` to
*N*, where *N* is the number
of power submodules specified in the **Number of power
submodules** parameter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Converter topology
  summary: Modular multilevel converter topology Half-bridge (default) | Full-bridge
  group: ''
- name: Number of power submodules
  summary: Number of modular multilevel submodules 1 (default) | positive scalar
  group: ''
- name: Timer period (s)
  summary: PWM period 0.001 (default) | positive scalar
  group: ''
- name: Sample time
  summary: Block sample time 5e-5 (default) | positive scalar
  group: ''
```

### **Converter topology** — Modular multilevel converter topology `Half-bridge` (default) | `Full-bridge`

Topology of the modular multilevel converter.

### **Number of power submodules** — Number of modular multilevel submodules `1` (default) | positive scalar

Number of power submodules of the modular multilevel converter.

### **Timer period (s)** — PWM period `0.001` (default) | positive scalar

PWM timer period. The **Timer period (s)** parameter is specified as 12fsw, where fsw is the switching frequency.

### **Sample time** — Block sample time `5e-5` (default) | positive scalar

Sample time for the block. For continuous-time simulation, set to zero. For discrete-time
simulation, to ensure adequate resolution in the generated signal, specify a
positive value that is less than or equal to `10 *
Tper`, where
*Tper* is the
**Timer period (s)**.
## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Generate pulse width modulated signal or waveform for modular multilevel converters

The PWM Generator (Multilevel) block implements a pulse width modulation
(PWM) generator for modular multilevel converters. The PWM technique controls power
transfer from one electrical component to another by quickly switching between full
power transfer and no power transfer.

The block calculates gate pulses for a modular, multilevel converter based on the number of
power submodules and two converter topologies: half-bridge and full-bridge. You can
specify the number of power submodules and the converter topology using the
**Number of power submodules** and **Converter
topology** parameters, respectively.
