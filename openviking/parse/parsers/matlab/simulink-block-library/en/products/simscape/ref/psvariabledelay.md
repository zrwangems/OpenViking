---
type: simulink-block
title: 'PS Variable Delay'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Delays'
documentation_page: 'psvariabledelay'
documentation_source_path: 'ref/psvariabledelay.html'
language: en
---

# PS Variable Delay

## Ports

### Input

### **U** — Input physical signal, untyped physical signal

Input physical signal that is being delayed.

### **T** — Delay time, s physical signal

Input physical signal that supplies the delay time.

### **H** — Output during initial time interval, untyped physical signal

Input physical signal that supplies the value to be output during the initial time
interval, when time since the start of simulation is less than or equal to the delay
time. The signal unit must be commensurate with the unit of the output signal at port
**Y**.
### Output

### **Y** — Output physical signal, untyped physical signal

Output physical signal.

## Parameters

### **Maximum delay time** — Delay time for the signal `10 s` (default)

The upper limit for the delay time. Exceeding the maximum delay time during
simulation results in a runtime error. The parameter value must be positive.

## Libraries

Simscape / Foundation Library / Physical Signals / Delays

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Delay input physical signal by variable time

The PS Variable Delay block generates the output physical
signal, **Y**, by delaying the input physical signal,
**U**:

*Y* = *U* ( *t* –
*τ* )

where *τ* is the delay time, which can vary throughout the simulation.
You supply the delay time as a signal through the input port **T**.

For the initial time interval, when *t* <= StartTime +
*τ*, the block outputs the value of the signal supplied through the input
port **H**.

**Note**

- When simulating a model that contains blocks with delays, memory allocation for
  storing the data history is controlled by the **Delay memory budget
  [kB]** parameter in the Solver Configuration block. If this budget is exceeded, simulation
  errors out. You can adjust this parameter value based on your available memory
  resources.
- For recommendation on how to linearize a model that contains blocks with delays, see
  Linearizing with Simulink Linearization Blocks.

Untyped physical ports facilitate unit propagation. The output signal at port
**Y** has the same physical unit as the input signal at port
**U**. The signal unit at port **H** must be commensurate
with the unit of the output signal.

The Variable Transport Delay example shows how you can model a
variable transport delay using a custom block authored in Simscape™ language.
