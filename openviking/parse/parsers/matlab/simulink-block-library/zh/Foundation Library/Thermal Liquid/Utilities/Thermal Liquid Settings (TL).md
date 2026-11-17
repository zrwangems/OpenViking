---
type: simulink-block
title: 'Thermal Liquid Settings (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Utilities'
documentation_page: 'thermalliquidsettingstl'
documentation_source_path: 'ref/thermalliquidsettingstl.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Liquid Settings (TL)

## 端口
```yaml
ports:
- name: A
  summary: 热液体网络连接器 thermal liquid
  direction: unspecified
```

### 守恒

### **A** — 热液体网络连接器 thermal liquid

用于标识所指定流体属性所适用的热液体网络的端口。
## 参数
```yaml
parameters:
- name: Table dimensions
  summary: 流体属性表的维度 2D tables based on temperature and pressure (T,p)（默认）| 1D vectors based on temperature (T)
  group: ''
- name: Temperature vector
  summary: '用于指定流体属性的参考温度 [273.1600 : 10 : 373.16]'' K（默认）| 单位为温度的 *M* 元素列向量'
  group: ''
- name: Pressure vector
  summary: '用于指定流体属性的参考压力 [0.01, 0.1, 5 : 5 : 50] MPa（默认）| 单位为压力的 *N* 元素行向量'
  group: ''
- name: Atmospheric pressure
  summary: 热液体网络环境的绝对压力 0.101325 MPa（默认）| 单位为压力的标量
  group: ''
- name: Valid pressure-temperature region parameterization
  summary: 压力-温度有效区域的规定方法 Specified minimum and maximum values（默认）| Validity matrix
  group: ''
- name: Minimum valid temperature
  summary: 模型中允许的最低温度 273.16 K（默认）| 单位为温度的标量
  group: ''
- name: Maximum valid temperature
  summary: 模型中允许的最高温度 373.16 K（默认）| 单位为温度的标量
  group: ''
- name: Minimum valid pressure
  summary: 模型中允许的最低压力 0.01 MPa（默认）| 单位为压力的标量
  group: ''
- name: Maximum valid pressure
  summary: 模型中允许的最高压力 50 MPa（默认）| 单位为压力的标量
  group: ''
- name: Pressure-temperature validity matrix
  summary: 允许和不允许的压力-温度条件矩阵 11×12 的零和一矩阵（默认）| 无量纲 *M*×*N* 矩阵
  group: ''
- name: Pressure and temperature outside valid range
  summary: 当压力或温度超出有效范围时是否发出通知 Error（默认）| Warning | None
  group: ''
- name: Density parameterization
  summary: 流体密度的指定方法 Density, bulk modulus and thermal expansion tables - rho(T,p), beta(T,p), alpha(T,p)（默认）| Density table
    - rho(T,p) | Reference density | Density vector - rho(T)
  group: ''
- name: Density table, rho(T,p)
  summary: 在指定温度和压力下的流体密度矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为质量/体积
  group: ''
- name: Density vector, rho(T)
  summary: 在指定温度下的流体密度向量 11 元素列向量（默认）| *M* 元素向量，单位为质量/体积
  group: ''
- name: Isothermal bulk modulus table, beta(T,p)
  summary: 在指定温度和压力下的等温体积模量矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为压力
  group: ''
- name: Isobaric thermal expansion coefficient table, alpha(T,p)
  summary: 在指定温度和压力下的等压热膨胀系数矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为 1/温度
  group: ''
- name: Reference density
  summary: 已知工况下的密度 998.21 kg/m^3（默认）| 标量，单位为质量/体积
  group: ''
- name: Reference temperature
  summary: 已知工况下的温度 293.16 K（默认）| 标量，单位为温度
  group: ''
- name: Reference pressure
  summary: 已知工况下的压力 0.101325 MPa（默认）| 标量，单位为压力
  group: ''
- name: Constant isothermal bulk modulus
  summary: 已知工况下的等温体积模量 2.1791 GPa（默认）| 标量，单位为压力
  group: ''
- name: Constant isobaric thermal expansion coefficient
  summary: 已知工作条件下的等压热膨胀系数 2.0691e-4 1/K（默认）| 单位为 1/温度的标量
  group: ''
- name: Internal energy parameterization
  summary: 流体比内能的指定方法 Specific internal energy and specific heat tables - u(T,p), cp(T,p)（默认）| Specific internal energy table
    - u(T,p) | Specific heat table - cp(T,p)
  group: ''
- name: Specific internal energy table, u(T,p)
  summary: 指定温度和压力下的比内能矩阵 11×12 矩阵（默认）| 单位为 能量/质量 的 *M*×*N* 矩阵
  group: ''
- name: Specific internal energy vector, u(T)
  summary: 指定温度下的比内能向量 11 元素向量（默认）| 单位为 能量/质量 的 *M* 元素向量
  group: ''
- name: Specific heat at constant pressure table, cp(T,p)
  summary: 指定温度和压力下的比热矩阵 11×12 矩阵（默认）| 单位为 能量/(质量\*温度) 的 *M*×*N* 矩阵
  group: ''
- name: Specific heat at constant pressure vector, u(T)
  summary: 指定温度下的比热向量 11 元素向量（默认）| 单位为 能量/(质量\*温度) 的 *M* 元素向量
  group: ''
- name: Kinematic viscosity table, nu(T,p)
  summary: 指定温度和压力下的运动粘度矩阵 11 元素向量（默认）| 单位为 面积/时间 的 *M* 元素向量
  group: ''
- name: Thermal conductivity table, K(T,p)
  summary: 指定温度和压力下的热导率矩阵 11 元素向量（默认）| 单位为 功率/(长度\*温度) 的 *M* 元素向量
  group: ''
- name: Kinematic viscosity vector, nu(T)
  summary: 指定温度下的运动粘度向量 11×12 矩阵（默认）| 单位为 面积/时间 的 *M*×*N* 矩阵
  group: ''
- name: Thermal conductivity vector, K(T)
  summary: 指定温度下的热导率向量 11×12 矩阵（默认）| 单位为 power/(length\*temperature) 的 *M*×*N* 矩阵
  group: ''
```

#### 温度和压力

### **Table dimensions** — 流体属性表的维度 `2D tables based on temperature and pressure (T,p)`（默认）| `1D vectors based on temperature (T)`

流体属性表的维度。此参数决定流体属性是否随压力变化。选择 `1D vectors based on temperature (T)` 可忽略流体属性的压力依赖性。

### **Temperature vector** — 用于指定流体属性的参考温度 `[273.1600 : 10 : 373.16]' K`（默认）| 单位为温度的 *M* 元素列向量

用于指定流体属性值的温度向量。每个温度对应流体属性表的一行。

### **Pressure vector** — 用于指定流体属性的参考压力 `[0.01, 0.1, 5 : 5 : 50] MPa`（默认）| 单位为压力的 *N* 元素行向量

用于指定流体属性值的压力向量。每个压力对应流体属性表的一列。

#### 依赖关系

此参数仅在 **Table dimensions** 参数设置为 `2D vectors based on temperature and pressure (T,p)` 时有效。

### **Atmospheric pressure** — 热液体网络环境的绝对压力 `0.101325 MPa`（默认）| 单位为压力的标量

所连接热液体网络外部环境的绝对压力。默认值对应于地球标准大气压。

### **Valid pressure-temperature region parameterization** — 压力-温度有效区域的规定方法 `Specified minimum and maximum values`（默认）| `Validity matrix`

压力-温度有效区域的规定方法。您可以指定方形压力-温度区域的限值，或为任意形状的压力-温度区域指定有效性值矩阵。

#### 依赖关系

此参数仅在 **Table dimensions** 参数设置为 `2D vectors based on temperature and pressure (T,p)` 时有效。

### **Minimum valid temperature** — 模型中允许的最低温度 `273.16 K`（默认）| 单位为温度的标量

所连接热液体网络在仿真期间允许达到的最低温度。

### **Maximum valid temperature** — 模型中允许的最高温度 `373.16 K`（默认）| 单位为温度的标量

所连接热液体网络在仿真期间允许达到的最高温度。

### **Minimum valid pressure** — 模型中允许的最低压力 `0.01 MPa`（默认）| 单位为压力的标量

所连接热液体网络在仿真期间允许达到的最低压力。

### **Maximum valid pressure** — 模型中允许的最高压力 `50 MPa`（默认）| 单位为压力的标量

所连接热液体网络在仿真期间允许达到的最高压力。

### **Pressure-temperature validity matrix** — 允许和不允许的压力-温度条件矩阵 11×12 的零和一矩阵（默认）| 无量纲 *M*×*N* 矩阵

各种温度-压力数据点的有效性值矩阵。值 `1` 表示有效点，值 `0` 表示无效点。

#### 依赖关系

此参数仅在 **Valid pressure-temperature region parameterization** 参数设置为 `Validity matrix` 时有效。

### **Pressure and temperature outside valid range** — 当压力或温度超出有效范围时是否发出通知 `Error`（默认）| `Warning` | `None`

选择当流体压力或温度在仿真期间超出有效范围时会发生什么：

- `None` ― 如果属性超出范围，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

#### 密度

### **Density parameterization** — 流体密度的指定方法 `Density, bulk modulus and thermal expansion tables - rho(T,p), beta(T,p), alpha(T,p)`（默认）| `Density table - rho(T,p)` | `Reference density` | `Density vector - rho(T)`

热液体的密度指定方法。密度可以是温度和压力的函数，也可以仅是温度的函数。

### **Density table, rho(T,p)** — 在指定温度和压力下的流体密度矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为质量/体积

在 **Temperature and Pressure** 部分提供的温度和压力下指定的表格密度数据。每一行对应不同的温度，每一列对应不同的压力。

### **Density vector, rho(T)** — 在指定温度下的流体密度向量 11 元素列向量（默认）| *M* 元素向量，单位为质量/体积

在 **Temperature and Pressure** 部分提供的温度下指定的表格密度数据。每个元素对应不同的温度。忽略密度对压力的依赖性。

### **Isothermal bulk modulus table, beta(T,p)** — 在指定温度和压力下的等温体积模量矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为压力

在 **Temperature and Pressure** 部分提供的温度和压力下指定的等温体积模量表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Isobaric thermal expansion coefficient table, alpha(T,p)** — 在指定温度和压力下的等压热膨胀系数矩阵 11×12 矩阵（默认）| *M*×*N* 矩阵，单位为 1/温度

在 **Temperature and Pressure** 部分提供的温度和压力下指定的等压热膨胀系数表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Reference density** — 已知工况下的密度 `998.21 kg/m^3`（默认）| 标量，单位为质量/体积

热液体在已知工作点处的密度。模块使用此数据得出密度作为压力和温度函数的解析表达式。

### **Reference temperature** — 已知工况下的温度 `293.16 K`（默认）| 标量，单位为温度

热液体在已知工作点处的温度。模块使用此数据得出密度作为压力和温度函数的解析表达式。

### **Reference pressure** — 已知工况下的压力 `0.101325 MPa`（默认）| 标量，单位为压力

热液体在已知工作点处的压力。模块使用此数据得出密度作为压力和温度函数的解析表达式。

### **Constant isothermal bulk modulus** — 已知工况下的等温体积模量 `2.1791 GPa`（默认）| 标量，单位为压力

热液体在已知工作点处的等温体积模量。模块使用此数据得出密度作为压力和温度函数的解析表达式。

### **Constant isobaric thermal expansion coefficient** — 已知工作条件下的等压热膨胀系数 `2.0691e-4 1/K`（默认）| 单位为 1/温度的标量

热液体在已知工作点下的等压热膨胀系数。该模块使用此数据推导密度作为压力和温度函数的解析表达式。

#### Internal Energy

### **Internal energy parameterization** — 流体比内能的指定方法 `Specific internal energy and specific heat tables - u(T,p), cp(T,p)`（默认）| `Specific internal energy table - u(T,p)` | `Specific heat table - cp(T,p)`

热液体比内能的指定方法。比内能可以是温度和压力的函数，也可以仅是温度的函数。它也可以根据你代替比内能指定的比热数据来计算。

### **Specific internal energy table, u(T,p)** — 指定温度和压力下的比内能矩阵 11×12 矩阵（默认）| 单位为 能量/质量 的 *M*×*N* 矩阵

在 **Temperature and Pressure** 部分提供的温度和压力下的比内能表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Specific internal energy vector, u(T)** — 指定温度下的比内能向量 11 元素向量（默认）| 单位为 能量/质量 的 *M* 元素向量

在 **Temperature and Pressure** 部分提供的温度下的比内能表格数据。每个元素对应不同的温度。忽略比内能对压力的依赖性。

### **Specific heat at constant pressure table, cp(T,p)** — 指定温度和压力下的比热矩阵 11×12 矩阵（默认）| 单位为 能量/(质量\*温度) 的 *M*×*N* 矩阵

在 **Temperature and Pressure** 部分提供的温度和压力下的比热表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Specific heat at constant pressure vector, u(T)** — 指定温度下的比热向量 11 元素向量（默认）| 单位为 能量/(质量\*温度) 的 *M* 元素向量

在 **Temperature and Pressure** 部分提供的温度下的比热表格数据。每一行对应不同的温度。忽略比热对压力的依赖性。

#### Viscosity and Conductivity

### **Kinematic viscosity table, nu(T,p)** — 指定温度和压力下的运动粘度矩阵 11 元素向量（默认）| 单位为 面积/时间 的 *M* 元素向量

在 **Temperature and Pressure** 选项卡提供的温度和压力下的运动粘度表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Thermal conductivity table, K(T,p)** — 指定温度和压力下的热导率矩阵 11 元素向量（默认）| 单位为 功率/(长度\*温度) 的 *M* 元素向量

在 **Temperature and Pressure** 部分提供的温度和压力下的热导率表格数据。每一行对应不同的温度，每一列对应不同的压力。

### **Kinematic viscosity vector, nu(T)** — 指定温度下的运动粘度向量 11×12 矩阵（默认）| 单位为 面积/时间 的 *M*×*N* 矩阵

在 **Temperature and Pressure** 部分提供的温度下的运动粘度表格数据。每一行对应不同的温度。忽略运动粘度对压力的依赖性。

### **Thermal conductivity vector, K(T)** — 指定温度下的热导率向量 11×12 矩阵（默认）| 单位为 power/(length\*temperature) 的 *M*×*N* 矩阵

在 **Temperature and Pressure** 部分提供的温度下的热导率表格数据。每一行对应一个不同的温度。热导率对压力的依赖性被忽略。
## 所属库

Simscape / Foundation Library / Thermal Liquid / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2025a：调整默认参数值以匹配域

在 R2025a 中，默认参数值已调整以匹配域文件中的对应值：

- **Maximum valid temperature** 从 `363.16 K` 改为 `373.16 K`。
- **Minimum valid pressure** 从 `0.05 MPa` 改为 `0.01 MPa`。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **Pressure and temperature outside valid range** 参数来控制仿真期间流体属性超出范围时的模块行为。

## 描述

热液体的物理属性

Thermal Liquid Settings (TL) 模块为热液体网络提供流体的物理属性。这些属性是全局的：它们不适用于某一个组件，而是适用于构成网络的所有组件。模型中的每个热液体网络必须恰好连接到此模块的一个实例。此模块中指定的属性包括：

- 热力学属性 — 密度、比内能和比热
- 导数属性 — 体积模量和热膨胀系数
- 输运属性 — 运动粘度和热导率

每个流体属性都以表格形式针对温度和压力或仅针对温度指定。如果已知压力引起的变化可忽略、如果预期压力几乎恒定，或者如果流体属性数据只能以温度形式获取，则使用忽略压力引起变化的选项。

### 数据可视化

该模块提供在其温度和压力域上绘制指定流体属性的选项。要创建绘图，请右键单击该模块并选择 **Foundation Library** > **Plot Fluid Properties**。使用绘图顶部的下拉列表选择要可视化的流体属性。在模块参数更新后，单击 **Reload** 按钮重新生成绘图。

使用绘图来可视化流体属性对压力和温度的依赖性——例如，更容易发现指定数据中的异常。大多数流体属性仅在指定为压力的函数时才显示为随压力变化。例外包括密度，它从体积模量和热膨胀系数推导出压力依赖性，以及任何由密度计算的属性，例如比热。

**Thermal Liquid Properties Plot**

### 参数化

该模块为独立状态变量、密度和比内能提供了多种参数化方式。你为每一项选择的参数化方式决定了你必须获取的数据，以及你必须针对哪些状态变量来指定这些数据。**表维度**参数的设置会影响你在其他选项卡中看到的参数。

**压力和温度**

压力和温度是热液体域的*跨量*变量。因此，它们是用于指定所有其他流体性质的独立状态变量的自然选择。该模块提供了两种基于这些状态变量的参数化方式。它们可通过**表维度**参数获得：

- `基于温度和压力的二维表` — 提供同时针对温度和压力的表格数据。有效温度和压力区域通过最小值和最大值（图中的 **I**）或通过有效性矩阵（**II**）来指定。

  **有效性区域类型**
- `基于温度的一维向量` — 提供针对温度的表格数据，并忽略对压力的任何依赖性。有效温度和压力区域仅通过最小值和最大值来指定。体积模量为密度以及任何由密度计算得到的流体性质提供了压力依赖性。

**密度和导数**

该模块为密度以及密度计算通常依赖的两个导数参数——等温体积模量和等压热膨胀系数——提供了三种参数化方式。选项包括：

- `密度、体积模量和热膨胀系数表` — 提供密度、体积模量和热膨胀系数的表格数据。数据必须同时针对温度和压力指定。**表维度**参数必须设置为 `基于温度和压力的二维表`。
- `密度表/向量` — 提供针对温度（在二维情况下还包括压力）的密度表格数据。该模块使用有限差分法从表格数据计算等温体积模量和等压热膨胀系数。等温体积模量 *β* 定义为：

  1β=1ρ(∂ρ∂p)T,

  其中 *ρ* 是密度，*T* 是温度，*p* 是压力。等压热膨胀系数 *α* 定义为：

  α=−1ρ(∂ρ∂T)p.
- `参考密度` — 提供在已知温度（在二维情况下还包括压力）下的密度、体积模量和热膨胀系数。该模块使用解析表达式来计算其他温度和压力下的密度。计算基于以下表达式：

  ln(ρρR)=−α(T−TR)+p−pRβ,

  其中下标 R 表示参考量（在模块对话框中指定）。

**比内能**

与密度的情况一样，该模块为比内能以及可由其计算得到的相关量——比热——提供了三种参数化方式。选项包括：

- `比内能和比热表` — 提供比内能和比热系数的表格数据。数据必须同时针对温度和压力指定。**表维度**参数必须设置为 `基于温度和压力的二维表`。
- `比内能表/向量` — 提供针对温度（在二维情况下还包括压力）的比内能表格数据。该模块从比内能数据计算比热系数。计算基于以下表达式：

  cp(T,p)=(∂u∂T)p+pαρ,

其中 *c*p 是比热容系数，*u* 是比内能。
- `Specific heat coefficient table/vector`
  — 提供比热容系数随温度（在二维情况下还包括压力）变化的表格数据。该模块根据比热容系数数据计算比内能。
  计算基于以下表达式：

  u(T,p)=∫TRT(cp(T,p)−pα(T,p)ρ(T,p))dT+uR，

  其中下标 R 表示参考量。*u*R 的值设为零，这是一个合适的选择，因为对于仿真而言，相关的是比内能的差值，而不是其绝对值。*u* 的值可能与其他来源（如 REFPROP 流体数据库）提供的值不同。

### 定容比热

定容比热 *c*v 必须大于零。该模块从其他流体属性推导出该量：

cv=cp−Tα2βρ。

如果您收到警告提示定容比热必须大于零，该方程可以帮助您理解如何通过调整提供给模块的流体属性来避免出现负的 *c*v 值。

您还可以使用数据可视化绘图。右键单击该模块，选择 **Foundation Library** > **Plot Fluid Properties**，然后从绘图顶部的下拉列表中选择 **Specific Heat at Constant Volume (kJ/(K\*kg))**。如果 *c*v 仅在绘图中的一小块压力和温度区域内为负，并且您不在该区域内仿真模型，则可以从流体属性表中删除这些压力和温度范围。
