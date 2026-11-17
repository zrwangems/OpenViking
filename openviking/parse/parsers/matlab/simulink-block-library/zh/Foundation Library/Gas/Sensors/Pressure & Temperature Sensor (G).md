---
type: simulink-block
title: 'Pressure & Temperature Sensor (G)'
family: 'gas'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'pressuretemperaturesensorg'
documentation_source_path: 'ref/pressuretemperaturesensorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure & Temperature Sensor (G)

## 端口

### 输出

### **Pa** — 绝对压力测量，单位为 Pascal (Pa) 的物理信号

用于绝对压力测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Absolute`，选中 **压力** 复选框，并将 **压力类型** 参数设置为 `Absolute pressure`。

### **Pg** — 表压测量，Pa 物理信号

用于表压测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Absolute`，选中 **压力** 复选框，并将 **压力类型** 参数设置为 `Gauge pressure`。

### **P** — 压差测量，Pa 物理信号

用于压差测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Difference`，并选中 **压力** 复选框。

### **T** — 温度测量，K 物理信号

用于温度测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **温度** 复选框。

### 守恒

### **A** — 传感器入口气体

气体守恒端口。使用此端口测量绝对压力或温度。

### **B** — 传感器出口气体

气体守恒端口。当传感器测量绝对压力或温度时，此端口隐藏，因为传感器包含一个隐式参考节点。启用此端口可测量模型中两个节点之间的相对压力或温度。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Difference`。

## 参数

### **测量参考** — 在绝对测量和相对测量之间选择 `Absolute` (默认) | `Difference`

在绝对测量和相对测量之间选择：

- `Absolute` — 传感器在端口 **A** 测量压力和温度。传感器包含一个隐式参考节点，这意味着进行绝对测量只需要一个端口。
- `Difference` — 传感器测量模型中两个节点之间的压力或温度差。选择此选项会在模块图标上显示端口 **B**。

### **压力** — 控制用于测量压力的输出端口可见性 `On` (默认) | `Off`

选中此复选框会显示输出端口 **Pa**、**Pg** 或 **P**，以便测量压力。

### **压力类型** — 在绝对压力和表压之间选择 `Absolute pressure` (默认) | `Gauge pressure`

选择传感器测量绝对压力还是表压：

- `Absolute pressure` — 传感器在端口 **A** 测量绝对压力。选择此选项会在模块图标上显示端口 **Pa**。
- `Gauge pressure` — 传感器在端口 **A** 测量表压。选择此选项会在模块图标上显示端口 **Pg**。

#### 依赖关系

要启用此参数，请将 **测量参考** 设置为 `Absolute`，并选中 **压力** 复选框。

### **温度** — 控制用于测量温度的输出端口可见性 `Off` (默认) | `On`

选中此复选框会显示输出端口 **T**，从而可以测量温度。

## 所属库

Simscape / Foundation Library / Gas / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2016b 中引入**

### R2023a：气体传感器可用性增强

具有多个输出端口的气体传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

此外，Pressure & Temperature Sensor (G) 模块现在包含一个隐式参考节点，这意味着进行压力或温度的绝对测量只需要一个端口。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要显示第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，需要将端口 **B** 连接到 Absolute Reference (G) 模块。现在不再需要这样做，因为您可以通过将 **测量参考** 参数设置为 `Absolute` 来进行绝对测量，但包含这些连接的现有模型仍像以前一样工作。

在模型中使用 Pressure & Temperature Sensor (G) 模块时没有兼容性影响。但是，如果您在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.gas.sensors.pressure_temperature_sensor;` | `sensor = foundation.gas.sensors.pressure_temperature_sensor(reference=foundation.enum.MeasurementReference.difference, temperature=true);` |

## 描述

测量气体网络中的压力和温度

Pressure & Temperature Sensor (G) 模块表示一个理想传感器，用于测量气体网络中的压力和温度。没有质量流量或能量流量通过该传感器。

传感器包含一个隐式参考节点，这意味着进行压力或温度的绝对测量只需要一个端口，即端口 **A**。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要显示第二个端口，即端口 **B**。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

温度测量与压力测量不同，因为能量流量取决于流动方向。温度测量表示所测量节点的上游温度。例如，如果 Pressure & Temperature Sensor (G) 的端口 **A** 连接到 pipe 1 和 pipe 2 之间的节点，并且气体从 pipe 1 流向 pipe 2，则在端口 **A** 测得的温度是 pipe 1 中气体体积的温度。如果气体随后改变方向并从 pipe 2 流向 pipe 1，则在端口 **A** 测得的温度是 pipe 2 中气体体积的温度。如果两个气体体积的温度不同，则当流动方向改变时，测得的温度会发生变化。如果有两条或更多上游流动路径在节点处汇合，则该节点处的温度测量表示基于汇合流动理想混合的加权平均值。

有四个物理信号端口可用于输出测量数据：

- 端口 **Pa** 输出绝对压力。
- 端口 **Pg** 输出表压。
- 端口 **P** 输出传感器两端的压差。
- 端口 **T** 输出温度。

这些端口在模块图标上具有条件端口可见性。使用模块参数仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或额外数据处理。
