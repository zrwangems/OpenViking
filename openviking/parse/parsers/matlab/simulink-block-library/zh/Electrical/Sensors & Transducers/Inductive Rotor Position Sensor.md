---
type: simulink-block
title: 'Inductive Rotor Position Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'inductiverotorpositionsensor'
documentation_source_path: 'ref/inductiverotorpositionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Inductive Rotor Position Sensor

## 端口

### 守恒

### **R** — 传感器正探头机械旋转的旋转速度

与传感器正探头关联的机械旋转守恒端口。

### **C** — 传感器负探头机械旋转的旋转速度

与传感器负（参考）探头关联的机械旋转守恒端口。

### **yp** — `y` 轴正端子电气

与 `y` 轴正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface** 设置为 `Electrical connections`。

### **yn** — `y` 轴负端子电气

与 `y` 轴负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface** 设置为 `Electrical connections`。

### **xp** — x 轴正端子电气

与 `x` 轴正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface** 设置为 `Electrical connections`。

### **xn** — x 轴负端子电气

与 `x` 轴负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface** 设置为 `Electrical connections`。
### 输出

### **Angle** — 旋转角度物理信号

磁场在 *x*-*y* 平面中的旋转角度，以物理信号形式返回。

#### 依赖关系

要启用此端口，请将 **Output interface** 设置为 `Decoded angular position`。

## 参数

### **Number of pole pairs** — 极对数 `2`（默认）| 标量

极对数。

### **X-axis voltage amplitude** — `x` 轴电压 `2.5` `V`（默认）| 标量

`x` 轴电压幅值。

### **Y-axis voltage amplitude** — `y` 轴电压 `2.5` `V`（默认）| 标量

`y` 轴电压幅值。

### **X-axis voltage offset** — `x` 轴电压偏移 `0` `V`（默认）| 标量

在 `x` 轴上无外部磁场时，电流通过电导体的电势差。

### **Y-axis voltage offset** — `y` 轴电压偏移 `0` `V`（默认）| 标量

在 `y` 轴上无外部磁场时，电流通过电导体的电势差。

### **Quadrature error** — 正交误差 `0` `deg`（默认）| 标量

正交误差量。正交切换可以减少偏移误差。

### **Tumbling coefficient** — 翻滚系数 `0`（默认）| 标量

翻滚系数，以度为单位。

### **Output interface** — 解码信息的接口 `Electrical connections`（默认）| `Decoded angular position`

用于解码信息的端口接口，指定为 `Electrical connections` 或 `Decoded angular position`。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

带四个感应线圈的感应式转子位置传感器

Inductive Rotor Position Sensor 模块使用涡流损耗理论来获取转子位置。它由四个平面线圈和一个检测转子位置的目标迹线组成。目标迹线呈正弦形状，由导电材料制成。四个平面线圈之间的距离相当于一个周期的 90 度。

### 方程

传感器各元件之间的电压由以下方程描述：

vx=Vx0+Axcos(Nθ)+Ksin(θ)

vy=Vy0+Aycos(Nθ−π2+β)+Ksin(θ)

其中：

- *vx* 是余弦电压。
- *vy* 是正弦电压。
- *Ax* 和 *Ay* 是 *x* 轴和 *y* 轴的电压幅值，反映灵敏度失配。
- *Vx0* 和 *Vy0* 是 *x* 轴和 *y* 轴的电压偏移。
- *N* 是极对数。
- *θ* 是机械位置。
- *β* 是正交误差。
- *K* 是翻滚因子。

该模块使用此方程解码角度：

θout=arctan(vyvx)。

下图显示了翻滚因子的影响：

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
