---
type: simulink-block
title: 'Thermodynamic Properties Sensor (TL)'
family: 'simscape'
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
```yaml
ports:
- name: u
  summary: 比内能测量，kJ/kg 物理信号
  direction: output
- name: ρ
  summary: 密度测量，kg/m^3 物理信号
  direction: output
- name: cp
  summary: 定压比热测量，kJ/(kg\*K) 物理信号
  direction: output
- name: A
  summary: 传感器入口热液体
  direction: output
```

### 输出

### **u** — 比内能测量，kJ/kg 物理信号

用于测量热液体比内能的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Internal energy** 复选框。

### **ρ** — 密度测量，kg/m^3 物理信号

用于测量热液体密度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Density** 复选框。

### **cp** — 定压比热测量，kJ/(kg\*K) 物理信号

用于测量热液体定压比热的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Specific heat** 复选框。
### 守恒

### **A** — 传感器入口热液体

热液体守恒端口。将此端口连接到热液体网络中您想要测量热力学属性的节点。所有测量均相对于绝对零度进行。
## 参数
```yaml
parameters:
- name: Internal energy
  summary: 控制用于测量比内能的输出端口可见性 Off（默认）| On
  group: ''
- name: Density
  summary: 控制用于测量密度的输出端口可见性 On（默认）| Off
  group: ''
- name: Specific heat
  summary: 控制用于测量比热的输出端口可见性 Off（默认）| On
  group: ''
```

### **Internal energy** — 控制用于测量比内能的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **u**，可用于测量热液体的比内能。

### **Density** — 控制用于测量密度的输出端口可见性 `On`（默认）| `Off`

选中此复选框将显示输出端口 **ρ**，可用于测量热液体的密度。

### **Specific heat** — 控制用于测量比热的输出端口可见性 `Off`（默认）| `On`

选中此复选框将显示输出端口 **cp**，可用于测量热液体的定压比热。
## 所属库

Simscape / Foundation Library / Thermal Liquid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023a：热液体传感器的可用性增强

具有多个输出端口的热液体传感器模块现在在模块图标上具有条件端口可见性。您可以使用模块参数仅显示特定模型中测量所需的端口。

在模型中使用 Thermodynamic Properties Sensor (TL) 模块时没有兼容性影响。但是，如果您在自定义复合组件中使用此模块，则需要更新复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor;` | `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor(internal_energy=true, specific_heat=true);` |

## 描述

测量热液体网络中的比内能、密度和定压比热

Thermodynamic Properties Sensor (TL) 模块表示一个理想传感器，用于测量热液体网络中的比内能、密度和定压比热。传感器中没有质量或能量流动。

该模块在连接到端口 **A** 的节点处测量这些热力学属性。所有测量均相对于绝对零度进行。
