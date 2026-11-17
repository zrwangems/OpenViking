---
type: simulink-block
title: 'Cap (TL)'
family: 'simscape'
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

### 守恒端口

### **A** — 质量流量和能量流量均为零的热流体

热流体守恒端口，其质量流量和能量流量均等于零。

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

### R2019b：不再需要封堵未连接的端口

不再需要此模块。从 R2019b 开始，Simscape™ 模型中禁止未连接守恒端口的限制已被取消。现在，如果保留某个守恒端口未连接，物理网络会将该端口处所有 Through 变量设置为 0。但是，您仍然可以使用终结器模块来提高图的可读性。

没有移除终结器模块的计划。所有使用这些模块的现有模型的工作方式与之前版本相同。

## 描述

完全隔热的流体流动止端

Cap (TL) 模块表示热流体支路的终点。该止端完全隔热，防止与周围环境进行热传递。

您可以使用此模块来封堵其他模块上您想要封堵的热流体端口。这不是必需的，因为如果您保留某个守恒端口未连接，物理网络会将该端口处所有 Through 变量设置为 0。但是，终结器模块可以提高图的可读性。

您还可以使用此模块来设置某个节点处的初始压力和温度。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
