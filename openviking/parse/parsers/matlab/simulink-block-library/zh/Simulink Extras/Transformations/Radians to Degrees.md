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
chinese_source: worker-translation
---

# Radians to Degrees

## 端口

### 输入

### **Port\_1** — 以弧度表示的输入角度 标量

指定以弧度表示的角度的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — 以度表示的输出角度 标量

指定转换为度的角度的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

R2025b 中未记录。

## 所属库

Simulink Extras / Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2008b 中引入**

## 描述

将弧度转换为度

Radians to Degrees 模块根据以弧度表示的输入角度计算以度表示的输出角度。

*degrees* = (180/ *n* ) ×
*radians*

*degrees* 是以度表示的角度，*radians* 是以弧度表示的角度。
