---
type: simulink-block
title: 'Cap (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'cap2p'
documentation_source_path: 'ref/cap2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (2P)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零的两相流体

两相流体守恒端口，其中质量流量和能量流量均等于零。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2019b：不再需要对未连接端口进行封端

此模块不再必需。从 R2019b 开始，Simscape™ 模型中不允许未连接守恒端口的限制已被取消。现在，如果您将某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍然可以使用 terminator 模块来提高图的可读性。

没有计划移除 terminator 模块。所有使用这些模块的现有模型的工作方式都与之前版本相同。

## 描述

流体流动的完全隔热封端

Cap (2P) 模块表示两相流体支路的完全隔热终端。通过该封端没有流体流动或热传递。

您可以使用此模块端接您想要封端的其他模块上的两相流体端口。这并不是必需的，因为如果您将某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，terminator 模块可以提高图的可读性。

您还可以使用此模块设置节点处的初始压力和比内能。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”和“具有有限气体体积的模块的初始条件”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
