---
type: simulink-block
title: 'Optocoupler'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'optocoupler'
documentation_source_path: 'ref/optocoupler.html'
language: en
---

# Optocoupler

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the diode positive terminal

### **-** — Negative terminal electrical

Electrical conserving port associated with the diode negative terminal

### **C** — Transistor collector terminal electrical

Electrical conserving port associated with the transistor collector terminal

### **E** — Transistor emitter terminal electrical

Electrical conserving port associated with the transistor emitter terminal

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Current transfer ratio** — Current transfer ratio `0.2` (default)

The output current flowing from the transistor collector to emitter junctions is equal
to the product of the current transfer ratio and the current flowing in the light-emitting
diode.

### **Diode parameterization** — Model parameterization `Use I-V curve data points` (default) | `Use parameters IS and N`

Select one of the following methods for model parameterization:

- `Use I-V curve data points` — Specify measured data
  at two points on the diode I-V curve.
- `Use parameters IS and N` — Specify saturation
  current and emission coefficient.

### **Currents [I1 I2]** — Vector of current values at two points `[.001, .015]` `A` (default)

A vector of the current values at the two points on the diode I-V curve that the block
uses to calculate *IS* and *N*.

#### Dependencies

This parameter is visible only when you select `Use I-V curve data
points` for the **Diode parameterization** parameter.

### **Voltages [V1 V2]** — Vector of voltage values at two points `[.9, 1.05]` `V` (default)

A vector of the voltage values at the two points on the diode I-V curve that the block
uses to calculate *IS* and *N*.

#### Dependencies

This parameter is visible only when you select `Use I-V curve data
points` for the **Diode parameterization** parameter.

### **Ohmic resistance, RS** — Ohmic resistance `0.1` `Ohm` (default)

The series diode connection resistance.

### **Saturation current, IS** — Saturation current `1e-10` `A` (default)

The magnitude of the current that the ideal diode equation approaches asymptotically for
very large reverse bias levels.

#### Dependencies

This parameter is visible only when you select `Use parameters IS and
N` for the **Diode parameterization** parameter.

### **Measurement temperature** — Measurement temperature `25` `°C` (default)

The temperature at which IS or the I-V curve was measured. The default value is
`25` °C.

### **Emission coefficient, N** — Diode emission coefficient `2` (default)

The diode emission coefficient or ideality factor.

#### Dependencies

This parameter is visible only when you select `Use parameters IS and
N` for the **Diode parameterization** parameter.

### Junction Capacitance

### **Capacitance** — Modeling diode junction capacitance `Fixed or zero junction capacitance` (default) | `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

Select one of the following options for modeling the diode junction capacitance:

- `Fixed or zero junction capacitance` — Model the
  junction capacitance as a fixed value.
- `Use C-V curve data points` — Specify measured data
  at three points on the diode C-V curve.
- `Use parameters CJ0, VJ, M & FC` — Specify
  zero-bias junction capacitance, junction potential, grading coefficient, and forward-bias
  depletion capacitance coefficient.

### **Junction capacitance** — Diode junction capacitance `5` `pF` (default)

Fixed junction capacitance value.

#### Dependencies

This parameter is visible only when you select `Fixed or zero junction
capacitance` for the **Capacitance** parameter.

### **Zero-bias junction capacitance, CJ0** — Zero-bias junction capacitance `5` `pF` (default)

The value of the capacitance placed in parallel with the exponential diode term.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Capacitance** parameter.

### **Junction potential, VJ** — Junction potential `1` `V` (default)

The junction potential.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Capacitance** parameter.

### **Grading coefficient, M** — Grading coefficient `0.5` (default)

The coefficient that quantifies the grading of the junction.

#### Dependencies

This parameter is visible only when you select `Use parameters CJ0, VJ, M
& FC` for the **Capacitance** parameter.

### **Reverse bias voltages [VR1 VR2 VR3]** — Vector of reverse bias voltages `[.1, 10, 100]` `V` (default)

A vector of the reverse bias voltage values at the three points on the diode C-V curve
that the block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` for the **Capacitance** parameter.

### **Corresponding capacitances [C1 C2 C3]** — Vector of corresponding capacitances `[3.5, 1, .4]` `pF` (default)

A vector of the capacitance values at the three points on the diode C-V curve that the
block uses to calculate *CJ0*, *VJ*, and
*M*.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` for the **Capacitance** parameter.

### **Capacitance coefficient, FC** — Fitting capacitance coefficient `0.5` (default)

Fitting coefficient that quantifies the decrease of the depletion capacitance with
applied voltage.

#### Dependencies

This parameter is visible only when you select `Use C-V curve data
points` or `Use parameters CJ0, VJ, M & FC` for
the **Capacitance** parameter.

### Temperature Dependence

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Use an I-V data point at second measurement temperature T2` | `Specify saturation current at second measurement temperature T2` | `Specify the energy gap EG`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter measurement temperature`
  — Temperature dependence is not modeled, or the model is simulated at the
  measurement temperature *T*m1 (as specified by the
  **Measurement temperature** parameter on the **Main**
  tab). This is the default method.
- `Use an I-V data point at second measurement temperature T2`
  — If you select this option, you specify a second measurement temperature
  *T*m2, and the current and voltage values at this
  temperature. The model uses these values, along with the parameter values at the first
  measurement temperature *T*m1, to calculate the
  energy gap value.
- `Specify saturation current at second measurement temperature
  T2` — If you select this option, you specify a second measurement
  temperature *T*m2, and saturation current value at
  this temperature. The model uses these values, along with the parameter values at the first
  measurement temperature *T*m1, to calculate the
  energy gap value.
- `Specify the energy gap EG` — Specify the energy gap
  value directly.

### **Current I1 at second measurement temperature** — Current I1 at second measurement temperature `0.029` `A` (default)

Specify the diode current *I1* value when the voltage is
*V1* at the second measurement temperature.

#### Dependencies

This parameter is visible only when you select `Use an I-V data point at
second measurement temperature T2` for the
**Parameterization** parameter.

### **Voltage V1 at second measurement temperature** — Voltage V1 at second measurement temperature `1.05` `V` (default)

Specify the diode voltage *V1* value when the current is
*I1* at the second measurement temperature.

#### Dependencies

This parameter is visible only when you select `Use an I-V data point at
second measurement temperature T2` for the
**Parameterization** parameter.

### **Saturation current, IS, at second measurement temperature** — Saturation current, IS, at second measurement temperature `1.8e-8` `A` (default)

Specify the saturation current *IS* value at the second measurement
temperature.

#### Dependencies

This parameter is visible only when you select `Specify saturation current
at second measurement temperature T2` for the
**Parameterization** parameter.

### **Second measurement temperature** — Second measurement temperature `125` `°C` (default)

Specify the value for the second measurement temperature.

#### Dependencies

This parameter is visible only when you select  `Use an I-V data point at
second measurement temperature T2` or `Specify saturation current
at second measurement temperature T2` for the
**Parameterization** parameter.

### **Energy gap parameterization** — Energy gap parameterization `Use nominal value for silicon (EG=1.11eV)` (default) | `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

Select a value for the energy gap from a list of predetermined options, or specify a
custom value:

- `Use nominal value for silicon (EG=1.11eV)` — This is
  the default.
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — If you select this option,
  the **Energy gap, EG** parameter appears in the dialog box, to let you
  specify a custom value for *EG*.

#### Dependencies

This parameter is visible only when you select `Specify the energy gap
EG` for the **Parameterization** parameter.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Specify a custom value for the energy gap, *EG*.

#### Dependencies

This parameter is visible only when you select `Specify a custom
value` for the **Energy gap parameterization**
parameter.

### **Saturation current temperature exponent parameterization** — Saturation current temperature exponent parameterization `Use nominal value for pn-junction diode (XTI=3)` (default) | `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

Select one of the following options to specify the saturation current temperature
exponent value:

- `Use nominal value for pn-junction diode (XTI=3)` —
  This is the default.
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — If you select this option,
  the **Saturation current temperature exponent, XTI** parameter appears in
  the dialog box, to let you specify a custom value for *XTI*.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Specify a custom value for the saturation current temperature exponent,
*XTI*.

#### Dependencies

This parameter is visible only when you select `Specify a custom
value` for the **Saturation current temperature exponent
parameterization** parameter.

### **Device simulation temperature** — Device simulation temperature `25` `°C` (default)

Specify the value for the temperature *T*s, at
which the device is to be simulated.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Behavioral model of optocoupler as LED, current sensor, and controlled current source

This block represents an optocoupler using a model that consists of the following components:

- An exponential light-emitting diode in series with a current sensor on the input
  side
- A controlled current source on the output side

The output-side current flows from the collector junction to the emitter
junction. It has a value of
*CTR*·*Id*, where
*CTR* is the **Current transfer ratio** parameter value and
*Id* is the diode current.

Use the Optocoupler block to interface two electrical
circuits without making a direct electrical connection. A common reason for doing this is that
the two circuits work at very different voltage levels.

**Note**

Each electrical circuit must have its own Electrical
Reference block.

If the output circuit is a phototransistor, typical values for the **Current
transfer ratio** parameter are 0.1 to 0.5. If the output stage consists of a Darlington
pair, the parameter value can be much higher than this. The **Current transfer
ratio** value also varies with the light-emitting diode current, but this effect is not
modeled by the Photodiode block.

Some manufacturers provide a maximum data rate for optocouplers. In practice, the maximum
data rate depends on the following factors:

- The capacitance of the photodiode and the type of the driving circuit
- The construction of the phototransistor and its associated capacitance

The Optocoupler block only lets you define the
capacitance on the light-emitting diode. You can use the **Junction
capacitance** parameter to add your own capacitance across the collector and emitter
connections.

The Optocoupler block lets you model temperature dependence
of the underlying diode. For details, see the Diode reference page.

### Thermal Port

You can expose the thermal port to model the effects of generated heat and device
temperature. To expose the thermal port, set the **Modeling option**
parameter to either:

- `No thermal port` — The block does not contain a
  thermal port and does not simulate heat generation in the device.
- `Show thermal port` — The block contains a thermal
  port that allows you to model the heat that conduction losses generate. For
  numerical efficiency, the thermal state does not affect the electrical behavior
  of the block.

For more information on using thermal ports and on the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
