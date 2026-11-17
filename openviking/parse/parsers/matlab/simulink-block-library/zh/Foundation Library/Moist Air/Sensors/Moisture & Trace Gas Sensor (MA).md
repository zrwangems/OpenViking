---
type: simulink-block
title: 'Moisture & Trace Gas Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sensors'
documentation_page: 'moisturetracegassensorma'
documentation_source_path: 'ref/moisturetracegassensorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Moisture & Trace Gas Sensor (MA)

## 端口

### 输出

### **W** — 湿度测量，无量纲物理信号

用于湿度测量的物理信号输出端口。要选择您想要测量的量，请使用 **Measured humidity specification** 参数。

#### 依赖关系

要启用此端口，请选中 **Humidity** 复选框，并将 **Measured humidity specification** 参数设置为

- `Relative humidity`
- `Specific humidity`
- `Mole fraction`
- `Humidity ratio`

### **Tw** — 湿球温度测量，K 物理信号

用于湿球温度测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Humidity** 复选框，并将 **Measured humidity specification** 参数设置为 `Wet-bulb temperature`。

### **G** — 微量气体水平测量，无量纲物理信号

用于微量气体水平测量的物理信号输出端口。要选择您想要测量的量，请使用 **Measured trace gas specification** 参数。

#### 依赖关系

要启用此端口，请选中 **Trace gas** 复选框。

### **D** — 水滴与湿空气的质量比，无量纲物理信号

用于水滴与湿空气质量比的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Water droplets** 复选框。

### 守恒

### **A** — 传感器入口湿空气

湿空气守恒端口。将此端口连接到湿空气网络中您想要测量湿度和微量气体水平的节点。

## 参数

### **Humidity** — 控制用于测量湿度的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **W** 或 **Tw**，使您能够测量由 **Measured humidity specification** 参数值指定的量。

### **Measured humidity specification** — 选择要测量的湿度属性 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择要测量的属性：

- `Relative humidity` ― 物理信号端口 **W** 报告相对湿度。
- `Specific humidity` ― 物理信号端口 **W** 报告比湿度。
- `Mole fraction` ― 物理信号端口 **W** 报告水蒸气摩尔分数。
- `Humidity ratio` ― 物理信号端口 **W** 报告湿度比。
- `Wet-bulb temperature` ― 物理信号端口 **Tw** 报告湿球温度。

### **Trace gas** — 控制用于测量微量气体的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **G**，使您能够测量由 **Measured trace gas specification** 参数值指定的量。

### **Measured trace gas specification** — 选择要测量的微量气体属性 `Mass fraction`（默认）| `Mole fraction`

选择要测量的属性：

- `Mass fraction` ― 物理信号端口 **G** 报告微量气体质量分数。
- `Mole fraction` ― 物理信号端口 **G** 报告微量气体摩尔分数。

### **Water droplets** — 控制用于测量水滴的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **D**，使您能够测量水滴与湿空气的质量比。

## 所属库

Simscape / Foundation Library / Moist Air / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：从 Humidity & Trace Gas Sensor (MA) 重命名

Humidity & Trace Gas Sensor (MA) 模块现在是 Moisture & Trace Gas Sensor (MA) 模块。

### R2024b：模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2023a：使用湿球温度测量湿度

该模块现在提供了一个使用湿球温度测量湿度的选项。
湿球温度是一种测量湿度的方法，涉及将湿布包裹在温度计上，以便测量包括蒸发导致能量损失在内的温度。传统干湿球湿度计以湿球温度的形式输出数据。

此外，具有多个输出端口的湿空气传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅暴露特定模型中测量所需的端口。

这些更改没有兼容性影响。

## 描述

测量湿空气网络中的湿度、水滴和痕量气体水平

Moisture & Trace Gas Sensor (MA) 模块测量湿空气网络中的湿度、水滴和痕量气体量。传感器中没有质量或能量流。

物理信号端口 **W**、**Tw**、**D** 和 **G** 分别报告在端口 **A** 处测得的湿度、湿球温度、水滴质量比和痕量气体水平。使用模块参数控制端口可见性并选择要测量的量。将这些端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或附加数据处理。

传感器测量值对应于被测节点上游的湿度和痕量气体水平。例如，如果 Moisture & Trace Gas Sensor (MA) 的端口 **A** 连接到管道 1 和管道 2 之间的节点，并且湿空气从管道 1 流向管道 2，则在端口 **A** 处测得的湿度和痕量气体水平是管道 1 中湿空气体积的湿度和痕量气体水平。如果气流随后改变方向并从管道 2 流向管道 1，则在端口 **A** 处测得的湿度和痕量气体水平是管道 2 中湿空气体积的湿度和痕量气体水平。如果两个湿空气体积的湿度和痕量气体水平不同，则测量值会在流动方向切换时发生变化。如果有两个或多个上游流动路径在节点处汇合，则节点处的湿度和痕量气体水平测量值表示基于汇合流理想混合的加权平均值。
