---
type: simulink-block
title: 'Eddy Current'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'eddycurrent'
documentation_source_path: 'ref/eddycurrent.html'
language: en
---

# Eddy Current

## Ports

### Conserving

### **N** — North terminal magnetic

Magnetic conserving port associated with the north terminal of the
block.

### **S** — South terminal magnetic

Magnetic conserving port associated with the south terminal of the
block.

### **H** — Thermal port thermal

Thermal conserving port associated with the thermal port of the
block.

#### Dependencies

To enable this port, select the **Show thermal
port** parameter.

## Parameters

### **Conductance of eddy current loop** — Eddy current conductance `1` `1/Ohm` (default) | positive number

Conductance, *Geddy*, of the eddy current loop.
This component is the magnetic-domain analog of inductance in the electrical
domain.

### **Parasitic series reluctance** — Series reluctance `1e-3` `1/H` (default) | nonnegative number

Parasitic reluctance, R, of the eddy current loop.

### **Parasitic parallel permeance** — Parallel leakage permeance `1e-6` `H` (default) | nonnegative number

Parasitic permeance, P, of the parallel leakage path. To aid simulation
convergence in some circuit topologies, set this parameter to a small
value.

### **Show thermal port** — Thermal port visibility `Off` (default) | `On`

Whether to enable the thermal port of the block.

### **Thermal mass** — Thermal mass `0.1` `J/K` (default) | positive number

Thermal mass of the block. This parameter models the ability of the
Eddy Current block to absorb and store
thermal energy.

#### Dependencies

To enable this parameter, select the **Show thermal
port** parameter.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Eddy current loss representation

The Eddy Current block models the effect of eddy currents by
generating a magnetomotive force (MMF) that opposes changes in the magnetic flux. In
addition, the block models parasitic effects using a series reluctance and a parallel
leakage permeance, and thermal effects using an optional thermal port,
**H**.

Eddy currents in magnetic core materials are caused by time-varying magnetic fields.
These changing field densities induce voltage potentials within the material, causing
current to flow in closed loops. Such currents are usually undesired and cause heating
of the magnetic material.

Use this block to add eddy current losses in the magnetic domain to a custom
transformer or other magnetic component.

The eddy current component is sometimes referred to as magnetic inductance because it
is the magnetic-domain analog to an inductor in the electrical domain.

### Equations

This is the equivalent magnetic circuit for the block, including the eddy current
path (bottom) and parallel leakage path (top).

In the diagram:

- Φ is the total flux at the terminals. This flux is the
  summation of the eddy current loop and the parallel leakage path.
- Φ*L* is the flux
  through the eddy current loop.

The block calculates the terminal MMF, F, and flux, Φ, as:

F=GeddydΦLdt+RΦLΦ=FP+ΦL

where:

- *Geddy* is the conductance of
  the eddy current loop.
- R is the parasitic series reluctance of the eddy current
  path.
- P is the parallel permeance.

Because the parasitic series reluctance and parallel permeance are lossless, the
total dissipated power over the block is:

Pdiss=Geddy(dΦLdt)2

### Relating Transformer Electrical and Magnetic Models

In the electrical domain, eddy current losses are modeled using a parallel
resistance across the primary winding. This is the equivalent circuit for a nonideal
two-winding transformer.

In the diagram:

- *Lp* and
  *Ls* are the
  self-inductances of the primary and secondary windings,
  respectively.
- *Lm* is the mutual inductance
  between the two windings.
- *Rm* is the mutual resistance
  between the two windings, caused by the eddy current losses.

This two-winding transformer can similarly be represented in the magnetic domain.
This is the equivalent circuit.

In the diagram:

- R*p* and R*s* are the
  reluctances associated with the primary and secondary windings,
  respectively.
- R*g* is the
  reluctance associated with the magnetic coupling of the two
  windings.
- *n* is the turns ratio between the two
  windings.

The electrical- and magnetic-domain circuits are equivalent if:

Rg=n2Lm

Rp=n2Lp

Rs=1Ls

Geddy=n2Rm

You can use these relationships to calculate the equivalent
two-winding transformer properties for one domain from the other.
