---
type: simulink-block
title: 'Thermodynamic Properties Sensor (TL)'
family: 'thermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Sensors'
documentation_page: 'thermodynamicpropertiessensortl'
documentation_source_path: 'ref/thermodynamicpropertiessensortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermodynamic Properties Sensor (TL)

## 端口

### 输出

### **u** — 比内能测量，kJ/kg 物理信号

用于测量热液比内能的物理信号输出端口。

#### 依赖项

要启用此端口，请选中 **Internal energy** 复选框。

### **ρ** — 密度测量，kg/m^3 物理信号

用于测量热液密度的物理信号输出端口。

#### 依赖项

要启用此端口，请选中 **Density** 复选框。

### **cp** — 定压比热容测量，kJ/(kg\*K) 物理信号

用于测量热液定压比热容的物理信号输出端口。

#### 依赖项

要启用此端口，请选中 **Specific heat** 复选框。

### 守恒

### **A** — 传感器入口热液

热液守恒端口。将此端口连接到热液网络中要测量热力学特性的节点。所有测量均相对于绝对零度进行。

## 参数

### **Internal energy** — 用于控制测量比内能的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **u**，可用于测量热液的比内能。

### **Density** — 用于控制测量密度的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **ρ**，可用于测量热液密度。

### **Specific heat** — 用于控制测量比热容的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **cp**，可用于测量热液的定压比热容。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023a: 热液传感器的易用性增强

具有多个输出端口的热液传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

在模型中使用 Thermodynamic Properties Sensor (TL) 模块时，不会产生兼容性影响。但是，如果在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor;` | `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor(internal_energy=true, specific_heat=true);` |

## 描述

测量热液网络中的比内能、密度和定压比热容

Thermodynamic Properties Sensor (TL) 模块表示一个理想传感器，用于测量热液网络中的比内能、密度和定压比热容。传感器中没有质量或能量流动。

该模块在连接到端口 **A** 的节点处测量这些热力学特性。所有测量均相对于绝对零度进行。
