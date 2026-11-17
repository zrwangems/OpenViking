---
type: simulink-block
title: 'PMSM Torque Estimator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmtorqueestimator'
documentation_source_path: 'ref/pmsmtorqueestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Torque Estimator

## 端口
```yaml
ports:
- name: idq
  summary: 定子电流向量
  direction: input
  data_types: single | double
- name: TqEst
  summary: 转矩估计标量
  direction: output
  data_types: single | double
```

### 输入

### **idq** — 定子电流向量

PMSM 的定子直轴和交轴电流，单位为 A。

**数据类型：** `single` | `double`
### 输出

### **TqEst** — 转矩估计标量

PMSM 的估计机械转矩值，单位为 N\*m。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Machine parameters
  summary: 参数选择策略 Constant parameters（默认）| Lookup table based parameters
  group: ''
- name: Number of pole pairs
  summary: 极对数 8（默认）| 正整数
  group: ''
- name: D-axis current vector, id (A)
  summary: 直轴电流断点向量 [-200,0,200]A（默认）| 单调递增向量
  group: ''
- name: Q-axis current vector, iq (A)
  summary: 交轴电流断点向量 [-200,0,200]A（默认）| 单调递增向量
  group: ''
- name: Ld matrix, Ld(id,iq) (H)
  summary: 直轴电感查找数据 0.0002 * ones(3, 3)H（默认）| 正矩阵
  group: ''
- name: Lq matrix, Lq(id,iq) (H)
  summary: 交轴电感查找数据 0.0002 * ones(3, 3)H（默认）| 正矩阵
  group: ''
- name: Permanent magnet flux linkage matrix, PM(id,iq) (Wb)
  summary: 磁链查找数据 0.04 * ones(3, 3)Wb（默认）| 实矩阵
  group: ''
- name: D-axis inductance (H)
  summary: 直轴电感 0.0002（默认）| 正标量
  group: ''
- name: Q-axis inductance (H)
  summary: 交轴电感 0.0002（默认）| 正标量
  group: ''
- name: Permanent magnet flux linkage (Wb)
  summary: 永磁体磁链 0.04Wb（默认）| 正标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| -1 或正数
  group: ''
```

### **Machine parameters** — 参数选择策略 `Constant parameters`（默认）| `Lookup table based parameters`

指定电机参数的类型，可以是常量值或表格数据的形式。

### **Number of pole pairs** — 极对数 `8`（默认）| 正整数

转子上永磁体的极对数。

### **D-axis current vector, id (A)** — 直轴电流断点向量 `[-200,0,200]``A`（默认）| 单调递增向量

用于参数确定查找表的直轴电流向量。

### **Q-axis current vector, iq (A)** — 交轴电流断点向量 `[-200,0,200]``A`（默认）| 单调递增向量

用于参数确定查找表的交轴电流向量。

### **Ld matrix, Ld(id,iq) (H)** — 直轴电感查找数据 `0.0002 * ones(3, 3)``H`（默认）| 正矩阵

用作查找表数据的 *Ld* 矩阵。

### **Lq matrix, Lq(id,iq) (H)** — 交轴电感查找数据 `0.0002 * ones(3, 3)``H`（默认）| 正矩阵

用作查找表数据的 *Lq* 矩阵。

### **Permanent magnet flux linkage matrix, PM(id,iq) (Wb)** — 磁链查找数据 `0.04 * ones(3, 3)``Wb`（默认）| 实矩阵

查找表中使用的永磁体磁链矩阵。

### **D-axis inductance (H)** — 直轴电感 `0.0002`（默认）| 正标量

直轴电感。

### **Q-axis inductance (H)** — 交轴电感 `0.0002`（默认）| 正标量

交轴电感。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `0.04``Wb`（默认）| 正标量

峰值永磁体磁链。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `-1` 或正数

模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 `-1`。如果在连续变步长模型中使用此模块，请显式设置采样时间。
## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

估计永磁同步电机转矩

PMSM Torque Estimator 模块实现了永磁同步电机（PMSM）的转矩估计器。

当电机的机械转矩无法直接测量时，可使用此模块进行估计。该模块使用已知的电机参数和 *dq0* 参考坐标系中测得的相电流向量来估计转矩。

使用 Park Transform 模块将 *abc* 参考坐标系中测得的相电流向量转换为 *dq0* 参考坐标系。

### 方程

该模块使用 *d*-*q* 转子参考坐标系中的转矩方程来估计 PMSM 的机械转矩 *Te*：

Te=3p2(ψmiq+(Ld−Lq)idiq)，

其中

- *p* 是 PMSM 的极对数。
- *ψm* 是永磁体的磁链。
- *Ld* 和 *Lq* 是 PMSM 的 *d* 轴和 *q* 轴电感。
- *id* 和 *iq* 是 PMSM 的 *d* 轴和 *q* 轴电流。

在实践中，电机参数并非恒定值，而是取决于某些物理现象。您可以选择将这些参数简单地定义为常量，或者更实际地，通过使用查找表将其定义为电流的函数。

### 假设

电机参数已知。
