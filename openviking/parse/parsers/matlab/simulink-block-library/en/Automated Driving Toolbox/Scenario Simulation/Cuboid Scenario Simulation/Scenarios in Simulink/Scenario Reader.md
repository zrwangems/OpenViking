---
type: simulink-block
title: 'Scenario Reader'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Cuboid Scenario Simulation / Scenarios in Simulink'
documentation_page: 'scenarioreader'
documentation_source_path: 'ref/scenarioreader.html'
language: en
---

# Scenario Reader

## Ports

### Input

### **Ego Vehicle** — Ego vehicle pose Simulink bus containing MATLAB® structure

Ego vehicle pose, specified as a Simulink bus containing a MATLAB structure.

The structure must have these fields.

| Field | Description |
| --- | --- |
| `ActorID` | Scenario-defined actor identifier, specified as a positive integer. |
| *In R2024b:*  `FrontAxlePosition` | Front-axle position of the vehicle, specified as a three-element row vector in the form [*x* *y* *z*]. Units are in meters.  **Note**  If the driving scenario does not contain a front-axle trajectory for at least one vehicle, then the `ActorPoses` structure does not contain this field. |
| `Position` | Position of actor, specified as a real-valued vector of the form [*x* *y* *z*]. Units are in meters. |
| `Velocity` | Velocity (*v*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*v**x* *v**y* *v**z*]. Units are in meters per second. |
| `Roll` | Roll angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Pitch` | Pitch angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Yaw` | Yaw angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `AngularVelocity` | Angular velocity (*ω*) of actor in the *x*-, *y*-, and *z*-directions, specified as a real-valued vector of the form [*ω**x* *ω**y* *ω**z*]. Units are in degrees per second. |

Output the ego vehicle pose when you are converting actors from ego
vehicle coordinates to world coordinates for use in the 3D simulation environment. For
example, see Visualize Sensor Data from Unreal Engine Simulation Environment.

#### Dependencies

To enable this port, set these parameters in this order:

1. Set the **Coordinate system of actors output** parameter
   to `Vehicle coordinates`.
2. Set the **Source of ego vehicle** parameter to
   `Input port`.
### Output

### **Actors** — Scenario actor poses Simulink bus containing MATLAB structure

Scenario actor poses, returned as a Simulink bus containing a MATLAB structure.

The structure has these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | Number of actors | Nonnegative integer |
| `Time` | Current simulation time | Real-valued scalar |
| `Actors` | Actor poses | `NumActors`-length array of actor pose structures |

Each actor pose structure in `Actors` has these fields.

| Field | Description |
| --- | --- |
| `ActorID` | Scenario-defined actor identifier, specified as a positive integer. |
| *In R2024b:*  `FrontAxlePosition` | Front-axle position of the vehicle, specified as a three-element row vector in the form [*x* *y* *z*]. Units are in meters.  **Note**  If the driving scenario does not contain a front-axle trajectory for at least one vehicle, then the `ActorPoses` structure does not contain this field. |
| `Position` | Position of actor, specified as a real-valued vector of the form [*x* *y* *z*]. Units are in meters. |
| `Velocity` | Velocity (*v*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*v**x* *v**y* *v**z*]. Units are in meters per second. |
| `Roll` | Roll angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Pitch` | Pitch angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Yaw` | Yaw angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `AngularVelocity` | Angular velocity (*ω*) of actor in the *x*-, *y*-, and *z*-directions, specified as a real-valued vector of the form [*ω**x* *ω**y* *ω**z*]. Units are in degrees per second. |

The pose of the ego vehicle is excluded from the `Actors`
array.

To return actor poses from the block, you must run the entire driving scenario
simulation to completion.

### **Lane Boundaries** — Scenario lane boundaries Simulink bus containing MATLAB structure

Scenario lane boundaries, returned as a Simulink bus containing a MATLAB structure.

The structure has these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumLaneBoundaries` | Number of lane boundaries | Nonnegative integer |
| `Time` | Current simulation time | Real scalar |
| `LaneBoundaries` | Lane boundaries starting from the leftmost lane with respect to the ego vehicle. | `NumLaneBoundaries`-length array of lane boundary structures |

Each lane boundary structure in `LaneBoundaries` has these
fields.

|  |  |
| --- | --- |
| **Field** | **Description** |
| `Coordinates` | Lane boundary coordinates, specified as a real-valued *N*-by-3 matrix, where *N* is the number of lane boundary coordinates. Lane boundary coordinates define the position of points on the boundary at specified longitudinal distances away from the ego vehicle, along the center of the road.  - In MATLAB, specify these distances by using the   `'XDistance'` name-value pair argument of   the `laneBoundaries` function. - In Simulink, specify these distances by using the   **Distances from ego vehicle for computing   boundaries (m)** parameter of the Scenario   Reader block or the **Distance from parent   for computing lane boundaries** parameter of the   Simulation 3D Vision Detection Generator   block.  This matrix also includes the boundary coordinates at zero distance from the ego vehicle. These coordinates are to the left and right of the ego-vehicle origin, which is located under the center of the rear axle. Units are in meters. |
| `Curvature` | Lane boundary curvature at each row of the `Coordinates` matrix, specified as a real-valued *N*-by-1 vector. *N* is the number of lane boundary coordinates. Units are in radians per meter. |
| `CurvatureDerivative` | Derivative of lane boundary curvature at each row of the `Coordinates` matrix, specified as a real-valued *N*-by-1 vector. *N* is the number of lane boundary coordinates. Units are in radians per square meter. |
| `HeadingAngle` | Initial lane boundary heading angle, specified as a real scalar. The heading angle of the lane boundary is relative to the ego vehicle heading. Units are in degrees. |
| `LateralOffset` | Lateral offset of the ego vehicle position from the lane boundary, specified as a real scalar. An offset to a lane boundary to the left of the ego vehicle is positive. An offset to the right of the ego vehicle is negative. Units are in meters. In this image, the ego vehicle is offset 1.5 meters from the left lane and 2.1 meters from the right lane.  Ego vehicle in a driving lane |
| `BoundaryType` | Type of lane boundary marking, specified as one of these values:  - `'Unmarked'` — No physical lane marker   exists - `'Solid'`  — Single unbroken line - `'Dashed'` — Single line of dashed lane   markers - `'DoubleSolid'` — Two unbroken lines - `'DoubleDashed'` — Two dashed lines - `'SolidDashed'` — Solid line on the left and   a dashed line on the right - `'DashedSolid'` — Dashed line on the left and   a solid line on the right |
| `Strength` | Saturation strength of the lane boundary marking, specified as a real scalar from 0 to 1. A value of `0` corresponds to a marking whose color is fully unsaturated. The marking is gray. A value of `1` corresponds to a marking whose color is fully saturated. |
| `Width` | Lane boundary width, specified as a positive real scalar. In a double-line lane marker, the same width is used for both lines and for the space between lines. Units are in meters. |
| `Length` | Length of dash in dashed lines, specified as a positive real scalar. In a double-line lane marker, the same length is used for both lines. |
| `Space` | Length of space between dashes in dashed lines, specified as a positive real scalar. In a dashed double-line lane marker, the same space is used for both lines. |

The number of returned lane boundary structures depends on the **Lane
boundaries to output** parameter value.

#### Dependencies

To enable this port, set these parameters in this order:

1. Set the **Coordinate system of actors output** parameter
   to `Vehicle coordinates`.
2. Set the **Lane boundaries to output** parameter to
   `Ego lane boundaries` or `All lane
   boundaries`.

### **Ego Vehicle Pose** — Ego vehicle pose Simulink bus containing MATLAB structure

Ego vehicle pose, returned as a Simulink bus containing a MATLAB structure.

The structure must contain these fields.

| Field | Description |
| --- | --- |
| `ActorID` | Scenario-defined actor identifier, specified as a positive integer. |
| *In R2024b:*  `FrontAxlePosition` | Front-axle position of the vehicle, specified as a three-element row vector in the form [*x* *y* *z*]. Units are in meters.  **Note**  If the driving scenario does not contain a front-axle trajectory for at least one vehicle, then the `ActorPoses` structure does not contain this field. |
| `Position` | Position of actor, specified as a real-valued vector of the form [*x* *y* *z*]. Units are in meters. |
| `Velocity` | Velocity (*v*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*v**x* *v**y* *v**z*]. Units are in meters per second. |
| `Roll` | Roll angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Pitch` | Pitch angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Yaw` | Yaw angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `AngularVelocity` | Angular velocity (*ω*) of actor in the *x*-, *y*-, and *z*-directions, specified as a real-valued vector of the form [*ω**x* *ω**y* *ω**z*]. Units are in degrees per second. |

#### Dependencies

To enable this port, set these parameters in this order:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Source of ego vehicle** parameter to
   `Scenario`.
3. Select the **Output ego vehicle pose** parameter.

### **Ego Vehicle State** — Ego vehicle state Simulink bus containing MATLAB structure

Ego vehicle state, returned as a Simulink bus containing a MATLAB structure.

The structure must contain these
fields.

| Field | Description |
| --- | --- |
| `Position` | Position of actor, specified as a real-valued vector of the form [*x* *y* *z*]. Units are in meters. |
| `Velocity` | Velocity (*v*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*v**x* *v**y* *v**z*]. Units are in meters per second. |
| `Orientation` | Orientation of actor, specified as a real-valued vector of [`roll pitch yaw`] angles. Units are in degrees. |
| `AngularVelocity` | Angular velocity (*ω*) of actor in the *x*-, *y*-, and *z*-directions, specified as a real-valued vector of the form [*ω**x* *ω**y* *ω**z*]. Units are in degrees per second. |
| `Acceleration` | Acceleration (*a*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*a**x* *a**y* *a**z*]. Units are in meters per second squared. |

#### Dependencies

To enable this port, set these parameters in this order:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Source of ego vehicle** parameter to
   `Scenario`.
3. Select the **Output ego vehicle state** parameter.

## Parameters

#### Scenario

### **Source of driving scenario** — Source of driving scenario `From file` (default) | `From workspace`

Source of driving scenario, specified as one of these options:

- `From file` — In the **Driving Scenario
  Designer file name** parameter, specify the name of a scenario file that
  was saved from the Driving Scenario
  Designer app.
- `From workspace` — In the **MATLAB or model
  workspace variable name** parameter, specify the name of a MATLAB or model workspace variable that contains a `drivingScenario` object.

### **Driving Scenario Designer file name** — Scenario file name `EgoVehicleGoesStraight.mat` (default) | scenario file on MATLAB search path | path to scenario file

Scenario file name, specified as a scenario file on the MATLAB search path or as the full path to a scenario file. A scenario file must
be a MAT-file saved from the Driving Scenario
Designer app. If the **Source of ego vehicle** parameter is set
to `Scenario`, then the scenario must contain an ego vehicle.
Otherwise, the block returns an error during simulation.

If the specified scenario file contains sensors, the block ignores them. To include
sensors from the scenario in your model, see Tips.

The default scenario file shows an ego vehicle traveling north on a straight,
two-lane road, with another vehicle traveling south in the opposite lane.

To add a scenario file to the MATLAB search path, use the `addpath` function. For example, this code adds the set of folders
containing prebuilt Euro NCAP® scenarios to the MATLAB search path.

```
path = fullfile(matlabroot,'toolbox','shared','drivingscenario', ...
'PrebuiltScenarios','EuroNCAP');
addpath(genpath(path))
```

In the **Driving Scenario Designer file name** parameter, you can
then specify the name of any scenario located in these folders, without having to
specify the full file path. For example:
`AEB_PedestrianChild_Nearside_50width.mat`.

When you are done using the scenario in your models, you can remove any added
folders from the MATLAB search path by using the `rmpath` function.

```
rmpath(genpath(path))
```

#### Dependencies

To enable this parameter, set the **Source of driving scenario**
parameter to `From file`.

### **MATLAB or model workspace variable name** — Scenario variable name `scenario` (default) | `drivingScenario` object variable name

Scenario variable name, specified as the name of a MATLAB or model workspace variable that contains a valid `drivingScenario` object. If a scenario variable with the same name appears in
both the MATLAB and model workspace, the block uses the variable defined in the model
workspace.

If the **Source of ego vehicle** parameter is set to
`Scenario`, then the `drivingScenario` object
must contain an ego vehicle. To designate which actor in the object is the ego vehicle,
in the **Ego vehicle ActorID** parameter, specify the
`ActorID` property value of that actor.

The default variable name, `scenario`, is the default name of
`drivingScenario` objects produced by the MATLAB functions that are exported from the Driving Scenario
Designer app. By default, this variable is not included in the MATLAB or model workspace.

#### Dependencies

To enable this parameter, set the **Source of driving scenario**
parameter to `From workspace`.

### **Coordinate system of actors output** — Coordinate system of actors output `Vehicle coordinates` (default) | `World coordinates`

Coordinate system of the output actors, specified as one of these values:

- `Vehicle coordinates` — Coordinates are defined with
  respect to the ego vehicle. Select this value when your scenario has only one ego
  vehicle.
- `World coordinates` — Coordinates are defined with
  respect to the driving scenario. Select this value in multi-agent scenarios that
  contain more than one ego vehicle. If you select this value, model visualization
  using the Bird's-Eye
  Scope is not supported.

For more details on the vehicle and world coordinate systems, see Coordinate Systems in Automated Driving Toolbox.

### **Source of ego vehicle** — Source of ego vehicle `Scenario` (default) | `Input port`

Source of ego vehicle, specified as one of these options:

- `Scenario` — Use the ego vehicle defined in the
  scenario that is specified by the **Driving Scenario Designer file
  name** or **MATLAB or model workspace variable name**
  parameter. The pose of the ego vehicle is excluded from the
  **Actors** output port. Actor positions are in vehicle
  coordinates, meaning that they are relative to the world coordinate position of the
  ego vehicle in the scenario.

  Select this option to test open-loop ADAS algorithms, where the ego vehicle
  behavior is predefined and does not change as the scenario advances. For an example,
  see Test Open-Loop ADAS Algorithm Using Driving Scenario.
- `Input port` — Specify the ego vehicle by using the
  **Ego Vehicle** input port. The pose of the ego vehicle is not
  included in the **Actors** output port.

  With this option, the ego vehicle in your model must include a starting position
  that is in world coordinates. All other actor poses are in vehicle coordinates and
  are positioned relative to the ego vehicle. For an example of an ego vehicle with
  defined position information, see Lane Keeping Assist with Lane Detection. When defining
  the starting position of the ego vehicle, consider using the position that is
  already defined in the scenario. By using this position, if you set **Source
  of ego vehicle** to `Scenario` and then back to
  `Input port`, you do not have to manually change the
  starting position.

  Select this option to test closed-loop ADAS algorithms, where the ego vehicle
  reacts to changes as the scenario advances. For an example, see Test Closed-Loop ADAS Algorithm Using Driving Scenario.

#### Dependencies

To enable this parameter, set the **Coordinate system of actors
output** parameter to `Vehicle
coordinates`.

### **Ego vehicle ActorID** — Actor ID of ego vehicle `1` (default) | positive integer

Actor ID of ego vehicle, specified as a positive integer. Use this parameter to
simulate using the ego vehicle that is read from a `drivingScenario`
object.

- When **Source of ego vehicle** is set to
  `Scenario`, set this parameter to an
  `ActorID` value that is stored in the
  `Actors` property of the specified
  `drivingScenario` object. To check valid
  `ActorID` values, use this syntax, where
  `scenario` is the name of the `drivingScenario`
  variable name.

  ```
  actorIDs = [scenario.Actors.ActorID]
  ```
- When **Source of ego vehicle** is set to `Input
  Port`, you must set this parameter to the
  `ActorID` value at the **Ego Vehicle** input
  port of the block.

#### Dependencies

To enable this parameter, set these parameters in this order:

1. Set the **Source of driving scenario** parameter to
   `From workspace`.
2. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.

### **Output ego vehicle pose** — Output pose of ego vehicle `off` (default) | `on`

Select this parameter to output the pose of the ego vehicle at the **Ego
Vehicle Pose** port.

#### Dependencies

To enable this parameter, set the **Coordinate system of actors
output** parameter to `Vehicle coordinates` and
the **Source of ego vehicle** parameter to
`Scenario`.

### **Output ego vehicle state** — Output state of ego vehicle `off` (default) | `on`

Select this parameter to output the state of the ego vehicle at the **Ego
Vehicle State** port.

#### Dependencies

To enable this parameter, set the **Coordinate system of actors
output** parameter to `Vehicle coordinates` and
the **Source of ego vehicle** parameter to
`Scenario`.

To output ego vehicle state, you must create the trajectory of the ego vehicle
using the `smoothTrajectory` function in the driving scenario API or by selecting
**Use smooth, jerk-limited trajectory** parameter in the Driving Scenario
Designer app.

### **Ego vehicle follows ground** — Orient ego vehicle to follow road surface `off` (default) | `on`

Select this parameter to orient the ego vehicle to follow the elevation of the road
surface. The block updates the elevation, roll, pitch, and yaw of the ego vehicle and
outputs actors and lane boundaries relative to the updated ego vehicle coordinates. The
block does not update the velocity or angular velocity of the ego vehicle.

Use this parameter in closed-loop simulations where the elevation of the road
network varies.

**Note**

At the junctions of roads that have different elevations and banking angles, the
updated ego vehicle values might not be accurate.

In open-loop simulations, where **Source of ego vehicle** is set to
`Scenario`, the ego vehicle follows the elevation specified
in the driving scenario.

#### Dependencies

To enable this parameter, set **Coordinate system of actors
output** to `Vehicle coordinates` and
**Source of ego vehicle** to `Input
port`.

### **Sample time (s)** — Sample time of simulation `0.1` (default) | positive real scalar

Sample time of simulation, in seconds, specified as a positive real scalar.
Inherited and continuous sample times are not supported. This sample time is separate
from the sample times that the Driving Scenario Designer app and
`drivingScenario` object use during simulation.

#### Lanes

### **Lane boundaries to output** — Lane boundaries to output `None` (default) | `Ego vehicle lane boundaries` | `All lane boundaries`

Lane boundaries to output, specified as one of these options:

- `None` — Do not output any lane boundaries.
- `Ego vehicle lane boundaries` — Output the left and
  right lane boundaries of the ego vehicle.
- `All lane boundaries` — Output all lane boundaries of
  the road on which the ego vehicle is traveling.

If you select `Ego vehicle lane boundaries` or
`All lane boundaries`, then the block returns the lane
boundaries in the **Lane Boundaries** output port.

#### Dependencies

To enable this parameter, set the **Coordinate system of actors
output** parameter to `Vehicle
coordinates`.

### **Distances from ego vehicle for computing boundaries (m)** — Distances from ego vehicle at which to compute lane boundaries `linspace(-150,150,101)` (default) | *N*-element real-valued vector

Distances from the ego vehicle at which to compute the lane boundaries, specified as
an *N*-element real-valued vector. *N* is the number
of distance values. When detecting lanes from rear-facing cameras, specify negative
distances. When detecting lanes from front-facing cameras, specify positive distances.
Units are in meters.

By default, the block computes 101 lane boundaries over the range from 150 meters
behind the ego vehicle to 150 meters ahead of the ego vehicle. These distances are
linearly spaced 3 meters apart.

**Example:** `1:0.1:10` computes a lane boundary every 0.1 meters over
the range from 1 to 10 meters ahead of the ego vehicle.

#### Dependencies

To enable this parameter, set the **Lane boundaries to output**
parameter to `Ego vehicle lane boundaries` or
`All lane boundaries`.

### **Location of boundaries on lane markings** — Lane boundary location `Center of lane markings` (default) | `Inner edge of lane markings`

Lane boundary location on the lane markings, specified as one of the options in this
table.

| Lane Boundary Location | Description | Example |
| --- | --- | --- |
| `Center of lane markings` | Lane boundaries are centered on the lane markings. | A three-lane road has four lane boundaries: one per lane marking.  Three-lane road with four lane boundaries |
| `Inner edge of lane markings` | Lane boundaries are placed at the inner edges of the lane markings. | A three-lane road has six lane boundaries: two per lane.  Three-lane road with six lane boundaries |

#### Dependencies

To enable this parameter, set the **Lane boundaries to output**
parameter to `Ego vehicle lane boundaries` or
`All lane boundaries`.

#### Port Settings

### **Source of actors bus name** — Source of name for actor poses bus `Auto` (default) | `Property`

Source of the name for the actor poses bus returned in the **Actors** output port, specified as one of these options:

- `Auto` — The block automatically creates an actor poses bus name.
- `Property` — Specify the actor poses bus name by using the **Actors bus name** parameter.

### **Actors bus name** — Name of actor poses bus valid bus name

Name of the actor poses bus returned in the **Actors** output port, specified as a valid bus name.

#### Dependencies

To enable this parameter, set **Source of actors bus name** to `Property`.

### **Source of maximum number of actors** — Source of maximum number of actors `Scenario` (default) | `Property`

Source of the maximum number of actors that you can have in the driving scenario,
specified as one of these options:

- `Scenario` — The block sets the maximum number of
  actors to the number of actors in the driving scenario. This value is equal to the
  `NumActors` field of the bus returned by the
  **Actors** output port. When you change the input scenario, the
  maximum number of actors updates to match the new `NumActors`
  value.
- `Property` — Specify the maximum number of actors by
  using the **Maximum number of actors** parameter. Select this
  option when you want to reuse the same actor bus across scenarios that have varying
  numbers of actors, such as when outputting actors from a referenced model.

### **Maximum number of actors** — Maximum number of actors `100` (default) | positive integer

Maximum number of actors that you can have in the scenario, specified as a positive
integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
actors** parameter to `Property`.

### **Source of lane boundaries bus name** — Source of name for lane boundaries bus `Auto` (default) | `Property`

Source of the name for the lane boundaries bus returned in the **Lane
Boundaries** output port, specified as one of these options:

- `Auto` — The block automatically creates a lane
  boundaries bus name.
- `Property` — Specify the lane boundaries bus name by
  using the **Lane boundaries bus name** parameter.

#### Dependencies

To enable this parameter:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Lane boundaries to output** parameter to
   `Ego vehicle lane boundaries` or `All
   lane boundaries`.

### **Lane boundaries bus name** — Name of lane boundaries bus valid bus name

Name of the lane boundaries bus returned in the **Lane Boundaries**
output port, specified as a valid bus name.

#### Dependencies

To enable this parameter:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Lane boundaries to output** parameter to
   `Ego vehicle lane boundaries` or `All
   lane boundaries`.
3. Set the **Source of lane boundaries bus name** parameter to
   `Property`.

### **Source of maximum number of lane boundaries** — Source of maximum number of lane boundaries `Scenario` (default) | `Property`

Source of the maximum number of lane boundaries that you can have in the driving
scenario, specified as one of these options:

- `Scenario` — The block sets the maximum number of lane
  boundaries to the number of lane boundaries in the driving scenario. This value is
  equal to the `NumLaneBoundaries` field of the bus returned by the
  **Lane Boundaries** output port. When you change the input
  scenario, the maximum number of lane boundaries updates to match the new
  `NumLaneBoundaries` value.
- `Property` — Specify the maximum number of lane
  boundaries by using the **Maximum number of lane boundaries**
  parameter. Select this option when you want to reuse the same lane boundaries bus
  across scenarios that have varying numbers of lane boundaries, such as when
  outputting lane boundaries from a referenced model.

#### Dependencies

To enable this parameter:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Lane boundaries to output** parameter to
   `All lane boundaries`.

### **Maximum number of lane boundaries** — Maximum number of lane boundaries `10` (default) | positive integer

Maximum number of lane boundaries that you can have in the scenario, specified as a
positive integer.

#### Dependencies

To enable this parameter:

1. Set the **Coordinate system of actors output** parameter to
   `Vehicle coordinates`.
2. Set the **Lane boundaries to output** parameter to
   `All lane boundaries`.
3. Set the **Source of maximum number of lane boundaries**
   parameter to `Property`.

### **Source of ego vehicle pose bus name** — Source of name for ego vehicle pose bus `Auto` (default) | `Property`

Source of the name for the ego vehicle pose bus returned in the **Ego
Vehicle Pose** output port, specified as one of these options:

- `Auto` — The block automatically creates an ego vehicle
  pose bus name.
- `Property` — Specify the ego vehicle pose bus name by
  using the **Ego vehicle pose bus name** parameter.

#### Dependencies

To enable this parameter, select the **Output ego vehicle pose**
parameter.

### **Ego vehicle pose bus name** — Name of ego vehicle pose bus valid bus name

Name of the ego vehicle pose bus returned in the **Ego Vehicle
Pose** output port, specified as a valid bus name.

#### Dependencies

To enable this parameter, select the **Output ego vehicle pose**
parameter and set the **Source of ego vehicle pose bus name**
parameter to `Property`.

### **Source of ego vehicle state bus name** — Source of name for ego vehicle state bus `Auto` (default) | `Property`

Source of the name for the ego vehicle state bus returned in the **Ego
Vehicle State** output port, specified as one of these options:

- `Auto` — The block automatically creates an ego vehicle
  state bus name.
- `Property` — Specify the ego vehicle state bus name by
  using the **Ego vehicle state bus name** parameter.

#### Dependencies

To enable this parameter, select the **Output ego vehicle state**
parameter.

### **Ego vehicle state bus name** — Name of ego vehicle state bus valid bus name

Name of the ego vehicle state bus returned in the **Ego Vehicle
State** output port, specified as a valid bus name.

#### Dependencies

To enable this parameter, select the **Output ego vehicle state**
parameter and set the **Source of ego vehicle state bus name**
parameter to `Property`.

### **Show coordinate labels** — Display coordinate system of inputs and outputs `on` (default) | `off`

Select this parameter to display the coordinate
system of block inputs and outputs on the Scenario Reader block in the
block diagram.

- The **Ego Vehicle** input and output are always in world
  coordinates.
- The **Lane Boundaries** output is always in vehicle
  coordinates.
- You can return the **Actors** output in either vehicle or
  world coordinates, depending on the **Coordinate system of actors
  output** parameter selection.

#### Simulation

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In `Interpreted
  execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C/C++
  code. The first time you run a simulation, Simulink generates C/C++ code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional startup
  time.

## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- When a model is in rapid accelerator mode, the Scenario Reader
  block does not automatically regenerate code based on changes made to the driving
  scenario between simulations. To regenerate these changes, manually delete the
  Simulink project folder, `slprj`, that was generated from the
  previous simulation. Then, rerun the simulation. Alternatively, either change modes or
  disable code generation by setting the **Simulate using** parameter
  to `Interpreted execution`.
- The **Driving Scenario Designer file name** and
  **MATLAB or model workspace variable name** parameters are
  character vectors. The limitations described in Encoding of Characters in Code Generation (Simulink)
  apply to these parameters.

## Version History

**Introduced in R2019a**

## Description

Read driving scenario into model

The Scenario Reader block reads the roads and actors from a scenario file
created using the Driving Scenario
Designer app or from a `drivingScenario` object. The block outputs the
poses of actors in either the coordinate system of the ego vehicle or the world coordinates of
the scenario. You can also output the lane boundaries or output the ego vehicle pose for use
in the 3D simulation environment. The block also allows output of the ego vehicle state, which
includes acceleration measurements, for use with sensor models.

To generate object and lane boundary detections from output actor poses and lane
boundaries, pass the pose and boundary outputs to sensor blocks. Use the synthetic detections
generated from these sensors to test the performance of sensor fusion algorithms, tracking
algorithms, and other automated driving assistance system (ADAS) algorithms. To visualize the
performance of these algorithms, use the Bird's-Eye
Scope.

You can read the ego vehicle from the scenario or specify an ego vehicle defined in your
model as an input to the Scenario Reader block. Use this option to test
closed-loop vehicle controller algorithms, such as autonomous emergency braking (AEB), lane
keeping assist (LKA), or adaptive cruise control (ACC).
