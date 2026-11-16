---
type: simulink-block
title: 'Celsius to Fahrenheit'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'celsiustofahrenheit'
documentation_source_path: '../simulink/ref_extras/celsiustofahrenheit.html'
language: zh-CN
chinese_source: worker-translation
---

# Celsius to Fahrenheit

## 端口

### 输入

### **Port\_1** — Celsius degree 输入标量

指定 Celsius degrees 的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — Fahrenheit degree 输出标量

指定 Fahrenheit degrees 的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

未在 R2025b 中记录。

## 所属库

Simulink Extras / Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2008b 中引入**

## 描述

将 degrees Celsius 转换为 degrees Fahrenheit

Celsius to Fahrenheit 模块根据以 degrees Celsius 为单位的输入温度计算以 degrees Fahrenheit 为单位的输出温度。

*T*F =
(9/5)*T*C + 32

*T*C 是以 degrees Celsius 为单位的温度，*T*F 是以 degrees Fahrenheit 为单位的温度。
