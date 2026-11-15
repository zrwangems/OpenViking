---
type: simulink-block
title: 'Limited Slip Differential'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain and Transmission / Drivetrain – Final Drive Unit and Wheels'
documentation_page: 'limitedslipdifferential'
documentation_source_path: 'ref/limitedslipdifferential.html'
language: en
---

# Limited Slip Differential

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
| `Cplng` | `CplngTrq` | | Torque coupling | N·m |
| `CplngSlipSpd` | | Slip speed | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | Mechanical power from driveshaft | W |
| `PwrAxl1` | Mechanical power from axle 1 | W |
| `PwrAxl2` | Mechanical power from axle 2 | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | Total power loss | W |
| `PwrDampLoss` | Power loss due to damping | W |
| `PwrCplngLoss` | Power loss due to clutch | W |
| `PwrStoredShft` | `PwrStoredShft` | Rate change of stored internal energy | W |

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

#### Open Differential

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

### **Carrier to drive shaft ratio, NC/ND** — Ratio `4` (default) | `scalar`

Carrier-to-driveshaft gear ratio, *N*.

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

#### Slip Coupling

### **Coupling type** — Torque coupling `Pre-loaded ideal clutch` (default) | `Slip speed dependent torque data` | `Input torque dependent torque data`

Specify the type of torque coupling.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `couplingType` |
| **Values:** | `Pre-loaded ideal clutch` (default) | `Slip speed dependent torque data` | `Input torque dependent torque data` |
| **Data Types:** | `character vector` |

### **Number of disks, Ndisks** — Torque coupling `4` (default) | `scalar`

Number of disks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ndisks` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the ideal clutch parameters, select `Pre-loaded
ideal clutch` for the **Coupling
type** parameter.

### **Effective radius, Reff** — Radius `.20` (default) | `scalar`

The effective radius, Reff, used with the applied clutch friction force to determine
the friction force. The effective radius is defined as:

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

The equation uses these variables.

|  |  |
| --- | --- |
| Ro | Annular disk outer radius |
| Ri | Annular disk inner radius |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Reff` |
| **Values:** | `.20` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the clutch parameters, select `Pre-loaded ideal
clutch` for the **Coupling type**
parameter.

### **Nominal preload force, Fc** — Force `500` (default) | `scalar`

Nominal preload force, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fc` |
| **Values:** | `500` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the clutch parameters, select `Pre-loaded ideal
clutch` for the **Coupling type**
parameter.

### **Friction coefficient vector, muc** — Friction `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]` (default) | `vector`

Friction coefficient vector.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `muc` |
| **Values:** | `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the clutch parameters, select `Pre-loaded ideal
clutch` for the **Coupling type**
parameter.

### **Slip speed vector, dw** — Angular velocity `[0 10 20 40 60 80 100]` (default) | `vector`

Slip speed vector, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dw` |
| **Values:** | `[0 10 20 40 60 80 100]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the clutch parameters, select `Pre-loaded ideal
clutch` for the **Coupling type**
parameter.

### **Torque - slip speed vector, Tdw** — Torque `[-100, -90, -50, -5, 0, 5, 50, 90, 100]` (default) | `vector`

Torque vector, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tdw` |
| **Values:** | `[-100, -90, -50, -5, 0, 5, 50, 90, 100]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the slip speed parameters, select `Slip speed
dependent torque data` for the **Coupling
type** parameter.

### **Slip speed vector, dwT** — Angular velocity `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]` (default) | `vector`

Slip speed vector, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dwT` |
| **Values:** | `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the slip speed parameters, select `Slip speed
dependent torque data` for the **Coupling
type** parameter.

### **Torque - input torque vector, TTin** — Torque `[-200 -175 -100 - 50 0 50 100 175 200]` (default) | `vector`

Torque vector, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TTin` |
| **Values:** | `[-200 -175 -100 - 50 0 50 100 175 200]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the input torque parameters, select `Input
torque dependent torque data` for the
**Coupling type** parameter.

### **Input torque vector, Tin** — Torque `[-200 -175 -100 - 50 0 50 100 175 200]` (default) | `vector`

Torque vector, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tin` |
| **Values:** | `[-200 -175 -100 - 50 0 50 100 175 200]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the input torque parameters, select `Input
torque dependent torque data` for the
**Coupling type** parameter.

### **Coupling time constant, tauC** — Constant `.01` (default) | `scalar`

Coupling time constant, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tauC` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Limited differential as a planetary bevel gear

The Limited Slip Differential block implements a differential as a
planetary bevel gear train. The block matches the driveshaft bevel gear to the crown
(ring) bevel gear. You can specify:

- Carrier-to-driveshaft ratio
- Crown wheel location
- Viscous and damping coefficients for the axles and carrier
- Type of slip coupling

Use the block in system-level driveline analysis to account for the power transfer
from the transmission to the wheels. The block is suitable for use in
hardware-in-the-loop (HIL) and optimization workflows. All the parameters are
tunable.

In a limited slip differential, to prevent one of the wheels from slipping, the
differential splits the torque applied to the left and right axles. With different
torque applied to the axles, the wheels can move at different angular velocities,
preventing slip. The block implements three methods for coupling the different torques
applied to the axes:

- Pre-loaded ideal clutch
- Slip speed-dependent torque data
- Input torque dependent torque data

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
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrMechLoss` | Total power loss | W˙loss= −(Pt+Pd+Pc)+PsPt=η(Tdωd+T1ω1+T2ω2) |
| `PwrDampLoss` | Power loss due to damping | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrCplngLoss` | Power loss due to clutch | Pc=Tc|ω¯| |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change of stored internal energy | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### Dynamics

The Limited Slip Differential block implements these differential
equations to represent the mechanical dynamic response for the crown gear, left
axle, and right axle.

| Mechanical Dynamic Response | Differential Equation |
| --- | --- |
| Crown Gear | ω˙dJd=ηTd-ωdbd-Ti |
| Left Axle | ω˙1J1=ηT1-ω1b1-Ti1 |
| Right Axle | ω˙2J2=ηT2-ω2b2-Ti2 |

The block assumes rigid coupling between the crown gear and axles. These
constraint equations apply.

ηT1=N2Ti−12TcηT2=N2Ti+12Tc

ωd=N2(ω1+ω2)

The equations use these variables.

|  |  |
| --- | --- |
| *N* | Carrier-to-driveshaft gear ratio |
| *Jd* | Rotational inertia of the crown gear assembly |
| *bd* | Crown gear linear viscous damping |
| *ωd* | Driveshaft angular speed |
| ϖ | Slip speed |
| *J1* | Axle 1 rotational inertia |
| *b1* | Axle 1 linear viscous damping |
| *ω1* | Axle 1 speed |
| *J2* | Axle 2 rotational inertia |
| *b2* | Axle 2 linear viscous damping |
| *ω2* | Axle 2 angular speed |
| *η* | Efficiency |
| *Td* | Driveshaft torque |
| *T1* | Axle 1 torque |
| *T2* | Axle 2 torque |
| *Ti* | Axle internal resistance torque |
| *Ti1* | Axle 1 internal resistance torque |
| *Ti2* | Axle 2 internal resistance torque |
| *μ* | Coefficient of friction |
| Reff | Effective clutch radius |
| Ro | Annular disk outer radius |
| *Ri* | Annular disk inner radius |
| *Fc* | Clutch force |
| *Tc* | Clutch torque |
| *μ* | Coefficient of friction |

Table blocks in the Limited Slip Differential have these parameter settings:

- **Interpolation method** —
  `Linear`
- **Extrapolation method** —
  `Clip`

**Ideal Clutch Coupling**

The ideal clutch coupling model uses the axle slip speed and friction to
calculate the clutch torque. The friction coefficient is a function of the slip speed.

Tc=FcNμ(|ϖ|)Refftanh(4|ϖ|)

The disc radii determine the effective clutch radius over which the clutch
force acts.

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

The angular velocities of the axles determine the slip speed.

ϖ=ω1−ω2

**Slip Speed Coupling**

To calculate the clutch torque, the slip speed coupling model uses torque data
that is a function of slip speed. The angular velocities of the axles determine
the slip speed.

ϖ=ω1−ω2

**Input Torque Coupling**

To calculate the clutch torque, the input torque coupling model uses torque
data that is a function of input torque.

The Open Differential block assumes rigid coupling between the
crown gear and axles. These constraint equations apply.

ηTi1= ηTi2=N2Ti

ωd=N2(ω1+ω2)
