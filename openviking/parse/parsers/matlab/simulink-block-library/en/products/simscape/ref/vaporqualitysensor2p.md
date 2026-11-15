---
type: simulink-block
title: 'Vapor Quality Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Sensors'
documentation_page: 'vaporqualitysensor2p'
documentation_source_path: 'ref/vaporqualitysensor2p.html'
language: en
---

# Vapor Quality Sensor (2P)

## Ports

### Output

### **X** — Vapor quality, unitless physical signal

Physical signal output port for measuring the fraction of vapor in a two-phase
fluid. Use the **Vapor fraction specification** parameter to select
the type of measurement.
### Conserving

### **A** — Sensor inlet two-phase fluid

Two-phase fluid conserving port. Connect this port to the node in the two-phase
fluid network where you want to measure the vapor quality.

## Parameters

### **Vapor fraction specification** — Whether to express vapor fraction on a mass basis or on a volume basis `Vapor quality` (default) | `Vapor void fraction`

Type of measurement to report at port **X**. Select
`Vapor quality` for the mass fraction of vapor in a two-phase
fluid. Select `Vapor void fraction` for the volume fraction
instead. The measurement can range from `0` to `1` in
both cases. For critical and supercritical fluids, the output is
`-1`.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Measure vapor fraction in two-phase fluids

The Vapor Quality Sensor (2P) block measures the fraction
of vapor in a two-phase fluid. That fraction can be expressed on a mass basis (the vapor
quality of the fluid) or on a volume basis (the vapor void fraction). Use the **Vapor
fraction specification** block parameter to specify the basis.

The block measures the vapor quality at port **A** and reports it as a
physical signal at port **X**. The physical signal value can range from
`0` in pure liquid to `1` in pure vapor. Intermediate
values correspond to two-phase mixtures. The sensor is ideal, that is, neither mass nor energy
exchanges take place.

If the pressure rises above the critical point for the fluid, vapor and liquid cease to
exist, and the measurement becomes undefined. The block then outputs `-1`, a
value that serves to indicate a critical or supercritical state.
