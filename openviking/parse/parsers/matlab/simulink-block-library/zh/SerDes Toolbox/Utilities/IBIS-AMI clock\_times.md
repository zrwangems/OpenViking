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

在 **clockTime** 端口更新输入，指定为标量或向量。**clockValid** 端口的值使得每个采样仅输出一个时钟时间。

**clockValid** 端口上输入信号的每个上升沿更新通过 **clockTime** 端口的 S 函数。通常每个单位间隔（UI）发生一次。

**数据类型：** `double` | `int8`

### **clockTime** — 时钟时间数据数组

时钟时间数据，指定为数组。时钟时间数据通过 S 函数传递给 AMI 包装代码。

**clockTime** 端口的时间值必须比实际数据采样时间提前半个 UI。

**数据类型：** `double`

## 参数

### **Enable IBIS-AMI Offset** — 将时钟时间值偏移半个 UI on（默认）| off

根据 IBIS-AMI 规范，将时钟时间值偏移半个 UI。

## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从自定义 DFECDR 和 CDR 恢复 SerDes 时钟时间值

当您使用自定义 DFECDR 或 CDR 模块而非 SerDes Toolbox™ 提供的模块时，IBIS-AMI clock\_times 模块可恢复 SerDes 系统的时钟时间值。该模块从 AMI\_GetWave 函数中恢复时钟时间值，并将其输出到生成的 IBIS-AMI 模型。

IBIS-AMI clock\_times 模块的输出是两个全局变量，`extern double* Rx_clock_times_buf` 和 `extern int Rx_clock_times_idx`。该模块仅创建这些变量。您必须将它们添加到自定义代码中才能使其工作。这些变量共同实现了 IBIS 7.0 规范中定义的 `clock_times` 向量。
