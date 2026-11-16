---
type: simulink-block
title: 'Interface (PB-Translational)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Utilities'
documentation_page: 'interfacepbtranslational'
documentation_source_path: 'ref/interfacepbtranslational.html'
language: en
---

# Interface (PB-Translational)

## Ports

### Conserving

### **Bpb** — Position-based port on left side position-based mechanical translational

Position-based mechanical translational conserving port that represents a passage
point through the interface. Connect this port to a position-based mechanical
translational port of another block.

#### Dependencies

To enable this port, set the **Position-based port** parameter
to `Base`.

### **Fpb** — Position-based port on right side position-based mechanical translational

Position-based mechanical translational conserving port that represents a passage
point through the interface. Connect this port to a position-based mechanical
translational port of another block.

#### Dependencies

To enable this port, set the **Position-based port** parameter
to `Follower`.

### **F** — Non-position-based port on right side mechanical translational

Mechanical translational conserving port that represents a passage point through
the interface. Connect this port to a regular, non-position-based, mechanical
translational port of another block.

#### Dependencies

To enable this port, set the **Position-based port** parameter
to `Base`.

### **B** — Non-position-based port on left side mechanical translational

Mechanical translational conserving port that represents a passage point through
the interface. Connect this port to a regular, non-position-based, mechanical
translational port of another block.

#### Dependencies

To enable this port, set the **Position-based port** parameter
to `Follower`.

## Parameters

### **Position-based port** — Interface orientation `Base` (default) | `Follower`

Specify the block orientation:

- `Base` — Exposes the position-based port
  **Bpb**, located on the left side of the block icon in the
  default orientation, and the mechanical translational port **F** on
  the right side. The block positive direction is from port **Bpb**
  to port **F**.
- `Follower` — Exposes the position-based port
  **Fpb**, located on the right side of the block icon in the
  default orientation, and the mechanical translational port **B** on
  the left side. The block positive direction is from port **B** to
  port **Fpb**.

## Libraries

Simscape / Foundation Library / Translational / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Connect position-based and non-position-based mechanical translational ports

The Interface (PB-Translational) block represents a rigid
connection between a position-based and non-position-based mechanical translational network.
Port velocities are equal. Forces at the interface are equal and opposite.

The **Position-based port** parameter value determines the block
orientation. Align the block positive direction with the positive direction of the connected
position-based network.
