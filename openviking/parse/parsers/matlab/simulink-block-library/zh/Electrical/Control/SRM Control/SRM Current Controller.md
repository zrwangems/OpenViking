---
type: simulink-block
title: 'SRM Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control'
documentation_page: 'srmcurrentcontroller'
documentation_source_path: 'ref/srmcurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# SRM Current Controller

## 端口
```yaml
ports:
- name: IsRef
  summary: 参考电流标量
  direction: input
  data_types: single | double
- name: Is
  summary: 测量电流标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 积分器复位标量
  direction: input
  data_types: Boolean
- name: theta
  summary: Theta 转子角度标量
  direction: input
  data_types: single | double
- name: thetaON
  summary: 开通角标量
  direction: input
  data_types: single | double
- name: thetaOFF
  summary: 关断角标量
  direction: input
  data_types: single | double
- name: abcRef
  summary: 参考电压矢量
  direction: output
  data_types: single | double
- name: abcOnOff
  summary: 开关信号矢量
  direction: output
  data_types: single | double
```

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **Is** — 测量电流标量

测量电流。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **theta** — Theta 转子角度标量

区间 [0, *β* ] 内的转子角度。

**数据类型：** `single` | `double`

### **thetaON** — 开通角标量

用于接通相电源的角度。

**数据类型：** `single` | `double`

### **thetaOFF** — 关断角标量

用于接通相电源的角度。

**数据类型：** `single` | `double`
### 输出

### **abcRef** — 参考电压矢量

在区间 [0, 1] 内归一化的控制信号。

**数据类型：** `single` | `double`

### **abcOnOff** — 开关信号矢量

用于 *a*、*b* 和 *c* 相的开关信号。`1` 表示开通条件，`0` 表示关断条件

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Proportional gain
  summary: 控制器比例增益，*Kp* 1（默认）| 正标量
  group: ''
- name: Integral gain
  summary: 积分增益，*Ki* 5（默认）| 正标量
  group: ''
- name: Anti-windup gain
  summary: 抗积分饱和增益，*Kaw* 1（默认）| 正标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: ''
```

### **Proportional gain** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **Integral gain** — 积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益 *Ki*。

### **Anti-windup gain** — 抗积分饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗积分饱和增益 *Kaw*。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。
## 所属库

Simscape / Electrical / Control / SRM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

开关磁阻电机的电流控制

SRM Current Controller 模块为 Switched Reluctance Machine (SRM) 模块执行离散时间比例积分 (PI) 电流控制。

### 方程

为确定占空比，该模块根据以下方程执行离散时间比例积分 (PI) 电流控制。

D=(Kp+KiTszz−1)(Is\_ref−Is)

其中：

- *D* 是占空比。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *Is\_ref* 是参考电流。
- *Is* 是测量电流。

为获得三相的控制信号，该模块随后将占空比与换相信号相乘。得到的三路控制信号在区间 [0, 1] 内归一化。
