---
type: simulink-block
title: 'Orifice (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Valves and Orifices'
documentation_page: 'orifice2p'
documentation_source_path: 'ref/orifice2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (2P)

## 端口

### 守恒

### **A** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### **B** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。
### 输入

### **S** — 控制构件位置，m 物理信号

设置孔口开度的控制构件位置。

#### 依赖关系

要启用此端口，请将 **Orifice type** 设置为
`Variable`。

## 参数

### **Modeling option** — 流体相的建模选项 `Liquid operating condition` (默认) | `Vapor operating condition`

孔口处流体相的建模选项。如果模块位置处的两相流体处于液态，请将此参数设置为
`Liquid operating condition`。如果模块位置处的两相流体处于气态，请将此参数设置为
`Vapor operating condition`。

### 参数

### **Orifice type** — 恒定或可变孔口 `Variable` (默认) | `Constant`

孔口类型。将此参数设置为 `Variable` 时，孔口面积根据端口
**S** 收到的输入信号而变化。

### **Orifice parameterization** — 可变或恒定孔口参数化 `Linear - Area vs. control member position` (默认) | `Orifice area` | `Nominal mass flow rate` | `Linear - Nominal mass flow rate vs. control member position` | `Tabulated data - Area vs. control member position` | `Cv flow coefficient` | `Kv flow coefficient`

模块用于根据孔口两端压差计算质量流量或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid
operating condition` 且 **Orifice
type** 为 `Variable` 时，此参数的选项为：

- `Linear - Area vs. control member
  position`
- `Linear - Nominal mass flow rate vs. control
  member position`
- `Tabulated data - Area vs. control member
  position`

当 **Modeling option** 为 `Liquid
operating condition` 且 **Orifice
type** 为 `Constant` 时，此参数的选项为：

- `Orifice area`
- `Nominal mass flow rate`

当 **Modeling option** 为 `Vapor operating
condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Nominal mass flow rate** — 额定质量流量 `0.1` kg/s (默认) | 正标量

通过恒定孔口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，
将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Nominal mass flow
rate`。

### **Nominal pressure drop** — 额定压降 `0.001` MPa (默认) | 正标量

通过恒定孔口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，
将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Nominal mass flow
rate`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature` (默认) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 参数的值以及 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定孔口额定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Nominal mass flow
  rate`。
- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa (默认) | 正标量

额定条件下的入口压力。模块根据 **Nominal inlet pressure** 参数的值以及 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Nominal mass flow
  rate`。
- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`。

### **Nominal inlet temperature** — 流体温度 `293.15` K (默认) | 正标量

额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，
  **Orifice parameterization** 为
  `Nominal mass flow rate`，
  且 **Nominal inlet condition
  specification** 为
  `Temperature`。
- **Orifice type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`，且
  **Nominal inlet condition
  specification** 为
  `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸气质量分数 `0` (默认) | 范围 [0,1] 内的正标量

额定运行条件下的入口混合物蒸气质量分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，
  **Orifice parameterization** 为
  `Nominal mass flow rate`，
  且 **Nominal inlet condition
  specification** 为 `Vapor
  quality`。
- **Orifice type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`，且
  **Nominal inlet condition
  specification** 为 `Vapor
  quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0` (默认) | 范围 [0,1] 内的正标量

额定运行条件下的入口混合物体积分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，
  **Orifice parameterization** 为
  `Nominal mass flow rate`，
  且 **Nominal inlet condition
  specification** 为 `Vapor void
  fraction`。
- **Orifice type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`，且
  **Nominal inlet condition
  specification** 为 `Vapor void
  fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg (默认) | 正标量

额定运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，
  **Orifice parameterization** 为
  `Nominal mass flow rate`，
  且 **Nominal inlet condition
  specification** 为 `Specific
  enthalpy`。
- **Orifice type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`，且
  **Nominal inlet condition
  specification** 为 `Specific
  enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg (默认) | 正标量

额定运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Constant`，
  **Orifice parameterization** 为
  `Nominal mass flow rate`，
  且 **Nominal inlet condition
  specification** 为 `Specific
  internal energy`。
- **Orifice type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Linear - Nominal mass flow rate vs.
  control member position`，且
  **Nominal inlet condition
  specification** 为 `Specific
  internal energy`。

### **Orifice area** — 孔口开口面积 `1e-4` `m^2` (默认) | 正标量

孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Orifice
area`。

### **Control member position at closed orifice** — 控制构件偏移 `0` m (默认) | 正标量

控制构件偏移，即孔口完全关闭时 **S** 处的值。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear – Nominal mass flow rate vs.
  control member position` 或
  `Linear – Area vs. control member
  position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Opening characteristic** 为
  `Linear`。

### **Control member travel between closed and open orifice** — 控制构件行程 `5e-3` m (默认) | 正标量

控制构件在孔口关闭与打开之间移动的距离。
当 **Opening orientation** 设置为
`Positive control member displacement opens
orifice` 时，孔口在 **Control member position at closed orifice** 与
**Control member travel between closed and open
orifice** 参数之和处完全打开。当 **Opening
orientation** 设置为 `Negative control member
displacement opens orifice` 时，孔口在 **Control member position at
closed orifice** 与 **Control member travel
between closed and open orifice** 参数之差处完全打开。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear – Nominal mass flow rate vs.
  control member position` 或
  `Linear – Area vs. control member
  position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Opening characteristic** 为
  `Linear`。

### **Opening orientation** — 打开孔口的位移方向 `Positive control member displacement opens orifice` (默认) | `Negative control member displacement opens orifice`

打开可变孔口的构件位移方向。正方向表示 **S** 处信号增加会打开孔口。负方向表示 **S** 处信号减小会打开孔口。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear – Nominal mass flow rate vs.
  control member position` 或
  `Linear – Area vs. control member
  position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Opening characteristic** 为
  `Linear`。

### **Nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` kg/s (默认) | 正标量

在典型、设计或额定条件下通过完全打开孔口的质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，
**Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear – Nominal
mass flow rate vs. control member position`。

### **Nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` MPa (默认) | 正标量

在典型、设计或额定条件下完全打开孔口上的压降。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，
**Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear – Nominal
mass flow rate vs. control member position`。

### **Maximum orifice area** — 最大孔口开口面积 `1e-4 m^2` (默认) | 正标量

孔口完全打开时的面积。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear – Area vs. control member
  position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Orifice area`，且
  **Opening characteristic** 为
  `Linear`。

### **Control member position vector** — 控制构件位置向量 `[0, .002, .004, .007, .017] m` (默认) | 1-by-*n* vector

用于表格化孔口参数化的控制构件位置向量。向量元素与 **Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的值一一对应。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating
  condition`，且 **Orifice
  parameterization** 为
  `Tabulated data - Area vs. control
  member position`。
- **Modeling option** 为
  `Vapor operating condition`
  且 **Opening characteristic** 为
  `Tabulated`。

### **Orifice area vector** — 孔口开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于孔口面积表格化参数化的孔口面积值向量。此向量中的值与 **Control member position vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Tabulated data - Area vs. control
  member position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，
  **Orifice parameterization** 为
  `Orifice area`，且
  **Opening characteristic** 为
  `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64` (默认) | 正标量

实际流量与理想流量之比。此参数用于考虑孔口方程中未捕获的实际损耗。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Orifice area`。
- **Modeling option** 为
  `Liquid operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Modeling option** 为
  `Vapor operating
  condition`，**Orifice
  type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Orifice area`。

### **Pressure recovery** — 是否考虑面积扩大中的压力升高 `off` (默认) | `on`

是否考虑从入口到孔口压降之后压力的小幅升高。当流体射流离开孔口时，它会耗散并膨胀以充满端口面积，从而导致这种小幅压力升高。当清除 **Pressure recovery** 复选框时，模块不会对此压力升高建模。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Liquid operating condition`，并且满足以下任一条件：

- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Orifice area`。

### **开启特性** — 将控制信号转换为流量容量度量值的方法 `Linear`（默认）| `Tabulated`

将端口
**S** 处指定的控制信号转换为所选流量
容量度量值的方法。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为
`Vapor operating condition`，并将
**孔口类型** 设置为
`Variable`。

### **Cv 流量系数** — 流量系数 `4`（默认）| 正标量

常数 *Cv*
流量系数的值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为
`Vapor operating condition`，
将 **孔口类型** 设置为
`Constant`，并将 **孔口
参数化** 设置为 `Cv flow
coefficient`。

### **最大 Cv 流量系数** — 对应组件最大开启的 *Cv* 系数 `4`（默认）| 正标量

孔口完全开启且可用于流动的面积最大时的 *Cv* 流量
系数值。此参数衡量蒸气在压差
驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项**
设置为 `Vapor operating condition`，
将 **孔口类型** 设置为
`Variable`，将 **孔口
参数化** 设置为 `Cv flow
coefficient`，并将 **开启
特性** 设置为
`Linear`。

### **Cv 流量系数向量** — 对应构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量
系数向量。每个系数对应
**控制构件位置向量** 参数中的一个值。此
参数衡量蒸气在压差驱动下穿过阻力
元件的难易程度。向量的大小
必须与 **控制构件位置
向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **建模选项**
设置为 `Vapor operating condition`，
将 **孔口类型** 设置为
`Variable`，将 **孔口
参数化** 设置为 `Cv flow
coefficient`，并将 **开启
特性** 设置为
`Tabulated`。

### **Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

常数 *Kv*
流量系数的值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为
`Vapor operating condition`，
将 **孔口类型** 设置为
`Constant`，并将 **孔口
参数化** 设置为 `Kv flow
coefficient`。

### **最大 Kv 流量系数** — 对应组件最大开启的 *Kv* 系数 `3.6`（默认）| 正标量

孔口完全开启且可用于流动的面积最大时的 *Kv* 流量
系数值。此参数衡量蒸气在压差
驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项**
设置为 `Vapor operating condition`，
将 **孔口类型** 设置为
`Variable`，将 **孔口
参数化** 设置为 `Kv flow
coefficient`，并将 **开启
特性** 设置为
`Linear`。

### **Kv 流量系数向量** — 对应构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量
系数向量。每个系数对应
**控制构件位置向量** 参数中的一个值。此
参数衡量蒸气在压差驱动下穿过阻力
元件的难易程度。向量的大小
必须与 **控制构件位置
向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **建模选项**
设置为 `Vapor operating condition`，
将 **孔口类型** 设置为
`Variable`，将 **孔口
参数化** 设置为 `Kv flow
coefficient`，并将 **开启
特性** 设置为
`Tabulated`。

### **xT 阻塞流压差比因子** — 压差比 `0.7`（默认）| 正标量

入口压力
*pin* 与出口
压力 *pout* 之间的比，定义为首次发生阻塞处的 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor
operating condition`，并将 **孔口
参数化** 设置为 `Cv flow
coefficient` 或 `Kv flow
coefficient`。

### **泄漏流量分数** — 流量的比率 `1e-6`（默认）| 正标量

孔口关闭时与开启时的流量之比。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为
`Variable`，并设置任意其他参数组合，但以下情况除外：

- **建模选项** 为
  `Liquid operating
  condition`，且 **孔口
  参数化** 为
  `Tabulated data - Area vs. control
  member position`。
- **建模选项** 为
  `Vapor operating condition`，
  且 **开启特性** 为
  `Tabulated`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当孔口处于接近开启或接近关闭
位置时，为流量响应引入一层渐变。将此参数设置为小于一的非零值，以
提高在这些区域中仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为
`Variable`，并设置任意其他参数组合，但以下情况除外：

- **建模选项** 为
  `Liquid operating
  condition`，且 **孔口
  参数化** 为
  `Tabulated data - Area vs. control
  member position`。
- **建模选项** 为
  `Vapor operating condition`，
  且 **开启特性** 为
  `Tabulated`。

### **入口相变时间常数** — 液体比容的滞后 `0.1` s（默认）| 正标量

计算流体比容时液体-蒸气混合物的时间滞后。

#### 依赖关系

要启用此参数，请将 **建模选项**
设置为 `Liquid operating condition`。

### **层流压力比** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

孔口出口压力与孔口入口压力之比，在该比值下流体在层流和湍流状态之间过渡。
在层流中压力损失与质量流量成线性关系，在湍流中成二次关系。

### **端口 A 和 B 的横截面积** — 阀端口面积 `0.01` m^2（默认）| 正标量

孔口端口 **A** 和
**B** 的面积。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a：对蒸气阀或液体阀建模

您现在可以使用 **建模选项** 参数在两相流体处于蒸气或液体状态时指定
孔口。两种建模
选项还都包含新的孔口参数化。

当 **建模选项** 为 `Liquid operating
condition` 时，您现在可以将 **孔口
参数化** 设置为：

- `Linear - Area vs. control member
  position`
- `Tabulated data - Area vs. control member
  position`
- `Orifice area`

当 **建模选项** 为 `Vapor operating
condition` 时，您现在可以将 **孔口
参数化** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

要保留先前版本中的恒定孔口行为，请将 **建模
选项** 设置为 `Liquid operating condition`，并将
**孔口参数化** 设置为 `Nominal mass flow
rate`。要保留先前版本中的可变孔口行为，请将 **建模选项** 设置为 `Liquid operating
condition`，并将 **孔口参数化** 设置为
`Linear – Nominal mass flow rate vs. control member
position`。

## 描述

两相流体网络中的恒定面积或可变面积孔口

Orifice (2P) 模块对两相流体网络中因恒定面积或可变面积孔口引起的压力损失进行建模。**建模选项** 参数控制
为对蒸气或液体建模而设计的阀的参数化选项，但
不影响流体属性。该模块根据入口条件计算阀内部的
流体属性。流体与
环境之间没有热交换，因此孔口内部的相变仅由于压降
或模型中其他部分传播的相变而发生。

孔口可以是恒定的或可变的。当 **孔口类型** 为
`Variable` 时，端口
**S** 处的物理信号设置控制构件的位置，从而开启和
关闭孔口。

### 液体孔口

当 **建模选项** 为 `Liquid operating
condition` 时，该模块的参数化取决于
**孔口类型** 参数的值。对于所有液体参数化
选项，该模块以相同方式计算压力
损失和压力恢复。

该模块通过使用整个孔口上的压力损失与紧邻孔板两侧的压降之比来计入压力损失。此比率，
*PRloss*，为

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport,

其中：

- *Cd* 是
  **排放系数** 参数的值。
- *Aorifice* 是
  瞬时孔口开启面积。
- *Aport* 是
  **端口 A 和 B 的横截面积**
  参数的值。

压力恢复是由于孔口孔后的面积增加而在阀中产生的正压力变化。如果您不希望捕获此压力增加，
请清除 **压力恢复** 复选框。在这种情况下，
*PRloss* 为 1，这会降低
模型复杂度。如果孔口孔相对于
端口面积相当小，或者下游下一个组件靠近该模块且射流
没有消散空间，请清除此设置。

临界压差 *Δpcrit* 是
流动在层流和湍流之间过渡时的压差，

Δpcrit=(pA+pB)2(1−Blam),

其中：

- *pA* 和
  *pB* 分别是
  端口 **A** 和 **B** 处的压力。
- *Blam* 是
  **层流压力比** 参数的值。

**额定质量流量参数化**

当您将 **孔口类型** 设置为 `Constant`，并将
**孔口参数化** 设置为 `Nominal mass
flow rate` 时，通过孔口的质量流量为

m˙=m˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中：

- *m˙nom* 是 **额定质量流量**
  参数的值。
- *Δpnom* 是
  **额定压降率**
  参数的值。
- *vnom* 是额定
  入口比容。该模块根据
  **额定入口条件规格**
  参数的值，从
  表格化流体属性数据确定此值。
- *vin* 是入口
  比容。

**液体孔口面积参数化**

当您将 **孔口类型** 设置为 `Constant`，并将
**孔口参数化** 设置为 `Orifice
area` 时，该模块按如下方式计算质量流量：

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp≈CdAorifice22vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit]1/4,

其中 *Δp* 是孔口上的压降，*pA ̶
pB*。

**线性 - 额定质量流量与控制构件位置关系
参数化**

当您将 **孔口类型** 设置为 `Variable`，并将
**孔口参数化** 设置为 `Nominal mass
flow rate vs. control member position` 时，通过可变面积孔口的质量流量
为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中 *λ* 是孔口开启分数，
即孔口总开启面积的一部分。

对于所有可变孔口
参数化，该模块按如下方式确定孔口开启：

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

其中：

- *ε* 在
  **开启方向** 为
  `Positive control member displacement opens
  orifice` 时为 `1`，在
  **开启方向** 为
  `Negative control member displacement opens
  orifice` 时为 `-1`。
- *fleak* 是
  **泄漏流量分数** 参数的值。
- *S* 是端口
  **S** 处信号的值。
- *Smin* 是
  **孔口关闭时的控制构件位置**
  参数的值。
- *ΔS* 是 **孔口关闭到开启之间的控制构件
  行程** 参数的值。

**线性 - 面积与控制构件位置关系参数化**

当您将 **孔口类型** 设置为
`Variable`，并将 **孔口
参数化** 设置为 `Linear - Area vs. control member
position` 时，孔口面积为

Aorifice=λAmax,

其中 *Amax* 是
**最大孔口面积** 参数的值。

质量流量为

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit2]1/4.

当孔口处于接近开启或接近关闭
位置时，您可以通过调整
**平滑因子** 参数来保持仿真的数值稳健性。如果
**平滑因子** 参数非零，该模块
会在
*Aleak* 与
*Amax* 之间平滑饱和开启面积，其中
*Aleak =
fleakAmax*。有关
详细信息，请参阅数值平滑。

**表格数据 - 面积与控制构件位置关系参数化**

当您将 **孔口类型** 设置为 `Variable`，并将
**孔口参数化** 设置为 `Tabulated data
- Area vs. control member position` 时，该模块根据
**孔口面积向量** 和 **控制构件
位置向量** 参数插值孔口面积 *Aorifice*。端口
**S** 处的信号指定控制构件位置。该模块使用
线性插值在数据点之间查询，并对超出表格边界的点使用最近邻外推。

该模块使用与 `Linear - Area vs. control member
position` 设置相同的方程计算体积流量。

**流体比容动态**

对于所有参数化，该模块在仿真期间基于液体状态计算流体比容。

如果孔口入口处的流体是液体-蒸气混合物，则该模块
按如下方式计算比容：

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸气
  干度。该模块对混合物的入口蒸气
  干度应用一阶滞后。
- *vliq* 是流体的液体
  比容。
- *vvap* 是流体的蒸气
  比容。

如果入口流体是液体或蒸气，
*vin* 是相应的液体
或蒸气比容。

如果入口蒸气干度处于液体-蒸气混合物状态，则该模块应用一阶时间滞后，

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 是动态
  蒸气干度。
- *xin* 是当前入口
  蒸气干度。
- *τ* 是 **入口相变
  时间常数** 参数的值。

如果入口流体是过冷液体，
则 *xin = 0*。如果入口流体是
过热蒸气，则 *xin = 1*。

### Vapor Orifice

当 **Modeling option** 为 `Vapor operating condition` 时，模块行为取决于 **Orifice type**、**Orifice parameterization** 和 **Opening characteristic** 参数。

**可变 Vapor Orifice**

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear` 时，模块使用端口 **S** 处的输入计算孔口开度，

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

其中 *S* 是端口 **S** 处信号的值，*Smin* 和 *ΔS* 分别是 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数的值。

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Tabulated` 时，模块根据 **Control member position vector** 参数和端口 **S** 处的输入对孔口特性进行插值。

对于可变孔口，孔口中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量与端口 **S** 处的控制信号成正比。随着控制信号增大，流量能力的度量从指定的最小值缩放到指定的最大值。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为独立于控制信号的常量。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处控制信号的函数。此函数使用一维查找表。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为控制信号的函数。

**Cv 流量系数参数化**

当您将 **Orifice parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常量，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值为 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞流，模块使用以下方程

m˙=23CvN6FγxTpinvin.

**Kv 流量系数参数化**

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**Vapor Orifice 面积参数化**

当您将 **Orifice parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞流，模块使用以下方程

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2.

### 质量平衡

孔口中的质量守恒，

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

### 能量平衡

孔口中的能量守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的孔口建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
