---
type: simulink-block
title: 'Battery Cell Contact Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'batterycellcontactmonitoring'
documentation_source_path: 'ref/batterycellcontactmonitoring.html'
language: en
---

# Battery Cell Contact Monitoring

## Ports

### Input

### **Voltage** — Parallel assembly voltages, V vector

Voltages of parallel assemblies, in volts, specified as a vector.
### Output

### **CellConnectionError** — Indication of contact loss error, unitless vector

Indication of a contact loss error, returned as a vector of values that can be
either `0` or `1`. Elements equal to
`1` correspond to cells or parallel assemblies that have a contact
loss symptom for a time longer than the value of the **Qualification time
(s)** parameter, which indicates a loss-of-contact failure.

The size of this port is equal to the size of the **Voltage** input
port.

### **CellConnectionSymptom** — Indication of contact loss symptom, unitless vector

Indication of a contact loss symptom, returned as a vector of values that can be
either `0` or `1`. Elements equal to
`1` correspond to cells or parallel assemblies where the block
senses a contact issue.

The size of this port is equal to the size of the **Voltage** input
port.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Time constant for voltage change smoothing (s)** — Time constant for voltage change smoothing 10 (default) | positive scalar

Time constant for the voltage change smoothing.

### **Threshold for voltage change detection (dV/dt)** — Threshold for voltage change detection 5e-4 (default) | positive scalar

Threshold over which the block detects a change in voltage.

### **Allowed voltage change peak-to-average ratio** — Allowed peak-to-average ratio of voltage change 0.02 (default) | positive scalar

Allowed peak-to-average ratio of the voltage change.

### **Cumulative error threshold** — Cumulative error threshold for contact loss symptom 1e-4 (default) | positive scalar

Cumulative error threshold that the block uses to detect the contact loss
symptom.

### **Qualification time (s)** — Time to qualify contact loss error `20` (default) | positive scalar

Time required to qualify the contact loss error after the block detects a symptom,
in seconds.

### **Disqualification time (s)** — Time to disqualify contact loss error `0` (default) | nonnegative scalar

Time required to disqualify the contact loss error after the block detects a
symptom, in seconds. If you set this parameter to `0`, the block does
not disqualify the errors.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | positive integer

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this parameter as a
positive integer. For continuous-time operation, specify this parameter as
`0`.

If this block is in a masked subsystem or a variant subsystem that allows you to
switch between continuous and discrete operations, promote the sample time parameter.
Promoting the sample time parameter ensures correct switching between the continuous and
discrete implementations of the block. For more information, see Promote Block Parameters on a Mask.

### **Algorithm data type** — Option to choose data type for block algorithm `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*Since R2025a*

Option to choose the data type for the block algorithm, specified as one of these values:

- `Inherit: auto` — You can simulate the block in
  both `single` and `double`
  precision. You must explicitly provide the inputs and parameters as either
  `single` or
  `double`.
- `double` — The block algorithm casts all inputs
  and parameters to `double` data type.
- `single` — The block algorithm casts all inputs
  and parameters to `single` data type.
- `<data type expression>` — The block
  algorithm casts all inputs and parameters to the data type object you
  specify.

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant and Control Data Types of Signals.

## Libraries

Simscape / Battery / BMS / Protection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Monitor for battery cell contact

The Battery Cell Contact Monitoring block monitors the state of contact
between the cells of a battery. Algorithms for cell contact monitoring are essential for the
safety, performance, and reliability of battery systems, especially in a battery pack with
many cells.

This block first checks for cell contact loss symptoms in parallel assemblies. If the
block detects a symptom, and this symptom lasts for longer than the value of the
**Qualification time (s)** parameter, then the block reports the symptom as
a loss-of-contact error.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the block for
continuous time, set the parameter to `0`. To configure the block for
discrete time, set the parameter to a positive, nonzero value, or to `-1` to
inherit the sample time from an upstream block.

This diagram shows the structure of the block:

### Equations

In faulty contacts between cells, the rate of voltage change can be very small, and the
noise can have a negative impact in the algorithm accuracy. The block computes the rate of
change of voltage using a filtered derivative that smooths the output,

Δvi=sTs+1vi,i=1,…,N;N>1,

where:

- *T* is the time constant for the smoothing.
- *vi* is the *i*th cell or
  parallel assembly voltage.
- *Δvi* is the smoothed rate of voltage
  change for the *i*th cell or parallel assembly.
- Δv=[Δv1,Δv2,…,ΔvN]T.
- v=[v1,v2,…,vN]T.

When a loss-of-contact fault occurs in a parallel assembly, the rate of voltage change
increases. The value of this increase is inversely related to the number of cells inside the
parallel assembly. This figure shows the evolution of voltage over time for a functioning
parallel assemblies and a faulted parallel assembly.

The block assumes that not all parallel assemblies are faulted and uses the average rate
of change for the voltage as reference. To check for faulty symptoms, the block directly
compares the deviation of the cumulative error against a given threshold,

ui={|Δvi|,when |Δvi|>ΔVthΔVth,when |Δvi|≤ΔVthuaverage=1NPA∑i=1NPAui

where *ΔVth* is the detection
threshold of the voltage change used to eliminate the measurements where the battery is in
idle mode or is close to idle mode, and *N*PA is the
number of parallel assemblies.

The block then detects the symptoms if

Symptom={0,when∫(u−(1+VoltageChangePar)uaverage)<eth1,when∫(u−(1+VoltageChangePar)uaverage)≥eth

where *eth* is the cumulative
error threshold and *VoltageChangePar* is the allowed peak-to-average
ratio. If *VoltageChangePar* is very small, the block can detect a false
positive. If *VoltageChangePar* is too large, the block can detect a false
negative.

### Assumptions and Limitations

- The block does not assume that all parallel assemblies are faulted.
- The block does not assume that all cells inside a parallel assemblies are
  faulted.
