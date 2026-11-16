---
type: simulink-block
title: 'Temperature Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sensors'
documentation_page: 'temperaturesensor'
documentation_source_path: 'ref/temperaturesensor.html'
language: zh-CN
chinese_source: official
---

# Temperature Sensor

## 端口

### 输出

### **T** — 温度测量 (K) 物理信号

用于温度测量的物理信号输出端口。
### 守恒

### **A** — 传感器入口 热

热守恒端口。

### **B** — 传感器出口 热

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

#### 依赖关系

要启用此端口，请将**测量参考**参数设置为**差值**。

## 参数

### **测量参考** — 在绝对测量和相对测量之间进行选择 **差值** (默认) | **绝对值**

在绝对测量和相对测量之间进行选择：

- **差值** - 传感器测量模型中两个节点之间的温差。选择此选项会在模块图标上公开端口 **B**。
- **绝对值** - 传感器测量端口 **A** 处的绝对温度。传感器包含一个隐式引用节点，这意味着，您只需一个端口即可进行绝对值测量。选择此选项会在模块图标上隐藏端口 **B**。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sensors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007b 中推出**

### R2023a: 传感器的可用性增强

Temperature Sensor 模块现在包含一个隐式引用节点，这意味着，您只需一个端口即可测量绝对温度值。

此更改不会影响兼容性。

## 描述

理想的温度传感器

Temperature Sensor 模块表示一个理想的温度传感器，即一种测量节点处的绝对温度或两个节点之间的温差而不吸取任何热量的设备。

连接端 **A** 和 **B** 是热守恒端口，连接到监测温度的两个点。端口 **T** 是输出温差值的物理信号端口。

此模块的正方向是从端口 **A** 到端口 **B**。所测量的温度确定为 *T = TA – TB*。

要测量某一节点处的绝对温度，请将**测量参考**参数设置为**绝对**并将端口 **A** 连接到所测量的节点。
