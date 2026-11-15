---
type: simulink-block
title: 'Quaternion Inverse'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: 'quaternioninverse'
documentation_source_path: 'quaternioninverse.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Inverse

## 端口

### 输入

### **q** — 四元数
quaternion | 四元数向量

四元数，形式为 [ *q*0 , *r*0 , ..., *q*1 , *r*1 , ... , *q*2 , *r*2 , ... , *q*3 , *r*3 , ...]，指定为四元数或四元数向量。

**数据类型:** `double`
### 输出

### **Inv(q)** — 四元数逆
四元数逆 | 四元数逆向量

四元数逆或四元数逆向量。

**数据类型:** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算四元数的逆

Quaternion Inverse 模块计算给定四元数的逆。Aerospace Blockset™ 使用采用标量在前约定定义的四元数。有关用于四元数和四元数逆的方程，请参阅算法。
