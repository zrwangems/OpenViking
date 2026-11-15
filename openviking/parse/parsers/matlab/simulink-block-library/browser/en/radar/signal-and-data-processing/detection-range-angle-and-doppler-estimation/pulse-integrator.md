---
type: simulink-block
title: 'Pulse Integrator'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'pulseintegrator'
documentation_source_path: '../phased/ref/pulseintegrator.html'
language: en
---

# Pulse Integrator

## Ports

### Input

### **x** — Pulse input data matrix

Pulse input data, specified as a matrix. Each column of
`x` is one pulse.

**Data Types:** `double`
### Output

### **∑x** — Integrated pulse column vector

Integrated pulse, returned as an *N*-by-1 column
vector, where *N* is the number of rows in the input
`x`.

**Data Types:** `double`

## Parameters

### **Integration method** — Integration method `Coherent` (default) | `Noncoherent`

Specify the integration method as `Coherent` or
`Noncoherent`.

### **Number of pulses to integrate** — Number of pulses to integrate `10` (default)

Specify the number of pulses to integrate as an integer.

### **Integration overlap (in pulses)** — Integration overlap `0` (default)

Specify the number of overlapped pulses in successive integrations as an
integer. This number must be less than the value specified in
**Number of pulses to integrate**.

## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Coherent or noncoherent pulse integration

The Pulse Integrator block performs coherent or noncoherent integration of
successive pulses of a signal and puts out an integrated output. You can specify how
many pulses to integrate and the number of overlapped pulses in successive
integrations.
