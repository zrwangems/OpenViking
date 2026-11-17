---
type: simulink-block
title: 'Gas-Charged Accumulator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'gaschargedaccumulatoril'
documentation_source_path: 'ref/gaschargedaccumulatoril.html'
language: en
---

# Gas-Charged Accumulator (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid port associated with the accumulator inlet. The flow
rate is positive if liquid flows into the accumulator.
## Parameters
```yaml
parameters:
- name: Total accumulator volume
  summary: Accumulator volume 8e-3 m^3 (default) | positive scalar
  group: ''
- name: Minimum gas volume
  summary: Gas chamber dead volume 4e-5 m^3 (default) | positive scalar
  group: ''
- name: Precharge pressure
  summary: Gas chamber pressure 1.101325 MPa (default) | positive scalar
  group: ''
- name: Specific heat ratio
  summary: Specific heat ratio 1.4 (default) | positive scalar
  group: ''
- name: Hard stop stiffness coefficient
  summary: Proportionality constant 1e4 MPa/m^3 (default) | positive scalar
  group: ''
- name: Enable dynamic compressibility
  summary: Fluid compressibility on (default) | off
  group: ''
```

### **Total accumulator volume** — Accumulator volume `8e-3` `m^3` (default) | positive scalar

Total volume of the accumulator, including the liquid chamber and the gas
chamber. It is the sum of the liquid chamber capacity and the minimum gas
volume.

### **Minimum gas volume** — Gas chamber dead volume `4e-5` `m^3` (default) | positive scalar

Gas chamber dead volume, which is defined as a small portion of the gas chamber that
remains filled with gas when the liquid chamber is filled to capacity. The
block requires a nonzero value to avoid divide-by-zero when the liquid
chamber is at capacity.

### **Precharge pressure** — Gas chamber pressure `1.101325` `MPa` (default) | positive scalar

Pressure in the gas chamber when the liquid chamber is empty.

### **Specific heat ratio** — Specific heat ratio `1.4` (default) | positive scalar

Specific heat ratio (adiabatic index). To account for heat exchange, set
it to a value normally between 1 and 2, depending on the properties of the
gas in the gas chamber. For dry air at 20°C, this value is 1 for an
isothermal process or 1.4 for an adiabatic (and isentropic) process.

### **Hard stop stiffness coefficient** — Proportionality constant `1e4` `MPa/m^3` (default) | positive scalar

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

Gas-charged accumulator in an isothermal liquid network

The Gas-Charged Accumulator (IL) block represents a
gas-charged accumulator in an isothermal liquid network. The accumulator consists of a
precharged gas chamber and a liquid chamber. The chambers are separated by a bladder, a
piston, or any kind of a diaphragm.

As the liquid pressure at the accumulator inlet becomes greater than the precharge
pressure, liquid enters the accumulator and compresses the gas through a polytropic
process. A decrease in the liquid pressure causes the gas to decompress and discharge
stored liquid into the system. The separator motion is restricted by a hard stop when
the liquid volume is zero and when the liquid volume is at the liquid chamber capacity.
The liquid chamber capacity is the total accumulator volume minus the minimum gas
volume.

Inlet liquid resistance, and separator properties such as inertia and damping are not
modeled. The flow rate is positive if liquid flows into the accumulator.

This diagram represents a gas-charged accumulator. The total accumulator volume,
`VT`, is divided into the liquid chamber
on the left and the gas chamber on the right by the vertical separator. The distance
between the left side and the separator defines the liquid volume,
`VL`. The distance between the right
side and the separator defines the gas volume,
`VG`. The liquid chamber capacity,
`VC`, is less than the total accumulator
volume, so that the gas volume never becomes zero:

VL=VT−VGVC=VT−Vdead

where:

- *VT* is the total volume of the
  accumulator, including the liquid chamber and the gas chamber.
- *VL* is the volume of the liquid
  in the accumulator.
- *VG* is the volume of the gas in
  the accumulator.
- *VC* is the liquid chamber
  capacity.
- *Vdead* is the gas chamber dead
  volume, a small portion of the gas chamber that remains filled with gas when
  the liquid chamber is at capacity.

The hard stop contact pressure is modeled with a stiffness term and a
damping term. The relationship of the gas pressure and gas volume between the current
state and the precharge state is polytropic and pressure is balanced at the
separator:

pGVGksh=pprVTksh,

where:

- *pG* is the gas pressure in the
  gas chamber.
- *ppr* is the pressure in the gas
  chamber when the liquid chamber is empty
- *ksh* is the specific heat ratio
  (adiabatic index).

### Conservation of Mass

The mass conservation in the block is

{p˙IdρIdpIVL+ρIV˙L=m˙A,     compressibility onρ0V˙L=m˙A,                       compressibility off

where:

- *pI* is the liquid pressure in
  the liquid chamber, which is equal to the pressure at the accumulator
  inlet.
- m˙A is the mass flow rate of
  liquid coming into port **A**.
- *ρI* is the density of the
  liquid in the liquid chamber.
- *ρ0* is the constant liquid
  density. The block calculates this value from **Precharge
  pressure** parameter.

V˙L={p˙IkshpGVG,            if 0 <VL<VCp˙IkshpGVG+Kstiff,                  else

where *Kstiff* is the
hard-stop stiffness coefficient.

### Conservation of Momentum

Conservation of momentum is represented by:

pI=pG+pHS

where *pHS* is the hard-stop contact
pressure.

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
