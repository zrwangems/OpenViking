---
type: simulink-block
title: 'Spring-Loaded Accumulator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Tanks and Accumulators'
documentation_page: 'springloadedaccumulatoril'
documentation_source_path: 'ref/springloadedaccumulatoril.html'
language: en
---

# Spring-Loaded Accumulator (IL)

## Ports

### Conserving

### **A** — Hydraulic conserving port hydraulic conserving

Hydraulic conserving port associated with the accumulator inlet. The
flow rate is positive if liquid flows into the accumulator.

## Parameters

### **Liquid capacity** — Liquid capacity `8e-3 m^3` (default) | positive scalar

Amount of liquid that the accumulator can hold.

### **Preload pressure** — Spring pressure `1.01325 MPa` (default) | positive scalar

Spring pressure when the liquid chamber is empty.

### **Pressure at full capacity** — Spring pressure `3.01325 MPa` (default) | positive scalar

Spring pressure when the liquid chamber is at capacity.

### **Hard stop stiffness coefficient** — Proportionality constant `1e4 MPa/m^3` (default) | positive scalar

Proportionality constant of the hard-stop contact pressure with respect to
the liquid volume penetrated into the hard stop. The hard stops are used to
restrict the liquid volume between zero and liquid chamber capacity.

### **Enable dynamic compressibility** — Fluid compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid compressibility.
When you select **Enable dynamic compressibility**, changes
due to the mass flow rate into the block are calculated in addition to
density changes due to changes in pressure. In the Isothermal Liquid
Library, all blocks calculate density as a function of pressure.

## Libraries

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Accumulator with a spring used for energy storage in an isothermal liquid system

This block models a spring-charged accumulator in an isothermal liquid network. The
accumulator consists of a preloaded spring and a liquid chamber.

As the liquid pressure at the accumulator inlet becomes greater than the preload
pressure, liquid enters the accumulator and compresses the spring. A decrease in the
liquid pressure causes the spring to decompress and discharge stored liquid into the
system. The separator motion is restricted by a hard stop when the liquid volume is zero
and when the liquid volume is at the liquid chamber capacity.

The inlet liquid resistance and spring properties, such as the spring inertia and
damping, are not modeled. The spring pressure is assumed to be linear with respect to
the liquid volume. The flow rate is positive if liquid flows into the
accumulator.

This diagram represents a spring-loaded accumulator.

|  |  |
| --- | --- |
| `VL` | Volume of the liquid in the accumulator. |
| `VC` | Liquid chamber capacity |
| `pmax` | Pressure at full capacity |
| `pI` | Liquid pressure in the liquid chamber, which is equal to the pressure at the accumulator inlet. |
| `pHS` | Hard-stop contact pressure. |
| `Kstiff` | Hard-stop stiffness coefficient. |
| `Kspring` | Spring gain. |
| m˙`A` | Mass flow rate of liquid coming into port A. |
| `ρI` | Density of the liquid in the liquid chamber. |

### Conservation of Mass

The mass conservation in the block is

{p˙IdρIdpIVL+ρIV˙L=m˙A,     compressibility onρ0V˙L=m˙A,                       compressibility off

where

V˙L={p˙IKspring,            if 0 <VL<VCp˙IKspring+Kstiff,                  else

*ρ0* is the constant liquid density. The block
calculates this value from **Preload pressure** parameter.

### Conservation of Momentum

Conservation of momentum is represented by the following equation.

pI=pspring+pHS

where

pspring=ppr+KspringVL

pHS={(VL−VC)Kstiff,    if VL≥VCVLKstiff,                          if VL ≤ 00,                                    else

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
