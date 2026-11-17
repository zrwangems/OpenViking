---
type: simulink-block
title: 'Check Singular Value Characteristics'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checksingularvaluecharacteristics'
documentation_source_path: 'ug/checksingularvaluecharacteristics.html'
language: en
---

# Check Singular Value Characteristics

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

The following table summarizes the Singular Value Plot block
parameters, accessible via the block parameter dialog box. For more information, see
Parameters in the Singular Value Plot block reference
page.

| Task | | Parameters |
| --- | --- | --- |
| Configure linearization. | Specify inputs and outputs (I/Os). | In **Linearizations** tab:  - **Linearization inputs/outputs** - **Click a model signal to add it as a   linearization I/O** |
| Specify settings. | In **Linearizations** tab:  - **Linearize on** - **Snapshot times** - **Trigger type** |
| Specify algorithm options. | In **Linearizations** tab:  - **Enable zero-crossing detection** - **Use exact delays** - **Linear system sample time** - **Sample time rate conversion   method** - **Prewarp frequency (rad/s)** |
| Specify labels for linear system I/Os and state names. | In **Linearizations** tab:  - **Use full block names** - **Use bus signal names** |
| Specify bounds on the linear system for assertion. | | In **Bounds** tab:  - **Include upper singular value bound in   assertion** - **Include lower singular value bound in   assertion** |
| Specify assertion options (only when you specify bounds on the linear system). | | In **Assertion** tab:  - **Enable assertion** - **Simulation callback when assertion fails   (optional)** - **Stop simulation when assertion   fails** - **Output assertion signal** |
| Save linear system to MATLAB workspace. | | **Save data to workspace** in **Logging** tab. |
| View bounds violations graphically in a plot window. | | **Show Plot** |
| Display plot window instead of block parameters dialog box on double-clicking the block. | | **Show plot on block open** |
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

## Description

Check that singular value bounds are satisfied during simulation

This block is the same as the Singular Value Plot block except for
default parameter settings in the **Bounds** tab:

Check that upper and lower bounds on singular values of a linear
system, computed from a nonlinear Simulink model, are satisfied
during simulation.

The Simulink model can be continuous-time, discrete-time or multirate and can have time delays.
The computed linear system can be single-input single-output (SISO) or multi-input multi-output
(MIMO).

During simulation, the software linearizes the portion of the
model between specified linearization input and output, computes the
singular values, and checks that the values satisfy the specified
bounds:

- If all bounds are satisfied, the block does nothing.
- If a bound is not satisfied, the block asserts and a warning message appears in the
  MATLAB® Command Window. You can also specify that the block:

  - Evaluate a MATLAB expression.
  - Stop the simulation and bring that block into focus.

During simulation, the block can also output a logical assertion signal.

- If all bounds are satisfied, the signal is true (`1`).
- If any bound is not satisfied, the signal is false (`0`).

For MIMO systems, the bounds apply to the singular values computed
for all input/output combinations.

You can add multiple Check Singular Value Characteristics blocks
in your model to check upper and lower singular value bounds on various
portions of the model.

You can also plot the singular values on a singular value plot
and graphically verify that the values satisfy the bounds.

This block and the other Model Verification blocks test that
the linearized behavior of a nonlinear Simulink model is within
specified bounds during simulation.

- When a model does not violate any bound, you can disable
  the block by clearing the assertion option. If you modify the model,
  you can re-enable assertion to ensure that your changes do not cause
  the model to violate a bound.
- When a model violates any bound, you can use Simulink
  Design Optimization™ software
  to optimize the linear system to meet the specified requirements in
  this block.

You can save the linear system as a variable in the MATLAB workspace.

The block does not support code generation and can be used only
in `Normal` simulation mode.
