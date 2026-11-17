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
language: zh-CN
chinese_source: worker-translation
---

# Memory Allocate

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Variable name
  summary: 变量名称 myVariable（默认）| string | 字符向量
  group: Memory
- name: Specify variable alignment
  summary: 变量对齐标志 off（默认）| on
  group: Memory
- name: Memory alignment boundary
  summary: 变量的内存对齐 4（默认）| 1 | 2 | 8
  group: Memory
- name: Data type
  summary: 变量的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | boolean
  group: Memory
- name: Specify data type qualifier
  summary: 数据类型限定符标志 off（默认）| on
  group: Memory
- name: Data type qualifier
  summary: 变量的数据类型限定符 volatile（默认）| sting | 字符向量
  group: Memory
- name: Data dimension
  summary: 变量数据类型的元素数 64（默认）| 正整数
  group: Memory
- name: Initialize memory
  summary: 内存初始化标志 off（默认）| on
  group: Memory
- name: Initial value
  summary: 变量的初始值 0（默认）| 标量 | 向量 | 矩阵
  group: Memory
- name: Specify memory section
  summary: 内存段标志 off（默认）| on
  group: Section
- name: Memory section
  summary: 变量的内存段 mySEC1（默认）| string | 字符向量
  group: Section
- name: Bind memory section
  summary: 将内存段绑定到起始地址标志 off（默认）| on
  group: Section
- name: Section start address
  summary: 变量的内存段起始地址 hex2dec('8000')（默认）| 十进制或十六进制形式的内存地址
  group: Section
```

### Memory

为存储变量分配内存。指定数据类型和大小。

### **Variable name** — 变量名称 myVariable（默认）| string | 字符向量

指定要为其分配内存的变量名称。该变量在生成的代码中分配。

### **Specify variable alignment** — 变量对齐标志 off（默认）| on

如果目标处理器需要，请选择此参数，以指示编译器将新变量对齐到字节对齐边界。

#### 参数依赖关系

如果选择此参数，请使用参数 **Memory alignment boundary** 设置字节对齐边界。

### **Memory alignment boundary** — 变量的内存对齐 4（默认）| 1 | 2 | 8

以字节为单位指定变量数据类型的对齐边界。对齐可以发生在 1、2、4 或 8 字节边界上。如果变量包含多个值，例如向量或数组，则该模块根据编译器应用的规则对齐元素。

#### 参数依赖关系

要启用此参数，请选择 **Specify variable alignment**。

### **Data type** — 变量的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | boolean

指定变量的数据类型。

### **Specify data type qualifier** — 数据类型限定符标志 off（默认）| on

选择此参数以指定要应用于变量的数据类型限定符。

#### 参数依赖关系

如果选择此参数，请使用参数 **Data type qualifier** 设置要应用于变量的数据类型限定符。

### **Data type qualifier** — 变量的数据类型限定符 volatile（默认）| sting | 字符向量

以字符串或字符向量形式指定要应用于生成代码中变量的数据类型限定符。常见的限定符有 `volatile`、`const`、`static` 和 `register`。该模块不检查您输入的值是否为有效的限定符。

### **Data dimension** — 变量数据类型的元素数 64（默认）| 正整数

以正整数形式指定变量指定数据类型的元素数。

### **Initialize memory** — 内存初始化标志 off（默认）| on

选择此参数以指定变量的初始值。

#### 参数依赖关系

如果选择此参数，请使用参数 **Initial value** 设置初始值。

### **Initial value** — 变量的初始值 0（默认）| 标量 | 向量 | 矩阵

指定变量的初始值。在运行时，该模块将内存位置设置为该值。

#### 参数依赖关系

要启用此参数，请选择 **Initialize memory**。

### Section

指定要在其中分配变量的内存段。

### **Specify memory section** — 内存段标志 off（默认）| on

选择此参数以指定用于为变量分配内存空间的内存段。

#### 参数依赖关系

如果选择此参数，请使用参数 **Memory section**、**Bind memory section**、**Section start address** 指定内存段详细信息。

### **Memory section** — 变量的内存段 mySEC1（默认）| string | 字符向量

以字符串或字符向量形式指定用于为变量分配内存的内存段名称。指定标准内存段或在代码其他位置声明的自定义内存段。

验证内存段是否有足够的空间存储变量。

#### 参数依赖关系

- 要启用此参数，请选择 **Specify memory section**。
- 要将指定的内存段绑定到内存中的特定起始地址，请选择 **Bind memory section** 并通过为 **Section start address** 输入值来指定地址。

### **Bind memory section** — 将内存段绑定到起始地址标志 off（默认）| on

选择此参数以将变量新建的内存段绑定到特定起始地址。

为 **Memory section** 指定的新内存段在您选择此参数时定义。

#### 参数依赖关系

- 选择此参数以启用参数 **Section start address**。
- 如果要将变量与现有内存段关联，请不要选择此参数。

### **Section start address** — 变量的内存段起始地址 hex2dec('8000')（默认）| 十进制或十六进制形式的内存地址

以十进制形式或十六进制形式（并转换为十进制，如默认值 `hex2dec('8000')` 所示）指定要将变量的内存段绑定到的起始地址。该模块不验证地址。请验证您指定的地址存在且可以包含指定的内存段。

#### 参数依赖关系

- 通过选择参数 **Bind memory section** 启用此参数。
- 如果要将变量与现有内存段关联，请不要为此参数指定值。
## 所属库

C2000 Microcontroller Blockset / Memory Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

为新变量分配内存

Memory Allocate 模块在 C2xxx 处理器上指示 TI 编译器为新变量分配内存位置。模块参数指定变量名称、变量在内存中的对齐方式、变量的数据类型以及其他完整定义所需内存的特性。

该模块不验证变量的参数设置是否有效，例如检查变量名称、数据类型或段。您必须检查参数设置是否有效。

您不需要将 Memory Allocation 模块连接到模型中的其他模块。
