---
type: simulink-block
title: 'Cartesian to Polar'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'cartesiantopolar'
documentation_source_path: '../simulink/ref_extras/cartesiantopolar.html'
language: zh-CN
chinese_source: official
---

# Cartesian to Polar

## 端口

### 输入

### **Port\_1** — *x* 笛卡尔坐标输入 标量

输入信号指定笛卡尔坐标 *(x,y)* 中的 *x* 值。两个输入必须是同一数据类型的实数标量。

**数据类型:** `single` | `double`

### **Port\_2** — *y* 笛卡尔坐标输入 标量

输入信号指定笛卡尔坐标 *(x,y)* 中的 *y* 值。两个输入必须是同一数据类型的实数标量。

**数据类型:** `single` | `double`
### 输出

### **Port\_1** — *r* 极坐标输出 标量

输出信号指定极坐标 *(r,theta)* 的 *r* 坐标。

**数据类型:** `single` | `double`

### **Output 2** — *theta* 极坐标输出 标量

输出信号指定极坐标 *(r,theta)* 的 *theta* 坐标。

**数据类型:** `single` | `double`

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

笛卡尔坐标转极坐标

Cartesian to Polar 模块将笛卡尔坐标（*x*、*y*）转换为极坐标（*r*、*theta*）。

第一个和第二个输入分别对应于 *x* 和 *y*。第一个和第二个输出分别对应于 *r* 和 *theta*。角度 *theta* 以弧度为单位。

笛卡尔坐标 (*x*, *y*) 描述相对于 *x* 轴和 *y* 轴的点。极坐标（*r*、*theta*）描述同一个点，其中 *r* 是距原点的距离，*theta* 是从正 *x* 轴逆时针旋转的弧度角。

r=x2+y2theta=arctan(yx)
