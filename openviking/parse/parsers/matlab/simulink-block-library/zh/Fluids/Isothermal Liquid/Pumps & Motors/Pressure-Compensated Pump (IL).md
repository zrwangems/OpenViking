---
type: simulink-block
title: 'Pressure-Compensated Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'pressurecompensatedpumpil'
documentation_source_path: 'ref/pressurecompensatedpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Compensated Pump (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: X
  summary: 压力参考 *P*x，MPa，等温液体
  direction: conserving
- name: Y
  summary: 压力参考 *P*y，MPa，等温液体
  direction: conserving
- name: R
  summary: 机械端口，机械旋转
  direction: conserving
- name: C
  summary: 机械端口，机械旋转
  direction: conserving
- name: EV
  summary: 容积效率，物理信号
  direction: conserving
- name: EM
  summary: 机械效率，物理信号
  direction: conserving
- name: LV
  summary: 泄漏流量，m^3/s，物理信号
  direction: conserving
- name: LM
  summary: 摩擦力矩，N*m，物理信号
  direction: conserving
```

### 守恒端口

### **A** — 液体端口，等温液体

液体进入或离开泵的入口或出口端口。

### **B** — 液体端口，等温液体

液体进入或离开泵的入口或出口端口。

### **X** — 压力参考 *P*x，MPa，等温液体

以 MPa 为单位的控制压力，记为
*P*x。控制压力
*P*x –
*P*y 与 **Set pressure differential** 进行比较，以触发或
调节变量泵排量。

### **Y** — 压力参考 *P*y，MPa，等温液体

以 MPa 为单位的控制压力，记为
*P*y。控制压力
*P*x –
*P*y 与 **Set pressure differential** 进行比较，以触发或
调节变量泵排量。

### **R** — 机械端口，机械旋转

旋转轴角速度和扭矩。

### **C** — 机械端口，机械旋转

泵壳体参考角速度和扭矩。

### **EV** — 容积效率，物理信号

用于流体排量的泵效率，指定为物理
信号。该值必须在 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **EM** — 机械效率，物理信号

用于机械能量供给的泵效率，指定为
物理信号。该值必须在 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，`m^3/s`，物理信号

与流体排量相关的泵损失，单位为
m3/s，指定为物理
信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **LM** — 摩擦力矩，`N*m`，物理信号

与机械能量供给相关的泵损失，单位为 N\*m，
指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。
## 参数
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: 泄漏流量和摩擦力矩的计算方法 Analytical（默认）| Tabulated data - volumetric and mechanical efficiencies | Tabulated data - volumetric
    and mechanical losses | Input signal - volumetric and mechanical efficiencies | Input signal - volumetric and mechanical
    losses
  group: 泵
- name: Nominal displacement
  summary: 固定容积流体排量 30 cm^3/rev（默认）| 标量
  group: 泵
- name: Nominal shaft angular velocity
  summary: 轴角速度 1800 rpm（默认）| 标量
  group: 泵
- name: Nominal pressure gain
  summary: 流体入口和出口之间的压力增益 10 MPa（默认）| 标量
  group: 泵
- name: Volumetric efficiency at nominal conditions
  summary: 实际流量与理想流量之比 0.92（默认）| (0,1] 范围内的正标量
  group: 泵
- name: No-load torque
  summary: 基线扭矩 0 N*m（默认）| 标量
  group: 泵
- name: Mechanical efficiency at nominal conditions
  summary: 实际机械功率与理想机械功率之比 0.88（默认）| 正标量
  group: 泵
- name: Pressure gain vector, dp
  summary: 表格数据参数化的压力数据向量 [.1, 1, 2] MPa（默认）| 1×*n* 向量
  group: 泵
- name: Shaft angular velocity vector, w
  summary: 表格数据参数化的角速度数据向量 [250, 500, 1000, 2000, 3000, 4000] rpm（默认）| 1×*n* 向量
  group: 泵
- name: Displacement vector, D
  summary: 表格数据参数化的排量体积向量 [-30, -19, 19, 30] cm^3/s（默认）| 1×*n* 向量
  group: 泵
- name: Volumetric efficiency table, e_v(dp,w,D)
  summary: 表格数据参数化的容积效率 repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892,
    .893, .91], 1, 1, 4)（默认）| *M*×*N*×*P* 矩阵
  group: 泵
- name: Mechanical efficiency table, e_m(dp,w,D)
  summary: 表格数据参数化的机械效率 repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982,
    .983, .984], 1, 1, 4)（默认）| *M*×*N*×*P* 矩阵
  group: 泵
- name: Volumetric loss table, q_loss(dp,w,D)
  summary: 表格数据参数化的容积损失 repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108,
    .11, .108, .1605, .18] * 1e-3, 1, 1, 4)m^3/s（默认）| 数值数组
  group: 泵
- name: Mechanical loss table, torque_loss(dp,w,D)
  summary: 表格数据参数化的机械损失 repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937,
    .1833, .1833, .1729, .1626], 1, 1, 4) N*m（默认）| 数值数组
  group: 泵
- name: Minimum volumetric efficiency
  summary: 容积效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: 泵
- name: Maximum volumetric efficiency
  summary: 容积效率的最大值 1（默认）| (0,1] 范围内的正标量
  group: 泵
- name: Minimum mechanical efficiency
  summary: 机械效率的最小值 1e-3（默认）| (0,1] 范围内的正标量
  group: 泵
- name: Maximum mechanical efficiency
  summary: 机械效率的最大值 1（默认）| (0,1] 范围内的正标量
  group: 泵
- name: Pressure gain threshold for pump-motor transition
  summary: 模式转换的压力阈值 1e-3 MPa（默认）| 正标量
  group: 泵
- name: Angular velocity threshold for pump-motor transition
  summary: 模式转换的角速度阈值 100 rpm（默认）| 正标量
  group: 泵
- name: Check if operating beyond the range of supplied tabulated data
  summary: 是否在超出所提供数据范围时发出通知 None（默认）| Warning | Error
  group: 泵
- name: 检查是否超出泵模式运行
  summary: 是否在模块超出泵模式功能范围运行时发出通知 None（默认）| Warning | Error
  group: 泵
- name: 检查压力是否低于泵最低压力
  summary: 是否在流体出口压力过低时发出通知 None（默认）| Warning | Error
  group: 泵
- name: 泵最低压力
  summary: 泵出口可接受压力的下限阈值 0.101325 MPa（默认）| 正标量
  group: 泵
- name: 最大排量
  summary: 泵排量的上限 30 cm^3/rev（默认）| 标量
  group: 压力补偿
- name: 最小排量
  summary: 泵排量的下限 0.1 cm^3/rev（默认）| 标量
  group: 压力补偿
- name: 设定压差
  summary: 可变排量功能的阈值 10 MPa（默认）| 正标量
  group: 压力补偿
- name: 压力调节范围
  summary: 可变排量工作范围 0.6 MPa（默认）| 正标量
  group: 压力补偿
- name: 排量动态特性
  summary: 是否考虑流量对排量变化的响应 off（默认）| on
  group: 压力补偿
- name: 时间常数
  summary: 流量响应时间常数 0.1 s（默认）| 正标量
  group: 压力补偿
```

### 泵

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的计算方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化方法。

- 在 `Analytical`
  参数化中，泄漏流量和摩擦力矩
  通过解析方程计算。
- 在 `Tabulated data - volumetric and
  mechanical efficiencies` 参数化中，
  容积效率和机械效率根据用户提供的 **Pressure gain vector,
  dp**、**Shaft angular velocity vector,
  w** 和 **Displacement vector,
  D** 参数计算，并从 3-D
  **Volumetric efficiency table,
  e\_v(dp,w,D)** 和 **Mechanical
  efficiency table, e\_m(dp,w,D)** 表中插值得到。
- 在 `Tabulated data - volumetric and
  mechanical losses` 参数化中，
  泄漏流量和摩擦力矩根据用户提供的 **Pressure gain vector,
  dp**、**Shaft angular velocity vector,
  w** 和 **Displacement vector,
  D** 参数计算，并从 3-D
  **Volumetric loss table,
  q\_loss(dp,w,D)** 和 **Mechanical loss
  table, torque\_loss(dp,w,D)** 参数中插值得到。
- 在 `Input signal - volumetric and
  mechanical efficiencies` 参数化中，
  容积效率和机械效率分别作为
  物理信号在端口 **EV** 和
  **EM** 处接收。
- 在 `Input signal - volumetric and
  mechanical loss` 参数化中，
  泄漏流量和摩擦力矩分别作为
  物理信号在端口 **LV** 和
  **LM** 处接收。

### **Nominal displacement** — 固定容积流体排量 `30 cm^3/rev`（默认）| 标量

在额定工况下轴旋转所排出的流体量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| 标量

在额定工况下的轴角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **Nominal pressure gain** — 流体入口和出口之间的压力增益 `10 MPa`（默认）| 标量

在额定工况下泵在流体入口和出口之间的压力增益。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **Volumetric efficiency at nominal conditions** — 实际流量与理想流量之比 `0.92`（默认）| (0,1] 范围内的正标量

在额定工况下实际流量与理想流量之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际机械功率与理想机械功率之比 `0.88`（默认）| 正标量

在额定工况下实际机械功率与理想机械功率之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为
`Analytical`。

### **Pressure gain vector, dp** — 表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的压差
值向量。该向量与 **Shaft angular velocity vector,
w** 和 **Displacement vector, D**
参数一起构成独立轴，用于 3-D 因变量 **Volumetric efficiency table,
e\_v(dp,w,D)** 和 **Mechanical efficiency table,
e\_m(dp,w,D)** 参数。向量元素必须
按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为以下之一：

- `表格数据 - 体积和
  mechanical efficiencies`
- `表格数据 - 体积和
  mechanical losses`

### **Shaft angular velocity vector, w** — 表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的角速度
数据向量。该向量与 **Pressure gain vector, dp** 和
**Displacement vector, D** 参数一起构成独立轴，用于 3-D
因变量 **Volumetric efficiency table, e\_v(dp,w,D)**
和 **Mechanical efficiency table, e\_m(dp,w,D)**
参数。向量元素必须按升序
排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为以下之一：

- `表格数据 - 体积和
  mechanical efficiencies`
- `表格数据 - 体积和
  mechanical losses`

### **Displacement vector, D** — 表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s`（默认）| 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的流体容积排量
数据向量。该向量与 **Shaft angular velocity vector,
w** 和 **Pressure gain vector, dp**
参数一起构成独立轴，用于 3-D 因变量 **Volumetric efficiency table,
e\_v(dp,w,D)** 和 **Mechanical efficiency table,
e\_m(dp,w,D)** 参数。向量元素必须
按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为以下之一：

- `表格数据 - 体积和
  mechanical efficiencies`
- `表格数据 - 体积和
  mechanical losses`

### **Volumetric efficiency table, e\_v(dp,w,D)** — 表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定流体压力增益、轴角速度和容积排量下的
*M*×*N*×*P*
容积效率矩阵。表元素之间采用线性
插值。*M*、*N* 和 *P* 是相应向量的
大小：

- *M* 是 **Pressure gain vector, dp**
  参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w**
  参数中向量元素的数量。
- *P* 是 **Displacement vector, D**
  参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Tabulated data -
volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w,D)** — 表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定流体压力增益、轴角速度和排量下的
*M*×*N*×*P*
机械效率矩阵。表元素之间采用线性插值。
*M*、*N* 和 *P* 是相应向量的
大小：

- *M* 是 **Pressure gain vector, dp**
  参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w**
  参数中向量元素的数量。
- *P* 是 **Displacement vector, D**
  参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Tabulated data -
volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w,D)** — 表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)`m^3/s（默认）| 数值数组

在指定流体压力增益、轴角速度和排量下的
*M*×*N*×*P*
容积泄漏矩阵。表元素之间采用线性插值。
*M*、*N* 和
*P* 是相应向量的大小：

- *M* 是 **Pressure gain vector, dp**
  参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w**
  参数中向量元素的数量。
- *P* 是 **Displacement vector, D**
  参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Tabulated data -
volumetric and mechanical loss`。

### **Mechanical loss table, torque\_loss(dp,w,D)** — 表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m`（默认）| 数值数组

在指定流体压力增益、轴角速度和排量下的
*M*×*N*×*P*
摩擦力矩矩阵。表元素之间采用线性插值。
*M*、*N* 和
*P* 是相应向量的大小：

- *M* 是 **Pressure gain vector, dp**
  参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w**
  参数中向量元素的数量。
- *P* 是 **Displacement vector, D**
  参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Tabulated data -
volumetric and mechanical loss`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

容积效率的最小值。如果输入信号低于
此值，则容积效率设置为最小容积
效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| (0,1] 范围内的正标量

容积效率的最大值。如果输入信号高于
此值，则容积效率设置为最大容积
效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

机械效率的最小值。如果输入信号低于
此值，则机械效率设置为最小机械
效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1`（默认）| (0,1] 范围内的正标量

机械效率的最大值。如果输入信号高于
此值，则机械效率设置为最大机械
效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical efficiencies`。

### **Pressure gain threshold for pump-motor transition** — 模式转换的压力阈值 `1e-3 MPa`（默认）| 正标量

泵和马达功能之间转换的阈值压力增益
值。在压力增益阈值的正值和负值之间围绕 0 MPa 定义了一个转换
区域。在该转换区域内，计算的泄漏流量和摩擦
力矩根据转换项
*α* 进行调整，以确保从一种模式
平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为以下之一：

- `表格数据 - 体积和
  mechanical efficiencies`
- `输入信号 - 体积和机械
  efficiencies`
- `输入信号 - 体积和机械
  losses`

### **Angular velocity threshold for pump-motor transition** — 模式转换的角速度阈值 `100 rpm`（默认）| 正标量

马达和泵功能之间转换的阈值角速度
值。在角速度阈值的正值和负值之间围绕 0 rpm 定义了一个转换
区域。在该转换区域内，计算的泄漏流量和摩擦
力矩根据转换项
*α* 进行调整，以确保从一种模式
平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `表格数据 - 体积和
  mechanical efficiencies`
- `输入信号 - 体积和机械
  efficiencies`
- `输入信号 - 体积和机械
  loss`

### **Check if operating beyond the range of supplied tabulated data** — 是否在超出所提供数据范围时发出通知 `None`（默认）| `Warning` | `Error`

是否在超出所提供数据范围时发出通知。
选择 `Warning` 以在模块使用超出所提供数据范围的值时
收到通知。选择
`Error` 以在模块使用超出所提供数据范围的值时
停止仿真。

#### 依赖关系

要启用此参数，请将**泄漏和摩擦参数化**设置为：

- `表格数据 - 体积和 mechanical efficiencies`
- `表格数据 - 体积和 mechanical losses`

### **检查是否超出泵模式运行** — 是否在模块超出泵模式功能范围运行时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块超出泵模式功能范围运行时发出通知。选择 `Warning` 以在模块运行于正向或反向马达模式时收到警告。选择 `Error` 以在模块运行于正向或反向马达模式时停止仿真。

#### 依赖关系

要启用此参数，请将**泄漏和摩擦参数化**设置为 `Input signal - volumetric and mechanical losses`。

### **检查压力是否低于泵最低压力** — 是否在流体出口压力过低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择 `Warning` 以在出口压力低于指定的最低值时收到警告。选择 `Error` 以在出口压力低于指定的最低值时停止仿真。

该参数有助于识别可能发生气蚀的条件，即流体压力低于流体蒸气压时。

### **泵最低压力** — 泵出口可接受压力的下限阈值 `0.101325 MPa`（默认）| 正标量

泵入口或出口可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将**检查压力是否低于泵最低压力**设置为：

- `Warning`
- `Error`

### 压力补偿

### **最大排量** — 泵排量的上限 `30 cm^3/rev`（默认）| 标量

泵排量的上限。

### **最小排量** — 泵排量的下限 `0.1 cm^3/rev`（默认）| 标量

泵排量的下限。

### **设定压差** — 可变排量功能的阈值 `10 MPa`（默认）| 正标量

超过此阈值后泵排量将被调整。

### **压力调节范围** — 可变排量工作范围 `0.6 MPa`（默认）| 正标量

可变排量工作范围。泵在**设定压差**与泵最大压力之间运行，泵最大压力为 *pset + pregulation*。

### **排量动态特性** — 是否考虑流量对排量变化的响应 `off`（默认）| `on`

是否考虑泵流体排量变化对流体系统的瞬态效应。选择**排量动态特性**通过引入流量响应的一阶滞后来近似工况变化。**时间常数**的大小也会影响所建模的排量动态特性。

### **时间常数** — 流量响应时间常数 `0.1 s`（默认）| 正标量

当改变流体排量时，流体达到稳态所需的时间常数。此参数影响所建模的排量动态特性。

#### 依赖关系

要启用此参数，请选择**排量动态特性**。
## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**检查是否超出所提供的表格数据的八分区运行**参数已重命名为**检查是否超出所提供的表格数据范围运行**。您可以启用**检查是否超出所提供的表格数据范围运行**参数来检查模块是否在模块参数所指定的数据范围之外运行，即在模块已扩展数据的区域中运行。

## 描述

等温液体网络中的恒压可变排量泵

Pressure-Compensated Pump (IL) 模块对等温液体网络中的恒压可变排量泵进行建模。泵排量由在端口 **X** 和 **Y** 之间测量的压差 *pcontrol* 控制。当该压力超过**设定压差**时，流体排量根据泵的**泄漏和摩擦参数化**进行调整。可变排量功能在**压力调节范围**内发生，介于 *pset* 处的**最大排量**与 *pmax* 处的**最小排量**之间。

流体可以从端口 **A** 流向端口 **B**，称为*正向模式*，或从端口 **B** 流向端口 **A**，称为*反向模式*。泵模式运行发生在沿流动方向存在压力增益时。马达模式运行发生在沿流动方向存在压力降时。

轴旋转对应于通过泵的流体体积的符号。正流体排量对应于正向模式下的正轴旋转。负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益 *Δp = p*B – *p*A；角速度 *ω = ω*R – *ω*C；以及由压差设定的流体体积排量。上图将这些模式映射到 *Δp*-*ω*-*D* 图的八分区：

- 模式 1，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力升高，以及从端口 **A** 到端口 **B** 的流动。
- 模式 2，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 3，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从 **B** 到 **A** 的流动。
- 模式 4，*正向马达*：从端口 **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 5，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低以及正轴角速度。
- 模式 6，*正向泵*：负轴角速度导致从 **A** 到 **B** 的压力升高以及从 **A** 到 **B** 的流动。
- 模式 7，*正向马达*：从端口 **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力降低以及负轴角速度。
- 模式 8，*反向泵*：正轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从 **B** 到 **A** 的流动。

该模块具有解析、查找表和物理信号参数化。当使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征泵运行。

阈值参数**泵-马达转换的压力增益阈值**、**泵-马达转换的角速度阈值**和**泵-马达转换的排量阈值**用于标识泵运行模式之间可发生数值平滑流量转换的区域。对于压力和角速度阈值，请选择一个为转换项提供一定裕度的转换区域，但该区域相对于典型泵压力增益和角速度足够小，以免影响计算结果。对于排量阈值，请选择一个小于正常运行期间典型排量体积的阈值。

### 解析泄漏和摩擦参数化

如果将**泄漏和摩擦参数化**设置为 `Analytical`，模块将根据轴速度、压力增益和扭矩的常数值计算泄漏和摩擦。与泵上压差相关的泄漏流量计算如下：

m˙leak=KρavgΔp，

其中：

- *Δp*nom 为 *p*B – *p*A。
- *ρ*avg 为平均流体密度。
- *K* 为解析损失的 Hagen-Poiseuille 系数，

  K=Dnomωnom(1−ηv,nom)Δpnom，

  其中：

  - *D*nom 为**额定排量**。
  - *ω*nom 为**额定轴角速度**。
  - *η*nom 为**额定条件下的容积效率**。
  - *Δp*nom 为**额定压力增益**。

与泵压差相关的摩擦扭矩计算如下：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom)，

其中：

- *τ*0 为**空载扭矩**。
- *k* 为额定排量下的摩擦扭矩与压力增益系数，由**额定条件下的机械效率** *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 为额定条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom。
- *ω* 为相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示泵效率或损失时，您可以为一种或多种泵运行模式提供数据。表格数据的符号决定模块的运行区间。当为少于八种运行模式提供数据时，模块通过将给定数据扩展到其余八分区来计算其他模式的补充数据。

**`Tabulated data - volumetric and mechanical efficiencies` 参数化**

泄漏流量计算如下：

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2)，

其中：

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

并且 *η*v 为容积效率，由用户提供的表格数据插值得到。转换项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold)，

其中：

- *Δp* 为 *p*B – *p*A。
- *p*threshold 为**泵-马达转换的压力增益阈值**。
- *ω* 为 *ω*R – *ω*C。
- *ω*threshold 为**泵-马达转换的角速度阈值**。

摩擦扭矩计算如下：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2)，

其中：

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

并且 *η*m 为机械效率，由用户提供的表格数据插值得到。

**`Tabulated data - volumetric and mechanical losses` 参数化**

泄漏流量计算如下：

m˙leak=ρavgqloss(Δp,ω,D)，

其中 *q*loss 由**容积损失表，q\_loss(dp,w,D)**参数插值得到，该参数基于用户提供的压力增益、轴角速度和流体体积排量数据。

轴摩擦扭矩计算如下：

τfr=τloss(Δp,ω,D)，

其中 *τ*loss 由**机械损失表，torque\_loss(dp,w,D)**参数插值得到，该参数基于用户提供的压力增益、轴角速度和流体体积排量数据。

### 输入信号参数化

当选择 `Input signal - volumetric and mechanical efficiencies` 时，端口 **EV** 和 **EM** 启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and mechanical efficiencies` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接在端口 **EV** 和 **EM** 处接收。

当选择 `Input signal - volumetric and mechanical losses` 时，端口 **LV** 和 **LM** 启用。这些端口以正物理信号形式接收泄漏流量和摩擦扭矩。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh)，

其中：

- *q*LV 为在端口 **LV** 处接收的泄漏流量。
- *p*thresh 为**泵-马达转换的压力增益阈值**参数。

摩擦扭矩计算如下：

τfr=τLMtanh(4ωωthresh)，

其中

- *τ*LM 为在端口 **LM** 处接收的摩擦扭矩。
- *ω*thresh 为**泵-马达转换的角速度阈值**参数。

容积效率和机械效率在用户指定的最小值和最大值之间。任何低于或高于此范围的值将分别取指定的最小值和最大值。

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

若要在模块超出所提供的表格数据运行时收到通知，请将**检查是否超出所提供的表格数据范围运行**设置为 `Warning` 以在发生此情况时收到警告，或设置为 `Error` 以在发生此情况时停止仿真。对于通过输入信号进行容积损失或机械损失参数化的情况，您可以使用**检查是否超出泵模式运行**参数在仿真超出运行模式时收到通知。

您还可以监控泵功能。将**检查压力是否低于泵最低压力**设置为 `Warning` 以在发生此情况时收到警告，或设置为 `Error` 以在发生此情况时停止仿真。

### 排量参数化

泵排量的线性参数化为：

D=p^(Dmin−Dmax)+Dmax，

其中归一化压力 p^ 为

p^=pcontrol−psetpmax−pset。

其中 *pmax* 为**设定压差**与**压力调节范围**之和。

### 排量动态特性

如果对排量动态特性进行建模，则会对所建模控制压力的流量响应引入滞后。*p*control 变为动态控制压力 *p*dyn；否则，*p*control 为稳态压力。动态控制压力的瞬时变化基于**时间常数** *τ* 计算：

p˙dyn=pcontrol−pdynτ。

默认情况下，**排量动态特性**复选框未选中。

### 数值平滑压力

您可以通过调整**平滑因子**参数来保持仿真中的数值鲁棒性。如果**平滑因子**参数非零，模块将在 *pset* 和 *pmax* 之间平滑饱和归一化控制压力。有关详细信息，请参阅数值平滑。
