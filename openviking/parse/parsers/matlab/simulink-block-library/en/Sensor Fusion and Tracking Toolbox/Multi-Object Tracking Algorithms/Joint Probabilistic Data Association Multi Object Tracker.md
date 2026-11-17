---
type: simulink-block
title: 'Joint Probabilistic Data Association Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'jointprobabilisticdataassociationmultiobjecttracker'
documentation_source_path: 'ref/jointprobabilisticdataassociationmultiobjecttracker.html'
language: en
---

# Joint Probabilistic Data Association Multi Object Tracker

## Ports
```yaml
ports:
- name: Detections
  summary: Detection list Simulink® bus containing MATLAB® structure
  direction: input
- name: Prediction Time
  summary: Track update time real scalar
  direction: input
- name: Cost Matrix
  summary: Cost matrix real-valued *N*t-by-*N*d matrix
  direction: input
- name: Detectable TrackIDs
  summary: Detectable track IDs real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix
  direction: input
- name: State Parameters
  summary: Track state parameters Simulink bus containing MATLAB structure
  direction: input
- name: Confirmed Tracks
  summary: Confirmed tracks Simulink bus containing MATLAB structure
  direction: output
- name: Tentative Tracks
  summary: Tentative tracks Simulink bus containing MATLAB structure
  direction: output
- name: All Tracks
  summary: Confirmed and tentative tracks Simulink bus containing MATLAB structure
  direction: output
- name: Info
  summary: Additional information for analyzing track updates Simulink bus containing MATLAB structure
  direction: output
```

### Input

### **Detections** — Detection list Simulink® bus containing MATLAB® structure

Detection list, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Integer |
| `Detections` | Object detections | Array of `objectDetection` structures. The first `NumDetections` of these detections are actual detections. |

The fields of detections are:

| Field | Description | Type |
| --- | --- | --- |
| `Time` | Measurement time | `Single` or `Double` |
| `Measurement` | Object measurements | `Single` or `Double` |
| `MeasurementNoise` | Measurement noise covariance matrix | `Single` or `Double` |
| `SensorIndex` | Unique ID of the sensor | `Single` or `Double` |
| `ObjectClassID` | Object classification ID | `Single` or `Double` |
| `MeasurementParameters` | Parameters used by initialization functions of tracking filters | Simulink Bus |
| `ObjectAttributes` | Additional information passed to tracker | Simulink Bus |

See `objectDetection` for more detailed
explanation of these fields.

**Note**

The object detection structure contains a `Time` field. The
time tag of each object detection must be less than or equal to the time of the
current invocation of the block. The time tag must also be greater than the update
time specified in the previous invocation of the block.

### **Prediction Time** — Track update time real scalar

Track update time, specified as a real scalar in seconds. The tracker updates all
tracks to this time. The update time must always increase with each invocation of the
block. The update time must be at least as large as the largest
`Time` specified in the **Detections** input
port.

If the port is not enabled, the simulation clock managed by Simulink determines
the update time.

#### Dependencies

To enable this port, on the **Port Setting** tab, set
**Prediction time source** to `Input
port`.

### **Cost Matrix** — Cost matrix real-valued *N*t-by-*N*d matrix

Cost matrix, specified as a real-valued
*N*t-by-*N*d
matrix, where *N*t is the number of existing
tracks and *N*d is the number of current
detections.

The rows of the cost matrix correspond to the existing tracks. The columns
correspond to the detections. Tracks are ordered as they appear in the list of tracks
from the **All Tracks** output port on the previous invocation of the
block.

In the first update to the tracker, or if the tracker has no previous tracks,
assign the cost matrix a size of [0, *N*d].
The cost must be calculated so that lower costs indicate a higher likelihood that the
tracker assigns a detection to a track. To prevent certain detections from being
assigned to certain tracks, use `Inf`.

If this port is not enabled, the filter initialized by the **Filter
initialization function** calculates the cost matrix using the distance
method.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable cost matrix input**.

### **Detectable TrackIDs** — Detectable track IDs real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix

Detectable track IDs, specified as a real-valued *M*-by-1 vector
or *M*-by-2 matrix. Detectable tracks are tracks that the sensors
expect to detect. The first column of the matrix contains a list of track IDs that the
sensors report as detectable. The optional second column enables you to add the
detection probability for each track.

Tracks whose identifiers are not included in **Detectable
TrackIDs** are considered undetectable. The track deletion logic does not
count the lack of detection as a "missed detection" for track deletion
purposes.

If this port is not enabled, the tracker assumes all tracks to be detectable at
each invocation of the block.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable detectable track IDs Input**.

### **State Parameters** — Track state parameters Simulink bus containing MATLAB structure

Track state parameters, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumParameters` | Number of non-default state parameters, specified as a nonnegative integer |
| `Parameters` | Array of state parameter structures |

The block uses the value of the `Parameters` field for the
`StateParameters` field of the generated tracks. You can use
these parameters to define the reference frame in which the track is reported or other
desirable attributes of the generated tracks.

For example, you can use the following structure to define a rectangular reference
frame whose origin position is at `[10 10 0]` meters and whose origin
velocity is `[2 -2 0]` meters per second with respect to the scenario
frame.

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### Dependencies

To enable this port, in the **Tracker Configuration** tab, select
the **Update track state parameters with time** parameter.
### Output

### **Confirmed Tracks** — Confirmed tracks Simulink bus containing MATLAB structure

Confirmed tracks, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

The fields of the track structure are shown in Track Structure.

Depending on the track logic, a track is confirmed if:

- History – A track receives at least `M` detections in the
  last `N` updates. `M` and `N`
  are specified in **Confirmation threshold** for the
  `History` logic.
- Integrated – The integrated probability of track existence is higher than
  the confirmation threshold specified in **Confirmation
  threshold** for the `Integrated` logic.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks, returned as a Simulink bus containing a MATLAB structure. A track is tentative before it is confirmed.

The fields of the track structure are shown in Track Structure.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable tentative tracks output**.

### **All Tracks** — Confirmed and tentative tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks, returned as a Simulink bus containing a MATLAB structure.

The fields of the track structure are shown in Track Structure.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable all tracks output**.

### **Info** — Additional information for analyzing track updates Simulink bus containing MATLAB structure

Additional information for analyzing track updates, returned as a Simulink bus containing a MATLAB structure.

This table shows the fields of the info structure:

|  |  |
| --- | --- |
| **Field** | **Description** |
| `OOSMDetectionIndices` | Indices of out-of-sequence measurements at the current step of the tracker |
| `TrackIDsAtStepBeginning` | Track IDs when step began. |
| `CostMatrix` | Cost of kinematic assignment matrix, in which the (*i*, *j*) element denotes the cost of assigning track *i* to detection *j*. |
| `Clusters` | Cell array of cluster reports. See Feasible Joint Events for more details. |
| `InitiatedTrackIDs` | IDs of tracks initiated during the step. |
| `DeletedTrackIDs` | IDs of tracks deleted during the step. |
| `TrackIDsAtStepEnd` | Track IDs when the step ended. |
| `MaxNumDetectionsPerCluster` | The maximum number of detections in all the clusters generated during the step. The structure has this field only when you set the **Enable memory management** parameters as `on`. |
| `MaxNumTracksPerCluster` | The maximum number of tracks in all the clusters generated during the step. The structure has this field only when you set the **Enable memory management** parameters as `on`. |
| `OOSMHandling` | Analysis information for out-of-sequence measurements handling, returned as a structure. The structure has this field only when the `Out-of-sequence measurement handling` parameter is specified as `Retordiction`. |

The `Clusters` field can include multiple cluster reports. Each
cluster report is a structure containing:

|  |  |
| --- | --- |
| **Field** | **Description** |
| `DetectionIndices` | Indices of clustered detections. |
| `TrackIDs` | Track IDs of clustered tracks. |
| `ValidationMatrix` | Validation matrix of the cluster. See Feasible Joint Events for more details. |
| `SensorIndex` | Index of the originating sensor of the clustered detections. |
| `TimeStamp` | Mean time stamp of clustered detections. |
| `MarginalProbabilities` | Matrix of marginal posterior joint association probabilities. |

The `OOSMHandling` structure contains these fields:

| Field | Description |
| --- | --- |
| `DiscardedDetections` | Indices of discarded out-of-sequence detections. An OOSM is discarded if it is not covered by the saved state history specified by the **Maximum number of OOSM steps** parameter. |
| `CostMatrix` | Cost of assignment matrix for the out-of-sequence detections. |
| `Clusters` | Clusters that are only related to the out-of-sequence detections. |
| `UnassignedDetections` | Indices of unassigned out-of-sequence detections. The tracker creates new tracks for unassigned out-of-sequence detections. |

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable information output**.
## Parameters
```yaml
parameters:
- name: Tracker identifier
  summary: Unique tracker identifier 0 (default) | nonnegative integer
  group: ''
- name: Filter initialization function
  summary: Filter initialization function initcvekf (default) | function name
  group: ''
- name: Value of k for k-best JPDA
  summary: Value of k for k-best JPDA inf (default) | positive integer
  group: ''
- name: Feasible joint events generation function name
  summary: Feasible joint events generation function name jpdaEvents (default) | function name
  group: ''
- name: Maximum number of tracks
  summary: Maximum number of tracks 100 (default) | positive integer
  group: ''
- name: Maximum number of sensors
  summary: Maximum number of sensors 20 (default) | positive integer
  group: ''
- name: Absolute tolerance between time stamps of detections
  summary: Absolute tolerance between time stamps of detections 20 (default) | positive integer
  group: ''
- name: Out-of-sequence measurements handling
  summary: Out-of-sequence measurements handling Terminate (default) | Neglect | Retrodiction
  group: ''
- name: Maximum number of OOSM steps
  summary: Maximum number of OOSM steps 3 (default) | positive integer
  group: ''
- name: Track state parameters
  summary: Parameters of track state reference frame structure | structure array
  group: ''
- name: Update track state parameters with time
  summary: Update track state parameters with time off (default) | on
  group: ''
- name: Enable memory management
  summary: Enable memory management off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted Execution (default) | Code Generation
  group: ''
- name: Threshold for assigning detections to tracks
  summary: Threshold for assigning detections to tracks 30*[1 Inf] (default) | positive scalar | 1-by-2 vector of positive
    values
  group: ''
- name: Threshold to initialize a track
  summary: Threshold to initialize a track 0 (default) | scalar in the range [0, 1]
  group: ''
- name: Probability of detection
  summary: Probability of detection 0.9 (default) | scalar in the range [0, 1]
  group: ''
- name: Spatial density of clutter measurements
  summary: Spatial density of clutter measurements 1e-5 (default) | positive scalar
  group: ''
- name: Type of track confirmation and deletion logic
  summary: Confirmation and deletion logic type History (default) | Integrated
  group: ''
- name: Confirmation threshold [M N]
  summary: Track confirmation threshold for history logic [2, 3] (default) | real-valued 1-by-2 vector of positive integers
  group: ''
- name: Deletion threshold [P Q]
  summary: Track deletion threshold for history logic [5, 5] (default) | real-valued 1-by-2 vector of positive integers
  group: ''
- name: Threshold for registering 'hit' or 'miss'
  summary: Threshold for registering a 'Hit' or a 'Miss' 0.2 (default) | scalar in the range [0, 1]
  group: ''
- name: Confirmation threshold [Probability]
  summary: Track confirmation threshold for integrated logic 0.95 (default) | positive scalar
  group: ''
- name: Deletion threshold [Probability]
  summary: Track deletion threshold for integrated logic 0.1 (default) | positive scalar
  group: ''
- name: Spatial density of new targets
  summary: Spatial density of new targets 1e-5 (default) | positive scalar
  group: ''
- name: Time rate of true target deaths
  summary: Time rate of true target deaths 0.01 (default) | scalar in the range [0, 1]
  group: ''
- name: Prediction time source
  summary: Source of prediction time Auto (default) | Input port
  group: ''
- name: Enable cost matrix input
  summary: Enable input port for cost matrix off (default) | on
  group: ''
- name: Enable detectable track IDs input
  summary: Enable detectable track IDs input off (default) | on
  group: ''
- name: Enable tentative tracks output
  summary: Enable output port for tentative tracks off (default) | on
  group: ''
- name: Enable all tracks output
  summary: Enable output port for all tracks off (default) | on
  group: ''
- name: Enable information output
  summary: Enable output port for analysis information off (default) | on
  group: ''
- name: Source of output bus name
  summary: Source of output track bus name Auto (default) | Property
  group: ''
- name: Source of output info bus name
  summary: Source of output info bus name Auto (default) | Property
  group: ''
- name: Maximum number of detections per sensor
  summary: Maximum number of detections per sensor 100 (default) | positive integer
  group: ''
- name: Maximum number of detections per cluster
  summary: Maximum number of detections per cluster 5 (default) | positive integer
  group: ''
- name: Maximum number of tracks per cluster
  summary: Maximum number of tracks per cluster 5 (default) | positive integer
  group: ''
- name: Handle run-time violation of cluster size
  summary: Handle run-time violation of cluster size Auto (default) | Property
  group: ''
```

#### Tracker Management

### **Tracker identifier** — Unique tracker identifier `0` (default) | nonnegative integer

Specify the unique tracker identifier as a nonnegative integer. This parameter is
passed as the `SourceIndex` in the tracker outputs, and distinguishes
tracks that come from different trackers in a multiple-tracker system. You must specify
this property as a positive integer to use the track outputs as inputs to a Track-To-Track Fuser
block.

**Example:** `1`

### **Filter initialization function** — Filter initialization function `initcvekf` (default) | function name

Filter initialization function, specified as the function name of a valid filter
initialization function. The tracker uses the filter initialization function when
creating new tracks.

Sensor Fusion and Tracking Toolbox™ supplies many initialization functions:

| Initialization Function | Function Definition |
| --- | --- |
| `initcvkf` | Initialize constant-velocity linear Kalman filter. |
| `initcakf` | Initialize constant-acceleration linear Kalman filter. |
| `initcvabf` | Initialize constant-velocity alpha-beta filter |
| `initcaabf` | Initialize constant-acceleration alpha-beta filter |
| `initcvekf` | Initialize constant-velocity extended Kalman filter. |
| `initcaekf` | Initialize constant-acceleration extended Kalman filter. |
| `initrpekf` | Initialize constant-velocity range-parametrized extended Kalman filter. |
| `initapekf` | Initialize constant-velocity angle-parametrized extended Kalman filter. |
| `initctekf` | Initialize constant-turn-rate extended Kalman filter. |
| `initcackf` | Initialize constant-acceleration cubature filter. |
| `initctckf` | Initialize constant-turn-rate cubature filter. |
| `initcvckf` | Initialize constant-velocity cubature filter. |
| `initcvukf` | Initialize constant-velocity unscented Kalman filter. |
| `initcaukf` | Initialize constant-acceleration unscented Kalman filter. |
| `initctukf` | Initialize constant-turn-rate unscented Kalman filter. |
| `initcvmscekf` | Initialize constant-velocity extended Kalman filter in modified spherical coordinates. |
| `initekfimm` | Initialize tracking IMM filter. |

You can also write your own initialization function using this
syntax:

```
filter = filterInitializationFcn(detection)
```

The
input to this function is a detection report like those created by `objectDetection`. The output of this function must be a filter object:
`trackingKF`, `trackingEKF`, `trackingUKF`, `trackingCKF`,
`trackingGSF`,
`trackingIMM`,
`trackingMSCEKF`, or `trackingABF`.

For guidance in writing this function, use the `type` command to
examine the details of built-in MATLAB
functions. For example:

```
type initcvekf
```

**Note**

The block does not accept all filter initialization functions in Sensor Fusion and Tracking Toolbox. The full list of filter initialization functions available in
Sensor Fusion and Tracking Toolbox are given in the **Initialization** section of Estimation Filters.

### **Value of k for k-best JPDA** — Value of k for k-best JPDA `inf` (default) | positive integer

Value of k for k-best JPDA, specified as a positive integer. This parameter defines
the maximum number of feasible joint events for the track and detection association of
each cluster. Setting this property to a finite value enables you to run a k-best JPDA
tracker, which generates a maximum of k events per cluster.

### **Feasible joint events generation function name** — Feasible joint events generation function name `jpdaEvents` (default) | function name

Feasible joint events generation function name, specified as the name of a feasible
joint events generation function. A generation function generates feasible joint event
matrices from an association likelihood matrix between tracks and detections. For
details, see `jpdaEvents`

To write your own generation function, you must use this
syntax.

```
[FJE,FJEProbs] = myfunction(likelihoodMatrix,k)
```

The
input and output arguments of this function must be the same as the arguments in
`jpdaEvents`.

You can use the `type` command to examine the details of
`jpdaEvents`.

```
type jpdaEvents
```

**Example:**
`myfunction`

### **Maximum number of tracks** — Maximum number of tracks `100` (default) | positive integer

Maximum number of tracks that the block can maintain, specified as a positive
integer.

### **Maximum number of sensors** — Maximum number of sensors `20` (default) | positive integer

Maximum number of sensors that the block can process, specified as a positive
integer. This value should be greater than or equal to the highest
`SensorIndex` value input at the **Detections**
input port.

### **Absolute tolerance between time stamps of detections** — Absolute tolerance between time stamps of detections `20` (default) | positive integer

Absolute time tolerance between detections for the same sensor, specified as a
positive scalar. The block expects detections from a sensor to have identical time
stamps. However, if the time stamp differences between detections of a sensor are within
the margin specified by this parameter, these detections will be used to update the
track estimate based on the average time of these detections.

### **Out-of-sequence measurements handling** — Out-of-sequence measurements handling `Terminate` (default) | `Neglect` | `Retrodiction`

Out-of-sequence measurements handling, specified as
`Terminate`, `Neglect`, or
`Retrodiction`. Each detection has an associated timestamp,
*t*d, and the tracker block has it own
timestamp, *t*t, which is updated in each
invocation. The tracker block considers a measurement as an OOSM if
*t*d <
*t*t.

When you specify the parameter as:

- `Terminate` — The block stops running when it
  encounters an out-of-sequence measurement.
- `Neglect` — The block neglects any out-of-sequence
  measurements and continues to run.
- `Retrodiction` — The block uses a retrodiction
  algorithm to update the tracker by either neglecting the OOSMs, updating existing
  tracks, or creating new tracks using the OOSMs. You must specify a filter
  initialization function that returns a `trackingKF`, `trackingEKF`, or `trackingIMM` object in the **Filter initialization
  function** parameter.

If you specify this parameter as `Retrodiction`,
the tracker follows these steps to handle the OOSM:

- If the OOSM timestamp is beyond the oldest correction timestamp (specified by
  the **Maximum number of OOSM steps** parameter) maintained in the
  tracker, the tracker discards the OOSMs.
- If the OOSM timestamp is within the oldest correction timestamp by the
  tracker, the tracker first retrodicts all the existing tracks to the time of the
  OOSMs. Then, the tracker applies the joint probability data association algorithm
  to try to associate the OOSMs to the retrodicted tracks.

  - If the tracker successfully associates the OOSM to at least one
    retrodicted track, then the tracker updates the retrodicted tracks using the
    OOSMs by applying the retro-correction algorithm to obtain current,
    corrected tracks.
  - If the tracker cannot associate an OOSM to any retrodicted track, then
    the tracker creates a new track based on the OOSM and predicts the track to
    the current time.

For more details on JPDA-based retrodiction, see JPDA-Based Retrodiction and Retro-Correction.To simulate
out-of-sequence detections, use `objectDetectionDelay`.

**Note**

- When you select `Retrodiction`, you cannot use the Cost Matrix input.
- The benefits of using retrodiction decreases as the number of targets that
  move in close proximity increases.
- The tracker requires all input detections that share the same
  `SensorIndex` have their `Time` differences
  bounded by the **Absolute tolerance between time stamps of
  detections** parameter. Therefore, when you set the
  **Out-of-sequence measurements handling** parameter to
  `Neglect`, you must make sure that the out-of-sequence
  detections have timestamps strictly less than the previous timestamp when running
  the tracker.

### **Maximum number of OOSM steps** — Maximum number of OOSM steps `3` (default) | positive integer

Maximum number of out-of-sequence measurement (OOSMs) steps, specified as a positive
integer.

Increasing the value of this parameter requires more memory but allows you to call
the tracker block with OOSMs that have a larger lag relative to the last timestamp when
the block was updated. Also, as the lag increases, the impact of the OOSM on the current
state of the track diminishes. The recommended value of this parameter is
`3`.

#### Dependencies

To enable this parameter, set the **Out-of-sequence measurements
handling** parameter to `Retrodiction`.

### **Track state parameters** — Parameters of track state reference frame structure | structure array

Specify the parameters of the track state reference frame as a
structure or a structure array. The block passes the value of this parameter to the
`StateParameters` field of the generated tracks. You can use these
parameters to define the reference frame in which the track is reported or other desirable
attributes of the generated tracks.

For example, you can use the following structure to define a
rectangular reference frame whose origin position is at
`[10 10 0]` meters and whose origin
velocity is `[2 -2 0]` meters per second with
respect to the scenario frame.

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

You can update the track state parameters through the **State
Parameters** input port by selecting the
**Update track state parameters with
time** parameter.

**Data Types:** `struct`

### **Update track state parameters with time** — Update track state parameters with time `off` (default) | `on`

Select this parameter to enable the input port for track state
parameters through the **State
Parameters** input port.

### **Enable memory management** — Enable memory management `off` (default) | `on`

Select this parameter to enable memory management in the tracker. Once selected, you
can use these four parameters in the **Memory Management** tab to
specify bounds for certain variable-sized arrays in the tracker as well as determine how
the tracker handles cluster size violations:

- **Maximum number of detections per sensor**
- **Maximum number of detections per cluster**
- **Maximum number of tracks per cluster**
- **Handle run-time violation of cluster size**

Specifying bounds for variable-sized arrays allows you to manage the memory
footprint of the tracker in the generated C/C++ code.

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.

#### Assignment

### **Threshold for assigning detections to tracks** — Threshold for assigning detections to tracks `30*[1 Inf]` (default) | positive scalar | 1-by-2 vector of positive values

Threshold for assigning detections to tracks (or gating threshold), specified as a
positive scalar or 1-by-2 vector of
[*C*1*,C*2],
where *C*1 ≤
*C*2. If specified as a scalar, the specified
value, *val*, is expanded to [*val*,
`Inf`].

Initially, the tracker executes a coarse estimation for the normalized distance
between all the tracks and detections. The tracker only calculates the accurate
normalized distance for the combinations whose coarse normalized distance is less than
*C*2. Also, the tracker can only assign a
detection to a track if the accurate normalized distance between them is less than
*C*1. See Algorithms for an explanation
of the normalized distance.

- Increase the value of *C*2 if there are
  track and detection combinations that should be calculated for assignment but are
  not. Decrease this value if the cost calculation takes too much time.
- Increase the value of *C*1 if there are
  detections that should be assigned to tracks but are not. Decrease this value if
  there are detections that are assigned to tracks they should not be assigned to (too
  far away).

**Note**

If the value of *C*2 is finite, the state
transition function and measurement function, specified in the tracking filter used in
the tracker, must be able to take an *M*-by-*N*
matrix of states as input and output *N* predicted states and
*N* measurements, respectively. *M* is the size of
the state. *N*, the number of states, is an arbitrary nonnegative
integer.

### **Threshold to initialize a track** — Threshold to initialize a track `0` (default) | scalar in the range [0, 1]

The probability threshold to initialize a new track, specified as a scalar in the
range [0, 1]. If the probabilities of associating a detection with any of the existing
tracks are all smaller than `InitializationThreshold`, the detection
is used to initialize a new track. This allows detections that are within the validation
gate of a track but have an association probability lower than the initialization
threshold to spawn a new track.

**Example:** `0.1`

### **Probability of detection** — Probability of detection `0.9` (default) | scalar in the range [0, 1]

Probability of detection, specified as a scalar in the range [0, 1]. This property
is used in calculations of the marginal posterior probabilities of association and the
probability of track existence when initializing and updating a track.

### **Spatial density of clutter measurements** — Spatial density of clutter measurements `1e-5` (default) | positive scalar

Spatial density of clutter measurements, specified as a positive scalar. The clutter
density describes the expected number of false positive detections per unit volume. It
is used as the parameter of a Poisson clutter model. When **Type of track
confirmation and deletion logic** is set to
`'Integrated'`, this parameter is also used in calculating the
initial probability of track existence.

#### Track Logic

### **Type of track confirmation and deletion logic** — Confirmation and deletion logic type `History` (default) | `Integrated`

Confirmation and deletion logic type, selected as:

- `History` – Track confirmation and deletion is based on the
  number of times the track has been assigned to a detection in the latest tracker
  updates.
- `Integrated` – Track confirmation and deletion is based on
  the probability of track existence, which is integrated in the assignment
  function.

### **Confirmation threshold [M N]** — Track confirmation threshold for history logic `[2, 3]` (default) | real-valued 1-by-2 vector of positive integers

Track confirmation threshold for history logic, specified as a real-valued 1-by-2
vector of positive integers `[M N]`. A track is confirmed if it
receives at least `M` detections in the last `N`
updates.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'History'`.

### **Deletion threshold [P Q]** — Track deletion threshold for history logic `[5, 5]` (default) | real-valued 1-by-2 vector of positive integers

Track deletion threshold for history logic, specified as a real-valued 1-by-2 vector
of positive integers, `[P Q]`. If, in `P` of the last
`Q` tracker updates, a confirmed track is not assigned to any
detection that has a likelihood greater than the **Threshold for registering
'hit' or 'miss'** parameter, then that track is deleted.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'History'`.

### **Threshold for registering 'hit' or 'miss'** — Threshold for registering a 'Hit' or a 'Miss' `0.2` (default) | scalar in the range [0, 1]

Threshold for registering a 'hit' or 'miss', specified as a scalar in the range [0,
1]. The track history logic registers a 'miss' and the track will be coasted if the sum
of the marginal probabilities of assignments is below the
`HitMissThreshold`. Otherwise, the track history logic registers a
'hit'.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'History'`.

### **Confirmation threshold [Probability]** — Track confirmation threshold for integrated logic `0.95` (default) | positive scalar

Track confirmation threshold for integrated logic, specified as a real-valued
positive scalar. A track is confirmed if its probability of existence is greater than or
equal to the confirmation threshold.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'Integrated'`.

### **Deletion threshold [Probability]** — Track deletion threshold for integrated logic `0.1` (default) | positive scalar

Track deletion threshold for integrated logic, specified as a positive scalar. A
track is deleted if its probability of existence drops below this threshold.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'Integrated'`.

### **Spatial density of new targets** — Spatial density of new targets `1e-5` (default) | positive scalar

Spatial density of new targets, specified as a positive scalar. The new target
density describes the expected number of new tracks per unit volume in the measurement
space. It is used in calculating the probability of track existence during track
initialization.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'Integrated'`.

### **Time rate of true target deaths** — Time rate of true target deaths `0.01` (default) | scalar in the range [0, 1]

Time rate of true target deaths, specified as a scalar in the range [0, 1]. This
parameter describes the probability with which true targets disappear. It is related to
the propagation of the probability of track existence (*PTE*) :

PTE(t+δt)=(1−DeathRate)δtPTE(t)

where *DeathRate* is the time rate of true target
deaths, and *δt* is the time interval since the previous update time
*t*.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `'Integrated'`.

#### Port Setting

### **Prediction time source** — Source of prediction time `Auto` (default) | `Input port`

Source for prediction time, specified as `Input port` or
`Auto`. Select `Input port` to input
an update time by using the **Prediction Time** input port. Otherwise,
the simulation clock managed by Simulink determines the update time.

### **Enable cost matrix input** — Enable input port for cost matrix off (default) | on

Select this check box to enable the input of a cost matrix by using the
**Cost Matrix** input port.

### **Enable detectable track IDs input** — Enable detectable track IDs input off (default) | on

Select this check box to enable the **Detectable track IDs**  input
port.

### **Enable tentative tracks output** — Enable output port for tentative tracks off (default) | on

Select this check box to enable the output of tentative tracks through the
**Tentative Tracks** output port.

### **Enable all tracks output** — Enable output port for all tracks off (default) | on

Select this check box to enable the output of all the tracks through the
**All Tracks** output port.

### **Enable information output** — Enable output port for analysis information off (default) | on

Select this check box to enable the output port for analysis information through the
**Info** output port.

### **Source of output bus name** — Source of output track bus name `Auto` (default) | `Property`

Source of the output track bus name, specified as:

- `Auto` — The block automatically creates an output
  track bus name.
- `Property` — Specify the output track bus name by
  using the **Specify an output bus name** parameter.

### **Source of output info bus name** — Source of output info bus name `Auto` (default) | `Property`

Source of the output info bus name, specified as one of these options:

- `Auto` — The block automatically creates an output
  info bus name.
- `Property` — Specify the output info bus name by
  using the **Specify an output bus name** parameter.

#### Memory Management

### **Maximum number of detections per sensor** — Maximum number of detections per sensor `100` (default) | positive integer

Specify the maximum number of detections per sensor as a positive integer. This
parameter determines the maximum number of detections that each sensor can pass to the
tracker during one call of the tracker.

Set this parameter to a finite value if you want the tracker to establish efficient
bounds on local variables for C/C++ code generation. Set this property to
`Inf` if you do not want to bound the maximum number of detections
per sensor.

#### Dependencies

To enable this parameter, select **Enable Memory Management** in
the **Tracker Management** tab.

### **Maximum number of detections per cluster** — Maximum number of detections per cluster `5` (default) | positive integer

Specify the maximum number of detections per cluster during the run-time of the
tracker as a positive integer.

Setting this parameter to a finite value allows the tracker to bound cluster sizes
and reduces the memory footprint of the tracker in generated C/C++ code. Set this
property to `Inf` if you do not want to bound the maximum number of
detections per cluster.

If during run-time, the number of detections in a cluster exceeds this parameter,
the tracker reacts based on the **Handle run-time violation of cluster
size** parameter.

#### Dependencies

To enable this parameter, select **Enable Memory Management** in
the **Tracker Management** tab.

### **Maximum number of tracks per cluster** — Maximum number of tracks per cluster `5` (default) | positive integer

Specify the maximum number of tracks per cluster during the run-time of the tracker
as a positive integer.

Setting this parameter to a finite value allows the tracker to bound cluster sizes
and reduces the memory footprint of the tracker in generated C/C++ code. Set this
property to `Inf` if you do not want to bound the maximum number of
detections per cluster.

If during run-time, the number of tracks in a cluster exceeds this parameter, the
tracker reacts based on the **Handle run-time violation of cluster
size** parameter.

#### Dependencies

To enable this parameter, select **Enable Memory Management** in
the **Tracker Management** tab.

### **Handle run-time violation of cluster size** — Handle run-time violation of cluster size `Auto` (default) | `Property`

Specify the handling of run-time violation of cluster size as one of these options:

- `Teminate` — The tracker reports an error if any of the
  cluster bounds specified in the **Maximum number of detections per
  cluster** and **Maximum number of tracks per cluster**
  parameters is violated during run-time.
- `Split and warn` — The tracker splits the size-violating
  cluster into smaller clusters by using a suboptimal approach. The tracker also
  reports a warning to indicate a violation.
- `Split` — The tracker splits the size-violating cluster into
  smaller clusters by using a suboptimal approach and does not report any warning.

In the suboptimal approach, the tracker separates out detections or tacks
that have the smallest likelihood of association to other tracks or detections until the
cluster bounds are satisfied. These separated-out detections or tracks can form one or
many new clusters depends on their association likelihoods with each other and the
**Threshold for assigning detections to tracks** parameter.

#### Dependencies

To enable this parameter, select **Enable Memory Management** in
the **Tracker Management** tab.
## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The block supports *strict single-precision* code generation with
  these restrictions:

  - You must specify the **Value of k for k-best JPDA** parameter
    as a finite positive integer.
  - You must specify the filter initialization function to return a `trackingEKF`, `trackingUKF`, `trackingCKF`, or `trackingIMM` object configured with single-precision.

  For details, see Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.
- The block supports *non-dynamic memory allocation* code
  generation with these restrictions:

  - You must specify the **Value of k for k-best JPDA** parameter
    as a finite positive integer.
  - You must specify the filter initialization function to return a `trackingEKF`, `trackingUKF`, `trackingCKF`, or `trackingIMM` object.

  For details, see Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.

  After enabling non-dynamic memory allocation code generation, consider using these
  parameters to set bounds on the local variables in the tracker:

  - **Enable memory management**
  - **Maximum number of detections per sensor**
  - **Maximum number of detections per cluster**
  - **Maximum number of tracks per cluster**
  - **Handle run-time violation of cluster size**
- In code generation, if the detection inputs are specified in `double` precision, then the `NumTracks` field of the track outputs is returned as a `double` variable. If the detection inputs are specified in `single` precision, then the `NumTracks` field of the track outputs is returned as a `uint32` variable.

## Version History

**Introduced in R2019b**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Joint probabilistic data association tracker

The Joint Probabilistic Data Association Multi Object Tracker block is
capable of processing detections of multiple targets from multiple sensors. The tracker uses
joint probabilistic data association to assign detections to each track. The tracker applies a
soft assignment, in which multiple detections can contribute to each track. The tracker
initializes, confirms, corrects, predicts (performs coasting), and deletes tracks. The tracker
estimates the state vector and state estimate error covariance matrix for each track. Each
detection is assigned to at least one track. If the detection cannot be assigned to any
existing track, the tracker creates a new track.

You can enable different JPDA tracking
modes by specifying the **Type of track confirmation and deletion logic** and
**Value of k for k-best JPDA** parameters.

- Setting the **Type of track confirmation and deletion logic**
  parameter to `'Integrated'` to enable the joint integrated data
  association (JIPDA) tracker, in which track confirmation and deletion is based on the
  probability of track existence.
- Setting the **Value of k for k-best JPDA** parameter to a finite
  integer to enable the k-best joint integrated data association (k-best JPDA) tracker,
  which generates a maximum of k events per cluster.

Any new track starts in a *tentative* state. If enough detections are
assigned to a tentative track, its status changes to *confirmed*. If the
detection already has a known classification (the `ObjectClassID` field of
the returned track is nonzero), that corresponding track is confirmed immediately. When a
track is confirmed, the tracker considers the track to represent a physical object. If
detections are not assigned to the track within a specifiable number of updates, the track is
deleted.
