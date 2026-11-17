---
type: simulink-block
title: 'Smith Predictor Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'smithpredictorcontroller'
documentation_source_path: 'ref/smithpredictorcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Smith Predictor Controller

## 端口
```yaml
ports:
- name: r
  summary: 被控对象参考值 标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 积分器复位 标量
  direction: input
  data_types: Boolean
- name: y
  summary: 被控对象输出 标量
  direction: input
  data_types: single | double
- name: u
  summary: 控制器输出 标量
  direction: output
  data_types: single | double
```

### 输入

### **r** — 被控对象参考值 标量

被控对象系统参考信号。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位 标量

积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **y** — 被控对象输出 标量

被控对象系统输出信号。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制器输出 标量

控制系统输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Proportional gain
  summary: '*Kp* 1（默认）| 正标量'
  group: ''
- name: Integral gain
  summary: '*Ki* 1（默认）| 正标量'
  group: ''
- name: Integrator initial condition
  summary: 积分器初始值 0（默认）| 标量
  group: ''
- name: Control action upper limit
  summary: '*umax* 5（默认）| 大于 Control action lower limit 参数值的标量'
  group: ''
- name: Control action lower limit
  summary: '*umin* 0（默认）| 标量'
  group: ''
- name: Model discrete transfer function numerator
  summary: 传递函数分子 1（默认）| 标量或向量
  group: ''
- name: Model discrete transfer function denominator
  summary: 传递函数分母 [1 0.5]（默认）| 向量
  group: ''
- name: System dead time (samples)
  summary: 死区时间采样数 2（默认）| 0 或正整数
  group: ''
- name: Sample time (-1 for inherited)
  summary: 采样间隔 -1（默认）| 默认值或正数
  group: ''
```

### **Proportional gain** — *Kp* `1`（默认）| 正标量

PI 控制器的比例增益 *Kp*。

### **Integral gain** — *Ki* `1`（默认）| 正标量

PI 控制器的积分增益 *Ki*。

### **Integrator initial condition** — 积分器初始值 `0`（默认）| 标量

仿真开始时刻的积分器值。

### **Control action upper limit** — *umax* `5`（默认）| 大于 **Control action lower limit** 参数值的标量

控制输出信号的上限。

### **Control action lower limit** — *umin* `0`（默认）| 标量

控制输出信号的下限。

### **Model discrete transfer function numerator** — 传递函数分子 `1`（默认）| 标量或向量

系统离散化传递函数的分子。若要确定离散传递函数，如果您拥有 Control System Toolbox™ 许可证，请使用 `c2d` 函数。

### **Model discrete transfer function denominator** — 传递函数分母 `[1 0.5]`（默认）| 向量

系统离散化传递函数的分母。若要确定离散传递函数，如果您拥有 Control System Toolbox 许可证，请使用 `c2d` 函数。

### **System dead time (samples)** — 死区时间采样数 `2`（默认）| `0` 或正整数

死区时间的采样数。

### **Sample time (-1 for inherited)** — 采样间隔 `-1`（默认）| 默认值或正数

采样之间的时间间隔。如果该模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果该模块位于连续变步长模型中，请显式指定采样时间。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。
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

Smith Predictor Controller 模块通过在离散时间中实现 Smith 死区时间 PI 控制结构来补偿死区时间。下图显示了该模块的等效电路。

### 方程

具有死区时间的系统的传递函数为

Gf(s)=Gp(s)e−τs,

其中：

- *τ* 是系统死区时间。
- *Gp(s)* 是过程模型。
- *Gf(s)* 是预测误差滤波器。
