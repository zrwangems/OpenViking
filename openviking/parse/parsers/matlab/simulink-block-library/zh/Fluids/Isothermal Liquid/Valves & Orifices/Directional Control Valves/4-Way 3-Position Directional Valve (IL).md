---
type: simulink-block
title: '4-Way 3-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalveil'
documentation_source_path: 'ref/4way3positiondirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: P
  summary: 液体端口，等温液体
  direction: conserving
- name: T
  summary: 液体端口，等温液体
  direction: conserving
- name: S
  summary: 阀芯位移，m，物理信号
  direction: input
```

### 守恒端口

### **A** — 液体端口，等温液体

阀的液体进入或出口端口。

### **B** — 液体端口，等温液体

阀的液体进入或出口端口。

### **P** — 液体端口，等温液体

阀的液体进入或出口端口。

### **T** — 液体端口，等温液体

阀的液体进入或出口端口。

### 输入

### **S** — 阀芯位移，m，物理信号

阀芯位移，单位为 m，指定为物理信号。
## 参数
```yaml
parameters:
- name: 正阀芯位置开启连接
  summary: 阀芯处于正位置时开启的流路 P-A, B-T（默认）| P-A, P-B | P-B, A-T | P-A | P-B | P-A, P-B, A-B
  group: 阀配置
- name: 中性阀芯位置开启连接
  summary: 阀芯处于中性位置时开启的流路 All closed（默认）| P-A, P-B, A-T, B-T | A-T, B-T | P-A, A-T | P-A, B-T | P-A, P-B | P-B, A-T | P-B,
    B-T | A-T | B-T | P-A | P-B | P-T | P-A, A-T, P-T | P-A, P-B, A-B | P-B, B-T, P-T | P-A, P-B, A-T, B-T, P-T
  group: 阀配置
- name: 负阀芯位置开启连接
  summary: 阀芯向负方向运动时开启的流路 P-A, B-T（默认）| P-A, P-B | P-B, A-T | P-A | P-B | P-A, P-B, A-B
  group: 阀配置
- name: 中性阀芯位置开启连接的一致性检查
  summary: 是否检查节流口设置是否与指定的最大节流口开度阀芯位置一致 Warning（默认）| Error | None
  group: 阀配置
- name: 面积特性
  summary: 节流口的流量方程 Identical for all flow paths（默认）| 每条流各不相同 path
  group: 模型参数化
- name: Orifice parameterization
  summary: 计算开口面积的方法 Linear area vs. spool travel（默认）| Tabulated data - Area vs. spool travel | Tabulated data - Volumetric
    flow rate vs. spool travel and pressure drop
  group: 模型参数化
- name: Spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: 模型参数化
- name: Maximum orifice area
  summary: 最大开口面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Leakage area
  summary: 节流孔完全关闭时的开口面积 1e-9 m^2（默认）| 正标量
  group: 模型参数化
- name: Spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: Orifice area vector
  summary: 阀开口面积向量 [1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: Spool travel vector, ds
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: Pressure drop vector, dp
  summary: 阀压降值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: 模型参数化
- name: Volumetric flow rate table, q(ds,dp)
  summary: 体积流量数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: 模型参数化
- name: Constant orifice area
  summary: 相同流路的节流孔面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Constant orifice pressure drop vector
  summary: 相同流路的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: 模型参数化
- name: Constant orifice volumetric flow rate vector
  summary: 相同流路的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: 模型参数化
- name: 端口 P、T、A 和 B 处的横截面积
  summary: 守恒端口处的面积 inf m^2（默认）| 正标量
  group: 模型参数化
- name: 流量系数
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: 临界雷诺数
  summary: 层流的雷诺数上限 150（默认）| 正标量
  group: 模型参数化
- name: 平滑因子
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: 模型参数化
- name: 压力恢复
  summary: 是否考虑面积扩大时的压力增加 off（默认）| on
  group: 模型参数化
- name: P-A 节流口最大面积处的阀芯位置
  summary: P-A 节流口完全开启时的阀芯偏移 7.5e-3 m（默认）| 正标量
  group: P-A 节流口
- name: P-A 阀芯在关闭与打开节流孔之间的行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-A 节流口
- name: P-A 最大节流孔面积
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: P-A 节流口
- name: P-A 节流孔阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A 节流孔面积向量
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice spool travel vector, ds
  summary: 阀芯开口距离相对于完全关闭位置的向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice pressure drop vector, dp
  summary: 压降值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-A 节流口
- name: P-A constant orifice area
  summary: 恒定节流口横截面积 1e-4 m^2（默认）| 正标量
  group: P-A 节流口
- name: P-A constant orifice pressure drop vector
  summary: 恒定节流口压差向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A constant orifice volumetric flow rate vector
  summary: 恒定节流口体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-A 节流口
- name: Spool position at maximum P-B orifice area
  summary: P-B 节流口面积最大时的阀芯位置 7.5e-3 m（默认）| 正标量
  group: P-B Orifice
- name: P-B spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-B Orifice
- name: P-B maximum orifice area
  summary: 最大节流口开口面积 1e-4 m^2（默认）| 正标量
  group: P-B Orifice
- name: P-B orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B orifice spool travel vector, ds
  summary: 相对于全关位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-B Orifice
- name: P-B constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: P-B Orifice
- name: P-B constant orifice pressure drop vector
  summary: 恒定节流口的压差向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-B Orifice
- name: A-T 节流孔面积最大时的阀芯位置
  summary: 完全打开 A-T 节流孔时阀芯偏离中位的位置 7.5e-3 m（默认）| 正标量
  group: A-T 节流孔
- name: A-T 节流孔关闭与打开之间的阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: A-T 节流孔
- name: A-T 最大节流孔面积
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: A-T 节流孔
- name: A-T 节流孔阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T orifice spool travel vector, ds
  summary: 相对于全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: A-T 节流孔
- name: A-T constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: A-T 节流孔
- name: A-T constant orifice pressure drop vector
  summary: 恒定节流口的压差向量或值 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: B-T 节流孔最大面积处的阀芯位置
  summary: 完全打开 B-T 节流孔时阀芯从中位偏移的距离 7.5e-3 m（默认）| 正标量
  group: B-T 节流孔
- name: B-T 节流孔关闭与打开之间的阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: B-T 节流孔
- name: B-T 最大节流孔面积
  summary: 最大节流孔开度面积 1e-4 m^2（默认）| 正标量
  group: B-T 节流孔
- name: B-T 节流孔阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: B-T orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: B-T orifice spool travel vector, ds
  summary: 相对于全关位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: B-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: B-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: B-T 节流孔
- name: B-T constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: B-T 节流孔
- name: B-T constant orifice pressure drop vector
  summary: 恒定节流口的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: B-T constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: B-T 节流孔
- name: 最大 P-T 节流口面积处的阀芯位置
  summary: 完全打开 P-T 节流口时阀芯从中位偏移的距离 0 m（默认）| 正标量
  group: P-T 节流口
- name: 节流口关闭与打开之间的 P-T 阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-T 节流口
- name: P-T 最大节流口面积
  summary: 最大节流口开度面积 1e-4 m^2（默认）| 正标量
  group: P-T 节流口
- name: P-T 节流口阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-T 节流口
- name: P-T 节流口阀芯行程向量，ds
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-T 节流口
- name: P-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-T 节流口
- name: P-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-T 节流口
- name: 4-Way 3-Position Directional Valve Area fault
  summary: 用于对阀面积故障建模的选项 Add fault
  group: 故障
- name: Spool position when faulted
  summary: 故障时的阀特性 Positive（默认）| Neutral | Negative | Maintain last value
  group: 故障
```

### 阀配置

### **正阀芯位置开启连接** — 阀芯处于正位置时开启的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯处于正位置时开启的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。当 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error` 时，可以将此参数的设置与其他节流口的定义进行一致性检查。

### **中性阀芯位置开启连接** — 阀芯处于中性位置时开启的流路 `All closed`（默认）| `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

阀芯处于中性位置时开启的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。当 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error` 时，可以将此参数的设置与其他节流口的定义进行一致性检查。

### **负阀芯位置开启连接** — 阀芯向负方向运动时开启的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯向负方向运动时开启的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。当 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error` 时，可以将此参数的设置与其他节流口的定义进行一致性检查。

### **中性阀芯位置开启连接的一致性检查** — 是否检查节流口设置是否与指定的最大节流口开度阀芯位置一致 `Warning`（默认）| `Error` | `None`

是否检查 **阀配置** 选项卡上的中性阀芯位置开启设置是否与最大节流口面积处指定的阀芯位置一致。对于每个启用的节流口，阀芯中性位置处的实际偏移量应与每个单独节流口指定的阀芯偏移量相匹配。

### 模型参数化

### **面积特性** — 节流口的流量方程 `Identical for all flow paths`（默认）| `每条流各不相同 path`

对阀节流口面积应用统一的或单独的流量方程。`Identical for all flow paths` 对所有阀节流口使用相同的节流口和阀芯几何参数、流量、压力和面积向量。使用 `每条流各不相同 path` 时，这些参数针对每个节流口单独指定。在两种情况下，节流口 **A**、**B**、**P** 和 **T** 在 `Linear - Area vs. spool travel` 和 `Tabulated data - Area vs. spool travel` 参数化中具有相同的横截面积、流量系数和雷诺数。相同的 **节流口参数化** 应用于所有流路。

### **Orifice parameterization** — 计算开口面积的方法 `Linear area vs. spool travel`（默认）| `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

计算阀开口面积的方法。在表格数据参数化中，您可以为非线性阀开口轮廓提供自己的阀面积和阀芯行程数据，或者您可以提供以体积流量、阀芯行程和流路压降表示的数据。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Maximum orifice area** — 最大开口面积 `1e-4 m^2`（默认）| 正标量

阀运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Leakage area** — 节流孔完全关闭时的开口面积 `1e-9 m^2`（默认）| 正标量

节流孔完全关闭时的开口面积。任何小于此值的面积都保持为指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀开口面积向量 `[1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **Pressure drop vector, dp** 参数一起构成二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。
压降向量与 **Spool travel vector, ds** 参数一起构成独立轴，用于二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Constant orifice area** — 相同流路的节流孔面积 `1e-4 m^2`（默认）| 正标量

当正、中和负滑阀位置具有相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`。
- `Tabulated data - Area vs. spool travel`

必须在所有三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中和负滑阀位置具有相同节流孔时，阀上的压差值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。这些值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

必须在所有三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中和负滑阀位置具有相同节流孔时，恒定节流孔的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。这些值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量与阀芯行程和压降的关系`。

在三个 **阀配置** 参数中必须选择相同的节流口：

- **正阀芯位置开启连接**
- **中位阀芯位置开启连接**
- **负阀芯位置开启连接**

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，用于确定通过阀的质量流量的压力-流量方程中。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为以下之一：

- `线性 - 面积与阀芯行程的关系`
- `表格数据 - 面积与阀芯行程的关系`

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中流量损失的修正因子。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为以下之一：

- `线性 - 面积与阀芯行程的关系`
- `表格数据 - 面积与阀芯行程的关系`

### **临界雷诺数** — 层流的雷诺数上限 `150`（默认）| 正标量

通过节流口的层流的雷诺数上限。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为：

- `线性 - 面积与阀芯行程的关系`
- `表格数据 - 面积与阀芯行程的关系`

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近开启和接近关闭位置时，基于流量响应引入一层渐变。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为 `线性 - 面积与阀芯行程的关系`。

### **压力恢复** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为：

- `线性 - 面积与阀芯行程的关系`
- `表格数据 - 面积与阀芯行程的关系`

### P-A 节流口

### **P-A 节流口最大面积处的阀芯位置** — P-A 节流口完全开启时的阀芯偏移 `7.5e-3 m`（默认）| 正标量

P-A 节流口完全开启时阀芯从中位位置的偏移量。**中位阀芯位置开启连接的一致性检查** 参数将根据其他节流口阀芯位置通知您为此阀芯位置设置的值是否不一致或不符合物理规律。要可视化定义的偏移量，请参阅可视化节流口开度。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**注意：**

仅当 P-A 节流口设置未同时出现在所有三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 阀芯在关闭与打开节流孔之间的行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A 最大节流孔面积** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作期间 P-A 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-A 节流孔面积向量**参数中的元素一一对应。
这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A 节流孔面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **P-A 阀芯行程向量**参数中的元素一一对应。
这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice spool travel vector, ds** — 阀芯开口距离相对于完全关闭位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-A orifice pressure drop vector, dp** 参数一起构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 参数。这些值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice pressure drop vector, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-A orifice spool travel vector, ds** 参数一起构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 参数。这些值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正、中、负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为以下任一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice pressure drop vector** — 恒定节流口压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中、负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **P-A constant orifice volumetric flow rate vector** 参数中的元素一一对应。这些值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice volumetric flow rate vector** — 恒定节流口体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。这些值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — P-B 节流口面积最大时的阀芯位置 `7.5e-3 m`（默认）| 正标量

P-B 节流口完全打开时阀芯偏离中位的位置。如果为此阀芯位置设置的值根据其他节流口阀芯位置不一致或不符合物理规律，**Consistency check for neutral spool position open connections** 参数会通知您。要可视化已定义的偏移，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接**设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**注意：**

仅当 P-B 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**设置为 `每条流各不相同 path`。
2. **节流口参数化**设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   或将**中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   或将**负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作过程中 P-B 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**设置为 `每条流各不相同 path`。
2. **节流口参数化**设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-B orifice area vector** 参数中的元素一一对应。各值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**设置为 `每条流各不相同 path`。
2. **节流口参数化**设置为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **P-B spool travel vector** 参数中的元素一一对应。各元素按升序排列，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice spool travel vector, ds** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-T orifice pressure drop vector, dp** 参数共同构成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table, q(ds,dp)** 参数。各值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`。

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-B orifice spool travel vector, ds** 参数共同构成独立轴，用于二维因变量 **P-B orifice volumetric flow rate table, q(ds,dp)** 参数。各值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector, ds** 参数中向量元素的个数。
- *N* 是 **P-B orifice pressure drop vector, dp** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中位和负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice pressure drop vector** — 恒定节流口的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中位和负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **P-B constant orifice volumetric flow rate vector** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice volumetric flow rate vector** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中位和负阀芯位置具有相同节流口时，阀门上的体积流量值向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### A-T 节流孔

### **A-T 节流孔面积最大时的阀芯位置** — 完全打开 A-T 节流孔时阀芯偏离中位的位置 `7.5e-3 m`（默认）| 正标量

完全打开 A-T 节流孔时阀芯偏离中位的位置。
**中位阀芯位置开启连接一致性检查**参数将根据其他节流孔阀芯位置，通知您为该阀芯位置设置的值是否不一致或不符合物理规律。要可视化所定义的偏移量，请参阅可视化节流孔开度。

#### 依赖项

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接**为 `P-B,
  A-T`。
- **中位阀芯位置开启连接**为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
- **负阀芯位置开启连接**为 `P-B,
  A-T`。

**注意：**

仅当 A-T 节流孔设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-T 节流孔关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回不符合物理规律的值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T 最大节流孔面积** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流孔的最大开口面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格参数化的阀芯行程距离向量。向量元素必须与 **A-T 节流孔面积向量**参数中的元素一一对应。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B,
   A-T`。

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B,
   A-T`。

### **A-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **A-T spool travel vector** 参数中的元素一一对应。
元素按升序列出，且必须大于
0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B,
   A-T`。

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B,
   A-T`。

### **A-T orifice spool travel vector, ds** — 相对于全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-T orifice pressure drop vector, dp**
参数一起构成独立轴，用于二维因变量 **A-T orifice volumetric flow
rate table, q(ds,dp)** 参数。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B,
   A-T`。

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B,
   A-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T
orifice spool travel vector, ds** 参数一起构成独立轴，用于二维
因变量 **A-T orifice volumetric flow rate table,
q(ds,dp)** 参数。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B,
   A-T`。

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B,
   A-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice pressure drop vector** — 恒定节流口的压差向量或值 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中和负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **A-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中和负阀芯位置具有相同节流口时的体积流量值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`。

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### B-T 节流孔

### **B-T 节流孔最大面积处的阀芯位置** — 完全打开 B-T 节流孔时阀芯从中位偏移的距离 `7.5e-3 m`（默认）| 正标量

完全打开 B-T 节流孔时阀芯从中位偏移的距离。
**中位阀芯位置开启连接一致性检查**参数将根据其他节流孔阀芯位置，通知您为此阀芯位置设置的值是否不一致或不符合物理规律。要可视化已定义的偏移量，请参阅可视化节流孔开度。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接**为 `P-A,
  B-T`。
- **中位阀芯位置开启连接**为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
- **负阀芯位置开启连接**为 `P-A,
  B-T`。

**注意：**

仅当 B-T 节流孔设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **B-T 节流孔关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T 最大节流孔面积** — 最大节流孔开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 B-T 节流孔的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T 节流孔阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **B-T 节流孔面积向量**参数中的元素一一对应。这些值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与
**B-T orifice spool travel vector**
参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice spool travel vector, ds** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。阀芯行程向量与
**B-T orifice pressure drop vector,
dp** 参数一起构成二维因变量 **B-T orifice
volumetric flow rate table, q(ds,dp)** 参数的独立轴。这些值按升序排列，且第一个元素必须为 0。
表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **B-T
orifice spool travel vector, ds** 参数一起构成二维因变量
**B-T orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。这些值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **B-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中和负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中和负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的一项设置：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### P-T 节流口

### **最大 P-T 节流口面积处的阀芯位置** — 完全打开 P-T 节流口时阀芯从中位偏移的距离 `0 m`（默认）| 正标量

完全打开 P-T 节流口时阀芯从中位偏移的距离。
**中位阀芯位置开启连接一致性检查**参数将根据其他节流口阀芯位置通知您
为该阀芯位置设置的值是否不一致或不符合物理规律。要可视化已定义的偏移量，请参见
可视化节流口开度。

#### 依赖关系

要启用此参数，请将 **中位阀芯位置开启
连接**设置为

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

。

### **节流口关闭与打开之间的 P-T 阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，
以便仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. **中位阀芯位置开启
   连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 最大节流口面积** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. **中位阀芯位置开启
   连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的控制构件行程距离向量。
向量元素必须与 **P-T 节流口面积
向量**参数中的元素一一对应。这些值按升序
列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. **中位阀芯位置开启
   连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 节流口阀芯行程向量，ds** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。
阀芯行程向量与 **P-T 节流口压降向量，
dp** 参数一起构成二维因变量 **P-T 节流口
体积流量表，q(ds,dp)** 参数的独立轴。这些
值按升序列出，且第一个元素必须为 0。
表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-T
orifice spool travel vector, ds** 参数一起构成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table,
q(ds,dp)** 参数。这些值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T orifice spool travel vector,
  ds** 参数中向量元素的数量。
- *N* 是 **P-T orifice pressure drop vector,
  dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### 故障

### **4-Way 3-Position Directional Valve Area fault** — 用于对阀面积故障建模的选项 `Add fault`

用于在模块中对阀面积故障建模的选项。要添加故障，请点击 **Add
fault** 超链接。当故障发生时，通常由开口参数化设置的阀面积将根据 **Spool position when faulted**
参数中指定的值进行设置。

### **Spool position when faulted** — 故障时的阀特性 `Positive`（默认）| `Neutral` | `Negative` | `Maintain last value`

故障时的阀滑阀位置。您可以选择当滑阀处于正位置、负位置或故障触发时的位置时使阀卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

4-Way 3-Position Directional Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的四位三通方向阀

四位三通方向阀 (IL) 模块对等温液体网络中的具有四个开口的阀进行建模，通常位于执行器、泵和油箱之间。阀的操作由单个阀芯控制，阀芯根据端口 **S** 处的信号而位移。您可以通过在 **Neutral spool position open connections** 参数中指定当阀芯处于中位（以 0 m 为中心）时打开的节流口，在 **Positive spool position open connections** 参数中指定当阀芯向正方向移动时打开的节流口，以及在 **Negative spool position open connections** 参数中指定当阀芯向负方向移动时打开的节流口，来设置阀的基线配置。

您可以在 **Orifice parameterization** 参数中将阀开口的模型设置为线性关系或用户提供数据的函数，该设置可应用于阀中的一个或所有流路。

**示例阀设置**

在此示例配置中，**Neutral spool position open connections** 设置为 `All closed`。当阀芯处于中位时，所有节流口均关闭，无流量通过：

在此配置中，**Negative spool position open connections** 设置为 `P-A, B-T`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开，允许流量通过。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭，无流量通过：

在此配置中，**Positive spool position open connections** 设置为 `P-B, A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开，允许流量通过，而端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭：

在示意图中，此配置显示为：

左侧对应正位置，右侧对应负位置。

### 滑阀位移与阀配置

*滑阀行程*是节流口从关闭位置到完全打开所需的滑阀移动量，并且针对**阀配置**选项卡上选择的每个节流口进行定义。下表显示了如何根据阀节流口参数化和流路特性计算行程。

**基于参数化和流路的滑阀行程**

| 节流口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| 线性 - 面积与滑阀行程的关系 | 由**关闭和打开节流口之间的滑阀行程**参数定义 | 由每个节流口的关闭和打开节流口之间的滑阀行程参数定义 |
| 表格数据 - 面积与滑阀行程的关系 | **滑阀行程向量**参数第一个和最后一个元素之间的差值 | 每个节流口的滑阀行程向量参数第一个和最后一个元素之间的差值 |
| 表格数据 - 体积流量与滑阀行程和压降的关系 | **滑阀行程向量，ds**参数第一个和最后一个元素之间的差值 | 每个节流口的滑阀行程向量，ds参数第一个和最后一个元素之间的差值 |

可视化节流口开度一节详细介绍了如何查看所有阀节流口的方向。

端口**S**处发出信号的滑阀运动方向取决于滑阀行程和节流口方向：

**节流口定义与滑阀行程方向**

| 节流口打开时的滑阀位置 | 滑阀行程，*ΔS* |
| --- | --- |
| 始终关闭（在任何滑阀位置配置中均未选择该节流口） | 不适用 |
| 始终打开（在正、中性和负滑阀位置配置中均选择了该节流口） | 不适用 |
| 负 | *S*orifice\_max + 滑阀行程 – **S** |
| 负和中性 | *S*orifice\_max + 滑阀行程 – **S** |
| 正 | *S*orifice\_max – 滑阀行程 + **S** |
| 正和中性 | *S*orifice\_max – 滑阀行程 + **S** |
| 中性 | \|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |
| 正和负 | –\|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |

其中*S*orifice\_max是为每个节流口定义的最大节流口面积处的滑阀位置。当*ΔS*为负时，节流口面积饱和于泄漏面积；当节流口完全打开时，节流口面积饱和于最大节流口面积。当节流口完全打开时，*ΔS*等于滑阀行程，因此*ΔS*大于滑阀行程不会进一步增加节流口面积。

**中性滑阀位置打开连接的一致性检查**参数验证

- **中性滑阀位置打开连接**中列出的任何节流口在**S**处信号为0时打开。
- **中性滑阀位置打开连接**中未列出的任何节流口在**S**处信号为0时关闭。

您可以选择在此检查被违反时接收警告或错误。

4-Way 3-Position Directional Valve (IL) 模块的可能配置如下所示。

**4-Way 3-Position Directional Valve 配置**

| 配置 | 参数值 |
| --- | --- |
|  | 在中位时四个节流口全部关闭。（默认）  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时四个节流口全部开启。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 |
|  | 节流口 A-T 和 B-T 开启。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 在中位时节流口 P-A 和 A-T 开启。节流口 P-B 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, A-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 A-T 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 B-T 开启。节流口 P-A、P-B 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 P-A、P-B 开启。节流口 A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-A 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 开启。节流口 P-A、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 和 B-T 开启。节流口 P-A 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-B, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中位时开启，并在阀芯位移时关闭。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = 任意值 |
|  | 节流口 P-A 是恒定节流口。节流口 P-B、A-T 和 B-T 在中位时开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = 任意值 - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 节流口 P-B 是恒定节流口。节流口 P-A、A-T、B-T 在中位时开启。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** > –P-A 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = 任意值 |
|  | 在中位时节流口 P-A 关闭。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。端口 **B** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 A-T 开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = 任意值 - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 B-T 开启。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = 任意值 |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`  - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = 任意值 |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-A, P-B`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = 任意值 |

### 阀门孔口参数化

**孔口参数化**参数设置通过一个或所有阀门孔口的开启面积或体积流量的模型。如果**面积特性**设置为`Identical for all flow paths`，则该模块对所有流路应用相同的数据；否则，对于`Different for all flow paths`设置，将应用各自的参数化。您可以通过三种方式对阀门开度进行建模：

- `Linear - area vs. spool travel`

  开启面积是作为端口**S**处信号接收的阀芯位置的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

  其中：

  - *ΔS* 是在 Orifice Definition and Spool Travel Direction 中定义的阀芯行程。
  - *ΔSmax* 是**Spool travel between closed and open orifice**。
  - *Amax* 是**Maximum orifice area**。
  - *Aleak* 是**Leakage area**。

  当*ΔS*为负时，*Aorifice*饱和于*Aleak*；当孔口完全打开时，*Aorifice*饱和于*Amax*。当孔口完全打开时，*ΔS*等于阀芯行程，因此*ΔS*大于阀芯行程不会进一步增加孔口面积。

  当阀门在线性参数化中处于接近打开或接近关闭的位置时，您可以通过调整**Smoothing factor**参数来保持仿真中的数值鲁棒性。如果**Smoothing factor**参数非零，则该模块在*Aleak*和*Amax*之间平滑地饱和开启面积。有关详细信息，请参阅 Numerical Smoothing。
- `Tabulated data - Area vs. spool travel`

  为您的系统或端口**P**、**A**、**B**和**T**之间的各个流路提供阀芯行程向量。此数据将用于计算孔口面积与阀芯位移之间的关系。插值用于确定给定数据点之间的开启面积。*A*leak和*A*max分别是开启面积向量的第一个和最后一个参数。
- `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

  提供阀芯行程和压降向量以及相关的二维体积流量数组。插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

### 可视化节流口开度

要可视化阀芯偏移和最大位移，请右键点击该模块，然后选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的节流口。节流口参数化决定坐标轴，坐标轴为以下之一：

- 节流口面积与阀芯位置的关系
- 体积流量与阀芯位置的关系，在特定压差下查询

当 **Valve Configuration** 中的正、中性和负设置对应同一个节流口时，该图将节流口开度显示为常数。

更改模块参数后要更新数据，请在图窗上点击 **Reload Data**。

此图显示了一个阀门配置示例。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Neutral spool position open connections** 为 `P-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`。

所有其他阀芯位置均为默认值。

**示例阀芯位置可视化**

该可视化显示，P-A 节流口在阀芯位置 `-2.53e-3` 到 `2.53e-3` m 之间打开。由于 P-A 节流口仅在阀芯沿正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，您可以更改：

- **Spool position at maximum P-A orifice area** 为大于 0.005 m 的值。
- **Consistency check for neutral spool position open connections** 为 `None`。
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置。

### 故障

要对故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Spool position when faulted** 参数有四个故障选项：

- `Positive` — 阀芯位置冻结在正位置，将 **Positive spool position open connections** 参数指定的流路打开到其最大值。由 **Negative spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Neutral` — 阀芯位置冻结在中性位置，将所有流路打开到其在 0 m 处指定的值。
- `Negative` — 阀芯位置冻结在负位置，将 **Negative spool position open connections** 参数指定的流路打开到其最大值。由 **Positive spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 触发发生时，阀门冻结在当时的阀芯位置。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其比例与 **Smoothing factor** 值成正比。有关详细信息，请参阅 Numerical Smoothing。

故障触发后，阀门在仿真的剩余时间内保持故障面积。

### Composite Structure

此模块是一个复合组件，由多个 Orifice
(IL) 模块实例组成。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice
(IL) 模块。

### Predefined Parameterization

您可以使用预参数化的制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，点击 **Selected part** 旁边的
   "<click to select>" 超链接，该链接位于模块对话框设置中的 **Selected part** 旁边。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，
   然后点击 **Apply all**。您可以使用
   **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。
   该模块现在具有您指定的参数化。
4. 您可以在 Block Parameterization Manager 窗口中选择一个部件，并查看
   **将选定部分与模块进行比较**
   部分中的数据，从而将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数
值。该模块会用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理
行为之间会存在一些偏差。为确保准确性，请根据实验数据验证仿真行为，
并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
