---
type: simulink-block
title: '3-Phase Sine Voltage Generator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Math Transforms'
documentation_page: '3phasesinevoltagegenerator'
documentation_source_path: 'ref/3phasesinevoltagegenerator.html'
language: en
---

# 3-Phase Sine Voltage Generator

## Ports

### Input

### **A** — Reference voltage amplitude scalar

Maximum amplitude of the reference voltage signal.

**Data Types:** `single` | `double` | `fixed point`

### **θe** — Reference voltage position scalar

Position or phase value of the reference voltage signal.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Va** — *a*-axis component of balanced, three-phase voltage scalar

Balanced, three-phase voltage signal component along the *a*-axis
of the *abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vb** — *b*-axis component of balanced, three-phase voltage scalar

Balanced, three-phase voltage signal component along the *b*-axis
of the *abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vc** — *c*-axis component of balanced, three-phase voltage scalar

Balanced, three-phase voltage signal component along the *c*-axis
of the *abc* reference frame.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Theta units** — Unit of `θe` `Per-unit` (default) | `Radians` | `Degrees`

Unit of the reference voltage position that you provide as input.

### **Number of data points for lookup table** — Size of lookup table `1024` (default) | scalar

Size of the lookup table.

## Libraries

Motor Control Blockset / Controls / Math Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Generate balanced three-phase sinusoidal signals

The 3-Phase Sine Voltage Generator block generates balanced, three-phase
sinusoidal signals using signal amplitude and position inputs.

The block uses the lookup table approach. This approach results in optimized
code-execution when used with the model settings and configuration adopted by the examples
shipped in Motor Control Blockset™. You can specify the number of lookup table points in the **Number of
data points for lookup table** parameter.

The following image shows a plot of position input and three-phase sinusoidal output
signals against time.

### Equations

The following equations describe how the block computes balanced, three-phase sinusoidal
signals.

- Va=A×sinωt
- Vb=A×sin(ωt−2π3)
- Vc=A×sin(ωt−4π3)

where:

- A is the reference voltage amplitude (volts).
- ω is the frequency of the reference voltage position input signal
  (`θe`) (radians/ sec).
- t is the time (seconds).
