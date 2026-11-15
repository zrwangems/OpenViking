---
type: simulink-block
title: 'UAV Scenario Get Transform'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenariogettransform'
documentation_source_path: 'ref/uavscenariogettransform.html'
language: en
---

# UAV Scenario Get Transform

## Ports

### Output

### **transform** — Transformation matrix 4-by-4 matrix

Output transformation specified as a 4-by-4 transformation matrix.

## Parameters

### **Source Frame** — Source frame `'ENU'` (default) | `'NED'` | string from UAV Scenario

Use **Select** to choose a global coordinate source frame from
the UAV Scenario loaded in your model. Select either North-East-Down
('`NED'`), or East-North-Up (`'ENU'`).

### **Target Frame** — Target frame `'NED'` (default) | `'ENU'` | string from UAV Scenario

Use **Select** to choose a global coordinate source frame from
the UAV Scenario loaded in your model. Select either North-East-Down
('`NED'`), or East-North-Up (`'ENU'`).

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Get transforms from UAV scenario platforms

This block outputs a 4-by-4 transformation matrix that maps points in source frame to
target frame in a UAV Scenario.

To use this block, ensure that UAV Scenario
Configuration block is in your model.

This block uses the sample time specified in the UAV Scenario Configuration
block.
