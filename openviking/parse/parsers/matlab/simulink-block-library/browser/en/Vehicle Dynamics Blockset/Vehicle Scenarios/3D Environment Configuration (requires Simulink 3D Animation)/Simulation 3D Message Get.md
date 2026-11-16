---
type: simulink-block
title: 'Simulation 3D Message Get'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dmessageget'
documentation_source_path: 'ref/simulation3dmessageget.html'
language: en
---

# Simulation 3D Message Get

## Ports

### Output

### **ReadMsg** — Data retrieved from scene `scalar` | `array`

Data retrieved from the 3D visualization environment scene data. In the
Unreal Engine environment, you can use the `Sim3DSet` class to
configure scene actors to send data to the Simulink model.

For example, in the
Unreal Editor, the Double Lane Change scene has a
`Sim3DSetBoolean` actor with tag name
`NumOfConesHit`. Use it to retrieve the number of cones the vehicle
hits during a double-lane change maneuver.

This
table provides the Double Lane Change scene cone name that corresponds to the
`ReadMsg` array element.

| Simulation 3D Message Get Block `ReadMsg` Value | Unreal Editor Cone Name | Simulation 3D Message Get Block Array Element | Unreal Editor Cone Name |
| --- | --- | --- | --- |
| `ReadMsg(1,1)` | `SM_Cone5` | `ReadMsg(2,1)` | `SM_Cone10` |
| `ReadMsg(1,2)` | `SM_Cone4` | `ReadMsg(2,2)` | `SM_Cone09` |
| `ReadMsg(1,3)` | `SM_Cone3` | `ReadMsg(2,3)` | `SM_Cone08` |
| `ReadMsg(1,4)` | `SM_Cone2` | `ReadMsg(2,4)` | `SM_Cone07` |
| `ReadMsg(1,5)` | `SM_Cone01` | `ReadMsg(2,5)` | `SM_Cone06` |
| `ReadMsg(1,6)` | `SM_Cone15` | `ReadMsg(2,6)` | `SM_Cone20` |
| `ReadMsg(1,7)` | `SM_Cone14` | `ReadMsg(2,7)` | `SM_Cone19` |
| `ReadMsg(1,8)` | `SM_Cone13` | `ReadMsg(2,8)` | `SM_Cone18` |
| `ReadMsg(1,9)` | `SM_Cone12` | `ReadMsg(2,9)` | `SM_Cone17` |
| `ReadMsg(1,10)` | `SM_Cone11` | `ReadMsg(2,10)` | `SM_Cone16` |
| `ReadMsg(1,11)` | `SM_Cone25` | `ReadMsg(2,11)` | `SM_Cone30` |
| `ReadMsg(1,12)` | `SM_Cone24` | `ReadMsg(2,12)` | `SM_Cone29` |
| `ReadMsg(1,13)` | `SM_Cone23` | `ReadMsg(2,13)` | `SM_Cone28` |
| `ReadMsg(1,14)` | `SM_Cone22` | `ReadMsg(2,14)` | `SM_Cone27` |
| `ReadMsg(1,15)` | `SM_Cone21` | `ReadMsg(2,15)` | `SM_Cone26` |

## Parameters

### **Signal name, SigName** — Message signal name `mySignal` (default)

Specifies the signal name in the 3D visualization environment. In the Unreal Engine environment, use the `Sim3DSet` actor class 'Tags'
property located in the 'Details' pane.

For example, you can retrieve data from the double-lane change scene that indicates
if cones are hit during a double-lane change maneuver. To retrieve cone hit data from
the double-lane change scene, set this parameter to `NumOfConesHit`. In
the double-lane change scene, the `Sim3DSet` actor class 'Tags'
property is set to `NumOfConesHit`.

### **Data type, DataType** — Message data type `double`\* | `single` | `int8`\* | `uint8`\* | `int16`\* | `uint16`\* | `int32` | `uint32`\* | `boolean`

3D visualization environment signal data type. The supported data types depend on
the Unreal Engine workflow.

| Workflow | Supported Data Types |
| --- | --- |
| Blueprint | `single`  `int32`  `Boolean` |
| \*C++ class | `double`  `single`  `int8`  `uint8`  `int16`  `uint16`  `int32`  `uint32`  `Boolean` |

In the Unreal Engine environment, instantiate the `Sim3DSet` actor class for
the data type that you want to send to the Simulink model. For example, you can retrieve data from the double-lane change
scene that indicates if cones are hit during a double-lane change maneuver. To retrieve
cone hit data from the double-lane change scene, set this parameter to
`boolean`. In the double-lane change scene, the
`Sim3DSetBoolean` actor class is instantiated to send the cone hit or
miss boolean data.

### **Message size, MsgSize** — Message dimension `[1 1]` (default) | `scalar` | `array`

3D visualization environment signal dimension. In the Unreal Engine environment blueprint, set the input to the node of the
`Sim3DSet` actor class to specify the dimensions of data that you
want to send to the Simulink model.

For example, you can retrieve data from the double-lane change scene that indicates
if cones are hit during a double-lane change maneuver. To retrieve cone hit data from
the double-lane change scene, set this parameter to `[2 15]`. In the
double-lane change scene, the input to the blueprint node for the
`Sim3DSetBoolean` actor class is set to 30, the number of cones in
the scene.

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

**Introduced in R2019b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Message Get block requires
Simulink
3D Animation.

## Description

Retrieve data from Unreal Engine visualization environment

**Note**

Simulating models with the Simulation 3D Message Get block requires
Simulink®
3D Animation™.

The Simulation 3D Message Get block retrieves data from the Unreal Engine® 3D visualization environment. In your model, ensure that the Simulation
3D Scene Configuration block is at the same level as the Simulation 3D
Message Get block.

**Tip**

Verify that the Simulation 3D Scene
Configuration block executes before the Simulation 3D Message Get
block. That way, the Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Message Get block receives it. To check the block execution order, right-click the
blocks and select **Properties**. On the **General** tab,
confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Get — `1`

For more information about execution order, see Control and Display Execution Order.

### Configure Scenes to Send Data

To use the block, you must configure scenes in the Unreal Engine environment to send data to the Simulink model:

1. Install the Customize 3D Scenes for Vehicle Dynamics Simulations.
2. In the Unreal® Editor, follow these general workflows to send data to Simulink. For detailed information, see Get Started Communicating with the Unreal Engine Visualization Environment.

   | Unreal Engine User | Workflow |
   | --- | --- |
   | Blueprint | 1. Instantiate the `Sim3DSet` actor that    corresponds to the data type you want to send to the    Simulink model. This example shows the Unreal Editor `Sim3DSet` data types.  Image of Unreal Engine options 2. Specify an actor tag name that matches the    Simulation 3D Message Get block    **Signal name** parameter. 3. Navigate to the Level Blueprint. 4. Find the blueprint method for the    `Sim3DSet` actor class based on the    data type and size specified by the Simulation 3D    Message Get block **Data type**    and **Message size** parameters.  For example, in Unreal Editor, this diagram shows that `Write    Array Boolean` is the method for the    `Sim3DSetBoolean` actor class that    sends Boolean data type of array size 30.  Image of Unreal Engine blueprint connections 5. Compile and save the scene.    **Note**  By default, the Double Lane Change scene has a `Sim3DSetBoolean` actor with tag name `NumOfConesHit`. |
   | C++ class | 1. Create a new actor class for the mesh or asset that you    want the Simulink model to interact with. Derive it from `ASim3dActor`. 2. In the new actor class:  - Declare a pointer to the signal name as a      class field.    - Get the class tag.    - Create a signal writer and assign the pointer      in the method `Sim3dSetup`.    - In the method `Sim3dStep`, invoke the `WriteSimulation3DMessage` function to      write the data to the Simulink model.    - Delete the signal writer in the method      `Sim3dRelease` of the actor. |

   For more information about the Unreal Editor, see the Unreal
   Engine Documentation.
