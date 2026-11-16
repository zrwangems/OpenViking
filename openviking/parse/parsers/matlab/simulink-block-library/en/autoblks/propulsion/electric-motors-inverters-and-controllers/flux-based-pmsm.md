---
type: simulink-block
title: 'Flux-Based PMSM'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors, Inverters, and Controllers'
documentation_page: 'fluxbasedpmsm'
documentation_source_path: 'ref/fluxbasedpmsm.html'
language: en
---

# Flux-Based PMSM

## Ports

### Input

### **LdTrq** — Rotor shaft torque `scalar`

Rotor shaft input torque,
*Tm*, in N·m.

#### Dependencies

To create this port, select `Torque` for
the **Port Configuration** parameter.

### **Spd** — Rotor shaft speed `scalar`

Angular velocity of the rotor, ωm, in
rad/s.

#### Dependencies

To create this port, select `Speed` for
the **Port Configuration** parameter.

### **PhaseVolt** — Stator terminal voltages `1`-by-`3` array

Stator terminal voltages,
*Va*,
*Vb*, and
*Vc*, in V.

#### Dependencies

To create this port, select `Speed` or
`Torque` for the **Port
Configuration** parameter.
### Output

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | Stator phase current A | *ia* | A |
| `IbStator` | | | Stator phase current B | *ib* | A |
| `IcStator` | | | Stator phase current C | *ic* | A |
| `IdSync` | | | Direct axis current | *id* | A |
| `IqSync` | | | Quadrature axis current | *iq* | A |
| `VdSync` | | | Direct axis voltage | *vd* | V |
| `VqSync` | | | Quadrature axis voltage | *vq* | V |
| `MtrSpd` | | | Angular mechanical velocity of the rotor | *ωm* | rad/s |
| `MtrPos` | | | Rotor mechanical angular position | *θm* | rad |
| `MtrTrq` | | | Electromagnetic torque | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | Mechanical power | *Pmot* | W |
| `PwrBus` | Electrical power | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | Resistive power loss | *Pelec* | W |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | Stored motor power | *Pstr* | W |

### **PhaseCurr** — Phase a, b, c current `1`-by-`3` array

Phase a, b, c current, *ia*,
*ib*, and
*ic*, in A.

### **MtrTrq** — Motor torque `scalar`

Motor torque, *Tmtr*, in
N·m.

#### Dependencies

To create this port, select `Speed` for
the **Port configuration** parameter.

### **MtrSpd** — Motor speed `scalar`

Angular speed of the motor,
*ωmtr*, in rad/s.

#### Dependencies

To create this port, select `Torque` for
the **Port configuration** parameter.

## Parameters

#### Block Options

### **Simulation type** — Select simulation type `Continuous` (default) | `Discrete`

By default, the block uses a continuous sample time
during simulation. If you want to generate code for single-precision targets, considering
setting the parameter to `Discrete`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sim_type` |
| **Values:** | `Continuous` (default) | `Discrete` |
| **Data Types:** | `character vector` |

#### Dependencies

Setting **Simulation Type** to `Discrete`
creates the **Sample Time, Ts** parameter.

### **Sample time, Ts** — Sample time for discrete integration `0.001` (default) | `scalar`

Integration sample time for discrete simulation, in
s.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

Setting **Simulation Type** to
`Discrete` creates the **Sample Time,
Ts** parameter.

### **Port Configuration** — Select port configuration `Torque` (default) | `Speed`

This table summarizes the port configurations.

| Port Configuration | Creates Input Port | Creates Output Port |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **Values:** | `Torque` (default) | `Speed` |
| **Data Types:** | `character vector` |

### **Enable memory optimized 2D LUT** — Selection `off` (default) | `on`

Enable generation of optimized lookup tables, suitable code generation
targets that limit memory.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `enable_hdl` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Vector of d-axis flux, flux\_d** — Flux breakpoints `1`-by-`M` vector

*d*-axis flux,
*Ψd*, breakpoints, in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `flux_d` |
| **Values:** | `1`-by-`M` vector |
| **Data Types:** | `double` |

### **Resample storage size for flux\_d, n1** — Flux bit size `2` (default) | `4` | `8` | `16` | `32` | `64` | `128` | `256`

Flux breakpoint storage size, *n1*, dimensionless. The
block resamples the **Corresponding d-axis current, id**
and **Corresponding q-axis current, iq** data based on the
storage size.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `n1` |
| **Values:** | `2` (default) | `4` | `8` | `16` | `32` | `64` | `128` | `256` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D
LUT**.

### **Vector of q-axis flux, flux\_q** — Flux breakpoints `1`-by-`N` vector

*q*-axis flux,
*Ψq*, breakpoints, in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `flux_q` |
| **Values:** | `1`-by-`N` vector |
| **Data Types:** | `double` |

### **Resample storage size for flux\_q, n2** — Flux bit size `2` (default) | `4` | `8` | `16` | `32` | `64` | `128` | `256`

Flux breakpoint storage size, *n2*, dimensionless. The
block resamples the **Corresponding d-axis current, id**
and **Corresponding q-axis current, iq** data based on the
storage size.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `n2` |
| **Values:** | `2` (default) | `4` | `8` | `16` | `32` | `64` | `128` | `256` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D
LUT**.

### **Corresponding d-axis current, id** — 2D lookup table `M`-by-`N` array

Array of values for *d*-axis current,
*id*, as a function of
`M`
*d*-fluxes, *Ψd*,
and `N`
*q*-fluxes, *Ψq*,
in A. Each value specifies the current for a specific combination of
*d*- and *q*-axis flux. The array
size must match the dimensions defined by the flux vectors.

If you set **Enable memory optimized 2D LUT**, the block
converts the data to single precision.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `id` |
| **Values:** | `M`-by-`N` array |
| **Data Types:** | `double` |

### **Corresponding q-axis current, iq** — 2D lookup table `M`-by-`N` array

Array of values for *q*-axis current,
*id*, as a function of
`M`
*d*-fluxes, *Ψd*,
and `N`
*q*-fluxes, *Ψq*,
in A. Each value specifies the current for a specific combination of
*d*- and *q*-axis flux. The array
size must match the dimensions defined by the flux vectors.

If you set **Enable memory optimized 2D LUT**, the block
converts the data to single precision.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `iq` |
| **Values:** | `M`-by-`N` array |
| **Data Types:** | `double` |

### **flux\_d max endpoint, u1max** — Flux breakpoint `0.22457` (default) | `scalar`

Flux breakpoint maximum extrapolation endpoint, *u1max*,
in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `u1max` |
| **Values:** | `0.22457` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **flux\_d min endpoint, u1min** — Flux breakpoint `-0.22607` (default) | `scalar`

Flux breakpoint minimum extrapolation endpoint, *u1min*,
in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `u1min` |
| **Values:** | `-0.22607` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **flux\_q max endpoint, u2max** — Flux breakpoint `0.42959` (default) | `scalar`

Flux breakpoint maximum extrapolation endpoint, *u2max*,
in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `u2max` |
| **Values:** | `0.42959` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **flux\_q min endpoint, u2min** — Flux breakpoint `-0.4296` (default) | `scalar`

Flux breakpoint minimum extrapolation endpoint, *u2min*,
in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `u2min` |
| **Values:** | `-0.4296` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select **Enable memory optimized 2D LUT** and
**Specify Extrapolation**.

### **Stator phase resistance, Rs** — Resistance `0.02` (default) | `scalar`

Stator phase resistance, *Rs*, in
ohm.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **Values:** | `0.02` (default) | `scalar` |
| **Data Types:** | `double` |

### **Number of pole pairs, P** — Pole pairs `4` (default) | `scalar`

Motor pole pairs, *P*.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `P` |
| **Values:** | `4` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial flux, fluxdq0** — Flux `[0 0]` (default) | `vector`

Initial *d*- and *q*-axis flux,
*Ψq0* and
*Ψd0*, in Wb.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `fluxdq0` |
| **Values:** | `[0 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Initial mechanical position, theta\_init** — Angle `0` (default) | `scalar`

Initial rotor angular position,
*θm0*, in rad.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `theta_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial mechanical speed, omega\_init** — Speed `0` (default) | `scalar`

Initial angular velocity of the rotor,
*ωm0*, in rad/s.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_init` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select the `Torque`
configuration parameter.

### **Physical inertia, viscous damping, and static friction, mechanical** — Inertia, damping, friction `[0.0027, 4.924e-4, 0]` (default) | `vector`

Mechanical properties of the rotor:

- Inertia, *J*, in kgm^2
- Viscous damping, *F*, in N·m/(rad/s)
- Static friction, *Tf*,
  in N·m

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `mechanical` |
| **Values:** | `[0.0027, 4.924e-4, 0]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select the `Torque`
configuration parameter.

## Libraries

Powertrain Blockset / Propulsion / Electric Motors and Inverters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Flux-based permanent magnet synchronous motor

The Flux-Based PMSM block implements a flux-based three-phase permanent
magnet synchronous motor (PMSM) with a tabular-based electromotive force. The block uses
the three-phase input voltages to regulate the individual phase currents, allowing
control of the motor torque or speed.

Flux-based motor models take into account magnetic saturation and iron losses. To
calculate the magnetic saturation and iron loss, the Flux-Based PMSM
block uses the inverse of the flux linkages. To obtain the block parameters, you can use
finite-element analysis (FEA) or measure phase voltages using a dynamometer.

By default, the block sets the **Simulation
Type** parameter to `Continuous` to use a continuous
sample time during simulation. If you want to generate code for fixed-step double- and
single-precision targets, considering setting the parameter to
`Discrete`. Then specify a **Sample Time, Ts**
parameter.

To enable power loss calculations suitable for code generation targets that limit
memory, select **Enable memory optimized 2D LUT**.

### Three-Phase Sinusoidal Model Electrical System

The block implements equations that are expressed in a stationary rotor reference
(dq) frame. The *d*-axis aligns with the
*a*-axis. All quantities in the rotor reference frame are
referred to the stator.

The block uses these equations.

| Calculation | Equation |
| --- | --- |
| *q*- and *d*-axis voltage | vd=dψddt+Rsid−ωeψqvq=dψqdt+Rsiq+ωeψd |
| *q*- and *d*-axis current | id=f(ψd,ψq)iq=g(ψd,ψq) |
| Electromechanical torque | Te=1.5P[ψdiq−ψqid] |

The equations use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor mechanical speed |
| *ωe* | Rotor electrical speed |
| *Θda* | dq stator electrical angle with respect to the rotor a-axis |
| *Rs*, *Rr* | Resistance of the stator and rotor windings, respectively |
| *iq*, *id* | *q*- and *d*-axis current, respectively |
| *vq*, *vd* | *q*- and *d*-axis voltage, respectively |
| *Ψq*, *Ψd* | *q*- and *d*-axis magnet flux, respectively |
| *P* | Number of pole pairs |
| *Te* | Electromagnetic torque |

### Transforms

To calculate the voltages and currents in balanced three-phase
(*a*, *b*) quantities, quadrature two-phase
(*α*, *β*) quantities, and rotating
(*d*, *q*) reference frames, the block uses
the Clarke and Park Transforms.

In the transform equations.

ωe=Pωmdθedt= ωe

| Transform | Description | Equations |
| --- | --- | --- |
| Clarke | Converts balanced three-phase quantities (*a*, *b*) into balanced two-phase quadrature quantities (*α*, *β*). | xα= 23xa− 13xb −13xcxβ= 32xb− 32xc |
| Park | Converts balanced two-phase orthogonal stationary quantities (*α*, *β*) into an orthogonal rotating reference frame (*d*, *q*). | xd= xαcosθe+ xβsinθexq= −xαsinθe+ xβcosθe |
| Inverse Clarke | Converts balanced two-phase quadrature quantities (*α*, *β*) into balanced three-phase quantities (*a*, *b*). | xa= xaxb= −12xα+ 32xβxc= −12xα− 32xβ |
| Inverse Park | Converts an orthogonal rotating reference frame (*d*, *q*) into balanced two-phase orthogonal stationary quantities (*α*, *β*). | xα= xdcosθe− xqsinθexβ= xdsinθe+ xqcosθe |

The transforms use these variables.

|  |  |
| --- | --- |
| *ωm* | Rotor mechanical speed |
| *P* | Motor pole pairs |
| *ωe* | Rotor electrical speed |
| *Θe* | Rotor electrical angle |
| *x* | Phase current or voltage |

### Mechanical System

The rotor angular velocity is given by:

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

The equations use these variables.

|  |  |
| --- | --- |
| *J* | Combined inertia of rotor and load |
| *F* | Combined viscous friction of rotor and load |
| *θm* | Rotor mechanical angular position |
| *Tm* | Rotor shaft torque |
| *Te* | Electromagnetic torque |
| *Tf* | Combined rotor and load friction torque |
| *ωm* | Rotor mechanical speed |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrMtr` | Mechanical power | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | Electrical power | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrElecLoss` | Resistive power loss | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | Mechanical power loss | *Pmech* | When **Port Configuration** is set to `Torque`:  Pmech= −(ωm2F+ |ωm|Tf)  When **Port Configuration** is set to `Speed`:  Pmech= 0 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrMtrStored` | Stored motor power | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

The equations use these variables.

|  |  |
| --- | --- |
| *Rs* | Stator resistance |
| *ia*,*ib*,*ic* | Stator phase a, b, and c current |
| *isq*,*isd* | Stator q- and d-axis currents |
| *van*, *vbn*, *vcn* | Stator phase a, b, and c voltage |
| *ωm* | Angular mechanical velocity of the rotor |
| *F* | Combined motor and load viscous damping |
| *Te* | Electromagnetic torque |
| *Tf* | Combined motor and load friction torque |

### Lookup Table Memory Optimization

The data for the **Corresponding d-axis current, id** and
**Corresponding q-axis current, iq** lookup tables are
functions of the *d*- and *q*-axis
flux.

To enable current calculations suitable for code generation targets that limit
memory, select **Enable memory optimized 2D LUT**. The block uses
linear interpolation to optimize the current lookup table values for code
generation. This table summarizes the optimization implementation.

| Use Case | | Implementation |
| --- | --- | --- |
| *d*- and *q*-axis flux aligns with the lookup table breakpoint values. | | Memory-optimized current is current lookup table value at intersection of flux values. |
| *d*- and *q*-axis flux does not align with the lookup table breakpoint values, but is within range. | | Memory-optimized current is linear interpolation between corresponding flux values. |
| *d*- and *q*-axis flux does not align with the lookup table breakpoint values, and is out of range. | | Cannot compute an memory-optimized current. Block uses extrapolated data. |

**Extrapolation**

The lookup tables optimized for code generation do not support extrapolation
for data that is out of range. However, you can include pre-calculated
extrapolation values in the power loss lookup table by selecting
**Specify Extrapolation**.

The block uses the endpoint parameters to resize the table data.

| User Input | Extrapolation |
| --- | --- |
| Lookup table to extrapolate to cover desired operating range | Extrapolated lookup table shown along with original table |
