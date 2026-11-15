---
type: simulink-block
title: 'Flow Rate Sensor (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Gas Models / Sensors'
documentation_page: 'flowratesensorg'
documentation_source_path: 'ref/flowratesensorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Sensor (G)

## 端口

### 输出

### **M** — 质量流量测量，kg/s 物理信号

用于质量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **质量流量** 复选框。

### **V** — 体积流量，m^3/s 物理信号

用于体积流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **体积流量** 复选框。

### **φ** — 能量流量测量，W 物理信号

用于能量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **能量流量** 复选框。
### 守恒

### **A** — 传感器入口气体

气体守恒端口。如果气体从端口 **A** 流向端口 **B**，则流量为正。

### **B** — 传感器出口气体

气体守恒端口。如果气体从端口 **A** 流向端口 **B**，则流量为正。

## 参数

### **质量流量** — 控制用于测量质量流量的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **M**，可用于测量质量流量。

### **体积流量** — 控制用于测量体积流量的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **V**，可用于测量体积流量。

### **体积流量测量条件** — 指定测量体积流量的条件 `Actual conditions`（默认）| `Standard conditions`

选择传感器是在实际工作条件下还是在标准压力和温度下计算体积流量：

- `Actual conditions` — 传感器使用系统实际工作条件下的密度计算体积流量。
- `Standard conditions` — 传感器使用标准条件下的密度计算体积流量。选择此选项后，将提供额外的参数，可用于指定标准压力和温度。

#### 依赖关系

要启用此参数，请选中 **体积流量** 复选框。

### **标准压力** — 标准条件下的气体压力 `0.10132 MPa`（默认）

标准条件下的气体压力。

#### 依赖关系

要启用此参数，请将 **体积流量测量条件** 设置为 `Standard conditions`。

### **标准温度** — 标准条件下的气体温度 `20 degC`（默认）

标准条件下的气体温度。

#### 依赖关系

要启用此参数，请将 **体积流量测量条件** 设置为 `Standard conditions`。

### **能量流量** — 控制用于测量能量流量的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **φ**，可用于测量能量流量。

## 所属库

Simscape / Foundation Library / Gas / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2023a: 气体传感器的可用性增强

在 R2023a 中，单独的 Mass & Energy Flow Rate Sensor (G) 和 Volumetric Flow Rate Sensor (G) 模块已合并为单个 Flow Rate Sensor (G) 模块，可用于测量质量流量、能量流量和体积流量。新模块允许您使用模块参数仅显示特定模型中测量所需的端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会对兼容性产生影响。打开现有模型时，其中的 Mass & Energy Flow Rate Sensor (G) 和 Volumetric Flow Rate Sensor (G) 模块会自动替换为具有相应已显示端口的 Flow Rate Sensor (G) 模块。

但是，如果您在自定义复合组件中使用 Mass & Energy Flow Rate Sensor (G) 和 Volumetric Flow Rate Sensor (G) 模块，则需要更新复合组件代码。

| 要更新的传感器模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (G) | `sensor = foundation.gas.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.gas.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (G) | `sensor = foundation.gas.sensors.volumetric_flow_sensor;` | `sensor = foundation.gas.sensors.flow_sensor(volumetric_flow_measure=true);` |

此外，当传感器测量体积流量时，您现在可以选择是使用标准压力和温度下的密度，还是使用系统的实际工作条件来计算体积流量。在以前的版本中，Volumetric Flow Rate Sensor (G) 模块只能使用实际工作条件。此更改不会对兼容性产生影响，因为默认模块行为保持不变。

## 描述

测量气体网络中的质量流量、能量流量和体积流量

Flow Rate Sensor (G) 模块表示一个理想传感器，用于测量气体网络中的质量流量、能量流量和体积流量。能量流量是总焓的平流。传感器两端没有压力或温度变化。

由于流量是 Through 变量，模块必须与被测组件串联连接。

端口 **A** 和 **B** 的相对方向决定了测量符号。如果流动从端口 **A** 到端口 **B**，则符号为正。交换端口连接会反转测量符号。

有三个物理信号端口可用于输出测量数据：

- 端口 **M** 输出质量流量。
- 端口 **V** 输出体积流量。
- 端口 **φ** 输出能量流量。

这些端口在模块图标上具有条件端口可见性。使用模块参数仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出的物理信号转换为 Simulink® 信号，例如用于绘图或额外的数据处理。
