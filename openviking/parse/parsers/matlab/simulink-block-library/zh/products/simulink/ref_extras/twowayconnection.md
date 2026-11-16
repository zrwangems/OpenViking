---
type: simulink-block
title: 'Two-Way Connection'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'twowayconnection'
documentation_source_path: '../simulink/ref_extras/twowayconnection.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Way Connection

## 端口

该模块具有一个 Simulink 输入端口、一个 Simulink 输出端口和一个双向连接器端口。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2007a 中引入**

## 描述

用于子系统的双向连接器端口

Two-Way Connection 模块具有一个双向连接器端口，可双向传输 Simulink® 信号。可考虑在以下情况下使用该模块：

- 减少端口连接数量。
- 将 Simulink 模块输入和反馈表示为单个物理连接。

要实现此功能，请将该双向连接器端口连接到另一个双向连接器端口。

该连接会传输信号。

- `Signal1` – 从第一个 Two-Way Connection 模块的输入端口到第二个 Two-Way Connection 模块的输出端口
- `Signal2` – 从第二个 Two-Way Connection 模块的输入端口到第一个 Two-Way Connection 模块的输出端口

Two-Way Connection 模块支持用于自顶向下或自底向上设计的不变模型架构。它允许您基于信号将子系统构建为 Simulink 模型，然后像物理系统一样将它们连接起来。将 Two-Way Connection 模块放置在子系统内部，并将其连接到 Connection Port (Simscape) 模块。然后，子系统边界上的端口将显示为双向连接器端口。

**注意**

Powertrain Blockset™ 和 Vehicle Dynamics Blockset™ 中的模块可能包含 **Port Configuration** 参数选项，允许您指定 `Two-way connection` 或 `Simulink` 连接。尽管连接的外观不同，但模块在两种配置下的功能相同。
