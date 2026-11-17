---
type: simulink-block
title: 'Prediction (discrete->continuous)'
family: 'network-couplers'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Fundamental Components'
documentation_page: 'predictiondiscretecontinuous'
documentation_source_path: '../simscape/ref/predictiondiscretecontinuous.html'
language: en
---

# Prediction (discrete->continuous)

## Ports
```yaml
ports:
- name: u
  summary: Signal with fixed-step sampling real scalar
  direction: input
- name: y
  summary: Prediction for the variable-step network real scalar
  direction: output
```

### Input

### **u** — Signal with fixed-step sampling real scalar

Connect this port to the fixed-step network, Network 2, to capture its output.
### Output

### **y** — Prediction for the variable-step network real scalar

Connect this port to the input of the variable-step network, Network 1.
## Parameters
```yaml
parameters:
- name: Port u discrete sample time (s)
  summary: Specify sample time for the fixed-step network -1 (default) | positive scalar
  group: ''
```

### **Port u discrete sample time (s)** — Specify sample time for the fixed-step network `-1` (default) | positive scalar

Specify sample time for the fixed-step network, Network 2, in seconds.
## Libraries

Simscape / Utilities / Network Couplers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Prevent accuracy loss when connecting fixed-step network to variable-step network

**Note**

Prediction and smoothing algorithms are built into the Network Coupler blocks, and you
can enable them by using the check boxes in the block dialogs. The prediction and smoothing
blocks in the Fundamental Components sublibrary are provided for your reference only.

Connecting a variable-step network (Network 1) to a fixed-step network (Network 2) may
result in accuracy loss in the Network 1 simulation when its sample times are between the
sample times of Network 2. The Prediction (discrete->continuous) block helps
prevent the accuracy loss. It predicts the output of Network 2 between its sample times by
using the last computed derivative of the output of Network 2 and provides the inter-sample
prediction to Network 1. The block implementation is a masked subsystem.

Prediction (discrete->continuous) subsystem diagram
