---
type: simulink-block
title: 'SPICE NIGBT'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Semiconductors'
documentation_page: 'spicenigbt'
documentation_source_path: 'ref/spicenigbt.html'
language: en
---

# SPICE NIGBT

## Ports

### Conserving

### **gx** — Gate terminal electrical

Electrical conserving port associated with the IGBT gate terminal.

### **cx** — Collector terminal electrical

Electrical conserving port associated with the IGBT collector terminal.

### **ex** — Emitter terminal electrical

Electrical conserving port associated with the IGBT emitter terminal.

## Parameters

### Dimensions

### **Gate-drain overlap area, AGD** — Gate-drain overlap area `5.0e-6` `m^2` (default) | positive scalar

Gate-drain overlap area. The value must be greater than
`0`.

### **Area of the device, AREA** — Device area `1.0e-5` `m^2` (default) | positive scalar

Area of the device. The value must be greater than
`0`.

### **Number of parallel devices, SCALE** — Number of parallel devices `1` (default) | positive integer

Number of parallel transistors the block represents. The value must be
an integer greater than `0`.

### General

### **Electron mobility, MUN** — Mobility of electron `1.5e3` `cm^2/s/V` (default) | scalar

Mobility of the electrons.

### **Hole mobility, MUP** — Mobility of hole `4.5e2` `cm^2/s/V` (default) | scalar

Mobility of the hole.

### **Base doping, NB** — Doping of base `2e14` `1/cm^3` (default) | scalar

Doping of the base.

### MOSFET

### **Triode region factor, KF** — Factor of triode region `1` (default)

Factor of the triode region.

### **MOS transconductance, KP** — MOS transconductance `0.38` `A/V^2` (default) | scalar

The derivative of the drain current with respect to the gate voltage. The value must be
greater than or equal to `0`

### **Threshold voltage, VT** — Threshold voltage `4.7` `V` (default) | scalar

Threshold voltage.

### **Transverse field factor, THETA** — Transverse field factor `0.02` `1/V` (default) | scalar

Transverse field factor.

### BJT

### **Ambipolar recombination lifetime, TAU** — Ambipolar recombination lifetime `7.1e-6` `s` (default) | scalar

Ambipolar recombination lifetime.

### **Metallurgical base width, WB** — Width of metallurgical base `9.0e-5` `m` (default) | scalar

Width of the metallurgical base.

### **Emitter saturation current density, JSNE** — Density of emitter saturation current `6.5e-13` `A/cm^2` (default) | scalar

Density of the emitter saturation current.

### **Avalanche uniformity factor, BVF** — Avalanche uniformity factor `1` (default) | scalar

Avalanche uniformity factor.

### **Avalanche multiplication exponent, BVN** — Avalanche multiplication exponent `4` (default) | scalar

Avalanche multiplication exponent.

### Capacitance

### **Gate-source capacitance per unit area, CGS** — Gate-source capacitance per unit area `1.24e-8` `F/cm^2` (default) | scalar

Gate-source capacitance per unit area.

### **Gate-drain oxide capacitance per unit area, COXD** — Gate-drain oxide capacitance per unit area `3.5e-8` `F/cm^2` (default) | scalar

Gate-drain oxide capacitance per unit area.

### **Gate-drain overlap depletion threshold, VTD** — Gate-drain overlap depletion threshold `1e-3` `V` (default) | scalar

Gate-drain overlap depletion threshold.

### **Specify initial condition** — Whether to specify initial condition `No` (default) | `Yes`

Whether to specify initial condition.

### **Initial condition voltage ICVGE** — Initial condition voltage ICVGE `0` `V` (default) | scalar

Initial condition voltage ICVGE.

#### Dependencies

To enable this parameter, set **Specify initial
condition** to `Yes`.

### **Initial condition voltage ICVCE** — Initial condition voltage ICVCE `0` `V` (default) | scalar

Initial condition voltage ICVCE.

#### Dependencies

To enable this parameter, set **Specify initial
condition** to `Yes`.

### Temperature

### **Model temperature dependence using** — Temperature dependence model `Device temperature` (default) | `Fixed temperature`

Options for modeling the transistor temperature dependence:

- `Device temperature` — Use
  the device temperature to model temperature
  dependence.
- `Fixed temperature` — Use
  a temperature that is independent of the circuit temperature
  to model temperature dependence.

For more information, see Temperature Dependence.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default) | positive scalar

Transistor simulation temperature. The value must be greater than
`0`
`K`.

#### Dependencies

To enable this parameter, set **Model temperature
dependence using** to `Fixed
temperature`.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default) | positive scalar

Temperature at which the transistor parameters are measured. The value must be greater
than `0`
`K`.

### **Offset local circuit temperature, TOFFSET** — Local circuit temperature offset `0` `K` (default) | scalar

Amount by which the transistor temperature differs from the circuit temperature.

#### Dependencies

To enable this parameter, set **Model temperature
dependence using** to `Device
temperature`.

## Libraries

Simscape / Electrical / Additional Components / SPICE Semiconductors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

SPICE-compatible N-Channel insulated gate bipolar transistor

The SPICE NIGBT block models a SPICE n-type insulated gate
bipolar transistor (IGBT).

SPICE, or Simulation Program with Integrated Circuit Emphasis,
is a simulation tool for electronic circuits. You can convert some SPICE subcircuits into
equivalent Simscape™
Electrical™ models using the Environment Parameters block and
SPICE-compatible blocks from the Additional Components library. For more
information, see `subcircuit2ssc`.

This figure shows the equivalent circuit for the SPICE
NIGBT block:

### Equations

Variables for the SPICE NIGBT block equations include:

- Variables that you define by specifying parameters for the
  SPICE NIGBT block.
- Temperature, *T*, which is `300.15`
  `K` by default. You can use a different value
  by specifying parameters for the SPICE
  NIGBT block or by specifying parameters for both the
  SPICE NIGBT block and an
  Environment
  Parameters block. For more information, see Transistor Temperature.

**MOSFET Channel Current**

This table shows the equations that define the relationship between the MOSFET channel
current, *Imos*, and the gate-source
voltage, *Vgs*.

| Applicable Range of *Vgs* Values | Corresponding *Imos* Equation |
| --- | --- |
| Vgs<VT | Imos=GMIN\*Vds\*SCALE |
| Vds≤Vgs−VTKF | Imos=SCALE\*(KF\*KP[(Vgs−VT)Vds−KF\*Vds22]1+THETA\*(Vgs−VT)+GMIN\*Vds) |
| Vds>(Vgs−VT)KF | Imos=SCALE\*(KP(Vgs−VT)22[1+THETA\*(Vgs−VT)]+GMIN\*Vds) |

In these equations:

- *Vds* is the drain-source
  voltage.
- *VT* is the threshold voltage.
- *KF* is the triode region
  factor.
- *KP* is the mosfet
  transconductance.
- *THETA* is the transverse field factor.

**Bipolar Steady-State Collector Current**

This table shows the equations that define the relationship between the steady-state
collector current, *Icss*, and the
emitter-base capacitance,
*Qeb*.

| Applicable Range of *Qeb* Values | Corresponding *Icss* Equation |
| --- | --- |
| Qeb<0 | Icss=0 |
| Qeb≥0 | Icss=[(11+b)IT+(b1+b)(4DpW2)Qeb]\*SCALE |

In these equations:

- b=MUNMUP is the ambipolar mobility ratio.
- Dp=KBTq\*MUP is the diffusion coefficient for holes.
- W=WB−Wbcj is the quasi-neutral base width, where:

  - *WB* is the metallurgical
    base width.
  - Wbcj=2εsiVbc+Vbiq\*NB is the base-collector depletion
    width.
  - *Vbc* is the
    base-collector voltage.
  - *Vbi* is the
    built-in voltage, and it is equal to
    `0.6`
    `V`

**Bipolar Steady-State Base Current**

This table shows the equations that define the relationship between the steady-state base
current, *Ibss*, and the emitter-base
capacitance, *Qeb*.

| Applicable Range of *Qeb* Values | Corresponding *Ibss* Equation |
| --- | --- |
| Qeb<0 | Ibss=0 |
| Qeb≥0 | Ibss=QebTAU+(QebQB)2(4\*NB2ni2)JSNE\*AREA\*SCALE |

In these equations:

- *TAU* is the ambipolar recombination
  lifetime.
- *JSNE* is the emitter saturation current
  density.
- *ni* is the intrinsic carrier concentration. At
  `300`
  `K` it is equal to
  `1.45*1010`
  `1/cm3`.
- QB=qWNB\*AREA is the background mobile carrier base charge, where:

  - *NB* is the
    base doping.
  - *AREA* is the area of the
    device.

**Bipolar Emitter-Base Voltage**

This table shows the equations that define the relationship between the emitter-base
voltage, *Veb*, and the emitter-base
capacitance, *Qeb*.

| Applicable Range of *Qeb* Values | Corresponding *Veb* Equation |
| --- | --- |
| Qeb<0 | Veb=Vebj |
| Qbi>Qeb≥0 | Vebmin=min(Vebj,Vebd) |
| Qeb>Qbi | Veb=Vebd |

In these equations:

- Vebj=Vbi−(Qeb−Qbi)22qNBεsiA2is the emitter-base depletion voltage.
- *Vbi* is the built-in
  voltage.
- Qbi=AREA\*2εsiqNB\*Vbi is the emitter-base junction built-in
  voltage.
- Vebd=kTqln[(P0ni2+1NB)(NB+P0)]−DCμnclnP0+NBNBis the emitter-base diffusion voltage.

**Anode Current**

The anode current is obtained from this equation:

IT=VaeRb\*SCALE,

where:

- *Vae* is the applied
  anode-emitter voltage.
- *Rb* is the
  conductivity-modulated base resistance.

This table shows the equations that define the relationship between the
conductivity-modulated base resistance,
*Rb*, and the emitter-base
capacitance, *Qeb*.

| Applicable Range of *Qeb* Values | Corresponding *Rb* Equation |
| --- | --- |
| Qeb<0 | Rb=Wq\*MUN\*AREA\*NB |
| Qeb≥0 | Rb=Wq\*μeff\*AREA\*neff |

In these equations:

- *μeff* is the effective
  carrier mobility.
- *neff* is the effective
  base doping concentration.
- *MUN* is the electron mobility.

*μeff* and
*neff* are obtained using these equations:

μnc=1(1μn+1μc)μpc=1(1μp+1μc)μeff=μnc+μpcQeb(Qeb+QB)Dc=2kTqμncμpcμnc+μpcL=Dc\*TAUP0=Qq\*AREA\*LtanhW2Lneff=W2LNB2+P02csch(WL)arctanh[NB2+P02csch(WL)tanh(W2L)NB+P0csch(WL)tanh(W2L)]δ¯p=P0sinh(W2L)sinh(WL)

where:

- *μnc* is the electron
  carrier scattering mobility.
- *μpc* is the hole carrier
  scattering mobility.
- *Dc* is the
  carrier-carrier scattering diffusivity.
- *L* is the ambipolar diffusion length.
- *P0* is the carrier
  concentration at emitter's end of the base.
- δp¯ is the average carrier concentration in
  base.

**Avalanche Multiplication Current**

The avalanche multiplication current is obtained from this equation:

Imult=(M−1)(Imos+Icss+Iccer)+M\*Igen,

where:

- Igen=SCALETAUqniAREA2εsiVbcqNBis the collector-base thermally generated
  current.
- *Icss* is the steady-state
  collector current.
- *Imos* is the MOSFET
  channel current.
- *Iccer* is the
  collector-emitter redistribution current.

This equation defines the relationship between the base-collector voltage,
*Vbc*, and the avalanche
multiplication factor, *M*:

M=11−(VbcBVcbo)BVN,

where:

- BVcbo=BVF\*5.34e13\*NB−0.75is the open-base collector-emitter breakdown
  voltage.
- *BVF* is the avalanche uniformity factor.
- *BVN* is the avalanche multiplication
  exponent.

**Capacitance Model**

The gate source capacitance is obtained from this equation:

Qgs=CGS\*Vgs\*SCALE.

The drain source capacitance is obtained from this equation:

Qds=q(AREA−AGD)\*NB\*Wdsj\*SCALE,

where *Wdsj =
Wbcj* is the drain-source depletion
width.

This table shows the equations that define the relationship between the gate-drain
capacitance, *Qdg*, and the drain-gate
voltage, *Vdg*

| Applicable Range of *Vdg* Values | Corresponding *Qdg* Equation |
| --- | --- |
| Vdg+VTD≤0 | Qdg=Cgdo\*Vdg\*SCALE |
| Vdg+VTD>0 | Qdg=[qNBεsiAGDCOXD(COXD\*Wdgjεsilog(1+COXD\*Wdgjεsi))−Cgdo\*VTD]\*SCALE |

In these equations:

- Cgdo=COXD\*AGD is the gate-drain overlap oxide
  capacitance.
- *Vdg* is the drain-gate
  voltage.
- *εsi* is the permittivity
  of silicon.
- Wdgj=2εsi(Vdg+VTD)qNB is the drain-gate overlap depletion width.
- *VTD* is the **Gate-drain overlap
  depletion threshold, VTD**.
- *COXD* is the **Gate-drain oxide
  capacitance per unit area, COXD**.
- *AGD* is the **Gate-drain overlap area,
  AGD**.
- *NB* is the **Base doping,
  NB**.

This equation shows the relationship between the collector-emitter redistribution current,
*Iccer*, and the
collector-emitter redistribution capacitance,
*Ccer*:

Iccer=Ccer\*dVecdt\*SCALE,

where *Vec* is the
emitter-collector voltage.

This table shows the equations that define the relationship between the collector-emitter
redistribution capacitance, *Ccer*, and
the emitter-base capacitance,
*Qeb*.

| Applicable Range of *Qeb* Values | Corresponding *Ccer* Equation |
| --- | --- |
| Qeb>0 | Ccer=QebCbcj3QB+Cmin\*AREA |
| Qeb≤0 | Ccer=CminAREA |

In these equations:

- *Cbcj* is the
  base-collector depletion capacitance.
- QB=qWNB\*AREA is the background mobile carrier base
  charge.

The implicit emitter-base capacitor current is obtained from this equation:

Iqeb=dQebdt\*SCALE.

**Transistor Temperature**

You can use these options to define transistor temperature,
*T*:

- Fixed temperature — The block uses a temperature that is
  independent of the circuit temperature when the **Model
  temperature dependence using** parameter in the
  **Temperature** settings of the
  SPICE NIGBT block is set to
  `Fixed temperature`. For this model,
  the block sets *T* equal to
  *TFIXED*.
- Device temperature — The block uses a temperature that depends on circuit
  temperature when the **Model temperature dependence
  using** parameter in the
  **Temperature** settings of the
  SPICE NIGBT block is set to
  `Device temperature`. For this model,
  the block defines temperature as

  T=TC+TOFFSET

  where:

  - *TC* is the
    circuit temperature.

    If there is not an Environment
    Parameters block in the circuit,
    *TC* is
    equal to 300.15 K.

    If there is an Environment
    Parameters block in the circuit,
    *TC* is
    equal to the value that you specify for the
    **Temperature** parameter in the
    **SPICE** settings of the
    Environment
    Parameters block. The default value
    for the **Temperature** parameter is
    `300.15`
    `K`.
  - *TOFFSET* is the offset local circuit
    temperature.
