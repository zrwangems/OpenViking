---
type: simulink-block
title: 'Extended EMF Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'extendedemfobserver'
documentation_source_path: 'ref/extendedemfobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Extended EMF Observer

## 端口

### 输入

### **Vα** — *α* 轴电压标量

静止 *αβ* 参考坐标系中沿 *α* 轴的标幺电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vβ** — *β* 轴电压标量

静止 *αβ* 参考坐标系中沿 *β* 轴的标幺电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Iα** — *α* 轴电流标量

静止 *αβ* 参考坐标系中沿 *α* 轴的标幺电流分量。

**数据类型：** `single` | `double` | `fixed point`

### **Iβ** — *β* 轴电流标量

静止 *αβ* 参考坐标系中沿 *β* 轴的标幺电流分量。

**数据类型：** `single` | `double` | `fixed point`

### **Rst** — 复位模块标量

用于复位并重新启动模块算法处理的脉冲（真值）。

**数据类型：** `single` | `double` | `fixed point`

### **ParameterBus** — Extended EMF Observer 的计算参数总线

Extended EMF Observer 模块的计算参数。该输入端口接受以下参数：

- **Number of pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator q-axis inductance (H)**
- **Maximum application speed (RPM)**
- **EEMF observer gain**
- **EEMF filter cutoff frequency (Hz)**
- **Proportional (P)**
- **Integral (I)**
- **Speed filter cutoff frequency (Hz)**

将此端口与 Compute Parameter 模块配合使用，以在运行时最优地更新上述模块参数。

#### 依赖关系

要启用此端口，请选择 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `single` | `double`
### 输出

### **θe** — PMSM 电位置标量

转子的估计电位置。

#### 依赖关系

要启用此端口，请将 **Position output** 参数设置为 `Electrical position`。

**数据类型：** `single` | `double` | `fixed point`

### **Sin θe** — PMSM 电位置的正弦标量

转子估计电位置的正弦。

#### 依赖关系

要启用此端口，请将 **Position output** 参数设置为 `Sine and Cosine electrical position`。

**数据类型：** `single` | `double` | `fixed point`

### **Cos θe** — PMSM 电位置的余弦标量

转子估计电位置的余弦。

#### 依赖关系

要启用此端口，请将 **Position output** 参数设置为 `Sine and Cosine electrical position`。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — PMSM 机械转速标量

转子的估计机械转速。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Use input port for computed parameters (run-time motor swap)** — 启用输入端口以接受计算参数的选项 `off`（默认）| on

选择此参数可启用 **ParameterBus** 输入端口并禁用以下参数：

- **Number of pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator q-axis inductance (H)**
- **Maximum application speed (RPM)**
- **EEMF observer gain**
- **EEMF filter cutoff frequency (Hz)**
- **Proportional (P)**
- **Integral (I)**
- **Speed filter cutoff frequency (Hz)**

此参数使您能够将输入端口与 Compute Parameter 模块配合使用，以在运行时最优地更新模块参数。

### **Input units** — 模块输入的单位 `SI unit`（默认）| `Per-unit`

模块输入的单位。

### **Position output** — 位置输出的类型 `Electrical position`（默认）| `Sine and Cosine electrical position`

模块输出的位置类型。

- `Electrical position` — 选择此值可启用 `θe` 端口。
- `Sine and Cosine electrical position` — 选择此值可启用 `Sin θe` 和 `Cos θe` 端口。

### **Discrete step size (s)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

模块两次连续执行之间的固定时间间隔（以秒为单位）。

### Motor Parameters

### **Stator resistance (ohm)** — 电阻 `0.36`（默认）| 标量

定子相绕组电阻（以欧姆为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Stator d-axis inductance (H)** — *D* 轴电感 `0.2e-3`（默认）| 标量

沿旋转 *d-q* 参考坐标系 *d* 轴的定子相绕组电感（以亨利为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Stator d-axis inductance (H)** — *Q* 轴电感 `0.2e-3`（默认）| 标量

沿旋转 *d-q* 参考坐标系 *q* 轴的定子相绕组电感（以亨利为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Maximum application speed (RPM)** — 支持的最大机械转速 `6000`（默认）| 标量

模块可支持的最大机械转速（以 RPM 为单位）。如果将转速设置为高于此值的值，模块将生成不正确的输出。

**Note**

模块使用此参数滤除估计转速信号中的噪声。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Maximum voltage (V)** — 对应一标幺值的标称电压 `13.8564`（默认）| 标量

施加到 PMSM 的最大相电压。有关详细信息，请参阅 Per-Unit System。

### **Maximum current (A)** — 对应一标幺值的标称电流 `21.4286`（默认）| 标量

提供给 PMSM 的最大可测量电流。有关详细信息，请参阅 Per-Unit System。

### Observer Parameters

### **EEMF observer gain** — 扩展 EMF 观测器增益 `10`（默认）| 标量

线性扩展 EMF 状态观测器的增益。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **EEMF filter cutoff frequency (Hz)** — EEMF 滤波器截止频率 `7500`（默认）| 标量

模块用于去除估计反 EMF 值中噪声的低通滤波器的截止频率。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Proportional (P)** — 转速观测器的比例增益 `250`（默认）| 标量

模块使用的转速观测器的比例增益。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **Integral (I)** — 转速观测器的积分增益 `200000`（默认）| 标量

模块使用的转速观测器的积分增益。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed
parameters (run-time motor swap)** 参数。

### **正弦-余弦查找表的数据点数量** — 用于速度计算的数据点数量 `1024`（默认）| 标量

速度观测器用于根据扩展反电动势值计算速度的查找表中的数据点数量。

### **速度滤波器截止频率 (Hz)** — 速度滤波器的截止频率 `15`（默认）| 标量

该模块用于消除估计速度中噪声的低通滤波器的截止频率。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### 数据类型

### **位置单位** — 位置输出的单位 `Degrees`（默认）| `Radians` | `Per-unit`

位置输出的单位。

### **位置数据类型** — 位置输出的数据类型 `single`（默认）| `double` | `fixed point`

位置输出的数据类型。

### **速度单位** — 速度输出的单位 `Degrees/sec`（默认）| `Radians/sec` | `RPM` | `Per-unit`

速度输出的单位。

### **速度数据类型** — 速度输出的数据类型 `single`（默认）| `double` | `fixed point`

速度输出的数据类型。

### **表数据类型** — 表的数据类型 `single`（默认）| `double` | `fixed point`

表的数据类型。

## 所属库

Motor Control Blockset / Sensorless Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023a 中引入**

## 描述

计算永磁同步电机 (PMSM) 的电气位置和机械速度

Extended EMF Observer 模块根据静止 *αβ* 参考坐标系中测得的电压和电流，计算 PMSM 的电气位置 *θe*（或 sin *θe* 和 cos *θe*），以及机械速度。

该模块包含一个线性扩展反电动势状态观测器，用于估计扩展反电动势。它使用低通滤波器消除估计反电动势值中的任何噪声。此外，该模块包含一个基于速度前馈的正交锁相环 (PLL)，用作速度观测器。速度观测器使用计算出的扩展反电动势来确定电机速度。即使在恒定角加速度期间，它也能以零误差计算速度。然后，该模块根据估计的电机电气速度计算位置输出。

此外，您可以使用高级选项启用 **ParameterBus** 输入端口，您可以将其与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。当电机参数可能随时间变化时，例如在构建可能需要在运行时切换电机的应用时，您可以使用此功能。

### 方程

IPMSM 状态方程定义为：

[i·e·]=[A11A120A22][ie]+[B10]v+[0W]i=C[ie]

这些方程描述了降阶 PMSM 状态模型：

i·=A11i+A12e+B1ve·=A22e

扩展反电动势，e={(Ld−Lq)(ωreid−i·q)+ωreKE}[−sinθrecosθre]

该方程描述了降维状态观测器：

e^·=(A^22−ξA12)e^+ξ(i·−A^11i−B1v)

这些方程描述了扩展 EMF 观测器参数：

A22−ξA12=ωreJ−(αI+βJ)(−1Ld)Iξ=(αI+βJ)

为确保收敛，如果您设置 β=ωre×Ld 并将 *α* 设置为负值，则扩展 EMF
观测器增益可确定为：

Extended EMF ​observer gain=−αLd

其中：

- i=[iαiβ]、e=[eαeβ] 和 v=[vαvβ]。
- W=(Ld−Lq)(ωreid·−iq··)[−sinθrecosθre]。
- A=[A11A120A22]、B=[B10] 和 C=[I0]。
- A11=−(RLd)I+(ωre(Ld−Lq)Ld)J、A12=(−1Ld)I 和 A22=ωreJ。
- B1=(1Ld)I、I=[1001] 和 J=[0−110]。

  **注意**

  A 和 C 是一对可观测对。
- “·”和“··”分别是一阶和二阶微分算子。
- *vα* 和
  *vβ* 分别是沿
  *α*- 和 *β*- 轴的定子电压。
- *iα* 和
  *iβ* 分别是沿
  *α*- 和 *β*- 轴的定子电流。
- *eα* 和
  *eβ* 分别是沿
  *α*- 和 *β*- 轴的扩展反电动势。
- *id* 和
  *iq* 分别是沿
  *d*- 和 *q*- 轴的定子电流。
- *R* 是 PMSM 的定子电阻。
- *Ld* 和
  *Lq* 分别是 PMSM 在
  *d* 和 *q* 轴上的定子电感。
- *KE* 是 EMF 常数。
- *ωre* 是电角度下的角速度。
- *θre* 是电角度下的转子位置。
- e^、A^22 和 A^11 是估计值。
- *ξ* 是反馈增益。
