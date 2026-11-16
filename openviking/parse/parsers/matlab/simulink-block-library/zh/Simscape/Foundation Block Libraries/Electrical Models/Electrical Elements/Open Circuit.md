---
type: simulink-block
title: 'Open Circuit'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'opencircuit'
documentation_source_path: 'ref/opencircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Circuit

## 端口

### 守恒

### **V** — 零电流电气

不汲取电流的电气守恒端口。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019b：不再需要对未连接端口进行封端

此模块不再需要。从 R2019b 开始，Simscape™ 模型中禁止未连接守恒端口的限制已取消。现在，如果将一个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍可以使用 Terminator 模块来提高图的可读性。

没有计划移除 Terminator 模块。所有使用这些模块的现有模型的工作方式与以前的版本相同。

## 描述

不汲取电流的电气端口终结器

Open Circuit 模块表示不汲取电流的电气端子。

您可以使用此模块来端接其他模块上您想要保持开路的电气端口。这不是必需的，因为如果将一个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，Terminator 模块可以提高图的可读性。

您还可以使用此模块设置节点处的初始绝对电压。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
