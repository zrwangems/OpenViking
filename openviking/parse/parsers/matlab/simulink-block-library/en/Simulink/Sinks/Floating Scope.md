---
type: simulink-block
title: 'Floating Scope and Scope Viewer'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'scopeviewer'
documentation_source_path: 'slref/scopeviewer.html'
language: en
---

# Floating Scope and Scope Viewer

## Ports

### Input

### **Port\_1** — Signal or signals to visualize scalar | vector | matrix | array | bus | nonvirtual bus

Connect the signals you want to visualize. You can have up to 96 input ports. Input signals can have
these characteristics:

- **Type** — Continuous (sample-based) or discrete (sample-based and
  frame-based).
- **Data type** — Any data type that Simulink supports. See Data Types Supported by Simulink.

  This block accepts fixed-point input, but converts it to
  `double` for display.
- **Dimension** — Scalar, one
  dimensional (vector), two dimensional (matrix), or multidimensional
  (array). Display multiple channels within one signal depending on
  the dimension. See Signal Dimensions and Determine Signal Dimensions.

#### Input Limitations

- When the input is a constant signal, the scope plots a single
  point.
- The scope shows gaps in the display when the signal value is
  `NaN`.
- When you visualize multiple frame-based signals in the scope,
  some samples of signals with a frame size of 1 might not be
  displayed. To visualize these signals, move the signals with
  frame size of 1 to a separate scope.

#### Bus Support

You can connect nonvirtual bus and arrays of bus signals to a scope.
To display the bus signals, use normal or accelerator simulation mode.
The scope displays each bus element signal in the order the elements
appear in the bus, from the top to the bottom. Nested bus elements are
flattened.

To log nonvirtual bus signals with a scope, set the **Save
format** parameter to `Dataset`.
You can use any **Save format** to log virtual bus
signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility
in subsystems that generate HDL code, but is not included in the hardware
implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block accepts fixed-point input, but converts it to double for
display.

## Version History

**Introduced in R2015b**

### R2025a: Improved Scope and new scope container to dock all scopes in one window

The Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer blocks in Simulink have a new user interface that you can use to access settings and measurements
of the scope. The scope is now more responsive and its performance is improved. Use the new
scope container to dock multiple scope windows into a single window and to manage and
organize the scopes. The scope container also enables you to view all the scopes in the
model in a single window.

Key improvements to the Scope, Time Scope, and
Floating Scope and Scope Viewer blocks are:

- Streamlined user interface: Easy access to all the general scope settings from
  the **Scope** tab and all the measurement settings from the
  **Measurements** tab of the new scope toolstrip.
- New scope container: A single window providing a unified view for all the
  scope displays in the model, enabling you to manage and organize multiple scopes
  in one place.
- Updated settings panel: Updated panel consolidates all general and style
  settings of the scope. To open the panel, click **Settings** in
  the **Scope** tab of the toolstrip.

### R2025a: Floating Signal Selection has been removed

The floating signal selection feature (Lock button used to enable the selection of multiple signals) in the Floating Scope block has been
removed. To connect signals to your floating scope, use the existing signal selector (signal selector icon on floating scope) instead. For more details, see Add Floating Scope Block to Model and Connect Signals.

### R2025a: Ability to dock Scopes to MATLAB desktop has been removed

The ability to dock the Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer to the MATLAB desktop has been removed. Use the new scope container instead. For more
information, see Scope Window Management.

If you have a model created in R2024b or a previous release with four or more open scopes,
and you open that model in R2025a, the opened scopes automatically dock in the scope
container window.

## Description

Display signals generated during simulation without signal lines

The Simulink® Scope Viewer and Floating Scope block display time domain
signals with respect to simulation time. The Scope Viewer and Floating
Scope block have the same functionality as the Scope block, but they are not connected
to signal lines.

**Scope Tab**

This screenshot highlights the important aspects of the scope window.

**Scope display features:**

- Simulation control — Run and debug models from a Scope window using
  **Run**, **Step Forward**, and
  **Step Backward** toolbar buttons.
- Multiple signals — Plot multiple signals on the same display.
- Multiple displays — Display signals on multiple subplots. All the
  *y*-axes of the subplots have a common time range on
  the *x*-axis. Control the layout of the subplots using
  the **Display Grid** parameter in the
  **Scope** tab of the toolstrip.
- Modify parameters — Modify scope parameter values before and during a
  simulation.
- Axis autoscaling — Autoscale axes during or at the end of a simulation.
  Margins are drawn at the top and bottom of the axes.
- Display data after simulation — Scope data is saved during a simulation.
  If a scope is closed at the start of a simulation, when you open the scope
  after a simulation, the scope displays simulation results for attached input signals.

  **Note**

  If you have a high sample rate or long simulation time, you may
  run into issues with memory or system performance because the scope
  saves data internally. To limit the amount of data saved for scope
  visualization, use the `Limit data points to
  last` property.
- Scope window management –– Use the new scope container to dock multiple
  scope windows into a single window and to manage and organize the scopes.
  The scope container also enables you to view all the scopes in the model in
  a single window.

**Measurements Tab**

This screenshot highlights the important aspects of the measurements window.

Here is a list of all the measurements the Scope Viewer and
Floating Scope block supports:

- Triggers — Set triggers on repeating signals and pause the
  display when events occur.
- Cursor
  Measurements — Measure signal values using vertical and
  horizontal cursors.
- Signal
  Statistics — Display the maximum, minimum, peak-to-peak
  difference, mean, median, and RMS values of a selected signal.

  **Note**

  You must have a Simscape™ or DSP System Toolbox™ license to use the Peak Finder, Bilevel Measurements, and
  Signal Statistics.
- Peak
  Finder — Find maxima, showing the *x*-axis
  values at which they occur.
- Bilevel
  Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

You must have a Simscape or DSP System Toolbox license to use the Peak Finder, Bilevel Measurements, and Signal
Statistics.

For information on controlling a Floating Scope block from the command
line, see Control Scope Blocks Programmatically.

### Connect Signals

In the Floating Scope window or Scope viewer window, use the  button to connect signals.

To add a viewer with a connected signal, select a signal in the model. Then, on
the **Simulation** tab, in the **Prepare**
gallery, click **Add Viewer**.

For more details, see Add Signals to Existing Floating Scope or Scope Viewer.

### Key Features

- Multiple *y*-axes (displays) — Display multiple
  *y*-axes. All the *y*-axes have a
  common time range on the *x*-axis.
- Multiple signals — Show multiple signals on the same
  *y*-axis (display).
- Modify parameters — Modify scope parameter values before and during
  a simulation.
- Display data after simulation — If a scope is closed at the start
  of a simulation, scope data is still written to the scope during the
  simulation. If you open the scope after a simulation, the scope displays
  simulation results for input signals.
