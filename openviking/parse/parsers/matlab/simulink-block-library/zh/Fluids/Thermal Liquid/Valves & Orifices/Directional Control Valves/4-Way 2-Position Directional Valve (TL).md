---
type: simulink-block
title: '4-Way 2-Position Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalvetl'
documentation_source_path: 'ref/4way2positiondirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 热液体进口或出口
  direction: conserving
- name: B
  summary: 热液体进口或出口
  direction: conserving
- name: P
  summary: 热液体进口或出口
  direction: conserving
- name: T
  summary: 热液体进口或出口
  direction: conserving
- name: S
  summary: 阀芯位移，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 热液体进口或出口

阀的热液体进口或出口。

### **B** — 热液体进口或出口

阀的热液体进口或出口。

### **P** — 热液体进口或出口

阀的热液体进口或出口。

### **T** — 热液体进口或出口

阀的热液体进口或出口。
### 输入

### **S** — 阀芯位移，m 物理信号

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
  summary: 计算开启面积的方法 线性面积 vs. 阀芯行程（默认）| 表格数据 - 面积 vs. 阀芯行程 | 表格数据 - 体积流量 vs. 阀芯行程和压降 | 表格数据 - 质量流量 vs. 阀芯行程和压降
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
- name: 质量流量表，mdot(ds,dp)
  summary: 质量流量数组 [-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91,
    6, 7.7, 9.13] kg/s（默认）| *M*×*N* 矩阵
  group: 模型参数化
- name: Reference inflow temperature
  summary: 指定质量流量数据时的温度 293.15 K（默认）| 正标量
  group: 模型参数化
- name: Reference inflow pressure
  summary: 指定表格化质量流量数据时的压力 0.101325 MPa（默认）| 正标量
  group: 模型参数化
- name: Constant orifice area
  summary: 相同流路的节流孔面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Constant orifice pressure drop vector
  summary: 相同流路的压差向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: 模型参数化
- name: Constant orifice volumetric flow rate vector
  summary: 相同流路的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: 模型参数化
- name: Cross-sectional area at ports P, T, A and B
  summary: 守恒端口处的面积 0.01 m^2（默认）| 正标量
  group: 模型参数化
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 模型参数化
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: 模型参数化
- name: Pressure recovery
  summary: 是否考虑面积扩大中的压力增加 off（默认）| on
  group: 模型参数化
- name: Spool position at maximum P-A orifice area
  summary: 完全打开 P-A 节流孔时的阀芯偏移 5e-3 m（默认）| 正标量
  group: P-A Orifice
- name: P-A spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-A Orifice
- name: P-A maximum orifice area
  summary: 最大节流孔开口面积 1e-4 m^2（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice spool travel vector
  summary: 相对于全关位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice area vector
  summary: 阀开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice spool travel vector, ds
  summary: 相对于全关位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice pressure drop vector, dp
  summary: 压降值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-A Orifice
- name: P-A orifice mass flow rate table, mdot(ds,dp)
  summary: 质量流量值数组 [-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91,
    6, 7.7, 9.13] kg/s（默认）| *M*×*N* 矩阵
  group: P-A Orifice
- name: P-A constant orifice area
  summary: 恒定节流口横截面积 1e-4 m^2（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice pressure drop vector
  summary: 恒定节流口的压差向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice mass flow rate vector
  summary: 恒定节流口的质量流量向量 [-.9, 1.6, 2, 2.4] kg/s（默认）| 1×*n* 向量
  group: P-A Orifice
- name: Spool position at maximum P-B orifice area
  summary: 完全打开 P-B 节流口时的阀芯偏移 -5e-3（默认）| 正标量
  group: P-B 节流口
- name: P-B spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-B 节流口
- name: P-B maximum orifice area
  summary: 最大节流口开度面积 1e-4 m^2（默认）| 正标量
  group: P-B 节流口
- name: P-B orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B orifice area vector
  summary: 阀门开度面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B orifice spool travel vector, ds
  summary: 相对于完全关闭位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: P-B 节流口
- name: P-B orifice mass flow rate table, mdot(ds,dp)
  summary: 质量流量值数组 [-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91,
    6, 7.7, 9.13] kg/s（默认）| *M*×*N* 矩阵
  group: P-B 节流口
- name: P-B constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: P-B 节流口
- name: P-B constant orifice pressure drop vector
  summary: 恒定节流口的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B constant volumetric flow rate vector
  summary: 恒定节流孔的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: P-B 节流口
- name: P-B constant orifice mass flow rate vector
  summary: 恒定节流孔的质量流量向量 [-.9, 1.6, 2, 2.4] kg/s（默认）| 1×*n* 向量
  group: P-B 节流口
- name: Spool position at maximum A-T orifice area
  summary: A-T 节流孔完全打开时的阀芯偏移 -5e-3 m（默认）| 正标量
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
- name: A-T orifice mass flow rate table, mdot(ds,dp)
  summary: 质量流量值数组 [-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91,
    6, 7.7, 9.13] kg/s（默认）| *M*×*N* 矩阵
  group: A-T Orifice
- name: A-T constant orifice area
  summary: 恒定节流口的横截面积 1e-4 m^2（默认）| 正标量
  group: A-T Orifice
- name: A-T constant orifice pressure drop vector
  summary: 恒定节流口的压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T constant orifice volumetric flow rate vector
  summary: 恒定节流口的体积流量值向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: A-T Orifice
- name: A-T constant orifice mass flow rate vector
  summary: 恒定节流口的质量流量向量 [-.9, 1.6, 2, 2.4] kg/s（默认）| 1×*n* 向量
  group: A-T Orifice
- name: Spool position at maximum B-T orifice area
  summary: 完全打开 B-T 节流口的阀芯偏移 5e-3 m（默认）| 正标量
  group: B-T Orifice
- name: B-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: B-T Orifice
- name: B-T maximum orifice area
  summary: 最大节流口开口面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice area vector
  summary: 阀门开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice spool travel vector, ds
  summary: 相对于完全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice pressure drop vector, dp
  summary: 压差值向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice volumetric flow rate table, q(ds,dp)
  summary: 体积流量值数组 [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054,
    .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s（默认）| *M*×*N* 矩阵
  group: B-T Orifice
- name: B-T orifice mass flow rate table, mdot(ds,dp)
  summary: 质量流量值数组 [-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91,
    6, 7.7, 9.13] kg/s（默认）| *M*×*N* 矩阵
  group: B-T Orifice
- name: B-T constant orifice area
  summary: 恒定节流孔的横截面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T constant orifice pressure drop vector
  summary: 恒定节流孔的压差向量 [-.1, .3, .5, .7] MPa（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T constant volumetric flow rate vector
  summary: 恒定节流孔的体积流量向量 [-.0009, .0016, .002, .0024] m^3/s（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T constant orifice mass flow rate vector
  summary: 恒定节流孔的质量流量向量 [-.9, 1.6, 2, 2.4] kg/s（默认）| 1×*n* 向量
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

是否对阀节流口面积应用统一或单独的流量方程。当您将此参数设置为 `所有流路相同` 时，模块对所有阀节流口使用相同的节流口和阀芯几何参数、流量、压力和面积向量。当您将此参数设置为 `每条流路不同` 时，您可以为每个节流口单独指定这些参数。对于这两种设置，当您将 **节流口参数化** 设置为 `线性 - 面积 vs. 阀芯行程` 或 `表格数据 - 面积 vs. 阀芯行程` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **节流口参数化** — 计算开启面积的方法 `线性面积 vs. 阀芯行程`（默认）| `表格数据 - 面积 vs. 阀芯行程` | `表格数据 - 体积流量 vs. 阀芯行程和压降` | `表格数据 - 质量流量 vs. 阀芯行程和压降`

计算阀开启面积的方法。如果您将此参数设置为表格数据参数化之一，您可以提供自己的阀面积和阀芯行程数据以用于非线性阀开启曲线，或者提供流路流量、阀芯行程和压降形式的数据。

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

根据表格体积流量数据参数化节流口时的阀芯行程距离向量。阀芯行程向量与 **压降向量，dp** 参数构成独立轴，用于二维因变量 **体积流量表，q(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降` 或 `表格数据 - 质量流量 vs. 阀芯行程和压降`。

### **压降向量，dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

根据表格流量数据参数化节流口时的压降值向量。压降向量与 **阀芯行程向量，ds** 参数构成独立轴，用于二维因变量 **体积流量表，q(ds,dp)** 参数。按升序列出值。值必须大于 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降` 或 `表格数据 - 质量流量 vs. 阀芯行程和压降`。

### **体积流量表，q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **阀芯行程向量，ds** 参数中向量元素的数量。
- *N* 是 **压降向量，dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 体积流量 vs. 阀芯行程和压降`。

### **质量流量表，mdot(ds,dp)** — 质量流量数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。

### **Reference inflow temperature** — 指定质量流量数据时的温度 `293.15 K`（默认）| 正标量

指定表格化质量流量数据时的温度。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。

### **Reference inflow pressure** — 指定表格化质量流量数据时的压力 `0.101325 MPa`（默认）| 正标量

指定表格化质量流量数据时的压力。该模块使用此参数计算第三个参考参数，即参考密度，模块使用该参考密度来缩放表格化压降数据，以适应偏离参考条件的压力和温度。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。

### **Constant orifice area** — 相同流路的节流孔面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

在 **Valve Configuration** 部分中为以下两个参数选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流孔时，阀门上的压差向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。模块在表格数据点之间使用线性插值。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - 体积流量与阀芯行程和压降的关系`。

在 **Valve Configuration** 部分中为以下两个参数选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流孔时，恒定节流孔的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。模块在表格数据点之间使用线性插值。

#### 依赖

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - 体积流量与阀芯行程和压降的关系`。

在 **Valve Configuration** 部分中为以下两个参数选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀门的质量流量的压力-流量方程中使用该面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流孔的层流的上限雷诺数。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀门处于接近打开和接近关闭位置时，基于流量响应引入一层逐渐变化。为了提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A Orifice

### **Spool position at maximum P-A orifice area** — 完全打开 P-A 节流孔时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 P-A 节流孔时阀芯从中位开始的偏移。

#### 依赖

要启用此参数，请设置以下参数之一。

将 **Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

将 **Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值提供计算的上限，使仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-A 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Linear - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice spool travel vector** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-A orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **P-A spool travel vector** 参数中的元素一一对应。元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice spool travel vector, ds** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-A orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 和 **P-A orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - 体积流量与阀芯行程和压降的关系`或`Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice pressure drop vector, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-A orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 和 **P-A orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出值。元素必须大于 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - 体积流量与阀芯行程和压降的关系`或`Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - 体积流量与阀芯行程和压降的关系`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为`Different for each flow path`。
2. **节流口参数化**为`Tabulated data - 质量流量与阀芯行程和压力的关系 drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为以下任一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在**正阀芯位置开启连接**和**负阀芯位置开启连接**参数中时，此参数才启用。

### **P-A constant orifice pressure drop vector** — 恒定节流口的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正阀芯位置和负阀芯位置包含相同节流口时，阀门上的压差值向量。向量元素与 **P-A constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在**正阀芯位置开启连接**和**负阀芯位置开启连接**参数中时，此参数才启用。

### **P-A constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正阀芯位置和负阀芯位置包含相同节流口时，阀门上的压差值向量。向量元素与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在**正阀芯位置开启连接**和**负阀芯位置开启连接**参数中时，此参数才启用。

### **P-A constant orifice mass flow rate vector** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正阀芯位置和负阀芯位置使用相同节流口时，阀门上的质量流量值向量。向量元素与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在**正阀芯位置开启连接**和**负阀芯位置开启连接**参数中时，此参数才启用。

### P-B 节流口

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 节流口时的阀芯偏移 `-5e-3`（默认）| 正标量

完全打开 P-B 节流口时阀芯从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接**为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**负阀芯位置开启连接**为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置未同时出现在**正阀芯位置开启连接**和**负阀芯位置开启连接**参数中时，此参数才启用。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将**负阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流口的最大开度面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格参数化的阀芯行程距离向量。向量元素必须与 **P-B orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为 `Different for
   each flow path`。
2. **节流口参数化**为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice area vector** — 阀门开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开度面积向量。向量元素必须与 **P-B spool travel vector** 参数中的元素一一对应。按升序列出元素。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-B orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-B orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **P-B orifice volumetric flow rate table, q(ds,dp)** 和 **P-B orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

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

### **P-B orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-B orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **P-B orifice volumetric flow rate table, q(ds,dp)** 和 **P-B orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

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

### **P-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **P-B orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

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

### **P-B orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **P-B orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

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

### **P-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
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

仅当 P-B 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才会启用。

### **P-B constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流口时，阀门上的压差值向量。向量元素与 **P-B constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
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

仅当 P-B 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才会启用。

### **P-B constant volumetric flow rate vector** — 恒定节流孔的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正负阀芯位置包含相同节流孔时，通过阀门的体积流量值向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 在每个参数中设置以下之一：

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

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才会启用。

### **P-B constant orifice mass flow rate vector** — 恒定节流孔的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正负阀芯位置使用相同节流孔时，通过阀门的质量流量值向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 在每个参数中设置以下之一：

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

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才会启用。

### A-T Orifice

### **Spool position at maximum A-T orifice area** — A-T 节流孔完全打开时的阀芯偏移 `-5e-3 m`（默认）| 正标量

A-T 节流孔完全打开时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
  B-T`。

**注意：**

仅当 A-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才会启用。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-T orifice pressure drop vector, dp** 参数一起构成二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 和 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数的独立轴。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T orifice spool travel vector, ds** 参数共同构成独立轴，用于二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 和 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出这些值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 体积流量矩阵。*M*
和 *N* 是相关向量的大小：

- *M* 是 **A-T
  orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **A-T
  orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 质量流量矩阵。*M*
和 *N* 是相关向量的大小：

- *M* 是 **A-T
  orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **A-T
  orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正滑阀位置和负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，才会启用此参数。

### **A-T constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正滑阀位置和负滑阀位置包含相同节流口时，阀门上的压差值向量。向量元素与 **A-T constant orifice volumetric flow
rate vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，才会启用此参数。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正滑阀位置和负滑阀位置包含相同节流口时的体积流量值向量。向量元素与 **A-T constant orifice pressure drop vector**
参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，才会启用此参数。

### **A-T constant orifice mass flow rate vector** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正滑阀位置和负滑阀位置使用相同节流口时，阀门上的质量流量值向量。向量元素与 **P-B constant orifice pressure drop vector**
参数中的元素一一对应。按升序列出这些值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，才会启用此参数。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流口的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 B-T 节流口时阀芯从中位开始的偏移。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

- **Positive spool position open connections** 设置为
  `P-A, B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open connections** 设置为
  `P-A, B-T` 或 `P-A, P-B, A-T,
  B-T`。

**注意：**

仅当 B-T 节流口设置未同时出现在 **Positive spool position open
connections** 和 **Negative spool position open
connections** 参数中时，此参数才会启用。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作过程中 B-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **B-T
orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的开口面积向量。向量元素必须与 **B-T
orifice spool travel vector** 参数中的元素一一对应。元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。阀芯行程向量与
**B-T orifice pressure drop vector, dp** 参数一起构成二维因变量
**B-T orifice volumetric flow rate table, q(ds,dp)** 和
**B-T orifice mass flow rate table, mdot(ds,dp)**
参数的独立轴。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **B-T
orifice spool travel vector, ds** 参数一起构成二维因变量
**B-T orifice volumetric flow rate table, q(ds,dp)** 和 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数的独立轴。
按升序列出这些值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M*
和 *N* 是相关向量的大小：

- *M* 是 **B-T
  orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **B-T
  orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M*
和 *N* 是相关向量的大小：

- *M* 是 **B-T
  orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **B-T
  orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 以下参数之一：

   - **Positive spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认）| 正标量

当正和负滑阀位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，此参数才启用。

### **B-T constant orifice pressure drop vector** — 恒定节流孔的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正和负滑阀位置包含相同节流孔时，阀门上的压差值向量。向量元素与 **B-T constant orifice volumetric flow
rate vector** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压降的关系`
   或 `Tabulated data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，此参数才启用。

### **B-T constant volumetric flow rate vector** — 恒定节流孔的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正和负滑阀位置包含相同节流孔时，阀门上的压差值向量。向量元素与 **B-T constant orifice pressure drop
vector** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 体积流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，此参数才启用。

### **B-T constant orifice mass flow rate vector** — 恒定节流孔的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正和负滑阀位置使用相同节流孔时，阀门上的质量流量值向量。向量元素与 **P-B constant orifice pressure drop vector**
参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for
   each flow path`。
2. **Orifice parameterization** 为 `Tabulated
   data - 质量流量与阀芯行程和压力的关系
   drop`。
3. 每个参数中的以下设置之一：

   - **Positive spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在 **Positive spool position open connections** 和
**Negative spool position open connections**
参数中时，此参数才启用。

### 故障

### **4-Way 2-Position Directional Valve Area fault** — 用于对阀门面积故障建模的选项 `Add fault`

用于在该模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，通常由开口参数化设置的阀门面积将根据 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障时的阀门特性 `Positive`（默认）| `Negative` | `Maintain last value`

故障时的阀门滑阀位置。您可以选择当滑阀处于正位置、负位置或故障触发时的位置时阀门卡滞。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

4-Way 2-Position Directional Valve (TL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块以查看开口特性图

您可以通过右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个节流孔的面积或体积流量相对于滑阀位置的图。

## 描述

热液网络中的四通两位方向阀

四通两位方向阀 (TL) 用于对热液网络中具有四个开口的阀进行建模——例如执行器、泵与油箱之间的阀。单个阀芯根据端口 **S** 处的信号控制阀的操作。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定阀芯向正方向和负方向移动时打开的节流口，来设置阀的基线配置。您可以在 **Orifice parameterization** 参数中将阀开口模型设置为线性关系或用户提供数据的函数，并可将其应用于阀中的一个或所有流路。

该模块是一个复合组件，由多个 Orifice (TL) 模块实例组成。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (TL) 模块。在某些配置中，该阀类似于三通阀。要在阀芯处于中位时设置额外的流路，请参阅 4-Way 3-Position Directional Valve (TL) 模块。

下图展示了一个阀设置示例，其中阀连接到油箱、执行器和泵，且 **Positive spool position open connections** 参数为 `P-B, A-T`：

下图展示了 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀：

在此配置中，当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开以允许流动。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭以阻止流动。

下图展示了 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀：

在此配置中，当端口 **S** 处的信号使阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开以允许流动，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭。

表示此配置的原理图如下：

左侧对应正位置，右侧对应负位置。阀通过中间中性区段中的位置进行切换。

### 阀芯位移与阀配置

*阀芯行程*是指节流口从关闭位置到完全打开所需的阀芯移动量。您可以使用 **Orifice parameterization** 和 **Area characteristics** 参数来指定流路特性：

| 节流口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义阀芯行程 | **Spool travel between closed and open orifice** 参数为每个节流口定义阀芯行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数第一个和最后一个元素之间的差值定义阀芯行程 | 每个节流口的 **Spool travel vector** 参数第一个和最后一个元素之间的差值定义阀芯行程 |
| `Tabulated data - 体积流量与阀芯行程和压降的关系` 或 `Tabulated data - 质量流量与阀芯行程和压力的关系 drop` | **Spool travel vector, ds** 参数第一个和最后一个元素之间的差值定义阀芯行程 | 每个节流口的 **Spool travel vector, ds** 参数第一个和最后一个元素之间的差值定义阀芯行程 |

阀芯移动方向取决于阀芯行程、节流口方向和端口 **S** 处的信号。下表显示了节流口的阀芯移动量，取决于 **Positive spool position open connection** 和 **Negative spool position open connection** 参数的选择：

| 节流口打开时的阀芯位置 | 阀芯移动量，*ΔS* |
| --- | --- |
| 节流口始终关闭：节流口未被选入 **Positive spool position open connection** 或 **Negative spool position open connection** 参数 | 不适用 |
| 节流口始终打开：节流口同时被选入 **Positive spool position open connection** 和 **Negative spool position open connection** 参数 | 不适用 |
| 负：节流口仅被选入 **Negative spool position open connection** 参数 | *S*orifice\_max + 阀芯行程 – **S** |
| 正：节流口仅被选入 **Positive spool position open connection** 参数 | *S*orifice\_max – 阀芯行程 + **S** |

其中 *S*orifice\_max 是为每个节流口定义的最大节流口面积处的阀芯位置。当 *ΔS* 为负时，节流口面积饱和于泄漏面积；当节流口完全打开时，节流口面积饱和于最大节流口面积。当节流口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增大节流口面积。

下表显示了 4-Way 2-Position Directional Valve (TL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四条路径均关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间所有四条路径均打开。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** < B-T 阀芯行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open connections**：`P-A` - **Negative spool position open connections**：`P-B` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice area** < –B-T 阀芯行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** > –P-A 阀芯行程 - **Spool position at maximum A-T orifice area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum B-T orifice area** < –B-T 阀芯行程 |
| 过渡期间所有路径均关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > –A-T 阀芯行程 |

### 阀门节流口参数化

**节流口参数化**参数指定一个或所有阀门节流口的开口面积或流量的模型。如果将**面积特性**设置为`所有流路相同`，则模块对所有流路应用相同的数据。当选择`所有流路不同`时，模块对每个流路使用各自的参数化。

当**节流口参数化**为`线性 - 面积与阀芯行程的关系`时，开口面积是作为端口 **S** 处信号接收的阀芯位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中：

- *ΔS* 是阀芯行程。

  *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，在节流口完全打开时饱和于 *Amax*。当节流口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程的值不会增加节流口面积。
- *ΔSmax* 是**节流口关闭与打开之间的阀芯行程**参数的值。
- *Amax* 是**最大节流口面积**参数的值。
- *Aleak* 是**泄漏面积**参数的值。

  当阀门在线性参数化中处于接近打开或接近关闭的位置时，可以通过调整**平滑因子**参数来保持仿真中的数值鲁棒性。如果**平滑因子**参数非零，模块将在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。

当**节流口参数化**为`表格数据 - 面积与阀芯行程的关系`时，可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各个流路提供阀芯行程向量。模块使用此数据计算节流口面积与阀芯位移之间的关系。模块使用插值确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。

当**节流口参数化**为`表格数据 - 体积流量与阀芯行程和压降的关系`时，可以提供阀芯行程和压降向量以及相关的二维体积流量数组。模块使用插值确定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

当**节流口参数化**为`表格数据 - 质量流量与阀芯行程和压降的关系`时，可以提供阀芯行程和压降向量以及相关的二维质量流量数组。模块使用插值确定数据点之间的流量。模块根据**阀芯行程向量，ds**、**压降向量，dp**和**质量流量表，mdot(ds,dp)**参数中的表格数据计算这三个变量之间的关系。

### 可视化节流口开口

要可视化阀芯偏移和最大位移，请右键单击模块并选择**流体** > **绘制阀门特性**。该图显示由**阀门配置**部分中的参数指定的节流口。坐标轴为以下之一：

- 节流口面积与阀芯位置的关系
- 体积流量与阀芯位置的关系，在特定压差下查询

当将**阀门配置**选项卡中的参数设置为同一声节流口时，节流口开口为常数。

单击**重新加载数据**以更新图中的数据。

此图显示了模块的默认配置：

- **正阀芯位置打开的连接**为`P-A, B-T`。
- **负阀芯位置打开的连接**为`P-B, A-T`。

所有其他阀芯位置均为默认值。

### 故障

要对故障建模，请在**故障**部分中，单击要建模的故障旁边的**添加故障**超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**故障时的阀芯位置**参数有三个故障选项：

- `正` — 阀芯位置冻结在正位置，将**正阀芯位置打开的连接**参数指定的流路打开至其最大值。**负阀芯位置打开的连接**参数指定的流路关闭。
- `负` — 阀芯位置冻结在负位置，将**负阀芯位置打开的连接**参数指定的流路打开至其最大值。**正阀芯位置打开的连接**参数指定的流路关闭。
- `保持最后的值` — 阀门在触发发生时冻结在阀芯位置。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于**泄漏面积**，最大面积小于**最大节流口面积**，其比例与**平滑因子**值成正比。有关详细信息，请参阅数值平滑。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 预定义参数化

可以使用预参数化的制造数据填充模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，单击**选定部件**旁边的“<单击以选择>”超链接，该链接位于模块对话框设置的**选定部件**旁边。
2. 将打开“模块参数化管理器”窗口。从菜单中选择一个部件，然后单击**全部应用**。可以使用**制造商**下拉菜单缩小选择范围。
3. 可以关闭**模块参数化管理器**菜单。模块现在具有指定的参数化。
4. 可以通过在“模块参数化管理器”窗口中选择一个部件并查看**比较选定部件与模块**部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源提供参数值。模块对缺失数据使用工程判断和简化假设进行替代。因此，仿真行为与实际物理行为之间可能会出现一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

要了解更多信息，请参阅预参数化组件列表。
