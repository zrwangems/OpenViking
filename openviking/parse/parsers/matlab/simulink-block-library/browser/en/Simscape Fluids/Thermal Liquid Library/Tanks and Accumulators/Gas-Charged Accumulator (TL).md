---
type: simulink-block
title: 'Gas-Charged Accumulator (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Tanks and Accumulators'
documentation_page: 'gaschargedaccumulatortl'
documentation_source_path: 'ref/gaschargedaccumulatortl.html'
language: en
---

# Gas-Charged Accumulator (TL)

## Ports

### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port associated with the accumulator inlet.
The flow rate is positive if liquid flows into the accumulator.

### **H** — Heat port thermal

Thermal conserving port associated with the thermal mass of the liquid
volume.

## Parameters

### **Total accumulator volume** — Accumulator volume `8e-3` `m^3` (default) | positive scalar

Total volume of the accumulator, including the liquid chamber and the gas
chamber. This is the sum of the liquid chamber capacity and the minimum gas
volume.

### **Minimum gas volume** — Gas chamber dead volume `4e-5` `m^3` (default) | positive scalar

Gas chamber dead volume. This is the amount of remaining gas when the
liquid chamber is full. A nonzero volume is necessary so that the gas
pressure does not become infinite when the liquid chamber is full.

### **Precharge pressure (gauge)** — Gas chamber pressure `0` `MPa` (default) | nonnegative scalar

Initial gauge pressure of the empty accumulator chamber. Fluid enters the
accumulator if the inlet pressure is equal to or greater than the precharge
pressure.

### **Specific heat ratio** — Specific heat ratio `1.4` (default) | positive scalar

Specific heat ratio for the gas in the chamber. This value is typically
1.4 for air at 20°C.

### **Cross-sectional area at port A** — Inlet cross-sectional area `0.01` `m^2`positive scalar (default)

Flow cross-sectional area at the accumulator inlet.

### **Hard stop stiffness coefficient** — Stiffness coefficient `1e4` `MPa/m^3` (default) | positive scalar

Stiffness coefficient of the top and bottom accumulator hard stops. The
hard stops restrict diaphragm motion between zero and the maximum liquid
chamber level.

### **Hard-stop damping coefficient** — Damping coefficient `1e4` `MPa*s/m^6` (default) | positive scalar

Damping coefficients of the top and bottom accumulator hard stops. The
hard stops restrict diaphragm motion between zero and the maximum liquid
chamber level. The damping coefficients account for the dissipative portion
of the hard-stop contact forces.

## Libraries

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Gas-charged accumulator in a thermal liquid network

The Gas-Charged Accumulator (TL) block represents a pressurized thermal
liquid container with a compressed gas charge. The accumulator consists of thermal
liquid and gas chambers separated by a hermetic and insulated diaphragm.

**Accumulator Schematic**

A diaphragm separates the gas sealed gas chamber from the liquid chamber with a port. There are hard stops near the top and bottom of the accumulator.

If the inlet pressure is greater than the gas charge pressure, the liquid chamber
volume increases, compressing the gas chamber. If the inlet pressure is lower than the
gas charge pressure, the liquid chamber volume decreases, decompressing the gas
chamber.

Hard stops limit the diaphragm motion when the liquid chamber is at capacity and when
the liquid chamber is empty. If the specified spring stiffness is too low, the liquid
volume can momentarily fall below zero or rise above capacity. Use the **Hard
stop stiffness coefficient** parameter to correct this.

### Mass Balance

The mass conservation equation in the liquid chamber is

VLρL(1βLdpLdt−αLdTLdt)+ρLdVLdt=m˙A,

where:

- *ρ*L is the thermal liquid
  density.
- *β*L is the isothermal bulk
  modulus.
- *α*L is the isobaric thermal
  expansion coefficient.
- *p*L is the thermal liquid
  pressure.
- *T*L is the thermal liquid
  temperature.
- m˙A is the thermal liquid mass flow rate into the
  accumulator through port **A**.

The block computes the time variation of the liquid chamber volume using the
conditional equation

dVLdt={p˙LkpprVTkVG(−k−1)+Ks+Kdm˙+/ρL,VL≥VCp˙LkpprVTkVG(−k−1)+Ks−Kdm˙−/ρL,VL≤0p˙LkpprVTkVG(−k−1),Else,

where:

- *Ks* is the
  **Hard-stop stiffness coefficient**
  parameter.
- *Kd* is the
  **Hard-stop damping coefficient** parameter.
- m˙+ is the mass flow rate into the liquid chamber when the
  accumulator diaphragm contacts the top hard stop:

  m˙+={m˙,m˙>00,Else,
- m˙− is the mass flow rate from the liquid chamber when the
  accumulator diaphragm contacts the bottom hard stop:

  m˙−={m˙,m˙<00,Else,

### Momentum Balance

The momentum conservation equation in the accumulator volume is

pL=pG+pHS,

where *pHS* is the
hard-stop contact pressure:

- pHS={(VL−VC)(Ks+Kdm˙+/ρ),VL≥VCVL(Ks−Kdm˙−/ρ),VL≤00,Else,

### Energy Balance

The energy conservation equation in the liquid chamber volume is

ddt(ρLuLVL)=ϕA+ϕH,

where:

- *u*L is the thermal liquid
  specific internal energy.
- *Φ*A is the energy flow rate
  into the liquid chamber through the accumulator inlet.
- *Φ*H is the thermal energy
  flow rate into the liquid chamber through the accumulator wall.

### Chamber Volumes

The liquid chamber volume is the difference between the total accumulator volume
and the gas chamber volume:

VL=VT−VG,

where:

- *V*L is the liquid chamber
  volume.
- *V*T is the total accumulator
  volume.
- *V*G is the gas chamber
  volume.

**Chamber Volumes**

The figure shows a diagram of the accumulator volume measurements.

The liquid chamber capacity is the difference between the total accumulator volume
and the dead volume of gas in the accumulator at full capacity:

VC=VT−VDead,

where:

- *V*C is the liquid chamber
  capacity.
- *V*Dead is the dead volume of
  gas at full capacity.

The gas chamber pressure and volume follow from the precharge states as described
by the polytropic equation

pGVGk=pprVTk,

where:

- *p*G is the gas chamber
  pressure at a given time step.
- *V*G is the gas chamber volume
  at a given time step.
- *p*pr is the precharge gas
  chamber pressure when the liquid chamber is empty.
- *V*T is the total liquid
  chamber volume.
- *k* is the polytropic index.

### Initial Targets

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

- The block treats the gas chamber compression as a polytropic
  process.
- The block ignores diaphragm loading.
- The block ignores the effects of fluid inertia.
