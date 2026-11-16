---
type: simulink-block
title: 'DC Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'dccurrentsource'
documentation_source_path: 'ref/dccurrentsource.html'
language: zh-CN
chinese_source: official
---

# DC Current Source

## 端口

### 守恒

### **+** — 正极端子 电气

与电气源正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电气源负极端子相关联的电气守恒端口。

## 参数

### **恒定电流** — 输出电流 `1 A` (默认) | 标量

源两端的电流。您可以指定正值，也可以指定负值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

理想的恒定电流源

DC Current Source 模块表示理想的电流源，无论该电流源两端的电压多大，它都能将通过的电流保持在指定值。

您可以使用**恒定电流**参数指定输出电流，可以是正值，也可以是负值。

箭头指示电流的正方向。
