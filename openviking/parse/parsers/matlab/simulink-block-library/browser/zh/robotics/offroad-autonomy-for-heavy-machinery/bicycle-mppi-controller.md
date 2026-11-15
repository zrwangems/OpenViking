---
type: simulink-block
title: 'Bicycle MPPI Controller'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Offroad Autonomy for Heavy Machinery'
documentation_page: 'bicyclemppicontroller'
documentation_source_path: 'ref/bicyclemppicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Bicycle MPPI Controller

## 端口

### 输入

### **State** — 车辆位姿三元素向量

车辆的当前 *xy* 位置和方向，指定为 *[x y theta]* 向量，单位为 meters 和 radians。

**数据类型：** `double`

### **Control** — 车辆当前控制命令二元素向量

车辆的当前控制命令，指定为二元素数值向量，其形式取决于 **General** 选项卡上 **Vehicle Input Type** 参数所指定的运动模型。

对于 bicycle vehicle model motion，**Vehicle Input Type** 参数中指定的这些值决定控制命令的格式：

- `Vehicle Speed & Steering Angle` — [*v* *psi*]
- `Vehicle Speed & Heading Rate` — [*v* *omegaDot*]

*v* 是沿运动方向的车辆速度，单位为 meters per second。*psi* 是转向角速率，单位为 radians per second。*omegaDot* 是后轴处的角速度，单位为 radians per second。

**数据类型：** `double`

### **Reference Path** — 要跟随的参考路径 *N*-by-3 矩阵

要跟随的参考路径，指定为 *N*-by-3 矩阵，其中每一行表示路径上的一个位姿。

**数据类型：** `double`

### **Vehicle Speed Range** — 车辆最小和最大速度 `[-0.1 5]`（默认）| 二元素向量

车辆速度范围是二元素向量，提供最小和最大车辆速度 [*MinSpeed MaxSpeed*]，单位为 meters per second。

#### 依赖关系

要启用此端口，请在 **Vehicle** 选项卡上选择 **Specify Vehicle Speed (m/s) Range from input port** 参数。

**数据类型：** `double`

### **Maximum Steering Angle** — 车辆可以向左或向右转向的最大量 `pi/4`（默认）| numeric scalar

最大转向角是车辆可以向右或向左转向的最大量，单位为 radians。此端口验证用户提供的状态输入。

如果 **Maximum Steering Angle** 设置为 `pi/2`，则最小转向半径为 zero meters。

#### 依赖关系

要启用此端口，请在 **Vehicle** 选项卡上选择 **Specify Maximum Steering Angle (rad) from input port** 参数。

**数据类型：** `double`

### 输出

### **Control Commands** — 车辆的最优控制命令 1-by-2 行矩阵

车辆的最优控制命令，返回为 1-by-2 行矩阵。矩阵的行对应于车辆沿轨迹某一状态的最优控制。每一列取决于 **Vehicle** 选项卡上 **Vehicle Input Type** 参数所指定的运动模型。

对于 bicycle vehicle model motion，**Vehicle Input Type** 参数中指定的这些值决定控制命令的格式：

- `Vehicle Speed & Steering Angle` — [*v* *psi*]
- `Vehicle Speed & Heading Rate` — [*v* *omegaDot*]

*v* 是沿运动方向的车辆速度，单位为 meters per second。*psi* 是转向角速率，单位为 radians per second。*omegaDot* 是后轴处的角速度，单位为 radians per second。

**数据类型：** `double`

### **Optimal Path** — 车辆的最优路径 *N*-by-3 矩阵

bicycle vehicle model 的最优路径，返回为 *N*-by-3 矩阵，其中每一行的形式为 [*x* *y* *θ*]。

*N* 是沿轨迹的状态数。*x* 是当前 *x*-coordinate，单位为 meters。*y* 是当前 *y*-coordinate，单位为 meters。*θ* 是车辆当前航向角，单位为 radians。矩阵的每一行表示沿最优轨迹的车辆状态。

**数据类型：** `double`

### **Solution Info** — 额外信息标量（bus）

额外信息，返回为具有以下字段的标量（bus）。

| 字段 | 描述 |
| --- | --- |
| `HasReachedGoal` | 指示车辆是否已在 goal tolerance 内成功到达参考路径的最后一个位姿，如果成功则返回 `true`。否则，此值为 `false`。 |
| `ExitFlag` | 指示退出条件的标量值。  - `0` — 输出的控制序列和轨迹可行。 - `1` — 由于约束违反，输出的控制序列和轨迹不可行。 - `2` — 在指定的 lookahead time 内，以车辆模型的最大前向速度行驶时，下一个参考路径位姿超过车辆能够覆盖的距离。 |

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### General

配置各种路径跟随参数，引导控制器确保车辆准确跟随期望路径。

#### 路径跟随参数

### **Goal Tolerance** — 目标位姿周围的容差 `[1 1 0.1]`（默认）| 三元素向量

目标位姿周围的容差，指定为形式为 [*x* *y* *θ*] 的三元素向量。*x* 和 *y* 分别表示机器人在 *x* 和 *y* 方向上的位置。单位为 meters。*θ* 是机器人的航向角，单位为 radians。此值指定规划器可以考虑机器人已到达目标位姿时距目标位姿的最大距离。

### **Lookahead Time** — 用于轨迹规划的前视时间，单位为 seconds 4（默认）| positive numeric scalar

用于轨迹规划的前视时间，单位为 seconds，指定为正数值标量。

车辆模型确定车辆的最大前向速度。控制器的前视时间乘以车辆的最大前向速度，确定控制器的前视距离。

控制器的前视距离是车辆当前位置到控制器必须优化局部路径的位置之间的距离。前视距离确定控制器在一次局部路径规划迭代中考虑的、从当前位置开始的全局参考路径段。距当前位置一个前视距离处的参考路径位姿是前瞻点，当前位置和前瞻点之间的所有参考路径位姿都是前瞻位姿。

增大前视时间的值会使控制器生成更远未来的控制，使车辆能够更早对未看到的障碍物作出反应，但代价是增加计算时间。相反，较小的前视时间会减少对新未知障碍物作出反应的可用时间，但使控制器能够以更快的速率运行。

#### 模块参数

### **Sample Time (s)** — 模块在仿真期间更新时的时间间隔，单位为 seconds `0.1`（默认）| numeric

模块在仿真期间更新时的时间间隔，单位为 seconds，指定为 numeric 值。对离散执行使用正标量，或使用 -1 以从上游模块继承。你必须确保与其他模型组件一致以获得最佳性能。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

指定要运行的仿真类型。

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

**可调：** No

### Vehicle

为 Bicycle Kinematic Model 指定车辆规格、限制和其他属性。

#### 车辆规格

### **Vehicle Input Type** — 车辆速度和方向输入的类型 `Vehicle Speed & Steering Angle`（默认）| `Vehicle Speed & Heading Rate`

车辆速度和方向输入的类型，指定为以下选项之一：

- `Vehicle Speed & Steering Angle` — 车辆速度，单位为 meters per second，以及转向角，单位为 radians。
- `Vehicle Speed & Heading Rate` — 车辆速度，单位为 meters per second，以及航向速率，单位为 radians per second。

### **Wheel Base** — 前轴和后轴之间的距离 `1`（默认）| positive numeric scalar

Wheel base 是车辆前轴和后轴之间的距离，单位为 meters。

#### 车辆限制

### **Vehicle Speed Range (m/s)** — 车辆最小和最大速度 `[-0.1 5]`（默认）| 二元素向量

车辆速度范围是二元素向量，提供最小和最大车辆速度 [*MinSpeed MaxSpeed*]，单位为 meters per second。

### **Maximum Steering Angle (rad)** — 车辆可以向左或向右转向的最大量 `pi/4`（默认）| numeric scalar

最大转向角是指车辆可以向右或向左转向的最大量，单位为 radians。此参数验证用户提供的状态输入。

如果 **Maximum Steering Angle** 设置为 `pi/2`，则最小转向半径为 zero meters。

#### 从输入端口指定车辆属性

### **Specify Vehicle Speed (m/s) Range from input port** — 自行车车辆模型的最小和最大速度 `off`（默认）| `on`

选择此参数可在 **Vehicle Speed Range** 输入端口指定自行车车辆模型的速度范围。启用此选项会从模块封装中移除 **Vehicle Speed (m/s) Range** 参数。

### **Specify Maximum Steering Angle (rad) from input port** — 自行车车辆模型的最大转向半径 `off`（默认）| `on`

选择此参数可在 **Maximum Steering Angle** 输入端口指定自行车车辆模型的最大转向半径。启用此选项会从模块封装中移除 **Maximum Steering Angle (rad)** 参数。

### Controller

指定 MPPI 控制器的各种参数，该控制器用于 Bicycle MPPI Controller 模块中自行车车辆模型的运动规划。

#### 成本权重

### **Path Alignment Weight** — 与前瞻位姿对齐的权重 1（默认）| nonnegative scalar

与参考路径的前瞻位姿对齐的权重，指定为非负标量。

### **Path Following Weight** — 紧密跟随前瞻点的权重 1（默认）| nonnegative scalar

紧密跟随前瞻点的权重，指定为非负标量。

### **Control Smoothness Weight** — 平滑控制动作的权重 1（默认）| nonnegative scalar

平滑控制动作、避免突变的权重，指定为非负标量。

#### 轨迹生成参数

### **Number of trajectories** — 采样的轨迹数 `500`（默认）| positive integer

采样的轨迹数，指定为正整数。

控制器通过对候选轨迹的控制进行平均来计算最优轨迹，权重由候选轨迹的关联成本确定。

更大的轨迹数可以导致对轨迹空间更彻底的搜索以及可能更好的解，但代价是增加计算时间。

### **Time Step (s)** — 轨迹连续状态之间的时间，单位为 seconds `0.1`（默认）| positive scalar

轨迹连续状态之间的时间，单位为 seconds，指定为正标量。较小的值会导致更精确的轨迹预测，但会增加计算时间。

### **Standard Deviation** — 车辆输入的标准差 `[2 0.5]`（默认）| 二元素 numeric 向量

车辆输入的标准差，指定为具有非负值的二元素 numeric 向量。对于自行车车辆模型，默认值为 `[2 0.5]`。

向量的每个元素指定车辆模型某个控制输入的标准差，例如转向或速度。每个模型有两个控制输入。通过在轨迹采样期间向控制输入引入此类变异性，控制器可以更好地探索不同的可能轨迹。更大的标准差使控制器能够考虑控制输入中的不确定性，并实现更真实的轨迹预测。

### **Trajectory Selection Bias (λ)** — 最优轨迹的选择性 `1000`（默认）| positive scalar

最优轨迹的选择性，指定为正标量。

指定接近 `0` 的值以倾向于将成本最低的轨迹作为最优轨迹。指定更大的值以倾向于将所有采样轨迹的平均值作为最优轨迹。

此参数调整 MPPI 算法对成本差异的敏感度，充当影响候选轨迹加权的缩放因子。

## 所属库

Offroad Autonomy Library / Vehicle Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 Model Predictive Path Integral (MPPI) 控制 bicycle vehicle model 的运动规划

Bicycle MPPI Controller 模块使您能够使用 model predictive path integral (MPPI) 算法，为 Bicycle Kinematic Model 规划局部路径，跟随通常由全局路径规划器（如 RRT\* 或 Hybrid A\*）生成的参考路径。

bicycle kinematic model 表示具有两个轴的车辆，两个轴由您在 **Wheel Base** 参数中指定的轴间距离定义。前轮可以使用转向角 `psi` 转动。车辆航向 `theta` 定义在后轴中心。

标注了 x, y, theta, psi, velocity, wheel base 和 turning radius 的 bicycle kinematic model 图

在车辆沿参考路径的每个状态处，MPPI 控制器基于车辆的当前状态和控制，为沿参考路径的短段采样潜在轨迹。控制器使用成本函数评估这些轨迹以平滑路径，并为车辆选择最优轨迹和最优控制。
