---
type: simulink-block
title: 'Supercapacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'supercapacitor'
documentation_source_path: 'ref/supercapacitor.html'
language: en
---

# Supercapacitor

## Ports

### Conserving

### **+** — Positive electrical terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative electrical terminal electrical

Electrical conserving port associated with the negative
terminal.

## Parameters

#### Cell Characteristics

### **Fixed resistances, [R1 R2 R3]** — Fixed resistance values for each branch `[0.2, 90.0, 1000.0]` `Ohm` (default)

Specify the resistances for the fixed resistors in the individual branches
of the supercapacitor as an array.

### **Fixed capacitances, [C1 C2 C3]** — Fixed capacitance values for each branch `[2.5, 1.5, 4.0]` `F` (default)

Specify the individual capacitances for the fixed capacitors in the
supercapacitor as an array.

### **Voltage-dependent capacitor gain** — Variable capacitance coefficient for the first branch `0.95` `F/V` (default)

Specify the variable capacitance coefficient,
*Kv*, for the
voltage-dependent capacitor in the first branch of the supercapacitor. For
information on determining the variable capacitance coefficient, see [1].

### **Self-discharge resistance** — Resistance to self-discharge `inf` (default)

Specify the self-discharge resistance of the supercapacitor that is
connected between the two terminals.

#### Configuration

### **Number of series cells** — Number of supercapacitor cells in series `1` (default)

Specify the number of cells in the supercapacitor that are in a series
configuration.

### **Number of parallel cells** — Number of supercapacitor cells in parallel `1` (default)

Specify the number of cells in the supercapacitor that are in a parallel
configuration.

#### Variables

### **Beginning Value** — Initial target value `0` (default)

Use the **Variables** tab to set the priority and initial
target values for the block variables before simulation. For more
information, see Set Priority and Initial Target for Block Variables.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Electrochemical double-layer capacitor

The Supercapacitor block represents an electrochemical
double-layer capacitor (ELDC), which is commonly referred to as a supercapacitor or an
ultracapacitor. The capacitance values for supercapacitors are orders of magnitude
larger than the values for regular capacitors. Supercapacitors can provide bursts of
energy because they can charge and discharge rapidly.

You can model any number of supercapacitor cells connected in series or in parallel
using a single Supercapacitor block. To do so, set the
relevant parameter, that is **Number of series cells** or
**Number of parallel cells**, to a value larger than
`1`. Internally, the block simulates only the equations for a
single supercapacitor cell, but it calculates:

- The output voltage according to the number of series-connected
  cells
- The current according to the number of parallel-connected cells

Calculating the output of a multiple-cell supercapacitor based on the
output for a single cell is more efficient than simulating the equations for each cell
individually.

The figure shows the equivalent circuit for a single cell in the
Supercapacitor block. The circuit is a network of
resistors and capacitors that is commonly used to model supercapacitor behavior.

Capacitors *C1*,
*C2*, and
*C3* have fixed capacitances. The
capacitance of capacitor *Cv* depends on the
voltage across it. Resistors *R1*,
*R2*, and
*R3* have fixed resistances. The voltage
across each individual fixed capacitor in the
Supercapacitor block is calculated as

Vcn=vNseries−inRn,

where:

- *v* is the voltage across the block.
- *Nseries*  is the number of cells
  in series.
- *n* is the branch number. *n* = [1, 2,
  3].
- *in* is the current through the
  *n*th branch.
- *Rn* is the resistance in the
  *n*th branch.
- *Vcn* is voltage across the
  capacitor in the *n*th branch.

The equation for the current through the first branch of the supercapacitor depends on
the voltage across the capacitors in the branch. If the capacitors experience a positive
voltage, that is

Vc1>0,

then

i1=(C1+KvVc1)dVc1dt,

else

i1=C1dVc1dt,

where:

- *Vc1* is voltage across the
  capacitors in the first branch.
- *C1*  is the capacitance of the
  fixed capacitor in the first branch.
- *Kv* is the voltage-dependent
  capacitance gain.
- *i1* is the current through the
  first branch.

For the remaining branches, the current is defined as

in=CndVcndt,

where:

- *n* is the branch number. *n* =[2,
  3].
- *Cn*  is the capacitance of the
  *n*th branch.

The total current through the Supercapacitor block is

i=Nparallel(i1+i2+i3+vRdischarge),

where:

- *Nparallel* is the number of cells
  in parallel.
- *Rdischarge* is the self-discharge
  resistance of the supercapacitor.
- *i* is the current through the supercapacitor.
