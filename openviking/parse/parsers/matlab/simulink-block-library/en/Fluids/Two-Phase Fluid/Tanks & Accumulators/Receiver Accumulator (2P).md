---
type: simulink-block
title: 'Receiver Accumulator (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Tanks & Accumulators'
documentation_page: 'receiveraccumulator2p'
documentation_source_path: 'ref/receiveraccumulator2p.html'
language: en
---

# Receiver Accumulator (2P)

## Ports
```yaml
ports:
- name: L
  summary: Liquid level physical signal
  direction: output
- name: AV
  summary: Tank opening two-phase fluid
  direction: conserving
- name: BV
  summary: Tank opening two-phase fluid
  direction: conserving
- name: AL
  summary: Tank opening two-phase fluid
  direction: conserving
- name: BL
  summary: Tank opening two-phase fluid
  direction: conserving
- name: H
  summary: Tank wall thermal
  direction: conserving
```

### Output

### **L** — Liquid level physical signal

Liquid level in the tank. Use this port to monitor the amount of
liquid remaining inside.
### Conserving

### **AV** — Tank opening two-phase fluid

Opening for the fluid to flow into or out of the tank. Both liquid and
vapor can enter through this port. However, only vapor can exit through
it—until the tank is depleted of vapor, in which event liquid too can
flow out through this port.

### **BV** — Tank opening two-phase fluid

Opening for the fluid to flow into or out of the tank. Both liquid and
vapor can enter through this port. However, only vapor can exit through
it—until the tank is depleted of vapor, in which event liquid too can
flow out through this port.

### **AL** — Tank opening two-phase fluid

Opening for the fluid to flow into or out of the tank. Both liquid and
vapor can enter through this port. However, only liquid can exit through
it—until the tank is depleted of liquid, in which event vapor too can
flow out through this port.

### **BL** — Tank opening two-phase fluid

Opening for the fluid to flow into or out of the tank. Both liquid and
vapor can enter through this port. However, only liquid can exit through
it—until the tank is depleted of liquid, in which event vapor too can
flow out through this port.

### **H** — Tank wall thermal

Thermal boundary between the fluid volume and the tank wall. Use this
port to capture heat exchanges of various kinds—for example, conductive,
convective, or radiative—between the fluid and the environment external
to the tank.
## Parameters
```yaml
parameters:
- name: Total tank volume
  summary: Aggregate volume of liquid and vapor phases in the tank 1 m^3 (default) | positive scalar
  group: Main
- name: Tank cross-sectional area
  summary: Tank cross-sectional area 0.5 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port AV
  summary: Area normal to the direction of flow at port AV 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port BV
  summary: Area normal to the direction of flow at port BV 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port AL
  summary: Area normal to the direction of flow at port AL 0.01 m^2 (default) | positive scalar
  group: Main
- name: Cross-sectional area at port BL
  summary: Area normal to the direction of flow at port BL 0.01 m^2 (default) | positive scalar
  group: Main
- name: Liquid volume fraction out of range
  summary: What happens when volume fractions are out of range No error (default) | Error | Warning
  group: Main
- name: Minimum liquid volume fraction
  summary: Value below which to trigger warning or error 0.05 (default) | positive scalar between 0 and 1
  group: Main
- name: Maximum liquid volume fraction
  summary: Value above which to trigger warning or error 0.95 (default) | positive scalar between 0 and 1
  group: Main
- name: Volume fraction threshold for transition to pure liquid or pure vapor
  summary: Volume fraction of a phase below which to transition to a single-phase tank 0.05 (default) | positive scalar between
    0 and 1
  group: Main
- name: Vapor heat transfer coefficient
  summary: Coefficient for heat exchange between vapor and the tank wall 20 W/(m^2*K) (default) | positive scalar
  group: Heat Transfer
- name: Liquid heat transfer coefficient
  summary: Coefficient for heat exchange between liquid and the tank wall 100 W/(m^2*K) (default) | positive scalar
  group: Heat Transfer
- name: Initial pressure
  summary: Absolute pressure at start of simulation 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Initial liquid fraction specification
  summary: Type of initial liquid fraction Liquid mass fraction (default) | Liquid volume fraction
  group: Effects and Initial Conditions
- name: Initial liquid mass fraction
  summary: Initial mass fraction of liquid in tank 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions
- name: Initial liquid volume fraction
  summary: Initial volume fraction of liquid in tank 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions
- name: Initial liquid and vapor volumes fully saturated
  summary: Option to specify liquid and vapor as fully saturated on (default) | off
  group: Effects and Initial Conditions
- name: Initial fluid energy specification
  summary: Thermodynamic variable to use to define initial fluid energy Degree of subcooling and superheating (default) |
    Temperature | Specific enthalpy | Specific internal energy
  group: Effects and Initial Conditions
- name: Initial liquid subcooling
  summary: Liquid subcooling at start of simulation 5 deltaK (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial vapor superheating
  summary: Vapor superheating at start of simulation 5 deltaK (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial liquid temperature
  summary: Liquid temperature at start of simulation 368.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Initial vapor temperature
  summary: Vapor temperature at start of simulation 378.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Initial liquid specific enthalpy
  summary: Liquid specific enthalpy at start of simulation 400 kJ/kg (default) | scalar
  group: Effects and Initial Conditions
- name: Initial vapor specific enthalpy
  summary: Vapor specific enthalpy at start of simulation 2700 kJ/kg (default) | scalar
  group: Effects and Initial Conditions
- name: Initial liquid specific internal energy
  summary: Liquid specific internal energy at start of simulation 400 kJ/kg (default) | scalar
  group: Effects and Initial Conditions
- name: Initial vapor specific internal energy
  summary: Vapor specific internal energy at start of simulation 2700 kJ/kg (default) | scalar
  group: Effects and Initial Conditions
- name: Vaporization and condensation time constant
  summary: Characteristic duration of phase-change event 0.1 s (default) | positive scalar
  group: Effects and Initial Conditions
```

### Main

### **Total tank volume** — Aggregate volume of liquid and vapor phases in the tank `1 m^3` (default) | positive scalar

Aggregate volume of liquid and vapor phases in the tank.

### **Tank cross-sectional area** — Tank cross-sectional area `0.5 m^2` (default) | positive scalar

Cross-sectional area of the tank.

### **Cross-sectional area at port AV** — Area normal to the direction of flow at port AV `0.01 m^2` (default) | positive scalar

Area normal to the direction of flow at port
**AV**.

### **Cross-sectional area at port BV** — Area normal to the direction of flow at port BV `0.01 m^2` (default) | positive scalar

Area normal to the direction of flow at port
**BV**.

### **Cross-sectional area at port AL** — Area normal to the direction of flow at port AL `0.01 m^2` (default) | positive scalar

Area normal to the direction of flow at port
**AL**.

### **Cross-sectional area at port BL** — Area normal to the direction of flow at port BL `0.01 m^2` (default) | positive scalar

Area normal to the direction of flow at port
**BL**.

### **Liquid volume fraction out of range** — What happens when volume fractions are out of range `No error` (default) | `Error` | `Warning`

Select what happens when the block has volume fractions lower than the
**Minimum liquid volume fraction** parameter or
higher than the **Maximum liquid volume fraction**
parameter. Select `Warning` to be notified when
the volume fraction crosses a specified range. Select
`Error` to stop simulation at such
events.

### **Minimum liquid volume fraction** — Value below which to trigger warning or error `0.05` (default) | positive scalar between 0 and 1

Lower bound of the valid range for the liquid volume fraction in the
tank. Fractions below this value will trigger a simulation warning or
error (depending on the setting of the **Liquid volume fraction
out of range** block parameter.

#### Dependencies

To enable this parameter, set **Liquid volume fraction out
of range** to `Warning` or
`Error`.

### **Maximum liquid volume fraction** — Value above which to trigger warning or error `0.95` (default) | positive scalar between 0 and 1

Upper bound of the valid range for the liquid volume fraction in the
tank. Fractions above this value will trigger a simulation warning or
error (depending on the setting of the **Liquid volume fraction
out of range** block parameter.

#### Dependencies

To enable this parameter, set **Liquid volume fraction
out of range** to `Warning` or
`Error`.

### **Volume fraction threshold for transition to pure liquid or pure vapor** — Volume fraction of a phase below which to transition to a single-phase tank `0.05` (default) | positive scalar between 0 and 1

Volume fraction of either phase below which to transition to a
single-phase tank—either subcooled liquid or superheated vapor. This
parameter determines how smooth the transition is. The larger its value,
the smoother the transition and therefore the faster the simulation
(though at the cost of lower accuracy).

### Heat Transfer

### **Vapor heat transfer coefficient** — Coefficient for heat exchange between vapor and the tank wall `20 W/(m^2*K)` (default) | positive scalar

Coefficient for heat exchange between the vapor zone and its section
of the tank wall. This parameter serves to calculate the rate of this
heat exchange.

### **Liquid heat transfer coefficient** — Coefficient for heat exchange between liquid and the tank wall `100 W/(m^2*K)` (default) | positive scalar

Coefficient for heat exchange between the liquid zone and its section
of the tank wall. This parameter serves to calculate the rate of this
heat exchange.

### Effects and Initial Conditions

### **Initial pressure** — Absolute pressure at start of simulation `0.101325 MPa` (default) | scalar

Pressure in the tank at the start of simulation.

### **Initial liquid fraction specification** — Type of initial liquid fraction `Liquid mass fraction` (default) | `Liquid volume fraction`

Whether to specify the initial fraction of the liquid volume as a mass
or volume fraction.

### **Initial liquid mass fraction** — Initial mass fraction of liquid in tank `0.5` (default) | unitless scalar between 0 and 1

Mass fraction of the liquid in the tank at the start of
simulation.

#### Dependencies

To enable this parameter, set **Initial liquid fraction
specification** to `Liquid mass
fraction`.

### **Initial liquid volume fraction** — Initial volume fraction of liquid in tank `0.5` (default) | unitless scalar between 0 and 1

Volume fraction of the liquid in the tank at the start of
simulation.

#### Dependencies

To enable this parameter, set **Initial liquid fraction
specification** to `Liquid volume
fraction`.

### **Initial liquid and vapor volumes fully saturated** — Option to specify liquid and vapor as fully saturated `on` (default) | `off`

Whether to initialize the liquid and vapor in the tank in a fully
saturated state. If you clear this check box, you can specify the
initial energy of the liquid and vapor volumes.

### **Initial fluid energy specification** — Thermodynamic variable to use to define initial fluid energy `Degree of subcooling and superheating` (default) | `Temperature` | `Specific enthalpy` | `Specific internal energy`

Thermodynamic variable that the block uses to define the initial fluid
energy. If you select this check box, the liquid and vapor are both
saturated. If you clear the check box, the block uses the initial fluid
energy specification parameters to calculate the degree of subcooling or
superheating for the liquid and vapor, respectively.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box.

### **Initial liquid subcooling** — Liquid subcooling at start of simulation `5 deltaK` (default) | positive scalar

Liquid subcooling in the tank at the start of simulation. The block
initializes the initial liquid temperature to
*Tsat
(pinit)-ΔTsub,init*,
where *Tsat
(pinit)* is the saturation
temperature at the value of the **Initial pressure**
parameter and *ΔTsub,init* is
the value of this parameter.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Degree of subcooling and
superheating`.

### **Initial vapor superheating** — Vapor superheating at start of simulation `5 deltaK` (default) | positive scalar

Vapor superheating in the tank at the start of simulation. The block
initializes the initial liquid temperature to
*Tsat
(pinit)+ΔTsup,init*,
where *Tsat
(pinit)* is the saturation
temperature at the value of the **Initial pressure**
parameter and *ΔTsup,init* is
the value of this parameter.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Degree of subcooling and
superheating`.

### **Initial liquid temperature** — Liquid temperature at start of simulation `368.15 K` (default) | scalar

Liquid temperature in the tank at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Temperature`.

### **Initial vapor temperature** — Vapor temperature at start of simulation `378.15 K` (default) | scalar

Vapor temperature in the tank at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Temperature`.

### **Initial liquid specific enthalpy** — Liquid specific enthalpy at start of simulation `400 kJ/kg` (default) | scalar

Liquid specific enthalpy in the tank at the start of
simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Specific enthalpy`.

### **Initial vapor specific enthalpy** — Vapor specific enthalpy at start of simulation `2700 kJ/kg` (default) | scalar

Vapor specific enthalpy in the tank at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Specific enthalpy`.

### **Initial liquid specific internal energy** — Liquid specific internal energy at start of simulation `400 kJ/kg` (default) | scalar

Liquid specific internal energy in the tank at the start of
simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Specific internal energy`.

### **Initial vapor specific internal energy** — Vapor specific internal energy at start of simulation `2700 kJ/kg` (default) | scalar

Vapor specific internal energy in the tank at the start of
simulation.

#### Dependencies

To enable this parameter, clear the **Initial liquid and
vapor volumes fully saturated** check box and set
**Initial fluid energy specification** to
`Specific internal energy`.

### **Vaporization and condensation time constant** — Characteristic duration of phase-change event `0.1 s` (default) | positive scalar

Characteristic time to equilibrium for a phase-change event that takes
place in the tank. Increase this parameter to slow the rate of phase
change or decrease it to speed up the rate.
## Libraries

Simscape / Fluids / Two-Phase Fluid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2024b: Specify the initial conditions for the liquid and vapor volume

You can now use initial conditions in the Receiver Accumulator
(2P) block to specify liquid and vapor volumes that are not
saturated. Previously, if you initialized the liquid volume at a subcooled state or
the vapor at a superheated state, the block could not also model vapor or liquid,
respectively. You can now specify the initial liquid or vapor volume. Clear the
**Initial liquid and vapor volumes fully saturated** parameter
to specify the initial energy of the liquid volume and vapor volume.

It you update a model that contains a Receiver Accumulator (2P) block, and the
upgrade tool cannot identify a Two-Phase Fluid Properties (2P)
 or Two-Phase Fluid Predefined Properties
(2P) block connected to the network, it issues an error that the
initial liquid fraction is not updated. To manually update your initial conditions,
you may need to calculate the initial saturation boundaries at
*pinit*, the value of the
**Initial pressure** parameter, where:

- *Tsat
  (pinit)* is the initial saturation
  temperature at *pinit*.
- *hsat,liq
  (pinit)* is the initial liquid
  saturation specific enthalpy at
  *pinit*.
- *hsat,vap
  (pinit)* is the initial vapor
  saturation specific enthalpy at
  *pinit*.
- *usat,liq
  (pinit)* is the initial liquid
  saturation specific internal energy at
  *pinit*.
- *usat,vap
  (pinit)* is the initial vapor
  saturation specific internal energy at
  *pinit*.

Update the parameters as shown in this table:

| Previous Initial Condition Parameters | New Initial Condition Parameters |
| --- | --- |
| - **Initial fluid energy   specification** is   `Temperature` - *Tinit* is   the value of the **Initial   temperature** parameter | - Set **Initial fluid fraction   specification** to `Liquid   mass fraction`. - Clear the **Initial liquid and vapor   volumes fully saturated** check   box. - Set **Initial fluid energy   specification** to   `Temperature`. - If *Tinit ≤   Tsat   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `1`.   - Set the value of the **Initial     liquid temperature** parameter to     *Tinit*. - If *Tinit >   Tsat   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `0`.   - Set the value of the **Initial vapor     temperature** parameter to     *Tinit*. |
| - **Initial fluid energy   specification** is `Liquid   mass fraction` - *Mfrac,init*   is the value of the **Initial liquid mass   fraction**  parameter | - Set **Initial fluid fraction   specification** to `Liquid   mass fraction`. - Select **Initial liquid and vapor volumes   fully saturated**. - Set the value of the **Initial liquid mass   fraction**  parameter to   *Mfrac,init*. |
| - **Initial fluid energy   specification** is `Liquid   volume fraction` - *Vfrac,init*   is the value of the **Initial liquid volume   fraction**  parameter | - Set **Initial fluid fraction   specification** to `Liquid   volume fraction`. - Select **Initial liquid and vapor volumes   fully saturated**. - Set the value of the **Initial liquid   volume fraction**  parameter to   *Vfrac,init*. |
| - **Initial fluid energy   specification** is `Specific   enthalpy` - *hinit* is   the value of the **Initial specific enthalpy** parameter | - Set **Initial fluid fraction   specification** to `Liquid   mass fraction`. - Clear the **Initial liquid and vapor   volumes fully saturated** check   box. - Set **Initial fluid energy   specification** to `Specific   enthalpy`. - If *hinit ≤   hsat,liq   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `1`.   - Set the value of the **Initial     liquid specific enthalpy** parameter to     *hinit*. - If *hinit ≥   hsat,vap   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `0`.   - Set the value of the **Initial vapor     specific enthalpy** parameter to     *hinit*. - If *hsat,liq   (pinit) <   hinit <   hsat,vap   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to hinit−hsat,liq(pinit)hsat,vap(pinit)−hsat,liq(pinit).   - Set the value of the **Initial     liquid specific enthalpy** parameter to     *hsat,liq     (pinit)*.   - Set the value of the **Initial vapor     specific enthalpy** parameter to     *hsat,vap     (pinit)*. |
| - **Initial fluid energy   specification** is `Specific   internal energy` - *uinit* is   the value of the **Initial specific internal   energy**  parameter | - Set **Initial fluid fraction   specification** to `Liquid   mass fraction`. - Clear the **Initial liquid and vapor   volumes fully saturated** check   box. - Set **Initial fluid energy   specification** to `Specific   internal energy`. - If *uinit ≤   usat,liq   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `1`.   - Set the value of the **Initial     liquid specific internal energy**     parameter to     *uinit*. - If *uinit ≥   usat,vap   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to     `0`.   - Set the value of the **Initial vapor     specific internal energy** parameter to     *uinit*. - If *usat,liq   (pinit) <   uinit <   usat,vap   (pinit)*:  - Set the value of the **Initial     liquid mass fraction** parameter to uinit−usat,liq(pinit)usat,vap(pinit)−usat,liq(pinit).   - Set the value of the **Initial     liquid specific internal energy**     parameter to     *usat,liq     (pinit)*.   - Set the value of the **Initial vapor     specific internal energy** parameter to     *usat,vap     (pinit)*. |

## Description

Tank with liquid and vapor volumes of variable proportion

The Receiver-Accumulator (2P) block represents a tank
with fluid that can undergo phase change. The liquid and vapor phases, referred to as
*zones*, are modeled as distinct volumes that can change in size
during simulation, but do not mix. The relative amount of space a zone occupies in the
system is called a *zone fraction*, which ranges from
`0` to `1`. The vapor-liquid mixture phase is not
modeled.

In an HVAC system, when this tank is placed between a condenser and an expansion
valve, it acts as a receiver. Liquid connections to the block are made at ports
**AL** and **BL**. When the tank is placed between
an evaporator and a compressor, it acts as an accumulator. Vapor connections to the
block are made at ports **AV** and **BV**. A fluid of
either phase can be connected to either port, however the fluid exiting from a V port is
in the vapor zone and an L port is in the liquid zone. There is no mass flow through
unconnected ports.

The temperature of the tank walls are set at port **H**.

The liquid level of the tank is reported as a zone fraction at port
**L**. If the liquid level reports `0`, the tank
is fully filled with vapor. The tank is never empty.

### Heat Transfer

The total heat transfer, *QH*, is the sum
of the heat transfer in the liquid and vapor phases:

QH=QL+QV.

The portion of the heat transfer that goes to the liquid volume,
*QL*, accounts for the heat transfer
between the liquid and the wall and between the liquid and the vapor,

QL=(Sc+zLSs)αL(TH−TL)+ScαLV(TV−TL)

where:

- *z*L is the liquid volume
  fraction of the tank.
- *S*c is the **Tank
  cross sectional area** parameter.
- *S*s is surface area of the
  tank side, which the block calculates from the volume and tank
  cross-sectional area, assuming that the tank is cylindrical.
- *α*L is the **Liquid
  heat transfer coefficient** parameter.
- *TH* is the temperature of the
  tank wall.
- *TL* is the temperature of the
  liquid.

The block calculates the heat transfer coefficient between the liquid
and the vapor as

αLV=11αL+1αV.

The portion of the heat transfer that goes to the vapor volume,
*QV*, accounts for the heat transfer
between the vapor and the wall and between the liquid and the vapor,

QV=(Sc+(1−zL)Ss)αV(TH−TV)+ScαLV(TL−TV),

where:

- *α*V is the **Vapor
  heat transfer coefficient**.
- *TV* is the temperature of the
  vapor.

The liquid volume fraction is determined from the liquid mass fraction:

zL=fM,LνLfM,LνL+(1−fM,L)νV,

where:

- *fM,L* is the mass fraction of
  the liquid.
- *νL* is the specific volume of
  the liquid.
- *νV* is the specific volume of
  the vapor.

### Energy Flow Rates Due to Phase Change

When the liquid specific enthalpy is greater than or equal to the saturated liquid
specific enthalpy, the mass flow rate of the vaporizing fluid is:

m˙Vap=ML(hL−hL,Sat)/(hV−hL,Sat)τ.

where:

- *ML* is the total liquid
  mass.
- *τ* is the **Vaporization and condensation
  time constant** parameter.
- *hL* is the specific enthalpy
  of the liquid at the internal node.
- *hL,Sat* is the saturated
  liquid specific enthalpy at the internal node.
- *hV* is the specific enthalpy
  of the vapor.
- *hV,Sat* is the saturated
  vapor specific enthalpy.

The energy flow associated with vaporization is:

ϕVap=m˙VaphV,Sat,

When the liquid specific enthalpy is lower than the saturated liquid specific
enthalpy, no vaporization occurs, and *ṁVap =
0*.

Similarly, when the vapor specific enthalpy is less than or equal to the saturated
vapor specific enthalpy, the mass flow rate of the condensing fluid is:

m˙Con=MV(hV−hV,Sat)/(hV−hL,Sat)τ.

where *MV* is the total
vapor mass.

The energy flow associated with condensation is:

ϕCon=m˙ConhL,Sat,

When the vapor specific enthalpy is higher than the saturated vapor specific
enthalpy, no condensation occurs, and *ṁCon =
0*.

### Mass Balance

The total tank volume is constant. Due to phase change, the volume fraction and
mass of the fluid changes. The mass balance in the liquid zone is:

dMLdt=m˙L,In−m˙L,Out+m˙Con−m˙Vap,

where:

- m˙L,In is the inlet liquid mass
  flow rate at all L and V ports.
- m˙L,Out is the outlet liquid mass
  flow rate:

  m˙L,Out=−(m˙AL+m˙BL),
- m˙Con is the mass flow rate of the
  condensing fluid.
- m˙Vap is the mass flow rate of the
  vaporizing fluid.

The mass balance in the vapor zone is:

dMVdt=m˙V,In−m˙V,Out−m˙Con+m˙Vap,

where:

- *MV* is the total vapor
  mass.
- m˙V,In is the inlet vapor mass
  flow rate at all L and V ports.
- m˙V,Out is the outlet vapor mass
  flow rate:

  m˙V,Out=−(m˙AV+m˙BV).

If there is only one zone present in the tank, the outlet mass flow
rate of the fluid is the sum of the flow rate through all of the ports:

m˙phase,Out=−(m˙AL+m˙BL+m˙AV+m˙BV).

where m˙phase,Out is m˙L,Out if the fluid is entirely liquid, and m˙V,Out if the fluid is entirely vapor.

### Energy Balance

The fluid can heat or cool depending on the heat transfer between the tank and
wall, which is set by the temperature at port **H**.

The energy balance in the liquid zone is:

MLduLdt+dMLdtuL=ϕL,In−ϕL,Out+ϕCon−ϕVap+QL.

where:

- *uL* is the specific internal
  energy of the liquid.
- *ϕL,In* is the inlet liquid
  energy flow rate at all L and V ports.
- *ϕL,Out* is the outlet liquid
  energy flow rate:

  ϕL,Out=−(ϕAL+ϕBL).
- *ϕCon* is the energy flow rate
  of the condensing vapor.
- *ϕVap* is the energy flow rate
  of the vaporizing liquid.
- *QL* is the heat transfer between the tank wall and the
  liquid.

The energy balance in the vapor zone is:

MVduVdt+dMVdtuV=ϕV,In−ϕV,Out−ϕCon+ϕVap+QV.

- *uV* is the specific internal
  energy of the vapor.
- *ϕV,In* is the inlet vapor
  energy flow rate at all L and V ports.
- *ϕV,Out* is the outlet vapor
  energy flow rate:

  ϕV,Out=−(ϕAV+ϕBV).
- *QV* is the heat transfer
  between the tank wall and the vapor.

If there is only one zone present in the tank, the outlet energy flow
rate is the sum of the flow rate through all of the ports:

ϕphase,Out=−(ϕAL+ϕBL+ϕAV+ϕBV).

where *ϕphase,Out* is
*ϕL,Out* if the fluid is entirely
liquid, and *ϕV,Out* if the fluid is
entirely vapor.

### Momentum Balance

There are no pressure changes modeled in the tank, including hydrostatic pressure.
The pressure at any port is equal to the internal tank pressure.

The Receiver Accumulator block models the vapor and
liquid volumes separately. If you input vapor or liquid quickly, the block may
compress the vapor volume and the pressure may rise faster than expected. The
pressure rises because when there is a high vapor or liquid mass flow rate input,
the temperature rise due to compression is faster than the heat transfer that cools
the vapor. If you add the vapor slowly, the heat transfer between the vapor and the
liquid brings the vapor temperature down, which allows it to condense into liquid,
and the pressure will not spike. Additionally, if you wait until the block achieves
equilibrium, adding vapor or liquid shifts the mass fraction and does not cause
pressure spikes.

### Assumptions and Limitations

- Pressure must remain below the critical pressure.
- Hydrostatic pressure is not modeled.
- The container wall is rigid, therefore the total volume of fluid is
  constant.
- The thermal mass of the tank wall is not modeled.
- Flow resistance through the outlets is not modeled. To model pressure
  losses associated with the outlets, connect a Local
  Restriction (2P) block or a Flow
  Resistance (2P) block to the ports of the
  Receiver-Accumulator (2P) block.
- A liquid-vapor mixture is not modeled.
