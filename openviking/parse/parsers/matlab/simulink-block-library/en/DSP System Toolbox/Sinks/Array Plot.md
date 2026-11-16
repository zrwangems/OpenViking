---
type: simulink-block
title: 'Array Plot'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'arrayplot'
documentation_source_path: 'ref/arrayplot.html'
language: en
---

# Array Plot

## Ports

### Input

### **Port\_1** — Signal or signals to visualize scalar | vector | matrix | array

Connect the signals you want to visualize. You can have up to 96 input
ports. Input signals must have these characteristics:

- Fixed number of channels, but size can be variable
- Discrete, continuous, or constant sample time
- Real or complex values
- Floating- or fixed-point data type
- 2-D and nonscalar

The Array Plot block supports inputs with different
frame lengths.

This block accepts fixed-point input, but converts it to
`double` for display.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

## Parameters

Not documented in R2025b.

## Libraries

DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

## Version History

**Introduced in R2015b**

### R2025a: Control plot type for each line individually

You can now individually control the type of plot for each line. To control the type of plot
for a line, select the line and set the **Plot Type**
parameter accordingly.

### R2024b: Support for bar plots

The Array Plot block now supports bar plots. To view data using a
bar plot, set **Plot Type** to `Bar` in
Array Plot settings > **Color and Styling**.

### R2024b: Support for multiple displays

Click the new **Display Grid** property in the
**Scope** tab to specify the layout of the Array Plot scope
display. When you select a 2-by-2 layout, for example, the scope shows four displays
arranged in a 2-by-2 matrix. The display grid can have a maximum of five rows and
five columns.

### R2024b: Specify active display

You can now specify the active display using the **Active
Display** property in the Array Plot settings > **Display and
Labels**. The settings in the **Y-Limits**,
**X-Label**, **Y-Label**, **Show
Legend**, **Show Grid**, **Title**,
and **Magnitude Phase Plot** properties affect only the active
display.

### R2024b: Higher display precision in scope UI

You can now increase the display precision to 15 digits using the **Display
Precision** property in the scope settings under **Display and
Labels**. This precision affects all the measurements and data that the scope
displays on its status bar.

### R2024b: **Preserve Colors** is now available in scope toolstrip

The **Preserve colors for copy to clipboard** property has been renamed to **Preserve Colors** and is now available in the scope toolstrip under **Copy Display**.

### R2024b: **Magnitude Phase** property is now available in Array Plot settings

The **Magnitude Phase** property has been renamed to
**Magnitude Phase Plot** and is now available in the Array Plot
settings > **Display and Labels**.

### R2024b: **Show Legend** property is now also available in Array Plot settings

The **Show Legend** property is now also available in the Array
Plot settings > **Display and Labels**. To control the legend
display, you can select **Legend** in the
**Scope** tab of the Array Plot toolstrip or select the
**Show Legend** property.

### R2024a: **Plot** tab has been renamed as **Scope** tab

The **Plot** tab in array plot has been renamed as
**Scope** tab.

## Description

Display vectors or arrays

The Array Plot  block plots vectors or arrays of data.

Array Plot block window

The Array Plot is a vector plot where data is uniformly spaced along
the *x*-axis. To modify the spacing, change the `Sample
Increment` property.

Measurements available:

- Data Cursors — Measure signal values using vertical and horizontal
  cursors.
- Signal Statistics — Display the maximum, minimum, peak-to-peak difference,
  mean, median, and RMS values of a selected signal.
- Peak Finder — Find maxima, showing the *x*-axis values at
  which they occur.
