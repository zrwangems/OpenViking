---
type: simulink-block
title: 'System Start'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Custom Code'
documentation_page: 'systemstart'
documentation_source_path: 'ref/systemstart.html'
language: zh-CN
chinese_source: worker-translation
---

# System Start

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: System Start Function Declaration Code
  summary: 要添加到所生成函数声明部分的代码 无默认值
  group: ''
- name: System Start Function Execution Code
  summary: 要添加到所生成函数执行部分的代码 无默认值
  group: ''
- name: System Start Function Exit Code
  summary: 要添加到所生成函数退出部分的代码 无默认值
  group: ''
```

### **System Start Function Declaration Code** — 要添加到所生成函数声明部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemStart` 函数声明部分的代码。

### **System Start Function Execution Code** — 要添加到所生成函数执行部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemStart` 函数执行部分的代码。

### **System Start Function Exit Code** — 要添加到所生成函数退出部分的代码 无默认值

指定希望代码生成器添加到模型或子系统的 `SystemStart` 函数退出部分的代码。
## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

## 描述

指定外部系统启动代码

对于包含 System Start 模块以及使用 `SystemStart` 函数的模块的模型或非虚拟子系统，代码生成器会将您指定的外部代码添加到其生成的 `SystemStart` 函数中。您可以指定希望代码生成器添加到函数代码的声明、执行和退出部分的代码。

如果将此模块包含在引用模型中，代码生成器会在仿真目标构建时忽略该模块，但会针对其他系统目标文件处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码中的特定位置。请参阅 C Caller 和 C Function 模块，它们更常用于将自定义算法代码集成到模型中。
