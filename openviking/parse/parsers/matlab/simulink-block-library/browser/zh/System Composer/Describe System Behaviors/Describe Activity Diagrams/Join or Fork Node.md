---
type: simulink-block
title: 'Join or Fork Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'joinorforknode'
documentation_source_path: 'ref/joinorforknode.html'
language: zh-CN
chinese_source: official
---

# Join or Fork Node

## 端口

R2025b 官方文档未提供。

## 参数

R2025b 官方文档未提供。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2024a 中推出**

## 描述

将多个输入令牌同步到一个输出中，或在所有输出流中复制一个输入令牌

一个 Join or Fork Node 模块用一条两端呈圆形的灰色粗线表示。您可以将 Join or Fork Node 模块用于 join 或 fork 函数，具体取决于您如何配置输入和输出令牌流。

- 连接节点 - 只包含一个输出令牌流，但可以有多个输入令牌流
- 分叉节点 - 只包含一个输入令牌流，但可以有多个输出令牌流

### 汇合

连接节点的目的是将所有传入的令牌流（包括控制流）连接成一个输出流。当一个对象令牌出现在所有输入流中时，连接节点会将这些令牌同步为一个合并令牌，并通过输出流输出。当所有输入流量都有控制令牌时，连接节点会输出一个有代表性的控制令牌。连接节点的所有输入对象令牌的数据类型必须相同。

### 分叉

分叉节点的函数是复制传入的令牌，并向每个输出流发送一份副本。

### 创建连接或分叉节点

您可以通过两种方式在活动图画布上创建连接或分叉节点：

- 将 Join or Fork Node 模块从左边的调色板拖放到画布上的任意位置。
- 在画布上所需位置按住鼠标左键，然后向任意方向拖动。节点的蓝色轮廓会出现在画布上。从轮廓下方出现的横向菜单中选择**创建汇合分叉**。
