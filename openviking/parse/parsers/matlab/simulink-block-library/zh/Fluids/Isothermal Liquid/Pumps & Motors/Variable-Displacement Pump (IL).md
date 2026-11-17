---
type: simulink-block
title: 'Variable-Displacement Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'variabledisplacementpumpil'
documentation_source_path: 'ref/variabledisplacementpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Pump (IL)

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
- name: D
  summary: 容积排量，cm^3/rad，物理信号
  direction: input
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
  summary: 摩擦力矩，N\*m，物理信号
  direction: input
```

### 守恒端口

### **A** — 液体端口，等温液体

泵的液体入口或出口端口。

### **B** — 液体端口，等温液体

泵的液体入口或出口端口。

### **R** — 机械端口，机械旋转

旋转轴的角速度和扭矩。

### **C** — 机械端口，机械旋转

泵壳体的参考角速度和扭矩。
### 输入

### **D** — 容积排量，cm^3/rad，物理信号

泵的容积排量，单位为 m^3/rad，指定为物理信号。

### **EV** — 容积效率，物理信号

流体排量的泵效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，物理信号

机械功率传递的泵效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，m^3/s，物理信号

泵的容积损失，单位为 m^3/s，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦力矩，N\*m，物理信号

泵的机械损失，单位为 N\*m，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。
## 参数
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: 泄漏流量和摩擦力矩的计算方法 Analytical（默认）| Tabulated data - volumetric and mechanical efficiencies | Tabulated data - volumetric
    and mechanical losses | Input signal - volumetric and mechanical efficiencies | Input signal - volumetric and mechanical
    losses
  group: ''
- name: Nominal displacement
  summary: 额定流体排量 30 cm^3/rev（默认）| 标量
  group: ''
- name: Nominal shaft angular velocity
  summary: 轴角速度 1800 rpm（默认）| 标量
  group: ''
- name: Nominal pressure gain
  summary: 流体入口与出口之间的压降 10 MPa（默认）| 标量
  group: ''
- name: Volumetric efficiency at nominal conditions
  summary: 额定工况下实际流量与理想流量之比 0.92（默认）| (0,1] 范围内的正标量
  group: ''
- name: No-load torque
  summary: 基线扭矩 0 N*m（默认）| 标量
  group: ''
- name: Mechanical efficiency at nominal conditions
  summary: 实际机械功率与理想机械功率之比 0.88（默认）| 正标量
  group: ''
- name: Pressure gain vector, dp
  summary: 表格数据参数化的压力数据向量 [.1, 1, 2] MPa（默认）| 1×*n* 向量
  group: ''
- name: Shaft angular velocity vector, w
  summary: 表格数据参数化的角速度数据向量 [250, 500, 1000, 2000, 3000, 4000] rpm（默认）| 1×*n* 向量
  group: ''
- name: Displacement vector, D
  summary: 表格数据参数化的排量体积向量 [-30, -19, 19, 30] cm^3/s（默认）| 1×*n* 向量
  group: ''
- name: Volumetric efficiency table, e_v(dp,w,D)
  summary: 用于表格数据参数化的容积效率 repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78,
    .892, .893, .91], 1, 1, 4)（默认）| *M*×*N*×*P* 矩阵
  group: ''
- name: Mechanical efficiency table, e_m(dp,w,D)
  summary: 用于表格数据参数化的机械效率 repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982,
    .982, .983, .984], 1, 1, 4)（默认）| *M*×*N*×*P* 矩阵
  group: ''
- name: Volumetric loss table, q_loss(dp,w,D)
  summary: 用于表格数据参数化的容积损失 repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108,
    .11, .108, .1605, .18] * 1e-3, 1, 1, 4)m^3/s（默认）| 数值数组
  group: ''
- name: Mechanical loss table, torque_loss(dp,w,D)
  summary: 用于表格数据参数化的机械损失 repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937,
    .1833, .1833, .1729, .1626], 1, 1, 4) N*m（默认）| 数值数组
  group: ''
- name: Minimum volumetric efficiency
  summary: 容积效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: ''
- name: Maximum volumetric efficiency
  summary: 容积效率的最大值 1（默认）| (0,1] 范围内的正标量
  group: ''
- name: Minimum mechanical efficiency
  summary: 机械效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: ''
- name: Maximum mechanical efficiency
  summary: 机械效率的最大值 1（默认）| (0,1] 范围内的正标量
  group: ''
- name: Pressure gain threshold for pump-motor transition
  summary: 模式切换的压力阈值 1e-3 MPa（默认）| 正标量
  group: ''
- name: Angular velocity threshold for pump-motor transition
  summary: 模式切换的角速度阈值 100 rpm（默认）| 正标量
  group: ''
- name: Displacement threshold for pump-motor transition
  summary: 模式切换的排量阈值 0.1 cm^3/s（默认）| 正标量
  group: ''
- name: 检查是否超出所提供的表格数据范围
  summary: 是否在超出所提供数据范围时发出通知 None（默认）| Warning | Error
  group: ''
- name: 检查是否超出泵模式运行
  summary: 是否在模块超出泵模式功能运行时发出通知 None（默认）| Warning | Error
  group: ''
- name: 检查压力是否低于泵最低压力
  summary: 是否在流体出口压力过低时发出通知 None（默认）| Warning | Error
  group: ''
- name: 泵最低压力
  summary: 泵出口可接受压力的下限阈值 0.101325 MPa（默认）| 正标量
  group: ''
```

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的计算方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化方法。

- 在 `Analytical` 参数化中，泄漏流量和摩擦力矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **Pressure gain vector, dp**、**Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数计算，并从三维依赖的 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure gain vector, dp**、**Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数计算，并从三维依赖的 **Volumetric loss table, q\_loss(dp,w,D)** 和 **Mechanical loss table, torque\_loss(dp,w,D)** 表中插值得到。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩分别作为物理信号在端口 **LV** 和 **LM** 接收。

### **Nominal displacement** — 额定流体排量 `30 cm^3/rev`（默认）| 标量

在额定工况下轴旋转所排出的流体量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| 标量

在额定工况下轴的角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure gain** — 流体入口与出口之间的压降 `10 MPa`（默认）| 标量

在额定工况下泵在流体入口与出口之间的压力增益。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 额定工况下实际流量与理想流量之比 `0.92`（默认）| (0,1] 范围内的正标量

额定工况下实际流量与理想流量之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际机械功率与理想机械功率之比 `0.88`（默认）| 正标量

额定工况下实际机械功率与理想机械功率之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure gain vector, dp** — 表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的压差值向量。该向量与 **Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数一起构成三维依赖的 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和机械` efficiencies`
- `表格数据 - 体积和机械` losses`

### **Shaft angular velocity vector, w** — 表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的角速度数据向量。该向量与 **Pressure gain vector, dp** 和 **Displacement vector, D** 参数一起构成三维依赖的 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和机械` efficiencies`
- `表格数据 - 体积和机械` losses`

### **Displacement vector, D** — 表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的流体容积排量数据向量。该向量与 **Shaft angular velocity vector, w** 和 **Pressure gain vector, dp** 参数一起构成三维依赖的 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和机械` efficiencies`
- `表格数据 - 体积和机械` losses`

### **Volumetric efficiency table, e\_v(dp,w,D)** — 用于表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益、轴角速度和容积排量下的 *M*×*N*×*P* 容积效率矩阵。表格元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的长度：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w,D)** — 用于表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益、轴角速度和排量下的 *M*×*N*×*P* 机械效率矩阵。表格元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的长度：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w,D)** — 用于表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)`m^3/s（默认）| 数值数组

在指定的流体压力增益、轴角速度和排量下的 *M*×*N*×*P* 容积泄漏矩阵。表格元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的长度：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w,D)** — 用于表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m`（默认）| 数值数组

在指定的流体压力增益、轴角速度和排量下的 *M*×*N*×*P* 摩擦力矩矩阵。表格元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的长度：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| (0,1] 范围内的正标量

容积效率的最大值。如果输入信号高于此值，则容积效率设置为最大容积效率。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

机械效率的最小值。如果输入信号低于此值，则机械效率设置为最小机械效率。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1`（默认）| (0,1] 范围内的正标量

机械效率的最大值。如果输入信号高于此值，则机械效率设置为最大机械效率。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure gain threshold for pump-motor transition** — 模式切换的压力阈值 `1e-3 MPa`（默认）| 正标量

指示泵与马达功能之间切换阈值的泵压力增益。在压力增益阈值的正值和负值之间围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `表格数据 - 体积和机械` efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Angular velocity threshold for pump-motor transition** — 模式切换的角速度阈值 `100 rpm`（默认）| 正标量

指示马达与泵功能之间切换阈值的轴角速度。在角速度阈值的正值和负值之间围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `表格数据 - 体积和机械` efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical loss`

### **Displacement threshold for pump-motor transition** — 模式切换的排量阈值 `0.1 cm^3/s`（默认）| 正标量

指示泵与马达功能之间切换阈值的容积排量。在排量阈值的正值和负值之间围绕 0 cm^3/s 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。当 **D** 的符号发生变化时，它也用于过渡理想质量流量。

### **检查是否超出所提供的表格数据范围** — 是否在超出所提供数据范围时发出通知 `None`（默认）| `Warning` | `Error`

是否在超出所提供数据范围时发出通知。
选择 `Warning` 可在模块使用超出所提供数据范围的值时收到通知。选择
`Error` 可在模块使用超出所提供数据范围的值时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `表格数据 - 体积和机械`
  efficiencies`
- `表格数据 - 体积和机械`
  losses`

### **检查是否超出泵模式运行** — 是否在模块超出泵模式功能运行时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块超出泵模式功能运行时发出通知。选择 `Warning` 可在
模块以正向或反向马达模式运行时收到通知。选择
`Error` 可在模块以正向或反向马达模式运行时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **检查压力是否低于泵最低压力** — 是否在流体出口压力过低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 和
**B** 处的流体经历低压时发出通知。选择
`Warning` 可在压力
低于指定的最小值时收到通知。选择
`Error` 可在
压力低于指定的最小值时停止仿真。

当流体压力低于流体蒸气压时，该参数有助于识别潜在的
气蚀条件。

### **泵最低压力** — 泵出口可接受压力的下限阈值 `0.101325 MPa`（默认）| 正标量

泵入口或出口处可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **Check if pressures are less
than pump minimum pressure** 设置为以下任一值：

- `Warning`
- `Error`
## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the octants of supplied tabulated
data** 参数已重命名为 **Check if operating
beyond the range of supplied tabulated data**。您可以启用
**Check if operating beyond the range of supplied tabulated
data** 参数来检查模块是否在模块参数中指定的数据之外运行，即在模块
已扩展数据的区域中运行。

## 描述

等温液体网络中的可变排量泵

Variable-Displacement Pump (IL) 模块对具有可变容积
排量的泵进行建模。流体可以从端口 **A** 流向端口
**B**，称为*正向模式*，或从端口
**B** 流向端口 **A**，称为*反向
模式*。当沿流动方向存在压力增益时，发生泵模式运行。当沿流动方向存在压降时，发生马达模式运行。

轴旋转对应于通过泵的流体体积的符号，该体积作为物理信号在端口 **D** 处接收。在
**D** 处的正流体排量对应于正向模式下的正轴旋转。在
**D** 处的负流体排量对应于正向模式下的
负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益，*Δp =
p*B – *p*A；
角速度，*ω = ω*R –
*ω*C；以及端口 **D** 处的流体容积排量。上图将这些模式映射到
*Δp*-*ω*-*D* 图的八分圆：

- 模式 1，*正向泵*：正轴角速度
  导致从端口 **A** 到端口
  **B** 的压力升高以及从端口 **A** 到端口
  **B** 的流动。
- 模式 2，*反向马达*：从端口
  **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力
  降低以及负
  轴角速度。
- 模式 3，*反向泵*：负轴角速度
  导致从端口 **B** 到端口
  **A** 的压力升高以及从 **B** 到
  **A** 的流动。
- 模式 4，*正向马达*：从端口
  **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力
  降低以及正轴角速度。
- 模式 5，*反向马达*：从端口
  **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力
  降低以及正
  轴角速度。
- 模式 6，*正向泵*：负轴角速度
  导致从 **A** 到
  **B** 的压力升高以及从 **A** 到
  **B** 的流动。
- 模式 7，*正向马达*：从端口
  **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力
  降低以及负
  轴角速度。
- 模式 8，*反向泵*：正轴角速度
  导致从端口 **B** 到端口
  **A** 的压力升高以及从 **B** 到
  **A** 的流动。

泵模块具有解析、查找表和物理信号参数化。当使用表格数据或输入信号进行参数化时，您可以选择
基于效率或损失来表征泵运行。

阈值参数 **Pressure gain threshold for pump-motor
transition**、**Angular velocity threshold for pump-motor
transition** 和 **Displacement threshold for pump-motor
transition** 标识了泵运行模式之间可发生数值平滑流动过渡的区域。对于压力和角速度
阈值，请选择为过渡项提供一定裕度的过渡区域，但该区域相对于典型泵压力增益和角
速度应足够小，以免影响计算结果。对于排量阈值，
请选择小于正常运行期间典型排量体积的阈值。

### 解析泄漏和摩擦参数化

如果将 **Leakage and friction parameterization** 设置为
`Analytical`，则该模块根据轴速度、压力增益、
容积排量和容积效率的恒定标称值计算内部泄漏和
轴摩擦。泄漏流量与泵上的压差相关，其计算公式为：

m˙leak=KρavgΔp，

其中：

- *Δp* 为 *p*B
  – *p*A。
- *ρ*avg 为平均流体
  密度。
- *K* 为用于
  解析损失的 Hagen-Poiseuille 系数，

  K=Dnomωnom(1−ηv,nom)Δpnom，

  其中：

  - *D*nom 为
    **Nominal displacement**。
  - *ω*nom 为
    **Nominal shaft angular
    velocity**。
  - *η*nom 为
    **Volumetric efficiency at nominal
    conditions**。
  - *Δp*nom 为
    **Nominal pressure gain**。

摩擦力矩与泵压差相关，其计算公式为：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom)，

其中：

- *τ*0 为 **No-load
  torque**。
- *k* 为标称排量下的摩擦力矩与压力增益系数，由 **Mechanical
  efficiency at nominal conditions**、
  *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 为
  标称条件下的摩擦力矩：

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom。
- *ω* 为相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示泵效率或损失时，您可以为一种或多种泵运行模式提供数据。表格数据的符号决定了模块的运行工况。当提供的数据少于八种运行模式时，模块通过将给定数据扩展到其余八分圆来计算其他模式的补充数据。

**`表格数据 - 容积效率和机械效率`参数化**

泄漏流量计算如下：

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2)，

其中：

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

而 *η*v 是容积效率，它由用户提供的表格数据插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold)，

其中：

- *Δp* 是 *p*B – *p*A。
- *Δp*threshold 是 **泵-马达过渡的压差阈值**。
- *ω* 是 *ω*R – *ω*C。
- *ω*threshold 是 **泵-马达过渡的角速度阈值**。

摩擦力矩计算如下：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2)，

其中：

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

而 *η*m 是机械效率，它由用户提供的表格数据插值得到。

**`表格数据 - 容积损失和机械损失`参数化**

泄漏流量计算如下：

m˙leak=ρavgqloss(Δp,ω,D)，

其中 *q*loss 由 **容积损失表，q\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压差、轴角速度和流体容积排量数据。

轴摩擦力矩计算如下：

τfr=τloss(Δp,ω,D)，

其中 *τ*loss 由 **机械损失表，torque\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压差、轴角速度和流体容积排量数据。

### 输入信号参数化

当您选择 `输入信号 - 容积效率和机械效率` 时，端口 **EV** 和 **EM** 被启用。内部泄漏和轴摩擦的计算方式与 `表格数据 - 容积效率和机械效率` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接从端口 **EV** 和 **EM** 接收。

当您选择 `输入信号 - 容积损失和机械损失` 时，端口 **LV** 和 **LM** 被启用。这些端口以正物理信号接收泄漏流量和摩擦力矩。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh)，

其中：

- *q*LV 是在端口 **LV** 接收的泄漏流量。
- *p*thresh 是 **泵-马达过渡的压差阈值** 参数。

摩擦力矩计算如下：

τfr=τLMtanh(4ωωthresh)，

其中

- *τ*LM 是在端口 **LM** 接收的摩擦力矩。
- *ω*thresh 是 **泵-马达过渡的角速度阈值** 参数。

容积效率和机械效率在用户指定的最小值和最大值之间取值。任何低于或高于此范围的值将分别取指定的最小值和最大值。

### 泵运行

泵流量为：

m˙=m˙ideal−m˙leak，

其中 m˙ideal=ρavgD⋅ω。

泵扭矩为：

τ=τideal+τfr，

其中 τideal=D⋅Δp。

泵轴传递的机械功率为：

φmech=τω，

泵液压功率为：

φhyd=Δpm˙ρavg。

若要在模块运行超出所提供的表格数据范围时收到通知，您可以将 **检查是否超出所提供的表格数据范围** 设置为 `Warning`，以便在发生此情况时收到警告，或设置为 `Error`，以便在发生此情况时停止仿真。当使用输入信号表示容积损失或机械损失时，您可以通过 **检查是否超出泵模式** 参数在仿真超出运行模式时收到通知。

您还可以监控泵的功能。将 **检查压力是否低于泵最低压力** 设置为 `Warning`，以便在发生此情况时收到警告，或设置为 `Error`，以便在发生此情况时停止仿真。
