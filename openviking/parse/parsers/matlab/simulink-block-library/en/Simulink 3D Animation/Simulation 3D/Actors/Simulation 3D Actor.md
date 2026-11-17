---
type: simulink-block
title: 'Simulation 3D Actor'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Actors'
documentation_page: 'simulation3dactor'
documentation_source_path: 'simulation3dactor.html'
language: en
---

# Simulation 3D Actor

## Ports
```yaml
ports:
- name: Instance
  summary: Instance number of actor real integer
  direction: input
- name: Valid
  summary: Validity of specified actor false (default) | true
  direction: output
```

### Input

### **Instance** — Instance number of actor real integer

Instance number of actor, specified as a real integer.

- For positive values, a new actor is created if it has not been
  created already. The reference block refers to this actor if the
  actor is present in the world.
- For negative values, actor instances are deleted, if they
  exist. For example, instance 1 is deleted if the value of this
  port is `-1` at a given time step.

#### Dependencies

This input is visible when the operating mode of the block is set to either
`Create at step` or
`Reference by instance number`.
### Output

### **Valid** — Validity of specified actor `false` (default) | `true`

Validity of the specified actor, returned as `false` if the specified
actor cannot be found in the world or `true` if the
actor is found.
## Parameters
```yaml
parameters:
- name: Actor Name
  summary: Name of actor Sim3dActor1 (default) | string
  group: Main
- name: Parent Name
  summary: Parent of actor Scene Origin (default) | string
  group: Main
- name: Operation
  summary: Operating mode of block Create at setup (default) | Create at step | Reference by name | Reference by instance
    number
  group: Main
- name: Path to source file
  summary: File from which actors are sourced string
  group: Main
- name: Initialization script
  summary: Code to initialize actor MATLAB script
  group: Main
- name: Sample time
  summary: Sample time -1 (default) | scalar
  group: Main
- name: Translation
  summary: Relative translation [0,0,0] (default) | real 1-by-3 vector
  group: Transform
- name: Rotation
  summary: Relative rotation [0,0,0] (default) | real 1-by-3 vector
  group: Transform
- name: Scale
  summary: Relative scale [1,1,1] (default) | real 1-by-3 vector
  group: Transform
- name: Input ports
  summary: List of user-selected input ports text area
  group: Inputs
- name: Output ports
  summary: List of user-selected output ports text area
  group: Outputs
```

### Main

### **Actor Name** — Name of actor `Sim3dActor1` (default) | string

Name of the root actor for the current Simulation 3D Actor block.

### **Parent Name** — Parent of actor `Scene Origin` (default) | string

Name of the parent actor of the actor, specified as a string.

### **Operation** — Operating mode of block `Create at setup` (default) | `Create at step` | `Reference by name` | `Reference by instance number`

Operating mode that determines block behavior, specified as one of
these options.

- `Create at setup` – Use this option
  to create actors in the scene. The actors are created during
  game setup, before the simulation runs. You can also control the
  simulation of these actors using the **Input**,
  **Output**, and **Event**
  ports.
- `Create at step` – Use this option to
  dynamically create and delete actors when the simulation is
  running. An **Instance** input port of the type
  `int` is created in this mode, and the
  actors are dynamically generated based on the values input to
  the block. If the value of **Instance** is
  greater than zero, an actor with the name `'Actor name +
  Instance value'` is created. The name of the actor
  is derived from `'Actor Name'` in the
  block mask. The instance value is the current value of the port.
  When the value of **Instance** is negative,
  then the actor is deleted. Unlike the `Create at
  setup` option, you cannot control the actors
  created with this option selected in the block mask.
- `Reference by name` – Use this option
  to refer to an actor in the scene using `Actor
  Name`, and control this actor's simulation
  using the inputs of the block. Get data of the actor using the
  outputs or events. This also provides a
  **Valid** output port.

  If an actor with the specified name is not present, the **Valid**
  port returns `false` or `0`.
  In this case, default values will be passed as output for rest
  of the out ports (if any). Use the `Valid`
  port to verify whether the other outputs generated are currently
  valid or not.

  **Note**

  **Path to source file** and
  **Initialization script** parameters
  are unavailable in the `Reference by
  name` operating mode.
- `Reference by instance number` – Use
  this option to refer to an instance created via a different
  actor block. Similar to the `Create at
  step` operating mode, this option creates an
  **Instance** input in the block, and the
  effective actor name `'Actor name + Instance
  value'` is used to reference the actor.

  If an actor with the generated name is not present, the
  **Valid** port returns
  `false` or `0`. In this
  case, default values are passed as output for rest of the output
  ports, if any. Use the **Valid** port to verify
  whether the other outputs generated are currently valid or
  not.

  **Note**

  **Path to source file** and
  **Initialization script** parameters
  are unavailable in the `Reference by instance
  number` operating mode.

#### Dependencies

The **Transform** tab is available if you set
**Operation** as either `Create at
setup` or `Create at
step`.

### **Path to source file** — File from which actors are sourced string

File from which actors are sourced, specified as a string.

This option loads a 3D file or imports a `sim3d.Actor` object, including child actor objects.
`Simulation 3D Actor` block supports these as sources.

**File Formats**

- MAT (MAT file from MATLAB®)
- STL (Stereolithography)
- FBX (Autodesk®
  Filmbox format)
- URDF (Unified Robot Description File)
- X3D (Extensible 3D)
- WRL (Virtual Reality Modeling Language)
- DAE (Collada digital asset exchange)
- USD, USDA, USDC (Universal Scene Description)

You can also instantiate actors using
`.m` files.

Alternatively, the **Select** button can also be
used to select a file from the Windows® file browser.

**Note**

USD file import is not supported on Linux®. USD files do not support collision detection.

### **Initialization script** — Code to initialize actor MATLAB script

Code to initialize the actor created by the block, specified as a MATLAB script. You can also use this script to create other actor
objects, set their properties, and add them to the 3D environment as
child actors using the `add` function. You must set the parent actor using the
`parent` in the `add`
function.

This MATLAB script runs when the 3D environment initializes the actors
created by the block. The order of actor creation is:

1. Root actor with specified name is created.
2. The **Path to source file** is loaded
   into the root actor.
3. The **Initialization script**
   runs.

Use the name `Actor` when modifying the root actor
of the block. `Actor` is a reserved handle in the
initialization script. Otherwise, use the `findBy` function to get the actor handle of a different
name, for example, one of the child actors. Then use the retrieved actor
handle to initialize that specific actor. For example, to add an actor
as child of the root actor, set `Actor` as the parent
actor in the `add` function.

Use the name `World` for actors in the 3D
environment. `World` is a reserved handle in the
initialization script for the 3D environment created by the
Simulation 3D Scene Configuration block.

You can create and add these `sim3d` actor objects.

- `sim3d.Light`
- `sim3d.graphics.Arrow`
- `sim3d.graphics.Text`
- `sim3d.graphics.PathMarker`

**Initialization script** does not use the base
workspace variables.

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The
graphics frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample time
specified in the Simulation 3D Scene Configuration
block.

For optimal performance, check that this value is not less than the value of **Sample
time** specified in the Simulation 3D Scene Configuration block.

### Transform

The **Transform** tab is available to set the initial transform properties
when you set **Operation** as either `Create at
setup` or `Create at step`. Otherwise, the
transform properties set in the **Initialization script** are used
in the **Transform** tab and overwrite any values set there.

### **Translation** — Relative translation `[0,0,0]` (default) | real 1-by-3 vector

Translation
(*x*,*y*,*z*) of
the actor object relative to its parent actor, specified as a real
1-by-3 vector, in meters.

#### Dependencies

The Translation property set in the
**Initialization script** overwrites this
parameter value.

### **Rotation** — Relative rotation `[0,0,0]` (default) | real 1-by-3 vector

Rotation (roll, pitch, yaw) of the actor object relative to its parent
actor, specified as a real 1-by-3 vector, in radians.

#### Dependencies

The Rotation property set in the
**Initialization script** overwrites this
parameter value.

### **Scale** — Relative scale `[1,1,1]` (default) | real 1-by-3 vector

Relative scale in *x*, *y* and
*z* coordinates, specified as a real 1-by-3
vector.

#### Dependencies

The Scale property set in the **Initialization
script** overwrites this parameter value.

**Note**

Setting the initial transform properties in the **Initialization
script** overwrites the **Transform** tab
values.

### Inputs

### **Input ports** — List of user-selected input ports text area

This text area lists the user-selected input ports of the block and
provides a button that opens the port selector app, which you can use to
modify the input ports. Each line in the text area represents one block
port.

You can manually modify the ports using the text area, but using the
port selector app is recommended for choosing the ports.

### Outputs

### **Output ports** — List of user-selected output ports text area

This text area lists the user-selected output ports of the block and
provides a button that opens the port selector app, which you can use to
modify the output ports. Each line in the text area represents one block
port.

You can manually modify the ports using the text area, but using the
port selector app is recommended for choosing the ports.
## Libraries

Simulink 3D Animation / Simulation 3D / Actors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2024b: Create Light and Annotation Actors

Use the Simulation 3D Actor block **Initialization script** to
initialize and add these actors in the 3D environment with tunable block parameters.

- Light using the `sim3d.Light` object
- Arrow using the `sim3d.graphics.Arrow` object
- Text using the `sim3d.graphics.Text` object

### R2023b: Tunable Translation, Rotation, and Scale Parameters

These Simulation 3D Actor block parameters are tunable, allowing you to use
the For Each Subsystem (Simulink) block to create
multiple instances of the same actor type in the virtual world.

- **Translation**
- **Rotation**
- **Scale**

For an example, see Create Multiple Instances of Actors.

### R2023a: Communicate Unreal Engine Events

Use the Simulation 3D Actor block event ports to communicate events in the
Unreal Engine simulation 3D environment, including when:

- You click on an actor.
- An actor collides or overlaps with another actor.

## Description

Create actors in 3D environment

The Simulation 3D Actor block implements an actor in the Unreal Engine® environment. You can use this block to specify actor name and source file,
set how the actor is created and behaves during simulation, and initialize the actor.
The block creates a movable actor. Additionally, you can create and add other
`sim3d` actor objects to the 3D environment as children of this
actor.
