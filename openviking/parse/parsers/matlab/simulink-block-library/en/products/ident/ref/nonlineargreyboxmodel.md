---
type: simulink-block
title: 'Nonlinear Grey-Box Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Model Analysis / Simulation and Prediction'
documentation_page: 'nonlineargreyboxmodel'
documentation_source_path: 'ref/nonlineargreyboxmodel.html'
language: en
---

# Nonlinear Grey-Box Model

## Ports

Not documented in R2025b.

## Parameters

**IDNLGREY model**
:   Name of `idnlgrey` variable in the MATLAB® workspace.

**Initial state**
:   Specify the initial states as one of the following:

    - `'z'`: Specifies zero, which corresponds
      to a system starting from rest.
    - `'m'`: Specifies the internal initial
      states of the model.
    - Vector of size equal to the number of states in the `idnlgrey` object.
    - An initial state structure array. For information
      about creating this structure, type `help idnlgrey/sim` in
      the MATLAB Command Window.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008a**

## Description

Simulate nonlinear grey-box model in Simulink software

Simulates systems of nonlinear grey-box (`idnlgrey`)
models.

### Input

Input signal to the model.

### Output

Output signal from the model.
