---
type: simulink-block
title: 'Induction Machine Direct Torque Control with Space Vector Modulator'
family: 'control'
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

### **FluxRef** — 磁通标量

参考定子磁通。

**数据类型：** `single` | `double`

### **TqRef** — 转矩标量

参考转矩。

**数据类型：** `single` | `double`

### **vabc** — 电压向量

定子相电压。

**数据类型：** `single` | `double`

### **iabc** — 电流向量

定子相电流。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压信号标量

变换器的直流母线电压。

**数据类型：** `single` | `double`

### **Reset** — 控制器复位标量

PI 控制器积分器的复位。

**数据类型：** `single` | `double`

### 输出

### **G** — 门极脉冲向量 | `0` 或 `1`

逆变器门极脉冲。该模块不考虑任何死区时间。

**数据类型：** `single` | `double`

### **ModWave** — 调制波向量

如果为具有 PWM 能力的硬件平台生成代码，则部署到硬件的调制波。否则，此数据仅供参考。

## 参数

### 通用

### **定子电阻 (Ohm)** — 电阻 `0.25` (默认) | 正标量

电机定子的电阻。

### **极对数** — 极数 `1` (默认) | 正整数

电机极对数。

### **逆变器直流母线电压阈值 (V)** — 电压 `300` (默认) | 正标量

激活功率逆变器的电压阈值。

### **基本采样时间 (s)** — SVM 采样时间 `5e-6` (默认) | 小于控制采样时间的正标量

空间矢量调制器的采样时间。基本采样时间必须小于控制采样时间。

### **控制采样时间 (s)** — PI 采样时间 `5e-5` (默认) | 大于基本采样时间的正标量

PI 控制器的采样时间。控制采样时间必须大于基本采样时间。

### **开关频率 (Hz)** — 开关速率 `1000` (默认) | 正标量

指定功率变换器中开关所需的开关速率。

### 控制参数

### **磁通控制器比例增益** — 磁通 PI 比例增益 `150` (默认) | 正标量

磁通控制器的比例增益。

### **磁通控制器积分增益** — 磁通 PI 积分增益 `3000` (默认) | 正标量

磁通控制器的积分增益。

### **磁通控制器抗积分饱和增益** — 磁通 PI 抗积分饱和增益 `1` (默认) | 正标量

磁通控制器的抗积分饱和增益。

### **转矩控制器比例增益** — 转矩 PI 比例增益 `1` (默认) | 正标量

转矩控制器的比例增益。

### **转矩控制器积分增益** — 转矩 PI 积分增益 `50` (默认) | 正标量

转矩控制器的积分增益。

### **转矩控制器抗积分饱和增益** — 转矩 PI 抗积分饱和增益 `1` (默认) | 正标量

转矩控制器的抗积分饱和增益。

### **轴优先级** — 电压限制器的轴优先级 `Q-axis` (默认) | `D-axis` | `D-Q equivalence`

当模块限制电压时，优先处理或保持 *d* 轴与 *q* 轴之间的比例。

## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带 SVM 的感应电机 DTC 结构

Induction Machine Direct Torque Control with Space Vector Modulator 模块实现一种带空间矢量调制器 (SVM) 的感应电机直接转矩控制结构 (DTC)。使用此模块可为控制感应电机的逆变器生成门极脉冲。下图显示了该模块的架构。

图中：

- 您提供参考转矩 *T\** 和磁通 *ψ\**。
- 磁通和转矩估算器根据测得的相电流 *iabc* 和电压 *vabc* 估算实际转矩 *T* 和磁通 *ψ*。
- 两个 PI 控制器分别根据磁通误差和转矩误差确定参考 *d* 和 *q* 电压 *vd* 和 *vq*。
- SVM 生成控制驱动感应电机的逆变器所需的门极脉冲 *Gij*。下标 *i* 对应相 (*a*、*b* 或 *c*)。下标 *j* 对应高电平信号 *H* 或低电平信号 *L*。

### 磁通和转矩估算器

为估算转矩和磁通，该模块使用后向欧拉法对静止 *ɑβ* 参考坐标系中的电机电压方程进行离散化。*ɑβ* 坐标系中定子磁通的离散时间方程为：

ψα=(vα−iαRs)Tszz−1

ψβ=(vβ−iβRs)Tszz−1

其中：

- *vɑ* 和 *vβ* 分别是 *ɑ* 轴和 *β* 轴电压。
- *iɑ* 和 *iβ* 分别是 *ɑ* 轴和 *β* 轴电流。
- *Ψɑ* 和 *Ψβ* 分别是 *ɑ* 轴和 *β* 轴定子磁通。
- *Rs* 是定子电阻。

该模块按下式计算转矩和总定子磁通：

T=3p2(ψαiβ−ψβiα)

ψs=ψα2+ψβ2

其中：

- *p* 是极对数。
- *Ψs* 是总定子磁通。

### 空间矢量调制器

SVM 将所需电压转换为门极脉冲，您可用来控制逆变器。下图显示了三相逆变器可能的开关状态。

六边形表示空间矢量图。六个顶点中的每一个表示三相逆变器的一个可能开关状态 *(GAH,GBH,GCH)*。每个低侧门极采用与其对应高侧门极相反的状态。逆变器图展示了当前状态。

空间矢量图中的旋转矢量对应于复数参考电压矢量，该矢量以电机所需电频率旋转。实际上，开关频率远快于该电频率。因此，逆变器在包围其当前区域 *Ri* 的两个状态与对应于 *(0,0,0)* 的零状态之间连续切换，以生成所需电压。

要了解此方法的实现，请参阅 PWM Generator (Three-phase, Two-level) 模块。
