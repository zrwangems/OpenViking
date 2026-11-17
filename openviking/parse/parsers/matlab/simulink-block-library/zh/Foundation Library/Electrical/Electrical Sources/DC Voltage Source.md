---
type: simulink-block
title: 'DC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'dcvoltagesource'
documentation_source_path: 'ref/dcvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Voltage Source

## 端口

### 守恒端口

### **+** — 正极端子电气

与电源正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电源负极端子关联的电气守恒端口。

## 参数

### **Constant voltage** — 输出电压 `1 V`（默认）| 标量

电源两端的电压。您可以指定正值或负值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想恒压源

DC Voltage Source 模块表示一个理想电压源，其功率足以在其端子之间维持指定的电压，无论流过电源的电流是多少。

您可以使用 **Constant voltage** 参数指定输出电压，该参数可以为正值或负值。

连接 **+** 和 **-** 是对应于电压源正极和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电源两端的电压等于正极端子电压与负极端子电压之差，*V*(+) – *V*(-)。
