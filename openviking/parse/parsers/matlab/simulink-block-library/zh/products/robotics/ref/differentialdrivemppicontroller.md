---
type: simulink-block
title: 'Differential Drive MPPI Controller'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Offroad Autonomy for Heavy Machinery'
documentation_page: 'differentialdrivemppicontroller'
documentation_source_path: 'ref/differentialdrivemppicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential Drive MPPI Controller

## 端口

### 输入

### **State** — 车辆位姿三元素向量

车辆的当前位置和方向，指定为 [*x y
theta*] 向量，以 meters 和 radians 为单位。

**数据类型：** `double`

### **Control** — 车辆当前控制指令二元素向量

车辆的当前控制指令，指定为二元素 numeric 向量，其形式取决于 **Vehicle** 选项卡上 **Vehicle Input
Type** 参数中指定的运动模型。

对于差速驱动车辆模型运动，在 **Vehicle Input Type** 参数中指定的这些值决定控制指令的格式：

- `Wheel Speeds` — [*wheelL*
  *wheelR*]
- `Vehicle Speed & Heading Angular Velocity` —
  [*v*
  *omegaDot*]

*v* 是车辆沿运动方向的速度，以 meters per second 为单位。*omegaDot* 是后轴处的角速度，以 radians per second 为单位。*wheelL* 和 *wheelR* 分别是左轮和右轮速度，以 radians per second 为单位。

**数据类型：** `double`

### **Reference Path** — 要跟随的参考路径 *N*-by-3 矩阵

要跟随的参考路径，指定为 *N*-by-3 矩阵，其中每一行表示路径上的一个位姿。

**数据类型：** `double`

### **Wheel Speed Range** — 车辆最小和最大车轮速度 `[-2, 100]`（默认）| 二元素向量

转向速率范围是一个二元素向量，提供车辆的最小和最大车轮速度 [*MinSpeed MaxSpeed*]，以 radians per second 为单位。

#### 依赖关系

要启用此端口，请在 **Vehicle** 选项卡上选择 **Specify Wheel
Speed (rad/s) Range from input port** 参数。

**数据类型：** `double`
### 输出

### **Control Commands** — 车辆的最优控制指令 1-by-2 行矩阵

车辆的最优控制指令，返回为 1-by-2 矩阵。矩阵的行对应于车辆沿轨迹的某个状态的最优控制。每一列取决于 **Vehicle** 选项卡上 **Vehicle Input
Type** 参数中指定的运动模型。

对于差速驱动车辆模型运动，在 **Vehicle Input Type** 参数中指定的这些值决定控制指令的格式：

- `Wheel Speeds` — [*wheelL*
  *wheelR*]
- `Vehicle Speed & Heading Angular Velocity` —
  [*v*
  *omegaDot*]

*v* 是车辆沿运动方向的速度，以 meters per second 为单位。*omegaDot* 是后轴处的角速度，以 radians per second 为单位。*wheelL* 和 *wheelR* 分别是左轮和右轮速度，以 radians per second 为单位。

**数据类型：** `double`

### **Optimal Path** — 车辆最优路径 *N*-by-3 矩阵

差速驱动车辆模型的最优路径，返回为 *N*-by-3 矩阵，其中每一行的形式为
[*x*
*y*
*θ*]。

*N* 是沿轨迹的状态数。
*x* 是当前 *x* 坐标，以 meters 为单位。
*y* 是当前 *y* 坐标，以 meters 为单位。
*θ* 是车辆当前航向角，以 radians 为单位。矩阵的每一行对应于车辆沿路径的某个状态的最优状态。

**数据类型：** `double`

### **Solution Info** — 额外信息标量 (bus)

额外信息，返回为具有以下字段的标量 (bus)。

| 字段 | 描述 |
| --- | --- |
| `HasReachedGoal` | 指示车辆是否已在目标容差内成功到达参考路径的最后一个位姿；如果成功，则返回 `true`。否则，该值为 `false`。 |
| `ExitFlag` | 指示退出条件的标量值。  - `0` — 输出的控制序列和轨迹可行。 - `1` — 由于约束违反，输出的控制序列和轨迹不可行。 - `2` — 下一个参考路径位姿比车辆模型以最大前进速度在指定前瞻时间内所能覆盖的距离更远。 |

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条中的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property
Inspector**。

### 常规

配置各种路径跟随参数，引导控制器使车辆准确跟随所需路径。

#### 路径跟随参数

### **Goal Tolerance** — 目标位姿周围的容差 `[1 1 0.1]`（默认）| 三元素向量

目标位姿周围的容差，指定为形式为
[*x*
*y*
*θ*] 的三元素向量。*x* 和 *y* 分别表示机器人在 *x*- 和
*y*-方向上的位置。单位是 meters。
*θ* 是机器人的航向角，以 radians 为单位。此值指定规划器可以认为机器人已到达目标位姿的距目标位姿的最大距离。

### **Lookahead Time** — 用于轨迹规划的前瞻时间，以 seconds 为单位 4（默认）| 正 numeric 标量

用于轨迹规划的前瞻时间，以 seconds 为单位，指定为正 numeric 标量。

车辆模型决定车辆的最大前进速度。控制器的前瞻时间乘以车辆的最大前进速度决定控制器的前瞻距离。

控制器的前瞻距离是车辆当前位置到控制器必须优化局部路径的距离。前瞻距离决定控制器在一次局部路径规划迭代中考虑的、从当前位置开始的全局参考路径段。距当前位置一个前瞻距离处的参考路径位姿是前瞻点，当前位置与前瞻点之间的所有参考路径位姿都是前瞻位姿。

增大前瞻时间的值会使控制器向未来更远处生成控制，使车辆能够更早地对未看见的障碍物作出反应，但会增加计算时间。相反，较小的前瞻时间会减少对新的未知障碍物作出反应的可用时间，但使控制器能够以更快的速率运行。

#### 模块参数

### **Sample Time (s)** — 模块在仿真期间更新的时间间隔，以 seconds 为单位 `0.1`（默认）| numeric

模块在仿真期间更新的时间间隔，以 seconds 为单位，指定为 numeric 值。对于离散执行，使用正标量；若要从上游模块继承，则使用 -1。为了获得最佳性能，必须确保与其他模型组件保持一致。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

指定要运行的仿真类型。

- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

**可调：** No

### 车辆

指定 Differential Drive Kinematic Model 的车辆规格、限制和其他属性。

#### 车辆规格

### **Vehicle Input Type** — 车辆速度和方向输入的类型 `Wheel Speeds`（默认）| `Vehicle Speed & Heading Angular Velocity`

模型输入指令的格式，指定为以下选项之一：

- `Wheel Speeds` — 两个车轮的角速度，以 radians per second 为单位。
- `Vehicle Speed & Heading Angular Velocity` —
  车辆速度，以 meters per second 为单位，并带有以 radians per second 为单位的航向角速度。

### **Wheel Radius** — 车辆的车轮半径 `0.05`（默认）| 正 numeric 标量

车辆上车轮的半径，以 meters 为单位指定。

### **Track Width** — 车辆从车轮到车轮的轮距长度 `0.2`（默认）| numeric 标量

从左轮到右轮的轮距长度，以 meters 为单位指定。

#### 车辆限制

### **Wheel Speed Range (rad/s)** — 车辆最小和最大车轮速度 `[-2 100]`（默认）| 二元素向量

车轮速度范围是一个二元素向量，提供车辆的最小和最大车轮速度 [*MinSpeed MaxSpeed*]，以 radians per second 为单位。

#### 从输入端口指定车辆属性

### **Specify Wheel Speed (rad/s) Range from input port** — 车辆最小和最大车轮速度 `off`（默认）| `on`

选择此参数以在 **Wheel Speed Range** 输入端口指定差速驱动车辆模型的车轮速度范围。启用此选项会从模块掩码中移除 **Wheel Speed (rad/s) Range** 参数。

### 控制器

指定用于 Differential Drive MPPI Controller 模块中自行车车辆模型运动规划的 MPPI 控制器的各种参数。

#### 成本权重

### **Path Alignment Weight** — 与前瞻位姿对齐的权重 1（默认）| 非负标量

与参考路径的前瞻位姿对齐的权重，指定为非负标量。

### **Path Following Weight** — 紧密跟随前瞻点的权重 1（默认）| 非负标量

紧密跟随前瞻点的权重，指定为非负标量。

### **Control Smoothness Weight** — 平滑控制动作的权重 1（默认）| 非负标量

平滑控制动作、避免突变变化的权重，指定为非负标量。

#### 轨迹生成参数

### **Number of trajectories** — 采样轨迹数 `500`（默认）| positive integer

采样轨迹数，指定为 positive integer。

控制器通过对候选轨迹的控制求平均来计算最优轨迹，权重由它们关联的成本决定。

更多的轨迹数可导致对轨迹空间进行更彻底的搜索，并可能获得更好的解，但会增加计算时间。

### **Time Step (s)** — 轨迹连续状态之间的时间，以 seconds 为单位 `0.1`（默认）| 正标量

轨迹连续状态之间的时间，以 seconds 为单位，指定为正标量。较小的值会带来更精确的轨迹预测，但会增加计算时间。

### **Standard Deviation** — 车辆输入的标准差 `[0.5 0.5]`（默认）| 二元素 numeric 向量

车辆输入的标准差，指定为具有非负值的二元素 numeric 向量。对于差速驱动车辆模型，默认值为 `[0.5 0.5]`。

向量的每个元素指定车辆模型某个控制输入（如转向或速度）的标准差。每个模型有两个控制输入。通过在轨迹采样期间向控制输入引入此类变化，控制器可以更好地探索不同的可能轨迹。较大的标准差使控制器能够考虑控制输入中的不确定性，并实现更真实的轨迹预测。

### **Trajectory Selection Bias (λ)** — 最优轨迹的选择性 `1000`（默认）| 正标量

最优轨迹的选择性，指定为正标量。

指定接近 `0` 的值，以偏向将成本最低的轨迹作为最优轨迹。指定较大的值，以偏向将所有采样轨迹的平均值作为最优轨迹。

此参数调整 MPPI 算法对成本差异的敏感度，充当影响候选轨迹加权的缩放因子。

## 所属库

Offroad Autonomy Library / Vehicle Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用模型预测路径积分 (MPPI) 控制差速驱动车辆模型的运动规划

Differential Drive MPPI Controller 模块使您能够使用模型预测路径积分 (MPPI) 算法，为 Differential Drive
Kinematic Model 规划局部路径，并跟随通常由全局路径规划器（如 RRT\* 或 Hybrid A\*）生成的参考路径。

该模型近似表示一辆具有单个固定轴、且车轮由 **Track Width**
参数指定的轮距分隔的车辆。每个车轮都可以使用在
**Vehicle Input
Type** 参数中为左轮和右轮分别指定的速度输入独立驱动。车辆速度和航向由轴中心定义。

带有 x、y、theta、velocity、track width 和 wheel radius 标注的差速驱动运动学模型图

在车辆沿参考路径的每个状态处，MPPI 控制器基于车辆的当前状态和控制，为沿参考路径的一小段采样潜在轨迹。控制器使用成本函数评估这些轨迹以平滑路径，并为车辆选择最优轨迹和最优控制。
