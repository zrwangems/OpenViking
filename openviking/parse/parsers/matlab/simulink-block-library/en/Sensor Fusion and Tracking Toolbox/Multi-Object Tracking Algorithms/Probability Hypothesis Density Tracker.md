---
type: simulink-block
title: 'Probability Hypothesis Density (PHD) Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'probabilityhypothesisdensityphdtracker'
documentation_source_path: 'ref/probabilityhypothesisdensityphdtracker.html'
language: en
---

# Probability Hypothesis Density (PHD) Tracker

## Ports

### Input

### **Detections** — Detection list Simulink® bus containing MATLAB® structure

Detection list, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Integer. |
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
tracks to this time. The update time must increase with each invocation of the block.
Units are in seconds. The update time must be at least as large as the largest
`Time` specified at the **Detections** input
port.

If this port is not enabled, the simulation clock managed by Simulink determines
the update time.

#### Dependencies

To enable this port, in the **Port Setting** tab, set
**Prediction time source** to `Input
port`.

### **Sensor Configurations** — Configurations of tracking sensors Simulink bus containing MATLAB structure

Configurations of tracking sensors, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description | Type |
| --- | --- | --- |
| `NumConfigurations` | Number of sensor configurations | Integer. |
| `Configurations` | Sensor configurations | Array of sensor configuration structures. The first `NumConfigurations` of these configurations are actual configurations. The field names and definitions must correspond to names and values, respectively, of properties of the `trackingSensorConfiguration` object.  If you use a Radar Data Generator (Radar Toolbox) block in the tracking system, you can directly specify this value by using the **Configuration** output of the Radar Data Generator (Radar Toolbox) block, instead. |

#### Dependencies

To enable this port, in the **Tracker** tab, select the
**Update sensor configurations with time** parameter.

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
| `NumTracks` | Number of tracks. |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

The fields of the track structure are shown in Track Structure.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks, returned as a Simulink bus containing a MATLAB structure. A track is tentative before it is confirmed. The output of
this port has the same form as the output of the **Confirmed Tracks**
port.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable tentative tracks output**.

### **All Tracks** — Confirmed and Tentative tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks, returned as a Simulink bus containing a MATLAB structure. The output of this port has the same form as the output of
the **Confirmed Tracks** port.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable all tracks output**.

### **Info** — Additional information for analyzing track updates Simulink bus containing MATLAB structure

Additional information for analyzing track updates, returned as a Simulink bus containing a MATLAB structure.

This table shows the fields of the info structure:

|  |  |
| --- | --- |
| **Field** | **Description** |
| `CorrectionOrder` | The order in which sensors are used for state estimate correction, returned as a row vector of `SensorIndex` values. For example, [1 3 2 4]. |
| `TrackIDsAtStepBeginning` | Track IDs when the step began. |
| `DeletedTrackIDs` | IDs of tracks deleted during the step. |
| `TrackIDsAtStepEnd` | Track IDs when the step ended. |
| `SensorAnalysisInfo` | Cell array of sensor analysis information. |

The `SensorAnalysisInfo` field can include multiple sensor
information reports. Each report is a structure containing these fields:

|  |  |
| --- | --- |
| **Field** | **Description** |
| `SensorIndex` | Sensor index. |
| `DetectionCells` | Detection cells, returned as a logical matrix. Each column of the matrix denotes a detection cell. In each column, if the *i*th element is 1, then the *i*th detection belongs to the detection cell denoted by that column. |
| `DetectionLikelihoods` | The association likelihoods between components in the density function and detection cells, returned as an *N*-by-*P* matrix. *N* is the number of components in the density function, and *P* is the number of detection cells. |
| `IsBirthCells` | Indicates if the detection cells listed in `DetectionCells` give birth to new tracks, returned as a 1-by-*P* logical vector, where *P* is the number of detection cells. |
| `NumPartitions` | Number of partitions. |
| `DetectionProbability` | Probability of existing tracks being detected by the sensor, returned as a 1-by-*N* row vector, where *N* is the number of components in the density function. |
| `LabelsBeforeCorrection` | Labels of components in the density function before correction, return as a 1-by-*M*b row vector. *M*b is the number of components maintained in the tracker before correction. Each element of the vector is a `TrackID`. For example, [1 1 2 0 0]. Note that multiple components can share the same `TrackID`. |
| `LabelsAfterCorrection` | Labels of components in the density function after correction, returned as a 1-by-*M*a row vector. *M*a is the number of components maintained in the tracker after correction. Each element of the vector is a `TrackID`. For example, [1 1 1 2 2 0 0]. Note that multiple components can share the same `TrackID`. |
| `WeightsBeforeCorrection` | Weights of components in the density function before correction, returned as a 1-by-*M*b row vector. *M*b is the number of components maintained in the tracker before correction. Each element of the vector is the weight of the corresponding component in `LabelsBeforeCorrection`. For example, [0.1 0.5 0.7 0.3 0.2]. |
| `WeightsAfterCorrection` | Weights of components in the density function after correction, returned as a 1-by-*M*a row vector. *M*a is the number of components maintained in the tracker after correction. Each element of the vector is the weight of the corresponding component in `LabelsAfterCorrection`. For example, [0.1 0.4 0.2 0.6 0.3 0.2 0.2]. |

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable information output**.

## Parameters

#### Tracker Configuration

### **Tracker identifier** — Unique tracker identifier `0` (default) | nonnegative integer

Specify the unique tracker identifier as a nonnegative integer. This parameter is
passed as the `SourceIndex` in the tracker outputs, and distinguishes
tracks that come from different trackers in a multiple-tracker system. You must specify
this property as a positive integer to use the track outputs as inputs to a Track-To-Track Fuser
block.

**Example:** `1`

### **Detection partition function** — Function to partition detections into detection cells `partitionDetections` (default) | function name

Function to partition detections into detection cells, specified as a function name.
When each sensor can report more than one detection per object, you must use a partition
function. The partition function reports all possible partitions of the detections from
a sensor. In each partition, the detections are separated into mutually exclusive
detection cells, assuming that each detection cell belongs to one extended
object.

You can also specify your own detections partition function. For guidance in writing
this function, you can examine the details of the default partitioning function,
`partitionDetections`, using the `type`
command:

```
type partitionDetections
```

**Example:**
`myfunction`

### **Assignment threshold** — Threshold of selecting detections for component initialization `25` (default) | real positive scalar

Threshold of selecting detections for component initialization, specified as a
positive scalar. During correction, the tracker calculates the likelihood of association
between existing tracks and detection cells. If the association likelihood (given by
negative log-likelihood) of a detection cell to all existing tracks is higher than the
threshold (which means the detection cell has low likelihood of association to existing
tracks), the detection cell is used to initialize new components in the adaptive birth
density.

**Example:** `18.1`

**Data Types:** `single` | `double`

### **Maximum number of sensors** — Maximum number of sensors `20` (default) | positive integer

Maximum number of sensors that can be connected to the tracker, specified as a
positive integer. `MaxNumSensors` must be greater than or equal to
the largest value of `SensorIndex` found in all the detections used to
update the block.

**Data Types:** `single` | `double`

### **Maximum number of tracks** — Maximum number of tracks `1000` (default) | positive integer

Maximum number of tracks that the tracker can maintain, specified as a positive
integer.

**Data Types:** `single` | `double`

### **Maximum number of components** — Maximum number of components `1000` (default) | positive integer

Maximum number of components that the tracker can maintain, specified as a positive
integer.

**Data Types:** `single` | `double`

### **Sensor configurations** — Configurations of tracking sensors `struct('SensorIndex',1,'IsValidTime',true)` (default) | structure | structure array

Configuration of tracking sensors, specified as a structure or an array of
structures. This parameter provides the tracking sensor configuration information, such
as sensor detection limits and sensor resolution, to the tracker. The allowable field
names of each structure are the same as the property names of the `trackingSensorConfiguration` object. If you set the
`MaxDetsPerObject` field of the structure to `1`,
the tracker creates only one partition, such that at most one detection can be assigned
to each target.

You can update the configuration through the **Sensor
configurations** input port by selecting the **Update sensor
configurations with time** parameter.

### **Update sensor configurations with time** — Update sensor configurations with time `off` (default) | `on`

Select this parameter to enable the input port for tracking sensor configurations
through the **Sensor Configurations** input port.

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

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In the
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.

#### Track Management

### **Birth rate of new targets** — Birth rate of new targets in the density `1e-3` (default) | positive real scalar

Birth rate of new targets in the density, specified as a positive real scalar. Birth
rate indicates the expected number of targets added in the density per unit time. The
birth density is created by using the `FilterInitializationFcn` of
the sensor configuration used with the tracker. In general, the tracker adds components
to the density function in two ways:

1. Predictive birth density — This density is initialized by the
   `FilterInitializationFcn` function when called with no
   inputs.
2. Adaptive birth density — This density is initialized by the
   `FilterInitializationFcn` function when called with detection
   inputs. The tracker chooses detections based on their log-likelihood of
   association with the current estimates of the targets.

The value for the **Birth rate of new targets** parameter
represents the summation of both predictive birth density and adaptive birth density for
each time step.

**Example:** `0.01`

**Data Types:** `single` | `double`

### **Death rate of components** — Death rate of components in the density `1e-6` (default) | positive real scalar

Death rate of components in the density, specified as a positive real scalar. Death
rate indicates the rate at which a component vanishes in the density after one time
step. This equation illustrates how death rate
(*P*d) relates to the survival probability
(*P*s) of a component between successive time steps:

Ps=(1−Pd)ΔT

where *Δ**T* is the time
step.

**Example:** `1e-4`

**Data Types:** `single` | `double`

### **Threshold for initializing tentative tracks** — Threshold for initializing tentative track `0.5` (default) | positive real scalar

Threshold for initializing a tentative track, specified as a positive real scalar.
If the weight of a component is higher than the threshold, the component is labeled as a
`'Tentative'` track and given a `TrackID`.

**Example:** `0.45`

**Data Types:** `single` | `double`

### **Threshold for track confirmation** — Threshold for track confirmation `0.8` (default) | positive real scalar

Threshold for track confirmation, specified as a positive real scalar. In a PHD
tracker, a track can have multiple components sharing the same
`TrackID`. If the weight summation of the components of a tentative
track is higher than the confirmation threshold, the track status is marked as
`'Confirmed'`.

**Example:** `0.85`

**Data Types:** `single` | `double`

### **Threshold for track deletion** — Threshold for component deletion `1e-3` (default) | positive real scalar

Threshold for component deletion, specified as a positive real scalar. In the PHD
tracker, if the weight of a component is lower than the deletion threshold, the
component is deleted.

**Example:** `0.01`

**Data Types:** `single` | `double`

### **Threshold for components merging** — Threshold for components merging `25` (default) | positive real scalar

Threshold for components merging, specified as a positive real scalar. In the PHD
tracker, if the Kullback-Leibler distance between components with the same
`TrackID` is smaller than the merging threshold, then these
components are merged into one component. The merged weight of the new component is
equal to the summation of the weights of the pre-merged components. Moreover, if the
merged weight is higher than the first threshold specified in the **Thresholds
for label management** parameter, the merged weight is truncated to the first
threshold. Note that components with a `TrackID` of
`0` can also be merged with each other.

**Example:** 30

**Data Types:** `single` | `double`

### **Thresholds for label management** — Thresholds for label management `[1.1 1 0.8]` (default) | 1-by-3 vector of positive values

Labeling thresholds, specified as a 1-by-3 vector of decreasing positive values,
[*C*1,
*C*2,
*C*3]. Based on this parameter, the tracker
manages components in the density using these rules:

1. The weight of any component that is higher than the first threshold
   *C*1 is reduced to
   *C*1.
2. For all components with the same `TrackID`, if the largest
   weight among these components is greater than
   *C*2, then the component with the
   largest weight is preserved to retain the `TrackID`, while all
   other components are deleted.
3. For all components with the same `TrackID`, if the ratio of
   the largest weight to the weight summation of all these components is greater than
   *C*3, then the component with the
   largest weight is preserved to retain the `TrackID`, while all
   other components are deleted.
4. If neither condition 2 nor condition 3 is satisfied, then the component with
   the largest weight retains the `TrackID`, while the labels of all
   other components are set to `0`. When this occurs, it means that
   some components may represent other objects. This process retains the possibility
   for these unreserved components to be extracted again in the future.

#### Port Setting

### **Prediction time source** — Source of prediction time `Auto` (default) | `Input port`

Source for prediction time, specified as `Input port` or
`Auto`. Select `Input port` to input
an update time by using the **Prediction Time** input port. Otherwise,
the simulation clock managed by Simulink determines the update time.

### **Enable tentative tracks output** — Enable output port for tentative tracks `off` (default) | `on`

Select this parameter to enable the output of tentative tracks through the
**Tentative Tracks** output port.

### **Enable all tracks output** — Enable output port for all tracks `off` (default) | `on`

Select this parameter to enable the output of all tracks through the **All
Tracks** output port.

### **Enable information output** — Enable output port for analysis information `off` (default) | `on`

Select this parameter to enable the output of analysis information through the
**Info** output port.

### **Source of output bus name** — Source of output track bus name `Auto` (default) | `Property`

Source of the output track bus name, specified as:

- `Auto` — The block automatically creates an output
  track bus name.
- `Property` — Specify the output track bus name by
  using the **Specify an output bus name** parameter.

### **Source of output info bus name** — Source of output information bus name `Auto` (default) | `Property`

Source of the output information bus name, specified as:

- `Auto` — The block automatically creates an output
  information bus name.
- `Property` — Specify the output information bus name
  by using the **Specify an output info bus name**
  parameter.

#### Dependencies

To enable this parameter, on the **Port Setting** tab, select
**Enable information output**.

## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- In code generation, if the detection inputs are specified in `double` precision, then the `NumTracks` field of the track outputs is returned as a `double` variable. If the detection inputs are specified in `single` precision, then the `NumTracks` field of the track outputs is returned as a `uint32` variable.

- The tracker supports *strict single-precision* code generation
  with these restrictions:

  - You must specify the filter initialization function as single-precision in
    each tracking sensor configuration structure.
  - The filter specified in each tracking sensor configuration structure must use
    motion and measurement models that support single-precision.

  For details on *strict single-precision* code generation, see
  Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.
- The tracker supports *non-dynamic memory allocation* code
  generation with these restrictions:

  - You must specify the `MaxNumDetections` and
    `MaxNumDetsPerObject` fields in each tracking sensor
    configuration structure as finite integers.
  - You must specify the **Maximum number of components**
    parameter as a finite integer.
  - You must specify the **Maximum number of tracks** parameter
    as a finite integer.

  For details on *non-dynamic memory allocation* code generation,
  see Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation.

## Version History

**Introduced in R2021a**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Multi-sensor, multi-object PHD tracker

The Probability Hypothesis Density (PHD) Tracker block creates and manages tracks of stationary and moving
objects in a multi-sensor environment. The tracker uses a multi-target probability hypothesis
density filter to estimate the states of point targets and extended objects. The PHD is
represented by a weighted summation of probability density functions, and peaks in the PHD are
extracted to represent possible targets. See Algorithms for more details.
