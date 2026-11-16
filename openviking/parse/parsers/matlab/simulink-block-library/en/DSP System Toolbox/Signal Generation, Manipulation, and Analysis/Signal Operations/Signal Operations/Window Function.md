---
type: simulink-block
title: 'Window Function'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Signal Operations'
documentation_page: 'windowfunction'
documentation_source_path: 'ref/windowfunction.html'
language: en
---

# Window Function

## Ports

### Input

### **In** — Input signal vector | matrix | *N*-D array

Input signal, specified as a vector, matrix, or an *N*-D
array.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

This port is enabled only when you set **Operation** to either
`Apply window to input` or `Generate and apply
window`.

This port is unnamed when you set **Operation** to
`Apply window to input`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Out** — Output vector | matrix | *N*-D array

Output signal, returned as a vector, matrix, or an *N*-D
array.

The **Out** port is enabled only when
**Operation** is set to:

- `Apply window to input` –– The block computes an
  *M*-by-1 window vector *w* and applies it to
  the *M*-by-*N* input, where
  *M* is the number of rows in the input signal.
- `Generate and apply window` –– The block generates
  an *M*-by-1 window vector *w* and applies it
  to the input.

The output signal has the same dimensions as the input signal. For more details,
see Operation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Win** — Window output vector

Window output, returned as a vector. When **Operation** is set to
`Apply window to input` or `Generate and apply
window`, the window vector is of the same length as the number of rows
in the input signal. When **Operation** is set to
`Generate window`, the length of window vector is
determined by the **Window length** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main

### **Operation** — Modes of operation `Apply window to input` (default) | `Generate window` | `Generate and apply window`

The Window Function block has three modes of operation that you can
select through the **Operation** parameter. In each mode, the block
first creates a window vector *w* by sampling the window specified in
the **Window type** parameter at *M* discrete
points. The operation modes are:

- `Apply window to input`

  In this mode, the block computes an *M*-by-1 window vector
  *w* and applies it to the input. The output
  *y* always has the same dimension as the input.

  When the input is an *M*-by-*N* matrix
  *u*, the window is multiplied element-wise with each of the
  *N* channels in the input matrix *u*. This is
  equivalent to the following MATLAB® code:

  ```
  y = repmat(w,1,N) .* u								% Equivalent MATLAB code
  ```

  The window is always applied to the first dimension:

  y(i,j,...,k)=w(i)\*u(i,j,...,k)       i=1,...,M,  j=1,...,N,  ...,  k=1,...,P

  A length-*M* unoriented vector input is treated as an
  *M*-by-1 vector.
- `Generate window`

  In this mode, the block generates an unoriented window vector
  *w* with length *M* specified by the
  **Window length** parameter. The **In** port
  is disabled for this mode.
- `Generate and apply window`

  In this mode, the block generates an *M*-by-1 window vector
  *w* and applies it to the input. The block produces two
  outputs:

  - At the **Out** port, the block produces the result of the
    multiplication *y*, which has the same dimension as the
    input.
  - At the **Win** port, the block produces the
    *M*-by-1 window vector *w*.

  When the input is an *M*-by-*N* matrix
  *u*, the window is multiplied element-wise with each of the
  *N* channels in the input matrix *u*. This is
  equivalent to the following MATLAB code:

  ```
  y = repmat(w,1,N) .* u								% Equivalent MATLAB code
  ```

  The window is always applied to the first dimension:

  y(i,j,...,k)=w(i)\*u(i,j,...,k)       i=1,...,M,  j=1,...,N,  ...,  k=1,...,P

  A length-*M* 1-D vector input is treated as an
  *M*-by-1 vector.

### **Window type** — Type of window `Hamming` (default) | `Bartlett` | `Blackman` | ...

This table lists the available window types.

| Window Type | Description |
| --- | --- |
| Bartlett | Computes a Bartlett window.  ``` w = bartlett(M) ``` |
| Blackman | Computes a Blackman window.  ``` w = blackman(M) ``` |
| Boxcar | Computes a rectangular window.  ``` w = rectwin(M) ``` |
| Chebyshev | Computes a Chebyshev window with stopband ripple `R`.  ``` w = chebwin(M,R) ``` |
| Hamming | Computes a Hamming window.  ``` w = hamming(M) ``` |
| Hann | Computes a Hann window (also known as a Hanning window).  ``` w = hann(M) ``` |
| Hanning | Obsolete. This window type is included only for compatibility with older models. Use the `Hann` **Window type** instead of `Hanning` whenever possible. |
| Kaiser | Computes a Kaiser window with the Kaiser parameter `beta`.  ``` w = kaiser(M,beta) ``` |
| Taylor | Computes a Taylor window.  ``` w = taylorwin(M) ``` |
| Triang | Computes a triangular window.  ``` w = triang(M) ``` |
| User Defined | Computes the user-defined window function specified by the entry in the **Window function name** parameter, `usrwin`.  ``` w = usrwin(M) % Window takes no extra parameters w = usrwin(M,x1,...,xn) % Window takes extra  parameters {x1 ... xn} ``` |

### **Sampling** — Type of sampling `Symmetric` (default) | `Periodic`

Specify the window sampling for generalized-cosine windows.

For the generalized-cosine windows (`Blackman`,
`Hamming`, `Hann`, and
`Hanning`), the **Sampling** parameter
determines whether the window samples are computed in a periodic or a symmetric
manner. For example, when **Sampling** is set to
`Symmetric`, a Hamming window of length
*M* is computed as:

```
w = hamming(M)					% Symmetric (aperiodic) window
```

When **Sampling** is set to `Periodic`, the same
window is computed as:

```
w = hamming(M+1)					% Periodic (asymmetric) window
w = w(1:M)
```

Tunable (Simulink) in
simulation only.

#### Dependencies

This parameter is visible only when you select
`Blackman`, `Hamming`,
`Hann`, or `Hanning` for the
**Window type** parameter.

### **Sample mode** — Sample mode `Continuous` (default) | `Discrete`

Specify the sample mode for the block, `Continuous` or
`Discrete`, when it is in the `Generate
window` mode. In the `Apply window to input`
and `Generate and apply window` modes, the block inherits the
sample mode from its driving block.

#### Dependencies

This parameter is visible only when you select `Generate
window` for the **Operation** parameter.

### **Sample time** — Sample time `1` (default) | real scalar

Specify the sample time for the block when **Operation** is set
to `Generate window` and **Sample mode** is
set to `Discrete`. When **Operation** is set
to `Apply window to input` and `Generate and
apply window`, the block inherits the sample time from its driving
block.

#### Dependencies

This parameter is visible only when you set **Sample mode** to
`Discrete`.

### **Window length** — Length of window `64` (default) | positive integer

Specify the length of the window to apply.

#### Dependencies

This parameter is visible only when you select `Generate
window` for the **Operation** parameter. Otherwise,
the window vector length is computed to match the length of the first dimension of
the input.

### **Stopband attenuation in dB** — Stopband attenuation in dB `50` (default) | nonnegative scalar

Specify the level of stopband attenuation
*R**s* in
decibels.

Tunable (Simulink) in
simulation only.

#### Dependencies

This parameter is visible only when you select
`Chebyshev` for the **Window type**
parameter.

### **Beta** — Kaiser window *β* parameter `10` (default) | real scalar

Specify the `Kaiser` window *β*
parameter. Increasing *β* widens the mainlobe and decreases the
amplitude of the window sidelobes in the window's frequency magnitude response.

Tunable (Simulink) in
simulation only.

#### Dependencies

This parameter is visible only when you select `Kaiser`
for the **Window type** parameter.

### **Number of sidelobes** — Number of sidelobes 4 (default) | positive integer

Specify the number of sidelobes as a scalar integer value greater than
zero.

#### Dependencies

This parameter is visible only when you select `Taylor`
for the **Window type** parameter.

### **Maximum sidelobe level relative to mainlobe (dB)** — Maximum sidelobe level relative to mainlobe `-30` (default) | scalar less than or equal to zero

Specify in decibels the maximum sidelobe level relative to the mainlobe. This
parameter must be a scalar less than or equal to zero. The default value of –30
produces sidelobes with peaks 30 dB down from the mainlobe peak.

#### Dependencies

This parameter is visible only when you select `Taylor`
for the **Window type** parameter.

### **Window function name** — Window function name `hamming` (default) | character vector

Specify the name of the user-defined window function to be calculated by the
block. The output window vector returned by the custom window function must be of data
type `double`.

#### Dependencies

This parameter is visible only when you select `User
defined` for the **Window type** parameter.

### **Specify additional arguments to the hamming function** — Specify additional arguments to the window function off (default) | on

Select to enable the **Cell array of additional arguments**
parameter, when the user-defined window requires parameters other than the window
length.

#### Dependencies

This parameter is visible only when you select `User
defined` for the **Window type** parameter.

### **Cell array of additional arguments** — Additional arguments `{'symmetric'}` (default) | cell array

Specify the extra parameters required by the user-defined window function, besides
the window length.

#### Dependencies

This parameter is only available when you select the **Specify
additional arguments to the hamming function** parameter. The entry must
be a cell array.

### Data Types

When the **Operation** parameter on the **Main** tab
is set to `Generate window`, the following parameters
appear.

### **Window data type** — Window data type `double` (default) | `single` | `Fixed-point` | `User-defined` | `Inherit via back propagation`

Specify the window data type in one of the following ways:

- `double`
- `single`
- `Fixed-point` –– To specify the window data type
  and scaling in the **Signed**, **Word
  length**, **Set fraction length in output to**, and
  **Fraction length** parameters.
- `User-defined` –– To specify the window data type
  and scaling in the **User-defined data type**, **Set
  fraction length in output to**, and **Fraction
  length** parameters.
- `Inherit via back propagation` –– To set the window
  data type and scaling to match the following block.

### **Signed** — Window output is signed on (default) | off

Select to output a signed fixed-point signal. Otherwise, the signal is
unsigned.

#### Dependencies

This parameter appears only when you set **Window data type**
to `Fixed-point`.

### **Word length** — Word length `16` (default) | positive integer in the range [2 128]

Specify the word length of the fixed-point window data type in bits.

#### Dependencies

This parameter is visible only when you set **Window data
type** to `Fixed-point`.

### **User-defined data type (e.g. sfix(16), float('single))** — user-defined data type `sfix(16)` (default) | built-in data type | fixed-point data type

Specify any built-in or fixed-point data type. You can specify fixed-point data
types using the `fixdt` (Simulink) function.

#### Dependencies

This parameter is only visible when you set **Window data
type** to `User-defined`.

### **Set fraction length in output to** — Scaling of fixed-point window data type `Best precision` (default) | `User-defined`

Specify the scaling of the fixed-point window data type by using either of these methods:

- Choose `Best precision` to have the window data
  type scaling automatically set such that the output signal has the best possible
  precision.
- Choose `User-defined` to specify the window data
  type scaling in the **Fraction length** parameter.

#### Dependencies

This parameter is visible only when you set **Window data
type** to `Fixed-point` or
`User-defined`, and when the specified window data type
is a fixed-point data type.

### **Fraction length** — User-defined fraction length `15` (default) | integer

Specify the fraction length of the fixed-point window data type in bits.

#### Dependencies

This parameter is visible only when you set **Window data
type** to `Fixed-point` or
`User-defined`, and when you set **Set fraction
length in output to** to `User-defined`.

When the **Operation** parameter on the **Main** tab
is set to either `Apply window to input` or `Generate
and apply window`, the following parameters appear.

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding mode for
fixed-point operations.

The window vector *w* does not obey this parameter. It always
rounds to `Nearest`.

**Note**

The **Rounding mode** and **Overflow mode**
settings have no effect on numerical results when both of these conditions exist:

- **Product output** is `Inherit via internal
  rule`
- **Output** is `Same as product
  output`

With these data type settings, the block is effectively operating in
a full-precision mode.

### **Overflow mode** — Overflow mode `Wrap` (default) | `Saturate`

Select the overflow mode for
fixed-point operations.

The window vector *w* does not obey this parameter. It is always
saturated.

### **Window** — Window data type `Same word length as input` (default) | `Specify word length` | `Binary point scaling` | `Slope and bias scaling`

Choose how you specify the word length and fraction length of the window vector
*w*.

When you select:

- `Same word length as input` –– The word length of
  the window vector elements is the same as the word length of the input. The
  fraction length is automatically set to the best precision possible.
- `Specify word length` –– You can enter the word
  length of the window vector elements in bits. The fraction length is
  automatically set to the best precision possible.
- `Binary point scaling` –– You can enter the word
  length and the fraction length of the window vector elements in bits.
- `Slope and bias scaling` –– You can enter the word
  length, in bits, and the slope of the window vector elements. This block
  requires power-of-two slope and a bias of zero.

The window vector does not obey the **Rounding mode** and
**Overflow mode** parameters. It is always saturated and rounded to
`Nearest`.

### **Product output** — Product output data type `Inherit via internal rule` (default) | `Same as input` | `Binary point scaling` | `Slope and bias scaling`

Use this parameter to specify how you want to designate the product output word
and fraction lengths.

When you select:

- `Inherit via internal rule` –– The product output
  word length and fraction length are calculated automatically. For information on
  how the product output word and fraction lengths are calculated when an internal
  rule is used, see Inherit via Internal Rule.
- `Same as input` –– These characteristics match
  those of the input to the block.
- `Binary point scaling` –– You can enter the word
  length and the fraction length of the product output in bits.
- `Slope and bias scaling` –– You can enter the word
  length in bits and the slope of the product output. This block requires
  power-of-two slope and a bias of zero.

### **Output** — Output data type `Same as product output` (default) | `Same as input` | `Binary point scaling` | `Slope and bias scaling`

Choose how you specify the word length and fraction length of the output of the
block.

When you select:

- `Same as product output` –– These characteristics
  match those of the product output.
- `Same as input` –– These characteristics match
  those of the input to the block.
- `Binary point scaling` –– You can enter the word
  length and the fraction length of the output in bits.
- `Slope and bias scaling` –– You can enter the word
  length in bits and the slope of the output. This block requires power-of-two
  slope and a bias of zero.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Compute and apply window to input signal

The Window Function block has three modes of operation that enable you to apply a window,
or compute a window, or compute and apply a window to an input signal. You can select the mode
via the **Operation** parameter. In each mode, the block first creates a
window vector *w* by sampling the window specified in the **Window
type** parameter.
