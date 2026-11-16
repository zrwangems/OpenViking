---
type: simulink-block
title: 'Quaternion Conjugate'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionconjugate'
documentation_source_path: 'quaternionconjugate.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Conjugate

## 端口

### 输入

### **q** — 输入四元数 quaternion | vector of quaternions

四元数采用以下形式
[*q*0,
*r*0, ... ,
*q*1,
*r*1, ... ,
*q*2,
*r*2, ... ,
*q*3,
*r*3, ...]，指定为
四元数或向量。

**数据类型：** `double` | `bus`
### 输出

### **q'** — 四元数共轭 quaternion conjugate | vector of quaternion conjugates

四元数共轭采用以下形式
[*q*0′,
*r*0′, ... ,
*q*1′,
*r*1′, ... ,
*q*2′,
*r*2′, ... ,
*q*3′,
*r*3′, ...]，以
四元数或向量形式返回。

**数据类型：** `double` | `bus`

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

计算四元数的共轭

Quaternion Conjugate 模块计算给定四元数的共轭。Aerospace Blockset™ 使用按标量优先约定定义的四元数。有关四元数形式的更多信息，请参阅 Algorithms。
