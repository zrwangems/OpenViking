---
type: simulink-block
title: 'Two-Way Connection'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'twowayconnection'
documentation_source_path: '../autoblks/../simulink/ref_extras/twowayconnection.html'
language: zh-CN
chinese_source: official
---

# Two-Way Connection

## 端口

该模块有 Simulink 输入端口、Simulink 输出端口和双向连接器端口。

## 参数

R2025b 官方文档未提供。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2007a 中推出**

## 描述

用于子系统的双向连接器端口

Two-Way Connection 模块有一个双向连接器端口，可双向传输 Simulink® 信号。请考虑使用该模块实现以下目的：

- 减少端口连接数量。
- 将 Simulink 模块输入和反馈表示为单个物理连接。

要实现，请将双向连接器端口连接到另一个双向连接器端口。

连接会传输信号。

- `Signal1` - 第一个 Two-Way Connection 模块输入端口到第二个 Two-Way Connection 模块输出端口
- `Signal2` - 第二个 Two-Way Connection 模块输入端口到第一个 Two-Way Connection 模块输出端口

Two-Way Connection 模块支持用于自上而下或自下而上设计的不变模型架构。它允许您基于信号将子系统构建为 Simulink 模型，然后像连接物理系统一样连接它们。将 Two-Way Connection 模块放置在子系统内部并将其连接到 Connection Port (Simscape) 模块。然后子系统边界上的端口显示为双向连接器端口 。

**注意**

Powertrain Blockset™ 和 Vehicle Dynamics Blockset™ 模块可能包含**端口配置**参数选项，该选项允许您指定**双向连接**或 **Simulink** 连接。尽管这些连接看起来不同，但模块在任一配置下的功能都相同。
