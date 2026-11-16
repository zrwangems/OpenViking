---
type: simulink-block
title: 'Create 3x3 Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: 'create3x3matrix'
documentation_source_path: 'create3x3matrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Create 3x3 Matrix

## 端口

### 输入

### **A11** — 矩阵的第一行、第一列矩阵元素

矩阵的第一行、第一列，指定为矩阵元素。

**示例:** 1

**数据类型:** `double`

### **A12** — 矩阵的第一行、第二列矩阵元素

矩阵的第一行、第二列，指定为矩阵元素。

**示例:** 2

**数据类型:** `double`

### **A13** — 矩阵的第一行、第三列矩阵元素

矩阵的第一行、第三列，指定为矩阵元素。

**示例:** 3

**数据类型:** `double`

### **A21** — 矩阵的第二行、第一列矩阵元素

矩阵的第二行、第一列，指定为矩阵元素。

**示例:** 4

**数据类型:** `double`

### **A22** — 矩阵的第二行、第二列矩阵元素

矩阵的第二行、第二列，指定为矩阵元素。

**示例:** 5

**数据类型:** `double`

### **A23** — 矩阵的第二行、第三列矩阵元素

矩阵的第二行、第三列，指定为矩阵元素。

**示例:** 6

**数据类型:** `double`

### **A31** — 矩阵的第三行、第一列矩阵元素

矩阵的第三行、第一列，指定为矩阵元素。

**示例:** 7

**数据类型:** `double`

### **A32** — 矩阵的第三行、第二列矩阵元素

矩阵的第三行、第二列，指定为矩阵元素。

**示例:** 8

**数据类型:** `double`

### **A33** — 矩阵的第三行、第三列矩阵元素

矩阵的第三行、第三列，指定为矩阵元素。

**示例:** 9

**数据类型:** `double`
### 输出

### **A** — 矩阵 3-by-3 矩阵

矩阵，输出为 3-by-3 矩阵。

**数据类型:** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

从九个输入值创建 3-by-3 矩阵

Create 3x3 Matrix 模块从九个输入值创建 3-by-3 矩阵，其中每个输入对应矩阵的一个元素。

输出矩阵的形式为

A=[A11A12A13A21A22A23A31A32A33]
