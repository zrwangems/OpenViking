---
type: simulink-block
title: 'Controlled Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'controlledvoltagesource'
documentation_source_path: 'ref/controlledvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Voltage Source

## 端口

### 输入

### **vT** — 电压控制信号，V 物理信号

用于指定电压值的输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 守恒

### **+** — 正极端子 电气

与电源正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与电源负极端子关联的电气守恒端口。

## 参数

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

由输入信号驱动的理想电压源

Controlled Voltage Source 模块表示一个理想电压源，其功率足以在其端子之间维持指定的电压，无论流过电源的电流大小如何。

输出电压为 *V = Vs*，其中 *Vs* 是物理信号端口上呈现的数值。
