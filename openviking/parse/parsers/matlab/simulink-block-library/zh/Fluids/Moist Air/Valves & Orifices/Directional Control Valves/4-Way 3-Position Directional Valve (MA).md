---
type: simulink-block
title: '4-Way 3-Position Directional Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalvema'
documentation_source_path: 'ref/4way3positiondirectionalvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (MA)

## 端口

### 守恒端口

### **A** — 湿空气进/出端口

与阀门进/出端口相关联的湿空气守恒端口。

### **B** — 湿空气进/出端口

与阀门进/出端口相关联的湿空气守恒端口。

### **P** — 湿空气进/出端口

与阀门进/出端口相关联的湿空气守恒端口。

### **T** — 湿空气进/出端口

与阀门进/出端口相关联的湿空气守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移相关联的物理信号，单位为 m。

## 参数

### 阀门配置

### **正阀芯位置开启连接** — 阀芯处于正位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯处于正位置时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中性阀芯位置开启连接** — 阀芯处于中性位置时打开的流路 `All closed`（默认）| `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

阀芯处于中性位置时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **负阀芯位置开启连接** — 阀芯向负方向运动时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯向负方向运动时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中性阀芯位置开启连接的一致性检查** — 是否检查节流口设置是否一致 `Warning`（默认）| `Error` | `None`

是否检查 **阀门配置** 部分中的中性阀芯位置开启设置是否与最大节流口面积处指定的阀芯位置一致。对于每个启用的节流口，阀芯中性位置处的实际偏移量应与每个单独节流口指定的阀芯偏移量相匹配。

### 模型参数化

### **面积特性** — 节流口的流量方程 `Identical for all flow paths`（默认）| `每条流不同 path`

是否对阀门节流口面积应用统一的或单独的流量方程。当将此参数设置为 `Identical for all flow paths` 时，模块对所有阀门节流口使用相同的节流口和阀芯几何形状、流量、压力及面积向量。当将此参数设置为 `每条流不同 path` 时，可以为每个节流口单独指定这些参数。对于这两种设置，当将 **节流口参数化** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 可变或恒定孔口参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据孔口两侧的压差计算质量流量，或根据质量流量计算压差的方法。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Linear`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 处指定的控制信号转换为所选流量能力度量的方法。

### **Spool travel vector** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀门面积数据对孔口进行参数化时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应于最大开度组件的 *Cv* 系数 `4`（默认）| 正标量

孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应于最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 构件位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，将 **孔口参数化** 设置为 `Kv 流量系数`，并将 **开启特性** 设置为 `表格化`。

### **最大孔口面积** — 最大孔口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间每个孔口的最大开启面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，将 **孔口参数化** 设置为 `孔口面积`，并将 **开启特性** 设置为 `线性`。

### **孔口面积向量** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀门面积数据对孔口进行参数化时的开启面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。按升序列出这些值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，将 **孔口参数化** 设置为 `孔口面积`，并将 **开启特性** 设置为 `表格化`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **孔口参数化** 设置为 `Cv 流量系数` 或 `Kv 流量系数`。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `孔口面积`。

### **最大声速导流** — 组件最大开启时对应的声速导流 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积达到最大时的声速导流值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，将 **孔口参数化** 设置为 `声速导流`，并将 **开启特性** 设置为 `线性`。

### **临界压力比** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，将 **孔口参数化** 设置为 `声速导流`，并将 **开启特性** 设置为 `线性`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **孔口参数化** 设置为 `声速导流`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导流值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **孔口参数化** 设置为 `声速导流`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 与滑阀行程向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速导纳向量。每个导纳对应于 **Spool travel vector** 参数中的一个值。该向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 与滑阀行程向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次发生阻塞时的临界压力比向量，每个临界压力比对应于 **Spool travel vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。该向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开和接近关闭位置时，基于流量响应引入一层渐变。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的节流口出口压力与入口压力之比。在层流中压力损失与质量流量成线性关系，在湍流中成二次关系。

### **Cross-sectional area at ports P, T, A, and B** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

### P-A Orifice

### **Spool position at maximum P-A orifice area** — P-A 节流口完全打开时的滑阀偏移 `5e-3 m`（默认）| 正标量

P-A 节流口完全打开时滑阀从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

**正阀芯位置开启连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-A 节流口在关闭与开启之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将**面积特性**设置为 `每条流不同 path`，将**开启特性**设置为 `Linear`，并设置以下参数之一：

**正阀芯位置开启连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

### **P-A 恒定节流口 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

P-A 节流口的恒定 *Cv* 流量系数值。此参数衡量当由压差驱动时，流体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `每条流不同 path`
2. **节流口参数化**为 `Cv flow coefficient`
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流口设置同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-A 节流口最大 Cv 流量系数** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

当 P-A 节流口完全开启且可用流通面积为最大时的 *Cv* 流量系数值。此参数衡量当由压差驱动时，流体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice Cv flow coefficient vector** — 对应 member position vector 中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-A 节流口的恒定 *Kv* 流量系数值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow
   coefficient`
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

当 P-A 节流口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中值的 *Kv* 系数 | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice spool travel vector** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `每条流不同 path`，将 **开启特性** 设置为 `Tabulated`，并设置以下参数之一：

**正阀芯位置开启连接**为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

### **P-A maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认） | 正标量

阀门运行期间 P-A 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice area vector** — 阀口开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开启面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在全部三个阀芯位置参数中时，此参数才会启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中至少一个：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A constant orifice sonic conductance** — 恒定节流口的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的声速流导。该值是在阻塞起始点测得的，通过阻力元件的质量流量与上游压力和标准条件下质量密度（如 ISO 8778 所定义）乘积之比。此参数决定了在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-A constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-A orifice maximum sonic conductance** — 最大开启节流口 `12` `l/(bar*s)`（默认）对应的声速导纳 | 正标量

当 P-A 节流口完全开启且可用于流动的面积达到最大时的声速导纳值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认） | 正标量

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice sonic conductance vector** — 阀芯行程向量中各值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1×*n* 向量

阻性元件内部的声速导纳向量。每个导纳对应 **P-A orifice spool
travel vector** 参数中的一个值。该向量的大小必须与 **P-A orifice spool travel vector**
参数相同。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice critical pressure ratio vector** — 与滑阀位移向量 `0.3 * ones(1, 6)`（默认）中的值对应的临界压力比 | 1×*n* 向量

临界压力比向量，在该压力比下流动首次发生阻塞，每个临界压力比对应 **P-A orifice spool travel vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。该向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认） | 正标量

用于更精确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

### **P-A orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

### **P-A orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `每条流不同 path`，将 **节流口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

### P-B 节流口

### **P-B 节流口面积最大时的阀芯位置** — P-B 节流口完全开启时的阀芯偏移量 `5e-3 m`（默认）| 正标量

P-B 节流口完全开启时阀芯相对于中位位置的偏移量。

#### 依赖项

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-B 节流口关闭与开启之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `每条流不同 path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

**正阀芯位置开启连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B 恒定节流口 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

P-B 节流口的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下流体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `每条流不同 path`
2. **节流口参数化** 为 `Cv flow coefficient`
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-B orifice maximum Cv flow coefficient** — 对应组件 `4` 最大开启时的 *Cv* 系数 `4`（默认）| 正标量

当 P-B 节流口完全打开且可用于流动的面积达到最大时，*Cv* 流量系数的值。该参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice Cv flow coefficient vector** — 成员位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。该参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-B 节流口的恒定 *Kv* 流量系数值。该参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才会启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Kv flow coefficient** — 与最大开启组件对应的 *Kv* 系数 `3.6`（默认）| 正标量

当 P-B 节流口完全打开且可用于流动的面积达到最大时，*Kv* 流量系数的值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow
   coefficient`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice Kv flow coefficient vector** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Opening
characteristic** 设置为
`Tabulated`，并设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice area vector** — 阀口开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开启面积向量。向量元素必须与
**P-B orifice spool travel vector** 参数中的元素一一对应。
元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Orifice area`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才会启用：
**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为
(pin−pout)/pin，其中 P-B 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中至少一个：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B constant orifice sonic conductance** — 恒定节流口的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的声速流导。该值是在阻塞起始时测得的，通过阻力元件的质量流量与上游压力和标准条件下质量密度（如 ISO 8778 所定义）乘积之比。此参数决定了在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-B constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-B orifice maximum sonic conductance** — 最大开启节流口 `12` `l/(bar*s)`（默认）| 正标量 对应的声速导纳

当 P-B 节流口完全开启且可用于流动的面积达到最大时的声速导纳值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice critical pressure ratio** — 流动首次发生阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice sonic conductance vector** — 与阀芯行程向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声速导纳向量。每个导纳对应于 **P-B orifice spool travel vector** 参数中的一个值。该向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice critical pressure ratio vector** — 与滑阀位移向量 `0.3 * ones(1, 6)` 中的值对应的临界压力比（默认） | 1×*n* 向量

临界压力比向量，在该压力比下流动首次发生阻塞，
每个临界压力比对应于
**P-B orifice spool travel vector** 参数中的一个值。
临界压力比是下游与上游压力之比的一个分数，在该分数下流速达到当地声速。
该向量的大小必须与 **P-B orifice
spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认） | 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Orifice
parameterization** 设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Orifice
parameterization** 设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `每条流不同 path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置开启连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### A-B 孔口

### **A-B 孔口面积最大时的阀芯位置** — A-B 孔口完全打开时的阀芯偏移量 `5e-3 m`（默认）| 正标量

A-B 孔口完全打开时阀芯相对于中位位置的偏移量。

#### 依赖项

要启用此参数，请设置以下参数之一。

**正阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-B 孔口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `每条流不同 path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

**正阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-B`

### **A-B 恒定孔口 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

A-B 孔口的恒定 *Cv* 流量系数值。该参数衡量当由压差驱动时，流体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 设置为 `每条流不同 path`
2. **孔口参数化** 设置为 `Cv flow coefficient`
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置同时出现在以下三个阀芯位置参数中时，此参数才会启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-B 孔口最大 Cv 流量系数** — 组件最大开启时对应的 *Cv* 系数 `4`（默认）| 正标量

A-B 孔口完全打开且可用流通面积最大时的 *Cv* 流量系数值。该参数衡量当由压差驱动时，流体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 设置为 `每条流不同 path`
2. **孔口参数化** 设置为 `Cv flow coefficient`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-B`

### **A-B orifice Cv flow coefficient vector** — *Cv* 系数，对应于成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

A-B 节流孔的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流孔设置出现在所有三个滑阀位置参数中时，此参数才会启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **A-B orifice maximum Kv flow coefficient** — 对应于组件最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

A-B 节流孔完全打开且可用流动面积最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice Kv flow coefficient vector** — *Kv* 系数，对应于成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow
   coefficient`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出各值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Opening
characteristic** 设置为
`Tabulated`，并设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

### **A-B maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-B 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **A-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才会启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice xT pressure differential ratio factor at choked flow** — 压差比因子 `0.7`（默认）| 正标量

A-B 节流口首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice sonic conductance** — 恒定节流口声速流导 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的声速流导。该值是在阻塞起始点测得的，通过阻力元件的质量流量与上游压力和标准条件下质量密度乘积之比，如 ISO 8778 所定义。此参数决定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. 每个参数中以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **A-B constant orifice critical pressure ratio** — 恒定节流口首次发生阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. 每个参数中以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **A-B orifice maximum sonic conductance** — 节流口最大开启时对应的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当 A-B 节流口完全打开且可用流动面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice sonic conductance vector** — 与阀芯行程向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻性元件内部的声速导纳向量。每个导纳对应于 **A-B orifice spool travel vector** 参数中的一个值。向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice critical pressure ratio vector** — 与阀芯行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应于 **A-B orifice spool travel vector** 参数中的一个值。临界压力比为下游与上游压力之比，在该比值下流速达到当地声速。向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下至少一个参数：

**Positive spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-B`

### **A-B orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下至少一个参数：

**Positive spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-B`

### **A-B orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下至少一个参数：

**Positive spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-B`

### A-T Orifice

### **Spool position at maximum A-T orifice area** — A-T 节流口全开时的阀芯偏移量 `5e-3 m`（默认）| 正标量

A-T 节流口全开时阀芯相对于中位位置的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open connections** 设置为 `P-B, A-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-B, A-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯的最大行程距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Opening characteristic** 设置为 `Linear`，并设置以下参数之一：

- **Positive spool position open connections** 设置为 `P-B, A-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-B, A-T`。

### **A-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

A-T 节流口的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Cv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启
连接**、**中位阀芯位置
开启连接**和**负阀芯位置开启连接**。

### **A-T 孔口最大 Cv 流量系数** — 对应组件 `4` 最大开启时的 *Cv* 系数（默认）| 正标量

当 A-T 孔口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Cv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

### **A-T 孔口 Cv 流量系数向量** — 成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` 中值对应的 *Cv* 系数（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应 **A-T 孔口阀芯行程向量**参数中的一个值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。向量的大小必须与 **A-T 孔口阀芯行程
向量**参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Cv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

### **A-T 恒定孔口 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

A-T 孔口的恒定 *Kv* 流量系数值。此参数衡量当由压差驱动时，蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Kv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流孔设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启
连接**、**中位阀芯位置
开启连接**和**负阀芯位置开启连接**。

### **A-T 节流孔最大 Kv 流量系数** — 对应最大开启分量 `3.6`（默认）| 正标量的 *Kv* 系数

当 A-T 节流孔完全打开且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

### **A-T 节流孔 Kv 流量系数向量** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **A-T 节流孔阀芯行程向量**参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。向量的大小必须与 **A-T 节流孔阀芯行程向量**参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

### **A-T 节流孔阀芯行程向量** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将**面积
特性**设置为 `Different for each
flow path`，将**开启
特性**设置为
`Tabulated`，并设置以下参数之一：

- **正阀芯位置开启
  连接**为 `P-B,
  A-T`。
- **中位阀芯位置开启
  连接**为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **负阀芯位置开启
  连接**为 `P-B,
  A-T`。

### **A-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice area vector** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开启面积向量。该向量的元素必须与 **A-T orifice spool travel vector** 参数中的元素一一对应。
元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流口设置出现在所有三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 A-T 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T 恒定节流孔声导** — 恒定节流孔的声导 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含相同节流孔时的声导。该值是在阻塞起始处测得的、通过阻力元件的质量流量与上游压力和 ISO 8778 中定义的标准条件下质量密度乘积之比。该参数决定给定上游压力下允许的最大流量。

#### 依赖

要启用该参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流孔设置出现在全部三个阀芯位置参数中时，才会启用该参数：**正阀芯位置开启
连接**、**中位阀芯位置
开启连接**和**负阀芯位置开启连接**。

### **A-T 恒定节流孔临界压力比** — 恒定节流孔下流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正和负阀芯位置包含相同节流孔时的临界压力比。该值是流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖

要启用该参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流孔设置出现在全部三个阀芯位置参数中时，才会启用该参数：**正阀芯位置开启
连接**、**中位阀芯位置
开启连接**和**负阀芯位置开启连接**。

### **A-T 节流孔最大声导** — 节流孔最大开启时对应的声导 `12` `l/(bar*s)`（默认）| 正标量

当 A-T 节流孔完全打开且可用于流动的面积最大时的声导值。

#### 依赖

要启用该参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **节流孔参数化**为
   `Sonic conductance`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-B,
     A-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-B,
     A-T`。

### **A-T orifice critical pressure ratio** — 下游与上游压力之比，在该比值下流动首次阻塞 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice sonic conductance vector** — 与滑阀行程向量中的值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声导向量。每个声导对应于 **A-T orifice spool
travel vector** 参数中的一个值。该向量的大小必须与 **A-T orifice spool travel vector**
参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice critical pressure ratio vector** — 与滑阀行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **A-T orifice spool travel vector**
参数中的一个值。临界压力比为下游与上游压力之比，在该比值下流速达到当地声速。该向量的大小必须与 **A-T orifice
spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-B, A-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-B, A-T`。

### **A-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-B, A-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-B, A-T`。

### **A-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-B, A-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-B, A-T`。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流口的阀芯偏移量 `5e-3 m`（默认）| 正标量

从中间位置到完全打开 B-T 节流口的阀芯偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open connections** 设置为 `P-A, B-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Opening characteristic** 设置为 `Linear`，并设置以下参数之一：

- **Positive spool position open connections** 设置为 `P-A, B-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

B-T 节流口的恒定 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才会启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice maximum Cv flow coefficient** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

当 B-T 节流口完全打开且可用流通面积为最大值时的 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice Cv flow coefficient vector** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel
vector** 参数相同。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Cv flow
   coefficient`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

B-T 节流口的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Kv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **正阀芯位置开启
     连接**为 `P-A,
     B-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-A,
     B-T`。

**注意：**

仅当 B-T 孔口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启
连接**、**中位阀芯位置
开启连接**和**负阀芯位置开启连接**。

### **B-T 孔口最大 Kv 流量系数** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

当 B-T 孔口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-A,
     B-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-A,
     B-T`。

### **B-T 孔口 Kv 流量系数向量** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **B-T 孔口阀芯行程向量**参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。向量的大小必须与 **B-T 孔口阀芯行程
向量**参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为 `P-A,
     B-T`。
   - **中位阀芯位置开启
     连接**为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **负阀芯位置开启
     连接**为 `P-A,
     B-T`。

### **B-T 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将**面积
特性**设置为 `Different for each
flow path`，将**开启
特性**设置为
`Tabulated`，并设置以下参数之一：

- **正阀芯位置开启
  连接**为 `P-A,
  B-T`。
- **中位阀芯位置开启
  连接**为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **负阀芯位置开启
  连接**为 `P-A,
  B-T`。

### **B-T maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 B-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice area vector** — 阀门开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开度面积向量。该向量的元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Orifice area`
3. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在所有三个阀芯位置参数中时，此参数才会启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 B-T 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T constant orifice sonic conductance** — 恒定节流口声导 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的声导。该值是在阻塞起始处测得的、通过阻力元件的质量流量与上游压力和 ISO 8778 中定义的标准条件下质量密度乘积之比。该参数决定给定上游压力下允许的最大流量。

#### 依赖

要启用该参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个阀芯位置参数中时，才会启用该参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到其最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖

要启用该参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个阀芯位置参数中时，才会启用该参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice maximum sonic conductance** — 最大开度节流口对应的声导 `12` `l/(bar*s)`（默认）| 正标量

当 B-T 节流口完全打开且可用于流动的面积最大时的声导值。

#### 依赖

要启用该参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice critical pressure ratio** — 下游与上游压力之比，在该比值下流动首次发生阻塞 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice sonic conductance vector** — 与滑阀行程向量中的值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声导向量。每个声导对应于 **B-T orifice spool
travel vector** 参数中的一个值。该向量的大小必须与 **B-T orifice spool travel vector**
参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice critical pressure ratio vector** — 与滑阀行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流动首次发生阻塞时的临界压力比向量，其中每个临界压力比对应于 **B-T orifice spool travel vector**
参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。该向量的大小必须与 **B-T orifice
spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流不同
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T`。
- **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设置为 `P-A, B-T`。

### P-T Orifice

### **Spool position at maximum P-T orifice area** — P-T 节流口完全打开时的阀芯偏移量 `5e-3 m`（默认）| 正标量

P-T 节流口完全打开时，阀芯相对于中位位置的偏移量。

#### 依赖关系

要启用此参数，请将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Opening characteristic** 设置为 `Linear`，并将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice maximum Cv flow coefficient** — 对应于组件最大打开状态的 *Cv* 系数 `4`（默认）| 正标量

P-T 节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice Cv flow coefficient vector** — 成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）中值对应的 *Cv* 系数 | 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认） | 正标量

当 P-T 节流口完全打开且可用于流动的面积达到最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中值对应的 *Kv* 系数 | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流不同 path`，将 **Opening characteristic** 设置为 `Tabulated`，并将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认） | 正标量

阀门运行期间 P-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **P-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-T 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice maximum sonic conductance** — 最大开度节流口对应的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当 P-T 节流口完全打开且可用流动面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-T orifice critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速决定）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流不同 path`
2. **Orifice parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Linear`
4. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice sonic conductance vector** — 与滑阀位移向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声速流导向量。每个流导对应 **P-T orifice spool travel vector** 参数中的一个值。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. **中位开口连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 孔口临界压力比向量** — 与滑阀行程向量 `0.3 * ones(1, 6)` 中值对应的临界压力比（默认）| 1×*n* 向量

流量首次发生阻塞时的临界压力比向量，每个临界压力比对应于
**P-T 孔口滑阀行程向量**参数中的一个值。临界压力比是
下游与上游压力之比中流速达到当地声速时的分数值。
该向量的大小必须与 **P-T 孔口滑阀行程向量**参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流不同
   path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. **中位开口连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 孔口亚声速指数** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖项

要启用此参数，请将**面积特性**设置为 `Different for each
flow path`，将**孔口参数化**设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**中位开口连接**为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T 孔口 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将**面积特性**设置为 `Different for each
flow path`，将**孔口参数化**设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**中位开口连接**为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T 孔口 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将**面积特性**设置为 `Different for each
flow path`，将**孔口参数化**设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**中位开口连接**为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的四位三通方向阀

4-Way 3-Position Directional Valve (MA) 模块对湿空气网络中的具有四个开口的阀进行建模，通常位于执行器、泵与油箱之间。单个阀芯根据端口 **S** 处的信号控制阀的操作。您可以通过在 **Neutral spool position open connections** 参数中指定当阀芯处于中立位置（居中于 0 m）时打开的孔口，在 **Positive spool position open connections** 参数中指定当阀芯向正方向移动时打开的孔口，以及在 **Negative spool position open connections** 参数中指定当阀芯向负方向移动时打开的孔口，来设置阀的基线配置。您可以使用 **Orifice parameterization** 参数将阀模型指定为用户提供数据的线性关系或函数。

此模块是一个复合组件，由多个 Orifice (MA) 模块实例组成。有关阀参数化和模块计算的更多信息，请参阅 Orifice (MA) 模块。

在此示例配置中，**Neutral spool position open connections** 参数为 `All closed`。当阀芯处于中立位置时，所有孔口均关闭，无流量：

在此配置中，**Negative spool position open connections** 为 `P-A, B-T`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开，允许流量通过。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭，无流量：

在此配置中，**Positive spool position open connections** 为 `P-B, A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开，允许流量通过，而端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭：

此示意图显示了此配置：

左侧对应正位置，右侧对应负位置。

### 滑阀位移与阀配置

*滑阀行程*是指节流口从关闭位置到完全打开所需的滑阀移动量。您可以使用**阀配置**部分中的参数来定义滑阀行程。下表显示了模块如何根据阀节流口参数化和流路特性来计算行程。

端口 **S** 指定的滑阀移动方向取决于滑阀行程和节流口方向。

| 节流口打开时的滑阀位置 | 滑阀移动量，*ΔS* |
| --- | --- |
| 始终关闭（在任何滑阀位置配置中均未选择该节流口） | 不适用 |
| 始终打开（在正、中性和负滑阀位置配置中均选择了该节流口） | 不适用 |
| 负 | *S*orifice\_max + 滑阀行程 – **S** |
| 负和中性 | *S*orifice\_max + 滑阀行程 – **S** |
| 正 | *S*orifice\_max – 滑阀行程 + **S** |
| 正和中性 | *S*orifice\_max – 滑阀行程 + **S** |
| 中性 | \|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |
| 正和负 | –\|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |

*S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积饱和为泄漏面积；当节流口完全打开时，节流口面积饱和为最大节流口面积。当节流口完全打开时，*ΔS* 等于滑阀行程，因此大于滑阀行程的 *ΔS* 值不会进一步增大节流口面积。

**中性滑阀位置打开连接的一致性检查**参数验证以下内容：

- **中性滑阀位置打开连接**中列出的任何节流口在 **S** 处信号为 0 时打开
- **中性滑阀位置打开连接**中未列出的任何节流口在 **S** 处信号为 0 时关闭

您可以选择在任何滑阀位置违反此检查时接收警告或错误。

下表显示了 4-Way 3-Position Directional Valve (MA) 模块的可能配置。

| 配置 | 参数值 |
| --- | --- |
|  | 在中位时四个节流口全部关闭。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时四个节流口全部开启。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 |
|  | 节流口 A-T 和 B-T 开启。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 在中位时节流口 P-A 和 A-T 开启。节流口 P-B 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, A-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 A-T 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 B-T 开启。节流口 P-A、P-B 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 P-A 和 P-B 开启。节流口 A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-A 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 开启。节流口 P-A、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 和 B-T 开启。节流口 P-A 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-B, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中位时开启，并在阀芯位移时关闭。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |
|  | 节流口 P-A 是恒定节流口。在中位时节流口 P-B、A-T 和 B-T 开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = any value - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 节流口 P-B 是恒定节流口。在中位时节流口 P-A、A-T、B-T 开启。    - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`    - **P-A 节流口最大面积处的阀芯位置** > –P-A 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-A 关闭。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。端口 **B** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 A-T 开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = any value - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 B-T 开启。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`  - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-A, P-B`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |

### 阀门节流口参数化

**Orifice parameterization** 参数指定一个或所有阀门节流口的开口面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路应用相同的数据。当选择 `Different for all flow paths` 时，模块对每条流路使用各自的参数化。

模块用于控制每个节流口的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量取决于端口 **S** 处的阀芯位置。当阀芯位移以打开节流口时，流量能力的度量从指定的最小值缩放到指定的最大值。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处阀芯位置的函数。该函数使用一维查找表。

**Orifice parameterization** 参数决定模块如何计算每个节流口中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 对每个节流口中的流量进行缩放。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，对每个节流口中的流量进行缩放。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Orifice area` — 节流口面积的尺寸对每个节流口中的流量进行缩放。

### 可视化节流口开度

要可视化阀芯偏移和最大位移，请右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的节流口。该图显示声导、*Kv* 流量系数、*Cv* 流量系数或节流口面积随阀芯位置的变化。

当 **Valve Configuration** 参数中的正、中和负设置具有相同的节流口时，该图将节流口开度显示为常数。

要在更改模块参数后更新数据，请点击图形窗口上的 **Reload Data**。

此图显示了一个阀门配置示例。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`
- **Neutral spool position open connections** 为 `P-T`
- **Negative spool position open connections** 为 `P-B, A-T`

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`

所有其他阀芯位置均为默认值。

每个节流口的面积与阀芯位置的关系图。

可视化显示 P-A 节流口在阀芯位置 `-2.53e-3` 和 `2.53e-3` m 之间打开。由于 P-A 节流口仅在阀芯沿正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，您可以更改：

- **Spool position at maximum P-A orifice area** 为大于 0.005 m 的值
- **Consistency check for neutral spool position open connections** 为 `None`
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，则可能需要按混合气体比重的平方根来缩放声速流导。
- 此模块不对超声速流进行建模。
- 阀门与环境之间不存在热交换。
