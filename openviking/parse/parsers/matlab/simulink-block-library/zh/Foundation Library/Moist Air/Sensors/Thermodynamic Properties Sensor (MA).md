---
type: simulink-block
title: 'Thermodynamic Properties Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sensors'
documentation_page: 'thermodynamicpropertiessensorma'
documentation_source_path: 'ref/thermodynamicpropertiessensorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermodynamic Properties Sensor (MA)

## 端口
```yaml
ports:
- name: h
  summary: 比焓测量，J/kg 物理信号
  direction: output
- name: ρ
  summary: 密度测量，kg/m^3 物理信号
  direction: output
- name: cp
  summary: 定压比热测量，J/(kg\*K) 物理信号
  direction: output
- name: s
  summary: 比熵测量，J/(kg\*K) 物理信号
  direction: output
- name: A
  summary: 传感器入口湿空气
  direction: output
```

### 输出

### **h** — 比焓测量，J/kg 物理信号

用于测量空气混合物比焓的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Enthalpy** 复选框。

### **ρ** — 密度测量，kg/m^3 物理信号

用于测量空气混合物密度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Density** 复选框。

### **cp** — 定压比热测量，J/(kg\*K) 物理信号

用于测量空气混合物定压比热的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Specific heat** 复选框。

### **s** — 比熵测量，J/(kg\*K) 物理信号

用于测量空气混合物比熵的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Entropy** 复选框。
### 守恒

### **A** — 传感器入口湿空气

湿空气守恒端口。将此端口连接到湿空气网络中您想要测量热力学属性的节点。
## 参数
```yaml
parameters:
- name: Measurements based on
  summary: 选择传感器输出的测量约定 Unit mass of moist air mixture（默认）| Unit mass of dry air and trace gas
  group: ''
- name: Enthalpy
  summary: 控制用于测量比焓的输出端口可见性 Off（默认）| On
  group: ''
- name: Enthalpy reference state
  summary: 选择比焓输出的参考状态 As provided in Moist Air Properties (MA) block（默认）| 0 degC with water as vapor | 0 degC with water
    as liquid
  group: ''
- name: Density
  summary: 控制用于测量密度的输出端口可见性 On（默认）| Off
  group: ''
- name: Specific heat
  summary: 控制用于测量比热的输出端口可见性 Off（默认）| On
  group: ''
- name: Entropy
  summary: 控制用于测量比熵的输出端口可见性 Off（默认）| On
  group: ''
```

### **Measurements based on** — 选择传感器输出的测量约定 `Unit mass of moist air mixture`（默认）| `Unit mass of dry air and trace gas`

选择测量值是按整个空气混合物的质量归一化，还是仅按干空气和痕量气体的质量归一化：

- `Unit mass of moist air mixture` —
  对于每个热力学属性，湿空气体积中该属性的测量质量除以湿空气混合物的质量。
- `Unit mass of dry air and trace gas`
  — 对于每个热力学属性，湿空气体积中该属性的测量质量除以干空气和痕量气体的质量（不包括水蒸气的质量）。当您需要将测量值与 ASHRAE 图表和数据进行比较时，请使用此选项。

### **Enthalpy** — 控制用于测量比焓的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **h**，可用于测量空气混合物的比焓。

### **Enthalpy reference state** — 选择比焓输出的参考状态 `As provided in Moist Air Properties (MA) block`（默认）| `0 degC with water as vapor` | `0 degC with water as liquid`

选择比焓输出的参考状态：

- `As provided in Moist Air Properties (MA)
  block` — 传感器直接基于
  Moist Air Properties (MA) 模块中提供的焓向量输出混合物焓，
  不做任何调整。此选项仅供参考，因为库模块使用调整后的值。
- `0 degC with water as vapor` —
  传感器输出调整为参考状态的混合物焓，即在 0 degC 时为 0
  kJ/kg。这些是库模块中使用的值，并显示在仿真数据日志中。
- `0 degC with water as liquid` —
  传感器输出调整为液态水在 0 degC 时具有 0 kJ/kg
  参考状态的混合物焓。在这种情况下，水蒸气的焓包括参考状态下的汽化焓或潜热。这些是壁面冷凝计算中使用的值。

#### 依赖

要启用此参数，请选中 **Enthalpy** 复选框。

### **Density** — 控制用于测量密度的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **ρ**，可用于测量空气混合物的密度。

### **Specific heat** — 控制用于测量比热的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **cp**，可用于测量空气混合物的比热。

### **Entropy** — 控制用于测量比熵的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **s**，可用于测量空气混合物的比熵。
## 所属库

Simscape / Foundation Library / Moist Air / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023b：湿空气域中比焓的一致参考状态

为确保湿空气混合物的一致性，所有比焓必须具有相同的参考温度。因此，从 R2023b 开始，湿空气域使用 0 degC 的一致参考温度。当您在湿空气属性 (MA) 模块中输入比焓向量时，该模块会在内部将这些向量偏移为在 0 degC 时为 0 kJ/kg。然后，库模块在内部计算中使用这些调整后的值。仿真数据日志也显示调整后的比焓值。

热力学属性传感器 (MA) 模块中新增的 **Enthalpy reference state** 参数允许您查看相对于不同参考状态调整后的比焓值。`As provided in Moist Air Properties (MA) block` 选项输出与之前版本相同的值。

### R2023a：湿空气传感器可用性增强

具有多个输出端口的湿空气传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

在模型中使用热力学属性传感器 (MA) 模块时没有兼容性影响。但是，如果您在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.moist_air.sensors.thermodynamic_sensor;` | `sensor = foundation.moist_air.sensors.thermodynamic_sensor(enthalpy=true, specific_heat=true, entropy=true);` |

## 描述

测量空气混合物的比焓、密度、定压比热和比熵

热力学属性传感器 (MA) 模块表示一个理想传感器，用于测量湿空气网络中空气混合物的比焓、密度、定压比热和比熵。传感器中没有质量或能量流动。

该模块在连接到端口 **A** 的节点处测量这些热力学属性。

您可以选择按整个空气混合物的质量归一化输出这些测量值，或仅按干空气和痕量气体的质量归一化输出。第二个选项与美国采暖、制冷与空调工程师学会 (ASHRAE) 标准一致。

用于传感器校准的比熵参考值为：湿混合物中各组分在大气压力和大气温度下均为 0。大气压力和大气温度由连接到回路的湿空气属性 (MA) 模块的参数定义。
