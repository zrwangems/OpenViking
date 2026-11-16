---
type: simulink-block
title: 'UAV Scenario Lidar'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenariolidar'
documentation_source_path: 'ref/uavscenariolidar.html'
language: en
---

# UAV Scenario Lidar

## Ports

### Output

### **Pointcloud** — Point cloud data *N*-by-*M*-by-3 double matrix | *N*-by-3 double matrix

Point cloud data reported in the Sensor Frame. When `Output organized
point cloud locations` is checked, the point cloud data is specified as a
*N*-by-*M*-by-3 double matrix, where
*N* is the number of vertical scans, and *M* is
the number of horizontal scans. When `Output organized point cloud
locations` is unchecked, the point cloud data is specified as an
*N*-by-3 double matrix, where *N* is the number of
points in the point cloud.

## Parameters

### **Sensor name** — Lidar sensor name `'UAV/Lidar'` (default) | string

Specify lidar sensor name as a string scalar.

To choose an existing lidar sensor from the UAV Scenario in the MATLAB® workspace, click **Select**. The UAV Scenario
Lidar block sets the parameters with the current values of the properties of
specified lidar sensor.

To add lidar sensors to the UAV Scenario, create `uavSensor`
objects with a `uavLidarPointCloudGenerator` as the specified sensor model and attach the
`uavSensor` to a
`uavPlatform` in
UAV Scenario. This scenario must be imported into Simulink® using the UAV Scenario
Configuration block. The available sensors will be listed as
*'platform name/sensor name'*.

### **Max range** — Max range of lidar `120` (default) | double

Specify max range of lidar as a double scalar in meters.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Max range** parameter to the `MaxRange`
property of the specified lidar sensor.

### **Range Accuracy** — Range accuracy of lidar `0.002` (default) | double

Specify range accuracy of lidar as a double scalar in meters.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**RangeAccuracy**parameter to the value of the
`RangeAccuracy` property of the specified lidar sensor.

### **Azimuthal limits** — Azimuthal limits of lidar `[-180, 180]` (default) | two-element vector

Specify azimuthal limits of lidar as a two-element vector in degrees.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Azimuthal limits** parameter to the value of the
`AzimuthLimits` property of the specified lidar sensor.

### **Azimuthal resolution** — Azimuthal resolution `0.16` (default) | double

Specify azimuthal resolution of lidar as a double scalar in degrees.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Azimuthal resolution** parameter to the value of the
`AzimuthResolution` property of the specified lidar sensor.

### **Elevation limits** — Elevation limits of lidar `[-20, 20]` (default) | two-element vector

Specify elevation limits of lidar as a two element vector in degrees.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Elevation limits** parameter to the value of the
`ElevationLimits` property of the specified lidar sensor.

### **Elevation resolution** — Elevation resolution `1.25` (default) | double

Specify elevation resolution of lidar as a double scalar in degrees.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Elevation resolution resolution** parameter to the value of the
`ElevationResolution` property of the specified lidar
sensor.

### **Add noise to measurement** — Add noise to measurement `'on'` (default) | `'off'`

Check this box to add noise to measurement of lidar. The noise generation of this
block currently does not allow for a user-specified seed.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Add noise to measurement** parameter to the value of the
`HasNoise` property of the specified lidar sensor.

### **Output organized point cloud locations** — Output point cloud locations `'on'` (default) | `'off'`

Check this box to output organized point cloud locations specified as
*N*-by-*M*-by-3, where *N* is the
number of vertical scans, and *M* is the number of horizontal scans. If
set to `'off'`, the output of the block is an *N*-by-3
double matrix, where *N* is the number of points in the point
cloud.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Output organized point cloud locations** parameter to the value
of the `HasOrganizedOutput` property of the specified lidar
sensor.

### **Sample Time** — Sample time `0.1` (default) | double

Specify sample time of the lidar as a double scalar in seconds. Sample time must be
a multiple of the sample time specified in the UAV Scenario
Configuration block.

If you use **Select** to specify the **Sensor
name** parameter, the UAV Scenario Lidar block sets the value of the
**Sample Time** parameter to `1/UpdateRate`.
`UpdateRate` is the `UpdateRate` property of the
specified lidar sensor.

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Simulate lidar measurements based on meshes in scenario

Use this block to simulate lidar measurements by outputting point cloud data based on
meshes in a UAV Scenario. To add meshes to your UAV Scenario, use the `addMesh` function to
add it to the `uavScenario` object
included by your UAV Scenario
Configuration block. See UAV Scenario Tutorial for more information on adding
meshes.

To use this block, ensure that UAV Scenario Configuration block is in your
model.
