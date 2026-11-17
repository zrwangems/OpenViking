---
type: simulink-block
title: 'ERT (optimized for floating-point)'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Configuration Wizards'
documentation_page: 'ertoptimizedforfloatingpoint'
documentation_source_path: 'ref/ertoptimizedforfloatingpoint.html'
language: en
---

# ERT (optimized for floating-point)

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Configure the model for
  summary: Configuration objective ERT (optimized for floating-point) (default) | ERT (optimized for fixed-point) | GRT (optimized
    for fixed/floating-point) | GRT (debug for fixed/floating-point) | Custom
  group: ''
- name: Configuration function
  summary: Custom MATLAB script rtwsampleconfig (default)
  group: ''
- name: Invoke build process after configuration
  summary: Initiate build process off (default) | on
  group: ''
```

### **Configure the model for** — Configuration objective `ERT (optimized for floating-point)` (default) | `ERT (optimized for fixed-point)` | `GRT (optimized for fixed/floating-point)` | `GRT (debug for fixed/floating-point)` | `Custom`

Objective for updating the active configuration parameters of a parent
model by using a predefined MATLAB script.

### **Configuration function** — Custom MATLAB script `rtwsampleconfig` (default)

Predefined or custom MATLAB script that updates the active configuration parameters of the
parent model.

#### Dependencies

This parameter is only used with the Custom MATLAB file block. To
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

**Introduced in R2006b**

## Description

Update active configuration parameters of parent model for ERT floating-point code generation

When you add an ERT (optimized for floating-point) block to your Simulink® model and double-click it, a predefined MATLAB® script executes and optimally configures the model parameters for
floating-point code generation with the ERT target. Set a block parameter to invoke the
build process after configuring the model.

After you double-click the block, open the Configuration Parameters dialog box to see
that the model parameter values have changed.

**Note**

To provide a quick way to switch between configurations, you can include more than
one Configuration Wizard block in your model.
