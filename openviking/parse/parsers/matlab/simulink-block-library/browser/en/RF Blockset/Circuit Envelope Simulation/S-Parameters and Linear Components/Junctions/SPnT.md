---
type: simulink-block
title: 'SPnT'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'spnt'
documentation_source_path: 'ref/spnt.html'
language: en
---

# SPnT

## Ports

### Input

### **Ctl** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`

## Parameters

#### Main

### **Insertion loss (dB)** — Insertion loss of switch `1` (default) | scalar

Insertion loss value of switch, specified as a finite scalar in decibels.
Specify an insertion loss value greater than zero but less than the
isolation value of the switch. For the equation, see Insertion Loss.

### **Isolation (dB)** — Isolation value of switch `70` (default) | scalar

Isolation value of switch, specified as a scalar in decibels. Specify an
isolation value greater than the insertion loss value of the switch. For the
equation, see Isolation.

### **Loading type** — Switch type `Absorptive` (default) | `Reflective`

Switch type, specified as `Absorptive` or
`Reflective`.

### **Number of outputs** — Number of outputs for switch `2` (default) | scalar

Number of outputs for the switch, specified as a scalar. The number of
outputs must be greater than or equal to two or less than or equal to
eight.

### **Port terminations (Ohm)** — Port terminations `50` (default) | scalar

Port terminations representing matching required at all input and output
ports, specified as a scalar in ohms. If you set the **Load
type** is `Absorptive`, the impedance
seen at all disconnected output ports is the value specified in
**Port terminations**.

### **Ground and hide reference terminals** — Ground RF circuit terminals on (default) | off

Select this parameter to internally ground and hide the reference
terminals. To expose the reference terminals, clear this parameter. By
exposing this terminal, you can connect it to other parts of your model.

## Libraries

RF Blockset / Circuit Envelope / Junctions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Single pole multiple throw switch

The SPnT block models a single pole multiple throw switch. This block
supports both reflective and absorptive switches. You can specify two to eight output
ports for the switch. The control signal is a Simulink® signal connected to the `Ctl` port of the block. The
control signal specifies which output port transmits the input signal. When the input to
the `Ctl` port is between one and the number of output ports, the
`Ctl` signal value is rounded to the nearest integer. The output
port that corresponds to the integer value transmits the data. If the rounded
`Ctl` signal value does not correspond to any of the output ports,
then all the output ports are turned off.
