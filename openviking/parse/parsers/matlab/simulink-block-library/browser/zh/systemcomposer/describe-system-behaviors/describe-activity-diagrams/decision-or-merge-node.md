---
type: simulink-block
title: 'Decision or Merge Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'decisionormergenode'
documentation_source_path: 'ref/decisionormergenode.html'
language: zh-CN
chinese_source: official
---

# Decision or Merge Node

## 端口

R2025b 官方文档未提供。

## 参数

### 决策或合并节点

### **显示名称** — 显示决策或合并节点的名称 `off` (默认) | `on`

选择**显示名称**时，节点名称 `MergeDecision` 将显示在其边界内。然后，您可以根据需要更改节点的名称。当您添加更多决策或合并节点时，编辑器会在名称 `MergeDecision` 中附加越来越多的数字后缀。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2024a 中推出**

## 描述

根据 MATLAB 表达式的计算结果路由输入令牌，或将多个输入令牌合并为一个输出流

决定或合并节点用灰色菱形表示。您可以根据输入和输出令牌流的配置方式，将 Decision or Merge Node 模块用于决策或合并函数。

- 决策节点 - 只包含一个输入令牌流，但可以有多个输出令牌流。
- 合并节点 - 只包含一个输出令牌流，但可以有多个输入令牌流。

### 决策

决策节点的作用是根据与每个流相关的布尔表达式的计算结果，将输入令牌（包括控制流）路由到输出流之一。这些表达式称为  *保护表达式*。如果相应的保护表达式求值为 `true`，则决策节点会将输入令牌路由到输出流。您可以通过 `token` 关键字在保护表达式中使用输入的令牌值。

Simple activity diagram with a Merge or Decision node using the token keyword on its output branches.

决策节点的所有保护表达式都有一个计算顺序。活动图编辑器会将输入令牌路由到防护表达式满足要求的第一个输出流。这意味着，如果传入对象令牌值的值满足一个以上的保护表达式，它就会通过最先求值的输出分支退出。

### 合并

合并节点的目的是，当输入令牌到达节点时，允许所有输入令牌流通过一个共同的输出流退出。

### 决策与合并

Decision or Merge Node 模块还可以同时作为决策节点和合并节点。如果要使用这种配置，必须创建具有多个输入和输出流的节点。

如果节点既是决策节点又是合并节点，那么它就等同于一个合并节点，紧接着一个决策节点。也就是说，首先合并输入对象令牌，然后再沿着最合适的输出流进行路由。

### 创建决策或合并节点

您可以通过两种方式在活动图画布上创建决策或合并节点：

- 将 Decision or Merge Node 模块从左边的调色板拖放到画布上的任意位置。
- 在画布上所需位置按住鼠标左键，然后向任意方向拖动。节点的蓝色轮廓会出现在画布上。从轮廓下方出现的横向菜单中选择**创建合并决策**。
