---
type: simulink-block
title: 'Read UAV Trajectory'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'readuavtrajectory'
documentation_source_path: 'ref/readuavtrajectory.html'
language: en
---

# Read UAV Trajectory

## Ports

### Input

### **Time** — Time point to sample along trajectory scalar

Time point to sample along the trajectory, specified as a scalar.

To align your translation and rotation samples with your simulation, use the
Clock (Simulink) block as the input for this
port

**Data Types:** `double`
### Output

### **Translation** — Position of UAV vector

Position of the UAV, returned as a vector of the form `[X Y Z]`,
where `X`, `Y`, and `Z` are
positions in the *x*-, *y*-, and
*z*-axes, respectively. Units are in meters.

If you enable the **Convert to ENU reference frame and Front-Left-Up body
frame** parameter, this block outputs position in the ENU reference frame.
Otherwise, the block returns position in the same frame as the trajectory
source.

**Example:** `[1 1 1]`

**Data Types:** `double`

### **Rotation** — Euler angle of UAV vector

Euler angle of UAV, returned as a vector of the form `[Rz Ry
Rx]`, where `Rz`, `Ry`, and
`Rx` are rotation angles around the *z*-,
*y*-, and *x*- axes, respectively. Units are in
radians.

If you enable the **Convert to ENU reference frame and Front-Left-Up body
frame** parameter, this block outputs rotation from the ENU frame to the
Front-Left-Up body frame. Otherwise, this block returns rotation in the same frame as
the trajectory source.

**Example:** `[1 0 0]`

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Trajectory source** — Source for trajectory `From trajectory object in workspace` (default) | `From UAV Scenario in workspace`

Select the source for the UAV trajectory from these options:

- `From trajectory object in workspace` —

  Use a trajectory in your workspace, created using a `multirotorFlightTrajectory`, `fixedwingFlightTrajectory`, `polynomialTrajectory`, or `waypointTrajectory` object.
- `From UAV Scenario in workspace` —

  Use a trajectory that you have added to a platform in a UAV scenario.

### **UAV scenario object** — UAV scenario object `singleUAVScenario` (default) | `uavScenario` object

UAV scenario object containing the UAV platform that has the trajectory you want to
use, specified as a `uavScenario`
object.

#### Dependencies

To enable this parameter, set **Trajectory source** to
`From UAV Scenario in workspace`.

### **UAV platform name** — Name of UAV platform `UAV` (default) | name of UAV platform

Name of the UAV that which has the trajectory you want to use.

#### Dependencies

To enable this parameter, set **Trajectory source** to
`From UAV Scenario in workspace`.

### **Trajectory object** — Trajectory object `waypointTrajectory()` (default) | `multirotorFlightTrajectory` object | `fixedwingFlightTrajectory` object | `polynomialTrajectory` object | `waypointTrajectory` object

Specify the trajectory using one of these objects in the workspace: `multirotorFlightTrajectory`, `fixedwingFlightTrajectory`, `polynomialTrajectory`, or `waypointTrajectory`.

#### Dependencies

To enable this parameter, set **Trajectory source** to
`From trajectory object in workspace`.

### **Convert to ENU reference frame and Front-Left-Up body frame** — Translation and rotation coordinate frame `on` (default) | `off`

Select this parameter to output translation in the ENU reference frame and rotation
from the ENU frame to the Front-Left-Up body frame. Otherwise, the block outputs
translation and rotation in the same frame as the trajectory source. Select this
parameter if you want to use the outputs of this block as
**Translation** and **Rotation** inputs for the
Simulation 3D UAV
Vehicle block.

## Libraries

UAV Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Generate translation and rotation samples from UAV trajectory for 3D simulation

The Read UAV Trajectory block generates translation and rotation samples
from a UAV trajectory that you create using a `multirotorFlightTrajectory`, `fixedwingFlightTrajectory`, `polynomialTrajectory`,
or `waypointTrajectory`
object.

Use the output of this block for the **Translation** and
**Rotation** input ports of the Simulation 3D UAV
Vehicle block to simulate a UAV trajectory in a 3D simulation environment.
