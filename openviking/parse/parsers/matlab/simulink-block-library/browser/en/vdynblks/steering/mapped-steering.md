---
type: simulink-block
title: 'Mapped Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'mappedsteering'
documentation_source_path: 'ref/mappedsteering.html'
language: en
---

# Mapped Steering

## Ports

### Input

### **AngIn** — Steering angle `scalar`

Steering angle, *δin*, in
rad.

Use the **Steering angle breakpoints, StrgAngBpts**
parameter to specify a steering angle range. By default, the value is
set to 1.25\*pi, which limits the steering angle to a range of -1.25\*pi
to 1.25\*pi.

### **VehSpd** — Vehicle speed `scalar`

Vehicle speed, *Vehspd*, in
m/s.

#### Dependencies

To create this port, select **Speed
dependent**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Variable | Unit |
| --- | --- | --- | --- |
| `AngLft` | Left wheel angle | *δL* | rad |
| `AngRght` | Left wheel angle | *δR* | rad |

### **AngLft** — Left wheel angle `scalar`

Left wheel angle, *δL*, in
rad.

### **AngRght** — Right wheel angle `scalar`

Right wheel angle, *δR*, in
rad.

## Parameters

#### Options

### **Speed dependent** — Use speed-dependent tables on (default) | off

Select to use speed-dependent tables.

#### Dependencies

Selecting this parameter creates input port
`VehSpd`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SpdDpd` |
| **Values:** | on (default) | off |
| **Data Types:** | `character vector` |

### **Steering type** — Use speed-dependent tables `Steering wheel angle` (default) | `Rack travel displacement`

If you set **Steering type** to `Steering
wheel angle`, the block implements these
tables.

| Speed Dependent | Implementation |
| --- | --- |
| `on` (default) | Block uses three tables:  - *fs*   — Function of vehicle speed - *fL*   — Function of superimposed steering wheel   angle - *fR*   — Function of superimposed steering wheel   angle |
| `off` | Block uses two tables:  - *fL*   — Function of steering wheel angle - *fR*   — Function of steering wheel angle |

If you set **Steering type** to `Rack travel
displacement`, the block implements these
tables.

| Speed Dependent | Implementation |
| --- | --- |
| `on` (default) | Block uses three tables:  - *fs*   — Function of vehicle speed - *fL*   — Function of rack travel displacement - *fR*   — Function of rack travel displacement |
| `off` | Block uses two tables:  - *fL*   — Function of rack travel displacement - *fR*   — Function of rack travel displacement |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IndexType` |
| **Values:** | `Steering wheel angle` (default) | `Rack travel displacement` |
| **Data Types:** | `character vector` |

### **Steering angle breakpoints, StrgAngBpts** — Steering angle breakpoints `[-1.5*pi 1.5*pi]` (default) | `vector`

Steering angle breakpoints, in rad.

#### Dependencies

If you set **Steering type** to `Rack
travel displacement`, to enable this parameter, set
**Gear ratio parameterized by** to
`Lookup table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgAngBpts` |
| **Values:** | `[-1.5*pi 1.5*pi]` (default) | `vector` |
| **Data Types:** | `double` |

### **Rack travel displacement breakpoints, RackDispBpts** — Rack travel displacement breakpoints `[-40 -19.2 -4.53 4.53 19.2 40]` (default) | `vector`

Rack travel displacement breakpoints, in mm.

#### Dependencies

To enable this parameter, set **Steering type** to
`Rack travel displacement` and
**Gear ratio parameterized by** to
`Lookup table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RackDispBpts` |
| **Values:** | `[-40 -19.2 -4.53 4.53 19.2 40]` (default) | `vector` |
| **Data Types:** | `double` |

### **Gear ratio table, GrTbl** — Gear ratio table `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi` (default) | `vector`

Gear ratio table as a function of rack travel displacement, in
mm/rev.

#### Dependencies

To enable this parameter, set **Steering type** to
`Rack travel displacement` and
**Gear ratio parameterized by** to
`Lookup table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `GrTbl` |
| **Values:** | `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi` (default) | `vector` |
| **Data Types:** | `double` |

### **Gear ratio constant, Gr** — Gear ratio constant `8.28*2*pi` (default) | `scalar`

Gear ratio constant, in mm/rev.

#### Dependencies

To enable this parameter, set **Steering type** to
`Rack travel displacement` and
**Gear ratio parameterized by** to
`Constant`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Gr` |
| **Values:** | `8.28*2*pi` (default) | `scalar` |
| **Data Types:** | `double` |

### **Left wheel angle table, WhlLftTbl** — Left wheel angle table `[-1.5*pi 1.5*pi]/13.5]` (default) | `vector`

Left wheel angle table, *δL*, in
rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WhlLftTbl` |
| **Values:** | `[-1.5*pi 1.5*pi]/13.5]` (default) | `vector` |
| **Data Types:** | `double` |

### **Right wheel angle table, WhlRghtTbl** — Right wheel angle table `[-1.5*pi 1.5*pi]/13.5]` (default) | `vector`

Right wheel angle table, *δR*, in
rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WhlRghtTbl` |
| **Values:** | `[-1.5*pi 1.5*pi]/13.5]` (default) | `vector` |
| **Data Types:** | `double` |

### **Vehicle speed breakpoints, VehSpdBpts** — Vehicle speed breakpoints `[-1 1]` (default) | `vector`

Vehicle speed breakpoints, in m/s.

#### Dependencies

To create this parameter, select **Speed dependent**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VehSpdBpts` |
| **Values:** | `[-1 1]` (default) | `vector` |
| **Data Types:** | `double` |

### **Superimposed speed factor table, SpdFctTbl** — Speed factor `[1 1]` (default) | `vector`

Superimposed speed factor table,
*ƒs*, dimensionless. The table
is a factor of vehicle speed, *v*.

#### Dependencies

To create this parameter, select **Speed dependent**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SpdFctTbl` |
| **Values:** | `[1 1]` (default) | `vector` |
| **Data Types:** | `double` |

## Libraries

Vehicle Dynamics Blockset / Steering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Mapped steering with speed-dependent option

The Mapped Steering block implements lookup tables to calculate the
right and left wheel angles. Use the **Speed dependent** parameter to
implement a speed-dependent table for the steering angle calculations. The block uses
the vehicle coordinate system.

### Steering Wheel Angle

If you set **Steering type** to `Steering wheel
angle`, the block implements these tables.

| Speed Dependent | Implementation | Calculations |
| --- | --- | --- |
| `on` (default) | Block uses three tables:  - *fs* —   Function of vehicle speed - *fL* —   Function of superimposed steering wheel   angle - *fR* —   Function of superimposed steering wheel   angle | δSpdF=fs(v)δSuprImp=δSpdF⋅δinδL=fL(δSuprImp)δR=fR(δSuprImp) |
| `off` | Block uses two tables:  - *fL* —   Function of steering wheel angle - *fR* —   Function of steering wheel angle | δL=fL(δin)δR=fR(δin) |

### Rack Travel Displacement

If you set **Steering type** to `Rack travel
displacement`, the block implements these tables.

| Speed Dependent | Implementation | Calculations |
| --- | --- | --- |
| `on` (default) | Block uses three tables:  - *fs* —   Function of vehicle speed - *fL* —   Function of rack travel displacement - *fR* —   Function of rack travel displacement | δSpdF=fs(v)δSuprImp=δSpdF⋅δinΔRack=δSuprImp⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |
| `off` | Block uses two tables:  - *fL* —   Function of rack travel displacement - *fR* —   Function of rack travel displacement | ΔRack=δin⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |

The block uses a gear ratio to adjust the rack travel displacement. To use a

- Constant gear ratio, set **Gear ratio parameterized
  by** to `Constant`.
- Gear ratio as a function of steering angle, set **Gear ratio
  parameterized by** to `Lookup
  table`.

The equations use these variables.

|  |  |
| --- | --- |
| *δin* | Steering wheel angle |
| *δSpdF* | Steering wheel angle speed factor |
| *δSuprImp* | Superimposed steering wheel angle |
| *δL*, *δR* | Left and right wheel angles, respectively |
| *ΔRack* | Rack travel displacement |
| *Gr* | Gear ratio |
