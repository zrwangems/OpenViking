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
chinese_source: official
---

# Controlled Current Source

## 端口

### 输入

### **iT** — 电流控制信号 (A) 物理信号

用于指定电流值的输入物理信号。

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

由输入信号驱动的理想电流源

Controlled Current Source 模块表示理想的电流源，无论该电流源两端的电压多大，它都能将通过的电流保持在指定值。

输出电流为 *I = Is*，其中 *Is* 是在物理信号端口处呈现的数值。

箭头指示电流的正方向。
