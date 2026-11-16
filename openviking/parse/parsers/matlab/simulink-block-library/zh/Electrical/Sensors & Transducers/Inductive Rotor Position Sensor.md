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

### **R** — 传感器正探头的旋转速度（机械旋转）

与传感器正探头关联的机械旋转守恒端口。

### **C** — 传感器负探头的旋转速度（机械旋转）

与传感器负（参考）探头关联的机械旋转守恒端口。

### **yp** — `y` 轴正端子（电气）

与 `y` 轴正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **输出接口** 设置为 `Electrical connections`。

### **yn** — `y` 轴负端子（电气）

与 `y` 轴负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **输出接口** 设置为 `Electrical connections`。

### **xp** — x 轴正端子（电气）

与 `x` 轴正端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **输出接口** 设置为 `Electrical connections`。

### **xn** — x 轴负端子（电气）

与 `x` 轴负端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **输出接口** 设置为 `Electrical connections`。
### 输出

### **Angle** — 旋转角物理信号

磁场在 *x*-*y* 平面中的旋转角，以物理信号形式返回。

#### 依赖关系

要启用此端口，请将 **输出接口** 设置为 `Decoded angular position`。

## 参数

### **极对数** — 极对数 `2`（默认） | scalar

极对数。

### **X 轴电压幅值** — `x` 轴电压 `2.5` `V`（默认） | scalar

`x` 轴电压幅值。

### **Y 轴电压幅值** — `y` 轴电压 `2.5` `V`（默认） | scalar

`y` 轴电压幅值。

### **X 轴电压偏移** — `x` 轴电压偏移 `0` `V`（默认） | scalar

在 `x` 轴上不存在外部磁场时，流经电导体的电流的电势差。

### **Y 轴电压偏移** — `y` 轴电压偏移 `0` `V`（默认） | scalar

在 `y` 轴上不存在外部磁场时，流经电导体的电流的电势差。

### **正交误差** — 正交误差 `0` `deg`（默认） | scalar

正交误差量。正交切换可减小偏移误差。

### **翻滚系数** — 翻滚系数 `0`（默认） | scalar

翻滚系数，单位为度。

### **输出接口** — 解码信息接口 `Electrical connections`（默认） | `Decoded angular position`

用于解码信息的端口接口，指定为 `Electrical connections` 或 `Decoded angular position`。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有四个感应线圈的感应式转子位置传感器

Inductive Rotor Position Sensor 模块使用涡流损耗理论来获得转子位置。它由四个平面线圈和一个目标迹线组成，用于检测转子位置。目标迹线呈正弦形状，并由导电材料制成。四个平面线圈之间的距离相当于一个周期的 90 度。

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

该模块使用以下方程解码角度：

θout=arctan(vyvx).

下图显示了翻滚因子的影响：

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅通过标称值进行系统缩放。
