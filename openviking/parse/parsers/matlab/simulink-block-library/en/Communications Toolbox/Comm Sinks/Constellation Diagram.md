---
type: simulink-block
title: 'Constellation Diagram'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'constellationdiagram'
documentation_source_path: '../comm/ref/constellationdiagram.html'
language: en
---

# Constellation Diagram

## Ports

### Input

### **In\_1, ..., In\_N** — Signals (as separate ports) column vectors | matrices

Signals, specified as separate arguments of
*N*sym-by-1 column vectors
or
*N*sym-by-*N*channel
matrices. *N*sym is the number
of symbols, and *N*channel is
the number of input signal channels. Signals can have different data
types and dimensions.

You must specify *N* input ports, where
*N* is the **Number
of input ports** parameter value. You can visualize up to
20 individual or collective signal channels in the constellation
diagram. For example, if you create a two-channel signal for every
input, then you can define up to 10 input ports.

**Example:** `[-1 + 1i; -1 - 1i; 1 + 1i; 1 - 1i]`
specifies a four-symbol input signal.

**Data Types:** `double`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Plot

In the **Plot** tab, you can adjust settings of the constellation
diagram configuration, simulate the model, take a snapshot of the plot, copy the
display, and print the figure. Parameters unique to the constellation diagram scope
are described.

### **Settings** — Constellation diagram settings button

On the **Plot** tab, click
**Settings** to open the Configuration Plot
Settings window. This window includes parameter subsections to configure
the data and axes, labels, and color and styling. Parameters unique to
the constellation diagram are described on this page.

### **Number of input ports** — Number of input ports on scope block `1` (default) | integer in the range [1, 20]

Specify the number of input ports on the scope block as an
integer in the range [1, 20].

The total number of input signal channels cannot exceed
20. When you specify multichannel input signals, the total
number of input signal channels limits the maximum number of
input ports.

### **Samples per symbol** — Number of samples used to represent each symbol `1` (default) | positive integer

Specify the number of samples used to represent each
symbol as a positive integer. The signal is downsampled by
the value of this parameter before it is plotted.

### **Offset** — Number of samples to skip before plotting points `0` (default) | nonnegative integer

Specify the number of samples to skip before plotting
points as a nonnegative integer less than the **Samples per symbol** parameter value. This
value specifies the number of samples to skip when
**Samples per symbol** is greater than
1.

### **Symbols to display** — Maximum number of symbols to display `Input frame length` (default) | positive integer

Specify the maximum number of symbols to display by
selecting `Input frame length` or
specifying a positive integer. To specify a positive
integer, select and then replace
`<user-defined>` with your
desired value. Use this parameter to limit the maximum
number of symbols that the constellation diagram displays
when you input long signals. The block plots the most
recently received symbols.

### **AxesLimits** — *x* and *y*-axis limits `[-1.375 1.375]` (default) | two-element row vector

Specify the *x* and *y*-axis limits
as a two-element row vector. The first element is the minimum axis
value, and the second element is the maximum axis value.

- If the scope window is square, then both X and Y axis will
  have the same limits as
  `AxesLimits`.
- If the scope window is rectangular, then the smaller axis
  will have the same limits as `AxesLimits`.
  The larger axes auto fills to maintain a 1:1 aspect
  ratio.

**Tunable:** Yes

**Data Types:** `double`

### **Reference Constellation** — Reference constellation configuration button

On the **Plot** tab or
**Measurements** tab, click **Reference
Constellation**, to open the Reference Constellation
window. This window includes parameters to configure the reference
constellation for each input port.

### **Show reference constellations** — Option to display reference constellations `on` (default) | `off`

Select this parameter to show reference constellations on
the plot.

### **Input** — Select input port 1 (default) | positive integer

Configure the reference constellation parameters for the
specified input port.

Each input port has its own reference constellation. For a
multichannel input signal, the block applies a single
reference constellation for all signals in that input
port.

### **Reference constellation** — Reference constellation `Custom` (default) | `BPSK` | `8-PSK` | `16-QAM` | `64-QAM` | `256-QAM`

Specify the reference constellation by selecting
`Custom`,
`BPSK`,
`QPSK`,
`8-PSK`,
`16-QAM`,
`64-QAM`, or
`256-QAM`. To specify a custom
value, first select `Custom`. Then
in the **Custom value** parameter, replace
the entry with your custom vector of symbol values.

Each input port had its own reference constellation. For a
multichannel input signal, the block applies a single
reference constellation for all signals in that input
port.

The EVM/MER measurements use the specified reference
constellation to calculate the signal quality of the
modulated input signal. For more information about the
signal quality measurements, see EVM and MER Measurements.

### **Custom value** — Input reference constellation `[0.7071+0.7071i -0.7071+0.7071i -0.7071-0.7071i 0.7070-0.7071i]` (default) | vector

Specify the reference constellation for an input as a
vector that defines symbol values for the custom modulation
scheme.

#### Dependencies

To enable this parameter, set the **Reference
constellation** parameter to
`Custom Reference
Constellation`.

### **Constellation normalization** — Normalization method `Average power` (default) | `Minimum distance` | `Peak power`

Specify the normalization method that the block uses for
the constellation diagram by selecting `Average
power`, `Minimum
distance`, or `Peak
power`.

#### Dependencies

To enable this parameter, set the **Reference
constellation** parameter to
`16-QAM`,
`64-QAM`, or
`256-QAM`.

### **Average reference power** — Average power of reference constellation `1` (default) | positive scalar

Specify the average power of the reference constellation
as a positive scalar. The average power is referenced to a
one-ohm load. Units are in watts.

#### Dependencies

To enable this parameter, set the **Reference
constellation** parameter to
`BPSK`,
`QPSK`,
`8-PSK`,
`16-QAM`,
`64-QAM`, or
`256-QAM`.

### **Reference phase offset (rad)** — Phase offset of reference constellation scalar

Specify the phase offset of the reference constellation as
a scalar. Units are in radians.

#### Dependencies

To enable this parameter, set the **Reference
constellation** parameter to
`BPSK`,
`QPSK`,
`8-PSK`,
`16-QAM`,
`64-QAM`, or
`256-QAM`.

- The default value is `0`
  for `BPSK`,
  `16-QAM`,
  `64-QAM`, and
  `256-QAM`.
- The default value is `pi/4`
  for `8-PSK`.
- The default value is `pi/8`
  for `QPSK`.

### **Legend** — Option to display legend button

On the **Plot** tab, click
**Legend** to toggle the display of the legend. The
names listed in the legend are the names for signals connected to input
ports as specified in the model. The legend does not display until the
model runs with an input signal.

In the scope legend, click a signal name to toggle the signal
visibility in the scope.

### **Trajectory** — Option to display signal trajectory button

On the **Plot** tab, click
**Trajectory** to toggle the display of the
trajectory. Select this parameter to display the trajectory between
constellation points for the plotted signals.

### Measurements

In the **Measurements** tab, you can select the active channel,
configure the signal quality measurements, and toggle the
**Measurements** pane.

For more information about the signal quality measurements, see EVM and MER Measurements.

#### Channel

### **Channel** — Active input channel name of first channel in first port (default) | list of channels

Select the active input channel for measurements from the list of
input channels. Click **EVM/MER** to display the
signal quality measurements for the active channel.

The total number of input signal channels cannot exceed 20. When you
specify multichannel input signals, the total number of input signal
channels limits the maximum permitted value for the **Number of
input ports** parameter.

#### Measurements

### **Measurement Interval** — Duration of EVM and MER measurement `Current display` (default) | `All displays` | positive integer

Specify the duration of the EVM and MER measurement in symbols by
selecting `Current Display`, or
`All displays` or by specifying a positive
integer. To specify a positive integer, select and then replace
`<user-defined>` with your desired
value. The value must be a positive value in the range [1,
**Symbols to display**). The block computes
measurements after the number of input data samples exceeds the
measurement interval.

### **EVM Normalization** — Normalization method `Average constellation power` (default) | `Peak constellation power`

Specify the normalization method that the block uses for the EVM
normalization by selecting `Average constellation
power` or `Peak constellation
power`.

### **Reference Constellation** — Reference constellation configuration button

On the **Plot** tab or
**Measurements** tab, click **Reference
Constellation**, to open the Reference Constellation
window. This window includes parameters to configure the reference
constellation for each input port. For parameter descriptions, see the
**Reference Constellation** parameter in the Plot
section.

### **EVM/MER** — Option to display signal quality measurements pane button

On the **Measurements** tab, click
**EVM/MER** to toggle display the signal quality
measurements pane. For more information, see EVM and MER Measurements.

## Libraries

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block is excluded from the generated code when code generation is performed on a system containing this block.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced in R2013b**

### R2025a: Single axes limit replaces separate x and y axis limits in constellation diagram block

The Constellation Diagram block now include
a unified axes limit, replacing the separate x and y axis limits. This change
ensures that the system applies the specified limits to at least one axis,
simplifying canvas size management. The scope automatically adjusts limits to
maintain a 1:1 aspect ratio when you resize or zoom the window.

## Description

Display and analyze input signals in IQ-plane

The Constellation Diagram block displays real- and complex-valued floating- and fixed-point
signals in the IQ plane. Use this block to perform qualitative and quantitative analysis
on modulated single-carrier signals. Specifically, the IQ-plane displays the in-phase
and quadrature components of modulated signals on the real and imaginary axis of an
xy-plot.

Constellation diagram displaying QPSK,16-QAM, and 8-DPSK signals, and signal quality measurements.

In the Constellation Diagram window, you can:

- Input and plot multiple signals on a single constellation diagram. To
  define a reference constellation for each input signal, use the **Reference
  Constellation** parameter.
- Select signals in the legend to toggle visibility of individual channels.
  To display the legend, use the **Legend** parameter on
  the **Plot** tab. For a multichannel signal, specify the
  input as a matrix with individual signals defined in the columns of the
  matrix.
- Display calculated error vector magnitude (EVM) and modulation error ratio
  (MER) measurements for individual signals. To view and configure the
  measurements, select **EVM/MER** on the
  **Measurements** tab. When multiple signals are input,
  you can select which signal to use for measurements in the
  **Channel** section.
