---
type: simulink-block
title: 'PWM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Real-Time Hardware Deployment / RCP and HIL Blocks'
documentation_page: 'pwm'
documentation_source_path: '../simulink/slref/pwm.html'
language: en
---

# PWM

## Ports

### Input

### **D** — Duty Cycle scalar

Desired duty cycle of the pulse *P*, specified as scalar within the range [0,1].

**Data Types:** `double`
### Output

### **Port 1** — Output pulse scalar

PWM signal corresponding to the input duty cycle.

**Data Types:** `double`

## Parameters

### **Period (s)** — Pulse width 1 (default) | real scalar

Time between rising edges of consecutive pulses of the output signal. A
small value represents a high-frequency pulse.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Period` |
| **Type:** string | character vector |
| **Values:** real scalar |
| **Default:** `'1'` |

### **Initial Delay** — Initial delay 0 (default) | real scalar

Specify an initial delay or phase delay for the generated PWM signal, in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialDelay` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0` |

### **Disallow zero duty cycle** — Avoid algebraic loops `off` | `on`

Enable this parameter to break algebraic loops containing the
PWM block.

**Note**

Enabling this parameter causes a signal value of 0 or below, which
causes the duty cycle input to throw an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DisallowZeroDutyCycle` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Run at fixed time intervals** — Select for discrete time behavior `on` (default) | `off`

Specify when the block executes and the sample time for the output signal.

- `off` — Block executes each time the delay
  for an input sample elapses. Output signal has fixed-in-minor
  sample time.
- `on` — Block executes at a fixed rate you
  specify using the **Sample time** parameter.
  Output signal has the sample time you specify using the
  **Sample time** parameter.

When you select **Run at fixed time intervals**:

- The delay signal values must be greater than the value you
  specify for the **Sample time**
  parameter.
- Delay signal values that are not integer multiples of the
  specified sample time are rounded down to the nearest integer
  multiple of the sample time. For example, if the sample time is
  `0.1` and the delay signal value is
  `0.68`, the software rounds the delay to
  `0.6`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RunAtFixedTimeIntervals` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Sample Time** — Set pulse resolution 0.1 (default) | scalar

Block execution rate and output signal sample time. The delay signal
values must be greater than the specified sample time.

When the delay signal value is not an integer multiple of the specified
sample time, the software rounds the delay value down to the closest value
that is an integer multiple of the sample time. For example, if the sample
time is `0.1` and the delay value is
`0.68`, the software rounds the delay to
`0.6`.

#### Dependencies

To enable this parameter, select **Run at fixed time
intervals**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0.1` |

## Libraries

Simulink / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into discrete equivalents that support production code generation. To start the Model Discretizer, in the Simulink® Editor, on the **Apps** tab, under **Apps**, under **Control Systems**, click **Model Discretizer**. One exception is the Second-Order Integrator block because, for this block, the Model Discretizer produces an approximate discretization.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

For HDL code generation from this block, the **Run at
fixed time intervals** parameter must be selected.

## Version History

**Introduced in R2020b**

## Description

Generate ideal pulse width modulated signal corresponding to input duty cycle

Use the PWM block to generate an ideal pulse width modulated signal.

Pulse-width modulation (PWM) is a technique for encoding an analog signal using square
pulses. This encoding is achieved by controlling the fraction of one period of the
square wave that is set to high. This fraction is the duty cycle of the signal. The
relationship between the modulated signal and the input duty cycle can be simply
described as:

y¯=Dymax+​(1−D)ymin

where *ymax* and *ymin* are the upper and lower bounds of the output signal, respectively. For
the PWM block, the duty cycle is constrained to `[0,1]`.
The ideal PWM signal is proportional to the duty cycle *D*.
