---
type: simulink-block
title: 'XCP CAN Transport Layer'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / Communication in Simulink'
documentation_page: 'xcpcantransportlayer'
documentation_source_path: 'ug/xcpcantransportlayer.html'
language: zh-CN
chinese_source: official
---

# XCP CAN Transport Layer

## 端口

R2025b 官方文档未提供。

## 参数

### **设备** — CAN 设备 设备列表选项

CAN 设备，从所有连接的 CAN 设备中选择。

### **总线速度** — CAN 总线的速度 数值

以每秒位数为单位的 CAN 总线速度。默认总线速度是由所选设备分配的默认值。

### **采样时间** — 仿真刷新率 `0.01` (默认) | 数值

仿真刷新率，指定为仿真期间模块的采样时间。此值定义 XCP CAN Transport Layer 子系统和底层模块在仿真期间运行的频率。有关仿真采样时间的信息，请参阅硬件接口模型中的计时。如果该模块位于触发子系统内或继承采样时间，请指定值 `-1`。您还可以为采样时间指定一个 MATLAB® 变量。默认值为 `0.01` 仿真秒。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN Simulink Real-Time / XCP / CAN

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

XCP 通信模块支持仅在主机或 Simulink Real-Time™ 目标上运行的具有有限部署可移植性的代码生成。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持和兼容的编译器。

## 版本历史

**在 R2013a 中推出**

## 描述

通过 CAN 传输 XCP 报文

XCP CAN Transport Layer 子系统使用指定的设备传输和接收 XCP 报文。

将此模块与 XCP CAN Data Acquisition 模块结合使用，可采集和分析特定 XCP 报文。将此模块与 XCP CAN Data Stimulation 模块结合使用，可将特定信息发送到模块。

### 其他支持的功能

XCP 通信模块支持使用 Simulink® 加速模式和快速加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。
