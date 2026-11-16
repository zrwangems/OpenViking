---
type: simulink-block
title: 'Split Torsional Compliance'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Couplings'
documentation_page: 'splittorsionalcompliance'
documentation_source_path: 'ref/splittorsionalcompliance.html'
language: en
---

# Split Torsional Compliance

## Ports

### Input

### **RSpd** — Input shaft speed `scalar`

Input shaft rotational velocity,
*ωin*, in rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **C1Spd** — First output shaft speed `scalar`

First output shaft rotational velocity,
*ω1out*, in
rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **C2Spd** — Second output shaft speed `scalar`

Second output shaft rotational velocity,
*ω2out*, in
rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **CSpd** — Input speed `scalar`

Output shaft rotational velocity,
*ωout*, in rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **R1Spd** — First input shaft speed `scalar`

First input shaft rotational velocity,
*ω1in*, in rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **R2Spd** — Second input shaft speed `scalar`

Second input shaft rotational velocity,
*ω2in*, in rad/s.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **R** — Input shaft angular velocity and torque two-way connector port

Input shaft angular velocity,
*ωin*, in rad/s and torque,
*Tin*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **R1** — First input shaft angular velocity and torque two-way connector port

First input shaft angular velocity,
*ω1in*, in rad/s and
torque, *T1in*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`

### **R2** — Second input shaft angular velocity and torque two-way connector port

Second input shaft angular velocity,
*ω2in*, in rad/s and
torque, *T2in*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`
### Output

### **Info** — Bus signal bus

If you set **Coupling Configuration** to
`Shaft split`, the Info bus contains these
signals.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | Input shaft torque | *Tin* | N·m |
| `C1` | | First output shaft torque | *T1out* | N·m |
| `C2` | | Second output shaft torque | *T2out* | N·m |
| `Damp` | `C1` | First output shaft damping torque | *b1**ω1out* | N·m |
| `C2` | Second output shaft damping torque | *b2**ω2out* | N·m |
| `Spring` | `C1` | First output shaft spring torque | *k1**θ1* | N·m |
| `C2` | Second output shaft spring torque | *k2**θ2* | N·m |
| Spd | `R` | | Input shaft angular velocity | *ωin* | rad/s |
| `C1` | | First output shaft angular velocity | *ω1out* | rad/s |
| `C2` | | Second output shaft angular velocity | *ω2out* | rad/s |
| `deltadot1` | | Difference in input and first output shaft angular velocity | θ˙1 | rad/s |
| `deltadot2` | | Difference in input and second output shaft angular velocity | θ˙2 | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | Mechanical power from input shaft | *PTR* | W |
| `PwrC1` | Mechanical power from first output shaft | *PTC1* | W |
| `PwrC2` | Mechanical power from second output shaft | *PTC2* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Mechanical damping loss | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal torsional energy | *Ps* | W |

If you set **Coupling Configuration** to
`Shaft merge`, the Info bus contains these
signals.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| Trq | `C` | | Output shaft torque | *Tout* | N·m |
| `R1` | | First input shaft torque | *T1in* | N·m |
| `R2` | | Second input shaft torque | *T2in* | N·m |
| `Damp` | `R1` | First input shaft damping torque | *b1**ω1in* | N·m |
| `R2` | Second in shaft damping torque | *b2**ω2in* | N·m |
| `Spring` | `R1` | First input shaft spring torque | *k1**θ1* | N·m |
| `R2` | Second in shaft spring torque | *k2**θ2* | N·m |
| Spd | `C` | | Output shaft angular velocity | *ωout* | rad/s |
| `R1` | | First input shaft angular velocity | *ω1in* | rad/s |
| `R2` | | Second input shaft angular velocity | *ω2in* | rad/s |
| `deltadot1` | | Difference in first input and output shaft angular velocity | θ˙1 | rad/s |
| `deltadot2` | | Difference in second input and output shaft angular velocity | θ˙2 | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrC` | Mechanical power from output shaft | *PTC* | W |
| `PwrR1` | Mechanical power from first input shaft | *PTR1* | W |
| `PwrR2` | Mechanical power from second input shaft | *PTR2* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | Mechanical damping loss | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | Rate change of stored internal torsional energy | *Ps* | W |

#### Dependencies

To enable this port, select **Output Info bus**.

### **RTrq** — Input shaft torque `scalar`

Input shaft torque, *Tin*, in
N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **C1Trq** — First output shaft torque `scalar`

First output shaft torque,
*T1out*, in N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **C2Trq** — Second output shaft torque `scalar`

Second output shaft torque,
*T2out*, in N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft split`

### **CTrq** — Output shaft torque `scalar`

Output shaft torque, *Tout*,
in N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **R1Trq** — First input shaft torque `scalar`

First input shaft torque,
*T1in*, in N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **R2Trq** — Second input shaft torque `scalar`

Second input shaft torque,
*T2in*, in N·m.

#### Dependencies

To enable this port, set both of these parameters:

- **Port Configuration** to `Simulink`
- **Coupling Configuration** to `Shaft merge`

### **C1** — First output shaft angular velocity and torque two-way connector port

First output shaft angular velocity,
*ω1out*, in rad/s and
torque, *T1out*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **C2** — Second output shaft angular velocity and torque two-way connector port

Second output shaft angular velocity,
*ω2out*, in rad/s and
torque, *T2out*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **C** — Output shaft angular velocity and torque two-way connector port

Output shaft angular velocity,
*ωout*, in rad/s and torque,
*Tout*, in N·m.

#### Dependencies

To enable this port, select:

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`

## Parameters

#### Block Options

### **Port Configuration** — Specify configuration `Simulink` (default) | `Two-way connection`

Specify the port configuration.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Simulink` (default) | `Two-way connection` |
| **Data Types:** | `character vector` |

### **Coupling Configuration** — Specify configuration `Shaft split` (default) | `Shaft merge`

Specify the coupling type.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CplrMode` |
| **Values:** | `Shaft split` (default) | `Shaft merge` |
| **Data Types:** | `character vector` |

### **Output Info bus** — Selection `off` (default) | `on`

Select to create the `Info` output port.

#### Coupling 1

### **Torsional stiffness, k1** — Stiffness `5e4` (default) | scalar greater than or equal to 0

Rotational inertia, *k1*, in
N·m/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `k1` |
| **Values:** | `5e4` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Torsional damping, b1** — Damping `1e2` (default) | scalar greater than or equal to 0

Torsional damping, *b1*, in N·m·
s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b1` |
| **Values:** | `1e2` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Damping cutoff frequency, omega1\_c** — Frequency `3000` (default) | positive scalar

Damping cutoff frequency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega1_c` |
| **Values:** | `3000` (default) | positive scalar |
| **Data Types:** | `double` |

#### Coupling 2

### **Torsional stiffness, k2** — Stiffness `5e4` (default) | scalar greater than or equal to 0

Rotational inertia, *k2*, in
N·m/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `k2` |
| **Values:** | `5e4` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Torsional damping, b2** — Damping `1e2` (default) | `scalar`

Torsional damping, *b2*, in N·m·
s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b2` |
| **Values:** | `1e2` (default) | scalar greater than or equal to 0 |
| **Data Types:** | `double` |

### **Damping cutoff frequency, omega2\_c** — Frequency `3000` (default) | positive scalar

Damping cutoff frequency, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega2_c` |
| **Values:** | `3000` (default) | positive scalar |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Split torsional coupler

The Split Torsional Compliance block implements parallel spring-damper
coupling between shafts. You can specify the type of coupling by selecting one of the
**Coupling Configuration** parameters:

- `Shaft split` — Single input shaft coupled to two
  output shafts
- `Shaft merge` — Two input shafts coupled to a
  single output shaft

In fuel economy and emissions studies, you can use the Split Torsional
Compliance block to model mechanical rotational compliance between common
driveline elements such as motors, planetary gears, and clutches. For example, use the
`Shaft split` configuration to couple a motor and two
planetary gear sets. Use the `Shaft merge` configuration to
couple a dual clutch transmission to an output shaft.

### Shaft Split

For the `Shaft split` configuration, the block implements
this schematic and equations.

Schematic diagram of shaft split rotational compliance

Tin=−(ωin−ω1out)b1−(ωin−ω2out)b2−θ1k1−θ2k2T1out=(ωin−ω1out)b1+θ1k1T2out=(ωin−ω2out)b2+θ2k2θ˙1=(ωin−ω1out)θ˙2=(ωin−ω2out)

To account for frequency-dependent damping, both damping terms
incorporate a low-pass filter.

The equations use these variables.

|  |  |
| --- | --- |
| *Tin* | Resulting applied input reaction torque |
| *ωin* | Input shaft rotational velocity |
| *T1out* | Resulting applied torque to first output shaft |
| *ω1out* | First output shaft rotational velocity |
| *T2out* | Resulting applied torque to second output shaft |
| *ω2out* | Second output shaft rotational velocity |
| *θ1*, *θ2* | First, second shaft rotation, respectively |
| *b1*, *b2* | First, second shaft viscous damping, respectively |
| *k1*, *k2* | First, second shaft torsional stiffness, respectively |

### Shaft Merge

For the `Shaft merge` configuration, the block implements
this schematic and equations.

Schematic diagram of shaft merge rotational compliance

Tout=(−ωout+ω1in)b1+(−ωout+ω2in)b2+θ1k1+θ2k2T1out=(ωout−ω1in)b1−θ1k1T2out=(ωout−ω2in)b2−θ2k2θ˙1=(ω1in−ωout)θ˙2=(ω2in−ωout)

To account for frequency-dependent damping, both damping terms
incorporate a low-pass filter.

The equations use these variables.

|  |  |
| --- | --- |
| *Tout* | Resulting applied output torque |
| *ωout* | Output shaft rotational velocity |
| *T1in* | Resulting reaction torque to first input shaft |
| *ω1in* | First input shaft rotational velocity |
| *T2in* | Resulting reaction torque to second input shaft |
| *ω2in* | Second input shaft rotational velocity |
| *θ1*, *θ2* | First, second shaft rotation, respectively |
| *b1*, *b2* | First, second shaft viscous damping, respectively |
| *k1*, *k2* | First, second shaft torsional stiffness, respectively |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrR` | For the `Shaft split` configuration, mechanical power from input shaft | *PTR* | PTR= −TRωR |
| `PwrC1` | For the `Shaft split` configuration, mechanical power from first output shaft | *PTC1* | PTC1= −TC1ωC1 |
| `PwrC2` | For the `Shaft split` configuration, mechanical power from second output shaft | *PTC2* | PTC2= −TC2ωC2 |
| `PwrC` | For the `Shaft merge` configuration, mechanical power from output shaft | *PTC* | PTC= TCωC |
| `PwrR1` | For the `Shaft merge` configuration, mechanical power from first input shaft | *PTR1* | PTR1= TR1ωR1 |
| `PwrR2` | For the `Shaft merge` configuration, mechanical power from second input shaft | *PTR2* | PTR2= TR2ωR2 |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrDampLoss` | Mechanical damping loss | *Pd* | Pd=−(b1|θ˙1|2+b2|θ˙2|2) |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredShft` | Rate change in spring energy | *Ps* | Ps=(k1θ1θ˙1+k2θ2θ˙2) |

The equations use these variables.

|  |  |
| --- | --- |
| *TR* | Shaft R torque |
| *TC* | Shaft C torque |
| *ωR* | Shaft R angular velocity |
| *ωC* | Shaft C angular velocity |
| *θ* | Coupled shaft rotation |
| *k* | Shaft torsional stiffness |
| *b* | Rotational viscous damping |
| *Pt* | Total mechanical power |
| *Pd* | Power loss due to damping |
| *Ps* | Rate change of stored spring energy |
