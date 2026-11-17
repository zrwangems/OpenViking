---
type: simulink-block
title: 'Thermodynamic Properties Sensor (2P)'
family: 'two-phase-fluid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'thermodynamicpropertiessensor2p'
documentation_source_path: 'ref/thermodynamicpropertiessensor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermodynamic Properties Sensor (2P)

## 端口

### 输出

### **T** — 温度测量，K 物理信号

物理信号输出端口，用于测量两相流体的温度。

#### 依赖关系

要启用此端口，请选中 **Temperature** 复选框。

### **h** — 比焓测量，kJ/kg 物理信号

物理信号输出端口，用于测量两相流体的比焓。

#### 依赖关系

要启用此端口，请选中 **Enthalpy** 复选框。

### **ρ** — 密度测量，kg/m^3 物理信号

物理信号输出端口，用于测量两相流体的密度。

#### 依赖关系

要启用此端口，请选中 **Density** 复选框。

### **v** — 比体积测量，m^3/kg 物理信号

物理信号输出端口，用于测量两相流体的比体积。

#### 依赖关系

要启用此端口，请选中 **Specific volume** 复选框。

### **s** — 比熵测量，kJ/(kg\*K) 物理信号

物理信号输出端口，用于测量两相流体的比熵。

#### 依赖关系

要启用此端口，请选中 **Entropy** 复选框。

### 守恒

### **A** — 传感器入口两相流体

两相流体守恒端口。将此端口连接到两相流体网络中您要测量热力学属性的节点。所有测量均相对于绝对零度进行。

## 参数

### **Temperature** — 控制用于测量温度的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **T**，从而可以测量两相流体的温度。

### **Enthalpy** — 控制用于测量比焓的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **h**，从而可以测量两相流体的比焓。

### **Density** — 控制用于测量密度的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **ρ**，从而可以测量两相流体的密度。

### **Specific volume** — 控制用于测量比体积的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **v**，从而可以测量两相流体的比体积。

### **Entropy** — 控制用于测量比熵的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **s**，从而可以测量两相流体的比熵。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a：两相流体传感器的可用性增强

Thermodynamic Properties Sensor (2P) 模块现在还可以测量密度。

模块端口现在在模块图标上具有条件可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

在模型中使用 Thermodynamic Properties Sensor (2P) 模块不会产生兼容性影响。但是，如果在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.two_phase_fluid.sensors.thermodynamic_sensor;` | `sensor = foundation.two_phase_fluid.sensors.thermodynamic_sensor(temperature=true, enthalpy=true, specific_volume=true, entropy=true);` |

## 描述

测量两相流体网络中的温度、密度、比焓、比熵和比体积

Thermodynamic Properties Sensor (2P) 模块表示一个理想传感器，用于测量两相流体网络中的温度、密度、比焓、比熵和比体积。没有质量或能量流过该传感器。

该模块在连接到端口 **A** 的节点处测量这些热力学属性。所有测量均相对于绝对零度进行。
