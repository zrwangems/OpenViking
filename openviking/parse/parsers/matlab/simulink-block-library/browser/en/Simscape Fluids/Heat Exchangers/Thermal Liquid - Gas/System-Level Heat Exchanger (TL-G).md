---
type: simulink-block
title: 'System-Level Heat Exchanger (TL-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'systemlevelheatexchangertlg'
documentation_source_path: 'ref/systemlevelheatexchangertlg.html'
language: en
---

# System-Level Heat Exchanger (TL-G)

## Ports

### Output

### **Q1** — Rate of heat transfer to thermal liquid, W physical signal

Rate of heat transfer to the thermal liquid, returned as a physical signal, in W. The
physical signals at ports **Q1** and
**Q2** are usually equal in value with the opposite
sign. However, if you select **Enable wall thermal
mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being
transferred.

### **Q2** — Rate of heat transfer to gas, W physical signal

Rate of heat transfer to the gas, returned as a physical signal, in W. The physical
signals at ports **Q1** and **Q2** are
usually equal in value with the opposite sign. However, if you select
**Enable wall thermal mass**, then these two
signals may have different values because the wall may absorb and
release some of the heat being transferred.
### Conserving

### **A1** — Thermal liquid port thermal liquid

Inlet or outlet port associated with the thermal liquid
network.

### **B1** — Thermal liquid port thermal liquid

Inlet or outlet port associated with the thermal liquid
network.

### **A2** — Gas port gas

Inlet or outlet port associated with the gas network.

### **B2** — Gas port gas

Inlet or outlet port associated with the gas network.

## Parameters

### Configuration

### **Flow arrangement at nominal operating conditions** — Flow path alignment `Counter flow - Thermal Liquid 1 flows from A to B, Gas 2 flows from B to A` (default) | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

Flow path alignment between the heat exchanger sides at nominal
operating condition. The available flow arrangements are:

- `Counter flow - Thermal Liquid 1 flows from A
  to B, Gas 2 flows from B to A` — The flows
  run parallel to each other, in the opposite
  directions.
- `Parallel flow - Both fluids flow from A to
  B` — The flows run in the same
  direction.
- `Cross flow - Both fluids flow from A to
  B` — The flows run perpendicular to each
  other.

The choice between parallel flow and counter flow affects how the
block determines the size of the heat exchanger. The counter flow
setting is the most effective, and needs the smallest size to meet the
specified performance. Conversely, parallel flow is the least effective,
and needs the biggest size to meet the specified performance.

Flow direction at the nominal condition (from A to B, or from B to A)
only affects the model initialization, when you select
**Initialize thermal liquid to nominal operating
conditions** or **Initialize gas to nominal
operating conditions**. If you set different initial
operating conditions, the flow directions can be different.

After the block determines the size of the heat exchanger, this
setting does not play a role in how the block calculates the heat
transfer during simulation. Instead, the heat transfer depends on the
flow directions during simulation. For example, if you set the parameter
to parallel flow but set up the model to run in counter flow, then the
rate of heat transfer during simulation will not match the specified
performance, even if the rest of the boundary conditions are the
same.

If you set the parameter to cross flow, then the block models the flow
paths as perpendicular inside the heat exchanger, so the flow directions
during simulation do not matter.

### **Enable wall thermal mass** — Whether to enable effect of thermal mass on heat transfer surface `off` (default) | `on`

Whether to enable the effect of thermal mass on the heat transfer
surface. When you select this parameter, the block introduces additional
dynamics to the simulation and takes longer to reach steady state, but
this parameter does not affect the results at steady-state simulation.

### **Wall mass** — Mass of heat transfer surface `1 kg` (default) | positive scalar

Mass of the heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### **Wall specific heat** — Specific heat of heat transfer surface `490 J/(K*kg)` (default) | positive scalar

Specific heat of the heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### **Initialize wall temperature to nominal operating conditions** — Option for initializing wall temperature `on` (default) | `off`

Option to initialize the wall temperature to nominal operating
conditions or specified values. If you select this parameter, the block
calculates the initial wall temperature from the nominal operating
conditions specified for both fluid sides. If you clear this parameter,
you can specify the initial wall temperature directly with the
**Initial wall temperature** parameter.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### **Initial wall temperature** — Initial temperature of wall `293.15 K` (default) | positive scalar or two element vector

Initial temperature of the wall. If you specify a scalar, the block assumes that the
initial wall temperature is uniform. If you specify a two-element
vector, then the block assumes that the initial wall temperature varies
linearly between ports **A1** and
**A2** and ports **B1** and
**B2**. The first element corresponds to the
temperature at ports **A1** and **A2**
and the second element corresponds to the temperature at ports
**B1** and **B2**.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass** and
clear the **Initialize wall temperature to nominal operating
conditions** check box.

### **Cross-sectional area at port A1** — Flow area at port A1 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01 m^2` (default) | positive scalar

Flow area at the gas port **A2**.

### **Cross-sectional area at port B2** — Area normal to flow at port B2 `0.01 m^2` (default) | positive scalar

Flow area at the gas port **B2**.

### Thermal Liquid 1

### **Nominal operating condition** — Nominal operating condition `Heat transfer from Thermal Liquid 1 to Gas 2` (default) | `Heat transfer from Gas 2 to Thermal Liquid 1`

Nominal operating condition to use for the thermal liquid network:
:

- `Heat transfer from Thermal Liquid 1 to Gas
  2` — The thermal liquid is cooled and the gas
  is heated.
- `Heat transfer from Gas 2 to Thermal Liquid
  1` — The gas is cooled and the thermal liquid
  is heated.

This setting relates only to the nominal operating condition
parameters. It does not mean that heat transfer can only happen in the
specified direction during simulation.

### **Nominal mass flow rate** — Mass flow rate between thermal liquid ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A1** to port
**B1** during the nominal operating
condition.

### **Nominal pressure drop** — Pressure drop between thermal liquid ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A1** to port
**B1** during the nominal operating
condition.

### **Nominal inlet pressure** — Pressure at the thermal liquid inlet `0.101325 MPa` (default) | positive scalar

Pressure at the thermal liquid inlet of the heat exchanger during nominal operating
condition.

### **Nominal inlet temperature** — Temperature at the thermal liquid inlet `333.15 K` (default) | positive scalar

Temperature at the thermal liquid inlet of the heat exchanger during the nominal
operating condition.

### **Heat transfer capacity specification** — How to specify heat transfer capacity of thermal liquid `Rate of heat transfer` (default) | `Outlet condition`

Whether to specify the performance of the heat exchanger for the
thermal liquid at the nominal operating condition directly, by the rate
of heat transfer, or indirectly, by the outlet condition.

### **Nominal rate of heat transfer** — Rate of heat transfer `1 kW` (default) | positive scalar

Rate of heat transfer. The **Nominal Operating
condition** parameter determines the network that the heat
transfers from and to:

- If **Nominal operating condition** is
  `Heat transfer from Thermal Liquid 1 to Gas
  2`, this parameter is the rate of the heat
  transfer from the thermal liquid to the gas during the nominal
  operating condition.
- If **Nominal operating condition** is
  `Heat transfer from Gas 2 to Thermal Liquid
  1`, this parameter is the rate of the heat
  transfer from the gas to the thermal liquid during the nominal
  operating condition.

#### Dependencies

To enable this parameter, set **Heat transfer capacity
specification** to `Rate of heat
transfer`.

### **Nominal outlet temperature** — Outlet temperature `323.15 K` (default) | positive scalar

Temperature at the thermal liquid outlet of the heat exchanger during
the nominal operating condition.

#### Dependencies

To enable this parameter, set **Heat transfer capacity
specification** to `Outlet
condition`.

### **Thermal liquid volume** — Total volume of thermal liquid `0.001 m^3` (default) | positive scalar

Total volume of thermal liquid inside the heat exchanger.

### **Initialize thermal liquid to nominal operating conditions** — Option for initializing thermal liquid `on` (default) | `off`

Option to initialize the thermal liquid to nominal operating
conditions or specified values. If you select this parameter, the block
initializes the thermal liquid to the nominal operating conditions. If
you clear this check box, you can specify the initial conditions
directly with additional parameters.

### **Initial thermal liquid pressure** — Thermal liquid pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Thermal liquid pressure at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize thermal
liquid to nominal operating conditions** check
box.

### **Initial thermal liquid temperature** — Thermal liquid temperature at start of simulation `293.15 K` (default) | positive scalar

Thermal liquid temperature at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize thermal
liquid to nominal operating conditions** check
box.

### Gas 2

### **Nominal mass flow rate** — Mass flow rate between gas ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A2** to port
**B2** during the nominal operating
condition.

### **Nominal pressure drop** — Pressure drop between gas ports during nominal operating condition `0.001 MPa` (default) | positive scalar

Pressure drop from port **A2** to port
**B2** during the nominal operating
condition.

### **Nominal inlet pressure** — Pressure at gas inlet `0.101325 MPa` (default) | positive scalar

Pressure at the gas inlet of the heat exchanger during the nominal
operating condition.

### **Nominal inlet temperature** — Temperature at the gas inlet `293.15 K` (default) | positive scalar

Temperature at the gas inlet of the heat exchanger during the nominal operating
condition.

### **Gas volume** — Total volume of gas in heat exchanger `0.1 m^3` (default) | positive scalar

Total volume of gas inside the heat exchanger.

### **Initialize gas to nominal operating conditions** — Option for initializing gas `on` (default) | `off`

Option to initialize the gas to nominal operating conditions or
specified values. If you select this parameter, the block initializes
the gas to the nominal operating conditions. If you clear this check
box, you can specify the initial conditions directly with additional
parameters.

### **Initial gas pressure** — Gas pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Gas pressure at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize gas to
nominal operating conditions** check box.

### **Initial gas temperature** — Gas temperature at the start of simulation `293.15 K` (default) | positive scalar

Gas temperature at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize gas to
nominal operating conditions** check box.

### Correlation Coefficients

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid** — Correlation coefficient for thermal liquid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for thermal liquid. The default value
is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid** — Reynolds number exponent in correlation for thermal liquid `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for thermal liquid.

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid** — Prandtl number exponent in correlation for thermal liquid `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for thermal liquid.

### **a in Nu = a\*Re^b\*Pr^c for gas** — Correlation coefficient for gas `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for gas. The default value is based
on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for gas** — Reynolds number exponent in correlation for gas `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for gas. The default value is based
on the Colburn equation.

### **c in Nu = a\*Re^b\*Pr^c for gas** — Prandtl number exponent in correlation for gas `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for gas. The default value is based
on the Colburn equation.

## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Heat exchanger based on performance data between thermal liquid and gas networks

The System-Level Heat Exchanger (TL-G) block models a heat
exchanger based on performance data between a thermal liquid and a gas network.

The block uses performance data from the heat exchanger datasheet, rather than the detailed
geometry of the exchanger. You can adjust the size and performance of the heat exchanger
during design iterations, or model heat exchangers with uncommon geometries. You can
also use this block to model heat exchangers with a certain level of performance at an
early design stage, when detailed geometry data is not yet available.

You parameterize the block by the nominal operating condition. The block sizes the
heat exchanger to match the specified performance at the nominal operating condition at
steady state.

This block is similar to the Heat Exchanger (G-TL)
block, but uses a different parameterization model. The table compares the two
blocks:

| Heat Exchanger (G-TL) | System-Level Heat Exchanger (TL-G) |
| --- | --- |
| Block parameters are based on the heat exchanger geometry | Block parameters are based on performance and operating conditions |
| Heat exchanger geometry may be limited by the available geometry parameter options | Model is independent of the specific heat exchanger geometry |
| You can adjust the block for different performance requirements by tuning geometry parameters, such as fin sizes and tube lengths | You can adjust the block for different performance requirements by directly specifying the desired heat and mass flow rates |
| You can select between parallel, counter, shell and tube, or cross flow configurations | You can select between parallel, counter, or cross-flow arrangement at nominal operating conditions to help with sizing |
| Predictively accurate results over a wide range of operating conditions, subject to the applicability of the E-NTU equations and the heat transfer coefficient correlations | Very accurate results around the specified operating condition; accuracy may decrease far away from the specified operating conditions |
| Heat transfer calculations account for the variation of temperature along the flow path by using the E-NTU model | Heat transfer calculations approximate the variation of temperature along the flow path by dividing it into three segments |

### Heat Transfer

The block divides the gas flow and the thermal liquid flow each into three segments of
equal size. The block calculates heat transfer between the fluids in each segment.
For simplicity, the equation in this section are for one segment.

If you clear the **Enable wall thermal mass** check box, then the heat
balance in the heat exchanger is

Qseg,G+Qseg,TL=0,

where:

- *Qseg,G* is the heat flow rate
  from the wall that is the heat transfer surface to the gas in the
  segment.
- *Qseg,TL* is the heat flow rate
  from the wall to the thermal liquid in the segment.

If you select **Enable wall thermal mass**, then the heat balance in the
heat exchanger is

Qseg,G+Qseg,TL=−MwallcpwallNdTseg,walldt,

where:

- *Mwall* is the mass of the
  wall.
- *cpwall* is
  the specific heat of the wall.
- *N* = 3 is the number of segments.
- *Tseg,wall* is the average wall
  temperature in the segment.
- *t* is time.

The heat flow rate from the wall to the gas in the segment is

Qseg,G=UAseg,G(Tseg,wall−Tseg,G),

where:

- *UAseg,G* is the heat transfer
  conductance for the gas in the segment.
- *Tseg,G* is the average
  temperature for the gas in the segment.

The heat flow rate from the wall to the thermal liquid in the segment is

Qseg,TL=UAseg,TL(Tseg,wall−Tseg,TL),

where:

- *UAseg,TL* is the heat transfer
  conductance for the thermal liquid in the segment.
- *Tseg,TL* is the average liquid
  temperature in the segment.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Thermal Liquid Heat Transfer Correlation

The heat transfer conductance on the thermal liquid side of the heat exchanger
is

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN,

where:

- *a*TL,
  *b*TL, and
  *c*TL are the coefficients of
  the Nusselt number correlation. These coefficients are block parameters in
  the **Correlation Coefficients** section.
- *Re*seg,TL is the average Reynolds
  number for the segment.
- *Pr*seg,TL is the average Prandtl
  number for the segment.
- *k*seg,TL is the average thermal
  conductivity for the segment.
- *G*TL is the geometry scale factor
  for the thermal liquid side of the heat exchanger. The block calculates the
  geometry scale factor so that the total heat transfer over all segments
  matches the specified performance at the nominal operating
  conditions.

The average Reynolds number is

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL,

where:

- m˙seg,TL is the mass flow rate through the segment.
- *μ*seg,TL is the average dynamic
  viscosity for the segment.
- *D*ref,TL is an arbitrary
  reference diameter.
- *S*ref,TL is an arbitrary
  reference flow area.

**Note**

The *D*ref,TL and
*S*ref,TL terms are included in this
equation for unit calculation purposes only, to make
*Re*seg,TL nondimensional. The
values of *D*ref,TL and
*S*ref,TL are arbitrary because the
*G*TL calculation overrides these
values.

### Gas Heat Transfer Correlation

The heat transfer conductance on the gas side of the heat exchanger is

UAseg,G=aG(Reseg,G)bG(Prseg,G)cGkseg,GGGN,

where:

- *aG*,
  *bG*, and
  *cG* are the coefficients of
  the Nusselt number correlation. These coefficients are block parameters in
  the **Correlation Coefficients** section.
- *Reseg,G* is the average Reynolds
  number for the segment.
- *Prseg,G* is the average Prandtl
  number for the segment.
- *kseg,G* is the average thermal
  conductivity for the segment.
- *GG* is the geometry scale factor
  for the gas side of the heat exchanger. The block calculates the geometry
  scale factor so that the total heat transfer over all segments matches the
  specified performance at the nominal operating conditions.

The average Reynolds number is

Reseg,G=m˙seg,GDref,Gμseg,GSref,G,

where:

- *ṁseg,G* is the mass flow rate
  through the segment.
- *μseg,G* is the average dynamic
  viscosity for the segment.
- *Dref,G* is an arbitrary reference
  diameter.
- *Sref,G* is an arbitrary reference
  flow area.

**Note**

The *Dref,G* and
*Sref,G* terms are included in
this equation for unit calculation purposes only, to make
*Reseg,G* nondimensional. The
values of *Dref,G* and
*Sref,G* are arbitrary because
the *GG* calculation overrides these
values.

### Pressure Loss

The pressure losses on the thermal liquid side are

pA,TL−pTL=KTL2m˙A,TLm˙2A,TL+m˙2thres,TL2ρavg,TLpB,TL−pTL=KTL2m˙B,TLm˙2B,TL+m˙2thres,TL2ρavg,TL

where:

- *pA,TL* and
  *pB,TL* are the pressures at
  ports **A1** and **B1**,
  respectively.
- *pTL* is internal thermal liquid
  pressure at which the block calculates heat transfer.
- m˙A,TL and m˙B,TL are the mass flow rates into ports **A1**
  and **B1**, respectively.
- *ρavg,TL* is the average thermal
  liquid density over all segments.
- m˙thres,TL is the laminar threshold for pressure loss, approximated
  as 1e-4 of the nominal mass flow rate. The block calculates the pressure
  loss coefficient, *KTL*, so that
  *pA,TL* –
  *pB,TL* matches the nominal
  pressure loss at the nominal mass flow rate.

The pressure losses on the gas side are

pA,G−pG=KG2m˙A,Gm˙2A,G+m˙2thres,G2ρavg,GpB,G−pG=KG2m˙B,Gm˙2B,G+m˙2thres,G2ρavg,G

where:

- *pA,G* and
  *p*B,G are the pressures at
  ports **A2** and **B2**,
  respectively.
- *pG* is the internal gas pressure
  at which the block calculates heat transfer.
- *ṁA,G* and
  *ṁB,G* are the mass flow
  rates into ports **A2** and **B2**,
  respectively.
- *ρavg,G* is the average gas
  density over all segments.
- *ṁthres,G* is the laminar
  threshold for pressure loss, approximated as 1e-4 of the nominal mass flow
  rate. The block calculates the pressure loss coefficient,
  *KG*, so that
  *pA,G* –
  *pB,G* matches the nominal
  pressure loss at the nominal mass flow rate.

### Thermal Liquid Mass and Energy Conservation

The mass conservation for the overall thermal liquid flow is

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL,

where:

- ∂ρseg,TL∂p is the partial derivative of density with respect to
  pressure for the segment.
- ∂ρseg,TL∂T is the partial derivative of density with respect to
  temperature for the segment.
- *T*seg,TL is the temperature for
  the segment.
- *V*TL is the total thermal liquid
  volume.

The summation is over all segments.

**Note**

Although the block divides the thermal liquid flow into *N*=3
segments for heat transfer calculations, it assumes all segments are at the same
internal pressure, *p*TL. Consequently,
*p*TL is outside of the
summation.

The energy conservation equation for each segment is

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL,

where:

- ∂useg,TL∂p is the partial derivative of the specific internal energy
  with respect to pressure for the segment.
- ∂useg,TL∂T is the partial derivative of the specific internal energy
  with respect to temperature for the segment.
- *M*TL is the total thermal liquid
  mass.
- m˙seg,in,TL and m˙seg,out,TL are the mass flow rates into and out of the segment.
- *Φ*seg,in,TL and
  *Φ*seg,out,TL are the energy
  flow rates into and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between the
values of m˙A,TL and m˙B,TL.

### Gas Mass and Energy Conservation

The mass conservation for the overall gas flow is

(dpGdt∑segments(∂ρseg,G∂p)+∑segments(dTseg,Gdt∂ρseg,G∂T))VGN=m˙A,G+m˙B,G,

where:

- ∂ρseg,G∂p is the partial derivative of density with respect to
  pressure for the segment.
- ∂ρseg,G∂T is the partial derivative of density with respect to
  temperature for the segment.
- *Tseg,G* is the temperature for
  the segment.
- *VG* is the total gas
  volume.

The summation is over all segments.

**Note**

Although the block divides the gas flow into *N*=3 segments
for heat transfer calculations, it assumes all segments are at the same internal
pressure, *pG*. Consequently,
*pG* is outside of the
summation.

The energy conservation equation for each segment is

(dpGdt∂useg,G∂p+dTseg,Gdt∂useg,G∂T)MGN+useg,G(m˙seg,in,G−m˙seg,out,G)=Φseg,in,G−Φseg,out,G+Qseg,G,

where:

- ∂useg,G∂p is the partial derivative of the specific internal energy
  with respect to pressure for the segment.
- ∂useg,G∂T is the partial derivative of the specific internal energy
  with respect to temperature for the segment.
- *MG* is the total gas mass.
- *ṁseg,in,G* and
  *ṁseg,out,G* are the mass
  flow rates into and out of the segment.
- *Φseg,in,G* and
  *Φseg,out,G* are the energy
  flow rates into and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between the
values of *ṁA,G* and
*ṁB,G*.
