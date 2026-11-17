---
type: simulink-block
title: 'Counterbalance Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'counterbalancevalveil'
documentation_source_path: 'ref/counterbalancevalveil.html'
language: en
---

# Counterbalance Valve (IL)

## Ports
```yaml
ports:
- name: L
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: P
  summary: Pressure port isothermal liquid
  direction: conserving
```

### Conserving

### **L** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the load.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the back pressure of the valve.

### **P** — Pressure port isothermal liquid

Pilot pressure port.
## Parameters
```yaml
parameters:
- name: Opening parameterization
  summary: Opening parameterization Linear - Area vs. pressure (default) | Tabulated data - Area vs. pressure | Tabulated
    data - Volumetric flow rate vs. pressure
  group: Model Parameterization
- name: Set pressure differential
  summary: Initial spring compression pressure 5 MPa (default) | nonnegative scalar
  group: Model Parameterization
- name: Pressure differential vector
  summary: 'Relief stage pressure drop values 5 : 0.2 : 6 MPa (default) | 1-by-*n* vector'
  group: Model Parameterization
- name: Reference pressure differential vector
  summary: 'Pressure drop across relief stage 5 : 0.2 : 6 MPa (default) | vector'
  group: Model Parameterization
- name: Reference volumetric flow rate vector
  summary: Flow rate through relief stage [6.4e-09, .0013, .0027, .0041, .0055, .007] m^3/s (default) | vector
  group: Model Parameterization
- name: Maximum opening pressure differential
  summary: Maximum relief valve pressure 6 MPa (default) | positive scalar
  group: Model Parameterization
- name: Maximum opening area
  summary: Relief stage maximum open area 1e-4 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Leakage area
  summary: Gap area when valve is in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Pilot ratio
  summary: Pilot area ratio 3 (default) | positive scalar
  group: Model Parameterization
- name: Back pressure ratio
  summary: Back pressure area ratio 4 (default) | positive scalar
  group: Model Parameterization
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Model Parameterization
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: Model Parameterization
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar
  group: Model Parameterization
- name: Opening area vector
  summary: Relief stage opening areas [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Opening dynamics
  summary: Whether to introduce flow lag due to orifice opening off (default) | on
  group: Model Parameterization
- name: Opening time constant
  summary: Orifice opening time constant 0.1 s (default) | positive scalar
  group: Model Parameterization
- name: Cracking pressure differential
  summary: Set pressure for check valve operation 0.01 MPa (default) | positive scalar
  group: Check Valve
- name: Maximum opening pressure differential
  summary: Maximum pressure in valve 0.1 MPa (default) | positive scalar
  group: Check Valve
- name: Maximum opening area
  summary: Maximum open area 1e-4 m^2 (default) | positive scalar
  group: Check Valve
- name: Pressure differential vector
  summary: 'Pressure differential for check valve operation [0.01 : 0.01 : 0.1] MPa (default) | 1-by-*n* vector'
  group: Check Valve
- name: Opening area vector
  summary: Check stage opening areas [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2 (default)
    | 1-by-*n* vector
  group: Check Valve
- name: Volumetric flow rate vector
  summary: Check stage volumetric flow rates [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s (default)
    | 1-by-*n* vector
  group: Check Valve
```

### Model Parameterization

### **Opening parameterization** — Opening parameterization `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of modeling the opening of the valve. When you select
`Linear - Area vs. pressure` or
`Tabulated data - Area vs. pressure`, the
block relates the opening area to the control pressure. When you select
`Tabulated data - Volumetric flow rate vs.
pressure`, the block takes a reference flow rate and
pressure differential curve for the relief and check stages of the
counterbalance valve, where the pressure at the back port and pilot port
corresponds to 1 atm in the reference curve for the relief stage.

### **Set pressure differential** — Initial spring compression pressure `5` `MPa` (default) | nonnegative scalar

Pressure differential to lift the relief stage. Use this parameter to
adjust the set pressure supplied by the data sheet.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Pressure differential vector** — Relief stage pressure drop values `5 : 0.2 : 6` `MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the relief stage. The
vector elements must correspond one-to-one with the elements in the
**Opening area vector** parameter. You must enter
the elements in ascending order. This vector defines the control
pressures that govern valve opening and shutting. The first element in
the vector defines the set pressure, which is the control pressure when
the relief stage just begins to open. The last element defines the
control pressure for which the valve is fully open.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Reference pressure differential vector** — Pressure drop across relief stage `5 : 0.2 : 6` `MPa` (default) | vector

Vector of pressure drops across the relief stage. The vector elements
must correspond one-to-one with the elements in the **Reference
volumetric flow rate vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Reference volumetric flow rate vector** — Flow rate through relief stage `[6.4e-09, .0013, .0027, .0041, .0055, .007]` `m^3/s` (default) | vector

Vector of flow rates through the relief stage. The vector elements
must correspond one-to-one with the elements in the **Reference
pressure differential vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Maximum opening pressure differential** — Maximum relief valve pressure `6` `MPa` (default) | positive scalar

The maximum relief valve pressure.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Maximum opening area** — Relief stage maximum open area `1e-4` `m^2` (default) | positive scalar

Maximum open area of the relief stage orifice.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Leakage area** — Gap area when valve is in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any
area smaller than this value is saturated to the specified leakage area.
This value contributes to numerical stability by maintaining continuity
in the flow.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Pilot ratio** — Pilot area ratio `3` (default) | positive scalar

Ratio of the pressure-acting area of the pilot to the pressure-acting
area of the load.

### **Back pressure ratio** — Back pressure area ratio `4` (default) | positive scalar

Ratio of the back pressure pressure-acting area to the load
pressure-acting area.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-shut
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

### **Opening area vector** — Relief stage opening areas `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001]` `m^2` (default) | 1-by-*n* vector

Vector of relief stage opening areas. The vector elements must
correspond one-to-one with the elements in the **Pressure
differential vector** parameter. List the elements in
ascending order. All elements must be greater than 0.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Opening dynamics** — Whether to introduce flow lag due to orifice opening `off` (default) | `on`

Whether to account for the transient effects to the fluid system due to opening the
valve. Selecting **Opening dynamics** approximates the
opening conditions by introducing a first-order lag in the pressure
response. The **Opening time constant** parameter also
impacts the modeled opening dynamics.

When enabled, these dynamics apply to the relief stage and not the
check stage of the counterbalance valve.

### **Opening time constant** — Orifice opening time constant `0.1` `s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state conditions when opening or closing the valve from one
position to another. This parameter impacts the modeled opening
dynamics.

#### Dependencies

To enable this parameter, select **Opening dynamics**.

### Check Valve

### **Cracking pressure differential** — Set pressure for check valve operation `0.01` `MPa` (default) | positive scalar

Pressure differential that lifts the check valve.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Maximum opening pressure differential** — Maximum pressure in valve `0.1` `MPa` (default) | positive scalar

Maximum valve pressure. This parameter bounds the pressures at the
valve exit to maintain physical values during simulation.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Maximum opening area** — Maximum open area `1e-4` `m^2` (default) | positive scalar

Maximum open area of the check valve in the load line. Internally, this check valve is
in parallel with the relief stage.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Linear - Area vs.
pressure`.

### **Pressure differential vector** — Pressure differential for check valve operation `[0.01 : 0.01 : 0.1]` `MPa` (default) | 1-by-*n* vector

Vector of pressure differentials for the check valve stage.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Area vs. pressure` or `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Opening area vector** — Check stage opening areas `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2` (default) | 1-by-*n* vector

Vector of opening areas for the check valve stage. The vector elements
must correspond one-to-one with the elements in the **Pressure
differential vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Volumetric flow rate vector** — Check stage volumetric flow rates `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rates for the check valve stage. The elements of this vector
must correspond to the elements in the **Pressure differential
vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2022b: Opening parameterization options include volumetric flow rate

You can set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs. pressure`.
This selection enables these new parameters:

- **Set pressure differential**
- **Reference pressure differential vector**
- **Reference volumetric flow rate vector**
- **Volumetric flow rate vector**

To improve clarity:

- The `Linear` option has been renamed to
  `Linear - Area vs. pressure`.
- The `Tabulated` option has been renamed to
  `Tabulated data - Area vs. pressure`

### R2022b: Access pre-parameterized block options

You can now select from available pre-parameterization options. Available
manufacturers are Rexroth Bosch Group and Sun Hydraulics.

## Description

High-pressure regulation valve in an isothermal liquid system

The Counterbalance Valve (IL) block represents a
counterbalance pressure control valve in an isothermal liquid network. A counterbalance
valve is common in applications where high-pressure events are common or when a task
requires high-pressure controlled manipulation at production speeds This includes tasks
such as overloading hydraulics or lowering suspended loads. The valve functions under
the force balance between a spring, the back pressure at port **B**,
and the load pressure at port **L**. The valve responds to changes in
the pilot line pressure. When the pilot pressure exceeds the back pressure, the valve
begins to open.

There is no flow between ports **B** and **P** or
ports **L** and **P**.

This figure shows a typical counterbalance valve cutaway.

### Valve Opening

The block balances the forces of the counterbalance valve, such that

ppilotApilot+ploadAload=pbackAback+Fset+kspringxspool,

where:

- *ppilot* is the pressure at
  port **P**.
- *pload* is the pressure at
  port **L**.
- *pback* is the pressure at
  port **B**.
- *Fset* is the accumulated
  force due to the spring.
- *kspring* is the spring
  constant.
- *xspool* is the linear
  position of the relief stage spool body. This position is relative to
  the unpressurized installed position.

The block sets the pressure-acting areas
*Apilot*,
*Aload*, and
*Aback* according to the
**Pilot ratio** parameter,
*Rpilot*, such that

Rpilot=ApilotAload,

and the **Back pressure ratio** parameter,
*Rback*, such that

Rback=AbackAload.

A ratio of 4:1 or 3:1 is typical for counterbalance
valves.

The preset force, *Fspring*, represents
the combined spring preloading and spring force at port **B**. This
force is a function of *pset*, the
**Set pressure differential** parameter, such that

Fset=psetAload.

This figure shows the schematic from the Counterbalance Valve with Test Harness example where the
pressure ports control the valve by acting on surfaces with differential area. The
arrows show the direction of force due to pressure or spring force acting on the
relief stage body. The gray sections represent a single, solid body that moves to
the right when the relief stage opens. The check valve travels to the left when it
opens.

Counterbalance valve schematic where the load pressure and pilot pressure act to the right, and the back pressure and spring act to the left.

### Opening Parameterization

The block accepts linear or tabulated parameterizations. The check valve portion of the
block operates identically to the  Check Valve
(IL) block.

**Linear Parameterization**

When you set **Opening parameterization** to
`Linear - Area vs. pressure`, the block calculates
the valve opening area, such that

Avalve=p^(Amax−Aleak)+Aleak.

The block calculates the normalized control pressure, p^, as

p^=(pload+ppilotRpilot−pbackRback)−pset(pmax−pset),

where *pmax* is the **Maximum
opening pressure differential** parameter.

The normalized check valve pressure is

p^=pcontrol−pcrackingpmax−pcracking,

where:

- *pcracking* is the
  **Cracking pressure differential**
  parameter.
- *pmax* is the check valve
  **Maximum opening pressure differential**
  parameter.

When the valve is in a near-open or near-closed position
in the linear parameterization, you can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter.
If the **Smoothing factor** parameter is nonzero, the block
smoothly saturates the control pressure between
*pcracking* and
*pmax*. For more information,
see Numerical Smoothing.

**Tabulated Area Parameterization**

When you set **Opening parameterization** to `Tabulated data
- Area vs. pressure`, the block uses the same equations as for
the linear parameterization but with tabulated data. The tabulated data
represents area with respect to a given control pressure, where *Pcontrol* =
*pload* +
*pPilotRPilot*
-
*pBackRBack*. The first element of the **Pressure differential
vector** parameter is the set pressure, which is the control
pressure when the relief stage begins to open. The last element defines the
control pressure when the valve is fully open.

**Tabulated Flow Rate Parameterization**

When you set **Opening parameterization** to `Tabulated data
- Volumetric flow rate vs. pressure`, the volumetric flow rate
equations refer to these quantities:

- ρ¯valve is the simulated average density of relief stage
  flow.
- *K* is the flow coefficient through the relief
  stage.
- *Δpvalve* is the pressure
  drop across the relief stage during flow.
- *Δpcrit* is the critical
  pressure drop across the relief stage during flow.
- *pcontrol* is the
  simulated control pressure.
- *pcontrol,TLU,Ref* is an
  internally derived lookup table of changing control
  pressures.
- *pset* is the set pressure
  differential.
- *Recrit* is the
  **Critical Reynolds number** parameter.
- *Cd* is the
  **Discharge coefficient** parameter.
- *ν* is the kinematic viscosity.
- *KTLU,Ref* is an
  internally derived lookup table of changing flow coefficients as a
  function of valve area.
- V˙TLU,Ref is the reference volumetric flow rate
  vector.
- *ppilot,Ref*,
  *pback,Ref*,
  *pload,Ref* are the
  pilot pressure, back pressure, and load pressure for the
  user-provided **Reference volumetric flow rate
  vector** parameter, respectively.

The block calculates the mass flow rate for the relief stage such that

m˙valve=ρ¯valveKΔpvalve(Δpvalve2+Δpcrit2)1/4,

where:

Δpvalve=pload−pbackΔpcrit=π2ρ¯valve8Cd(Recritυ)K=tablelookup(pcontrol,TLU,Ref,KTLU,Ref,pcontrol,interpolation = linear, extrapolation = nearest)

Liquid flows from the load port to the back port. The block
extrapolates *K* to the nearest point after it calculates
*KTLU,Ref* as

KTLU,Ref=V˙TLU,RefΔpvalve,TLU,ref,

where *Δpvalve,TLU,ref* =
*pload,Ref* -
*pback,Ref*. The block calculates the control pressure as

pcontrol=Rpilotppilot+pload−Rbackpback

and the reference control vector as

pcontrol,TLU,Ref=Rpilotppilot,Ref+pload,Ref−Rbackpback,Ref+poffset,

where:

ppilot,Ref=1 atmpback,Ref=1 atmpload,Ref=pback,Ref+Δpvalve,TLU,Ref

The
block internally derives *Δpflow,Ref*,
which is the pressure drop for fluid flow in the specified reference
curve. The block calculates
*poffset* internally as

poffset=pset−Rpilotppilot,Ref−pload,Ref(1)+Rbackpback,Ref.

The table shows how the block controls the relief and check stages opening
areas depending the **Opening area** parameter
setting.

| Opening parameterization | Relief stage | Check stage |
| --- | --- | --- |
| `Linear - Area vs. pressure` |  |  |
| `Tabulated - Area vs. pressure` |  |  |
| `Tabulated - Volumetric flow rate vs. pressure` |  |  |

### Predefined Parameterization

You can populate the block with pre-parameterized manufacturing data, which allows you to
model a specific supplier component.

To load a predefined parameterization:

1. In the block dialog box, next to **Selected part**, click the
   "<click to select>" hyperlink next to **Selected part** in
   the block dialog box settings.
2. The Block Parameterization Manager window opens. Select a part from the menu
   and click **Apply all**. You can narrow the choices using the
   **Manufacturer** drop down menu.
3. You can close the **Block Parameterization Manager** menu.
   The block now has the parameterization that you specified.
4. You can compare current parameter settings with a specific supplier component
   in the Block Parameterization Manager window by selecting a part and viewing the
   data in the **Compare selected part with block**
   section.

**Note**

Predefined block parameterizations use available data sources to supply parameter
values. The block substitutes engineering judgment and simplifying assumptions for
missing data. As a result, expect some deviation between simulated and actual physical
behavior. To ensure accuracy, validate the simulated behavior against experimental data
and refine your component models as necessary.

To learn more, see List of Pre-Parameterized Components.
