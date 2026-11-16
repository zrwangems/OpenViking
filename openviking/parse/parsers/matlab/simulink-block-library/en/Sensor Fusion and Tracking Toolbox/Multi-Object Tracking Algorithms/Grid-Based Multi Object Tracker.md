---
type: simulink-block
title: 'Grid-Based Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'gridbasedmultiobjecttracker'
documentation_source_path: 'ref/gridbasedmultiobjecttracker.html'
language: en
---

# Grid-Based Multi Object Tracker

## Ports

### Input

### **Sensor Data** — Sensor data Simulink® bus containing MATLAB® structure

Sensor data, specified as a Simulink bus containing a MATLAB structure. The structure contains these fields:

| Field | Description |
| --- | --- |
| `NumSensors` | Number of sensors, specified as a nonnegative integer. |
| `SensorData` | Sensor data, specified as an array of sensor data structures. The first `NumSensors` elements of the array are actual detections. |

Each `SensorData` structure contains these
fields::

| Field | Description |
| --- | --- |
| `Time` | Measurement time, specified as a nonnegative scalar. |
| `SensorIndex` | Unique identifier of the sensor, specified as a positive integer. |
| `Measurement` | Object measurements, specified a *K*-by-*M* matrix. *K* is the dimension of each measurement and *M* is the number of measurements. Each measurement defines the positional aspects of the detection in a rectangular or spherical frame. |
| `MeasurementParameters` | Measurement parameters, specified as a structure describing the transformation from the particle state to the measurement. See the `MeasurementParameter` property of the `objectDetection` object for details on setting up this field. |
| `NumMeasurements` | Number of measurements or number of points in the point cloud sensor detections, specified as a positive integer. |

**Note**

The `Time` field of each structure must be less than or equal
to the time of the current invocation of the block. The time must also be greater
than the update time specified in the previous invocation of the block.

### **Prediction Time** — Track update time real scalar

Track update time, specified as a real scalar in seconds. The tracker updates all
tracks to this time. The update time must increase with each invocation of the block,
and must be at least as large as the largest `Time` specified to the
**Sensor Data** input port.

If this port is not enabled, the simulation clock managed by Simulink determines
the update time.

#### Dependencies

To enable this port, in the **Port Setting** tab, set the
**Prediction time source** parameter to `Input
port`.

### **Sensor Configurations** — Configurations of tracking sensors Simulink bus containing MATLAB structure

Configurations of the tracking sensors, specified as a Simulink bus containing a MATLAB structure. The structure contains these fields:

| Field | Description |
| --- | --- |
| `NumConfigurations` | Number of sensor configurations, specified as a positive integer. |
| `Configurations` | Sensor configurations, specified as an array of sensor configuration structures. The first `NumConfigurations` elements of the array are actual configurations. The field names and definitions must correspond to names and values, respectively, of properties of the `trackingSensorConfiguration` object. The tracker ignores the `FilterInitializationFcn`, `SensorTransformFcn`, and `MaxNumDetsPerObject` fields, even when you specify them in the structure.  If you use a Radar Data Generator (Radar Toolbox) block in the tracking system, you can directly specify this value by using the **Configuration** output of the Radar Data Generator (Radar Toolbox) block, instead. |

#### Dependencies

To enable this port, in the **Tracker Configuration** tab,
select the **Update sensor configurations with time**
parameter.

### **State Parameters** — Track state parameters Simulink bus containing MATLAB structure

Track state parameters, specified as a Simulink bus containing a MATLAB structure. The block uses this structure as the value of the
`StateParameters` field of the generated tracks. You can use
these parameters to define the reference frame in which the block report tracks as
well as other desirable attributes of the generated tracks.

For example, you can use a structure with these fields to define a rectangular
reference frame with origin position at `[10 10 0]` meters and
origin velocity of `[2 -2 0]` meters per second, with respect to the
scenario frame.

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### Dependencies

To enable this port, in the **Tracker Configuration** tab,
select the **Update track state parameters with time**
parameter.
### Output

### **Confirmed Tracks** — Confirmed tracks Simulink bus containing MATLAB structure

Confirmed tracks updated to the current time, returned as a Simulink bus containing a MATLAB structure. The structure contains these fields:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks. |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` element of the array are actual tracks. |

The fields of the track structure are shown in Track Structure. The state form of
each track follows the form specified in the **Motion model for
tracking** parameter.

### **Tentative Tracks** — Tentative tracks Simulink bus containing MATLAB structure

Tentative tracks updated to the current time, returned as a Simulink bus containing a MATLAB structure. A track is tentative before it is confirmed.

The structure contains these fields:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` elements of the array are actual tracks. |

The fields of the track structure are shown in Track Structure. The state form of
each track follows the form specified in the **Motion model for
tracking** parameter.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable tentative tracks output**.

### **All Tracks** — Confirmed and Tentative tracks Simulink bus containing MATLAB structure

Combined list of confirmed and tentative tracks updated to the current time,
returned as a Simulink bus containing a MATLAB structure.

The structure contains these fields:

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` elements of the array are actual tracks. |

The fields of the track structure are shown in Track Structure. The state form of
each track follows the form specified in the **Motion model for
tracking** parameter.

#### Dependencies

To enable this port, in the **Port Setting** tab, select
**Enable all tracks output**.

## Parameters

#### Tracker Configuration

### **Tracker identifier** — Unique tracker identifier `0` (default) | nonnegative integer

Specify the unique tracker identifier as a nonnegative integer. This parameter is
passed as the `SourceIndex` in the tracker outputs, and distinguishes
tracks that come from different trackers in a multiple-tracker system. You must specify
this property as a positive integer to use the track outputs as inputs to a Track-To-Track Fuser
block.

**Example:** `1`

### **Maximum number of tracks** — Maximum number of tracks `100` (default) | positive integer

Maximum number of tracks that the block can maintain, specified as a positive
integer.

### **Maximum number of sensors** — Maximum number of sensors `20` (default) | positive integer

Specify the maximum number of sensors that can be connected to the tracker as a
positive integer. `MaxNumSensors` must be greater than or equal to
the largest value of `SensorIndex` found in all the sensor data used to
update the block.

**Data Types:** `single` | `double`

### **Sensor configurations** — Configurations of tracking sensors `struct('SensorIndex',1,'IsValidTime',true,'SensorLimits',[-180 180; 0 100])` (default) | structure | structure array

Specify the configurations of tracking sensors as a structure or an array of
structures. This parameter provides the tracking sensor configuration information, such
as sensor detection limits and sensor resolution, to the tracker. You must specify these
fields for each structure:

| Field Name | Format |
| --- | --- |
| `SensorIndex` | Unique identifier of the sensor, specified as a positive integer. |
| `IsValidTime` | Indicate if the sensor data should be used to update tracks, specified as `true` or `false`. |
| `SensorTransformParameters` | Parameters of the sensor transform function, specified as a *p*-element array of measurement parameter structures. *p* is the number of sensors. Each structure should contain fields with the same names as the measurement parameters used in a measurement function, such as the `cvmeas` function.  The first structure must describe the transformation from the autonomous system to the sensor coordinates. The subsequent structure describes the transformation from the autonomous system to the tracking coordinate frame. If you only provide one structure, the tracker assumes tracking is performed in the coordinate frame of the autonomous system. |
| `SensorLimits` | Sensor detection limits, specified as a 2-by-2 matrix. The first row specifies the lower and upper limits of the azimuth angle in degrees. The second row specifies the lower and upper limits of the detection range in meters. |

The other allowed field names of each structure correspond to the
property names of the `trackingSensorConfiguration` object. The tracker ignores the
`FilterInitializationFcn`, `SensorTransformFcn`,
and `MaxNumDetsPerObject` fields, even when you specify them in the
structure.

You can update the configurations by using the **Sensor
configurations** input port after selecting the **Update sensor
configurations with time** parameter.

### **Update sensor configurations with time** — Update sensor configurations with time `off` (default) | `on`

Select this parameter to enable the **Sensor Configurations** input
port. This enables you to update tracking sensor configurations during the
simulation.

### **Track state parameters** — Parameters of track state reference frame structure

Specify the parameters of the track state reference frame as a structure. The block
passes the value of this parameter to the `StateParameters` field of
the generated tracks. You can use these parameters to define the reference frame in
which the block reports tracks, as well as other desirable attributes of the generated
tracks.

For example, you can use a structure with these fields to define a rectangular
reference frame with origin position at `[10 10 0]` meters and origin
velocity of `[2 -2 0]` meters per second with respect to the scenario
frame.

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

You can update the track state parameters through the **State
Parameters** input port by selecting the **Update track state
parameters with time** parameter.

**Data Types:** `struct`

### **Update track state parameters with time** — Update track state parameters with time `off` (default) | `on`

Select this parameter to enable the input port for track state
parameters through the **State
Parameters** input port.

### **Enable GPU computation** — Enable GPU computation `off` (default) | `on`

Select this parameter to enable using GPU for the estimation of the dynamic grid
map. Enabling GPU computation requires the Parallel Computing Toolbox™.

### **X-dimension of grid** — X-dimension of grid `100` (default) | positive scalar

Specify the x-dimension of the grid in the local coordinates as a positive scalar,
in meters.

### **Y-dimension of grid** — Y-dimension of grid `100` (default) | positive scalar

Specify the y-dimension of the grid in the local coordinates as a positive scalar,
in meters.

### **Resolution of grid** — Resolution of grid `1` (default) | positive scalar

Specify the resolution of the grid as a positive scalar. The resolution represents
the number of cells per meter of the grid for both the x- and y-directions of the
grid.

### **Grid origin** — Origin of grid `[-50 -50]` (default) | positive scalar

Specify the origin of the grid in the local coordinate frame as a two-element vector
of scalars, in meters.

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

#### Particle Filtering

### **Motion model for tracking** — Motion model for tracking `constant-velocity` (default) | `constant-acceleration` | `constant-turnrate`

Select the motion model for tracking as
`constant-velocity`,
`constant-acceleration`, or
`constant-turnrate`.

The particle state and object state for each motion model are:

| Motion Model | Particle State | Object State |
| --- | --- | --- |
| `constant-velocity` | `[x; vx; y; vy]` | `[x; vx; y; vy; yaw; L; W]` |
| `constant-acceleration` | `[x; vx; ax; y; vy; ay]` | `[x; vx; ax; y; vy; ay; yaw; L; W]` |
| `constant-turn-rate` | `[x; vx; y; vy; w]` | `[x; vx; y; vy; w; yaw; L; W]` |

where:

- `x` — Position of the object in the x-direction of the local
  tracking frame (m)
- `y` — Position of the object in the y-direction of the local
  tracking frame (m)
- `vx` — Velocity of the object in the x-direction of the local
  tracking frame (m/s)
- `vy` — Velocity of the object in the y-direction of the local
  tracking frame (m/s)
- `ax` — Acceleration of the object in the x-direction of the
  local tracking frame (m/s2)
- `ay` — Acceleration of the object in the y-direction of the
  local tracking frame (m/s2)
- `w` — Yaw-rate of the object in the local tracking frame
  (deg/s)
- `yaw` — Yaw angle of the object in the local tracking frame
  (deg)
- `L` — Length of the object (m)
- `W` — Width of the object (m)

### **Minimum and maximum velocity of objects (m/s)** — Minimum and maximum velocities of objects (m/s) `[-10 10; -10 10]` (default) | 2-by-2 matrix of scalar

Specify the minimum and maximum velocities of objects as a 2-by-2 matrix of scalars
in m/s. The first row specifies the lower and upper velocity limits in the x-direction,
and the second row specifies the lower and upper velocity limits in the y-direction. The
tracker uses these limits to sample new particles in the grid using a uniform
distribution.

### **Enable additive process noise** — Enable additive process noise `false` (default) | `true`

Select this parameter to model process noise as additive. When selected, process
noise is added directly to the state vector. Otherwise, noise is incorporated in the
motion model.

### **Process noise covariance matrix** — Process noise covariance matrix `eye(2)` (default) | *N*-by-*N* matrix

Specify process noise covariance as an *N*-by-*N*
matrix. This parameter specifies the process noise for positions of particles and the
geometric centers of targets.

- If you select the **Enable additive process noise**
  parameter, the process noise adds directly to the prediction model. In this case,
  *N* is equal to the dimension of the particle state in the
  **Motion model for tracking** parameter.
- If you do not select the **Enable additive process noise**
  parameter, define the process noise according to the selected motion model. The
  model adds process noise to the higher-order terms, such as acceleration for the
  `constant-velocity` model.

  | `MotionModel` | Number of Terms for Acceleration | Meaning of Terms |
  | --- | --- | --- |
  | `constant-velocity` | `2` | Acceleration in the x- and y- directions |
  | `constant-acceleration` | `2` | Jerk in the x- and y- directions |
  | `constant-turn-rate` | `3` | Acceleration in the x- and y- directions, as well as the angular acceleration |

**Example:** `[1.0 0.05; 0.05 2]`

### **Number of persistent particles** — Number of persistent particles `1e5` (default) | positive integer

Specify the number of persistent particles per grid as a positive integer. A higher
number of particles can improve estimation quality, but can increase computational cost.

### **Number of new-born particles per step** — Number of new-born particles per step `1e4` (default) | positive scalar

Specify the number of new-born (initialized) particles per time step as a positive
integer. The tracker determines the locations of these new-born particles by using the
mismatch between the predicted and the updated occupancy belief masses and the
**Probability of birth in a cell per step** parameter. A reasonable
value of this parameter is approximately 10 percent of the number of particles specified
by the **Number of persistent particles** parameter.

### **Probability of birth in a cell per step** — Probability of birth in a cell per step `0.01` (default) | scalar in range `[0, 1)`

Specify the probability of target birth in a cell per step as a scalar in the range
`[0, 1)`. The birth probability controls the
probability that new particles are generated in a cell.

**Example:** `1e-4`

### **Death rate of targets per unit time** — Death rate of targets per unit time `1e-3` (default) | positive scalar

Specify the death rate of targets per unit time as a positive scalar. Death rate
indicates the possibility that a particle or target vanishes after each time step. Death
rate (*P*d) influences the survival probability
(*P*s) of a component across successive time
steps as:

Ps=(1−Pd)ΔT

where *Δ**T* is the number of time
steps.

**Example:** `1e-4`

### **Confidence in free space prediction** — Confidence in free space prediction `0.8` (default) | scalar

Specify the confidence in free space prediction as a scalar. In the prediction stage
of the tracker, this parameter reduces the belief mass of a cell to be in the "free"
(unoccupied) state as:

mk|k−1(F)=αΔTmk−1(F)

where *k* is the time step index,
*m* is the belief mass, *α* is the factor
representing the confidence in free space prediction, and
*Δ**T* is the time step.

### **Random number generation** — Method of random number seed generation `Repeatable` (default) | `Not repeatable` | `Specify seed`

Select the method of random number seed generation as
`Repeatable`, `Not repeatable`, or
`Specify seed`.

- `Repeatable` — The block uses the same random
  seed every time.
- `Not repeatable` — The block uses a different
  random seed every time.
- `Specify seed` — Specify a random seed for the
  block using the **Initial Seed** parameter.

### **Initial Seed** — Initial seed for randomization `0` (default) | nonnegative integer

Specify the initial seed for randomization in the block as a nonnegative
integer.

#### Dependencies

To enable this parameter, select the **Random number generation**
parameter as `Specify seed`.

#### Track Management

### **Clustering method for new object extraction** — Clustering method for new object extraction `DBSCAN` (default) | `Custom`

Specify the clustering method used for new object extraction as
`DBSCAN` or `Custom`.

- `DBSCAN` — Cluster unassigned dynamic grid cells using the
  density-based spatial clustering of applications with noise (DBSCAN) algorithm.
  You can configure the DBSCAN algorithm by specifying the **Threshold for
  DBSCAN clustering** and **Minimum number of cells per cluster
  for DBSCAN** parameters.
- `Custom` — Cluster unassigned dynamic grid cells using a
  custom clustering function specified in the **Name of 'Custom' clustering
  function** parameter.

### **Threshold for DBSCAN clustering** — Threshold for DBSCAN clustering `5` (default) | positive scalar

Specify the threshold for DBSCAN clustering as a positive scalar.

#### Dependencies

To enable this parameter, select the **Clustering method for new object
extraction** parameter as `DBSCAN`.

### **Minimum number of cells per cluster for DBSCAN** — Minimum number of cells per cluster for DBSCAN `2` (default) | positive integer

Specify the minimum number of cells per cluster for DBSCAN as a positive integer.
This parameter affects whether a point is a core point in the DBSCAN algorithm.

#### Dependencies

To enable this parameter, select the **Clustering method for new object
extraction** parameter as `DBSCAN`.

### **Name of 'Custom' clustering function** — Name of custom clustering function function name

Specify the name of the custom function for clustering unassigned grid cells as a
function name. The function must support this
signature:

```
function indices = myFunction(dynamicGridCells)
```

where
`dynamicGridCells` is a structure that defines a set of grid cells
initializing the track. It must have these fields:

| Field | Description |
| --- | --- |
| `Width` | Width of the cell, specified as a positive scalar. |
| `GridIndices` | Indices of the grid cells, specified as an *N*-by-2 array, where *N* is the number of unassigned cells. The first element specifies the grid index in the x-direction and the second element specifies the grid index in the y-direction. |
| `State` | States of the grid cells, specified as a *P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
| `StateCovariance` | State covariances of the grid cells, specified as a *P*-by-*P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
| `OccupancyMass` | Occupancy belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |
| `FreeMass` | Free belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |

The custom function must return `indices` as an
*N*-element vector of indices that defines the cluster index for each
dynamic grid cell.

#### Dependencies

To enable this parameter, select the **Clustering method for new object
extraction** parameter as `Custom`.

### **Function to initialize tracks from grid cell sets** — Function to initialize tracks from grid cell sets `trackerGridRFS.defaultTrackInitialization` (default) | function name

Specify the function used to initialize new tracks as a function name. The
initialization function initiates a track from a set of dynamic grid cells.

The default initialization function merges the Gaussian estimates from cells to
describe the state of the object. The orientation of the object aligns with the
direction of its mean velocity. With a defined orientation, the length and width of the
object are extracted using the geometric properties of the cells. The block calculates
uncertainties in length, width, and orientation estimates using linear
approximations.

If you choose to use your own initialization function, the function must support
this
signature:

```
function track = myFunction(dynamicGridCells)
```

where
`dynamicGridCells` is a structure that defines a set of grid cells
initializing the track. It has these fields:

| Field | Description |
| --- | --- |
| `Width` | Width of the cell, specified as a positive scalar. |
| `GridIndices` | Indices of the grid cells, specified as an *N*-by-2 array, where *N* is the number of unassigned cells. The first element specifies the grid index in the x-direction and the second element specifies the grid index in the y-direction. |
| `State` | States of the grid cells, specified as a *P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
| `StateCovariance` | State covariances of the grid cells, specified as a *P*-by-*P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
| `OccupancyMass` | Occupancy belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |
| `FreeMass` | Free belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |

The custom function must return `track` as an `objectTrack` object or a structure
with field names that correspond to the property names of an `objectTrack` object. The dimension
of the state must be the same as the state dimension specified in the **Motion
model for tracking** parameter.

**Example:** `myFunction`

### **Function to update existing tracks** — Function to update existing tracks `trackerGridRFS.defaultTrackUpdate` (default) | function name

Specify the function used to update an existing track using its associated set of
dynamic grid cells as a function name.

The default update function updates the `State` and
`StateCovariance` fields of the track using the new estimate from
the dynamic grid cells associated with the track. The update process is similar to the
initialization process for the **Function to initialize tracks from grid cell
sets** parameter. The tracker does not apply filtering to the state and state
covariance.

If you choose to customize your own update function, the function must support this signature:

```
function updatedTrack = TrackUpdateFcn(predictedTrack,dynamicGridCells)
```

where:

- `predictedTrack` is the predicted track of an object, specified
  as an `objectTrack` object.
- `dynamicGridCells` is a structure that defines a set
  of dynamic grid cells associated with the track. The structure has these
  fields:

  | Field | Description |
  | --- | --- |
  | `Width` | Width of the cell, specified as a positive scalar. |
  | `GridIndices` | Indices of the grid cells, specified as an *N*-by-2 array, where *N* is the number of unassigned cells. The first element specifies the grid index in the x-direction and the second element specifies the grid index in the y-direction. |
  | `State` | States of the grid cells, specified as a *P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
  | `StateCovariance` | State covariances of the grid cells, specified as a *P*-by-*P*-by-*N* array of scalars, where *P* is the dimension of the state and *N* is the number of unassigned cells. |
  | `OccupancyMass` | Occupancy belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |
  | `FreeMass` | Free belief mass of the cells, specified as an *N*-element vector, where *N* is the number of unassigned cells. |
- `updatedTrack` is the updated track, returned as an `objectTrack` object or a
  structure that has field names that correspond to the property names of an
  `objectTrack` object.

**Example:** `TrackUpdateFcn`

### **Threshold for assigning dynamic grid cells to tracks** — Threshold for assigning dynamic grid cells to tracks `30` (default) | positive scalar

Specify the threshold for assigning dynamic grid cells to tracks as a positive
scalar. A dynamic grid cell can only be associated to a track if its distance
(represented by the negative log-likelihood) to the track is less than the value of this parameter.

- Increase the threshold if a dynamic cell is not being assigned to a track that
  it should be assigned to.
- Decrease the threshold if there are dynamic cells being assigned to a track
  that they should be not assigned to.

**Example:** `18.1`

### **Confirmation threshold [M N]** — Threshold for track confirmation `[2 3]` (default) | 1-by-2 vector of positive integers

Specify the threshold for track confirmation as a 1-by-2 vector of positive
integers `[M N]`. A track is confirmed if it has been assigned to
dynamic grid cells in at least `M` updates of the last
`N` updates.

### **Deletion threshold [P Q]** — Threshold for track deletion `[5 5]` (default) | 1-by-2 vector of positive integers

Specify the threshold for track deletion as a 1-by-2 vector of positive integers
`[P Q]`. A track is deleted if has not been assigned to any dynamic
grid cell in at least `P` updates of the last `Q`
updates.

**Example:** `0.01`

**Data Types:** `single` | `double`

#### Visualization

### **Enable dynamic grid map visualization** — Enable dynamic grid map visualization `on` (default) | `off`

Select this parameter to enable the dynamic grid map visualization. If a current
axes exists, the block shows the dynamic map on the current axes. Otherwise, the block
creates an axes to show the map.

### **Plot velocity** — Enable velocity plotting `off` (default) | `on`

Select this parameter to enable velocity plotting on the dynamic grid map.

### **Fast update** — Enable updating from previous map `on` (default) | `off`

Select this parameter to enable updating from previous map. When selected, the
block plots the map via a lightweight update to the previous map in the figure.
Otherwise, the block plots a new map on the figure every time.

### **Invert colors** — Enable inverted colors `off` (default) | `on`

Select this parameter to enable inverted colors on the map. When selected, the
block plots empty space in white and occupied space in black. Otherwise, the block plots
empty space in black and occupied space in white.

#### Port Setting

### **Prediction time source** — Source of prediction time `Input port` (default) | `Auto`

Specify the source for prediction time as `Input port` or
`Auto`. Select `Input port` to input
an update time by using the **Prediction Time** input port. Otherwise,
the simulation clock managed by Simulink determines the update time.

### **Enable tentative tracks output** — Enable output port for tentative tracks `off` (default) | `on`

Select this parameter to enable the output of tentative tracks through the
**Tentative Tracks** output port.

### **Enable all tracks output** — Enable output port for all tracks `off` (default) | `on`

Select this parameter to enable the output of all the tracks through the
**All Tracks** output port.

### **Source of output bus name** — Source of output track bus name `Auto` (default) | `Property`

Source of the output track bus name, specified as:

- `Auto` — The block automatically creates an output
  track bus name.
- `Property` — Specify the output track bus name by
  using the **Specify an output bus name** parameter.

## Libraries

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The visualization of the grid map does not support code generation.

## Version History

**Introduced in R2021b**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Grid-based multi-object tracker using random finite set approach

The Grid-Based Multi Object Tracker is a tracker capable of processing
detections of multiple targets from multiple sensors in a 2-D environment. The tracker tracks
dynamic objects around an autonomous system using high resolution sensor data such as point
clouds and radar detections. The tracker uses the random finite set (RFS) based approach,
combined with Dempster-Shafer approximations [1], to estimate the dynamic
characteristics of the grid cells. To extract objects from the grid, the tracker uses a
cell-to-track association scheme [2]. For more details, see
Algorithms.
