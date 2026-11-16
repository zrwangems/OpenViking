---
type: simulink-block
title: 'VR Signal Expander'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsignalexpander'
documentation_source_path: 'vrsignalexpander.html'
language: en
---

# VR Signal Expander

## Ports

Not documented in R2025b.

## Parameters

**Output width** — How long the output vector should
be.

**Output signal indices** — Vector indicating the position at
which the input signals appear at the output. The remaining positions are
filled with VR Placeholder signals.

For example, suppose you want an input vector with two signals and an output
vector with four signals, with the first input signal in position 2 and the
second input signal in position 4. In the **Output width**
box, enter `4` and in the **Output signal
indices** box, enter `[2,4]`. The first
and third output signals are unspecified.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2023b: To be removed

The `VR Signal Expander` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Expand input vectors into fully qualified virtual world field vectors

The VR Signal Expander block creates a vector of predefined length, using some
values from the input ports and filling the rest with placeholder signal
values.

To open the Block Parameters dialog box, double-click the block.
