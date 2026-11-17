---
type: simulink-block
title: 'Polar to Cartesian'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'polartocartesian'
documentation_source_path: '../simulink/ref_extras/polartocartesian.html'
language: zh-CN
chinese_source: worker-translation
---

# Polar to Cartesian

## 端口
```yaml
ports:
- name: Port_1
  summary: '*r* 极坐标输入标量'
  direction: input
  data_types: single | double
- name: Port_2
  summary: '*theta* 极坐标输入标量'
  direction: input
  data_types: single | double
- name: Port_1
  summary: '*x* 坐标输出标量'
  direction: output
  data_types: single | double
- name: Port_2
  summary: '*y* 笛卡尔坐标输出标量'
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — *r* 极坐标输入标量

指定极坐标 *(r,theta)* 中 *r* 坐标的输入信号。两个输入必须是相同数据类型的实数标量。

**数据类型：** `single` | `double`

### **Port\_2** — *theta* 极坐标输入标量

指定极坐标 *(r,theta)* 中 *theta* 坐标的输入信号。两个输入必须是相同数据类型的实数标量。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — *x* 坐标输出标量

指定笛卡尔坐标 *(x,y)* 中 *x* 值的输出信号。

**数据类型：** `single` | `double`

### **Port\_2** — *y* 笛卡尔坐标输出标量

指定笛卡尔坐标 *(x,y)* 中 *y* 值的输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters: []
```

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

将极坐标转换为笛卡尔坐标

Polar to Cartesian 模块将极坐标 (*r*, *theta*) 变换为笛卡尔坐标 (*x*, *y*)。

第一个和第二个输入分别对应于 *r* 和 *theta*。角度 *theta* 以弧度为单位。第一个和第二个输出分别对应于 *x* 和 *y*。

极坐标 (*r*, *theta*) 描述一个点，其中 *r* 是到原点的距离，*theta* 是从正 *x* 轴逆时针方向的角度（以弧度为单位）。笛卡尔坐标 (*x*, *y*) 描述相对于 *x* 轴和 *y* 轴的同一个点。

*x* = *r* × cos(*theta*)

*y* = *r* × sin(*theta*)
