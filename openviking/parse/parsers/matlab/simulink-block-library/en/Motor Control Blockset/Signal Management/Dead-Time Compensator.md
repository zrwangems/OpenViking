---
type: simulink-block
title: 'Dead-Time Compensator'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'deadtimecompensator'
documentation_source_path: 'ref/deadtimecompensator.html'
language: en
---

# Dead-Time Compensator

## Ports

### Input

### **Vabc** — Reference voltages scalar

Three-phase reference voltages (in volts).

**Data Types:** `single` | `double` | `fixed point`

### **Iab** — Measured motor currents scalar

Measured values of phase-*a* and phase-*b*
currents of the motor (in amperes).

**Data Types:** `single` | `double` | `fixed point`

### **fPWM** — PWM frequency scalar

Frequency (in hertz) of the carrier wave used to perform pulse-width
modulation.

**Data Types:** `single` | `double` | `fixed point`

### **Vdc** — Inverter DC voltage scalar

DC voltage supply of the inverter (in volts).

**Data Types:** `single` | `double` | `fixed point`

### **Enable** — Signal to enable block outputs scalar

Signal that enables block outputs:

- `1` — Enable compensation (block outputs compensated
  voltages).
- `0` — Disable compensation (block outputs input
  voltages).

#### Dependencies

To enable this port, select the **Show enable port**
parameter.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Vabc ± Δ** — Compensated three-phase voltages scalar

Motor three-phase voltages (in volts) that is compensated for inverter
dead-time effect.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Dead time (s)** — Inverter switching dead-time `1e-6` (default) | scalar

Dead time in Inverter switches (in seconds).

### **Enable hysteresis for currents near zero-crossing** — Option to enable hysteresis algorithm for currents near zero-crossing `off` (default) | `on`

Select this parameter to enable hysteresis algorithm near the region of
zero-crossing of the input motor phase currents.

The block detects motor current polarity to determine voltage compensation.
Using a hysteresis band near zero-crossing of currents aids in better detection of
current polarity when motor currents are noisy.

### **Current hysteresis band (A)** — Current hysteresis band around zero-crossing `0.1` (default) | scalar

Hysteresis band, *h*, for the current controller. The
switch-on point is *h* and the switch-off point is
*-h*.

#### Dependencies

To enable this parameter, select **Enable hysteresis for currents
near zero-crossing**.

### **Motor current input** — Type of motor current input `Two currents (Ia,Ib)` (default) | `Three currents (Ia,Ib,Ic)`

Number of motor current inputs. You can select one of the following
options:

- `Two currents (Ia,Ib)`
- `Three currents (Ia,Ib,Ic)`

### Inputs

### **Show enable port** — Option to enable input port off (default) | `on`

Select this parameter to show the input port
**Enable**.

## Libraries

Motor Control Blockset / Signal Management Motor Control Blockset HDL Support / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation
and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The block does not support HDL code generation when you select the
**Enable hysteresis for currents near zero-crossing**
parameter.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024a**

## Description

Overcome dead-time effect by modifying reference voltages

The Dead-Time Compensator block compensates for the inverter dead-time.
Use this block to compensate for the dead-time effect of a three-phase inverter.

Three-phase inverters used in motor drive applications are nonlinear in nature. Dead
time in an inverter (that is added to avoid short circuit in the inverter legs) contributes
significantly to this nonlinearity. Even though dead time ensures safe operation of the
inverter, it can adversely affect the performance of the inverter. This causes the inverter
output voltage waveform to deviate from its originally expected form.

The block accepts three-phase reference voltages, measured motor currents, PWM
frequency, and inverter DC voltage as inputs. It provides a three-phase voltage output that
compensates for the dead-time effect of the inverter. The compensation helps reduce the
noise or ripple in motor torque or currents, and therefore, improves the motor drive
performance.

The following image shows the block position inside a motor control algorithm.
