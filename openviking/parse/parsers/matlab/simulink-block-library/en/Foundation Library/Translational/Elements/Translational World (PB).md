---
type: simulink-block
title: 'Translational World (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalworldpb'
documentation_source_path: 'ref/translationalworldpb.html'
language: en
---

# Translational World (PB)

## Ports

### Conserving

### **R** — Absolute zero position and velocity position-based mechanical translational

Position-based mechanical translational conserving port that sets absolute zero
position and velocity for the connected circuit.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Global reference frame for position-based translational network

The Translational World (PB) block represents the
stationary global reference frame. This block sets absolute zero position and velocity for the
connected circuit. All positions in the connected circuit are relative to this reference. All
position-based translational ports connected to this block are stationary.

Each position-based translational circuit requires a Translational World
(PB) block

The Translational World (PB) block represents a single
point in space. Therefore, in most situations it is consistent with the physical view to have
only one Translational World (PB) block in a connected circuit.
