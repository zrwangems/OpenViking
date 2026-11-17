---
type: simulink-block
title: 'Cap (IL)'
family: 'isothermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'capil'
documentation_source_path: 'ref/capil.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (IL)

## 端口

### 守恒

### **A** — 质量流量为零的等温液体

等温液体守恒端口，其中质量流量等于零。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

零流量的等温液体端口终端

Cap (IL) 模块表示等温液体分支的终端。没有质量流量通过该模块。

您可以使用此模块终止其他模块上想要封端的等温液体端口。使用此模块并非必需，因为如果使守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，终端模块可提高框图可读性。

您还可以使用此模块设置节点处的初始压力。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
