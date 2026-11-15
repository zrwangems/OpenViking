---
type: simulink-block
title: 'Ackermann MPPI Controller'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Offroad Autonomy for Heavy Machinery'
documentation_page: 'ackermannmppicontroller'
documentation_source_path: 'ref/ackermannmppicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Ackermann MPPI Controller

## 端口

### 输入

### **State** — 车辆的状态四元素向量

车辆的全局 *xy*-位置、航向角和转向角，指定为形式为 [*x y theta psi*] 的四元素向量。全局 *xy*-位置以 meters 为单位指定，车辆航向角 `theta` 和转向角 `psi` 以 radians 为单位指定。

**数据类型：** `double`

### **Control** — 车辆当前控制指令二元素向量

车辆当前控制指令，指定为二元素数值向量。

对于 Ackermann 车辆模型运动，控制指令为 [*v* *psiDot*]。*v* 是车辆沿运动方向的速度，单位为 meters per second。*psiDot* 是转向角速率，单位为 radians per second。

**数据类型：** `double`

### **Reference Path** — 要跟随的参考路径 *N*-by-3 矩阵

要跟随的参考路径，指定为 *N*-by-3 矩阵，其中每一行表示路径上的一个位姿。

**数据类型：** `double`

### **Vehicle Speed Range** — 车辆最小和最大速度 `[-0.1 5]`（默认） | 二元素向量

车辆速度范围是一个二元素向量，提供车辆的最小和最大速度 [*MinSpeed MaxSpeed*]，单位为 meters per second。

#### 依赖关系

要启用此端口，请在 **车辆** 选项卡上选择 **Specify Vehicle Speed (m/s) Range from input port** 参数。

**数据类型：** `double`

### **Steering Rate Range** — 车辆最小和最大转向速率 `[-0.5, 1]`（默认） | 二元素向量

转向速率范围是一个二元素向量，提供车辆可向右或向左转向的最小和最大速率，单位为 radians per second。

#### 依赖关系

要启用此端口，请在 **车辆** 选项卡上选择 **Specify Steering Rate Range (rad) from input port** 参数。

**数据类型：** `double`
### 输出

### **Control Commands** — 车辆的最优控制指令二元素向量

车辆的最优控制指令，指定为二元素数值向量。

对于 Ackermann 车辆模型运动，控制指令为 [*v* *psi*]。*v* 是车辆沿运动方向的速度，单位为 meters per second。*psi* 是转向角速率，单位为 radians per second。

**数据类型：** `double`

### **Optimal Path** — 车辆的最优轨迹 *N*-by-4 矩阵

车辆的最优轨迹，返回为 *N*-by-4 矩阵，其中每一行的形式为 [*x* *y* *θ* *ψ*]。

*N* 是轨迹上的状态数量。*x* 是当前 *x*-坐标，单位为 meters。*y* 是当前 *y*-坐标，单位为 meters。*θ* 是车辆当前航向角，单位为 radians。*ψ* 是车辆转向角，单位为 radians。矩阵的每一行表示最优轨迹上的车辆状态。

**数据类型：** `double`

### **Solution Info** — 额外信息标量 (bus)

额外信息，返回为标量 (bus)，包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `HasReachedGoal` | 指示车辆是否已在目标容差内成功到达参考路径的最后一个位姿，如果成功则返回 `true`。否则，此值为 `false`。 |
| `ExitFlag` | 指示退出条件的标量值。  - `0` — 输出的控制序列和轨迹可行。 - `1` — 输出的控制序列和轨迹由于约束违反而不可行。 - `2` — 在指定的前视时间内，以车辆模型最大前进速度行驶时，下一个参考路径位姿比车辆能覆盖的距离更远。 |

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 常规

配置各种路径跟随参数，引导控制器使车辆准确跟随期望路径。

#### 路径跟随参数

### **Goal Tolerance** — 目标位姿周围的容差 `[1 1 0.1]`（默认） | 三元素向量

目标位姿周围的容差，指定为形式为 [*x* *y* *θ*] 的三元素向量。*x* 和 *y* 分别表示机器人在 *x*- 和 *y*- 方向上的位置。单位为 meters。*θ* 是机器人的航向角，单位为 radians。此值指定规划器可认为机器人已到达目标位姿时距目标位姿的最大距离。

### **Lookahead Time** — 轨迹规划的前视时间，单位为 seconds 4（默认） | 正数值标量

轨迹规划的前视时间，单位为 seconds，指定为正数值标量。

车辆模型确定车辆的最大前进速度。控制器的前视时间乘以车辆的最大前进速度，确定控制器的前视距离。

控制器的前视距离是控制器必须针对其优化局部路径的、距车辆当前位姿的距离。前视距离确定控制器在局部路径规划的一次迭代中考虑的、从当前位姿开始的那段全局参考路径。距当前位姿一个前视距离处的参考路径位姿是前视点，当前位姿与前视点之间的所有参考路径位姿都是前视位姿。

增大前视时间的值会使控制器生成更远未来的控制，使车辆能够更早对未看见的障碍物作出反应，但代价是计算时间增加。相反，较小的前视时间会减少对新未知障碍物作出反应的可用时间，但使控制器能以更快速率运行。

#### 模块参数

### **Sample Time (s)** — 模块在仿真期间更新的时间间隔，单位为 seconds `0.1`（默认） | numeric

模块在仿真期间更新的时间间隔，单位为 seconds，指定为 numeric 值。对于离散执行，请使用正标量；若要继承上游模块，请使用 -1。为确保最佳性能，必须与其他模型组件保持一致。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

指定要运行的仿真类型。

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

**可调：** No

### 车辆

指定 Ackermann Kinematic Model 的车辆规格、限制及其他属性。

#### 车辆规格

### **Wheel Base** — 前轴与后轴之间的距离 `1`（默认） | 正数值标量

Wheel base 是车辆前轴与后轴之间的距离，单位为 meters。

#### 车辆限制

### **Vehicle Speed Range (m/s)** — 车辆最小和最大速度 `[-0.1, 5]`（默认） | 二元素向量

车辆速度范围是一个二元素向量，提供车辆的最小和最大速度 [*MinSpeed MaxSpeed*]，单位为 meters per second。

### **Steering Rate Range (rad/s)** — 车辆最小和最大转向速率 `[-0.5, 1]`（默认） | 二元素向量

转向速率范围是一个二元素向量，提供车辆可向右或向左转向的最小和最大速率 [*MinSteerRate MaxSteerRate*]，单位为 radians per second。

#### 从输入端口指定车辆属性

### **Specify Vehicle Speed (m/s) Range from input port** — Ackermann 车辆模型的最小和最大速度 `off`（默认） | `on`

选择此参数可在 **Vehicle Speed Range** 输入端口指定 Ackermann 车辆模型的速度范围。启用此选项会从模块掩码中移除 **Vehicle Speed Range (m/s)** 参数。

### **Specify Steering Rate Range (rad) from input port** — Ackermann 车辆模型的最大和最小转向速率 `off`（默认） | `on`

选择此参数可在 **Steering Rate Range** 输入端口指定 Ackermann 车辆模型的最大和最小转向速率。启用此选项会从模块掩码中移除 **Steering Rate Range (rad)** 参数。

### 控制器

指定 MPPI 控制器的各种参数，该控制器用于 Ackermann MPPI Controller 模块中自行车车辆模型的运动规划。

#### 成本权重

### **Path Alignment Weight** — 与前视位姿对齐的权重 1（默认） | 非负标量

与参考路径的前视位姿对齐的权重，指定为非负标量。

### **Path Following Weight** — 紧密跟随前视点的权重 1（默认） | 非负标量

紧密跟随前视点的权重，指定为非负标量。

### **Control Smoothness Weight** — 平滑控制动作的权重 1（默认） | 非负标量

为获得最优轨迹而平滑控制动作的权重，指定为非负标量。

#### 轨迹生成参数

### **Number of trajectories** — 采样的轨迹数量 `500`（默认） | 正整数

采样的轨迹数量，指定为正整数。

控制器通过对候选轨迹的控制进行加权平均来计算最优轨迹，权重由其关联成本确定。

较大的轨迹数量可以更彻底地搜索轨迹空间，并可能获得更好的解，但代价是计算时间增加。

### **Time Step (s)** — 轨迹连续状态之间的时间，单位为 seconds `0.1`（默认） | 正标量

轨迹连续状态之间的时间，单位为 seconds，指定为正标量。较小的值会带来更精确的轨迹预测，但会增加计算时间。

### **Standard Deviation** — 车辆输入的标准差 `[2 0.5]`（默认） | 二元素 numeric 向量

车辆输入的标准差，指定为具有非负值的二元素 numeric 向量。对于 Ackermann 车辆模型，默认值为 `[2 0.5]`。

向量的每个元素指定车辆模型某个控制输入（如转向或速度）的标准差。每个模型有两个控制输入。通过在轨迹采样期间将此类变异性引入控制输入，控制器可以更好地探索不同的可能轨迹。较大的标准差使控制器能够考虑控制输入中的不确定性，并实现更真实的轨迹预测。

### **Trajectory Selection Bias (λ)** — 最优轨迹的选择性 `1000`（默认） | 正标量

最优轨迹的选择性，指定为正标量。

指定接近 `0` 的值，以倾向于将成本最低的轨迹作为最优轨迹。指定较大的值，以倾向于将所有采样轨迹的平均值作为最优轨迹。

此参数调整 MPPI 算法对成本差异的敏感度，充当影响候选轨迹权重的缩放因子。

## 所属库

Offroad Autonomy Library / Vehicle Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用模型预测路径积分 (MPPI) 控制 Ackermann 车辆模型的运动规划

Ackermann MPPI Controller 模块使您能够为 Ackermann Kinematic Model 规划局部路径，遵循通常由全局路径规划器（如 RRT\* 或 Hybrid A\*）生成的参考路径，并使用模型预测路径积分 (MPPI) 算法。

Ackermann 车辆模型表示具有两个轴的车辆，两轴之间的距离由 **Wheel Base** 参数指定。车辆的状态定义为四元素向量 [*x y θ ψ*]，包含全局 *xy-*位置、车辆航向角 *θ* 和转向角 *ψ*。车辆航向角和 *xy*-位置定义在后轴中心。

Ackermann 运动学模型图，标注了 x、y、theta、psi、velocity、wheel base 和 turning radius

在沿参考路径的每个车辆状态处，MPPI 控制器基于车辆的当前状态和控制，为参考路径上的短片段采样潜在轨迹。控制器使用成本函数评估这些轨迹以平滑路径，并为车辆选择最优轨迹和最优控制。
