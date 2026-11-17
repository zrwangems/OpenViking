---
type: simulink-block
title: 'System Terminate'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Custom Code'
documentation_page: 'systemterminate'
documentation_source_path: 'ref/systemterminate.html'
language: en
---

# System Terminate

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: System Terminate Function Declaration Code
  summary: Code to add to the declaration section of the generated function no default
  group: ''
- name: System Disable Terminate Execution Code
  summary: Code to add to the execution section of the generated function no default
  group: ''
- name: System Disable Terminate Exit Code
  summary: Code to add to the exit section of the generated function no default
  group: ''
```

### **System Terminate Function Declaration Code** — Code to add to the declaration section of the generated function no default

Specify code that you want the code generator to add to the declaration section of
the `SystemTerminate` function for the model or subsystem.

### **System Disable Terminate Execution Code** — Code to add to the execution section of the generated function no default

Specify code that you want the code generator to add to the execution section of the
`SystemTerminate` function for the model or subsystem.

### **System Disable Terminate Exit Code** — Code to add to the exit section of the generated function no default

Specify code that you want the code generator to add to the exit section of the
`SystemTerminate` function for the model or subsystem.
## Libraries

Simulink Coder / Custom Code

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

## Description

Specify external system termination code

For a model or nonvirtual subsystem that includes the System Terminate
block and a block that uses a `SystemTerminate` function, the code
generator adds external code, which you specify, to the `SystemTerminate`
function that it generates. You can specify code for the code generator to add to the
declaration, execution, and exit sections of the function code.

If you include this block in a referenced model, the code generator ignores the block for
simulation target builds, but processes the block for other system target files.

**Note**

This block is intended for inserting arbitrary custom code into the generated code in
specific locations. See the C Caller and
C Function
blocks, which are more typically used for integrating custom algorithmic code into a
model.
