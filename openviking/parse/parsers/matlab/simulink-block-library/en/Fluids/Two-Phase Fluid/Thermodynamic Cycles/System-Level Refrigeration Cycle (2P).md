---
type: simulink-block
title: 'System-Level Refrigeration Cycle (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Thermodynamic Cycles'
documentation_page: 'systemlevelrefrigerationcycle2p'
documentation_source_path: 'ref/systemlevelrefrigerationcycle2p.html'
language: en
---

# System-Level Refrigeration Cycle (2P)

## Ports

### Input

### **S** — Signal that operates compressor, unitless physical signal

Physical signal input that operates the compressor. A value of
`0` means the compressor is off. A value of
`1` means the compressor is operating at the
nominal capacity.
### Conserving

### **F** — Refrigerant properties two-phase fluid

Two-phase fluid conserving port associated with the refrigerant
properties. Connect a Two-Phase Fluid Properties
(2P) or Two-Phase Fluid Predefined
Properties (2P) block to this port. Do not connect
any other Two-Phase Fluid blocks to port **F** because
this port acts as an absolute reference.

### **Ac** — Condenser external fluid inlet gas | moist air | thermal liquid | two-phase fluid

Gas, moist air, thermal liquid, or two-phase fluid conserving port associated with the
condenser external fluid inlet. The block assumes that the condenser
external fluid flows from port **Ac** to port
**Bc**. The **External fluid for condenser
heat transfer** parameter controls the port fluid.

### **Bc** — Condenser external fluid outlet gas | moist air | thermal liquid | two-phase fluid

Gas, moist air, thermal liquid, or two-phase fluid conserving port associated with the
condenser external fluid outlet. The block assumes that the condenser
external fluid flows from port **Ac** to port
**Bc**. The **External fluid for condenser
heat transfer** parameter controls the port fluid.

### **Ae** — Evaporator external fluid inlet gas | moist air | thermal liquid | two-phase fluid

Gas, moist air, thermal liquid, or two-phase fluid conserving port associated with the
evaporator external fluid inlet. The block assumes that the evaporator
external fluid flows from port **Ae** to port
**Be**. The **External fluid for evaporator
heat transfer** parameter controls the port fluid.

### **Be** — Evaporator external fluid outlet gas | moist air | thermal liquid | two-phase fluid

Gas, moist air, thermal liquid, or two-phase fluid conserving port associated with the
evaporator external fluid outlet. The block assumes that the evaporator
external fluid flows from port **Ae** to port
**Be**. The **External fluid for evaporator
heat transfer** parameter controls the port fluid.
### Output

### **Qc** — Heat rejected in condenser, W physical signal

Physical signal output port that measures the heat rejected by the refrigerant in the
condenser, in W.

### **Qe** — Heat absorbed in evaporator, W physical signal

Physical signal output port that measures the heat absorbed by the refrigerant in the
evaporator, in W.

### **Pwr** — Mechanical power consumed by the compressor, W physical signal

Physical signal output port that measures the mechanical power consumed by the
compressor, in W.

### **W** — Rate of condensation in evaporator, kg/s physical signal

Physical signal output port that measures rate of condensation in the evaporator
external fluid, in kg/s, if the **External fluid for evaporator
heat transfer** parameter is `Moist
air`. If the **External fluid for evaporator
heat transfer** parameter is not moist air, this port
outputs `0`. The value of this port does not include
the portion of condensation that is entrained as water droplets.

## Parameters

### Refrigeration Cycle

### **Capacity specification** — Method for specifying size of system `Cooling load` (default) | `Heating load` | `Refrigerant mass flow rate`

Method for specifying the size of the system. You can specify the
cooling load, heating load, or the refrigerant mass flow rate.

### **Nominal condenser heat transfer** — Rate of heat transfer in condenser `15` `kW` (default) | positive scalar

Rate of heat transfer from the refrigerant to the external fluid in
the condenser.

#### Dependencies

To enable this parameter, set **Capacity
specification** to `Heating
load`.

### **Nominal evaporator heat transfer** — Rate of heat transfer in evaporator `15` `kW` (default) | positive scalar

Rate of heat transfer from the external fluid to the refrigerant in
the evaporator.

#### Dependencies

To enable this parameter, set **Capacity
specification** to `Cooling
load`.

### **Nominal mass flow rate** — Refrigerant mass flow rate `0.005` `kg/s` (default) | positive scalar

Refrigerant mass flow rate through the cycle.

#### Dependencies

To enable this parameter, set **Capacity
specification** to `Refrigerant mass flow
rate`.

### **Pressure specification** — Method for specifying condenser and evaporator pressure `Specified pressure` (default) | `Pressure at specified saturation temperature`

Method for providing condenser and evaporator pressures. Select
whether to directly provide the pressures or provide the corresponding
saturation temperatures.

### **Nominal condenser pressure** — Refrigerant pressure in condenser `1` `MPa` (default) | positive scalar

Pressure of refrigerant in the condenser.

#### Dependencies

To enable this parameter, set **Pressure
specification** to `Specified
pressure`.

### **Nominal evaporator pressure** — Refrigerant pressure in evaporator `0.1` `MPa` (default) | positive scalar

Pressure of refrigerant in the evaporator.

#### Dependencies

To enable this parameter, set **Pressure
specification** to `Specified
pressure`.

### **Nominal condensing (saturation) temperature** — Condenser refrigerant saturation temperature `333.15` `K` (default) | positive scalar

Saturation temperature of refrigerant in the condenser.

#### Dependencies

To enable this parameter, set **Pressure
specification** to `Pressure at specified
saturation temperature`.

### **Nominal evaporating (saturation) temperature** — Evaporator refrigerant saturation temperature `273.15` `K` (default) | positive scalar

Saturation temperature of refrigerant in the evaporator.

#### Dependencies

To enable this parameter, set **Pressure
specification** to `Pressure at specified
saturation temperature`.

### **Nominal condenser subcooling** — Operational condenser outlet temperature differential `5` `deltaK` (default) | positive scalar

Degrees of temperature below saturation temperature at the condenser
outlet.

### **Nominal (static + opening) evaporator superheat** — Operational evaporator outlet temperature differential `10` `deltaK` (default) | positive scalar

Degrees of temperature above saturation temperature at the evaporator
outlet. The expansion valve adjusts its valve area to try to maintain
this superheat.

### **Static (minimum) evaporator superheat** — Minimum allowable temperature differential at evaporator outlet `5` `deltaK` (default) | positive scalar

Superheat threshold to close the expansion valve.

### **Performance specification** — Method to specify refrigeration cycle efficiency `Coefficient of performance for cooling` (default) | `Coefficient of performance for heating` | `Compressor isentropic efficiency`

Method to specify the refrigeration cycle efficiency. Choose based on the coefficient of
performance of the cycle for heating, cooling, or the compressor
efficiency.

### **Coefficient of performance at nominal conditions** — Ratio of cooling or heating to power consumed for compressor `3` (default) | positive scalar

Ratio of useful cooling or heating by the refrigeration cycle to the
power consumed by the compressor.

#### Dependencies

To enable this parameter, set **Performance
specification** to `Coefficient of
performance for cooling` or
`Coefficient of performance for
heating`.

### **Compressor isentropic efficiency** — Ratio of ideal-to-actual change in specific enthalpy across compressor `0.8` (default) | positive scalar

Ratio of ideal, or isentropic, change in specific enthalpy to the
actual change in specific enthalpy across the compressor.

#### Dependencies

To enable this parameter, set **Performance
specification** to `Compressor isentropic
efficiency`.

### **Compressor volumetric efficiency at nominal conditions** — Ratio of volumetric flow rate to displacement rate `0.95` (default) | positive scalar

Ratio of actual volumetric flow rate to the displacement rate of the
compressor.

### **Compressor mechanical efficiency** — Efficiency of conversion to torque `0.95` (default) | positive scalar

Ratio of the power delivered to the fluid flow to the power driving
the mechanical shaft.

### **Ratio of maximum to nominal expansion valve opening** — Ratio of open valve areas to maintain superheat `1.5` (default) | positive scalar

Ratio of the fully opened valve area to the valve area needed to
maintain superheat at nominal conditions.

### **Ratio of leakage to nominal expansion valve opening** — Ratio of closed valve areas to maintain superheat `1e-6` (default) | positive scalar

Ratio of the closed valve area to the valve area needed to maintain
superheat at nominal conditions

### **Expansion valve smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Smoothing factor that introduces a layer of gradual change to the flow
response when the valve is in near-open or near-closed positions. Set
this value to a nonzero value less than one to increase the stability of
your simulation in these regimes.

### **Condenser refrigerant volume** — Volume of condenser refrigerant `0.001` `m^3` (default) | positive scalar

Volume of refrigerant in the condenser.

### **Evaporator refrigerant volume** — Volume of evaporator refrigerant `0.001` `m^3` (default) | positive scalar

Volume of refrigerant in the evaporator.

### **Liquid receiver tank volume** — Volume of liquid and vapor phases in receiver tank `0.01` `m^3` (default) | positive scalar

Total physical volume of liquid receiver tank, including both the volume of liquid and
vapor phases.

### **Initial receiver liquid level** — Initial liquid volume fraction in tank `0.5` (default) | positive scalar

Liquid volume fraction in the receiver tank at the start of simulation.

### **Initialize refrigerant to nominal operating conditions** — Whether to specify refrigerant initial conditions `on` (default) | `off`

Whether refrigerant in the cycle starts simulation at the nominal
operating conditions based on the nominal operating parameters or
specified explicitly with initial condition parameters.

### **Initial condenser pressure** — Initial refrigerant pressure in condenser `1` `MPa` (default) | positive scalar

Pressure of the refrigerant in the condenser and liquid receiver at
the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** check
box.

### **Initial evaporator pressure** — Initial refrigerant pressure in evaporator `0.1` `MPa` (default) | positive scalar

Pressure of the refrigerant in the evaporator at the start of
simulation.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** check
box.

### **Initial condenser specific enthalpy [inlet, outlet]** — Initial refrigerant specific energy in condenser `[450, 250]` `kJ/kg` (default) | positive scalar | two-element vector

Specific enthalpy of the refrigerant in the condenser at the start of simulation. If you
specify this parameter as a vector of two values, the first element is
the inlet specific enthalpy value and the second element is the outlet
specific enthalpy value. If you enter a scalar, the block assumes that
the inlet and outlet specific enthalpy are the same value.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** check
box.

### **Initial evaporator specific enthalpy [inlet, outlet]** — Initial refrigerant specific energy in evaporator `[250, 400]` `kJ/kg` (default) | positive scalar | two-element vector

Specific enthalpy of the refrigerant in the evaporator at the start of simulation. If
you specify this parameter as a vector of two values, the first element
is the inlet specific enthalpy value and the second element is the
outlet specific enthalpy value. If you enter a scalar, the block assumes
that the inlet and outlet specific enthalpy are the same value.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** check
box.

### **Initial receiver liquid and vapor fully saturated** — Whether to specify receiver initial conditions `on` (default) | `off`

Whether the receiver starts the simulation at the saturation
equilibrium, meaning the liquid and vapor volumes are both at the
saturated state, or uses explicitly specified initial conditions.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** check
box.

### **Initial receiver liquid specific enthalpy** — Receiver initial liquid specific enthalpy `500` `kJ/kg` (default) | positive scalar

Specific enthalpy of the liquid portion of the refrigerant in the
receiver at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** and
**Initial receiver liquid and vapor fully
saturated** check boxes.

### **Initial receiver vapor specific enthalpy** — Receiver initial vapor specific enthalpy `3500` `kJ/kg` (default) | positive scalar

Specific enthalpy of the vapor portion of the refrigerant in the
receiver at the start of simulation.

#### Dependencies

To enable this parameter, clear the **Initialize
refrigerant to nominal operating conditions** and
**Initial receiver liquid and vapor fully
saturated** check boxes.

### Condenser External Fluid

### **External fluid for condenser heat transfer** — External fluid for heat transfer in condenser `Moist air` (default) | `Gas` | `Thermal liquid` | `Two-phase fluid`

External fluid for heat transfer in the condenser.

### **Nominal mass flow rate** — Mass flow rate between condenser ports `0.5` `kg/s` (default) | positive scalar

Mass flow rate from port **Ac** to port
**Bc** during nominal operating conditions.

### **Nominal pressure drop** — Pressure drop between condenser ports `0.001` `MPa` (default) | positive scalar

Pressure drop from port **Ac** to port
**Bc** during nominal operating conditions.

### **Pressure specification** — Method of pressure specification `Specified pressure` (default) | `Pressure at specified saturation temperature`

Method of pressure specification:

- `Specified pressure` — Specify
  the nominal inlet pressure.
- `Pressure at specified saturation
  temperature` — Specify the nominal
  saturation temperature that corresponds to the inlet
  pressure.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`.

### **Nominal inlet pressure** — Pressure at external fluid side inlet of condenser `0.101325` `MPa` (default) | positive scalar

Pressure at the inlet of the condenser on the external fluid side of
the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set either:

- **External fluid for condenser heat
  transfer** to
  `Gas`, `Moist
  air`, or `Thermal
  liquid`.
- **External fluid for condenser heat
  transfer** to `Two-phase
  fluid`, and set **Pressure
  specification** to `Specific
  pressure`.

### **Nominal saturation temperature** — Nominal saturation temperature to specify pressure `400` `K` (default) | positive scalar

Saturation temperature at the outlet of the condenser external fluid
side of the heat exchanger during the nominal operating condition. The
pressure in the condenser is the corresponding saturation
pressure.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid` and **Pressure
specification** to `Pressure at specified
saturation temperature`.

### **Inlet condition specification** — Method to describe inlet condition of fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality`

Method the block uses to describe the inlet condition of the condenser
external fluid at the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`.

### **Nominal inlet temperature** — Temperature at condenser external fluid side inlet `400` `K` (default) | positive scalar

Temperature at the inlet of the external fluid side of the condenser
during the nominal operating condition.

#### Dependencies

To enable this parameter, set either:

- **External fluid for condenser heat
  transfer** to
  `Gas`.
- **External fluid for condenser heat
  transfer** to `Two-phase
  fluid` and **Initial condition
  specification** to
  `Temperature`.

### **Nominal inlet specific enthalpy** — Specific enthalpy at condenser external fluid side inlet `500` `kJ/kg` (default) | positive scalar

Specific enthalpy at the inlet of the external fluid side of the
condenser during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid` and **Initial condition
specification** to `Specific
enthalpy`.

### **Nominal inlet vapor quality** — Vapor quality at condenser external fluid side inlet `1` (default) | positive scalar

Vapor quality, defined as the mass fraction of vapor in a liquid-vapor
mixture, at the inlet of the external fluid side of the condenser during
the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid` and **Initial condition
specification** to `Vapor
quality`.

### **Inlet humidity specification** — Method to describe humidity level at condenser external fluid side inlet `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method the block uses to describe the humidity level at the inlet
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### **Nominal inlet relative humidity** — Relative humidity at inlet `0.1` (default) | scalar in the range [0,1]

Relative humidity at the inlet of the external fluid side of the
condenser during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet humidity
specification** to `Relative
humidity`.

### **Nominal inlet specific humidity** — Specific humidity at inlet `0.01` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a
moist air mixture, at the inlet of the external fluid side of the
condenser during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet humidity
specification** to `Specific
humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of the water vapor in a moist air mixture at the inlet
of the external fluid side of the condenser during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet humidity
specification** to `Mole
fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at inlet `0.01` (default) | scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air
and trace gas, at the inlet of the external fluid side of the condenser
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet humidity
specification** to `Humidity
ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the inlet of the external fluid side of the
condenser during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet humidity
specification** to `Wet-bulb
temperature`.

### **Inlet trace gas specification** — Method to describe trace gas level at inlet `Mass fraction` (default) | `Mole fraction`

Method the block uses to describe the trace gas level at the external
fluid side inlet of the condenser during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of trace gas in a moist air mixture at the inlet of the
external fluid side of the condenser during the nominal operating
condition.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet trace gas
specification** to `Mass
fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at inlet `0.001` (default) | scalar in the range [0,1]

Mole fraction of the trace gas in a moist air mixture at the inlet of
the external fluid side of the condenser during the nominal operating
condition.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and **Inlet trace gas
specification** to `Mole
fraction`.

### **External fluid volume** — Volume of fluid in condenser `0.1` `m^3` (default) | positive scalar

Total volume of external fluid in the condenser.

### **Cross-sectional area at port Ac** — Flow area at port Ac `0.01` `m^2` (default) | positive scalar

Flow area at the condenser external fluid port
**Ac**.

### **Cross-sectional area at port Bc** — Flow area at port Bc `0.01` `m^2` (default) | positive scalar

Flow area at the condenser external fluid port
**Bc**.

### **Enable condenser wall thermal mass** — Option to model condenser wall heat transfer `Off` (default) | `On`

Whether to include the temperature dynamics of the heat transfer
surface.

### **Condenser wall mass** — Condenser heat transfer mass `1` `kg` (default) | positive scalar

Total mass of the condenser heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable condenser wall thermal
mass**.

### **Condenser wall specific heat** — Specific heat of condenser transfer surface `490` `J/(K*kg)` (default) | positive scalar

Specific heat of the condenser heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable condenser wall thermal
mass**.

### **Initialize to nominal operating conditions** — Whether to specify condenser initial conditions `On` (default) | `Off`

Whether to start the simulation at the nominal operating condition or
specify a different set of initial conditions using additional
parameters.

### **Initial pressure** — Fluid pressure at start of simulation `0.101325` `MPa` (default) | positive scalar

Condenser external fluid pressure at the start of the
simulation.

#### Dependencies

To enable this parameter, clear the **Initialize to
nominal operating conditions** check box.

### **Initial fluid energy specification** — Initial state of the condenser external fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

Quantity used to describe the initial state of the condenser external
fluid.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid` and clear the **Initialize to
nominal operating conditions** check box.

### **Initial temperature** — Temperature at start of simulation `293.15` `K` (default) | positive scalar | two-element vector

Temperature at the start of simulation. If the value is a scalar, then
the block assumes that the initial temperature is uniform. If the value
is a two-element vector, then the block assumes that the initial
temperature varies linearly between the ports condenser ports, with the
first element corresponding to port **Ac** and the
second element corresponding to port **Bc**.

#### Dependencies

To enable this parameter, set either:

- **External fluid for condenser heat
  transfer** to
  `Gas`, `Moist
  air`, or `Thermal
  liquid` and clear the
  **Initialize to nominal operating
  conditions** check box.
- **External fluid for condenser heat
  transfer** to `Two-phase
  fluid`, clear the **Initialize
  to nominal operating conditions** check
  box, and set **Initial fluid energy
  specification** to
  `Temperature`.

### **Initial vapor quality** — Vapor mass fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Condenser external fluid vapor quality, defined as the mass fraction
of vapor in a liquid-vapor mixture, at the start of simulation. If the
value is a scalar, then the block assumes that the initial vapor quality
is uniform. If the value is a two-element vector, then the block assumes
that the initial vapor quality varies between the condenser ports, with
the first element corresponding to port **Ac** and the
second element corresponding to port **Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Vapor quality`.

### **Initial vapor void fraction** — Vapor volume fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Condenser external fluid vapor void fraction, defined as the volume
fraction of vapor in a liquid-vapor mixture, at the start of simulation.
If the value is a scalar, then the block assumes that the initial vapor
void fraction is uniform. If the value is a two-element vector, then the
block assumes that the initial vapor void quality varies between the
condenser ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Vapor void fraction`.

### **Initial specific enthalpy** — Enthalpy per unit mass at start of simulation `1500` `kJ/kg` (default) | positive scalar | two-element vector

Condenser external fluid specific enthalpy at the start of simulation.
If the value is a scalar, then the block assumes that the initial
specific enthalpy is uniform. If the value is a two-element vector, then
the block assumes that the initial specific enthalpy varies between the
condenser ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Specific enthalpy`.

### **Initial specific internal energy** — Internal energy per unit mass at start of simulation `1500` `kJ/kg` (default) | positive scalar | two-element vector

Condenser external fluid specific internal energy at the start of
simulation. If the value is a scalar, then the block assumes that the
initial specific internal energy is uniform. If the value is a
two-element vector, then the block assumes that the initial specific
internal energy varies between the condenser ports, with the first
element corresponding to port **Ac** and the second
element corresponding to port **Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Specific internal energy`.

### **Initial humidity specification** — Method used to describe initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method used to describe the initial humidity level in condenser
external fluid.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Condenser external fluid relative humidity at the start of simulation.
If the value is a scalar, then the block assumes that the initial
relative humidity is uniform. If the value is a two-element vector, then
the block assumes that the initial relative humidity varies linearly
between the ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial humidity specification** to
`Relative humidity`.

### **Initial specific humidity** — Specific humidity at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Condenser external fluid specific humidity, defined as the mass
fraction of water vapor in a moist air mixture, at the start of
simulation. If the value is a scalar, then the block assumes that the
initial specific humidity is uniform. If the value is a two-element
vector, then the block assumes that the initial specific humidity varies
linearly between the ports, with the first element corresponding to port
**Ac** and the second element
corresponding to port **Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial humidity specification** to
`Specific humidity`.

### **Initial water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of the water vapor in the condenser external fluid at
the start of simulation. If the value is a scalar, then the block
assumes that the initial water vapor mole fraction is uniform. If the
value is a two-element vector, then the block assumes that the initial
water vapor mole fraction varies linearly between the ports, with the
first element corresponding to port **Ac** and the
second element corresponding to port **Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial humidity specification** to
`Mole fraction`.

### **Initial humidity ratio** — Humidity ratio at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Condenser external fluid humidity ratio, defined as the mass ratio of
water vapor to dry air and trace gas, at the start of simulation. If the
value is a scalar, then the block assumes that the initial humidity
ratio is uniform. If the value is a two-element vector, then the block
assumes that the initial humidity ratio varies linearly between the
ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial humidity specification** to
`Humidity ratio`.

### **Initial moist air wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Condenser wet-bulb temperature at the start of the simulation.

If the value is a scalar, then the block assumes that the initial
wet-bulb temperature is uniform. If the value is a two-element vector,
then the block assumes that the initial wet-bulb temperature varies
linearly between the ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial humidity specification** to
`Wet-bulb temperature`.

### **Initial trace gas specification** — Method to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Method used to describe the trace gas level at the start of
simulation.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial trace gas mass fraction** — Mass fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mass fraction of trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the block assumes that the
initial mass fraction is uniform. If the value is a two-element vector,
then the block assumes that the initial mass fraction varies linearly
between the ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial trace gas specification** to
`Mass fraction`.

### **Initial trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of the trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the block assumes that the
initial mole fraction is uniform. If the value is a two-element vector,
then the block assumes that the initial mole fraction varies linearly
between the ports, with the first element corresponding to port
**Ac** and the second element corresponding to port
**Bc**.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial trace gas specification** to
`Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial condenser wall temperature** — Condenser surface temperature at simulation start `293.15` `K` (default) | positive scalar | two-element vector

Heat transfer surface temperature at the start of simulation. If this
value is a scalar, the block assumes that the initial temperature is
uniform. If this value is a two-element vector, then the block assumes
that the temperature varies linearly between ports
**Ac** and **Bc** with the first
element corresponding to **Ac** and second element
corresponding to **Bc**.

#### Dependencies

To enable this parameter, clear the **Initialize to nominal operating
conditions** and **Enable condenser wall
thermal mass** check boxes.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | nonnegative scalar

Relative humidity point of condensation. Condensation occurs above
this value. In most cases, this value is 1, which is equivalent to 100%.
A value greater than 1 indicates a supersaturated vapor.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume returns to
saturation by condensing out excess humidity.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

#### Dependencies

To enable this parameter, set **External fluid for
condenser heat transfer** to `Moist
air`.

### Evaporator External Fluid

### **External fluid for evaporator heat transfer** — External fluid for heat transfer in evaporator `Moist air` (default) | `Gas` | `Thermal liquid` | `Two-phase fluid`

External fluid for heat transfer in the evaporator.

### **Nominal mass flow rate** — Mass flow rate between evaporator ports `0.5` `kg/s` (default) | positive scalar

Mass flow rate from port **Ae** to port
**Be** during nominal operating conditions.

### **Nominal pressure drop** — Pressure drop between evaporator ports `0.001` `MPa` (default) | positive scalar

Pressure drop from port **Ae** to port
**Be** during nominal operating conditions.

### **Pressure specification** — Method of pressure specification `Specified pressure` (default) | `Pressure at specified saturation temperature`

Method of pressure specification:

- `Specified pressure` — Specify
  the nominal inlet pressure.
- `Pressure at specified saturation
  temperature` — Specify the nominal
  saturation temperature that corresponds to the inlet
  pressure.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`.

### **Nominal inlet pressure** — Pressure at external fluid side inlet of evaporator `0.101325` `MPa` (default) | positive scalar

Pressure at the inlet of the evaporator on the external fluid side of
the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set either:

- **External fluid for evaporator heat
  transfer** to
  `Gas`, `Moist
  air`, or `Thermal
  liquid`.
- **External fluid for evaporator heat
  transfer** to `Two-phase
  fluid`, and set **Pressure
  specification** to `Specific
  pressure`.

### **Nominal saturation temperature** — Nominal saturation temperature to specify pressure `400` `K` (default) | positive scalar

Saturation temperature at the outlet of the evaporator external fluid side of the heat
exchanger during the nominal operating condition. The pressure in the
evaporator is the corresponding saturation pressure.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid` and **Pressure
specification** to `Pressure at specified
saturation temperature`.

### **Inlet condition specification** — Method to describe inlet condition of fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality`

Method the block uses to describe the inlet condition of the
evaporator external fluid at the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`.

### **Nominal inlet temperature** — Temperature at evaporator external fluid side inlet `400` `K` (default) | positive scalar

Temperature at the inlet of the external fluid side of the evaporator during the nominal
operating condition.

#### Dependencies

To enable this parameter, set either:

- **External fluid for evaporator heat
  transfer** to
  `Gas`.
- **External fluid for evaporator heat
  transfer** to `Two-phase
  fluid` and **Initial condition
  specification** to
  `Temperature`.

### **Nominal inlet specific enthalpy** — Specific enthalpy at evaporator external fluid side inlet `500` `kJ/kg` (default) | positive scalar

Specific enthalpy at the inlet of the external fluid side of the evaporator during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid` and **Initial condition
specification** to `Specific
enthalpy`.

### **Nominal inlet vapor quality** — Vapor quality at evaporator external fluid side inlet `1` (default) | positive scalar

Vapor quality, defined as the mass fraction of vapor in a liquid-vapor mixture, at the
inlet of the external fluid side of the evaporator during the nominal
operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid` and **Initial condition
specification** to `Vapor
quality`.

### **Inlet humidity specification** — Method to describe humidity level at evaporator external fluid side inlet `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method the block uses to describe the humidity level at the inlet
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air`.

### **Nominal inlet relative humidity** — Relative humidity at inlet `0.1` (default) | scalar in the range [0,1]

Relative humidity at the inlet of the external fluid side of the evaporator during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air` and
**Inlet humidity specification** to
`Relative humidity`.

### **Nominal inlet specific humidity** — Specific humidity at inlet `0.01` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a moist air mixture,
at the inlet of the external fluid side of the evaporator during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air` and
**Inlet humidity specification** to
`Specific humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at the inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of the water vapor in a moist air mixture at the inlet of the external
fluid side of the evaporator during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air` and
**Inlet humidity specification** to
`Mole fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at inlet `0.01` (default) | scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air
and trace gas, at the inlet of the external fluid side of the evaporator
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air` and
**Inlet humidity specification** to
`Humidity ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Evaporator wet-bulb temperature in a moist air mixture at the inlet of
the external fluid side of the evaporator during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air` and
**Inlet humidity specification** to
`Wet-bulb temperature`.

### **Inlet trace gas specification** — Method to describe trace gas level at inlet `Mass fraction` (default) | `Mole fraction`

Method the block uses to describe the trace gas level at the external fluid side inlet
of the evaporator during the nominal operating condition.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of the trace gas in a moist air mixture at the inlet of the external fluid
side of the evaporator during the nominal operating condition.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air` and **Inlet trace gas
specification** to `Mass
fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at inlet `0.001` (default) | scalar in the range [0,1]

Mole fraction of the trace gas in a moist air mixture at the inlet of the external fluid
side of the evaporator during the nominal operating condition.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air` and **Inlet trace gas
specification** to `Mole
fraction`.

### **External fluid volume** — Volume of fluid in evaporator `0.1` `m^3` (default) | positive scalar

Total volume of external fluid in the evaporator.

### **Cross-sectional area at port Ae** — Flow area at port Ae `0.01` `m^2` (default) | positive scalar

Flow area at the evaporator external fluid port
**Ae**.

### **Cross-sectional area at port Be** — Flow area at port Be `0.01` `m^2` (default) | positive scalar

Flow area at the evaporator external fluid port
**Be**.

### **Enable evaporator wall thermal mass** — Option to model evaporator wall heat transfer `Off` (default) | `On`

Whether to include the temperature dynamics of the heat transfer
surface.

### **Evaporator wall mass** — Evaporator heat transfer mass `1` `kg` (default) | positive scalar

Total mass of the evaporator heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable evaporator wall thermal
mass**.

### **Evaporator wall specific heat** — Specific heat of evaporator transfer surface `490` `J/(K*kg)` (default) | positive scalar

Specific heat of the evaporator heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable evaporator wall thermal
mass**.

### **Initialize to nominal operating conditions** — Whether to specify evaporator initial conditions `On` (default) | `Off`

Whether to start the simulation at the nominal operating condition or
specify a different set of initial conditions using additional
parameters.

### **Initial pressure** — Fluid pressure at start of simulation `0.101325` `MPa` (default) | positive scalar

Evaporator external fluid pressure at the start of the
simulation.

#### Dependencies

To enable this parameter, clear the **Initialize to
nominal operating conditions** check box.

### **Initial fluid energy specification** — Initial state of the evaporator external fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

Quantity used to describe the initial state of the evaporator external
fluid.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid` and clear the **Initialize to
nominal operating conditions** check box.

### **Initial temperature** — Temperature at start of simulation `293.15` `K` (default) | positive scalar | two-element vector

Temperature at the start of simulation. If the value is a scalar, then
the block assumes that the initial temperature is uniform. If the value
is a two-element vector, then the block assumes that the initial
temperature varies linearly between the ports evaporator ports, with the
first element corresponding to port **Ae** and the
second element corresponding to port **Be**.

#### Dependencies

To enable this parameter, set either:

- **External fluid for evaporator heat
  transfer** to
  `Gas`, `Moist
  air`, or `Thermal
  liquid` and clear the
  **Initialize to nominal operating
  conditions** check box.
- **External fluid for evaporator heat
  transfer** to `Two-phase
  fluid`, clear the **Initialize
  to nominal operating conditions** check
  box, and set **Initial fluid energy
  specification** to
  `Temperature`.

### **Initial vapor quality** — Vapor mass fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Evaporator external fluid vapor quality, defined as the mass fraction
of vapor in a liquid-vapor mixture, at the start of simulation. If the
value is a scalar, then the block assumes that the initial vapor quality
is uniform. If the value is a two-element vector, then the block assumes
that the initial vapor quality varies between the evaporator ports, with
the first element corresponding to port **Ae** and the
second element corresponding to port **Be**.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Vapor quality`.

### **Initial vapor void fraction** — Vapor volume fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Evaporator external fluid vapor void fraction, defined as the volume fraction of vapor
in a liquid-vapor mixture, at the start of simulation. If the value is a
scalar, then the block assumes that the initial vapor void fraction is
uniform. If the value is a two-element vector, then the block assumes
that the initial vapor void quality varies between the evaporator ports,
with the first element corresponding to port **Ae** and
the second element corresponding to port **Be**.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Vapor void fraction`.

### **Initial specific enthalpy** — Enthalpy per unit mass at start of simulation `1500` `kJ/kg` (default) | positive scalar | two-element vector

Evaporator external fluid specific enthalpy at the start of
simulation. If the value is a scalar, then the block assumes that the
initial specific enthalpy is uniform. If the value is a two-element
vector, then the block assumes that the initial specific enthalpy varies
between the evaporator ports, with the first element corresponding to
port **Ae** and the second element corresponding to
port **Be**.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Specific enthalpy`.

### **Initial specific internal energy** — Internal energy per unit mass at start of simulation `1500` `kJ/kg` (default) | positive scalar | two-element vector

Evaporator external fluid specific internal energy at the start of
simulation. If the value is a scalar, then the block assumes that the
initial specific internal energy is uniform. If the value is a
two-element vector, then the block assumes that the initial specific
internal energy varies between the evaporator ports, with the first
element corresponding to port **Ae** and the second
element corresponding to port **Be**.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`, clear the **Initialize to nominal
operating conditions** check box, and set
**Initial fluid energy specification** to
`Specific internal energy`.

### **Initial humidity specification** — Method used to describe initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method used to describe the initial humidity level in evaporator
external fluid.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Evaporator external fluid relative humidity at the start of
simulation. If the value is a scalar, then the block assumes that the
initial relative humidity is uniform. If the value is a two-element
vector, then the block assumes that the initial relative humidity varies
linearly between the ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial
humidity specification** to `Relative
humidity`.

### **Initial specific humidity** — Specific humidity at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Evaporator external fluid specific humidity, defined as the mass
fraction of water vapor in a moist air mixture, at the start of
simulation. If the value is a scalar, then the block assumes that the
initial specific humidity is uniform. If the value is a two-element
vector, then the block assumes that the initial specific humidity varies
linearly between the ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial
humidity specification** to `Specific
humidity`.

### **Initial water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of the water vapor in the evaporator external fluid at
the start of simulation. If the value is a scalar, then the block
assumes that the initial water vapor mole fraction is uniform. If the
value is a two-element vector, then the block assumes that the initial
water vapor mole fraction varies linearly between the ports, with the
first element corresponding to port **Ae** and the
second element corresponding to port **Be**.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial
humidity specification**
`Mole fraction`.

### **Initial humidity ratio** — Humidity ratio at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Evaporator external fluid humidity ratio, defined as the mass ratio of
water vapor to dry air and trace gas, at the start of simulation. If the
value is a scalar, then the block assumes that the initial humidity
ratio is uniform. If the value is a two-element vector, then the block
assumes that the initial humidity ratio varies linearly between the
ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial
humidity specification**
`Humidity ratio`.

### **Initial moist air wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses this value to
calculate humidity.

If the value is a scalar, then the block assumes that the initial
wet-bulb temperature is uniform. If the value is a two-element vector,
then the block assumes that the initial wet-bulb temperature varies
linearly between the ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial
humidity specification** to `Wet-bulb
temperature`.

### **Initial trace gas specification** — Method to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Method used to describe the trace gas level at the start of
simulation.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial trace gas mass fraction** — Mass fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mass fraction of trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the block assumes that the
initial mass fraction is uniform. If the value is a two-element vector,
then the block assumes that the initial mass fraction varies linearly
between the ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial trace
gas specification** to `Mass
fraction`.

### **Initial trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of the trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the block assumes that the
initial mole fraction is uniform. If the value is a two-element vector,
then the block assumes that the initial mole fraction varies linearly
between the ports, with the first element corresponding to port
**Ae** and the second element corresponding to port
**Be**.

The block ignores this parameter if the **Trace gas
model** parameter in the  Moist Air
Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist air`,
clear the **Initialize to nominal operating
conditions** check box, and set **Initial trace
gas specification** to `Mole
fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air` and clear the **Initialize to nominal
operating conditions** check box.

### **Initial evaporator wall temperature** — Evaporator surface temperature at simulation start `293.15` `K` (default) | positive scalar | two-element vector

Heat transfer surface temperature at the start of simulation. If it this value is a
scalar, the block assumes that the initial temperature is uniform. If
this value is a two-element vector, then the block assumes that the
temperature varies linearly between ports **Ae** and
**Be** with the first element corresponding to
**Ae** and second element corresponding to
**Be**.

#### Dependencies

To enable this parameter, clear the **Initialize to nominal operating
conditions** and **Enable evaporator wall
thermal mass** check boxes.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | nonnegative scalar

Relative humidity point of condensation. Condensation occurs above this value. In most
cases, this value is 1, which is equivalent to 100%. A value greater
than 1 indicates a supersaturated vapor.

#### Dependencies

To enable this parameter, set **External fluid for evaporator heat
transfer** to `Moist
air`.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume returns to
saturation by condensing out excess humidity.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air`.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air`.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

#### Dependencies

To enable this parameter, set **External fluid for
evaporator heat transfer** to `Moist
air`.

### Correlation Coefficients

### **Modify condenser Nusselt number correlation coefficients** — Whether to modify condenser Nusselt number correlation coefficients `Off` (default) | `On`

Whether to manually modify the condenser Nusselt number correlation
coefficients. Select this parameter to adjust the off-design performance
of the condenser.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, liquid regime** — Correlation coefficient for refrigerant subcooled liquid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for a subcooled liquid for the
condenser. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, mixture regime** — Correlation coefficient for refrigerant liquid-vapor mixture `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the liquid-vapor mixture for the
condenser. The default value is based on the Cavallini and Zecchin
correlation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, vapor regime** — Correlation coefficient for refrigerant superheated vapor `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the superheated vapor for the
condenser. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **b in Nu = a\*Re^b\*Pr^c for refrigerant** — Reynolds number exponent in correlation for refrigerant `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the condenser refrigerant. The
same value applies to subcooled liquid, liquid-vapor mixture, and
superheated vapor.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **c in Nu = a\*Re^b\*Pr^c for refrigerant** — Prandtl number exponent in correlation for refrigerant `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for condenser refrigerant. The same
value applies to subcooled liquid, liquid-vapor mixture, and superheated
vapor.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, liquid regime** — Correlation coefficient for subcooled liquid in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the subcooled condenser external
fluid. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients** and set
**External fluid for condenser heat transfer**
to `Two-phase fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, mixture regime** — Correlation coefficient for liquid-vapor mixture in two-phase fluid `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for liquid-vapor mixture in the
condenser external fluid. The default value is based on the Cavallini
and Zecchin correlation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients** and set
**External fluid for condenser heat transfer**
to `Two-phase fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, vapor regime** — Correlation coefficient for superheated vapor in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for superheated vapor in the
condenser external fluid. The default value is based on the Colburn
equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients** and set
**External fluid for condenser heat transfer**
to `Two-phase fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid** — Correlation coefficient for condenser external fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the condenser external fluid. The
default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients** and set
**External fluid for condenser heat transfer**
to `Moist air` or `Thermal
liquid`.

### **b in Nu = a\*Re^b\*Pr^c for external fluid** — Reynolds number exponent in correlation for condenser external fluid `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the condenser external fluid. The
default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **c in Nu = a\*Re^b\*Pr^c for external fluid** — Prandtl number exponent in correlation for condenser external fluid `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the condenser external fluid. The
default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify condenser
Nusselt number correlation coefficients**.

### **Modify evaporator Nusselt number correlation coefficients** — Whether to modify evaporator Nusselt number correlation coefficients `Off` (default) | `On`

Whether to manually modify the evaporator Nusselt number correlation
coefficients. Select this parameter to adjust the off-design performance
of the evaporator.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, liquid regime** — Correlation coefficient for refrigerant subcooled liquid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for a subcooled liquid for the
evaporator. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, mixture regime** — Correlation coefficient for refrigerant liquid-vapor mixture `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the liquid-vapor mixture for the
evaporator. The default value is based on the Cavallini and Zecchin
correlation.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

### **a in Nu = a\*Re^b\*Pr^c for refrigerant, vapor regime** — Correlation coefficient for refrigerant superheated vapor `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the superheated vapor for the
condenser. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

### **b in Nu = a\*Re^b\*Pr^c for refrigerant** — Reynolds number exponent in correlation for refrigerant `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the evaporator refrigerant. The
same value applies to subcooled liquid, liquid-vapor mixture, and
superheated vapor.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

### **c in Nu = a\*Re^b\*Pr^c for refrigerant** — Prandtl number exponent in correlation for refrigerant `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for evaporator refrigerant. The same
value applies to subcooled liquid, liquid-vapor mixture, and superheated
vapor.

#### Dependencies

To enable this parameter, select **External fluid for
evaporator heat transfer**.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, liquid regime** — Correlation coefficient for subcooled liquid in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the subcooled evaporator external
fluid. The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator Nusselt number correlation
coefficients** and set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, mixture regime** — Correlation coefficient for liquid-vapor mixture in two-phase fluid `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for liquid-vapor mixture in the
evaporator external fluid. The default value is based on the Cavallini
and Zecchin correlation.

#### Dependencies

To enable this parameter, select **Modify evaporator Nusselt number correlation
coefficients** and set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid, vapor regime** — Correlation coefficient for superheated vapor in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for superheated vapor in the
evaporator external fluid. The default value is based on the Colburn
equation.

#### Dependencies

To enable this parameter, select **Modify evaporator Nusselt number correlation
coefficients** and set **External fluid for
evaporator heat transfer** to `Two-phase
fluid`.

### **a in Nu = a\*Re^b\*Pr^c for external fluid** — Correlation coefficient for evaporator external fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the evaporator external fluid.
The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator Nusselt number correlation
coefficients** and set **External fluid for
evaporator heat transfer** to `Moist
air` or `Thermal
liquid`.

### **b in Nu = a\*Re^b\*Pr^c for external fluid** — Reynolds number exponent in correlation for evaporator external fluid `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the evaporator external fluid.
The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

### **c in Nu = a\*Re^b\*Pr^c for external fluid** — Prandtl number exponent in correlation for evaporator external fluid `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of the
Reynolds number and Prandtl number for the evaporator external fluid.
The default value is based on the Colburn equation.

#### Dependencies

To enable this parameter, select **Modify evaporator
Nusselt number correlation coefficients**.

## Libraries

Simscape / Fluids / Two-Phase Fluid / Thermodynamic Cycles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: Choose gas as the condenser and evaporator external fluid

Set the **External fluid for condenser heat transfer** or
**External fluid for evaporator heat transfer** parameters to
`Gas` to model the condenser or evaporator external
fluid as gas.

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist
air flow. To enable droplet tracking, select **Enable entrained water
droplets** in the Moist Air
Properties (MA) block connected to your moist air network.

### R2024a: New moisture specification option

The block has new options for the **Inlet humidity specification** and
**Initial humidity specification** parameters for both the
condenser and evaporator external fluids. This option, called `Wet-bulb
temperature`, allows you to input data in the form of a wet-bulb
temperature.

## Description

System-level, two-phase refrigeration block in a gas, moist air, thermal liquid, or two-phase fluid network

The System-Level Refrigeration Cycle (2P) block models a
basic refrigeration cycle consisting of a compressor, a condenser, a liquid receiver, a
thermostatic expansion valve, and an evaporator. The block models the refrigerant loop
within the block in the two-phase fluid domain using the fluid properties specified at
port **F**. The condenser and evaporator external fluids can be part of
a gas, moist air, thermal liquid, or two-phase fluid network. The external fluids are
the fluids in the condenser and evaporator opposite the refrigerant.

When the compressor is on, the refrigeration cycle consumes power to transfer heat from the
evaporator external fluid to the condenser external fluid. The subcomponents provide the
specified nominal heat transfer under nominal operating conditions.

### Block Structure

This block behaves as a simplified version of this refrigeration cycle made from
Simscape™
Fluids™ blocks that model the condenser, compressor, evaporator, expansion
device, and liquid receiver:

Diagram of refrigeration cycle consisting of condenser, compressor, evaporator, expansion device, and liquid receiver

The refrigerant flows through the loop counterclockwise. The compressor, which is
controlled by the signal at port **S**, sucks in refrigerant vapor
and produces a hot, high-pressure vapor, which moves to the condenser. The condenser
rejects heat from the refrigerant to the external fluid to condense the refrigerant.
The liquid receiver acts as a storage tank for the refrigerant and only allows
liquid flow to exit, which helps maintain normal operation even if fluctuating
external conditions cause the condenser output to vary. From the tank, the
refrigerant flows to the expansion device, which is typically a valve or capillary
tube that produces a large pressure loss. The drop in pressure partially vaporizes
the refrigerant, which chills it. The refrigerant moves to the evaporator, which
absorbs heat from the external fluid to the cold refrigerant to vaporize the
refrigerant.

The subcomponents of the System-Level Refrigeration Cycle
(2P) block behave the same as these Simscape
Fluids blocks in this model, but the equations for the positive displacement
compressor, expansion valve, receiver component, and condenser and evaporator
subcomponents vary. For more information on the individual components of a
refrigeration system, see:

- Compressor (2P)
- Thermostatic Expansion Valve (2P)
- Receiver
  Accumulator (2P)

The compressor and evaporator components depend on the **External fluid for
condenser heat transfer** and **External fluid for evaporator
heat transfer** parameters. For more information, see:

- System-Level Condenser Evaporator (2P-G)
- System-Level Condenser Evaporator (2P-MA)
- System-Level Condenser Evaporator (2P-TL)
- System-Level Heat Exchanger (2P-2P)

**Positive Displacement Compressor Subcomponent**

The compressor subcomponent determines the refrigerant mass flow rate for the system. The
physical signal input port **S** controls the compressor
operation. When the value at port **S** is
`0`, the compressor is off and the mass flow rate is
`0`. When the value at port **S** is
`1`, the compressor runs at the nominal shaft speed, which
produces the nominal mass flow rate under nominal operating conditions. To
prevent reverse flow, the value of **S** must be greater than
or equal to `0`.

The mass flow rate in the compressor is

m˙=ηvV˙nominalSvin,

where:

- *ηv* is the volumetric
  efficiency.
- *S* is the value of the signal at port
  **S**.
- *vin* is the inlet specific
  volume.
- V˙nominal is the nominal volumetric flow rate, which the block
  determines from the nominal mass flow rate, m˙nominal, which depends on the setting of the
  **Capacity specification** parameter:

  - When the **Capacity specification**
    parameter is `Cooling load`,

    m˙nominal=Qcoolingh1−h4,

    where
    *Qcooling*
    is the **Nominal evaporator heat transfer**
    parameter, *h1* is
    the evaporator outlet specific enthalpy, and
    *h4* is the
    valve outlet specific enthalpy.
  - When the **Capacity specification**
    parameter is `Heating load`,

    m˙nominal=Qheatingh2−h3,

    where
    *Qcooling*
    is the **Nominal condenser heat transfer**
    parameter, *h2* is
    the compressor outlet specific enthalpy, and
    *h3* is the
    condenser outlet specific enthalpy.
  - When the **Capacity specification**
    parameter is `Refrigerant mass flow
    rate`, m˙nominal is the value of the **Nominal mass
    flow rate** parameter.

The fluid power that the compressor adds to the flow is

Φfluid=m˙hout,isen−hinηs,

where:

- *hout,isem* is the
  specific enthalpy evaluated at the output pressure for an isentropic
  process.
- *hin* is the inlet
  specific enthalpy.
- *ηs* is the isentropic
  efficiency.

  - When **Performance specification** is
    `Coefficient of performance for
    cooling` or `Coefficient of
    performance for heating`, the block
    solves for *ηs*
    by calculating
    *h2* and
    using the relation

    h2=h2isen−h1ηs+h1,

    where
    *h2isen*
    is the compressor outlet specific enthalpy assuming an
    isentropic process.

    - When **Performance
      specification** is
      `Coefficient of performance for
      cooling`, the block solves for
      *h2* with CoPcooling=h1−h4h2−h1, where
      *CoPcooling*
      is the **Coefficient of performance at
      nominal conditions** parameter.
    - When **Performance
      specification** is
      `Coefficient of performance for
      heating`, the block solves for
      *h2* with CoPheating=h2−h3h2−h1=h2−h4h2−h1=CoPcooling+1, where
      *CoPheating*
      is the **Coefficient of performance at
      nominal conditions** parameter.
  - When **Performance specification** is
    `Compressor isentropic
    efficiency`,
    *ηs* is
    the value of the **Compressor isentropic
    efficiency** parameter.

The block calculates the volumetric efficiency directly from the inlet and outlet specific
volumes

ηv=1+C−Cvinvout,

where:

- *C* is the clearance volume fraction that the
  block determines from the nominal operating conditions.
- *vin* and
  *vout* are the inlet
  and outlet specific volumes evaluated at the inlet and outlet
  pressures.

The compressor subcomponent does not have mechanical rotational ports and does
not need to calculate shaft torque. The mechanical power is

Φmech=Φfluidηm,

where *ηm* is the mechanical
efficiency.

**Expansion Valve Subcomponent**

The relationship between mass flow rate, which the compressor determines, and the pressure
drop across the thermostatic expansion valve subcomponent is

m˙=Seff2vinΔp(Δp2−Δplam2)0.25,

where:

- *vin* is the inlet
  specific volume.
- *Δp* is the pressure differential over the
  valve.
- *Δplam* is the pressure
  threshold for transitional flow. Below this value, the flow is
  laminar.

The effective valve area depends on the pressure difference
between the measured pressure, *pbulb*,
and the equalization pressure, *peq*

Seff=β[(pbulb−peq)−(psat(Tevap+ΔTstatic)−psat(Tevap))],

where:

- *β* is a valve constant the block determines from
  the nominal operating conditions.
- *Tevap* is the evaporating
  temperature, which depends on the **Pressure
  specification** setting:

  - When **Pressure specification** is
    `Pressure at specified saturation
    temperature`,
    *Tevap* is
    the value of the **Nominal evaporating (saturation)
    temperature** parameter.
  - When **Pressure specification** is
    `Specified pressure`,
    *Tevap* is
    the saturation temperature that corresponds to the value of
    the **Nominal evaporator pressure**
    parameter.
- *ΔTstatic* is the
  **Static (minimum) evaporator superheat**
  parameter.
- *psat(Tevap)*
  is the fluid saturation pressure as a function of
  *Tevap*.
- *psat(Tevap+ΔTstatic)*
  is the fluid saturation pressure as a function of
  *Tevap+ΔTstatic*.
- *pbulb* is the fluid
  pressure of the bulb. This pressure is the saturation pressure at
  the evaporator outlet temperature.
- *peq* is the equalization
  pressure, which is the evaporator pressure for this block.

The effective valve area has limits. The minimum effective valve
area, *Seff,min*, is

Seff,min=fleakSeff,nom,

where *fleak* is the
value of the **Ratio of leakage to nominal expansion valve
opening** parameter. The maximum effective valve area,
*Seff,mmax*, is

Seff,max=fmaxSeff,nom,

where *fmax* is the
value of the **Ratio of maximum to nominal expansion valve
opening** parameter.

**Receiver Subcomponent**

Excluding the receiver, the block assumes that the refrigerant mass flow rate is the same
value through the loop. In the receiver, the total mass is based on the balance
between the mass flow rate produced by the compressor and the mass flow rate
metered by the expansion valve. The outflow from the receiver subcomponent is
always liquid and perfectly insulated from the environment.

The liquid mass fraction in the receiver subcomponent is

M dxliqdt=m˙liq,in−m˙out−m˙vaporization+m˙condensation,

where:

- *xliq* is the liquid mass
  fraction.
- m˙liq,in is the portion of the
  flow in that is liquid.
- m˙out is the mass flow rate out of
  the receiver.
- m˙vaporization  is the rate of
  vaporization from the liquid volume to the vapor volume.
- m˙condensation is the rate of
  condensation from the vapor volume to the liquid volume.

The pressure relates to the total mass via the specific volume using the relation

M(xliqvliq+(1−xliq)vvap)=V,

where:

- *V* is the total receiver volume.
- *vliq* is the is the
  specific volume of the liquid volume.
- *vvap* is the is the
  specific volume of the vapor volume.

**Condenser and Evaporator Subcomponents**

The condenser and evaporator subcomponents model the refrigerant thermal mass, but do not
model fluid volume. For the condenser and evaporator, the energy conservation
equation is

M dhIdt=m˙(hin−hout)+Q,

where:

- *M* is the constant mass of refrigerant in the
  component.
- *hI* is the refrigerant
  specific enthalpy at the component internal node.
- m˙ is the refrigerant mass flow rate.
- *Q* is the rate of heat transfer from the
  external fluid to the refrigerant.
- *hin* and
  *hout* are the
  refrigerant specific enthalpy in and out of the component.

### Visualize the P-H Diagram

To visualize the refrigeration cycle, use a Probe block from the Simscape > Utilities library to output the
variables `p_cycle` and `h_cycle`. These variables
contain the four pressure and specific enthalpy points of the refrigeration cycle.
Connect the variables to the P-H Diagram
(2P) block to visualize the refrigeration cycle.

This diagram shows the fluid attributes throughout the system for the refrigerant R-410a.
Segment 1 to 2 is the compressor, segment 2 to 3 is the condenser, point 3 is the
receiver, segment 3 to 4 is the expansion valve, and segment 4 to 1 is the
evaporator.

P-H diagram for the refrigeration cycle

### Assumptions and Limitations

- The block does not model reverse flow and limits the refrigeration cycle
  to zero and forward flow only. To prevent reverse flow, the block limits the
  compressor control to zero or forward operation and only models fluid volume
  in the liquid receiver subcomponent.
- Excluding the liquid receiver, the subcomponents do not model refrigerant
  fluid volume, which prevents the accumulation of mass in subcomponents. As a
  result, the refrigerant mass flow rate is the same through the evaporator,
  compressor, and condenser subcomponents.
- There is no refrigerant pressure loss in the evaporator or
  condenser.
- The block does not model kinetic energy changes in the refrigerant
  flow.
- The evaporator subcomponent models approximate pressure dynamics to
  maintain numerical robustness. However, the condenser subcomponent does not
  model approximate pressure dynamics, because the condenser pressure is equal
  to the receiver pressure, which does model pressure dynamics.
- The condenser and evaporator subcomponents only model counter flow because
  the refrigerant is primarily in the two-phase mixture state within the
  condenser and evaporator. Consequently, the temperature is uniform across
  most of the condenser and evaporator, and there is no significant difference
  between counter flow and cross flow.
- When determining the heat exchanger size, the block ignores the values of
  the **Fraction of condensate entrained as water droplets**
  parameters and assumes that the condensate is not entrained as
  droplets.
