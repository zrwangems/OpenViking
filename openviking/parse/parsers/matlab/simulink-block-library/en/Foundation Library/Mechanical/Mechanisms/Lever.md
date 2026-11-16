---
type: simulink-block
title: 'Lever'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanisms'
documentation_page: 'lever'
documentation_source_path: 'ref/lever.html'
language: en
---

# Lever

## Ports

### Conserving

### **A** — Node A of the lever mechanical translational

Mechanical translational conserving port associated with the node A of
the lever.

### **B** — Node B of the lever mechanical translational

Mechanical translational conserving port associated with the node B of
the lever.

### **C** — Node C of the lever mechanical translational

Mechanical translational conserving port associated with the node C of
the lever.

## Parameters

### **AC arm length** — Arm length between nodes A and C `0.1 m` (default)

Arm length between nodes A and C.

### **BC arm length** — Arm length between nodes B and C `0.1 m` (default)

Arm length between nodes B and C.

## Libraries

Simscape / Foundation Library / Mechanical / Mechanisms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Generic mechanical lever

The Lever block represents a mechanical lever in its
generic form, known as a free or summing lever, shown in the following schematic.

The summing lever equations are derived with the assumption of small angle deviation
from initial position:

vC=KAC·vA+KBC·vB

FA=KAC·FC

FB=KBC·FC

KAC=lBClAC+lBC

KBC=lAClAC+lBC

where

- *v*A,
  *v*B,
  *v*C are level joint
  velocities.
- *F*A,
  *F*B,
  *F*C are level joint forces.
- *l*AC,
  *l*BC are arm lengths.

The above equations are derived with the assumption that the lever sums forces and
motions at node C. The assumption is arbitrary and does not impose any limitations on
how the forces or motions are applied to the lever. In other words, any of the lever
nodes can be “input” or “output” nodes, depending on the
value of the force. Moreover, any of the block nodes can be connected to the reference
point, thus converting a three-node lever into a first-class lever, with the fulcrum in
the middle, or a second-class lever, with the fulcrum at the end.

The following illustration shows a schematic of a first-class lever, with the fulcrum
in the middle.

It is described with the following equations:

vA=−lAClBC·vB

FB=−lAClBC·FA

The next illustration shows a schematic of a second-class lever, with the fulcrum at
node A.

It is described with the following equations:

vC=KBC·vB

FB=KBC·FC

The Linkage Mechanism example illustrates the use
of the Lever block in three different modes. Linkages L\_1
and L\_4 simulate first-class levers with the fulcrum at the end. Linkage L\_2 represents
a summing lever. Linkage L\_3 simulates a second-class lever with the fulcrum in the
middle.

As far as the block directionality is concerned, the joints' absolute displacements
are positive if they are in line with the globally assigned positive direction.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
