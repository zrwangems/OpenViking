---
type: simulink-block
title: '3-Way Directional Valve (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: '3waydirectionalvalvema'
documentation_source_path: 'ref/3waydirectionalvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# 3-Way Directional Valve (MA)

## 端口

### 守恒

### **A** — 湿空气端口 湿空气

阀的入口或出口点。

### **P** — 湿空气端口 湿空气

阀的入口或出口点。

### **T** — 湿空气端口 湿空气

阀的入口或出口点。

### 输入

### **S** — 控制构件位移，m physical signal

阀芯位置位移，以 m 为单位，作为 physical signal 接收。对于在正阀芯位置打开的流路，正信号打开孔口。对于在负阀芯位置打开的流路，负信号打开孔口。

## 参数

### 阀配置

### **正阀芯位置开启连接** — 当阀芯处于正位置时打开的流路 `All closed` (默认) | `P-A, A-T, P-T` | `P-A` | `A-T` | `P-T`

当阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### **负阀芯位置开启连接** — 当阀芯沿负方向移动时打开的流路 `All closed` (默认) | `P-A, A-T, P-T` | `P-A` | `A-T` | `P-T`

当阀芯沿负方向移动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### 模型参数化

### **面积特性** — 孔口的流量方程 `Identical for all flow paths` (默认) | `Different for each flow path`

是否对阀孔口面积应用统一的或单独的流量方程。当您将此参数设置为 `Identical for all flow paths` 时，模块对所有阀孔口使用相同的孔口和阀芯几何形状、流量、压力和面积向量。当您将此参数设置为 `Different for each flow path` 时，您可以单独指定每个孔口的这些参数。对于这两种设置，当您将 **阀参数化** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，孔口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **阀参数化** — 可变或恒定孔口参数化 `Cv flow coefficient` (默认) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据孔口两端的压差计算质量流量或根据质量流量计算压差的方法。

### **关闭和打开孔口之间的阀芯行程** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **开启特性** 设置为 `Linear`。

### **开启特性** — 将控制信号转换为流量能力度量的方法 `Linear` (默认) | `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

根据表格化阀面积数据参数化孔口时的阀芯行程距离向量。向量元素必须与 **孔口面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 对应于最大开启组件的 *Cv* 系数 `4` (默认) | positive scalar

当孔口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 构件位置向量中值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (默认) | 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应于 **控制构件位置向量** 参数中的一个值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。向量的大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应于最大开启组件的 *Kv* 系数 `3.6` (默认) | positive scalar

当孔口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 构件位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (默认) | 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应于 **控制构件位置向量** 参数中的一个值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。向量的大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大孔口面积** — 最大孔口开启面积 `1e-4 m^2` (默认) | positive scalar

阀操作期间每个孔口的最大的开启面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Linear`。

### **孔口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (默认) | 1-by-*n* vector

根据表格化阀面积数据参数化孔口时的开启面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7` (默认) | positive scalar

入口压力 *pin* 和出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **阀参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **流量系数** — 流量系数 `0.64` (默认) | positive scalar

用于解释理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Orifice area`。

### **最大声速导** — 对应于最大开启组件的声速导 `12 l/(bar*s)` (默认) | positive scalar

当端口 **S** 指定的控制信号为 `1` 且可用于流动的横截面积最大时，声速导的值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **临界压力比** — 流动首次阻塞时的下游和上游压力之比 `0.3` (默认) | positive scalar

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5` (默认) | positive scalar

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **阀参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K` (默认) | scalar

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用在不同参考值下获得的声速导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **阀参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3` (默认) | positive scalar

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用在不同参考值下获得的声速导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **阀参数化** 设置为 `Sonic conductance`。

### **声速导向量** — 阀芯行程向量中值对应的声速导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)` (默认) | vector of positive values

阻力元件内部的声速导向量。每个声速导对应于 **阀芯行程向量** 参数中的一个值。向量的大小必须与 **阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **临界压力比向量** — 阀芯行程向量中值对应的临界压力比 `0.3 * ones(1,6)` (默认) | vector of positive numbers

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **阀芯行程向量** 参数中的一个值。临界压力比是下游与上游压力之比，此时流速达到当地声速。向量的大小必须与 **阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **泄漏流量分数** — 流量比 `1e-6` (默认) | positive scalar

孔口关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01` (默认) | positive scalar in the range of [0,1]

连续平滑因子，根据阀处于接近打开和接近关闭位置时的流量响应引入一层逐渐变化。为了在这些状态下提高仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **层流压力比** — 层流-湍流转换压力比 `0.999` (默认) | positive scalar

孔口出口压力与孔口入口压力之比，此时流体在层流和湍流状态之间转换。在层流中，压力损失与质量流量成线性关系，在湍流中成二次关系。

### **端口 A、P 和 T 处的横截面积** — 守恒端口处的面积 `0.01 m^2` (默认) | positive scalar

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用这些面积。

### P-A 孔口

### **最大 P-A 孔口面积处的阀芯位置** — 完全打开 P-A 孔口的阀芯偏移 `5e-3 m` (默认) | positive scalar

完全打开 P-A 孔口时，阀芯从中性位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 孔口设置未同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **关闭和打开孔口之间的 P-A 阀芯行程** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 恒定孔口 Cv 流量系数** — 流量系数 `4` (默认) | positive scalar

P-A 孔口的恒定 *Cv* 流量系数的值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Cv flow coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 孔口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 孔口最大 Cv 流量系数** — 对应于最大开启组件的 *Cv* 系数 `4` (默认) | positive scalar

当 P-A 孔口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Cv flow coefficient`
3. **开度特性**为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔 Cv 流量系数向量** — 构件位置向量中值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应于 **P-A 节流孔阀芯行程向量** 参数中的一个值。此参数衡量当由压差驱动时，蒸气穿过阻力元件的难易程度。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Cv flow coefficient`
3. **开度特性**为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

P-A 节流孔的恒定 *Kv* 流量系数值。此参数衡量当由压差驱动时，蒸气穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Kv flow coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流孔设置同时出现在两个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流孔最大 Kv 流量系数** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

当 P-A 节流孔完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量当由压差驱动时，蒸气穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Kv flow coefficient`
3. **开度特性**为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔 Kv 流量系数向量** — 构件位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应于 **P-A 节流孔阀芯行程向量** 参数中的一个值。此参数衡量当由压差驱动时，蒸气穿过阻力元件的难易程度。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Kv flow coefficient`
3. **开度特性**为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开度特性** 设置为 `Tabulated`，并设置以下参数之一：

- **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 最大节流孔面积** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作期间 P-A 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Orifice area`
3. **开度特性**为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **P-A 节流孔阀芯行程向量** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Orifice area`
3. **开度特性**为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 恒定节流孔面积** — 恒定节流孔的横截面积 `1e-4 m^2`（默认）| 正标量

当正、负阀芯位置包含同一个节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Orifice area`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流孔设置同时出现在两个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流孔阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 恒定节流孔声速流导** — 恒定节流孔的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当正、负阀芯位置包含同一个节流孔时的声速流导。该值是阻塞开始时通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度之积的比值。此参数确定在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流孔设置同时出现在两个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 恒定节流孔临界压力比** — 恒定节流孔中流量首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

当正、负阀芯位置包含同一个节流孔时的临界压力比。该值是流量首次开始阻塞且流速达到其最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流孔设置同时出现在两个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流孔最大声速流导** — 最大开度节流孔对应的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当 P-A 节流孔完全打开且可用于流动的面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. **开度特性**为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔临界压力比** — 流量首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到其最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. **开度特性**为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔声速流导向量** — 滑阀行程向量中值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声速流导向量。每个流导对应于 **P-A 节流孔阀芯行程向量** 参数中的一个值。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. **开度特性**为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔临界压力比向量** — 滑阀行程向量中值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，其中每个临界压力比对应于 **P-A 节流孔阀芯行程向量** 参数中的一个值。临界压力比是流速达到局部声速时的下游压力与上游压力之比。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for each flow path`
2. **阀门参数化**为 `Sonic conductance`
3. **开度特性**为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **阀门参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **阀门参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### **P-A 节流孔 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **阀门参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-A` 或 `P-A, A-T, P-T`。

### A-T 节流孔

### **最大 A-T 节流孔面积时的阀芯位置** — 完全打开 A-T 节流孔时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 A-T 节流孔时阀芯从中位开始的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **A-T 关闭与打开节流口之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 恒定节流口 Cv 流量系数** — 流量系数 `4`（默认） | positive scalar

A-T 节流口的恒定 *Cv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Cv flow coefficient`
3. 在每个参数中采用以下设置之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 节流口最大 Cv 流量系数** — 对应组件最大开度的 *Cv* 系数 `4`（默认） | positive scalar

当 A-T 节流口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Cv flow coefficient`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口 Cv 流量系数向量** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应 **A-T 节流口阀芯行程向量** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Cv flow coefficient`
3. **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 恒定节流口 Kv 流量系数** — 流量系数 `3.6`（默认） | positive scalar

A-T 节流口的恒定 *Kv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Kv flow coefficient`
3. 在每个参数中采用以下设置之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 节流口最大 Kv 流量系数** — 对应组件最大开度的 *Kv* 系数 `3.6`（默认） | positive scalar

当 A-T 节流口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Kv flow coefficient`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口 Kv 流量系数向量** — 成员位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应 **A-T 节流口阀芯行程向量** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Kv flow coefficient`
3. **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Tabulated`，并设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 最大节流口面积** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间 A-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Orifice area`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的开启面积向量。向量元素必须与 **A-T 节流口阀芯行程向量** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Orifice area`
3. **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Orifice area`
3. 在每个参数中采用以下设置之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 节流口阻塞流时的 xT 压差比因子** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 和出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时 A-T 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 恒定节流口声速导** — 恒定节流口的声速导 `12` `l/(bar*s)`（默认） | positive scalar

当正和负阀芯位置包含相同节流口时的声速导。此值是在阻塞开始时测量的，通过阻力元件的质量流量与上游压力及 ISO 8778 定义的标准条件下质量密度的乘积之比。此参数确定在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 恒定节流口临界压力比** — 恒定节流口流动首次阻塞时的下游与上游压力之比 `0.3`（默认） | positive scalar

当正和负阀芯位置包含相同节流口时的临界压力比。此值是流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 节流口最大声速导** — 对应节流口最大开度的声速导 `12` `l/(bar*s)`（默认） | positive scalar

当 A-T 节流口完全打开且可用于流动的面积最大时的声速导值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Sonic conductance`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口临界压力比** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认） | positive scalar

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Sonic conductance`
3. **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口声速导向量** — 阀芯行程向量中各值对应的声速导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1-by-*n* vector

阻力元件内部的声速导向量。每个声速导对应 **A-T 节流口阀芯行程向量** 参数中的一个值。向量的大小必须与 **A-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为 `Different for each flow path`
2. **阀参数化** 设置为 `Sonic conductance`
3. **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。
   - **负阀芯位置开启连接** 设置为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T 节流口临界压力比向量** — 阀芯行程向量中各值对应的临界压力比 `0.3 * ones(1, 6)`（默认） | 1-by-*n* vector

流动首次阻塞时的临界压力比向量，其中每个临界压力比对应 **A-T 节流口阀芯行程向量** 参数中的一个值。临界压力比是下游压力与上游压力之比，在该比值下流速达到当地声速。向量的大小必须与 **A-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice subsonic index** — 用于表征亚声速流态质量流量的指数 `0.5` (默认) | positive scalar

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K` (默认) | scalar

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3` (默认) | positive scalar

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### P-T 节流孔

### **Spool position at maximum P-T orifice area** — 完全打开的 P-T 节流孔的阀芯偏移量 `5e-3 m` (默认) | positive scalar

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯行程的最大距离。此值提供计算的上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Linear`，并设置以下参数之一：

- **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T constant orifice Cv flow coefficient** — 流量系数 `4` (默认) | positive scalar

P-T 节流孔的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Cv flow coefficient`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数 **Positive spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **P-T orifice maximum Cv flow coefficient** — 对应于最大打开组件的 *Cv* 系数 `4` (默认) | positive scalar

当 P-T 节流孔完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice Cv flow coefficient vector** — 用于成员位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (默认) | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T constant orifice Kv flow coefficient** — 流量系数 `3.6` (默认) | positive scalar

P-T 节流孔的恒定 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `Different for each flow path`
3. **Valve parameterization** 为 `Kv flow coefficient`
4. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数 **Positive spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **P-T orifice maximum Kv flow coefficient** — 对应于最大打开组件的 *Kv* 系数 `3.6` (默认) | positive scalar

当 P-T 节流孔完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice Kv flow coefficient vector** — 用于成员位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (默认) | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `Different for each flow path`
3. **Valve parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块使用表格数据点之间的线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

- **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
- **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2` (默认) | positive scalar

阀运行期间 P-T 节流孔的最大打开面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **P-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2` (默认) | positive scalar

当正阀芯位置和负阀芯位置包含同一节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Orifice area`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数 **Positive spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **P-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7` (默认) | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-T 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T constant orifice sonic conductance** — 恒定节流孔的声导 `12` `l/(bar*s)` (默认) | positive scalar

当正阀芯位置和负阀芯位置包含同一节流孔时的声导。此值是在阻塞开始时测得的通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度之积的比值。此参数确定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数 **Positive spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **P-T constant orifice critical pressure ratio** — 恒定节流孔下流动首次阻塞时的下游压力与上游压力之比 `0.3` (默认) | positive scalar

当正阀芯位置和负阀芯位置包含同一节流孔时的临界压力比。此值是流动首次开始阻塞且流速达到其最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Valve parameterization** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open connections** 为 `P-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数 **Positive spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **P-T orifice maximum sonic conductance** — 对应于最大打开节流孔的声导 `12` `l/(bar*s)` (默认) | positive scalar

当 P-T 节流孔完全打开且可用于流动的面积最大时的声导值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Valve parameterization** 设置为 `Sonic conductance`
3. 将 **Opening characteristic** 设置为 `Linear`
4. 设置以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
   - 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice critical pressure ratio** — 流量首次发生阻塞时的下游与上游压力之比 `0.3`（默认） | 正标量

流量首次开始阻塞且流速达到其最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Valve parameterization** 设置为 `Sonic conductance`
3. 将 **Opening characteristic** 设置为 `Linear`
4. 设置以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
   - 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice sonic conductance vector** — 与滑阀行程向量中的值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1×*n* 向量

阻力元件内部的声导向量。每个声导对应于 **P-T orifice spool travel vector** 参数中的一个值。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Valve parameterization** 设置为 `Sonic conductance`
3. 将 **Opening characteristic** 设置为 `Tabulated`
4. 设置以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
   - 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice critical pressure ratio vector** — 与滑阀行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认） | 1×*n* 向量

临界压力比向量，流量在这些临界压力比下首次发生阻塞；每个临界压力比对应于 **P-T orifice spool travel vector** 参数中的一个值。临界压力比是流速达到当地声速时下游压力与上游压力的比值。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Valve parameterization** 设置为 `Sonic conductance`
3. 将 **Opening characteristic** 设置为 `Tabulated`
4. 设置以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
   - 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
- 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
- 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

### **P-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Valve parameterization** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。
- 将 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的三通方向阀

3-Way Directional Valve (MA) 模块对湿空气网络中的具有三个开口的阀进行建模，通常位于执行器、泵与油箱之间。阀的操作由单个滑阀控制，该滑阀根据端口 **S** 处的信号发生位移。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定当滑阀沿正方向和负方向移动时打开的节流孔，来设置阀的基线配置。有关该模块如何计算通过可变节流孔的流量的更多详细信息，请参阅 Orifice (MA)。

示例阀配置示意图

在此配置中，**Positive spool position open connections** 设置为 `A-T`。当端口 **S** 处的信号将滑阀移动到正位置时，端口 **A** 与 **T** 之间的路径打开以允许流动。端口 **P** 与 **A** 之间以及端口 **P** 与 **T** 之间的路径关闭：

显示端口 A 与 T 之间流动且端口 P 关闭的示意图

在此配置中，**Negative spool position open connections** 设置为 `P-A`。当端口 **S** 处的信号将滑阀移动到负位置时，端口 **P** 与 **A** 之间的路径打开以允许流动，并且端口 **T** 与 **A** 之间以及端口 **P** 与 **T** 之间的路径关闭：

显示端口 A 与 T 之间流动且端口 P 关闭的示意图

您可以通过将 **Positive spool position open connections** 或 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T` 来打开端口 **P** 与 **T** 之间的路径。

一条流动路径可以在正滑阀位置或负滑阀位置打开，但不能同时在两者中打开。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在某一压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v（其中 Kv=0.865Cv）决定模块参数化。流量系数衡量湿空气在某一压差驱动下流动的容易程度。
- `Sonic conductance` — 稳态下阻力元件的声导决定模块参数化。声导衡量湿空气在*阻塞*时流动的容易程度；阻塞是一种流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，会发生阻塞。
- `Orifice area` — 流量限制的尺寸决定模块参数化。

### 可视化节流孔开口

要可视化滑阀偏移和位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示声导、*Kv* 流量系数、*Cv* 流量系数或节流孔面积随滑阀位置的变化。

更改模块参数后要更新数据，请在图窗中点击 **Reload Data**。

此图显示具有默认值的阀配置。

每个节流孔的面积与滑阀位置的关系图。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于含有高水平痕量气体的湿空气，或对空气以外的流体进行建模，则可能需要按混合气体比重的平方根对声导进行缩放。
- 此模块不对超声速流动进行建模。
- 阀与环境之间没有热交换。
