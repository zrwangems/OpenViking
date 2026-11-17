---
type: simulink-block
title: 'Longitudinal Controller Stanley'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Vehicle Control'
documentation_page: 'longitudinalcontrollerstanley'
documentation_source_path: 'ref/longitudinalcontrollerstanley.html'
language: zh-CN
chinese_source: worker-translation
---

# Longitudinal Controller Stanley

## 端口
```yaml
ports:
- name: RefVelocity
  summary: 参考速度 实数标量
  direction: input
- name: CurrVelocity
  summary: 当前速度 实数标量
  direction: input
- name: Direction
  summary: 行驶方向 1（前进运动） | -1（倒车运动）
  direction: input
- name: Reset
  summary: 重置速度误差积分的触发信号 0（保持稳定） | 非零标量（重置）
  direction: input
- name: AccelCmd
  summary: 加速度指令 范围为 [0, *M*A] 的实数标量
  direction: output
- name: DecelCmd
  summary: 减速度指令 范围为 [0, *M*D] 的实数标量
  direction: output
```

### 输入

### **RefVelocity** — 参考速度 实数标量

参考速度，以米每秒为单位，指定为实数标量。

### **CurrVelocity** — 当前速度 实数标量

车辆的当前速度，以米每秒为单位，指定为实数标量。

### **Direction** — 行驶方向 `1`（前进运动） | `-1`（倒车运动）

车辆的行驶方向，指定为 `1` 表示前进运动，`-1` 表示倒车运动。

### **Reset** — 重置速度误差积分的触发信号 `0`（保持稳定） | 非零标量（重置）

将速度误差的积分 *e*(*k*) 重置为零的触发信号。值为 `0` 时保持 *e*(*k*) 稳定。非零值重置 *e*(*k*)。
### 输出

### **AccelCmd** — 加速度指令 范围为 [0, *M*A] 的实数标量

加速度指令，返回为范围 [0, *M*A] 内的实数标量，其中 *M*A 是 **Maximum longitudinal acceleration (m/s^2)** 参数的值。

### **DecelCmd** — 减速度指令 范围为 [0, *M*D] 的实数标量

减速度指令，返回为范围 [0, *M*D] 内的实数标量，其中 *M*D 是 **Maximum longitudinal deceleration (m/s^2)** 参数的值。
## 参数
```yaml
parameters:
- name: Proportional gain, Kp
  summary: 比例增益 2.5（默认值） | 正实数标量
  group: ''
- name: Integral gain, Ki
  summary: 积分增益 1（默认值） | 正实数标量
  group: ''
- name: Sample time (s)
  summary: 采样时间 0.05（默认值） | 正实数标量
  group: ''
- name: Maximum longitudinal acceleration (m/s^2)
  summary: 最大纵向加速度 3（默认值） | 正实数标量
  group: ''
- name: Maximum longitudinal deceleration (m/s^2)
  summary: 最大纵向减速度 6（默认值） | 正实数标量
  group: ''
```

### **Proportional gain, Kp** — 比例增益 `2.5`（默认值） | 正实数标量

控制器的比例增益 *K*p，指定为正实数标量。

### **Integral gain, Ki** — 积分增益 `1`（默认值） | 正实数标量

控制器的积分增益 *K*i，指定为正实数标量。

### **Sample time (s)** — 采样时间 `0.05`（默认值） | 正实数标量

控制器的采样时间，以秒为单位，指定为正实数标量。

### **Maximum longitudinal acceleration (m/s^2)** — 最大纵向加速度 `3`（默认值） | 正实数标量

最大纵向加速度，以米每二次方秒为单位，指定为正实数标量。

该模块将 **AccelCmd** 的输出饱和至范围 [0, *M*A]，其中 *M*A 是该参数的值。高于 *M*A 的值被设置为 *M*A。

### **Maximum longitudinal deceleration (m/s^2)** — 最大纵向减速度 `6`（默认值） | 正实数标量

最大纵向减速度，以米每二次方秒为单位，指定为正实数标量。

该模块将 **DecelCmd** 端口的输出饱和至范围 [0, *M*D]，其中 *M*D 是该参数的值。高于 *M*D 的值被设置为 *M*D。
## 所属库

Automated Driving Toolbox / Vehicle Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用 Stanley 方法控制车辆的纵向速度

Longitudinal Controller Stanley 模块计算加速度和减速度指令（以米每秒为单位），用于控制车辆的速度。指定参考速度、当前速度和当前行驶方向。控制器使用 Stanley 方法 [1] 计算这些指令，该模块将其实现为具有积分抗饱和的离散比例积分（PI）控制器。有关更多详细信息，请参阅算法。

您还可以使用 Stanley 方法计算车辆的转向角指令。请参阅 Lateral Controller Stanley 模块。
