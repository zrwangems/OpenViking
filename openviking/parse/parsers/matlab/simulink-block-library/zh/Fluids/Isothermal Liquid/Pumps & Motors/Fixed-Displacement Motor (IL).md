---
type: simulink-block
title: 'Fixed-Displacement Motor (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementmotoril'
documentation_source_path: 'ref/fixeddisplacementmotoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Displacement Motor (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: R
  summary: 机械端口，机械旋转
  direction: conserving
- name: C
  summary: 机械端口，机械旋转
  direction: conserving
- name: EV
  summary: 容积效率，物理信号
  direction: input
- name: EM
  summary: 机械效率，物理信号
  direction: input
- name: LV
  summary: 泄漏流量，m^3/s，物理信号
  direction: input
- name: LM
  summary: 摩擦力矩，N*m，物理信号
  direction: input
```

### 守恒端口

### **A** — 液体端口，等温液体

电机的入口或出口端口。

### **B** — 液体端口，等温液体

电机的入口或出口端口。

### **R** — 机械端口，机械旋转

旋转轴的角速度和扭矩。

### **C** — 机械端口，机械旋转

电机壳体的参考角速度和扭矩。
### 输入

### **EV** — 容积效率，物理信号

用于流体排量的电机效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **EM** — 机械效率，物理信号

用于机械能量提取的电机效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **LV** — 泄漏流量，`m^3/s`，物理信号

与流体排量相关的电机损失，单位为 m^3/s，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 losses`。

### **LM** — 摩擦力矩，`N*m`，物理信号

与机械能量提取相关的电机损失，单位为 N\*m，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 losses`。
## 参数
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: 泄漏流量和摩擦力矩的计算方法 Analytical（默认）| Tabulated data - volumetric and mechanical efficiencies | Tabulated data - volumetric
    and mechanical losses | Tabulated data - torque and speed | 输入信号 - 体积和机械 efficiencies | 输入信号 - 体积和机械 losses
  group: 参数
- name: Displacement
  summary: 固定体积流体排量 30 cm^3/rev（默认）| 标量
  group: 参数
- name: Nominal shaft angular velocity
  summary: 轴角速度 1800 rpm（默认）| 标量
  group: 参数
- name: Nominal pressure drop
  summary: 流体入口和出口之间的压降 10 MPa（默认）| 标量
  group: 参数
- name: Volumetric efficiency at nominal conditions
  summary: 额定工况下实际流量与理想流量的比值 0.92（默认）| 正标量
  group: 参数
- name: No-load torque
  summary: 基线扭矩 0 N*m（默认）| 标量
  group: 参数
- name: Mechanical efficiency at nominal conditions
  summary: 额定工况下实际扭矩与理想生成扭矩的比值 0.88（默认）| 正标量
  group: 参数
- name: Pressure drop vector, dp
  summary: 表格数据参数化的压力数据向量 [.1, 1, 2] MPa（默认）| 1×*n* 向量
  group: 参数
- name: Shaft angular velocity vector, w
  summary: 表格数据参数化的角速度数据向量 [250, 500, 1000, 2000, 3000, 4000] rpm（默认）| 1×*n* 向量
  group: 参数
- name: Flow rate vector, q
  summary: 流量数据向量 [.125, .25, .5, 1, 1.5, 2] * 1e-3 m^3/s（默认）| 1×*n* 向量
  group: 参数
- name: Volumetric efficiency table, e_v(dp,w)
  summary: 表格数据参数化的容积效率 [.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893,
    .91]（默认）| *M*×*N* 矩阵
  group: 参数
- name: Mechanical efficiency table, e_m(dp,w)
  summary: 表格数据参数化的机械效率 [.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983,
    .984]（默认）| *M*×*N* 矩阵
  group: 参数
- name: Volumetric loss table, q_loss(dp,w)
  summary: 表格数据参数化的容积损失 [.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108,
    .1605, .18] * 1e-3 m^3/s（默认）| *M*×*N* 矩阵
  group: 参数
- name: Mechanical loss table, torque_loss(dp,w)
  summary: 表格数据参数化的机械损失 [.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833,
    .1833, .1729, .1626] N*m（默认）| *M*×*N* 矩阵
  group: 参数
- name: Torque table, T(q,dp)
  summary: 表格数据参数化的扭矩值 [.47, 4.72, 9.35; .47, 4.7, 9.36; .47, 4.7, 9.4; .47, 4.7, 9.41; .47, 4.7, 9.46; .47, 4.68, 9.5] N*m（默认）|
    *M*×*N* 矩阵
  group: 参数
- name: Shaft speed table, w(q,dp)
  summary: 表格数据参数化的轴转速 [205, 80, 35; 455, 330, 285; 955, 831, 780; 1950, 1830, 1780; 2940, 2775, 2680; 3940, 3780, 3640] rpm（默认）|
    *M*×*N* 矩阵
  group: 参数
- name: Minimum volumetric efficiency
  summary: 容积效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: 参数
- name: Maximum volumetric efficiency
  summary: 容积效率的最大值 1（默认）| 正标量
  group: 参数
- name: Minimum mechanical efficiency
  summary: 机械效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: 参数
- name: Maximum mechanical efficiency
  summary: 机械效率的最大值 1（默认）| (0,1] 范围内的正标量
  group: 参数
- name: Pressure drop threshold for motor-pump transition
  summary: 模式转换的压力阈值 1e-3 MPa（默认）| 正标量
  group: 参数
- name: Angular velocity threshold for motor-pump transition
  summary: 模式转换的角速度阈值 100 rpm（默认）| 正标量
  group: 参数
- name: 检查是否超出所提供表格数据的范围
  summary: 是否在超出所提供数据范围时发出通知 None（默认）| Warning | Error
  group: 参数
- name: 检查是否在电机模式之外运行
  summary: 是否在模块于电机模式功能之外运行时发出通知 None（默认）| Warning | Error
  group: 参数
- name: 检查压力是否低于电机最低压力
  summary: 是否在流体出口压力过低时发出通知 None（默认）| Warning | Error
  group: 参数
- name: 电机最低压力
  summary: 电机出口可接受压力的下限阈值 0.101325 MPa（默认）| 正标量
  group: 参数
- name: 排量故障
  summary: 用于对排量故障建模的选项 Add fault
  group: 故障
- name: 故障排量系数
  summary: 用于缩放故障排量的系数 0.5（默认）| 正标量
  group: 故障
- name: 泄漏故障
  summary: 用于对泄漏故障建模的选项 Add fault
  group: 故障
- name: 故障泄漏系数
  summary: 用于缩放泄漏故障的系数 2.0（默认）| 正标量
  group: 故障
- name: 轴摩擦扭矩故障
  summary: 用于对轴摩擦扭矩故障建模的选项 Add fault
  group: 故障
- name: 故障轴摩擦扭矩系数
  summary: 用于缩放轴摩擦扭矩故障的系数 2.0（默认）| 正标量
  group: 故障
```

### 参数

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的计算方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Tabulated data - torque and speed` | `输入信号 - 体积和机械 efficiencies` | `输入信号 - 体积和机械 losses`

泵的泄漏和摩擦特性的参数化方法。

- 在 `Analytical` 参数化中，泄漏流量和摩擦力矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **Pressure drop vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维依赖的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和扭矩摩擦根据用户提供的 **Pressure drop vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维依赖的 **Volumetric loss table, q\_loss(dp,w)** 和 **Mechanical loss table, torque\_loss(dp,w)** 表中插值得到。
- 在 `Tabulated data - torque and speed` 参数化中，您可以通过 **Torque table T(q,dp)** 和 **Shaft speed table w(q,dp)** 参数输入扭矩和轴转速作为流量和压降的函数。
- 在 `输入信号 - 体积和机械 efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 接收。
- 在 `输入信号 - 体积和机械 loss` 参数化中，泄漏流量和扭矩摩擦分别作为物理信号在端口 **LV** 和 **LM** 接收。

### **Displacement** — 固定体积流体排量 `30 cm^3/rev`（默认）| 标量

固定体积流体排量的大小。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| 标量

额定工况下轴的角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 流体入口和出口之间的压降 `10 MPa`（默认）| 标量

额定工况下电机流体入口和出口之间的压降。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 额定工况下实际流量与理想流量的比值 `0.92`（默认）| 正标量

额定工况下实际流量与理想流量的比值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 额定工况下实际扭矩与理想生成扭矩的比值 `0.88`（默认）| 正标量

额定工况下实际扭矩与理想生成扭矩的比值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的压差数值向量。该向量与 **Shaft angular velocity vector, w** 参数或 **Flow rate vector, q** 参数构成独立轴，用于三维依赖的 **Volumetric efficiency table, e\_v(dp,w)**、**Mechanical efficiency table, e\_m(dp,w)**、**Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和 mechanical efficiencies`
- `表格数据 - 体积和 mechanical losses`
- `表格数据 - 扭矩和 speed`

### **Shaft angular velocity vector, w** — 表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的角速度数据向量。该向量与 **Shaft angular velocity vector, w** 参数构成独立轴，用于三维依赖的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和 mechanical efficiencies`
- `表格数据 - 体积和 mechanical losses`

### **Flow rate vector, q** — 流量数据向量 `[.125, .25, .5, 1, 1.5, 2] * 1e-3 m^3/s`（默认）| 1×*n* 向量

用于扭矩和转速表格参数化的流量数据向量。该向量与 **Pressure drop vector, dp** 参数构成独立轴，用于三维依赖的 **Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Volumetric efficiency table, e\_v(dp,w)** — 表格数据参数化的容积效率 `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]`（默认）| *M*×*N* 矩阵

在指定流体压降和轴角速度下的 *M*×*N* 容积效率矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w)** — 表格数据参数化的机械效率 `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]`（默认）| *M*×*N* 矩阵

在指定流体压降和轴角速度下的 *M*×*N* 机械效率矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w)** — 表格数据参数化的容积损失 `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s`（默认）| *M*×*N* 矩阵

在指定流体压降和轴角速度下的 *M*×*N* 容积效率矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w)** — 表格数据参数化的机械损失 `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m`（默认）| *M*×*N* 矩阵

在指定流体压降和轴角速度下的 *M*×*N* 机械损失矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Torque table, T(q,dp)** — 表格数据参数化的扭矩值 `[.47, 4.72, 9.35; .47, 4.7, 9.36; .47, 4.7, 9.4; .47, 4.7, 9.41; .47, 4.7, 9.46; .47, 4.68, 9.5] N*m`（默认）| *M*×*N* 矩阵

在指定流体压降和流量下的 *M*×*N* 扭矩值矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中元素的个数。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的个数。

如果您的表在四个角中的任何位置有未知数据点，请使用 `NaN` 代替这些值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Shaft speed table, w(q,dp)** — 表格数据参数化的轴转速 `[205, 80, 35; 455, 330, 285; 955, 831, 780; 1950, 1830, 1780; 2940, 2775, 2680; 3940, 3780, 3640] rpm`（默认）| *M*×*N* 矩阵

在指定流体压降和流量下的 *M*×*N* 轴转速值矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中元素的个数。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的个数。

如果您的表在四个角中的任何位置有未知数据点，请使用 `NaN` 代替这些值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| 正标量

容积效率的最大值。如果输入信号高于此值，则容积效率设置为最大容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

机械效率的最小值。如果输入信号低于此值，则机械效率设置为最小机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1`（默认）| (0,1] 范围内的正标量

机械效率的最大值。如果输入信号高于此值，则机械效率设置为最大机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `输入信号 - 体积和机械 efficiencies`。

### **Pressure drop threshold for motor-pump transition** — 模式转换的压力阈值 `1e-3 MPa`（默认）| 正标量

泵和电机功能之间转换的阈值压降值。在压降阈值的正值和负值之间围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算出的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和 mechanical efficiencies`
- `输入信号 - 体积和机械 efficiencies`
- `输入信号 - 体积和机械 losses`

### **Angular velocity threshold for motor-pump transition** — 模式转换的角速度阈值 `100 rpm`（默认）| 正标量

泵和电机功能之间转换的阈值角速度值。在角速度阈值的正值和负值之间围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算出的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和 mechanical efficiencies`
- `输入信号 - 体积和机械 efficiencies`
- `输入信号 - 体积和机械 losses`

### **检查是否超出所提供表格数据的范围** — 是否在超出所提供数据范围时发出通知 `None`（默认）| `Warning` | `Error`

是否在超出所提供数据范围时发出通知。
选择 `Warning`，当模块使用超出所提供数据范围的值时发出通知。选择
`Error`，当模块使用超出所提供数据范围的值时停止仿真。

当 **Leakage and friction parameterization** 设置为
`Tabulated data - torque and speed` 时，此参数还会检查模块是否在所提供的
`NaN` 值区域内运行。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `表格数据 - 体积和
  mechanical efficiencies`
- `表格数据 - 体积和
  mechanical losses`
- `表格数据 - 扭矩和
  speed`

### **检查是否在电机模式之外运行** — 是否在模块于电机模式功能之外运行时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块于电机模式功能之外运行时发出通知。此模块有四种运行模式：正向电机、
反向电机、反向泵和正向泵。选择
`Warning`，当模块在正向或反向电机泵模式下运行时发出通知。选择
`Error`，当模块在正向或反向泵模式下运行时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **检查压力是否低于电机最低压力** — 是否在流体出口压力过低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 或
**B** 处的流体经历低压时发出通知。选择
`Warning`，当出口压力降至指定的最低值以下时发出通知。选择
`Error`，当出口压力降至指定的最低值以下时停止仿真。

当流体压力降至流体蒸气压以下时，此参数有助于识别可能发生气蚀的条件。

### **电机最低压力** — 电机出口可接受压力的下限阈值 `0.101325 MPa`（默认）| 正标量

电机入口或出口可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **Check if pressures are
less than motor minimum pressure** 设置为以下任一值：

- `Warning`
- `Error`

### 故障

### **排量故障** — 用于对排量故障建模的选项 `Add fault`

用于对模块中的排量故障建模的选项。发生故障时，排量按 **Faulted displacement
factor** 参数的值进行缩放。要添加故障，请点击 **Add
fault** 超链接。

### **故障排量系数** — 用于缩放故障排量的系数 `0.5`（默认）| 正标量

模块在发生故障时用于缩放排量的系数。

#### 依赖关系

要启用此参数，请点击 **Displacement fault** 参数的 **Add fault**
超链接。

### **泄漏故障** — 用于对泄漏故障建模的选项 `Add fault`

用于对模块中的泄漏故障建模的选项。发生故障时，容积效率或损失按 **Faulted
leakage factor** 参数的值进行缩放。要添加故障，请点击 **Add
fault** 超链接。

### **故障泄漏系数** — 用于缩放泄漏故障的系数 `2.0`（默认）| 正标量

模块在发生故障时用于缩放容积效率或损失的系数。

#### 依赖关系

要启用此参数，请点击 **Leakage fault** 参数的 **Add fault**
超链接。

### **轴摩擦扭矩故障** — 用于对轴摩擦扭矩故障建模的选项 `Add fault`

用于对模块中的轴摩擦扭矩故障建模的选项。发生故障时，机械效率或损失按
**Faulted shaft friction torque factor** 参数的值进行缩放。要添加
故障，请点击 **Add fault** 超链接。

### **故障轴摩擦扭矩系数** — 用于缩放轴摩擦扭矩故障的系数 `2.0`（默认）| 正标量

模块在发生故障时用于缩放机械效率或损失的系数。

#### 依赖关系

要启用此参数，请点击 **Shaft friction torque fault**
参数的 **Add fault** 超链接。
## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

Fixed-Displacement Motor (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024a：使用扭矩和轴转速对模块进行参数化

现在，您可以通过将 **Leakage and friction parameterization** 参数设置为
`Tabulated data - torque and speed` 来指定扭矩和轴转速，从而对模块进行参数化。制造商
通常以这种格式提供电机数据表。

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the quadrants of supplied tabulated
data** 参数已重命名为 **Check if operating
beyond the range of supplied tabulated data**。您可以启用
**Check if operating beyond the range of supplied tabulated
data** 参数，以检查模块是否在模块参数中指定的数据范围之外运行，即在模块
已扩展数据的区域内运行。

## 描述

等温液体系统中的固定排量电机

Fixed-Displacement Motor (IL) 模块对具有恒定容积排量的电机进行建模。流体可以从端口 **A** 流向端口
**B**，称为*正向模式*，或从端口
**B** 流向端口 **A**，称为*反向
模式*。当沿流动方向存在压降时，发生电机模式运行。当沿流动方向存在压力增益时，
发生泵模式运行。

轴旋转对应于通过电机的流体体积的符号。
正向模式下，正流体排量对应于正轴旋转。
正向模式下，负流体排量对应于负轴角速度。

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B**
的压降，*Δp = p*A –
*p*B 以及角速度，*ω =
ω*R – *ω*C：

- 模式 1，*正向电机*：流体从端口
  **A** 流向端口 **B** 导致从 **A** 到 **B**
  的压力降低以及正轴角速度。
- 模式 2，*反向泵*：负轴角速度
  导致从端口 **B** 到端口
  **A** 的压力升高以及流体从 **B** 流向端口
  **A**。
- 模式 3，*反向电机*：流体从端口
  **B** 流向端口 **A** 导致从 **B** 到 **A**
  的压力降低以及负轴角速度。
- 模式 4，*正向泵*：正轴角速度
  导致从端口 **A** 到端口
  **B** 的压力升高以及流体从 **A** 流向
  **B**。

电机模块具有解析、查找表和物理信号参数化。当使用表格数据或输入信号进行参数化时，您可以选择
基于效率或损失来表征电机运行。

在表格数据和输入信号参数化选项中，阈值参数 **Pressure drop threshold for motor-pump transition** 和
**Angular velocity threshold for motor-pump transition** 标识了电机运行模式之间可进行数值平滑流动过渡的
区域。请选择一个为过渡项提供一定裕度的过渡区域，
但该区域相对于压力和角速度要足够小，以免影响计算结果。

### 解析泄漏和摩擦参数化

如果将 **Leakage and friction parameterization** 设置为
`Analytical`，模块将根据轴速度、压降和摩擦扭矩的恒定值计算泄漏和摩擦。与电机上的压差相关的
泄漏流量计算如下：

m˙leak=KρavgΔp，

其中：

- *Δp* 为 *p*A
  – *p*B。
- *ρ*avg 为平均流体
  密度。
- *K* 为解析损失的 Hagen-Poiseuille 系数，

  K=Dωnom(1ηv,nom−1)Δpnom，

  其中：

  - *D* 为
    **Displacement** 参数的值。
  - *ωnom* 为
    **Nominal shaft angular
    velocity** 参数的值。
  - *ηv, nom* 为
    **Volumetric efficiency at nominal
    conditions** 参数的值。
- *Δpnom* 为
  **Nominal pressure drop** 参数的值。

与轴角速度相关的摩擦扭矩计算如下：

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom)，

其中：

- *τ*0 为
  **No-load torque** 参数的值。
- *k* 为额定排量下的摩擦扭矩与压力增益
  系数，由 **Mechanical efficiency at nominal
  conditions** 参数的值
  *ηm* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfric* 为
  额定条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nom)DΔpnom。
- *Δp* 为端口
  **A** 和 **B** 之间的压降。
- *ω* 为相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示电机效率或损失时，您可以为一种或多种电机运行模式提供数据。表格数据的符号
决定模块的运行区域。当提供的运行模式数据少于四种时，模块通过将给定数据扩展到其余象限来计算
其他模式的补充数据。

**表格数据 - 容积和机械效率参数化**

泄漏流量为

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2)，

其中：

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

且 *ηv* 为容积效率，
由用户提供的表格数据插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)，

其中：

- *Δp* 为
  *p*A –
  *p*B。
- *p*threshold 为
  **Pressure drop threshold for motor-pump
  transition** 参数的值。
- *ω* 为
  *ω*R –
  *ω*C。
- *ω*threshold 为
  **Angular velocity threshold for motor-pump
  transition** 参数的值。

摩擦扭矩为

τfr=τfr,motor(1+α2)+τfr,pump(1−α2)，

其中：

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

且 *η*m 为
机械效率，由用户提供的表格数据插值得到。

**表格数据 - 容积和机械损失参数化**

泄漏流量为

m˙leak=ρavgqloss(Δp,ω)，

其中 *qloss* 由
**Volumetric loss table, q\_loss(dp,w)** 参数插值得到，该参数
基于用户提供的压降、轴角速度和流体容积排量数据。

轴摩擦扭矩为

τfr=τloss(Δp,ω)tanh(4ωωthreshold)，

其中 *τloss* 由
**Mechanical loss table, torque\_loss(dp,w)** 参数插值得到，
该参数基于用户提供的压降和轴角速度数据。

**表格数据 - 扭矩和转速参数化**

模块计算容积损失表
*qloss,TLU* 和机械
损失表 *τloss,TLU*，如下

qloss,TLU=qTLU−DωTLUτloss,TLU=DΔpTLU−TTLU

其中：

- *qTLU* 为
  **Flow rate vector, q** 参数的值。
- *ωTLU* 为
  **Shaft speed table, w(q,dp)**
  参数的值。
- *ΔpTLU* 为
  **Pressure drop vector, dp** 参数的值。
- *TTLU* 为
  **Torque table, T(q,dp)** 参数的值。

如果 **Shaft speed table, w(q,dp)**
和 **Torque table, T(q,dp)** 参数的提供值未覆盖所有四个
象限，模块通过以下方式扩展数据：

- 对称镜像 **Pressure drop
  vector, dp** 和 **Flow rate vector,
  q** 参数的值以包含负值。
- 对称扩展容积损失表
  *qloss,TLU* 的值到
  其他象限。这些扩展值的符号与每个
  象限中的 *ΔpTLU* 符号一致。
- 根据流量向量和容积损失表的扩展值
  计算轴转速向量
  *ωTLU* 的扩展值，ωTLU=qTLU−qloss,TLUD。
- 对称扩展机械损失表
  *τloss,TLU* 的值到
  其他象限。这些扩展值的符号与每个
  象限中的 *ωTLU* 符号一致。

如果您的数据表在四个角中的任何一个有未知数据点，或者
**Shaft speed table, w(q,dp)** 或 **Torque table,
T(q,dp)** 参数中有未知数据点，请在这些值的位置使用 `NaN`。模块使用相对于压降的最近外推法
填充所得容积损失表和机械损失表中的 `NaN` 元素。模块调整外推机械损失表中的符号，使其与
轴转速向量 *ωTLU* 中对应元素的符号一致，其中 ωTLU=qTLU−qloss,TLUD。

在扩展或填充未知数据后，模块使用线性
插值和最近外推法在仿真期间计算容积和
机械损失表

qloss=tablelookup(qTLU,ΔpTLU,qloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)τloss=tablelookup(qTLU,ΔpTLU,τloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)

其中 Q=m˙Aρavg。

### 输入信号参数化

当 **Leakage and friction parameterization** 为
`输入信号 - 体积和机械
efficiencies` 时，端口 **EV** 和
**EM** 启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and
mechanical efficiencies` 参数化相同，不同之处在于
*η*v 和
*η*m 分别直接在端口
**EV** 和 **EM** 处接收。

当 **Leakage and friction parameterization** 为
`输入信号 - 体积和机械 losses` 时，
端口 **LV** 和 **LM** 启用。这些端口
以正物理信号的形式接收泄漏流量和摩擦扭矩。泄漏
流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh)，

其中：

- *q*LV 为在端口 **LV**
  处接收的泄漏流量。
- *p*thresh 为
  **Pressure drop threshold for motor-pump
  transition** 参数的值。

摩擦扭矩计算如下：

τfr=τLMtanh(4ωωthresh)，

其中

- *τ*LM 为在端口 **LM**
  处接收的摩擦扭矩。
- *ω*thresh 为
  **Angular velocity threshold for motor-pump
  transition** 参数的值。

容积效率和机械效率在用户定义的
指定最小值和最大值之间。任何低于或高于此范围的值
将分别取指定的最小值和最大值。

### 泵运行

电机流量为：

m˙=m˙ideal+m˙leak，

其中 m˙ideal=ρavgD⋅ω。

电机扭矩为：

τ=τideal−τfr，

其中 τideal=D⋅Δp。

电机轴提取的机械功率为：

φmech=τω，

电机液压功率为：

φhyd=Δpm˙ρavg。

如果您想知道模块是否在所提供的表格数据范围之外运行，可以将 **Check if operating beyond the range
of supplied tabulated data** 设置为 `Warning`，以便在发生这种情况时
收到警告，或设置为 `Error`，以便在发生这种情况时停止
仿真。对于通过容积或机械损失输入信号进行参数化的情况，您可以使用 **Check if operating outside of motor mode**
参数在仿真超出运行模式时收到通知。

您还可以监控电机功能。将 **Check if pressures are
less than motor minimum pressure** 设置为
`Warning`，以便在发生这种情况时收到警告，或设置为
`Error`，以便在发生这种情况时停止仿真。

### 预定义参数化

此模块提供了预参数化的制造商数据。这些数据允许您对特定供应商组件进行建模。

要加载预定义参数化，

1. 在模块对话框描述的“选择一个预定义参数化”超链接处单击。
2. 从下拉菜单中选择一个部件，然后单击 **Update block with selected part**。
3. 如果加载参数化后更改了任何参数设置，可以通过单击 **Compare block settings with selected part** 来检查更改。模块与预定义参数化之间的任何设置差异都将显示在 MATLAB® 命令窗口中。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。该模块用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

您可以对位移故障、泄漏或轴摩擦扭矩故障建模。

当您启用 **Displacement fault** 参数时，当故障触发时，模块会按 **Faulted displacement factor** 参数的值缩放位移，

DFault=fDD，

其中 *fD* 是 **Faulted displacement factor** 参数的值。当 **Leakage and friction parameterization** 参数为 `Analytical` 时，模块不使用故障位移值来计算 Hagen-Poiseuille 系数或摩擦力矩。

当您启用 **Leakage fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `输入信号 - 体积和机械 efficiencies` 时，故障容积效率为

ηv,Fault=ηvfLeak，

其中 *fLeak* 是 **Faulted leakage factor** 参数的值，*ηv* 是容积效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障容积效率来计算 Hagen-Poiseuille 系数。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses`、`输入信号 - 体积和机械 losses` 或 `Tabulated data - torque and speed` 时，故障泄漏体积流量为

qLeak,Fault=fLeakqLeak。

当 **Leakage and friction parameterization** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *qLeak*。

当您启用 **Shaft friction torque fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `输入信号 - 体积和机械 efficiencies` 时，故障机械效率为

ηm,Fault=ηmfFriction，

其中 *fFriction* 是 **Shaft friction torque fault** 参数的值，*ηm* 是机械效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障机械效率来计算摩擦力矩。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses`、`输入信号 - 体积和机械 losses` 或 `Tabulated data - torque and speed` 时，故障摩擦力矩为

τFriction,Fault=fFrictionτFriction。

当 **Leakage and friction parameterization** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *τLeak*。
