---
type: simulink-block
title: 'BLDC Configuration'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'bldcconfiguration'
documentation_source_path: '../mcb/ref/bldcconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC Configuration

## 端口

### 输出

### **Config** — 模块配置信号向量

BLDC 电机的配置信号，其中包含您使用此模块配置的以下参数。

| 配置元素 | | | 单位 |
| --- | --- | --- | --- |
| 极对数 | | | - |
| 每相定子电阻 | | | ohm |
| 定子 d 轴电感 | | | Henries |
| 定子 q 轴电感 | | | Henries |
| 永磁磁链常数 | | | Weber |
| 惯量 | | | kgm^2 |
| 反电动势，EMF | | | Vpk\_LL/krpm  Vpk\_LL 是峰值电压线对线测量值 |
| 粘性阻尼 | | | N·m/(rad/s) |
| 机械输入配置（Torque 或 Speed） | | | - |

**数据类型：** `single`

## 参数

### 模块选项

### **Mechanical input configuration** — 选择端口配置 `Torque`（默认）| `Speed`

下表总结了每种端口配置下的输入和输出端口。

| 机械输入配置参数值 | | | LdTrq/Spd 端口配置 |
| --- | --- | --- | --- |
| Torque | | | **LdTrq** |
| Speed | | | **Spd** |

### **Sample Time (Ts)** — 模块再次执行前的采样时间 `1e-6`（默认）| 标量

每两次连续模块执行实例之间的固定时间间隔（以秒为单位）。

### 参数

### **Number of pole pairs** — 极对数 `4`（默认）| 标量

电机中的极对数，*P*。

### **Stator resistance per phase (Ohm)** — 定子电阻 `0.02`（默认）| 标量

每相定子电阻，*Rs*，单位为欧姆。

### **Stator d-axis inductance (H)** — *d* 轴电感 `1.7e-3`（默认）| 标量

定子电感，*Ld*，单位为 H。

### **Stator q-axis inductance (H)** — *q* 轴电感 `3.2e-3`（默认）| 标量

定子电感，*Lq*，单位为 H。

### **Permanent flux linkage constant (Wb)** — 磁链常数 `0.2205`（默认）| 标量

永磁磁链常数，*λpm*，单位为 Wb。

### **Inertia (kgm^2)** — 物理惯量 `0.0027`（默认）| 标量

电机的物理惯量，*J*，单位为
kg.m2。

### **Viscous damping (Nm/rad/s)** — 粘性阻尼 `4.924e-4`（默认）| 标量

电机的粘性阻尼，*F*，单位为 Nm/(rad/s)。

### **Static friction (Nm)** — 静摩擦 `0`（默认）| 标量

电机中的静摩擦，*Tf*，单位为 Nm。

## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

配置 BLDC 系统参数

BLDC Configuration 模块为无刷直流（BLDC）电机生成配置信号。您可以使用此信号更新支持 FPGA 部署的 BLDC 模块（例如 BLDC HDL
模块）的参数。
