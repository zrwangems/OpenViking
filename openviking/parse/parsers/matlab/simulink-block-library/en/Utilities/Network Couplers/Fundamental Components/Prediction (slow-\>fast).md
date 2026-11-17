---
type: simulink-block
title: 'Prediction (slow->fast)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers / Fundamental Components'
documentation_page: 'predictionslowfast'
documentation_source_path: '../simscape/ref/predictionslowfast.html'
language: en
---

# Prediction (slow->fast)

## Ports
```yaml
ports:
- name: u
  summary: Signal with slower sampling real scalar
  direction: input
- name: y
  summary: Prediction for the faster network real scalar
  direction: output
```

### Input

### **u** — Signal with slower sampling real scalar

Connect this port to the slower network, Network 2, to capture its output.
### Output

### **y** — Prediction for the faster network real scalar

Connect this port to the input of the faster network, Network 1.
## Parameters
```yaml
parameters:
- name: Port u discrete sample time (s)
  summary: Specify sample time for the slower network -1 (default) | positive scalar
  group: ''
- name: Port y discrete sample time (s)
  summary: Specify sample time for the faster network -1 (default) | positive scalar
  group: ''
```

### **Port u discrete sample time (s)** — Specify sample time for the slower network `-1` (default) | positive scalar

Specify sample time for the slower network, Network 2, in seconds.

### **Port y discrete sample time (s)** — Specify sample time for the faster network `-1` (default) | positive scalar

Specify sample time for the faster network, Network 1, in seconds.
## Libraries

Simscape / Utilities / Network Couplers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024a: Support arrays of electrical nodes

To support arrays of electrical nodes and three-phase connections, the trigger logic has
been updated. Previously, just a change in the first element of input *u*
triggered a prediction cycle. Now, a change in any of the inputs triggers a prediction
cycle. As a result, the two selector (U->Y) blocks added in R2023b have been
removed.

For battery models with arrays of thermal nodes, the simulation results are the same as
in previous releases. However, for models where the elements of the array of nodes are not
physically coupled, this change can lead to a change in the trigger logic and therefore to a
slight difference in simulation results.

### R2023b: Support arrays of thermal nodes

To support arrays of thermal nodes, needed for the Network Coupler
(Thermal Mass) block, two selector (U->Y) blocks have been
added to the Prediction (slow->fast) block diagram, to keep the triggering
signal scalar.

This change has no compatibility impact. If you open an existing model, the simulation
results are the same as in previous releases.

## Description

Prevent accuracy loss when connecting fixed-step networks with different step sizes

**Note**

Prediction and smoothing algorithms are built into the Network Coupler blocks, and you
can enable them by using the check boxes in the block dialogs. The prediction and smoothing
blocks in the Fundamental Components sublibrary are provided for your reference only.

Connecting a network with faster sampling (Network 1) to a network with slower sampling
(Network 2) may result in accuracy loss in the Network 1 simulation when its sample times are
between the sample times of Network 2. The Prediction (slow->fast) block helps
prevent the accuracy loss. It predicts the output of Network 2 between its sample times by
using the last computed derivative of the output of Network 2. The block implementation is a
masked subsystem.

Prediction (slow->fast) subsystem diagram

The subsystem contains blocks that run at both the slower and the faster rate. The
Delay block is driven by the slower rate, and changes in its output are used
as a trigger, so that the triggered subsystem captures the latest derivative of input
*u*. The discrete-time integrator runs at the faster rate and uses this
derivative to predict the output *y* until the next trigger event happens.
