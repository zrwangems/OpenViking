---
type: simulink-block
title: 'Pressure & Temperature Sensor (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Liquid Models / Sensors'
documentation_page: 'pressuretemperaturesensortl'
documentation_source_path: 'ref/pressuretemperaturesensortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure & Temperature Sensor (TL)

## 端口

### 输出

### **Pa** — 绝对压力测量，Pascal (Pa) 物理信号

绝对压力测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Absolute`，选中 **压力** 复选框，并将 **压力类型** 参数设置为 `Absolute pressure`。

### **Pg** — 表压测量，Pa 物理信号

表压测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Absolute`，选中 **压力** 复选框，并将 **压力类型** 参数设置为 `Gauge pressure`。

### **P** — 压力差测量，Pa 物理信号

压力差测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Difference`，并选中 **压力** 复选框。

### **T** — 温度测量，K 物理信号

温度测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **温度** 复选框。

### 守恒

### **A** — 传感器入口热流体

热流体守恒端口。使用此端口测量绝对压力或温度。

### **B** — 传感器出口热流体

热流体守恒端口。当传感器测量绝对压力或温度时，此端口隐藏，因为传感器包含一个隐式参考节点。启用此端口可测量模型中两个节点之间的相对压力或温度。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

#### 依赖关系

要启用此端口，请将 **测量参考** 参数设置为 `Difference`。

## 参数

### **测量参考** — 在绝对测量和相对测量之间选择 `Absolute`（默认）| `Difference`

在绝对测量和相对测量之间选择：

- `Absolute` — 传感器测量端口 **A** 处的压力和温度。传感器包含一个隐式参考节点，这意味着您只需要一个端口即可进行绝对测量。
- `Difference` — 传感器测量模型中两个节点之间的压力或温度差。选择此选项会在模块图标上显示端口 **B**。

### **压力** — 控制用于测量压力的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **Pa**、**Pg** 或 **P**，以便测量压力。

### **压力类型** — 在绝对压力和表压之间选择 `Absolute pressure`（默认）| `Gauge pressure`

选择传感器测量绝对压力还是表压：

- `Absolute pressure` — 传感器测量端口 **A** 处的绝对压力。选择此选项会在模块图标上显示端口 **Pa**。
- `Gauge pressure` — 传感器测量端口 **A** 处的表压。选择此选项会在模块图标上显示端口 **Pg**。

#### 依赖关系

要启用此参数，请将 **测量参考** 设置为 `Absolute`，并选中 **压力** 复选框。

### **温度** — 控制用于测量温度的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **T**，以便测量温度。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023a：热流体传感器可用性增强

具有多个输出端口的热流体传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

此外，Pressure & Temperature Sensor (TL) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才显示第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到 Absolute Reference (TL) 模块。现在不再需要这样做，因为您可以通过将 **测量参考** 参数设置为 `Absolute` 来进行绝对测量，但具有这些连接的现有模型仍会像以前一样工作。

在模型中使用 Pressure & Temperature Sensor (TL) 模块不会产生兼容性影响。但是，如果在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.thermal_liquid.sensors.pressure_temperature_sensor;` | `sensor = foundation.thermal_liquid.sensors.pressure_temperature_sensor(reference=foundation.enum.MeasurementReference.difference, temperature=true);` |

## 描述

测量热流体网络中的压力和温度

Pressure & Temperature Sensor (TL) 模块表示一个理想传感器，用于测量热流体网络中的压力和温度。没有质量或能量流过该传感器。

该传感器包含一个隐式参考节点，这意味着您只需要一个端口（端口 **A**）即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才显示第二个端口（端口 **B**）。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

有四个物理信号端口可用于输出测量数据：

- 端口 **Pa** 输出绝对压力。
- 端口 **Pg** 输出表压。
- 端口 **P** 输出传感器两端的压力差。
- 端口 **T** 输出温度。

这些端口在模块图标上具有条件端口可见性。使用模块参数仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或附加数据处理。
