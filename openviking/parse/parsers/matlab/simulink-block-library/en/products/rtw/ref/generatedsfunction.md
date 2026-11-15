---
type: simulink-block
title: 'Generated S-Function'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Code and Tool Customization / Code Generation for Custom Blocks'
documentation_page: 'generatedsfunction'
documentation_source_path: 'ref/generatedsfunction.html'
language: en
---

# Generated S-Function

## Ports

### Input

### **Input** — S-function input varies

See requirements.
### Output Arguments

### **Output** — S-function output varies

See requirements.

## Parameters

### **Generated S-function name (model\_sf)** — Name of S-function `model_sf` (default) | character vector

The name of the generated S-function. The code generator derives the name by
appending `_sf` to the name of the model or subsystem from which the
block is generated.

### **Show module list** — Select display module list off (default) | on

If selected, displays modules generated for the S-function.

## Libraries

Simulink Coder / S-Function Target

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011b**

## Description

Represent model or subsystem as generated S-function code

An instance of the Generated S-Function block represents code that the code
generator produces from its S-function system target file for a model or subsystem.

### Requirements

- The S-Function block must perform identically to the model or
  subsystem from which it was generated.
- Before creating the block, explicitly specify Inport block signal
  attributes, such as signal widths or sample times. The sole exception to this rule
  concerns sample times, as described in Sample Time Propagation in Generated S-Functions.
- Set the solver parameters of the Generated S-Function block to be the
  same as the parameters of the original model or subsystem. The generated S-function code
  operates identically to the original subsystem. For an exception to this rule, see Solver Type for Top Models with Generated S-Functions.
