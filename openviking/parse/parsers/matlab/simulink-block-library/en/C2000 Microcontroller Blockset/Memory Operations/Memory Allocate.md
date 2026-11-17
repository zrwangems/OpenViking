---
type: simulink-block
title: 'Memory Allocate'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Memory Operations'
documentation_page: 'memoryallocate'
documentation_source_path: 'ref/memoryallocate.html'
language: en
---

# Memory Allocate

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Variable name
  summary: Name for variable myVariable (default) | string | character vector
  group: Memory
- name: Specify variable alignment
  summary: Variable alignment flag off (default) | on
  group: Memory
- name: Memory alignment boundary
  summary: Memory alignment for variable 4 (default) | 1 | 2 | 8
  group: Memory
- name: Data type
  summary: Data type for variable uint32 (default) | double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64
    | boolean
  group: Memory
- name: Specify data type qualifier
  summary: Data type qualifier flag off (default) | on
  group: Memory
- name: Data type qualifier
  summary: Data type qualifier for variable volatile (default) | sting | character vectory
  group: Memory
- name: Data dimension
  summary: Number of elements of variable data type 64 (default) | positive integer
  group: Memory
- name: Initialize memory
  summary: Memory initialization flag off (default) | on
  group: Memory
- name: Initial value
  summary: Initial value for variable 0 (default) | scalar | vector | matrix
  group: Memory
- name: Specify memory section
  summary: Memory section flag off (default) | on
  group: Section
- name: Memory section
  summary: Memory section for variable mySEC1 (default) | string | character vector
  group: Section
- name: Bind memory section
  summary: Bind memory section to start address flag off (default) | on
  group: Section
- name: Section start address
  summary: Start address of memory section for variable hex2dec('8000') (default) | memory address in decimal or hexadecimal
    form
  group: Section
```

### Memory

Allocate memory for storing the variable. Specify the data type and size.

### **Variable name** — Name for variable myVariable (default) | string | character vector

Specify the name of the variable for which to allocate memory. The variable is
allocated in the generated code.

### **Specify variable alignment** — Variable alignment flag off (default) | on

Select this parameter, if required by your target processor, to direct the
compiler to align the new variable to a byte alignment boundary.

#### Parameter Dependencies

If you select this parameter, use parameter **Memory alignment
boundary** to set the byte alignment boundary.

### **Memory alignment boundary** — Memory alignment for variable 4 (default) | 1 | 2 | 8

Specify the alignment boundary for the variable data type in bytes. Alignment can
occur on 1-, 2-, 4-, or 8-byte boundaries. If the variable contains multiple values,
such as a vector or an array, the block aligns elements according to rules applied by
the compiler.

#### Parameter Dependencies

To enable this parameter, select **Specify variable
alignment**.

### **Data type** — Data type for variable uint32 (default) | double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | boolean

Specify the data type for the variable.

### **Specify data type qualifier** — Data type qualifier flag off (default) | on

Select this parameter to specify a data type qualifier to apply to the
variable.

#### Parameter Dependencies

If you select this parameter, use parameter **Data type
qualifier** to set the data type qualifier to apply to the
variable.

### **Data type qualifier** — Data type qualifier for variable volatile (default) | sting | character vectory

Specify the data type qualifier to apply to the variable in generated code as a
string or character vector. Common qualifiers are `volatile`,
`const`, `static`, and
`register`. The block does not check whether the value that you enter
is a valid qualifier.

### **Data dimension** — Number of elements of variable data type 64 (default) | positive integer

Specify the number of elements of the specified data type for the variable as a
positive integer.

### **Initialize memory** — Memory initialization flag off (default) | on

Select this parameter to specify an initial value for the variable.

#### Parameter Dependencies

If you select this parameter, use parameter **Initial value**
to set the initial value.

### **Initial value** — Initial value for variable 0 (default) | scalar | vector | matrix

Specify the initial value for the variable. At run time, the block sets the memory
location to this value.

#### Parameter Dependencies

To enable this parameter, select **Initialize memory**.

### Section

Specify the memory section in which to allocate the variable.

### **Specify memory section** — Memory section flag off (default) | on

Select this parameter to specify a memory section to use for allocating space in
memory for the variable.

#### Parameter Dependencies

If you select this parameter, use parameters **Memory
section**, **Bind memory section**, **Section
start address** to specify memory section details.

### **Memory section** — Memory section for variable mySEC1 (default) | string | character vector

Specify the name of the memory section to use for allocating memory for the
variable as a string or character vector. Specify a standard memory section or a
custom memory section that you declare elsewhere in your code.

Verify that the memory section has enough space to store the variable.

#### Parameter Dependencies

- To enable this parameter, select  **Specify memory
  section**.
- To bind the specified memory section to a specific start address in memory,
  select **Bind memory section** and specify the address by
  entering a value for **Section start address**.

### **Bind memory section** — Bind memory section to start address flag off (default) | on

Select this parameter to bind a newly created memory section for the variable to a
specific start address.

The new memory section specified for **Memory
section** is defined when you select this parameter.

#### Parameter Dependencies

- Select this parameter to enable parameter **Section start
  address**.
- Do not select this parameter if you are associating the variable with an
  existing memory section.

### **Section start address** — Start address of memory section for variable hex2dec('8000') (default) | memory address in decimal or hexadecimal form

Specify the start address to which to bind the memory section for the variable in
decimal form or in hexadecimal form with a conversion to decimal as shown by the
default value `hex2dec('8000')`. The block does not verify the
address. Verify that the address that you specify exists and that it can contain the
specified memory section.

#### Parameter Dependencies

- Enable this parameter by selecting parameter **Bind memory
  section**.
- Do not specify a value for this parameter if you are associating the
  variable with an existing memory section.
## Libraries

C2000 Microcontroller Blockset / Memory Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Allocate memory for new variable

The Memory Allocate block, on C2xxx processors, directs the TI compiler to allocate a
memory location for a new variable. Block parameters specify the variable name, the alignment
of the variable in memory, the data type of the variable, and other features that fully define
the memory required.

The block does not verify whether the parameter settings for the variable are valid, such
as checking the variable name, data type, or section. You must check that the parameters
settings are valid.

You do not connect the Memory Allocation block to other blocks in a model.
