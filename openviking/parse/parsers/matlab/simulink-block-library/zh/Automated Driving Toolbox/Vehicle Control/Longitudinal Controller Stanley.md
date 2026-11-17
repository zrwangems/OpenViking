---
type: simulink-block
title: 'Longitudinal Controller Stanley'
family: 'vehicle-control'
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

### 输入

### **RefVelocity** — 参考速度 real scalar

参考速度，以 meters per second 为单位，指定为 real scalar。

### **CurrVelocity** — 当前速度 real scalar

车辆的当前速度，以 meters per second 为单位，指定为 real scalar。

### **Direction** — 行驶方向 `1`（前进运动） | `-1`（倒车运动）

车辆的行驶方向，指定为 `1` 表示前进运动，`-1` 表示倒车运动。

### **Reset** — 用于重置速度误差积分的触发 `0`（保持稳定） | nonzero scalar（重置）

用于将速度误差的积分 *e*(*k*) 重置为零的触发。`0` 值使 *e*(*k*) 保持稳定。非零值重置 *e*(*k*)。

### 输出

### **AccelCmd** — 加速度命令 real scalar，范围为 [0, *M*A]

加速度命令，以范围 [0, *M*A] 内的 real scalar 形式返回，其中 *M*A 是 **最大纵向加速度 (m/s^2)** 参数的值。

### **DecelCmd** — 减速度命令 real scalar，范围为 [0, *M*D]

减速度命令，以范围 [0, *M*D] 内的 real scalar 形式返回，其中 *M*D 是 **最大纵向减速度 (m/s^2)** 参数的值。

## 参数

### **比例增益, Kp** — 比例增益 `2.5`（默认） | positive real scalar

控制器的比例增益，*K*p，指定为 positive real scalar。

### **积分增益, Ki** — 积分增益 `1`（默认） | positive real scalar

控制器的积分增益，*K*i，指定为 positive real scalar。

### **采样时间 (s)** — 采样时间 `0.05`（默认） | positive real scalar

控制器的采样时间，以 seconds 为单位，指定为 positive real scalar。

### **最大纵向加速度 (m/s^2)** — 最大纵向加速度 `3`（默认） | positive real scalar

最大纵向加速度，以 meters per second squared 为单位，指定为 positive real scalar。

模块将 **AccelCmd** 的输出饱和到范围 [0, *M*A]，其中 *M*A 是此参数的值。高于 *M*A 的值设置为 *M*A。

### **最大纵向减速度 (m/s^2)** — 最大纵向减速度 `6`（默认） | positive real scalar

最大纵向减速度，以 meters per second squared 为单位，指定为 positive real scalar。

模块将 **DecelCmd** 端口的输出饱和到范围 [0, *M*D]，其中 *M*D 是此参数的值。高于 *M*D 的值设置为 *M*D。

## 所属库

Automated Driving Toolbox / Vehicle Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用 Stanley 方法控制车辆的纵向速度

Longitudinal Controller Stanley 模块计算加速度和减速度命令（以 meters per second 为单位），这些命令控制车辆的速度。指定参考速度、当前速度和当前行驶方向。控制器使用 Stanley 方法 [1] 计算这些命令，模块将该方法实现为具有积分抗饱和的离散比例积分 (PI) 控制器。有关详细信息，请参阅算法。

您还可以使用 Stanley 方法计算车辆的转向角命令。请参阅 Lateral Controller Stanley 模块。
