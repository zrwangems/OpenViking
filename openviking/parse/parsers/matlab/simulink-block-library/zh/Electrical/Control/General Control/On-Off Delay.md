---
type: simulink-block
title: 'On-Off Delay'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'onoffdelay'
documentation_source_path: 'ref/onoffdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# On-Off Delay

## 端口

### 输入

### **u** — 输入信号 `0` | `1`

输入 Boolean 信号。

**数据类型：** `Boolean`
### 输出

### **y** — 输出信号 `0` | `1`

带延迟的输出信号。

**数据类型：** `Boolean`

## 参数

### **ON delay time (s)** — 输入 ON 延迟时间 `0.01`（默认）| `0` | 正标量

指定输入为 ON 时的延迟时间。

### **OFF delay time (s)** — 输入 OFF 延迟时间 `0`（默认）| 正标量

指定输入为 OFF 时的延迟时间。

### **Initial state** — 信号初始状态 `0`（默认）| `1`

指定初始状态。

### **Sample time** — 模块采样时间 `0.001`（默认）| 0 | 正标量

连续模块执行之间的时间。
在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

对于离散时间操作，将采样时间设置为正值。对于连续时间操作，将采样时间设置为 `0`。

如果此模块位于封装子系统中，或位于允许连续和离散操作的其他变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅“提升封装上的模块参数”。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

Boolean 信号延迟

On-Off Delay 模块对 Boolean 输入信号施加延迟。

当在输入信号中检测到跳变时，会添加时间延迟。此模块允许你在以下情况下向输入信号添加时间延迟：

- 检测到 ON 跳变（输入从 0 变为 1），
- 检测到 OFF 跳变（输入信号从 1 变为 0），或
- 检测到任一跳变。

On-Off Delay 的操作如下图所示：
