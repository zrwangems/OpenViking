---
type: simulink-block
title: '3x3 Cross Product'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: '3x3crossproduct'
documentation_source_path: '3x3crossproduct.html'
language: en
---

# 3x3 Cross Product

## Ports

### Input

### **A** — First cross product input 3-by-1 vector

First cross product input, specified as a vector.

**Example:** `[10 2 3]`

**Data Types:** `double`

### **B** — Second cross product input 3-by-1 vector

Second cross product input, specified as a vector.

**Example:** `[10 2 3]`

**Data Types:** `double`
### Output

### **C** — Cross product 3-by-1 vector

Cross product, output as a vector.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Utilities / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate cross product of two 3-by-1 vectors

The 3x3 Cross Product block computes cross (or vector)
product of two vectors, *A* and *B*. The block
generates a third vector, *C*, in a direction normal to the plane
containing *A* and *B*, with magnitude equal to the
product of the lengths of *A* and *B* multiplied by
the sine of the angle between them. The direction of *C* follows the
right-hand rule in turning from *A* to *B*. For
related equations, see Algorithms.
