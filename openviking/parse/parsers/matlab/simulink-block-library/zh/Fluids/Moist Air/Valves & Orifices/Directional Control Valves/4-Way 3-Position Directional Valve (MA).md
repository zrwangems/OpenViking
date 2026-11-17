---
type: simulink-block
title: '4-Way 3-Position Directional Valve (MA)'
family: 'moist-air'
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

### 守恒

### **A** — 湿空气入口或出口端口

与阀门的入口或出口端口关联的湿空气守恒端口。

### **B** — 湿空气入口或出口端口

与阀门的入口或出口端口关联的湿空气守恒端口。

### **P** — 湿空气入口或出口端口

与阀门的入口或出口端口关联的湿空气守恒端口。

### **T** — 湿空气入口或出口端口

与阀门的入口或出口端口关联的湿空气守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。

## 参数

### 阀门配置

### **Positive spool position open connections** — 当阀芯处于正位置时打开的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯处于正位置时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯移动方向。要检查参数设置与其他节流孔的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Neutral spool position open connections** — 当阀芯处于中位时打开的流路 `All closed`（默认） | `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

当阀芯处于中位时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯移动方向。要检查参数设置与其他节流孔的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Negative spool position open connections** — 当阀芯沿负方向移动时打开的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯沿负方向移动时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯移动方向。要检查参数设置与其他节流孔的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Consistency check for neutral spool position open connections** — 是否检查节流孔设置是否一致 `Warning`（默认） | `Error` | `None`

是否检查 **阀门配置** 部分中的中位阀芯位置打开设置是否与最大节流孔面积处指定的阀芯位置一致。对于每个启用的节流孔，阀芯中位处的实际偏移应与每个单独节流孔指定的阀芯偏移相称。

### 模型参数化

### **Area characteristics** — 节流孔的流量方程 `Identical for all flow paths`（默认） | `Different for each flow path`

是否对阀门节流孔面积应用统一或独立的流量方程。将此参数设置为 `Identical for all flow paths` 时，模块对所有阀门节流孔使用相同的节流孔和阀芯几何、流量、压力以及面积向量。将此参数设置为 `Different for each flow path` 时，可以为每个节流孔单独指定这些参数。对于这两种设置，当将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 可变或恒定节流孔参数化 `Cv flow coefficient`（默认） | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据节流孔两端压差计算质量流量，或根据质量流量计算压差的方法。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | 正标量

阀芯行程的最大距离。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Linear`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认） | `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

### **Spool travel vector** — 相对于完全关闭位置的阀芯打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* 向量

根据表格化阀门面积数据对节流孔进行参数化时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大打开组件的 *Cv* 系数 `4`（默认） | 正标量

当节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 用于 member position vector 中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* 向量

*Cv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。该向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大打开组件的 *Kv* 系数 `3.6`（默认） | 正标量

当节流孔完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 用于 member position vector 中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* 向量

*Kv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。该向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | 正标量

阀门运行期间每个节流孔的最大打开面积。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* 向量

根据表格化阀门面积数据对节流孔进行参数化时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出这些值。元素必须大于 0。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该值处首次发生阻塞流。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | 正标量

用于考虑理论流动中流出损失的修正系数。

#### 依赖项

要启用此参数，请将 **Orifice parameterization** 设置为 `Orifice area`。

### **Maximum sonic conductance** — 对应最大打开组件的声速导纳 `12 l/(bar*s)`（默认） | 正标量

当端口 **S** 指定的控制信号为 `1` 且可用于流动的横截面积最大时，声速导纳的值。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态质量流量的指数 `0.5`（默认） | 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认） | 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 对应 spool travel vector 中值的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认） | 正值向量

阻力元件内部的声速导纳向量。每个导纳对应 **Spool travel vector** 参数中的一个值。该向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 对应 spool travel vector 中值的临界压力比 `0.3 * ones(1,6)`（默认） | 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应 **Spool travel vector** 参数中的一个值。临界压力比是流动速度达到当地声速时的下游压力与上游压力之比。该向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认） | 正标量

节流孔关闭时的流量与打开时的流量之比。

#### 依赖项

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，根据阀门处于接近打开和接近关闭位置时的流量响应引入一层渐变变化。为提高在这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖项

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流转换压力比 `0.999`（默认） | 正标量

流体在层流和湍流流态之间转换时的节流孔出口压力与节流孔入口压力之比。压力损失在层流中与质量流量成线性关系，在湍流中与质量流量成二次关系。

### **Cross-sectional area at ports P, T, A, and B** — 守恒端口处的面积 `0.01 m^2`（默认） | 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀门的质量流量的压力-流量方程中使用该面积。

### P-A 节流孔

### **Spool position at maximum P-A orifice area** — 完全打开 P-A 节流孔的阀芯偏移 `5e-3 m`（默认） | 正标量

完全打开的 P-A 节流孔相对于中位的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一。

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流孔设置未出现在全部三个阀芯位置参数中时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-A 节流口在关闭和打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

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

### **P-A 恒定节流口 Cv 流量系数** — 流量系数 `4`（默认） | positive scalar

P-A 节流口的恒定 *Cv* 流量系数值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Cv flow coefficient`
3. 在每个参数中使用以下设置之一：

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

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流口最大 Cv 流量系数** — 对应于最大程度开启组件的 *Cv* 系数 `4`（默认） | positive scalar

P-A 节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Cv flow coefficient`
3. **开启特性** 为 `Linear`
4. 设置以下参数之一：

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

### **P-A 节流口 Cv 流量系数向量** — 对应成员位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **P-A 节流口阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。向量的大小必须与 **P-A 节流口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Cv flow coefficient`
3. **开启特性** 为 `Tabulated`
4. 设置以下参数之一：

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

### **P-A 恒定节流口 Kv 流量系数** — 流量系数 `3.6`（默认） | positive scalar

P-A 节流口的恒定 *Kv* 流量系数值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Kv flow coefficient`
3. 在每个参数中使用以下设置之一：

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

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流口最大 Kv 流量系数** — 对应于最大程度开启组件的 *Kv* 系数 `3.6`（默认） | positive scalar

P-A 节流口完全打开且可用流动面积最大时的 *Kv* 流量系数值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Kv flow coefficient`
3. **开启特性** 为 `Linear`
4. 设置以下参数之一：

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

### **P-A 节流口 Kv 流量系数向量** — 对应成员位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **P-A 节流口阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下蒸气通过阻性元件的难易程度。向量的大小必须与 **P-A 节流口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Kv flow coefficient`
3. **开启特性** 为 `Tabulated`
4. 设置以下参数之一：

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

### **P-A 节流口阀芯行程向量** — 相对于全闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Tabulated`，并设置以下参数之一：

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

### **P-A 最大节流口面积** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀操作期间 P-A 节流口的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Orifice area`
3. **开启特性** 为 `Linear`
4. 设置以下参数之一：

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

### **P-A 节流口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的开启面积向量。向量元素必须与 **P-A 节流口阀芯行程向量** 参数中的元素一一对应。这些元素必须大于 0 并按升序列出。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Orifice area`
3. **开启特性** 为 `Tabulated`
4. 设置以下参数之一：

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

### **P-A 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Orifice area`
3. 在每个参数中使用以下设置之一：

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

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流口在阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 节流口首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 设置以下参数中的至少一个：

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

### **P-A 恒定节流口声速流导** — 恒定节流口的声速流导 `12` `l/(bar*s)`（默认） | positive scalar

当正和负阀芯位置包含相同节流口时的声速流导。该值是在开始发生阻塞时测得的，通过阻性元件的质量流量与上游压力和 ISO 8778 所定义标准条件下质量密度的乘积之比。该参数确定在给定上游压力下允许的最大流量。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流口参数化** 为 `Sonic conductance`
3. 在每个参数中使用以下设置之一：

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

**注意：**

仅当 P-A 节流口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 恒定节流孔临界压力比** — 恒定节流孔中流量首次发生阻塞时下游压力与上游压力之比 `0.3`（默认） | positive scalar

当正阀芯位置和负阀芯位置包含同一节流孔时的临界压力比。此值是流量首次开始阻塞且流速达到由局部声速给出的最大值时的压力比。压力比为出口压力除以进口压力。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow
   path`
2. 将 **节流孔参数化** 设置为
   `Sonic conductance`
3. 设置每个参数中的以下之一：

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

**注意：**

仅当 P-A 节流孔设置出现在全部三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流孔最大声速导纳** — 节流孔最大开启时对应的声速导纳 `12` `l/(bar*s)`（默认） | positive scalar

P-A 节流孔完全打开且可用于流动的面积最大时的声速导纳值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

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

### **P-A 节流孔临界压力比** — 流量首次发生阻塞时的下游压力与上游压力之比 `0.3`（默认） | positive scalar

流量首次开始阻塞且流速达到由局部声速给出的最大值时的压力比。压力比为出口压力除以进口压力。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

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

### **P-A 节流孔声速导纳向量** — 与阀芯行程向量中各值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1-by-*n* vector

阻力元件内部的声速导纳向量。每个声速导纳对应 **P-A 节流孔阀芯行程向量** 参数中的一个值。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

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

### **P-A 节流孔临界压力比向量** — 与阀芯行程向量中各值对应的临界压力比 `0.3 * ones(1, 6)`（默认） | 1-by-*n* vector

流量首次发生阻塞时的临界压力比向量，其中每个临界压力比对应 **P-A 节流孔阀芯行程向量** 参数中的一个值。临界压力比是流速达到局部声速时的下游压力与上游压力之比。向量的大小必须与 **P-A 节流孔阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

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

### **P-A 节流孔亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | positive scalar

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

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

### **P-A 节流孔 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认） | scalar

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

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

### **P-A 节流孔 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | positive scalar

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

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

### P-B 节流孔

### **最大 P-B 节流孔面积处的阀芯位置** — P-B 节流孔完全打开时的阀芯偏移 `5e-3 m`（默认） | positive scalar

P-B 节流孔完全打开时，阀芯从中位位置起的偏移。

#### 依赖项

要启用此参数，请设置以下参数之一：

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

仅当 P-B 节流孔设置未出现在全部三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-B 节流孔关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。此值提供计算上限，以便仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

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

### **P-B 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认） | positive scalar

P-B 节流孔的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下蒸气通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 设置每个参数中的以下之一：

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

仅当 P-B 节流孔设置出现在全部三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-B 节流孔最大 Cv 流量系数** — 最大开启组件对应的 *Cv* 系数 `4`（默认） | positive scalar

P-B 节流孔完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸气通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

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

### **P-B 节流孔 Cv 流量系数向量** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应 **P-B 节流孔阀芯行程向量** 参数中的一个值。此参数衡量在压差驱动下蒸气通过阻力元件的难易程度。向量的大小必须与 **P-B 节流孔阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

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

### **P-B 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认） | positive scalar

P-B 节流孔的恒定 *Kv* 流量系数值。此参数衡量在压差驱动下蒸气通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 在每个参数中采用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 孔口设置在全部三个阀芯位置参数中都出现时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Kv flow coefficient** — 对应于最大开度组件的 *Kv* 系数 `3.6`（默认） | positive scalar

当 P-B 孔口完全打开且可用于流动的面积最大时，*Kv* flow coefficient 的值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Kv flow coefficient`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice Kv flow coefficient vector** — 成员位置向量中的值所对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* flow coefficient 的向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积的表格参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间 P-B 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积的表格参数化的开启面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 且按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. 在每个参数中采用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 孔口设置在全部三个阀芯位置参数中都出现时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-B 孔口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice sonic conductance** — 恒定孔口的声速流导 `12` `l/(bar*s)`（默认） | positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的声速流导。此值是在阻塞开始时测得的，通过阻力元件的质量流量与上游压力和标准条件下质量密度（如 ISO 8778 所定义）的乘积之比。此参数确定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 孔口设置在全部三个阀芯位置参数中都出现时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice critical pressure ratio** — 恒定孔口的流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认） | positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的临界压力比。此值是流动首次开始阻塞且流速达到最大值（由局部声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 孔口设置在全部三个阀芯位置参数中都出现时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum sonic conductance** — 对应于最大开度孔口的声速流导 `12` `l/(bar*s)`（默认） | positive scalar

当 P-B 孔口完全打开且可用于流动的面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice critical pressure ratio** — 流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认） | positive scalar

流动首次开始阻塞且流速达到最大值（由局部声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice sonic conductance vector** — 阀芯行程向量中的值所对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1-by-*n* vector

阻力元件内部的声速流导向量。每个流导对应于 **P-B orifice spool travel vector** 参数中的一个值。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice critical pressure ratio vector** — 与滑阀行程向量 `0.3 * ones(1, 6)`（默认）中的值对应的临界压力比 | 1-by-*n* vector

临界压力比向量，在这些临界压力比下流量首次阻塞，其中每个临界压力比对应于 **P-B orifice spool travel vector** 参数中的一个值。临界压力比是流速达到当地声速时下游压力与上游压力之比。该向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认） | positive scalar

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认） | scalar

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### **P-B orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | positive scalar

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

### A-B Orifice

### **Spool position at maximum A-B orifice area** — 完全打开 A-B 节流口的滑阀偏移 `5e-3 m`（默认） | positive scalar

完全打开的 A-B 节流口相对于中立位置的滑阀偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 为：

- `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流口设置未出现在全部三个滑阀位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **A-B spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | positive scalar

滑阀行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Linear`，并设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 为：

- `P-A, P-B, A-B`

### **A-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认） | positive scalar

A-B 节流口的恒定 *Cv* 流量系数值。该参数度量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流口设置出现在全部三个滑阀位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **A-B orifice maximum Cv flow coefficient** — 对应于最大开启组件的 *Cv* 系数 `4`（默认） | positive scalar

当 A-B 节流口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。该参数度量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice Cv flow coefficient vector** — 成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）中值的 *Cv* 系数 | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。该参数度量在压差驱动下气体通过阻力元件的难易程度。该向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Cv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认） | positive scalar

A-B 节流口的恒定 *Kv* 流量系数值。该参数度量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流口设置出现在全部三个滑阀位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **A-B orifice maximum Kv flow coefficient** — 对应于最大开启组件的 *Kv* 系数 `3.6`（默认） | positive scalar

当 A-B 节流口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。该参数度量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中值的 *Kv* 系数 | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。该参数度量在压差驱动下气体通过阻力元件的难易程度。该向量的大小必须与 **A-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Kv flow coefficient`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice spool travel vector** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格化参数化的滑阀行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open connections** 为：

- `P-A, P-B, A-B`

### **A-B maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间 A-B 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格化参数化的开启面积向量。向量元素必须与 **A-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正滑阀位置和负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Orifice area`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流口设置出现在全部三个滑阀位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，才启用此参数。

### **A-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在此处 A-B 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`
2. **Orifice parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B 恒定孔口声导** — 恒定孔口的声导 `12` `l/(bar*s)` (默认) | positive scalar

当正和负阀芯位置包含相同孔口时的声导。该值是在阻塞开始时测量的，通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度的乘积之比。此参数决定在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中性阀芯位置打开连接**和**负阀芯位置打开连接**。

### **A-B 恒定孔口临界压力比** — 恒定孔口在流动首次阻塞时的下游与上游压力之比 `0.3` (默认) | positive scalar

当正和负阀芯位置包含相同孔口时的临界压力比。该值是流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中性阀芯位置打开连接**和**负阀芯位置打开连接**。

### **A-B 孔口最大声导** — 对应于最大打开孔口的声导 `12` `l/(bar*s)` (默认) | positive scalar

当 A-B 孔口完全打开且可用于流动的面积最大时的声导值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

### **A-B 孔口临界压力比** — 流动首次阻塞时的下游与上游压力之比 `0.3` (默认) | positive scalar

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

### **A-B 孔口声导向量** — 对应于阀芯行程向量中各值的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)` (默认) | 1-by-*n* vector

阻力元件内部的声导向量。每个声导对应于 **A-B 孔口阀芯行程向量** 参数中的一个值。向量的大小必须与 **A-B 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

### **A-B 孔口临界压力比向量** — 对应于阀芯行程向量中各值的临界压力比 `0.3 * ones(1, 6)` (默认) | 1-by-*n* vector

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **A-B 孔口阀芯行程向量** 参数中的一个值。临界压力比是流动速度达到当地声速时的下游与上游压力之比。向量的大小必须与 **A-B 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **中性阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置打开连接**为：

   - `P-A, P-B, A-B`

### **A-B 孔口亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5` (默认) | positive scalar

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**中性阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**负阀芯位置打开连接**为：

- `P-A, P-B, A-B`

### **A-B 孔口 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K` (默认) | scalar

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**中性阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**负阀芯位置打开连接**为：

- `P-A, P-B, A-B`

### **A-B 孔口 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3` (默认) | positive scalar

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**中性阀芯位置打开连接**为：

- `P-A, P-B, A-B`

**负阀芯位置打开连接**为：

- `P-A, P-B, A-B`

### A-T Orifice

### **最大 A-T 孔口面积处的阀芯位置** — 完全打开 A-T 孔口时的阀芯偏移 `5e-3 m` (默认) | positive scalar

完全打开 A-T 孔口时，阀芯从中位的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **正阀芯位置打开连接**为 `P-B, A-T`。
- **中性阀芯位置打开连接**为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置打开连接**为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置未出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中性阀芯位置打开连接**和**负阀芯位置打开连接**。

### **A-T 孔口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开口特性** 设置为 `Linear`，并设置以下参数之一：

- **正阀芯位置打开连接**为 `P-B, A-T`。
- **中性阀芯位置打开连接**为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置打开连接**为 `P-B, A-T`。

### **A-T 恒定孔口 Cv 流量系数** — 流量系数 `4` (默认) | positive scalar

A-T 孔口的恒定 *Cv* 流量系数的值。此参数衡量在压差驱动下气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Cv flow coefficient`
3. 在每个参数中设置以下之一：

   - **正阀芯位置打开连接**为 `P-B, A-T`。
   - **中性阀芯位置打开连接**为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置打开连接**为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中性阀芯位置打开连接**和**负阀芯位置打开连接**。

### **A-T 孔口最大 Cv 流量系数** — 对应于最大打开组件的 *Cv* 系数 `4` (默认) | positive scalar

当 A-T 孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Cv flow coefficient`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置打开连接**为 `P-B, A-T`。
   - **中性阀芯位置打开连接**为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置打开连接**为 `P-B, A-T`。

### **A-T 孔口 Cv 流量系数向量** — 对应于构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (默认) | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。此参数衡量在压差驱动下气体穿过阻力元件的难易程度。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Cv flow coefficient`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置打开连接**为 `P-B, A-T`。
   - **中性阀芯位置打开连接**为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置打开连接**为 `P-B, A-T`。

### **A-T 恒定孔口 Kv 流量系数** — 流量系数 `3.6` (默认) | positive scalar

A-T 孔口的恒定 *Kv* 流量系数的值。此参数衡量在压差驱动下气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Kv flow coefficient`
3. 在每个参数中设置以下之一：

   - **正阀芯位置打开连接**为 `P-B, A-T`。
   - **中性阀芯位置打开连接**为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置打开连接**为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中性阀芯位置打开连接**和**负阀芯位置打开连接**。

### **A-T 孔口最大 Kv 流量系数** — 对应于最大打开组件的 *Kv* 系数 `3.6` (默认) | positive scalar

当 A-T 孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow path`
2. **孔口参数化**为
   `Kv flow coefficient`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置打开连接**为 `P-B, A-T`。
   - **中性阀芯位置打开连接**为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置打开连接**为 `P-B, A-T`。

### **A-T 孔口 Kv 流量系数向量** — 对应于成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中值的 *Kv* 系数（默认） | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Kv flow coefficient`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Tabulated`，并设置以下参数之一：

- 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
- 将 **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 最大孔口面积** — 最大孔口开启面积 `1e-4 m^2`（默认） | 正标量

阀运行期间 A-T 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Orifice area`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1×*n* 向量

用于阀面积表格参数化的开启面积向量。向量元素必须与 **A-T 孔口阀芯行程向量** 参数中的元素一一对应。这些元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Orifice area`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 恒定孔口面积** — 恒定孔口横截面积 `1e-4 m^2`（默认） | 正标量

当正和负阀芯位置包含相同孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Orifice area`
3. 在每个参数中采用以下设置之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 孔口阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 A-T 孔口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 恒定孔口声导** — 恒定孔口声导 `12` `l/(bar*s)`（默认） | 正标量

当正和负阀芯位置包含相同孔口时的声导。此值是在阻塞开始时测得的通过阻力元件的质量流率与上游压力和在 ISO 8778 定义的标准条件下的质量密度之积的比值。此参数确定给定上游压力下允许的最大流率。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 恒定孔口临界压力比** — 恒定孔口流动首次阻塞时的下游与上游压力比 `0.3`（默认） | 正标量

当正和负阀芯位置包含相同孔口时的临界压力比。此值是流动首次开始阻塞且流速达到其最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 在每个参数中采用以下设置之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 孔口最大声导** — 最大开启孔口对应的声导 `12` `l/(bar*s)`（默认） | 正标量

当 A-T 孔口完全打开且可用于流动的面积最大时的声导值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口临界压力比** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到其最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口声导向量** — 对应于阀芯行程向量中值的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1×*n* 向量

阻力元件内部的声导向量。每个声导对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口临界压力比向量** — 对应于阀芯行程向量中值的临界压力比 `0.3 * ones(1, 6)`（默认） | 1×*n* 向量

流动首次阻塞时的临界压力比向量，其中每个临界压力比对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。临界压力比是流速达到局部声速时的下游与上游压力之比。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开启特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
   - 将 **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口亚声速指数** — 用于表征亚声速流态中质量流率的指数 `0.5`（默认） | 正标量

用于更准确地计算亚声速流态中质量流率的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
- 将 **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认） | 标量

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用在不同参考值下获得的声导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
- 将 **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### **A-T 孔口 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用在不同参考值下获得的声导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置开启连接** 设置为 `P-B, A-T`。
- 将 **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置开启连接** 设置为 `P-B, A-T`。

### B-T Orifice

### **最大 B-T 孔口面积处的阀芯位置** — 完全打开 B-T 孔口时的阀芯偏移 `5e-3 m`（默认） | 正标量

从中位到完全打开 B-T 孔口的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一。

- **正阀芯位置开启连接** 设置为 `P-A, B-T`。
- **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置未出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 关闭和打开节流孔之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | 正标量

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `P-A, B-T`。
- **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认） | 正标量

B-T 节流孔的恒定 *Cv* 流量系数值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Cv flow coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 节流孔最大 Cv 流量系数** — 对应于组件最大开启的 *Cv* 系数 `4`（默认） | 正标量

当 B-T 节流孔完全打开且可用于流动的面积达到最大时，*Cv* 流量系数的值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Cv flow coefficient`
3. **开启特性** 为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 节流孔 Cv 流量系数向量** — 成员位置向量中值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应于 **B-T 节流孔阀芯行程向量** 参数中的一个值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。向量的大小必须与 **B-T 节流孔阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Cv flow coefficient`
3. **开启特性** 为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认） | 正标量

B-T 节流孔的恒定 *Kv* 流量系数值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Kv flow coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 节流孔最大 Kv 流量系数** — 对应于组件最大开启的 *Kv* 系数 `3.6`（默认） | 正标量

当 B-T 节流孔完全打开且可用于流动的面积达到最大时，*Kv* 流量系数的值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Kv flow coefficient`
3. **开启特性** 为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 节流孔 Kv 流量系数向量** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应于 **B-T 节流孔阀芯行程向量** 参数中的一个值。此参数衡量当由压差驱动时气体通过阻力元件的难易程度。向量的大小必须与 **B-T 节流孔阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Kv flow coefficient`
3. **开启特性** 为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Tabulated`，并设置以下参数之一：

- **正阀芯位置开启连接** 设置为 `P-A, B-T`。
- **中位阀芯位置开启连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 最大节流孔面积** — 最大节流孔开启面积 `1e-4 m^2`（默认） | 正标量

阀操作期间 B-T 节流孔的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Orifice area`
3. **开启特性** 为 `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 节流孔面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的开启面积向量。向量元素必须与 **B-T 节流孔阀芯行程向量** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Orifice area`
3. **开启特性** 为 `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 恒定节流孔面积** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | 正标量

当正和负阀芯位置包含相同的节流孔时的节流孔面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Orifice area`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 节流孔阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 和出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 B-T 节流孔首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

### **B-T 恒定节流孔声导** — 恒定节流孔的声导 `12` `l/(bar*s)`（默认） | 正标量

当正和负阀芯位置包含相同的节流孔时的声导。此值是在阻塞开始时测量的，通过阻力元件的质量流量与上游压力和标准条件下质量密度（如 ISO 8778 所定义）的乘积之比。此参数确定给定上游压力下允许的最大流量。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 恒定节流孔临界压力比** — 恒定节流孔流动首次阻塞时的下游与上游压力比 `0.3`（默认） | 正标量

当正和负阀芯位置包含相同的节流孔时的临界压力比。此值是流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 设置为 `P-A, B-T`。
   - **中位阀芯位置开启连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数（**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**）中时，才启用此参数。

### **B-T 孔口最大声导** — 对应于孔口最大打开时的声导 `12` `l/(bar*s)`（默认） | positive scalar

当 B-T 孔口完全打开且可用流通面积最大时的声导值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
   - 将 **中位阀芯位置打开连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口临界压力比** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认） | positive scalar

流动首次开始阻塞且流速达到最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
   - 将 **中位阀芯位置打开连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口声导向量** — 对应于阀芯行程向量中值的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1-by-*n* vector

阻性元件内的声导向量。每个声导对应于 **B-T 孔口阀芯行程向量** 参数中的一个值。向量的大小必须与 **B-T 孔口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
   - 将 **中位阀芯位置打开连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口临界压力比向量** — 对应于阀芯行程向量中值的临界压力比 `0.3 * ones(1, 6)`（默认） | 1-by-*n* vector

临界压力比向量，在这些压力比下流动首次阻塞，每个临界压力比对应于 **B-T 孔口阀芯行程向量** 参数中的一个值。临界压力比是下游压力与上游压力之比，在该比值下流速达到局部声速。向量的大小必须与 **B-T 孔口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
   - 将 **中位阀芯位置打开连接** 设置为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | positive scalar

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
- 将 **中位阀芯位置打开连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认） | scalar

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
- 将 **中位阀芯位置打开连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### **B-T 孔口 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | positive scalar

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **孔口参数化** 设置为 `Sonic conductance`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-A, B-T`。
- 将 **中位阀芯位置打开连接** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- 将 **负阀芯位置打开连接** 设置为 `P-A, B-T`。

### P-T 孔口

### **最大 P-T 孔口面积时的阀芯位置** — 完全打开 P-T 孔口时的阀芯偏移 `5e-3 m`（默认） | positive scalar

完全打开 P-T 孔口时相对于中位位置的阀芯偏移。

#### 依赖项

要启用此参数，请将 **中位阀芯位置打开连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口在关闭和打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开口特性** 设置为 `Linear`，并将 **中位阀芯位置打开连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口最大 Cv 流量系数** — 对应于组件最大打开时的 *Cv* 系数 `4`（默认） | positive scalar

当 P-T 孔口完全打开且可用流通面积最大时 *Cv* 流量系数的值。该参数衡量在压差驱动下蒸气通过阻性元件的容易程度。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Cv flow coefficient`
3. 将 **开口特性** 设置为 `Linear`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口 Cv 流量系数向量** — 对应于构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **P-T 孔口阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下蒸气通过阻性元件的容易程度。向量的大小必须与 **P-T 孔口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Cv flow coefficient`
3. 将 **开口特性** 设置为 `Tabulated`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口最大 Kv 流量系数** — 对应于组件最大打开时的 *Kv* 系数 `3.6`（默认） | positive scalar

当 P-T 孔口完全打开且可用流通面积最大时 *Kv* 流量系数的值。该参数衡量在压差驱动下蒸气通过阻性元件的容易程度。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Kv flow coefficient`
3. 将 **开口特性** 设置为 `Linear`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口 Kv 流量系数向量** — 对应于构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **P-T 孔口阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下蒸气通过阻性元件的容易程度。向量的大小必须与 **P-T 孔口阀芯行程向量** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Kv flow coefficient`
3. 将 **开口特性** 设置为 `Tabulated`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀门面积表格参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开口特性** 设置为 `Tabulated`，并将 **中位阀芯位置打开连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T 最大孔口面积** — 最大孔口开口面积 `1e-4 m^2`（默认） | positive scalar

阀门工作期间 P-T 孔口的最大打开面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Orifice area`
3. 将 **开口特性** 设置为 `Tabulated`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀门面积表格参数化的开口面积向量。向量元素必须与 **P-T 孔口阀芯行程向量** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Orifice area`
3. 将 **开口特性** 设置为 `Tabulated`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 和出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在此处 P-T 孔口首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口最大声导** — 对应于孔口最大打开时的声导 `12` `l/(bar*s)`（默认） | positive scalar

当 P-T 孔口完全打开且可用流通面积最大时的声导值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Linear`
4. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-T 孔口临界压力比** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认） | positive scalar

流动首次开始阻塞且流速达到最大值（由局部声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **孔口参数化** 设置为 `Sonic conductance`
3. 将 **开口特性** 设置为 `Linear`
4. 将 **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口声导向量** — 对应于阀芯行程向量中值的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认） | 1-by-*n* vector

阻性元件内的声导向量。每个声导对应于 **P-T 孔口阀芯行程向量** 参数中的一个值。向量的大小必须与 **P-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `Different for each flow
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice critical pressure ratio vector** — 与滑阀位移向量 `0.3 * ones(1, 6)` 中的值对应的临界压力比（默认）| 1-by-*n* vector

临界压力比向量，在此压力比下流动首次发生壅塞，
其中每个临界压力比对应于
**P-T orifice spool travel vector** 参数中的一个值。临界压力比是
下游压力与上游压力的比值，在该比值下流速达到当地声速。
该向量的大小必须与 **P-T orifice
spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `Different for each flow
   path`
2. **Orifice parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| positive scalar

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Orifice
parameterization** 设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**Neutral spool position open connections** 为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| scalar

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用在不同参考值下获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Orifice
parameterization** 设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**Neutral spool position open connections** 为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| positive scalar

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用在不同参考值下获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，将 **Orifice
parameterization** 设置为 `Sonic
conductance`，并设置以下参数中的至少一个：

**Neutral spool position open connections** 为：

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

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的 4 通 3 位方向阀

4-Way 3-Position Directional Valve (MA) 模块
为湿空气网络中的阀门建模，该阀门具有四个开口，通常位于执行器、
泵与储气罐之间。单个滑阀根据端口 **S** 处的信号控制阀门操作。您可以通过在 **Neutral spool position open connections**
参数中指定当滑阀处于中位（以 0 m 为中心）时打开的孔口，在 **Positive
spool position open connections** 参数中指定当滑阀沿正方向移动时打开的孔口，以及在 **Negative spool position open
connections** 参数中指定当滑阀沿负方向移动时打开的孔口，来设置阀门的基线配置。您可以使用 **Orifice
parameterization** 参数将阀门模型指定为用户提供数据的线性关系或函数。

此模块是一个复合组件，包含多个
Orifice
(MA) 模块实例。有关阀门参数化和模块计算的更多信息，请参阅 Orifice
(MA) 模块。

在此示例配置中，**Neutral spool position open
connections** 参数为 `All closed`。当
滑阀处于中位时，所有孔口均关闭，无流动：

在此配置中，**Negative spool position open connections**
为 `P-A, B-T`。当端口 **S**
处的信号将滑阀移动到负位置时，端口 **P**
与 **A** 之间以及端口 **B** 与
**T** 之间的路径打开，允许流动。端口
**P** 与 **B** 之间以及端口 **A**
与 **T** 之间的路径关闭，禁止流动：

在此配置中，**Positive spool position open connections**
为 `P-B, A-T`。当端口 **S**
处的信号将滑阀移动到正位置时，端口 **P**
与 **B** 之间以及端口 **A** 与
**T** 之间的路径打开，允许流动，并且端口
**P** 与 **A** 之间以及端口
**B** 与 **T** 之间的路径关闭：

此示意图显示了此配置：

左侧对应正位置，右侧
对应负位置。

### 阀芯位移和阀配置

*spool stroke* 是节流口从关闭位置完全打开所需的阀芯位移量。您可以使用 **Valve Configuration** 部分中的参数定义 spool stroke。下表显示模块如何根据阀节流口参数化和流路特性计算该行程。

由端口 **S** 指定的阀芯移动方向取决于 spool stroke 和节流口方向。

| 节流口打开时的阀芯位置 | 阀芯位移，*ΔS* |
| --- | --- |
| 始终关闭（未在任何阀芯位置配置中选择该节流口） | N/A |
| 始终打开（在正、中间和负阀芯位置配置中选择该节流口） | N/A |
| 负 | *S*orifice\_max + spool stroke – **S** |
| 负和中间 | *S*orifice\_max + spool stroke – **S** |
| 正 | *S*orifice\_max – spool stroke + **S** |
| 正和中间 | *S*orifice\_max – spool stroke + **S** |
| 中间 | |*S*orifice\_max| + spool stroke – |**S**| |
| 正和负 | –|*S*orifice\_max| + spool stroke – |**S**| |

*S*orifice\_max 是为每个节流口定义的最大节流口面积处的阀芯位置。当 *ΔS* 为负时，节流口面积饱和到泄漏面积；当节流口完全打开时，饱和到最大节流口面积。当节流口完全打开时，*ΔS* 等于 spool stroke，因此大于 spool stroke 的 *ΔS* 值不会进一步增大节流口面积。

**Consistency check for neutral spool position open connections** 参数验证：

- 当 **S** 处的信号为 0 时，**Neutral spool position open connections** 中列出的任何节流口均打开
- 当 **S** 处的信号为 0 时，**Neutral spool position open connections** 中未列出的任何节流口均关闭

您可以选择在任一阀芯位置违反此检查时接收警告或错误。

下表显示 4-Way 3-Position Directional Valve (MA) block 的可能配置。

| 配置 | 参数值 |
| --- | --- |
|  | 在中间位置，所有四个节流口均关闭。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 在中间位置，所有四个节流口均打开。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 重叠。  - **Positive spool position open   connections**:   `P-A` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**:   `P-B`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke |
|  | 节流口 A-T 和 B-T 打开。节流口 P-A 和 P-B 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 在中间位置，节流口 P-A 和 A-T 打开。节流口 P-B 和 B-T 重叠。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > P-B spool stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** < –B-T spool   stroke |
|  | 在中间位置，节流口 A-T 打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `A-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 在中间位置，节流口 B-T 打开。节流口 P-A、P-B 和 A-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 节流口 P-A 和 P-B 打开。节流口 A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 在中间位置，节流口 P-A 打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-A` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 在中间位置，节流口 P-B 打开。节流口 P-A、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 在中间位置，节流口 P-B 和 B-T 打开。节流口 P-A 和 A-T 重叠。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-B,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < –P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | 在中间位置，节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中间位置打开，并在阀芯位移时关闭。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke - **Spool position at maximum P-T   orifice area** = any value |
|  | 节流口 P-A 是恒定节流口。在中间位置，节流口 P-B、A-T 和 B-T 打开。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** = any value - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | 节流口 P-B 是恒定节流口。在中间位置，节流口 P-A、A-T、B-T 打开。    - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   P-B`    - **Spool position at maximum P-A   orifice area** > –P-A spool stroke - **Spool position at maximum A-T   orifice area** < A-T spool   stroke - **Spool position at maximum B-T   orifice area** = any value |
|  | 在中间位置，节流口 P-A 关闭。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke |
|  | 在中间位置，节流口 P-B 关闭。端口 **B** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke |
|  | 在中间位置，节流口 P-A 关闭。在中间位置，节流口 A-T 打开。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** = any value - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
|  | 在中间位置，节流口 P-B 关闭。在中间位置，节流口 B-T 打开。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
|  | 在中间位置，节流口 P-B 关闭。节流口 P-T 在中间位置打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |
|  | 在中间位置，节流口 P-A 关闭。节流口 P-T 在中间位置打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-A,   P-B`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |

### 阀节流口参数化

**Orifice parameterization** 参数指定一个或所有阀节流口的打开面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路应用相同数据。当选择 `Different for all flow paths` 时，模块对每条流路使用单独的参数化。

模块用于控制每个节流口的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量取决于端口 **S** 处的阀芯位置。当阀芯位移以打开节流口时，流量能力的度量从指定最小值缩放到指定最大值。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处阀芯位置的函数。此函数使用一维查找表。

**Orifice parameterization** 参数决定模块如何计算每个节流口中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 对每个节流口中的流量进行缩放。流量系数衡量流体在特定压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，对每个节流口中的流量进行缩放。流量系数衡量流体在特定压差驱动下流动的容易程度。
- `Orifice area` — 节流口面积的尺寸对每个节流口中的流量进行缩放。

### 可视化节流口开度

要可视化阀芯偏移和最大位移，请右键点击该模块，然后选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的节流口。该图显示声速流导、*Kv* 流量系数、*Cv* 流量系数或节流口面积随阀芯位置的变化。

当 **Valve Configuration** 参数中的正、中、负设置使用相同节流口时，该图将节流口开度显示为常量。

更改模块参数后要更新数据，请在图窗上点击 **Reload Data**。

此图显示了一个阀门配置示例。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`
- **Neutral spool position open connections** 为 `P-T`
- **Negative spool position open connections** 为 `P-B, A-T`

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`

所有其他阀芯位置均为默认值。

每个节流口的面积随阀芯位置变化的图。

可视化结果显示，P-A 节流口在阀芯位置为 `-2.53e-3` 到 `2.53e-3` m 之间打开。由于 P-A 节流口仅在阀芯沿正方向位移时打开，因此将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，您可以更改：

- 将 **Spool position at maximum P-A orifice area** 更改为大于 0.005 m 的值
- 将 **Consistency check for neutral spool position open connections** 更改为 `None`
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置

### 假设与限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模除空气以外的流体，则可能需要按混合气体比重的平方根来缩放声速流导。
- 此模块不对超声速流进行建模。
- 阀门与环境之间没有热交换。
