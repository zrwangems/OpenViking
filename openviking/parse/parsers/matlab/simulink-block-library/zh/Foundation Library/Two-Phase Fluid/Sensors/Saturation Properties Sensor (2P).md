---
type: simulink-block
title: 'Saturation Properties Sensor (2P)'
family: 'two-phase-fluid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'saturationpropertiessensor2p'
documentation_source_path: 'ref/saturationpropertiessensor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Saturation Properties Sensor (2P)

## 端口

### 输出

### **TL** — 饱和液体温度，K 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和液体温度。

#### 依赖关系

要启用此端口，请选中 **Saturated temperature measurement** 复选框。

### **TV** — 饱和蒸气温度，K 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和蒸气温度。

#### 依赖关系

要启用此端口，请选中 **Saturated temperature measurement** 复选框。

### **PL** — 饱和液体压力，MPa 物理信号

物理信号输出端口，基于端口 **A** 处的温度测量饱和液体压力。

#### 依赖关系

要启用此端口，请选中 **Saturated pressure measurement** 复选框。

### **PV** — 饱和蒸气压力，MPa 物理信号

物理信号输出端口，基于端口 **A** 处的温度测量饱和蒸气压力。

#### 依赖关系

要启用此端口，请选中 **Saturated pressure measurement** 复选框。

### **UL** — 饱和液体比内能，kJ/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和液体比内能。

#### 依赖关系

要启用此端口，请将 **Energy measurement** 参数设置为 `Saturated specific internal energy`。

### **UV** — 饱和蒸气比内能，kJ/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和蒸气比内能。

#### 依赖关系

要启用此端口，请将 **Energy measurement** 参数设置为 `Saturated specific internal energy`。

### **HL** — 饱和液体比焓，kJ/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和液体比焓。

#### 依赖关系

要启用此端口，请将 **Energy measurement** 参数设置为 `Saturated specific enthalpy`。

### **HV** — 饱和蒸气比焓，kJ/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和蒸气比焓。

#### 依赖关系

要启用此端口，请将 **Energy measurement** 参数设置为 `Saturated specific enthalpy`。

### **VL** — 饱和液体比体积，m^3/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和液体比体积。

#### 依赖关系

要启用此端口，请将 **Density measurement** 参数设置为 `Saturated specific volume`。

### **VV** — 饱和蒸气比体积，m^3/kg 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和蒸气比体积。

#### 依赖关系

要启用此端口，请将 **Density measurement** 参数设置为 `Saturated specific volume`。

### **rhoL** — 饱和液体密度，kg/m^3 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和液体密度。

#### 依赖关系

要启用此端口，请将 **Density measurement** 参数设置为 `Saturated density`。

### **rhoV** — 饱和蒸气密度，kg/m^3 物理信号

物理信号输出端口，基于端口 **A** 处的压力测量饱和蒸气密度。

#### 依赖关系

要启用此端口，请将 **Density measurement** 参数设置为 `Saturated density`。

### 守恒

### **A** — 传感器入口两相流体

与传感器入口关联的两相流体守恒端口。将此端口连接到两相流体网络中要测量液体和蒸气饱和属性的节点。

## 参数

### **Saturated temperature measurement** — 基于压力测量饱和液体和蒸气温度 `On`（默认）| `Off`

选中此复选框会显示输出端口 **TL** 和 **TV**，它们基于端口 **A** 处的压力分别测量饱和液体温度和饱和蒸气温度。

### **Saturated pressure measurement** — 基于温度测量饱和液体和蒸气压力 `Off`（默认）| `On`

选中此复选框会启用 **Saturated pressure beyond min and max pressure** 参数，并显示输出端口 **PL** 和 **PV**，它们基于端口 **A** 处的温度分别测量饱和液体压力和饱和蒸气压力。

### **Saturated pressure beyond min and max pressure** — 越界饱和压力的报告首选项 `Error`（默认）| `Warning` | `None`

当任一饱和压力低于流体属性中指定的最小压力或高于最大压力时，饱和压力值基于温度表的外推值，而不是表内的插值。选择饱和压力越界时的报告首选项：

- `Error` — 仿真停止并报错。
- `Warn` — 该模块发出警告。
- `None` — 该模块不发出断言。

#### 依赖关系

要启用此参数，请将 **Saturated pressure measurement** 设置为 `On`。

### **Energy measurement** — 基于压力测量饱和比内能或饱和比焓 `Off`（默认）| `Saturated specific internal energy` | `Saturated specific enthalpy`

将此参数设置为：

- `Saturated specific internal energy` — 显示输出端口 **UL** 和 **UV**，它们基于端口 **A** 处的压力分别测量液体和蒸气的饱和比内能。
- `Saturated specific enthalpy` — 显示输出端口 **HL** 和 **HV**，它们基于端口 **A** 处的压力分别测量液体和蒸气的饱和比焓。

### **Density measurement** — 基于压力测量饱和比体积或饱和密度 `Off`（默认）| `Saturated specific volume` | `Saturated density`

将此参数设置为：

- `Saturated specific volume` — 显示输出端口 **VL** 和 **VV**，它们基于端口 **A** 处的压力分别测量液体和蒸气的饱和比体积。
- `Saturated density` — 显示输出端口 **rhoL** 和 **rhoV**，它们基于端口 **A** 处的压力分别测量液体和蒸气的饱和密度。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a: 传感器的易用性增强

Saturation Properties Sensor (2P) 模块现在具有 **Saturated temperature measurement** 复选框，它控制模块图标上端口 **TL** 和 **TV** 的可见性。用于控制端口 **PL** 和 **PV** 可见性的 **Saturated pressure measurement** 参数现在是一个复选框。

此更改没有兼容性影响。

## 描述

测量两相流体中的液体和蒸气饱和属性

Saturation Properties Sensor (2P) 模块表示一个理想传感器，可用于测量两相流体网络中的以下液体和蒸气饱和属性：

- 基于压力测量的饱和温度、比体积、比内能或比焓
- 基于温度测量的饱和压力

该模块在连接到端口 **A** 的节点处测量这些属性。传感器中没有质量或能量流动。

默认情况下，模块图标上仅显示测量饱和液体和蒸气温度的输出端口 **TL** 和 **TV**。使用模块参数控制其他测量的输出端口的可见性。
