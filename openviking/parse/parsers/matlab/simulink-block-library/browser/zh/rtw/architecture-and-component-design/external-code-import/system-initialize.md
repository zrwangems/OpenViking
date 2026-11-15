---
type: simulink-block
title: 'System Initialize'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / External Code Import'
documentation_page: 'systeminitialize'
documentation_source_path: 'ref/systeminitialize.html'
language: zh-CN
chinese_source: official
---

# System Initialize

## 端口

R2025b 官方文档未提供。

## 参数

### **系统初始化函数声明代码** — 要添加到生成函数的声明节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数的声明节的代码。

### **系统初始化函数执行代码** — 要添加到生成函数的执行节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数的执行节的代码。

### **系统初始化函数退出代码** — 添加到生成函数的退出节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数的退出节的代码。

## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 中推出**

## 描述

指定外部系统初始化代码

对于包含 System Initialize 模块和使用 `SystemInitialize` 函数的模块的模型或非虚拟子系统，代码生成器会将您指定的外部代码添加到它生成的 `SystemInitialize` 函数中。您可以为代码生成器指定要添加到函数代码的声明、执行和退出节的代码。如果模型还包含 Initialize Function，代码生成器会将为该模块生成的代码放在您在 System Initialize 模块中指定的代码后。

如果在引用模型中包含此模块，则代码生成器在编译仿真目标时将忽略该模块，但会在其他系统目标文件中处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码中的特定位置。请参阅 C Caller 和 C Function 模块，它们通常用于将自定义算法代码集成到模型中。
