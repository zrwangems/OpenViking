---
type: simulink-block
title: 'Articulated Steering MPPI Controller'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Offroad Autonomy for Heavy Machinery'
documentation_page: 'articulatedsteeringmppicontroller'
documentation_source_path: 'ref/articulatedsteeringmppicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Articulated Steering MPPI Controller

## 端口

### 输入

### **State** — 车辆四元向量状态

车辆的全局 *xy* 位置、前车身朝向和转向角，指定为形式为 [*x y theta gamma*] 的四元向量，取有限实数值。全局 *xy* 位置以米为单位。前车身朝向 `theta` 和铰接角 `gamma` 以弧度为单位。铰接角定义为前车身相对于后车身的转向。

**数据类型：** `double`

### **Control** — 车辆当前控制命令二元向量

车辆的当前控制命令，指定为取有限实数值的二元向量。

对于铰接转向车辆模型运动，控制命令为 [*v* *gammaDot*]。*v* 是车辆沿运动方向的速度，以米/秒为单位。*gammaDot* 是转向角速率，以弧度/秒为单位。

**数据类型：** `double` | `numeric`

### **Reference Path** — 要跟随的参考路径 *N*×3 矩阵

要跟随的参考路径，指定为 *N*×3 矩阵，其中每一行表示路径上的一个位姿。

**数据类型：** `double` | `numeric`

### **Vehicle Speed Range** — 最小和最大车辆速度 `[-5 10]` (default) | 二元向量

车辆速度范围是一个二元向量，提供最小和最大车辆速度 [*MinSpeed MaxSpeed*]，取有限实数值，以米/秒为单位。

#### 依赖关系

要启用此端口，请在 **Vehicle** 选项卡上选择 **Specify Vehicle Speed (m/s) Range from input port** 参数。

**数据类型：** `double`

### **Max Steering Rate** — 最大转向角速率 `0.784` (default) | 正数值标量

前车身相对于后车身的最大转向角速率 *gammaDot*，以弧度/秒为单位。如果输入转向速率超过最大转向角速率，则将其限制为最大转向角速率。

#### 依赖关系

要启用此端口，请在 **Vehicle** 选项卡上选择 **Specify Maximum Steering Rate (rad/s) from input port** 参数。

**数据类型：** `double`

### 输出

### **Control Commands** — 车辆的最优控制命令二元向量

车辆的最优控制命令，指定为二元数值向量。

对于铰接车辆模型运动，控制命令为 [*v* *gammaDot*]。*v* 是车辆沿运动方向的速度，以米/秒为单位。*gammaDot* 是转向角速率，以弧度/秒为单位。

**数据类型：** `double`

### **Optimal Path** — 车辆的最优轨迹 *N*×4 矩阵

车辆的最优轨迹，返回为 *N*×4 矩阵，其中每一行的形式为 [*x* *y* *θ* *γ*]。

*N* 是沿轨迹的状态数量。*x* 是当前 *x* 坐标，以米为单位。*y* 是当前 *y* 坐标，以米为单位。*θ* 是车辆当前前车身朝向角，以弧度为单位。*γ* 是车辆的转向角，以弧度为单位。矩阵的每一行表示沿最优轨迹的车辆状态。

**数据类型：** `double`

### **Solution Info** — 额外信息标量 (bus)

额外信息，返回为标量 (bus)，包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `HasReachedGoal` | 指示车辆是否已在目标容差内成功到达参考路径的最后一个位姿，如果成功则返回 `true`。否则，该值为 `false`。 |
| `ExitFlag` | 指示退出条件的标量值。  - `0` — 输出的控制序列和轨迹可行。 - `1` — 由于约束违反，输出的控制序列和轨迹不可行。 - `2` — 在车辆模型以最大前进速度行驶时，下一个参考路径位姿比车辆在指定前视时间内能够覆盖的距离更远。 |

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 常规

配置各种路径跟随参数，引导控制器使车辆准确跟随所需路径。

#### 路径跟随参数

### **Goal Tolerance** — 目标位姿周围的容差 `[1 1 0.1]` (default) | 三元向量

目标位姿周围的容差，指定为形式为 [*x* *y* *θ*] 的三元向量。*x* 和 *y* 分别表示机器人在 *x* 和 *y* 方向上的位置。单位为米。*θ* 是车辆的前车身朝向角，以弧度为单位。该值指定规划器可以认为机器人已到达目标位姿时距目标位姿的最大距离。

### **Lookahead Time** — 用于轨迹规划的前视时间，以秒为单位 4 (default) | 正数值标量

用于轨迹规划的前视时间，以秒为单位，指定为正数值标量。

车辆模型确定车辆的最大前进速度。控制器的前视时间乘以车辆的最大前进速度，得到控制器的前视距离。

控制器的前视距离是控制器必须为其优化局部路径的距车辆当前位姿的距离。前视距离决定控制器在一次局部路径规划迭代中从当前位姿开始考虑的全局参考路径段。距当前位姿一个前视距离处的参考路径位姿是前视点，当前位姿与前视点之间的所有参考路径位姿都是前视位姿。

增大前视时间会使控制器生成更远未来的控制量，使车辆能够更早对未看见的障碍物做出反应，但代价是计算时间增加。相反，较小的前视时间会减少对新未知障碍物做出反应的可用时间，但使控制器能够以更快的速率运行。

#### 模块参数

### **Sample Time (s)** — 模块在仿真期间更新时的时间间隔，以秒为单位 `0.1` (default) | 数值

模块在仿真期间更新时的时间间隔，以秒为单位，指定为数值。对于离散执行，请使用正标量；或使用 -1 从上游模块继承。为确保最佳性能，必须确保与其他模型组件保持一致。

### **Simulate using** — 要运行的仿真类型 `Code generation` (default) | `Interpreted execution`

指定要运行的仿真类型。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不更改，后续仿真将重用该 C 代码。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

**可调：** No

### 车辆

为 `articulatedSteeringKinematics` 车辆模型指定车辆规格、限制和其他属性。

#### 车辆规格

### **Front Angle Offset (m)** — 从铰接关节到前轴的长度 `4` (default) | 正数值标量

前角度偏移是指从铰接关节到前轴的长度，以米为单位。

### **Rear Angle Offset (m)** — 从铰接关节到后轴的长度 `6` (default) | 正数值标量

后角度偏移是指从铰接关节到后轴的长度，以米为单位。

### **Maximum Steering Angle** — 最大转向角 `pi/4` (default) | 正数值标量

前车身相对于后车身的最大转向角，以弧度为单位。

#### 车辆限制

### **Vehicle Speed Range (m/s)** — 最小和最大车辆速度 `[-5, 10]` (default) | 二元向量

车辆速度范围是一个二元向量，提供最小和最大车辆速度 [*MinSpeed MaxSpeed*]，以米/秒为单位。

### **Maximum Steering Rate (rad/s)** — 最大车辆转向速率 `0.7854` (default) | 二元向量

前车身相对于后车身的最大转向角速率 *gammaDot*，以弧度/秒为单位。如果输入转向速率超过最大转向角速率，则将其限制为最大转向角速率。

#### 从输入端口指定车辆属性

### **Specify Vehicle Speed (m/s) Range from input port** — 铰接转向车辆模型的最小和最大速度 `off` (default) | `on`

选择此参数可在 **Vehicle Speed Range** 输入端口指定铰接转向车辆模型的速度范围。启用此选项会从模块封装中移除 **Vehicle Speed Range (m/s)** 参数。

### **Specify Maximum Steering Rate (rad/s) from input port** — 铰接转向车辆模型的最大转向速率 `off` (default) | `on`

选择此参数可在 **Max Steering Rate** 输入端口指定铰接转向车辆模型的最大转向速率。启用此选项会从模块封装中移除 **Maximum Steering Rate (rad/s)** 参数。

### 控制器

为 MPPI Controller 指定各种参数，MPPI Controller 用于 Articulated Steering MPPI Controller 模块中自行车车辆模型的运动规划。

#### 成本权重

### **Path Alignment Weight** — 与参考路径的前视位姿对齐的权重 1 (default) | 非负标量

与参考路径的前视位姿对齐的权重，指定为非负标量。

### **Path Following Weight** — 紧密跟随前视点的权重 1 (default) | 非负标量

紧密跟随前视点的权重，指定为非负标量。

### **Control Smoothness Weight** — 平滑控制动作的权重 1 (default) | 非负标量

为获得最优轨迹而对控制动作进行平滑的权重，指定为非负标量。

#### 轨迹生成参数

### **Number of trajectories** — 采样轨迹的数量 `500` (default) | 正整数

采样轨迹的数量，指定为正整数。

控制器通过对候选轨迹的控制量进行加权平均来计算最优轨迹，权重由各候选轨迹的相关成本确定。

较多的轨迹数量可以更彻底地搜索轨迹空间并可能获得更好的解，但代价是计算时间增加。

### **Time Step (s)** — 轨迹连续状态之间的时间，以秒为单位 `0.1` (default) | 正标量

轨迹连续状态之间的时间，以秒为单位，指定为正标量。较小的值会带来更精确的轨迹预测，但会增加计算时间。

### **Standard Deviation** — 车辆输入的标准差 `[2 0.5]` (default) | 二元数值向量

车辆输入的标准差，指定为具有非负值的二元数值向量。对于铰接转向车辆模型，默认值为 `[2 0.5]`。

向量的每个元素指定车辆模型某个控制输入（例如转向或速度）的标准差。每个模型有两个控制输入。通过在轨迹采样期间向控制输入引入这种变化，控制器可以更好地探索不同的可能轨迹。较大的标准差使控制器能够考虑控制输入中的不确定性，并实现更真实的轨迹预测。

### **Trajectory Selection Bias (λ)** — 最优轨迹的选择性 `1000` (default) | 正标量

最优轨迹的选择性，指定为正标量。

指定接近 `0` 的值，以倾向于将成本最低的轨迹作为最优轨迹。指定较大的值，以倾向于将所有采样轨迹的平均值作为最优轨迹。

此参数调整 MPPI 算法对成本差异的敏感度，作为影响候选轨迹权重的缩放因子。

## 所属库

Offroad Autonomy Library / Vehicle Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025b 中引入**

## 描述

使用模型预测路径积分 (MPPI) 控制铰接转向车辆模型的运动规划

Articulated Steering MPPI Controller 模块使您能够为使用 `articulatedSteeringKinematics` 对象建模的车辆规划局部路径。该模块使用模型预测路径积分 (MPPI) 算法并跟随参考路径，该参考路径通常由全局规划器（如 RRT\* 或 Hybrid A\*）生成。

铰接转向车辆模型表示具有铰接关节和两个车轴的车辆。前轴位于距铰接关节由 **Front Angle Offset (m)** 参数指定的偏移处。后轴位于距铰接关节由 **Rear Angle Offset (m)** 参数指定的偏移处。铰接关节是主动的，这意味着通过控制前车身与后车身之间的铰接角来实现转向。车辆状态定义为四元向量 [*x* *y* *theta* *gamma*]，其中前轴中点的坐标 *xy* 以米为单位，前车身朝向 *theta* 以及铰接角或转向角 *gamma* 以弧度为单位。铰接角定义为前车身相对于后车身的转向。

MPPI 控制器在模块采样时间运行。每次更新时，控制器采样控制序列，传播这些控制序列以生成潜在轨迹，使用成本函数评估轨迹，并计算最优控制命令。为获得最佳性能，必须以高频率运行控制器。
