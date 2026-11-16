---
type: simulink-block
title: 'UAV Scenario Configuration'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenarioconfiguration'
documentation_source_path: 'ref/uavscenarioconfiguration.html'
language: en
---

# UAV Scenario Configuration

## Ports

Not documented in R2025b.

## Parameters

### Main

### **MATLAB or model workspace variable name** — MATLAB or model workspace variable name `'singleUAVScenario'` (default) | string

Specify `uavScenario`
object to import from the MATLAB or model workspace, specified by variable name as a string. Click
**Refresh** to reload the scenario from the
`uavScenario` object.

### **Sample time** — Sample time `0.1` (default) | positive double

Specify sample time of the UAV scenario in seconds. This block only supports
discrete sample time.

### Scenario Bus and Signal Names

### **Sensor motion bus name** — Sensor motion bus name `'SensorMotionBus'` (default) | string

Specify the name of the sensor motion bus type as a string. Sensor motion read by
the UAV Scenario Motion
Read uses a bus object with the specified name.

### **Platform motion bus name** — Platform motion bus name `'PlatformMotionBus'` (default) | string

Specify the name of the platform motion bus type as a string. Platform motion read
and written by the UAV Scenario Motion
Read and UAV Scenario Motion
Write respectively will use a bus object with the specified name.

### **Scenario motion bus name** — Scenario motion bus name `'SensorMotionBus'` (default) | string

Specify the name of the scenario motion bus type as a string. This bus type is
used by the UAV Scenario Configuration block to store the motion data
of all the platforms and sensors within the UAV Scenario.

### **Scenario motion signal name** — Scenario motion signal name `'ScenarioMotions'` (default) | string

Specify the name of the scenario motion bus signal as a string. This is the name
used for the Data Store Read block that stores the data for the UAV
Scenario.

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Configure and simulate UAV scenarios

This block allows you to import a `uavScenario`object and
simulate the scenario. This block must be in a model that contains a UAV Scenario Lidar and
Motion blocks in order to test perception, control, and planning algorithms with data from a
`uavScenario`
environment. Models with a UAV Scenario can only use one UAV Scenario
Configuration block at a time and is not intended to be used in a cross-model
workflow. In a UAV scenario, this block must be executed before other UAV Scenario blocks.
Update the UAV Scenario Configuration block with the **Refresh** button and click **Apply** to reflect any changes made to the
imported `uavScenario` in
MATLAB®.

This block internally stores motion states from platforms and sensors in a global data
store memory block as buses within a bus with a name specified in the **Scenario
motion bus name** parameter. The bus contains the following fields:

- *NumPlatforms* — Number of UAV platforms in the scenario stored as
  a scalar.
- *Time* — Simulation time associated with the motion state stored as
  a scalar.
- *Platforms* — Bus array with name specified in the
  **Platform motion bus name** parameter containing all platforms in
  the UAV Scenario with each of the following fields:

  - *PlatformID* — ID of platform based on order of platforms in
    the `uavScenario.Platforms` Property.
  - *Position* — Position in NED frame specified as a 1-by-3
    vector.
  - *Orientation* — Orientation in NED frame specified as a
    1-by-4 vector, quaternion, frame rotation from NED frame to UAV body frame.
  - *Velocity* — Velocity in NED frame specified as a 1-by-3
    vector.
  - *Acceleration* — Acceleration in NED frame specified as a
    1-by-3 vector.
  - *AngularVelocity* — Angular velocity in NED frame specified
    as a 1-by-3 vector.
