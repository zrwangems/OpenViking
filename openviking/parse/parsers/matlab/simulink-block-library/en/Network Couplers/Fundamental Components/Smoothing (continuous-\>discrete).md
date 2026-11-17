---
type: simulink-block
title: 'Smoothing (continuous->discrete)'
family: 'utilities'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Network Couplers / Fundamental Components'
documentation_page: 'smoothingcontinuousdiscrete'
documentation_source_path: '../simscape/ref/smoothingcontinuousdiscrete.html'
language: en
---

# Smoothing (continuous->discrete)

## Ports

### Input

### **u** — Signal with high-frequency activity real scalar

Connect this port to the variable-step network, Network 1, to capture its output.
### Output

### **y** — Smoothed signal for the fixed-step network real scalar

Connect this port to the input of the fixed-step network, Network 2.

## Parameters

### **Smoothing time constant (s)** — Specify time constant for the first-order filter `0.001` (default) | positive scalar

Specify the time constant for the first-order filter, in seconds. Typically, the
smoothing time constant is at least 10 times larger than the step size of the fixed-step
network, Network 2.

### **Initial output** — Specify initial output value `0` (default) | scalar

Specify initial output value for the variable-step network, Network 1.

## Libraries

Simscape / Utilities / Network Couplers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Apply output smoothing when connecting variable-step network to fixed-step network

**Note**

Prediction and smoothing algorithms are built into the Network Coupler blocks, and you
can enable them by using the check boxes in the block dialogs. The prediction and smoothing
blocks in the Fundamental Components sublibrary are provided for your reference only.

When variable-step network (Network 1) has high-frequency activity above what the
fixed-step network (Network 2) can sample, applying smoothing to the output of Network 1 can
sometimes be advantageous because it helps you avoid picking a local peak or trough of the
Network 1 activity. The Smoothing (continuous->discrete) block uses a
first-order filter to remove unwanted high-frequency information from the Network 1 output
before providing the value to Network 2. The block implementation is a masked
subsystem.

Smoothing (continuous->discrete) subsystem diagram
