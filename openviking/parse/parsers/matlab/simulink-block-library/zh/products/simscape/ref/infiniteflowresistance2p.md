---
type: simulink-block
title: 'Infinite Flow Resistance (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'infiniteflowresistance2p'
documentation_source_path: 'ref/infiniteflowresistance2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (2P)

## 端口

该模块具有一对两相流体守恒端口 A 和 B，表示相邻两相流体网络的分支。

## 参数

R2025b 中未提供相关文档。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中推出**

## 描述

两相流体网络中的完全绝热断开处

Infinite Flow Resistance (2P) 模块表示两相流体网络中的断开处。没有质量或能量流经该断开处。但是，由连接到回路的 Two-Phase Fluid Properties (2P) 模块指定的流体属性在断开处两侧相同。使用此模块可设置端口 **A** 与端口 **B** 之间压力差和比内能差的优先级及初始目标值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
