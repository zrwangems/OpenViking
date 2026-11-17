---
type: simulink-block
title: 'DRMS'
family: 'rms-blocks'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'RMS Blocks'
documentation_page: 'drms'
documentation_source_path: 'ref/drms.html'
language: zh-CN
chinese_source: worker-translation
---

# DRMS

## 端口

### 输入

### **Port\_1** — 输入信号标量

输入值，指定为标量信号。
### 输出

### **Port\_1** — DRMS 值标量

计算得到的离散时间均方根值，作为标量信号输出。

## 参数

### **采样间隔** — 采样时间 `1`（默认）| 正标量

用于计算 DRMS 值的采样时间。

#### 编程用法

|  |
| --- |
| **参数：** `Ts` |
| **值：** 带引号的正标量 |
| **默认值：** `'1'` |

## 所属库

Simulink Design Optimization / RMS Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009a 中引入**

## 描述

计算信号的离散时间累积均方根 (DRMS)

将 DRMS 模块连接到信号，以计算其离散时间累积均方根
(DRMS) 值，该值提供信号中平均能量的度量。

信号
*u*(*t*) 的离散时间累积均方根值定义为

DRMS=1N∑i=1N‖u(ti)‖2

为了优化信号能量，请将此模块与 Check Custom Bounds
模块结合使用。
