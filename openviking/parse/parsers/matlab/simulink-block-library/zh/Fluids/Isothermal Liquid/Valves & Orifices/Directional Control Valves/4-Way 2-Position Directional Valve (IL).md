---
type: simulink-block
title: '4-Way 2-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalveil'
documentation_source_path: 'ref/4way2positiondirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (IL)

## 端口
```yaml
ports:
- name: A
  summary: 进油或出油口，等温液体
  direction: conserving
- name: B
  summary: 进油或出油口，等温液体
  direction: conserving
- name: P
  summary: 进油或出油口，等温液体
  direction: conserving
- name: T
  summary: 进油或出油口，等温液体
  direction: conserving
- name: S
  summary: 阀芯位移，m，物理信号
  direction: input
```

### 守恒端口

### **A** — 进油或出油口，等温液体

阀的液体进入或流出口。

### **B** — 进油或出油口，等温液体

阀的液体进入或流出口。

### **P** — 进油或出油口，等温液体

阀的液体进入或流出口。

### **T** — 进油或出油口，等温液体

阀的液体进入或流出口。
### 输入

### **S** — 阀芯位移，m，物理信号

与阀芯位移相关的物理信号，单位为 m。
## 参数
```yaml
parameters:
- name: 正阀芯位置开启连接
  summary: 阀芯处于正位置时打开的流路 P-A, B-T（默认）| P-A, P-B | P-B, A-T | P-A | P-B | P-A, P-B, A-T, B-T
  group: 阀配置
- name: 负阀芯位置开启连接
  summary: 阀芯沿负方向运动时打开的流路 P-B, A-T（默认）| P-A, B-T | P-A, P-B | P-A | P-B | P-A, P-B, A-T, B-T
  group: 阀配置
- name: 面积特性
  summary: 节流口的流量方程 所有流路相同（默认）| 每条流路不同
  group: 模型参数化
- name: 节流口参数化
  summary: 计算开启面积的方法 线性面积 vs. 阀芯行程（默认）| 表格数据 - 面积 vs. 阀芯行程 | 表格数据 - 体积流量 vs. 阀芯行程和压降
  group: 模型参数化
- name: 关闭和开启节流口之间的阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: 模型参数化
- name: 最大节流口面积
  summary: 最大节流口开启面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: 泄漏面积
  summary: 节流口完全关闭时的开启面积 1e-10 m^2（默认）| 正标量
  group: 模型参数化
- name: 阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: 节流口面积向量
  summary: 阀开启面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: 阀芯行程向量，ds
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: 压降向量，dp
  summary: 阀压降值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: 模型参数化
- name: 体积流量表，q(ds,dp)
  summary: 体积流量数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: 模型参数化
- name: 恒定节流口面积
  summary: 相同流路的节流口面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: 恒定节流口压降向量
  summary: 相同流路的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: 模型参数化
- name: 恒定节流口体积流量向量
  summary: 相同流路的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: 模型参数化
- name: 端口 P、T、A 和 B 处的横截面积
  summary: 守恒端口处的面积 inf m^2（默认）| 正标量
  group: 模型参数化
- name: 流量系数
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: 临界雷诺数
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 模型参数化
- name: 平滑因子
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: 模型参数化
- name: 压力恢复
  summary: 是否考虑面积扩大时的压力增加 off（默认）| on
  group: 模型参数化
- name: 最大 P-A 节流口面积处的阀芯位置
  summary: 完全开启 P-A 节流口的阀芯偏移 5e-3 m（默认）| 正标量
  group: P-A 节流口
- name: 关闭和开启节流口之间的 P-A 阀芯行程
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-A 节流口
- name: P-A 最大节流口面积
  summary: 最大节流口开启面积 1e-4 m^2（默认）| 正标量
  group: P-A 节流口
- name: P-A 节流口阀芯行程向量
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A 节流口面积向量
  summary: 阀开启面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice spool travel vector, ds
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice pressure drop vector, dp
  summary: 压降值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-A 节流口
- name: P-A constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: P-A 节流口
- name: P-A constant orifice pressure drop vector
  summary: 恒定节流口的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A 节流口
- name: P-A constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-A 节流口
- name: Spool position at maximum P-B orifice area
  summary: 完全打开 P-B 节流口时的阀芯偏移 -5e-3（默认）| 正标量
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
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
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
  summary: 恒定节流孔压降向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B constant volumetric flow rate vector
  summary: 恒定节流孔体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-B Orifice
- name: Spool position at maximum A-T orifice area
  summary: 完全打开 A-T 节流孔的阀芯偏移 -5e-3 m（默认）| 正标量
  group: A-T Orifice
- name: A-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: A-T Orifice
- name: A-T maximum orifice area
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice spool travel vector, ds
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: A-T Orifice
- name: A-T constant orifice area
  summary: 恒定节流孔横截面积 1e-4 m^2（默认）| 正标量
  group: A-T Orifice
- name: A-T constant orifice pressure drop vector
  summary: 恒定节流孔压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T constant orifice volumetric flow rate vector
  summary: 恒定节流孔体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: A-T Orifice
- name: Spool position at maximum B-T orifice area
  summary: 完全打开 B-T 节流孔的阀芯偏移 5e-3 m（默认）| 正标量
  group: B-T Orifice
- name: B-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: B-T Orifice
- name: B-T maximum orifice area
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice spool travel vector, ds
  summary: 相对于全关位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: B-T Orifice
- name: B-T constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T constant orifice pressure drop vector
  summary: 恒定节流口的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T constant volumetric flow rate vector
  summary: 恒定节流口的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: B-T Orifice
- name: 4-Way 2-Position Directional Valve Area fault
  summary: 用于对阀门面积故障建模的选项 Add fault
  group: 故障
- name: Spool position when faulted
  summary: 故障时的阀门特性 Positive（默认）| Negative | Maintain last value
  group: 故障
```

### 阀配置

### **正阀芯位置开启连接** — 阀芯处于正位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **负阀芯位置开启连接** — 阀芯沿负方向运动时打开的流路 `P-B, A-T`（默认）| `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯沿负方向运动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### 模型参数化

### **面积特性** — 节流口的流量方程 `所有流路相同`（默认）| `每条流路不同`

是否对阀节流口面积应用统一或单独的流量方程。当您将此参数设置为 `所有流路相同` 时，模块对所有阀节流口使用相同的节流口和阀芯几何形状、流量、压力和面积向量。当您将此参数设置为 `每条流路不同` 时，您可以为每个节流口单独指定这些参数。对于这两种设置，当您将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程` 或 `表格数据 - 面积 vs. 阀芯行程` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **节流口参数化** — 计算开启面积的方法 `线性面积 vs. 阀芯行程`（默认）| `表格数据 - 面积 vs. 阀芯行程` | `表格数据 - 体积流量 vs. 阀芯行程和压降`

计算阀开启面积的方法。如果您将此参数设置为表格数据参数化之一，您可以为非线性阀开启曲线提供自己的阀面积和阀芯行程数据，或者提供体积流量、阀芯行程和流路压降形式的数据。

### **关闭和开启节流口之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程`。

### **最大节流口面积** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀运行期间每个节流口的最大开启面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程`。

### **泄漏面积** — 节流口完全关闭时的开启面积 `1e-10 m^2`（默认）| 正标量

节流口完全关闭时的开启面积。模块将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程`。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格阀面积数据参数化节流口时的阀芯行程距离向量。向量元素必须与 **节流口面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 面积 vs. 阀芯行程`。

### **节流口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格阀面积数据参数化节流口时的开启面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 面积 vs. 阀芯行程`。

### **阀芯行程向量，ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格体积流量数据参数化节流口时的阀芯行程距离向量。阀芯行程向量与 **压降向量，dp** 参数构成二维因变量 **体积流量表，q(ds,dp)** 参数的独立轴。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

### **压降向量，dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

根据表格流量数据参数化节流口时的压降值向量。压降向量与 **阀芯行程向量，ds** 参数构成二维因变量 **体积流量表，q(ds,dp)** 参数的独立轴。按升序列出值。值必须大于 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

### **体积流量表，q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **阀芯行程向量，ds** 参数中的向量元素数量。
- *N* 是 **压降向量，dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

### **恒定节流口面积** — 相同流路的节流口面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为以下之一：

- `线性 - 面积 vs. 阀芯行程`
- `表格数据 - 面积 vs. 阀芯行程`

在 **阀配置** 部分的两个参数中选择相同的节流口：

- **正阀芯位置开启连接**
- **负阀芯位置开启连接**

### **恒定节流口压降向量** — 相同流路的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流口时，阀上的压差值向量。向量元素与 **恒定节流口体积流量向量** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

在 **阀配置** 部分的两个参数中选择相同的节流口：

- **正阀芯位置开启连接**
- **负阀芯位置开启连接**

### **恒定节流口体积流量向量** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流口时，恒定节流口的体积流量值向量。向量元素与 **恒定节流口压降向量** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

在 **阀配置** 部分的两个参数中选择相同的节流口：

- **正阀芯位置开启连接**
- **负阀芯位置开启连接**

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

进入和流出口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为以下之一：

- `线性 - 面积 vs. 阀芯行程`
- `表格数据 - 面积 vs. 阀芯行程`

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

考虑理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为以下之一：

- `线性 - 面积 vs. 阀芯行程`
- `表格数据 - 面积 vs. 阀芯行程`

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流口的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为：

- `线性 - 面积 vs. 阀芯行程`
- `表格数据 - 面积 vs. 阀芯行程`

### **平滑因子** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近开启和接近关闭位置时，基于流量响应引入逐渐变化的层。为了提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程`。

### **压力恢复** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为：

- `线性 - 面积 vs. 阀芯行程`
- `表格数据 - 面积 vs. 阀芯行程`

### P-A 节流口

### **最大 P-A 节流口面积处的阀芯位置** — 完全开启 P-A 节流口的阀芯偏移 `5e-3 m`（默认）| 正标量

完全开启 P-A 节流口时阀芯从中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

将 **正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

将 **负阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置未同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **关闭和开启节流口之间的 P-A 阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流路不同`。
2. **节流口参数化** 为 `线性 - 面积 vs. 阀芯行程`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 最大节流口面积** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀运行期间 P-A 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流路不同`。
2. **节流口参数化** 为 `线性 - 面积 vs. 阀芯行程`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **P-A 节流口面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流路不同`。
2. **节流口参数化** 为 `表格数据 - 面积 vs. 阀芯行程`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 节流口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格参数化的开启面积向量。向量元素必须与 **P-A 阀芯行程向量** 参数中的元素一一对应。元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与
**P-A orifice pressure drop vector, dp** 参数一起构成二维因变量
**P-A orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。按升序列出这些值。
第一个元素必须为 0。该模块在数据点之间使用线性插值。

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

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice pressure drop vector, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与
**P-A orifice spool travel vector, ds** 参数一起构成二维因变量
**P-A orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。按升序列出这些值。
元素必须大于 0。该模块在数据点之间使用线性插值。

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

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector,
  ds** 参数中的向量元素数量。
- *N* 是 **P-A orifice pressure drop vector,
  dp** 参数中的向量元素数量。

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

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive
spool position open connections** 和 **Negative spool position open
connections** 参数中时，此参数才启用。

### **P-A constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流口时，阀门上的压差值向量。
向量元素与 **P-A constant orifice volumetric flow rate
vector** 参数中的元素一一对应。按升序列出这些值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive
spool position open connections** 和 **Negative spool position open
connections** 参数中时，此参数才启用。

### **P-A constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流口时，阀门上的压差值向量。
向量元素与 **P-A constant orifice pressure drop vector**
参数中的元素一一对应。按升序列出这些值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，此参数才启用。

### P-B Orifice

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 节流口时的阀芯偏移 `-5e-3`（默认）| 正标量

完全打开 P-B 节流口时相对于中位位置的阀芯偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，此参数才启用。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值提供了计算的上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   或将 **Negative spool position
   open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与
**P-B orifice area vector** 参数中的元素一一对应。按升序列出这些值。
第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与
**P-B spool travel vector** 参数中的元素一一对应。按升序列出这些元素。
元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与
**P-B orifice pressure drop vector, dp** 参数一起构成二维因变量
**P-B orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。按升序列出这些值。
第一个元素必须为 0。该模块在数据点之间使用线性插值。

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

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与
**P-B orifice spool travel vector, ds** 参数一起构成二维因变量
**P-B orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。按升序列出这些值。
元素必须大于 0。该模块在数据点之间使用线性插值。

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

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector,
  ds** 参数中的向量元素数量。
- *N* 是 **P-B orifice pressure drop vector,
  dp** 参数中的向量元素数量。

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

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-B 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，此参数才启用。

### **P-B constant orifice pressure drop vector** — 恒定节流孔压降向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流孔时，阀门上的压差值的向量。向量元素与 **P-B constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B constant volumetric flow rate vector** — 恒定节流孔体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流孔时，阀门上的体积流量值的向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### A-T Orifice

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 节流孔的阀芯偏移 `-5e-3 m`（默认）| 正标量

完全打开 A-T 节流孔时阀芯从中位位置的偏移。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门操作期间 A-T 节流孔的最大开口面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-T orifice pressure drop vector, dp** 参数一起构成二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 参数的独立轴。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T orifice spool travel vector, ds** 参数一起构成二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 参数的独立轴。按升序列出值。元素必须大于 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的体积流量 *M*×*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T constant orifice area** — 恒定节流孔横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **A-T constant orifice pressure drop vector** — 恒定节流孔压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流孔时，阀门上的压差值的向量。向量元素与 **A-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流孔体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正和负阀芯位置包含相同节流孔时的体积流量值的向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流孔的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 B-T 节流孔时阀芯从中位位置的偏移。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Negative spool position open connections** 为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门操作期间 B-T 节流孔的最大开口面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素按升序排列。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T orifice spool travel vector, ds** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。阀芯行程向量与 **B-T orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **B-T orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。元素必须大于 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

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

   **Negative spool position open connections** 为 `P-A, B-T`。

### **B-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **B-T constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正阀芯位置和负阀芯位置包含相同节流口时，阀门上的压差值向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **B-T constant volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正阀芯位置和负阀芯位置包含相同节流口时，阀门上的压差值向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-A, B-T`。

   **Negative spool position open connections** 为 `P-A, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### 故障

### **4-Way 2-Position Directional Valve Area fault** — 用于对阀门面积故障建模的选项 `Add fault`

用于在该模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将根据 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障时的阀门特性 `Positive`（默认）| `Negative` | `Maintain last value`

故障时的阀芯位置。您可以选择当阀芯处于正位置、负位置或故障触发时的位置时使阀门卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a：使用 Simscape faults 接口对故障建模

4-Way 2-Position Directional Valve (IL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体网络中的四通两位方向阀

4-Way 2-Position Directional Valve (IL) 模块在等温液体网络中为具有四个开口的阀门建模——例如执行器、泵与油箱之间的阀门。阀门操作由单个阀芯控制，该阀芯根据端口 **S** 处的信号发生位移。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定当阀芯沿正方向和负方向移动时打开的节流口，来设置阀门的基线配置。您可以在 **Orifice parameterization** 参数中将阀门开口模型设置为线性关系或用户提供数据的函数，并可将其应用于阀门中的一个或所有流路。

该模块是一个复合组件，由多个 Orifice (IL) 模块实例组成。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice (IL) 模块。在某些配置中，该阀门类似于三通阀。要在阀芯处于中位时设置附加流路，请参阅 4-Way 3-Position Directional Valve (IL) 模块。

此图显示了一个示例阀门设置，其中阀门连接到油箱、执行器和泵，并且 **Positive spool position open connections** 参数为 `P-B, A-T`：

此图显示了当 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀门：

在此配置中，当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开以允许流动。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭以阻止流动。

此图显示了当 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀门：

在此配置中，当端口 **S** 处的信号使阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开以允许流动，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭。

表示此配置的示意图为：

左侧对应正位置，右侧对应负位置。阀门通过中间中性区段中的位置进行过渡。

### 滑阀位移与阀配置

*滑阀行程*是指节流口从关闭位置到完全打开所需的滑阀移动量。您可以使用**节流口参数化**和**面积特性**参数来指定流路特性：

| 节流口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义滑阀行程 | **Spool travel between closed and open orifice** 参数为每个节流口定义滑阀行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数的第一个和最后一个元素之差定义滑阀行程 | 每个节流口的 **Spool travel vector** 参数的第一个和最后一个元素之差定义滑阀行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数的第一个和最后一个元素之差定义滑阀行程 | 每个节流口的 **Spool travel vector, ds** 参数的第一个和最后一个元素之差定义滑阀行程 |

滑阀移动方向取决于滑阀行程、节流口方向和端口 **S** 处的信号。下表显示了根据 **Positive spool position open connection** 和 **Negative spool position open connection** 参数的选择，节流口的滑阀行程：

| 节流口打开时的滑阀位置 | 滑阀行程，*ΔS* |
| --- | --- |
| 节流口始终关闭：节流口未被选入 **Positive spool position open connection** 或 **Negative spool position open connection** 参数 | 不适用 |
| 节流口始终打开：节流口同时被选入 **Positive spool position open connection** 和 **Negative spool position open connection** 参数 | 不适用 |
| 负：节流口仅被选入 **Negative spool position open connection** 参数 | *S*orifice\_max + 滑阀行程 – **S** |
| 正：节流口仅被选入 **Positive spool position open connection** 参数 | *S*orifice\_max – 滑阀行程 + **S** |

其中 *S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积饱和于泄漏面积；当节流口完全打开时，节流口面积饱和于最大节流口面积。当节流口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程不会进一步增加节流口面积。

下表显示了 4-Way 2-Position Directional Valve (IL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四条路径均关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** > B-T 滑阀行程 |
| 过渡期间所有四条路径均打开。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** < B-T 滑阀行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** > B-T 滑阀行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open   connections**：   `P-A` - **Negative spool position open   connections**：   `P-B`  - **Spool position at maximum P-A orifice   area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** < –P-B 滑阀行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** < –B-T 滑阀行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** > –B-T 滑阀行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 滑阀行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > –P-A 滑阀行程 - **Spool position at maximum A-T orifice   area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum B-T orifice   area** < –B-T 滑阀行程 |
| 过渡期间所有路径均关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** > A-T 滑阀行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 滑阀行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** < –P-B 滑阀行程 - **Spool position at maximum B-T orifice   area** > B-T 滑阀行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice   area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice   area** > –A-T 滑阀行程 |

### 阀节流口参数化

**Orifice parameterization** 参数指定通过一个或所有阀节流口的打开面积或体积流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路应用相同的数据。当您选择 `Different for all flow paths` 时，模块对每条流路使用单独的参数化。

当 **Orifice parameterization** 为 `Linear - area vs. spool travel` 时，打开面积是端口 **S** 处接收到的滑阀位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中：

- *ΔS* 是滑阀行程。

  *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，在节流口完全打开时饱和于 *Amax*。当节流口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程的值不会增加节流口面积。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。

  当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和打开面积。有关详细信息，请参阅 Numerical Smoothing。

当 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 时，您可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供滑阀行程向量。模块使用此数据计算节流口面积与滑阀位移之间的关系。模块使用插值确定数据点之间的打开面积。*A*leak 和 *A*max 分别是打开面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，您可以提供滑阀行程和压降向量以及相关的二维体积流量数组。模块使用插值确定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

### 可视化节流口开度

要可视化滑阀偏移和最大位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示由 **Valve Configuration** 部分中的参数指定的节流口。坐标轴为以下之一：

- 节流口面积对滑阀位置
- 体积流量对滑阀位置，在特定压差下查询

当您将 **Valve Configuration** 选项卡中的参数设置为同一节流口时，节流口开度为常数。

单击 **Reload Data** 以更新图中的数据。

此图显示了模块的默认配置：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

所有其他滑阀位置均为默认值。

**滑阀位置可视化示例**

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Spool position when faulted** 参数有三个故障选项：

- `Positive` — 滑阀位置冻结在正位置，将 **Positive spool position open connections** 参数指定的流路打开到其最大值。**Negative spool position open connections** 参数指定的流路关闭。
- `Negative` — 滑阀位置冻结在负位置，将 **Negative spool position open connections** 参数指定的流路打开到其最大值。**Positive spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 阀在触发发生时的滑阀位置冻结。

由于阀面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其比例与 **Smoothing factor** 值成正比。有关详细信息，请参阅 Numerical Smoothing。

故障触发后，阀在仿真的剩余时间内保持在故障面积。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的“<click to select>”超链接。
2. Block Parameterization Manager 窗口打开。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块对缺失数据使用工程判断和简化假设进行替代。因此，预期仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
