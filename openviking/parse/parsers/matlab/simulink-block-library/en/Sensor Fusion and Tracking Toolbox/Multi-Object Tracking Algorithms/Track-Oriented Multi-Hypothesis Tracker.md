---
type: simulink-block
title: 'Track-Oriented Multi-Hypothesis Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'trackorientedmultihypothesistracker'
documentation_source_path: 'ref/trackorientedmultihypothesistracker.html'
language: en
---

# Track-Oriented Multi-Hypothesis Tracker

## Ports

### Input

### **Detections** — Detection list Simulink® bus containing MATLAB® structure

Detection list, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Integer |
| `Detections` | Object detections | Array of `objectDetection` structures. The first `NumDetections` of these detections are actual detections. |

The fields of the detections structure are:

| Field | Description | Type |
| --- | --- | --- |
| `Time` | Measurement time | `Single` or `Double` |
| `Measurement` | Object measurements | `Single` or `Double` |
| `MeasurementNoise` | Measurement noise covariance matrix | `Single` or `Double` |
| `SensorIndex` | Unique ID of the sensor | `Single` or `Double` |
| `ObjectClassID` | Object classification ID | `Single` or `Double` |
| `MeasurementParameters` | Parameters used by initialization functions of tracking filters | Simulink Bus |
| `ObjectAttributes` | Additional information passed to tracker | Simulink Bus |

See `objectDetection` for a more detailed
explanation of these fields.

**Note**

The object detection structure contains a `Time` field. The
time tag of each object detection must be less than or equal to the time at the
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

### **Cost Matrix** — Cost matrix real-valued *N*-by-*M* matrix

Cost matrix, specified as a real-valued
*N*-by-*M* matrix, where *N* is
the number of branches and *M* is the number of current
detections.

The rows of the cost matrix must be in the same order as the list of branches.
Branches are ordered as they appear in the list of branches from the **All
Branches** output port on the previous invocation of the block. The columns
correspond to the detections.

In the first update to the tracker, or if the tracker has no previous tracks,
assign the cost matrix a size of [0, *N*]. The cost must be
calculated so that lower costs indicate a higher likelihood that the tracker assigns a
detection to a track. To prevent certain detections from being assigned to certain
tracks, use `Inf`.

If this port is not enabled, the filter initialized by the **Filter
initialization function** calculates the cost matrix using the distance
method.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable cost matrix input**.

### **Detectable BranchIDs** — Detectable Branch IDs real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix

Detectable branch IDs, specified as a real-valued *M*-by-1
vector or *M*-by-2 matrix. Detectable branches are branches that the
sensors expect to detect. The first column of the matrix contains a list of branch IDs
that the sensors report as detectable. The optional second column enables you to add
the detection probability for each branch. Branches are listed in the **All
Branches** output from the previous invocation of the block.

Tracks whose identifiers are not included in **Detectable
BranchIDs** are considered undetectable. The track deletion logic does not
count the lack of detection as a "missed detection" for track deletion
purposes.

If this port is not enabled, the tracker assumes all tracks to be detectable at
each invocation of the block.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable detectable branch IDs input**.

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

A track is confirmed if it satisfies the threshold specified in the**Confirmation threshold** parameter under the **Track
Logic** tab.

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
| `OOSMDetectionIndices` | Indices of out-of-sequence measurements |
| `BranchIDsAtStepBeginning` | Branch IDs when the update began. |
| `CostMatrix` | Cost of kinematic assignment matrix, in which the (*i*, *j*) element denotes the cost of assigning track *i* to detection *j*. |
| `Assignments` | Assignments returned from the `assignTOMHT` function. |
| `UnassignedTracks` | IDs of unassigned branches returned from the tracker. |
| `UnassignedDetections` | IDs of unassigned detections returned from the tracker. |
| `InitialBranchHistory` | Branch history after branching and before pruning. |
| `InitialBranchScores` | Branch scores before pruning. |
| `KeptBranchHistory` | Branch history after initial pruning. |
| `KeptBranchScores` | Branch scores after initial pruning. |
| `Clusters` | Logical array mapping branches to clusters. Branches belong in the same cluster if they share detections in their history or belong to the same track either directly or through other branches. |
| `TrackIncompatibility` | Branch incompatibility matrix. The `(i,j)` element is true if the *i*-th and *j*-th branches have shared detections in their history or belong to the same track. |
| `GlobalHypotheses` | Logical matrix mapping branches to global hypotheses. Compatible branches can belong in the same hypotheses. |
| `GlobalHypScores` | Total score of global hypotheses. |
| `PrunedBranches` | Logical array of branches that the `pruneTrackBranches` function determines to prune. |
| `GlobalBranchProbabilities` | Global probability of each branch existing in the global hypotheses. |
| `BranchesDeletedByPruning` | Branches deleted by the tracker. |
| `BranchIDsAtStepEnd` | Branch IDs when the update ended. |

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable information output**.

### **All Branches** — All branches Simulink bus containing MATLAB structure

All branches, returned as a Simulink bus containing a MATLAB structure.

The fields of the branch structure are the same as the Track Structure.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable all branches output**.

## Parameters

#### Tracker Management

### **Tracker identifier** — Unique tracker identifier `0` (default) | nonnegative integer

Unique tracker identifier, specified as a nonnegative integer. This parameter is
passed as the `SourceIndex` in the tracker outputs, and distinguishes
tracks that come from different trackers in a multiple-tracker system. You must specify
this property as a positive integer to use the track outputs as inputs to a `trackFuser` object.

**Example:** `1`

### **Filter initialization function** — Filter initialization function `@initcvekf` (default) | function name

Filter initialization function, specified as the name of a filter initialization
function. The tracker uses a filter initialization function when creating new
tracks.

Sensor Fusion and Tracking Toolbox™ provides many initialization functions that are compatible with this
block.

| Initialization Function | Function Definition |
| --- | --- |
| `initcvabf` | Initialize constant-velocity alpha-beta filter |
| `initcaabf` | Initialize constant-acceleration alpha-beta filter |
| `initcvekf` | Initialize constant-velocity extended Kalman filter. |
| `initcackf` | Initialize constant-acceleration cubature filter. |
| `initctckf` | Initialize constant-turn-rate cubature filter. |
| `initcvckf` | Initialize constant-velocity cubature filter. |
| `initcapf` | Initialize constant-acceleration particle filter. |
| `initctpf` | Initialize constant-turn-rate particle filter. |
| `initcvpf` | Initialize constant-velocity particle filter. |
| `initcvkf` | Initialize constant-velocity linear Kalman filter. |
| `initcvukf` | Initialize constant-velocity unscented Kalman filter. |
| `initcaekf` | Initialize constant-acceleration extended Kalman filter. |
| `initcakf` | Initialize constant-acceleration linear Kalman filter. |
| `initcaukf` | Initialize constant-acceleration unscented Kalman filter. |
| `initctekf` | Initialize constant-turn-rate extended Kalman filter. |
| `initctukf` | Initialize constant-turn-rate unscented Kalman filter. |
| `initcvmscekf` | Initialize constant-velocity modified spherical coordinates extended Kalman filter. |
| `initrpekf` | Initialize constant-velocity range-parametrized extended Kalman filter. |
| `initapekf` | Initialize constant-velocity angle-parametrized extended Kalman filter. |
| `initekfimm` | Initialize tracking IMM filter. |

You can also write your own initialization function. The function must have the
following
syntax:

```
filter = filterInitializationFcn(detection)
```

The
input to this function is a detection report like those created by the `objectDetection` object. The output of this function must be a filter object:
`trackingKF`, `trackingEKF`, `trackingUKF`, `trackingCKF`,
`trackingPF`,
`trackingMSCEKF`, `trackingGSF`,
`trackingIMM`,
or `trackingABF`.

To guide you in writing this function, you can examine the details of the supported
functions from within MATLAB. For example:

```
type initcvekf
```

### **Threshold for assigning detections to tracks** — Threshold for assigning detections to tracks `30*[0.3 0.7 1 Inf]` (default) | positive scalar | 1-by-3 vector of positive values | 1-by-4 vector of positive values

Threshold for assigning detections to tracks, specified as a positive scalar, a
1-by-3 vector of non-decreasing positive values,
[*C*1,*C*2,*C*3],
or a1-by-4 vector of non-decreasing positive values,
[*C*1,*C*2,*C*3,*C*4].
If specified as a scalar, the specified value, *val*, will be expanded
to [0.3,0.7,1,`Inf`]\**val*. If specified as
[*C*1,*C*2,*C*3],
it will be expanded as
[*C*1,*C*2,*C*3,`Inf`].

The thresholds control (1) the assignment of a detection to a track, (2) the
creation of a new branch from a detection, and (3) the creation of a new branch from an
unassigned track. The threshold values must satisfy:
*C*1
*<=*
*C*2
*<=*
*C*3*<=**C*4.

- *C*1 defines a distance such that if a
  track has an assigned detection with lower distance than
  *C*1, the track is no longer considered
  unassigned and does not create an unassigned track branch.
- *C*2 defines a distance such that if a
  detection has been assigned to a track with lower distance than
  *C*2, the detection is no longer
  considered unassigned and does not create a new track branch.
- *C*3 defines the maximum distance for
  assigning a detection to a track.
- *C*4 defines combinations of track and
  detection for which an accurate normalized cost calculation is performed.
  Initially, the tracker executes a coarse estimation for the normalized distance
  between all the tracks and detections. The tracker only calculates the accurate
  normalized distance for the combinations whose coarse normalized distance is less
  than *C*4.

See Algorithms for an explanation
of the normalized distance.

- Increase the value of *C*3 if there
  are detections that should be assigned to tracks but are not. Decrease the value
  if there are detections that are assigned to tracks they should not be assigned to
  (too far away).
- Increasing the values *C*1 and
  *C*2 helps control the number of track
  branches that are created. However, doing so reduces the number of branches
  (hypotheses) each track has.
- Increase the value of *C*4 if there
  are combinations of track and detection that should be calculated for assignment
  but are not. Decrease it if cost calculation takes too long.

**Note**

If the value of *C*4 is finite, the state
transition function and measurement function, specified in the tracking filter used in
the tracker, must be able to take an *M*-by-*N*
matrix of states as input and output *N* predicted states and
*N* measurements, respectively. *M* is the size of
the state. *N*, the number of states, is an arbitrary nonnegative
integer.

**Data Types:** `single` | `double`

### **Maximum number of tracks** — Maximum number of tracks `100` (default) | positive integer

Maximum number of tracks that the block can maintain, specified as a positive
integer.

### **Maximum number of sensors** — Maximum number of sensors `20` (default) | positive integer

Maximum number of sensors that can be connected to the tracker, specified as a
positive integer. `MaxNumSensors` must be greater than or equal to
the largest value of `SensorIndex` found in all the detections used to
update the tracker. `SensorIndex` is one of the properties of an
`objectDetection` object. The block's
`MaxNumSensors` property determines how many sets of
`ObjectAttributes` fields each output track can have.

### **Out-of-sequence measurements handling** — Out-of-sequence measurements handling `Terminate` (default) | `neglect`

Out-of-sequence measurements handling, specified as
`Terminate` or `neglect`. Each
detection has a timestamp associated with it,
*t*d, and the tracker block has it own
timestamp, *t*t, which is updated in each
invocation. The tracker block considers a measurement as an OOSM if
*t*d <
*t*t.

When the parameter is specified as:

- `Terminate` — The block stops running when it
  encounters any out-of-sequence measurements.
- `Neglect` — The block neglects any out-of-sequence
  measurements and continue to run.

To simulate out-of-sequence detections, use `objectDetectionDelay`.

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

### **Track output method** — Track output method `'Tracks'` (default) | `'Hypothesis'` | `'Clusters'`

Track output method, specified as `'Tracks'`,
`'Hypothesis'`, or `'Clusters'`.

- `'Tracks'` – Output the centroid of each track based on its
  track branches.
- `'Hypothesis'` – Output branches that are in certain
  hypotheses. If you choose this option, list the hypotheses to output using the
  `HypothesesToOutput` property.
- `'Clusters'` – Output the centroid of each cluster. Similar
  to the `'Tracks'` output, but includes all tracks within a
  cluster.

**Data Types:** `char`

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In the
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.

#### Hypotheses Management

### **Maximum number of hypotheses to be maintained** — Maximum number of hypotheses to be maintained `5` (default) | positive integer

Maximum number of global assignment hypotheses maintained by the tracker at each
step, specified as a positive integer. If the number of hypotheses is larger than the
property value, the tracker prunes the hypotheses of lower likelihoods and its
associated branches until the number of hypotheses reaches the property value. Larger
values increase the computational load.

**Example:** `10`

**Data Types:** `single` | `double`

### **Maximum number of track branches per track** — Maximum number of track branches per track `3` (default) | positive integer

Maximum number of track branches allowed for each track, specified as a positive
integer. Larger values increase the computational load.

**Data Types:** `single` | `double`

### **Maximum number of scans maintained in the branch history** — Maximum number of scans maintained in the branch history `4` (default) | positive integer

Maximum number of scans maintained in the branch history, specified as a positive
integer. The number of track history scans is typically from 2 through 6. Larger values
increase the computational load.

**Data Types:** `single` | `double`

### **Minimum probability required to keep a branch** — Minimum probability required to keep a branch `.001` (default) | positive scalar

Minimum probability required to keep a track branch, specified as a positive scalar
less than one. Any track with probability lower than the specified probability is
pruned. Typical values are 0.001 to 0.005.

**Example:** `.003`

**Data Types:** `single` | `double`

### **N-scan pruning method** — N-scan pruning method `'None'` (default) | `'Hypothesis'`

N-scan pruning method, specified as `'None'` or
`'Hypothesis'`. In N-scan pruning, branches that belong to the same
track are pruned (deleted) if, in the N-scans history, they contradict the most likely
branch for the same track. The most-likely branch is defined in one of two ways:

- `'None'` – No N-scan pruning is performed.
- `'Hypothesis'` – The chosen branch is in the most likely
  hypothesis.

**Example:** `'Hypothesis'`

#### Track Logic

### **Confirmation threshold [positive scalar]** — Minimum score required to confirm track `20` (default) | positive scalar

Minimum score required to confirm a track, specified as a positive scalar. Any track
with a score higher than this threshold is confirmed.

**Example:** `12`

**Data Types:** `single` | `double`

### **Deletion threshold [negative scalar]** — Maximum score drop for track deletion `-7` (default) | scalar

The maximum score drop before a track is deleted, specified as a scalar. Any track
with a score that falls by more than this parameter from the maximum score is deleted.
Deletion threshold is affected by the probability of a false alarm.

**Example:** `-1`

**Data Types:** `single` | `double`

### **Probability of detection used for track score** — Probability of detection used for track score `0.9` (default) | positive scalar between 0 and 1

Probability of detection, specified as a positive scalar between 0 and 1. This
property is used to compute track score.

**Example:** `0.5`

**Data Types:** `single` | `double`

### **Rate of false positives used for track score** — Probability of false alarm used for track score `1e-6` (default) | scalar

The probability of false alarm, specified as a scalar. This property is used to
compute track score.

**Example:** `1e-5`

**Data Types:** `single` | `double`

### **Volume of the sensor's detection bin** — Volume of sensor measurement bin `1` (default) | positive scalar

The volume of a sensor measurement bin, specified as a positive scalar. For example,
if a radar produces a 4-D measurement, which includes azimuth, elevation, range, and
range rate, the 4-D volume is defined by the radar angular beam width, the range bin
width, and the range-rate bin width. Volume is used in calculating the track score when
initializing and updating a track.

**Example:** `1.5`

**Data Types:** `single` | `double`

### **Rate of new tracks per unit volume** — Rate of new tracks per unit volume `1` (default) | positive scalar

The rate of new tracks per unit volume, specified as a positive scalar. The
parameter is used in calculating the track score during track initialization.

**Example:** `2.5`

**Data Types:** `single` | `double`

#### Port Setting

### **Prediction time source** — Source of prediction time `Auto` (default) | `Input port`

Source for prediction time, specified as `Input port` or
`Auto`. Select `Input port` to input
an update time by using the **Prediction Time** input port. Otherwise,
the simulation clock managed by Simulink determines the update time.

### **Enable cost matrix input** — Enable input port for cost matrix off (default) | on

Select this parameter to enable the input of a cost matrix by using the
**Cost Matrix** input port.

### **Enable detectable branch IDs input** — Enable detectable branch IDs input off (default) | on

Select this parameter to enable the **Detectable branch IDs** input
port.

### **Enable tentative tracks output** — Enable output port for tentative tracks off (default) | on

Select this parameter to enable the output of tentative tracks through the
**Tentative Tracks** output port.

### **Enable all tracks output** — Enable output port for all tracks off (default) | on

Select this parameter to enable the output of all the tracks through the
**All Tracks** output port.

### **Enable information output** — Enable output port for analysis information off (default) | on

Select this parameter to enable the output port for analysis information through the
**Info** output port.

### **Enable all branches output** — Enable output port for all branches off (default) | on

Select this parameter to enable the output of all the branches through the
**All Branches** output port.

### **Source of output bus name** — Source of output track bus name `Auto` (default) | `Property`

Source of the output track bus name, specified as:

- `Auto` — The block automatically creates an output
  track bus name.
- `Property` — Specify the output track bus name by
  using the **Specify an output bus name** parameter.

### **Source of output info bus name** — Source of output information bus name `Auto` (default) | `Property`

Source of the output info bus name, specified as:

- `Auto` — The block automatically creates an output
  info bus name.
- `Property` — Specify the output info bus name by
  using the **Specify an output info bus name** parameter.

#### Dependencies

To enable this parameter, on the **Port Setting** tab, select
**Enable information output**.

## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- In code generation, if the detection inputs are specified in `double` precision, then the `NumTracks` field of the track outputs is returned as a `double` variable. If the detection inputs are specified in `single` precision, then the `NumTracks` field of the track outputs is returned as a `uint32` variable.

## Version History

**Introduced in R2020a**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Track-Oriented Multi-Hypothesis Tracker

The Track-Oriented Multi-Hypothesis Tracker block processes detections of
multi targets from multiple sensors. The tracker block initializes, confirms, predicts,
corrects, and deletes tracks. Inputs to the tracker block are detection reports generated by
`objectDetection`, `fusionRadarSensor`,
`irSensor`, or
`sonarSensor`
objects. The tracker block estimates the state vector and state vector covariance matrix for
each track. The tracker assigns detections based on a track-oriented, multi-hypothesis
approach.

Any new track starts in a *tentative* state. If enough detections are
assigned to a tentative track, its status changes to *confirmed*. If the
detection already has a known classification (the `ObjectClassID` field of
the returned track is nonzero), that track is confirmed immediately. When a track is
confirmed, the multi-object tracker considers the track to represent a physical object. If
detections are not assigned to the track within a specifiable number of updates, the track is
deleted. For an overview of how the tracker functions, see Algorithms.
