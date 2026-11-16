---
type: simulink-block
title: 'CTLE'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'ctle'
documentation_source_path: 'ref/ctle.html'
language: en
---

# CTLE

## Ports

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal. The input signal can be a sample-by-sample signal
specified as a scalar, or an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output. If the input signal is a sample-by-sample signal
specified as a scalar, then the output is also scalar. If the input signal is an
impulse response vector signal, then the output is also a vector.

**Data Types:** `double`

## Parameters

### **Mode** — CTLE operating mode `Adapt` (default) | `Off` | `Fixed`

CTLE operating mode:

- `Off` — CTLE is bypassed and the input
  waveform remains unchanged.
- `Fixed` — CTLE applies the CTLE transfer
  function as specified by **Configuration select** to the input
  waveform.
- `Adapt` — If the input signal is an impulse response vector
  or a waveform vector, then the Init subsystem calls to the CTLE System object™. The CTLE System object determines the CTLE transfer function to maximize the SNR and
  applies the transfer function to the input waveform for time domain simulation.
  This optimized transfer function is used by the CTLE for entire time domain
  simulation. For more information about the Init subsystem, see Statistical Analysis in SerDes Systems

  If the input signal is a sample-by-sample scalar, then the CTLE
  operates in the `Fixed` mode.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current CTLE
  **Mode**.
- Use `set_param(gcb,'Mode',value)` to set CTLE to a specific
  **Mode**.

### **Slice select** — Select which corner of 3D GPZ matrix to use `0` (default) | nonegative scalar integer

Select which slice, family, or corner of a 3-D GPZ matrix to use during CTLE
configuration.

You must set the **Specification** parameter to `'GPZ
Matrix'` to effectively use the **Slice Select**
parameter. Depending on how many slices are available in your GPZ matrix, you can then
select the slice you are interested in from a zero-based index available from the
dropdown menu.

You cannot use GPZ for a given slice and the peaking gain, DC gain, or AC gain for
another slice.

#### Programmatic Use

- Use `get_param(gcb,'SliceSelect')` to view the current
  value of **Slice select**.
- Use `set_param(gcb,'SliceSelect',value)` to set
  **Slice select** to a specific value.

**Data Types:** `double`

### **Configuration select** — Select which member of transfer function to apply in fixed mode `0` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8`

Select which transfer function configuration to apply in CTLE fixed mode, specified
as a real integer scalar. Depending on the **Specification**,
**Configuration select** specifies which gain coefficient is applied
to the filter transfer function.

For example, setting **Configuration select** to
*n* and **Specification** to `'DC Gain
and Peaking Gain'` selects the (*n*+1)-th element in the
**DC gain (dB)** and **Peaking gain (dB)** vectors
to be applied to the filter transfer function.

If CTLE **Mode** is set to `Adapt` and the
input is an impulse response vector or a waveform vector, **Configuration
select** is automatically calculated to determine the best eye height
opening. To view the value of the **Configuration select** parameter,
choose **Add Plots** > **Report** in the SerDes Designer
app.

#### Programmatic Use

- Use `get_param(gcb,'ConfigSelect')` to view the current
  value of **Configuration select**.
- Use `set_param(gcb,'ConfigSelect',value)` to set
  **Configuration select** to a specific value.

**Data Types:** `double`

### **Specification** — Input specification for CTLE response `'DC Gain and Peaking Gain'` (default) | `'DC Gain and AC Gain'` | `'AC Gain and Peaking Gain'` | `'GPZ Matrix'`

Defines which inputs will be used for the CTLE transfer function family. There are
five inputs which can be used to define the CTLE transfer function family: **DC
gain (dB)**, **Peaking gain (dB)**, **AC gain
(dB)**, **Peaking frequency (Hz)**, and **Gain pole
zero matrix**.

You can define the CTLE response from any two of the three gains and peaking
frequency or you can define the GPZ matrix for the CTLE.

- Select `'DC Gain and Peaking Gain'` to specify CTLE response
  from **DC gain (dB)**, **Peaking gain (dB)**,
  and **Peaking frequency (Hz)**.
- Select `'DC Gain and AC Gain'` to specify CTLE response is
  from **DC gain (dB)**, **AC gain (dB)**, and
  **Peaking frequency (Hz)**.
- Select `'AC Gain and Peaking Gain'` to specify CTLE response
  from **AC gain (dB)**, **Peaking gain (dB)**,
  and **Peaking frequency (Hz)**.
- Select `'GPZ Matrix'` to specify CTLE response is from
  **Gain pole zero matrix**.

#### Programmatic Use

- Use `get_param(gcb,'Specification')` to view the current
  CTLE **Specification**.
- Use `set_param(gcb,'Specification',value)` to set CTLE to a
  specific **Specification**.

**Data Types:** `char`

### **DC gain (dB)** — Gain at zero frequency `[0:-1:-8]` (default) | scalar | vector

Gain at zero frequency for the CTLE transfer function, specified as a scalar or a
vector in dB. If specified as a scalar, it is converted to match the length of
**Peaking gain (dB)**, **AC gain (dB)**, and
**Peaking frequency (Hz)** by scalar expansion. If specified as a
vector, the vector length must be the same as the vectors in **Peaking gain
(dB)**, **AC gain (dB)**, and **Peaking frequency
(Hz)**.

#### Dependencies

This parameter is only available when **Specification** is set to
`'DC Gain and Peaking Gain'` or `'DC Gain and
AC Gain'`.

#### Programmatic Use

- Use `get_param(gcb,'DCGain')` to view the current value of
  **DC gain (dB)**.
- Use `set_param(gcb,'DCGain',value)` to set **DC
  gain (dB)** to a specific value.

**Data Types:** `double`

### **Peaking gain (dB)** — Difference between AC and DC gain `[0:8]` (default) | scalar | vector

Peaking gain, specified as a scalar or vector in dB. **Peaking gain
(dB)** is the difference between **AC gain (dB)** and
**DC gain (dB)** for the CTLE transfer function. If specified as a
scalar, it is converted to match the length of **DC gain (dB)**,
**AC gain (dB)**, and **Peaking frequency (Hz)** by
scalar expansion. If specified as a vector, the vector length must be the same as the
vectors in **DC gain (dB)**, **AC gain (dB)**, and
**Peaking frequency (Hz)**.

#### Dependencies

This parameter is only available when **Specification** is set to
`'DC Gain and Peaking Gain'` or `'AC Gain and
Peaking Gain'`.

#### Programmatic Use

- Use `get_param(gcb,'PeakingGain')` to view the current
  value of **Peaking gain (dB)**.
- Use `set_param(gcb,'PeakingGain',value)` to set
  **Peaking gain (dB)** to a specific value.

**Data Types:** `double`

### **AC gain (dB)** — Gain at peaking frequency `0` (default) | scalar | vector

Gain at the peaking frequency for the CTLE transfer function, specified as a scalar
or vector in dB. If specified as a scalar, it is converted to match the length of
**DC gain (dB)**, **Peaking gain (dB)**, and
**Peaking frequency (Hz)** by scalar expansion. If specified as a
vector, the vector length be the same as the vectors in **DC gain
(dB)**, **Peaking gain (dB)**, and **Peaking
frequency (Hz)**.

#### Dependencies

This parameter is only available when **Specification** is set to
`'DC Gain and AC Gain'` or `'AC Gain and
Peaking Gain'`.

#### Programmatic Use

- Use `get_param(gcb,'ACGain')` to view the current value of
  **AC gain (dB)**.
- Use `set_param(gcb,'ACGain',value)` to set **AC
  gain (dB)** to a specific value.

**Data Types:** `double`

### **Peaking frequency (Hz)** — Approximate frequency at which CTLE transfer function peaks `5e9` (default) | scalar | vector

Approximate frequency at which CTLE transfer function peaks in magnitude, specified
as a scalar or a vector in GHz. If specified as a scalar, it is converted to match the
length of **DC gain (dB)**, **AC gain (dB)**, and
**Peaking gain (dB)** by scalar expansion. If specified as a vector,
the vector length must be the same as the vectors in **DC gain (dB)**,
**AC gain (dB)**, and **Peaking gain (dB)**.

#### Dependencies

This parameter is not available when **Specification** is set to
`'GPZ Matrix'`.

#### Programmatic Use

- Use `get_param(gcb,'PeakingFrequency')` to view the current
  value of **Peaking frequency (Hz)**.
- Use `set_param(gcb,'PeakingFrequency',value)` to set
  **Peaking frequency (Hz)** to a specific value.

**Data Types:** `double`

### **Gain pole zero matrix** — Gain pole zero matrix

Gain pole zero, specified as a matrix. **Gain pole zero matrix**
explicitly defines the family of CTLE transfer functions by specifying the **DC
gain (dB)** (dB) in the first column and then poles and zeros in alternating
columns. The poles and zeros are specified in Hz. Use the parameter
**Configuration Select** to select filters defined by rows of the GPZ
matrix

The block only allows repeated poles or zeros when it uses a cascaded filter. To
change the filter method the block uses, look under the mask and double click the CTLE
System object. This launches block parameters dialog box, and you can find the
**Filter method** parameter in the
**Advanced** tab.

Complex poles or zeros must have conjugates. The number of poles must be greater
than number of zeros for system stability. The block ignores poles and zeros of 0 Hz and
you can use them to zero-pad the matrix.

You can define multiple slices of CTLE responses by using a 3-D GPZ matrix. You can
concatenate and zero-pad two GPZ matrices to extend to the third dimension.

**Example:** To create a gain pole zero matrix with three poles and two zeroes, input the
matrix as follows: [G, P1, Z1, P2, Z2, P3].

#### Dependencies

This parameter is only available when **Specification** is set to
`'GPZ Matrix'`.

#### Programmatic Use

- Use `get_param(gcb,'GPZ')` to view the current value of
  **Gain pole zero matrix**.
- Use `set_param(gcb,'GPZ',value)` to set **Gain pole
  zero matrix** to a specific value.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Visualize Response** — Plot CTLE response button

Click to plot the CTLE response. The resulting plot shows CTLE transfer function
family curves for different CTLE configurations.

### **Launch CTLE Fitter App** — Launch CTLE Fitter app button

Click to launch the CTLE fitter app. For more information, see CTLE
Fitter.

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file. If
you deselect **Mode**, it is removed from the AMI files, effectively
hard-coding **Mode** to its current value.

### **Slice select** — Include Slice select parameter in IBIS-AMI model on (default) | off

Select to include **Slice select** as a parameter in the IBIS-AMI
file. If you deselect **Slice select**, it is removed from the AMI
files, effectively hard-coding **Slice select** to its current
value.

### **Configuration select** — Include Configuration select parameter in IBIS-AMI model on (default) | off

Select to include **Configuration select** as a parameter in the
IBIS-AMI file. If you deselect **Configuration select**, it is removed
from the AMI files, effectively hard-coding **Configuration select** to
its current value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2023b: Slice Select

you can now select which slice, family, or corner of a 3-D GPZ matrix to use during CTLE
configuration.

## Description

Models continuous time linear equalizer (CTLE)

The CTLE block applies a linear peaking filter to equalize the frequency
response of a sample-by-sample input signal. The equalization process reduces distortions
resulting from lossy channels. The filter is a real one-zero two-pole (1z/2p) filter, unless
you define the gain-pole-zero (GPZ) matrix. The time domain filter coefficients can be
calculated from one large partial fraction or many cascaded sections.
