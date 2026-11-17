---
type: simulink-block
title: 'Mach Number'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'machnumber'
documentation_source_path: 'machnumber.html'
language: zh-CN
chinese_source: worker-translation
---

# Mach Number

## 端口

### 输入

### **V** — 速度 三元向量

速度向量，指定为三元向量。

**数据类型：** `double`

### **a** — 声速 1×1 数组

声速，指定为 1×1 数组。

**数据类型：** `double`
### 输出

### **Mach** — 马赫数 标量

马赫数，返回为标量。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用速度和声速计算马赫数

Mach Number 模块计算马赫数。马赫数定义为

Mach=V⋅Va，

其中 *a* 是声速，*V* 是速度向量。
