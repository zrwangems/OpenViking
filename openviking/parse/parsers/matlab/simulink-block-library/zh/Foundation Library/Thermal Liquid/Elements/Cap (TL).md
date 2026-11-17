---
type: simulink-block
title: 'Cap (TL)'
family: 'thermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'captl'
documentation_source_path: 'ref/captl.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (TL)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零的热液体

热液体守恒端口，其中质量流量和能量流量均等于零。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2019b：不再需要封端未连接的端口

此模块不再必需。从 R2019b 开始，禁止 Simscape™ 模型中存在未连接守恒端口的限制已被解除。现在，如果让某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍然可以使用 Terminator 模块来提高图的可读性。

没有计划移除 Terminator 模块。所有使用这些模块的现有模型的工作方式与之前的版本相同。

## 描述

流体流动的完全隔热止端

Cap (TL) 模块表示热液体支路的末端。该止端完全隔热，可防止与其周围环境进行热传递。

您可以使用此模块终止其他模块上想要封端的热液体端口。这并非必需，因为如果让守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，Terminator 模块可提高图的可读性。

您还可以使用此模块设置节点处的初始压力和温度。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同的源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
