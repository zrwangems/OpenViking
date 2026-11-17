---
type: simulink-block
title: 'Simulation 3D Spacecraft'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dspacecraft'
documentation_source_path: 'simulation3dspacecraft.html'
language: en
---

# Simulation 3D Spacecraft

## Ports
```yaml
ports:
- name: Translation
  summary: Spacecraft translation 10-by-3 array | 20-by-3 array
  direction: input
  data_types: single | double
- name: Rotation
  summary: Spacecraft rotation 10-by-3 array | 20-by-3 array
  direction: input
  data_types: single | double
- name: Scale
  summary: Mesh scale [1 1 1] (default) | 1-by-3 array
  direction: input
```

### Input

### **Translation** — Spacecraft translation 10-by-3 array | 20-by-3 array

Spacecraft translation, specified as:

- 10-by-3 array — Spacecraft **Type** is
  `CubeSat`.
- 20-by-3 array — Spacecraft **Type** is
  `SmallSat`.

The signal contains translation [*X*, *Y*,
*Z*], in meters, with one row of the array for each bone of the
spacecraft.

The translation applies to these bones of the `CubeSat`
type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ANTENNA1 | 2 |
| ANTENNA2 | 3 |
| ANTENNA3 | 4 |
| SENSOR | 5 |
| SOLAR\_ARRAY1 | 6 |
| SOLAR\_ARRAY1\_1 | 7 |
| SOLAR\_ARRAY2 | 8 |
| SOLAR\_ARRAY2\_2 | 9 |
| THRUSTER | 10 |

The translation applies to these bones of the `SmallSat`
type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ANTENNA1 | 2 |
| ANTENNA2 | 3 |
| ANTENNA3 | 4 |
| ANTENNA4 | 5 |
| SENSOR1 | 6 |
| SENSOR2 | 7 |
| SENSOR3 | 8 |
| SENSOR4 | 9 |
| SOLAR\_ARRAY1 | 10 |
| SOLAR\_ARRAY1\_1 | 11 |
| SOLAR\_ARRAY1\_1\_1 | 12 |
| SOLAR\_ARRAY1\_1\_1\_1 | 13 |
| SOLAR\_ARRAY1\_1\_1\_1\_1 | 14 |
| SOLAR\_ARRAY2 | 15 |
| SOLAR\_ARRAY2\_2 | 16 |
| SOLAR\_ARRAY2\_2\_2 | 17 |
| SOLAR\_ARRAY2\_2\_2\_2 | 18 |
| SOLAR\_ARRAY2\_2\_2\_2\_2 | 19 |
| THRUSTER | 20 |

**Data Types:** `single` | `double`

### **Rotation** — Spacecraft rotation 10-by-3 array | 20-by-3 array

Spacecraft rotation, specified as:

- 10-by-3 array — Spacecraft **Type** is
  `CubeSat`.
- 20-by-3 array — Spacecraft **Type** is
  `SmallSat`.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the spacecraft.

**Data Types:** `single` | `double`

### **Scale** — Mesh scale `[1 1 1]` (default) | 1-by-3 array

Mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this port, set the **Scale source** parameter to `Port`.
## Parameters
```yaml
parameters:
- name: Type
  summary: Spacecraft type CubeSat (default) | SmallSat
  group: ''
  block_parameter: Mesh
  values: CubeSat (default) | SmallSat
- name: Path to CubeSat mesh
  summary: Path to CubeSat mesh /MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat (default)
    | character vector
  group: ''
  block_parameter: MeshPath
  values: /MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat | character vector
- name: Path to SmallSat mesh
  summary: Path to SmallSat mesh /MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat (default)
    | character vector
  group: ''
  block_parameter: MeshPathSmall
  values: /MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat | character vector
- name: Name
  summary: Spacecraft name SimulinkVehicle1 (default) | character vector
  group: ''
  block_parameter: ActorName
  values: SimulinkVehicle1 (default) | character vector
- name: Initial translation (m)
  summary: Initial translation of spacecraft zeros(10,3) (default) | 10-by-3 array | 20-by-3 array
  group: ''
  type: . Failure to appropriately set these array sizes causes an
  block_parameter: Translation
  values: zeros(10,3) (default) | 10-by-3 array | 20-by-3 array
- name: Initial rotation (rad)
  summary: Initial rotation of spacecraft zeros(10,3) (default) | 10-by-3 array | 20-by-3 array
  group: ''
  type: . Failure to appropriately set these array sizes causes an
  block_parameter: Rotation
  values: zeros(10,3) (default) | 10-by-3 array | 20-by-3 array
- name: Scale source
  summary: Scale source Dialog (default) | Port
  group: ''
  block_parameter: ScaleInputPort
  values: Dialog (default) | Port
- name: Initial scale
  summary: Initial mesh scale [1 1 1] (default) | 1-by-3 array
  group: ''
  block_parameter: InitialScale
  values: '[1 1 1] (default) | 1-by-3 array'
- name: Scale
  summary: Mesh scale [1 1 1] (default) | 1-by-3 array
  group: ''
  block_parameter: Scale
  values: '[1 1 1] (default) | 1-by-3 array'
- name: Sample time
  summary: Sample time 0.02 (default) | real scalar
  group: ''
  block_parameter: SampleTime
  values: '''-1'' (default) | real scalar'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Type** — Spacecraft type `CubeSat` (default) | `SmallSat`

Spacecraft type, specified as `CubeSat` or
`SmallSat`.

#### Dependencies

To set this parameter, set the **Initial translation** and
**Initial rotation** parameters to the matching array size. Failure
to appropriately set these array sizes causes an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Mesh` |
| **Values:** | `CubeSat` (default) | `SmallSat` |

**Example:** `CubeSat`

### **Path to CubeSat mesh** — Path to CubeSat mesh `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat` (default) | character vector

Path to CubeSat mesh, specified as a character vector. To create a custom aerospace
mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

To enable this parameter, set **Type** to
`CubeSat`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MeshPath` |
| **Values:** | `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat` | character vector |

**Example:** `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat`

### **Path to SmallSat mesh** — Path to SmallSat mesh `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat` (default) | character vector

Path to SmallSat mesh, specified as a character vector. To create a custom aerospace
mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

To enable this parameter, set **Type** to
`SmallSat`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MeshPathSmall` |
| **Values:** | `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat` | character vector |

**Example:** `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat`

### **Name** — Spacecraft name `SimulinkVehicle1` (default) | character vector

Spacecraft name, specified as a character vector. By default, when you use the
Simulation 3D Spacecraft block in your model, the block sets the
**Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of other
Simulation 3D blocks that you have in your model.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ActorName` |
| **Values:** | `SimulinkVehicle1` (default) | character vector |

**Example:** `SimulinkVehicle1`

### **Initial translation (m)** — Initial translation of spacecraft `zeros(10,3)` (default) | 10-by-3 array | 20-by-3 array

Initial translation of spacecraft, specified as a 10-by-3 array or 20-by-3 array.

#### Dependencies

This parameter must match the spacecraft type you set in
**Type**. Failure to appropriately set these array sizes causes an
error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Translation` |
| **Values:** | `zeros(10,3)` (default) | 10-by-3 array | 20-by-3 array |
| **Data Types:** | `single` | `double` |

**Example:** `zeros(10,3)`

### **Initial rotation (rad)** — Initial rotation of spacecraft `zeros(10,3)` (default) | 10-by-3 array | 20-by-3 array

Initial rotation of spacecraft, specified as a 10-by-3 or 20-by-3 array.

#### Dependencies

This parameter must match the spacecraft type you set in
**Type**. Failure to appropriately set these array sizes causes an
error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rotation` |
| **Values:** | `zeros(10,3)` (default) | 10-by-3 array | 20-by-3 array |
| **Data Types:** | `single` | `double` |

**Example:** `zeros(10,3)`

### **Scale source** — Scale source `Dialog` (default) | `Port`

Scale source, specified as `Dialog` or
`Port`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ScaleInputPort` |
| **Values:** | `Dialog` (default) | `Port` |

**Example:** `Dialog`

### **Initial scale** — Initial mesh scale `[1 1 1]` (default) | 1-by-3 array

Initial mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this parameter, set **Scale source** to
`Port`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialScale` |
| **Values:** | `[1 1 1]` (default) | 1-by-3 array |
| **Data Types:** | `single` | `double` |

**Example:** `[1 1 1]`

### **Scale** — Mesh scale `[1 1 1]` (default) | 1-by-3 array

Mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this parameter, set **Scale source** to
`Dialog`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Scale` |
| **Values:** | `[1 1 1]` (default) | 1-by-3 array |
| **Data Types:** | `single` | `double` |

**Example:** `[1 1 1]`

### **Sample time** — Sample time `0.02` (default) | real scalar

Sample time, *Ts*. The graphics frame rate
is the inverse of the sample time.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'-1'` (default) | real scalar |

**Example:** `'-1'`
## Libraries

Aerospace Blockset / Animation / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2024b: Simulation 3D Environment: Scale mesh for Simulation 3D Spacecraft

You can now change the size of the mesh for the Simulation 3D Spacecraft block using the
**Scale** parameter or the **Scale** port. The default scale is
a 1-by-3 vector of `[1 1 1]`.

To enable the parameters or port, use the **Scale source**
parameter.

- `Dialog` — Enable the **Scale** parameter.
- `Port` — Enable the **Scale** port and
  **Initial scale** parameter.

## Description

Implement spacecraft in 3D environment

**Note**

Simulating models with the Simulation 3D Spacecraft block requires
Simulink®
3D Animation™.

The Simulation 3D Spacecraft block implements spacecraft in a 3D
visualization environment using translation and rotation to place the spacecraft.

To use this block, your model must contain a Simulation 3D Scene
Configuration block. If you set the **Sample time** parameter of
the Simulation 3D Spacecraft block to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block.

The block input uses the spacecraft north-east-down (NED)
*right-handed* (RH) *Cartesian* coordinate system.

- *X*-axis — Along spacecraft longitudinal axis, points forward
- *Y*-axis — Along spacecraft lateral axis, points to the
  right
- *Z*-axis — Points downward

For more information, see Fundamental Coordinate System Concepts.

**Tip**

Verify that the Simulation 3D Spacecraft
block executes before the Simulation 3D Scene Configuration block. That way,
the Simulation 3D Spacecraft block prepares the signal data before the
Unreal Engine® 3D visualization environment receives the data. To check the block execution
order, right-click each block and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Spacecraft — `-1`

For more information about execution order, see Control and Display Execution Order.

### Skeletons, Bones, and Meshes

Unreal Engine uses a *skeleton*, *bones*, and a
*mesh* to define a 3D model. A skeleton is comprised of a set of
bones. A mesh is the outer covering of the skeleton. Spacecraft parts are sections of the
mesh, such as antenna or thrusters, that are linked to the bones. For more information, see
https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/.

For more information on how the Simulation 3D Space block translation
input arrays connect to spacecraft types, see Algorithms.
