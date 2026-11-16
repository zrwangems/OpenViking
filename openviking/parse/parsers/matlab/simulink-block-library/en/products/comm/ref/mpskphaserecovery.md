---
type: simulink-block
title: 'M-PSK Phase Recovery'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Propagation and Channel Models'
documentation_page: 'mpskphaserecovery'
documentation_source_path: 'ref/mpskphaserecovery.html'
language: en
---

# M-PSK Phase Recovery

## Ports

Not documented in R2025b.

## Parameters

**M-ary number**
:   The number of points in the signal constellation of the transmitted PSK
    signal. This value as an even integer.

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

### R2020a: M-PSK Phase Recovery has been removed

M-PSK Phase Recovery has been removed. Use Carrier Synchronizer instead.

## Description

(Removed) Recover carrier phase using M-Power method

The M-PSK Phase Recovery block recovers the carrier phase of the input signal using
the M-Power method. This feedforward, non-data-aided, clock-aided method is suitable for
systems that use baseband phase shift keying (PSK) modulation. It is also suitable for
systems that use baseband quadrature amplitude modulation (QAM), although the results
are less accurate than those for comparable PSK systems. The alphabet size for the
modulation must be an even integer.

For PSK signals, the **M-ary number** parameter represents the
alphabet size. For QAM signals, the **M-ary number** should be 4
regardless of the alphabet size because the 4-power method is the most appropriate for
QAM signals.

The M-Power method assumes that the carrier phase is constant over a series of
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
  carrier phase estimate is between -180/M and 180/M degrees and might
  differ from the actual carrier phase by an integer multiple of 360/M
  degrees.

### Delays and Latency

The block's algorithm requires it to collect symbols during a period of length
**Observation interval** before computing a single estimate of
the carrier phase. Therefore, each estimate is delayed by **Observation
interval** symbols and the corrected signal has a latency of
**Observation interval** symbols, relative to the input
signal.
