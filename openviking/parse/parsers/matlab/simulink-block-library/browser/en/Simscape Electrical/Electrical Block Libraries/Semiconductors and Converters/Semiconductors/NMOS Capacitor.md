---
type: simulink-block
title: 'NMOS Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'nmoscapacitor'
documentation_source_path: 'ref/nmoscapacitor.html'
language: en
---

# NMOS Capacitor

## Ports

### Conserving

### **G** — Gate terminal electrical

Electrical conserving port associated with the gate terminal of the NMOS
capacitor.

### **B** — Bulk terminal electrical

Electrical conserving port associated with the bulk terminal of the NMOS
capacitor.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Capacitor model** — Parameterization option for capacitor `Fundamental nonlinear equations` (default) | `Lookup table (2-D, temperature dependent)`

Parameterization option for the capacitor. To specify the equation parameters
directly, set this parameter to `Fundamental nonlinear
equations`. To manually tabulate the C-V characteristics, set this
parameter to `Lookup table (2-D, temperature
dependent)`.

### **Gate-bulk capacitance lookup table, Cgb(T,Vgb)** — Lookup table for gate-bulk capacitance `[3.4574, 3.4541, 3.4407, 3.4274, 3.404, 3.374, 3.3339, 3.2938, 3.227, 3.1402, 3.0467, 2.9332, 2.8063, 2.6828, 2.5426, 2.3255, 2.0985, 1.7679, 1.5576, 1.2671, .9466, .6895, .4691, .2688, .182, .1386, .1152, .1085, .0952, .0851, .0851, .0785, .0751, .0751, .0751]` `nF` (default) | vector or matrix of positive entries

Lookup table for the gate-bulk capacitance, specified as a function of the
temperature and the gate-bulk voltage. The number of rows must be equal to the number
of elements of the **Temperature, T** parameter. The number of
columns must be equal to the number of elements of the **Gate-bulk voltage,
Vgb** parameter.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Lookup table (2-D, temperature dependent)`.

### **Temperature, T** — Temperature for gate-bulk capacitance lookup table `25` `degC` (default) | scalar | vector

Temperature for the gate-bulk capacitance lookup table.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Lookup table (2-D, temperature dependent)`.

### **Gate-bulk voltage, Vgb** — Gate-bulk voltage `[-2.9897, -2.8711, -2.7216, -2.5052, -2.2887, -2.0464, -1.8402, -1.6701, -1.4948, -1.3608, -1.2526, -1.1624, -1.1031, -1.0567, -1.0077, -.9536, -.9149, -.8686, -.8428, -.8093, -.7706, -.7268, -.6804, -.6082, -.5, -.4021, -.3015, -.2216, -.134, -.0309, .0851, .201, .3995, .7165, .9897]` `V` (default) | vector

Gate-bulk voltage. The elements of this vector must be in strictly ascending
order.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Lookup table (2-D, temperature dependent)`.

### Semiconductor Material Parameters

### **Oxide capacitance, Cox** — Total oxide capacitance of capacitor `345.31` `nF` (default) | positive scalar

Total oxide capacitance of the capacitor.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Band-gap energy, EG** — Energy of band gap `1.12` `eV` (default) | scalar

Energy of the band gap. Set this parameter to a value appropriate for the material
of the semiconductor in the capacitor.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Threshold voltage, Vth** — Threshold gate voltage for inversion mode `1.1471` `V` (default) | scalar

Threshold gate voltage. If the gate-to-bulk voltage is greater than or equal to
the value of this parameter, the NMOS capacitor enters inversion mode.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Surface potential, phib** — Surface potential `0.9338` `V` (default) | positive scalar

Semiconductor surface potential at which the surface minority carrier
concentration is equal to the bulk majority carrier concentration. The block
transitions between the depletion and inversion modes at this value.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Body factor, gamma** — Body effect parameter `1.1798` `V^(1/2)` (default) | positive scalar

Body effect parameter, which relates the threshold voltage,
`Vth`, to the flat-band voltage.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Model high-frequency C-V behavior for strong inversion** — Option to model high-frequency C-V behavior for strong inversion mode `off` (default) | `on`

Option to model the high-frequency C-V behavior for strong inversion mode. If you
clear this parameter, the block assumes that the minority carriers can quickly respond
to the change in voltage and an inversion layer charge forms beneath the oxide.
Otherwise, the block assumes that the minority carriers do not have enough time to
quickly respond to the change in the voltage and form the inversion layer charge
beneath the oxide layer of the MOS capacitor.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### **Measurement temperature** — Temperature at which block quotes parameters `25` `degC` (default) | positive scalar

Temperature at which the block quotes the parameters.

#### Dependencies

To enable this parameter, set **Capacitor model** to
`Fundamental nonlinear equations`.

### Temperature Dependence

### **Parameterization** — Option to specify simulation temperature of device `None - Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Option to specify the simulation temperature of the device.

If you set this parameter to `None - Simulate at parameter measurement
temperature` and **Capacitor model** to
`Lookup table (2-D, temperature dependent)`, the block uses
a simulation temperature of 25 `degC`.

### **Device simulation temperature** — Temperature at which to simulate device `25` `degC` (default) | positive scalar

Temperature at which to simulate the device.

#### Dependencies

To enable this parameter, set one of these options:

- **Capacitor model** to `Fundamental nonlinear
  equations` and **Parameterization** to
  `Model temperature dependence`.
- **Capacitor model** to `Lookup table (2-D,
  temperature dependent)`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

N-type metal-oxide-semiconductor capacitor

The NMOS Capacitor block represents an N-type
metal-oxide-semiconductor (NMOS) capacitor. You can parameterize this block by using MOS
equation parameters or parameterize the values as a function of temperature and voltage by
using a tabulated capacitance lookup table.

This figure shows the elements that comprise a MOS capacitor:

Schematic of a MOS capacitor. The top element is the gate, the middle element is the oxide component, the bottom element is the semiconductor.

The NMOS Capacitor block uses a P-type bulk
semiconductor.

### Equation-Based Model

When you set the **Capacitor model** parameter to
`Fundamental nonlinear equations`, the NMOS
Capacitor block operates in three operating modes depending on the
gate-bulk voltage, `Vgb`, the flat-band voltage,
`Vfb`, and the threshold voltage,
`Vth`:

- Vgb<Vfb — Accumulation mode. The voltage on the metal plate accumulates the
  majority charge carriers, or the holes, of the bulk material on the surface of the
  semiconductor.
- Vfb≤Vgb<Vth — Depletion mode. The applied voltage induces the minority charge
  carriers, or the electrons, and creates a depletion region at the surface.
- Vgb≥Vth — Inversion mode. The majority carrier type at the surface of the
  semiconductor is inverted.

To calculate the flat-band voltage, the block uses this equation:

Vfb=Vth−φ−γφ,

where *γ* is the body factor and *φ* is
the surface potential.

The block adjusts the value of the surface potential *φ* by using the equation

φ(Tsim)=kTsimqlog(TmeasTsim)3+TsimTmeasφ(Tmeas)+EG(1−TsimTmeas),

where:

- *Tsim* is the value of the
  **Device simulation temperature** parameter, in Kelvin.
- *Tmeas* is the value of the
  **Measurement temperature** parameter, in Kelvin.
- *EG* is the value of the **Band-gap energy**
  parameter, in electron-volts. The block assumes this parameter is temperature
  independent.
- *q* is the electron charge, in Coulomb, and is equal to
  `1.60217663e-19`
  `C`.
- *k* is equal to `1.380649e-23`
  `J/K`.

This equation defines the total gate charge of the capacitor,
`QG`,

QG=−(Qacc+Qdep+Qinv),

where:

- *Qacc* is the accumulation charge that the
  majority charge carriers form.
- *Qdep* is the depletion region charge
  within the semiconductor layer.
- *Qinv* is the inversion charge that the
  minority charge carriers form.

**Accumulation Mode**

When the gate-bulk voltage is less than the flat-band voltage, the block enters the
accumulation operating mode. In accumulation mode, the majority carriers accumulate on the
surface of the semiconductor. The block calculates the accumulation, depletion, and
inversion charges by using these equations:

Qacc=−Cox⋅(Vgb−Vfb)Qdep=0Qinv=0

where *Cox* is the total oxide
capacitance.

**Depletion Mode**

When the gate-bulk voltage is less than the threshold gate voltage and greater than or
equal to the flat-band voltage, the block enters the depletion operating mode. In
depletion mode, the minority carriers stack on the surface of the semiconductor. The block
calculates the accumulation, depletion, and inversion charges by using these equations:

Qacc=0Qdep=Coxγ22(1−1+4(Vgb−Vfb)γ2)Qinv=0

where *Cox* is the total oxide
capacitance and *γ* is the body factor.

**Inversion Mode**

When the gate-bulk voltage is greater than or equal to the threshold gate voltage, the
block enters the inversion operating mode. In inversion mode, the majority carrier type at
the surface of the semiconductor is inverted. The block calculates the accumulation,
depletion, and inversion charges by using these equations:

Qacc=0Qdep={Coxγ22(1−1+4(Vth−Vfb)γ2)if you clear Model high-frequency C-V behavior at strong inversionCoxγ22(1−1+4(Vth−Vfb)γ2)−CGB,th⋅(Vgb−Vth)if you select Model high-frequency C-V behavior at strong inversion}Qinv={−Cox⋅(Vgb−Vth)if you clear Model high-frequency C-V behavior at strong inversion0if you select Model high-frequency C-V behavior at strong inversion}

where *Cox* is the total oxide
capacitance, *γ* is the body factor, and CGB,th=Cox1+CoxCdep=CoxCdepCox+Cdep is the gate-bulk capacitance at the inversion threshold, which is
equivalent to *Cox* and
*Cdep* in series.
*Cdep* is the depletion layer
capacitance.

If you select the **Model high-frequency C-V behavior at strong
inversion** parameter, the block assumes that the minority carriers do not have
enough time to react to the change in the applied voltage. Consequently, the inversion
charge, *Qinv* is zero and the applied voltage
drops across the oxide capacitance and the depletion region capacitance.

If you clear the **Model high-frequency C-V behavior at strong
inversion** parameter, the block assumes that the minority carriers have enough
time to quickly respond to the change in the voltage and form the inversion layer charge
beneath the oxide layer of the MOS capacitor.

### Tabulated Model

When you set the **Capacitor model** parameter to `Lookup
table (2-D, temperature dependent)`, the NMOS Capacitor block tabulates the
total gate charge of the capacitor, `QG`, in terms
of voltage and temperature. To parameterize the block parameters as a function of
temperature and voltage by using a tabulated capacitance lookup table, specify the
**Gate-bulk capacitance lookup table, Cgb(T,Vgb)**, **Gate-bulk
voltage, Vgb**, and **Temperature, T** parameters.

If you specify only one value in the **Temperature, T** parameter, the
C-V characteristics of the capacitor become temperature independent.

To ensure the gate charge conservation over one full AC cycle, the block converts the
**Gate-bulk capacitance lookup table, Cgb(T,Vgb)** parameter to an
equivalent charge lookup table. The block uses this equivalent charge table to calculate the
variations in the gate charge, *Qg*, with respect to
the voltage by using linear interpolation and extrapolation methods.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
