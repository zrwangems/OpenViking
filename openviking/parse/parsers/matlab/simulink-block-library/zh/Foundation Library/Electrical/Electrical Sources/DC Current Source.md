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
chinese_source: worker-translation
---

# DC Current Source

## 端口

### 守恒端口

### **+** — 正极端子电气

与源正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与源负极端子关联的电气守恒端口。

## 参数

### **Constant current** — 输出电流 `1 A`（默认）| 标量

通过源的电流。您可以指定正值或负值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想恒流源

DC Current Source 模块表示一个理想电流源，其足够强大，无论源两端的电压如何，都能维持通过它的指定电流。

您可以使用 **Constant current** 参数指定输出电流，该参数可以为正值或负值。

电流的正方向由箭头指示。
