---
type: simulink-block
title: 'Model Source'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Custom Code'
documentation_page: 'modelsource'
documentation_source_path: 'ref/modelsource.html'
language: en
---

# Model Source

## Ports

Not documented in R2025b.

## Parameters

### **Top of Model Source** — Code to add near top of generated source file no default

Specify code that you want the code generator to add near the top of the source file
for the model. The code generator places the code in the section labeled `user
code (top of source file)`.

### **Bottom of Model Source** — Code to add at bottom of generated source file no default

Specify code that you want the code generator to add at the bottom of the source
file for the model. The code generator places the code in the section labeled
`user code (bottom of source file)`.

## Libraries

Simulink Coder / Custom Code

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

## Description

Specify external source code

For a model that includes the Model Source block, the code generator adds
external code that you specify to the source file
(`model.c` or
`model.cpp`) that it generates. You can
specify code for the code generator to add near the top and bottom of the source file.

If you include this block in a referenced model, the code generator ignores the block for
simulation target builds, but processes the block for other system target files.

**Note**

This block is intended for inserting arbitrary custom code into the generated code in
specific locations. See the C Caller and
C Function
blocks, which are more typically used for integrating custom algorithmic code into a
model.
