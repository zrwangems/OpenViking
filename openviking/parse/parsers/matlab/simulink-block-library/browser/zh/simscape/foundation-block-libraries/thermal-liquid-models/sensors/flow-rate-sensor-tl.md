---
type: simulink-block
title: 'Flow Rate Sensor (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Liquid Models / Sensors'
documentation_page: 'flowratesensortl'
documentation_source_path: 'ref/flowratesensortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Sensor (TL)

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

### **A** — 传感器入口热液体

热液体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正。

### **B** — 传感器出口热液体

热液体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正。

## 参数

### **质量流量** — 控制用于测量质量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **M**，可用于测量质量流量。

### **体积流量** — 控制用于测量体积流量的输出端口可见性 `Off` (默认) | `On`

选中此复选框将显示输出端口 **V**，可用于测量体积流量。

### **能量流量** — 控制用于测量能量流量的输出端口可见性 `On` (默认) | `Off`

选中此复选框将显示输出端口 **φ**，可用于测量能量流量。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2023a：热液体传感器的易用性增强

在 R2023a 中，单独的 Mass & Energy Flow Rate Sensor (TL) 和 Volumetric Flow Rate Sensor (TL) 模块已合并为一个 Flow Rate Sensor (TL) 模块，可用于测量质量流量、能量流量和体积流量。新模块允许使用模块参数仅在特定模型中显示测量所需的端口，这有助于减少杂乱并改进模块图布局。

当在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。打开现有模型时，其中的 Mass & Energy Flow Rate Sensor (TL) 和 Volumetric Flow Rate Sensor (TL) 模块会自动替换为已显示相应端口的 Flow Rate Sensor (TL) 模块。

但是，如果在自定义复合组件中使用 Mass & Energy Flow Rate Sensor (TL) 和 Volumetric Flow Rate Sensor (TL) 模块，则需要更新复合组件代码。

| 要更新的传感器模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (TL) | `sensor = foundation.thermal_liquid.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.thermal_liquid.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (TL) | `sensor = foundation.thermal_liquid.sensors.volumetric_flow_sensor;` | `sensor = foundation.thermal_liquid.sensors.flow_sensor(volumetric_flow_measure=true);` |

## 描述

测量热液体网络中的质量流量、能量流量和体积流量

Flow Rate Sensor (TL) 模块表示一个理想传感器，用于测量热液体网络中的质量流量、能量流量和体积流量。传感器两端的压力和温度没有变化。

由于流量是 Through 变量，该模块必须与被测量组件串联连接。

端口 **A** 和 **B** 的相对方向确定测量符号。如果流体从端口 **A** 流向端口 **B**，则符号为正。交换端口连接会反转测量符号。

有三个物理信号端口可用于输出测量数据：

- 端口 **M** 输出质量流量。
- 端口 **V** 输出体积流量。
- 端口 **φ** 输出能量流量。

这些端口在模块图标上具有条件端口可见性。使用模块参数可以仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或其他数据处理。
