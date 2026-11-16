---
type: simulink-block
title: 'Radians to Degrees'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'radianstodegrees'
documentation_source_path: '../simulink/ref_extras/radianstodegrees.html'
language: zh-CN
chinese_source: official
---

# Radians to Degrees

## 端口

### 输入

### **Port\_1** — 以弧度表示的输入角度 标量

以弧度为单位指定角度的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — 以度为单位的输出角度 标量

输出信号（指定转换为度数的角度）。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Extras / Transformations

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2008b 中推出**

## 描述

将弧度转换为度

Radians to Degrees 模块根据以弧度表示的输入角度计算以度表示的输出角度。

*degrees* = (180/ *n*) × *radians*

*degrees* 是以度为单位的角度，*radians* 是以弧度为单位的角度。
