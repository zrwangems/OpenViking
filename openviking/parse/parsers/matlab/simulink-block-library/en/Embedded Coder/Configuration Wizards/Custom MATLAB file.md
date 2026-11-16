---
type: simulink-block
title: 'Custom MATLAB file'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Configuration Wizards'
documentation_page: 'custommatlabfile'
documentation_source_path: 'ref/custommatlabfile.html'
language: en
---

# Custom MATLAB file

## Ports

Not documented in R2025b.

## Parameters

### **Configure the model for** — Configuration objective `Custom` (default) | `ERT (optimized for fixed-point)` | `ERT (optimized for floating-point)` | `GRT (optimized for fixed/floating-point)` | `GRT (debug for fixed/floating-point)`

Objective for updating the active configuration parameters of a parent
model by using a predefined MATLAB script.

### **Configuration function** — Custom MATLAB script `rtwsampleconfig` (default)

Predefined or custom MATLAB script that updates the active configuration parameters of the
parent model.

#### Dependencies

This parameter is only used with this Configuration Wizards block. To
enable this parameter, set **Configure the model for**
to `Custom`.

### **Invoke build process after configuration** — Initiate build process `off` (default) | `on`

If selected, the predefined script initiates the code generation and build
process after updating the configuration parameters.

## Libraries

Embedded Coder / Configuration Wizards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Update active configuration parameters of parent model by using file containing custom MATLAB code

When you add a Custom MATLAB file block to your Simulink® model and double-click it, a custom MATLAB® script executes and configures model parameters that are relevant to code
generation. Set a block parameter to invoke the build process after configuring the
model.

After you double-click the block, open the Configuration Parameters dialog box to see
that the model parameter values have changed.

Use the example MATLAB script,
`matlabroot/toolbox/coder/simulinkcoder_core/rtwsampleconfig.m` with the Custom MATLAB file
block. Adapt the script to your model requirements. The block and the script provide a
starting point for customization. For more information, see Create a Custom Configuration Wizard Block.

**Note**

To provide a quick way to switch between configurations, you can include more than
one Configuration Wizard block in your model.
