---
type: simulink-block
title: 'BLDC Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control'
documentation_page: 'bldccurrentcontroller'
documentation_source_path: 'ref/bldccurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC Current Controller

## 端口

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **Is** — 测量电流标量

实际电流。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### **Hall** — 霍尔传感器向量

霍尔传感器数据。

**数据类型：** `single` | `double`

### **Direction** — 电机方向标量

电机旋转方向。

**数据类型：** `single` | `double`
### 输出

### **vabcRef** — 参考电压向量

*a* 相、*b* 相和 *c* 相的参考电压。

**数据类型：** `single` | `double`

## 参数

### **Proportional gain** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **Integral gain** — 积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益 *Ki*。

### **Anti-windup gain** — 抗饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗饱和增益 *Kaw*。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

#### 依赖关系

如果将 **Sample time (-1 for inherited)** 设置为 `-1` 并选择 **Enable zero cancellation** 选项，则 **Discretization sample time** 参数将变为可见。

### **Discretization sample time** — 离散化采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，以 s 为单位。零抵消需要离散化。

#### 依赖关系

仅当同时满足以下两个条件时，此参数才可见：

- **Sample time** 设置为 `-1`。
- 已选择 **Enable zero cancellation**。

### **Enable zero cancellation** — 前馈零抵消 off（默认）| on

在前馈路径上使用零抵消的选项。

#### 依赖关系

如果选择 **Enable zero cancellation** 选项并将 **Sample time (-1 for inherited)** 设置为 `-1`，则 **Discretization sample time** 参数将变为可见。

## 所属库

Simscape / Electrical / Control / BLDC Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

离散时间无刷直流电机电流 PI 控制器

BLDC Current Controller 模块使用此算法控制直流无刷电机中的电流。

### 方程

BLDC Current Controller 通过使用此方程实现比例积分（PI）电流控制，为 BLDC 模块产生占空比。

D=(Kp+KiTszz−1)(Is\_ref−Is)

其中：

- *D* 是占空比。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是时间周期。
- *Is\_ref* 是参考电流。
- *Is* 是测量电流。
- *Gzc* 是零抵消多项式。

PI 控制算法的闭环传递函数产生一个零点，可以通过在前馈路径中使用零抵消来抵消该零点。离散时间下的零抵消传递函数为：

GZC(z)=TsKiKpz+(Ts−KpKiKpKi)。

该模块通过将占空比与换向信号相乘来获得三相的控制信号。所得的三路控制信号在区间 [-1, 1] 上归一化。
