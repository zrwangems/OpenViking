---
type: simulink-block
title: 'Degrees to Radians'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'degreestoradians'
documentation_source_path: '../simulink/ref_extras/degreestoradians.html'
language: zh-CN
chinese_source: worker-translation
---

# Degrees to Radians

## 端口
```yaml
ports:
- name: Port_1
  summary: 以度数为单位的输入角度 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: 以弧度为单位的输出角度 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### 输入

### **Port\_1** — 以度数为单位的输入角度 标量

指定以度数为单位的输入角度的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — 以弧度为单位的输出角度 标量

指定以弧度为单位的角度的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
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

将度数转换为弧度

Degrees to Radians 模块根据以度数为单位的输入角度计算以弧度为单位的输出角度。

*radians*  = (*n*/180) ×
*degrees*

*radians* 是以弧度为单位的角度，*degrees* 是以度数为单位的角度。
