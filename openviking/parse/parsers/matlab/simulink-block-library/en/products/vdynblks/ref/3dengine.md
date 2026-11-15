---
type: simulink-block
title: '3D Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: '3dengine'
documentation_source_path: 'ref/3dengine.html'
language: en
---

# 3D Engine

## Ports

### Input

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.

## Parameters

#### 3D Engine

### **3D Engine** — Enable 3D visualization `off` (default) | `on`

Enable 3D visualization.

### **Scene** — 3D scene `Straight road` | `Curved road` | `Parking lot` | `Double lane change` | `Open surface` | `US city block` | `US highway` | `Virtual Mcity` | `Large parking lot`

Specify the name of the 3D scene.

### **Engine frame rate, dt3D** — Graphics `.03` (default)

Graphics frame rate, in s. The graphics frame rate is the inverse of the sample time.

### **Recommended for scene** — Initial vehicle position `on` (default) | `off`

Use vehicle positions that are recommended for the scene.

### **User-specified** — Initial vehicle position `off` (default) | `on`

Specify to set your own initial vehicle position values.

### **Initial longitudinal position, X\_o** — Initial longitudinal position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *X*-axis, in m.

### **Initial lateral position, Y\_o** — Initial lateral position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *Y*-axis, in m.

### **Initial vertical position, Z\_o** — Initial vertical position `off` (default) | `on`

Initial vehicle CG position along the earth-fixed *Z*-axis, in m.

### **Initial roll angle, phi\_o** — Roll `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll), in rad.

### **Initial pitch angle, theta\_o** — Pitch `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch), in rad.

### **Initial yaw angle, psi\_o** — Yaw `off` (default) | `on`

Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw), in rad.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Configure scenes in reference applications

The 3D Engine block implements the 3D simulation environment. Vehicle Dynamics Blockset™ integrates the 3D simulation environment with Simulink® so that you can query the world around the vehicle for virtually testing
perception, control, and planning algorithms.

To position the vehicle in the scene:

1. Select the position initialization method:

   - **Recommended for scene** — Set the initial vehicle
     position to values recommended for the scene
   - **User-specified** — Set your own initial vehicle
     position
2. Click **Update the model workspaces with the initial values** to
   overwrite the initial vehicle position in the model workspaces with the applied
   values.
