---
type: simulink-block
title: 'Eye Diagram'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'eyediagramscope'
documentation_source_path: '../comm/ref/eyediagramscope.html'
language: en
---

# Eye Diagram

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | column vector
  direction: input
  data_types: double
```

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or column vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Samples per symbol
  summary: Samples per symbol 8 (default) | positive integer
  group: Display and Traces
- name: Sample offset
  summary: Sample offset 0 (default) | nonnegative integer
  group: Display and Traces
- name: Symbols per trace
  summary: Symbols per trace 2 (default) | positive integer
  group: Display and Traces
- name: Traces to display
  summary: Number of traces to display 40 (default) | positive integer
  group: Display and Traces
- name: Color fading
  summary: Color fading off (default) | on
  group: Display and Traces
- name: Plot Imaginary Axes
  summary: Plot imaginary axes on (default) | off
  group: Display and Traces
- name: Real axes label
  summary: Real axis label Real Amplitude (default)
  group: Axes and Labels
- name: Title
  summary: Title label *None* (default)
  group: Axes and Labels
- name: Imaginary axes label
  summary: Imaginary axis label Imaginary Amplitude (default)
  group: Axes and Labels
- name: Y-limits
  summary: Lower and upper limit values [-1.1,1 1] (default) | scalar
  group: Axes and Labels
- name: Show grid
  summary: Show grid on plot on (default) | off
  group: Axes and Labels
- name: Preserve colors for copy to clipboard
  summary: Preserve colors for copy to clipboard off (default) | on
  group: COLOR AND STYLING
- name: Background
  summary: Background colors black (default)
  group: COLOR AND STYLING
- name: Axes
  summary: Axes colors black (default)
  group: COLOR AND STYLING
- name: Labels
  summary: Label colors grey (default)
  group: COLOR AND STYLING
- name: Style
  summary: Line style continuous (default)
  group: COLOR AND STYLING
- name: Width
  summary: Thickness for line plots 1.5 (default)
  group: COLOR AND STYLING
- name: Marker
  summary: Data point marker None (default) | ...
  group: COLOR AND STYLING
- name: Color
  summary: Color for lines yellow (default)
  group: COLOR AND STYLING
```

### Display and Traces

### **Samples per symbol** — Samples per symbol 8 (default) | positive integer

Number of samples per symbol, specified as a positive integer. Use
with **Symbols per trace** to determine the number of
samples per trace.

**Tunable:** Yes

### **Sample offset** — Sample offset 0 (default) | nonnegative integer

Sample offset, specified as a nonnegative integer smaller than the
product of **Samples per symbol** and **Symbols
per trace**. The offset provides the number of samples to
omit before plotting the first point.

**Tunable:** Yes

### **Symbols per trace** — Symbols per trace 2 (default) | positive integer

Number of symbols plotted per trace, specified as a positive
integer.

**Tunable:** Yes

### **Traces to display** — Number of traces to display 40 (default) | positive integer

Number of traces plotted, specified as a positive integer.

**Tunable:** Yes

#### Dependencies

### **Color fading** — Color fading `off` (default) | `on`

Select this check box to fade the points in the display as the
interval of time after they are first plotted increases.

### **Plot Imaginary Axes** — Plot imaginary axes `on` (default) | `off`

Select this check box to display the imaginary plot of the eye
diagram.

### Axes and Labels

### **Real axes label** — Real axis label `Real Amplitude` (default)

Text that the scope displays along the real axis.

**Tunable:** Yes

### **Title** — Title label *None* (default)

Label that appears above the eye diagram plot.

**Tunable:** Yes

### **Imaginary axes label** — Imaginary axis label `Imaginary Amplitude` (default)

Text that the scope displays along the imaginary axis.

**Tunable:** Yes

### **Y-limits** — Lower and upper limit values `[-1.1,1 1]` (default) | scalar

Lower and upper limit values of the *y*-axis.

**Tunable:** Yes

### **Show grid** — Show grid on plot `on` (default) | `off`

Select this radio button to show the grid on the scope window.

### COLOR AND STYLING

Use this tab to customize the style of the active display. You can change the
color of the figure containing the displays, the background and foreground colors of
display axes, and properties of lines in a display.

### **Preserve colors for copy to clipboard** — Preserve colors for copy to clipboard `off` (default) | `on`

Select this radio button to preserve the colors when copying to a
clipboard.

### **Background** — Background colors `black` (default)

Specify the background color for the plot..

### **Axes** — Axes colors `black` (default)

Specify the fill and line colors for the axes.

### **Labels** — Label colors `grey` (default)

Specify the color of the labels on the axes.

### **Style** — Line style `continuous` (default)

Specify the line style for the displayed signal.

### **Width** — Thickness for line plots `1.5` (default)

Specify the line thickness for the lines on displayed signal.

### **Marker** — Data point marker `None` (default) | ...

Data point marker for the selected signal, specified as one of the
choices in this table data point markers. This parameter is similar to
the `Marker` property for MATLAB®
Handle Graphics® plot objects.

| Specifier | Marker Type |
| --- | --- |
| none | No marker (default) |
|  | Circle |
|  | Square |
|  | Cross |
|  | Point |
|  | Plus sign |
|  | Asterisk |
|  | Diamond |
|  | Downward-pointing triangle |
|  | Upward-pointing triangle |
|  | Left-pointing triangle |
|  | Right-pointing triangle |
|  | Five-pointed star (pentagram) |
|  | Six-pointed star (hexagram) |

### **Color** — Color for lines `yellow` (default)

Specify the color for the lines on displayed signal.
## Libraries

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block is excluded from the generated code when code generation is performed on a system containing this block.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced in R2023b**

## Description

Display eye diagram of time-domain signal

The Eye Diagram block displays multiple traces of a modulated signal to
produce an eye diagram. You can use the block to reveal the modulation characteristics
of the signal, such as the effects of pulse shaping or channel distortions.

The Eye Diagram block has one input port. This block accepts a column
vector or scalar input signal. The block accepts a signal with the following data types:
double, single, base integer, and fixed point. All data types are cast as double before
the block displays results.

To modify the eye diagram display, select **SCOPE** and click the
**Settings** button () in **CONFIGURATION**.
