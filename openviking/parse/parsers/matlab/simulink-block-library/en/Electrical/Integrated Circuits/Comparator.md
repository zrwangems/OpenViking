---
type: simulink-block
title: 'Comparator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'comparator'
documentation_source_path: 'ref/comparator.html'
language: en
---

# Comparator

## Ports
```yaml
ports:
- name: +
  summary: Non-inverting input electrical
  direction: conserving
- name: '-'
  summary: Inverting input electrical
  direction: conserving
- name: OUT
  summary: Output port electrical
  direction: conserving
```

### Conserving

### **+** — Non-inverting input electrical

Electrical conserving port associated with the comparator
non-inverting input.

### **-** — Inverting input electrical

Electrical conserving port associated with the comparator inverting
input.

### **OUT** — Output port electrical

Electrical conserving port associated with the comparator
output
## Parameters
```yaml
parameters:
- name: Input offset voltage
  summary: Input offset voltage 5 mV (default)
  group: Input
- name: Average input capacitance
  summary: Average input capacitance 0 pF (default)
  group: Input
- name: Low level output voltage
  summary: Low level output voltage 0 V (default)
  group: Output
- name: High level output voltage
  summary: High level output voltage 5 V (default)
  group: Output
- name: Output resistance
  summary: Output resistance 50 Ohm (default)
  group: Output
- name: Propagation delay
  summary: Propagation delay 0 s (default)
  group: Output
```

### Input

### **Input offset voltage** — Input offset voltage `5` `mV` (default)

The voltage which the difference in the input voltages must be greater
than so that the comparator gives a logic output 1.

### **Average input capacitance** — Average input capacitance `0` `pF` (default)

You can usually find this capacitance value on a manufacturer
datasheet. Setting this value to zero can result in faster simulation
times.

### Output

### **Low level output voltage** — Low level output voltage `0` `V` (default)

The steady-state output voltage, VOL, when the voltage difference across the inputs is less
than or equal to the threshold voltage, and the output current is
zero.

### **High level output voltage** — High level output voltage `5` `V` (default)

The steady-state output voltage, VOH, when the voltage difference across the inputs is
greater than the threshold voltage, and the output current is
zero.

### **Output resistance** — Output resistance `50` `Ohm` (default)

This parameter is the ratio of output voltage drop to output current.
Set this parameter to (VOH−VOH1)/IOH1, where VOH1 is the reduced output high voltage when the output
current is IOH1.

### **Propagation delay** — Propagation delay `0` `s` (default)

Set this value based on the high-to-low and low-to-high propagation
delays.
## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Behavioral model of a comparator integrated circuit

The Comparator block is an abstracted behavioral model
of a comparator integrated circuit. It does not model an internal transistor-level
implementation. Therefore, the block runs quickly during simulation but retains the
correct I/O behavior. The block models differential inputs electrically as having
infinite resistance and a finite or zero capacitance.

The block models the gate output as a voltage source driving a series resistor and a
capacitor that connects to ground. The output pin connects to the resistor-capacitor
connection node. If the difference in the inputs is greater than the input threshold
voltage, then the output is equal to the **High level output voltage** (VOH). Otherwise, the output is equal to the **Low level output
voltage** (VOL).

The output model is shown in the following illustration.
