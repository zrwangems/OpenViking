---
type: simulink-block
title: 'Generalized Optimal Subpattern Assignment Metric'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Track Metrics'
documentation_page: 'generalizedoptimalsubpatternassignmentmetric'
documentation_source_path: 'ref/generalizedoptimalsubpatternassignmentmetric.html'
language: en
---

# Generalized Optimal Subpattern Assignment Metric

## Ports
```yaml
ports:
- name: Tracks
  summary: Track list Simulink® bus containing MATLAB® structure
  direction: input
- name: Truths
  summary: Truth list Simulink bus containing MATLAB structure
  direction: input
- name: Assignments
  summary: Known assignment *K*-by-2 matrix of nonnegative integers
  direction: input
- name: GOSPA Metric
  summary: GOSPA metric including switching error component nonnegative real scalar
  direction: output
- name: GOSPA Metric Without Switching
  summary: GOSPA metric without switching error component nonnegative real scalar
  direction: output
- name: Switching Error
  summary: Switching error component nonnegative real scalar
  direction: output
- name: Localization Error
  summary: Localization error component nonnegative real scalar
  direction: output
- name: Missed Target Error
  summary: Missed target error component nonnegative real scalar
  direction: output
- name: False Track Error
  summary: False track error component nonnegative real scalar
  direction: output
```

### Input

### **Tracks** — Track list Simulink® bus containing MATLAB® structure

Track list, specified as a Simulink bus containing a MATLAB structure.

If you specify the **Track bus** parameter on the **Port
Setting** tab to `objectTrack`, the structure must
use this form:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures |

Each track structure must contain `TrackID` and `State`
fields. Additionally, if you specify an NEES-based distance (`posnees`
or `velnees`) in the **Distance type** parameter, each
structure must contain a `StateCovariance` field.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks, specified as a nonnegative integer. |
| `State` | Value of state vector at the update time, specified as an *N*-element vector, where *N* is the dimension of the state. |
| `StateCovariance` | Uncertainty covariance matrix, specified as an *N*-by-*N* matrix, where *N* is the dimension of the state. |

If you specify an NEES-based distance (`posnees` or
`velnees`) in the **Distance type** parameter,
then the structure must contain a `StateCovariance` field.

If you specify the **Track bus** parameter to
`custom`, then you can use your own track bus format. In
this case, you must define a track extractor function using the **Track
extractor function** parameter. The function must use this
syntax:

```
tracks = trackExtractorFcn(trackInputFromBus)
```

where
`trackInputFromBus` is the input from the track bus and
`tracks` must return as an array of structures with
`TrackID` and `State` fields.

### **Truths** — Truth list Simulink bus containing MATLAB structure

Truth list, specified as a Simulink bus containing a MATLAB structure.

If you specify the **Truth bus** parameter on the **Port
Setting** tab to
`Platform`, the structure
must use this form:

| Field | Description |
| --- | --- |
| `NumPlatforms` | Number of truth platforms |
| `Platforms` | Array of truth platform structures |

Each platform structure has these fields:

| Field | Definition |
| --- | --- |
| `PlatformID` | Unique identifier used to distinguish platforms, specified as a nonnegative integer. |
| `Position` | Position of the platform, specified as an *M*-element vector, where *M* is the dimension of the position state. For example, *M* = 3 for 3-D position. |
| `Velocity` | Velocity of the platform, specified as an *M*-element vector, where *M* is the dimension of the velocity state. For example, *M* = 3 for 3-D velocity. |

If you specify the **Truth bus** parameter as
`Actor`, the structure must
use this form:

| Field | Description |
| --- | --- |
| `NumActors` | Number of truth actors |
| `Actors` | Array of truth actor structures |

Each actor structure has these fields:

| Field | Definition |
| --- | --- |
| `ActorID` | Unique identifier used to distinguish actors, specified as a nonnegative integer. |
| `Position` | Position of the actor, specified as an *M*-element vector, where *M* is the dimension of the position state. For example, *M* = 3 for 3-D position. |
| `Velocity` | Velocity of the actor, specified as an *M*-element vector, where *M* is the dimension of the velocity state. For example, *M* = 3 for 3-D velocity. |

If you specify the **Truth bus** parameter to
`custom`, then you can define your own truth bus format. In this
case, you must define a truth extractor function using the **Truth extractor
function** parameter. The function must use this
syntax:

```
 truths = truthExtractorFcn(truthInputFromBus)
```

where
`truthInputFromBus` is the input from the truth bus and
`truths` must return as an array of structures with
`PlatformID`, `Position`, and `Velocity`
fields.

### **Assignments** — Known assignment *K*-by-2 matrix of nonnegative integers

Known assignment, specified as an *K*-by-2 matrix of nonnegative
integers. *K* is the number of assignment pairs. The first column
elements are track IDs, and the second column elements are truth IDs. The IDs in the
same row are assigned to each other. If a track or truth is not assigned, specify
`0` as the same row element.

The assignment must be a unique assignment between tracks and truths. Redundant or
false tracks should be treated as unassigned tracks by assigning them to the "0"
`TruthID`.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Assignments**.
### Output

### **GOSPA Metric** — GOSPA metric including switching error component nonnegative real scalar

GOSPA metric including switching error component, returned as a nonnegative real
scalar.

### **GOSPA Metric Without Switching** — GOSPA metric without switching error component nonnegative real scalar

GOSPA metric without switching error component, returned as a nonnegative real
scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**GOSPA metric without switching error component**.

### **Switching Error** — Switching error component nonnegative real scalar

Switching error component, returned as a nonnegative real scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Switching error**.

### **Localization Error** — Localization error component nonnegative real scalar

Localization error component, returned as a nonnegative real scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Localization error**.

### **Missed Target Error** — Missed target error component nonnegative real scalar

Missed target error component, returned as a nonnegative real scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Missed target error**.

### **False Track Error** — False track error component nonnegative real scalar

False track error component, returned as a nonnegative real scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**False track error**.
## Parameters
```yaml
parameters:
- name: Cutoff distance
  summary: Threshold for cutoff distance between track and truth 30 (default) | real positive scalar
  group: ''
- name: Order
  summary: Order of GOSPA metric 2 (default) | positive integer
  group: ''
- name: Alpha
  summary: Alpha parameter of GOSPA metric 2 (default) | positive scalar in range [0, 2]
  group: ''
- name: Distance type
  summary: Distance type posnees (default) | velnees | posabserr | velabserr | custom
  group: ''
- name: Custom distance function
  summary: Custom distance function function handle
  group: ''
- name: Motion model
  summary: Desired platform motion model constvel (default) | constacc | constturn | singer
  group: ''
- name: Switching penalty
  summary: Penalty for assignment switching 0 (default) | nonnegative real scalar
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code Generation
  group: ''
- name: Assignments
  summary: Enable assignment input off (default) | on
  group: ''
- name: GOSPA metric without switching error
  summary: Enable GOSPA metric without switching error output off (default) | on
  group: ''
- name: Switching error
  summary: Enable switching error component output off (default) | on
  group: ''
- name: Localization error
  summary: Enable localization error component output off (default) | on
  group: ''
- name: Missed target error
  summary: Enable missed target error component output off (default) | on
  group: ''
- name: False track error
  summary: Enable false track error component output off (default) | on
  group: ''
- name: Track bus
  summary: Track bus selection objectTrack (default) | custom
  group: ''
- name: Truth bus
  summary: Truth bus selection Platform (default) | Actor | custom
  group: ''
- name: Track extractor function
  summary: Track extractor function function handle
  group: ''
- name: Truth extractor function
  summary: Truth extractor function function handle
  group: ''
```

#### Properties

### **Cutoff distance** — Threshold for cutoff distance between track and truth `30` (default) | real positive scalar

Threshold for cutoff distance between track and truth, specified as a real positive
scalar. If the computed distance between a track and the assigned truth is higher than
the threshold, the actual distance incorporated in the metric is reduced to the
threshold.

**Example:** `40`

### **Order** — Order of GOSPA metric `2` (default) | positive integer

Order of GOSPA metric, specified as a positive integer.

**Example:**
`10`

### **Alpha** — Alpha parameter of GOSPA metric `2` (default) | positive scalar in range [0, 2]

Alpha parameter of the GOSPA metric, specified as a positive scalar in the range [0,
2].

**Example:**
`1`

### **Distance type** — Distance type `posnees` (default) | `velnees` | `posabserr` | `velabserr` | `custom`

Distance type, specified as `posnees`, `velnees`,
`posabserr`, or `velabserr`. The distance type
specifies the physical quantity used for distance calculations:

- `posnees` – Normalized estimation error squared (NEES) of
  track position
- `velnees` – NEES error of track velocity
- `posabserr` – Absolute error of track position
- `velabserr` – Absolute error of track velocity
- `custom` – Custom distance error

If you specify it as `custom`, you must also specify the distance
function in the **Custom distance function** parameter.

### **Custom distance function** — Custom distance function function handle

Custom distance function, specified as a function handle. The function must support
the following syntax:

```
d = myCustomFcn(Track,Truth)
```

where
`Track` is a structure for track information,
`Truth` is a structure of truth information, and `d`
is the distance between the truth and the track. See `objectTrack` for an example on how
to organize track information.

**Example:**
`@myCustomFcn`

#### Dependencies

To enable this property, set the **Distance type** parameter to
`custom`.

### **Motion model** — Desired platform motion model `constvel` (default) | `constacc` | `constturn` | `singer`

Desired platform motion model, specified as `constvel`,
`constacc`, `constturn`, or
`singer`. This property selects the motion model used by the
**Tracks** input port.

The motion models expect the `State` field of the track structure
to have a column vector containing these values:

- `constvel` — Position is in elements [1 3 5], and velocity is in
  elements [2 4 6].
- `constacc` — Position is in elements [1 4 7], velocity is in
  elements [2 5 8], and acceleration is in elements [3 6 9].
- `constturn` — Position is in elements [1 3 6], velocity is in
  elements [2 4 7], and yaw rate is in element 5.
- `singer` — Position is in elements [1 4 7], velocity is in
  elements [2 5 8], and acceleration is in elements [3 6 9].

The `StateCovariance` field of the track structure input
must have position, velocity, and turn-rate covariances in the rows and columns
corresponding to the position, velocity, and turn-rate of the `State`
field of the track structure.

### **Switching penalty** — Penalty for assignment switching `0` (default) | nonnegative real scalar

Penalty for assignment switching, specified as a nonnegative real scalar.

**Example:**
`2`

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code Generation`

Select a simulation type from these options:

- `Interpreted execution` — Simulate the model using the MATLAB interpreter. This option shortens startup time. In `Interpreted execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent simulations as long as the model does not change. This option requires additional startup time.

#### Port Setting

### **Assignments** — Enable assignment input `off` (default) | `on`

Select this parameter to enable the input of know assignments through the
**Assignments** input port.

### **GOSPA metric without switching error** — Enable GOSPA metric without switching error output `off` (default) | `on`

Select this parameter to enable the output of the GOSPA metric without the switching
error component through the **GOSPA Metric Without Switching** output
port.

### **Switching error** — Enable switching error component output `off` (default) | `on`

Select this parameter to enable the output of the switching error component through
the **Switching Error** output port.

### **Localization error** — Enable localization error component output `off` (default) | `on`

Select this parameter to enable the output of the localization error component
through the **Localization Error** output port.

### **Missed target error** — Enable missed target error component output `off` (default) | `on`

Select this parameter to enable the output of the missed target error component
through the **Missed Target Error** output port.

### **False track error** — Enable false track error component output `off` (default) | `on`

Select this parameter to enable the output of the false track error component
through the **False Track Error** output port.

### **Track bus** — Track bus selection `objectTrack` (default) | `custom`

Track bus selection, specified as `objectTrack` or
`custom`. See the description of the **Tracks**
input port for more details about each selection.

### **Truth bus** — Truth bus selection `Platform` (default) | `Actor` | `custom`

Truth bus selection, specified as `Platform`,
`Actor`, or `custom`. See the
description of the **Truths** input port for more details about each
selection.

### **Track extractor function** — Track extractor function function handle

Track extractor function, specified as a function handle. The function must support this
syntax:

```
tracks = trackExtractorFcn(trackInputFromBus)
```

where
`trackInputFromBus` is the input from the track bus and
`tracks` must return as an array of structures with
`TrackID` and `State` fields. If you specify an
NEES-based distance (`posnees` or `velnees`) in the
**Distance type** parameter, then the structure must contain a
`StateCovariance` field.

**Example:**  `@myCustomFcn`

#### Dependencies

To enable this property, set the **Track bus** parameter to `custom`.

### **Truth extractor function** — Truth extractor function function handle

Truth extractor function, specified as a function handle. The function must support
this
syntax:

```
 truths = truthExtractorFcn(truthInputFromBus)
```

where
`truthInputFromBus` is the input from the track bus and
`truths` must return as an array of structures with
`PlatformID`, `Position`, and
`Velocity` as field names.

**Example:**
`@myCustomFcn`

#### Dependencies

To enable this property, set the **Truth bus** parameter to
`custom`.
## Libraries

Sensor Fusion and Tracking Toolbox / Track Metrics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Calculate Generalized Optimal Subpattern Assignment Metric

The Generalized Optimal Subpattern Assignment Metric block evaluates the performance of a tracking algorithm by
computing the generalized optimal subpattern assignment (GOSPA) metric between tracks and
known truths. The metric is comprised of the switching error, localization error, missed
target error, and false track error components. You can also select each individual error
components as a block output.
