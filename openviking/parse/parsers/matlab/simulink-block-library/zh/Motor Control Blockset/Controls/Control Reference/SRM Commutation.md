---
type: simulink-block
title: 'SRM Commutation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'srmcommutation'
documentation_source_path: 'ref/srmcommutation.html'
language: zh-CN
chinese_source: worker-translation
---

# SRM Commutation

## 端口

### 输入

### **θe** — 电机电角度标量

相对于电机第一相（即 *a* 相）测量的电机电角度位置。指定位置时使用 `0-2π` 弧度或 `0-360` 度或 `0-1` 标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **θeOn** — 开通电机电角度标量

*a* 相（`θe` 输入所使用的相）的电机电角度位置，在该位置开关序列从 `0` 变为 `1` 并激励对应相。指定位置时使用 `0`-`2π` 弧度或 `0`-`360` 度或 `0`-`1` 标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **θeOff** — 关断电机电角度标量

*a* 相（`θe` 输入所使用的相）的电机电角度位置，在该位置开关序列从 `1` 变为 `0` 并断开对应相的激励。该值应位于 `0-2π` 弧度或 `0-360` 度或 `0-1` 标幺值之间。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Ctrl** — 控制信号向量

开关序列的组合，可用于将每一相切换为开通和关断以驱动电机。

**数据类型：** `Boolean`

## 参数

### **Number of motor phases** — SRM 中的相数 `3`（默认）| `4` | `5` | `6`

SRM 定子绕组中的相数。

### **Input position units** — 位置输入的单位 `Radians`（默认）| `Per unit` | `Degrees`

`θe`、`θeOn` 和 `θeOff` 输入的单位。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

为 n 相开关磁阻电机（SRM）生成开关序列

SRM Commutation 模块实现了一个换相系统，该系统生成开关序列以激励 *n* 相 SRM 的定子绕组。

该模块支持三相、四相、五相或六相 SRM。

有关该模块所用算法的更多详细信息，请参阅 Algorithm。
