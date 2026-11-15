---
type: simulink-block
title: 'Cannon'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'cannon'
documentation_source_path: 'supportpkg/parrot_ref/cannon.html'
language: zh-CN
chinese_source: worker-translation
---

# Cannon

## 端口

### 输入

### **Port\_1** — 用于控制 Cannon 模块的输入信号 `1` | `0`

每当输入从
`0` 变为 `1` 时，Cannon 模块发射一个球。

如果发往 Cannon 模块的输入命令有多个（用于连续发射球），这些命令会排队，并按顺序逐个执行。

**提示**

你也可以在同一 Simulink
模型中使用多个 Cannon 模块（而不是在一个 Cannon 模块中排队命令）来连续发射球。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 队列中待处理的发射命令数，标量整数 | `-1`

当 Cannon 模块忙时，队列中待处理的发射命令数。

输出值 `-1` 表示 Cannon
模块未连接到无人机，或者 Cannon 模块未工作。

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

控制连接到 Parrot Mambo 迷你无人机的 Cannon 模块

Cannon 模块控制连接到 Parrot® Mambo 迷你无人机的 Cannon 模块。
