---
type: simulink-block
title: 'Electrolyzer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'electrolyzer'
documentation_source_path: 'ref/electrolyzer.html'
language: en
---

# Electrolyzer

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: purge
  summary: Purge logic input, unitless physical signal
  direction: input
- name: vol
  summary: Water volume, m^3 physical signal
  direction: input
- name: T
  summary: Water temperature, K physical signal
  direction: input
- name: volPurging
  summary: Purged water volume, m^3 physical signal
  direction: output
- name: pH
  summary: Water pH, unitless physical signal
  direction: output
- name: mdotH2
  summary: Mass flow rate of hydrogen, g/s physical signal
  direction: output
- name: mdotH2O
  summary: Mass flow rate of consumed water, g/s physical signal
  direction: output
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the anode of the
electrolyzer tank.

### **-** — Negative terminal electrical

Electrical conserving port associated with the cathode of the
electrolyzer tank.
### Input

### **purge** — Purge logic input, unitless physical signal

Purge logic input, specified as a physical signal. This signal enables
the substitution of the water in the tank.

### **vol** — Water volume, m^3 physical signal

Water volume in the electrolyzer tank, in
m3, specified as a physical
signal.

### **T** — Water temperature, K physical signal

Water temperature, in K, specified as a physical signal.
### Output

### **volPurging** — Purged water volume, m^3 physical signal

Volume of water consumed for purging, in
m3, specified as a physical signal.

### **pH** — Water pH, unitless physical signal

Water pH in the electrolyzer tank, specified as a physical
signal.

### **mdotH2** — Mass flow rate of hydrogen, g/s physical signal

Mass flow rate of the hydrogen, in g/s, specified as a physical
signal.

### **mdotH2O** — Mass flow rate of consumed water, g/s physical signal

Mass flow rate of the consumed water, in g/s, specified as a physical
signal.
## Parameters
```yaml
parameters:
- name: Assumption pH
  summary: Constant or dynamic pH Constant (default) | Dynamic
  group: ''
- name: Resistance
  summary: External resistance 10 Ohm (default) | nonnegative scalar
  group: ''
- name: Cross-sectional transport area
  summary: Cross-sectional transport area 0.04 m^2 (default) | positive scalar
  group: ''
- name: Distance anode-cathode
  summary: Distance between anode and cathode 0.01 m (default) | positive scalar
  group: ''
- name: Number of cells
  summary: Number of cells 50 (default) | positive scalar
  group: ''
- name: Initial pH
  summary: Initial pH 0 (default) | scalar
  group: ''
- name: Constant pH
  summary: Constant pH 6 (default) | scalar
  group: ''
- name: pH vector, pH_vec
  summary: pH vector [5, 5.5, 6, 6.5, 7] (default) | row vector of positive scalars
  group: ''
- name: Electrical resistivity vector, rho_vec
  summary: Electrical resistivity vector [.2, .75, 2.5, 8, 18.2] MOhm*cm (default) | vector of scalars
  group: ''
- name: Temperature vector for efficiency, T_vec
  summary: Efficiency temperature vector [273, 298, 323, 348, 373] K (default) | vector of scalars
  group: ''
- name: Electrolysis efficiency vector, efficiency(T)
  summary: Electrolysis efficiency vector ones(5, 1) (default) | vector of scalars
  group: ''
```

### **Assumption pH** — Constant or dynamic pH `Constant` (default) | `Dynamic`

Whether to assume constant or dynamic pH in the electrolyzer tank.

### **Resistance** — External resistance `10` `Ohm` (default) | nonnegative scalar

Amount of external resistance.

### **Cross-sectional transport area** — Cross-sectional transport area `0.04` `m^2` (default) | positive scalar

Normal area to the vector that links the anode and the cathode. Positively
charged ions travel across this area from anode to cathode, where they get
reduced and the hydrogen is produced.

### **Distance anode-cathode** — Distance between anode and cathode `0.01` `m` (default) | positive scalar

Distance between the anode and the cathode, submerged in the electrolytic
solution.

### **Number of cells** — Number of cells `50` (default) | positive scalar

Number of cells in the electrolyzer.

### **Initial pH** — Initial pH `0` (default) | scalar

Initial pH value of the water in the tank.

### **Constant pH** — Constant pH `6` (default) | scalar

Constant pH value of the water in the tank.

#### Dependencies

To enable this parameter, set **Assumption pH** to
`Constant`.

### **pH vector, pH\_vec** — pH vector `[5, 5.5, 6, 6.5, 7]` (default) | row vector of positive scalars

Vector of pH values. This parameter must have the same number of elements
as the **Electrical resistivity vector, rho\_vec**
parameter.

#### Dependencies

To enable this parameter, set **Assumption pH** to
`Dynamic`

### **Electrical resistivity vector, rho\_vec** — Electrical resistivity vector `[.2, .75, 2.5, 8, 18.2]` `MOhm*cm` (default) | vector of scalars

Vector of electrical resistivity values. This parameter must have the same
number of elements as the **pH vector, pH\_vec**
parameter.

#### Dependencies

To enable this parameter, set **Assumption pH** to
`Dynamic`

### **Temperature vector for efficiency, T\_vec** — Efficiency temperature vector `[273, 298, 323, 348, 373]` `K` (default) | vector of scalars

Vector of temperatures for efficiency. This parameter must have the same
number of elements as the **Electrolysis efficiency vector,
efficiency(T)** parameter.

### **Electrolysis efficiency vector, efficiency(T)** — Electrolysis efficiency vector `ones(5, 1)` (default) | vector of scalars

Vector of electrolysis efficiency values. This parameter must have the
same number of elements as the **Temperature vector for efficiency,
T\_vec** parameter.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024a: The **Number of electrode pairs** parameter has been removed

The **Number of electrode pairs** parameter has been
removed.

## Description

Electric load for electrolyzer

The Electrolyzer block represents the electric load
associated with an electrolyzer. An electrolyzer consists of an anode and a cathode
separated by an electrolyte. The block calculates the amount of produced hydrogen based
on the electrical energy provided and the water temperature in the tank.

In polymer electrolyte membrane (PEM) electrolyzers, these chemical reactions define
the anode and cathode conversions:

2H2O→O2+4H++4e−

4H++4e−→2H2

An electrolysis stack comprises several series-connected individual
electrolyzer cells. Specify the **Assumption pH** parameter to model
this block either in a pH-dependent state or in an ideal state with constant pH.

### Equations

The Electrolyzer block calculates the electrical power by using

PE=v2RT,

where *v* is the voltage and
*RT* is the total resistance. The
total resistance, *RT*, is defined by

1RT=1Rel+1R,

where:

- *R* is the external resistance.
- Rel=ρ(pH)xA. This value is a resistive term obtained from the
  cross-sectional transport area, *A*, the distance
  anode-cathode, *x*, and the electrical resistivity of
  the solution, *ρ(pH)*.

The molar energy stored across the electrical load enables the process of water
electrolysis and is calculated by this equation:

GE=PE1 mol/s.

To accomplish electrolysis, the electrolyzer requires a minimum
amount of energy

Gmin=ΔH−TT0TΔS,

where:

- *ΔH* is the water enthalpy.
- *TΔS* is the reaction
  entropy.
- *T* is the water temperature.
- *T0* is the reference
  temperature.

If the electrical energy is not sufficient to dissociate the water, the
electrolyzer does not produce hydrogen. Therefore, the Electrolyzer block calculates
the mole rate of electron, *mole*, and the
mole rate of hydrogen, *molH2*

mole={μ(GE−Gmin)eVNAGE>Gmin0GE≤Gmin

molH2={Ncmole2,GE>Gmin0,GE≤Gmin

where:

- *NA* is the Avogadro
  constant.
- *eV* is the energy per
  electron.
- *Nc* is the number of
  cells.
- *μ* is the temperature-dependent efficiency of the
  electrolysis.

The current that flows through the electrolyzer tank is then obtained as

i=moleF,

where *F* is the Faraday constant.

The Electrolyzer block calculates the mass rates of consumed water and generated
hydrogen by using these equations:

m˙H2 O=molH2MH2 Om˙H2=molH2MH2

where *MH2O* is the molar
mass of water and *MH2* is the molar mass of
hydrogen.

To compute the pH of the water in the tank, the block uses

pH=−ln(xhpmolH2\_acc),

where:

- xhp={∫mole,pH assumed constant∫(1−purge)mole,pH assumed dynamic captures the floating hydrons (H+) in the
  solution.
- molH2\_acc=VρH2 O(T)MH2 O is the number of moles of water.
- *V* is the volume.
- *ρH2O(T)* is the density of
  the water in the tank.

The residual protons in the solution inside the electrolyzer naturally increases
the pH and conductivity of the water in the tank over time. The increase in
conductivity leads to a run-away phenomenon. To prevent the run-away, you must purge
the water in the tank by taking out the volume of the tank and fill it with clean
water.
