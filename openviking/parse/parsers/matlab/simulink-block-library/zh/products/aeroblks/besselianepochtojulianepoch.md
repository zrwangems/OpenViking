---
type: simulink-block
title: 'Besselian Epoch to Julian Epoch'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Reference System Transformations'
documentation_page: 'besselianepochtojulianepoch'
documentation_source_path: 'besselianepochtojulianepoch.html'
language: zh-CN
chinese_source: worker-translation
---

# Besselian Epoch to Julian Epoch

## 端口

### 输入

### **rB1950** — 位置 3×1 向量

标准贝塞尔历元 (B1950) 中的位置，指定为 3×1 向量。

**数据类型：** `double`

### **vB1950** — 速度 3×1 向量

标准贝塞尔历元 (B1950) 中的速度，指定为 3×1 向量。

**数据类型：** `double`
### 输出

### **rJ2000** — 位置 3×1 向量

标准儒略历元 (J2000) 中的位置，返回为 3×1 向量。

**数据类型：** `double`

### **vJ2000** — 速度 3×1 向量

标准儒略历元 (J2000) 中的速度，返回为 3×1 向量。

**数据类型：** `double`

## 参数

在 R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

将位置和速度分量从已停用的标准贝塞尔历元 (B1950) 转换到标准儒略历元 (J2000)

Besselian Epoch to Julian Epoch 模块将贝塞尔历元位置 (r¯B1950) 和贝塞尔历元速度 (v¯B1950) 的两个 3×1 向量转换为儒略历元位置 (r¯J2000) 和儒略历元速度 (v¯J2000)。有关该变换的详细信息，请参阅算法。
