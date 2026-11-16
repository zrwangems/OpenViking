---
type: simulink-block
title: 'Cartesian to Spherical'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'cartesiantospherical'
documentation_source_path: '../simulink/ref_extras/cartesiantospherical.html'
language: zh-CN
chinese_source: official
---

# Cartesian to Spherical

## 端口

### 输入

### **Port\_1** — *x* 笛卡尔坐标输入 标量

输入信号指定笛卡尔坐标 *(x,y,z)* 中的 *x* 值。所有输入必须是同一数据类型的实标量。

**数据类型:** `single` | `double`

### **Port\_2** — *y* 笛卡尔坐标输入 标量

输入信号指定笛卡尔坐标 *(x,y,z)* 中的 *y* 值。所有输入必须是同一数据类型的实标量。

**数据类型:** `single` | `double`

### **Port\_3** — *z* 笛卡尔坐标输入 标量

输入信号指定笛卡尔坐标 *(x,y,z)* 中的 *z* 值。所有输入必须是同一数据类型的实标量。

**数据类型:** `single` | `double`
### 输出

### **Port\_1** — *r* 球面坐标输出 标量

输出信号指定球面坐标 *(r,theta,phi)* 的 *r* 坐标。

**数据类型:** `single` | `double`

### **Port\_2** — *theta* 球面坐标输出 标量

输出信号指定球面坐标 *(r,theta,phi)* 的 *theta* 坐标。

**数据类型:** `single` | `double`

### **Port\_3** — *phi* 球面坐标输出 标量

输出信号指定球面坐标 *(r,theta,phi)* 的 *phi* 坐标。

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

笛卡尔坐标转球坐标

Cartesian to Spherical 模块将笛卡尔坐标（*x*、*y*、*z*）转换为球面坐标（*r*、*theta*、*phi*）。

第一个输入是 *x*，第二个输入是 *y*，第三个输入是 *z*。第一个输出是 *r*，第二个输出是 *theta*，第三个输出是 *phi*。角度 *theta* 和 *phi* 以弧度为单位。

笛卡尔坐标 (*x*, *y*, *z*) 描述点 *P* 相对于 *x* 轴、*y* 轴和 *z* 轴的坐标。球面坐标 *r*  是从原点到点 *P* 的线的长度。球面坐标 *theta*（方位角）是从正 *x* 轴到在 *x*-*y* 平面中从原点到 *P* 的线的投影所测量的角度（以弧度为单位）。球面坐标 *phi*（天顶）是从正 *z* 轴到从原点到 *P* 的线的角度，以弧度为单位。

**注意**

MATLAB® 函数 `cart2sph` 从 *x*-*y* 平面测量 *phi*。

r=x2+y2+z2theta=arctan(yx)phi=arctan(x2+y2z)

**注意**

球面坐标的符号在其他参考文献中可能有所不同。有时，*theta*  和 *phi* 的顺序会颠倒。有时，*theta* 表示天顶，*phi* 表示方位角。
