---
type: simulink-block
title: 'Voltage-Controlled Oscillator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'voltagecontrolledoscillator'
documentation_source_path: 'ref/voltagecontrolledoscillator.html'
language: en
---

# Voltage-Controlled Oscillator

## Ports
```yaml
ports:
- name: 1+
  summary: Positive input voltage electrical
  direction: conserving
- name: 1-
  summary: Negative input voltage electrical
  direction: conserving
- name: 2+
  summary: Positive output voltage electrical
  direction: conserving
- name: 2-
  summary: Negative output voltage electrical
  direction: conserving
```

### Conserving

### **1+** — Positive input voltage electrical

Electrical conserving port associated with the oscillator positive
input voltage.

### **1-** — Negative input voltage electrical

Electrical conserving port associated with the oscillator negative
input voltage.

### **2+** — Positive output voltage electrical

Electrical conserving port associated with the oscillator positive
output voltage.

### **2-** — Negative output voltage electrical

Electrical conserving port associated with the oscillator negative
output voltage.
## Parameters
```yaml
parameters:
- name: Frequency dependence on input voltage
  summary: Block parameterization Linear (default) | Tabulated
  group: Frequency
- name: Nominal frequency
  summary: Nominal frequency 1000 Hz (default)
  group: Frequency
- name: Input voltage corresponding to nominal frequency
  summary: Input voltage corresponding to nominal frequency 0.5 V (default)
  group: Frequency
- name: Rate of change of frequency with input voltage
  summary: Rate of change of frequency with input voltage 1 Hz/V (default)
  group: Frequency
- name: Minimum input voltage
  summary: Minimum input voltage 0 V (default)
  group: Frequency
- name: Maximum input voltage
  summary: Maximum input voltage 1 V (default)
  group: Frequency
- name: Input voltage vector
  summary: Input voltage vector [0, .2, .4, .6, .8, 1] V (default)
  group: Frequency
- name: Frequency deviation from nominal
  summary: Frequency deviation from nominal [-1000, -329, -51, 162, 342, 500] Hz (default)
  group: Frequency
- name: Output voltage peak amplitude
  summary: Output voltage peak amplitude 1 V (default)
  group: Electrical Characteristics
- name: Input resistance
  summary: Input resistance inf Ohm (default)
  group: Electrical Characteristics
- name: Output resistance
  summary: Output resistance 0 Ohm (default)
  group: Electrical Characteristics
- name: Dynamics
  summary: Dynamics specification No dynamics (default) | Model frequency tracking dynamics
  group: Dynamics
- name: Frequency tracking time constant
  summary: Frequency tracking time constant 1e-3 s (default)
  group: Dynamics
- name: Initial frequency
  summary: Initial frequency 1000 Hz (default)
  group: Dynamics
```

### Frequency

### **Frequency dependence on input voltage** — Block parameterization `Linear` (default) | `Tabulated`

Select one of the following methods for block parameterization:

- `Linear` — Define a linear
  function by specifying the rate of change of frequency with
  input voltage. This is the default option.
- `Tabulated` — Provide the
  vectors of input voltages and corresponding output frequency
  deviations from nominal. The block determines the frequency
  deviation by table lookup based on these values.

### **Nominal frequency** — Nominal frequency `1000` `Hz` (default)

The oscillator frequency when the input control voltage is at the
nominal value.

### **Input voltage corresponding to nominal frequency** — Input voltage corresponding to nominal frequency `0.5` `V` (default)

The input voltage corresponding to the oscillator nominal
frequency.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Frequency
dependence on input voltage** parameter.

### **Rate of change of frequency with input voltage** — Rate of change of frequency with input voltage `1` `Hz/V` (default)

The linear coefficient defining the rate of change of frequency
depending on input voltage.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Frequency
dependence on input voltage** parameter.

### **Minimum input voltage** — Minimum input voltage `0` `V` (default)

The minimum input voltage that affects VCO frequency.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Frequency
dependence on input voltage** parameter.

### **Maximum input voltage** — Maximum input voltage `1` `V` (default)

The maximum input voltage that affects VCO frequency.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Frequency
dependence on input voltage** parameter.

### **Input voltage vector** — Input voltage vector `[0, .2, .4, .6, .8, 1]` `V` (default)

The vector of voltages for the tabulated VCO frequency.

#### Dependencies

This parameter is visible only when you select
`Tabulated` for the **Frequency
dependence on input voltage** parameter.

### **Frequency deviation from nominal** — Frequency deviation from nominal `[-1000, -329, -51, 162, 342, 500]` `Hz` (default)

The corresponding vector of VCO frequencies relative to the nominal
frequency.

#### Dependencies

This parameter is visible only when you select
`Tabulated` for the **Frequency
dependence on input voltage** parameter.

### Electrical Characteristics

### **Output voltage peak amplitude** — Output voltage peak amplitude `1` `V` (default)

The peak amplitude of the voltage across the 2+ and 2–
terminals.

### **Input resistance** — Input resistance `inf` `Ohm` (default)

The resistance seen at the 1+ and 1– terminals.

### **Output resistance** — Output resistance `0` `Ohm` (default)

The value of the series output resistance.

### Dynamics

### **Dynamics** — Dynamics specification `No dynamics` (default) | `Model frequency tracking dynamics`

Select one of the following methods for specifying dynamics:

- `No dynamics` — Do not
  model the time delay between a change in the input control
  voltage and the oscillator frequency. This is the default
  option.
- `Model frequency tracking
  dynamics` — Model a first order
  dynamic between the input control voltage and the oscillator
  frequency.

### **Frequency tracking time constant** — Frequency tracking time constant `1e-3` `s` (default)

Time constant for the first-order filter that delays the measured
input control voltage, to model the lag between a change in VCO demanded
frequency and the resulting VCO frequency.

#### Dependencies

This parameter is visible only when you select `Model
frequency tracking dynamics` for the
**Dynamics** parameter.

### **Initial frequency** — Initial frequency `1000` `Hz` (default)

The initial VCO output frequency.
## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Behavioral model of voltage-controlled oscillator

The Voltage-Controlled Oscillator block provides a
behavioral model of a voltage-controlled oscillator (VCO). The output voltage is defined
by the following equations:

vlim={vminfor vin<vminvinfor vmin≤vin≤vmaxvmaxfor vin>vmax

Φ˙=2πF(vlim)

vout=Asin(2πfnomt+Φ)−ioutRout

where:

- *v*in is the voltage applied across
  the 1+ and 1– ports.
- *v*out is the voltage across the 2+
  and 2– ports.
- *f*nom is the oscillator frequency
  when the input control voltage is
  *v*nom.
- *F* is a linear function of
  *v*lim or a lookup table function of
  *v*lim.
- *A* is the output voltage peak amplitude.
- *t* is simulation time.
- *i*out is the output current.
- *R*out is the output
  resistance.

If you choose `Linear` for the **Frequency dependence
on input voltage** parameter, then the function *F* is
given by:

F=fnom+k(vlim−vnom)

where *k* is the rate of change of frequency with input
voltage.

If you choose `Tabulated` for the **Frequency
dependence on input voltage** parameter, then the function
*F* is defined by the vectors of input voltages and corresponding
output frequency deviations from nominal that you supply. The values for
*v*min and
*v*max are the first and the last values of
the input voltage vector.

You can model the time delay between a change in the input control voltage and the
oscillator frequency. Do this by modeling a first-order dynamic between
*v*lim and the value passed to the function
*F*.
