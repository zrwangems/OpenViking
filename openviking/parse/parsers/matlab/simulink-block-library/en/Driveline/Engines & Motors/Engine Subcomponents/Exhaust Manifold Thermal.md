---
type: simulink-block
title: 'Exhaust Manifold Thermal'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'exhaustmanifoldthermal'
documentation_source_path: 'ref/exhaustmanifoldthermal.html'
language: en
---

# Exhaust Manifold Thermal

## Ports

### Input

### **Qeng** — Gas energy flow, W physical signal

Physical signal input port associated with the gas energy flow, in W. Attach this port
to the **Weo** physical signal output port on the
SI Combustion Cylinder block.
### Output

### **Texh** — Exhaust manifold temperature, K physical signal

Physical signal output port associated with the lumped-parameter exhaust manifold
temperature, in K.

## Parameters

### **Number of exhaust ports** — Number of exhaust ports `1` (default) | positive scalar

Number of SI Combustion Cylinder
blocks.

### **Ambient temperature** — Reference temperature `298.15` `K` (default) | positive scalar

Temperature of the air entering the intake.

### **Surface area of exhaust wall** — Exhaust wall surface area `pi * ((1.5 / 2) ^ 2)` `m^2` (default) | positive scalar

Surface area of the exhaust
wall.
This is only the surface area of the internal wall that makes contact with
the exhaust.

### **Mass of exhaust wall** — Exhaust wall total mass `5` `kg` (default) | positive scalar

Mass of the exhaust wall.

### **Heat capacity of exhaust wall** — Exhaust wall heat capacity `100` `J/(K*kg)` (default) | positive scalar

Heat capacity of the exhaust wall.

### **Time constant of exhaust heat flow** — Exhaust heat flow time constant `10` `s` (default) | positive scalar

Time constant for the rate of exhaust heat flow.

### **Convective heat transfer coefficient for the outer side of exhaust** — Exhaust external convective heat transfer coefficient `100` `W/(K*m^2)` (default) | positive scalar

Convective heat transfer coefficient for the outer side of the
exhaust.

### **Radiation constant** — Exhaust radiation constant `0.3` (default) | positive scalar

Radiation constant of the exhaust.

### **Stefan-Boltzmann constant** — Stefan-Boltzmann constant of exhaust `5.7e-8` `W/(K^4*m^2)` (default) | positive scalar

Stefan-Boltzmann constant for the total exhaust.

## Libraries

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Thermodynamics of combustion engine exhaust manifold

The Exhaust Manifold Thermal block represents the abstracted
thermodynamics of a combustion engine exhaust manifold. The block integrates with the
SI Combustion Cylinder block.

### Equations

The block takes exhaust gas flow from the SI Combustion
Cylinder blocks and computes the exhaust manifold temperature,
*Texh*, which the block outputs at
port **Texh**. The block calculates the output using a
lumped-parameter model, such that

CexhMexhddtTexh=hexh−hx,

where

- *Cexh* is the **Heat
  capacity of exhaust wall** parameter.
- *Mexh* is the **Mass
  of exhaust wall** parameter.
- *hexh* is the heat flow at the
  exhaust manifold.
- *hx* is the heat exchange
  between the exhaust gas and the environment.

The block calculates *hx* as

hx=Sexh(hconvec(Texh−Tamb)−kraσ(Texh4−Tamb4)),

where

- *Sexh* is the
  **Surface area of exhaust wall** parameter.
- *hconvec* is the
  **Convective heat transfer coefficient for the outer side of
  exhaust** parameter.
- *kra* is the
  **Radiation constant** parameter.
- *σ* is the **Stefan-Boltzmann
  constant** parameter.
- *Tamb* is the
  **Ambient temperature** parameter.

The block finds *hexh* as

kgasddthexh=hin−hexh,

where *kgas* is the
**Time constant of exhaust heat flow** parameter, and
*hin* is the instantaneous heat flow
from the engine exhaust outlets to the exhaust manifold. The instantaneous heat flow
is the sum of the individual instantaneous heat flows at the exhaust outlets,
*hi*, such that

hin=∑i=1Nportshi,

where *Nports* is the
**Number of exhaust ports** parameter.
