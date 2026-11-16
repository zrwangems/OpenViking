---
type: simulink-block
title: 'S-Parameter Rational Fit'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'sparameterrationalfit'
documentation_source_path: 'ref/sparameterrationalfit.html'
language: en
---

# S-Parameter Rational Fit

## Ports

### Conserving

### **pk** — *k*th positive terminal electrical

Electrical conserving port associated with the positive terminal of the
*kth* port.

The number of ports of this type is equal to the value of the **Number of
ports** parameter.

### **nk** — *k*th negative terminal electrical

Electrical conserving port associated with the negative terminal of the
*kth* port.

The number of ports of this type is equal to the value of the **Number of
ports** parameter.

#### Dependencies

To enable this port, clear the **Ground and hide negative
terminals** parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of ports** — Number of electrical connection pairs `2` (default) | positive integer

Number of electrical connection pairs. The term "port" in the name of this parameter
refers to a pair of terminals connecting two electrical networks. This definition is
common in the telecommunications industry.

If you clear the **Ground and hide negative terminals** parameter,
the number of Simscape "conserving ports" that the block exposes is twice the value of the
**Number of ports** parameter.

If you select the **Ground and hide negative terminals** parameter,
the number of Simscape "conserving ports" that the block exposes is equal to the value of the
**Number of ports** parameter.

### **Reference impedance (Ohm)** — Reference line impedance `50` (default) | real scalar

Reference line impedance *Z*0, in
ohms.

### **Rational fit object** — Rational fit object `[]` (default) | square matrix | `rational` object | `rfmodel.rational` object

Rational fit object. Use the `rational` (RF Toolbox) function
to fit a rational function object to the component data.

The default value of `[]` indicates that there is no cross-coupling
and all ports have an impedance equal to the value of the **Reference
impedance** parameter. Use the default value of `[]` for
early testing and building models when you do not have the `rational`
object.

### **Ground and hide negative terminals** — Option to ground and hide negative terminals `Off` (default) | `On`

Option to ground and hide the negative terminals.

Clear this parameter to enable the **nk** ports associated with the
negative terminals of the block.

Select this parameter to ground all the electrical connection pair negative
terminals. The block models the connections to the ground inside the
S-Parameter Rational Fit block using Electrical Reference blocks.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Implement rational fit approximation to S-parameter description of linear system

The S-Parameter Rational Fit block implements a rational
approximation of a linear system characterized with scattering parameters (S-parameters).
S-parameters describe the frequency behavior of a system. For more information about the
S-parameters format, see Data Import and Network Parameters (RF Toolbox). For more information about how to calculate
S-parameters, see `sparameters` (RF Toolbox).

The S-Parameter Rational Fit block operates with passband
signals. If you need to simulate a *baseband signal*, a frequency band
limited signal superimposed on a carrier frequency, use the S-Parameters (RF Blockset) block with other blocks in the RF Blockset™ Circuit Envelope library instead. For more information about the relationship
between baseband and passband signals, see the Passband Signal Representation in Circuit Envelope (RF Blockset) example. For more information about
using blocks in the Circuit Envelope library, see Circuit Envelope Simulation (RF Blockset).

You define the rational fit by specifying a value for the **Rational fit
object** parameter. There are two ways to construct a rational fit object:

- You can fit a `rational` function object to the component data using
  the `rational` (RF Toolbox)
  function.
- You can use the `rfmodel.rational` (RF Toolbox)
  constructor to specify the pole-residue representation of the component directly. Use
  the `rationalfit` (RF Toolbox) function to return an
  `rfmodel.rational` object.

**Note**

To run a simulation that uses a `rational` or `rfmodel.rational` object as a parameter value in the S-Parameter
Rational Fit block you must have RF Toolbox™ installed.

`rational` (RF Toolbox) is
recommended over `rationalfit` because it enables faster simulation and
has improved fitting controls.

For testing purposes, you can also specify the rational fit object as:

- The empty set `[]` — This option creates a nonreflective rational
  system with no cross-coupling between ports. All ports present an impedance to the
  external circuit equal to the value of the **Reference impedance
  (Ohm)** parameter.
- A square constant matrix with dimensions equal to the number of ports — This matrix
  defines the constant term connecting the ports. A matrix of zeros is equivalent to the
  empty set option and an entry of `1` in the *(i,j)*
  element implies a direct feedthrough from port *j* to port
  *i*.

**Note**

In this context, a "port" refers to a pair of terminals connecting two electrical
networks. This definition is common in the telecommunications industry. By this
definition, a single "port" represents two "conserving ports" in the Simscape™ family of products.

You can specify the number of ports by setting the value of the **Number of
ports** parameter. Limit this value to `33`. Higher values
significantly increase compilation and simulation time. Higher order rational fits also
increase the compilation and simulation time. If the rest of your model is linear or switched
linear, avoid including delay terms in the rational fit object so that the
S-Parameter Rational Fit block also uses linear equations.
For more information about checking your model for blocks with nonlinear equations, see
`simscape.findNonlinearBlocks`.

### Equations

This figure shows the four-element S-parameter matrix for a two-port device.

In this figure:

- *a*i is the incident power wave from port
  *i*.
- *b*i is the reflected power wave from port
  *i*.
- *S*ij is the transmission coefficient that
  indicates how much of the signal that enters the network at port *j*
  transmits to port *i*.

The block assumes that all the reference impedances are equal and have a real scalar
value. These equations describe the relationship between the incident power wave and the
reflected power waves at each port over a range of frequencies,

b1=S11a1+S12a2b2=S21a1+S22a2

ai=bi=12(Vi+Z0Ii)

where:

- *V*i is the voltage at port
  *i* relative to the ground.
- *Z*0 is the value of the
  **Reference impedance (Ohm)** parameter.
- *I*i is the current through port
  *i*.

The `rational` object approximates the frequency responses
*S*ij by rational transfer functions of the
form,

F(s)=∑k=1nCks−Ak+D,

where:

- *s* is the angular frequency.
- *C*k are the residues.
- *A*k are the poles.
- *D* is the direct term.
