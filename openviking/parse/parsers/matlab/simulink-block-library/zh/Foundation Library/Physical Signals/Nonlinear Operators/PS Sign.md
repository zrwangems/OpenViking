---
type: simulink-block
title: 'PS Sign'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'pssign'
documentation_source_path: 'ref/pssign.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Sign

## 端口
```yaml
ports:
- name: I
  summary: 输入物理信号，无类型物理信号
  direction: input
- name: O
  summary: 输出物理信号，无类型物理信号
  direction: output
```

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。信号大小与输入信号的大小相同，但单位始终为 `1`（无单位）。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

输出输入物理信号的符号

PS Sign 模块返回输入物理信号的符号：

- 当输入大于零时，输出为 1。
- 当输入等于零时，输出为 0。
- 当输入小于零时，输出为 –1。

输入和输出均为物理信号。无类型物理端口有助于信号大小传播。输出信号始终无单位。
