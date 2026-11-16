---
type: simulink-block
title: 'Open Differential'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Final Drive Unit'
documentation_page: 'opendifferential'
documentation_source_path: 'ref/opendifferential.html'
language: en
---

# Open Differential

## Ports

### Inputs

### **DriveshftTrq** — Torque `scalar`

Applied input torque, typically from the engine crankshaft, in
N·m.

### **Axl1Trq** — Torque `scalar`

Axle 1 torque, *T1*, in
N·m.

### **Axl2Trq** — Torque `scalar`

Axle 2 torque, *T2*, in
N·m.

### **Temp** — Temperature `scalar`

Temperature, in K.

#### Dependencies

To enable this port:

- Set **Efficiency factors** to `Driveshaft
  torque, speed and temperature`.
- Select **Input temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | | Driveshaft torque | N·m |
| `DriveshftSpd` | | Driveshaft speed | rad/s |
| `Axl1` | `Axl1Trq` | | Axle 1 torque | N·m |
| `Axl1Spd` | | Axle 1 speed | rad/s |
| `Axl2` | `Axl2Trq` | | Axle 2 torque | N·m |
| `Axl2Spd` | | Axle 2 speed | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | Mechanical power from driveshaft | W |
| `PwrAxl1` | Mechanical power from axle 1 | W |
| `PwrAxl2` | Mechanical power from axle 2 | W |
| `PwrTrnsfrd` | `PwrMechLoss` | Total power loss | W |
| `PwrDampLoss` | Power loss due to damping | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal energy | W |

### **DriveshftSpd** — Angular speed `scalar`

Driveshaft angular speed,
*ωd*, in rad/s.

### **Axl1Spd** — Angular speed `scalar`

Axle 1 angular speed, *ω1*, in
rad/s.

### **Axl2Spd** — Angular speed `scalar`

Axle 2 angular speed, *ω2*, in
rad/s.

## Parameters

#### Block Options

### **Efficiency factors** — Specify configuration `Constant` (default) | `Driveshaft torque, speed and temperature`

To account for the block efficiency, use the **Efficiency factors** parameter. This table summarizes the block implementation for each setting.

| Setting | Implementation |
| --- | --- |
| `Constant` | Constant efficiency that you can set with the **Constant efficiency factor, eta** parameter. |
| `Driveshaft torque, temperature and speed` | Efficiency as a function of base gear input torque, air temperature, and driveshaft speed. Use these parameters to specify the lookup table and breakpoints:  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    For the air temperature, you can either:  - Select **Input ambient temperature** to   create an input port. - Set a **Ambient temperature, Tamb**   parameter value.    To select the interpolation method, use the **Interpolation method** parameter. For more information, see Interpolation Methods. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DiffEffModelPopup` |
| **Values:** | `Constant` (default) | `Driveshaft torque, speed and temperature` |
| **Data Types:** | `character vector` |

### **Interpolation method** — Method `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

For more information, see Interpolation Methods.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InterpMethod` |
| **Values:** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Input ambient temperature** — Create input port `off` (default) | `on`

Select to create input port `Temp` for the temperature.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `extTamb` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Crown wheel (ring gear) located** — Specify crown wheel connection `To the left of center-line` (default) | `To the right of center-line`

Specify the crown wheel connection to the driveshaft.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `shaftSwitchMask` |
| **Values:** | `To the left of center-line` (default) | `To the right of center-line` |
| **Data Types:** | `character vector` |

### **Carrier to drive shaft ratio, Ndiff** — Ratio `4` (default) | `scalar`

Carrier-to-driveshaft gear ratio, *N*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ndiff` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Carrier inertia, Jd** — Inertia `.1` (default) | `scalar`

Rotational inertia of the crown gear assembly,
*Jd*, in kg·m^2. You can
include the driveshaft inertia.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jd` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Carrier damping, bd** — Damping `1e-3` (default) | `scalar`

Crown gear linear viscous damping,
*bd*, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bd` |
| **Values:** | `1e-3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 inertia, Jw1** — Inertia `.1` (default) | `scalar`

Axle 1 rotational inertia, *J1*,
in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jw1` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 damping, bw1** — Damping `1e-3` (default) | `scalar`

Axle 1 linear viscous damping,
*b1*, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bw1` |
| **Values:** | `1e-3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 inertia, Jw2** — Inertia `.1` (default) | `scalar`

Axle 2 rotational inertia, *J2*,
in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jw2` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 damping, bw2** — Damping `1e-3` (default) | `scalar`

Axle 2 linear viscous damping,
*b2*, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bw2` |
| **Values:** | `1e-3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 initial velocity, omegaw1o** — Angular velocity `0` (default) | `scalar`

Axle 1 initial velocity, *ωo1*, in
rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegaw1o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 initial velocity, omegaw2o** — Angular velocity `0` (default) | `scalar`

Axle 2 initial velocity, *ωo2*, in
rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegaw2o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Efficiency

### **Constant efficiency factor, eta** — Efficiency `1` (default) | positive scalar

Constant efficiency, *η*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta` |
| **Values:** | `1` (default) | positive scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors**
to `Constant`.

### **Efficiency lookup table, eta\_tbl** — Lookup table `M`-by-`N`-by-`L` array

Dimensionless array of values for efficiency as a function of:

- `M` input torques
- `N` input speed
- `L` air temperatures

Each value specifies the efficiency for a specific combination of torque,
speed, and temperature. The array size must match the dimensions defined by the torque,
speed, and temperature breakpoint vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_tbl` |
| **Values:** | `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency torque breakpoints, Trq\_bpts** — Torque breakpoints `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector

Vector of input torque, breakpoints for efficiency, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **Values:** | `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency speed breakpoints, omega\_bpts** — Speed breakpoints `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector

Vector of speed, breakpoints for efficiency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_bpts` |
| **Values:** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Efficiency temperature breakpoints, Temp\_bpts** — Temperature breakpoints `[290 358]` (default) | `1`-by-`L` vector

Vector of ambient temperature breakpoints for efficiency, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Temp_bpts` |
| **Values:** | `[290 358]` (default) | `1`-by-`L` vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Efficiency factors** to
`Driveshaft torque, speed and temperature`.

### **Ambient temperature, Tamb** — Ambient temperature `297.15` (default) | `scalar`

Ambient air temperature, *Tair*, in K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tamb` |
| **Values:** | `297.15` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter:

- Set **Efficiency factors** to `Driveshaft
  torque, speed and temperature`.
- Clear **Input ambient temperature**.

## Libraries

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Differential as a planetary bevel gear

The Open Differential block implements a differential as a planetary
bevel gear train. The block matches the driveshaft bevel gear to the crown (ring) bevel
gear. You can specify:

- Carrier-to-driveshaft ratio
- Crown wheel location
- Viscous and damping coefficients for the axles and carrier

Use the Open Differential block to:

- Dynamically couple the post-transmission driveshaft to the wheel axles or
  universal joints
- Model simplified or older drivetrains when optimal traction control does
  not require passive or active torque vectoring
- Model mechanical power splitting in generic gearbox and drive line
  scenarios

The block is suitable for use in hardware-in-the-loop (HIL) and
optimization workflows. All the parameters are tunable.

The block uses a coordinate system that produces positive tire and vehicle motion for
standard engine, transmission, and differential configurations. The arrows indicate
positive motion.

Transmission diagram

### Efficiency

To account for the block efficiency, use the **Efficiency factors** parameter. This table summarizes the block implementation for each setting.

| Setting | Implementation |
| --- | --- |
| `Constant` | Constant efficiency that you can set with the **Constant efficiency factor, eta** parameter. |
| `Driveshaft torque, temperature and speed` | Efficiency as a function of base gear input torque, air temperature, and driveshaft speed. Use these parameters to specify the lookup table and breakpoints:  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    For the air temperature, you can either:  - Select **Input ambient temperature** to   create an input port. - Set a **Ambient temperature, Tamb**   parameter value.    To select the interpolation method, use the **Interpolation method** parameter. For more information, see Interpolation Methods. |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrDriveshft` | Mechanical power from driveshaft | ηTdωd |
| `PwrAxl1` | Mechanical power from axle 1 | ηT1ω1 |
| `PwrAxl2` | Mechanical power from axle 2 | ηT2ω2 |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrMechLoss` | Total power loss | W˙loss= −(Pt+Pd)+PsPt=ηTdωd+ηT1ω1+ηT2ω2 |
| `PwrDampLoss` | Power loss due to damping | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change of stored internal energy | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### Dynamics

The Open Differential block implements these differential equations
to represent the mechanical dynamic response for the crown gear, left axle, and
right axle.

| Mechanical Dynamic Response | Differential Equation |
| --- | --- |
| Crown Gear | ω˙dJd=ηTd-ωdbd-Ti |
| Left Axle | ω˙1J1=ηT1-ω1b1-Ti1 |
| Right Axle | ω˙2J2=ηT2-ω2b2-Ti2 |

The Open Differential block assumes rigid coupling between the
crown gear and axles. These constraint equations apply.

ηTi1= ηTi2=N2Ti

ωd=N2(ω1+ω2)

The equations use these variables.

|  |  |
| --- | --- |
| *N* | Carrier-to-driveshaft gear ratio |
| *Jd* | Rotational inertia of the crown gear assembly |
| *bd* | Crown gear linear viscous damping |
| *ωd* | Driveshaft angular speed |
| *η* | Differential efficiency |
| *J1* | Axle 1 rotational inertia |
| *b1* | Axle 1 linear viscous damping |
| *ω1* | Axle 1 speed |
| *J2* | Axle 2 rotational inertia |
| *b2* | Axle 2 linear viscous damping |
| *ω2* | Axle 2 angular speed |
| *Td* | Driveshaft torque |
| *T1* | Axle 1 torque |
| *T2* | Axle 2 torque |
| *Ti* | Driveshaft internal resistance torque |
| *Ti1* | Axle 1 internal resistance torque |
| *Ti2* | Axle 2 internal resistance torque |
