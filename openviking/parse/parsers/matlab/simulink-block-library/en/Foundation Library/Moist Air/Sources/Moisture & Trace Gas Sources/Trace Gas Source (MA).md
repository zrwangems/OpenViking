---
type: simulink-block
title: 'Trace Gas Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources / Moisture & Trace Gas Sources'
documentation_page: 'tracegassourcema'
documentation_source_path: 'ref/tracegassourcema.html'
language: en
---

# Trace Gas Source (MA)

## Ports

### Input

### **M** — Mass flow rate control signal, kg/s physical signal

Input physical signal that specifies the trace gas mass flow rate
through the source.

#### Dependencies

To enable this port, set the **Source type**
parameter to `Controlled`.

### **T** — Temperature of added trace gas, K physical signal

Input physical signal that specifies the temperature of added trace
gas. The block uses this value to evaluate the specific enthalpy of the
added trace gas only. The specific enthalpy of removed trace gas is
based on the temperature of the connected moist air volume.

#### Dependencies

To enable this port, set the **Source type**
parameter to `Controlled`.
### Conserving

### **S** — Inject or extract trace gas moist air source

Connect this port to port **S** of a block with
finite moist air volume to add or remove trace gas through that
block.

## Parameters

### **Source type** — Select whether trace gas mass flow rate and temperature can change during simulation `Controlled` (default) | `Constant`

Select whether the trace gas mass flow rate and temperature can change
during simulation:

- `Controlled` — The trace gas mass
  flow rate and temperature are variable, controlled by input physical
  signals. Selecting this option exposes the input ports
  **M** and **T**.
- `Constant` — The trace gas mass
  flow rate and temperature are constant during simulation, specified
  by block parameters. Selecting this option enables these
  parameters.

### **Rate of added trace gas** — Constant mass flow rate through the source `0 kg/s` (default)

Trace gas mass flow rate through the source. A positive value adds trace
gas to the connected moist air volume. A negative value extracts trace gas
from that volume.

#### Dependencies

To enable this parameter, set **Source type** to
`Constant`.

### **Added trace gas temperature specification** — Select specification method for the temperature of added trace gas `Atmospheric temperature` (default) | `Specified temperature`

Select a specification method for the trace gas temperature:

- `Atmospheric temperature` — Use
  the atmospheric temperature, specified by the Moist Air
  Properties (MA) block connected to the circuit.
- `Specified temperature` — Specify
  a value by using the **Temperature of added trace
  gas** parameter.

#### Dependencies

To enable this parameter, set **Source type** to
`Constant`.

### **Temperature of added trace gas** — Trace gas temperature `293.15 K` (default)

Enter the desired temperature of added trace gas. This temperature remains
constant during simulation. The block uses this value to evaluate the
specific enthalpy of the added trace gas only. The specific enthalpy of
removed trace gas is based on the temperature of the connected moist air
volume.

#### Dependencies

To enable this parameter, set **Added trace gas temperature
specification** to `Specified
temperature`.

## Libraries

Simscape / Foundation Library / Moist Air / Sources / Moisture & Trace Gas Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2023b: Usability enhancement for moist air sources

In R2023b, separate Trace Gas Source (MA) and Controlled
Trace Gas Source (MA) blocks have been combined into a single
Trace Gas Source (MA) block that lets you select between constant
or time-varying source or sink of trace gas.

This change has no compatibility impact when you use these Foundation library
blocks in your models. When you open an existing model, the Controlled Trace
Gas Source (MA) blocks are automatically replaced by Trace Gas
Source (MA) blocks with exposed input ports.

However, if you use these blocks in your custom composite components, you need to
update the composite component code.

| Source Block to Update | Old Syntax | New Syntax |
| --- | --- | --- |
| Controlled Trace Gas Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source_controlled;` | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source;` |
| Trace Gas Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source;` | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source(source_type=foundation.enum.constant_controlled.constant);` |

## Description

Inject or extract trace gas at a constant or time-varying rate

The Trace Gas Source (MA) block represents a constant
or time-varying source or sink of trace gas for the connected moist air volume. A
positive or negative trace gas mass flow rate causes trace gas levels to increase or
decrease, respectively.

For a time-varying source, two physical signal input ports, **M** and
**T**, supply the mass flow rate and temperature values,
respectively. Alternatively, you can specify constant mass flow rate and temperature as
block parameters.

The energy associated with the added or removed trace gas is

Φs={m˙specified⋅hg(Tspecified),if m˙specified≥0m˙specified⋅hg(Ts),if m˙specified<0

where:

- m˙specified is the trace gas mass flow rate specified by the input
  physical signal at port **M** or by the **Trace gas
  mass flow rate** parameter.
- *h*g is the trace gas specific
  enthalpy.
- *T*specified is the temperature of
  added trace gas, as specified by the input physical signal at port
  **T** or by the block parameters. The block uses this value
  to evaluate the specific enthalpy of the added trace gas only. The specific
  enthalpy of removed trace gas is based on the temperature of the connected moist
  air volume.
- *T*s is the temperature at port
  **S**, which is the same as the temperature of the
  connected moist air volume.

Port **S** is a moist air source conserving port. Connect this port
to port **S** of a block with finite moist air volume to add or remove
trace gas through that block. For more information, see Using Moisture and Trace Gas Sources.
