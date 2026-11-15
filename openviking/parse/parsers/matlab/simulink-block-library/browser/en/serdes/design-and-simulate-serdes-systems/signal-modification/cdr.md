---
type: simulink-block
title: 'CDR'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'cdr'
documentation_source_path: 'ref/cdr.html'
language: en
---

# CDR

## Ports

### Input

### **WaveIn** — Input baseband signal scalar

Input baseband signal. The input to the CDR must be applied as one sample at a
time and not as a vector.

**Data Types:** `double`

## Parameters

### **CDR Mode** — Determine CDR order `1st order` (default) | `2nd order`

Determine the CDR order to enable phase and frequency tracking.

- `1st order` — Only tracks the phase.
- `2nd order` — Tracks both the phase and
  frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CDRMode` |
| **Type:** character vector |
| **Values:** `1st order` | `2nd order` |
| **Default:** `1st order` |

### **Phase Detector** — Clock phase detector option `BangBang` (default) | `BaudRateTypeA`

Clock phase detector option used in the clock data recovery. You can choose between
bang-bang (Alexander) or baud-rate type-A (Mueller-Muller).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseDetector` |
| **Type:** character vector |
| **Values:** `BangBang` | `BaudRateTypeA` |
| **Default:** `BangBang` |

### **Phase Offset (symbol time)** — Clock phase offset `0` (default) | real scalar in the range [-0.5,0.5]

Clock phase offset, specified as a real scalar in the range [-0.5,0.5] in fraction
of symbol time. **Phase Offset** is used to manually shift clock
probability distribution function (PDF) for better bit error rate (BER).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseOffset` |
| **Type:** character vector |
| **Values:** real scalar in the range [-0.5,0.5] |
| **Default:** `0` |

**Data Types:** `double`

### **Reference offset (ppm)** — Reference clock offset impairment `0` (default) | real scalar in the range [0, 300]

Reference clock offset impairment, specified as a real scalar in the range [0, 300]
in parts per million (ppm). **Reference offset (ppm)** is the deviation
between transmitter oscillator frequency and receiver oscillator frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ReferenceOffset` |
| **Type:** character vector |
| **Values:** real scalar in the range [0, 300] |
| **Default:** `0` |

**Data Types:** `double`

### **Early/late count threshold** — Early or late CDR count threshold to trigger phase update `16` (default) | real positive integer ≥5

Early or late CDR count threshold to trigger a phase update, specified as a unitless
real positive integer ≥5. Increasing the value of **Early/late count
threshold** provides a more stable output clock phase at the expense of
convergence speed. Because the bit decisions are made at the clock phase output, a more
stable clock phase has a better bit error rate (BER).

**Early/late count threshold** also controls the bandwidth of the
CDR.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Count` |
| **Type:** character vector |
| **Values:** real positive integer ≥5 |
| **Default:** `16` |

**Data Types:** `double`

### **Step (symbol time)** — Clock phase resolution `0.0078` (default) | real scalar

Clock phase resolution, specified as a real scalar in fraction of symbol time.
**Step (symbol time)** is the inverse of the number of phase
adjustments in CDR.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Step` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0.0078` |

**Data Types:** `double`

### **Frequency tracking gain** — Internal gain for frequency tracking `0.00048828125` (default) | nonnegative real scalar

Internal gain for the frequency tracking loop, specified as a nonnegative real
scalar.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyStep` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0.00048828125` |

**Data Types:** `double`

### **Frequency tracking update** — Frequency tracking update `16` (default) | nonnegative integer scalar

Once every **Frequency tracking update** symbols, update the system
phase rotator clock with the frequency estimate.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyCount` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `16` |

**Data Types:** `double`

### **Frequency step ramp** — Number of symbol times required for initial internal frequency tracking gain to reach specified value `3000` (default) | nonnegative integer scalar

To help frequency tracking loop lock early in a simulation, the initial
**Frequency tracking gain** starts at a high value of 1/(2\***Frequency tracking update)**. Then the **Frequency tracking gain** gradually
reduces to the specified value by roughly **Frequency step ramp**
symbol times.

#### Dependencies

To enable this parameter, set the **CDR Mode** to
`2nd order`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyStepRamp` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `3000` |

**Data Types:** `double`

### **Sensitivity (V)** — Sampling latch metastability voltage `0` (default) | real scalar

Sampling latch metastability voltage, specified as a real scalar in volts. If the
data sample voltage lies within the region (±**Sensitivity (V)**),
there is a 50% probability of bit error.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Sensitivity` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

**Data Types:** `double`

#### IBIS-AMI parameters

### **Phase Offset** — Include Phase Offset parameter in IBIS-AMI model on (default) | off

Select to include **Phase Offset** as a parameter in the IBIS-AMI
file. If you deselect **Phase Offset**, it is removed from the AMI
files, effectively hard-coding **Phase Offset** to its current
value.

### **Reference offset** — Include Reference offset parameter in IBIS-AMI model on (default) | off

Select to include **Reference offset** as a parameter in the
IBIS-AMI file. If you deselect **Reference offset**, it is removed from
the AMI files, effectively hard-coding **Reference offset** to its
current value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Models a clock data recovery circuit

The CDR block provides clock sampling times and estimates data symbols at
the receiver using a first order phase tracking and optionally a second order frequency
tracking CDR model. For more information, see Clock and Data Recovery in SerDes System..
