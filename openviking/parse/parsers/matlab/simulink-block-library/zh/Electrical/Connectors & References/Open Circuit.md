---
type: simulink-block
title: 'Open Circuit'
family: 'electrical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'opencircuit'
documentation_source_path: '../simscape/ref/opencircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Circuit

## 端口

### 守恒端口

### **V** — 零电流电气端口

不汲取电流的电气守恒端口。

## 参数

在 R2025b 中未提供相关文档。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## 模块特性

在 R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019b: 不再需要端接未连接的端口

此模块不再是必需的。从 R2019b 开始，Simscape™ 模型中不允许存在未连接守恒端口的限制已取消。现在，如果让某个守恒端口保持未连接状态，物理网络会将此端口处的所有 Through 变量设置为 0。不过，您仍然可以使用端接模块来提高框图的可读性。

目前没有移除端接模块的计划。所有使用这些模块的现有模型，其工作方式均与以前版本相同。

## 描述

不汲取电流的电气端口端接器

Open Circuit 模块表示一个不汲取电流的电气端子。

您可以使用此模块端接其他模块上希望保持开路状态的电气端口。但这并非必需，因为如果让守恒端口保持未连接状态，物理网络会将该端口处的所有 Through 变量设置为 0。不过，端接模块可以提高框图的可读性。

您还可以使用此模块设置节点处的初始绝对电压。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
