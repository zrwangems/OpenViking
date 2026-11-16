---
type: simulink-block
title: 'Optimal Subpattern Assignment Metric'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Track Metrics'
documentation_page: 'optimalsubpatternassignmentmetric'
documentation_source_path: 'ref/optimalsubpatternassignmentmetric.html'
language: en
---

# Optimal Subpattern Assignment Metric

## Ports

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

Known assignment, specified as a*K*-by-2 matrix of nonnegative
integers. *K* is the number of assignment pairs. The first column
elements are track IDs, and the second column elements are truth IDs. The two IDs in a
row are assigned to each other. If a track or truth is not assigned, specify
`0` as the other element in the row.

Assignments between tracks and truths must be unique. Redundant or false tracks
should be treated as unassigned tracks by assigning them to the "`0`"
`TruthID`.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Assignments**.
### Output

### **OSPA Metric** — OSPA metric nonnegative real scalar

OSPA metric, returned as a nonnegative real scalar. Depending on the values of the
**Metric** and **Labeling error** parameters, the
block can output traditional OSPA, labeled OSPA (LOSPA), or
OSPA(2).

| **Metric** Parameter Value | **Labeling error** Parameter Value | Metric |
| --- | --- | --- |
| `OSPA` | `0` | OSPA |
| `OSPA` | Positive scalar | LOSPA |
| `OSPA(2)` | Not applicable | OSPA(2) |

**Example:** 10.1

### **Localization Error** — Localization error component nonnegative real scalar

Localization error component, returned as a nonnegative real scalar.

**Example:** 8.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Localization error**.

### **Cardinality Error** — Cardinality error component nonnegative real scalar

Cardinality error component, returned as a nonnegative real scalar.

**Example:** 6

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Cardinality error**.

### **Labeling Error** — Labeling error component nonnegative real scalar

Labeling error component, returned as a nonnegative real scalar.

**Example:** 7.5

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Labeling error**.

## Parameters

#### Properties

### **Metric** — Metric option `OPSA` (default) | `OSPA(2)`

Metric option, specified as `OSPA` or `OSPA(2)`.

- `OSPA` — Computes the traditional OSPA metric by default, or
  computes the labeled OSPA metric after additionally specifying the
  **Labeling error** parameter as a positive value.
- `OSPA(2)` — Computes the OSPA(2)
  metric, which evaluates cumulative tracking performance. Selecting this option
  enables these parameters for configuring the metric:

  - **Window length**
  - **Window sum order (q)**
  - **Window weights**
  - **Window weight exponent (r)**
  - **Custom window weights**

  Selecting this option also disables two parameters used to evaluate
  the labeling error component:

  - **Assignments**
  - **Labeling error**

### **Cutoff distance** — Threshold for cutoff distance between track and truth `30` (default) | real positive scalar

Threshold for the cutoff distance between track and truth, specified as a real
positive scalar. If the computed distance between a track and the assigned truth is
higher than the threshold, the actual distance incorporated in the metric is reduced to
the threshold.

**Example:** `40`

### **Order** — Order of OSPA metric `2` (default) | positive integer

Order of the OSPA metric, specified as a positive integer.

**Example:**
`3`

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

If you select `custom`, you must also specify a distance function
in the **Custom distance function** parameter.

### **Custom distance function** — Custom distance function function handle

Custom distance function, specified as a function handle. The function must support
the following syntax:

```
d = myCustomFcn(Track,Truth)
```

where
`Track` is a structure of track information, `Truth`
is a structure of truth information, and `d` is the distance between
the truth and the track. See `objectTrack` for an example on how
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

### **Labeling error** — Penalty for incorrect assignment `0` (default) | nonnegative scalar

Penalty for incorrect assignment of track to truth, specified as a nonnegative
scalar. The function decides if an assignment is correct based on the provided known
assignment input from the **Assignments** input port. If the assignment
is not provided as an input, the last known assignment is assumed to be correct.

**Example:**
`5`

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA`.

### **Window length** — Sliding window length for OSPA(2) metric `100` (default) | positive integer

Sliding window length for the OSPA(2) metric, specified
as a positive integer. The window length defines the number of time steps from a
previous time to the current time used to evaluate the metric. For more details, see
OSPA(2) Metric.

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA(2)`.

**Data Types:** `single` | `double`

### **Window sum order (q)** — Order of weighted sum for track and truth history `2` (default) | positive scalar

Order of weighted sum for the track and truth history, specified as a positive
scalar. For more details, see OSPA(2) Metric.

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA(2)`.

**Data Types:** `single` | `double`

### **Window weights** — Options for window weights `auto` (default) | `custom`

Options for window weights, specified as `auto` or
`custom`.

- `auto` — Automatically generates the window weights using the
  algorithm given in OSPA(2) Metric.
- `custom` — Customizes the window weights using the
  **Custom window weights** parameter.

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA(2)`.

**Data Types:** `single` | `double`

### **Window weight exponent (r)** — Exponent for automatic weight calculation `1` (default) | nonnegative scalar

Exponent for automatic weight calculation, specified as a nonnegative scalar. An
exponent value, *r*, of `0` represents equal weights
in the window. A higher value of *r* assigns more weights on recent
data. For more details, see OSPA(2) Metric.

#### Dependencies

To enable this parameter, set the **Window weights** parameter to
`auto`.

**Data Types:** `single` | `double`

### **Custom window weights** — Custom weights in time window *N*-element of vector of nonnegative values

Custom weights in the time window, specified as an *N*-element of
vector of nonnegative values, when *N* is the window length, specified
in the **Window length** parameter.

#### Dependencies

To enable this parameter, set the **Window weights** parameter to
`custom`.

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code Generation`

Select a simulation type from these options:

- `Interpreted execution` — Simulate the model using the MATLAB interpreter. This option shortens startup time. In `Interpreted execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent simulations as long as the model does not change. This option requires additional startup time.

#### Port Setting

### **Assignments** — Enable assignment input `off` (default) | `on`

Select this parameter to enable the input of known assignments through the
**Assignments** input port.

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA`.

### **Localization error** — Enable localization error component output `off` (default) | `on`

Select this parameter to enable the output of the localization error component
through the **Localization Error** output port.

### **Cardinality error** — Enable cardinality error component output `off` (default) | `on`

Select this parameter to enable the output of the cardinality error component
through the **Cardinality Error** output port.

### **Labeling error** — Enable labeling error component output `off` (default) | `on`

Select this parameter to enable the output of the labeling error component through
the **Labeling Error** output port.

#### Dependencies

To enable this parameter, set the **Metric** parameter to
`OSPA`.

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

Calculate Optimal Subpattern Assignment Metric

The Optimal Subpattern Assignment Metric block computes the optimal subpattern assignment metric
between a set of tracks and known truths. You can enable different types of OSPA metrics by
configuring these parameters:

- Traditional OSPA — Specify the **Metric** parameter as
  `OSPA` and specify the **Labeling error** parameter,
  on the **Properties** tab, as `0`. The traditional
  OSPA metric, which evaluates instantaneous tracking performance, contains two components:

  - Localization error component — Accounts for state estimation errors between
    assigned tracks and truths.
  - Cardinality error component— Accounts for the number of unassigned tracks and
    truths.
- Labeled OSPA — Specify the **Metric** parameter as
  `OSPA` and specify the **Labeling error** parameter,
  on the **Properties** tab, as a positive scalar. The labeled OSPA
  (LOSPA) metric, which evaluates instantaneous tracking performance and includes
  penalties for incorrect assignments, contains three components:

  - Localization error component — Accounts for state estimation errors between
    assigned tracks and truths.
  - Cardinality error component— Accounts for the number of unassigned tracks and
    truths.
  - Labelling error component — Accounts for the error of incorrect
    assignments.
- OSPA(2) — Specify the **Metric**
  parameter as `OSPA(2)`. The OSPA(2) metric
  evaluates cumulative tracking performance for a duration of time.

You can output each component individually from the block. For more details on
the algorithm, see Algorithm and References.
