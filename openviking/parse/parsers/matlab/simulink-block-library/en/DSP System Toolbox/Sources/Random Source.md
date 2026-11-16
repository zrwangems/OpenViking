---
type: simulink-block
title: 'Random Source'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'randomsource'
documentation_source_path: 'ref/randomsource.html'
language: en
---

# Random Source

## Ports

### Output

### **Port\_1** — Signal of randomly distributed values scalar | vector | matrix

Signal of random values with uniform or Gaussian (normal)
distribution. The settings in the block dialog box determine the size,
data type, and complexity of the signal.

The block can generate a single-channel or a multichannel signal. The
**Samples per frame** parameter determines the
number of samples in each channel (column) of the signal. The
**Output data type** and **Signal
complexity** parameters determine the data type and
complexity of the signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

#### Distribution Settings

### **Distribution** — Uniform or Gaussian `Uniform` (default) | `Gaussian`

Specify the distribution from which to draw the random values as one of these:

- `Uniform` –– The block draws the
  output samples from a uniform distribution. You can specify the
  minimum and maximum values of the distribution using the
  **Minimum** and
  **Maximum** parameters, respectively. You
  can generate a complex number from the uniform distribution by
  setting the **Signal complexity** parameter to
  `Complex`.

  All values in this [**Minimum**
  **Maximum**] range have an equal likelihood to
  be selected.

  For an example, see Generate Random Signal with Uniform Distribution.
- `Gaussian` –– The block produces
  Gaussian random values by using the Ziggurat method. You can
  specify the mean and variance of the distribution using the
  **Mean** and **Variance**
  parameters. You can generate a complex Gaussian signal by
  setting the **Signal complexity** parameter to
  `Complex`.

  For an example, see Generate Random Signal with Gaussian Distribution.

### **Minimum** — Minimum value of uniform distribution `0` (default) | scalar | row vector

Specify the minimum value in the uniform distribution as a scalar or a row vector of
length *N*. When you specify a row vector, the block
generates an *M*-by-*N* matrix containing
a unique random distribution in each channel. *M* is the
value you specify in the **Samples per frame**
parameter.

For example, when you set **Minimum** to `[0 0 -3
-3]` and **Maximum** to `[10 10 20
20]`, the block generates a four-channel output whose first and
second columns contain random values in the range [0, 10], and whose third
and fourth columns contain random values in the range [-3, 20].

The **Minimum** and **Maximum** values must be scalars
or have the same number of columns. When you specify only one of the
**Minimum** and **Maximum** parameters
as a vector, the block expands the other parameter so that it is the same
length as the vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Distribution** to
`Uniform`.

### **Maximum** — Maximum value of uniform distribution `1` (default) | scalar | row vector

Specify the maximum value in the uniform distribution as a scalar or a row vector of
length *N*. When you specify a row vector, the block
generates an *M*-by-*N* matrix containing
a unique random distribution in each channel. *M* is the
value you specify in the **Samples per frame**
parameter.

For example, when you set **Minimum** to `[0 0 -3 -3]`
and **Maximum** to `[10 10 20 20]`, the
block generates a four-channel output whose first and second columns contain
random values in the range [0, 10], and whose third and fourth columns
contain random values in the range [−3, 20].

The **Minimum** and **Maximum** values must be scalars
or have the same number of columns. When you specify only one of the
**Minimum** and **Maximum** parameters
as a vector, the block expands the other parameter so it is the same length
as the vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Distribution** to
`Uniform`.

### **Mean** — Mean value of Gaussian distribution `0` (default) | scalar | row vector

Specify the mean of the Gaussian (normal) distribution as a scalar or a row vector of
length *N*. When you specify a row vector, the block
generates an *M*-by-*N* matrix containing
a distinct random distribution in each channel. *M* is the
value you specify in the **Samples per frame**
parameter.

The **Mean** and **Variance** values must be scalars or
have the same number of columns. When you specify only one of the
**Mean** and **Variance** parameters
as a vector, the block expands the other parameter so that it is the same
length as the vector.

To generate a complex output signal with a `Gaussian`
distribution, set **Signal complexity** to
`Complex` and specify a complex value in the
**Mean** parameter. For more information, see the
**Signal complexity** parameter description.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Distribution** to
`Gaussian`.

**Complex Number Support:** Yes

### **Variance** — Variance of Gaussian distribution `1` (default) | scalar | row vector

Specify the variance of the Gaussian (normal) distribution as a scalar or a row vector of
length *N*. When you specify a row vector, the block
generates an *M*-by-*N* matrix containing
a distinct random distribution in each channel. *M* is the
value you specify in the **Samples per frame**
parameter.

The **Mean** and **Variance** values must be scalars or
have the same number of columns. When you specify only one of the
**Mean** and **Variance** parameters
as a vector, the block expands the other parameter so that it is the same
length as the vector.

To generate a complex output signal with a `Gaussian`
distribution, the **Variance** parameter
σ2 specifies the total variance for each
output channel. This value is the sum of the variances of the real and
imaginary components in that channel. For more information, see the
**Signal complexity** parameter description.

#### Dependencies

To enable this parameter, set **Distribution** to
`Gaussian`.

#### Random Generator Settings

### **Repeatability** — Option to repeat block output `Specify seed` (default) | `Not repeatable`

Option to repeat block output, specified as one of these:

- `Specify seed` — The block uses
  the initial seed that you specify in the **Initial
  seed** parameter to produce a repeatable output for
  every simulation.
- `Not repeatable` — The block
  randomly selects an initial seed and produces a different
  pseudorandom sequence for every simulation.

For an example that shows the behavior of this parameter, see Repeat Random Signal Output.

### **Initial seed** — Initial seed for random number generator `1` (default) | scalar

Specify the initial seed(s) for the random number generator as a scalar. The generator
produces an identical sequence of pseudorandom numbers each time you
simulate the block with a particular initial seed.

#### Dependencies

To enable this parameter, set **Repeatability** to
`Specify seed`.

#### Signal Properties

### **Inherit via output port** — Inherit output port parameters from downstream block `off` (default) | `on`

When you select this check box, the block inherits the signal properties such as the
samples per frame, output data type, signal complexity, and sample time from
the downstream block and disables the corresponding parameters in the block
dialog box. For an example, see Inherit Signal Properties Via Output Port.

Suppose that you want to back propagate a 1-D vector. The output of the
Random Source block is a 1-D vector of length
*M*, where the block inherits the length
*M* from the downstream block. When the
**Minimum**, **Maximum**,
**Mean**, or **Variance** parameter
specifies *N* channels, the 1-D vector output contains
*M*/*N* samples from each channel. An
error occurs in this case when *M* is not an integer
multiple of `N`.

Suppose that you want to back propagate a *M*-by-*N*
signal. When *N* > `1`, your signal has
*N* channels. When *N* =
`1`, your signal has *M* channels. The
value of the **Minimum**, **Maximum**,
**Mean**, or **Variance** parameter
can be a scalar or a vector of length equal to the number of channels. You
can specify these parameters as row or column vectors, except when the
signal is a row vector. In this case, you must specify the
**Minimum**, **Maximum**,
**Mean**, or **Variance** parameter as
a row vector.

### **Sample time** — Output sample period `1` (default) | −1 | real positive scalar

Specify the sample period *T*s of the random
output sequence as a real positive scalar or `-1`. The
output frame period is *MT*s.

If *T*s = −1, the block inherits
the output sample period from its output port, but determines the dimensions
and complexity of the signal from the block settings.

#### Dependencies

To enable this parameter, clear the **Inherit via output
port** parameter.

### **Samples per frame** — Samples per output frame `1` (default) | positive integer

Specify the number of samples *M* in each output frame as
a positive integer. The output frame period is
*MT*s, where
*T*s is the value you specify in
the **Sample time** parameter.

#### Dependencies

To enable this parameter, clear the **Inherit via output
port** parameter.

### **Signal complexity** — Complexity of output `Real` (default) | `Complex`

Specify the complexity of the output as `Real` or
`Complex`. These settings control all channels
of the output. The real and complex components of the output are
statistically independent.

For a complex output with a `Uniform`
distribution, the block draws the real and imaginary components in each
channel from the same uniform random distribution, defined by the
**Minimum** and **Maximum** parameters
for that channel.

For a complex output with a `Gaussian`
distribution, the block draws the real and imaginary components in each
channel from normal distributions with different means. In this case, the
**Mean** parameter for each channel must be a complex
value. The real component of the **Mean** parameter
specifies the mean of the real components in the channel, while the
imaginary component specifies the mean of the imaginary components in the
channel. When you omit the real or imaginary component from the
**Mean** parameter, the block uses a default value of 0
for the mean of that component.

For example, a **Mean** parameter setting of
`[5+2i 0.5 3i]` generates a three-channel output with
these mean values.

|  |  |  |
| --- | --- | --- |
| Channel 1 mean | *real* = 5 | *imaginary* = 2 |
| Channel 2 mean | *real* = 0.5 | *imaginary* = 0 |
| Channel 3 mean | *real* = 0 | *imaginary* = 3 |

For a more detailed example, see Generate Complex Random Signal.

For a complex output, the **Variance** parameter
σ2 specifies the total variance for each
output channel. This value is the sum of the variances of the real and
imaginary components in that channel.

σ2=σRe2+σIm2

The block divides the variance value you specify equally between the real
and imaginary components.

σRe2=σ22σIm2=σ22

#### Dependencies

To enable this parameter, clear the **Inherit via output
port** parameter.

### **Output data type** — Output data type `double` (default) | `single`

Specify the data type of the output as double precision or single
precision.

#### Dependencies

To enable this parameter, clear the **Inherit via output
port** parameter.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: Random Source block has been updated

The Random Source block has been updated with these changes:

- Support for Mersenne Twister random number generator.
- The `Gaussian` distribution always uses the
  Zigguart method. The `Sum of uniform values`
  method is no longer supported.
- `Repeatable` option is removed. To generate a
  repeatable output, set **Repeatability** to
  `Specify seed`.
- The initial seed must be a scalar. You can no longer specify a vector
  of seed values.
- When you specify an initial seed, the seed is no longer tunable, that
  is, you cannot change the value of the seed during simulation.
- The **Sample mode** parameter is removed. The sample
  mode of the block is now always discrete.

If you open a model saved in R2023b or a previous version of MATLAB, the model continues to use the older version of the block in R2024a.
To use the updated version, obtain the Random Source block from the
**DSP System Toolbox**/**Sources**
library.

## Description

Generate randomly distributed values

The Random Source block outputs a random signal with a uniform or Gaussian
(normal) pseudorandom distribution. The block uses the Mersenne Twister random number
generator to generate the sequence. The settings in the block dialog box determine the
size, data type, and complexity of the signal.

The block can generate a single-channel or a multichannel signal.
