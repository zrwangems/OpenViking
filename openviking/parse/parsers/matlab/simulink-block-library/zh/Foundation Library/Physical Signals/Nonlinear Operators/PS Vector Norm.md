---
type: simulink-block
title: 'PS Vector Norm'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psvectornorm'
documentation_source_path: 'ref/psvectornorm.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Vector Norm

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

输入物理信号，指定为行向量或列向量或矩阵。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。如果输入信号是向量，则输出信号是标量。如果输入信号是矩阵，则输出信号是表示输入矩阵的按列向量范数的向量或矩阵。

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

**在 R2023b 中引入**

## 描述

计算向量或矩阵物理信号的欧几里得范数

PS Vector Norm 模块计算向量或矩阵输入物理信号的欧几里得范数：

y=sqrt(dot(u,u))

其中：

- *y* 是输出端口 **O** 处的物理信号。
- *u* 是输入端口 **I** 处的物理信号。

如果输入信号是矩阵，则该模块计算按列向量范数。
