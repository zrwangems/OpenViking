---
type: simulink-block
title: 'RoadRunner Scenario Reader'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / RoadRunner Scenario Simulation / Simulate RoadRunner Scenarios with MATLAB and Simulink'
documentation_page: 'roadrunnerscenarioreader'
documentation_source_path: 'ref/roadrunnerscenarioreader.html'
language: en
---

# RoadRunner Scenario Reader

## Ports

### Input

### **Port\_1** — Actor ID scalar

Specify the ID of the actor whose parent or children information you
require.

To convert the ID to the `uint64` data type, you can either set
the **Constant value** parameter of the Constant (Simulink) block to `uint64(ID)`, where
`ID` is the Actor ID, or use the Data Type Conversion (Simulink) block.

#### Dependencies

To enable this port, set the **Filter** parameter to
`Actor ID (provided by input)`.

**Data Types:** `uint64`
### Output

### **Message** — State information from scenario Simulink message

State information from scenario, returned as a Simulink message. To extract data from the Simulink message, connect the RoadRunner Scenario Reader block to
the Receive (Simulink) block.

## Parameters

### **Topic Category** — Topic category `Actor` (default) | `Action` | `Sensor` | `Event`

Topic category, specified as one of these values:

- `Actor` — Reads the actor data from the scenario
- `Action` — Reads the action data from the scenario
- `Sensor` — Reads the sensor data from the scenario
- `Event` — Reads the event data from the scenario

### **Actor Type** — Type of actor in scenario `All Types` (default) | `Vehicle` | `Traffic Signal` | `Traffic Signal Controller`

Type of actor in scenario, specified as `All Types`,
`Vehicle`, `Traffic Signal`, or `Traffic
Signal Controller`. The `Vehicle` type includes additional
wheel information of the actor.

The `Traffic Signal` type represents traffic signal actors, while
the `Traffic Signal Controller` type represents a traffic signal
controller entity that connects all traffic signal actors of a junction together.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Actor`.

### **Action Type** — Type of action `Path Following` (default) | `Change Parameter` | `Lane Change` | `Lateral Offset` | `Longitudinal Distance` | `Speed Change` | `User Defined`

Type of action that can be read from the scenario, specified as one of these values:

| Field Name | Description |
| --- | --- |
| `Change Parameter` | Reads the user-created parameter from the scenario. For more information, see Change Parameter. |
| `Lateral Offset` | Reads the lateral offset action data from the scenario. For more information, see Lateral Offset. |
| `Path Following` | Reads the path following action data from the scenario. For more information, see Path Following. |
| `Speed Change` | Reads the speed change action data from the scenario. For more information, see Speed Change. |
| `Lane Change` | Reads the lane change action data from the scenario. For more information, see Lane Change. |
| `Longitudinal Distance` | Reads the longitudinal distance action data from the scenario. For more information, see Longitudinal Distance. |
| `User Defined` | Reads the custom parameters of a user-defined action from the scenario. For more information, see User Defined. |

#### Dependencies

To enable this parameter, set **Topic Category** to
`Action`.

### **Sensor View** — Sensor data derived from scenario ground truth `Target Poses` (default) | `Target Poses For Host` | `Lane Boundaries` | `Target Poses And Lane Boundaries`

Sensor data derived from the scenario ground truth, specified as one of these options:

- `Target Poses` — The block outputs poses of targets
  within sensor range in host vehicle coordinates. For the bus structure of the
  output target poses, see the output argument description of the `targetPoses` function.
- `Target Poses For Host` — The block outputs poses of
  all targets in the in host vehicle coordinates. For the bus structure of the
  output target poses, see the output argument description of the `targetPoses` function.
- `Lane Boundaries` — The block outputs lane boundaries
  within sensor range in host vehicle coordinates. For the bus structure of the
  output lane boundaries, see the output argument description of the `laneBoundaries` function.
- `Target Poses And Lane Boundaries` — The block
  outputs both lane boundaries and poses of targets within the sensor range in host
  vehicle coordinates.

The origin of the host vehicle coordinates is the geometric center of
the host vehicle.

You can send the above outputs directly to sensor detection generator blocks and
obtain detections.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Sensor`.

### **Event Type** — Type of event `User-Defined`

Type of event to read from a scenario.

The event being read must be mapped to the corresponding bus object in the
RoadRunner Scenario block.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Event`.

### **Topic** — Actor data, or lane boundary data captured through sensor views `Actor Specifications` | `Actor Pose` | `Actor Pose (Driving Scenario compatible)` | `Actor Lane Location` | `Vehicle Specifications` | ...

Actor data, or lane boundary captured through sensor views.

The **Topic** parameter can hold various sets of options, as
specified in the tables below, depending on the configuration of other fields.

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to `All
  Types`.

| Option | Description |
| --- | --- |
| `Actor Specifications` (default) | Static attributes associated with the actor, such as actor ID, actor name, and bounding box. For more information, see Actor Specifications. |
| `Actor Pose` | Dynamic data associated with the actor, such as pose, velocity, and angular velocity. For vehicle assets included with or created in RoadRunner, the actor origin is the geometric center of the actor. For more information, see Actor Pose. |
| `Actor Pose (Driving Scenario compatible)` | Dynamic data associated with the actor, such as actor ID, position, velocity, roll, pitch, yaw, and angular velocity. For vehicle assets included with or created in RoadRunner, the actor origin is the point on the ground below the center of its rear axle. For more information, see Actor Pose (Driving Scenario compatible). |
| `Actor Lane Location` | Dynamic data associated with the lane location of actors. For more information, see Actor Lane Location. |

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to
  `Vehicle`.

| Option | Description |
| --- | --- |
| `Vehicle Specifications` (default) | Static attributes associated with the vehicle, such as paint color, and wheel specifications. For more information, see Vehicle Specifications. |
| `Vehicle Pose` | Dynamic data associated with the actor, such as wheel poses. For more information, see Vehicle Pose. |

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to `Traffic
  Signal`.

| Option | Description |
| --- | --- |
| `Traffic Signal Specifications` (default) | Static specifications of a traffic signal actor. For more information, see Traffic Signal Specifications Topic. |
| `Traffic Signal Runtime` | Run-time information of a traffic signal actor. For more information, see Traffic Signal Runtime Topic. |

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to `Traffic Signal
  Controller`.

| Option | Description |
| --- | --- |
| `Traffic Signal Controller Specifications` (default) | Static specifications of a traffic signal controller. For more information, see Traffic Signal Controller Specifications Topic. |
| `Traffic Signal Controller Runtime` | Run-time information of a traffic signal controller. For more information, see Traffic Signal Controller Runtime Topic. |

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Sensor`.
- **Sensor View** is set to `Lane
  Boundaries`.

| Option | Description |
| --- | --- |
| `Ego-Lane` (default) | Boundaries of the lane in which the host vehicle actor is traveling |
| `Ego and Adjacent Lanes` | Boundaries of the adjacent left and right lanes, as well as the lane in which host vehicle actor is traveling |
| `All Lanes` | Boundaries of all lanes on the road |

### **Filter** — Filter criteria `Self` (default) | `None` | `Actor ID (provided by input)`

Filter criteria for relevant topic data, specified as one of these options:

| Option | Description |
| --- | --- |
| `None` | Output data for all actors in the scenario.  When you set **Filter** to `None`, the block outputs a message for each actor in your simulation. Messages carry data, including the actor ID. You can store messages in a Queue (Simulink) block. Then, you can process these messages using, for example, a MATLAB System block. For more information, see Process Message Payload Using MATLAB System Block (Simulink).  RoadRunner Scenario Reader block outputs messages associated actors when Filter is selected as None. Queue block stores messages and MATLAB Function block processes messages. |
| `Self` | Output data for the actor associated with the Simulink model behavior. |
| `Actor ID (provided by input)` | Output data for a specific actor. Selecting this option exposes input port **Port\_1** through which you can provide an actor ID. For example, you can connect the Constant block to **Port\_1** to provide a fixed value that represents the ID of an actor in a scenario. |

#### Dependencies

To enable this parameter, set **Topic Category** to
`Actor` or `Action`.

### **Additional Relationship** — Relationship to filtered entity `None` (default) | `Parent` | `Children`

Relationship to the filtered entity, specified as one of these options:

- `None` — No selection. The RoadRunner Scenario
  reader block outputs data associated with the entity filtered according
  to the **Filter** parameter.
- `Parent` — Parent actor of filtered entity. The
  RoadRunner Scenario reader block outputs data associated with the
  parent of the entity filtered according to the **Filter**
  parameter.
- `Children` — Children actors of filtered entity. The
  RoadRunner Scenario reader block outputs data associated with the
  children of the entity filtered according to the **Filter**
  parameter.

For example, select `Actor ID (provided by input)` as the
filter to expose input port **Port\_1**. Attach a Constant block
that outputs a value of `uint64(2)` to the input port. If you select
`Parent` from the **Additional
Relationship** field, then the RoadRunner Scenario Reader
block outputs data associated with the parent of the actor with ID
`2`.

**Note**

You can also use the **Additional Relationship** parameter to
output information about actions of parent or child actors.

#### Dependencies

To enable this parameter, set **Filter** to `Actor ID
(provided by input)` or `Self`.

### **Sensor ID** — Unique index of sensor `1` (default) | positive integer

Unique index of the sensor, specified as a positive integer. The `Sensor
ID` must correspond to the **Unique identifier of
sensor** parameter of the corresponding sensor model detection generator
block.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Sensor` and **Sensor View** to either
`Target Poses`, `Lane Boundaries`
or `Target Poses And Lane Boundaries`.

### **Sample Time** — Sample time of simulation positive real scalar

Sample time of simulation in seconds, specified as a positive real scalar.

### **Event Name** — Name of event string

Name of the user-defined event to read from a scenario.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Event` and **Event Type** to
`User-Defined`.

## Libraries

Automated Driving Toolbox / RoadRunner Scenario

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

### R2025a: Get traffic signal and traffic signal controller information

Get traffic signal and traffic signal controller information by setting the
**Topic Category** parameter to `Actor`, and
**Actor Type** to `Traffic Signal` or
`Traffic Signal Controller`.

You can then output the static or run-time specifications of the specified traffic
signal or traffic signal controller by changing the **Topic**
parameter.

### R2025a: Get actor or action information associated with parent or child actors

Get actor or action information associated with the parent or children actors of a
specific actor by setting the **Topic Category** parameter to
`Actor` or `Action`, and
**Filter** to `Actor ID (provided by input)`.
Setting these parameter values exposes the input port **Port\_1**. Depending on your
requirement, set the **Additional Relationship** parameter to
`Parent` or `Children`.

### R2023a: `LaneLocation` topic for all actors

Starting in R2023a, `MapLocation` and its bus definition
`BusVehicleMaplocation` are not supported, when you access
`Vehicle Pose` using a RoadRunner Scenario Reader block.
To read an actor location, use the new dedicated topic `Actor Lane
Location`. The change allows you to access location data associated with any
actor in your RoadRunner Scenario simulation.

## Description

Reads selected topic from RoadRunner scenario

The RoadRunner Scenario Reader block reads the selected topic from the
`RoadRunner` scenario. You can set the **Topic Category**
parameter to `Actor`, `Action`,
`Sensor`, or `Event`. The block outputs
data as messages.

When you select the `Actor` topic, the block outputs the data
associated with the actor, such as `Actor Specifications` and
`Actor Pose`. When you select the `Action`
topic, the block outputs data such as `Speed Change` and
`Lane Change`. The block returns the simulation states from the previous
time step. You can filter data based on the actor associated with the Simulink® actor model.

When you select the `Sensor` topic, the block outputs the data
associated with the sensor of specified `Sensor ID`. You can select the
type of sensor data the block must output by specifying `Target
Poses` or `Lane Boundaries`. When you select the
`Event` topic, the block outputs data for the user-defined event
specified for the **Event name** parameter.
