---
type: simulink-block
title: 'Hydraulic Cap'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydrauliccap'
documentation_source_path: 'ref/hydrauliccap.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Cap

## 端口

### 守恒

### **P** — 零流量液压

零流量的液压守恒端口。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Hydraulic / Hydraulic Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2023a: 将被删除

Hydraulic 库将在未来版本中删除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅将 Hydraulic 模型升级为使用 Isothermal Liquid 模块。

### R2019b: 不再需要对未连接的端口进行封堵

不再需要此模块。从 R2019b 开始，已取消在 Simscape™ 模型中禁止未连接守恒端口的限制。现在，如果您将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍可以使用 terminator 模块来提高图的可读性。

目前没有删除 terminator 模块的计划。所有使用这些模块的现有模型的工作方式与之前版本相同。

## 描述

（将被删除）零流量液压端口终止器

Hydraulic Cap 模块表示一个液压堵头，即一个通过流量为零的液压端口。

您可以使用此模块终止其他模块上要封堵的液压端口。这并不是必需的，因为如果您将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，terminator 模块可提高图的可读性。

您还可以使用此模块设置节点处的初始表压。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种方式来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
