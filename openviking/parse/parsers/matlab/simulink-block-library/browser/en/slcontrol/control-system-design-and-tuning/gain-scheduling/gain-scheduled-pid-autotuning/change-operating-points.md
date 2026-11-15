---
type: simulink-block
title: 'Change Operating Points'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Operating Points'
documentation_page: 'changeoperatingpoints'
documentation_source_path: 'ug/changeoperatingpoints.html'
language: en
---

# Change Operating Points

## Ports

### Input

### **systeminputs\_in** — System inputs array

Specify the value of the input level at the operating point.

When the block is operating in the snapshot mode, the block directly
passes through this input to the **systeminputs\_out**
port.

### **enable/disable** — Enable and disable changing operating points scalar

Specify a signal to enable (`1`) or disable
(`0`) the block action.

### **autotuning times** — Time vector to start autotuning vector

Specify the time vector to start autotuning. The value at each index
of this vector is the autotuning start time for the operating point at
that index. Use the **Autotuning time span (sec)**
parameter to specify the duration of the experiment.

#### Dependencies

To enable this port, use this configuration.

- Set **Operating mode** to
  `Import operating
  points`.
- Select **Use block for
  autotuning**.
- Set **Method for starting autotuning**
  to `External time vector`.

### **next OP** — Next operating point scalar

Specify the custom logic to switch to the next operating point.

#### Dependencies

To enable this port, use this configuration.

- Set **Operating mode** to
  `Import operating
  points`.
- Set **Transition method** to
  `External trigger`.

### **y** — Plant output scalar | vector

Connect the output of your plant to this port. The block determines
the current operating state of the system using this signal.

#### Dependencies

To enable this port, use this configuration.

- Set **Operating mode** to
  `Import operating
  points`.
- Select **Use block for
  autotuning**.
- Set **Method for starting autotuning**
  to `Time after reaching
  steady-state`.

### **enable autotuning** — Enable or disable autotuning scalar

Use this port to manually specify a scalar flag to enable
(`1`) or disable (`0`) the
autotuning process.

#### Dependencies

To enable this port, use this configuration.

- Set **Operating mode** to
  `Import operating
  points`.
- Select **Use block for autotuning** and
  **Add enable/disable port for
  autotuning**.

### **snapshot trigger** — Snapshot trigger vector

Specify the time-based or event-based snapshot triggers at which you
want to extract the operating point of the model.

When **Snapshot mode** is
**Time-based**, specify the time values for which
you want to snapshot operating point data. For example, to snapshot at
3, 5, and 7 s, use a vector `[3,5,7]` as input to this
port.

When **Snapshot mode** is **Event-based**, the block
snapshots the operating point data at the rising edges of the input
signal.

#### Dependencies

To enable this port, set **Operating mode** to
`Snapshot operating points`, and use
one of these configurations.

- Set **Snapshot mode** to
  **Time-based** and select
  **Use external source**.
- Set **Snapshot mode** to
  **Event-based**.
### Output

### **systeminputs\_out** — Operating point output bus

Reference signal to move the system to the switched operating
point.

### **start\_stop** — Signal to start and stop the autotuning scalar

Signal to start and stop the autotuning process with the Closed-Loop PID Autotuner
block. The generated signal depends on the additional parameters such as
the autotuning method and steady-state settings.

#### Dependencies

To enable this port, set **Operating mode** to
`Import operating points` and select
**Use block for autotuning**.

## Parameters

### Import operating point Tab

### **Operating mode** — Mode for operating point data `Import operating points` (default) | `Snapshot operating points`

Specify the mode for obtaining the operating point data.

- `Import operating points` — Specify
  predefined operating point data by either manually editing the
  table in block dialog box or importing an
  `OperatingPoint` object.

  In this mode, you can use the block to implement a streamlined
  workflow for autotuning gain-scheduled PID controllers over an
  operating range.
- `Snapshot operating points` —
  Snapshot operating points at specified times or events during
  simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OperatingMode` |
| **Type:** string |
| **Values:** `"Import operating points"` | `"Snapshot operating points"` |
| **Default:** `"Import operating points"` |

### **Input method** — Input method for operating point data **Manually edit table** (default) | **Automatically fill Table**

Specify the input method for operating point data.

- **Manually edit table** — Manually specify
  the operating point data in the block dialog.
- **Automatically fill table** — Import
  operating point data using an `OperatingPoint`
  object. Typically, you obtain operating points using functions
  such as `operpoint` and
  `findop`, or Steady State Manager and Model Linearizer
  apps. You can also import the operating point data obtained
  using the snapshot mode of this block.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputMethod` |
| **Type:** string |
| **Values:** `"Manually edit table"` | `"Automatically fill table"` |
| **Default:** `"Manually Edit Table"` |

### **Number of inputs** — Number of model inputs `3` (default) | positive scalar

Specify the number of inputs in the model.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Input method** to **Manually edit
table**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumSystemInputs` |
| **Type:** string |
| **Values:** positive scalar in quotes |
| **Default:** `"3"` |

### **Workspace** — Workspace to import operating point data `Base workspace` (default) | `Model workspace` | `Data dictionary`

Specify the workspace from which you want to import the operating
point data from. The specified workspace must contain the
`OperatingPoint` object with the same name as the
value in **Operating point variable**.

- `Base workspace` — Import data from
  base MATLAB® workspace.
- `Model workspace` — Import data from
  the current model workspace.
- `Data dictionary` — Import data from
  a Simulink® data dictionary.

Additionally, to import the operating point data generated by the
block in the snapshot mode, click the **Save to
Workspace** button and specify the name of the operating
point structure.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Input method** to **Automatically
fill table**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImportWorkspace` |
| **Type:** string |
| **Values:** `"Data dictionary"` | `"Base workspace"` | `"Model workspace"` |
| **Default:** `"Data dictionary"` |

### **Data dictionary name** — Data dictionary name `myDataDictionary.sldd` (default) | string

Specify the name of the data dictionary to read the operating point
data from. The `OperatingPoint` object must be stored in
the `Other Data` section of the dictionary. For more
information, see What Is a Data Dictionary?.

#### Dependencies

To enable this parameter, set these parameters.

- **Operating mode** to `Import
  operating points`
- **Input method** to
  **Automatically fill table**
- **Workspace** to `Data
  dictionary`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataDictionaryName` |
| **Type:** string |
| **Default:** `"myDataDictionary.sldd"` |

### **Operating point variable** — Name of operating point variable `myOperatingPoint` (default) | string

Specify the name of the operating point variable.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Input method** to **Automatically
fill table**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OperatingPointVariable` |
| **Type:** string |
| **Default:** `"myOperatingPoint"` |

### **Snapshot mode** — Operating point snapshot mode **Time-based** (default) | **Event-based**

Specify the snapshot mode to obtain the operating point data.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Snapshot operating points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SnapshotMode` |
| **Type:** string |
| **Values:** `"Time-based"` | `"Event-based"` |
| **Default:** `"Time-based"` |

### **Snapshot times (sec)** — Simulation snapshot times `[0 1 2]` (default) | scalar | vector

Specify the simulation snapshot times at which to extract the
operating point of the model. Use a scalar for a single snapshot or a
vector for multiple snapshots.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Snapshot operating points` and
**Snapshot mode** to
**Time-based**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SnapshotTimes` |
| **Type:** string |
| **Values:** scalar or vector in quotes |
| **Default:** `"[1 2 3]"` |

### **Use external source** — Use input port for snapshot times `off` (default) | `on`

Specify the simulation snapshot times as block input.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Snapshot operating points` and
**Snapshot mode** to
**Time-based**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SnapshotTimesExternalSource` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Sample time (-1 for inherited)** — Sample time `-1` (default) | positive scalar

Specify the sample time.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Snapshot operating points` and
**Snapshot mode** to
**Time-based**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string |
| **Values:** positive scalar in quotes | "–1" |
| **Default:** `"–1"` |

### **Operating point definitions** — Operating point data multiple table entries

Operating point data, specified as multiple table entries.

When the **Input Method** is **Manually edit
table**, use the **Value** column of the
table to manually specify the corresponding data for index, snapshot
time, and input level of the operating points.

When the **Input Method** is **Automatically
fill table**, the **Value** show the value
of the operating point based on the imported operating point.

To populate the entries of the table after obtaining the data in
snapshot mode, click **Save to Table**.

#### Dependencies

To enable manual data entry for the **Value**
column of this table, set **Operating mode** to
`Import operating points` and
**Input method** to **Manually edit
table**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OperatingPointTable` |
| **Type:** string |
| **Values:** cell array in quotes |
| **Default:** `"{'Indicies','[1 2 3]';'Times (sec)','[0 1 2]';'SystemInput_1','[1 1 1]';'SystemInput_2','[2 2 2]';'SystemInput_3','[3 3 3]'}"` |

### **Bus name** — Name of bus object `scdPlantOPsBusObject` (default) | string

Specify a name for the `Simulink.Bus` object created by the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BusName` |
| **Type:** string |
| **Values:** string |
| **Default:** `"scdPlantOPsBusObject"` |

### **Specify bus name** — Specify bus name `off` (default) | `on`

Specify a bus name for the object manually.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpecifyBusName` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Data Type** — Floating point precision `Double` (default) | `Single`

Specify the floating-point precision based on simulation environment
or hardware requirements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BlockDataType` |
| **Type:** string |
| **Values:** `"Double"` | `"Single"` |
| **Default:** `"Double"` |

### Change operating point setting Tab

### **Use block for autotuning** — Use block for PID autotuning workflow `on` (default) | `off`

Use the block for gain-scheduled PID autotuning workflow. When you enable this option,
the block generates a signal at the **start\_stop**
output port. Use the **start\_stop** signal to start and
stop the autotuning process with the Closed-Loop PID
Autotuner block. The generated signal depends on the
additional parameters such as the autotuning method and steady-state
settings.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseAutotuning` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Method for starting autotuning** — Method for starting autotuning `External time vector` (default) | `Time after reaching steady-state`

Specify the method for starting PID autotuning.

- `External time vector` — Specify a
  time vector using the **autotuning times**
  input port. The value at each index of this vector is the
  autotuning start time for the operating point at that index. Use
  the **Autotuning time span (sec)** parameter to
  specify the duration of the experiment.
- `Time after reaching steady-state` —
  Start the autotuning when the model output reaches steady state.
  Use the **Settling time upper bounds**,
  **Settling time lower bounds**, and
  **Settling time interval** parameters to
  define the criteria for steady state of each operating
  point.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and select
**Use block for autotuning**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AutotuningTriggerMethod` |
| **Type:** string |
| **Values:** `"External time vector"` | `"Time after reaching steady-state"` |
| **Default:** `"External time vector"` |

### **Add enable/disable port for autotuning** — Add enable/disable port for autotuning `off` (default) | `on`

Add the **enable autotuning** input port to the
block. Use this port to manually specify a scalar flag to enable
(`1`) or disable (`0`) the
autotuning process.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and select
**Use block for autotuning**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AddEnableDisableAutotuning` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Autotuning time span (sec)** — Autotuning experiment duration `10` (default) | positive scalar | vector

Specify the duration of the autotuning experiment. You must let the
experiment run long enough for the algorithm to collect sufficient data
for a good estimate of the plant frequency responses. Running the
experiment for insufficient time may result in inaccurate results. For
more information, see the **start/stop** input port of
the Closed-Loop PID Autotuner block.

- To run the autotuning experiment with the same duration for
  all operating points, specify a positive scalar value.
- To run the experiment for different duration for each
  operating point, specify a vector of positive values. Each
  duration value corresponds to the operating point at that index
  of the vector.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and select
**Use block for autotuning**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AutotuningExperimentLength` |
| **Type:** string |
| **Values:** positive scalar or vector in quotes |
| **Default:** `"10"` |

### **Number of samples to start autotuning after reaching steady-state** — Delay to start autotuning `2` (default) | positive scalar

Specify the number of samples for which the block delays starting the
autotuning process after the model reaches the steady state.

#### Dependencies

To enable this parameter, use this configuration.

- Set **Operating mode** to
  `Import operating
  points`.
- Select **Use block for
  autotuning**.
- Set **Method for starting autotuning** to
  `Time after reaching
  steady-state`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumAutotuningDelaySamples` |
| **Type:** string |
| **Values:** positive scalar in quotes |
| **Default:** `"2"` |

### **Transition method** — Operating point transition method `Internal time vector (from operating point table)` (default) | `Time after reaching steady-state` | `Time after completing autotuning` | `External trigger`

Specify the operating point transition method.

- `Internal time vector (from operating point
  table)` — Change operating points based on the
  values in the time vector of the operating point data.
- `Time after reaching steady-state` —
  Change operating points after the model output reaches the
  steady state condition defined for that operating point.
- `Time after completing autotuning` —
  Change operating points after the autotuning time span has
  passed for that operating point.
- `External trigger` — Change operating
  point based on the custom logic specified at the **next
  OP** block input port.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransitionMethod` |
| **Type:** string |
| **Values:** `"Internal time vector (from operating point table)"` | `"Time after reaching steady-state"` | `"Time after completing autotuning"` | `"External trigger"` |
| **Default:** `"Internal time vector (from operating point table)"` |

### **Change operating point algorithm** — Operating point transition algorithm `Step` (default) | `Ramp`

Specify the algorithm to transition from one operating point to
another.

- `Step` — Use a step signal to step
  between two operating levels.
- `Ramp` — Use a ramp signal to between
  two operating levels as a constantly increasing or decreasing
  signal.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChangeOPAlgorithm` |
| **Type:** string |
| **Value** `"Step"` | `"Ramp"` |
| **Default:** `"Step"` |

### **Rising slew rate (/sec)** — Limit of derivative for increasing input `1` (default) | scalar | vector

Specify the limit of the rising rate of the input signal.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Change operating point algorithm** to
`Ramp`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RampSlewUpRate` |
| **Type:** string |
| **Values:** scalar or vector in quotes |
| **Default:** `"1"` |

### **Falling slew rate (/sec)** — Limit of derivative for decreasing input `-1` (default) | scalar | vector

Specify the lower limit on the falling rate of the input
signal.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Change operating point algorithm** to
`Ramp`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RampSlewLoRate` |
| **Type:** string |
| **Values:** scalar or vector in quotes |
| **Default:** `"–1"` |

### **Number of samples to transition after reaching steady-state** — Delay to transition operating points `2` (default) | nonnegative scalar

Specify the number of samples for which the block delays transition to
the next operating point after the model reaches the steady
state.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Transition method** to `Time
after reaching steady-state`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumTransitionDelaySamples` |
| **Type:** string |
| **Values:** nonnegative scalar in quotes |
| **Default:** `"2"` |

### **Number of samples to transition after completing autotuning** — Delay to transition operating points `2` (default) | nonnegative scalar

Specify the number of samples for which the block delays transition to
the next operating point after the autotuning experiment has
completed.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Transition method** to `Time
after completing autotuning`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumSamplesAutotuningTranstion` |
| **Type:** string |
| **Values:** nonnegative scalar in quotes |
| **Default:** `"2"` |

### **Settling time upper bounds** — Upper bound for settling time `[1.1 2.1 3.1]` (default) | vector

Specify the upper bound for the operating value used to determine
settling time and steady state of the operating point.

Each value of this vector corresponds to the upper bound for the
operating point value at that index.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Transition method** to `Time
after reaching steady-state`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SettlingTimeUpper` |
| **Type:** string |
| **Values:** scalar or vector in quotes |
| **Default:** `"[1.1 2.1 3.1]"` |

### **Settling time lower bounds** — Lower bound for settling time `[0.9 1.9 2.9]` (default) | vector

Specify the lower bound for the operating value used to determine
settling time and steady state of the operating point.

Each value of this vector corresponds to the lower bound for the
operating point value at that index.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Transition method** to `Time
after reaching steady-state`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SettlingTimeLower` |
| **Type:** string |
| **Values:** scalar or vector in quotes |
| **Default:** `"[0.9 1.9 2.9]"` |

### **Settling time interval** — Settling time interval `5` (default) | scalar | vector

Specify the time interval for which the operating condition remains in
steady state.

Use a vector to specify different time intervals for different
operating points.

#### Dependencies

To enable this parameter, set **Operating mode**
to `Import operating points` and
**Transition method** to `Time
after reaching steady-state`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SettlingTimeInterval` |
| **Type:** string |
| **Values:**scalar or vector in quotes |
| **Default:** `"5"` |

## Libraries

Simulink Control Design / Autotuning

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Change Operating Points block supports code generation only
when **Operating mode** is `Import operating
points`.

## Version History

**Introduced in R2023b**

## Description

tSwitch between operating points during simulation

The Change Operating Points block lets you manage and switch operating points
during simulation. You can use the block in one of these configurations:

- Import predefined operating data from workspace and switch between operating
  range during the simulation.
- Automatically snapshot at specified times or events during simulation to
  obtain the operating point data at the specified range. For example, for a motor
  model, you can snapshot at:

  - 3, 5, and 7 s (time-based).
  - 2000, 5000, and 8000 rpm (event-based).

When you have predefined operating point data, you can use this block in
gain-scheduled controller tuning workflows. This block helps generate reference signals
which move your plant from one operating point to another. Otherwise, snapshot the
operating points first, and then use the data for gain scheduling workflows.

Typically, tuning a gain-scheduled controller is a complex process. It requires you to run
multiple simulations for tuning at each operating point and provide a logic to store PID
gains at that operating point. Using this block, along with the PID Gains Store
and Update and PID Gain
Scheduler blocks, helps you implement a streamlined workflow for autotuning
gain-scheduled PID controllers over an operating range in a single run. To do so, use
this workflow.

1. Switch between predefined or snapshot operating point data during the
   simulation using the Change Operating Points block.
2. Perform autotuning at the operating points using Closed-Loop PID
   Autotuner.
3. Store the PID gains corresponding to the operating point in an array using
   PID Gains Store and Update block.
4. Perform lookup table based gain scheduling from the array using the PID
   Gain Scheduler block.

On a high level, you can use these blocks to implement the gain-scheduled workflow as
shown in this diagram.

Diagram of a gain-scheduled system, with Closed-Loop PID Autotuner, PID Controller, Change Operating Points, Gain Scheduler, and PID Gains Store and Update blocks.
