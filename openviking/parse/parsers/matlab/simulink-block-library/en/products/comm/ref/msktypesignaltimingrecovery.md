---
type: simulink-block
title: 'MSK-Type Signal Timing Recovery'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'msktypesignaltimingrecovery'
documentation_source_path: 'ref/msktypesignaltimingrecovery.html'
language: en
---

# MSK-Type Signal Timing Recovery

## Ports

Not documented in R2025b.

## Parameters

**Modulation type**
:   The type of modulation in the system. Choices are
    `MSK` and
    `GMSK`.

**Samples per symbol**
:   The number of samples, N, that represent each symbol in the input signal.
    This must be greater than 1.

**Error update gain**
:   A positive real number representing the step size that the block uses for
    updating successive phase estimates. Typically, this number is less than
    1/N, which corresponds to a slowly varying phase.

    This parameter is tunable in normal mode, Accelerator mode and Rapid
    Accelerator mode. If you use the Simulink®
    Coder™ rapid simulation (RSIM) target to build an RSIM executable,
    then you can tune the parameter without recompiling the model. For more
    information, see Tunable
    Parameters (Simulink).

**Reset**
:   Determines whether and under what circumstances the block restarts the
    phase estimation process. Choices are `None`,
    `Every frame`, and `On nonzero
    input via port`. The last option causes the block to have a
    second input port, labeled `Rst`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Recover symbol timing phase using fourth-order nonlinearity method

The MSK-Type Signal Timing Recovery block recovers the symbol timing phase of the
input signal using a fourth-order nonlinearity method. This block implements a general
non-data-aided feedback method that is independent of carrier phase recovery but
requires prior compensation for the carrier frequency offset. This block is suitable for
systems that use baseband minimum shift keying (MSK) modulation or Gaussian minimum
shift keying (GMSK) modulation.

### Inputs

By default, the block has one input port. The input signal could be (but is not
required to be) the output of a receive filter that is matched to the transmitting
pulse shape, or the output of a lowpass filter that limits the amount of noise
entering this block.

This block accepts a scalar-valued or column vector input signal.
The input uses *N* samples to represent each symbol,
where *N* > 1
is the **Samples per symbol** parameter.

- For a column vector input signal, the block operates
  in single-rate processing mode. In this mode, the output signal inherits
  its sample rate from the input signal. The input length must be a
  multiple of *N*.
- For a scalar input signal, the block operates in multirate
  processing mode. In this mode, the input and output signals have different
  sample rates. The output sample rate equals *N* multiplied
  by the input sample rate.
- This block accepts input signals of type Double or
  Single

If you set the **Reset** parameter to `On
nonzero input via port`, then the block has a second
input port, labeled `Rst`. The `Rst` input
determines when the timing estimation process restarts, and must be
a scalar.

- If the input signal is a scalar value, the sample
  time of the `Rst` input equals the symbol period
- If the input signal is a column vector, the sample
  time of the `Rst` input equals the input port sample
  time
- This block accepts reset signals of type Double or
  Boolean

### Outputs

The block has two output ports, labeled `Sym` and `Ph`:

- The `Sym` output is the result of
  applying the estimated phase correction to the input signal. This
  output is the signal value for each symbol, which can be used for
  decision purposes. The values in the `Sym` output
  occur at the symbol rate:

  - For a column vector input signal of length *N*\**R*,
    the `Sym` output is a column vector of length *R* having
    the same sample rate as the input signal.
  - For a scalar input signal, the sample rate of the `Sym` output
    equals *N* multiplied by the input sample rate.
- The `Ph` output gives the phase estimate
  for each symbol in the input.

  The `Ph` output contains nonnegative real numbers
  less than *N*. Noninteger values for the phase estimate
  correspond to interpolated values that lie between two values of the
  input signal. The sample time of the `Ph` output
  is the same as that of the `Sym` output.

  **Note**

  If the `Ph` output is very close to either
  zero or **Samples per symbol**, or if the actual
  timing phase offset in your input signal is very close to zero, then
  the block's accuracy might be compromised by small amounts of noise
  or jitter. The block works well when the timing phase offset is significant
  rather than very close to zero.
- The output signal inherits its data type from the
  input signal.

### Delays

When the input signal is a vector, this block incurs a delay
of two symbols. When the input signal is a scalar, this block incurs
a delay of three symbols.
