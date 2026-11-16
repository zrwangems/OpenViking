---
type: simulink-block
title: 'Moisture Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources / Moisture & Trace Gas Sources'
documentation_page: 'moisturesourcema'
documentation_source_path: 'ref/moisturesourcema.html'
language: en
---

# Moisture Source (MA)

## Ports

### Input

### **M** — Mass flow rate control signal, kg/s physical signal

Input physical signal that specifies the water vapor or water droplets
mass flow rate through the source.

#### Dependencies

To enable this port, set the **Source type**
parameter to `Controlled`.

### **T** — Temperature of added moisture, K physical signal

Input physical signal that specifies the temperature of added
moisture. The block uses this value to evaluate the specific enthalpy of
the added moisture only. The specific enthalpy of removed moisture is
based on the temperature of the connected moist air volume.

#### Dependencies

To enable this port, set the **Source type**
parameter to `Controlled`.
### Conserving

### **S** — Inject or extract humidity or water droplets moist air source

Connect this port to port **S** of a block with
finite moist air volume to add or remove humidity or water droplets
through that block.

## Parameters

### **Source type** — Select whether moisture mass flow rate and temperature can change during simulation `Controlled` (default) | `Constant`

Select whether the moisture mass flow rate and temperature can change
during simulation:

- `Controlled` — The moisture mass
  flow rate and temperature are variable, controlled by input physical
  signals. Selecting this option exposes the input ports
  **M** and **T**.
- `Constant` — The moisture mass
  flow rate and temperature are constant during simulation, specified
  by block parameters. Selecting this option enables these
  parameters.

### **Moisture added or removed** — Select whether the block adds or removes moisture as water vapor or water droplets `Water vapor` (default) | `Water droplets`

Select whether the block adds or removes moisture as water vapor or water
droplets.

### **Water vapor evaporated from liquid or condensed to liquid** — How the block adds or removes water vapor `off` (default) | `on`

Select how the block adds or removes water vapor. If you clear this check
box, the enthalpy of the added or removed moisture corresponds to the
enthalpy of water vapor, which is greater than that of liquid water.

If you select this check box, the enthalpy of the added or removed
moisture corresponds to the enthalpy of liquid water, which is less than
that of water vapor. When water vapor is added, it evaporates from liquid
and the latent heat is contributed by the connected fluid volume. When water
vapor is removed, it condenses to liquid and the latent heat is released to
the connected fluid volume.

#### Dependencies

To enable this parameter, set **Moisture added or
removed** to `Water vapor`.

### **Rate of moisture added** — Constant mass flow rate through the block `0 kg/s` (default)

Water vapor or water droplets mass flow rate through the block. A positive
value adds moisture to the connected moist air volume. A negative value
extracts moisture from that volume.

#### Dependencies

To enable this parameter, set **Source type** to
`Constant`.

### **Added moisture temperature specification** — Select specification method for the temperature of added moisture `Atmospheric temperature` (default) | `Specified temperature`

Select a specification method for the moisture temperature:

- `Atmospheric temperature` — Use
  the atmospheric temperature, specified by the Moist Air
  Properties (MA) block connected to the circuit.
- `Specified temperature` — Specify
  a value by using the **Temperature of added
  moisture** parameter.

#### Dependencies

To enable this parameter, set **Source type** to
`Constant`.

### **Temperature of added moisture** — Moisture temperature `293.15 K` (default)

Enter the desired temperature of added moisture. This temperature remains
constant during simulation. The block uses this value to evaluate the
specific enthalpy of the added moisture only. The specific enthalpy of
removed moisture is based on the temperature of the connected moist air
volume.

#### Dependencies

To enable this parameter, set **Source type** to
`Constant` and **Added moisture
temperature specification** to `Specified
temperature`.

## Libraries

Simscape / Foundation Library / Moist Air / Sources / Moisture & Trace Gas Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

### R2023b: Usability enhancement for moist air sources

In R2023b, separate Moisture Source (MA) and Controlled
Moisture Source (MA) blocks have been combined into a single
Moisture Source (MA) block that lets you select between constant
or time-varying source or sink of moisture.

This change has no compatibility impact when you use these Foundation library
blocks in your models. When you open an existing model, the Controlled
Moisture Source (MA) blocks are automatically replaced by
Moisture Source (MA) blocks with exposed input ports.

However, if you use these blocks in your custom composite components, you need to
update the composite component code.

| Source Block to Update | Old Syntax | New Syntax |
| --- | --- | --- |
| Controlled Moisture Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source_controlled;` | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source;` |
| Moisture Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source;` | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source(source_type=foundation.enum.constant_controlled.constant);` |

## Description

Inject or extract moisture at a constant or time-varying rate

The Moisture Source (MA) block represents a constant or
time-varying source or sink of humidity or droplets for the connected moist air volume.
A positive or negative moisture mass flow rate results in moisture being added or
removed, respectively.

For a time-varying source, two physical signal input ports, **M** and
**T**, supply the mass flow rate and temperature values,
respectively. Alternatively, you can specify constant mass flow rate and temperature as
block parameters.

When the **Moisture added or removed** parameter is
`Water vapor`, the **Water vapor evaporated from
liquid or condensed to liquid** parameter controls how the vapor leaves or
enters the block. When you clear **Water vapor evaporated from liquid or
condensed to liquid**, the block removes water vapor from the fluid volume
at a specified rate. When you select **Water vapor evaporated from liquid or
condensed to liquid**, the block assumes that the vapor that enters the
fluid volume originates from evaporated water and that the vapor that leaves the volume
condenses to liquid. In this case, the block also models the changes in latent heat from
either process.

When you clear the **Water vapor evaporated from liquid or condensed to
liquid** check box, the energy associated with the added or removed vapor
is

Φs={m˙specified⋅hw(Tspecified),if m˙specified≥0m˙specified⋅hw(Ts),if m˙specified<0

where:

- m˙specified is the water vapor mass flow rate specified by the input
  physical signal at port **M** or by the **Rate of added
  moisture** parameter.
- *h*w is the water vapor specific
  enthalpy.
- *T*specified is the temperature of
  added moisture, as specified by the input physical signal at port
  **T** or by the block parameters. The block uses this value
  to evaluate the specific enthalpy of the added moisture only. The specific
  enthalpy of removed moisture is based on the temperature of the connected moist
  air volume.
- *T*s is the temperature at port
  **S**, which is the same as the temperature of the
  connected moist air volume.

When you select **Water vapor evaporated from liquid or condensed to
liquid**, the energy associated with the added or removed vapor is

Φs={m˙specified⋅(hw(Tspecified)−Δhvap(Tspecified)),if m˙specified≥0m˙specified⋅(hw(Ts)−Δhvap(Ts)),if m˙specified<0

where *Δh*vap is the water specific enthalpy
of vaporization.

Port **S** is a moist air source conserving port. Connect this port
to port **S** of a block with finite moist air volume to add or remove
moisture through that block. For more information, see Using Moisture and Trace Gas Sources.
