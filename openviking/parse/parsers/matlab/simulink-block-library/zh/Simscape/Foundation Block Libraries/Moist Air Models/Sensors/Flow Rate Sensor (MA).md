---
type: simulink-block
title: 'Flow Rate Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Sensors'
documentation_page: 'flowratesensorma'
documentation_source_path: 'ref/flowratesensorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Sensor (MA)

## 端口

### 输出

### **M** — 混合物质量流量，kg/s 物理信号

用于混合物质量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **质量流量** 复选框。

### **V** — 混合物容积流量，m^3/s 物理信号

用于混合物容积流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **容积流量** 复选框。

### **φ** — 混合物能量流量，W 物理信号

用于混合物能量流量测量的物理信号输出端口。

### **Mw** — 水蒸气质量流量，kg/s 物理信号

用于水蒸气质量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **水蒸气质量流量** 复选框。

### **Mg** — 示踪气体质量流量，kg/s 物理信号

用于示踪气体质量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **示踪气体质量流量** 复选框。

### **Md** — 水滴质量流量，kg/s 物理信号

用于水滴质量流量的物理信号输出端口，单位为 kg/s。

#### 依赖关系

要启用此端口，请选中 **水滴质量流量** 复选框。

### 守恒

### **A** — 传感器入口湿空气

湿空气守恒端口。如果空气从端口 **A** 流向端口 **B**，则流量为正。

### **B** — 传感器出口湿空气

湿空气守恒端口。如果空气从端口 **A** 流向端口 **B**，则流量为正。

## 参数

### **质量流量** — 控制用于测量质量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **M**，可用于测量质量流量。

### **容积流量** — 控制用于测量容积流量的输出端口可见性 `Off` (默认) | `On`

选中此复选框将显示输出端口 **V**，可用于测量容积流量。

### **容积流量测量条件** — 指定测量容积流量的条件 `Actual conditions` (默认) | `Standard conditions`

选择传感器是在实际工作条件下还是在标准压力、温度和相对湿度下计算容积流量：

- `Actual conditions` — 传感器使用系统实际工作条件下的湿空气密度计算容积流量。
- `Standard conditions` — 传感器使用标准条件下的湿空气密度计算容积流量。选择此选项后，将显示其他参数，以便您指定标准压力、温度和相对湿度。

#### 依赖关系

要启用此参数，请选中 **容积流量** 复选框。

### **标准压力** — 标准条件下的湿空气压力 `0.10132 MPa` (默认)

标准条件下的湿空气压力。

#### 依赖关系

要启用此参数，请将 **容积流量测量条件** 设置为 `Standard conditions`。

### **标准温度** — 标准条件下的湿空气温度 `20 degC` (默认)

标准条件下的湿空气温度。

#### 依赖关系

要启用此参数，请将 **容积流量测量条件** 设置为 `Standard conditions`。

### **标准相对湿度** — 标准条件下的湿空气相对湿度 `0.65` (默认)

标准条件下的湿空气相对湿度。

#### 依赖关系

要启用此参数，请将 **容积流量测量条件** 设置为 `Standard conditions`。

### **能量流量** — 控制用于测量能量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **φ**，可用于测量能量流量。

### **水蒸气质量流量** — 控制用于测量水蒸气质量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **Mw**，可用于测量水蒸气质量流量。

### **示踪气体质量流量** — 控制用于测量示踪气体质量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **Mg**，可用于测量示踪气体质量流量。

### **水滴质量流量** — 控制用于测量水滴质量流量的输出端口可见性 `Off` (默认) | `On`

选中此复选框将显示输出端口 **Md**，可用于测量水滴质量流量。

## 所属库

Simscape / Foundation Library / Moist Air / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选中 **启用夹带水滴**。

### R2023a：湿空气传感器的可用性增强

在 R2023a 中，单独的 Mass & Energy Flow Rate Sensor (MA) 和 Volumetric Flow Rate Sensor (MA) 模块已合并为单个 Flow Rate Sensor (MA) 模块，可用于测量质量流量、能量流量和容积流量。新模块允许您使用模块参数仅公开特定模型中测量所需的端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会影响兼容性。当您打开现有模型时，其中的 Mass & Energy Flow Rate Sensor (MA) 和 Volumetric Flow Rate Sensor (MA) 模块会自动替换为具有适当公开端口的 Flow Rate Sensor (G) 模块。

但是，如果您在自定义复合组件中使用 Mass & Energy Flow Rate Sensor (MA) 和 Volumetric Flow Rate Sensor (MA) 模块，则需要更新复合组件代码。

| 要更新的传感器模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (MA) | `sensor = foundation.moist_air.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.moist_air.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (MA) | `sensor = foundation.moist_air.sensors.volumetric_flow_sensor;` | `sensor = foundation.moist_air.sensors.flow_sensor(volumetric_flow_measure=true);` |

## 描述

测量湿空气网络中的质量、能量和容积流量

Flow Rate Sensor (MA) 模块表示一个理想传感器，用于测量湿空气网络中的质量流量、能量流量和容积流量。传感器两端的压力、温度、比湿度或示踪气体质量分数均无变化。

由于流量是 Through 变量，模块必须与要测量的组件串联连接。

端口 **A** 和 **B** 的相对方向决定了测量符号。如果流动从端口 **A** 到端口 **B**，则符号为正。交换端口连接会反转测量符号。

有五个物理信号端口可用于输出测量数据：

- 端口 **M** 输出质量流量。
- 端口 **V** 输出容积流量。
- 端口 **φ** 输出能量流量。
- 端口 **Mw** 输出水蒸气质量流量。
- 端口 **Mg** 输出示踪气体质量流量。
- 端口 **Md** 输出水滴质量流量。

这些端口在模块图标上具有条件端口可见性。使用模块参数可以仅公开特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或额外的数据处理。
