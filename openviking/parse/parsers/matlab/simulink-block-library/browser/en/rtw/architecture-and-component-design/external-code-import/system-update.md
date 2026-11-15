---
type: simulink-block
title: 'System Update'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / External Code Import'
documentation_page: 'systemupdate'
documentation_source_path: 'ref/systemupdate.html'
language: en
---

# System Update

## Ports

Not documented in R2025b.

## Parameters

### **System Update Function Declaration Code** — Code to add to the declaration section of the generated function no default

Specify code that you want the code generator to add to the declaration section of
the `SystemUpdate` function for the model or subsystem.

### **System Update Function Execution Code** — Code to add to the execution section of the generated function no default

Specify code that you want the code generator to add to the execution section of the
`SystemUpdate` function for the model or subsystem.

### **System Update Function Exit Code** — Code to add to the exit section of the generated function no default

Specify code that you want the code generator to add to the exit section of the
`SystemUpdate` function for the model or subsystem.

## Libraries

Simulink Coder / Custom Code

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

## Description

Specify external system update code

For a model or nonvirtual subsystem that includes the System Update block
and a block that uses a `SystemUpdate` function, the code generator adds
external code, which you specify, to the `SystemUpdate` function that it
generates. You can specify code for the code generator to add to the declaration, execution,
and exit sections of the function code.

If you include this block in a referenced model, the code generator ignores the block for
simulation target builds, but processes the block for other system target files.

**Note**

This block is intended for inserting arbitrary custom code into the generated code in
specific locations. See the C Caller and
C Function
blocks, which are more typically used for integrating custom algorithmic code into a
model.
