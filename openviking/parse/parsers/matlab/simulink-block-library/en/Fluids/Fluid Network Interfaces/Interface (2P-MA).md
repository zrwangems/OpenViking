---
type: simulink-block
title: 'Interface (2P-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interface2pma'
documentation_source_path: 'ref/interface2pma.html'
language: en
---

# Interface (2P-MA)

## Ports

### Input

### **W** — Humidity, unitless physical signal

Physical signal port associated with the humidity content at the
interface.

#### Dependencies

To enable this port, select **Provide input signal for
interface humidity** and set **Interface
humidity specification** to `Relative
humidity`, `Specific
humidity`, `Mole
fraction`, or `Humidity
ratio`.

### **Tw** — Temperature, K physical signal

Physical signal port associated with the wet-bulb temperature at the interface, in
K.

#### Dependencies

To enable this port, select **Provide input signal for interface
humidity** and set **Interface humidity
specification** to `Wet-bulb
temperature`.

### **TG** — Trace gas, unitless physical signal

Physical signal port associated with the trace gas at the
interface.

#### Dependencies

To enable this port, select **Provide input signal for interface trace
gas**.

### **D** — Water droplet mass ratio, unitless physical signal

Physical signal port associated with the mass ratio of water droplets
to moist air at the interface.

#### Dependencies

To enable this port, select **Provide input signal for
interface water droplets**.
### Conserving

### **2P** — Two-phase port two-phase fluid

Two-phase fluid conserving port associated with the two-phase fluid at the
interface.

### **MA** — Moist air port moist air

Moist air conserving port associated with the moist air at the interface.

## Parameters

### **Provide input signal for interface humidity** — Interface humidity control option `off` (default) | `on`

Option for specifying the interface humidity. If you select this check
box, the block enables port **W**. If you clear this check
box, you can specify constant humidity conditions.

### **Interface humidity specification** — Humidity parameterization option `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Whether to calculate humidity using relative humidity, specific humidity,
mole fraction, humidity ratio, or wet-bulb temperature.

### **Interface relative humidity** — Relative humidity at interface `0.5` (default) | positive scalar

Relative humidity at the interface. The block uses this value to calculate the
humidity.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface
humidity** check box and set **Interface humidity
specification** to `Relative
humidity`.

### **Interface specific humidity** — Specific humidity at interface `0.01` (default) | positive scalar

Specific humidity at the interface. The block uses this value to calculate the
humidity.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface
humidity** check box and set **Interface humidity
specification** to `Specific
humidity`.

### **Interface water vapor mole fraction** — Water vapor mole fraction at interface `0.01` (default) | positive scalar

Water vapor mole fraction at the interface. The block uses this value to calculate the
humidity.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface
humidity** check box and set **Interface humidity
specification** to `Mole
fraction`.

### **Interface humidity ratio** — Humidity ratio at interface `0.01` (default) | positive scalar

Humidity ratio at the interface. The block uses this value to calculate the
humidity.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface
humidity** check box and set **Interface humidity
specification** to `Humidity
ratio`.

### **Interface wet-bulb temperature** — Wet-bulb temperature at interface `287 K` (default) | positive scalar

Wet bulb temperature at the interface. The block uses this value to calculate
humidity.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface
humidity** check box and set **Interface humidity
specification** to `Wet-bulb
temperature`.

### **Provide input signal for interface trace gas** — Interface trace gas control option `off` (default) | `on`

Option for specifying the trace gas fraction. If you select this check
box, the block enables port **TG**. If you clear this check
box, you can specify constant trace gas conditions.

### **Interface trace gas specification** — Trace gas parameterization `Mass fraction` (default) | `Mole fraction`

Whether to parameterize the trace gas at the interface using mass fraction
or mole fraction.

### **Interface trace gas mass fraction** — Trace gas mass fraction at interface `0.001` (default) | positive scalar

Mass fraction of trace gas at the interface.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface trace
gas** check box and set **Interface trace gas
specification** to `Mass
fraction`.

### **Interface trace gas mole fraction** — Trace gas mole fraction at interface `0.001` (default) | positive scalar

Mole fraction of trace gas at the interface.

#### Dependencies

To enable this parameter, clear the **Provide input signal for interface trace
gas** check box and set **Interface trace gas
specification** to `Mole
fraction`.

### **Provide input signal for interface water droplets** — Interface water droplet control option `off` (default) | `on`

Option for specifying the mass ratio of water droplets to moist air. If
you select this check box, the block enables port **D**. If
you clear this check box, you can specify constant water droplet conditions
with the **Interface mass ratio of water droplets to moist
air** parameter.

### **Interface mass ratio of water droplets to moist air** — Ratio of water droplets to moist air at interface `0` (default) | positive scalar

Mass ratio of water droplets to moist air at the interface.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
interface water droplets** check box.

### **Relative humidity at saturation** — Saturation point relative humidity `1` (default) | positive scalar

Relative humidity at the point of saturation.

### **Cross-sectional area at ports 2P and MA** — Port area `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the two-phase fluid and moist air ports.

### **Two-phase fluid superheated vapor check** — Two-phase fluid superheated conditions check `None` (default) | `Warning` | `Error`

Action to perform when the fluid at the interface does not meet
superheated conditions.

### **Inputs outside valid range** — Option to monitor or control invalid inputs `Limit to valid values` (default) | `Warn and limit to valid values` | `Error`

Monitor or control invalid inputs. When you select `Limit to
valid values`, the block saturates the inputs within the
bounds. You can choose to have the block issue a warning when it limits the
inputs by selecting `Warn and limit to valid
values`, or you can stop the simulation when the block
receives invalid inputs by selecting
`Error`.

## Libraries

Simscape / Fluids / Fluid Network Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist
air flow. To enable droplet tracking, select **Enable entrained water
droplets** in the Moist Air
Properties (MA) block connected to your moist air network.

Instead of using the **Moisture and trace gas specification**
parameter to specify whether the interface is constant or controlled, use the new
**Provide input signal for interface humidity**,
**Provide input signal for interface trace gas**, and
**Provide input signal for interface water droplets**
parameters to enable the physical signal input ports.

## Description

Two-phase fluid and moist air network interface

The Interface (2P-MA) block represents a flow connection
between a two-phase fluid network and moist air network. Pressure, temperature, and mass
flow rate are equal at the interface. The block does not transfer the fluid properties
of each fluid network across the interface. When moist air leaves port
**MA**, the block assigns the values of the **Interface
relative humidity**, **Interface trace gas mass
fraction**, and **Interface mass ratio of water droplets to moist
air** parameters, or the values of the input signals, to the signal.
However, when moist air enters port **MA**, the block retains the
upstream values.

You can choose whether to maintain constant humidity, water droplets, and trace gas amounts
at the interface or to specify them using the **W** or
**Tw**, **D**, and **TG** ports
respectively. The fluid at the **2P** port must remain superheated. You
can use the **Two-phase fluid superheated vapor check** parameter to
choose what action the block performs if the fluid does not meet this condition.

### Equations

The block conserves mass such that

m˙2P+m˙MA=0,

where:

- *ṁ2P* is the mass flow rate
  into port **2P**.
- *ṁMA* is the mass flow rate
  into port **MA**.

The block maintains equal port pressures and temperatures such that

p2P=pMAT2P=TMA

The block calculates the energy balance over the interface as

Φ2P+ΦMA=m˙2P(h2P+w2P22)+m˙MA(hMA+wMA22),

where:

- *Φ2P* is the energy flow rate
  into port **2P**.
- *ΦMA* is the energy flow rate
  into port **MA**.
- *h2P* is the specific enthalpy
  at port **2P**.
- *hMA* is the specific enthalpy
  at port **MA**.
- *v2P* is the specific volume
  at port **2P**.
- *vMA* is the specific volume
  at port **MA**.
- *w2P* is the flow velocity at
  port **2P**.
- *wMA* is the flow velocity at
  port **MA**.

For a given cross-sectional area, *S*, the block
defines *w2P* as

w2P=m˙2Pv2PS,

and *wMA* as

wMA=m˙MAvMAS,

where

vMA=RITMApMA.

You specify *S* using the
**Cross-sectional area at ports 2P and MA** parameter. The
block computes the specific gas constant of the interface mixture,
*RI*, as a function of the fluid on
either side such that

RI=f(RA,RW,RG,xWI,xGI),

where:

- *RA* is the dry air specific
  gas constant.
- *RW* is the water vapor
  specific gas constant.
- *RG* is the trace gas specific
  gas constant.
- *xWI* is the interface specific humidity. The
  block determines this value when the flow exits port
  **MA**, based on your parameter settings:

  - When you clear the **Provide input signal for
    interface humidity** check box, the block
    calculates *xWI*
    based on the method specified with the **Interface
    humidity specification** parameter.
  - When you select **Provide input signal for
    interface humidity**, the block bases
    *xWI* on the
    input that you supply at port **W** or port
    **Tw**.
- *xGI* is the interface trace gas mass fraction.
  The block determines this value when the flow exits port
  **MA**, based on your parameter settings:

  - When you clear the **Provide input signal for
    interface trace gas** check box, the block
    calculates *xGI*
    based on the value of the **Interface trace gas mass
    fraction** or **Interface trace gas
    mole fraction** parameter.
  - When you select **Provide input signal for
    interface trace gas**, the block bases
    *xGI* on the
    input that you supply at port
    **TG**.
