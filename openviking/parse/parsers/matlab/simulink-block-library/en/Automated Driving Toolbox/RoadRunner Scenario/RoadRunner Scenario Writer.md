---
type: simulink-block
title: 'RoadRunner Scenario Writer'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'RoadRunner Scenario'
documentation_page: 'roadrunnerscenariowriter'
documentation_source_path: 'ref/roadrunnerscenariowriter.html'
language: en
---

# RoadRunner Scenario Writer

## Ports
```yaml
ports:
- name: Message
  summary: State information Simulink message
  direction: input
```

### Input

### **Message** — State information Simulink message

State information to write to the scenario, specified as a Simulink message. To construct a Simulink message from an input signal within your model, use the Send (Simulink) block. Then, connect the output of the Send block to
the RoadRunner Scenario Writer block.
## Parameters
```yaml
parameters:
- name: Topic Category
  summary: Topic category Actor (default) | Event | Diagnostics
  group: ''
- name: Actor Type
  summary: Type of actor in scenario All Types (default) | Vehicle
  group: ''
- name: Topic
  summary: Actor or vehicle data Actor Pose | Actor Pose (Driving Scenario compatible) | Vehicle Pose
  group: ''
- name: Event Type
  summary: Type of event Action Complete (default) | User-Defined
  group: ''
```

### **Topic Category** — Topic category `Actor` (default) | `Event` | `Diagnostics`

Topic category, specified as one of these options:

- `Actor` — Write the actor data to the scenario.
- `Event` — Write event data to the scenario.
- `Diagnostics` — Write custom diagnostic messages of type
  BusDiagnostics to the
  scenario.

### **Actor Type** — Type of actor in scenario `All Types` (default) | `Vehicle`

Type of actor in scenario, specified as `All Types` or
`Vehicle`. The `Vehicle` type additionally includes
wheel information of the actor.

The actor type that you select determines which values are available for the
**Topic** parameter.

**Note**

The `All Types` actor type also applies to pedestrians in a
scenario.

### **Topic** — Actor or vehicle data `Actor Pose` | `Actor Pose (Driving Scenario compatible)` | `Vehicle Pose`

Actor data or vehicle data. The **Topic** parameter can hold two
sets of values depending on the configuration of the **Actor Type**
parameter.

The **Topic** parameter holds the options described in the table
below if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to `All
  Types`.

| Option | Description |
| --- | --- |
| `Actor Pose (Driving Scenario compatible)` (default) | Dynamic data associated with the actor, such as actor ID, position, velocity, roll, pitch, yaw, and angular velocity. When you select this value, the block writes a bus of type `BusActorPose` to the scenario. |
| `Actor Pose` | Dynamic data associated with the actor, such as pose, velocity, and angular velocity. When you select this value, the block writes a bus of type `BusActorRuntime` to the scenario. |

The **Topic** parameter holds the `Vehicle Pose`
option if both these field configurations are true:

- **Topic Category** is set to
  `Actor`.
- **Actor Type** is set to
  `Vehicle`.

Choosing the `Vehicle Pose` option enables writing
dynamic data associated with a vehicle, such as wheel poses, to a scenario. When you
select this value, the block writes a bus of type `BusVehicleRuntime` to the
scenario.

### **Event Type** — Type of event `Action Complete` (default) | `User-Defined`

Type of event written to the scenario, specified as one of the following.

- `Action Complete` — Indicates that a custom action
  has been processed. When you select this value, the block writes a bus of type
  `BusActionComplete`
  to the scenario.
- `User-Defined` — Indicates that a user-defined event
  has been returned to a scenario.

  The event being written must be mapped to its corresponding bus object in the
  RoadRunner Scenario block.

#### Dependencies

To enable this parameter, set **Topic Category** to
`Event`.
## Libraries

Automated Driving Toolbox / RoadRunner Scenario

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Write selected topic to RoadRunner scenario

The RoadRunner Scenario Writer block writes actor, event, or diagnostic
information to a RoadRunner scenario. The block receives this topic information,
computed internally by a Simulink® actor behavior model, as input in the form of
Simulink® messages. You can set the **Topic
Category** parameter to `Actor`,
`Event`, or `Diagnostics`. For example,
when you select the `Actor` topic, the block writes dynamic data
associated with the actor, such as actor ID, velocity and angular velocity, to the
scenario.

The RoadRunner Scenario Writer block writes information to a scenario in
the form of certain bus types. A bus type defines the fixed structure of a bus object,
including the names, data types, and dimensions of the bus elements. To enable writing to a
scenario, load the required bus types into the MATLAB® base workspace by clicking load function in the Block Parameters
dialog box. This action enables the block to receive a bus of the expected type to write to a
scenario. For example, while building a Simulink actor behavior model, you can set the **Output data type**
parameter of a Bus Creator (Simulink) block to a loaded bus type and then fill in values of
the corresponding bus elements. You can then forward this bus as an input to the
RoadRunner Scenario Writer block.

If you are using an actor group in RoadRunner Scenario, you can use the RoadRunner
Scenario Writer block to control the behavior of individual child actors in the
following ways.

- Use one RoadRunner Scenario Writer block to send messages to
  different actors. For example, you can queue messages carrying results of different
  logic implementations within the model to the RoadRunner Scenario Writer
  block by using the Message Merge block. Each of these messages can carry
  a different value of `ActorID`.
- Use multiple RoadRunner Scenario Writer blocks. You can point the
  `ActorID` value of the `Actor Pose`, `Actor
  Pose (Driving Scenario compatible)`, or `Vehicle Pose` bus
  of each RoadRunner Scenario Writer block to a different child
  actor.
