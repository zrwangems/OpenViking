---
type: simulink-block
title: 'UAV Scenario Scope'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenarioscope'
documentation_source_path: 'ref/uavscenarioscope.html'
language: en
---

# UAV Scenario Scope

## Ports

### Input

### **In\_1, In\_2, ..., In\_N** — Point cloud data inputs for lidar sensors *N*-by-*M*-by-3 double matrix | *N*-by-3 double matrix

Input point cloud data for sensors in the UAV Scenario. An input port is created
for every lidar sensor checked for visualization in the `Lidar
Sensors` table in the **Visualize** column. The name of
the port is set to the name of the sensor, which includes the name of the platform the
sensor belongs too. For example, an input port for a lidar sensor on a platform named
`EgoVehicle` will have the name,
`EgoVehicle/Lidar`.

If the `Organized point cloud locations` parameter of the lidar
sensor is set to `'on'`, then the input port expects a
*N*-by-*M*-by-3 double matrix, where
*N* is the number of vertical scans, and *M* is
the number of horizontal scans. If the `Organized point cloud
locations` of the lidar sensor is set to `'off'`, the
input port expects an *N*-by-3 double matrix, where
*N* is the number of points in the point cloud.

## Parameters

### **Lidar Sensors** — List of lidar sensors and their visualization table

The `Lidar Sensors` table lists all of the lidar sensors in the
UAV scenario. In the first column, **Sensor name**, all of the sensor
names are listed with their associated platform as *'platform name/sensor
name'*. The second column, **Visualize**, contains a
check-box for every lidar sensor in the table. Setting a visualization to
`'on'` for a lidar sensor creates an input port with the name of that
lidar sensor.

Enter a string in the **Filter table contents** to filter through
the list of sensors by their name in the **Sensor Name** column of the
table.

If the list of lidar sensors in the UAV Scenario has changed, click
**Refresh sensor table** to update the `Lidar
Sensors` table.

Click **Show animation** to show or hide the animation figure for
the UAV scenario.

### **Sample time** — Sample time `0.1` (default)

Specify sample time of the visualization. If `Sample time` is set
to `-1`, this block uses the sample time specified in the UAV Scenario
Configuration block.

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Visualize UAV scenario and lidar point clouds

Use this block to visualize a UAV scenario and lidar point clouds in an animation figure
window. Click **Show animation** in the block parameters to visualize the
UAV scenario. The visualization in the figure window updates continuously as the model is
running.

An input port is created for every sensor checked for visualization in the
**Visualize** column of the `Lidar Sensors`
table.

To use this block, ensure that UAV Scenario
Configuration block is in your model.
