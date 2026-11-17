---
type: simulink-block
title: 'Induction Motor Configuration'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'inductionmotorconfiguration'
documentation_source_path: '../mcb/ref/inductionmotorconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Motor Configuration

## 端口
```yaml
ports:
- name: Config
  summary: 模块配置信号向量
  direction: output
  data_types: single
```

### 输出

### **Config** — 模块配置信号向量

感应电机或电动机的配置信号，包含您使用此模块配置的以下参数。

| 配置元素 | | | 单位 |
| --- | --- | --- | --- |
| 极对数 | | | - |
| 每相定子电阻 | | | ohm |
| 定子漏电感 | | | Henries |
| 转子电阻 | | | ohm |
| 转子漏电感 | | | Henries |
| 励磁电感 | | | Henries |
| 惯量 | | | kgm^2 |
| 反电动势，EMF | | | Vpk\_LL/krpm  Vpk\_LL 是峰值线电压测量值 |
| 粘性阻尼 | | | N·m/(rad/s) |
| 端口配置（Torque 或 Speed） | | | - |

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Port configuration
  summary: 选择端口配置 Torque（默认）| Speed
  group: 模块选项
- name: Sample Time (Ts)
  summary: 模块再次执行前的采样时间 1e-6（默认）| 标量
  group: 模块选项
- name: Number of pole pairs
  summary: 极对数 2（默认）| 标量
  group: 参数
- name: Stator resistance (Ohm)
  summary: 定子电阻 1.77（默认）| 标量
  group: 参数
- name: Leakage inductance (H)
  summary: 定子漏电感 0.0139（默认）| 标量
  group: 参数
- name: Rotor resistance (Ohm)
  summary: 转子电阻 1.34（默认）| 标量
  group: 参数
- name: Leakage inductance (H)
  summary: 转子漏电感 0.0121（默认）| 标量
  group: 参数
- name: Magnetizing inductance (H)
  summary: 电感 0.3876（默认）| 标量
  group: 参数
- name: Physical Inertia (kg\*m^2)
  summary: 物理惯量 0.001（默认）| 标量
  group: 参数
- name: Viscous damping (N\*m/rad/s)
  summary: 粘性阻尼 0（默认）| 标量
  group: 参数
- name: Static friction (N\*m)
  summary: 静摩擦 0（默认）| 标量
  group: 参数
```

### 模块选项

### **Port configuration** — 选择端口配置 `Torque`（默认）| `Speed`

下表总结了每种配置下的输入和输出端口。

| 机械输入配置参数值 | | | LdTrq/Spd 端口配置 |
| --- | --- | --- | --- |
| Torque | | | **LdTrq** |
| Speed | | | **Spd** |

### **Sample Time (Ts)** — 模块再次执行前的采样时间 `1e-6`（默认）| 标量

每两次连续模块执行实例之间的固定时间间隔（以秒为单位）。

### 参数

### **Number of pole pairs** — 极对数 `2`（默认）| 标量

电动机中的极对数，*P*。

### **Stator resistance (Ohm)** — 定子电阻 `1.77`（默认）| 标量

定子电阻，*Rs*，单位为 ohm。

### **Leakage inductance (H)** — 定子漏电感 `0.0139`（默认）| 标量

定子漏电感，*Lls*，单位为 H。

### **Rotor resistance (Ohm)** — 转子电阻 `1.34`（默认）| 标量

转子电阻，*Rr*，单位为 ohm。

### **Leakage inductance (H)** — 转子漏电感 `0.0121`（默认）| 标量

转子漏电感，*Llr*，单位为 H。

### **Magnetizing inductance (H)** — 电感 `0.3876`（默认）| 标量

励磁电感，*Lm*，单位为 H。

### **Physical Inertia (kg\*m^2)** — 物理惯量 `0.001`（默认）| 标量

电动机的物理惯量，*J*，单位为 kg.m^2。

### **Viscous damping (N\*m/rad/s)** — 粘性阻尼 `0`（默认）| 标量

电动机的粘性阻尼，*F*，单位为 N·m/(rad/s)。

### **Static friction (N\*m)** — 静摩擦 `0`（默认）| 标量

电动机中的静摩擦，*Tf*，单位为 N·m。
## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

配置感应电动机的系统参数

Induction Motor Configuration 模块生成感应电机或电动机的配置信号。您可以使用此信号更新支持 FPGA 部署的感应电动机模块的参数，例如 Induction Motor HDL 模块。
