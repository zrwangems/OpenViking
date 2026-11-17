---
type: simulink-block
title: 'Spherical to Cartesian'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'sphericaltocartesian'
documentation_source_path: '../simulink/ref_extras/sphericaltocartesian.html'
language: zh-CN
chinese_source: worker-translation
---

# Spherical to Cartesian

## 端口

### 输入

### **Port\_1** — *r* 球坐标输入标量

指定球坐标 *(r,theta,phi)* 中 *r* 坐标的输入信号。所有输入必须是相同数据类型的实数标量。

**数据类型：** `single` | `double`

### **Port\_2** — *theta* 球坐标输入标量

指定球坐标 *(r,theta,phi)* 中 *r* 坐标的输入信号。所有输入必须是相同数据类型的实数标量。

**数据类型：** `single` | `double`

### **Port\_3** — *phi* 球坐标输入标量

指定球坐标 *(r,theta,phi)* 中 *r* 坐标的输入信号。所有输入必须是相同数据类型的实数标量。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — *x* 笛卡尔坐标输出标量

指定笛卡尔坐标 *(x,y,z)* 中 *x* 值的输出信号。

**数据类型：** `single` | `double`

### **Port\_2** — *y* 笛卡尔坐标输出标量

指定笛卡尔坐标 *(x,y,z)* 中 *x* 值的输出信号。

**数据类型：** `single` | `double`

### **Port\_3** — *z* 笛卡尔坐标输出标量

指定笛卡尔坐标 *(x,y,z)* 中 *x* 值的输出信号。

**数据类型：** `single` | `double`

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

将球坐标变换为笛卡尔坐标

Spherical to Cartesian 模块将球坐标 *(r*, *theta*, *phi*) 变换为笛卡尔坐标 (*x*, *y*, *z*)。

第一个输入是 *r*，第二个输入是 *theta*，第三个输入是 *phi*。角度 *theta* 和 *phi* 以弧度为单位。第一个输出是 *x*，第二个输出是 *y*，第三个输出是 *z*。

球坐标 *r* 是从原点到点 *P* 的线段长度。球坐标 *theta*（方位角）是从正 x 轴到从原点到 *P* 的线段在 *x*-*y* 平面上的投影所测得的弧度角。球坐标 *phi*（天顶角）是从正 *z* 轴到从原点到 *P* 的线段所测得的弧度角。笛卡尔坐标 (*x*, *y*, *z*) 描述点 *P* 相对于 *x* 轴、*y* 轴和 *z* 轴的位置。

**注意**

MATLAB® 函数 `cart2sph` 从 *x*-*y* 平面测量 *phi*。

*x* = *r* ×
sin(*phi*) ×
cos(*theta*)

*y* = *r* ×
sin(*phi*) ×
sin(*theta*)

*z* = *r* ×
cos(*phi*)

**注意**

球坐标的记法可能与其他参考文献中使用的记法不同。有时，*theta* 和 *phi* 的顺序是相反的。有时，*theta* 表示天顶角，*phi* 表示方位角。
