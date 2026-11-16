---
type: simulink-block
title: 'PMSM Field-Weakening Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmfieldweakeningcontroller'
documentation_source_path: 'ref/pmsmfieldweakeningcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Field-Weakening Controller

## 端口

### 输入

### **idqRef** — 参考电流矢量

用于控制永磁同步电机的期望 *d* 轴和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **vdq** — 电压矢量

永磁同步电机的直轴和交轴电压，单位为 V。

**数据类型：** `single` | `double`

### **VphMax** — 最大相电压标量

每相最大允许电压，单位为 V。

**数据类型：** `single` | `double`
### 输出

### **idqRefFW** — 弱磁参考电流矢量

弱磁参考直轴和交轴电流，单位为 A。

**数据类型：** `single` | `double`

## 参数

### **调制指数阈值** — 调制指数阈值 `1`（默认）| 正数

参考调制指数。

### **弱磁控制器积分增益** — 积分增益 `100`（默认）| 正数

弱磁控制器的积分器增益。

### **积分抗饱和增益** — 抗饱和增益 `10`（默认）| 正数

弱磁控制器的抗饱和增益。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `-1` 或正数

用于模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 `-1`。如果在连续变步长模型中使用此模块，请显式设置采样时间。

## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

永磁同步电机弱磁控制器

PMSM Field-Weakening Controller 模块实现用于永磁同步电机（PMSM）的弱磁控制器。

使用此模块对电流控制的 PMSM 施加相电压约束。当电压矢量幅值超过其限制时，模块通过调整参考电流矢量的角度来降低 PMSM 相电压。模块不调整电流矢量的幅值。

您可以将此模块用作 PMSM 控制系统的一部分：

- 使用零 *d* 轴控制技术生成用于驱动 PMSM 的无约束电流参考矢量。您可以使用 PMSM Current Reference Generator 模块实现此策略。
- 使用此模块调整电流参考矢量的角度，以满足电压相位约束。
- 使用 PMSM Current Controller 生成用于驱动 PMSM 的电压参考矢量。

### 方程

内部积分控制器输出因子 *β∈[0,1]*，该因子由所需定子电压在任意时刻接近饱和电压值的程度决定：

- 当所需定子电压超过限制时，*β* 趋于 0，从而减小 *q* 轴电流。
- 当所需定子电压在其限制范围内时，*β* 趋于 1，且角度保持不变。

此图显示了弱磁控制器的结构。

在图中，您将调制指数阈值 *Mth* 作为输入参数提供给模块，模块将调制指数 *M* 计算为实际相电压与最大可用相电压 *Vph\_max* 之比：

M = √(vd^2 + vq^2) / Vph\_max,

其中 *vd* 和 *vq* 是电压矢量的 *d* 轴和 *q* 轴分量。
