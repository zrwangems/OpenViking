---
type: simulink-block
title: 'Smoothing (fast->slow)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers / Fundamental Components'
documentation_page: 'smoothingfastslow'
documentation_source_path: '../simscape/ref/smoothingfastslow.html'
language: en
---

# Smoothing (fast->slow)

## Ports

### Input

### **u** — Signal with faster sampling real scalar

Connect this port to the faster network, Network 1, to capture its output.
### Output

### **y** — Smoothed signal for the slower network real scalar

Connect this port to the input of the slower network, Network 2.

## Parameters

### **Number of samples over which to smooth** — Specify number of samples for averaging the output `1` (default) | positive scalar

Specify the number of samples for averaging the output of the faster network,
Network 1.

### **Port u discrete sample time (s)** — Specify sample time for the faster network `-1` (default) | positive scalar

Specify sample time for the faster network, Network 1, in seconds.

### **Initial output** — Specify initial output value `0` (default) | scalar

Specify initial output value for the faster network, Network 1.

## Libraries

Simscape / Utilities / Network Couplers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2023b: Support arrays of thermal nodes

To support arrays of thermal nodes, needed for the Network Coupler
(Thermal Mass) block, the For Each subsystem layer has been added to the
Smoothing (fast->slow) block diagram.

This change has no compatibility impact. If you open an existing model, the simulation
results are the same as in previous releases.

## Description

Apply output smoothing when connecting fixed-step networks with different step sizes

**Note**

Prediction and smoothing algorithms are built into the Network Coupler blocks, and you
can enable them by using the check boxes in the block dialogs. The prediction and smoothing
blocks in the Fundamental Components sublibrary are provided for your reference only.

When network with faster sampling (Network 1) has high-frequency activity above what the
slower network (Network 2) can sample, applying smoothing to the output of Network 1 can
sometimes be advantageous because it helps you avoid picking a local peak or trough of the
Network 1 activity. The Smoothing (fast->slow) block provides an averaged value
of the Network 1 output to Network 2. The block implementation is a masked subsystem shown in
the first block diagram. The second diagram shows the contents of the For Each subsystem in
the first diagram.

Smoothing (fast->slow) subsystem diagram

For Each subsystem diagram

The smoothing works by averaging the last *N* samples. You specify
*N* by using the **Number of samples over which to
smooth** parameter.
