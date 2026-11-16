---
type: simulink-block
title: 'Induction Machine Direct Torque Control with Space Vector Modulator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrolwithspacevectormodulator'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrolwithspacevectormodulator.html'
language: en
---

# Induction Machine Direct Torque Control with Space Vector Modulator

## Ports

### Input

### **FluxRef** — Flux scalar

Reference stator flux.

**Data Types:** `single` | `double`

### **TqRef** — Torque scalar

Reference torque.

**Data Types:** `single` | `double`

### **vabc** — Voltage vector

Stator phase voltages.

**Data Types:** `single` | `double`

### **iabc** — Current vector

Stator phase currents.

**Data Types:** `single` | `double`

### **Vdc** — DC-link voltage signal scalar

DC-link voltage for the converter.

**Data Types:** `single` | `double`

### **Reset** — Controller reset scalar

Reset for the PI controller integrators.

**Data Types:** `single` | `double`
### Output

### **G** — Gate pulses vector | `0` or `1`

Inverter gate pulses. The block does not consider any dead
time.

**Data Types:** `single` | `double`

### **ModWave** — Modulation wave vector

Modulation wave you deploy to the hardware if you are generating code for a platform
with PWM-capable hardware. Otherwise, this data is only for your
reference.

## Parameters

### General

### **Stator resistance (Ohm)** — Resistance `0.25` (default) | positive scalar

Resistance of the machine stator.

### **Number of pole pairs** — Pole number `1` (default) | positive integer

Number of machine pole pairs.

### **Inverter dc-link voltage threshold (V)** — Voltage `300` (default) | positive scalar

Voltage threshold to activate the power inverter.

### **Fundamental sample time (s)** — SVM sample time `5e-6` (default) | positive scalar less than the control sample time

Sample time for the space vector modulator. Fundamental sample time
must be less than the control sample time.

### **Control sample time (s)** — PI sample time `5e-5` (default) | positive scalar greater than the fundamental sample time

Sample time for PI controllers. Control sample time must be greater
than the fundamental sample time.

### **Switching frequency (Hz)** — Switching rate `1000` (default) | positive scalar

Specify the rate at which you want the switches in the power converter
to switch.

### Control Parameters

### **Flux controller proportional gain** — Flux PI proportional gain `150` (default) | positive scalar

Proportional gain for the flux controller.

### **Flux controller integral gain** — Flux PI integral gain `3000` (default) | positive scalar

Integral gain for the flux controller.

### **Flux controller anti-windup gain** — Flux PI anti-windup gain `1` (default) | positive scalar

Anti-windup gain for the flux controller.

### **Torque controller proportional gain** — Torque PI proportional gain `1` (default) | positive scalar

Proportional gain for the torque controller.

### **Torque controller integral gain** — Torque PI integral gain `50` (default) | positive scalar

Integral gain for the torque controller.

### **Torque controller anti-windup gain** — Torque PI anti-windup gain `1` (default) | positive scalar

Anti-windup gain for the torque controller.

### **Axis prioritization** — Axis prioritization for voltage limiter `Q-axis` (default) | `D-axis` | `D-Q equivalence`

Prioritize or maintain ratio between *d*- and
*q*-axes when the block limits voltage.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Induction machine DTC structure with SVM

The Induction Machine Direct Torque Control with Space Vector Modulator
implements an induction machine direct torque control structure (DTC) with space vector
modulator (SVM). Use this block to generate the gate pulses for an inverter controlling
an induction machine. This diagram shows the architecture of the block.

In the diagram:

- You provide the reference torque, *T\**, and flux,
  *ψ\**.
- The Flux and Torque Estimator estimates the actual torque,
  *T*, and flux, *ψ* from the measured
  phase currents, *iabc*, and
  voltages, *vabc*.
- Two PI controllers determine the reference *d* and
  *q* voltages,
  *vd* and
  *vq*, from the flux and
  torque errors, respectively.
- The SVM generates the gates pulses,
  *Gij*, required to control an
  inverter driving the induction machine. Subscript *i*
  corresponds to the phase (*a*, *b*, or
  *c*). Subscript *j* corresponds to the
  high, *H*, or low, *L*, signal.

### Flux and Torque Estimator

To estimate the torque and flux, the block discretizes the machine voltage
equations in the stationary *ɑβ* reference frame using the backward
Euler method. The discrete-time equations for stator fluxes in the
*ɑβ* frame are:

ψα=(vα−iαRs)Tszz−1

ψβ=(vβ−iβRs)Tszz−1

Where:

- *vɑ* and
  *vβ* are the
  *ɑ*- and *β*-axis voltages,
  respectively.
- *iɑ* and
  *iβ* are the
  *ɑ*- and *β*-axis currents,
  respectively.
- *Ψɑ* and
  *Ψβ* are the
  *ɑ*- and *β*-axis stator fluxes,
  respectively.
- *Rs* is the stator
  resistance.

The block calculates the torque and total stator flux as:

T=3p2(ψαiβ−ψβiα)

ψs=ψα2+ψβ2

Where:

- *p* is the number of pole pairs.
- *Ψs* is the total stator
  flux.

### Space Vector Modulator

The SVM converts the desired voltages into gate pulses, which you use to control
an inverter. This figure shows possible switching states of a three-phase inverter.

The hexagon represents the space vector diagram. Each of the six
vertices represents a possible switching state
*(GAH,GBH,GCH)*
of the three-phase inverter. Each low gate takes the opposite state as its
corresponding high gate. The inverter diagram illustrates the current state.

The rotating vector in the space vector diagram corresponds to the complex
reference voltage vector, which rotates at the desired electrical frequency of the
machine. In reality, the switching frequency is much faster than this electrical
frequency. As a result, the inverter switches continually between the two states
enclosing its current region *Ri*, and the zero state corresponding
to *(0,0,0)*, to generate the desired voltages.

To learn about the implementation of this method, see the PWM Generator (Three-phase, Two-level) block.
