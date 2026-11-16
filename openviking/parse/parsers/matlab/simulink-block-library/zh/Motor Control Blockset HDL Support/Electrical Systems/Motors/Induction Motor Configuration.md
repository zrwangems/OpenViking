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
chinese_source: official
---

# Induction Motor Configuration

## 端口

### 输出

### **Config** — 模块配置信号 矢量

感应电机或电机的配置信号，包括使用该模块配置的以下参数。

| 配置元素 | | | 单位 |
| --- | --- | --- | --- |
| 极对数 | | | - |
| 每相定子电阻 | | | 欧姆 |
| 定子泄漏电感 | | | 亨 |
| 转子电阻 | | | 欧姆 |
| 转子泄漏电感 | | | 亨 |
| 磁化电感 | | | 亨 |
| 惯量 | | | kgm^2 |
| 反电动势、电动势 | | | Vpk\_LL/krpm  Vpk\_LL 是线电压峰值 |
| 粘性阻尼 | | | N·m/（弧度/秒） |
| 端口配置（转矩或转速） | | | - |

**数据类型:** `single`

## 参数

### 模块选项

### **端口配置** — 选择端口配置 **转矩** (默认) | **转速**

下表总结了每个配置中的输入端口和输出端口。

| 机械输入配置参数值 | | | LdTrq/Spd 端口配置 |
| --- | --- | --- | --- |
| 转矩 | | | **LdTrq** |
| 转速 | | | **Spd** |

### **采样时间(Ts)** — 采样时间，在此采样时间过后模块将再次执行 `1e-6` (默认) | 标量

每两个连续的模块执行实例之间的固定时间间隔（以秒为单位）。

### 参数

### **极对数** — 极对 `2` (默认) | 标量

电机中的极对数 *P*。

### **定子电阻(欧姆)** — 定子电阻 `1.77` (默认) | 标量

定子电阻 *Rs*，以 ohm 为单位。

### **泄漏电感(H)** — 定子泄漏电感 `0.0139` (默认) | 标量

定子泄漏电感 *Lls*，以 H 为单位。

### **转子电阻(Ohm)** — 转子电阻 `1.34` (默认) | 标量

转子电阻 *Rr*，以 ohm 为单位。

### **泄漏电感(H)** — 转子泄漏电感 `0.0121` (默认) | 标量

转子泄漏电感 *Llr*，以 H 为单位。

### **磁化电感(H)** — 电感 `0.3876` (默认) | 标量

磁化电感 *Lm*，以 H 为单位。

### **物理惯量(kg\*m^2)** — 物理惯量 `0.001` (默认) | 标量

电机的物理惯量 *J*，以 kg.m^2 为单位。

### **粘性阻尼(N\*m/rad/s)** — 粘性阻尼 `0` (默认) | 标量

电机的粘性阻尼 *F*，以 N·m/（弧度/秒）为单位。

### **静态摩擦(N\*m)** — 静态摩擦 `0` (默认) | 标量

电机中的静态摩擦 *Tf*，以 N·m 为单位。

## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2022b 中推出**

## 描述

配置感应电机的系统参数

Induction Motor Configuration 模块可生成感应电机或电机的配置信号。您可以使用该信号来更新支持 FPGA 部署的感应电机模块的参数，例如 Induction Motor HDL 模块。
