---
type: simulink-block
title: 'CPM Phase Recovery'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Propagation and Channel Models'
documentation_page: 'cpmphaserecovery'
documentation_source_path: 'ref/cpmphaserecovery.html'
language: en
---

# CPM Phase Recovery

## Ports

Not documented in R2025b.

## Parameters

**P**
:   The denominator of the modulation index for CPM
    (h = K / P) when expressed as a proper fraction.

**Observation interval**
:   The number of symbols for which the carrier phase is assumed constant. The
    observation interval parameter must be an integer multiple of the input
    signal vector length.

    When this parameter is exactly equal to the vector length of the input
    signal, then the block always works. When the integer multiple is not equal
    to `1`, on the **Simulation** tab,
    select **Model Settings**. Then in the
    **Solver** > **Solver selection**
    section, choose **Type:**
    `Fixed-step` and clear the **Treat each discrete
    rate as a separate task** checkbox.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2020a: CPM Phase Recovery has been removed

CPM Phase Recovery has been removed. Use Carrier Synchronizer instead.

## Description

(Removed) Recover carrier phase using 2P-Power method

The CPM Phase Recovery block recovers the carrier phase of the input signal using the
2P-Power method. This feedforward, non-data-aided, clock-aided method is suitable for
systems that use these types of baseband modulation: continuous phase modulation (CPM),
minimum shift keying (MSK), continuous phase frequency shift keying (CPFSK), and
Gaussian minimum shift keying (GMSK). This block is suitable for use with blocks in the
Baseband Continuous Phase Modulation library.

If you express the modulation index for CPM as a proper fraction,
h = K / P, then P is the number to which the name "2P-Power" refers.
The observation interval parameter must be an integer multiple of the input signal
vector length.

The 2P-Power method assumes that the carrier phase is constant over a series of
consecutive symbols, and returns an estimate of the carrier phase for the series. The
**Observation interval** parameter is the number of symbols for
which the carrier phase is assumed constant. This number must be an integer multiple of
the input signal's vector length.

### Input and Output Signals

This block accepts a scalar or column vector input signal of type
`double` or `single`. The input signal
represents a baseband signal at the symbol rate, so it must be complex-valued and
must contain one sample per symbol.

The outputs are as follows:

- The output port labeled `Sig` gives the result of
  rotating the input signal counterclockwise, where the amount of rotation
  equals the carrier phase estimate. The `Sig` output is thus
  a corrected version of the input signal, and has the same sample time and
  vector size as the input signal.
- The output port labeled `Ph` outputs the carrier phase
  estimate, in degrees, for all symbols in the observation interval. The
  `Ph` output is a scalar signal.

  **Note**

  Because the block internally computes the argument of a complex
  number, the carrier phase estimate has an inherent ambiguity. The
  carrier phase estimate is between -90/P and 90/P degrees and might
  differ from the actual carrier phase by an integer multiple of 180/P
  degrees.

### Delays and Latency

The block's algorithm requires it to collect symbols during a period of length
**Observation interval** before computing a single estimate of
the carrier phase. Therefore, each estimate is delayed by **Observation
interval** symbols and the corrected signal has a latency of
**Observation interval** symbols, relative to the input
signal.
