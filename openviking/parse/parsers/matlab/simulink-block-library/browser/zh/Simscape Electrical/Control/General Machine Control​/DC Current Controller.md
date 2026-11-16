---
type: simulink-block
title: 'DC Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control\u200b'
documentation_page: 'dccurrentcontroller'
documentation_source_path: 'ref/dccurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Current Controller

## 端口

### 输入

### **iRef** — 参考电流标量

被控对象的期望输出电流。

**数据类型：** `single` | `double`

### **i** — 测量电流标量

被控对象的测量电流。

**数据类型：** `single` | `double`

### **vmax** — 最大直流电压标量

被控对象的最大直流输出电压。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### 输出

### **vRef** — 参考直流电压标量

被控对象的期望直流输出电压。

**数据类型：** `single` | `double`

## 参数

### **比例增益** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **积分增益** — 积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益 *Ki*。

### **抗积分饱和增益** — 抗积分饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗积分饱和增益 *Kaw*。

### **电压限制** — 负电压限制 `Positive and negative voltage`（默认）| `Positive voltage only`

允许正负直流电压输出，或将输出限制为正直流电压。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块生成输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，则将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，则使用正标量显式指定采样时间。

#### 依赖关系

如果将 **采样时间（-1 表示继承）** 设置为 `-1` 并选择 **启用零点对消** 选项，则 **离散化采样时间** 参数将变为可见。

### **离散化采样时间** — 用于离散化的采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，单位为 s。零点对消需要离散化。

#### 依赖关系

仅当同时满足以下两个条件时，此参数才可见：

- **采样时间** 设置为 `-1`。
- 选中 **启用零点对消**。

### **启用零点对消** — 前馈零点对消 off（默认）| on

在前馈路径上使用零点对消的选项。

#### 依赖关系

如果选择 **启用零点对消** 选项，并将 **采样时间（-1 表示继承）** 设置为 `-1`，则 **离散化采样时间** 参数将变为可见。

## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带积分抗饱和的离散时间直流电流 PI 控制

DC Current Controller 模块实现离散时间比例积分 (PI) 直流电压控制器。该模块可以在前馈路径中实现零点对消。为避免积分增益饱和，该模块可以实现抗积分饱和增益。

### 方程

DC Current Controller 模块用于计算参考电压的方程为

vref=(Kp+KiTszz−1)(iref−i),

其中：

- *vref* 是参考电压。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *iref* 是参考电流。
- *i* 是测量电流。

PI 控制计算会在闭环传递函数中产生一个零点。为对消该零点，模块使用以下离散时间零点对消传递函数：

GZC(z)=TsKiKpz+(Ts−KpKiKpKi).

为避免积分器输出饱和，模块使用抗积分饱和机制。积分器增益随后等于

Ki+Kaw(vref\_sat−vref\_unsat),

其中：

- *Kaw* 是抗积分饱和增益。
- *vref\_sat* 是饱和参考电压信号，模块将其计算为 vref\_sat=min(max(vref\_unsat,vmin),vmax)，

  其中：

  - *vref\_unsat* 是未饱和参考电压信号。
  - *vmin* 是输出电压的下限。对于 positive voltage only，vmin=0。对于 positive and negative voltage，vmin=−vmax
  - *vmax* 是输出电压的上限。
