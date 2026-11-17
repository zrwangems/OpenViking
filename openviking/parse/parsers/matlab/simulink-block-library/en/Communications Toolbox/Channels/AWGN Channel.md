---
type: simulink-block
title: 'AWGN Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'awgnchannel'
documentation_source_path: 'ref/awgnchannel.html'
language: en
---

# AWGN Channel

## Ports
```yaml
ports:
- name: In
  summary: Input data signal vector | matrix
  direction: input
  data_types: double | single
- name: Var
  summary: Variance of additive white Gaussian noise positive scalar | vector
  direction: input
  data_types: double
- name: Out
  summary: Output data signal vector | matrix
  direction: output
```

### Input

### **In** — Input data signal vector | matrix

Input data signal, specified as an
*N*S-by-1 vector or an
*N*S-by-*N*C
matrix. *N*S represents the number of samples
in the input signal. *N*C represents the
number of channels, as determined by the number of columns in the input signal matrix.
Both *N*S and
*N*C can be equal to `1`.

The block adds frames of length-*N*S
Gaussian noise to each of the *N*C channels,
using a distinct random distribution per channel.

This port is unnamed on the block until the **Var** port is
added.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Var** — Variance of additive white Gaussian noise positive scalar | vector

Variance of additive white Gaussian noise, specified as a positive scalar or a
1-by-*N*C vector.
*N*C represents the number of channels, as
determined by the number of columns in the input signal matrix. For more information,
see Specifying the Variance Directly or Indirectly.

#### Dependencies

To enable this port, set **Mode** to
`Variance` and **Noise variance
source** to `Input port`.

**Data Types:** `double`
### Output

### **Out** — Output data signal vector | matrix

Output data signal for the AWGN channel, returned as a vector or matrix. The
datatype and dimensions of **Out** match those of the input signal, **In**. This port
is unnamed on the block.
## Parameters
```yaml
parameters:
- name: Mode
  summary: Variance mode Signal to noise ratio (SNR) (default) | Signal to noise ratio (Eb/No) | Signal to noise ratio (Es/No)
    | Variance
  group: ''
- name: SNR (dB)
  summary: Ratio of signal power to noise power 10 (default) | scalar | vector
  group: ''
- name: Eb/No (dB)
  summary: Ratio of information bit energy per symbol to noise power spectral density 10 (default) | scalar | vector
  group: ''
- name: Es/No (dB)
  summary: Ratio of information symbol energy per symbol to noise power spectral density 10 (default) | scalar | vector
  group: ''
- name: Number of bits per symbol
  summary: Number of bits in each input symbol 1 (default) | scalar | vector
  group: ''
- name: Input signal power, referenced to 1 ohm (watts)
  summary: Mean square power of input 1 (default) | scalar | vector
  group: ''
- name: Specify symbol duration in seconds
  summary: Specify symbol duration in seconds off (default) | on
  group: ''
- name: Samples per symbol
  summary: Samples per symbol 1 (default) | positive integer | vector of positive integers
  group: ''
- name: Symbol period (s)
  summary: Symbol period in seconds [1 2 4] (default) | positive scalar | vector
  group: ''
- name: Noise variance source
  summary: Noise variance source Parameter (default) | Input port
  group: ''
- name: Noise variance
  summary: Variance of white Gaussian noise 1 (default) | scalar | vector
  group: ''
- name: Random number source
  summary: Random number source Global stream (default) | mt19937ar with seed
  group: ''
- name: Initial seed
  summary: Noise generator initial seed 67 (default) | nonnegative integer
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Mode** — Variance mode `Signal to noise ratio (SNR)` (default) | `Signal to noise ratio (Eb/No)` | `Signal to noise ratio (Es/No)` | `Variance`

Variance mode, specified as `Signal to noise ratio
(Eb/No)`, `Signal to noise ratio (Es/No)`,
`Signal to noise ratio (SNR)`, or
`Variance`. For more information, see Relationship Among Eb/No, Es/No, and SNR Modes and
Specifying the Variance Directly or Indirectly.

### **SNR (dB)** — Ratio of signal power to noise power `10` (default) | scalar | vector

Ratio of signal power to noise power in decibels, specified as a scalar or
vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (SNR)`.

### **Eb/No (dB)** — Ratio of information bit energy per symbol to noise power spectral density `10` (default) | scalar | vector

Ratio of information bit energy per symbol to noise power spectral density in
decibels, specified as a scalar or vector. The information bit energy is the magnitude
without channel coding.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)`.

### **Es/No (dB)** — Ratio of information symbol energy per symbol to noise power spectral density `10` (default) | scalar | vector

Ratio of information symbol energy per symbol to noise power spectral density in
decibels, specified as a scalar or vector. The information symbol energy is the
magnitude without channel coding.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Es/No)`.

### **Number of bits per symbol** — Number of bits in each input symbol 1 (default) | scalar | vector

Number of bits in each input symbol, specified as a scalar or vector.

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)`.

### **Input signal power, referenced to 1 ohm (watts)** — Mean square power of input `1` (default) | scalar | vector

Mean square power of the input in watts, specified as a scalar or vector.

- When **Mode**
  is `Signal to noise ratio (Eb/No)` or `Signal
  to noise ratio (Es/No)`, the parameter is the mean square power of
  the input symbols.
- When **Mode**
  is `Signal to noise ratio (SNR)`, this parameter is the
  mean square power of the input samples.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)`, `Signal to
noise ratio (Es/No)`, or `Signal to noise ratio
(SNR)`.

### **Specify symbol duration in seconds** — Specify symbol duration in seconds `off` (default) | `on`

Select this parameter to specify symbol duration in seconds.

- When you select this parameter, set the **Symbol period
  (s)** parameter to specify the symbol period in seconds.
- When this parameter is not selected, set the **Samples per
  symbol** parameter to specify the samples per symbol in
  samples.

The block determines the sample time and appropriate noise to add at
model run time.

For more information, see Relationship Among Eb/No, Es/No, and SNR Modes.

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)` or `Signal to
noise ratio (Es/No)`.

### **Samples per symbol** — Samples per symbol `1` (default) | positive integer | vector of positive integers

Samples per symbol in samples, specified as a positive integer scalar or
vector.

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)` or `Signal to
noise ratio (Es/No)`, and do not select **Specify symbol
duration in seconds**.

### **Symbol period (s)** — Symbol period in seconds `[1 2 4]` (default) | positive scalar | vector

Symbol period in seconds, specified as a positive scalar or vector. When you use
this parameter, the block determines the sample time and appropriate noise to add at
model run time.

#### Dependencies

To enable this parameter, set **Mode** to
`Signal to noise ratio (Eb/No)` or `Signal to
noise ratio (Es/No)`, and select **Specify symbol
duration in seconds**.

### **Noise variance source** — Noise variance source `Parameter` (default) | `Input port`

Noise variance source, specified as a `Parameter` or
`Input port`. For more information, see Specifying the Variance Directly or Indirectly.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mode** to
`Variance`.

### **Noise variance** — Variance of white Gaussian noise `1` (default) | scalar | vector

Variance of the white Gaussian noise, specified as a scalar or vector. For more
information, see Specifying the Variance Directly or Indirectly.

**Tunable:** Yes

#### Dependencies

To enable this port, set **Mode** to
`Variance` and **Noise variance
source** to `Parameter`.

#### Randomization

### **Random number source** — Random number source `Global stream` (default) | `mt19937ar with seed`

Random number source, specified as a `Global stream` or
`mt19937ar with seed`. If you use the `parsim` (Simulink) function, see Tips.

### **Initial seed** — Noise generator initial seed `67` (default) | nonnegative integer

Noise generator initial seed for the mt19937ar algorithm, specified as a nonnegative
integer.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Random number
source** to `mt19937ar with seed`.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).
## Libraries

Communications Toolbox / Channels

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2025a: Specify symbol duration in seconds

In R2025a, this block adds the **Specify symbol duration in
seconds** parameter. When you select **Specify symbol duration in
seconds**, you specify the **Symbol period
(s)** parameter value. The block determines the sample time and appropriate
noise to add at model run time. For more information, see Specifying the Variance Directly or Indirectly.

### R2023b: Variance calculation update

In R2023b, use Upgrade Advisor (Simulink) to update instances of the
AWGN Channel block in your pre-R2023a models. In addition to the updates for
R2023a, these AWGN Channel block updates occur for this configuration:

- If the **Mode** parameter setting is `Signal to
  noise ratio (Eb/No)` or `Signal to noise ratio
  (Es/No)` and **Symbol period (s)** together with the
  block sample time results in a noninteger samples per symbol,
  **Mode** gets set to `Signal to noise ratio
  (SNR)` in the upgraded block.
- The **SNR (db)** parameter gets set to the appropriate SNR
  setting.

In R2023a, if the combination of the **Symbol period (s)** parameter
value and the block sample time resulted in a noninteger samples per symbol, using Upgrade Advisor (Simulink) to update the AWGN Channel block generates noise with
incorrect variance values.

If you have already updated your block in R2023a:

1. Select the AWGN Channel block in your model.
2. Run `set_param(gcb,'LegacyMode','on')` at the command line to
   revert the update.
3. Rerun Upgrade Advisor.

### R2023a: Variable-size support

This support enables you to vary the length of input signal each time the block executes
in your simulation.

### R2023a: Random number generator update

The AWGN Channel block updates the random number generator (RNG) source
permitting selection of `Global stream` or `mt19937ar with
seed`.

The new RNG provides better random number statistics. For simulations created before
R2023a, the block defaults to legacy mode with prior RNG (Ziggurat method - V5 RANDN
algorithm). In this mode, the block uses the Random
Source block to generate noise. Random numbers are generated using the Ziggurat
method (V5 RANDN algorithm). The block reuses the same initial seeds every time you rerun
the simulation, so that this block outputs the same signal each time you run a simulation.
To improve statistics, it is recommended that you run **Update Model** on
pre-R2023a simulations that use the AWGN Channel block.

### R2023a: Code Generation

Code generation is enabled by default. For more information, see **Simulate
using**.

## Description

Add white Gaussian noise to input signal

The AWGN Channel block adds white Gaussian noise to the input signal. It inherits the
sample time from the input signal.
