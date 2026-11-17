---
type: simulink-block
title: '6th Order Point Mass Forces (Coordinated Flight)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '6thorderpointmassforcescoordinatedflight'
documentation_source_path: '6thorderpointmassforcescoordinatedflight.html'
language: zh-CN
chinese_source: worker-translation
---

# 6th Order Point Mass Forces (Coordinated Flight)

## 端口
```yaml
ports:
- name: Lift
  summary: 升力 标量 | 数组
  direction: input
  data_types: double
- name: Drag
  summary: 阻力 标量 | 数组
  direction: input
  data_types: double
- name: Weight
  summary: 重力 标量 | 数组
  direction: input
  data_types: double
- name: Thrust
  summary: 推力 标量 | 数组
  direction: input
  data_types: double
- name: ɣ
  summary: 航迹角 标量 | 数组
  direction: input
  data_types: double
- name: μ
  summary: 滚转角 标量 | 数组
  direction: input
  data_types: double
- name: ɑ
  summary: 迎角 标量 | 数组
  direction: input
  data_types: double
- name: Fx
  summary: '*x* 轴方向的力 标量 | 数组'
  direction: output
  data_types: double
- name: Fy
  summary: '*y* 轴方向的力 标量 | 数组'
  direction: output
  data_types: double
- name: Fz
  summary: '*z* 轴方向的力 标量 | 数组'
  direction: output
  data_types: double
```

### 输入

### **Lift** — 升力 标量 | 数组

升力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **Drag** — 阻力 标量 | 数组

阻力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **Weight** — 重力 标量 | 数组

重力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **Thrust** — 推力 标量 | 数组

推力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **ɣ** — 航迹角 标量 | 数组

航迹角，指定为标量或数组，单位为弧度。

**数据类型：** `double`

### **μ** — 滚转角 标量 | 数组

滚转角，指定为标量或数组，单位为弧度。

**数据类型：** `double`

### **ɑ** — 迎角 标量 | 数组

迎角，指定为标量或数组，单位为弧度。

**数据类型：** `double`
### 输出

### **Fx** — *x* 轴方向的力 标量 | 数组

*x* 轴方向的力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **Fy** — *y* 轴方向的力 标量 | 数组

*y* 轴方向的力，指定为标量或数组，单位为力。

**数据类型：** `double`

### **Fz** — *z* 轴方向的力 标量 | 数组

*z* 轴方向的力，指定为标量或数组，单位为力。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算协调飞行中六阶点质量所使用的力

6th Order Point Mass Forces (Coordinated Flight) 模块计算单个点质量或多个点质量所施加的力。有关所施加力的系统的更多信息，请参阅算法。
