---
type: simulink-block
title: 'Band-Limited White Noise'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'bandlimitedwhitenoise'
---

# Band-Limited White Noise

Introduce white noise into continuous system

## Libraries

Simulink / Sources

## Description

The Band-Limited White Noise block generates normally distributed
random numbers that are suitable for use in continuous or hybrid systems.

### Simulation of White Noise

Theoretically, continuous white noise has a correlation time of 0, a flat power
spectral density (PSD), and a total energy of infinity. In practice, physical
systems are never disturbed by white noise, although white noise is a useful
theoretical approximation when the noise disturbance has a correlation time that is
very small relative to the natural bandwidth of the system.

In Simulink® software, you can simulate the effect of white noise by using a random
sequence with a correlation time much smaller than the shortest time constant of the
system. The Band-Limited White Noise block produces such a sequence.
The correlation time of the noise is the sample rate of the block. For accurate
simulations, use a correlation time much smaller than the fastest dynamics of the
system. You can get good results by specifying

tc≈11002πfmax,

where *fmax* is the bandwidth of the
system in rad/sec.

### Comparison with the Random Number Block

The primary difference between this block and the Random Number
block is that the Band-Limited White Noise block produces output at a
specific sample rate. This rate is related to the correlation time of the
noise.

### Usage with the Averaging Power Spectral Density Block

The Band-Limited White Noise block specifies a two-sided spectrum, where the
units are Hz. The Averaging Power Spectral Density block specifies a
one-sided spectrum, where the units are the square of the magnitude per unit radial
frequency: mag^2/(rad/sec). When you feed the output of a Band-Limited White
Noise block into an Averaging Power Spectral Density block, the average
PSD value is π times smaller than the **Noise power** of the
Band-Limited White Noise block. This difference is the result of
converting the units of one block to the units of the other, 1/(1/2)(2`π`) = 1/`π`, where:

- 1/2 is the factor for converting from a two-sided to one-sided
  spectrum.
- 2`π` is the factor for converting from Hz to
  rad/sec.

## Ports

### Output

### **Port\_1** — Normally distributed random numbers scalar | vector | matrix | N-D array

Normally distributed random numbers specified as a scalar, vector,
matrix, or N-D array.

**Data Types:** `double`

## Parameters

### **Noise power** — Height of PSD of white noise `[0.1]` (default) | scalar | vector | matrix | N-D array

Specify the height of the PSD of the white noise as a scalar, vector,
matrix, or N-D array of positive values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Cov` |
| **Type:** character vector |
| **Values:** `scalar | vector | matrix | N-D array` |
| **Default:** `'[0.1]'` |

### **Sample time** — Correlation time of noise `0.1` (default) | scalar | vector

Correlation time of the noise. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** character vector |
| **Values:** `scalar | vector` |
| **Default:** `'0.1'` |

### **Seed** — Starting seed `[23341]` (default) | scalar | vector | matrix | N-D array

Specify the starting seed for the random number generator as a scalar,
vector, matrix, or N-D array. Values must be positive, real-valued, and
finite.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `seed` |
| **Type:** character vector |
| **Values:** `scalar | vector | matrix | N-D array` |
| **Default:** `'[23341]'` |

### **Interpret vector parameters as 1-D** — Treat vector parameters as 1-D `on` (default) | `off`

Select to output a 1-D array when the block parameters are vectors.
Otherwise, output a 2-D array one of whose dimensions is
`1`. For more information, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

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

Cannot use inside a triggered subsystem hierarchy.

## Version History

**Introduced before R2006a**
