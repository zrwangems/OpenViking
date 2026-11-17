---
type: simulink-block
title: '3-Way Directional Valve (MA)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 湿空气端口 湿空气
  direction: conserving
- name: P
  summary: 湿空气端口 湿空气
  direction: conserving
- name: T
  summary: 湿空气端口 湿空气
  direction: conserving
- name: S
  summary: 控制构件位移，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 湿空气端口 湿空气

阀门的入口或出口点。

### **P** — 湿空气端口 湿空气

阀门的入口或出口点。

### **T** — 湿空气端口 湿空气

阀门的入口或出口点。
### 输入

### **S** — 控制构件位移，m 物理信号

以 m 为单位的阀芯位置位移，以物理信号形式接收。对于在正阀芯位置打开的流路，正信号打开节流孔。对于在负阀芯位置打开的流路，负信号打开节流孔。
## 参数
```yaml
parameters:
- name: 正阀芯位置打开的连接
  summary: 阀芯处于正位置时打开的流路 All closed（默认）| P-A, A-T, P-T | P-A | A-T | P-T
  group: 阀门配置
- name: 负阀芯位置打开的连接
  summary: 阀芯沿负方向移动时打开的流路 All closed（默认）| P-A, A-T, P-T | P-A | A-T | P-T
  group: 阀门配置
- name: 面积特性
  summary: 节流孔的流量方程 Identical for all flow paths（默认）| 每条流各不相同 path
  group: 模型参数化
- name: 阀门参数化
  summary: 可变或恒定节流孔参数化 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: 模型参数化
- name: 关闭和打开节流孔之间的阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: 模型参数化
- name: 开启特性
  summary: 将控制信号转换为流量能力度量的方法 Linear（默认）| Tabulated
  group: 模型参数化
- name: 阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: 最大 Cv 流量系数
  summary: 对应于最大开启组件的 *Cv* 系数 4（默认）| 正标量
  group: 模型参数化
- name: Cv 流量系数向量
  summary: 构件位置向量中各值对应的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: 模型参数化
- name: 最大 Kv 流量系数
  summary: 对应于最大开启组件的 *Kv* 系数 3.6（默认）| 正标量
  group: 模型参数化
- name: Kv 流量系数向量
  summary: 构件位置向量中各值对应的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: 模型参数化
- name: 最大节流孔面积
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: 节流孔面积向量
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: 阻塞流下的 xT 压差比系数
  summary: 压差比 0.7（默认）| 正标量
  group: 模型参数化
- name: 流量系数
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: Maximum sonic conductance
  summary: 对应组件最大开启状态的声导 12 l/(bar*s)（默认）| 正标量
  group: 模型参数化
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: 模型参数化
- name: Subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: 模型参数化
- name: ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: 模型参数化
- name: ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: 模型参数化
- name: Sonic conductance vector
  summary: 对应阀芯行程向量中各值的声导 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 正值向量
  group: 模型参数化
- name: Critical pressure ratio vector
  summary: 对应阀芯行程向量中各值的临界压力比 0.3 * ones(1,6)（默认）| 正数向量
  group: 模型参数化
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认）| 正标量
  group: 模型参数化
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: 模型参数化
- name: Laminar flow pressure ratio
  summary: 层流-湍流过渡压力比 0.999（默认）| 正标量
  group: 模型参数化
- name: Cross-sectional area at ports A, P, and T
  summary: 守恒端口处的面积 0.01 m^2（默认）| 正标量
  group: 模型参数化
- name: Spool position at maximum P-A orifice area
  summary: P-A 节流口完全打开时的阀芯偏移 5e-3 m（默认）| 正标量
  group: P-A Orifice
- name: P-A spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice maximum Cv flow coefficient
  summary: 对应组件最大开启状态的 *Cv* 系数 4（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice Cv flow coefficient vector
  summary: 对应成员位置向量 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）中值的 *Cv* 系数 | 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice maximum Kv flow coefficient
  summary: 对应最大开启组件的 *Kv* 系数 3.6（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice Kv flow coefficient vector
  summary: 对应成员位置向量 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）中值的 *Kv* 系数 | 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A maximum orifice area
  summary: 最大孔口开启面积 1e-4 m^2（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice area vector
  summary: 阀门开启面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice area
  summary: 恒定孔口的横截面积 1e-4 m^2（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice xT pressure differential ratio factor at choked flow
  summary: 压差比 0.7（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice sonic conductance
  summary: 恒定节流口声导 12 l/(bar*s)（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice critical pressure ratio
  summary: 恒定节流口流量首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice maximum sonic conductance
  summary: 节流口最大开启时对应的声导 12 l/(bar*s)（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice critical pressure ratio
  summary: 流量首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice sonic conductance vector
  summary: 阀芯行程向量中各值对应的声导 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice critical pressure ratio vector
  summary: 阀芯行程向量中各值对应的临界压力比 0.3 * ones(1, 6)（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: P-A Orifice
- name: P-A orifice ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: P-A Orifice
- name: Spool position at maximum A-T orifice area
  summary: A-T 节流口完全打开时的阀芯偏移 5e-3 m（默认）| 正标量
  group: A-T Orifice
- name: A-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: A-T Orifice
- name: A-T constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice maximum Cv flow coefficient
  summary: 对应组件最大开启状态的 *Cv* 系数 4（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice Cv flow coefficient vector
  summary: 对应构件位置向量中各值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice maximum Kv flow coefficient
  summary: 对应组件最大开启状态的 *Kv* 系数 3.6（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice Kv flow coefficient vector
  summary: 对应构件位置向量中各值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T maximum orifice area
  summary: 最大节流口开启面积 1e-4 m^2（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice xT pressure differential ratio factor at choked flow
  summary: 压差比 0.7（默认）| 正标量
  group: A-T Orifice
- name: A-T constant orifice sonic conductance
  summary: 恒定节流口的声速导流 12 l/(bar*s)（默认）| 正标量
  group: A-T Orifice
- name: A-T constant orifice critical pressure ratio
  summary: 恒定节流口流量首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice maximum sonic conductance
  summary: 节流口最大开启时对应的声速导流 12 l/(bar*s)（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice critical pressure ratio
  summary: 流量首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice sonic conductance vector
  summary: 与阀芯行程向量中的值对应的声速导流 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice critical pressure ratio vector
  summary: 与阀芯行程向量中的值对应的临界压力比 0.3 * ones(1, 6)（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice subsonic index
  summary: 用于表征亚声速流态下质量流量的指数 0.5（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: A-T Orifice
- name: A-T orifice ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: A-T Orifice
- name: Spool position at maximum P-T orifice area
  summary: 完全打开 P-T 节流口的阀芯偏移量 5e-3 m（默认）| 正标量
  group: P-T Orifice
- name: P-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-T Orifice
- name: P-T constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice maximum Cv flow coefficient
  summary: 对应组件最大开度的 *Cv* 系数 4（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice Cv flow coefficient vector
  summary: 成员位置向量中各值对应的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: P-T Orifice
- name: P-T constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice maximum Kv flow coefficient
  summary: 对应组件最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice Kv flow coefficient vector
  summary: '*Kv* coefficients for values in member position vector [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量'
  group: P-T Orifice
- name: P-T orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m（默认）| 1×*n*
    向量
  group: P-T Orifice
- name: P-T maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-T Orifice
- name: P-T constant orifice area
  summary: Cross-sectional area for constant orifice 1e-4 m^2（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7（默认）| 正标量
  group: P-T Orifice
- name: P-T constant orifice sonic conductance
  summary: Sonic conductance for constant orifice 12 l/(bar*s)（默认）| 正标量
  group: P-T Orifice
- name: P-T constant orifice critical pressure ratio
  summary: Ratio of downstream and upstream pressures at which the flow first chokes for constant orifice 0.3（默认）| 正标量
  group: P-T Orifice
- name: P-T orifice maximum sonic conductance
  summary: Sonic conductance corresponding to maximally open orifice 12 l/(bar*s)（默认）| 正标量
  group: P-T Orifice
- name: P-T 节流孔临界压力比
  summary: 流量首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: P-T Orifice
- name: P-T 节流孔声速导纳向量
  summary: 与阀芯行程向量中的值对应的声速导纳 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 1×*n* 向量
  group: P-T Orifice
- name: P-T 节流孔临界压力比向量
  summary: 与阀芯行程向量中的值对应的临界压力比 0.3 * ones(1, 6)（默认）| 1×*n* 向量
  group: P-T Orifice
- name: P-T 节流孔亚声速指数
  summary: 用于表征亚声速流态下质量流量的指数 0.5（默认）| 正标量
  group: P-T Orifice
- name: P-T 节流孔 ISO 参考温度
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: P-T Orifice
- name: P-T 节流孔 ISO 参考密度
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: P-T Orifice
```

### 阀门配置

### **正阀芯位置打开的连接** — 阀芯处于正位置时打开的流路 `All closed`（默认）| `P-A, A-T, P-T` | `P-A` | `A-T` | `P-T`

阀芯处于正位置时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **负阀芯位置打开的连接** — 阀芯沿负方向移动时打开的流路 `All closed`（默认）| `P-A, A-T, P-T` | `P-A` | `A-T` | `P-T`

阀芯沿负方向移动时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### 模型参数化

### **面积特性** — 节流孔的流量方程 `Identical for all flow paths`（默认）| `每条流各不相同 path`

是否对阀门节流孔面积应用统一的或各自的流量方程。当您将此参数设置为 `Identical for all flow paths` 时，模块对所有阀门节流孔使用相同的节流孔和阀芯几何形状、流量、压力和面积向量。当您将此参数设置为 `每条流各不相同 path` 时，您可以为每个节流孔单独指定这些参数。对于这两种设置，当您将 **Valve parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **阀门参数化** — 可变或恒定节流孔参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据节流孔两端的压差计算质量流量或根据质量流量计算压差的方法。

### **关闭和打开节流孔之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Linear`。

### **开启特性** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀门面积数据对节流孔进行参数化时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 对应于最大开启组件的 *Cv* 系数 `4`（默认）| 正标量

节流孔完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv 流量系数向量** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **Control member position vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应于最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

节流孔完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv 流量系数向量** — 构件位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **Control member position vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **最大节流孔面积** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **节流孔面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀门面积数据对节流孔进行参数化时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出这些值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Orifice area`。

### **Maximum sonic conductance** — 对应组件最大开启状态的声导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时的声导值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，
**Valve parameterization** 设置为
`Sonic conductance`，并将
**Opening characteristic** 设置为
`Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，
**Valve parameterization** 设置为
`Sonic conductance`，并将
**Opening characteristic** 设置为
`Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，并将
**Valve parameterization** 设置为
`Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，并将
**Valve parameterization** 设置为
`Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，并将
**Valve parameterization** 设置为
`Sonic conductance`。

### **Sonic conductance vector** — 对应阀芯行程向量中各值的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声导向量。每个声导对应 **Spool travel
vector** 参数中的一个值。向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，
**Valve parameterization** 设置为
`Sonic conductance`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Critical pressure ratio vector** — 对应阀芯行程向量中各值的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应 **Spool travel
vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **Spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`Identical for all flow paths`，
**Valve parameterization** 设置为
`Sonic conductance`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening
characteristic** 设置为
`Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，基于阀门处于接近打开和接近关闭位置时的流量响应引入一层渐变。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Opening
characteristic** 设置为
`Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的节流口出口压力与入口压力之比。在层流中压力损失与质量流量成线性关系，在湍流中成二次关系。

### **Cross-sectional area at ports A, P, and T** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、
**A** 和 **B** 处的最大横截面积，模块在确定通过阀门的质量流量的压力-流量方程中使用该值。

### P-A Orifice

### **Spool position at maximum P-A orifice area** — P-A 节流口完全打开时的阀芯偏移 `5e-3 m`（默认）| 正标量

P-A 节流口完全打开时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 设置为 `P-A`
  或 `P-A, A-T, P-T`。
- **Negative spool position open
  connections** 设置为 `P-A`
  或 `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，才启用此参数。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，**Opening
characteristic** 设置为 `Linear`，
并设置以下参数之一：

- **Positive spool position open
  connections** 设置为 `P-A`
  或 `P-A, A-T, P-T`。
- **Negative spool position open
  connections** 设置为 `P-A`
  或 `P-A, A-T, P-T`。

### **P-A constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-A 节流口的恒定 *Cv*
流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `每条流各不相同
   path`
2. **Valve parameterization** 设置为
   `Cv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 设置为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设置为
     `P-A` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流口设置同时出现在两个阀芯位置参数中时才启用此参数：**Positive spool position open connections** 和
**Negative spool position open
connections**。

### **P-A orifice maximum Cv flow coefficient** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

P-A 节流口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Cv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice Cv flow coefficient vector** — 对应成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）中值的 *Cv* 系数 | 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Cv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-A 孔口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow
   coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-A 孔口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-A orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

P-A 孔口完全开启且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice Kv flow coefficient vector** — 对应成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中值的 *Kv* 系数 | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `每条流各不相同 path`，将 **Opening characteristic** 设置为 `Tabulated`，并设置以下参数之一：

- **正阀芯位置开启
  连接**为 `P-A`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启
  连接**为 `P-A`
  或 `P-A, A-T, P-T`。

### **P-A maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-A 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice area vector** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开启面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-A 孔口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-A orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即 P-A 孔口首次发生阻塞流时的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中至少一个：

   - **正阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A constant orifice sonic conductance** — 恒定节流口声导 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的声导。该值是在阻塞起始点测得的，通过阻力元件的质量流量与上游压力和 ISO 8778 中定义的标准条件下质量密度的乘积之比。该参数决定了在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和
**Negative spool position open
connections**。

### **P-A constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-A 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和
**Negative spool position open
connections**。

### **P-A orifice maximum sonic conductance** — 节流口最大开启时对应的声导 `12` `l/(bar*s)`（默认）| 正标量

当 P-A 节流口完全打开且可用流动面积最大时的声导值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice sonic conductance vector** — 阀芯行程向量中各值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声导向量。每个声导对应 **P-A orifice spool
travel vector** 参数中的一个值。向量的大小必须与 **P-A orifice spool travel vector**
参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice critical pressure ratio vector** — 阀芯行程向量中各值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应 **P-A orifice spool travel vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **P-A orifice
spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`
2. **Valve parameterization** 为
   `Sonic conductance`
3. **Opening characteristic** 为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为
     `P-A` 或
     `P-A, A-T, P-T`。

### **P-A orifice subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`每条流各不相同 path`，
**Valve parameterization** 设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。
- **Negative spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。

### **P-A orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`每条流各不相同 path`，
**Valve parameterization** 设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。
- **Negative spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。

### **P-A orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为
`每条流各不相同 path`，
**Valve parameterization** 设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **Positive spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。
- **Negative spool position open
  connections** 为 `P-A`
  或 `P-A, A-T, P-T`。

### A-T Orifice

### **Spool position at maximum A-T orifice area** — A-T 节流口完全打开时的阀芯偏移 `5e-3 m`（默认）| 正标量

A-T 节流口完全打开时阀芯从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **Negative spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，此参数才启用。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设为 `Different for each
flow path`，**Opening
characteristic** 设为 `Linear`，
并设置以下参数之一：

- **Positive spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **Negative spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。

### **A-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

A-T 节流口的恒定 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Cv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和
**Negative spool position open
connections**。

### **A-T orifice maximum Cv flow coefficient** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

A-T 节流口完全打开且可用流通面积为最大值时的 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Cv flow
   coefficient`
3. **Opening characteristic** 设为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T orifice Cv flow coefficient vector** — 对应构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Cv flow
   coefficient`
3. **Opening characteristic** 设为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

A-T 节流口的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Kv flow
   coefficient`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**Positive spool position open connections** 和
**Negative spool position open
connections**。

### **A-T orifice maximum Kv flow coefficient** — 对应组件最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

A-T 节流口完全打开且可用流通面积为最大值时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Kv flow
   coefficient`
3. **Opening characteristic** 设为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T orifice Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Kv flow
   coefficient`
3. **Opening characteristic** 设为
   `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的阀芯行程距离向量。按升序列出各值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设为 `Different for each
flow path`，**Opening
characteristic** 设为
`Tabulated`，并设置以下参数之一：

- **Positive spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **Negative spool position open
  connections** 设为
  `A-T` 或 `P-A,
  A-T, P-T`。

### **A-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀门工作过程中 A-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设为
   `每条流各不相同
   path`
2. **Valve parameterization** 设为
   `Orifice area`
3. **Opening characteristic** 设为
   `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 设为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **A-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序排列。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Orifice area`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Orifice area`
3. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

A-T 节流口首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Kv flow coefficient` 或 `Cv flow
   coefficient`
3. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T constant orifice sonic conductance** — 恒定节流口的声速导流 `12` `l/(bar*s)`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的声速导流。该值是在阻塞开始时测得的，通过阻力元件的质量流量与上游压力和标准条件下质量密度（如 ISO 8778 所定义）乘积之比。此参数决定了在给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **A-T constant orifice critical pressure ratio** — 恒定节流口流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的临界压力比。该值是流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

**注意：**

仅当 A-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **A-T orifice maximum sonic conductance** — 节流口最大开启时对应的声速导流 `12` `l/(bar*s)`（默认）| 正标量

当 A-T 节流口完全打开且可用于流动的面积最大时的声速导流值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Linear`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice sonic conductance vector** — 与阀芯行程向量中的值对应的声速导流 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻力元件内部的声速导流向量。每个导流值对应于 **A-T orifice spool travel vector** 参数中的一个值。向量的大小必须与 **A-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同
   path`
2. **Valve parameterization** 为 `Sonic conductance`
3. **Opening characteristic** 为 `Tabulated`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。
   - **Negative spool position open
     connections** 为 `A-T` 或 `P-A, A-T, P-T`。

### **A-T orifice critical pressure ratio vector** — 与阀芯行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应于 **A-T orifice spool travel vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **A-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `A-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `A-T` 或
     `P-A, A-T, P-T`。

### **A-T orifice subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将**面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **负阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。

### **A-T orifice ISO reference temperature** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将**面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **负阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。

### **A-T orifice ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将**面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并设置以下参数中的至少一个：

- **正阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。
- **负阀芯位置开启
  连接**为
  `A-T` 或 `P-A,
  A-T, P-T`。

### P-T Orifice

### **Spool position at maximum P-T orifice area** — 完全打开 P-T 节流口的阀芯偏移量 `5e-3 m`（默认）| 正标量

完全打开 P-T 节流口时阀芯从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启
  连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启
  连接**为 `P-T`
  或 `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流口设置未同时出现在**正阀芯
位置开启连接**和**负阀芯位置开启
连接**参数中时，此参数才启用。

### **P-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值用于为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请将**面积
特性**设置为 `Different for each
flow path`，**开度
特性**设置为 `Linear`，
并设置以下参数之一：

- **正阀芯位置开启
  连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启
  连接**为 `P-T`
  或 `P-A, A-T, P-T`。

### **P-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-T 节流口的常数 *Cv*
流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Cv flow
   coefficient`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**和
**负阀芯位置开启
连接**。

### **P-T orifice maximum Cv flow coefficient** — 对应组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

P-T 节流口完全打开且可用流通面积为最大值时的 *Cv* 流量
系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Cv flow
   coefficient`
3. **开度特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T orifice Cv flow coefficient vector** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应
**P-T orifice spool travel vector** 参数中的一个值。此
参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。向量的大小
必须与 **P-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Cv flow
   coefficient`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-T 节流口的常数 *Kv*
流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `每条流各不相同
   path`
3. **阀门参数化**为
   `Kv flow
   coefficient`
4. 每个参数中的以下设置之一：

   - **正阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启
     连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流口设置同时出现在两个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**和
**负阀芯位置开启
连接**。

### **P-T orifice maximum Kv flow coefficient** — 对应组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

P-T 节流口完全打开且可用流通面积为最大值时的 *Kv* 流量
系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow
   coefficient`
3. **开启特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T orifice Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `每条流各不相同
   path`
3. **阀门参数化**为
   `Kv flow
   coefficient`
4. **开启特性**为
   `Tabulated`
5. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性**设置为 `Different for each
flow path`，将 **开启特性**设置为
`Tabulated`，并设置以下参数之一：

- **正阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。

### **P-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-T 节流孔的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开启面积向量。向量元素必须与 **P-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. **开启特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Orifice area`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-T orifice xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-T 节流孔首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
3. 以下参数中的至少一个：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T constant orifice sonic conductance** — Sonic conductance for constant orifice `12` `l/(bar*s)`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流孔时的声速导。此值是在阻塞流开始时测得的通过阻力元件的质量流量与上游压力和标准条件下质量密度乘积之比，如 ISO 8778 中所定义。此参数决定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-T constant orifice critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes for constant orifice `0.3`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流孔时的临界压力比。此值是流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

**注意：**

仅当 P-T 节流孔设置同时出现在两个阀芯位置参数中时，此参数才会启用：**Positive spool position open connections** 和 **Negative spool position open connections**。

### **P-T orifice maximum sonic conductance** — Sonic conductance corresponding to maximally open orifice `12` `l/(bar*s)`（默认）| 正标量

当 P-T 节流孔完全打开且可用于流动的面积最大时的声速导值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T 节流孔临界压力比** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速决定）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Linear`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T 节流孔声速导纳向量** — 与阀芯行程向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12]` `l/(bar*s)`（默认）| 1×*n* 向量

阻性元件内部的声速导纳向量。每个导纳对应于 **P-T 节流孔阀芯行程向量**参数中的一个值。向量的大小必须与 **P-T 节流孔阀芯行程向量**参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T 节流孔临界压力比向量** — 与阀芯行程向量中的值对应的临界压力比 `0.3 * ones(1, 6)`（默认）| 1×*n* 向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应于 **P-T 节流孔阀芯行程向量**参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **P-T 节流孔阀芯行程向量**参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`
2. **阀门参数化**为
   `Sonic conductance`
3. **开度特性**为
   `Tabulated`
4. 以下参数之一：

   - **正阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。
   - **负阀芯位置开启连接**为
     `P-T` 或
     `P-A, A-T, P-T`。

### **P-T 节流孔亚声速指数** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并至少设置以下参数之一：

- **正阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。

### **P-T 节流孔 ISO 参考温度** — ISO 8778 参考温度 `293.15` `K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并至少设置以下参数之一：

- **正阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。

### **P-T 节流孔 ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **面积特性**设置为
`每条流各不相同 path`，
**阀门参数化**设置为
`Sonic conductance`，并至少设置以下参数之一：

- **正阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。
- **负阀芯位置开启连接**为 `P-T`
  或 `P-A, A-T, P-T`。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的三位三通方向阀

3-Way Directional Valve (MA) 模块对湿空气网络中具有三个开口的阀门进行建模，通常位于执行器、泵和油箱之间。阀门操作由根据端口 **S** 处信号位移的单个阀芯控制。您可以通过分别在 **正阀芯位置开启连接**和 **负阀芯位置开启连接**参数中指定阀芯正向和负向移动时开启的节流孔，来设置阀门的基线配置。有关模块如何计算通过可变节流孔的流量的更多详细信息，请参阅 Orifice (MA)。

示例阀门配置图

在此配置中，**正阀芯位置开启连接**设置为 `A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **A** 和 **T** 之间的路径打开以允许流动。端口 **P** 和 **A** 之间以及端口 **P** 和 **T** 之间的路径关闭：

显示端口 A 和 T 之间流动且端口 P 关闭的图

在此配置中，**负阀芯位置开启连接**设置为 `P-A`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 和 **A** 之间的路径打开以允许流动，端口 **T** 和 **A** 之间以及端口 **P** 和 **T** 之间的路径关闭：

显示端口 A 和 T 之间流动且端口 P 关闭的图

您可以通过将 **正阀芯位置开启连接**或 **负阀芯位置开启连接**设置为 `P-T` 或 `P-A, A-T, P-T` 来打开端口 **P** 和 **T** 之间的路径。

流路可以在正阀芯位置或负阀芯位置打开，但不能同时在两者中打开。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数
  *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导率决定模块参数化。声速导率衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 可视化孔口开度

要可视化阀芯偏移和位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示声速导率、
*Kv* 流量
系数、*Cv* 流量
系数或孔口面积随阀芯位置的变化。

要在更改模块参数后更新数据，请在图窗中单击 **Reload
Data**。

下图显示了使用默认值的阀门配置。

每个孔口的面积与阀芯位置关系图。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于
  气动应用。如果将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能
  需要按混合气体比重的平方根来缩放声速导率。
- 此模块不建模超声速流动。
- 阀门与环境之间没有热交换。
