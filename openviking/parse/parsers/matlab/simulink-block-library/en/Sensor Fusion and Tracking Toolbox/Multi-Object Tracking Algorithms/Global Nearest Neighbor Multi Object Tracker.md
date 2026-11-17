---
type: simulink-block
title: 'Global Nearest Neighbor Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'globalnearestneighbormultiobjecttracker'
documentation_source_path: 'ref/globalnearestneighbormultiobjecttracker.html'
language: en
---

# Global Nearest Neighbor Multi Object Tracker

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
  summary: Confirmed and Tentative tracks Simulink bus containing MATLAB structure
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
| `NumDetections` | Number of detections | integer |
| `Detections` | Object detections | Array of object detection structures. The first `NumDetections` of these detections are actual detections. |

The fields of `Detections` are:

| Field | Description | Type |
| --- | --- | --- |
| `Time` | Measurement time | `single` or `double` |
| `Measurement` | Object measurements | `single` or `double` |
| `MeasurementNoise` | Measurement noise covariance matrix | `single` or `double` |
| `SensorIndex` | Unique ID of the sensor | `single` or `double` |
| `ObjectClassID` | Object classification ID | `single` or `double` |
| `MeasurementParameters` | Parameters used by initialization functions of tracking filters | Simulink Bus |
| `ObjectAttributes` | Additional information passed to tracker | Simulink Bus |

See `objectDetection` for more detailed
explanations of these fields.

**Note**

The object detection structure contains a `Time` field. The
time tag of each object detection must be less than or equal to the time of the
current invocation of the block. The time tag must also be greater than the update
time specified in the previous invocation of the block.

### **Prediction Time** — Track update time real scalar

Track update time, specified as a real scalar in seconds. The tracker updates all
tracks to this time. The update time must always increase with each invocation of the
block. Units are in seconds. The update time must be at least as large as the largest
`Time` specified at the **Detections** input
port.

If this port is not enabled, the simulation clock managed by Simulink determines
the update time.

#### Dependencies

To enable this port, in the **Port Setting** tab, set
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
at the **All Tracks** output port on the previous invocation of the
block.

In the first update to the tracker, or if the track has no previous tracks, assign
the cost matrix a size of [0, *N*d]. The cost
must be calculated so that lower costs indicate a higher likelihood that the tracker
assigns a detection to a track. To prevent certain detections from being assigned to
certain tracks, use `Inf`.

If this port is not enabled, the filter initialized by the **Filter
initialization function** calculates the cost matrix using the distance
method.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable cost matrix input**.

### **Detectable TrackIDs** — Detectable track IDs real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix

Detectable track IDs, specified as a real-valued *M*-by-1 vector
or *M*-by-2 matrix. Detectable tracks are tracks that the sensors
expect to detect. The first column of the matrix contains a list of track IDs that the
sensors report as detectable. The second column contains the detection probability for
the track. The detection probability is either reported by a sensor or, if not
reported, obtained from the **Probability of detection used for track
score** parameter.

Tracks whose identifiers are not included in **Detectable
TrackIDs** are considered undetectable. The track deletion logic does not
count the lack of detection as a "missed detection" for track deletion
purposes.

If this port is not enabled, the tracker assumes all tracks to be detectable at
each invocation of the block.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
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
- Score – The track score is at least as high as the confirmation threshold
  specified in **Confirmation threshold** for the
  `Score` logic.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks, returned as a Simulink bus containing a MATLAB structure. A track is tentative before it is confirmed.

The fields of the track structure are shown in Track Structure.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable tentative tracks output**.

### **All Tracks** — Confirmed and Tentative tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks, returned as a Simulink bus containing a MATLAB structure.

The fields of the track structure are shown in Track Structure.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable all tracks output**.

### **Info** — Additional information for analyzing track updates Simulink bus containing MATLAB structure

Additional information for analyzing track updates, returned as a Simulink bus containing a MATLAB structure.

This table shows the fields of the info structure:

|  |  |
| --- | --- |
| **Field** | **Description** |
| `OOSMDetectionIndices` | Indices of out-of-sequence measurements at the current step of the tracker |
| `TrackIDsAtStepBeginning` | Track IDs when step began |
| `CostMatrix` | Cost of kinematic assignment matrix, in which the (*i*, *j*) element denotes the cost of assigning track *i* to detection *j*. |
| `Assignments` | Assignments from the assignment function, returned as an integer-valued *L*-by-2 matrix, where *L* is the number of assignments. The first column of the matrix contains the track IDs and the second column contains the indices of assigned detections. The detection indices are the array-indices of the detections that you used to update the tracker. |
| `UnassignedTracks` | IDs of unassigned tracks returned from the tracker |
| `UnassignedDetections` | IDs of unassigned detections returned from the tracker |
| `InitiatedTrackIDs` | IDs of tracks initiated during the step |
| `DeletedTrackIDs` | IDs of tracks deleted during the step |
| `TrackIDsAtStepEnd` | Track IDs when the step ended |
| `MaxNumDetectionsPerCluster` | The maximum number of detections in all the clusters generated during the step. The structure has this field only when you set both the **Cluster tracks and detections for assignment** and **Enable memory management** parameters as `on`. |
| `MaxNumTracksPerCluster` | The maximum number of tracks in all the clusters generated during the step. The structure has this field only when you set both the **Cluster tracks and detections for assignment** and **Enable memory management** parameters as `on`. |
| `OOSMHandling` | Analysis information for out-of-sequence measurements handling, returned as a structure. The structure has this field only when the **Out-of-sequence measurements handling** parameter of the tracker is specified as `Retordiction`. |

The `OOSMHandling` structure contains these fields:

| Field | Description |
| --- | --- |
| `DiscardedDetections` | Indices of discarded out-of-sequence detections. An OOSM is discarded if it is not covered by the saved state history specified by the **Maximum number of OOSM steps** parameter. |
| `CostMatrix` | Cost of assignment matrix for the out-of-sequence measurements |
| `Assignments` | Assignments between the out-of-sequence detections and the maintained tracks |
| `UnassignedDetections` | Indices of unassigned out-of-sequence detections. The tracker creates new tracks for unassigned out-of-sequence detections. |

#### Dependencies

To enable this port, in the **Port Setting** tab, select
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
- name: Maximum number of tracks
  summary: Maximum number of tracks 200 (default) | positive integer
  group: ''
- name: Maximum number of sensors
  summary: Maximum number of sensors 20 (default) | positive integer
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
- name: Assignment algorithm name
  summary: Assignment algorithm name 'MatchPairs' (default) | 'Munkres' | 'Jonker-Volgenant' | 'Auction' | 'Custom'
  group: ''
- name: Name of 'Custom' assignment function
  summary: Custom assignment function name character vector
  group: ''
- name: Threshold for assigning detections to tracks
  summary: Threshold for assigning detections to tracks 30*[1 Inf] (default) | positive scalar | 1-by-2 vector of positive
    values
  group: ''
- name: Cluster tracks and detections for assignment
  summary: Cluster tracks and detections for assignment off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted Execution (default) | Code Generation
  group: ''
- name: Type of track confirmation and deletion logic
  summary: Confirmation and deletion logic type History (default) | Score
  group: ''
- name: Confirmation threshold [M N]
  summary: Track confirmation threshold for history logic [2 3] (default) | real-valued 1-by-2 vector of positive integers
  group: ''
- name: Deletion threshold [P Q]
  summary: Track deletion threshold for history logic [5 5] (default) | real-valued 1-by-2 vector of positive integers
  group: ''
- name: Confirmation threshold [positive scalar]
  summary: Track confirmation threshold for score logic 20 (default) | positive scalar
  group: ''
- name: Deletion threshold [negative scalar]
  summary: Track deletion threshold for score logic -7 (default) | scalar | negative scalar
  group: ''
- name: Probability of detection used for track score
  summary: Probability of detection used for track score 0.9 (default) | scalar in (0,1)
  group: ''
- name: Rate of false positives used for track score
  summary: Probability of false alarm used for track score 1e-6 (default) | scalar in (0,1)
  group: ''
- name: Volume of the sensor's detection bin
  summary: Volume of sensor detection bin 1 (default) | positive scalar
  group: ''
- name: Rate of new tracks per unit volume
  summary: Rate of new tracks per unit volume 1 (default) | positive scalar
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

Filter initialization function, specified as the name of a valid filter
initialization function. The tracker uses the filter initialization function when
creating new tracks.

Sensor Fusion and Tracking Toolbox™ supplies many initialization functions that you can use:

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

You can also write your own initialization function. The function must have this
syntax:

```
filter = filterInitializationFcn(detection)
```

The
input to this function is a detection report like those created by `objectDetection`. The output of this function must be a filter object:
`trackingKF`, `trackingEKF`, `trackingUKF`, `trackingCKF`,
`trackingPF`,
`trackingMSCEKF`, `trackingGSF`,
`trackingIMM`,
or `trackingABF`.

To guide you in writing this function, you can examine the details of the supplied
functions from within MATLAB. For example:

```
type initcvekf
```

### **Maximum number of tracks** — Maximum number of tracks `200` (default) | positive integer

Maximum number of tracks that the block can maintain, specified as a positive
integer.

### **Maximum number of sensors** — Maximum number of sensors `20` (default) | positive integer

Maximum number of sensors that the block can process, specified as a positive
integer. This value should be greater than or equal to the highest
`SensorIndex` value input at the **Detections**
input port.

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
  algorithm to update the tracker by either neglecting the OOSM, updating existing
  tracks, or creating new tracks using the OOSM. You must specify a filter
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

For more details on the retrodiction and retro-correction algorithms, see
Retrodiction and Retro-Correction. To simulate out-of-sequence detections, use `objectDetectionDelay`.

**Note**

- When you select `Retrodiction`, you cannot use the
  **Cost Matrix** input.

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

Select this parameter to enable memory management using the **Maximum number
of detections per sensor** parameter to specify the maximum number of
detections that each sensor can pass to the tracker during one call of the tracker.
Additionally, if the **Cluster tracks and detections for assignment**
parameter is specified as `on`, you can use three more
parameters to specify bounds for certain variable-sized arrays in the tracker as well as
determine how the tracker handles cluster size violations:

- **Maximum number of detections per cluster**
- **Maximum number of tracks per cluster**
- **Handle run-time violation of cluster size**

Specifying bounds for variable-sized arrays allows you to manage the memory
footprint of the tracker in the generated C/C++ code.

### **Assignment algorithm name** — Assignment algorithm name `'MatchPairs'` (default) | `'Munkres'` | `'Jonker-Volgenant'` | `'Auction'` | `'Custom'`

Assignment algorithm, specified as `'MatchPairs'`,
`'Munkres'`, `'Jonker-Volgenant'`,
`'Auction'`, or `'Custom'`. Munkres is the only
assignment algorithm that guarantees an optimal solution, but it is also the slowest,
especially for large numbers of detections and tracks. The other algorithms do not
guarantee an optimal solution but can be faster for problems with 20 or more tracks and
detections. Use`'Custom'` to define your own assignment function and
specify its name in the `CustomAssignmentFcn` property.

### **Name of 'Custom' assignment function** — Custom assignment function name character vector

Custom assignment function name, specified as a character string. An assignment
function must have this
syntax:

```
 [assignment,unTrs,unDets] = f(cost,costNonAssignment)
```

For
an example of an assignment function and a description of its arguments, see `assignmunkres`.

**Example:** `'mycustomfcn'`

#### Dependencies

To enable this property, set the **Assignment algorithm name**
name to `'Custom'`.

### **Threshold for assigning detections to tracks** — Threshold for assigning detections to tracks `30*[1 Inf]` (default) | positive scalar | 1-by-2 vector of positive values

Threshold for assigning detections to tracks (or gating threshold), specified as a
positive scalar or a 1-by-2 vector of
[*C*1*,C*2],
where *C*1 ≤
*C*2. If specified as a scalar, the specified
value, *val*, will be expanded to [*val*,
`Inf`].

Initially, the tracker executes a coarse estimation for the normalized distance
between all the tracks and detections. The tracker only calculates the accurate
normalized distance for the combinations whose coarse normalized distance is less than
*C*2. Also, the tracker can only assign a
detection to a track if their accurate normalized distance is less than
*C*1. See Algorithms for an explanation
of the normalized distance.

- Increase the value of *C*2 if there are
  combinations of track and detection that should be calculated for assignment but are
  not. Decrease it if cost calculation takes too much time.
- Increase the value of *C*1 if there are
  detections that should be assigned to tracks but are not. Decrease it if there are
  detections that are assigned to tracks they should not be assigned to (too far
  away).

**Note**

If the value of *C*2 is finite, the state
transition function and measurement function, specified in the tracking filter used in
the tracker, must be able to take an *M*-by-*N*
matrix of states as input and output *N* predicted states and
*N* measurements, respectively. *M* is the size of
the state. *N*, the number of states, is an arbitrary nonnegative
integer.

### **Cluster tracks and detections for assignment** — Cluster tracks and detections for assignment `off` (default) | `on`

Specify cluster tracks and detections for assignment as:

- `off` — The tracker solves the global nearest
  neighbor assignment problem per sensor using a cost matrix. The number of columns
  in the cost matrix is equal to the number of detections by the sensor, and the
  number of rows is equal to the number of tracks maintained by the tracker.
  Forbidden assignments (assignments with a cost greater than the
  **Threshold for assigning detections to tracks** parameter)
  have an infinite cost of assignment.
- `on` — The tracker creates a cluster after separating out the
  forbidden assignments (assignments with a cost greater than the
  **Threshold for assigning detections to tracks** parameter) and
  uses the forbidden assignments to form new clusters based one the
  **Threshold for assigning detections to tracks** parameter. A
  *cluster* is a collection of detections (per sensor) and
  tracks considered to be assigned to each other. In this case, the tracker solves
  the global nearest neighbor assignment problem per cluster.

  When you both specify this property as `on` and select
  **Enable memory management** in the **Tracker
  Management** tab, you can use these three parameters to specify bounds
  for certain variable-sized arrays in the tracker as well as determine how the
  tracker handles cluster size violations:

  - **Maximum number of detections per cluster**
  - **Maximum number of tracks per cluster**
  - **Handle run-time violation of cluster size**

  Specifying bounds for variable-sized arrays enables you to manage the memory
  footprint of the tracker, especially in the generated C/C++ code.

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.

#### Track Logic

### **Type of track confirmation and deletion logic** — Confirmation and deletion logic type `History` (default) | `Score`

Confirmation and deletion logic type, selected as `History`
or `Score`.

- `History` – Track confirmation and deletion is based on the
  number of times the track has been assigned to a detection in the latest tracker
  updates.
- `Score` – Track confirmation and deletion is based on a
  log-likelihood track score. A high score means that the track is more likely to be
  valid. A low score means that the track is more likely to be a false alarm.

### **Confirmation threshold [M N]** — Track confirmation threshold for history logic `[2 3]` (default) | real-valued 1-by-2 vector of positive integers

Track confirmation threshold for history logic, specified as a real-valued 1-by-2
vector of positive integers `[M N]`. A track is confirmed if it
receives at least `M` detections in the last `N`
updates.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `History`.

### **Deletion threshold [P Q]** — Track deletion threshold for history logic `[5 5]` (default) | real-valued 1-by-2 vector of positive integers

Track deletion threshold for history logic, specified as a real-valued 1-by-2 vector
of positive integers `[P Q]`. If a confirmed track is not assigned to
any detection `P` times in the last `Q` tracker
updates, then the track is deleted.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `History`.

### **Confirmation threshold [positive scalar]** — Track confirmation threshold for score logic `20` (default) | positive scalar

Track confirmation threshold for score logic, specified as a real-valued positive
scalar. A track is confirmed if its score is at least as high as the confirmation
threshold.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

### **Deletion threshold [negative scalar]** — Track deletion threshold for score logic `-7` (default) | scalar | negative scalar

Track deletion threshold for score logic, specified as a negative scalar. A track is
deleted if its score decreases by at least the threshold from the maximum track
score.

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

### **Probability of detection used for track score** — Probability of detection used for track score `0.9` (default) | scalar in (0,1)

Probability of detection used for track score, specified as a positive scalar in
(0,1).

**Example:** `0.5`

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

### **Rate of false positives used for track score** — Probability of false alarm used for track score `1e-6` (default) | scalar in (0,1)

The probability of false alarm used for track score, specified as a scalar in (0,1).

**Example:** `1e-5`

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

### **Volume of the sensor's detection bin** — Volume of sensor detection bin `1` (default) | positive scalar

The volume of a sensor detection bin, specified as a positive scalar. For example,
if a radar produces a 4-D measurement, which includes azimuth, elevation, range, and
range rate, the 4-D volume is defined by the radar angular beam width, the range bin
width, and the range-rate bin width. Volume is used in calculating the track score when
initializing and updating a track.

**Example:** `1.5`

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

### **Rate of new tracks per unit volume** — Rate of new tracks per unit volume `1` (default) | positive scalar

The rate of new tracks per unit volume, specified as a positive scalar. The rate of
new tracks is used in calculating the track score during track initialization.

**Example:** `2.5`

#### Dependencies

To enable this parameter, set **Type of track confirmation and deletion
logic** to `Score`.

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
tracker in each call of the tracker.

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

To enable this parameter, specify the **Cluster tracks and detections for
assignment** as `on` and select **Enable
Memory Management** in the **Tracker Management**
tab.

### **Maximum number of tracks per cluster** — Maximum number of tracks per cluster `5` (default) | positive integer

Specify the maximum number of tracks per cluster during the run-time of the tracker
as a positive integer.

Setting this parameter to a finite value allows the tracker to bound cluster sizes
and reduces the memory footprint of the tracker in generated C/C++ code. Set this
property to `Inf` if you do not want to bound the maximum number of
detections per cluster.

If, during run-time, the number of tracks in a cluster exceeds this parameter, the
tracker reacts based on the **Handle run-time violation of cluster
size** parameter.

#### Dependencies

To enable this parameter, specify the **Cluster tracks and detections for
assignment** as `on` and select **Enable
Memory Management** in the **Tracker Management**
tab.

### **Handle run-time violation of cluster size** — Handle run-time violation of cluster size `Auto` (default) | `Property`

Specify the handling of run-time violation of cluster size as one of these options:

- `Teminate` — The tracker reports an error if, during
  run-time, any cluster violates the cluster bounds specified in the
  **Maximum number of detections per cluster** and
  **Maximum number of tracks per cluster** parameters.
- `Split and warn` — The tracker splits the size-violating
  cluster into smaller clusters by using a suboptimal approach. The tracker also
  reports a warning to indicate the violation.
- `Split` — The tracker splits the size-violating cluster into
  smaller clusters by using a suboptimal approach. The tracker does not report a
  warning.

In the suboptimal approach, the tracker separates out detections or tacks
that have the smallest likelihoods of association to other tracks or detections until
the cluster bounds are satisfied. These separated-out detections or tracks can form one
or many new clusters depends on their association likelihoods with each other and the
**Threshold for assigning detections to tracks** parameter.

#### Dependencies

To enable this parameter, specify the **Cluster tracks and detections for
assignment** as `on` and select **Enable
Memory Management** in the **Tracker Management**
tab.
## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The block supports *strict single-precision* code generation
  with these restrictions:

  - You must specify the assignment algorithm as
    `'Jonker-Volgenant'`.
  - You must specify the filter initialization function to return a `trackingEKF`, `trackingUKF`, `trackingCKF`, or `trackingIMM` object configured with single-precision.

  For details, see Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.
- The tracker supports *non-dynamic memory allocation* code
  generation with these restrictions:

  - You must specify the assignment algorithm as
    `'Jonker-Volgenant'` or
    `'MatchPairs'`.
  - You must specify the filter initialization function to return a `trackingEKF`, `trackingUKF`, `trackingCKF`, or `trackingIMM` object.

  For details, see Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.

  After enabling non-dynamic memory allocation code generation, consider using these
  parameters to set bounds on the local variables in the tracker:

  - **Enable memory management**
  - **Cluster tracks and detections for assignment**
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

Multi-sensor, multi-object tracker using GNN assignment

The Global Nearest Neighbor Multi Object Tracker block is capable of
processing detections of many targets from multiple sensors, much like the `trackerGNN`
System object™. The tracker initializes, confirms, predicts, corrects, and deletes tracks based
on a global nearest neighbor (GNN) assignment algorithm. The tracker estimates the state
vector and state vector covariance matrix for each track. Each detection is assigned to at
most one track. If the detection cannot be assigned to any track, the tracker initializes a
new track.

Any new track starts in a tentative state. If enough detections are assigned to a
tentative track, its status changes to confirmed. If the detection already has a known
classification (the `ObjectClassID` field of the returned track is nonzero),
that track is confirmed immediately. When a track is confirmed, the tracker considers the
track to represent a physical object. If detections are not assigned to the track within a
specifiable number of updates, the track is deleted.
