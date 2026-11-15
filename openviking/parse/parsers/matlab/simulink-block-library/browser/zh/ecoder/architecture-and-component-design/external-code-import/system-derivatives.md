---
type: simulink-block
title: 'System Derivatives'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / External Code Import'
documentation_page: 'systemderivatives'
documentation_source_path: 'ref/systemderivatives.html'
language: zh-CN
chinese_source: official
---

# System Derivatives

## 端口

R2025b 官方文档未提供。

## 参数

### **系统导数函数声明代码** — 要添加到生成函数的声明节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemDerivatives` 函数的声明节的代码。

### **系统导数函数执行代码** — 要添加到生成函数的执行节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemDerivatives` 函数的执行节的代码。

### **系统导数函数退出代码** — 添加到生成函数的退出节的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemDerivatives` 函数的退出节的代码。

## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 中推出**

## 描述

指定外部系统导数代码

对于包含 System Derivatives 模块和计算连续状态的模块的模型或非虚拟子系统，代码生成器会将您指定的外部代码添加到它生成的 `SystemDerivatives` 函数中。您可以为代码生成器指定要添加到函数代码的声明、执行和退出节的代码。

如果在引用模型中包含此模块，则代码生成器在编译仿真目标时将忽略该模块，但会在其他系统目标文件中处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码中的特定位置。请参阅 C Caller 和 C Function 模块，它们通常用于将自定义算法代码集成到模型中。
