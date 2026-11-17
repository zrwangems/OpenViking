---
type: simulink-block
title: 'Track-To-Track Fuser'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'tracktotrackfuser'
documentation_source_path: 'ref/tracktotrackfuser.html'
language: en
---

# Track-To-Track Fuser

## Ports
```yaml
ports:
- name: Tracks
  summary: Track list Simulink bus containing MATLAB® structure
  direction: input
- name: Prediction Time
  summary: Track update time real scalar
  direction: input
- name: Source Configurations
  summary: Source configuration list Simulink bus containing MATLAB structure
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

### **Tracks** — Track list Simulink bus containing MATLAB® structure

Track list, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures |

The fields of the track structure are shown in Track Structure.

### **Prediction Time** — Track update time real scalar

Track update time, specified as a real scalar in seconds. The fuser updates all
tracks to this time. The update time must increase with each invocation of the block.
The update time must be at least as large as the largest `UpdateTime`
specified in the **Tracks** input port.

If this port is not enabled, the simulation clock managed by Simulink determines
the update time.

#### Dependencies

To enable this port, on the **Port Setting** tab, set
**Prediction time source** to `Input
port`.

### **Source Configurations** — Source configuration list Simulink bus containing MATLAB structure

Source configuration list, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumConfigurations` | Number of non-default source configurations. The field value must be less than the value specified in the **Maximum number of source configurations** parameter. |
| `Configurations` | Array of source configuration structures. |

The fields of the source configuration structure are:

| Field Name | Description |
| --- | --- |
| `SourceIndex` | Unique index for the source system, specified as a positive integer. |
| `IsInternalSource` | Indicate if the source is internal to the fuser, specified as `true` or `false`. An internal source is a source that the fuser directly fuses tracks from even if the tracks are not self reported. For example, if the fuser is at the vehicle level, a tracking radar installed on the associated vehicle is considered internal, while another vehicle that reports fused tracks is considered external. |
| `IsInitializingCentralTracks` | Indicate if the source can initialize a central track in the fuser, specified as `true` or `false`. A central track is a track maintained in the fuser. |
| `LocalToCentralTransformFcn` | Function to transform a track from local to central state space, specified as a string or character vector containing the name of the transform function. |
| `CentralToLocalTransformFcn` | Function to transform a track from central to local state space, specified as a string or character vector containing the name of the transform function. |

#### Dependencies

To enable this port, on the **Fuser Management** tab, select
the **Update source configurations with time** parameter.

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
| `Tracks` | Array of track structures of a length set by the **Maximum number of central tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

The fields of the track structure are shown in Track Structure.

A track is confirmed if it satisfies the threshold specified in the**Confirmation threshold** parameter on the **Tracks** tab.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks, returned as a Simulink bus containing a MATLAB structure. A track is tentative before it is confirmed.

The structure has the form:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks. |
| `Tracks` | Array of track structures of a length set by the **Maximum number of central tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

The fields of the track structure are shown in Track Structure.

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable tentative tracks output**.

### **All Tracks** — Confirmed and tentative tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks, returned as a Simulink bus containing a MATLAB structure.

The structure has the form:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks. |
| `Tracks` | Array of track structures of a length set by the **Maximum number of central tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

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
| `BranchIDsAtStepBeginning` | Branch IDs when the update began. |
| `CostMatrix` | Cost of assignment matrix. |
| `Assignments` | Assignments returned from the `assignTOMHT` function. |
| `UnassignedTracks` | IDs of unassigned branches returned from the tracker. |
| `UnassignedDetections` | IDs of unassigned detections returned from the tracker. |
| `InitialBranchHistory` | Branch history after branching and before pruning. |
| `InitialBranchScores` | Branch scores before pruning. |
| `KeptBranchHistory` | Branch history after initial pruning. |
| `KeptBranchScores` | Branch scores after initial pruning. |
| `Clusters` | Logical array mapping branches to clusters. Branches belong in the same cluster if they share detections in their history or belong to the same track either directly or through other branches. |
| `TrackIncompatibility` | Branch incompatibility matrix. The `(i,j)` element is `true` if the *i*-th and *j*-th branches have shared detections in their history or belong to the same track. |
| `GlobalHypotheses` | Logical matrix mapping branches to global hypotheses. Compatible branches can belong in the same hypotheses. |
| `GlobalHypScores` | Total score of global hypotheses. |
| `PrunedBranches` | Logical array of branches that the `pruneTrackBranches` function determines to prune. |
| `GlobalBranchProbabilities` | Global probability of each branch existing in the global hypotheses. |
| `BranchesDeletedByPruning` | Branches deleted by the tracker. |
| `BranchIDsAtStepEnd` | Branch IDs when the update ended. |

#### Dependencies

To enable this port, on the **Port Setting** tab, select
**Enable information output**.
## Parameters
```yaml
parameters:
- name: Fuser Index
  summary: Unique index for track fuser 1 (default) | positive integer
  group: ''
- name: Assignment algorithm name
  summary: Assignment algorithm MatchPairs (default) | Munkres | Jonker-Volgenant | Auction | Custom
  group: ''
- name: Name of 'Custom' assignment function
  summary: Name of 'Custom' assignment function function name
  group: ''
- name: Threshold for assigning source to central tracks
  summary: Threshold for assigning source to central tracks [1 Inf]*30.0 (default) | positive scalar | 1-by-2 vector of positive
    values
  group: ''
- name: Maximum number of central tracks
  summary: Maximum number of central tracks 100 (default) | positive integer
  group: ''
- name: Maximum number of source configurations
  summary: Maximum number of source configurations 20 (default) | positive integer
  group: ''
- name: Source configurations
  summary: Configuration of source systems struct('SourceIndex',1) (default) | array of source configuration structures
  group: ''
- name: Update source configurations with time
  summary: Update source configurations with time off (default) | on
  group: ''
- name: Track state parameters
  summary: Parameters of track state reference frame structure | structure array
  group: ''
- name: Update track state parameters with time
  summary: Update track state parameters with time off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code Generation
  group: ''
- name: Confirmation threshold [M N]
  summary: Threshold for central track confirmation [2 3] (default) | positive integer | real-valued 1-by-2 vector of positive
    integers
  group: ''
- name: Deletion threshold [P Q]
  summary: Threshold for central track deletion [5 5] (default) | positive integer | real-valued 1-by-2 vector of positive
    integers
  group: ''
- name: Central track state size
  summary: Central track state size 6 (default) | positive integer
  group: ''
- name: Central track object attributes
  summary: Central track object attributes struct (default) | structure
  group: ''
- name: State transition function
  summary: State transition function constvel (default) | function name
  group: ''
- name: State transition Jacobian function
  summary: State transition Jacobian function function name
  group: ''
- name: Process noise matrix
  summary: Process noise matrix eye(3) (default) | positive real scalar | positive definite matrix
  group: ''
- name: Enable additive process noise
  summary: Enable additive process noise off (default) | on
  group: ''
- name: State fusion function
  summary: State fusion function Cross (default) | Intersection | Custom
  group: ''
- name: Name of 'Custom' fusion function
  summary: Name of custom assignment function function name
  group: ''
- name: State fusion parameters source
  summary: State fusion parameters source Auto (default) | Property
  group: ''
- name: Cross covariance factor
  summary: Cross covariance factor 0.4 (default) | scalar in range (0,1)
  group: ''
- name: Optimize covariance based on
  summary: Intersection algorithm criteria det (default) | trace
  group: ''
- name: State fusion custom algorithm parameters
  summary: State fusion custom algorithm parameters MATLAB variable
  group: ''
- name: Fuse only confirmed source tracks
  summary: Fuse only confirmed source tracks on (default) | off
  group: ''
- name: Fuse coasted source tracks
  summary: Fuse only confirmed source tracks off (default) | on
  group: ''
- name: Prediction time source
  summary: Source of prediction time Auto (default) | Input port
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
```

#### Fuser Management

### **Fuser Index** — Unique index for track fuser `1` (default) | positive integer

Unique index for the fuser, specified as a positive integer. Use this property to
distinguish different fusers in a multiple-fuser environment.

**Example:**
`2`

### **Assignment algorithm name** — Assignment algorithm `MatchPairs` (default) | `Munkres` | `Jonker-Volgenant` | `Auction` | `Custom`

Assignment algorithm, specified as `MatchPairs`,
`Munkres`, `Jonker-Volgenant`,
`Auction`, or `Custom`. Munkres is the only
assignment algorithm that guarantees an optimal solution, but it is also the slowest,
especially for large numbers of detections and tracks. The other algorithms do not
guarantee an optimal solution but can be faster for problems with 20 or more tracks and
detections. Use `Custom` to define your own assignment function and
specify its name in the **Name of 'Custom' assignment function**
parameter.

**Data Types:** `char`

### **Name of 'Custom' assignment function** — Name of 'Custom' assignment function function name

Name of 'Custom' assignment function, specified as a function name. An assignment
function must have the following
syntax:

```
 [assignments,unassignedCentral,unassignedLocal] = myfun(cost,costNonAssignment)
```

For
an example of an assignment function and a description of its arguments, see `assignmunkres`.

**Example:** `myfun`

#### Dependencies

To enable this property, set the **Assignment algorithm name**
parameter to `Custom`.

### **Threshold for assigning source to central tracks** — Threshold for assigning source to central tracks `[1 Inf]*30.0` (default) | positive scalar | 1-by-2 vector of positive values

Threshold for assigning source to central tracks, specified as a positive scalar or
a 1-by-2 vector of form [*C*1
*C*2], where
*C*1 ≤
*C*2. If specified as a scalar, the specified
value, *val*, is expanded to [*val*
`Inf`].

Initially, the fuser executes a coarse estimation for the normalized distance
between all the source and central tracks. The fuser only calculates the accurate
normalized distance for the source and central combinations whose coarse normalized
distance is less than *C*2. Also, the fuser can
only assign a local track to a central track if their accurate normalized distance is
less than *C*1. See Algorithms for an explanation
of the normalized distance.

**Tip**

- Increase the value of *C*2 if there
  are combinations of source and central tracks that should be calculated for
  assignment but are not. Decrease it if the calculation takes too much time.
- Increase the value of *C*1 if there
  are source tracks that should be assigned to central tracks but are not. Decrease
  it if there are local tracks that are assigned to central tracks they should not
  be assigned to (too far away).

### **Maximum number of central tracks** — Maximum number of central tracks `100` (default) | positive integer

Maximum number of central tracks that the tracker can maintain, specified as a
positive integer.

### **Maximum number of source configurations** — Maximum number of source configurations `20` (default) | positive integer

Maximum number of source configurations that the fuser can maintain, specified as a
positive integer.

### **Source configurations** — Configuration of source systems `struct('SourceIndex',1)` (default) | array of source configuration structures

Configuration of source systems, specified as an array of source configuration
structures. The fields of a source configuration structure are:

| Field Name | Description |
| --- | --- |
| `SourceIndex` | Unique index for the source system, specified as a positive integer. |
| `IsInternalSource` | Indicate if the source is internal to the fuser, specified as `true` or `false`. An internal source is a source that the fuser directly fuses tracks from even if the tracks are not self reported. For example, if the fuser is at the vehicle level, a tracking radar installed on the associated vehicle is considered internal, while another vehicle that reports fused tracks is considered external. |
| `IsInitializingCentralTracks` | Indicate if the source can initialize a central track in the fuser, specified as `true` or `false`. A central track is a track maintained in the fuser. |
| `LocalToCentralTransformFcn` | Function to transform a track from local to central state space, specified as a string or character vector containing the name of the transform function. |
| `CentralToLocalTransformFcn` | Function to transform a track from central to local state space, specified as a string or character vector containing the name of the transform function. |

### **Update source configurations with time** — Update source configurations with time `off` (default) | `on`

Select this parameter to enable the input of source configurations through the
**Source configurations** input port.

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

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code Generation`

Select a simulation type from these options:

- `Interpreted execution` — Simulate the model using the MATLAB interpreter. This option shortens startup time. In `Interpreted execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent simulations as long as the model does not change. This option requires additional startup time.

#### Tracks

### **Confirmation threshold [M N]** — Threshold for central track confirmation `[2 3]` (default) | positive integer | real-valued 1-by-2 vector of positive integers

Threshold for central track confirmation, specified as a positive integer,
*M*, or a real-valued 1-by-2 vector of positive integers,
[*M*
*N*]. A central track is confirmed if it is assigned to local tracks at
least *M* times in the last *N* updates. If specified
as a positive integer, *M*, the confirmation threshold is expanded to
[*M*
*M*].

### **Deletion threshold [P Q]** — Threshold for central track deletion `[5 5]` (default) | positive integer | real-valued 1-by-2 vector of positive integers

Threshold for central track deletion, specified as a positive integer,
*P*, or a 1-by-2 vector of positive integers [*P*
*Q*] with *P*
*≤*
*Q*. A central track is deleted if the track is not assigned to local
tracks at least *P* times in the last *Q* updates. If
specified a positive integer *P*, the confirmation threshold is
expanded to [*P*
*P*].

### **Central track state size** — Central track state size `6` (default) | positive integer

Central track state size, specified as a positive integer.

### **Central track object attributes** — Central track object attributes `struct` (default) | structure

Central track object attributes, specified as a structure. The tracker passes the
value of this parameter to the `ObjectAttributes` field of the track
output.

### **State transition function** — State transition function `constvel` (default) | function name

State transition function, specified as a function name. This function calculates
the state at time step *k* based on the state at time step
*k*–1.

- If the **Enable additive process noise** parameter on the
  **Tracks** tab is enabled, the function must use the following syntax:

  ```
  x(k) = f(x(k-1),dt)
  ```

  where:

  - `x(k)` — The estimated state at time
    `k`, specified as a vector or a matrix. If specified as a
    matrix, then each column of the matrix represents one state vector.
  - `dt` — The time step for prediction.
- If the **Enable additive process noise** parameter on the
  **Tracks** tab is not enabled, the function must use this syntax:

  ```
  x(k) = f(x(k-1),w(k-1),dt)
  ```

  where:

  - `x(k)` — The estimated state at time
    `k`, specified as a vector or a matrix. If specified as a
    matrix, then each column of the matrix represents one state vector.
  - `w(k)` — The process noise at time
    `k`.
  - `dt` — The time step for prediction.

**Example:** `@constacc`

### **State transition Jacobian function** — State transition Jacobian function function name

Jacobian of the state transition function, specified as a function name. If not
specified, the Jacobian is numerically computed, which may increase processing time and
numerical inaccuracy. If specified, the function must support one of these two syntaxes:

- If the **Enable additive process noise** parameter on the
  **Tracks** tab is enabled, the function must use this syntax:

  ```
  Jx(k) = statejacobianfcn(x(k),dt)
  ```

  where:

  - `x(k)` — The estimated state at time
    `k`, specified as an *M*-by-1 vector of
    real values.
  - `dt` — The time step for prediction.
  - `Jx(k)` — The Jacobian of the state transition function
    with respect to the state, `df/dx`, evaluated at
    `x(k)`. The Jacobian is returned as an
    *M*-by-*M* matrix.
- If the **Enable additive process noise** parameter on the
  **Tracks** tab is not enabled, the function must use this syntax::

  ```
  [Jx(k),Jw(k)] = statejacobianfcn(x(k),w(k),dt)
  ```

  where:

  - `x(k)` — The (estimated) state at time
    `k`, specified as an *M*-by-1 vector of
    real values.
  - `w(k)` — The process noise at time
    `k`, specified as a *W*-by-1 vector of
    real values.
  - `dt` — The time step for prediction.
  - `Jx(k)` — The Jacobian of the state transition function
    with respect to the state, `df/dx`, evaluated at
    `x(k)`. The Jacobian is returned as an
    *M*-by-*M* matrix.
  - `Jw(k)` — The Jacobian of the state transition function
    with respect to the process noise, `df/dw`, evaluated at
    `x(k)` and `w(k)`. The Jacobian is
    returned as an *M*-by-*W* matrix.

**Example:** `@constaccjac`

### **Process noise matrix** — Process noise matrix `eye(3)` (default) | positive real scalar | positive definite matrix

Process noise covariance matrix, specified as a positive real scalar or a positive
definite matrix.

- When the **Enable additive process noise** parameter on the
  **Tracks** tab is enabled, specify the process noise covariance
  as a positive real scalar or a positive definite
  *M*-by-*M* matrix. *M* is the
  dimension of the state vector. When specified as a scalar, the matrix is an
  *M*-by-*M* diagonal matrix with each diagonal
  element equal to the scalar.
- When the **Enable additive process noise** parameter on the
  **Tracks** tab is not enabled, specify the process noise
  covariance as a *W*-by-*W* matrix.
  *W* is the dimension of the process noise vector.

**Example:** `[1.0 0.05; 0.05 2`]

### **Enable additive process noise** — Enable additive process noise `off` (default) | `on`

Enable additive process noise, specified as `on` or
`off`. When it is `on`, process noise is added to
the state vector. Otherwise, noise is incorporated into the state transition
function.

#### Fusion

### **State fusion function** — State fusion function `Cross` (default) | `Intersection` | `Custom`

State fusion function, specified as one of those options:

- `Cross` — Uses the cross-covariance fusion algorithm
- `Intersection` — Uses the covariance intersection fusion
  algorithm
- `Custom` — Enables you to specify a customized fusion
  function using the **Name of 'Custom' fusion function**
  parameter

Use the **State fusion parameters source** parameter to specify
additional parameters used by the state fusion algorithm.

### **Name of 'Custom' fusion function** — Name of custom assignment function function name

Name of custom assignment function, specified as a string or function name.

The state fusion function must support one of the following syntaxes:

```
[fusedState,fusedCov] = f(trackState,trackCov)
[fusedState,fusedCov] = f(trackState,trackCov,fuseParams)
```

where:

- `trackState` is specified as an
  *N*-by-*M* matrix. *N* is the
  dimension of the track state, and *M* is the number of tracks.
- `trackCov` is specified as an
  *N*-by-*N*-by-*M* matrix.
  *N* is the dimension of the track state, and
  *M* is the number of tracks.
- `fuseParams` is the optional parameters defined in the
  **State fusion parameters source** parameter.
- `fusedState` is returned as an *N*-by-1
  vector.
- `fusedCov` is returned as an
  *N*-by-*N* matrix.

#### Dependencies

To enable this property, set the **State fusion function**
parameter to `Custom`.

### **State fusion parameters source** — State fusion parameters source `Auto` (default) | `Property`

State fusion parameters source, specified as one of these options:

- `Auto` — The block uses the default value fusion
  parameters for each sate fusion algorithm. See **Cross covariance
  factor**, **Optimize covariance based on**, and
  **State fusion custom algorithm parameters** for more
  details.
- `Property` — Set state fusion parameters using

  - **Cross covariance factor** parameter when
    **State fusion function** is selected as
    `Cross`.
  - **Optimize covariance based on** parameter when
    **State fusion function** is selected as
    `Intersection`.
  - **State fusion custom algorithm parameters** parameter
    when **State fusion function** is selected as
    `Custom`.

### **Cross covariance factor** — Cross covariance factor `0.4` (default) | scalar in range (0,1)

Cross covariance factor, specified as a scalar in the range (0,1). See `fusexcov`
for more details.

### **Optimize covariance based on** — Intersection algorithm criteria `det` (default) | `trace`

Intersection algorithm criteria, specified as `det` or
`trace`. See `fusecovint`
for more details.

### **State fusion custom algorithm parameters** — State fusion custom algorithm parameters MATLAB variable

State fusion custom algorithm parameters, specified in any variable type, as long as
it matches the setup of the optional `fuseParams` input of the custom
state fusion function, specified in the **Name of 'Custom' assignment
function** parameter.

### **Fuse only confirmed source tracks** — Fuse only confirmed source tracks `on` (default) | `off`

Fuse only confirmed source tracks, specified as `on` or
`off`. Set this parameter to `off` if you want to
fuse all source tracks regardless of their confirmation status.

### **Fuse coasted source tracks** — Fuse only confirmed source tracks `off` (default) | `on`

Fuse coasted source tracks, specified as `off` or
`on`. Set this parameter to `on` if you want to fuse
coasted source tracks. Set it to `off` if you want to only fuse source
tracks that are not coasted.

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

Select this parameter to enable the output of all the tracks through the
**All Tracks** output port.

### **Enable information output** — Enable output port for analysis information `off` (default) | `on`

Select this parameter to enable the output port for analysis information through the
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
  using the **Fuser info bus name** parameter.
## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Track-to-Track Fusion

The Track-to-Track Fuser
Simulink® block is a multi-source, multi-object, track-level fuser that uses the global
nearest neighbor (GNN) association to maintain a single hypothesis about the tracks it fuses.
The inputs to the block are tracks from sources that already track multiple objects, like
multi-object tracker blocks or other track-to-track fuser blocks. The input tracks are called
*source* or *local tracks*, whereas the tracks
maintained in the fuser are called *central tracks*.
