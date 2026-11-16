---
type: simulink-block
title: 'Band-Limited Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'bandlimitedopamp'
documentation_source_path: 'ref/bandlimitedopamp.html'
language: en
---

# Band-Limited Op-Amp

## Ports

### Conserving

### **+** — Non-inverting input electrical

Electrical conserving port associated with the op-amp non-inverting
input

### **-** — Inverting input electrical

Electrical conserving port associated with the op-amp inverting
input

### **OUT** — Output voltage electrical

Electrical conserving port associated with the op-amp output
voltage

## Parameters

### **Gain, A** — Open-loop gain `1000` (default)

The open-loop gain of the operational amplifier.

### **Input resistance, Rin** — Input resistance `1e6` `Ohm` (default)

The resistance at the input of the operational amplifier that the block
uses to calculate the input current.

### **Output resistance, Rout** — Output resistance `100` `Ohm` (default)

The resistance at the output of the operational amplifier that the block
uses to calculate the drop in output voltage due to the output
current.

### **Minimum output, Vmin** — Minimum output `-15` `V` (default)

The lower limit on the operational amplifier no-load output
voltage.

### **Maximum output, Vmax** — Maximum output `15` `V` (default)

The upper limit on the operational amplifier no-load output
voltage.

### **Maximum slew rate, Vdot** — Maximum slew rate `1000` `V/s` (default)

The maximum positive or negative rate of change of output voltage
magnitude.

### **Bandwidth, f** — Open-loop bandwidth `1e5` `Hz` (default)

The open-loop bandwidth, that is, the frequency at which the gain drops by
3 dB compared to the low-frequency gain, *A*.

### **Initial output voltage, V0** — Initial output voltage `0` `V` (default)

The output voltage at the start of the simulation when the output current
is zero.

**Note**

This parameter value does not account for the voltage drop across the
output resistor.

## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Model band-limited operational amplifier

The Band-Limited Op-Amp block models a band-limited
operational amplifier. If the voltages at the positive and negative ports are
*Vp* and *Vm*, respectively, the output voltage is:

Vout = A(Vp-Vm)s2πf+1−Iout\*Rout

where:

- *A* is the gain.
- *Rout* is the output
  resistance.
- *Iout* is the output
  current.
- *s* is the Laplace operator.
- *f* is the 3-dB bandwidth.

The input current is:

Vp-VmRin

where *Rin* is the input
resistance.

The block does not use the initial condition you specify using the **Initial
output voltage, V0** parameter if you select the **Start simulation
from steady state** check box in the Simscape™
Solver Configuration block.
