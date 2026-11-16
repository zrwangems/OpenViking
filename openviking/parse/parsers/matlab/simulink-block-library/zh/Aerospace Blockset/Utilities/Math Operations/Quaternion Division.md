---
type: simulink-block
title: 'Quaternion Division'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaterniondivision'
documentation_source_path: 'quaterniondivision.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Division

## 端口

### 输入

### **q** — 被除四元数 quaternion | vector of quaternions

被除四元数采用以下形式：
[*q*0,
*p*0, ...,
*q*1,
*p*1, ... ,
*q*2,
*p*2, ... ,
*q*3,
*p*3, ...]，指定为四元数或四元数向量。

**数据类型：** `double`

### **r** — 除数四元数 quaternion | vector of quaternions

除数四元数采用以下形式：
[*s*0,
*r*0, ...,
*s*1,
*r*1, ... ,
*s*2,
*r*2, ... ,
*s*3,
*r*3, ...]，指定为四元数或四元数向量。

**数据类型：** `double`
### 输出

### **q/r** — 输出四元数 quaternion | vector

输出四元数或除法得到的四元数向量。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将四元数除以另一个四元数

Quaternion Division 模块将一个给定四元数除以另一个四元数。Aerospace Blockset™ 使用采用标量在前约定定义的四元数。输出是除法得到的四元数或除法得到的四元数向量。有关所使用的四元数形式，请参阅算法。
