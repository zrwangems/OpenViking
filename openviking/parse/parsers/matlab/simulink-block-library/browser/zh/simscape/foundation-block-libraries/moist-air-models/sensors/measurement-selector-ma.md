---
type: simulink-block
title: 'Measurement Selector (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Sensors'
documentation_page: 'measurementselectorma'
documentation_source_path: 'ref/measurementselectorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Measurement Selector (MA)

## 端口

### 输入

### **F** — 包含压力、温度、湿度和痕量气体水平数据的向量物理信号 physical signal vector

将此端口连接到具有有限内部湿空气体积的模块的物理信号输出端口 **F** 以访问数据。具有有限湿空气体积的模块有一个物理信号输出端口 **F**，该端口输出一个向量信号，其中包含组件内部的压力（以 Pa 为单位）、温度（以 K 为单位）、湿度、水滴质量比和痕量气体水平测量值。使用 Measurement Selector (MA) 模块解包此向量信号。
### 输出

### **P** — 压力测量，Pa 物理信号

用于压力测量的物理信号输出端口。

### **T** — 温度测量，K 物理信号

用于温度测量的物理信号输出端口。

### **W** — 湿度水平测量，unitless 物理信号

用于湿度水平测量的物理信号输出端口。要选择要测量的量，请使用 **Measured humidity specification** 参数。

### **G** — 痕量气体水平测量，unitless 物理信号

用于痕量气体水平测量的物理信号输出端口。要选择要测量的量，请使用 **Measured trace gas specification** 参数。

### **D** — 水滴与湿空气的质量比，unitless 物理信号

用于水滴与湿空气质量比的物理信号输出端口。

## 参数

### **Measured humidity specification** — 选择要测量的湿度属性 `Relative humidity`（默认） | `Specific humidity` | `Mole fraction` | `Humidity ratio`

选择要测量的属性：

- `Relative humidity` ― 物理信号端口 **W** 报告相对湿度。
- `Specific humidity` ― 物理信号端口 **W** 报告比湿度。
- `Mole fraction` ― 物理信号端口 **W** 报告水蒸气摩尔分数。
- `Humidity ratio` ― 物理信号端口 **W** 报告湿度比。

### **Measured trace gas specification** — 选择要测量的痕量气体属性 `Mass fraction`（默认） | `Mole fraction`

选择要测量的属性：

- `Mass fraction` ― 物理信号端口 **G** 报告痕量气体质量分数。
- `Mole fraction` ― 物理信号端口 **G** 报告痕量气体摩尔分数。

## 所属库

Simscape / Foundation Library / Moist Air / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

测量湿空气内部体积中的压力、温度、湿度和痕量气体水平

Measurement Selector (MA) 模块允许您访问具有有限湿空气体积的模块内部的压力、温度、湿度水平和痕量气体水平测量值。没有质量或能量流过传感器。

具有有限湿空气体积的模块包含一个内部节点，该节点表示组件内部的湿空气体积。有关这些模块的完整列表，请参阅 Blocks with Moist Air Volume。常规传感器无法连接到此内部节点。因此，每个具有有限湿空气体积的模块都有一个物理信号输出端口 **F**，该端口输出一个向量信号，其中包含组件内部的压力（以 Pa 为单位）、温度（以 K 为单位）、湿度、水滴质量比和痕量气体水平测量值。有关详细信息，请参阅 Measuring Moisture and Trace Gas Levels。

使用 Measurement Selector (MA) 模块解包该向量信号，并为压力值和温度值重新指定单位。将 Measurement Selector (MA) 模块的输入端口 **F** 连接到具有有限内部湿空气体积的模块的物理信号输出端口 **F**，以访问数据。

将 Measurement Selector (MA) 模块的输出端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或其他数据处理。使用连接到端口 **P** 和 **T** 的 PS-Simulink Converter 模块的 **Output signal unit** 参数，分别将单位重新指定给压力值和温度值。
