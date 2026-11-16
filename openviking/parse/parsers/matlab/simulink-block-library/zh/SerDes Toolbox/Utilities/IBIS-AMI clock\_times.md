---
type: simulink-block
title: 'IBIS-AMI clock_times'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'ibisamiclock_times'
documentation_source_path: 'ref/ibisamiclock_times.html'
language: zh-CN
chinese_source: worker-translation
---

# IBIS-AMI clock_times

## 端口

### 输入

### **clockValid** — 在 clockTime 端口更新输入 标量 | 向量

更新 **clockTime** 端口处的输入，指定为标量或向量。**clockValid** 端口处的值使得每个样本仅输出一个时钟时间。

**clockValid** 端口处输入信号的每个上升沿会更新通过 **clockTime** 端口传递的 S function。通常，每个单位间隔 (UI) 发生一次。

**数据类型：** `double` | `int8`

### **clockTime** — 时钟时间数据数组

时钟时间数据，指定为数组。时钟时间数据使用 S function 传递给 AMI wrapper 代码。

**clockTime** 端口处的时间值必须在实际数据采样时间之前半个 UI。

**数据类型：** `double`

## 参数

### **Enable IBIS-AMI Offset** — 按半个 UI 偏移时钟时间值 on（默认）| off

根据 IBIS-AMI 规范，按半个 UI 偏移时钟时间值。

## 所属库

SerDes Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从自定义 DFECDR 和 CDR 恢复 SerDes 时钟时间值

当使用自定义 DFECDR 或 CDR 模块而不是 SerDes Toolbox™ 提供的模块时，IBIS-AMI clock\_times 模块会恢复 SerDes 系统的时钟时间值。该模块从 AMI\_GetWave 函数恢复时钟时间值，并将其输出到生成的 IBIS-AMI 模型。

IBIS-AMI clock\_times 模块的输出是两个全局变量：`extern double* Rx_clock_times_buf` 和 `extern int
Rx_clock_times_idx`。该模块仅创建这些变量。必须将它们添加到自定义代码中才能使其工作。这些变量共同实现 IBIS 7.0 规范中定义的 `clock_times` 向量。
