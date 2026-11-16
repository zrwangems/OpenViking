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
chinese_source: official
---

# Controlled Voltage Source

## 端口

### 输入

### **vT** — 电压控制信号（单位：V） 物理信号

指定电压值的输入物理信号。

端口名称在模块图标中不可见，但您可以在模块对话框的**描述**选项卡中点击**源代码**链接，在基础源文件中查看此名称。
### 守恒

### **+** — 正极端子 电气

与电气源正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电气源负极端子相关联的电气守恒端口。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

由输入信号驱动的理想电压源

Controlled Voltage Source 模块表示理想的电压源，无论流过电压源的电流多大，它都能将其两端的电压保持在指定值。

输出电压为 *V = Vs*，其中 *Vs* 是在物理信号端口处呈现的数值。
