---
type: simulink-block
title: 'Simulation Pace'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Simulator Interfaces'
documentation_page: 'simulationpace'
documentation_source_path: 'simulationpace.html'
language: en
---

# Simulation Pace

## Ports

### Output

### **Port\_1** — Pace error scalar

Pace error, specified as a scalar.

The block optionally outputs the pace error value
(*simulationTime* minus
*ClockTime*), in seconds. The pace error is
positive if the simulation is running faster than the specified pace and
negative if slower than the specified pace.

Outputting the pace error from the block lets you record the overall
pace achieved during the simulation or routing the signal to other
blocks to determine if the simulation is too slow to keep up with the
specified pace.

#### Dependencies

To enable this port, select the **Output pace error
(sec)** check box.

**Data Types:** `double`

## Parameters

### **Simulation pace** — Ratio of simulation time to clock time `1` (default) | scalar

Ratio of simulation time to clock time, specified as a scalar, in seconds
of simulation time per second of clock time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputPaceError` |
| **Type**: character vector |
| **Values:**`'1'` | scalar |
| **Default**: `'1'` |

### **Sleep mode** — Control simulation pace `Auto` (default) | `MATLAB Thread` | `Off` | `Busy-Wait`

Control simulation pace of model using one of these methods. `MATLAB
Thread`, `Busy-Wait`, and
`Auto` slow down the simulation pace at
simulation-second 0.1 to wait for the wall clock to get to time 1. Use this
parameter when one simulation-second is completed in a few wall clock time
milliseconds.

- `Auto` — Use the model configuration
  parameter setting **Enable pacing to slow down
  simulation** to control the simulation pace. If the
  model configuration parameter setting **Enable pacing to
  slow down simulation** is not selected, the block
  behaves as though the `MATLAB Thread`
  option is selected.
- `MATLAB Thread` — Use the operating
  system `sleep` function during simulation to wait
  for the wall clock to get to time 1.
- `Off` — Disable the pace functionality
  and let the simulation run as fast as possible.
- `Busy-Wait` — Use a while loop in
  conjunction with the Simstruct to wait for the simulation to wait
  for the wall clock to get to time 1.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SleepMode` |
| **Type**: character vector |
| **Values:**`'MATLAB Thread'` | `'Off'` | `'Busy-Wait'` | `'Auto'` |
| **Default**: `'Auto'` |

### **Output pace error** — Display pace error `off` (default) | `on`

Select this check box to output the pace error value (*simulationTime*
minus *ClockTime*), in seconds. The pace error is positive
if the simulation is running faster than the specified pace and negative if
slower than the specified pace. To disable the display, clear this check box
.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputPaceError` |
| **Type**: character vector |
| **Values:**`'off' | 'on'` |
| **Default**: `'off'` |

### **Sample time** — Sample time 1/30 (default) | `-1` | scalar | vector

Specify the sample time as a scalar. The default 1/30th of a second
corresponds to a 30 frames-per-second visualization rate (typical for
desktop computers). To set how often the Simulink interface synchronizes with the wall clock, use this
parameter.

The block sample time must be:

- Discrete
- Greater than 0.0 or an inherited sample time (-1)

The block sample time and its optional offset time ([`Ts``,
To`]) must be finite and
discrete.

**Caution**

Choose as slow a sample time as needed for smooth animation, since
oversampling has little benefit and undersampling can cause animation
jumpiness. Undersampling can also potentially block the MATLAB® main thread on your computer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'1/30'` |

## Libraries

Aerospace Blockset / Animation / Animation Support Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2023a: Simulation Pace Block Support for Referenced Models

The Simulation Pace block is not supported in referenced models for
simulation in accelerator or rapid accelerator mode. Starting in R2023a, to slow
down the simulation in these modes, in the **Simulation** tab of
the Simulink Editor toolstrip, select **Run** > **Simulation Pacing**.

## Description

Set simulation rate for animation viewing

The Simulation Pace block lets you run model simulation at a
slower pace so that you can comfortably view connected animations and understand and
observe the system behavior. Visualizing simulations at a slower rate makes it easier to
understand underlying system design, identify design issues and demonstrate near
real-time behavior. You can view the results and inspect your system while the
simulation is in progress.

Use this block in scenarios where one simulation-second is completed in a few wall
clock time milliseconds.

When configuring this block, also consider the block sample time, which affects the
simulation pace. The default is 1/30th of a second, which corresponds to a 30
frames-per-second visualization rate (typical for desktop computers). For more
information, see Sample time.

To use this block:

- Set the model solver to `Fixed-step`.
- Use a discrete sample time.

**Tip**

The Simulation Pace block:

- Does not produce deployable code.
- Is not supported in referenced models for simulation in accelerator or
  rapid accelerator mode. To slow down the simulation in these modes, in the
  **Simulation** tab of the Simulink® Editor toolstrip, select **Run** > **Simulation Pacing**.
