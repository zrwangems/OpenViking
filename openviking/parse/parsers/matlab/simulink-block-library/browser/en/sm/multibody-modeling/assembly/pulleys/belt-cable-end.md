---
type: simulink-block
title: 'Belt-Cable End'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Pulleys'
documentation_page: 'beltcableend'
documentation_source_path: 'ref/beltcableend.html'
language: en
---

# Belt-Cable End

## Ports

### Frame

### **R** — Local reference frame frame

Reference frame by which to connect the tip of the cord to the
remainder of a multibody model.
### Belt-Cable

### **E** — Cord attachment point belt-cable

Point at which to terminate the cord of a pulley system.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Multibody / Belts and Cables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Tip of the cord of a pulley system

The Belt-Cable End block represents the tip of a cord by which to
anchor, drive, or load a pulley system. This tip serves as an interface between the
belt-cable domain specific to pulleys and the frame domain general to all multibody
components. A belt-cable port (**E**) identifies the cord whose tip
this block defines and its relative placement within a pulley system. A frame port
(**R**) identifies the local reference frame of the tip and its
placement in the broader multibody model.

The cord is inextensible. Its effective length can change only if a source of a cord
is provided—for example, in the form of a spool. If the second terminus of the cord is
another tip, the length of the cord is fixed, and so must be the distance around the
pulleys from one tip to the other. This distance is monitored during simulation, through
calculations based on the placement and geometry of the pulleys. The two measures—the
length and the distance—must always agree.

The cord is also always taut. From one of its tips to the nearest pulley, the cord
must form a straight line, one tangent to the circumference of the pulley and parallel
to its plane of rotation. The reference frame of the tip is placed on this line with its
*z*-axis directed along it and away from the pulley. Constraints
imposed on the tip by components outside of the pulley system must act without
interfering with this alignment.

Note that the frame and belt-cable ports belong to different physical domains. As a
rule, ports connect only to like ports—frame ports to other frame ports, belt-cable
ports to other belt-cable ports. The belt-cable domain imposes also the special
requirement that each network of belt-cable connection lines contain one (and no more
than one) Belt-Cable
Properties block. The necessary attributes of the pulley cord are
specified through this block.
