---
type: simulink-block
title: 'Controlled Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'controlledcurrentsource'
documentation_source_path: 'ref/controlledcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Current Source

## 端口
```yaml
ports:
- name: iT
  summary: 电流控制信号，A physical signal
  direction: input
- name: +
  summary: 正极端口 electrical
  direction: input
- name: '-'
  summary: 负极端口 electrical
  direction: input
```

### 输入

### **iT** — 电流控制信号，A physical signal

输入物理信号，用于指定电流值。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 守恒

### **+** — 正极端口 electrical

与源正极端子相关联的电学守恒端口。

### **-** — 负极端口 electrical

与源负极端子相关联的电学守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

由输入信号驱动的理想电流源

Controlled Current Source 模块表示一个理想电流源，其能力足以维持通过它的指定电流，无论源两端的电压如何。

输出电流为 *I = Is*，其中 *Is* 是物理信号端口上呈现的数值。

电流流动的正方向由箭头指示。
