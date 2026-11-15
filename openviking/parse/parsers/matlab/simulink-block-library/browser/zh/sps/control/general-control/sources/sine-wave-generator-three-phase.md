---
type: simulink-block
title: 'Sine Wave Generator (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Sources'
documentation_page: 'sinewavegeneratorthreephase'
documentation_source_path: 'ref/sinewavegeneratorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Sine Wave Generator (Three-Phase)

## 端口

### 输入

### **mag** — 生成的三相正弦波的幅值，标量

生成的三相正弦波的幅值，指定为标量。

### **ang** — 生成的三相正弦波的相移，deg 标量

生成的三相正弦波中相 *a* 的相移，指定为以 degrees 为单位的标量。

### **freq** — 生成的三相正弦波的频率，Hz 标量

生成的三相正弦波的频率，指定为以 Hz 为单位的标量。
### 输出

### **abc** — 三相正弦波向量

三相正弦波，以 Simulink 信号向量形式返回。

### **wt** — 所有三相正弦波的角度，rad 向量

正弦波所有三相的角度，以 rad 为单位的 Simulink 信号向量形式返回。

## 参数

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于 inherited 离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在封装上提升模块参数。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间三相正弦波生成器

Sine Wave Generator (Three-Phase) 模块根据幅值、相移和频率输入生成平衡三相正弦波。
