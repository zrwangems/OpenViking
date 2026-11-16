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
chinese_source: official
---

# BLDC Configuration

## 端口

### 输出

### **Config** — 模块配置信号 矢量

BLDC 电机的配置信号，包括使用此模块配置的以下参数。

| 配置元素 | | | 单位 |
| --- | --- | --- | --- |
| 极对数 | | | - |
| 每相定子电阻 | | | 欧姆 |
| 定子 d 轴电感 | | | 亨 |
| 定子 q 轴电感 | | | 亨 |
| 永磁磁链常量 | | | 韦伯 |
| 惯量 | | | kgm^2 |
| 反电动势、电动势 | | | Vpk\_LL/krpm  Vpk\_LL 是线电压峰值 |
| 粘性阻尼 | | | N·m/（弧度/秒） |
| 机械输入配置（转矩或转速） | | | - |

**数据类型:** `single`

## 参数

### 模块选项

### **机械输入配置** — 选择端口配置 **转矩** (默认) | **转速**

下表总结了每个端口配置中的输入端口和输出端口。

| 机械输入配置参数值 | | | LdTrq/Spd 端口配置 |
| --- | --- | --- | --- |
| 转矩 | | | **LdTrq** |
| 转速 | | | **Spd** |

### **采样时间(Ts)** — 采样时间，在此采样时间过后模块将再次执行 `1e-6` (默认) | 标量

每两个连续的模块执行实例之间的固定时间间隔（以秒为单位）。

### 参数

### **极对数** — 极对 `4` (默认) | 标量

电机中的极对数 *P*。

### **每相定子电阻(欧姆)** — 定子的电阻 `0.02` (默认) | 标量

每相位的定子电阻 *Rs* ，以欧姆为单位。

### **定子 d 轴电感(H)** — *d* 轴电感 `1.7e-3` (默认) | 标量

定子电感 *Ld* ，以 H 为单位。

### **定子 q 轴电感(H)** — *q* 轴电感 `3.2e-3` (默认) | 标量

定子电感 *Lq* ，以 H 为单位。

### **永磁链常量(Wb)** — 磁链常量 `0.2205` (默认) | 标量

永磁链常量 *λpm* ，以 Wb 为单位。

### **惯量(kgm^2)** — 物理惯量 `0.0027` (默认) | 标量

电机的物理惯量 *J*，以 kg.m2 为单位。

### **粘性阻尼(Nm/rad/s)** — 粘性阻尼 `4.924e-4` (默认) | 标量

电机的粘性阻尼 *F*，以 Nm/（弧度/秒）为单位。

### **静态摩擦(Nm)** — 静态摩擦 `0` (默认) | 标量

电机中的静态摩擦 *Tf* ，以 Nm 为单位。

## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2023b 中推出**

## 描述

配置 BLDC 系统参数

BLDC Configuration 模块可为无刷 DC (BLDC) 机器或电机生成配置信号。您可以使用此信号来更新支持 FPGA 部署的 BLDC 模块的参数，例如 BLDC HDL 模块。
