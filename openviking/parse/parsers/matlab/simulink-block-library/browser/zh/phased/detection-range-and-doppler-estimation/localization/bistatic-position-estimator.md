---
type: simulink-block
title: 'Bistatic Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Localization'
documentation_page: 'bistaticpositionestimator'
documentation_source_path: 'ref/bistaticpositionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Bistatic Position Estimator

## 端口

### 输入

### **RngEst** — 距离测量 (meters) 实值 1-by-*K* 向量 | 实值 *J*-by-*L* 矩阵

双基地距离或距离和测量，指定为实值 *1*-by-*K* 向量或实值 *J*-by-*L* 矩阵。

- 当 **RngEst** 为实值 *J*-by-*L* 矩阵时，该测量表示在 *J* 个发射锚点和 *L* 个接收锚点处测量的双基地距离或距离和测量。
- 当 **RngEst** 为实值 1-by-*K* 向量时，该测量表示在针对 *K* 个目标的一个发射锚点和一个接收锚点处测量的双基地距离或距离和测量。

单位是 meters。

**示例：** `[1000 2000]`

**数据类型：** `single` | `double`

### **AngEst** — 到达角估计 (degrees) 实值 1-by-*L* 行向量 | 实值 2-by-*L* 矩阵

- 当 **RngEst** 为实值 *J*-by-*L* 矩阵时，**AngEst** 应为实值长度为 *L* 的行向量或 2-by-*L* 矩阵。当 **AngEst** 为行向量时，它表示在 *L* 个接收锚点处测量的方位角。当 **AngEst** 为矩阵时，其第一行表示方位角，第二行表示在 *L* 个接收锚点处测量的仰角。
- 当 **RngEst** 为实值 1-by-*K* 向量时，**AngEst** 应为实值 *K* 元素行向量或 2-by-*K* 矩阵。

**示例：** `[10 20]`

**数据类型：** `single` | `double`

### **RngVar** — 距离方差 (meters-squared) 正实值 *J*-by-*L* 矩阵 | 正实值长度为 *K* 的行向量

距离方差，指定为正实值 *J*-by-*L* 矩阵或正实值长度为 *K* 的行向量。当 **RngVar** 为空时，方差估计未知，并且对所有目标设置为 1。

- 当 **RngVar** 为 *J*-by-*L* 时，它表示在 *J*-*L* 个锚点对处测量的一个目标的双基地距离或距离和估计的方差。当 **RngVar** 为空时，方差估计未知，并且对所有锚点对设置为 1。单位是 meters-squared。
- 当 **RngVar** 为长度为 K 的向量时，它表示在一个锚点对处测量的 *K* 个目标的双基地距离或距离和估计的方差。

**示例：** `[10 15]`

#### 依赖关系

要启用此端口，请选中 **Enable known variance input** 复选框。

**数据类型：** `single` | `double`

### **AngVar** — 角度方差 (degrees-squared) 实值 1-by-*L* 行向量 | 实值 2-by-*L* 矩阵

角度测量方差，指定为空、实值 1-by-*L* 行向量或正实值 2-by-*L* 矩阵。当 **AngVar** 为向量时，它表示在 *L* 个接收锚点处测量的一个目标的方位角方差估计。当 **AngVar** 为矩阵时，它表示在 *L* 个接收锚点处测量的一个目标的角度方差估计。当 **AngVar** 为空时，方差估计未知，并且对所有 *L* 个接收锚点设置为 1。当测量准确时，我们可以将对应方差设置为空。

**示例：** `[.10 .15]`

#### 依赖关系

要启用此端口，请选中 **Enable known variance input** 复选框。

**数据类型：** `single` | `double`

### **TxPos** — 发射锚点位置 (meters) 实值 *Q*-by-*J* 矩阵

发射锚点位置，指定为实值 *Q*-by-*J* 矩阵。*J* 是发射锚点的数量。每列表示一个不同锚点的位置。位置可以是二维或三维的。对于二维位置，*Q=2*；对于三维位置，*Q=3*。**TxPos** 的第 *j* 列表示第 *j* 个发射机在 *Q* 维笛卡尔空间中的位置。单位是 meters。

**示例：** `[20 31 –16; 13 64 –44]`

**数据类型：** `single` | `double`

### **RxPos** — 接收锚点位置 (meters) 实值 *Q*-by-*L* 矩阵

接收锚点位置，指定为实值 *Q*-by-*L* 矩阵。*L* 是接收锚点的数量。每列表示一个不同锚点的位置。位置可以是二维或三维的。对于二维位置，*Q*=2；对于三维位置，*Q*=3。**RxPos** 的第 *l* 列表示第 *l* 个接收机在 *Q* 维笛卡尔空间中的位置。单位是 meters。

**示例：** `[20 31 –16; 13 64 –44]`

**数据类型：** `single` | `double`

### 输出

### **TgtPosEst** — 目标位置估计 (meters) 实值 *Q*-by-1 向量

目标位置估计，返回为实值 *Q*-by-1 向量或实值 *Q*-by-*K* 矩阵，表示估计的 *K* 个目标位置。单位是 meters。

**数据类型：** `single` | `double`

### **TgtPosCov** — 估计的目标位置协方差 (meters-squared) 实值 *Q*-by-*Q* 矩阵 | 实值 *Q*-by-*Q*-by-*K* 数组

当输入包含 *JL* 个锚点对且有一个目标时，`tgtposcov` 是 *Q*-by-*Q* 矩阵，它是一个实正半定对称矩阵，表示估计的目标位置协方差。当输入包含 1 个锚点对且有 *K* 个目标时，`tgtposcov` 是 *Q*-by-*Q*-by-*K* 数组，其中每页是一个实值正半定对称矩阵，表示估计的目标位置协方差。单位是 meters-squared。

#### 依赖关系

要启用此端口，请选中 **Output covariances of position estimates** 复选框。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Range Measurement** — 距离测量类型 **Bistatic range** (默认) | **Range sum**

距离测量类型，指定为 **Bistatic range** 或 **Range sum**。双基地距离是距离和减去基线距离。当选择 **Bistatic range** 时，目标位置估计使用双基地距离和 AOA 测量。当选择 **Range sum** 时，目标位置估计使用距离和与 AOA 测量。

### **Enable known variance input** — 启用已知方差输入 on (默认) | off

选中此复选框以允许来自 **RngVar** 和 **AngVar** 端口的输入。

### **Output covariances of position estimates** — 输出位置估计协方差 off (默认) | on

选中此复选框以从 **TgtPosCov** 端口输出位置协方差估计。

**数据类型：** `single` | `double`

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用双基地距离和角度测量估计目标位置

Bistatic Position Estimator 模块根据带有已知锚点位置的双基地距离或距离和测量估计目标位置。
