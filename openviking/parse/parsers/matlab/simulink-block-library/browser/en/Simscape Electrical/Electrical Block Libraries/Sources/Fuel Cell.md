---
type: simulink-block
title: 'Fuel Cell'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'fuelcell'
documentation_source_path: 'ref/fuelcell.html'
language: en
---

# Fuel Cell

## Ports

### Input

### **pfuel** — Supply absolute pressure of fuel, bar physical signal

Physical signal port associated with the supply absolute pressure of
the fuel, in `bar`, specified as a physical
signal.

#### Dependencies

To enable this port, set **Model fidelity** to
`Detailed with physical inputs`.

### **pair** — Supply gauge pressure of air, bar physical signal

Physical signal port associated with the supply gauge pressure of air,
in `bar`, specified as a physical
signal.

#### Dependencies

To enable this port, set **Model fidelity** to
`Detailed with physical inputs`.

### **qfuel** — Fuel flow rate, l/min physical signal

Physical signal port associated with the fuel flow rate, specified as
a physical signal.

#### Dependencies

To enable this port, set **Model fidelity** to
`Detailed with physical inputs`.

### **qair** — Air flow rate, l/min physical signal

Physical signal port associated with the air flow rate, specified as a
physical signal.

#### Dependencies

To enable this port, set **Model fidelity** to
`Detailed with physical inputs`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the fuel cell positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the fuel cell negative
terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Model fidelity** to
`Detailed with physical inputs`.

## Parameters

### Main

### **Model fidelity** — Fuel cell fidelity `Detailed with physical inputs` (default) | `Simplified - nominal conditions`

Level of fidelity of the fuel cell model.

### **Open-circuit voltage** — Open-circuit voltage `65` `V` (default) | positive scalar

Open-circuit voltage.

When the amount of flow is very low or close to zero and the values of
the fuel and air pressures are equal to their nominal values, the output
voltage of the fuel cell is equal to the open-circuit voltage multiplied
by the number of module units. The current that flows out of the fuel
cell is negligible. This figure shows how to set the open-circuit test:

### **Tafel slope** — Tafel slope `0.23` `V` (default) | positive scalar

Amount of overpotential required to
increase the reaction rate by a factor ten.

### **Internal resistance** — Internal resistance `0.05` `Ohm` (default) | positive scalar

Internal resistance.

### **Nominal exchange current** — Nominal exchange current `80` `A` (default) | positive scalar

Exchange current at the nominal temperature.

At the nominal exchange current, the fuel cell leaves the region of
activation polarization and enters the region of ohmic polarization.

### **Collapse current** — Collapse current `200` `A` (default) | positive scalar

Value of current at which the fuel cell voltage becomes zero. As the fuel cell enters
the region of concentration polarization and the current continues to
increase, the voltage starts decreasing at a faster rate.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Number of cells per module** — Number of cells per module `65` (default) | positive scalar

Number of cells per module.

The cell count value in this block is consistent with the fuel cell
delivering its maximum output power for specified set points of flow and
H2 pressure.

### **Module units (Series)** — Stack of module units in series `10` (default) | positive scalar

Stack of module units in series.

Stack module in series to scale up voltage. For example, 10 module
units in series with an open-circuit voltage of 65 V deliver a voltage
of 650V.

### Supply

To enable these parameters, in the **Main** tab, set **Model
fidelity** to `Detailed with physical
inputs`.

### **Nominal H2 pressure** — Nominal hydrogen pressure `1.5e5` `Pa` (default) | positive scalar

Hydrogen gauge pressure at nominal temperature.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Nominal O2 pressure** — Nominal oxygen pressure `1.0e5` `Pa` (default) | positive scalar

Oxygen gauge pressure at nominal temperature.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Concentration H2 in fuel (%)** — Hydrogen concentration in fuel `99` (default) | integer between `0` and `100`

Molar fraction concentration of hydrogen in fuel, in percent.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Concentration O2 in air (%)** — Oxygen concentration in fuel `21` (default) | integer between `0` and `100`

Molar fraction concentration of oxygen in fuel, in percent.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Concentration vapor in air (%)** — Vapor concentration in air `1` (default) | integer between `0` and `100`

Molar fraction concentration of vapor in air, in percent.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### Dynamics

### **Model activation delay** — Activation delay modeling option `No` (default) | `Yes`

Whether to model the activation delay of the fuel cell.

### **Sum of activation and concentration resistance** — Sum of activation and concentration resistance `0.005` `Ohm` (default) | positive scalar

Sum of the activation resistance and concentration resistance.

#### Dependencies

To enable this parameter, set **Model activation
delay** to `Yes`.

### **Time constant** — Time constant `10` `s` (default) | positive scalar

Time constant.

#### Dependencies

To enable this parameter, set **Model activation
delay** to `Yes`.

### Thermal

To enable these parameters, in the **Main** tab, set **Model
fidelity** to `Detailed with physical
inputs`.

### **Nominal temperature** — Nominal temperature `293.15` `K` (default) | scalar

Temperature at which the nominal parameters are measured.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

### **Thermal mass** — Thermal mass associated with thermal port H `30000` `J/K` (default) | positive scalar

Thermal mass associated with the thermal port, **H**.
This value represents the energy required to raise the temperature of
the thermal port by one degree.

#### Dependencies

To enable this parameter, set **Model fidelity**
to `Detailed with physical inputs`.

## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Fuel cell electrical system

The Fuel Cell block models a fuel cell that converts the
chemical energy of hydrogen into electrical energy.

This chemical reaction defines the electrical conversion:

H2+12O2→H2O+heat

which occurs due to these anode and cathode half-reactions:

H2→2H++2e−12O2+2H++2e−→H2O

A fuel cell stack comprises several series-connected fuel cells. This figure shows the
equivalent circuit of a single fuel cell that this block uses

where:

- *VFC* is the cell voltage.
- *Ri* is the **Internal
  resistance**.
- *Rd* is the **Sum of
  activation and concentration resistances**.
- *Cdl* is the parallel RC
  capacitance that accounts for time dynamics in the cell.

### Equations

You can use the **Model fidelity** parameter to set the
Fuel Cell block to two different levels of fidelity:

- `Simplified - nominal conditions` — The block
  calculates the Nernst voltage at the nominal condition of temperature
  and pressure.
- `Detailed with physical inputs` — The block
  calculates the Nernst voltage by considering the pressures and flow
  rates of fuel and air.

**Simplified Electrical Model**

When **Model fidelity** is set to `Simplified - nominal
conditions`, the Fuel Cell block
calculates the Nernst voltage, *E*, at the nominal condition of
temperature and pressure, as defined by these equations:

E=Eoc−NAln(iFCi0)vFC=NunitE−RiiFC−vd1Rd(τdvddt+vd)=iFC

where:

- *Eoc* is the
  **Open-circuit voltage**.
- *N* is the **Number of cells per
  module**.
- *iFC* is the current that
  the fuel cell generates.
- *vFC* is the voltage
  across the fuel cell terminals.
- *Nunit* is the
  **Module units (Series)**.
- *vd* is the voltage drop
  that accounts for fuel cell dynamics.
- *A* is the **Tafel slope**, in
  volts.
- *i0* is the
  **Nominal exchange current**.
- τ=RdCdl.

**Detailed Electrical Model**

When **Model fidelity** is set to `Detailed with physical
inputs`, the Fuel Cell block
calculates the Nernst voltage, *E*, by considering the
pressures and flow rates of fuel and air.

These equations determine the rates of utilization of hydrogen,
*UH2*,
and oxygen, *UO2*

UH2=60000NiFCVepfuelqfuelxH2UO2=60000NiFCVe2pairqairxO2

where:

- *Ve* is the thermal
  voltage at room temperature.
- *pfuel* is the supply
  pressure of the fuel, in `bar`.
- *qfuel* is the fuel flow
  rate.
- *xH2*
  is the concentration of hydrogen in the fuel, in percent.
- *pair* is the supply
  pressure of air, in `bar`.
- *qair* is the air flow
  rate.
- *xO2*
  is the concentration of oxygen in the air, in percent.

These equations define the partial pressures:

pH2=pfuelxH2−UH2pO2=pairxO2−UO2pH2O=pairxH2O−2UO2

where
*xH2O* is
the concentration of vapor in air, in percent.

Then, the block computes the Nernst voltage as

where:

- Kz=Eoc\_admKcN−1.229(Tnom−298)−44.43z0F+RTnomz0Fln(pnH2pnO212).
- ETafel=NATln(iFCi0) is the electrokinetic term for the
  activation.
- Econc=VeT298ln(ilimilim−iFC) is the electrokinetic term for the
  concentration.
- Eoc\_adm=max(Eoc,N(1.229+RTnom2Fln(pnH2pnO212))).
- *Kc* is the voltage
  constant at nominal condition of operation.
- *T* is the operating temperature of the fuel
  cell.
- *Tnom* is the value of the
  **Nominal temperature** parameter.
- *z* is the number of moving electrons per
  second.
- *z0* is the number of
  moving electrons per second at the value of the **Nominal
  exchange current** parameter.
- *F* is the Faraday constant.
- *R* is the universal gas constant.
- *pnH2*
  is the nominal hydrogen pressure, in
  `bar`.
- *pnO2*
  is the nominal oxygen pressure, in
  `bar`.
- AT=ATln(10)∗298 is the Tafel slope as a function of the
  temperature.
- *ilim* is the value of the
  **Collapse current** parameter.
- The voltage `1.229` represents the standard cell
  potential for the Nernst equation.

The block computes the power dissipated, or the heat released in the fuel cell, by using
this equation

Pdissipated=Ze\_agg(TΔS)+RiiFC+vd21Rd

where:

- Ze\_agg=(NunitE−RiiFC−vd)iFC2ΔG is the total electron circulation rate, in
  `mol/s`.
- *TΔS* is the change in entropy of the fuel cell
  reaction, in `kJ/(mol*K)`, at the operating
  temperature of the fuel cell.
- *ΔG* is the change in Gibbs free energy of the
  full fuel cell reaction, in `kJ/mol`, at
  the operating temperature of the fuel cell.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
