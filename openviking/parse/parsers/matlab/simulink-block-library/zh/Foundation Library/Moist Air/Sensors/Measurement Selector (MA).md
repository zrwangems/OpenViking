---
type: simulink-block
title: 'Measurement Selector (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sensors'
documentation_page: 'measurementselectorma'
documentation_source_path: 'ref/measurementselectorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Measurement Selector (MA)

## 端口
```yaml
ports:
- name: F
  summary: 包含压力、温度、湿度和微量气体水平数据的向量物理信号 物理信号向量
  direction: input
- name: P
  summary: 压力测量值，Pa 物理信号
  direction: output
- name: T
  summary: 温度测量值，K 物理信号
  direction: output
- name: W
  summary: 湿度水平测量值，无量纲 物理信号
  direction: output
- name: G
  summary: 微量气体水平测量值，无量纲 物理信号
  direction: output
- name: D
  summary: 水滴与湿空气的质量比，无量纲 物理信号
  direction: output
```

### 输入

### **F** — 包含压力、温度、湿度和微量气体水平数据的向量物理信号 物理信号向量

将此端口连接到具有有限内部湿空气体积的模块的物理信号输出端口 **F** 以访问数据。具有有限湿空气体积的模块有一个物理信号输出端口 **F**，它输出一个向量信号，包含组件内部的压力（单位为 Pa）、温度（单位为 K）、湿度、水滴质量比和微量气体水平测量值。使用 Measurement Selector (MA) 模块来解包此向量信号。
### 输出

### **P** — 压力测量值，Pa 物理信号

压力测量值的物理信号输出端口。

### **T** — 温度测量值，K 物理信号

温度测量值的物理信号输出端口。

### **W** — 湿度水平测量值，无量纲 物理信号

湿度水平测量值的物理信号输出端口。要选择您想要测量的量，请使用 **Measured humidity specification** 参数。

### **G** — 微量气体水平测量值，无量纲 物理信号

微量气体水平测量值的物理信号输出端口。要选择您想要测量的量，请使用 **Measured trace gas specification** 参数。

### **D** — 水滴与湿空气的质量比，无量纲 物理信号

水滴与湿空气质量比的物理信号输出端口。
## 参数
```yaml
parameters:
- name: Measured humidity specification
  summary: 选择要测量的湿度属性 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio
  group: ''
- name: Measured trace gas specification
  summary: 选择要测量的微量气体属性 Mass fraction（默认）| Mole fraction
  group: ''
```

### **Measured humidity specification** — 选择要测量的湿度属性 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio`

选择要测量的属性：

- `Relative humidity` ― 物理信号端口 **W** 报告相对湿度。
- `Specific humidity` ― 物理信号端口 **W** 报告比湿度。
- `Mole fraction` ― 物理信号端口 **W** 报告水蒸气摩尔分数。
- `Humidity ratio` ― 物理信号端口 **W** 报告湿度比。

### **Measured trace gas specification** — 选择要测量的微量气体属性 `Mass fraction`（默认）| `Mole fraction`

选择要测量的属性：

- `Mass fraction` ― 物理信号端口 **G** 报告微量气体质量分数。
- `Mole fraction` ― 物理信号端口 **G** 报告微量气体摩尔分数。
## 所属库

Simscape / Foundation Library / Moist Air / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b: 对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

测量湿空气内部体积中的压力、温度、湿度和微量气体水平

Measurement Selector (MA) 模块允许您访问具有有限湿空气体积的模块内部的压力、温度、湿度水平和微量气体水平测量值。传感器中没有质量或能量流动。

具有有限湿空气体积的模块包含一个内部节点，该节点表示组件内部的湿空气体积。有关这些模块的完整列表，请参阅 Blocks with Moist Air Volume。常规传感器无法连接到该内部节点。因此，每个具有有限湿空气体积的模块都有一个物理信号输出端口 **F**，该端口输出一个向量信号，其中包含组件内部的压力（单位为 Pa）、温度（单位为 K）、湿度、水滴质量比和微量气体水平测量值。有关更多信息，请参阅 Measuring Moisture and Trace Gas Levels。

使用 Measurement Selector (MA) 模块来解包向量信号并重新分配压力和温度值的单位。将 Measurement Selector (MA) 模块的输入端口 **F** 连接到具有有限内部湿空气体积的模块的物理信号输出端口 **F**，以访问数据。

将 Measurement Selector (MA) 模块的输出端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或额外的数据处理。使用连接到端口 **P** 和 **T** 的 PS-Simulink Converter 模块的 **Output signal unit** 参数，分别重新分配压力和温度值的单位。
