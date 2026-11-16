---
type: simulink-block
title: 'Fully Differential Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'fullydifferentialopamp'
documentation_source_path: 'ref/fullydifferentialopamp.html'
language: en
---

# Fully Differential Op-Amp

## Ports

### Conserving

### **+** — Non-inverting input electrical

Electrical conserving port associated with the op-amp non-inverting
input.

### **-** — Inverting input electrical

Electrical conserving port associated with the op-amp inverting
input.

### **cm** — Common-mode port electrical

Electrical conserving port associated with the op-amp common-mode
port. If you want to leave this pin open-circuit, connect a voltage
sensor between the `cm` port and a reference
port.

### **Vout+** — Non-inverting output electrical

Electrical conserving port associated with the op-amp non-inverting
output.

### **Vout-** — Inverting output electrical

Electrical conserving port associated with the op-amp inverting
output.

## Parameters

### Gain

### **Differential gain** — Differential gain `1e3` (default)

The gain applied to a voltage difference between the + and –
inputs.

### **Bandwidth** — Bandwidth `1.5` `GHz` (default)

The frequency at which the differential voltage gain drops by 3 dB
from its dc value.

### Input Impedance

### **Differential input resistance** — Differential input resistance `1.3` `MOhm` (default)

The input resistance seen by a voltage source applied across the + and
– inputs. The default value is `1.3` MOhm.

### **Differential input capacitance** — Differential input capacitance `1.8` `pF` (default)

The input capacitance seen by a current source applied across the +
and – inputs.

### **Common-mode input resistance** — Common-mode input resistance `1.0` `MOhm` (default)

The input resistance seen by a voltage source applied between ground
and the + input, or between ground and the – input.

### **Common-mode input capacitance** — Common-mode input capacitance `2.3` `pF` (default)

The input capacitance seen by a current source applied between ground
and the + input, or between ground and the – input.

### Output Limits

### **Output resistance** — Output resistance `1` `Ohm` (default)

The output resistance of either of the outputs with respect to the
common-mode voltage reference. Differential output resistance is
therefore twice the value of the output resistance R\_out.

### **Minimum output voltage low** — Minimum output voltage low `-1.4` `V` (default)

The minimum output voltage for either of the two output pins with
respect to ground.

### **Maximum output voltage low** — Maximum output voltage low `1.4` `V` (default)

The maximum output voltage for either of the two output pins with
respect to ground.

### **Differential maximum slew rate** — Differential maximum slew rate `5000` `V/us` (default)

The maximum slew rate of the differential output voltage.

### Output Bias

### **Common-mode port input resistance** — Common-mode port input resistance `23.0` `kOhm` (default)

The input resistance seen by a voltage source applied between ground
and the common mode port.

### **Negative supply voltage** — Negative supply voltage `-5` `V` (default)

The value of the negative supply voltage connected to common-mode bias
resistor R3b (see diagram).

### **Positive supply voltage** — Positive supply voltage `5` `V` (default)

The value of the positive supply voltage connected to common-mode bias
resistor R3a (see diagram).

### Initial Conditions

### **Initial differential output voltage** — Initial differential output voltage `0` `V` (default)

The initial differential voltage across the two outputs if the output
current is zero.

## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Operational amplifier with fully differential output, that is, not referenced to ground

The Fully Differential Op-Amp block models a fully
differential operational amplifier. Differential signal transmission is better than
single-ended transmission due to reduced susceptibility to external noise sources.
Applications include data acquisition where inputs are differential, for example,
sigma-delta converters.

The following diagram shows the internal representation of the amplifier.

Parameters for the circuit components are derived from the block parameters that you
provide. The gain of the two voltage-controlled voltage sources (VCVS1 and VCVS2) is set
to half of the differential gain value. Similarly the slew rate of each of the voltage
sources is set to half of the differential maximum slew rate value. The voltages of the
two output ports `Vout+` and `Vout-` are both limited
to be within the minimum and maximum output voltages that you specify.

The output voltage for zero differential input voltage is controlled by the
common-mode port, `cm`. If no current is drawn from the
`cm` port by the external circuit, then the output voltage is set
to be the average of the positive and negative supply voltages by the resistor ladder of
R3a and R3b. Note that the negative supply voltage can be zero, which corresponds to
operation when a split supply is not available. The values for the minimum and maximum
output voltages that you provide must be consistent with the values for the supply
voltages that you provide. So, for example, the maximum output high voltage will be less
than the positive supply voltage, the difference corresponding to the number of p-n
junction voltage drops in the circuit.
