---
type: simulink-block
title: 'Filter'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'filteridealizedbaseband'
documentation_source_path: 'ref/filteridealizedbaseband.html'
language: en
---

# Filter

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
- name: Design method
  summary: Filter design method Butterworth (default) | Chebyshev | Inverse Chebyshev
  group: Main
- name: Filter type
  summary: Filter response type Lowpass (default) | Highpass | Bandpass | Bandstop
  group: Main
- name: Implement using filter order
  summary: Implement using filter order off (default) | on
  group: Main
- name: Filter order
  summary: Filter order 3 (default) | integer greater than 2
  group: Main
- name: Passband frequency (Hz)
  summary: Passband frequency 1e9 (default) | positive real scalar | positive ascending two-tuple vector
  group: Main
- name: Passband attenuation (dB)
  summary: Passband attenuation 10*log10(2) (default) | positive real scalar
  group: Main
- name: Stopband frequencies (Hz)
  summary: Stopband frequencies for bandstop filters 2000000000 (default) | positive real scalar | positive ascending two-tuple
    vector
  group: Main
- name: Stopband attenuation (dB)
  summary: Stopband attenuation 40 (default) | positive real scalar
  group: Main
- name: RF frequency (Hz)
  summary: Center of signal bandwidth 1000000000 (default) | positive real scalar
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

### **Design method** — Filter design method `Butterworth` (default) | `Chebyshev` | `Inverse Chebyshev`

Filter design method, specified as one of the following:

- `Butterworth`
- `Chebyshev`
- `Inverse Chebyshev`

### **Filter type** — Filter response type `Lowpass` (default) | `Highpass` | `Bandpass` | `Bandstop`

Filter response type, specified as one of the following:

- `Lowpass` — Simulates a lowpass filter type with the
  design specified in **Design method**.
- `Highpass` — Simulates a highpass filter type with
  the design specified in **Design method**.
- `Bandpass` — Simulates a bandpass filter type with
  the design specified in **Design method**.
- `Bandstop` — Simulates a bandstop filter type with
  the design specified in **Design method**.

### **Implement using filter order** — Implement using filter order `off` (default) | `on`

Select this parameter to implement the filter order manually.

### **Filter order** — Filter order `3` (default) | integer greater than `2`

Filter order, specified as a integer greater than `2`. If you
set **Filter design** to `Lowpass` or
`Highpass`, specify the number of lumped storage elements.
If you set  **Filter design** to `Bandpass`
or `Bandstop`, specify twice the number of lumped storage
elements.

#### Dependencies

To enable this parameter, select **Implement using filter
order**.

### **Passband frequency (Hz)** — Passband frequency `1e9` (default) | positive real scalar | positive ascending two-tuple vector

Passband frequency for lowpass, highpass, and bandpass filter types, specified as
a positive real scalar or positive ascending two-tuple vector in Hz. Based on the
**Filter Type**, accepted value types and default values differ as
follows.

| Filter Type | Value Type | Default Values (Hz) |
| --- | --- | --- |
| Lowpass | Positive real scalar | `1e9` |
| Highpass | Positive real scalar | `2000000000` |
| Bandpass | Positive ascending two-tuple vector | `[2000000000 3000000000]` |

#### Dependencies

To enable this parameter, set **Filter type** to
`Lowpass`, `Highpass`, or
`Bandpass`.

### **Passband attenuation (dB)** — Passband attenuation `10*log10(2)` (default) | positive real scalar

Passband attenuation of the filter, specified as a positive real scalar in dB. For
bandpass filters, this value is applied equally to both edges of the passband.

#### Dependencies

To enable this parameter, set **Filter type** to
`Lowpass`, `Highpass`, or
`Bandpass`.

### **Stopband frequencies (Hz)** — Stopband frequencies for bandstop filters `2000000000` (default) | positive real scalar | positive ascending two-tuple vector

Stopband frequencies for bandstop filters, specified as either a positive real
scalar or positive ascending two-tuple vector in Hz. Based on the **Filter
Type** and **Implement using filter order** parameters,
accepted value types and default values differ as follows.

| Filter Type | Value Type | Default Values (Hz) | To enable this parameter |
| --- | --- | --- | --- |
| Lowpass | Positive real scalar | `2000000000` | Set **Filter type** to `Lowpass` and clear **Implement using filter order**. |
| Highpass | Positive real scalar | `1000000000` | Set **Filter type** to `Highpass` and clear **Implement using filter order**. |
| Bandpass | Positive ascending two-tuple vector | `[1500000000 3500000000]` | Set **Filter type** to `Bandpass` and clear **Implement using filter order**. |
| Bandstop | Positive ascending two-tuple vector | `[2100000000 2900000000]` | Set **Filter type** to `Bandstop` and clear or select **Implement using filter order**. |

### **Stopband attenuation (dB)** — Stopband attenuation `40` (default) | positive real scalar

Stopband attenuation, specified as a positive real scalar greater than the
**Passband attenuation (dB)** value in dB.

#### Dependencies

To enable this parameter, you can either:

- Set **Filter type** to
  `Lowpass`, `Highpass`, or
  `Bandpass` and clear **Implement using
  filter order**.
- Set **Filter type** to
  `Bandstop`, select **Implement using filter
  order**.

### **RF frequency (Hz)** — Center of signal bandwidth `1000000000` (default) | positive real scalar

Center of the signal bandwidth with respect to the filter transfer function,
specified as a positive real scalar in Hz. The signal bandwidth is 1Simulink Step Size.

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

- `Time (Fixed step)` — Model using fixed-step
  solvers (`NDF2`,
  `Trapezoidal`, and `Backward
  Euler`)
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
  to `Time (Fixed step)`.
- Continuous time-domain solvers, set **Modeling domain**
  to `Time (Continuous)`.

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

### R2024b: Parameters of Filter block from idealized baseband library have been renamed

The following in the Filter block in the idealized baseband library have
been renamed:

| Parameter Name Before R2024b | Parameter Name Since R2024b |
| --- | --- |
| **Carrier frequency (Hz)** | **RF frequency (Hz)** |

The following parameter values in the Filter block in the idealized
baseband library have been changed.

| Parameter | Values Before R2024b | Values Since R2024b |
| --- | --- | --- |
| **Modeling domain** | `Time domain (Fixed step)` | `Time (Fixed step)` |
| `Time domain (Continuous)` | `Time (Continuous)` |
| `Frequency domain (Digital filter)` | `Frequency (Digital filter)` |

When you open a model created before R2024b containing the S-parameters block, the
software replaces the parameter names and values as shown in the table.

### R2023a: Lowpass RF, Highpass RF, Bandpass RF, and Bandstop RF Filter blocks have been replaced

Starting in R2023a, the idealized baseband Filter block
replaces the Lowpass RF Filter, Highpass RF Filter,
Bandpass RF Filter, and Bandstop RF Filter blocks.

When you open a model created before R2023a containing the Lowpass RF
Filter, Highpass RF Filter, Bandpass RF Filter, and
Bandstop RF Filter Filter blocks, the software replace the old blocks with
the new idealized baseband Filter
block.

## Description

Filter RF complex baseband signals in Simulink

Use the Idealized Baseband Filter block to filter RF complex baseband
signals in Simulink. You can use the Butterworth, Chebyshev, or inverse Chebyshev design
methods to design your filter. You can also model your filter either in the time- or
frequency-domain and plot the filter characteristics.

To design an RF filter with impedance mismatches, use the Circuit Envelope Filter block.

**Note**

The Idealized Baseband Filter block replaces the Lowpass RF Filter,
Highpass RF Filter, Bandpass RF Filter, and Bandstop RF Filter blocks.
