---
type: simulink-block
title: 'System Initialize'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Custom Code'
documentation_page: 'systeminitialize'
documentation_source_path: 'ref/systeminitialize.html'
language: zh-CN
chinese_source: worker-translation
---

# System Initialize

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: System Initialize Function Declaration Code
  summary: 要添加到所生成函数声明部分的代码 无默认值
  group: ''
- name: System Initialize Function Execution Code
  summary: 要添加到所生成函数执行部分的代码 无默认值
  group: ''
- name: System Initialize Function Exit Code
  summary: 要添加到所生成函数退出部分的代码 无默认值
  group: ''
```

### **System Initialize Function Declaration Code** — 要添加到所生成函数声明部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数声明部分的代码。

### **System Initialize Function Execution Code** — 要添加到所生成函数执行部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数执行部分的代码。

### **System Initialize Function Exit Code** — 要添加到所生成函数退出部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemInitialize` 函数退出部分的代码。
## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

## 描述

指定外部系统初始化代码

对于包含 System Initialize 模块以及使用 `SystemInitialize` 函数的模块的模型或非虚拟子系统，代码生成器会将您指定的外部代码添加到其生成的 `SystemInitialize` 函数中。您可以指定要由代码生成器添加到函数代码的声明、执行和退出部分的代码。如果模型中还包含 Initialize Function，则代码生成器会将针对该模块生成的代码放置在您在 System Initialize 模块中指定的代码之后。

如果将此模块包含在引用模型中，代码生成器会针对仿真目标构建忽略该模块，但会针对其他系统目标文件处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码中的特定位置。请参阅 C Caller 和 C Function 模块，它们更常用于将自定义算法代码集成到模型中。
