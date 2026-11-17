---
type: simulink-block
title: 'Flow Rate Sensor (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Sensors'
documentation_page: 'flowratesensoril'
documentation_source_path: 'ref/flowratesensoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Sensor (IL)

## 端口
```yaml
ports:
- name: M
  summary: 质量流量，kg/s 物理信号
  direction: output
- name: V
  summary: 体积流量，m^3/s 物理信号
  direction: output
- name: A
  summary: 传感器入口等温液体
  direction: output
- name: B
  summary: 传感器出口等温液体
  direction: output
```

### 输出

### **M** — 质量流量，kg/s 物理信号

用于质量流量测量的物理信号输出端口。

#### 依赖关系

如果将 **Sensor Measurements** 参数设置为 `Mass flow rate` 或 `Mass and volumetric flow rate`，则此端口可见。

### **V** — 体积流量，m^3/s 物理信号

用于体积流量测量的物理信号输出端口。

#### 依赖关系

如果将 **Sensor Measurements** 参数设置为 `Volumetric flow rate` 或 `Mass and volumetric flow rate`，则此端口可见。
### 守恒

### **A** — 传感器入口等温液体

等温液体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正。

### **B** — 传感器出口等温液体

等温液体守恒端口。如果流体从端口 **A** 流向端口 **B**，则流量为正。
## 参数
```yaml
parameters:
- name: Sensor Measurements
  summary: 选择传感器测量质量流量、体积流量还是两者 Mass flow rate（默认）| Volumetric flow rate | Mass and volumetric flow rate
  group: ''
```

### **Sensor Measurements** — 选择传感器测量质量流量、体积流量还是两者 `Mass flow rate`（默认）| `Volumetric flow rate` | `Mass and volumetric flow rate`

选择测量类型：

- `Mass flow rate` — 传感器测量质量流量。选择此选项将显示输出端口 **M**。
- `Volumetric flow rate` — 传感器测量体积流量。选择此选项将显示输出端口 **V**。
- `Mass and volumetric flow rate` — 传感器同时测量质量流量和体积流量。选择此选项将显示输出端口 **M** 和 **V**。
## 所属库

Simscape / Foundation Library / Isothermal Liquid / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

测量质量流量和体积流量

Flow Rate Sensor (IL) 模块表示一个理想传感器，用于测量等温液体网络中的质量流量和体积流量。传感器两端的压力和温度没有变化。

由于流量是 Through 变量，该模块必须与被测组件串联连接。

端口 **A** 和 **B** 分别表示传感器入口和出口。端口 **A** 和 **B** 的相对方向确定了测量符号。如果流体从端口 **A** 流向端口 **B**，则符号为正。交换端口连接会反转测量符号。

物理信号端口 **M** 和 **V** 分别输出通过传感器的质量流量和体积流量。**Sensor Measurements** 参数通过显示或隐藏相应端口来控制测量类型。将已显示的物理信号端口连接到 PS-Simulink Converter 模块，以将输出物理信号转换为 Simulink® 信号，例如用于绘图或附加数据处理。

模块图标会根据 **Sensor Measurements** 参数的值而变化。

| Sensor Measurements | 模块图标 |
| --- | --- |
| `Mass flow rate` |  |
| `Volumetric flow rate` |  |
| `Mass and volumetric flow rates` |  |

如果传感器测量包括体积流量，则该模块根据测得的质量流量计算体积流量：

q=m˙ρ

其中：

- *q* 是体积流量。
- m˙ 是测得的质量流量。
- *ρ* 是端口 **A** 或 **B** 处的流体混合物密度。传感器两端没有压差，因此端口 **A** 和 **B** 处的密度相同。
  用于计算流体混合物密度的方程取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。
