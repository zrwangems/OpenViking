---
type: simulink-block
title: 'Neural State-Space Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Models'
documentation_page: 'neuralstatespacemodel'
documentation_source_path: 'ref/neuralstatespacemodel.html'
language: en
---

# Neural State-Space Model

## Ports

### Input

### **u** — Input of the neural state-space model scalar | vector

Input of the neural state-space model, specified as a vector signal with as many
elements as the number of inputs you specify when creating the corresponding
`idNeuralStateSpace` object. If the
`idNeuralStateSpace` object specified in the block dialog box does
not have inputs, this port does not appear.

### **x0** — Initial state of the neural state-space model scalar | vector

Initial state of the neural state-space model, specified as a vector signal with
as many elements as the number of states you specify when creating the corresponding
`idNeuralStateSpace` object.

#### Dependencies

To enable this input port, select the **initial state source**
parameter as `External`. Then, connect the port to an
upstream signal supplying the value of the initial state.
### Output

### **y** — Output of the neural state-space model scalar | vector

Output of the neural state-space model, returned as a vector signal with as many
elements as the number of outputs you specify when creating the corresponding
`idNeuralStateSpace` object.

### **x** — State of the neural state-space model scalar | vector

State of the neural state-space model, output as a vector signal with as many
elements as the number of states *nx* that you
specify when creating the corresponding `idNeuralStateSpace` object.
These values are identical to the first *nx*
values in the `y` output.

#### Dependencies

To enable this output port, select the **Output state**
parameter.

### **dx** — State derivative/difference of the neural state-space model scalar | vector

State derivative or state difference of the neural state-space model, output as a
vector signal with as many elements as the number of states you specify when creating
the corresponding `idNeuralStateSpace` object.

For continuous-time neural state space models, this value is the derivative of the
state with respect to time. For discrete-time neural state space models, this value is
the difference between the next state and the current one.

#### Dependencies

To enable this output port, select the **Output state
derivative/difference** parameter.

### **z** — Latent state of the neural state-space model scalar | vector

Internal (latent) state of the neural state-space model, output as a vector signal
with as many elements as the value of the LatentDim
property that you specify when creating the corresponding
`idNeuralStateSpace` object.

#### Dependencies

To enable this output port, specify the value of the
`LatentDim` property of the `idNeuralStateSpace`
object as a finite positive scalar and select the **Output state**
parameter.

### **dz** — Latent state derivative/difference of the neural state-space model scalar | vector

Internal (latent) state derivative or latent state difference of the neural
state-space model, output as a vector signal with as many elements as the value of the
LatentDim
property that you specify when creating the corresponding
`idNeuralStateSpace` object.

For continuous-time neural state space models, this value is the derivative of the
latent state with respect to time. For discrete-time neural state space models, this
value is the difference between the next latent state and the current one.

#### Dependencies

To enable this output port, specify the value of the
`LatentDim` property of the `idNeuralStateSpace`
object as a finite positive scalar and select the **Output state
derivative/difference** parameter.

## Parameters

### **Model** — Neural state space object `idNeuralStateSpace(1,'NumInputs',1,'NumOutputs',2)` (default) | `idNeuralStateSpace` object

Specify an `idNeuralStateSpace` object that defines a neural state-space system by
entering the name of an `idNeuralStateSpace` object from the
MATLAB® workspace.

Currently, the Neural State-Space Model block does not support
`idNeuralStateSpace` objects whose neural network layer activation
functions are `elu`, `swish`,
`softplus`, or `scaling`.

**Note**

If you change the input/output configuration of `Model` in the
workspace, click the **...** button next to the
**Model** edit field in the block dialog box to refresh the
Neural State-Space Model block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sys` |
| **Type:** string, character vector |
| **Default:** `"idNeuralStateSpace(1,'NumInputs',1,'NumOutputs',2)"` |

### **Initial state source** — Initial state source `internal` (default) | `external`

Specify whether to enter the initial condition directly on the dialog box or to
receive the initial condition from an input port.

- If you set **Initial state source** to
  `internal`, enter the initial condition in the edit field
  under **Initial state**.
- If you set **Initial state source** to
  `external`, the input port `x0` is added
  to the block. You must then connect an upstream signal supplying the value of the
  initial state to the `x0` input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `x0type` |
| **Type**: character vector |
| **Values**: `'internal'` | `'external'` |
| **Default**: `'internal'` |

### **Initial state** — Initial state `0` (default) | scalar | vector

Specify the initial state of the neural state-space object as a vector of
*nx* entries, where
*nx* is the number of states in
`Model`.

Use this parameter make sure that the system states reflect the true plant
environment at the start of your simulation, to the best of your knowledge.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ic` |
| **Type:** string, character vector |
| **Default:** `"0"` |

### **Output state** — Add external output state port `off` (default) | `on`

Select this parameter to add the **x** output port to the block.
During simulation this port outputs the internal state of the `idNeuralStateSpace` object specified in `Model`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `returnx` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

### **Output state derivative/difference** — Add external output state derivative port `off` (default) | `on`

Select this parameter to add the **dx** output port to the block.
During simulation this port outputs the time derivative of the internal state of the
`idNeuralStateSpace` object specified in **Model**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `returndx` |
| **Type:** string, character vector |
| **Values:** `"off"`, `"on"` |
| **Default:** `"off"` |

## Libraries

System Identification Toolbox / Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024b: Code generation does not create temporary `.m` files

Starting in 2024b, temporary `.m` files will no longer be created in
the current folder when updating the Neural State-Space Model Block for
prediction and code generation.

However, if the structure of the `dlnetwork` object assigned to the state
or output networks of the neural state-space object is not a multi-layer perceptron (MLP)
network, then the implementation of the Neural State-Space Model Block uses
the Predict (Deep Learning Toolbox) Block and
`.mat` files will still be generated in the current folder. In all other
cases, `.mat` files will also not be created.

## Description

Simulate neural state-space model in Simulink

Simulates neural state-space (`idNeuralStateSpace`) models.
