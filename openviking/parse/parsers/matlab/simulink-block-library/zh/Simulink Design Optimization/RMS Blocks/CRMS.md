---
type: simulink-block
title: 'CRMS'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'RMS Blocks'
documentation_page: 'crms'
documentation_source_path: 'ref/crms.html'
language: zh-CN
chinese_source: worker-translation
---

# CRMS

## 端口

### 输入

### **Port\_1** — 输入信号 标量

输入值，指定为标量信号。
### 输出

### **Port\_1** — CRMS 值 标量

计算得到的连续时间均方根值，输出为标量信号。

## 参数

R2025b 中未记录。

## 所属库

Simulink Design Optimization / RMS Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。

## 版本历史

**在 R2009a 中引入**

## 描述

计算信号的连续时间累积均方根

将 CRMS 模块连接到信号以计算其连续时间累积均方根（CRMS）值，该值提供了信号中平均能量的度量。

信号 *u*(*t*) 的连续时间累积均方根值定义为

CRMS=1T∫0T‖u(t)‖2dt

要优化信号能量，请将此模块与 Check Custom Bounds 模块配合使用。
