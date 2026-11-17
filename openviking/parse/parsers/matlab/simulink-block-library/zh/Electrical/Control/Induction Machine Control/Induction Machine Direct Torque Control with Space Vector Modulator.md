---
type: simulink-block
title: 'Induction Machine Direct Torque Control with Space Vector Modulator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrolwithspacevectormodulator'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrolwithspacevectormodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Direct Torque Control with Space Vector Modulator

## 端口

### 输入

### **FluxRef** — 磁链标量

参考定子磁链。

**数据类型：** `single` | `double`

### **TqRef** — 转矩标量

参考转矩。

**数据类型：** `single` | `double`

### **vabc** — 电压矢量

定子相电压。

**数据类型：** `single` | `double`

### **iabc** — 电流矢量

定子相电流。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压信号标量

变换器的直流母线电压。

**数据类型：** `single` | `double`

### **Reset** — 控制器复位标量

PI 控制器积分器的复位。

**数据类型：** `single` | `double`
### 输出

### **G** — 门极脉冲矢量 | `0` 或 `1`

逆变器门极脉冲。该模块不考虑任何死区时间。

**数据类型：** `single` | `double`

### **ModWave** — 调制波矢量

如果为具有 PWM 能力的硬件平台生成代码，则部署到硬件的调制波。否则，此数据仅供您参考。

## 参数

### 常规

### **Stator resistance (Ohm)** — 电阻 `0.25`（默认）| 正标量

电机定子电阻。

### **Number of pole pairs** — 极对数 `1`（默认）| 正整数

电机极对数。

### **Inverter dc-link voltage threshold (V)** — 电压 `300`（默认）| 正标量

激活功率逆变器的电压阈值。

### **Fundamental sample time (s)** — SVM 采样时间 `5e-6`（默认）| 小于控制采样时间的正标量

空间矢量调制器的采样时间。基本采样时间必须小于控制采样时间。

### **Control sample time (s)** — PI 采样时间 `5e-5`（默认）| 大于基本采样时间的正标量

PI 控制器的采样时间。控制采样时间必须大于基本采样时间。

### **Switching frequency (Hz)** — 开关频率 `1000`（默认）| 正标量

指定功率变换器中开关的期望开关速率。

### 控制参数

### **Flux controller proportional gain** — 磁链 PI 比例增益 `150`（默认）| 正标量

磁链控制器的比例增益。

### **Flux controller integral gain** — 磁链 PI 积分增益 `3000`（默认）| 正标量

磁链控制器的积分增益。

### **Flux controller anti-windup gain** — 磁链 PI 抗饱和增益 `1`（默认）| 正标量

磁链控制器的抗饱和增益。

### **Torque controller proportional gain** — 转矩 PI 比例增益 `1`（默认）| 正标量

转矩控制器的比例增益。

### **Torque controller integral gain** — 转矩 PI 积分增益 `50`（默认）| 正标量

转矩控制器的积分增益。

### **Torque controller anti-windup gain** — 转矩 PI 抗饱和增益 `1`（默认）| 正标量

转矩控制器的抗饱和增益。

### **Axis prioritization** — 电压限制器的轴优先级 `Q-axis`（默认）| `D-axis` | `D-Q equivalence`

当模块限制电压时，优先处理或维持 *d* 轴和 *q* 轴之间的比例。

## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带 SVM 的感应电机 DTC 结构

Induction Machine Direct Torque Control with Space Vector Modulator 模块实现了带空间矢量调制器（SVM）的感应电机直接转矩控制结构（DTC）。使用此模块可生成用于控制感应电机的逆变器门极脉冲。下图展示了该模块的架构。

图中：

- 您提供参考转矩 *T\** 和磁链 *ψ\**。
- Flux and Torque Estimator 根据测量的相电流 *iabc* 和电压 *vabc* 估算实际转矩 *T* 和磁链 *ψ*。
- 两个 PI 控制器分别根据磁链误差和转矩误差确定参考 *d* 轴和 *q* 轴电压 *vd* 和 *vq*。
- SVM 生成控制驱动感应电机的逆变器所需门极脉冲 *Gij*。下标 *i* 对应相（*a*、*b* 或 *c*）。下标 *j* 对应高电平 *H* 或低电平 *L* 信号。

### 磁链和转矩估算器

为估算转矩和磁链，该模块使用后向欧拉法在静止 *ɑβ* 参考坐标系中离散化电机电压方程。*ɑβ* 坐标系中定子磁链的离散时间方程为：

ψα=(vα−iαRs)Tszz−1

ψβ=(vβ−iβRs)Tszz−1

其中：

- *vɑ* 和 *vβ* 分别为 *ɑ* 轴和 *β* 轴电压。
- *iɑ* 和 *iβ* 分别为 *ɑ* 轴和 *β* 轴电流。
- *Ψɑ* 和 *Ψβ* 分别为 *ɑ* 轴和 *β* 轴定子磁链。
- *Rs* 为定子电阻。

该模块计算转矩和总定子磁链如下：

T=3p2(ψαiβ−ψβiα)

ψs=ψα2+ψβ2

其中：

- *p* 为极对数。
- *Ψs* 为总定子磁链。

### 空间矢量调制器

SVM 将期望电压转换为门极脉冲，用于控制逆变器。下图展示了三相逆变器的可能开关状态。

六边形表示空间矢量图。六个顶点分别表示三相逆变器的可能开关状态 *(GAH,GBH,GCH)*。每个低侧门极与其对应的高侧门极状态相反。逆变器图展示了当前状态。

空间矢量图中的旋转矢量对应复数参考电压矢量，该矢量以电机期望电气频率旋转。实际上，开关频率远快于该电气频率。因此，逆变器在其当前区域 *Ri* 的两个包围状态与对应 *(0,0,0)* 的零状态之间持续切换，以生成期望电压。

要了解此方法的实现，请参阅 PWM Generator (Three-phase, Two-level) 模块。
