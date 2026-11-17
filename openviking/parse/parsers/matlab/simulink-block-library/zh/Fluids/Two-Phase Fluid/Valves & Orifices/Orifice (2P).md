---
type: simulink-block
title: 'Orifice (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices'
documentation_page: 'orifice2p'
documentation_source_path: 'ref/orifice2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (2P)

## 端口
```yaml
ports:
- name: A
  summary: 流体入口或出口两相流体
  direction: conserving
- name: B
  summary: 流体入口或出口两相流体
  direction: conserving
- name: S
  summary: 控制构件位置，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### **B** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### 输入

### **S** — 控制构件位置，m 物理信号

设定节流孔开度的控制构件位置。

#### 依赖关系

要启用此端口，请将 **Orifice type** 设置为 `Variable`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 流体相的建模选项 Liquid operating condition（默认）| Vapor operating condition
  group: ''
- name: Orifice type
  summary: 恒定或可变节流孔 Variable（默认）| Constant
  group: 参数
- name: Orifice parameterization
  summary: 可变或恒定节流孔参数化 Linear - Area vs. control member position（默认）| Orifice area | Nominal mass flow rate | Linear - Nominal
    mass flow rate vs. control member position | Tabulated data - Area vs. control member position | Cv flow coefficient |
    Kv flow coefficient
  group: 参数
- name: Nominal mass flow rate
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: 参数
- name: Nominal pressure drop
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: 参数
- name: Nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: 参数
- name: Nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: 参数
- name: Nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: 参数
- name: Nominal inlet vapor quality
  summary: 入口蒸汽质量分数 0（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Nominal inlet vapor void fraction
  summary: 入口体积分数 0（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: 参数
- name: Nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: 参数
- name: Orifice area
  summary: 孔口开口面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: Control member position at closed orifice
  summary: 控制构件偏移量 0 m（默认）| 正标量
  group: 参数
- name: Control member travel between closed and open orifice
  summary: 控制构件行程 5e-3 m（默认）| 正标量
  group: 参数
- name: Opening orientation
  summary: 打开孔口的位移方向 Positive control member displacement opens orifice（默认）| Negative control member displacement opens orifice
  group: 参数
- name: Nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: 参数
- name: 最大孔口开度下的额定压降
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: 参数
- name: 最大孔口面积
  summary: 最大孔口开度面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: 控制构件位置向量
  summary: 控制构件位置向量 [0, .002, .004, .007, .017] m（默认）| 1×*n* 向量
  group: 参数
- name: 孔口面积向量
  summary: 孔口开度面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 参数
- name: 流量系数
  summary: 流量系数 0.64（默认）| 正标量
  group: 参数
- name: 压力恢复
  summary: 是否考虑面积扩张中的压力升高 off（默认）| on
  group: 参数
- name: Opening characteristic
  summary: 将控制信号转换为流量能力度量的方法 Linear（默认）| Tabulated
  group: 参数
- name: Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: 参数
- name: Maximum Cv flow coefficient
  summary: 对应组件最大开启状态的 *Cv* 系数 4（默认）| 正标量
  group: 参数
- name: Cv flow coefficient vector
  summary: 对应控制构件位置向量中各值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: 参数
- name: Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: 参数
- name: Maximum Kv flow coefficient
  summary: 对应组件最大开启状态的 *Kv* 系数 3.6（默认）| 正标量
  group: 参数
- name: Kv flow coefficient vector
  summary: 与成员位置向量 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）中的值对应的 *Kv* 系数 | 1×*n* 向量
  group: 参数
- name: xT pressure differential ratio factor at choked flow
  summary: 阻塞流时的压差比系数 0.7（默认） | 正标量
  group: 参数
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认） | 正标量
  group: 参数
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认） | 范围 [0,1] 内的正标量
  group: 参数
- name: Inlet phase change time constant
  summary: 液体比容的滞后 0.1 s（默认） | 正标量
  group: 参数
- name: Laminar flow pressure ratio
  summary: 层流-湍流过渡压力比 0.999（默认） | 正标量
  group: 参数
- name: Cross-sectional area at ports A and B
  summary: 阀端口面积 0.01 m^2（默认） | 正标量
  group: 参数
```

### **Modeling option** — 流体相的建模选项 `Liquid operating condition`（默认）| `Vapor operating condition`

节流孔处流体相的建模选项。如果模块位置处的两相流体处于液态，请将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，请将此参数设置为 `Vapor operating condition`。

### 参数

### **Orifice type** — 恒定或可变节流孔 `Variable`（默认）| `Constant`

节流孔类型。当您将此参数设置为 `Variable` 时，节流孔面积根据端口 **S** 处接收的输入信号而变化。

### **Orifice parameterization** — 可变或恒定节流孔参数化 `Linear - Area vs. control member position`（默认）| `Orifice area` | `Nominal mass flow rate` | `Linear - Nominal mass flow rate vs. control member position` | `Tabulated data - Area vs. control member position` | `Cv flow coefficient` | `Kv flow coefficient`

模块用于根据节流孔两端的压差计算质量流量，或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 且 **Orifice type** 为 `Variable` 时，此参数的选项为：

- `Linear - Area vs. control member position`
- `Linear - Nominal mass flow rate vs. control member position`
- `Tabulated data - Area vs. control member position`

当 **Modeling option** 为 `Liquid operating condition` 且 **Orifice type** 为 `Constant` 时，此参数的选项为：

- `Orifice area`
- `Nominal mass flow rate`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Nominal mass flow rate** — 额定质量流量 `0.1` kg/s（默认）| 正标量

通过恒定节流孔的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Nominal mass flow rate`。

### **Nominal pressure drop** — 额定压降 `0.001` MPa（默认）| 正标量

通过恒定节流孔的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Nominal mass flow rate`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 参数的值和 **Nominal inlet condition specification** 参数的设置，从表格化的流体属性数据中确定节流孔额定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 设置为 `Constant`，**Orifice parameterization** 设置为 `Nominal mass flow rate`。
- **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. control member position`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认）| 正标量

额定工况下的入口压力。该模块根据**Nominal inlet pressure**参数的值以及**Nominal inlet condition specification**参数的设置，从表格化的流体属性数据中确定入口比体积。

#### 依赖关系

要启用此参数，请将**Modeling option**设置为`Liquid operating condition`，并且满足以下任一条件：

- **Orifice type**设置为`Constant`，且**Orifice parameterization**设置为`Nominal mass flow rate`。
- **Orifice type**设置为`Variable`，且**Orifice parameterization**设置为`Linear - Nominal mass flow rate vs. control member position`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认）| 正标量

额定运行工况下的入口流体温度。

#### 依赖关系

要启用此参数，请将**Modeling option**设置为`Liquid operating condition`，并且满足以下任一条件：

- **Orifice type**设置为`Constant`，**Orifice parameterization**设置为`Nominal mass flow rate`，且**Nominal inlet condition specification**设置为`Temperature`。
- **Orifice type**设置为`Variable`，**Orifice parameterization**设置为`Linear - Nominal mass flow rate vs. control member position`，且**Nominal inlet condition specification**设置为`Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认）| 范围 [0,1] 内的正标量

额定运行工况下入口混合物的蒸汽质量分数。值为`0`表示入口流体为过冷液体。值为`1`表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将**Modeling option**设置为`Liquid operating condition`，并且满足以下任一条件：

- **Orifice type**设置为`Constant`，**Orifice parameterization**设置为`Nominal mass flow rate`，且**Nominal inlet condition specification**设置为`Vapor quality`。
- **Orifice type**设置为`Variable`，**Orifice parameterization**设置为`Linear - Nominal mass flow rate vs. control member position`，且**Nominal inlet condition specification**设置为`Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认）| 范围 [0,1] 内的正标量

额定运行工况下入口混合物的体积分数。值为`0`表示入口流体为过冷液体。值为`1`表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将**Modeling option**设置为`Liquid operating condition`，并且满足以下任一条件：

- **Orifice type**设置为`Constant`，**Orifice parameterization**设置为`Nominal mass flow rate`，且**Nominal inlet condition specification**设置为`Vapor void fraction`。
- **Orifice type**设置为`Variable`，**Orifice parameterization**设置为`Linear - Nominal mass flow rate vs. control member position`，且**Nominal inlet condition specification**设置为`Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

额定运行工况下的入口比焓。

#### 依赖关系

要启用此参数，请将**Modeling option**设置为`Liquid operating condition`，并且满足以下任一条件：

- **Orifice type**设置为`Constant`，**Orifice parameterization**设置为`Nominal mass flow rate`，且**Nominal inlet condition specification**设置为`Specific enthalpy`。
- **Orifice type**设置为`Variable`，**Orifice parameterization**设置为`Linear - Nominal mass flow rate vs. control member position`，且**Nominal inlet condition specification**设置为`Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认）| 正标量

额定运行工况下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 设置为 `Constant`，**Orifice parameterization** 设置为 `Nominal mass flow rate`，并且 **Nominal inlet condition specification** 设置为 `Specific internal energy`。
- **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. control member position`，并且 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Orifice area** — 孔口开口面积 `1e-4` `m^2`（默认）| 正标量

孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Control member position at closed orifice** — 控制构件偏移量 `0` m（默认）| 正标量

控制构件偏移量，即孔口完全关闭时 **S** 处的值。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Linear – Nominal mass flow rate vs. control member position` 或 `Linear – Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，并且 **Opening characteristic** 设置为 `Linear`。

### **Control member travel between closed and open orifice** — 控制构件行程 `5e-3` m（默认）| 正标量

控制构件在孔口关闭和打开之间移动的距离。当您将 **Opening orientation** 设置为 `Positive control member displacement opens orifice` 时，孔口在 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数之和处完全打开。当您将 **Opening orientation** 设置为 `Negative control member displacement opens orifice` 时，孔口在 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数之差处完全打开。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Linear – Nominal mass flow rate vs. control member position` 或 `Linear – Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，并且 **Opening characteristic** 设置为 `Linear`。

### **Opening orientation** — 打开孔口的位移方向 `Positive control member displacement opens orifice`（默认）| `Negative control member displacement opens orifice`

打开可变孔口的构件位移方向。正方向意味着 **S** 处信号的增加会打开孔口。负方向意味着 **S** 处信号的减小会打开孔口。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Linear – Nominal mass flow rate vs. control member position` 或 `Linear – Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，并且 **Opening characteristic** 设置为 `Linear`。

### **Nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` kg/s（默认）| 正标量

在典型、设计或额定条件下通过完全打开孔口的质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear – Nominal mass flow rate vs. control member position`。

### **最大孔口开度下的额定压降** — 额定压降 `0.001` MPa（默认）| 正标量

在典型、设计或额定工况下，完全打开的孔口上的压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear – Nominal mass flow rate vs. control member position`。

### **最大孔口面积** — 最大孔口开度面积 `1e-4 m^2`（默认）| 正标量

孔口完全打开时的面积。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Linear – Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Linear`。

### **控制构件位置向量** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于表格化孔口参数化的控制构件位置向量。该向量的元素与 **Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的值一一对应。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **孔口面积向量** — 孔口开度面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

用于孔口面积表格化参数化的孔口面积值向量。该向量中的值与 **Control member position vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量的比值。此参数用于考虑孔口方程中未捕获的实际损失。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Orifice type** 设置为 `Constant`，并且 **Orifice parameterization** 设置为 `Orifice area`。
- **Modeling option** 设置为 `Liquid operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，并且 **Orifice parameterization** 设置为 `Orifice area`。

### **压力恢复** — 是否考虑面积扩张中的压力升高 `off`（默认）| `on`

是否考虑从入口到孔口孔处压降之后压力的小幅上升。当流体射流离开孔口孔时，它会耗散并膨胀以充满端口面积，从而导致这一小幅压力上升。当您清除 **Pressure recovery** 复选框时，该模块不会对此压力升高进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 设置为 `Variable`，且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- **Orifice type** 设置为 `Constant`，且 **Orifice parameterization** 设置为 `Orifice area`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 处指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，并将 **Orifice type** 设置为 `Variable`。

### **Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

常数 *Cv* 流量系数的值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient`。

### **Maximum Cv flow coefficient** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

当节流孔完全打开且可用流通面积为最大值时的 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应控制构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应 **Control member position vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

常数 *Kv* 流量系数的值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应组件最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

当节流孔完全打开且可用流通面积为最大值时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 与成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中的值对应的 *Kv* 系数 | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认） | 正标量

孔口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable` 以及任意其他参数组合，但以下情况除外：

- **Modeling option** 为 `Liquid operating condition` 且 **Orifice parameterization** 为 `Tabulated data - Area vs. control member position`。
- **Modeling option** 为 `Vapor operating condition` 且 **Opening characteristic** 为 `Tabulated`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高在这些区域中仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable` 以及任意其他参数组合，但以下情况除外：

- **Modeling option** 为 `Liquid operating condition` 且 **Orifice parameterization** 为 `Tabulated data - Area vs. control member position`。
- **Modeling option** 为 `Vapor operating condition` 且 **Opening characteristic** 为 `Tabulated`。

### **Inlet phase change time constant** — 液体比容的滞后 `0.1` s（默认） | 正标量

计算流体比容时液-汽混合物的时间滞后。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认） | 正标量

流体在层流和湍流状态之间过渡时的孔口出口压力与孔口入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Cross-sectional area at ports A and B** — 阀端口面积 `0.01` m^2（默认） | 正标量

孔口端口 **A** 和 **B** 的面积。
## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a: 对蒸汽或液体阀门进行建模

现在，当两相流体处于蒸汽或液体状态时，您可以使用 **Modeling option** 参数来指定孔口。两种建模选项也都包含新的孔口参数化。

当 **Modeling option** 为 `Liquid operating
condition` 时，您现在可以将 **Orifice
parameterization** 设置为：

- `Linear - Area vs. control member
  position`
- `Tabulated data - Area vs. control member
  position`
- `Orifice area`

当 **Modeling option** 为 `Vapor operating
condition` 时，您现在可以将 **Orifice
parameterization** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

若要保留以前版本中的恒定孔口行为，请将 **Modeling
option** 设置为 `Liquid operating condition`，并将
**Orifice parameterization** 设置为 `Nominal mass flow
rate`。若要保留以前版本中的可变孔口行为，请将 **Modeling option** 设置为 `Liquid operating
condition`，并将 **Orifice parameterization** 设置为
`Linear – Nominal mass flow rate vs. control member
position`。

## 描述

两相流体网络中的恒定或可变面积孔口

Orifice (2P) 模块用于对两相流体网络中由恒定或可变面积孔口引起的压力损失进行建模。**Modeling option** 参数控制用于为蒸汽或液体建模的阀门的参数化选项，但不会影响流体属性。该模块根据入口条件计算阀门内部的流体属性。流体与环境之间没有热交换，因此孔口内部的相变仅由压降或模型中其他部分传播来的相变引起。

孔口可以是恒定的，也可以是可变的。当 **Orifice type** 为
`Variable` 时，端口 **S** 处的物理信号会设置控制构件的位置，从而打开和关闭孔口。

### Liquid Orifice

当 **Modeling option** 为 `Liquid operating
condition` 时，模块参数化取决于 **Orifice type** 参数的值。对于所有液体参数化选项，模块以相同方式计算压力损失和压力恢复。

模块通过使用整个孔板上的压力损失与紧邻孔板处的压降之比来考虑压力损失。该比值 *PRloss* 为

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport，

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Aorifice* 是瞬时孔口开口面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。

压力恢复是由于孔口孔后面积增加而在阀中产生的正压力变化。如果你不希望捕捉这种压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1，这会降低模型复杂度。如果孔口孔相对于端口面积非常小，或者下一个下游组件靠近该模块且任何射流都没有空间耗散，请清除此设置。

临界压差 *Δpcrit* 是流动在层流和湍流之间过渡时的压差，

Δpcrit=(pA+pB)2(1−Blam)，

其中：

- *pA* 和 *pB* 分别是端口 **A** 和 **B** 处的压力。
- *Blam* 是 **Laminar flow pressure ratio** 参数的值。

**Nominal Mass Flow Rate Parameterization**

当你将 **Orifice type** 设置为 `Constant` 且将 **Orifice Parameterization** 设置为 `Nominal mass
flow rate` 时，通过孔口的质量流量为

m˙=m˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25，

其中：

- m˙nom 是 **Nominal mass flow
  rate** 参数的值。
- *Δpnom* 是 **Nominal pressure drop rate** 参数的值。
- *vnom* 是标称入口比容。模块根据 **Nominal inlet condition specification** 参数的值，从表格化流体属性数据中确定该值。
- *vin* 是入口比容。

**Liquid Orifice Area Parameterization**

当你将 **Orifice type** 设置为 `Constant` 且将 **Orifice Parameterization** 设置为 `Orifice
area` 时，模块计算质量流量为

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp≈CdAorifice22vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit]1/4，

其中 *Δp* 是孔口上的压降，*pA ̶
pB*。

**Linear - Nominal Mass Flow Rate vs. Control Member Position
Parameterization**

当你将 **Orifice type** 设置为 `Variable` 且将 **Orifice Parameterization** 设置为 `Nominal mass
flow rate vs. control member position` 时，通过可变面积孔口的质量流量为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25，

其中 *λ* 是孔口开度分数，它是总孔口开口面积的一部分。

对于所有可变孔口参数化，模块按如下方式确定孔口开度：

λ=ε(1−fleak)(S−Smin)ΔS+fleak，

其中：

- 当 **Opening orientation** 为 `Positive control member displacement opens
  orifice` 时，*ε* 为 `1`；当 **Opening orientation** 为 `Negative control member displacement opens
  orifice` 时，*ε* 为 `-1`。
- *fleak* 是 **Leakage flow fraction** 参数的值。
- *S* 是端口 **S** 处信号的值。
- *Smin* 是 **Control member position at closed orifice** 参数的值。
- *ΔS* 是 **Control member
  travel between closed and open orifice** 参数的值。

**Linear - Area vs. Control Member Position Parameterization**

当你将 **Orifice type** 设置为 `Variable` 且将 **Orifice
Parameterization** 设置为 `Linear - Area vs. control member
position` 时，孔口面积为

Aorifice=λAmax，

其中 *Amax* 是 **Maximum orifice area** 参数的值。

质量流量为

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit2]1/4。

当节流孔处于接近全开或接近全闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积，其中 *Aleak = fleakAmax*。有关详细信息，请参阅 Numerical Smoothing。

**Tabulated Data - Area vs. Control Member Position Parameterization**

当您将 **Orifice type** 设置为 `Variable` 并将 **Orifice Parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，模块会根据 **Orifice area vector** 和 **Control member position vector** 参数插值计算节流孔面积 *Aorifice*。端口 **S** 处的信号指定控制构件位置。模块使用线性插值在数据点之间进行查询，并对超出表格边界的点使用最近邻外推。

模块使用与 `Linear - Area vs. control member position` 设置相同的方程来计算体积流量。

**Fluid Specific Volume Dynamics**

对于所有参数化方式，模块在仿真期间根据液体状态计算流体比体积。

如果节流孔入口处的流体为液-汽混合物，模块按以下公式计算比体积

vin=(1−xdyn)vliq+xdynvvap，

其中：

- *xdyn* 是入口蒸汽干度。模块对混合物的入口蒸汽干度应用一阶滞后。
- *vliq* 是流体的液相 比体积。
- *vvap* 是流体的汽相 比体积。

如果入口流体为液体或蒸汽，*vin* 分别为相应的液相或汽相比体积。

如果入口蒸汽干度为液-汽混合物，模块应用一阶时间滞后，

dxdyndt=xin−xdynτ，

其中：

- *xdyn* 是动态蒸汽干度。
- *xin* 是当前入口蒸汽干度。
- *τ* 是 **Inlet phase change time constant** 参数的值。

如果入口流体为过冷液体，*xin = 0*。如果入口流体为过热蒸汽，*xin = 1*。

### Vapor Orifice

当 **Modeling option** 为 `Vapor operating
condition` 时，模块行为取决于 **Orifice
type**、**Orifice parameterization** 和
**Opening characteristic** 参数。

**Variable Vapor Orifice**

当您将 **Orifice type** 设置为 `Variable` 且
**Opening characteristic** 设置为
`Linear` 时，模块使用端口
**S** 处的输入来计算孔口开度，

λ=ε(1−fleak)(S−Smin)ΔS+fleak，

其中 *S* 是端口
**S** 处信号的值，*Smin*
和 *ΔS* 分别是 **Control member
position at closed orifice** 和 **Control member travel
between closed and open orifice** 参数的值。

当您将 **Orifice type** 设置为
`Variable` 且 **Opening
characteristic** 设置为 `Tabulated` 时，模块根据 **Control member
position vector** 参数和端口 **S** 处的输入来插值孔口特性。

对于可变孔口，孔口中的流量取决于
**Opening characteristic** 参数：

- `Linear` — 流量能力的度量与端口 **S** 处的控制信号成正比。随着控制信号增大，流量
  能力的度量从指定的最小值缩放到指定的
  最大值。

  当您将 **Orifice parameterization** 设置为
  `Cv flow coefficient` 或 `Kv
  flow coefficient` 时，模块将参数
  **xT pressure differential ratio factor at choked
  flow** 视为与控制信号无关的常数。
- `Tabulated` — 模块将
  流量能力的度量计算为端口
  **S** 处控制信号的函数。此函数使用一维查找表。

  当您将 **Orifice parameterization** 设置为
  `Cv flow coefficient` 或 `Kv
  flow coefficient` 时，模块将参数
  **xT pressure differential ratio factor at choked
  flow** 视为控制信号的函数。

**Cv Flow Coefficient Parameterization**

当您将 **Orifice parametrization** 设置为 `Cv
flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin，

其中：

- *Cv* 是流量
  系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口
  压力。
- *pout* 是出口
  压力。
- *vin* 是入口
  比体积。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是
  等熵指数与 1.4 的比值。
- *xT* 是
   **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数的值
*Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块使用方程

m˙=23CvN6FγxTpinvin。

**Kv Flow Coefficient Parameterization**

当您将 **Orifice parametrization** 设置为 `Kv flow
coefficient` 时，模块使用与
`Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将
*Cv* 替换为
*Kv*。

**Vapor Orifice Area Parameterization**

当您将 **Orifice parametrization** 设置为
`Orifice area` 时，质量流量为

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ]，

其中：

- *Cd* 是
  **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow
pressure ratio** 参数的值
*Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块使用
方程

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2。

### Mass Balance

质量在节流孔中守恒，

m˙A+m˙B=0，

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

### Energy Balance

能量在节流孔中守恒，

ΦA+ΦB=0，

其中：

- *ΦA* 是端口 **A** 处的能量流量。
- *ΦB* 是端口 **B** 处的能量流量。

### 假设和限制

- 阀门与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的节流孔进行建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
