---
type: simulink-block
title: 'Cap (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'capg'
documentation_source_path: 'ref/capg.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (G)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零的气体

气体守恒端口，其中质量流量和能量流量均等于零。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2019b：不再需要对未连接端口进行封端

不再需要此模块。从 R2019b 开始，禁止 Simscape™ 模型中未连接守恒端口的限制已解除。现在，如果您让某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍然可以使用 Terminator 模块来提高图的可读性。

没有计划移除这些 Terminator 模块。所有使用这些模块的现有模型与先前版本的工作方式相同。

## 描述

零流量的气体端口终结器

Cap (G) 模块表示气体网络分支的完全绝缘终端。通过该 cap 没有质量或能量流动。

您可以使用此模块来终止其他模块上您想要封端的气体端口。这不是必需的，因为如果您让某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，Terminator 模块可提高图的可读性。

您还可以使用此模块设置节点处的初始压力和温度。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”和“具有有限气体体积的模块的初始条件”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
