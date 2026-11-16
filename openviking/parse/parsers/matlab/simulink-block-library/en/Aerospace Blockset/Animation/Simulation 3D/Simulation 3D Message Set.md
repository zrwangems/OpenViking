---
type: simulink-block
title: 'Simulation 3D Message Set'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dmessageset'
documentation_source_path: 'simulation3dmessageset.html'
language: en
---

# Simulation 3D Message Set

## Ports

### Input

### **WriteMsg** — Data sent to scene `scalar` | `array`

Data sent to the 3D visualization environment scene. In the Unreal Engine environment, you can configure the `Sim3DGet` class to
receive the data from the Simulink model.

## Parameters

### **Signal name, SigName** — Message signal name `mySignal` (default)

Specifies the signal name in the 3D visualization environment. In the Unreal Engine environment, use the `Sim3Get` actor class 'Tags'
property located in the 'Details' pane.

For example, you can send data to the double lane change scene that changes the
traffic signal light color to red, yellow, or green. To send data to the traffic signal
light, set this parameter to `TrafficLight1`. In the double lane change
scene, the 'Tags' property value for `Sim3dGetInteger` actor class is
set to TrafficLight1.

### **Sample time** — Sample time `0.02` (default) | `-1` | `scalar`

Sample time, in s. The graphics frame rate is the inverse of the sample time. If you
set the sample time to `-1`, the block uses the sample time specified
in the Simulation 3D Scene Configuration block.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Message Set block requires
Simulink
3D Animation.

## Description

Send data to Unreal Engine visualization environment

**Note**

Simulating models with the Simulation 3D Message Set block requires
Simulink®
3D Animation™.

The Simulation 3D Message Set block sends data to the Unreal Engine® 3D visualization environment. In your model, ensure that the Simulation
3D Scene Configuration block is at the same level as the Simulation 3D
Message Set block.

**Tip**

Verify that the Simulation 3D Message
Set block executes before the Simulation 3D Scene Configuration
block. That way, Simulation 3D Message Set prepares the signal data before
the Unreal Engine 3D visualization environment receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Set — `-1`

For more information about execution order, see Control and Display Execution Order.

### Configure Scenes to Receive Data

To use the block, you must configure scenes in the Unreal Engine environment to receive data from the Simulink model:

1. Install the customize 3D scenes for aerospace
   simulations.
2. In the Unreal® Editor, follow these general workflows to receive data from Simulink.

   | Unreal Engine User | Workflow |
   | --- | --- |
   | Blueprint | 1. Instantiate the `Sim3DGet` actor that    corresponds to the data type you want to receive from the    Simulink model. This example shows the Unreal Editor `Sim3DGet` data types.  Image of Unreal Engine options 2. Specify an actor tag name that matches the    Simulation 3D Message Set block    **Signal name** parameter. 3. Navigate to the Level Blueprint. 4. Find the blueprint method for the    `Sim3DGet` actor class based on the    data type and size that you want to receive from the    Simulink model.  For example, in Unreal Editor, this diagram shows that `Read    Scalar Integer` is the method for    `Sim3DGetInteger` actor class to    receive `int32` data type of size scalar.  Image of Unreal Engine blueprint connections 5. Compile and save the scene.    **Note**  By default, the Double Lane Change scene has a `Sim3DGetInteger` actor with tag name `TrafficLight1`. |
   | C++ class | 1. Create a new actor class for the mesh or asset that you    want the Simulink model to interact with. Derive it from `ASim3dActor`. 2. In the new actor class:  - Declare a pointer to the signal name as a      class field.    - Get the class tag.    - Create a signal reader and assign the pointer      in the method `Sim3dSetup`.    - In the method `Sim3dStep`, invoke the `ReadSimulation3DMessage` function to      read the data from a Simulink model.    - Delete the signal reader in the method      `Sim3dRelease` of the actor. |

   For more information about the Unreal Editor, see the Unreal
   Engine Documentation.
