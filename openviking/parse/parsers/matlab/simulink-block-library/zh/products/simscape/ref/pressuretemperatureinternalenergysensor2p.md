---
type: simulink-block
title: 'Pressure, Temperature & Internal Energy Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Sensors'
documentation_page: 'pressuretemperatureinternalenergysensor2p'
documentation_source_path: 'ref/pressuretemperatureinternalenergysensor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure, Temperature & Internal Energy Sensor (2P)

## 端口

### 输出

### **Pa** — 绝对压力测量，单位为 Pascal (Pa) 的物理信号

用于绝对压力测量的物理信号输出端口。

#### 依赖项

要启用此端口，请将 **测量参考**
参数设置为 `Absolute`，选中
**压力** 复选框，并将 **压力类型**
参数设置为 `Absolute pressure`。

### **Pg** — 表压测量，Pa 物理信号

用于表压测量的物理信号输出端口。

#### 依赖项

要启用此端口，请将 **测量参考**
参数设置为 `Absolute`，选中
**压力** 复选框，并将 **压力类型**
参数设置为 `Gauge pressure`。

### **P** — 压力差测量，Pa 物理信号

用于压力差测量的物理信号输出端口。

#### 依赖项

要启用此端口，请将 **测量参考**
参数设置为 `Difference` 并选中
**压力** 复选框。

### **T** — 温度测量，K 物理信号

用于温度测量的物理信号输出端口。

#### 依赖项

要启用此端口，请选中 **温度** 复选框。

### **U** — 比内能测量，kJ/kg 物理信号

用于比内能测量的物理信号输出端口。

#### 依赖项

要启用此端口，请选中 **内能** 复选框。

### 守恒

### **A** — 传感器入口两相流体

两相流体守恒端口。使用此端口测量绝对压力、
温度和比内能。

### **B** — 传感器出口两相流体

两相流体守恒端口。当传感器执行绝对测量时，
此端口会隐藏，因为传感器包含一个隐式参考节点。启用
此端口以测量模型中两个节点之间的相对压力、温度或比内能。当端口
**A** 处的值大于端口
**B** 处的值时，测量值为正。

#### 依赖项

要启用此端口，请将 **测量参考**
参数设置为 `Difference`。

## 参数

### **测量参考** — 在绝对测量和相对测量之间选择 `Absolute` (默认) | `Difference`

在绝对测量和相对测量之间选择：

- `Absolute` — 传感器测量端口 **A** 处的压力和
  温度。传感器包含一个隐式
  参考节点，这意味着只需一个端口即可进行绝对
  测量。
- `Difference` — 传感器测量模型中两个节点之间的压力或温度
  差。选择此
  选项会在模块图标上显示端口 **B**。

### **压力** — 控制用于测量压力的输出端口可见性 `On` (默认) | `Off`

选中此复选框会显示输出端口 **Pa**、
**Pg** 或 **P**，以便测量
压力。

### **压力类型** — 在绝对压力和表压之间选择 `Absolute pressure` (默认) | `Gauge pressure`

选择传感器测量绝对压力还是表压：

- `Absolute pressure` — 传感器测量端口 **A** 处的
  绝对压力。选择此选项会在模块图标上显示端口
  **Pa**。
- `Gauge pressure` — 传感器测量端口 **A** 处的表压。
  选择此选项会在模块图标上显示端口
  **Pg**。

#### 依赖项

要启用此参数，请将 **测量参考** 设置为
`Absolute` 并选中 **压力**
复选框。

### **温度** — 控制用于测量温度的输出端口可见性 `Off` (默认) | `On`

选中此复选框会显示输出端口 **T**，从而可以
测量温度。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a: 两相流体传感器的可用性增强

Pressure & Internal Energy Sensor (2P) 模块已重命名为
Pressure, Temperature & Internal Energy Sensor (2P)，因为它现在
还可以测量温度。

模块端口现在在模块图标上具有条件可见性。您可以使用模块
参数仅显示特定模型中测量所需的端口。

此外，模块现在包含一个隐式参考节点，这意味着您
只需一个端口即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才显示
第二个端口。

在以前的版本中，要在端口
**A** 处测量绝对压力和绝对温度，需要将端口 **B** 连接到
Absolute Reference (2P) 模块。这不再必要，
因为您现在可以通过将 **测量参考** 参数设置为 `Absolute` 来进行绝对测量，但具有这些连接的现有模型
将继续像以前一样工作。

在模型中使用此模块时没有兼容性影响。当您打开
现有模型时，其中的 Pressure & Internal Energy Sensor (2P) 模块会自动替换为
Pressure, Temperature & Internal Energy Sensor
(2P) 模块，并显示相应的端口。

但是，如果您在自定义复合组件中使用此模块，则需要更新
复合组件代码。

| 旧语法 | 新语法 |
| --- | --- |
| `sensor = foundation.two_phase_fluid.sensors.pressure_internal_energy_sensor;` | `sensor = foundation.two_phase_fluid.sensors.pressure_internal_energy_sensor(reference=foundation.enum.MeasurementReference.difference, internal_energy=true);` |

## 描述

测量两相流体网络中的压力、温度和比内能

Pressure, Temperature & Internal Energy Sensor (2P)
模块表示一个理想传感器，用于测量两相流体网络中的压力、温度和比内能。没有质量或能量流过
传感器。

传感器包含一个隐式参考节点，这意味着您只需一个端口，
端口 **A**，即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才显示
第二个端口，端口 **B**。当端口 **A** 处的值大于端口
**B** 处的值时，测量值为正。

有五个物理信号端口可用于输出测量数据：

- 端口 **Pa** 输出绝对压力。
- 端口 **Pg** 输出表压。
- 端口 **P** 输出传感器两端的压力差。
- 端口 **T** 输出温度。
- 端口 **U** 输出比内能。

这些端口在模块图标上具有条件端口可见性。使用模块参数
仅显示特定模型中测量所需的端口。

将测量端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为
Simulink® 信号，例如用于绘图或附加数据处理。
