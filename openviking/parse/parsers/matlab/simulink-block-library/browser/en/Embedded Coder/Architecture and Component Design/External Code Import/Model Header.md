---
type: simulink-block
title: 'Model Header'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / External Code Import'
documentation_page: 'modelheader'
documentation_source_path: 'ref/modelheader.html'
language: en
---

# Model Header

## Ports

Not documented in R2025b.

## Parameters

### **Top of Model Header** — Code to add near top of generated header file no default

Specify code that you want the code generator to add near the top of the header file
for the model. The code generator places the code in the section labeled `user
code (top of header file)`.

### **Bottom of Model Header** — Code to add at bottom of generated header file no default

Specify code that you want the code generator to add at the bottom of the header
file for the model. The code generator places the code in the section labeled
`user code (bottom of header file)`.

## Libraries

Simulink Coder / Custom Code

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

## Description

Specify external header code

For a model that includes the Model Header block, the code
generator adds external code that you specify to the header file
(`model.h`) that it generates. You can specify
code for the code generator to add near the top and bottom of the header file.

If you include this block in a referenced model, the code generator ignores the block for
simulation target builds, but processes the block for other system target files.

**Note**

This block is intended for inserting arbitrary custom code into the generated code in
specific locations. See the C Caller and
C Function
blocks, which are more typically used for integrating custom algorithmic code into a
model.
