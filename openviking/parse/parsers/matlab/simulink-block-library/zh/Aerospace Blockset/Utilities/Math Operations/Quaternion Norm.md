---
type: simulink-block
title: 'Quaternion Norm'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionnorm'
documentation_source_path: 'quaternionnorm.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Norm

## 端口

### 输入

### **q** — 四元数范数 四元数范数 | 四元数范数向量

以 [ *q*
0 , *r*
0 , ..., *q*
1 , *r*
1 , ... , *q*
2 , *r*
2 , ... , *q*
3 , *r*
3 , ...] 形式表示的四元数，指定为四元数范数或四元数范数向量。

**数据类型：** `double`
### 输出

### **norm(q)** — 四元数范数 四元数范数 | 四元数范数向量

以 [ *norm* (q), *norm* (r), ...] 形式表示的四元数范数或四元数范数向量。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算四元数的范数

Quaternion Norm 模块计算给定四元数的范数。Aerospace Blockset™ 使用按标量优先约定定义的四元数。有关四元数和四元数范数所使用的方程，请参见算法。
