---
type: simulink-block
title: 'CLA Math'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'clamath'
documentation_source_path: 'ref/clamath.html'
language: zh-CN
chinese_source: worker-translation
---

# CLA Math

## 端口

### 输入

### **u** — 输入数据向量

该模块接受指定为 *N*×1 数组的数据。

**数据类型：** `single`
### 输出

### **y** — 输出数据标量

该模块输出 single 类型的 *N*×1 数组数据。该模块输出所选函数参数的值。

**数据类型：** `single`

## 参数

### **Function** — 选择 CLA Math 函数 `CLAsin`（默认）| `CLAcos` | `CLAasin` | `CLAacos` | `CLAatan` | `CLAatan2` | `CLAsinPU` | `CLAcosPU` | `CLAatan2PU` | `CLAexp` | `CLAexp2` | `CLAexp10` | `CLAexpN` | `CLALn` | `CLALog10` | `CLALogN` | `CLAdiv` | `CLAsqrt` | `CLAisqrt`

选择 CLA Math 函数，其中包括三角函数、对数函数、指数函数和幂函数。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

实现 CLA Math 库中的 CLA Math 函数

CLA Math 实现 CLA Math 库中的 CLA Math 函数。CLA Math 函数包括三角函数、对数函数、指数函数和幂函数。

**注意**

CLA Math 模块仅在为 CLA 配置的模型中工作。

三角函数接受以弧度表示的输入。PU 三角函数接受以标幺值表示的输入。

该模块仅接受 single 数据类型的输入，并输出 single 类型的数据。
