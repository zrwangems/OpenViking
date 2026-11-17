---
type: simulink-block
title: 'Multi-Object Tracker'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'multiobjecttracker'
documentation_source_path: 'ref/multiobjecttracker.html'
language: en
---

# Multi-Object Tracker

## Ports
```yaml
ports:
- name: Detections
  summary: Detection list Simulink bus containing MATLAB® structure
  direction: input
- name: Prediction Time
  summary: Track update time real scalar
  direction: input
- name: Cost Matrix
  summary: Cost matrix real-valued *N*t-by-*N*d matrix
  direction: input
- name: Detectable Track IDs
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
  summary: All tracks Simulink bus containing MATLAB structure
  direction: output
```

### Input

### **Detections** — Detection list Simulink bus containing MATLAB® structure

Detection list, specified as a Simulink bus containing a MATLAB structure. See Group Signals or Messages into Virtual Buses (Simulink). The structure has the form:

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures. The first `NumDetections` of these detections are actual detections. |

The definitions of the object detection structures are
found in the **Detections** output port descriptions of
the Driving Radar Data Generator and Vision Detection Generator blocks.

**Note**

The object detection structure contains a
`Time` field. The time tag of each object
detection must be less than or equal to the time of the current
invocation of the block. The time tag must also be greater than
the update time specified in the previous invocation of the
block.

### **Prediction Time** — Track update time real scalar

Track update time, specified as a real scalar. The multi-object
tracker updates all tracks to this time. Update time must always
increase with each invocation of the block. Units are in seconds.

**Note**

The object detection structure contains a
`Time` field. The time tag of each object
detection must be less than or equal to the time of the current
invocation of the block. The time tag must also be greater than
the update time in the previous invocation of the block.

#### Dependencies

To enable this port, set **Prediction time
source** to `Input
port`.

### **Cost Matrix** — Cost matrix real-valued *N*t-by-*N*d matrix

Cost matrix, specified as a real-valued
*N*t-by-*N*d
matrix, where *N*t is the number
of existing tracks and *N*d is
the number of current detections.

The rows of the cost matrix correspond to the existing tracks. The
columns correspond to the detections. Tracks are ordered as they appear
in the list of tracks in the **All Tracks** output port
of the previous invocation of the block.

In the first update to the multi-object tracker, or if the track has
no previous tracks, assign the cost matrix a size of [0,
*N*d]. The cost must be
calculated so that lower costs indicate a higher likelihood that the
multi-object tracker assigns a detection to a track. To prevent certain
detections from being assigned to certain tracks, use
`Inf`.

#### Dependencies

To enable this port, select **Enable cost matrix
input**.

### **Detectable Track IDs** — Detectable track IDs real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix

Detectable track IDs, specified as a real-valued
*M*-by-1 vector or *M*-by-2 matrix.
Detectable tracks are tracks that the sensors expect to detect. The
first column of the matrix contains a list of track IDs that the sensors
report as detectable. The optional second column contains the detection
probability for the track.

Tracks whose identifiers are not included in **Detectable
Track IDs** are considered undetectable. The track deletion
logic does not count the lack of detection as a "missed detection" for
track deletion purposes.

If this port is not enabled, the tracker assumes all tracks to be
detectable at each invocation of the block.

#### Dependencies

To enable this port, in the **Port Setting** tab,
select **Enable detectable track IDs
Input**.

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

Confirmed tracks, returned as a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink).

This table shows the structure fields.

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

This table shows the fields of each track structure.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks. |
| `BranchID` | Unique track branch identifier used to distinguish multiple track branches. |
| `SourceIndex` | Unique source index used to distinguish tracking sources in a multiple tracker environment. |
| `UpdateTime` | Time at which the track is updated. Units are in seconds. |
| `Age` | Number of times the track was updated. |
| `State` | Value of state vector at the update time. |
| `StateCovariance` | Uncertainty covariance matrix. |
| `ObjectClassID` | Integer value representing the object classification. The value `0` represents an unknown classification. Nonzero classifications apply only to confirmed tracks. |
| `TrackLogic` | Confirmation and deletion logic type. This value is always `'History'` for radar sensors, to indicate history-based logic. |
| `TrackLogicState` | Current state of the track logic type, returned as a 1-by-*K* logical array. *K* is the number of latest track logical states recorded. In the array, `1` denotes a hit and `0` denotes a miss. |
| `IsConfirmed` | Confirmation status. This field is `true` if the track is confirmed to be a real target. |
| `IsCoasted` | Coasting status. This field is `true` if the track is updated without a new detection. |
| `IsSelfReported` | Indicate if the track is reported by the tracker. This field is used in a track fusion environment. It is returned as `true` by default. |
| `ObjectAttributes` | Additional information about the track. |

For more details about these fields, see `objectTrack`.

A track is confirmed if:

- At least *M* detections are assigned to
  the track during the first *N* updates
  after track initialization. To specify the values
  *M* and *N*, use the
  **M and N for the M-out-of-N
  confirmation** parameter.
- The detection initiating the track has an
  `ObjectClassID` greater than
  zero.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks, returned as a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink). A track is tentative before it
is confirmed.

This table shows the structure fields.

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

This table shows the fields of each track structure.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks. |
| `BranchID` | Unique track branch identifier used to distinguish multiple track branches. |
| `SourceIndex` | Unique source index used to distinguish tracking sources in a multiple tracker environment. |
| `UpdateTime` | Time at which the track is updated. Units are in seconds. |
| `Age` | Number of times the track was updated. |
| `State` | Value of state vector at the update time. |
| `StateCovariance` | Uncertainty covariance matrix. |
| `ObjectClassID` | Integer value representing the object classification. The value `0` represents an unknown classification. Nonzero classifications apply only to confirmed tracks. |
| `TrackLogic` | Confirmation and deletion logic type. This value is always `'History'` for radar sensors, to indicate history-based logic. |
| `TrackLogicState` | Current state of the track logic type, returned as a 1-by-*K* logical array. *K* is the number of latest track logical states recorded. In the array, `1` denotes a hit and `0` denotes a miss. |
| `IsConfirmed` | Confirmation status. This field is `true` if the track is confirmed to be a real target. |
| `IsCoasted` | Coasting status. This field is `true` if the track is updated without a new detection. |
| `IsSelfReported` | Indicate if the track is reported by the tracker. This field is used in a track fusion environment. It is returned as `true` by default. |
| `ObjectAttributes` | Additional information about the track. |

For more details about these fields, see `objectTrack`.

#### Dependencies

To enable this port, select **Enable tentative tracks
output**.

### **All Tracks** — All tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks, returned as a
Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink).

This table shows the structure fields.

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

This table shows the fields of each track structure.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks. |
| `BranchID` | Unique track branch identifier used to distinguish multiple track branches. |
| `SourceIndex` | Unique source index used to distinguish tracking sources in a multiple tracker environment. |
| `UpdateTime` | Time at which the track is updated. Units are in seconds. |
| `Age` | Number of times the track was updated. |
| `State` | Value of state vector at the update time. |
| `StateCovariance` | Uncertainty covariance matrix. |
| `ObjectClassID` | Integer value representing the object classification. The value `0` represents an unknown classification. Nonzero classifications apply only to confirmed tracks. |
| `TrackLogic` | Confirmation and deletion logic type. This value is always `'History'` for radar sensors, to indicate history-based logic. |
| `TrackLogicState` | Current state of the track logic type, returned as a 1-by-*K* logical array. *K* is the number of latest track logical states recorded. In the array, `1` denotes a hit and `0` denotes a miss. |
| `IsConfirmed` | Confirmation status. This field is `true` if the track is confirmed to be a real target. |
| `IsCoasted` | Coasting status. This field is `true` if the track is updated without a new detection. |
| `IsSelfReported` | Indicate if the track is reported by the tracker. This field is used in a track fusion environment. It is returned as `true` by default. |
| `ObjectAttributes` | Additional information about the track. |

For more details about these fields, see `objectTrack`.

#### Dependencies

To enable this port, select **Enable all tracks
output**.
## Parameters
```yaml
parameters:
- name: Tracker identifier
  summary: Unique tracker identifier 0 (default) | nonnegative integer
  group: Tracker Management
- name: Filter initialization function name
  summary: Kalman filter initialization function initcvkf (default) | function name
  group: Tracker Management
- name: Threshold for assigning detections to tracks
  summary: Detection assignment threshold 30.0 (default) | positive real scalar
  group: Tracker Management
- name: M and N for the M-out-of-N confirmation
  summary: Confirmation parameters for track creation [2,3] (default) | two-element vector of positive integers
  group: Tracker Management
- name: P and R for the P-out-of-R deletion
  summary: Track deletion threshold [5 5] (default) | real-valued 1-by-2 vector of positive integers
  group: Tracker Management
- name: Maximum number of tracks
  summary: Maximum number of tracks 200 (default) | positive integer
  group: Tracker Management
- name: Maximum number of sensors
  summary: Maximum number of sensors 20 (default) | positive integer
  group: Tracker Management
- name: Out-of-sequence measurements handling
  summary: Out-of-sequence measurements handling Terminate (default) | neglect
  group: Tracker Management
- name: Track state parameters
  summary: Parameters of track state reference frame structure | structure array
  group: Tracker Management
- name: Update track state parameters with time
  summary: Update track state parameters with time off (default) | on
  group: Tracker Management
- name: Prediction time source
  summary: Source for prediction time Input port (default) | Auto
  group: Inputs and Outputs
- name: Enable cost matrix input
  summary: Enable input port for cost matrix off (default) | on
  group: Inputs and Outputs
- name: Enable detectable track IDs input
  summary: Enable detectable track IDs input off (default) | on
  group: Inputs and Outputs
- name: Source of output bus name
  summary: Source of output bus name Auto (default) | Property
  group: Inputs and Outputs
- name: Specify an output bus name
  summary: Name of output bus no default
  group: Inputs and Outputs
- name: Enable tentative tracks output
  summary: Enable output port for tentative tracks off (default) | on
  group: Inputs and Outputs
- name: Enable all tracks output
  summary: Enable output port for all tracks off (default) | on
  group: Inputs and Outputs
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: Inputs and Outputs
```

### Tracker Management

### **Tracker identifier** — Unique tracker identifier `0` (default) | nonnegative integer

Unique tracker identifier, specified as a nonnegative integer. This
parameter is used as the `SourceIndex` in the outputs,
and distinguishes tracks that come from different trackers in a
multiple-tracker system. You must specify this property as a positive
integer to use the track outputs as inputs to a track fuser.

**Example:** `1`

### **Filter initialization function name** — Kalman filter initialization function `initcvkf` (default) | function name

Kalman filter initialization function, specified as a function name.
The toolbox provides several initialization functions. For an example of
an initialization function, see `initcvekf`.

### **Threshold for assigning detections to tracks** — Detection assignment threshold `30.0` (default) | positive real scalar

Detection assignment threshold, specified as a positive real scalar.
To assign a detection to a track, the detection's normalized distance
from the track must be less than the assignment threshold. If some
detections remain unassigned to tracks that you want them assigned to,
then increase the threshold. If some detections are assigned to
incorrect tracks, decrease the threshold.

### **M and N for the M-out-of-N confirmation** — Confirmation parameters for track creation `[2,3]` (default) | two-element vector of positive integers

Confirmation parameters for track creation, specified as a two-element
vector of positive integers, `[M,N]`. A track is
confirmed when at least `M` detections are assigned to
the track during the first `N` updates after track
initialization. `M` must be less than or equal to
`N`.

- When setting `N`, consider the number of
  times you want the tracker to update before it confirms a
  track. For example, if a tracker updates every 0.05 seconds,
  and you allow 0.5 seconds to make a confirmation decision,
  set `N` = 10.
- When setting `M`, take into account the
  probability of object detection for the sensors. The
  probability of detection depends on factors such as
  occlusion or clutter. You can reduce `M`
  when tracks fail to be confirmed or increase
  `M` when too many false detections are
  assigned to tracks.

**Example:** `[3,5]`

### **P and R for the P-out-of-R deletion** — Track deletion threshold `[5 5]` (default) | real-valued 1-by-2 vector of positive integers

Track deletion threshold for history logic, specified as a real-valued
1-by-2 vector of positive integers `[P R]`. If a
confirmed track is not assigned to any detection `P`
times in the last `R` tracker updates, then the track
is deleted.

### **Maximum number of tracks** — Maximum number of tracks `200` (default) | positive integer

Maximum number of tracks that the block can process, specified as a
positive integer.

### **Maximum number of sensors** — Maximum number of sensors 20 (default) | positive integer

Maximum number of sensors that the block can process, specified as a
positive integer. This value should be greater than or equal to the
highest `SensorIndex` value used in the
**Detections** input port.

### **Out-of-sequence measurements handling** — Out-of-sequence measurements handling `Terminate` (default) | `neglect`

Out-of-sequence measurements handling, specified as `Terminate` or
`neglect`. Each detection has a timestamp associated with
it, *t*d, and the tracker block has it own
timestamp, *t*t, which is updated in each
invocation. The tracker block considers a measurement as an OOSM if
*t*d <
*t*t.

When the parameter is specified as:

- `Terminate` — The block stops running when it encounters any out-of-sequence measurements.
- `Neglect` — The block neglects any out-of-sequence measurements and continue to run.

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

### Inputs and Outputs

### **Prediction time source** — Source for prediction time `Input port` (default) | `Auto`

Source for prediction time, specified as `Input
port` or `Auto`. Select
`Input port` to input an update time by
using the **Prediction Time** input port. Otherwise,
the simulation clock managed by Simulink determines the update time.

**Example:** `Auto`

### **Enable cost matrix input** — Enable input port for cost matrix `off` (default) | `on`

Select this check box to enable the input of a cost matrix by using
the **Cost Matrix** input port.

### **Enable detectable track IDs input** — Enable detectable track IDs input `off` (default) | `on`

Select this check box to enable the **Detectable Track IDs** input port.

### **Source of output bus name** — Source of output bus name `Auto` (default) | `Property`

Source of output bus name, specified as `Auto` or
`Property`.

- If you select `Auto`, the block
  automatically creates a bus name.
- If you select `Property`, specify the bus
  name using the **Specify an output bus
  name** parameter.

### **Specify an output bus name** — Name of output bus no default

#### Dependencies

To enable this parameter, set the **Source of output bus
name** parameter to `Property`.

### **Enable tentative tracks output** — Enable output port for tentative tracks `off` (default) | `on`

Select this check box to enable the output of tentative tracks by
using the **Tentative Tracks** output port.

### **Enable all tracks output** — Enable output port for all tracks `off` (default) | `on`

Select this check box to enable the output of all the tracks by using
the **All Tracks** output port.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In `Interpreted
  execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C/C++
  code. The first time you run a simulation, Simulink generates C/C++ code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional startup
  time.
## Libraries

Automated Driving Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- When the filter initialization function specified in the block returns
  a `trackingEKF` or `trackingUKF` (Sensor Fusion and Tracking Toolbox) object, the
  block supports static memory allocation code generation.
- In code generation, if the detection inputs are specified in `double` precision, then the `NumTracks` field of the track outputs is returned as a `double` variable. If the detection inputs are specified in `single` precision, then the `NumTracks` field of the track outputs is returned as a `uint32` variable.

## Version History

**Introduced in R2017b**

## Description

Create and manage tracks of multiple objects

The Multi-Object Tracker block initializes, confirms, predicts,
corrects, and deletes the tracks of moving objects. Inputs to the multi-object tracker
are detection reports generated by Driving Radar Data
Generator and Vision Detection
Generator blocks. The multi-object tracker accepts detections from multiple
sensors and assigns them to tracks using a global nearest neighbor (GNN) criterion. Each
detection is assigned to a separate track. If the detection cannot be assigned to any
track, the multi-object tracker creates a new track.

A new track starts in a *tentative* state. If enough detections are
assigned to a tentative track, its status changes to *confirmed*.
When a track is confirmed, the multi-object tracker considers that track to represent a
physical object. If detections are not added to the track within a specifiable number of
updates, the track is deleted.

The multi-object tracker also estimates the state vector and state vector covariance
matrix for each track using a Kalman filter. These state vectors are used to predict a
track's location in each frame and determine the likelihood of each detection being
assigned to each track.
