---
type: simulink-block
title: 'Quaternion Multiplication'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionmultiplication'
documentation_source_path: 'quaternionmultiplication.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Multiplication

## 端口

### 输入

### **q** — 第一个四元数 四元数 | 四元数向量

第一个四元数，指定为向量或四元数向量。四元数向量具有以下形式，其中 *q* 和
*p* 是四元数：

`[ q
0 , p
0 , ..., q
1 , p
1 , ... , q
2 , p
2 , ... , q
3 , p
3 , ...]`

**数据类型：** `double`

### **r** — 第二个四元数 四元数 | 四元数向量

第二个四元数，指定为向量或四元数向量。四元数向量具有以下形式，其中 *s* 和
*r* 是四元数：

`[ s
0 , r
0 , ..., s
1 , r
1 , ... , s
2 , r
2 , ... , s
3 , r
3 , ...]`

**数据类型：** `double`
### 输出

### **q\*r** — 乘积 向量 | 四元数乘积向量

两个四元数的乘积，输出为向量或四元数乘积向量。

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

计算两个四元数的乘积

Quaternion Multiplication 模块计算两个给定四元数的乘积。Aerospace Blockset™ 使用按标量优先约定定义的四元数。有关四元数形式的更多信息，请参阅算法。
