---
type: simulink-block
title: 'Ejector (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'ejectorma'
documentation_source_path: 'ref/ejectorma.html'
language: en
---

# Ejector (MA)

## Ports
```yaml
ports:
- name: A
  summary: Primary inlet moist air
  direction: conserving
- name: B
  summary: Outlet moist air
  direction: conserving
- name: S
  summary: Secondary inlet moist air
  direction: conserving
```

### Conserving

### **A** — Primary inlet moist air

Moist air conserving port associated with the primary nozzle
inlet.

### **B** — Outlet moist air

Moist air conserving port associated with the diffuser outlet.

### **S** — Secondary inlet moist air

Moist air conserving port associated with the secondary inlet.
## Parameters
```yaml
parameters:
- name: Primary nozzle throat area
  summary: Area of primary nozzle throat 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Area ratio of nozzle exit to throat
  summary: Ratio of areas of nozzle exit to nozzle throat 3 (default) | positive scalar
  group: ''
- name: Area ratio of mixing chamber to throat
  summary: Ratio of areas of mixing chamber to throat 8 (default) | positive scalar
  group: ''
- name: Minimum area ratio of secondary throat to primary throat
  summary: Limit on ratio of aerodynamic areas of secondary throat to primary throat 0.1 (default) | positive scalar
  group: ''
- name: Report when secondary throat area falls below minimum
  summary: Notification when secondary throat area is below minimum Warning (default) | None | Error
  group: ''
- name: Efficiency for primary flow through nozzle
  summary: Efficiency factor of primary flow through nozzle 0.95 (default) | positive scalar
  group: ''
- name: Efficiency for secondary suction flow
  summary: Efficiency factor of secondary suction flow 0.85 (default) | positive scalar
  group: ''
- name: Efficiency for primary flow expansion
  summary: Efficiency factor of primary flow expansion 0.88 (default) | positive scalar
  group: ''
- name: Efficiency for mixing
  summary: Efficiency factor for mixed flow velocity due to mixing 0.84 (default) | positive scalar
  group: ''
- name: Cross-sectional area at port A
  summary: Cross-sectional area of port A 0.01 m^2 (default) | positive scalar
  group: ''
- name: Cross-sectional area at port B
  summary: Cross-sectional area of port B 0.01 m^2 (default) | positive scalar
  group: ''
- name: Cross-sectional area at port S
  summary: Cross-sectional area of port S 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Primary nozzle throat area** — Area of primary nozzle throat `1e-4` `m^2` (default) | positive scalar

Area of the throat for the primary flow nozzle.

### **Area ratio of nozzle exit to throat** — Ratio of areas of nozzle exit to nozzle throat `3` (default) | positive scalar

Ratio of the area of the nozzle exit to the area of the nozzle throat.
This parameter limits how big the secondary aerodynamic throat can be.

### **Area ratio of mixing chamber to throat** — Ratio of areas of mixing chamber to throat `8` (default) | positive scalar

Ratio of the area of the mixing chamber to the area of the throat. The
difference between the mixing chamber area and the expanded jet area of the
primary flow creates a fictitious aerodynamic throat for the secondary
flow.

### **Minimum area ratio of secondary throat to primary throat** — Limit on ratio of aerodynamic areas of secondary throat to primary throat `0.1` (default) | positive scalar

Minimum aerodynamic area ratio for the secondary throat to the primary
throat. The block does not allow the area of the fictitious aerodynamic
throat to go below this value. To avoid hitting this minimum, increase the
value of the **Area ratio of mixing chamber to throat**
parameter.

### **Report when secondary throat area falls below minimum** — Notification when secondary throat area is below minimum `Warning` (default) | `None` | `Error`

Whether the block does nothing, generates a warning, or generates an error when the
secondary throat area falls below the minimum, specified by the
**Minimum area ratio of secondary throat to primary
throat** parameter.

### **Efficiency for primary flow through nozzle** — Efficiency factor of primary flow through nozzle `0.95` (default) | positive scalar

Empirical factor that accounts for reduction in primary mass flow rate due
to losses in the primary nozzle.

### **Efficiency for secondary suction flow** — Efficiency factor of secondary suction flow `0.85` (default) | positive scalar

Empirical factor that accounts for reduction in secondary mass flow rate due to losses in
the suction of the secondary flow.

### **Efficiency for primary flow expansion** — Efficiency factor of primary flow expansion `0.88` (default) | positive scalar

Empirical factor that accounts for reduction in the expansion of the
primary flow jet due to mixing losses.

### **Efficiency for mixing** — Efficiency factor for mixed flow velocity due to mixing `0.84` (default) | positive scalar

Empirical factor that accounts for reduction in the mixed flow velocity
due to losses in the mixing chamber.

### **Cross-sectional area at port A** — Cross-sectional area of port A `0.01` `m^2` (default) | positive scalar

Cross-sectional area of port **A**.

### **Cross-sectional area at port B** — Cross-sectional area of port B `0.01` `m^2` (default) | positive scalar

Cross-sectional area of port **B**.

### **Cross-sectional area at port S** — Cross-sectional area of port S `0.01` `m^2` (default) | positive scalar

Cross-sectional area of port **S**.
## Libraries

Simscape / Fluids / Moist Air / Turbomachinery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To
model water droplets, select **Enable entrained water droplets** in the
Moist Air Properties
(MA) block connected to your moist air network.

## Description

Ejector in a moist air network

The Ejector (MA) block models an ejector in a moist air network. The ejector forces the
high-pressure primary flow through a nozzle with a specific throat area, which creates
a low-pressure jet that draws in the secondary flow. The expansion of the primary jet
creates a throat for the secondary flow. The block assumes that the two flows mix under
uniform pressure and the combined flow exits through a diffuser to recover pressure. The
primary and secondary flows must contain the same moist air species but may have
different compositions.

You can use an ejector as a pump or compressor to drive a secondary fluid. Unlike a pump or
compressor, there is no external source of mechanical energy, and the high pressure
primary fluid is the energy source that drives the secondary fluid.

### Ejector Geometry

The high-pressure primary flow enters the ejector at location p and flows through a
convergent-divergent nozzle with throat area
*Spt*, which is the value of the
**Primary nozzle throat area** parameter. The ejector chokes
the primary flow at the throat (location pt) and accelerates the flow to a
low-pressure supersonic jet at the primary nozzle exit (location pn). The low
pressure of the supersonic primary flow jet draws in the secondary flow at location
s around the nozzle.

The supersonic primary flow jet continues to expand and decrease in pressure
beyond the nozzle exit until it reaches its largest area at the expanded primary
flow jet (location pe). The expansion of the supersonic primary flow jet creates a
fictitious aerodynamic throat for the secondary flow at location st, which is at the
same location as pe. The secondary flow also chokes at the aerodynamic throat. After
passing the aerodynamic throat, the primary and secondary flow mix under uniform
pressure (location m). If the mixed flow is still supersonic, the flow causes a
shock in the mixing chamber at location s and the diffuser (location d) decelerates
the mixed flow to raise the outlet pressure.

This schematic describes the ejector where:

- Location p is the primary inlet.
- Location s is the secondary inlet.
- Location pt is the primary nozzle throat.
- Location pn is the primary nozzle exit.
- Location pe is the expanded primary flow jet.
- Location st is the secondary aerodynamic throat.
- Location m is the mixed flow.
- Location ms is the shock in the mixing chamber.
- Location d is the diffuser outlet.

Diagram of ejector showing the locations of the primary and secondary flow, inlet, throat, mixing, and shock.

### Mass Flow Rate

The ejector accelerates the primary moist air flow through the nozzle. The mass
flow rate of the primary flow is

m˙p=Spt(2γγ−1)ηpppρp[(pmpp)2γ−(pmpp)γ+1γ],

where:

- *Spt* is the value of the
  **Primary nozzle throat area** parameter.
- γ=cpcv is the ratio of heat capacities where
  *cp* is the specific
  heat at constant pressure and
  *cv* is the specific heat at
  constant volume.
- *ηp* is the value of the
  **Efficiency for primary flow through nozzle**
  parameter.
- *pp* is the pressure at the
  primary flow inlet.
- *pm* is the pressure after the
  primary and secondary flow mix.
- *ρp* is the density at the
  primary flow inlet.

The primary flow draws the secondary moist air flow into the suction chamber and
accelerates it towards the fictitious aerodynamic throat created by the expanding
primary jet. The mass flow rate of the secondary flow is

m˙s=Sst(2γγ−1)ηspsρs[(pmps)2γ−(pmps)γ+1γ],

where:

- *Sst* is the area of the
  fictitious aerodynamic throat. The block calculates the value based on
  the expansion of the primary flow jet.
- *ηs* is the value of the
  **Efficiency for secondary suction flow**
  parameter.
- *ps* is the pressure at the
  secondary flow inlet.
- *ρs* is the density at the
  secondary flow inlet.

When pmpp<Bcrit, where Bcrit=(2γ+1)γγ−1, the primary flow becomes choked and the mass flow rate reaches the
maximum value

m˙p\*=Sptηpppρpγ(2γ+1)γ+1γ−1.

When pmps<Bcrit, the secondary flow becomes choked and the mass flow rate reaches
the maximum value

m˙s\*=Sstηspsρsγ(2γ+1)γ+1γ−1.

### Primary and Secondary Flow Relations

The flow area expansion of the supersonic primary flow jet comes from the relation

SpeSpt=Ψpe(γ−12)(2γ+1)γ+1γ−1(pmpp)2γ−(pmpp)γ+1γ,

where *ψpe* is the value of the
**Efficiency for primary flow expansion** parameter.

The block uses the area of the expanded supersonic primary flow jet,
*Spe*, to calculate the flow area of
the fictitious secondary flow aerodynamic throat,
*Sst*

SstSpt=SmSpt−max{SpeSpt,SpmSpt},

where:

- SmSpt is the value of the **Area ratio of mixing
  chamber to throat** parameter.
- SpnSpt is the value of the **Area ratio of nozzle
  exit to throat** parameter.

The primary flow velocity of the expanded jet is

vpe=2γγ−1(ppρp)[1−(pmpp)γ−1γ].

The secondary flow velocity at the aerodynamic throat is

vst=2γγ−1(psρs)[1−(pmps)γ−1γ].

The secondary flow velocity is limited to the choked value. When pmps<Bcrit,, the secondary flow reaches the maximum value of

vst\*=2γγ+1(psρs).

### Mixing Model

After the fictitious aerodynamic throat, the primary and secondary flows mix under
uniform pressure. The mixed flow temperature is

Tm=m˙pTp+m˙sTsm˙m−γ−12γRvm2,

where:

- *Tp* is the primary flow inlet
  temperature. The block assumes that this value is equal to the primary
  flow stagnation temperature because kinetic energy at the inlet is
  negligible relative to the inside of the ejector.
- *Tm* is the mixed flow
  temperature.
- *Ts* is the secondary flow
  inlet temperature. The block assumes that this value is equal to the
  secondary flow stagnation temperature because kinetic energy at the
  inlet is negligible relative to the inside of the ejector.
- *R* is the specific gas constant.
- *vm* is the flow velocity
  after the primary and secondary flow mix.
- m˙m is the mass flow rate after
  the primary and secondary flow mix, meaning m˙m=m˙p+m˙s.

The momentum balance in the mixing region is

pmSm+m˙mvm=pmSpe+m˙pvpe+pmSst+m˙svst,

where *Sm* is the
cross-sectional area after the primary and secondary flow mix.

The pressure terms drop out due to the uniform pressure mixing assumption, and the mixed
flow velocity is

vm=ψmm˙pvpe+m˙svstm˙m,

where *ψm* is the value
of the **Efficiency for mixing** parameter.

The mixed flow Mach number is

Mm=vmγRTm.

### Mixed Diffuser Flow Relations

If the flow is supersonic after mixing, meaning
*MM* > 1, a shock wave occurs. The
pressure rise after the shock is

pmspm=1+2γγ+1(Mm2−1),

where *Mm* is the Mach
number after the primary and secondary flow mix.

The Mach number after the shock is

Mms2=γ−1γ+1(Mm2−1)+12γγ+1(Mm2−1)+1.

After the shock, the diffuser decelerates the flow to raise the pressure. The
block assumes that the kinetic energy at the diffuser outlet is negligible and
decelerates the flow to stagnation pressure at
*pd*:

pdpms=(1+γ−12Mms2)γγ−1.

If *MM* ≤ 1, there is no shock and

pmspm=1Mms2=Mm2.

The relationship between the mixing pressure,
*pm*, and the diffuser outlet pressure,
*pd*, is

pdpm={[γ+12Mm2]γγ−1[2γγ+1(Mm2−1)+1]1γ−1,Mm>1(1+γ−12Mm2)γγ−1,Mm≤1

### Critical Mode Operation

In normal operation, the primary flow is high pressure and is choked during
operation. The block can also operate if the secondary flow is choked. If both the
primary and secondary flows are choked, the block operates in critical mode.

The critical mixing pressure,
*pm\**, is
a low pressure threshold that causes choking in both primary and secondary flow:

pm\*=min{pp,ps}(2γ+1)γγ−1.

The block uses the same equations as above, with
*pm* replaced by
*pm\**, to
calculate the critical diffuser outlet pressure,
*pd\**. If
the actual outlet pressure is greater than the critical diffuser outlet pressure,
then the ejector is subcritical and the block relates the mixing pressure to
diffuser outlet pressure. If the actual outlet pressure is less than the critical
diffuser outlet pressure, then the ejector is critical and the block limits the
mixing pressure to the critical mixing pressure. This means that:

pm={pd(pdpm)pd≥pd\*pm\*pd<pd\*

### Assumptions and Limitations

- The block uses isentropic ideal gas relations to derive the model
  equations.
- The block accounts for losses due to friction, mixing, and expansion waves
  and shocks at the nozzle exit using empirical loss coefficients.
- After the primary flow exits the nozzle, the flows do not mix until the
  primary flow has fully expanded.
- After expansion, the flows mix under uniform pressure.
- Kinetic energy at the primary flow inlet, secondary flow inlet, and
  diffuser outlet are negligible compared to the kinetic energy of the flow
  inside the ejector.
- The flow is steady and one-dimensional.
- The flow is adiabatic.
- Model results with reversed flow may not be accurate.
