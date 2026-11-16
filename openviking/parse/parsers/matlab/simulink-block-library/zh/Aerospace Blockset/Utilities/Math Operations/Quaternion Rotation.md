---
type: simulink-block
title: 'Quaternion Rotation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionrotation'
documentation_source_path: 'quaternionrotation.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Rotation

## 端口

### 输入

### **q** — 四元数 quaternion | vector

形式为
[*q*0,
*r*0, ...,
*q*1,
*r*1, ... ,
*q*2,
*r*2, ... ,
*q*3,
*r*3, ...] 的四元数，指定为四元数或四元数向量。

**数据类型：** `double`

### **vec** — 初始向量 vector | vector of vectors

初始向量或向量组成的向量，形式为
[*v*1,
*u*1, ... ,
*v*2,
*u*2, ... ,
*v*3,
*u*3, ...]。

**数据类型：** `double`

### 输出

### **vec\_rot** — 最终四元数旋转后的 quaternion | vector of rotated quaternions

最终向量或旋转后的向量组成的向量。

**数据类型：** `double`

## 参数

在 R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用四元数旋转向量

Quaternion Rotation 模块计算初始向量 `vec` 经四元数 `q` 进行被动旋转后得到的结果向量，并返回最终向量，即旋转后的向量或旋转后的向量组成的向量。Aerospace Blockset™ 使用按标量优先约定定义的四元数。此模块会归一化所有四元数输入。有关用于四元数、初始向量和最终向量的方程，请参阅算法。
