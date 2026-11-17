---
type: simulink-block
title: 'PMSM Torque Estimator'
family: 'control'
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

### 输入

### **idq** — 定子电流向量

PMSM 的定子直轴和交轴电流，单位为 A。

**数据类型：** `single` | `double`
### 输出

### **TqEst** — 转矩估计标量

PMSM 的机械转矩估计值，单位为 N\*m。

**数据类型：** `single` | `double`

## 参数

### **电机参数** — 参数选择策略 `Constant parameters` （默认） | `Lookup table based parameters`

指定电机参数的类型，可采用常量值或表格数据形式。

### **极对数** — 极对数 `8` （默认） | 正整数

转子上的永磁体极对数。

### **D 轴电流向量，id (A)** — D 轴电流断点向量 `[-200,0,200]``A` （默认） | 单调递增向量

用于参数确定查找表的直轴电流向量。

### **Q 轴电流向量，iq (A)** — Q 轴电流断点向量 `[-200,0,200]``A` （默认） | 单调递增向量

用于参数确定查找表的交轴电流向量。

### **Ld 矩阵，Ld(id,iq) (H)** — D 轴电感查找数据 `0.0002 * ones(3, 3)``H` （默认） | 正矩阵

用作查找表数据的 *Ld* 矩阵。

### **Lq 矩阵，Lq(id,iq) (H)** — Q 轴电感查找数据 `0.0002 * ones(3, 3)``H` （默认） | 正矩阵

用作查找表数据的 *Lq* 矩阵。

### **永磁体磁链矩阵，PM(id,iq) (Wb)** — 磁链查找数据 `0.04 * ones(3, 3)``Wb` （默认） | 实数矩阵

查找表中使用的永磁体磁链矩阵。

### **D 轴电感 (H)** — d 轴电感 `0.0002` （默认） | 正标量

直轴电感。

### **Q 轴电感 (H)** — q 轴电感 `0.0002` （默认） | 正标量

交轴电感。

### **永磁体磁链 (Wb)** — PM 磁链 `0.04``Wb` （默认） | 正标量

峰值永磁体磁链。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1` （默认） | `-1` 或正数

模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 `-1`。如果在连续可变步长模型中使用此模块，请显式设置采样时间。

## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2017b 中引入**

## 描述

估计永磁同步电机转矩

PMSM Torque Estimator 模块为永磁同步电机（PMSM）实现转矩估计器。

当电机的机械转矩无法直接测量时，可使用此模块进行估计。该模块使用已知的电机参数以及 *dq0* 参考坐标系中测得的相电流向量来估计转矩。

使用 Park Transform 模块将 *abc* 参考坐标系中测得的相电流向量转换为 *dq0* 参考坐标系。

### 方程

该模块使用 *d*-*q* 转子参考坐标系中的转矩方程来估计 PMSM 的机械转矩 *Te*：

Te=3p2(ψmiq+(Ld−Lq)idiq),

其中

- *p* 是 PMSM 的极对数。
- *ψm* 是永磁体的磁链。
- *Ld* 和 *Lq* 是 PMSM 的 *d* 轴和 *q* 轴电感。
- *id* 和 *iq* 是 PMSM 的 *d* 轴和 *q* 轴电流。

在实践中，电机参数并非恒定不变，而是取决于一些物理现象。您可以选择将这些参数简单地定义为常量，或者更真实地通过查找表将其定义为电流的函数。

### 假设

电机参数已知。
