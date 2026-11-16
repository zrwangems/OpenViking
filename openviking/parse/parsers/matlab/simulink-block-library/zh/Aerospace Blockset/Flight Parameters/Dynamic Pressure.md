---
type: simulink-block
title: 'Dynamic Pressure'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'dynamicpressure'
documentation_source_path: 'dynamicpressure.html'
language: zh-CN
chinese_source: worker-translation
---

# Dynamic Pressure

## 端口

### 输入

### **V** — 速度三元素向量

速度，指定为三元素向量。

**数据类型：** `double`

### **ρ** — 空气密度标量

空气密度，指定为标量。

**数据类型：** `double`

### 输出

### **Output 1** — 动压标量

动压，以标量形式返回。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用速度和空气密度计算动压

Dynamic Pressure 模块计算动压。

动压定义为：

q¯=12ρV2,

其中 ρ 是空气密度，*V* 是速度。
