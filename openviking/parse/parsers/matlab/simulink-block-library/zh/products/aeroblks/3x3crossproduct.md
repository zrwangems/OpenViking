---
type: simulink-block
title: '3x3 Cross Product'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: '3x3crossproduct'
documentation_source_path: '3x3crossproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# 3x3 Cross Product

## 端口

### 输入

### **A** — 第一个叉积输入 3×1 向量

第一个叉积输入，指定为向量。

**示例：** `[10 2 3]`

**数据类型：** `double`

### **B** — 第二个叉积输入 3×1 向量

第二个叉积输入，指定为向量。

**示例：** `[10 2 3]`

**数据类型：** `double`
### 输出

### **C** — 叉积 3×1 向量

叉积，输出为向量。

**数据类型：** `double`

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

**R2006a 之前引入**

## 描述

计算两个 3×1 向量的叉积

3x3 Cross Product 模块计算两个向量 *A* 和 *B* 的叉积（或向量积）。该模块生成第三个向量 *C*，其方向垂直于包含 *A* 和 *B* 的平面，大小等于 *A* 和 *B* 的长度之积乘以它们之间夹角的正弦。*C* 的方向遵循从 *A* 转向 *B* 的右手定则。相关方程，请参阅算法。
