---
type: simulink-block
title: 'Barometer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'barometer'
documentation_source_path: 'ref/barometer.html'
language: en
---

# Barometer

## Ports

### Input

### **True pressure** — True air pressure scalar | vector

True air pressure in Pa, specified as a scalar or *N*-element
vector, where *N* is the number of air pressure measurements.

**Data Types:** `single` | `double`
### Output

### **Measured pressure** — Measured air pressure scalar | vector

Measured air pressure in Pa, returned as a nonnegative scalar or
*N*-element vector. The length of Measured pressure matches the
length of True pressure.

**Data Types:** `single` | `double`

## Parameters

### **Constant bias** — Constant measurement bias 0 (default) | finite scalar

Specify the constant measurement bias as a finite scalar, in Pa.

### **Noise density** — White noise standard variance 1 (default) | nonnegative finite scalar

Specify the white noise standard variance as a nonnegative finite scalar. This
parameter specifies the power spectral density of the sensor noise in Pa/√Hz.

### **Bias instability** — Correlated noise standard variance 1 (default) | nonnegative finite scalar

Specify the correlated noise standard variance as a nonnegative finite scalar, in
Pa

### **Decay factor** — Correlated noise decay factor 0.99 (default) | positive scalar in the range (0,1)

Specify the correlated noise decay factor as a scalar in the range (0, 1).

Specifying a smaller decay factor models the correlated noise closer to white noise,
while specifying a larger decay factor models the correlated noise closer to a random
walk process.

### **Seed** — Random number initial seed `67` (default) | nonnegative integer scalar

Specify the Initial seed of the mt19937ar random number generator algorithm as a
real, nonnegative integer scalar.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate the model
  using the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change.

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Barometer sensor model with noise

The Barometer block models a barometer sensor that generates an air
pressure reading with a measurement noise that consists of constant measurement bias,
uncorrelated white noise, and correlated noise [1]. For more information on the
noise model, see Noise Model.
