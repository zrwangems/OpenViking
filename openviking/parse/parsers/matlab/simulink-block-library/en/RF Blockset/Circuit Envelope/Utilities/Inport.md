---
type: simulink-block
title: 'Inport'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'inport'
documentation_source_path: 'ref/inport.html'
language: en
---

# Inport

## Ports

Not documented in R2025b.

## Parameters

### **Source type** — Inport block interpretation of Simulink signal `Ideal voltage` (default) | `Ideal current` | `Power`

Inport block interpretation of a Simulink signal, specified as:

- `Ideal voltage` — The block
  outputs Simulink signals as voltage signals
  *v*(*t*) in the
  RF Blockset environment. When you choose an ideal voltage
  input port you need to manually add a series of source impedance
  to match the blocks connected to the input port. The following
  figure illustrates the internal configuration of the
  block.

  Internal configuration of the Inport block with voltage source, v(t).
- `Ideal current` — The block
  outputs Simulink signals as current signals
  *i*(*t*) in the
  RF Blockset environment. When you use an ideal current input
  port, you manually add a parallel source impedance to match the
  blocks connected to the input port. The following figure
  illustrates the internal configuration of the block.

  Internal configuration of the Inport block with current source, i(t).
- `Power` — The block interprets
  the Simulink signals,
  *Pv*(*t*),
  as available power and internally uses a voltage source, and
  series impedance. You use this option to import a 50 ohm
  environment or different reference impedance signals created
  using Communications Toolbox™. When you select this option, the input port
  automatically inserts a source impedance in your circuit as
  shown in the following figure.

  Source impedance, Zs with voltage source, v(t).

  The voltage *v*(*t*) is a
  scaling of the Simulink signal
  *vSL*(*t*):

  v(t)=2Re(Zs)vSL(t)

  In the preceding equation,
  *Zs* is the
  value of the **Source
  impedance (Ohm)** parameter.

  The generator delivers real power to the load
  *Zl*:

  Pload=|v(t)|2Re(Zs)|Zs+Zl|​2

  When *Zl* = *Zs\**, this generator delivers the available power
  |*vSL*(*t*)|2.

### **Source impedance (Ohm)** — Source impedance for available power match `50` (default) | vector of positive integers

Source impedance for available power match, specified as a vector of
positive integers in ohms

#### Dependencies

To enable this parameter, select `Power` in **Source
type**.

### **Carrier frequencies** — Carrier frequencies `0 Hz` (default) | vector | scalar

Carrier frequencies, specified as a vector or scalar in Hz, kHz, MHz, or GHz. Specify
**Carrier frequencies** as a positive scalar greater
than `0` when you select the **Use
Square Wave** parameter. In carrier frequencies, the
elements are a combination of fundamental tones and corresponding harmonics
in the Configuration block.

### **Use Square Wave** — Use square carrier wave `off` (default) | `on`

Select this parameter to modulate your input signal onto a square carrier
wave.

### **View** — Plot square wave button

Plot the simulation frequencies of the square carrier wave and the
approximate square wave with RSM error.

#### Dependencies

To enable this parameter, select **Use
Square Wave**.

### **Number of Fourier Coefficients** — Number of Fourier coefficients `10` (default) | integer greater than or equal to `1`

Number of Fourier coefficients required to modulate an input signal onto a
square carrier wave, specified as an integer greater than or equal to
`1`.

#### Dependencies

To enable this parameter, select **Use
Square Wave**.

### **DC Bias** — DC bias `0` (default) | real number

DC bias, specified as a real number.

#### Dependencies

To enable this parameter, select **Use
Square Wave**.

### **Duty Cycle (%)** — Duty cycle of square carrier wave `50` (default) | positive integer between `0` and `100`

Duty cycle of a square carrier wave, specified as a positive integer
between `0` and `100` in %.

#### Dependencies

To enable this parameter, select **Use
Square Wave**.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to ground and hide the negative terminals. Clear the parameter to expose
the negative terminals. By exposing these terminals, you can connect them to
other parts of your model.

## Libraries

RF Blockset / Circuit Envelope / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2022b: Modulate input signal onto square carrier wave in circuit envelope simulation environment

Select the new **Use Square
Wave** parameter to modulate an input signal onto a square carrier
wave in the circuit envelope simulation environment.

### R2021b: Inport block icon updated

Starting in R2021b, the Inport block icon is now updated. When you
open a model created before R2021b containing a Inport block, the
software replaces the block icon with the R2021b version.

## Description

Convert Simulink input signal to RF Blockset signal

The Inport block imports Simulink® signals into the RF Blockset™ circuit envelope simulation environment. For an introduction to RF
simulation, see the example, Simulate High Frequency Components. You can also
modulate an input signal onto a square carrier wave in the RF Blockset circuit envelope
simulation environment.

Complex-valued input signals
*Ik*(*t*) + *j* · *Qk*(*t*)
are the modulations at the frequencies {*fk*}
specified in the **Carrier
frequencies** parameter of the block. The input port converts the
complex-valued input signals into an RF signal suitable for multicarrier
simulation:

out=Real(∑k=1N(Ik(t)+j·Qk(t))·ej2πfkt)

The **Source type** parameter
specifies the Simulink signal as either current, or voltage, or power source. For more
information, see How to Use Inport Block.
Inport block mask icons are dynamic and show the current type of
source. This table shows you how the icons on this block vary based on the type of
source you set on the **Source type** parameter on the
block.

| Source type: `Ideal voltage` | Source type: `Ideal current` | Source type:  `Power` |
| --- | --- | --- |
| Inport block icon with Source type is set to Ideal voltage. | Inport block icon with Source type is set to Ideal current. | Inport block icon with Source type is set to Ideal current. |
