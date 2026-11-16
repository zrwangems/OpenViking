---
type: simulink-block
title: 'Positive-Displacement Compressor (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'positivedisplacementcompressorma'
documentation_source_path: 'ref/positivedisplacementcompressorma.html'
language: en
---

# Positive-Displacement Compressor (MA)

## Ports

### Conserving

### **A** — Compressor inlet moist air

Moist air conserving port associated with the compressor inlet.

### **B** — Compressor outlet moist air

Moist air conserving port associated with the compressor outlet.

### **C** — Compressor casing mechanical rotational

Mechanical rotational conserving port associated with the compressor case.

### **R** — Compressor shaft mechanical rotational

Mechanical rotational conserving port associated with the compressor shaft.

## Parameters

### Displacement

### **Displacement specification** — Option to specify displacement by volume or nominal conditions `Volumetric displacement` (default) | `Nominal mass flow rate and shaft speed`

Whether to specify the fluid displacement according to volume per cycle or nominal
condition values.

### **Displacement volume** — Displacement volume `130` `cm^3/rev` (default) | positive scalar

Fluid volume displaced per cycle. The block defines a cycle as one compression
stroke and one expansion stroke, which occur during a single crank shaft revolution.
This volume is the difference between the maximum cylinder volume and the clearance
volume, (*Va* —
*Vc*). In general, the displacement volume is the volume swept out by the
compressor over one shaft revolution.

#### Dependencies

To enable this parameter, set **Displacement specification** to
`Volumetric displacement`.

### **Nominal mass flow rate** — Nominal mass flow rate `0.01` `kg/s` (default) | positive scalar

Nominal mass flow rate that the block uses to find the displacement volume.

#### Dependencies

To enable this parameter, set **Displacement specification** to
`Nominal mass flow rate and shaft speed`.

### **Nominal shaft speed** — Nominal shaft speed `1000` `rpm` (default) | positive scalar

Nominal shaft speed that the block uses to find the displacement volume.

#### Dependencies

To enable this parameter, set **Displacement specification** to
`Nominal mass flow rate and shaft speed`.

### Efficiency

The table shows how the options for the **Thermodynamic model** and
**Efficiency specification** parameters affect the availability of
dependent efficiency parameters.

| **Thermodynamic model** | | | |
| --- | --- | --- | --- |
| `Polytropic` | | `Isentropic` | |
| **Efficiency specification** | | **Efficiency specification** | |
| `Analytical` | `Tabulated` | `Analytical` | `Tabulated` |
| **Polytropic exponent** | **Polytropic exponent** | **Isentropic efficiency** | **Isentropic efficiency table, eta\_isen(pr,w)** |
| **Nominal volumetric efficiency** | **Pressure ratio vector, pr** | **Nominal volumetric efficiency** | **Pressure ratio vector, pr** |
| **Shaft speed vector, w** | **Shaft speed vector, w** |
| **Volumetric efficiency table, eta\_vol(pr,w)** | **Volumetric efficiency table, eta\_vol(pr,w)** |

### **Efficiency specification** — Option to parameterize volumetric efficiency analytically or by using tables `Analytical` (default) | `Tabulated`

Whether to parameterize the displacement volumetric efficiency by using analytical
equations or tabulated data.

### **Thermodynamic model** — Thermodynamic model parameterization option `Polytropic` (default) | `Isentropic`

Whether to use a polytropic or isentropic thermodynamic model.

### **Polytropic exponent** — Polytropic exponent `1.2` (default) | positive scalar

Exponent that the block uses when implementing the polytropic pressure-volume
relationship.

#### Dependencies

To enable this parameter, set **Thermodynamic model** to
`Polytropic`.

### **Isentropic efficiency** — Isentropic efficiency `0.65` (default) | positive scalar

Constant efficiency the block uses when implementing the analytical isentropic
pressure-volume relationship.

#### Dependencies

To enable this parameter, set **Thermodynamic model** to
`Isentropic` and **Efficiency
specification** to `Analytical`.

### **Isentropic efficiency table, eta\_isen(pr,w)** — Isentropic efficiency table `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]` (default) | matrix

Efficiencies the block uses when implementing the tabulated isentropic
pressure-volume relationship.

#### Dependencies

To enable this parameter, set **Thermodynamic model** to
`Isentropic` and **Efficiency
specification** to `Tabulated`.

### **Nominal volumetric efficiency** — Nominal volumetric efficiency `0.95` (default) | positive scalar

Nominal volumetric efficiency to compute the clearance volume fraction. The
nominal volumetric efficiency is the volumetric efficiency when the compressor
operates at nominal conditions.

#### Dependencies

To enable this parameter, set **Efficiency specification** to
`Analytical`.

### **Pressure ratio vector, pr** — Pressure ratio vector `[2, 4, 6, 8]` (default) | vector

Vector of pressure ratios that correspond to the compressor volumetric efficiency.
Each element corresponds to a row of the **Volumetric efficiency table,
eta\_vol(pr,w)** parameter. This parameter must be a vector of size
`N`, where `N` is the length of the
**Volumetric efficiency table, eta\_vol(pr,w)** parameter.

#### Dependencies

To enable this parameter, set **Efficiency specification** to
`Tabulated`.

### **Shaft speed vector, w** — Shaft speed vector `[800, 1500, 2800, 3300, 4000]` `rpm` (default) | vector

Vector of shaft speeds that correspond to the compressor volumetric efficiency.
Each element corresponds to a column of the **Volumetric efficiency table,
eta\_vol(pr,w)** parameter. This parameter must be a vector of size
`M`, where `M` is the width of the
**Volumetric efficiency table, eta\_vol(pr,w)** parameter.

#### Dependencies

To enable this parameter, set **Efficiency specification** to
`Tabulated`.

### **Volumetric efficiency table, eta\_vol(pr,w)** — Volumetric efficiency `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]` (default) | matrix

Volumetric efficiency for a given shaft speed and pressure ratio. This parameter
must be a matrix of size `N` by `M`, where
`N` is the length of the **Pressure ratio vector,
pr** parameter and `M` is the length of the
**Shaft speed vector, w** parameter.

#### Dependencies

To enable this parameter, set **Efficiency specification** to
`Tabulated`.

### Nominal Conditions

The table shows how the options for the **Displacement specification**,
**Thermodynamic model**, and **Efficiency
specification** parameters affect the availability of dependent nominal condition
parameters.

This table shows the dependent parameters when you set the **Displacement
specification** parameter to `Volumetric displacement`:

| When the **Displacement specification** parameter is `Volumetric displacement` | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Efficiency specification** | | | | | | | |
| `Analytical` | | | | `Tabulated` | | | |
| **Thermodynamic model** | | | | **Thermodynamic model** | | | |
| `Polytropic` | | `Isentropic` | | `Polytropic` | | `Isentropic` | |
| **Nominal pressure ratio** | | **Nominal pressure ratio** | |  | | **Nominal pressure ratio** | |
| **Nominal inlet pressure** | | **Nominal inlet pressure** | |
| **Nominal inlet temperature** | | **Nominal inlet temperature** | |
| Nominal inlet humidity, water droplet, and trace gas parameters | | Nominal inlet humidity, water droplet, and trace gas parameters | |

When you set **Displacement specification** to `Nominal
mass flow rate and shaft speed`, the parameters in **Nominal
Conditions** do not depend on the **Efficiency specification**
or **Thermodynamic model** parameters.

### **Nominal pressure ratio** — Nominal pressure ratio `5` (default) | positive scalar

Nominal pressure ratio that the block uses to compute the clearance volume
fraction.

#### Dependencies

To enable this parameter, select any parameterization except when
**Displacement specification** is `Volumetric
displacement`, **Thermodynamic model** is
`Polytropic`, and **Efficiency
specification** is `Tabulated`.

### **Nominal inlet pressure** — Nominal inlet pressure `0.101325` `MPa` (default) | positive scalar

Nominal inlet pressure that the block uses to find the displacement volume.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### **Nominal inlet temperature** — Nominal inlet temperature `293.15` `K` (default) | positive scalar

Nominal inlet temperature that the block uses to find the displacement
volume.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### **Inlet humidity specification** — Quantity to use to describe inlet humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Whether to describe the inlet moist air humidity level using the relative
humidity, specific humidity, water vapor mole fraction, or humidity ratio.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### **Nominal inlet relative humidity** — Relative humidity at inlet `0.5` (default) | scalar in the range [0,1]

Moist air relative humidity at the inlet under nominal operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet humidity
  specification** to `Relative
  humidity`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet humidity
  specification** to `Relative
  humidity`.

### **Nominal inlet specific humidity** — Specific humidity at inlet `0.01` (default) | scalar in the range [0,1]

Moist air specific humidity, defined as the mass fraction of water vapor in a
moist air mixture, at the inlet under nominal operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet humidity
  specification** to `Specific
  humidity`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet humidity
  specification** to `Specific
  humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of the water vapor in a moist air mixture at the inlet under nominal
operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet humidity
  specification** to `Mole fraction`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet humidity
  specification** to `Mole fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at inlet `0.01` (default) | scalar in the range [0,1]

Moist air humidity ratio, defined as the mass ratio of water vapor to dry air and
trace gas, at the inlet under nominal operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet humidity
  specification** to `Humidity
  ratio`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet humidity
  specification** to `Humidity
  ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at inlet `287` `K` (default) | positive scalar

Wet-bulb temperature of the moist air mixture at the inlet under nominal operating
conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet humidity
  specification** to `Wet-bulb
  temperature`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet humidity
  specification** to `Wet-bulb
  temperature`.

### **Inlet trace gas specification** — Quantity to use to describe inlet trace gas level `Mass fraction` (default) | `Mole fraction`

Whether to use the mass fraction or mole fraction to describe the trace gas level
at the inlet.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of the trace gas in a moist air mixture at the inlet under nominal
operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet trace gas
  specification** to `Mass fraction`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet trace gas
  specification** to `Mass fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1]

Mole fraction of the trace gas in a moist air mixture at the inlet under nominal
operating conditions.

#### Dependencies

To enable this parameter, either set:

- **Displacement specification** to `Nominal
  mass flow rate and shaft speed` and **Inlet trace gas
  specification** to `Mole fraction`.
- **Displacement specification** to `Volumetric
  displacement`, **Thermodynamic model** to
  `Isentropic`, and **Inlet trace gas
  specification** to `Mole fraction`.

### **Nominal inlet mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Mass ratio of water droplets to moist air at the inlet under nominal operating
conditions.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs in the compressor.

#### Dependencies

To enable this parameter, either set **Displacement
specification** to `Nominal mass flow rate and shaft
speed` or set **Displacement specification** to
`Volumetric displacement` and set **Thermodynamic
model** to `Isentropic`.

### Parameters

### **Mechanical efficiency** — Compressor mechanical efficiency `0.9` (default) | positive scalar

Ratio of the fluid power to the mechanical shaft power.

### **Model water droplets evaporation** — Option to model water droplet evaporation `off` (default) | `on`

Option to model evaporation of water droplets due to temperature change in the
compressor.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs in the compressor.

### **Inlet area at port A** — Inlet area `0.01` `m^2` (default) | positive scalar

Inlet area associated with port **A**.

### **Outlet area at port B** — Outlet area `0.01` `m^2` (default) | positive scalar

Outlet area associated with port **B**.

## Libraries

Simscape / Fluids / Moist Air / Turbomachinery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Model water droplet evaporation

Model water droplet evaporation due to temperature change by using the **Model
water droplets evaporation** parameter.

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To
model water droplets, select **Enable entrained water droplets** in the
Moist Air Properties
(MA) block connected to your moist air network.

## Description

Positive displacement compressor in a moist air network

The Positive-Displacement Compressor (MA) block represents
a positive-displacement compressor, such as a reciprocating piston, rotary screw, rotary vane,
or scroll, in a moist air network. Port **R** and port **C**
are mechanical rotational conserving ports associated with the compressor shaft and casing,
respectively. When there is positive rotation at port **R** with respect to
port **C**, moist air flows from port **A** to port
**B**. The block may not be accurate for reversed flow.

The figure shows the steps of a piston compressor on a P-V diagram, which has these states:

- *a* — The compressor cylinder is full at inlet pressure.
- *b* — The pressure inside the compressor exceeds that of the
  outlet, which results in fluid discharge.
- *c* — The compressor reaches the top of the piston stroke, and only
  the clearance volume remains in the cylinder.
- *d* — The pressure inside the cylinder drops below the inlet
  pressure, which results in fluid intake.

Figure showing piston compressor process where point A is at low pressure, high volume, point B is at high pressure, high volume, port C is at high pressure, low volume, and point d is at low pressure, low volume.

### Mass Flow Rate

The block calculates the mass flow rate as

m˙=ηVωVdispvs,

where:

- *ṁ* is the mass flow rate.
- *ω* is the angular velocity of port **R**
  relative to port **C**.
- *vs* is the specific volume at the inlet.
  The block calculates this value from the nominal inlet conditions.
- *Vdisp* is the displacement volume that
  the block uses.

### Displacement Volume

When you set **Displacement specification** to `Volumetric
displacement`, the block uses the **Displacement volume**
parameter as the value for *Vdisp*.

When you set **Displacement specification** to `Nominal
mass flow rate and shaft speed`, the block calculates the displacement volume
as

Vdisp=m˙nominalvs,nominalωnominalηVnominal,

where:

- *ṁnominal* is the value of the
  **Nominal mass flow rate** parameter.
- *ωnominal* is the value of the
  **Nominal shaft speed** parameter.
- *ηVnominal* is the
  value of the **Nominal volumetric efficiency** parameter when the
  **Efficiency specification** parameter is
  `Analytical`. When the **Volumetric
  efficiency** parameter is `Tabulated`, the block
  uses the `tablelookup` function to
  interpolate *ηVnominal*
  as a function of the shaft speed and the pressure ratio.

### Volumetric Efficiency

You can parameterize the volumetric efficiency by using analytical values or a lookup
table.

**Analytical Volumetric Efficiency**

When you set **Efficiency specification** to
`Analytical`, the block calculates the volumetric efficiency by
using analytical values. When the **Thermodynamic model** parameter is
`Polytropic`, the volumetric efficiency is

ηV=1+C−C(poutpin)1n,

where *pin* and
*pout* are the inlet and outlet pressures,
respectively, and *n* is the value of the **Polytropic
exponent** parameter. The block calculates the clearance volume fraction,
*C*, as

C=1−ηVnominalpratio1/n−1,

where
*ηVnominal* is the value
of the **Nominal volumetric efficiency** parameter and
*pratio* is the value of the **Nominal
pressure ratio** parameter.

When the **Thermodynamic model** parameter is
`Isentropic`, the volumetric efficiency is

ηV=1+C−C(vinvout),

where *vin* and
*vout* are the inlet and outlet specific
volumes, respectively. The block calculates the clearance volume fraction,
*C*, as

C=1-ηVnominalvrnominal-1

where vrnominal=vinnominal/voutnominal is the nominal specific volume ratio. The block calculates this value
from the nominal inlet conditions and the isentropic efficiency.

**Tabulated Volumetric Efficiency**

When you set **Efficiency specification** to
`Tabulated`, the block calculates the volumetric efficiency by
interpolating the values of the **Volumetric efficiency table,
eta\_vol(pr,w)** parameter as a function of the shaft speed and the pressure
ratio.

### Conservation of Mass

When you clear the **Model water droplets evaporation** parameter, the
block conserves mass such that

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where:

- m˙*B* is the mixture mass flow
  rate at port **B**.
- m˙*wA* and m˙*wB* are the water vapor mass
  flow rates at ports **A** and **B**,
  respectively.
- m˙*gA* and m˙*gB* are the trace gas mass
  flow rates at ports **A** and **B**,
  respectively.
- m˙*dA* and m˙*dB* are the mass flow rates
  of the water droplets at ports **A** and **B**,
  respectively.

If you select **Model water droplets evaporation**, the mass balance
equations are

m˙A+m˙B+m˙devap=0m˙wA+m˙wB−m˙devap=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙devap=0

The mass flow rate for the evaporated droplets, m˙*devap*, is

m˙devap=max{m˙A,0}rdevap.

*rdevap* is the mass ratio of
water droplets that can evaporate,

rdevap=min{rdA,xwcapacity},

which depends on *rdA*,
the mass ratio of water droplets to moist air at port **A**.

The capacity of the moist air to hold more water vapor is

xwcapacity=max{xwsB−xwA,0},

where *xwsB* is the
specific humidity at saturation, and
*xwA* is the specific
humidity.

### Conservation of Energy

The block conserves energy such that

ϕA+ϕB+m˙AΔht=0,

where *Δht* is the change in
specific total enthalpy and
*ṁAΔht* is the fluid power,
which is equal to the mechanical power, *torque\*ω*.

When the **Thermodynamic model** parameter is
`Polytropic`, the fluid power is

W˙c=ωnn−1ηVpinVdisp[(pinpout)n−1n−1],

where the block uses the polytropic relationship pvn=constant to relate *pin*,
*pout*,
*vin*, and
*vout*.

When the **Thermodynamic model** parameter is
`Isentropic`, the fluid power is

W˙C=m˙AΔht.

The block calculates *Δht* from
the isentropic efficiency, *ηisen*. When the
**Efficiency specification** parameter is
`Analytical`, *ηisen* is
equal to the value of the **Isentropic efficiency** parameter. When the
**Efficiency specification** parameter is
`Tabulated`, the block calculates
*ηisen* by interpolating the values of the
**Isentropic efficiency table, eta\_isen(pr,w)** parameter as a function
of the pressure ratio and the shaft speed.

### Visualizing the Volumetric Efficiency

To visualize the block volumetric efficiency, right-click the block and select **Fluids** > **Plot Volumetric Efficiency**.

Each time you modify the block settings, click **Reload Data** in the
figure window.

When you set **Efficiency specification** to
`Analytical` and **Thermodynamic model** to
`Polytropic`, the block plots the compressor volumetric
efficiency against the pressure ratio.

Volumetric Efficiency

When you set **Efficiency specification** to
`Analytical` and **Thermodynamic model** to
`Isentropic`, the block plots the compressor volumetric
efficiency against the pressure ratio at *Tout nom*,
the nominal outlet temperature.

Volumetric Efficiency

When you set **Efficiency specification** to
`Tabulated`, the block plots the compressor volumetric efficiency
against the pressure ratio for each element in the **Shaft speed vector,
w** parameter.

Volumetric Efficiency

### Assumptions and Limitations

- The block may not be accurate for flow from port **B** to port
  **A**.
- The block assumes that the flow is quasi-steady. The compressor does not accumulate
  mass.
