---
type: simulink-block
title: 'Cap (MA)'
family: 'moist-air'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'capma'
documentation_source_path: 'ref/capma.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (MA)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零的湿空气

湿空气守恒端口，其中质量流量和能量流量均等于零。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2019b：不再需要对未连接端口进行封端

不再需要此模块。从 R2019b 开始，Simscape™ 模型中不允许未连接守恒端口的限制已解除。现在，如果使某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍然可以使用 Terminator 模块来提高图的可读性。

没有计划移除这些 Terminator 模块。所有使用这些模块的现有模型都与之前版本中的工作方式相同。

## 描述

零流量湿空气端口终结器

Cap (MA) 模块表示湿空气网络支路的完全隔热终端。没有质量或能量流经该封端。

您可以使用此模块来终结您想要封端的其他模块上的湿空气端口。这不是必需的，因为如果您使某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，Terminator 模块可提高图的可读性。

您还可以使用此模块在仿真前设置节点处的初始变量，例如压力或温度。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标以及具有有限湿空气体积的模块的初始条件。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
