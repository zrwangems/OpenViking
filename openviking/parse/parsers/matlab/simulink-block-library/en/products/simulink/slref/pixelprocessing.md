---
type: simulink-block
title: 'Pixel Processing'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'pixelprocessing'
documentation_source_path: 'slref/pixelprocessing.html'
language: en
---

# Pixel Processing

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Control block for Pixel Processing Subsystem

The Pixel Processing block serves as a control block for the Pixel Processing
Subsystem block. The Pixel Processing Subsystem block iterates over a
3-dimensional input matrix. At each iteration step, the subsystem processes a
1-by-1-by-*`n`* subset of the input matrix, where
*`n`* is the size of the third dimension of the input matrix. The
subsystem outputs a 2-dimensional matrix with the same first two dimensions as the input
matrix.
