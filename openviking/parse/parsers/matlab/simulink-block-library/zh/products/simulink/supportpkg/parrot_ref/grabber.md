---
type: simulink-block
title: 'Grabber'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'grabber'
documentation_source_path: 'supportpkg/parrot_ref/grabber.html'
language: zh-CN
chinese_source: worker-translation
---

# Grabber

## 端口

### 输入

### **Port\_1** — 用于控制 Grabber 模块的输入信号 `1` | `0`

如果输入为 `1`，Grabber 关闭（以抓取物体）；如果输入为 `0`，Grabber 打开（以将物体放置到位）。

**注意**

输入信号值的变化（`0` 到 `1` 或 `1` 到 `0`）会导致 Grabber 立即执行动作。例如，即使由于先前输入信号值为 `0` 而正在执行打开动作，只要输入信号变为 `1`，Grabber 也会立即关闭。

**数据类型：** `Boolean`

### 输出

### **Port\_1** — Grabber 模块的当前状态 `0` | `1` | `-1`

该模块输出以下三个值之一，这些值对应于 Grabber 模块的当前状态：

- `1` – Grabber 已关闭
- `0` – Grabber 已打开
- `-1` – Grabber 未连接到无人机或无法工作

**数据类型：** `uint8`

## 参数

在 R2025b 中未记录。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

控制连接到 Parrot Mambo minidrone 的 Grabber 模块

Grabber 模块控制连接到 Parrot® Mambo minidrone 的 Grabber 模块。
