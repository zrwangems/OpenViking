---
type: simulink-block
title: 'Frequency-Dependent Overhead Line (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Lines'
documentation_page: 'frequencydependentoverheadlinethreephase'
documentation_source_path: 'ref/frequencydependentoverheadlinethreephase.html'
language: en
---

# Frequency-Dependent Overhead Line (Three-Phase)

## Ports

### Conserving

### **~1** — Three-phase AC voltage 1 electrical

Expandable electrical conserving three-phase port associated with AC voltage
1.

### **~2** — Three-phase AC voltage 2 electrical

Expandable electrical conserving three-phase port associated with AC voltage
2.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **X position of the line** — Horizontal line position `[-6, 0, 6]` `m` (default) | vector of three elements

Position of the line in terms of the *x*-axis of the reference
frame.

### **Y position of the line** — Vertical line position `[16, 26, 16]` `m` (default) | vector of three positive elements

Position of the line in terms of the *y*-axis of the reference
frame. The elements of the vector must be greater than `0`.

### **Resistivity of the conductor** — Conductor resistivity `2.7e-8` `m*Ohm` (default) | positive scalar

Conductor resistivity. The value must be greater than `0`.

### **Resistivity of the earth** — Earth return resistivity `100` `m*Ohm` (default) | positive scalar

Earth return resistivity. The value must be greater than
`0`.

### **Radius of the conductor** — Conductor radius `0.017` `m` (default) | positive scalar

Conductor radius. The value must be greater than `0`.

### **Length of the line** — Line length `150e3` `m` (default) | scalar in the range [1, 300000]

Length of the frequency-dependent overhead line.

### **Ground configuration** — Ground node accessibility `Internally grounded` (default) | `Accessible ground nodes`

Configuration of the ground nodes.

## Libraries

Simscape / Electrical / Passive / Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Three-phase overhead line which includes effects that vary as a function of frequency

The Frequency-Dependent Overhead Line (Three-Phase) block
represents a high-fidelity frequency-dependent overhead line that offers accurate transient
response simulation from 0.01 Hz to 100 kHz.

The block computes frequency-dependent impedance and admittance matrices. The calculations
also depend on the loss, inductance, and capacitance of the return path.

For more information on using a frequency-dependent overhead line (three-phase), see
Engineering Applications.

### Equations

**Line Model**

The electromagnetic behavior of a multiconductor transmission line is described by the
telegrapher's equation.

−dVdx=ZI

−dIdx=YV

Where:

- *V* is the vector of line phase voltages.
- *I* is the vector of phase currents.
- *Z* is the series impedance matrix in per unit length.
- *Y* is the shunt admittance matrix in per unit length.

These are general solutions for the vector of currents and voltages.

|  |  |
| --- | --- |
| I(x)=e−ΨxC1+eΨxC2 | **(1)** |

|  |  |
| --- | --- |
| YcV(x)= e−ΨxC1−eΨxC2 | **(2)** |

Where Ψ=YZ is the propagation matrix and Yc=(YZ)−1Y is the characteristic admittance.

Consider now a transmission line segment of length *x* =
*l*. At the beginning of one of its ends, when *x* =
*0*, the equations 1 and 2 are evaluated as follows.

|  |  |
| --- | --- |
| I1=C1+C2 | **(3)** |

|  |  |
| --- | --- |
| YcV1= C1−C2 | **(4)** |

The integration constant vectors *C1* and
*C2* can be expressed in terms of
*I0* and
*V0*.

|  |  |
| --- | --- |
| C1=(I1+YcV1)2 | **(5)** |

|  |  |
| --- | --- |
| C2=(I1−YcV1)2 | **(6)** |

Similarly, at *x* = *l*, equations 1 and 2 are
evaluated as follows.

|  |  |
| --- | --- |
| I2=e−ΨlC1+eΨlC2 | **(7)** |

|  |  |
| --- | --- |
| YcV2=e−ΨlC1−eΨlC2 | **(8)** |

To obtain the two fundamental equations for the transmission line model, first you use
equations 7 and 8 to perform this calculation.

|  |  |
| --- | --- |
| I2−YcV2=−2e−ΨlC1 | **(9)** |

Then you substitute equation 5 into equation 9.

|  |  |
| --- | --- |
| I2−YcV2=−H(I1+YcV1) | **(10)** |

Where H=e−Ψl is the propagation factor matrix. Equation 10 establishes the relation
between voltages and currents at the terminals of a multi-conductor line section.

You can obtain a companion expression providing the model for the terminal 1 at
*x* = *0*.

|  |  |
| --- | --- |
| I1−YcV1=−H(I2+YcV2) | **(11)** |

Define:

- Ish,1=YcV1 — Shunt current vector produced at terminal 1 by injected voltages
  *V1*
- Ish,2=YcV2 — Shunt current vector produced at terminal 2 by injected voltages
  *V2*
- Irfl,1=12(I1+YcV1) — Reflected currents of terminal 1
- Irfl,2=12(I2+YcV2) — Reflected currents of terminal 2

And finally rewrite equations 10 and 11 as follows:

I1=Ish,1−2HIrfl,2

I2=Ish,2−2HIrfl,1

These equations constitute a traveling wave line model for the segment of length
L.

Particularly for transmission lines with ground return, the parameters are highly
dependent on frequency. Model solutions are then carried out directly in the phase domain.
The block computes automatically the impedance and the characteristic admittance matrices
on the full frequency range, performing an approximation through rational fitting.

Rational fitting for this model is performed by using the vector fitting (VF)
procedure. For more information on the phase domain line model and the state-space
analysis, see *Wide-Band Line Model Implementation in Matlab for EMT
Analysis* [1].

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
