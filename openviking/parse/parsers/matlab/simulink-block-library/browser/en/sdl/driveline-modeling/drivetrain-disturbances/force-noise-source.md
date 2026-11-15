---
type: simulink-block
title: 'Force Noise Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Drivetrain Disturbances'
documentation_page: 'forcenoisesource'
documentation_source_path: 'ref/forcenoisesource.html'
language: en
---

# Force Noise Source

## Ports

### Input

### **P** — Single-sided noise power spectral density physical signal

The power spectral density (*PSD*) of noise is the
average noise power per unit of bandwidth, in
N2/Hz.
### Conserving

### **B** — Base interface mechanical translational

Mechanical translational conserving port associated with the base
interface.

### **F** — Follower interface mechanical translational

Mechanical translational conserving port associated with the follower
interface.

## Parameters

### **Sample time** — Time step period and offset `1e-3` `s` (default) | `[step, offset]` `s`

The values of the time *step* period and the initial time
*offset*. If you specify a scalar value for
*step*, the block assumes an *offset*
value of `0`.To specify a nonzero value for the initial
time offset, specify the parameter values using the vector
`[step,
offset]`. The *offset*
value must be less than the *step* value and greater than
or equal to zero.

### **Repeatability** — Random number seed control `Not repeatable` (default) | `Repeatable` | `Specify seed`

The random number seed is the number that initializes the random number
generator. The seed is `0` or a positive integer. To
control the random number seed, set this parameter to:

- `Not repeatable` — The seed
  changes every time you simulate your model. The block resets the
  random seed using the MATLAB® random number generator command:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The seed is the
  same random number at the start of every simulation. The block
  sets the value using the same MATLAB random number generator command used by the
  `Not repeatable` parameter.

  When you add a Force Noise Source block to your
  model from the Sources library, the block generates and stores a
  random value for the repeated seed. When you make a copy of the
  Force Noise Source block from an existing
  block in a model, the copy generates a new random value for the
  repeated seed.
- `Specify seed` — The seed is a
  number that you specify using the **Seed**
  parameter. The **Seed** parameter is only
  available when you choose `Specify
  seed` for the
  **Repeatability** parameter.

### **Seed** — Random number generation seed value `0` (default)

The seed must be `0` or a positive integer. This
parameter is only available when you select `Specify
seed` for the **Repeatability**
parameter.

## Libraries

Simscape / Driveline / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Model zero-mean normally (Gaussian) distributed force

The Force Noise Source block generates zero-mean normally (Gaussian)
distributed force using the PS Random Number source in the
Simscape™ Foundation library. The force produced by the block depends on two factors:

- The noise power spectral density input to the block
- A random number seed that you control using the
  **Repeatability** and, as applicable,
  **Seed** parameters

The defining equation for the force that the block generates is

F=PSD/2N(0,1)h,

where:

- *F* is the output force.
- *PSD* is the single-sided noise power spectral
  density.
- *N* is a Gaussian random number with zero mean and
  standard deviation of one.
- *h* is the sampling interval.
