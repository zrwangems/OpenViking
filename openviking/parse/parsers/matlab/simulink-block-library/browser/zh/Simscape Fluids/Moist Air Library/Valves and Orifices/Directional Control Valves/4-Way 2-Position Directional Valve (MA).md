---
type: simulink-block
title: '4-Way 2-Position Directional Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Valves and Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalvema'
documentation_source_path: 'ref/4way2positiondirectionalvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (MA)

## 端口

### 守恒

### **A** — 入口或出口端口湿空气

与阀的入口或出口端口关联的湿空气守恒端口。

### **B** — 入口或出口端口湿空气

与阀的入口或出口端口关联的湿空气守恒端口。

### **P** — 入口或出口端口湿空气

与阀的入口或出口端口关联的湿空气守恒端口。

### **T** — 入口或出口端口湿空气

与阀的入口或出口端口关联的湿空气守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。

## 参数

### 阀配置

### **正阀芯位置打开连接** — 当阀芯处于正位置时打开的流路 `All closed`（默认）| `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### **负阀芯位置打开连接** — 当阀芯沿负方向移动时打开的流路 `All closed`（默认）| `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当阀芯沿负方向移动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### 模型参数化

### **面积特性** — 节流孔的流量方程 `Identical for all flow paths`（默认）| `Different for each flow path`

是对阀节流孔面积应用统一还是单独的流量方程。当将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流孔使用相同的节流孔和阀芯几何、流量、压力和面积向量。当将此参数设置为 `Different for each flow path` 时，可以为每个节流孔单独指定这些参数。对于这两种设置，当将 **节流孔参数化** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流出系数和雷诺数。

### **节流孔参数化** — 节流孔的可变或恒定参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据节流孔两端压差计算质量流量，或根据质量流量计算压差的方法。

### **节流孔关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **开启特性** 设置为 `Linear`。

### **开启特性** — 将控制信号转换为流量容量度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量容量度量的方法。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流孔进行参数化时的阀芯行程距离向量。向量元素必须与 **节流孔面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 对应于最大程度打开组件的 *Cv* 系数 `4`（默认）| 正标量

当节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 用于构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **控制构件位置向量** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应于最大程度打开组件的 *Kv* 系数 `3.6`（默认）| 正标量

当节流孔完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 用于构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **控制构件位置向量** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大节流孔面积** — 最大节流孔打开面积 `1e-4 m^2`（默认）| 正标量

阀运行期间每个节流孔的最大打开面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Linear`。

### **节流孔面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流孔进行参数化时的开启面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比，定义为 (pin−pout)/pin，其中首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **流出系数** — 流出系数 `0.64`（默认）| 正标量

用于考虑理论流动中流出损失的修正因子。

#### 依赖关系

要启用此参数，请将 **节流孔参数化** 设置为 `Orifice area`。

### **最大声速流导** — 对应于最大程度打开组件的声速流导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 指定的控制信号为 `1` 且可用于流动的横截面积最大时，声速流导的值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **临界压力比** — 流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到局部声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **亚声速指数** — 用于表征亚声速流动状态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流动状态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Sonic conductance`。

### **声速流导向量** — 与阀芯行程向量中各值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内的声速流导向量。每个流导对应于 **阀芯行程向量** 参数中的一个值。向量大小必须与 **阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **临界压力比向量** — 与阀芯行程向量中各值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，其中每个临界压力比对应于 **阀芯行程向量** 参数中的一个值。临界压力比是流速达到局部声速时的下游压力与上游压力之比。向量大小必须与 **阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，将 **节流孔参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，根据阀处于接近打开和接近关闭位置时的流量响应引入一层渐变。为提高仿真在这些状态下的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **层流压力比** — 层流-湍流转换压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间转换时的节流孔出口压力与节流孔入口压力之比。在层流中压力损失与质量流量成线性关系，在湍流中成二次关系。

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

### P-A 节流孔

### **最大 P-A 节流孔面积时的阀芯位置** — 完全打开 P-A 节流孔时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 P-A 节流孔时相对于中位位置的阀芯偏移。

#### 依赖关系

要启用此参数，请设置下列参数之一。

**正阀芯位置打开连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**负阀芯位置打开连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置未同时出现在 **正阀芯位置打开连接** 和 **负阀芯位置打开连接** 两个参数中时，才启用此参数。

### **P-A 节流孔关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开启特性** 设置为 `Linear`，并设置下列参数之一：

**正阀芯位置打开连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**负阀芯位置打开连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

### **P-A 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

P-A 节流孔的恒定 *Cv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`
2. **节流孔参数化** 为 `Cv flow coefficient`
3. 在每个参数中设置下列之一：

   **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **P-A 节流口最大 Cv 流量系数** — 对应最大打开组件 `4`（默认）的 *Cv* 系数 | 正标量

当 P-A 节流口完全打开且可用于流动的面积达到最大时，*Cv* 流量系数的值。此参数衡量当由压差驱动时，气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Cv flow
   coefficient`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口 Cv 流量系数向量** — 对应成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` 中各值的 *Cv* 系数（默认） | 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应于 **P-A 节流口滑阀行程向量** 参数中的一个值。此参数衡量当由压差驱动时，气体穿过阻力元件的难易程度。向量的大小必须与 **P-A 节流口滑阀行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Cv flow
   coefficient`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 恒定节流口 Kv 流量系数** — 流量系数 `3.6`（默认） | 正标量

P-A 节流口的恒定 *Kv* 流量系数的值。此参数衡量当由压差驱动时，气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Kv flow
   coefficient`
3. 每个参数中的以下设置之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在两个滑阀位置参数中时，此参数才会启用：**正滑阀位置打开连接** 和 **负滑阀位置打开连接**。

### **P-A 节流口最大 Kv 流量系数** — 对应最大打开组件 `3.6`（默认）的 *Kv* 系数 | 正标量

当 P-A 节流口完全打开且可用于流动的面积达到最大时，*Kv* 流量系数的值。此参数衡量当由压差驱动时，气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Kv flow
   coefficient`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口 Kv 流量系数向量** — 对应成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中各值的 *Kv* 系数（默认） | 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应于 **P-A 节流口滑阀行程向量** 参数中的一个值。此参数衡量当由压差驱动时，气体穿过阻力元件的难易程度。向量的大小必须与 **P-A 节流口滑阀行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Kv flow
   coefficient`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口滑阀行程向量** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格参数化的滑阀行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开口特性** 设置为 `Tabulated`，并设置以下参数之一：

**正滑阀位置打开连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**负滑阀位置打开连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

### **P-A 最大节流口面积** — 最大节流口开口面积 `1e-4 m^2`（默认） | 正标量

阀运行期间 P-A 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口面积向量** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1×*n* 向量

用于阀面积表格参数化的开口面积向量。向量元素必须与 **P-A 节流口滑阀行程向量** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Orifice area`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | 正标量

当正滑阀位置和负滑阀位置包含同一节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Orifice area`
3. 每个参数中的以下设置之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在两个滑阀位置参数中时，此参数才会启用：**正滑阀位置打开连接** 和 **负滑阀位置打开连接**。

### **P-A 节流口阻塞流时的 xT 压差比因子** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的压差比，定义为 (pin−pout)/pin，在该处 P-A 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中的至少一个：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 恒定节流口声速流导** — 恒定节流口的声速流导 `12` `l/(bar*s)`（默认） | 正标量

当正滑阀位置和负滑阀位置包含同一节流口时的声速流导。此值是在阻塞流开始时测得的质量流量与上游压力和标准条件下质量密度乘积之比，标准条件如 ISO 8778 所定义。此参数确定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在两个滑阀位置参数中时，此参数才会启用：**正滑阀位置打开连接** 和 **负滑阀位置打开连接**。

### **P-A 恒定节流口临界压力比** — 恒定节流口下流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认） | 正标量

当正滑阀位置和负滑阀位置包含同一节流口时的临界压力比。此值是流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在两个滑阀位置参数中时，此参数才会启用：**正滑阀位置打开连接** 和 **负滑阀位置打开连接**。

### **P-A 节流口最大声速流导** — 对应最大打开节流口的声速流导 `12` `l/(bar*s)`（默认） | 正标量

当 P-A 节流口完全打开且可用于流动的面积达到最大时，声速流导的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口临界压力比** — 流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Linear`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口声速流导向量** — 对应滑阀行程向量 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` 中各值的声速流导 `l/(bar*s)`（默认） | 1×*n* 向量

阻力元件内部的声速流导向量。每个流导对应于 **P-A 节流口滑阀行程向量** 参数中的一个值。向量的大小必须与 **P-A 节流口滑阀行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口临界压力比向量** — 对应滑阀行程向量 `0.3 * ones(1, 6)` 中各值的临界压力比（默认） | 1×*n* 向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **P-A 节流口滑阀行程向量** 参数中的一个值。临界压力比是流动速度达到当地声速时的下游压力与上游压力之比。向量的大小必须与 **P-A 节流口滑阀行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `Different for each flow
   path`
2. **节流口参数化**为
   `Sonic conductance`
3. **开口特性**为
   `Tabulated`
4. 以下参数之一：

   **正滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **负滑阀位置打开连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A 节流口亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流口参数化** 设置为 `Sonic conductance`，并设置以下参数之一：

**正滑阀位置打开连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**负滑阀位置打开连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

### **P-A orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认） | scalar

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并至少设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

### **P-A orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | positive scalar

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并至少设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — 完全打开的 P-B 节流孔对应的阀芯偏移 `5e-3 m`（默认） | positive scalar

完全打开的 P-B 节流孔相对于中位位置的阀芯偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。该值提供计算上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Linear`，并设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

### **P-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认） | positive scalar

P-B 节流孔的恒定 *Cv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Cv flow coefficient`
3. 在每个参数中使用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Cv flow coefficient** — 对应于最大打开组件的 *Cv* 系数 `4`（默认） | positive scalar

P-B 节流孔完全打开且可用于流动的面积最大时 *Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Cv flow coefficient`
3. 将 **Opening characteristic** 设置为 `Linear`
4. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice Cv flow coefficient vector** — 对应于 member position vector 中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Cv flow coefficient`
3. 将 **Opening characteristic** 设置为 `Tabulated`
4. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认） | positive scalar

P-B 节流孔的恒定 *Kv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Vapor operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 在每个参数中使用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Kv flow coefficient** — 对应于最大打开组件的 *Kv* 系数 `3.6`（默认） | positive scalar

P-B 节流孔完全打开且可用于流动的面积最大时 *Kv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Kv flow coefficient`
3. 将 **Opening characteristic** 设置为 `Linear`
4. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice Kv flow coefficient vector** — 对应于 member position vector 中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Vapor operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 将 **Opening characteristic** 设置为 `Tabulated`
5. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

### **P-B maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | positive scalar

阀门运行期间 P-B 节流孔的最大打开面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Orifice area`
3. 将 **Opening characteristic** 设置为 `Tabulated`
4. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Orifice area`
3. 将 **Opening characteristic** 设置为 `Tabulated`
4. 设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | positive scalar

当正和负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Orifice area`
3. 在每个参数中使用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 和出口压力 *pout* 之间的压力差比，定义为 (pin−pout)/pin，其中 P-B 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 至少设置以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B constant orifice sonic conductance** — 恒定节流孔的声速流导 `12` `l/(bar*s)`（默认） | positive scalar

当正和负阀芯位置包含相同节流孔时的声速流导。该值是在阻塞开始时测得的，通过阻力元件的质量流量与上游压力和 ISO 8778 中定义的标准条件下质量密度的乘积之比。此参数确定在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Sonic conductance`
3. 在每个参数中使用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice critical pressure ratio** — 恒定节流孔流动首次阻塞时的下游和上游压力比 `0.3`（默认） | positive scalar

当正和负阀芯位置包含相同节流孔时的临界压力比。该值是流动首次开始阻塞且流速达到最大值时的压力比，该最大值由当地声速给出。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`
2. 将 **Orifice parameterization** 设置为 `Sonic conductance`
3. 在每个参数中使用以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在两个阀芯位置参数中时，才启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum sonic conductance** — 对应于最大打开节流孔的声速流导 `12` `l/(bar*s)`（默认） | positive scalar

当 P-B 节流孔完全打开且可用于流动的面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Sonic conductance`
3. 将 **开度特性** 设置为
   `Linear`
4. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **负阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔临界压力比** — 流量首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Sonic conductance`
3. 将 **开度特性** 设置为
   `Linear`
4. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **负阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔声速流导向量** — 与阀芯行程向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内的声速流导向量。每个流导对应于 **P-B 节流孔阀芯行程向量** 参数中的一个值。向量大小必须与 **P-B 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Sonic conductance`
3. 将 **开度特性** 设置为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **负阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔临界压力比向量** — 与阀芯行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应于 **P-B 节流孔阀芯行程向量** 参数中的一个值。临界压力比是流量速度达到当地声速时的下游压力与上游压力之比。向量大小必须与 **P-B 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Sonic conductance`
3. 将 **开度特性** 设置为
   `Tabulated`
4. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **负阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔亚声速指数** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **负阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

### **P-B 节流孔 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **负阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

### **P-B 节流孔 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

**正阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **负阀芯位置打开连接** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

### A-T 节流孔

### **最大 A-T 节流孔面积处的阀芯位置** — A-T 节流孔完全打开时的阀芯偏移 `5e-3 m`（默认）| 正标量

A-T 节流孔完全打开时相对于中位位置的阀芯偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置未同时出现在 **正阀芯位置打开连接** 和 **负阀芯位置打开连接** 两个参数中时，才启用此参数。

### **关闭与打开节流孔之间的 A-T 阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开度特性** 设置为 `Linear`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

A-T 节流孔的恒定 *Cv* 流量系数值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Cv flow coefficient`
3. 在每个参数中进行以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在两个阀芯位置参数：**正阀芯位置打开连接** 和 **负阀芯位置打开连接** 中时，才启用此参数。

### **A-T 节流孔最大 Cv 流量系数** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

当 A-T 节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Cv flow coefficient`
3. 将 **开度特性** 设置为
   `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔 Cv 流量系数向量** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **A-T 节流孔阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。向量大小必须与 **A-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Cv flow coefficient`
3. 将 **开度特性** 设置为
   `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

A-T 节流孔的恒定 *Kv* 流量系数值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Kv flow coefficient`
3. 在每个参数中进行以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在两个阀芯位置参数：**正阀芯位置打开连接** 和 **负阀芯位置打开连接** 中时，才启用此参数。

### **A-T 节流孔最大 Kv 流量系数** — 对应于组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

当 A-T 节流孔完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Kv flow coefficient`
3. 将 **开度特性** 设置为
   `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔 Kv 流量系数向量** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **A-T 节流孔阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下流体穿过阻力元件的难易程度。向量大小必须与 **A-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Kv flow coefficient`
3. 将 **开度特性** 设置为
   `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开度特性** 设置为 `Tabulated`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 最大节流孔面积** — 最大节流孔开度面积 `1e-4 m^2`（默认）| 正标量

阀操作期间 A-T 节流孔的最大打开面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Orifice area`
3. 将 **开度特性** 设置为
   `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔面积向量** — 阀开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开度面积向量。向量元素必须与 **A-T 节流孔阀芯行程向量** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Orifice area`
3. 将 **开度特性** 设置为
   `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 恒定节流孔面积** — 恒定节流孔的横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含同一个节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow path`
2. 将 **节流孔参数化** 设置为
   `Orifice area`
3. 在每个参数中进行以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在两个阀芯位置参数：**正阀芯位置打开连接** 和 **负阀芯位置打开连接** 中时，才启用此参数。

### **A-T 节流孔 xT 阻塞流压差比因子** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比，定义为 (pin−pout)/pin，其中 A-T 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中的至少一个：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 恒定节流孔声速流导** — 恒定节流孔的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含同一节流孔时的声速流导。该值是当阻塞开始时测得的、通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度乘积之比。该参数决定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **A-T 恒定节流孔临界压力比** — 恒定节流孔流量首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

当正和负阀芯位置包含同一节流孔时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **A-T 节流孔最大声速流导** — 对应于最大开度节流孔的声速流导 `12` `l/(bar*s)`（默认）| 正标量

当 A-T 节流孔完全打开且可用流通面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开度特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔临界压力比** — 流量首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开度特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔声速流导向量** — 与阀芯行程向量中各值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声速流导向量。每个流导对应 **A-T 节流孔阀芯行程向量** 参数中的一个值。向量大小必须与 **A-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开度特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔临界压力比向量** — 与阀芯行程向量中各值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应 **A-T 节流孔阀芯行程向量** 参数中的一个值。临界压力比是流速达到当地声速时的下游压力与上游压力之比。向量大小必须与 **A-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Sonic conductance`
3. 将 **开度特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔亚声速指数** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流孔 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **节流孔参数化** 设置为 `Sonic conductance`，并设置以下参数中的至少一个：

- 将 **正阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### B-T 节流孔

### **最大 B-T 节流孔面积时的阀芯位置** — B-T 节流孔完全打开时的阀芯偏移 `5e-3 m`（默认）| 正标量

使 B-T 节流孔完全打开时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流孔设置未同时出现在 **正阀芯位置打开连接** 和 **负阀芯位置打开连接** 参数中时，此参数才启用。

### **B-T 阀芯在节流孔关闭与打开之间的行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值对计算设置上限，以使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，将 **开度特性** 设置为 `Linear`，并设置以下参数之一：

- 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

B-T 节流孔的恒定 *Cv* 流量系数值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 每个参数中的以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **B-T 节流孔最大 Cv 流量系数** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

当 B-T 节流孔完全打开且可用流通面积最大时的 *Cv* 流量系数值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 将 **开度特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T 节流孔 Cv 流量系数向量** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **B-T 节流孔阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。向量大小必须与 **B-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Cv flow coefficient`
3. 将 **开度特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

B-T 节流孔的恒定 *Kv* 流量系数值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Kv flow coefficient`
3. 每个参数中的以下设置之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **B-T 节流孔最大 Kv 流量系数** — 对应于组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

当 B-T 节流孔完全打开且可用流通面积最大时的 *Kv* 流量系数值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Kv flow coefficient`
3. 将 **开度特性** 设置为 `Linear`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T 节流孔 Kv 流量系数向量** — 成员位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **B-T 节流孔阀芯行程向量** 参数中的一个值。该参数衡量在压差驱动下气体通过阻力元件的难易程度。向量大小必须与 **B-T 节流孔阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`
2. 将 **节流孔参数化** 设置为 `Kv flow coefficient`
3. 将 **开度特性** 设置为 `Tabulated`
4. 以下参数之一：

   - 将 **正阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **负阀芯位置打开连接** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

- **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| positive scalar

阀门运行期间 B-T 节流口最大的开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| positive scalar

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Orifice area`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在两个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **B-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 和出口压力 *pout* 之间的比率，定义为 (pin−pout)/pin，此时 B-T 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
3. 以下参数中至少一个：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T constant orifice sonic conductance** — 恒定节流口声速流导 `12` `l/(bar*s)`（默认）| positive scalar

当正和负阀芯位置包含相同节流口时的声速流导。此值是在阻塞流开始时测得的，通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度的乘积之比。此参数确定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在两个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **B-T constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力之比 `0.3`（默认）| positive scalar

当正和负阀芯位置包含相同节流口时的临界压力比。此值是流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在两个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **B-T orifice maximum sonic conductance** — 最大开度节流口对应的声速流导 `12` `l/(bar*s)`（默认）| positive scalar

当 B-T 节流口完全打开且可用于流动的面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice critical pressure ratio** — 流量首次阻塞时的下游与上游压力之比 `0.3`（默认）| positive scalar

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Linear`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice sonic conductance vector** — 与阀芯行程向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1-by-*n* vector

阻力元件内部的声速流导向量。每个流导对应 **B-T orifice spool travel vector** 参数中的一个值。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice critical pressure ratio vector** — 与阀芯行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1-by-*n* vector

流量首次阻塞时的临界压力比向量，每个临界压力比对应 **B-T orifice spool travel vector** 参数中的一个值。临界压力比是下游与上游压力之比，在此比值下流速达到当地声速。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for each flow path`
2. **Orifice parameterization** 设置为 `Sonic conductance`
3. **Opening characteristic** 设置为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice subsonic index** — 用于表征亚声速流态质量流量的指数 `0.5`（默认）| positive scalar

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| scalar

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| positive scalar

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并设置以下参数中至少一个：

- **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的 4 通 2 位方向控制阀

4-Way 2-Position Directional Valve (MA) 对湿空气网络中具有四个开口的阀门（例如执行器、泵与储罐之间的阀）进行建模。单个阀芯根据端口 **S** 处的信号控制阀门操作。您可以通过在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中分别指定阀芯沿正方向和负方向移动时打开的节流口，来设置阀门的基线配置。您可以在 **Orifice parameterization** 参数中将阀门开口模型设置为线性关系或用户提供数据的函数，并可将其应用于阀门中的一个或所有流路。

此模块是一个复合组件，由多个 Orifice (MA) 模块实例组成。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice (MA) 模块。在某些配置中，此阀门类似于 3 通阀。要设置阀芯处于中位时的附加流路，请参阅 4-Way 3-Position Directional Valve (MA) 模块。

下图显示了一个示例阀门设置，其中阀门连接到储罐、执行器和泵，且 **Positive spool position open connections** 参数为 `P-B, A-T`：

下图显示了当 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀门：

在此配置中，当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的流路打开。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的流路关闭。

下图显示了当 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀门：

在此配置中，当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的流路打开，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的流路关闭。

表示此配置的原理图是：

左侧对应正位置，右侧对应负位置。阀门通过中间中性段中的位置进行转换。

### 阀芯位移和阀配置

*阀芯行程* 是阀口从关闭位置完全打开所需的阀芯移动量。您可以使用 **Orifice parameterization** 和 **Area characteristics** 参数来指定流路特性：

| 阀口参数化 | 对所有流路相同 | 对每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义阀芯行程 | **Spool travel between closed and open orifice** 参数为每个阀口定义阀芯行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数的第一个和最后一个元素之差定义阀芯行程 | 每个阀口的 **Spool travel vector** 参数的第一个和最后一个元素之差定义阀芯行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数的第一个和最后一个元素之差定义阀芯行程 | **Spool travel vector, ds** 参数的第一个和最后一个元素之差为每个阀口定义阀芯行程 |

阀芯移动方向取决于阀芯行程、阀口方向和端口 **S** 处的信号。下表显示了根据 **Positive spool position open connection** 和 **Negative spool position open connection** 参数的选择，阀口的阀芯行程：

| 当阀口打开时的阀芯位置 | 阀芯行程，*ΔS* |
| --- | --- |
| 阀口始终关闭：未为 **Positive spool position open connection** 或 **Negative spool position open connection** 参数选择该阀口 | N/A |
| 阀口始终打开：该阀口同时被 **Positive spool position open connection** 和 **Negative spool position open connection** 参数选中 | N/A |
| 负：该阀口仅被 **Negative spool position open connection** 参数选中 | *S*orifice\_max + 阀芯行程 – **S** |
| 正：该阀口仅被 **Positive spool position open connection** 参数选中 | *S*orifice\_max – 阀芯行程 + **S** |

其中 *S*orifice\_max 是为每个阀口定义的最大阀口面积处的阀芯位置。当 *ΔS* 为负时，阀口面积饱和在泄漏面积；当阀口完全打开时，阀口面积饱和在最大阀口面积。当阀口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增大阀口面积。

下表显示了 4-Way 2-Position Directional Valve (MA) 模块的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四个路径均关闭。 | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间所有四个路径均打开。 | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** < B-T 阀芯行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open   connections**:   `P-A` - **Negative spool position open   connections**:   `P-B`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** < –B-T 阀芯行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > –P-A 阀芯行程 - **Spool position at maximum A-T orifice   area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum B-T orifice   area** < –B-T 阀芯行程 |
| 过渡期间所有路径均关闭。 | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > –A-T 阀芯行程 |

### 阀口参数化

**Orifice parameterization** 参数指定一个或所有阀口的打开面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路应用相同的数据。当您选择 `Different for all flow paths` 时，模块对每条流路使用各自的参数化。

模块用于控制每个阀口的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量取决于端口 **S** 处的阀芯位置。当阀芯移动以打开阀口时，流量能力的度量从指定的最小值按比例变化到指定的最大值。
- `Tabulated` — 模块根据端口 **S** 处的阀芯位置计算流量能力的度量。该函数使用一维查找表。

**Orifice parameterization** 参数决定模块如何计算每个阀口中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 缩放每个阀口中的流量。流量系数衡量流体在某一压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，缩放每个阀口中的流量。流量系数衡量流体在某一压差驱动下流动的难易程度。
- `Orifice area` — 阀口面积的大小缩放每个阀口中的流量。

### 可视化阀口开度

要可视化阀芯偏移和最大位移，请右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示声速流导、*Kv* 流量系数、*Cv* 流量系数或阀口面积随阀芯位置的变化。

更改模块参数后要更新数据，请在图窗中点击 **Reload Data**。

下图显示了使用默认值的阀配置。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或正在对空气以外的流体建模，则可能需要按混合气体比重的平方根缩放声速流导。
- 此模块不对超声速流建模。
- 阀与环境之间没有热交换。
