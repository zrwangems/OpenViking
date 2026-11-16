---
type: simulink-block
title: 'Fourth-Order Section Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'fourthordersectionfilter'
documentation_source_path: 'ref/fourthordersectionfilter.html'
language: en
---

# Fourth-Order Section Filter

## Ports

### Input

### **x** — Input signal vector | matrix

Input signal, specified as a vector or a matrix. The input can be a variable size
signal. That is, the frame size of the signal can change during simulation but the
number of channels cannot.

This port is unnamed until you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Num** — Numerator coefficients *P*-by-5 matrix

Specify the numerator coefficients of the fourth-order section filter as a
*P*-by-5 matrix, where *P* is the number of filter
sections. For more details on this input port, see **Numerator coefficients of
filter**.

While the simulation is running, you can change the number of sections (rows) in
the numerator coefficients. You can also change the coefficient values.

#### Dependencies

This port appears only when you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Den** — Denominator coefficients *P*-by-5 matrix | *P*-by-4 matrix

Specify the denominator coefficients of the fourth-order section filter as a
*P*-by-5 matrix or a *P*-by-4 matrix, where
*P* is the number of filter sections. For more details on this
input port, see **Denominator coefficients of filter**.

While the simulation is running, you can change the number of sections (rows) in
the denominator coefficients. You can also change the coefficient values.

#### Dependencies

This port appears only when you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **y** — Filtered output vector | matrix

Filtered output, returned as a vector or a matrix. The output has the same size
and data type as the input. The output signal is complex if either the input signal,
numerator coefficients, or the denominator coefficients are complex.

This port is unnamed until you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Coefficient source** — Filter coefficient source `Dialog parameters` (default) | `Input ports` | `Filter object`

Specify the filter coefficient source as one of the following:

- `Dialog parameters` –– Specify the filter
  coefficients through the **Numerator coefficients of filter** and
  the **Denominator coefficients of filter** parameters in the
  block dialog box.
- `Input ports` –– Specify the filter coefficients
  through the **Num** and **Den** input
  ports.
- `Filter object` –– Specify the filter coefficients
  using a `dsp.FourthOrderSectionFilter` object.

To view the filter response, set this parameter to `Dialog
parameters` or `Filter object`, and then click
the **View Filter Response** button.

### **Numerator coefficients of filter** — Numerator coefficients [`0.07795634 0 -0.15591268 0 0.07795634`; `0.06188520 0 -0.12377039 0 0.06188520`] (default) | *P*-by-5 matrix

Specify the numerator coefficients **b** of the fourth-order
section filter as a *P*-by-5 matrix, where *P* is the
number of filter sections.

b=[b01b11b21b31b41b02b12b22b32b42⋮⋮⋮⋱⋮b0Pb1Pb2Pb3Pb4P]

In the transfer function form, the fourth-order section filter can be represented
using the following equation:

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

where,

- **a** –– Denominator coefficients matrix. For more details on
  how to specify this matrix, see **Denominator coefficients of
  filter**.
- *k* –– Row index.

You cannot change the size of this parameter during simulation, but you can change
its value.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Dialog parameters`.

**Tunable:** Yes

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Denominator coefficients of filter** — Denominator coefficients [`1 0 1.32091343 0 0.63273879`; `1 0 1.04859957 0 0.29614035`] (default) | *P*-by-5 matrix | *P*-by-4 matrix

Specify the denominator coefficients **a** of the fourth-order
section filter as a *P*-by-5 matrix or a *P*-by-4
matrix, where *P* is the number of filter sections.

a=[a01a11a21a31a41a02a12a22a32a42⋮⋮⋮⋱⋮a0Pa1Pa2Pa3Pa4P]

The block algorithm assumes that the value of the leading coefficients is always 1.
If the denominator is of size *P*-by-4, the block algorithm places 1s
in the first column to make the denominator size *P*-by-5. If the
denominator is of size *P*-by-5 and the elements in the first column do
not equal 1, the algorithm ignores the values in the first column and appends them with
1s.

In the transfer function form, the fourth-order section filter can be represented
using the following equation:

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

where,

- **b** –– Numerator coefficients matrix. For more details on
  how to specify this matrix, see **Numerator coefficients of
  filter**.
- *k* –– Row index.

You cannot change the size of this parameter during simulation, but you can change
its value.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Dialog parameters`.

**Tunable:** Yes

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Filter** — Filter object `dsp.FourthOrderSectionFilter` object

Specify the filter coefficients using a `dsp.FourthOrderSectionFilter` object. You can enter this object directly in
the **Filter** parameter. Alternatively, you can create this object in
the MATLAB® workspace or model workspace and specify the filter variable in the
**Filter** parameter. When you specify the filter as a variable and
you simulate the model, you cannot change the complexity, data type, and size of the
filter coefficients in the workspace between simulations.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Filter object`.

### **View Filter Response** — Visualize frequency response `gui button`

Clicking this button opens the filter visualizer and displays the magnitude response
of the fourth-order section filter. The response is based on the coefficients that you
specify in the block dialog box. If you set **Coefficient source** to
`Input ports` and click **Apply**, you
cannot view the magnitude response using this button.

To update the filter response while the visualizer is running, modify the
coefficients in the block dialog box and click **Apply**.

You can configure the plot settings and the frequency response measurements from the
interface of the visualizer.

On the **Scope** tab, you can enable the legend, specify to plot
both magnitude and phase responses of the filter, modify the plot settings, generate a
script to re-create the plot, and even save or share the settings. On the
**Measurements** tab, you can enable data cursors, and display the
peak values of the filter response.

For more details on the filter visualizer interface and its tools, see Configure Filter Visualizer.

#### Dependencies

To enable this button, you must specify the filter coefficients directly in the
block dialog box or through the `dsp.FourthOrderSectionFilter`
object.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Filtering / Filter Implementations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2022b: Enhancements to Fourth-Order Section Filter block

Starting in R2022b, when you pass numerator and denominator coefficients through the
input ports of the Fourth-Order Section
Filter block, you can change the number of sections (rows) in the filter
coefficients while the simulation is running.

You can also specify the coefficients in the block dialog box using a `dsp.FourthOrderSectionFilter` object. Set **Coefficient source**
to `Filter object` and specify a
`dsp.FourthOrderSectionFilter` object directly in the
**Filter** parameter. Alternatively, you can create this object in the
MATLAB workspace or model workspace and specify the filter variable in the
**Filter** parameter.

## Description

Implement cascade of fourth-order section filters

The Fourth-Order Section Filter block implements a cascade of fourth-order
section filters in Simulink®. You can specify the numerator and denominator coefficients of the filter in the
block parameters dialog box or through input ports.
