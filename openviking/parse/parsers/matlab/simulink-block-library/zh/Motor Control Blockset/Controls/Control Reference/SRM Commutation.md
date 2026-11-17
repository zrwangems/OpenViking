---
type: simulink-block
title: 'SRM Commutation'
family: 'controls'
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

### **θe** — 电机电气位置标量

电机相对于相 *a*（电机的第一相）测量的电气位置。指定位置在 `0-2π` radians 或 `0-360` degrees 或 `0-1` per-unit 之间。

**数据类型：** `single` | `double` | `fixed point`

### **θeOn** — 开启电机电气位置标量

相 *a*（由 `θe` 输入使用的相）的电机电气位置，在该位置开关序列从 `0` 变为 `1` 并激励对应相。指定位置在 `0`-`2π` radians 或 `0`-`360` degrees 或 `0`-`1` per-unit 之间。

**数据类型：** `single` | `double` | `fixed point`

### **θeOff** — 关闭电机电气位置标量

相 *a*（由 `θe` 输入使用的相）的电机电气位置，在该位置开关序列从 `1` 变为 `0` 并使对应相断电。该值应介于 `0-2π` radians 或 `0-360` degrees 或 `0-1` per-unit 之间。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Ctrl** — 控制信号向量

开关序列的组合，可用于将每一相切换到 on 和 off 以驱动电机。

**数据类型：** `Boolean`

## 参数

### **电机相数** — SRM 中的相数 `3`（默认） | `4` | `5` | `6`

SRM 定子绕组中的相数。

### **输入位置单位** — 位置输入的单位 `Radians`（默认） | `Per unit` | `Degrees`

`θe`、`θeOn` 和 `θeOff` 输入的单位。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

为 n 相开关磁阻电机 (SRM) 生成开关序列

SRM Commutation 模块实现一个换相系统，该系统生成开关序列以激励 *n* 相 SRM 的定子绕组。

该模块支持三相、四相、五相或六相 SRM。

有关该模块所用算法的更多详细信息，请参阅算法。
