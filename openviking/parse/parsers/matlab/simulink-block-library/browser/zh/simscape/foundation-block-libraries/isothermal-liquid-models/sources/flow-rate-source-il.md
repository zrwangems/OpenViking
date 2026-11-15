---
type: simulink-block
title: 'Flow Rate Source (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Sources'
documentation_page: 'flowratesourceil'
documentation_source_path: 'ref/flowratesourceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (IL)

## 端口

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过源的质量流量。

#### 依赖关系

如果将 **Source type** 参数设置为 `Controlled`，并将 **Flow rate type** 参数设置为 `Mass flow rate`，则此端口可见。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过源的体积流量。

#### 依赖关系

如果将 **Source type** 参数设置为 `Controlled`，并将 **Flow rate type** 参数设置为 `Volumetric flow rate`，则此端口可见。

### 守恒

### **A** — 源入口等温液体

等温液体守恒端口。正流量会使流体从端口 **A** 流向端口 **B**。

### **B** — 源出口等温液体

等温液体守恒端口。正流量会使流体从端口 **A** 流向端口 **B**。

## 参数

### **Source type** — 选择流量在仿真期间是否可以变化 `Controlled`（默认） | `Constant`

选择源生成的流量在仿真期间是否可以变化：

- `Controlled` — 流量是可变的，由输入物理信号控制。选择此选项会显示输入端口 **M** 或 **V**，具体取决于 **Flow rate type** 参数的值。
- `Constant` — 流量在仿真期间恒定，由模块参数指定。选择此选项会启用 **Mass flow rate** 或 **Volumetric flow rate** 参数，具体取决于 **Flow rate type** 参数的值。

### **Flow rate type** — 选择源生成质量流量还是体积流量 `Mass flow rate`（默认） | `Volumetric flow rate`

选择流量类型：`Mass flow rate` 或 `Volumetric flow rate`。

### **Mass flow rate** — 通过源的恒定质量流量 `0 kg/s`（默认） | scalar

期望通过源的流体质量流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`，并将 **Flow rate type** 设置为 `Mass flow rate`。

### **Volumetric flow rate** — 通过源的恒定体积流量 `0 m^3/s`（默认） | scalar

期望通过源的流体体积流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`，并将 **Flow rate type** 设置为 `Volumetric flow rate`。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

生成指定的质量流量或体积流量

Flow Rate Source (IL) 模块表示等温液体网络中的理想机械能量源。该源可以维持指定的质量流量或体积流量，而不受压差影响。没有流动阻力，也没有与环境的热交换。您可以使用 **Flow rate type** 参数指定流量类型。

端口 **A** 和 **B** 表示源的入口和出口。端口 **M** 或 **V** 处的输入物理信号（取决于流量类型）指定流量。或者，您可以将固定流量指定为模块参数。正流量会使流体从端口 **A** 流向端口 **B**。

模块图标会根据 **Source type** 和 **Flow rate type** 参数的值而变化。

| 源类型 | 流量类型 | 模块图标 |
| --- | --- | --- |
| `Controlled` | `Mass flow rate` |  |
| `Volumetric flow rate` |  |
| `Constant` | `Mass flow rate` |  |
| `Volumetric flow rate` |  |

模块计算对流体所做的功，并将结果包含在仿真数据日志中，以供参考：

Wmech=m˙pB−pAρ¯

ρ¯=ρA+ρB2

其中：

- *W*mech 是源所做的机械功。
- m˙ 是源生成的质量流量。
- *p*A 和 *p*B 分别是端口 **A** 和 **B** 处的压力。
- ρ¯ 是平均流体混合物密度。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的流体混合物密度值。用于计算流体混合物密度的方程取决于所选的等温液体模型。有关详细信息，请参阅等温液体建模选项。

如果 **Flow rate type** 参数设置为 `Volumetric flow rate`，则模块根据指定的体积流量计算质量流量：

m˙=ρoutq

ρout={ρB,q>0ρA,q≤0

其中：

- *ρ*out 是流出密度。
- *q* 是体积流量。

有关查看记录的仿真数据的信息，请参阅数据记录。

### 假设和限制

- 不存在不可逆损失。
- 与环境没有热交换。
