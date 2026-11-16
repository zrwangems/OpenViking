---
type: simulink-block
title: 'Minimum Snap Polynomial Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'minimumsnappolynomialtrajectory'
documentation_source_path: 'ref/minimumsnappolynomialtrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Minimum Snap Polynomial Trajectory

## 端口

### 输入

### **Time** — 沿轨迹的时间点 标量 | 向量

沿轨迹的时间点，指定为标量或向量。

- 当时间指定为标量时，此值与仿真时间同步，并用于指定对轨迹采样的时间点。模块在该时刻输出轨迹变量的向量。
- 如果时间指定为向量，模块输出矩阵，其中每一列对应于该向量的每个元素。

**数据类型：** `single` | `double`

### **Waypoints** — 沿轨迹的路点位置 *n*×*p* 矩阵

给定时间点处轨迹的路点位置，指定为 *n*×*p* 矩阵。*n* 是轨迹的维度，*p* 是路点数量。

**数据类型：** `single` | `double`

### **TimePoints** — 轨迹路点的时间点 *p* 元素行向量

轨迹路点的时间点，指定为 *p* 元素行向量。*p* 是路点数量。

**数据类型：** `single` | `double`

### **VelBC** — 路点的速度边界条件 *n*×*p* 矩阵

路点的速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹对应维度（共 *n* 个维度）在每个 *p* 路点处的速度边界。

默认情况下，模块在边界路点处使用值 `0`，在中间路点处使用 `NaN`。

#### 依赖关系

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### **AccelBC** — 路点的加速度边界条件 *n*×*p* 矩阵

路点的加速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹对应维度（共 *n* 个维度）在每个 *p* 路点处的加速度边界。

默认情况下，模块在边界路点处使用值 `0`，在中间路点处使用 `NaN`。

#### 依赖关系

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### **JerkBC** — 路点的加加速度边界条件 *n*×*p* 矩阵

路点的加加速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹对应维度（共 *n* 个维度）在每个 *p* 路点处的加加速度边界。

默认情况下，模块在边界路点处使用值 `0`，在中间路点处使用 `NaN`。

#### 依赖关系

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### **SnapBC** — 路点的加加加速度边界条件 *n*×*p* 矩阵

路点的加加加速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹对应维度（共 *n* 个维度）在每个 *p* 路点处的加加加速度边界。

默认情况下，模块在边界路点处使用值 `0`，在中间路点处使用 `NaN`。

#### 依赖关系

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### 输出

### **q** — 轨迹的位置 *n* 元素向量 | *n*×*m* 矩阵

轨迹的位置，返回为 *n* 元素向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qd** — 轨迹的速度 *n* 元素向量 | *n*×*m* 矩阵

轨迹的速度，返回为 *n* 元素向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qdd** — 轨迹的加速度 *n* 元素向量 | *n*×*m* 矩阵

轨迹的加速度，返回为 *n* 元素向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qddd** — 轨迹的加加速度 *n* 元素向量 | *n*×*m* 矩阵

轨迹的加加速度，返回为 *n* 元素向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qdddd** — 轨迹的加加加速度 *n* 元素向量 | *n*×*m* 矩阵

轨迹的加加加速度，返回为 *n* 元素向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **TimeOfArrival** — 每个路点的到达时间 *p* 元素向量

每个路点的到达时间，返回为 *p* 元素向量。*p* 是路点数量。

**数据类型：** `single` | `double`

### **PolynomialCoefs** — 多项式系数 *n*(*p*`–``1`)×`10` 矩阵

多项式系数，返回为 *n*(*p*`–``1`)×`10` 矩阵。*n* 是轨迹的维度，*p* 是路点数量。每组 *n* 行定义用于描述每个变量轨迹的多项式的系数。

#### 依赖关系

要启用此输出端口，请选择 `Show polynomial coefficients output port`。

**数据类型：** `single` | `double`

### **Status** — 轨迹生成的状态 形如 `[SingularityStatus MaxIterStatus MaxTimeStatus]` 的三元素向量

轨迹生成的状态，返回为形如 `[SingularityStatus MaxIterStatus MaxTimeStatus]` 的三元素向量。

*SingularityStatus* 返回为 `0` 或 `1`，指示是否出现奇异。如果出现奇异，请减小 `Maximum segment time` 与 `Minimum segment time` 的比值。

*MaxIterStatus* 返回为 `0` 或 `1`，指示求解器的迭代次数是否已超过 `Maximum iterations`。

*MaxTimeStatus* 返回为 `0` 或 `1`，指示求解器的时间限制是否已超过 `Maximum time`。

#### 依赖关系

要启用此输出端口，请选择 `Show status output port`。

**数据类型：** `uint8`

## 参数

### **Show boundary conditions input ports** — 接受边界条件输入 `off`（默认） | `on`

选择此参数以分别在 `VelBC`、`AccelBC`、`JerkBC` 和 `SnapBC` 端口输入速度、加速度、加加速度和加加加速度边界条件。

**可调：** 否

### **Show polynomial coefficients output port** — 输出多项式系数 `off`（默认） | `on`

选择此参数以在 `PolynomialCoefs` 端口输出多项式系数。

**可调：** 否

### **Show status output port** — 输出状态 `off`（默认） | `on`

选择此参数以在 `Status` 端口输出状态。

**可调：** 否

### **Time allocation** — 启用时间分配 `off`（默认） | `on`

启用以使用 `Time weight`、`Minimum segment time`、`Maximum segment time`、`Maximum iterations` 和 `Maximum time` 参数为轨迹指定时间分配。

**可调：** 否

### **Time weight** — 时间分配的权重 `100`（默认） | 正标量

时间分配的权重，指定为正标量。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 `Time allocation`。

### **Minimum segment time** — 最小时间段长度 `0.1`（默认） | 正标量 | (*p*`–``1`) 元素正行向量

最小时间段长度，指定为正标量或 (*p*`–``1`) 元素正行向量。*p* 是路点数量。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 `Time allocation`。

### **Maximum segment time** — 最大时间段长度 `1`（默认） | 正标量 | (*p*`–``1`) 元素正行向量

最大时间段长度，指定为正标量或 (*p*`–``1`) 元素正行向量。*p* 是路点数量。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 `Time allocation`。

### **Maximum iterations** — 求解器的最大迭代次数 `1500`（默认） | 正整数标量

求解器的最大迭代次数，指定为正整数标量。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 `Time allocation`。

### **Maximum time** — 求解器的最大时间 `10`（默认） | 正标量

求解器的最大时间，指定为正标量。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 `Time allocation`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

## 所属库

UAV Toolbox / Algorithms Robotics System Toolbox / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022a 中引入**

## 描述

生成通过多个路点的最小加加加速度多项式轨迹

Minimum Snap Polynomial Trajectory 模块生成最小加加加速度多项式轨迹，这些轨迹在时间点中指定的时间通过路点。该模块基于 `Time` 输入输出用于实现此轨迹的位置、速度、加速度、加加速度、加加加速度和到达时间。

该模块还接受路点的边界条件。该模块还输出多项式的系数和轨迹生成的状态。

在 `TimePoints` 输入定义的时间段之外，轨迹的位置、速度、加速度、加加速度和加加加速度的初始值和最终值保持恒定。
