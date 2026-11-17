---
type: simulink-block
title: 'Minimum Jerk Polynomial Trajectory'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'minimumjerkpolynomialtrajectory'
documentation_source_path: 'ref/minimumjerkpolynomialtrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Minimum Jerk Polynomial Trajectory

## 端口
```yaml
ports:
- name: Time
  summary: 沿轨迹的时间点 标量 | 向量
  direction: input
  data_types: single | double
- name: Waypoints
  summary: 沿轨迹的路径点位置 *n*×*p* 矩阵
  direction: input
  data_types: single | double
- name: TimePoints
  summary: 轨迹路径点的时间点 *p* 元素行向量
  direction: input
  data_types: single | double
- name: VelBC
  summary: 路径点的速度边界条件 *n*×*p* 矩阵
  direction: input
  data_types: single | double
- name: AccelBC
  summary: 路径点的加速度边界条件 *n*×*p* 矩阵
  direction: input
  data_types: single | double
- name: JerkBC
  summary: 路径点的加加速度边界条件 *n*×*p* 矩阵
  direction: input
  data_types: single | double
- name: q
  summary: 轨迹的位置 *n* 元素向量 | *n*×*m* 矩阵
  direction: output
  data_types: single | double
- name: qd
  summary: 轨迹的速度 *n* 元素向量 | *n*×*m* 矩阵
  direction: output
  data_types: single | double
- name: qdd
  summary: 轨迹的加速度 *n* 元素向量 | *n*×*m* 矩阵
  direction: output
  data_types: single | double
- name: qddd
  summary: 轨迹的加加速度 *n* 元向量 | *n*×*m* 矩阵
  direction: output
  data_types: single | double
- name: TimeOfArrival
  summary: 到达每个路点的时间 *p* 元向量
  direction: output
  data_types: single | double
- name: PolynomialCoefs
  summary: 多项式系数 *n*(*p*–1)×8 矩阵
  direction: output
  data_types: single | double
- name: Status
  summary: 轨迹生成状态，形式为 [SingularityStatus MaxIterStatus MaxTimeStatus] 的三元向量
  direction: output
  data_types: uint8
```

### 输入

### **Time** — 沿轨迹的时间点 标量 | 向量

沿轨迹的时间点，指定为标量或向量。

- 当时间指定为标量时，该值与仿真时间同步，并用于指定轨迹采样的时间点。模块在该时间点输出轨迹变量的向量。
- 如果时间指定为向量，模块输出一个矩阵，其中每一列对应向量的每个元素。

**数据类型：** `single` | `double`

### **Waypoints** — 沿轨迹的路径点位置 *n*×*p* 矩阵

给定时间点处轨迹路径点的位置，指定为 *n*×*p* 矩阵。*n* 是轨迹的维度，*p* 是路径点的数量。

**数据类型：** `single` | `double`

### **TimePoints** — 轨迹路径点的时间点 *p* 元素行向量

轨迹路径点的时间点，指定为 *p* 元素行向量。*p* 是路径点的数量。

**数据类型：** `single` | `double`

### **VelBC** — 路径点的速度边界条件 *n*×*p* 矩阵

路径点的速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹 *n* 的对应维度在 *p* 个路径点中每个路径点处的速度边界。

默认情况下，模块在边界路径点处使用值 `0`，在中间路径点处使用 `NaN`。

#### 依赖

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### **AccelBC** — 路径点的加速度边界条件 *n*×*p* 矩阵

路径点的加速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹 *n* 的对应维度在 *p* 个路径点中每个路径点处的加速度边界。

默认情况下，模块在边界路径点处使用值 `0`，在中间路径点处使用 `NaN`。

#### 依赖

要启用此输入端口，请选择 `Show boundary conditions input ports`。

**数据类型：** `single` | `double`

### **JerkBC** — 路径点的加加速度边界条件 *n*×*p* 矩阵

路径点的加加速度边界条件，指定为 *n*×*p* 矩阵。每一行设置轨迹 *n* 的对应维度在 *p* 个路径点中每个路径点处的加加速度边界。

默认情况下，模块在边界路径点处使用值 `0`，在中间路径点处使用 `NaN`。

#### 依赖

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

### **qddd** — 轨迹的加加速度 *n* 元向量 | *n*×*m* 矩阵

轨迹的加加速度，返回为 *n* 元向量或 *n*×*m* 矩阵。

- 如果为 `Time` 输入指定标量并给出 *n* 维轨迹，则输出为具有 *n* 个元素的向量。
- 如果为 `Time` 输入指定 *m* 元向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **TimeOfArrival** — 到达每个路点的时间 *p* 元向量

到达每个路点的时间，返回为 *p* 元向量。*p* 是路点数量。

**数据类型：** `single` | `double`

### **PolynomialCoefs** — 多项式系数 *n*(*p*`–``1`)×`8` 矩阵

多项式系数，返回为 *n*(*p*`–``1`)×`8` 矩阵。*n* 是轨迹的维度，*p* 是路点数量。每组 *n* 行定义描述每个变量轨迹的多项式的系数。

#### 依赖

要启用此输出端口，请选择 `Show polynomial coefficients output port`。

**数据类型：** `single` | `double`

### **Status** — 轨迹生成状态，形式为 `[SingularityStatus MaxIterStatus MaxTimeStatus]` 的三元向量

轨迹生成状态，返回为形式为 `[SingularityStatus
MaxIterStatus
MaxTimeStatus]` 的三元向量。

*SingularityStatus* 返回为 `0` 或 `1`，表示是否发生奇异。如果发生奇异，请减小 `Maximum segment time` 与 `Minimum segment time` 的比值。

*MaxIterStatus* 返回为 `0` 或 `1`，表示求解器的迭代次数是否超过 `Maximum iterations`。

*MaxTimeStatus* 返回为 `0` 或 `1`，表示求解器的时间是否超过 `Maximum time`。

#### 依赖

要启用此输出端口，请选择 `Show status output port`。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Show boundary conditions input ports
  summary: 接受边界条件输入 off（默认）| on
  group: ''
- name: Show polynomial coefficients output port
  summary: 输出多项式系数 off（默认）| on
  group: ''
- name: Show status output port
  summary: 输出状态 off（默认）| on
  group: ''
- name: Time allocation
  summary: 启用时间分配 off（默认）| on
  group: ''
- name: Time weight
  summary: 时间分配权重 100（默认）| 正标量
  group: ''
- name: Minimum segment time
  summary: 最小时间段长度 0.1（默认）| 正标量 | (*p*–1) 元正行向量
  group: ''
- name: Maximum segment time
  summary: 最大时间段长度 1（默认）| 正标量 | (*p*–1) 元正行向量
  group: ''
- name: Maximum iterations
  summary: 求解器的最大迭代次数 1500（默认）| 正整数标量
  group: ''
- name: Maximum time
  summary: 求解器的最大时间 10（默认值）| 正标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认值）| Code generation
  group: ''
```

### **Show boundary conditions input ports** — 接受边界条件输入 `off`（默认）| `on`

选择此参数可通过 `VelBC`、`AccelBC` 和 `JerkBC` 端口分别输入速度、加速度和加加速度边界条件。

**可调：** 否

### **Show polynomial coefficients output port** — 输出多项式系数 `off`（默认）| `on`

选择此参数可在 `PolynomialCoefs` 端口输出多项式系数。

**可调：** 否

### **Show status output port** — 输出状态 `off`（默认）| `on`

选择此参数可在 `Status` 端口输出状态。

**可调：** 否

### **Time allocation** — 启用时间分配 `off`（默认）| `on`

启用以使用 `Time
weight`、`Minimum segment time`、`Maximum segment time`、`Maximum iterations` 和 `Maximum time` 参数为轨迹指定时间分配。

**可调：** 否

### **Time weight** — 时间分配权重 `100`（默认）| 正标量

时间分配权重，指定为正标量。

**可调：** 否

#### 依赖

要启用此参数，请选择 `Time
allocation`。

### **Minimum segment time** — 最小时间段长度 `0.1`（默认）| 正标量 | (*p*`–``1`) 元正行向量

最小时间段长度，指定为正标量或 (*p*`–``1`) 元正行向量。*p* 是路点数量。

**可调：** 否

#### 依赖

要启用此参数，请选择 `Time
allocation`。

### **Maximum segment time** — 最大时间段长度 `1`（默认）| 正标量 | (*p*`–``1`) 元正行向量

最大时间段长度，指定为正标量或 (*p*`–``1`) 元正行向量。*p* 是路点数量。

**可调：** 否

#### 依赖

要启用此参数，请选择 `Time
allocation`。

### **Maximum iterations** — 求解器的最大迭代次数 `1500`（默认）| 正整数标量

求解器的最大迭代次数，指定为正整数标量。

**可调：** 否

#### 依赖项

要启用此参数，请选择 `Time
allocation`。

### **Maximum time** — 求解器的最大时间 `10`（默认值）| 正标量

求解器的最大时间，指定为正标量。

**可调：** 否

#### 依赖项

要启用此参数，请选择 `Time
allocation`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认值）| `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否
## 所属库

UAV Toolbox / Algorithms Robotics System Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

通过多个路点生成最小加加速度多项式轨迹

Minimum Jerk Polynomial Trajectory 模块生成最小加加速度多项式轨迹，这些轨迹在时间点中指定的时间通过路点。该模块基于 `Time` 输入输出实现此轨迹的位置、速度、加速度、加加速度和到达时间。

该模块还接受路点的边界条件。该模块还输出多项式的系数和轨迹生成的状态。

轨迹的位置、速度、加速度和加加速度的初始值和最终值在 `TimePoints` 输入中定义的时间段之外保持恒定。
