---
type: simulink-block
title: 'Smith Predictor Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Controllers'
documentation_page: 'smithpredictorcontroller'
documentation_source_path: 'ref/smithpredictorcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Smith Predictor Controller

## 端口

### 输入

### **r** — 被控对象参考标量

被控对象系统参考信号。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **y** — 被控对象输出标量

被控对象系统输出信号。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制器输出标量

控制系统输出信号。

**数据类型：** `single` | `double`

## 参数

### **比例增益** — *Kp* `1` (默认) | 正标量

PI 控制器的比例增益 *Kp*。

### **积分增益** — *Ki* `1` (默认) | 正标量

PI 控制器的积分增益 *Ki*。

### **积分器初始条件** — 积分器初始值 `0` (默认) | 标量

仿真开始时的积分器值。

### **控制作用上限** — *umax* `5` (默认) | 大于 **控制作用下限** 参数值的标量

控制输出信号的上限。

### **控制作用下限** — *umin* `0` (默认) | 标量

控制输出信号的下限。

### **模型离散传递函数分子** — 传递函数分子 `1` (默认) | 标量或向量

系统离散化传递函数的分子。要确定离散传递函数，如果您拥有 Control System Toolbox™ 许可证，请使用 `c2d` 函数。

### **模型离散传递函数分母** — 传递函数分母 `[1 0.5]` (默认) | 向量

系统离散化传递函数的分母。要确定离散传递函数，如果您拥有 Control System Toolbox 许可证，请使用 `c2d` 函数。

### **系统死区时间 (samples)** — 死区时间采样数 `2` (默认) | `0` 或正整数

死区时间的采样数。

### **采样时间（-1 表示继承）** — 采样间隔 `-1` (默认) | 默认值或正数

采样之间的时间间隔。如果该模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果该模块位于连续变步长模型中，请显式指定采样时间。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间 Smith 死区时间补偿器

Smith Predictor Controller 模块通过在离散时间中实现 Smith 死区时间 PI 控制结构来补偿死区时间。该图显示了该模块的等效电路。

### 方程

具有死区时间的系统的传递函数为

Gf(s)=Gp(s)e−τs,

其中：

- *τ* 是系统死区时间。
- *Gp(s)* 是过程模型。
- *Gf(s)* 是预测误差滤波器。
