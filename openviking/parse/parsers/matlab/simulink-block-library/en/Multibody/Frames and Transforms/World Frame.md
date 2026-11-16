---
type: simulink-block
title: 'World Frame'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Frames and Transforms'
documentation_page: 'worldframe'
documentation_source_path: 'ref/worldframe.html'
language: en
---

# World Frame

## Ports

### Frame

### **W** — World frame frame

World frame represented by the block. Connect to another frame to fix
the position and orientation of that frame to the world frame.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Multibody / Frames and Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Inertial reference frame

This block represents the global reference frame in a model. This frame is inertial
and at absolute rest. Rigidly connecting a frame to the World frame makes that frame
inertial. Frame axes are orthogonal and arranged according to the right-hand
rule.

In a frame network, the World frame is the ultimate reference frame. Directly or
indirectly, all other frames are defined with respect to the World frame. If multiple
World Frame blocks connect to the same frame network, those blocks identify the same
frame. If no World Frame block connects to a frame network, a copy of an existing frame,
frozen in its initial position and orientation, serves as the World frame.
