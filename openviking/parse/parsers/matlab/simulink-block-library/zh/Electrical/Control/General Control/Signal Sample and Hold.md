---
type: simulink-block
title: 'Signal Sample and Hold'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'signalsampleandhold'
documentation_source_path: 'ref/signalsampleandhold.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Sample and Hold

## 端口

### 输入

### **u** — 输入信号 标量 | 向量

输入信号。

**数据类型：** `single` | `double`

### **S** — 控制信号 `0` | `1`

采样脉冲，`0` 表示 `false`，或 `1` 表示 `true`。

**数据类型：** `Boolean`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号。

**数据类型：** `single` | `double`

## 参数

### **初始条件** — 初始输出值 标量 | 向量

指定初始条件。该值必须为标量，或与输入信号大小相同的向量。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认） | `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在掩码上提升模块参数。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散时间或连续时间采样保持输入信号

Signal Sample and Hold 模块在离散时间或连续时间中实现信号采样保持。

当输入 *S* 为 `true` 时，输出 *y* 等于输入 *u*。当输入 *S* 为 `false` 时，模块保持输出，直到 *S* 再次变为 `true`。
