---
type: simulink-block
title: 'Frequency-Domain FIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'frequencydomainfirfilter'
documentation_source_path: 'ref/frequencydomainfirfilter.html'
language: en
---

# Frequency-Domain FIR Filter

## Ports
```yaml
ports:
- name: x
  summary: Data Input vector | matrix
  direction: input
  data_types: single | double
- name: Num
  summary: Time-domain FIR filter coefficients row vector | matrix *(since R2024a)*
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: NumFFT
  summary: Frequency-domain FIR filter coefficients row vector | matrix | 3-D array *(since R2024a)*
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: output
  summary: Filtered output vector | matrix | 3D array *(since R2024a)*
  direction: input
  data_types: single | double
- name: latency
  summary: Filter latency positive integer
  direction: input
  data_types: uint32
```

### Input

### **x** — Data Input vector | matrix

Data input, specified as a vector or a matrix of size
*L*-by-*T*. This block supports
variable-size input signals, that is, you can change the input frame
size (number of rows) even after calling the algorithm. However, the
number of channels (number of columns) must remain constant.

This port is unnamed until you select the **Specify
coefficients from input port** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Num** — Time-domain FIR filter coefficients row vector | matrix *(since R2024a)*

Specify the time-domain FIR filter coefficients as a row vector
(single filter) or a matrix (multiple
filters) *(since R2024a)* of size
*F*-by-*NumLen*, where
*F* is the number of filters and
*NumLen* is the filter length. If
*F* is greater than 1, then its value must be a
multiple of the product of the number of input channels (columns)
*T* and the number of paths *P*
you specify through the **Number of propagation paths**
parameter. The multiplication factor determines the number of output
channels *R* and equals
*F*/(*T* ×
*P*).

The coefficient values can change during simulation but the size of
the numerator must remain constant.

#### Dependencies

To enable this port, set **Numerator domain** to
`Time` and select the **Specify
coefficients from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes

### **NumFFT** — Frequency-domain FIR filter coefficients row vector | matrix | 3-D array *(since R2024a)*

Specify the frequency-domain FIR filter coefficients as a row vector,
matrix, or a 3-D array *(since R2024a)*.

When you clear the **Partition numerator to reduce
latency** parameter, the coefficients input at this port
can be a row vector or a matrix of size
*F*-by-*FFTLength*. The FFT length
is equal to the length of the vector input. If *F* is greater than 1 (multiple
filters) *(since R2024a)*, then its value must be a multiple of the product
of the number of input channels (columns) *T* and the
number of paths *P* you specify through the
**Number of propagation paths** parameter. The
multiplication factor determines the number of output channels
*R* and equals
*F*/(*T* ×
*P*).

When you select the **Partition numerator to reduce
latency** parameter, **Frequency
response** must be a matrix of size
2*PL*-by-*N* to represent a single
filter or a 3-D array *(since R2024a)* of size
2*PL*-by-*N*-by-*F*
to represent multiple filters, where *PL* is the
partition size, *N* is the number of partitions, and
*F* is the number of filters.

#### Dependencies

To enable this port, set **Numerator domain** to
`Frequency` and select the **Specify
frequency response from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes
### Output Arguments

### **output** — Filtered output vector | matrix | 3D array *(since R2024a)*

Filtered output, returned as a vector, matrix or a 3D array *(since R2024a)*.

When the number of filters
*F* is greater than 1 and you select the
**Sum filtered output contributions from all input
channels** parameter, the block adds the filtered output
from each input channel to generate an
*L*-by-*R* output matrix, where
*L* is the input frame size (number of input rows)
and *R* is the number of output channels.
*R* equals
*F*/(*T* x *P*),
where *F* is the number of filters,
*T* is the number of input channels, and
*P* is the value that you specify in the
**Number of propagation paths** parameter. *(since R2024a)*

When you clear the **Sum
filtered output contributions from all input channels**
parameter, the block does not sum filtered output contributions from all
input channels. The output is an
*L*-by-*R*-by-*T*
array. `output(:,j,k)` refers to the output from the
*k*th input channel for
the *j*th output channel.
For example, `output(:,3,2)` indicates output on the
third output channel from the second input channel. *(since R2024a)*

For more information on how the object computes the output, see Algorithms.

The output has the same data type and complexity as the input
signal.

This port is unnamed until you select the **Output filter
latency** parameter and click
**Apply**.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **latency** — Filter latency positive integer

Filter latency, returned as a scalar. This latency is inherent to
overlap-add and overlap-save methods and does not include the group
delay of the filter. This port appears only when you select the
**Output filter latency** check box.

This port is unnamed until you select the **Output filter
latency** check box and click
**Apply**.

**Data Types:** `uint32`
## Parameters
```yaml
parameters:
- name: Frequency-domain filter method
  summary: Filtering method in frequency domain Overlap-save (default) | Overlap-add
  group: ''
- name: Numerator domain
  summary: Numerator domain Time (default) | Frequency
  group: ''
- name: Specify coefficients from input port
  summary: Flag to specify time-domain FIR filter coefficients off (default) | on
  group: ''
- name: Filter coefficients
  summary: Time-domain FIR filter coefficients fir1(100,0.3) (default) | row vector | matrix *(since R2024a)*
  group: ''
- name: Specify frequency response from input port
  summary: Flag to specify frequency-domain filter coefficients off (default) | on
  group: ''
- name: Frequency response
  summary: Frequency response of filter fft(fir1(100,0.3),202) (default) | row vector | matrix | 3-D array *(since R2024a)*
  group: ''
- name: Number of propagation paths
  summary: Number of propagation paths between each input channel and output channel pair 1 (default) | positive integer
  group: ''
- name: Sum filtered output contributions from all input channels
  summary: Option to sum filtered output contributions from all input channels true (default) | false
  group: ''
- name: Partition numerator to reduce latency
  summary: Option to partition the numerator to reduce latency off (default) | on
  group: ''
- name: Numerator partition length
  summary: Partition length of numerator 32 (default) | positive integer
  group: ''
- name: Time-domain numerator length
  summary: Time-domain numerator length 101 (default) | positive integer
  group: ''
- name: Inherit FFT length from numerator length
  summary: Flag to inherit FFT length from the numerator length on (default) | off
  group: ''
- name: FFT length
  summary: FFT length 1024 (default) | positive integer
  group: ''
- name: Filter is real
  summary: Flag to specify if filter is real true (default) | false
  group: ''
- name: Output filter latency
  summary: Flag to output filter latency 'off' (default) | 'on'
  group: ''
- name: View Filter Response
  summary: Visualize frequency response button
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Frequency-domain filter method** — Filtering method in frequency domain `Overlap-save` (default) | `Overlap-add`

Specify the filtering method in the frequency domain as
`Overlap-save` or
`Overlap-add`. For more details on these two
methods, see Algorithms.

### **Numerator domain** — Numerator domain `Time` (default) | `Frequency`

Specify the domain of the filter coefficients as one of the following:

- `Time` –– Specify the time-domain
  filter coefficients in the **Filter
  coefficients** parameter or through the
  **Num** input port.
- `Frequency` –– Specify the filter's
  frequency response in the **Frequency
  response** parameter or through the
  **NumFFT** input port.

### **Specify coefficients from input port** — Flag to specify time-domain FIR filter coefficients `off` (default) | `on`

When you select this check box, the time-domain FIR filter coefficients
are input through the port, **Num**. When you clear this
check box, the coefficients are specified in the block dialog box through
the **Filter coefficients** parameter.

To view the filter response, clear this check box, specify the
coefficients in the block dialog box, and click on the **View
Filter Response** button.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Time`.

### **Filter coefficients** — Time-domain FIR filter coefficients `fir1(100,0.3)` (default) | row vector | matrix *(since R2024a)*

Specify the time-domain FIR filter coefficients as a row vector (single
filter) or a matrix (multiple filters) *(since R2024a)*
of size *F*-by-*NumLen*, where
*F* is the number of filters and
*NumLen* is the filter length. If *F*
is greater than 1, then its value must be a multiple of the product of the
number of input channels (columns) *T* and the number of
paths *P* you specify through the **Number of
propagation paths** parameter. The multiplication factor
determines the number of output channels *R* and equals
*F*/(*T* ×
*P*).

The coefficient values can change during simulation but the size of the
numerator must remain constant.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Time` and clear the **Specify
coefficients from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

### **Specify frequency response from input port** — Flag to specify frequency-domain filter coefficients off (default) | on

When you select this check box, the FIR filter coefficients in the
frequency domain are input through the port, **NumFFT**.
When you clear this check box, the coefficients are specified in the block
dialog box through the **Frequency response**
parameter.

To view the filter response, clear this check box, specify the frequency
response in the block dialog box, and click on the **View Filter
Response** button.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Frequency`.

### **Frequency response** — Frequency response of filter `fft(fir1(100,0.3),202)` (default) | row vector | matrix | 3-D array *(since R2024a)*

Specify the frequency response of the filter as a row vector, matrix, or a
3-D array *(since R2024a)*.

When you clear the **Partition numerator to reduce
latency** parameter, **Frequency response**
can be a row vector or a matrix of size
*F*-by-*FFTLength*. The FFT length is
equal to the length of the **Frequency
response** vector. If
*F* is greater than 1 (multiple filters) *(since R2024a)*,
then its value must be a multiple of the product of the number of input
channels (columns) *T* and the number of paths
*P* you specify through the **Number of
propagation paths** parameter. The multiplication factor
determines the number of output channels *R* and equals
*F*/(*T* ×
*P*).

When you select the **Partition numerator to reduce
latency** parameter, **Frequency response**
must be a matrix of size 2*PL*-by-*N* to
represent a single filter or a 3-D
array *(since R2024a)* of size
2*PL*-by-*N*-by-*F*
to represent multiple filters, where *PL* is the partition
size, *N* is the number of partitions, and
*F* is the number of filters.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Frequency` and clear the **Specify
frequency response from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes

### **Number of propagation paths** — Number of propagation paths between each input channel and output channel pair `1` (default) | positive integer

*Since R2024a*

Specify the number of propagation paths *P* between each
input channel and output channel pair as a positive integer. Each path is
represented by a unique filter. When you specify the number of paths to be
greater than `1`, the filter models multipath propagation.
The algorithm sums up the filtered output contributions from all paths
between each input channel and output channel pair.

For an example, see Filter Input Signal Using 1-by-2 SIMO System.

#### Dependencies

To enable this parameter, the number of filters *F*
must be greater than 1.

**Data Types:** `single` | `double`

### **Sum filtered output contributions from all input channels** — Option to sum filtered output contributions from all input channels `true` (default) | `false`

*Since R2024a*

Select this check box to sum filtered output contributions from all input
channels. When you select this check box, the block adds the filtered output
from each input channel to generate an
*L*-by-*R* output matrix, where
*L* is the input frame size (number of input rows) and
*R* is the number of output channels.
*R* equals *F*/(*T* x
*P*), where *F* is the number of
filters, *T* is the number of input channels, and
*P* is the value that you specify through the
**Number of propagation paths** parameter.

When you clear this parameter, the block does not sum filtered output
contributions from all input channels. The output is an
*L*-by-*R*-by-*T*
array.

For more information on how the block computes the output based on the
value of this parameter, see Modeling MIMO System with Multiple Propagation Paths.

#### Dependencies

To enable this property, the number of filters *F*
must be greater than 1.

### **Partition numerator to reduce latency** — Option to partition the numerator to reduce latency `off` (default) | `on`

Select this parameter to partition the numerator to reduce latency. When
you select this parameter, the block partitions the numerator into segments
of length specified by the **Numerator partition length**
parameter. The filter performs overlap-save or overlap-add on each
partition, and combines the partial results to form the overall output. This
option reduces latency to the partition length.

When you clear this parameter, the filter uses the traditional
overlap-save or overlap-add method. The latency in this case is FFT length –
*NumLen* + 1, where *NumLen* is the
filter length. See the **Filter coefficients** parameter
for more information on the filter length.

### **Numerator partition length** — Partition length of numerator `32` (default) | positive integer

Specify the partition length of the numerator *PL* as a
positive integer less than or equal to the length of the numerator.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Time` and select the **Partition
numerator to reduce latency** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Time-domain numerator length** — Time-domain numerator length `101` (default) | positive integer

Specify the time-domain numerator length as a positive integer.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Frequency` and clear the
**Partition numerator to reduce latency** check
box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Inherit FFT length from numerator length** — Flag to inherit FFT length from the numerator length on (default) | off

When you select this check box, the FFT length equals twice the numerator
length. When you clear this check box, you specify the FFT length through
the **FFT length** parameter.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Time` and clear the **Partition
numerator to reduce latency** parameter.

### **FFT length** — FFT length `1024` (default) | positive integer

The FFT length you specify must be greater than or equal to the length of
the numerator you specify in the **Filter coefficients**
parameter.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Time`, clear the **Partition
numerator to reduce latency** and the **Inherit FFT
length from numerator length** parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter is real** — Flag to specify if filter is real `true` (default) | `false`

Select this parameter to specify that the filter coefficients are all
real.

#### Dependencies

To enable this parameter, set **Numerator domain** to
`Frequency`.

### **Output filter latency** — Flag to output filter latency `'off'` (default) | `'on'`

When you select this check box and click **Apply**, the
block outputs the filter latency through the **latency**
port.

### **View Filter Response** — Visualize frequency response `button`

Clicking this button opens the filter visualizer and displays the
magnitude response of the frequency domain FIR filter. The response is based
on the parameters you select in the block dialog box. To update the response
while the visualizer is running, modify the parameters in the dialog box and
click **Apply**.

You can configure the plot settings and the frequency response
measurements from the interface of the visualizer.

On the **Scope** tab, you can enable the legend, specify
to plot both magnitude and phase responses of the filter, modify the plot
settings, generate a script to re-create the plot, and even save or share
the settings. On the **Measurements** tab, you can enable
data cursors, and display the peak values of the filter response.

For more details on the filter visualizer interface and its tools, see
Configure Filter Visualizer.

#### Dependencies

To enable this button, clear the **Specify coefficients from
input port** and the **Specify frequency response
from input port** parameters.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Filtering / Filter Implementations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2024a: Support for multiple filters

You can model MIMO systems by specifying multiple filters in the time and
frequency domains. You can also specify multiple paths between each input and output
pair.

## Description

Filter input signal in the frequency domain

The Frequency-Domain FIR Filter block implements frequency-domain, fast
Fourier transform (FFT)-based filtering to filter a streaming input signal. In the time
domain, the filtering operation involves a convolution between the input and the impulse
response of the finite impulse response (FIR) filter. In the frequency domain, the
filtering operation involves the multiplication of the Fourier transform of the input
and the Fourier transform of the impulse response. The frequency-domain filtering
becomes more efficient than time-domain filtering as the impulse response grows longer.
You can specify the filter coefficients directly in the frequency domain by setting
**Numerator domain** to
`Frequency`.

This block uses the overlap-save and overlap-add methods to perform the
frequency-domain filtering. For filters with a long impulse response length, the latency
inherent to these two methods can be significant. To mitigate this latency, the
Frequency-Domain FIR Filter block partitions the impulse response
into shorter blocks and implements the overlap-save and overlap-add methods on these
shorter blocks. To partition the impulse response, select the **Partition
numerator to reduce latency** check box. For more details on these two
methods and on reducing latency through impulse response partitioning, see Algorithms.

The Frequency-Domain FIR Filter
block can model single-input multiple-output (SIMO) and multiple-input multiple-output
(MIMO) systems by supporting multiple filters in the time domain and the frequency
domain. For examples that show how to model such systems, see Filter Input Signal Using 1-by-2 SIMO System and Filter Input Signal Using 3-by-2 MIMO System. You can also specify
multiple paths between each input channel and output channel pair using the
**Number of propagation paths** parameter. For more information on
modeling MIMO systems, see Modeling MIMO System with Multiple Propagation Paths. *(since R2024a)*
