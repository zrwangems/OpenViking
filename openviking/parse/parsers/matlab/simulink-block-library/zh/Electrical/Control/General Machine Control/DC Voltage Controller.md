---
type: simulink-block
title: 'DC Voltage Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control'
documentation_page: 'dcvoltagecontroller'
documentation_source_path: 'ref/dcvoltagecontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Voltage Controller

## 端口

### 输入

### **vRef** — 参考直流电压标量

被控对象的期望直流输出电压。

**数据类型：** `single` | `double`

### **v** — 测量直流电压标量

被控对象的测量直流输出电压。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **Control** — 控制信号标量

控制信号 *control*，表示为占空比或电流。

**数据类型：** `single` | `double`

## 参数

### **Proportional gain** — 比例增益，*Kp* `0.1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **Integral gain** — 积分增益，*Ki* `50`（默认）| 正标量

控制器的积分增益 *Ki*。

### **Anti-windup gain** — 抗饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗饱和增益 *Kaw*。

### **Control action upper limit** — 控制信号上限，*controlmax* `1`（默认）| 正标量

**Control** 输出信号的上限。该值必须大于 **Control action lower limit** 参数的值。

### **Control action lower limit** — 控制信号下限，*controlmin* `0`（默认）| 非负标量

**Control** 输出信号的下限。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **Discretization sample time** — 离散化采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，单位为 s。

### **Time constant voltage filter** — 直流电压滤波器时间常数，*τ* `0.001`（默认）| 正标量

直流电压滤波器的时间常数 *τ*。

#### 依赖关系

**Time constant voltage filter** 参数仅在选中 **Filter DC voltage** 复选框时可见。

### **Enable zero cancellation** — 前馈零点对消 off（默认）| on

在前馈路径上使用零点对消的选项。

#### 依赖关系

如果选择 **Enable zero cancellation** 选项并将 **Sample time (-1 for inherited)** 设置为 `-1`，则 **Discretization sample time** 参数变为可见。

### **Filter DC voltage** — 直流电压滤波器选项 on（默认）| off

要启用电压测量路径上的滤波器，请选中该复选框。要禁用滤波器，请清除该复选框。

#### 依赖关系

**Time constant voltage filter** 参数仅在选中 **Filter DC voltage** 复选框时可见。

## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

具有前馈零点对消和积分抗饱和的离散时间直流电压 PI 控制

DC Voltage Controller 模块实现基于离散时间 PI 的直流电压控制。该模块可以在前馈路径中实现零点对消。为避免积分增益饱和，该模块可以实现抗饱和增益。

### 方程

DC Voltage Controller 模块用于计算控制信号的方程为

control=(Kp+KiTszz−1)(vref−v),

其中：

- *control* 是控制信号，表示为占空比或电流。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *vref* 是参考电压。
- *v* 是测量电压。

PI 控制计算会在闭环传递函数中产生一个零点。为对消该零点，模块使用以下离散时间零点对消传递函数：

GZC(z)=TsKiKpz+(Ts−KpKiKpKi)。

为避免积分器输出饱和，模块使用抗饱和机制。积分器增益则等于

Ki+Kaw(controlsat−controlunsat),

其中：

- *Kaw* 是抗饱和增益。
- *controlsat* 是饱和控制信号，模块将其计算为 controlsat=min(max(controlunsat,controlmin),controlmax)，

  其中：

  - *controlunsat* 是未饱和控制信号。
  - *controlmin* 是控制信号的下限。
  - *vmax* 是控制信号的上限。
