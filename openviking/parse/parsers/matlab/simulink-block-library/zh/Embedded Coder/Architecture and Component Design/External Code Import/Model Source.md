---
type: simulink-block
title: 'Model Source'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / External Code Import'
documentation_page: 'modelsource'
documentation_source_path: 'ref/modelsource.html'
language: zh-CN
chinese_source: official
---

# Model Source

## 端口

R2025b 官方文档未提供。

## 参数

### **模型源顶部** — 要添加到生成的源文件顶部附近的代码 无默认值

指定需要代码生成器添加到模型源文件顶部附近的代码。代码生成器将代码放在标注为 `user code (top of source file)` 的节中。

### **模型源底部** — 要添加到生成的源文件底部的代码 无默认值

指定需要代码生成器添加到模型源文件底部的代码。代码生成器将代码放在标注为 `user code (bottom of source file)` 的节中。

## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 中推出**

## 描述

指定外部源代码

对于包含 Model Source 模块的模型，代码生成器会将您指定的外部代码添加到它生成的源文件（`model.c` 或 `model.cpp`）中。您可以指定代码生成器要添加到源文件顶部和底部附近的代码。

如果在引用模型中包含此模块，则代码生成器在编译仿真目标时将忽略该模块，但会在其他系统目标文件中处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码中的特定位置。请参阅 C Caller 和 C Function 模块，它们通常用于将自定义算法代码集成到模型中。
