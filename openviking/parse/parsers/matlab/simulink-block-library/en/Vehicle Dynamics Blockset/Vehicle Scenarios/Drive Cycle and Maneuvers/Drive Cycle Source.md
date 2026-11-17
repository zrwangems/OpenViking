---
type: simulink-block
title: 'Drive Cycle Source'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'drivecyclesource'
documentation_source_path: 'ref/drivecyclesource.html'
language: en
---

# Drive Cycle Source

## Ports
```yaml
ports:
- name: VelFdbk
  summary: Vehicle longitudinal speed scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: RefSpd
  summary: Vehicle reference speed scalar
  direction: output
- name: RefAcc
  summary: Vehicle reference acceleration scalar
  direction: output
- name: Gear
  summary: Vehicle gear scalar
  direction: output
```

### Input

### **VelFdbk** — Vehicle longitudinal speed `scalar`

Longitudinal vehicle speed.

#### Dependencies

To enable this port, on the **Fault Tracking**
tab, select **Enable fault tracking**. Set the
**Velocity feedback units, inUnit** parameter
to the `VelFdbk` input port signal units.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | Description |
| --- | --- | --- |
| `Reference Speed` | | Vehicle reference speed |
| `Reference Accel` | | Vehicle reference acceleration |
| `Gear` | | Vehicle gear |
| `Fault` | `UpprBnd` | Upper bound of allowable vehicle speed range. |
| `LowerBnd` | Lower bound of allowable vehicle speed range. |
| `Fault` | Boolean value indicating fault condition:  - 1 — Fault - 0 — No fault    If the vehicle speed is not within the allowable speed range, the block sets a fault condition. |
| `FaultCnt` | Number of faults. |
| `CumFaultTime` | Cumulative time spent in fault condition. |
| `SnglFaultTime` | Time spent in a single fault. |
| `Fail` | Boolean value indicating fault failure:  - 1 — Failure - 0 — No failure    If the fault conditions exceed the maximum number of faults, maximum single fault time, or maximum total fault time, the block sets a fault failure. |

#### Dependencies

To enable this port, on the **Fault Tracking**
tab, select **Enable fault tracking**.

### **RefSpd** — Vehicle reference speed `scalar`

Vehicle reference speed, in units that you specify. To specify the
units, use the **Output velocity units**
parameter.

### **RefAcc** — Vehicle reference acceleration `scalar`

To calculate the acceleration, the block implements Savitzky-Golay
differentiation using a second-order polynomial with a three-sample
point filter.

#### Dependencies

To create the output acceleration port, select **Output
acceleration**. Selecting **Output acceleration** enables
the **Output acceleration units** parameter.

### **Gear** — Vehicle gear `scalar`

#### Dependencies

To enable this port:

1. First specify a drive cycle that contains a gear shift
   schedule. You can use:

   - A support package to install standard drive cycles that include the gear shift
     schedules, for example `JC08` and `CUEDC`.
   - Workspace variables.
   - .`mat`, .`xls`, .`xlsx`, or
     .`txt` files.
2. Select **Output gear shift**
   data.
## Parameters
```yaml
parameters:
- name: Drive cycle source
  summary: Select the drive cycle source FTP75 (default) | Wide Open Throttle (WOT) | Workspace variable | .mat, .xls, .xlsx
    or .txt file
  group: Cycle Setup
- name: From workspace
  summary: Workspace variable
  group: Cycle Setup
- name: Drive cycle source file
  summary: File name .mat, .xls, .xlsx or .txt
  group: Cycle Setup
- name: Repeat cyclically
  summary: Repeat drive cycle off (default) | on
  group: Cycle Setup
- name: Output acceleration
  summary: Output the acceleration off (default)
  group: Cycle Setup
- name: Output gear shift data
  summary: Output the gear off (default) | on
  group: Cycle Setup
- name: Start time, t_wot1
  summary: Drive cycle start time 5 (default) | scalar
  group: Cycle Setup
- name: Initial reference speed, xdot_woto
  summary: Speed 0 (default) | scalar
  group: Cycle Setup
- name: Nominal reference speed, xdot_wot1
  summary: Speed 30 (default) | scalar
  group: Cycle Setup
- name: Time to start deceleration, t_wot2
  summary: Time 20 (default) | scalar
  group: Cycle Setup
- name: Final reference speed, xdot_wot2
  summary: Speed 0 (default) | scalar
  group: Cycle Setup
- name: WOT simulation time, t_wotend
  summary: Time duration of simulation 30 (default) | scalar
  group: Cycle Setup
- name: Source velocity units
  summary: Specify velocity units m/s (default)
  group: Cycle Setup
- name: Output velocity units
  summary: Specify velocity units m/s (default)
  group: Cycle Setup
- name: Output acceleration units
  summary: Specify acceleration units m/s^2 (default)
  group: Cycle Setup
- name: Output sample period (0 for continuous), dt
  summary: Period between samples 0 (default) | scalar
  group: Cycle Setup
- name: Enable fault tracking
  summary: Enable fault tracking off (default) | on
  group: Fault Tracking
- name: Speed tolerance, velBnd
  summary: Drive cycle speed tolerance 2.0 (default) | scalar
  group: Fault Tracking
- name: Speed tolerance units, velBndUnit
  summary: Set units mph (default)
  group: Fault Tracking
- name: Velocity feedback units, inUnit
  summary: Set velocity feedback units m/s (default)
  group: Fault Tracking
- name: Time tolerance, timeBnd
  summary: Time tolerance 1.0 (default) | scalar
  group: Fault Tracking
- name: Enable Failure Tracking
  summary: Enable failure tracking off (default) | on
  group: Fault Tracking
- name: Stop simulation when trace fails
  summary: Stop simulation when trace fails off (default) | on
  group: Fault Tracking
- name: Maximum number of faults, maxFaultCnt
  summary: Maximum number of faults allowed 10 (default) | scalar
  group: Fault Tracking
- name: Maximum single fault time, maxFaultTime
  summary: Maximum allowed duration of single fault 2.0 (default) | scalar
  group: Fault Tracking
- name: Maximum total fault time, maxTotFaultTime
  summary: Maximum total fault time 15.0 (default) | scalar
  group: Fault Tracking
- name: Display simulation trace
  summary: Display velocity trace off (default) | on
  group: Fault Tracking
- name: Simulation trace update rate, dtTrace
  summary: Trace update period 1 (default) | scalar
  group: Fault Tracking
- name: Simulation trace display window, traceWindow
  summary: Trace window update rate 10 (default) | scalar
  group: Fault Tracking
```

### Cycle Setup

#### Setup

### **Drive cycle source** — Select the drive cycle source `FTP75` (default) | `Wide Open Throttle (WOT)` | `Workspace variable` | `.mat, .xls, .xlsx or .txt file`

- `FTP75` — Load the FTP75 drive
  cycle from a .`mat` file into a 1-D
  Lookup Table block. The FTP75 represents a
  city drive cycle that you can use to determine tailpipe
  emissions and fuel economy of passenger cars.

  To install additional drive cycles from a support package, see
  Support Package for Maneuver and Drive Cycle Data.
- `Wide Open Throttle (WOT)` —
  Use WOT parameters to specify a drive cycle for performance
  testing.
- `Workspace variable` — Specify
  time, speed, and, optionally, gear data as a structure, 2-D
  array, or time series object.
- `.mat, .xls, .xlsx or .txt file`
  — Specify a file that contains time, speed and,
  optionally, gear data in column format.

Once you have installed additional cycles, you can use
`set_param` to set the drive cycle. For example,
to use drive cycle
`US06`:

```
set_param([gcs '/Drive Cycle Source'],'cycleVar','US06')
```

#### Dependencies

This table summarizes the parameter dependencies.

| Drive Cycle Source | Enables Parameter |
| --- | --- |
| `Wide Open Throttle (WOT)` | **Start time, t\_wot1** |
| **Initial reference speed, xdot\_woto** |
| **Nominal reference speed, xdot\_wot1** |
| **Time to start deceleration, t\_wot2** |
| **Final reference speed, xdot\_wot2** |
| **WOT simulation time, t\_wotend** |
| **Source velocity units** |
| `Workspace variable` | **From workspace** |
| **Source velocity units** |
| **Output gear shift data**, if drive cycle includes gear shift schedule |
| `.mat, .xls, .xlsx or .txt file` | **Drive cycle source file** |
| **Source velocity units** |
| **Output gear shift data**, if drive cycle includes gear shift schedule |

### **From workspace** — Workspace `variable`

A workspace variable containing a monotonically increasing time
vector, a velocity vector, and, optionally, a gear data vector. You can
use a structure, 2-D array, or time series object. Enter units for
velocity in the **Source velocity units** parameter
field.

A valid point must exist for each corresponding time value. You cannot
specify `inf`, `empty`, or
`NaN`.

This table provides examples for using workspace variables to create your own drive cycles.

| Workspace Variable | Source Velocity Units | Output Velocity Units | Drive Cycle Plot |
| --- | --- | --- | --- |
| Structure without a gear shift schedule, with **From workspace** set to `myCycleS`.  ``` t = 0:1:100; xdot = 5.*sin(t)+10; myCycleS.time = t'; myCycleS.signals.values = xdot'; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| Structure with a gear shift schedule, with **From workspace** set to `myCycleS`.  ``` gears=[0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4]; t=0:1:10; xdot=[0,5,10,15,20,25,30,30,30,30,30]; myCycleS.time=t'; myCycleS.signals.values=[xdot',gears']; ``` | `m/s` | `mph` | Velocity versus time plot showing a linear increase from 0 mph at 0 seconds to 70 mph at 6 seconds. After 6 seconds, velocity remains constant at 70 mph. |
| 2-D array without a gear shift schedule, with **From workspace** set to `myCycleA`.  ``` t = 0:1:100; xdot = 5.*sin(t)+5; myCycleA = [t',xdot']; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| 2-D array with a gear shift schedule, with **From workspace** set to `myCycleA`.  ``` gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,5,10,15,20,25,30,40,50,60,60]; myCycleA=[t',xdot',gears']; ``` | `mph` | `mph` | Velocity versus time plot showing linear increases from 0 mph at 0 seconds to 30 mph at 6 seconds to 60 mph at 9 sec. After 9 seconds, velocity remains constant at 60 mph. |
| Time series object without a gear shift schedule, with **From workspace** set to `myCycleT`.  ``` myCycleT = timeseries; t = 0:1:100; xdot = 5.*sin(t)+20; myCycleT.Data = xdot'; myCycleT.Time = t'; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| Time series object without a gear shift schedule, with **From workspace** set to `myCycleT`.  ``` myCycleT = timeseries; gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,10,20,30,32,33,34,40,50,60,60]; myCycleT.Data = [xdot',gears']; myCycleT.Time = t'; ``` | `mph` | `mph` | Velocity versus time plot showing linear increases in mph. After 9 seconds, velocity remains constant at 60 mph. |

#### Dependencies

To enable this parameter, select `Workspace
variable` from **Drive cycle
source**.

### **Drive cycle source file** — File name `.mat, .xls, .xlsx or .txt`

File containing monotonically increasing time data, velocity data,
and, optionally, gear data in column or comma-separated format. The
block ignores units in the file. Enter units for source velocity in the
**Source velocity units** parameter field.

| File | Source Velocity Unit | Output Velocity Unit | Drive Cycle Plot |
| --- | --- | --- | --- |
| A .`mat` file containing a matrix with the same name as the file name.  The matrix contains time in column 1 and velocity in column 2. It can optionally contain gear selection in a column 3.  ``` sampcyc =           0         0     0.5000    0.7000     1.0000    2.0000      1.5000    3.6000     2.0000    5.6000     2.5000    7.9000      3.0000   10.3000     3.5000   13.0000      4.0000   16.0000     4.5000   19.0000     5.0000   22.3000     5.5000   25.7000     6.0000   29.3000 ``` | `m/s` | `m/s` | Velocity versus time plot |
| An .`xls` or .`xlsx` file with time in column A and velocity in column B.  11 rows with time in column A and velocity in column B | `mph` | `mph` | Velocity versus time plot |
| An .`xls` or .`xlsx` file with time in column A, velocity in column B, and gear in column C. The block:  - Ignores the headers and units in the   file. - Converts the gear information to integers:  - N to 0   - D to 2    12 rows with time in sec in column A, velocity in mph in column B, and gear in column C | `mph` | `mph` | Velocity versus time plot |
| A .`txt` with time in column 1 and velocity in column 2. The block ignores the header and units information.  20 rows with time in sec in column A and velocity in mph in column B | `mph` | `mph` | Velocity versus time plot |

You can import standard drive cycle file from an external source. For
example, you can import the Worldwide Harmonized Motorcycle Emissions
Certification and Test Procedure (WMTC) cycle by following the
instructions on WTMC. Specifically:

1. Download the gearshift sheets and instructions.
2. Follow the instructions to calculate the gear shift data
   based on your inputs.
3. The velocity units are `km/hr`. Convert
   the velocity to `m/s` using the conversion
   factor 1000/3600.
4. Copy and save the data into a new .`xls`
   or .`xlsx` file for use as a source file.

If you provide the gear schedule using **P**, **R**, **N**,
**D**, **L**, **OD**, the block maps the gears to integers.

| Gear | Integer |
| --- | --- |
| P | `80` |
| R | `-1` |
| N | `0` |
| L | `1` |
| D | `2` |
| OD | Next integer after highest specified gear. |

For example, the block converts the gear schedule `P P N L D 3 4 5 6 5 4
5 6 7 OD 7` to `80 80 0 1 2 3 4 5 6 5 4 5 6 7 8 7`.

#### Dependencies

To enable this parameter, select `.mat, .xls, .xlsx or
.txt file` from **Drive cycle
source**.

### **Repeat cyclically** — Repeat drive cycle `off` (default) | `on`

Repeat the drive cycle if the simulation run time exceeds the length
of the drive cycle.

### **Output acceleration** — Output the acceleration `off` (default)

To calculate the acceleration, the block implements Savitzky-Golay
differentiation using a second-order polynomial with a three-sample
point filter.

#### Dependencies

To create the output acceleration port, select **Output
acceleration**. Selecting **Output acceleration** enables
the **Output acceleration units** parameter.

### **Output gear shift data** — Output the gear `off` (default) | `on`

#### Dependencies

- First specify a drive cycle that contains a gear shift
  schedule. You can use:

  - A support package to install standard drive cycles that include the gear shift
    schedules, for example `JC08` and `CUEDC`.
  - Workspace variables.
  - .`mat`, .`xls`, .`xlsx`, or
    .`txt` files.
- Clicking this parameter creates input port
  **Gear**.

#### WOT Parameters

### **Start time, t\_wot1** — Drive cycle start time `5` (default) | `scalar`

Drive cycle start time, in s. For example, this plot shows a drive
cycle with a start time of `10` s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

### **Initial reference speed, xdot\_woto** — Speed `0` (default) | `scalar`

Initial reference speed, in units that you specify with the
**Source velocity units** parameter. For example,
this plot shows a drive cycle with an initial reference speed of
`4` m/s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

### **Nominal reference speed, xdot\_wot1** — Speed `30` (default) | `scalar`

Nominal reference speed, in units that you specify with the
**Source velocity units** parameter. This is the
maximum speed in the cycle. For example, this plot shows a drive cycle
with a nominal reference speed of `28` m/s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

### **Time to start deceleration, t\_wot2** — Time `20` (default) | `scalar`

Time to start vehicle deceleration, in s. For example, this plot shows
a drive cycle with vehicle deceleration starting at
`25` s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

### **Final reference speed, xdot\_wot2** — Speed `0` (default) | `scalar`

Final reference speed, in units that you specify with the
**Source velocity units** parameter. For example,
this plot shows a drive cycle with a final reference speed of
`2` m/s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

### **WOT simulation time, t\_wotend** — Time duration of simulation `30` (default) | `scalar`

Drive cycle WOT simulation time duration, in s. For example, this plot
shows a drive cycle with a total simulation time of
`50` s.

Velocity versus time plot

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`.

#### Units and Sample Period

### **Source velocity units** — Specify velocity units `m/s` (default)

Input velocity units.

#### Dependencies

To enable this parameter, select the **Drive cycle source** parameter
`Wide Open Throttle (WOT)`, `Workspace
variable`, or `.mat, .xls, .xlsx or .txt
file`.

### **Output velocity units** — Specify velocity units `m/s` (default)

Output velocity units.

### **Output acceleration units** — Specify acceleration units `m/s^2` (default)

Specify the output acceleration units.

#### Dependencies

To enable this parameter, select **Output
acceleration**.

### **Output sample period (0 for continuous), dt** — Period between samples `0` (default) | `scalar`

Sample period. Set to `0` for continuous sampling.
For discrete sampling, specify a non-zero period.

### Fault Tracking

#### Fault Settings

### **Enable fault tracking** — Enable fault tracking `off` (default) | `on`

Select this parameter to enable drive cycle fault tracking. Use the
parameters to specify the fault tolerances. If the vehicle speed is not
within the allowable speed range, the block sets a fault
condition.

#### Dependencies

Selecting this parameter enables these parameters:

- **Speed tolerance, velBnd**
- **Speed tolerance units,
  velBndUnit**
- **Velocity feedback units,
  inUnit**
- **Time tolerance, timeBnd**

### **Speed tolerance, velBnd** — Drive cycle speed tolerance `2.0` (default) | `scalar`

Standardized tests specify the speed tolerance to use. Here are two
examples:

- EPA dynamometer driving schedules —
  `2.0`
- WLTP tests — `2.0`

Note that the units for the EPA schedule are mph and for the WLTP
tests are km/h.

The block uses the speed tolerance to determine the allowable speed
range at the reference time. Within the time span defined by the
reference time +/- the time tolerance, the vehicle speed must be within
the reference speed range +/- the velocity tolerance, or the block will
set a fault condition. These figures illustrate how the block uses the
velocity and time tolerances to determine the allowable speed
range.

|  |  |
| --- | --- |
| Speed versus time plot indicating allowable speed range for increasing speed | Speed versus time plot indicating allowable speed range for decreasing speed |

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable fault
tracking**.

### **Speed tolerance units, velBndUnit** — Set units `mph` (default)

Standardized tests specify the units for speed tolerance. Here are two
examples:

- EPA dynamometer driving schedules —
  `mph`
- WLTP tests — `km/h`

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable fault
tracking**.

### **Velocity feedback units, inUnit** — Set velocity feedback units `m/s` (default)

Velocity feedback units. Set the value to the
`VelFdbk` input port signal units.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable fault
tracking**.

### **Time tolerance, timeBnd** — Time tolerance `1.0` (default) | `scalar`

The time tolerance, in units of seconds. Standardized tests specify
the time tolerance to use. Here are two examples:

- EPA dynamometer driving schedules —
  `1.0`
- WLTP tests — `1.0`

The block uses the time tolerance to determine the allowable speed
range at the reference time. Within the time span defined by the
reference time +/- the time tolerance, the vehicle speed must be within
the reference speed range +/- the velocity tolerance, or the block will
set a fault condition. These figures illustrate how the block uses the
velocity and time tolerances to determine the allowable speed
range.

|  |  |
| --- | --- |
| Speed versus time plot indicating allowable speed range for increasing speed | Speed versus time plot indicating allowable speed range for decreasing speed |

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable fault
tracking**.

#### Failure Settings

### **Enable Failure Tracking** — Enable failure tracking `off` (default) | `on`

Select this parameter to enable drive cycle failure tracking.

#### Dependencies

To enable this parameter, select **Enable fault
tracking**. Selecting **Enable failure
tracking** parameter enables these parameters:

- **Stop simulation when trace fails,
  stopSim**
- **Maximum number of faults,
  maxFaultCnt**
- **Maximum single fault time,
  maxFaultTime**
- **Maximum total fault time,
  maxTotFaultTime**

### **Stop simulation when trace fails** — Stop simulation when trace fails `off` (default) | `on`

Select this parameter to stop the simulation when the trace
fails.

To enable this parameter, on the **Fault Tracking**
tab, select **Enable failure tracking**.

### **Maximum number of faults, maxFaultCnt** — Maximum number of faults allowed `10` (default) | `scalar`

Maximum number of faults allowed during the drive cycle. For the
number specified by the standardized tests, use these settings:

- EPA dynamometer driving schedules — *Not
  specified*
- WLTP tests — `10`

If the number of faults exceeds the maximum number of faults, the
block sets a fault failure.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable failure
tracking**.

### **Maximum single fault time, maxFaultTime** — Maximum allowed duration of single fault `2.0` (default) | `scalar`

Maximum duration of single fault, in s. For the time specified by the
standardized tests, use these settings:

- EPA dynamometer driving schedules —
  `2.0`
- WLTP tests — `1.0`

If any fault duration exceeds the maximum single fault time, the block
sets a fault failure.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable failure
tracking**.

### **Maximum total fault time, maxTotFaultTime** — Maximum total fault time `15.0` (default) | `scalar`

Maximum accumulated time spent under fault condition, in s.

If the accumulated time spent under fault condition exceeds the
maximum total fault time, the block sets a fault failure.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Enable failure
tracking**.

#### Simulation Trace

### **Display simulation trace** — Display velocity trace `off` (default) | `on`

Select this parameter to display a velocity trace window. Selecting
this parameter can slow the simulation time.

#### Dependencies

Selecting this parameter enables these parameters:

- **Simulation trace update rate,
  dtTrace**
- **Simulation trace display window,
  traceWindow**

### **Simulation trace update rate, dtTrace** — Trace update period `1` (default) | `scalar`

Simulation trace update period, in s. Set to `0` for
continuous sample period. For a discrete period, specify a non-zero
rate.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Display simulation
trace**.

### **Simulation trace display window, traceWindow** — Trace window update rate `10` (default) | `scalar`

Simulation trace window update rate, in s.

#### Dependencies

To enable this parameter, on the **Fault
Tracking** tab, select **Display simulation
trace**.
## Libraries

Powertrain Blockset / Vehicle Scenario Builder Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2023b: Install additional standard drive cycles, including EPA test procedure cycles and duty cycles for commercial vehicles

In R2023b, you can install additional standard drive cycles, including:

- `EPA Federal Test Procedure(FTP75) - Without the Hot Soak
  Phase`
- `EPA Federal Test Procedure(FTP75) - Cold Stabilized
  Phase`
- `China Light-Duty Vehicle Test Cycle for Passenger
  Car`
- `China Heavy-Duty Commercial Vehicle Test Cycle for
  Tractor-Trailer`

## Description

Standard or specified longitudinal drive cycle

The Drive Cycle Source block generates a standard or user-specified
longitudinal drive cycle. The block output is the vehicle longitudinal reference speed
as a function of time, along with gear shift schedule if applicable. You can use the
drive cycle to:

- Predict the required engine torque and fuel consumption for a vehicle to
  follow a specified speed profile, with a given gear shift schedule.
- Produce realistic velocity and shift schedules for closed loop
  acceleration and braking commands for vehicle control and plant
  models.
- Study, tune, and optimize vehicle control, system performance, and system
  robustness in covering multiple drive cycles.
- Identify faults outside the tolerances specified by standardized tests.
  These include:

  - EPA dynamometer driving
    schedules1
  - Worldwide Harmonised Light Vehicle Test Procedure (WLTP)
    laboratory tests2

To generate drive cycles, you can use:

- Drive cycles from predefined sources. The block includes the
  `FTP–75` drive cycle by default, and additional cycles
  can be loaded from a support package.

  To install additional drive cycles from a support package, see Support Package for Maneuver and Drive Cycle Data. Certain drive cycles include the gear shift
  schedules, for example `JC08` and `CUEDC`.
- Workspace variables that define your own drive cycles.
- .`mat`, .`xls`,
  .`xlsx`, or .`txt` files. This allows you
  to load other standard drive cycles, or ones you have built.
- Wide open throttle (WOT) parameters. An initial and a nominal reference
  speed are set to produce a sudden large change in reference speed, inducing
  a WOT condition in the vehicle.

To achieve the goals listed in this table, use the specified Drive Cycle
Source block parameter options.

| Goal | Action |
| --- | --- |
| Repeat the drive cycle if the simulation run time exceeds the drive cycle length. | Select **Repeat cyclically**. |
| Output the acceleration, as calculated by Savitzky-Golay differentiation. | Select **Output acceleration**. |
| Specify a sample period for discrete applications. | Specify an **Output sample period (0 for continuous), dt** parameter. |
| Update the simulation run time so that it equals the length of the drive cycle. | Click **Update simulation time**. If a model configuration reference exists, the block does not enable this option. |
| Plot the drive cycle in a MATLAB® figure. | Click **Plot drive cycle**. |
| Specify the drive cycle using a workspace variable. | Click **Specify variable**. The block:  - Sets the **Drive cycle source**   parameter to `Workspace   variable`. - Enables the **From workspace**   parameter.    Specify the workspace variable so that it contains time, velocity, and, optionally, the gear shift schedule. |
| Specify the drive cycle by selecting a file.  This allows you to load standard cycles other than those listed. | Click **Select file**. The block:  - Sets the **Drive cycle source**   parameter to `.mat, .xls, .xlsx or .txt   file`. - Enables the **Drive cycle source   file** parameter.    Specify a file that contains time, velocity, and, optionally, the gear shift schedule. |
| Output the drive cycle gear. | First specify a drive cycle that contains a gear shift schedule. You can use:  - A support package to install standard drive cycles that include the gear shift   schedules, for example `JC08` and `CUEDC`. - Workspace variables. - .`mat`, .`xls`, .`xlsx`, or   .`txt` files.    Then click **Output gear shift data**. |
| Install additional drive cycles from a support package. | Click **Install additional drive cycles**. The block enables this option if you can install additional drive cycles from a support package. |
| Identify drive cycle faults outside the tolerances specified by standardized tests. | On the **Fault Tracking** tab, use the parameters to specify the fault tolerances. If the vehicle speed is not within the allowable speed range, the block sets a fault condition. |

### Fault and Failure Tracking

On the **Fault Tracking** tab, use the parameters to specify the
fault tolerances. If the vehicle speed is not within the allowable range a given
reference time, the block sets a fault condition. Examples for EPA and WLTP cycles
are shown here:

| Parameter | Description | Setting | |
| --- | --- | --- | --- |
| EPA Standard1 | WLTP Tests2 |
| **Speed tolerance** | Speed tolerance above the highest point and below the lowest point of the drive cycle speed trace within the time tolerance. | 2.0 mph | 2.0 km/h |
| **Time tolerance** | Time that the block uses to determine the allowable speed range. | 1.0 s | 1.0 s |
| **Maximum number of faults** | Maximum number of faults allowed during the drive cycle without causing fault failure. | *Not specified* | 10 |
| **Maximum single fault time** | Maximum fault duration allowed without causing fault failure. | 2.0 s | 1.0 s |
| **Maximum total fault time** | Maximum allowed accumulated time under fault condition without causing fault failure. | *Not specified* | *Not specified* |

The block uses the time tolerance to determine the allowable speed range at the
reference time. Within the time span defined by the reference time +/- the time
tolerance, the vehicle speed must be within the reference speed range +/- the
velocity tolerance, or the block will set a fault condition. These figures
illustrate how the block uses the velocity and time tolerances to determine the
allowable speed range.

|  |  |
| --- | --- |
| Speed versus time plot indicating allowable speed range for increasing speed | Speed versus time plot indicating allowable speed range for decreasing speed |

### Create Drive Cycles Using Workspace Variables

If you set **Drive cycle source** to `Workspace
variable`, you can specify a workspace variable that defines the
drive cycle.

This table provides examples for using workspace variables to create your own drive cycles.

| Workspace Variable | Source Velocity Units | Output Velocity Units | Drive Cycle Plot |
| --- | --- | --- | --- |
| Structure without a gear shift schedule, with **From workspace** set to `myCycleS`.  ``` t = 0:1:100; xdot = 5.*sin(t)+10; myCycleS.time = t'; myCycleS.signals.values = xdot'; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| Structure with a gear shift schedule, with **From workspace** set to `myCycleS`.  ``` gears=[0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4]; t=0:1:10; xdot=[0,5,10,15,20,25,30,30,30,30,30]; myCycleS.time=t'; myCycleS.signals.values=[xdot',gears']; ``` | `m/s` | `mph` | Velocity versus time plot showing a linear increase from 0 mph at 0 seconds to 70 mph at 6 seconds. After 6 seconds, velocity remains constant at 70 mph. |
| 2-D array without a gear shift schedule, with **From workspace** set to `myCycleA`.  ``` t = 0:1:100; xdot = 5.*sin(t)+5; myCycleA = [t',xdot']; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| 2-D array with a gear shift schedule, with **From workspace** set to `myCycleA`.  ``` gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,5,10,15,20,25,30,40,50,60,60]; myCycleA=[t',xdot',gears']; ``` | `mph` | `mph` | Velocity versus time plot showing linear increases from 0 mph at 0 seconds to 30 mph at 6 seconds to 60 mph at 9 sec. After 9 seconds, velocity remains constant at 60 mph. |
| Time series object without a gear shift schedule, with **From workspace** set to `myCycleT`.  ``` myCycleT = timeseries; t = 0:1:100; xdot = 5.*sin(t)+20; myCycleT.Data = xdot'; myCycleT.Time = t'; ``` | `m/s` | `mph` | Velocity versus time plot showing a sine wave |
| Time series object without a gear shift schedule, with **From workspace** set to `myCycleT`.  ``` myCycleT = timeseries; gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,10,20,30,32,33,34,40,50,60,60]; myCycleT.Data = [xdot',gears']; myCycleT.Time = t'; ``` | `mph` | `mph` | Velocity versus time plot showing linear increases in mph. After 9 seconds, velocity remains constant at 60 mph. |
