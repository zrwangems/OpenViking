---
type: simulink-block
title: 'Multiplier'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'multiplier'
documentation_source_path: 'ref/multiplier.html'
language: en
---

# Multiplier

## Ports
```yaml
ports:
- name: X1
  summary: X-input non-inverting input electrical
  direction: conserving
- name: X2
  summary: X-input inverting input electrical
  direction: conserving
- name: Y1
  summary: Y-input non-inverting input electrical
  direction: conserving
- name: Y2
  summary: Y-input inverting input electrical
  direction: conserving
- name: Z1
  summary: Z-input non-inverting input electrical
  direction: conserving
- name: Z2
  summary: Z-input inverting input electrical
  direction: conserving
- name: '~'
  summary: Multiplied output signal electrical
  direction: conserving
```

### Conserving

### **X1** — X-input non-inverting input electrical

Electrical conserving port associated with the multiplier X1
non-inverting input.

### **X2** — X-input inverting input electrical

Electrical conserving port associated with the multiplier X2 inverting
input.

### **Y1** — Y-input non-inverting input electrical

Electrical conserving port associated with the multiplier Y1
non-inverting input.

### **Y2** — Y-input inverting input electrical

Electrical conserving port associated with the multiplier Y2 inverting
input.

### **Z1** — Z-input non-inverting input electrical

Electrical conserving port associated with the multiplier Z1
non-inverting input.

### **Z2** — Z-input inverting input electrical

Electrical conserving port associated with the multiplier Z2 inverting
input.

### **~** — Multiplied output signal electrical

Electrical conserving port associated with the multiplier output
port.
## Parameters
```yaml
parameters:
- name: Scaling factor, K
  summary: Scaling factor 10 V (default)
  group: Main
- name: Gain, A
  summary: Gain 3000 (default)
  group: Main
- name: Differential resistance, Rin
  summary: Differential resistance 10e6 Ohm (default)
  group: Inputs
- name: Differential signal voltage range
  summary: Differential signal voltage range 10 V (default)
  group: Inputs
- name: Output resistance, Rout
  summary: Output resistance 0.1 Ohm (default)
  group: Outputs
- name: Minimum output, Vmin
  summary: Minimum output -11 V (default)
  group: Outputs
- name: Maximum output, Vmax
  summary: Maximum output 11 V (default)
  group: Outputs
- name: Maximum slew rate, Vdot
  summary: Maximum slew rate 20 V/us (default)
  group: Outputs
- name: Bandwidth, f
  summary: Bandwidth 1 MHz (default)
  group: Outputs
- name: Initial output voltage, V0
  summary: Initial output voltage 0 V (default)
  group: Outputs
```

### Main

### **Scaling factor, K** — Scaling factor `10` `V` (default)

The scaling factor *K* in the equation that defines
output voltage. Datasheets sometimes refer to it as the scale factor, or
SF.

### **Gain, A** — Gain `3000` (default)

The gain of the internal operational amplifier, corresponding to the
gain *A* in the equation that defines output
voltage.

### Inputs

### **Differential resistance, Rin** — Differential resistance `10e6` `Ohm` (default)

Each of the differential inputs is approximated as a linear resistor
with value *Rin*. Set this value to the datasheet value
for differential resistance.

### **Differential signal voltage range** — Differential signal voltage range `10` `V` (default)

This value, *Vdiff\_max*, is used to limit the
magnitude of each of the three differential input voltages. Set this
value to the datasheet value for differential signal voltage
range.

### Outputs

### **Output resistance, Rout** — Output resistance `0.1` `Ohm` (default)

The multiplier output stage is modeled as a voltage source plus series
resistor inside the Band-Limited Op-Amp block. This parameter specifies
the value of this series resistor.

### **Minimum output, Vmin** — Minimum output `-11` `V` (default)

The lower limit of the output voltage.

### **Maximum output, Vmax** — Maximum output `11` `V` (default)

The upper limit of the output voltage.

### **Maximum slew rate, Vdot** — Maximum slew rate `20` `V/us` (default)

The maximum positive or negative rate of change of output voltage
magnitude.

### **Bandwidth, f** — Bandwidth `1` `MHz` (default)

The bandwidth of the Band-Limited Op-Amp block.

### **Initial output voltage, V0** — Initial output voltage `0` `V` (default)

The value of the initial Multiplier block output if the
**Start simulation from steady-state** option is
not selected in the Solver block.
## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010b**

## Description

Integrated circuit multiplier

The Multiplier block models an integrated circuit
multiplier. The block implements the following equation, which defines the voltage
applied to the output port:

Vout=A((X1−X2)(Y1−Y2)K−(Z1−Z2))

where *X1*,
*X2*,
*Y1*,
*Y2*,
*Z1*,
*Z2* are the voltages presented at the input
ports, *A* is the gain, and *K* is the scale
factor.

In a typical multiplication circuit, the output is fed back into input Z1, which
results in the following gain (assuming that *A* is large):

Vout=((X1−X2)(Y1−Y2)K+Z2)

The value of the scale factor *K* is usually altered by an external
resistor bias network. The Multiplier block implements *K* as an
internal gain, and the external bias network is not necessary for system simulation. A
typical value for *K* is 10, with a typical adjustment down to
3.

You can use the Multiplier block to implement a number of other functions, as well as
multiplication. Examples include division, squares, and square roots. For example
circuits, consult manufacturer datasheets.

The following figure shows the internal model structure of the
Multiplier block. It includes the
Band-Limited Op-Amp block to model finite bandwidth
and slew-rate limiting.

The next figure shows one of the differential subsystem blocks. All three differential
subsystem blocks are identical in structure.
