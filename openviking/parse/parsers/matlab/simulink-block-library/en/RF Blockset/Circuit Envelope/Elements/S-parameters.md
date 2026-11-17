---
type: simulink-block
title: 'S-parameters'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'sparametersidealizedbaseband'
documentation_source_path: 'ref/sparametersidealizedbaseband.html'
language: en
---

# S-parameters

## Ports
```yaml
ports:
- name: Port_1
  summary: Time-dependent input signal real scalar | real column | complex scalar | complex column
  direction: input
  data_types: double | single
- name: Port_1
  summary: Time-dependent output signal complex scalar | complex column
  direction: output
  data_types: double | single
```

### Input

### **Port\_1** — Time-dependent input signal real scalar | real column | complex scalar | complex column

Time-dependent input signal, specified as a real scalar, real column, complex
scalar, or complex column. A column represents consecutive points in time.

**Data Types:** `double` | `single`
### Output

### **Port\_1** — Time-dependent output signal complex scalar | complex column

Time-dependent output signal, returned as a complex scalar or complex column. The
output time-dependent signal is equal in size to the input time-dependent
signal.

**Data Types:** `double` | `single`
## Parameters
```yaml
parameters:
- name: Data source
  summary: Data source to model RF complex baseband S-parameters file (default) | sparameters | rational
  group: Main
- name: File
  summary: Two-port Touchstone data file unitygain.s2p (default) | character vector
  group: Main
- name: Sparameter object
  summary: Use sparameters object as data source sparameters('unitygain.s2p') (default)
  group: Main
- name: Rational object
  summary: Use rational object as data source rational('unitygain.s2p','TendsToZero',false) (default)
  group: Main
- name: Carrier frequency (Hz)
  summary: Carrier frequency at which S-parameters are modeled 1000000000 (default) | positive real scalar
  group: Main
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: Main
- name: Modeling domain
  summary: Modeling domain Time (Fixed step) (default) | Time (Continuous) | Frequency (Digital filter)
  group: Modeling
- name: Solver
  summary: Time-domain solvers NDF2 (default) | Trapezoidal | Backward Euler | ode15s | ode23s | ode23t (trap) | ode23tb (trap+BE)
  group: Modeling
- name: Pole fitting options
  summary: Rational fit fitting options Share all poles (default) | Fit individually | Share poles by columns
  group: Modeling
- name: Rational arguments
  summary: Rational fit arguments to control the fit { 'Tolerance',-40,'TendsToZero',false,'MaxPoles',48,'Qlimit',inf } (default)
    | cell array
  group: Modeling
- name: FIR filter length
  summary: Filter length of 1-D digital filter 128 (default) | real positive integer
  group: Modeling
- name: First plot type
  summary: Plot type S21 (default) | Phase delay | Group delay | Impulse response | Step response
  group: Visualization
- name: Impulse response arguments
  summary: Input arguments to plot impulse response [ 1e-11, 1e4] (default) | two-element vector
  group: Visualization
- name: Step response arguments
  summary: Input arguments to plot step response [ 1e-11, 1e4, 1e-10 ] (default) | three-element vector
  group: Visualization
- name: First plot y-axis units
  summary: Y-axis units of first plot Magnitude (dB) (default) | Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: Visualization
- name: Second Plot type
  summary: Plot type of second plot None (default) | S21 | Phase delay | Group delay | Impulse response | Step response
  group: Visualization
- name: Second plot y-axis units
  summary: Y-axis units of second plot Magnitude (dB) (default) | Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: Visualization
- name: X-axis frequency points (Hz)
  summary: Frequency points to plot S-parameter data logspace(8,10,2001) (default) | positive real vector
  group: Visualization
- name: X-axis scale
  summary: Linear or logarithmic X-axis scale Linear (default) | Logarithmic
  group: Visualization
- name: Y-axis scale
  summary: Linear or logarithmic Y-axis scale Linear (default) | Logarithmic
  group: Visualization
- name: Plot Sparameter characteristics
  summary: Plot S-parameters data button
  group: Visualization
```

### Main

### **Data source** — Data source to model RF complex baseband S-parameters `file` (default) | `sparameters` | `rational`

Data source to model RF complex baseband S-parameters, specified as one of the
following:

- `file` — Select this option to specify a
  Touchstone file with the extension `.s2p`. The block ignores
  noise and nonlinearity data in imported files.
- `sparameters` — Select this option to specify
  an `sparameters` object.
- `rational` — Select this option to specify a
  `rational` object.

### **File** — Two-port Touchstone data file `unitygain.s2p` (default) | character vector

Name of the two-port Touchstone file, specified as a character vector.

#### Dependencies

To enable this parameter, set **Data source** to
`file`.

### **Sparameter object** — Use `sparameters` object as data source `sparameters('unitygain.s2p')` (default)

Select this parameter to use an `sparameters` object as the data source to model the S-parameters.

#### Dependencies

To enable this parameter, set **Data source** to
`sparameters`.

### **Rational object** — Use `rational` object as data source `rational('unitygain.s2p','TendsToZero',false)` (default)

Select this parameter to use a `rational` object
as the data source to model the S-parameters.

#### Dependencies

To enable this parameter, set **Data source** to
`rational`.

### **Carrier frequency (Hz)** — Carrier frequency at which S-parameters are modeled `1000000000` (default) | positive real scalar

Carrier frequency at which the S-parameters are modeled, specified as a positive
real scalar in Hz.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as one of the following:

- `Interpreted execution` — Simulate the model using
  the MATLAB® interpreter. This option shortens the startup time, but the speed
  of the subsequent simulations is slower than when you use the `Code
  generation` option. Use this mode to debug the source code of the
  block.
- `Code generation` — Simulate the model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time, but the speed of the subsequent simulations is
  faster than when you use the `Interpreted execution`
  option.

### Modeling

### **Modeling domain** — Modeling domain `Time (Fixed step)` (default) | `Time (Continuous)` | `Frequency (Digital filter)`

Modeling domain, specified as one of the following:

- `Time(Fixed step)` — Model using fixed-step solvers
  (`NDF2`, `Trapezoidal`, and
  `Backward Euler`)
- `Time(Continuous)` — Model using continuous or
  stiff solvers (`ode15s`,
  `ode23s`, `ode23t`, and
  `ode23tb`)
- `Frequency (Digital filter)` — model using a 1-D
  digital filter.

### **Solver** — Time-domain solvers `NDF2` (default) | `Trapezoidal` | `Backward Euler` | `ode15s` | `ode23s` | `ode23t (trap)` | `ode23tb (trap+BE)`

Fixed-step and continuous time-domain solvers, specified as one of the
following:

**Fixed-step Solvers**

- `NDF2` — Balance narrowband and wideband accuracy.
  This solver is suitable for situations where the frequency content of the
  signals in the system is unknown relative to the Nyquist rate.
- `Trapezoidal` — Perform narrowband simulations.
  Frequency warping and the lack of damping effects make this method inappropriate
  for most wideband simulations.
- `Backward Euler` — Simulate the largest class of
  systems and signals. Damping effects make this solver suitable for wideband
  simulation, but overall accuracy is low.

**Continuous Solvers**

- `ode15s` — Solve stiff differential equations and
  DAEs using a variable order method
- `ode23s` — Solve stiff differential equations using
  a low-order method
- `ode23t (trap)` — Solve moderately stiff ODEs and
  DAEs using a trapezoidal rule
- `ode23tb (trap+BE)` — Solve stiff differential
  equations using a trapezoidal rule and backward differentiation formula

#### Dependencies

To enable:

- Fixed-step time-domain solvers, set **Modeling domain**
  to `Time(Fixed step)`.
- Continuous time-domain solvers, set **Modeling domain**
  to `Time (Continuous)`.

### **Pole fitting options** — Rational fit fitting options `Share all poles` (default) | `Fit individually` | `Share poles by columns`

Rational fit fitting options to control the complex frequency-dependent data
fitting process, specified as `Share all poles`,
`Fit individually`, or `Share poles by
columns`.

#### Dependencies

To set this parameter, set **Data source** to either
`file` or `sparameters`.

### **Rational arguments** — Rational fit arguments to control the fit `{ 'Tolerance',-40,'TendsToZero',false,'MaxPoles',48,'Qlimit',inf }` (default) | cell array

Rational fit fitting arguments to control the fit, specified as a cell
array.

#### Dependencies

To set this parameter, set **Data source** to either
`file` or `sparameters`.

### **FIR filter length** — Filter length of 1-D digital filter `128` (default) | real positive integer

Filter length of the 1-D digital filter or impulse response duration, specified as
a real positive integer.

#### Dependencies

To set this parameter, set **Modeling domain** to
`Frequency (Digital filter)`.

### Visualization

### **First plot type** — Plot type `S21` (default) | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

Plot type of the first plot, specified as one of the following:

- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **Impulse response arguments** — Input arguments to plot impulse response `[ 1e-11, 1e4]` (default) | two-element vector

Input arguments to plot the impulse response, specified as a two-element vector.
Plot the impulse response by specifying the sample time of the input signal and the
number of samples in this parameter. For more information, see `impulse`.

#### Dependencies

To set this parameter, set **First plot type** or
**Second plot type** to `Impulse
response`.

### **Step response arguments** — Input arguments to plot step response `[ 1e-11, 1e4, 1e-10 ]` (default) | three-element vector

Input arguments to plot the step response, specified as a three-element vector.
Plot the step response by specifying the sample time of the input signal, the number
of samples, and the amount of time required for the step signal to reach the maximum
value in this parameter. For more information, see `stepresp`.

#### Dependencies

To set this parameter, set **First plot type** or
**Second plot type** to `Step
response`.

### **First plot y-axis units** — Y-axis units of first plot `Magnitude (dB)` (default) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

Y-axis units of the first plot, specified as one of the following:

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### Dependencies

To set this parameter, set **First plot type** to
`S21`.

### **Second Plot type** — Plot type of second plot `None` (default) | `S21` | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

Plot type of the second plot, specified as one of the following:

- `None`
- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **Second plot y-axis units** — Y-axis units of second plot `Magnitude (dB)` (default) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

Y-axis units of the second plot, specified as one of the following:

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### Dependencies

To set this parameter, set **Second plot type** to
`S21`.

### **X-axis frequency points (Hz)** — Frequency points to plot S-parameter data `logspace(8,10,2001)` (default) | positive real vector

Frequency points to plot the S-parameter data, specified as a positive real vector
in Hz.

### **X-axis scale** — Linear or logarithmic X-axis scale `Linear` (default) | `Logarithmic`

Select this parameter to plot your data on a linear or logarithmic X-axis scale.
Specify `Linear` or
`Logarithmic`.

### **Y-axis scale** — Linear or logarithmic Y-axis scale `Linear` (default) | `Logarithmic`

Select this parameter to plot your data in a linear or logarithmic Y-axis scale.
Specify `Linear` or
`Logarithmic`.

### **Plot Sparameter characteristics** — Plot S-parameters data button

Select this button to plot the characteristics of the S-parameters data.
## Libraries

RF Blockset / Idealized Baseband

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: Parameter of S-Parameter block from Idealized Baseband library renamed

The **RF frequency (Hz)** parameter in the S-parameters block
in the Idealized Baseband library has been renamed to **Carrier frequency
(Hz)**.

When you open a model created in R2024b containing the S-parameter block,
the software replaces the **RF frequency (Hz)** parameter with the
**Carrier frequency (Hz)** parameter.

### R2024b: Parameters of S-parameters block from idealized baseband library have been renamed

The following parameters in the S-parameters block in the idealized
baseband library have been renamed.

| Parameter Name Before R2024b | Parameter Name Since R2024b |
| --- | --- |
| **Data File** | **File** |
| **Carrier frequency (Hz)** | **RF frequency (Hz)** |

The following parameter values in the S-parameters block in the idealized
baseband library have been changed.

| Parameter | Values Before R2024b | Values Since R2024b |
| --- | --- | --- |
| **Data source** | `Data file` | `file` |
| `S-parameters object` | `sparameters` |
| `Rational object` | `rational` |
| **Modeling domain** | `Time domain (Fixed step)` | `Time (Fixed step)` |
| `Time domain (Continuous)` | `Time (Continuous)` |
| `Frequency domain (Digital filter)` | `Frequency (Digital filter)` |

When you open a model created before R2024b containing the S-parameters block, the
software replaces the parameter names and values as shown in the table.

## Description

Model RF complex baseband S-parameters in Simulink

Use the Idealized Baseband S-parameter block to model RF complex baseband S-parameters in
Simulink®. You can input your S-parameters as a Touchstone file,
an `sparameters` object, or as a `rational` object. If you
describe the S-parameters using a Touchstone file or an `sparameters` object,
the software uses rational fitting to derive a `rational` object. You can also
model your S-parameters data in either the time or frequency domain and plot the S-parameters
characteristics.

If you want to design S-parameters with impedance mismatches, use the Circuit Envelope
S-Parameters block.
