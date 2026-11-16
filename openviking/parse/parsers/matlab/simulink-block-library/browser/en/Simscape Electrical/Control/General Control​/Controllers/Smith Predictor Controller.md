---
type: simulink-block
title: 'Smith Predictor Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Controllers'
documentation_page: 'smithpredictorcontroller'
documentation_source_path: 'ref/smithpredictorcontroller.html'
language: en
---

# Smith Predictor Controller

## Ports

### Input

### **r** — Plant reference scalar

Plant system reference signal.

**Data Types:** `single` | `double`

### **Reset** — Integrator reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `Boolean`

### **y** — Plant output scalar

Plant system output signal.

**Data Types:** `single` | `double`
### Output

### **u** — Controller output scalar

Control system output signal.

**Data Types:** `single` | `double`

## Parameters

### **Proportional gain** — *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the PI
controller.

### **Integral gain** — *Ki* `1` (default) | positive scalar

Integral gain, *Ki*, of the PI
controller.

### **Integrator initial condition** — Initial integrator value `0` (default) | scalar

Value of the integrator at simulation start time.

### **Control action upper limit** — *umax* `5` (default) | scalar greater than the value of the **Control action lower limit** parameter

Upper limit for the control output signal.

### **Control action lower limit** — *umin* `0` (default) | scalar

Lower limit for the control output signal.

### **Model discrete transfer function numerator** — Transfer function numerator `1` (default) | scalar or vector

Numerator of the system discretized transfer function. To determine the
discrete transfer function, if you have a license for Control System Toolbox™, use the `c2d` function.

### **Model discrete transfer function denominator** — Transfer function denominator `[1 0.5]` (default) | vector

Denominator of the system discretized transfer function. To determine the
discrete transfer function, if you have a license for Control System Toolbox, use the `c2d` function.

### **System dead time (samples)** — Number of dead-time samples `2` (default) | `0` or a positive integer

Number of samples of the dead time.

### **Sample time (-1 for inherited)** — Sampling interval `-1` (default) | default value or a positive number

Time interval between samples. If the block is
inside a triggered subsystem, inherit the sample time by setting this
parameter to `-1`. If this block is in a continuous
variable-step model, specify the sample time explicitly. For more
information, see What Is Sample Time? and
Specify Sample Time.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time Smith dead-time compensator

The Smith Predictor Controller block compensates for dead time by
implementing a Smith dead-time PI control structure in discrete time. This diagram shows
the equivalent circuit for the block.

### Equations

The transfer function for a system with dead-time is

Gf(s)=Gp(s)e−τs,

where:

- *τ* is the system dead time.
- *Gp(s)* is the process
  model.
- *Gf(s)* is prediction error
  filter.
