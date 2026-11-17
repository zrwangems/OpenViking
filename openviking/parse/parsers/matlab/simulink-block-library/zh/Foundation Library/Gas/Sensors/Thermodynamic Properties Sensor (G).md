---
type: simulink-block
title: 'Thermodynamic Properties Sensor (G)'
family: 'gas'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'thermodynamicpropertiessensorg'
documentation_source_path: 'ref/thermodynamicpropertiessensorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermodynamic Properties Sensor (G)

## 端口

### 输出

### **h** — 比焓测量，kJ/kg 物理信号

用于测量气体比焓的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Enthalpy** 复选框。

### **ρ** — 密度测量，kg/m^3 物理信号

用于测量气体密度的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Density** 复选框。

### **cp** — 定压比热测量，kJ/(kg\*K) 物理信号

用于测量气体定压比热的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Specific heat** 复选框。

### **s** — 比熵测量，kJ/(kg\*K) 物理信号

用于测量气体比熵的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Entropy** 复选框。

### 守恒端口

### **A** — 传感器入口气体

气体守恒端口。将此端口连接到气体网络中要测量热力学属性的节点。所有测量均相对于绝对零度进行。

## 参数

### **Enthalpy** — 控制用于测量比焓的输出端口可见性 `Off` (默认) | `On`

选中此复选框会显示输出端口 **h**，可用于测量气体比焓。

### **Density** — 控制用于测量密度的输出端口可见性 `On` (默认) | `Off`

选中此复选框会显示输出端口 **ρ**，可用于测量气体密度。

### **Specific heat** — 控制用于测量比热的输出端口可见性 `Off` (默认) | `On`

选中此复选框会显示输出端口 **cp**，可用于测量气体比热。

### **Entropy** — 控制用于测量比熵的输出端口可见性 `Off` (默认) | `On`

选中此复选框会显示输出端口 **s**，可用于测量气体比熵。

### **Specific entropy at reference pressure and temperature** — 用于传感器校准的参考比熵 3.8635 kJ/kg/K (默认)

传感器经过校准，以便当端口 **A** 处于参考压力和温度时输出此比熵值。

#### 依赖关系

要启用此参数，请选中 **Entropy** 复选框。

### **Reference pressure for specific entropy** — 用于传感器校准的参考压力 0.101325 MPa (默认)

传感器经过校准，以便当端口 **A** 处于参考压力和温度时，输出由 **Specific entropy at reference pressure and temperature** 参数指定的值。

#### 依赖关系

要启用此参数，请选中 **Entropy** 复选框。

### **Reference temperature for specific entropy** — 用于传感器校准的参考温度 293.15 K (默认)

传感器经过校准，以便当端口 **A** 处于参考压力和温度时，输出由 **Specific entropy at reference pressure and temperature** 参数指定的值。

#### 依赖关系

要启用此参数，请选中 **Entropy** 复选框。

## 所属库

Simscape / Foundation Library / Gas / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023a：气体传感器可用性增强

具有多个输出端口的气体传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

在模型中使用 Thermodynamic Properties Sensor (G) 模块不会产生兼容性影响。但是，如果在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.gas.sensors.thermodynamic_sensor;` | `sensor = foundation.gas.sensors.thermodynamic_sensor(enthalpy=true, specific_heat=true, entropy=true);` |

## 描述

测量比焓、密度、定压比热和比熵

Thermodynamic Properties Sensor (G) 模块表示理想传感器，用于测量气体网络中的比焓、密度、定压比热和比熵。传感器中没有质量或能量流。

该模块在连接到端口 **A** 的节点处测量这些热力学属性。前三个测量值（比焓、密度、定压比热）均相对于绝对零度进行测量。对于什么构成零熵没有通用定义，因此您可以使用模块参数提供用于传感器校准的参考熵值。
