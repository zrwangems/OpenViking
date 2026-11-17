---
type: simulink-block
title: 'Vector Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'vectorcontrolreference'
documentation_source_path: 'ref/vectorcontrolreference.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Control Reference

## 端口
```yaml
ports:
- name: magref
  summary: 参考矢量幅值 标量
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: 参考矢量电角度位置 标量
  direction: input
  data_types: single | double | fixed point
- name: dref
  summary: 参考矢量的 *d* 轴分量 标量
  direction: output
  data_types: single | double | fixed point
- name: qref
  summary: 参考矢量的 *q* 轴分量 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **magref** — 参考矢量幅值 标量

作为模块输入提供的参考电压、电流或磁链矢量的幅值。

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 参考矢量电角度位置 标量

作为模块输入提供的参考电压、电流或磁链矢量的电角度位置。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **dref** — 参考矢量的 *d* 轴分量 标量

参考电压、电流或磁链矢量沿旋转 *dq* 参考坐标系直轴的分量。

**数据类型：** `single` | `double` | `fixed point`

### **qref** — 参考矢量的 *q* 轴分量 标量

参考电压、电流或磁链矢量沿旋转 *dq* 参考坐标系交轴的分量。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Alpha (phase-a) axis alignment
  summary: '*dq* 参考坐标系对齐方式 D-axis（默认） | Q-axis'
  group: ''
- name: Theta units
  summary: 输入位置值的单位 Per-unit（默认） | Radians | Degrees
  group: ''
- name: Number of data points for trigonometric lookup table
  summary: 查找表数组大小 1024（默认） | 标量
  group: ''
```

### **Alpha (phase-a) axis alignment** — *dq* 参考坐标系对齐方式 `D-axis`（默认） | `Q-axis`

将旋转参考坐标系的 *d* 轴或 *q* 轴与静止参考坐标系的 *α* 轴对齐。

### **Theta units** — 输入位置值的单位 `Per-unit`（默认） | `Radians` | `Degrees`

参考电压、电流或磁链矢量输入电角度位置的单位。

### **Number of data points for trigonometric lookup table** — 查找表数组大小 `1024`（默认） | 标量

查找表数组的大小。
## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算参考矢量的 d 轴和 q 轴分量

Vector Control Reference 模块计算作为模块输入提供的参考电压、电流或磁链矢量的 *d* 轴和 *q* 轴分量。

该模块接受参考矢量的幅值和位置作为输入。模块输出参考矢量沿旋转 *dq* 参考坐标系直轴和交轴的分量。

### 方程

该模块使用以下方程计算 *d* 轴和 *q* 轴矢量分量输出。

dref=magref×cosθe

qref=magref×sinθe

其中：

- dref 是参考矢量的 *d* 轴分量。
- qref 是参考矢量的 *q* 轴分量。
- magref 是参考矢量的幅值。
- θe 是参考矢量的电角度位置。
