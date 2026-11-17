---
type: simulink-block
title: 'Pressure Source (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Sources'
documentation_page: 'pressuresourcetl'
documentation_source_path: 'ref/pressuresourcetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Source (TL)

## 端口

### 输入

### **P** — 压差控制信号，Pa 物理信号

输入物理信号，用于指定源两端的压差。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`。
### 守恒

### **A** — 源入口热液体

热液体守恒端口。正压差使端口 **B** 处的压力大于端口
**A** 处的压力。

### **B** — 源出口热液体

热液体守恒端口。正压差使端口 **B** 处的压力大于端口
**A** 处的压力。

## 参数

### **Source type** — 选择压差是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择源产生的压差是否可以在仿真期间变化：

- `Controlled` — 压差是可变的，
  由输入物理信号控制。选择此选项将显示
  输入端口 **P**。
- `Constant` — 压差在仿真期间
  恒定，由模块参数指定。选择此选项
  将启用 **Pressure differential** 参数。

### **Pressure differential** — 源两端的恒定压差 `0 Pa`（默认）| 标量

源端口两端所需的压差。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对流体流做功：

- `Isentropic` — 源对流体执行等熵
  功以维持指定的压差。使用此选项
  来表示理想化的泵或压缩机，并正确考虑能量
  输入和输出，尤其是在闭环系统中。
- `None` — 源不对
  流体做功，无论源产生的压差如何，既不添加也不移除功率。使用此选项
  在系统上游设置所需的流动条件，
  而不影响流体的温度。

### **Cross-sectional area at ports A and B** — 入口和出口处垂直于流动路径的面积 `0.01 m^2`（默认）| 正标量

源入口和出口处垂直于流动方向的
面积。假设两个横截面积相同。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023b：热液体源可用性增强

在 R2023b 中，单独的 Pressure Source (TL) 和 Controlled Pressure
Source (TL) 模块已合并为单个 Pressure Source
(TL) 模块，允许您选择生成恒定或时变压差。

当您在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。当您打开现有模型时，Controlled Pressure Source
(TL) 模块会自动替换为具有暴露输入端口的 Pressure Source (TL)
模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新
复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (TL) | `source = foundation.thermal_liquid.sources.controlled_pressure_source;` | `source = foundation.thermal_liquid.sources.pressure_source;` |
| Pressure Source (TL) | `source = foundation.thermal_liquid.sources.pressure_source;` | `source = foundation.thermal_liquid.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

### R2023a: 在不影响温度的情况下配置流动条件

该模块包含 **Power added** 参数，可用于指定源是否对流体流动做功。默认选项 `Isentropic power` 等效于之前版本中的模块行为。使用新的 `None` 选项可在系统上游设置所需的流动条件，而不影响流动的温度。

## 描述

生成恒定或时变的压差

Pressure Source (TL) 模块表示热液体网络中的理想机械能源。无论通过源的流量如何，该源都可以在其端口之间维持指定的压差。没有流动阻力，也没有与环境的热交换。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **P** 处的输入物理信号指定压差。或者，您可以将恒定压差指定为模块参数。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

源处的能量平衡是端口 **A** 和 **B** 的能量流率以及对流体所做功的函数：

ϕA+ϕB+ϕwork=0,

其中：

- *ϕ*A 是通过端口 **A** 进入源的能量流率。
- *ϕ*B 是通过端口 **B** 进入源的能量流率。
- *ϕ*work 是对流体所做的等熵功。

等熵功项为

ϕwork=m˙(pB−pA)ρavg,

其中：

- *ϕ*work 是对热液体所做的等熵功。
- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。
- *ρ*avg 是平均液体密度，

  ρavg=ρA+ρB2。

### 假设和限制

- 不存在不可逆损失。
- 与环境没有热交换。
