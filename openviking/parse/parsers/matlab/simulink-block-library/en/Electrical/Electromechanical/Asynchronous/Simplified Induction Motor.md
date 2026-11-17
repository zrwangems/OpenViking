---
type: simulink-block
title: 'Simplified Induction Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'simplifiedinductionmotor'
documentation_source_path: 'ref/simplifiedinductionmotor.html'
language: en
---

# Simplified Induction Motor

## Ports
```yaml
ports:
- name: W
  summary: Real power physical
  direction: output
- name: wm
  summary: Mechanical speed physical
  direction: output
- name: VAR
  summary: Imaginary power physical
  direction: output
- name: s
  summary: Motor slip physical
  direction: output
- name: R
  summary: Rotor mechanical
  direction: conserving
- name: C
  summary: Case mechanical
  direction: conserving
- name: H1
  summary: Rotor thermal
  direction: conserving
- name: H2
  summary: Rotor thermal
  direction: conserving
```

### Output

### **W** — Real power physical

Physical signal port associated with the motor real power.

### **wm** — Mechanical speed physical

Physical signal port associated with the motor mechanical
speed.

### **VAR** — Imaginary power physical

Physical signal port associated with the motor imaginary power.

### **s** — Motor slip physical

Physical signal port associated with the motor slip.
### Conserving

### **R** — Rotor mechanical

Mechanical rotational conserving port associated with the
rotor.

### **C** — Case mechanical

Mechanical rotational conserving port associated with the motor
case.

### **H1** — Rotor thermal

Stator thermal port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **H2** — Rotor thermal

Rotor thermal port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal ports No thermal port (default) | Show thermal port
  group: ''
- name: Model parameterization
  summary: Block parameterization By motor ratings (default) | By equivalent circuit parameters
  group: Electrical Torque
- name: Stator resistance R1
  summary: Stator winding resistance 1 Ohm (default)
  group: Electrical Torque
- name: Rotor resistance R2
  summary: Rotor resistance 1 Ohm (default)
  group: Electrical Torque
- name: Stator inductance L1
  summary: Stator winding inductance 0.02 H (default)
  group: Electrical Torque
- name: Rotor inductance L2
  summary: Rotor inductance 0.02 H (default)
  group: Electrical Torque
- name: Magnetizing inductance Lm
  summary: Stator magnetizing inductance 0.5 H (default)
  group: Electrical Torque
- name: Rated mechanical power
  summary: Motor mechanical power 825 W (default)
  group: Electrical Torque
- name: Rated speed
  summary: Rated motor speed 3500 rpm (default)
  group: Electrical Torque
- name: Rated RMS line-to-line voltage
  summary: Rated line-to-line voltage 200 V (default)
  group: Electrical Torque
- name: Rated supply frequency
  summary: Frequency of the AC supply voltage 60 Hz (default)
  group: Electrical Torque
- name: Rated RMS line current
  summary: Rated line current 2.7 A (default)
  group: Electrical Torque
- name: R1 parameterization
  summary: Equivalent circuit resistance parameterization From motor efficiency (default) | From power factor | Use measured
    stator resistance R1
  group: Electrical Torque
- name: Motor efficiency (percent)
  summary: Motor efficiency 95 (default)
  group: Electrical Torque
- name: Motor power factor
  summary: Motor power factor 0.93 (default)
  group: Electrical Torque
- name: Measured stator resistance R1
  summary: Measured stator resistance 1 Ohm (default)
  group: Electrical Torque
- name: Number of pole pairs
  summary: Number of motor pole pairs 1 (default)
  group: Electrical Torque
- name: Number of phases
  summary: Number of supply phases 3 (default)
  group: Electrical Torque
- name: Stator connections
  summary: Motor stator configurations Delta configuration (default) | Star configuration
  group: Electrical Torque
- name: Supply RMS line-to-line voltage
  summary: Supply RMS line-to-line voltage 200 V (default)
  group: Power Supply
- name: Supply frequency
  summary: AC supply frequency 60 Hz (default)
  group: Power Supply
- name: Rotor inertia
  summary: Rotor inertia 1e-3 kg*m^2 (default)
  group: Mechanical
- name: Rotor damping
  summary: Rotor damping 1e-4 N*m/(rad/s) (default)
  group: Mechanical
- name: Initial rotor speed
  summary: Initial rotor speed 0 rpm (default)
  group: Mechanical
- name: Stator and rotor resistance temperature coefficients, [alpha_1 alpha_2]
  summary: Stator and rotor resistance temperature coefficients [.00393, .00393] 1/K (default)
  group: Temperature Dependence
- name: Measurement temperature
  summary: Measurement temperature 25 C (default)
  group: Temperature Dependence
- name: Stator and rotor thermal masses, [M_1 M_2]
  summary: Stator and rotor thermal masses [100, 100] J/K (default)
  group: Thermal Port
- name: Stator and rotor initial temperatures, [T_1 T_2]
  summary: Stator and rotor initial temperatures [25, 25] C (default)
  group: Thermal Port
```

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that
convert power to heat.

### Electrical Torque

### **Model parameterization** — Block parameterization `By motor ratings` (default) | `By equivalent circuit parameters`

Select one of the following methods for block parameterization:

- `By motor ratings` —
  Provide electrical torque parameters that the block converts
  to an equivalent circuit model of the motor assuming that
  the effect of the magnetizing inductance
  Lm is negligible.
- `By equivalent circuit
  parameters` — Provide electrical
  parameters for an equivalent circuit model of the
  motor.

### **Stator resistance R1** — Stator winding resistance `1` `Ohm` (default)

Resistance of the stator winding. The default value is
`1` Ω.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By
equivalent circuit parameters`.

### **Rotor resistance R2** — Rotor resistance `1` `Ohm` (default)

Resistance of the rotor, specified with respect to the stator.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By
equivalent circuit parameters`.

### **Stator inductance L1** — Stator winding inductance `0.02` `H` (default)

Inductance of the stator winding.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By
equivalent circuit parameters`.

### **Rotor inductance L2** — Rotor inductance `0.02` `H` (default)

Inductance of the rotor, specified with respect to the stator.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By
equivalent circuit parameters`.

### **Magnetizing inductance Lm** — Stator magnetizing inductance `0.5` `H` (default)

Magnetizing inductance of the stator. Its value is hard to estimate
from motor parameters, but the effect is usually small. If you do not
know its value, use a typical value of 25 times the **Stator
inductance L1** value.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By
equivalent circuit parameters`.

### **Rated mechanical power** — Motor mechanical power `825` `W` (default)

Mechanical power the motor delivers when running at the rated
speed.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **Rated speed** — Rated motor speed `3500` `rpm` (default)

Speed at which the motor delivers the specified **Rated
mechanical power** value.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **Rated RMS line-to-line voltage** — Rated line-to-line voltage `200` `V` (default)

Line-to-line voltage at which the motor ratings are specified.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **Rated supply frequency** — Frequency of the AC supply voltage `60` `Hz` (default)

Frequency of the AC supply voltage at which the motor ratings are
specified.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **Rated RMS line current** — Rated line current `2.7` `A` (default)

Line current at which the motor delivers the specified **Rated
mechanical power** value.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **R1 parameterization** — Equivalent circuit resistance parameterization `From motor efficiency` (default) | `From power factor` | `Use measured stator resistance R1`

Select one of the following parameterizations for the equivalent
circuit resistance, R1, of the motor:

- `From motor efficiency` —
  Calculate R1 from the motor
  efficiency. This is the default method.
- `From power factor` —
  Calculate R1 from the motor power
  factor.
- `Use measured stator resistance
  R1` — Measure
  R1 directly.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings`.

### **Motor efficiency (percent)** — Motor efficiency `95` (default)

The percentage of input power to the motor that gets delivered to the
mechanical load when running at the **Rated speed**
value.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings` and the **R1
parameterization** parameter to `From motor
efficiency`.

### **Motor power factor** — Motor power factor `0.93` (default)

The cosine of the angle by which the supply current lags the supply
voltage when running at the **Rated mechanical power**
value.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings` and the **R1
parameterization** parameter to `From power
factor`.

### **Measured stator resistance R1** — Measured stator resistance `1` `Ohm` (default)

The measured stator resistance.

#### Dependencies

This parameter is visible only when you set the **Model
parameterization** parameter to `By motor
ratings` and the **R1
parameterization** parameter to `Use
measured stator resistance R1`.

### **Number of pole pairs** — Number of motor pole pairs `1` (default)

Total number of pole pairs for the motor.

### **Number of phases** — Number of supply phases `3` (default)

Number of supply phases.

### **Stator connections** — Motor stator configurations `Delta configuration` (default) | `Star configuration`

Select one of the following motor configurations:

- `Delta configuration` —
  Connect the motor stator windings in delta
  configuration.
- `Star configuration` —
  Connect the motor stator windings in star
  configuration.

### Power Supply

### **Supply RMS line-to-line voltage** — Supply RMS line-to-line voltage `200` `V` (default)

The line-to-line voltage that supplies the motor.

### **Supply frequency** — AC supply frequency `60` `Hz` (default)

Frequency of the AC supply voltage.

### Mechanical

### **Rotor inertia** — Rotor inertia `1e-3` `kg*m^2` (default)

Rotor inertia. The value can be zero.

### **Rotor damping** — Rotor damping `1e-4` `N*m/(rad/s)` (default)

Rotor damping. The value can be zero.

### **Initial rotor speed** — Initial rotor speed `0` `rpm` (default)

Speed of the rotor at the start of the simulation.

### Temperature Dependence

This tab appears only for blocks with exposed thermal ports.

### **Stator and rotor resistance temperature coefficients, [alpha\_1 alpha\_2]** — Stator and rotor resistance temperature coefficients `[.00393, .00393]` `1/K` (default)

A 1 by 2 row vector defining the coefficient α in the equation
relating resistance to temperature, as described in Thermal Model for Actuator Blocks. The first element
corresponds to the stator, and the second to rotor. The default value is
for copper.

### **Measurement temperature** — Measurement temperature `25` `C` (default)

The temperature for which motor parameters are defined.

### Thermal Port

This tab appears only for blocks with exposed thermal ports.

### **Stator and rotor thermal masses, [M\_1 M\_2]** — Stator and rotor thermal masses `[100, 100]` `J/K` (default)

A 1 by 2 row vector defining the thermal mass for the stator and rotor
windings. The thermal mass is the energy required to raise the
temperature by one degree.

### **Stator and rotor initial temperatures, [T\_1 T\_2]** — Stator and rotor initial temperatures `[25, 25]` `C` (default)

A 1 by 2 row vector defining the temperature of the stator and rotor
thermal ports at the start of simulation.
## Libraries

Simscape / Electrical / Electromechanical / Asynchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Induction motor powered by ideal AC supply

The Simplified Induction Motor block represents the
electrical and torque characteristics of an induction motor powered by an ideal AC
supply. The following figure shows the equivalent circuit model of the
Simplified Induction Motor block.

In the figure:

- *R1* is the stator
  resistance.
- *R2* is the rotor resistance with
  respect to the stator.
- *L1* is the stator
  inductance.
- *L2* is the rotor inductance with
  respect to the stator.
- *Lm* is magnetizing
  inductance.
- s is the rotor slip.
- V¯ and I¯ are the sinusoidal supply voltage and current
  phasors.

Rotor slip s is defined in terms of the mechanical rotational speed ωm, the number of pole pairs p, and the electrical supply frequency ω by

s=1−pωmω

This means that the slip is one when starting, and zero when running
synchronously with the supply frequency.

For an *n*-phase induction motor the torque-speed relationship is
given by:

T=npR2sωVrms2(R1+R2+1−ssR2)2+(X1+X2)2

where:

- *Vrms* is the line-neutral supply
  voltage for a star-configuration induction motor, and the line-to-line
  voltage for a delta-configuration induction motor.
- *n* is the number of phases.

You can parameterize this block in terms of the preceding equivalent circuit model
parameters or in terms of the motor ratings the block uses to derive these
parameters.

This block produces a positive torque acting from the mechanical C to R ports.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to heat. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain
  thermal ports.
- `Show thermal port` — The block contains multiple
  thermal conserving ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
