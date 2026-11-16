---
type: simulink-block
title: 'Active Differential'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Final Drive Unit'
documentation_page: 'activedifferential'
documentation_source_path: 'ref/activedifferential.html'
language: en
---

# Active Differential

## Ports

### Inputs

### **Prs1** — Clutch 1 pressure `scalar`

Clutch 1 pressure, *P1*, in
Pa.

### **Prs2** — Clutch 2 pressure `scalar`

Clutch 2 pressure, *P2*, in
Pa.

### **DriveshftTrq** — Driveshaft torque `scalar`

Applied input torque, *Td*,
typically from the engine driveshaft, in N·m.

### **Axl1Trq** — Torque `scalar`

Axle 1 torque, *T1*, in
N·m.

### **Axl2Trq** — Torque `scalar`

Axle 2 torque, *T2*, in
N·m.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | Description | Units |
| --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | Drive shaft torque | N·m |
| `DriveshftSpd` | Drive shaft angular velocity | rad/s |
| `Axl1` | `Axl1Trq` | Axle 1 torque | N·m |
| `Axl1Spd` | Axle 1 angular velocity | rad/s |
| `Axl2` | `Axl2Trq` | Axle 2 torque | N·m |
| `Axl2Spd` | Axle 2 angular velocity | rad/s |
| `Cplng` | `CplngTrq1` | Clutch 1 coupling torque | N·m |
| `CplngTrq2` | Clutch 2 coupling torque | N·m |
| `CplngSlipSpd1` | Clutch 1 slip speed | rad/s |
| `CplngSlipSpd2` | Clutch 2 slip speed | rad/s |
| `CplngPrs1` | Clutch 1 input pressure | Pa |
| `CplngPrs2` | Clutch 2 input pressure | Pa |

### **DriveshftSpd** — Angular velocity `scalar`

Driveshaft angular velocity,
*ωd*, in rad/s.

### **Axl1Spd** — Angular velocity `scalar`

Axle 1 angular velocity, *ω1*,
in rad/s.

### **Axl2Spd** — Angular velocity `scalar`

Axle 2 angular velocity, *ω2*,
in rad/s.

## Parameters

#### Active Differential

### **Active differential type** — Differential `Spur gears, superposition clutches` (default) | `Double planetary gears, stationary clutches`

Specify the type of active differential.

| Setting | Block Implementation |
| --- | --- |
| `Spur gears, superposition clutches` | Clutches are in superposition through a three-gang gear system and a differential case |
| `Double planetary gears, stationary clutches` | Clutches are fixed to the carrier and axles through double planetary gear sets |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `diffType` |
| **Values:** | `Spur gears, superposition clutches` (default) | `Double planetary gears, stationary clutches` |
| **Data Types:** | `character vector` |

### **Clutch 1 to differential case gear ratio, Ns1** — Clutch 1-spur gear ratio `.875` (default) | `scalar`

Clutch 1-to-carrier spur gear ratio,
*Ns1*, dimensionless.

#### Dependencies

To enable the spur gear parameters, select `Spur
gears, superposition clutches` for the **Active differential
type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ns1` |
| **Values:** | `.875` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch 2 to differential case gear ratio, Ns2** — Clutch 2-spur gear ratio `1.125` (default) | `scalar`

Clutch 2-to-carrier spur gear ratio,
*Ns2*, dimensionless.

#### Dependencies

To enable the spur gear parameters, select `Spur
gears, superposition clutches` for the **Active differential
type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ns2` |
| **Values:** | `1.125` (default) | `scalar` |
| **Data Types:** | `double` |

### **Three-gang gear inertia, Jgc** — Rotational inertia `.003` (default) | `scalar`

Three-gang gear rotational inertia,
*Jgc*, in kg·m^2.

#### Dependencies

To enable the spur gear parameters, select `Spur
gears, superposition clutches` for the **Active differential
type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jgc` |
| **Values:** | `.003` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 planetary carrier to axle gear ratio, Np1** — Planetary 1 carrier gear ratio `1.125` (default) | `scalar`

Planetary 1 carrier-to-axle gear ratio,
*Np1*, dimensionless.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Np1` |
| **Values:** | `1.125` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 sun gear inertia, Js1** — Planetary 1 sun gear inertia `.001` (default) | `scalar`

Planetary 1 sun gear inertia,
*Js1*, in kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Js1` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 carrier inertia, Jc1** — Planetary 1 carrier inertia `.001` (default) | `scalar`

Planetary 1 carrier inertia,
*Jc1*, in kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jc1` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 1 ring inertia, Jr1** — Planetary 1 ring gear inertia `.002` (default) | `scalar`

Planetary 1 ring gear inertia,
*Jr1*, kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jr1` |
| **Values:** | `.002` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 planetary carrier to axle gear ratio, Np2** — Planetary 2 carrier gear ratio `1.125` (default) | `scalar`

Planetary 2 carrier-to-axle gear ratio,
*Np2*, dimensionless.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Np2` |
| **Values:** | `1.125` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 sun gear inertia, Js2** — Planetary 2 sun gear inertia `.001` (default) | `scalar`

Planetary 2 sun gear inertia,
*Js2*, in kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Js2` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 carrier inertia, Jc2** — Planetary 2 carrier inertia `.001` (default) | `scalar`

Planetary 2 carrier inertia,
*Jc2*, in kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jc2` |
| **Values:** | `.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Axle 2 ring inertia, Jr2** — Planetary 2 ring gear inertia `.002` (default) | `scalar`

Planetary 2 ring gear inertia,
*Jr2*, in kg·m^2.

#### Dependencies

To enable the planetary gear parameters, select
`Double planetary gears, stationary clutches` for the
**Active differential type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Jr2` |
| **Values:** | `.002` (default) | `scalar` |
| **Data Types:** | `double` |

#### Open Differential

### **Crown wheel (ring gear) located** — Specify crown wheel connection `To the left of center-line` (default) | `To the right of center-line`

Specify the crown wheel connection to the drive shaft.

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

Carrier-to-drive shaft gear ratio, *N*.

Specify the crown wheel connection to the drive shaft.

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
include the drive shaft inertia.

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

#### Slip Coupling

### **Coupling type** — Torque coupling `Ideal pre-loaded clutch` (default) | `Slip speed dependent torque data` | `Input torque dependent torque data`

Specify the type of torque coupling.

| Setting | Block Implementation |
| --- | --- |
| `Pre-loaded ideal clutch` | Torque modeled as a wet clutch with a constant velocity |
| `Slip speed dependent torque data` | Torque determined from a lookup table that is a function of slip-speed and clutch pressure |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `couplingType` |
| **Values:** | `Ideal pre-loaded clutch` (default) | `Slip speed dependent torque data` | `Input torque dependent torque data` |
| **Data Types:** | `character vector` |

### **Effective applied pressure area** — Pressure area `0.01` (default) | `scalar`

Effective applied pressure area, in N/m^2.

#### Dependencies

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Aeff` |
| **Values:** | `0.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Number of disks, Ndisks** — Torque coupling `4` (default) | `scalar`

Number of disks.

#### Dependencies

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

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

### **Effective radius, Reff** — Radius `.20` (default) | `scalar`

The effective radius, Reff, used with the applied clutch friction force to determine
the friction force. The effective radius is defined as:

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

The equation uses these variables.

|  |  |
| --- | --- |
| Ro | Annular disk outer radius |
| Ri | Annular disk inner radius |

#### Dependencies

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

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

### **Nominal preload force, Fc** — Force `500` (default) | `scalar`

Nominal preload force, in N.

#### Dependencies

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

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

### **Friction coefficient vector, mu** — Friction `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125 .10125]` (default) | `vector`

Friction coefficient vector.

#### Dependencies

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu` |
| **Values:** | `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125 .10125]` (default) | `vector` |
| **Data Types:** | `double` |

### **Slip speed vector, dw** — Angular velocity `[0 10 20 40 60 80 100 500]` (default) | `vector`

Slip speed vector, in rad/s.

To enable the clutch parameters, select `Ideal pre-loaded clutch` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dw` |
| **Values:** | `[0 10 20 40 60 80 100 500]` (default) | `vector` |
| **Data Types:** | `double` |

### **Torque - slip speed matrix, TdPdw** — Clutch torque `[-1000,-500,-90,-50,-5,0,5,50,90,500,1000].*ones(11)` (default) | `matrix`

Torque matrix, *Tc*, in
N·m.

#### Dependencies

To enable the slip speed parameters, select `Slip speed dependent torque data` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TdPdw` |
| **Values:** | `[-1000,-500,-90,-50,-5,0,5,50,90,500,1000].*ones(11)` (default) | `matrix` |
| **Data Types:** | `double` |

### **Clutch pressure vector, pT** — Clutch pressure breakpoints `[0 1e3 5e3 7e3 1e4 2e4 5e4 1e5 5e5 1e6 5e6]` (default) | `vector`

Clutch pressure breakpoints vector,
*P1,2*, in Pa.

#### Dependencies

To enable the slip speed parameters, select `Slip speed dependent torque data` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `pT` |
| **Values:** | `[0 1e3 5e3 7e3 1e4 2e4 5e4 1e5 5e5 1e6 5e6]` (default) | `vector` |
| **Data Types:** | `double` |

### **Slip speed vector, dwT** — Slip speed breakpoints `[-500 -200, -175, -100, - 50, 0, 50, 100, 175, 200, 500]` (default) | `vector`

Slip speed breakpoints vector, *ω*, in rad/s.

#### Dependencies

To enable the slip speed parameters, select `Slip speed dependent torque data` for the **Coupling type** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dwT` |
| **Values:** | `[-500 -200, -175, -100, - 50, 0, 50, 100, 175, 200, 500]` (default) | `vector` |
| **Data Types:** | `double` |

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

Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Spur or planetary active differential gear

The Active Differential block implements an active differential to
account for the power transfer from the transmission to the axles. The block models the
active differential as an open differential coupled to either a spur or planetary
differential gear set. The block uses external pressure signals to regulate the clutch
pressure to either speed up or slow down each axle rotation.

Use the block in hardware-in-the-loop (HIL) and optimization workflows to dynamically
couple the driveshaft to the wheel axles when you want to direct the transmission torque
to a specific axle. For detailed front wheel driving studies, use the block to couple
the driveshaft to universal joints. The block is suitable to use in system-level
closed-loop control studies, for example, yaw stability and torque vectoring. All the
parameters are tunable.

To specify the active differential, open the **Active Differential**
parameters and specify **Active differential type**.

| Setting | Block Implementation |
| --- | --- |
| `Spur gears, superposition clutches` | Clutches are in superposition through a three-gang gear system and a differential case |
| `Double planetary gears, stationary clutches` | Clutches are fixed to the carrier and axles through double planetary gear sets |

Use the **Open Differential** parameter **Crown wheel (ring
gear) located** to specify the open differential location, either to the
left or right of the center-line.

Depending on the available data, to specify the method to couple the different torques
applied to the axles, use the **Slip Coupling** parameter
**Coupling type**.

| Setting | Block Implementation |
| --- | --- |
| `Pre-loaded ideal clutch` | Torque modeled as a dry clutch with constant friction coefficients |
| `Slip speed dependent torque data` | Torque determined from a lookup table that is a function of slip-speed and clutch pressure |

The Active Differential block does not include a controller or external
clutch actuator dynamics. Use this information to control the input clutch pressure. The
info bus contains the slip speeds at clutch 1,
*Δωcl1*, and clutch 2,
*Δωcl2*.

| Input Axle Torque | *Δωcl1* | *Δωcl2* | Input Clutch Pressure |
| --- | --- | --- | --- |
| Positive axle 1 torque | `> 0` | N/A | Increase clutch 1 pressure |
| Positive axle 1 torque | `< 0` | N/A | Disengage clutch 1 and 2 |
| Positive axle 2 torque | N/A | `> 0` | Increase clutch 1 pressure |
| Positive axle 2 torque | N/A | `< 0` | Disengage clutch 1 and 2 |

### Differentials

The Active Differential block implements these equations to
represent the mechanical dynamic response for the superposition and stationary
clutch configurations. To determine the gear ratios, the block uses the clutch speed
and the number of teeth for each gear pair. The allowable wheel speed difference
(AWSD) limits the wheel speed difference for positive torque.

| Mechanical Dynamic Response | Equations | |
| --- | --- | --- |
| Superposition Clutches and Spur Gearing | Stationary Clutches and Planetary Gearing |
| Crown gear | ω˙d(Jd+Jgs)=Td−ωdbd−Ti | ω˙d( Jd+Js1+Js2)=Td−ωdbd−Ti |
| Axle 1 | ω˙1J1=ηT1-ω1b1-Ti1 | ω˙1(J1+Jr1)=T1−ω1b1−Ti1 |
| Axle 2 | ω˙2J2=ηT2-ω2b2-Ti2 | ω˙2(Jaxle2+Jr1)=T2−ω2b2−Ti2 |
| Gear ratios | ωcl1ωd=Ns1=z1z6z4z3ωcl2ωd=Ns2=z1z5z4z2 | ωcl1ωd=Np1=z1z6z4z3ωcl2ωd=Np2=z1z5z4z2 |
| Rigid Coupling Constraints | T1= NTi2−Ns22Tcl2+Ns12Tcl1T2= NTi2+(1−Ns22)Tcl2−(1−Ns12)Tcl1ωd==N2(ω1+ω2) | T1= NTi2−Np2(Np2−1)2Tcl2+(2−Np1)(Np1−1)2Tcl1T2= NTi2+(2−Np2)(Np2−1)2Tcl2−Np1(Np1−1)2Tcl1ωd==N2(ω1+ω2) |
| Allowable wheel speed difference (AWSD) | Δω¯max=(Ns2−Ns1)⋅100% | Δω¯max=(Np1,2−1)⋅100% |

**Superposition Clutches and Spur Gearing**

These superposition clutch illustrations show the clutch configuration and
schematic for torque transfer to the left wheel.

Detailed illustration of torque transfer to the left wheel

Schematic of clutch torque transfer to the left wheel

**Stationary Clutches and Planetary Gearing**

The illustrations show the stationary clutch configuration and schematic.

Detailed illustration of a stationary clutch

Schematic of stationary clutch

### Slip Coupling

For both the ideal clutch and slip-speed configurations, the slip coupling is a
function of the slip-speed and clutch pressure. The slip-speed depends on the slip
velocity at each of the clutch interfaces.

ϖ=[Δωc1,Δωc2]

**Ideal Clutch**

The ideal clutch coupling model uses the axle slip speed, clutch pressure, and
friction to calculate the clutch torque. The friction coefficient is a function
of the slip speed.

TC=FTNdμ(|ω¯|)Refftanh(4ω¯)

To calculate the total clutch force, the block uses the effective radius,
clutch pressure, and clutch preload force.

FT= FC+P1,2Aeff, FT≥0

The disc radii determine the effective clutch radius over which the clutch
force acts.

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

**Slip-Speed**

To calculate the clutch torque, the slip speed coupling model uses torque data
that is a function of slip speed and clutch pressure. The angular velocities of
the axles determine the slip speed.

TC=TC(ϖ, P1,2)

The equations use these variables.

|  |  |
| --- | --- |
| *Aeff* | Effective clutch pressure area |
| *bd* | Crown gear linear viscous damping |
| *b1*, *b2* | Axle 1 and 2 linear viscous damping, respectively |
| *Fc*, *FT* | Clutch preload force and total force, respectively |
| *Jd* | Carrier rotational inertia |
| *Jgc* | Three-gang gear rotational inertia |
| *Jc1*, *Jc2* | Planetary carrier 1 and 2 rotational inertia, respectively |
| *Jr1*, *Jr2* | Planetary ring gear 1 and 2 rotational inertia, respectively |
| *Js1*, *Js2* | Planetary sun gear 1 and 2 rotational inertia, respectively |
| *J1*, *J2* | Axle 1 and 2 rotational inertia, respectively |
| *N* | Carrier-to-drive shaft gear ratio |
| *Nd* | Number of disks |
| *Ns1*, *Ns2* | Clutch 1 and 2 carrier-to-spur gear ratio, respectively |
| *Np1*, *Np2* | Planetary 1 and 2 carrier-to-axle gear ratio, respectively |
| *P1*, *P2* | Clutch 1 and 2 pressure, respectively |
| *Reff* | Effective clutch radius |
| *Ri*, *Ro* | Annular disk inner and outer radius, respectively |
| *Tc* | Clutch torque |
| *Tcl1*, *Tcl2* | Clutch 1 and 2 coupling torque, respectively |
| *Td* | Driveshaft torque |
| *T1*, *T2* | Axle 1 and 2 torque, respectively |
| *Ti* | Axle internal resistance torque |
| *Ti1*, *Ti2* | Axle 1 and 2 internal resistance torque |
| *ωd* | Driveshaft angular velocity |
| *ϖ* | Slip speed |
| *ω1*, *ω2* | Axle 1 and 2 angular velocity, respectively |
| *Δωcl1*, *Δωcl2* | Clutch 1 and 2 slip speed at interface, respectively |
| *ωcl1*, *ωcl2* | Clutch 1 and 2 angular velocity, respectively |
| *μ* | Clutch coefficient of friction |
| *zi* | Number of teeth on gear *i* |
