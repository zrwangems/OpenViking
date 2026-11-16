---
type: simulink-block
title: 'Change Detector'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'changedetector'
documentation_source_path: 'ref/changedetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Change Detector

## 端口

### 输入

### **u** — Boolean 输入 `0` 或 `1`

输入 Boolean 信号。如果为 false，则 `0`。如果为 true，则 `1`。

**数据类型：** `Boolean`
### 输出

### **y** — 变化报告 `0` 或 `1`

当模块检测到与指定条件（rising、falling 或 either edge）相对应的变化时，输出为 true，`1`。否则，输出为 false，`0`。

**数据类型：** `Boolean`

## 参数

### **变化检测** — 变化条件 `Rising edge`（默认）| `Falling edge` | `Either edge`

变化检测的条件。

### **初始条件** — 初始 Boolean 值 `0`（默认）| 1

前一个输入的初始值。如果仿真开始时的输入与初始条件值不同，则模块检测到边沿。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

Boolean 信号变化检测器

Change Detector 模块在检测到 Boolean 输入信号中满足以下变化条件之一的变化时，输出 `true` 的 Boolean 响应：

- Rising edge — 输入从 false 变为 true。
- Falling edge — 输入从 true 变为 false。
- Either edge — 输入从 true 变为 false 或从 false 变为 true。
