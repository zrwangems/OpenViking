---
type: simulink-block
title: 'Flow Rate Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'flowratesensor2p'
documentation_source_path: 'ref/flowratesensor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Sensor (2P)

## 端口
```yaml
ports:
- name: M
  summary: 质量流量测量，kg/s 物理信号
  direction: output
- name: V
  summary: 体积流量，m^3/s 物理信号
  direction: output
- name: φ
  summary: 能量流量测量，W 物理信号
  direction: output
- name: A
  summary: 传感器入口两相流体
  direction: conserving
- name: B
  summary: 传感器出口两相流体
  direction: conserving
```

### 输出

### **M** — 质量流量测量，kg/s 物理信号

用于质量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Mass flow rate** 复选框。

### **V** — 体积流量，m^3/s 物理信号

用于体积流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Volumetric flow rate** 复选框。

### **φ** — 能量流量测量，W 物理信号

用于能量流量测量的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Energy flow rate** 复选框。

### 守恒端口

### **A** — 传感器入口两相流体

两相流体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正值。

### **B** — 传感器出口两相流体

两相流体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正值。
## 参数
```yaml
parameters:
- name: Mass flow rate
  summary: 控制用于测量质量流量的输出端口可见性 On（默认）| Off
  group: ''
- name: Volumetric flow rate
  summary: 控制用于测量体积流量的输出端口可见性 Off（默认）| On
  group: ''
- name: Energy flow rate
  summary: 控制用于测量能量流量的输出端口可见性 On（默认）| Off
  group: ''
```

### **Mass flow rate** — 控制用于测量质量流量的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **M**，可用于测量质量流量。

### **Volumetric flow rate** — 控制用于测量体积流量的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **V**，可用于测量体积流量。

### **Energy flow rate** — 控制用于测量能量流量的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **φ**，可用于测量能量流量。
## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2023a：热液体传感器可用性增强

在 R2023a 中，单独的 Mass & Energy Flow Rate Sensor (2P) 和 Volumetric Flow Rate Sensor (2P) 模块已合并为单个 Flow Rate Sensor (2P) 模块，可用于测量质量流量、能量流量和体积流量。新模块允许您使用模块参数仅显示特定模型中测量所需的端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，其中的 Mass & Energy Flow Rate Sensor (2P) 和 Volumetric Flow Rate Sensor (2P) 模块会自动替换为具有适当端口的 Flow Rate Sensor (2P) 模块。

但是，如果您在自定义复合组件中使用 Mass & Energy Flow Rate Sensor (2P) 和 Volumetric Flow Rate Sensor (2P) 模块，则需要更新复合组件代码。

| 要更新的传感器模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (2P) | `sensor = foundation.two_phase_fluid.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.two_phase_fluid.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (2P) | `sensor = foundation.two_phase_fluid.sensors.volumetric_flow_sensor;` | `sensor = foundation.two_phase_fluid.sensors.flow_sensor(volumetric_flow_measure=true);` |

## 描述

测量两相流体网络中的质量流量、能量流量和体积流量

Flow Rate Sensor (2P) 模块表示一个理想传感器，用于测量两相流体网络中的质量流量、能量流量和体积流量。传感器两端的压力和温度不发生变化。

由于流量是通变量（Through variables），该模块必须与被测量的组件串联连接。

端口 **A** 和 **B** 的相对方向决定了测量符号。如果流体从端口 **A** 流向端口 **B**，则符号为正。交换端口连接会反转测量符号。

有三个物理信号端口可用于输出测量数据：

- 端口 **M** 输出质量流量。
- 端口 **V** 输出体积流量。
- 端口 **φ** 输出能量流量。

这些端口在模块图标上具有条件端口可见性。使用模块参数可以仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出的物理信号转换为 Simulink® 信号，例如用于绘图或额外的数据处理。
