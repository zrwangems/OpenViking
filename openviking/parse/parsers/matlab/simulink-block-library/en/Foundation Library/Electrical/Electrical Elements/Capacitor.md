---
type: simulink-block
title: 'Capacitor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'capacitor'
documentation_source_path: 'ref/capacitor.html'
language: en
---

# Capacitor

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the capacitor positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the capacitor negative terminal.

## Parameters

### **Capacitance** — Capacitance of the capacitor `1e-6 F` (default) | positive scalar

Capacitance value.

### **Series resistance** — Small parasitic effects `1e-6 Ohm` (default) | nonnegative scalar

Represents small parasitic effects. The series resistance can be used to represent
component internal resistance, effective series resistance (ESR), or connection
resistance. Simulation of some circuits may require the presence of the small series
resistance.

### **Parallel conductance** — Small parasitic effects `0 1/Ohm` (default) | nonnegative scalar

Represents small parasitic effects. The parallel conductance directly across the
capacitor can be used to model dielectric losses, or leakage current per volt.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Linear capacitor in electrical systems

The Capacitor block models a linear capacitor, described
with the following equation:

I=CdVdt

where:

- *I* is current.
- *C* is capacitance.
- *V* is voltage.
- *t* is time.

The **Series resistance** and **Parallel conductance**
parameters represent small parasitic effects. The parallel conductance directly across the
capacitor can be used to model dielectric losses, or equivalently leakage current per volt.
The series resistance can be used to represent component effective series resistance (ESR) or
connection resistance. Simulation of some circuits may require the presence of the small
series resistance. For more information, see Modeling Best Practices.

Connections + and – are conserving electrical ports corresponding to the positive and
negative terminals of the capacitor, respectively. The current is positive if it flows from
positive to negative, and the voltage across the capacitor is equal to the difference between
the voltage at the positive and the negative terminal, *V*(+) –
*V*(–).

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

**Current** and **Voltage** are the electrical domain
variables. **Capacitor voltage** is the initial voltage across the
capacitor. See the block source code for more information.
