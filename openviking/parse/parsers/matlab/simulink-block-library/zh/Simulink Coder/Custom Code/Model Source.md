---
type: simulink-block
title: 'Model Source'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Custom Code'
documentation_page: 'modelsource'
documentation_source_path: 'ref/modelsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Model Source

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Top of Model Source
  summary: 在生成的源文件顶部附近添加的代码 无默认值
  group: ''
- name: Bottom of Model Source
  summary: 在生成的源文件底部添加的代码 无默认值
  group: ''
```

### **Top of Model Source** — 在生成的源文件顶部附近添加的代码 无默认值

指定希望代码生成器添加到模型源文件顶部附近的代码。代码生成器将该代码放置在标记为 `user
code (top of source file)` 的部分中。

### **Bottom of Model Source** — 在生成的源文件底部添加的代码 无默认值

指定希望代码生成器添加到模型源文件底部的代码。代码生成器将该代码放置在标记为
`user code (bottom of source file)` 的部分中。
## 所属库

Simulink Coder / Custom Code

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

## 描述

指定外部源代码

对于包含 Model Source 模块的模型，代码生成器会将您指定的外部代码添加到其生成的源文件
（`model.c` 或
`model.cpp`）中。您可以指定代码生成器添加到源文件顶部和底部附近的代码。

如果将此模块包含在引用模型中，代码生成器会针对仿真目标构建忽略该模块，但会针对其他系统目标文件处理该模块。

**注意**

此模块用于将任意自定义代码插入到生成代码的特定位置。请参阅
C Caller 和
C Function
模块，它们更常用于将自定义算法代码集成到模型中。
