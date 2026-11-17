---
type: simulink-block
title: 'Timed Elastic Band'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'timedelasticband'
documentation_source_path: 'ref/timedelasticband.html'
language: zh-CN
chinese_source: worker-translation
---

# Timed Elastic Band

## 端口

### 输入

### **Pose** — 机器人当前位姿，形式为 [*x* *y* *theta*] 的三元素向量

机器人的当前位姿，指定为形式为
[*x*
*y*
*theta*] 的三元素向量。*x* 和 *y* 以米为单位指定
机器人位置。*theta* 以弧度为单位指定机器人朝向。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Vel** — 机器人当前速度，形式为 [*v* *w*] 的二元素向量

机器人的当前速度，指定为形式为
[*v*
*w*] 的二元素向量。*v* 以米每秒为单位指定机器人的线速度。
*w* 以弧度每秒为单位指定机器人的角速度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MapInfo** — 局部地图信息总线

局部地图信息，指定为总线。该总线包含以下字段：

- `Resolution` - 网格分辨率，指定为以每米单元格数为单位的标量，表示网格位置的数量和大小。
- `GridLocationInWorld` - 网格左下角的世界坐标 [*x*,*y*]，指定为 1×2 向量。
- `OccupancyMatrix` - 占据栅格值，指定为
  *h*×*w* 矩阵。*h* 和
  *w* 由占据栅格对象的
  `GridSize` 属性的两个元素定义。
- `GridSize` - 网格中的行数和列数，指定
  为 1×2 实值向量，按顺序表示行数和列数。
- `GridOriginInLocal` - 网格左下角在局部坐标系中的位置，指定为二元素向量，
  [*xLocal*
  *yLocal*]。

**数据类型：** `bus`

### **RefPath** — 要跟随的参考路径，*N*×3 矩阵

要跟随的参考路径，指定为 *N*×3 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxVel** — 线速度和角速度的最大限制 `[0.8, 1.6]`（默认）| 二元素正向量

速度命令的线速度和角速度最大限制，指定为
二元素正向量。第一个元素是线速度限制，单位为
米每秒，第二个元素是角速度限制，单位为弧度
每秒。

#### 依赖

要启用此输入端口，请在 `Trajectory` 选项卡中选中 **Specify max velocity using
input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxRevVel** — 反向运动的最大速度 `NaN`（默认）| 正标量

车辆反向运动时的最大速度，指定为
正标量。默认值为 `NaN`。当该属性设置为
`NaN` 时，最大反向速度的值与
最大线速度相同。单位为米每秒。

#### 依赖

要启用此输入端口，请在 `Trajectory`
选项卡中选中 **Specify max reverse velocity
using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MaxAccel** — 线加速度和角加速度的最大限制 `[2.4, 4.8]`（默认）| 二元素正向量

速度命令的线加速度和角加速度最大限制，指定
为二元素正向量。第一个元素是线加速度限制，
单位为米每二次方秒，第二个元素是角加速度
限制，单位为弧度每二次方秒。

#### 依赖

要启用此输入端口，请在 `Trajectory` 选项卡中选中 **Specify max acceleration using
input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **MinTurnRad** — 车辆在优化路径上的最小转弯半径 0（默认）| 非负标量

车辆在优化路径上的最小转弯半径，指定为非负标量。该值对应于车辆在最大转向角下的转弯圆半径。单位为米。

减小该值可允许急转弯和原地旋转。增大该值可限制急转弯。当增大该值时，车辆将在受限空间内进行更多的前进和倒车运动以完成转向。

#### 依赖关系

要启用此输入端口，请在 `Trajectory` 选项卡中选中 **Specify min turning radius using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **TimeWeight** — 时间权重 10（默认）| 正标量

时间权重，指定为正标量。要缩短行驶时间，请增大该权重值。

#### 依赖关系

要启用此输入端口，请在 `Optimization` 选项卡中选中 **Specify time weight using input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **SmoothWeight** — 平滑运动权重 1000（默认）| 正标量

平滑运动的代价函数权重，指定为正标量。要获得更平滑的路径，请增大该权重值。

#### 依赖关系

要启用此输入端口，请在 `Optimization` 选项卡中选中 **Specify smoothness weight using input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **ObstWeight** — 与障碍物保持安全距离的权重 50（默认）| 正标量

与障碍物保持安全距离的代价函数权重，指定为正标量。

#### 依赖关系

要启用此输入端口，请在 `Optimization` 选项卡中选中 **Specify obstacle weight using input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **ObstMargin** — 机器人与障碍物之间的安全距离 0.5（默认）| 正标量

机器人与障碍物之间的安全距离，指定为正标量，单位为米。

#### 依赖关系

要启用此输入端口，请在 `Main` 选项卡中选中 **Specify obstacle safety margin using input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **NumIter** — 优化轨迹的迭代次数 2（默认）| 正整数

优化轨迹的迭代次数，指定为正整数。

#### 依赖关系

要启用此输入端口，请在 `Optimization` 选项卡中选中 **Specify number of iterations using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **LookAheadTime** — 前视时间 5（默认）| 正标量

前视时间，指定为正标量，单位为秒。

#### 依赖关系

要启用此输入端口，请在 `Main` 选项卡中选中 **Specify lookahead time using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **GoalTol** — 目标位姿周围的容差 `[0.1,0.1,0.1]`（默认）| 三元素列向量

目标位姿周围的容差，指定为 [*x*
*y*
*θ*] 形式的三元素向量。*x* 和 *y* 分别表示机器人在 *x* 和 *y* 方向上的位置。单位为米。*θ* 是机器人的航向角，单位为弧度。

#### 依赖关系

要启用此输入端口，请在 `Main` 选项卡中选中 **Specify goal tolerance using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **RefDelTime** — 参考增量时间 `0.3`（默认）| 正标量

参考增量时间，指定为以秒为单位的正标量。它指定连续位姿之间的行驶时间。

#### 依赖关系

要启用此输入端口，请在 `Trajectory` 选项卡中选中 **Specify reference delta time using input port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **VelCmds** — 速度命令 *N*×2 矩阵

速度命令，以 *N*×2 矩阵形式返回。第一列为线速度，单位为米每秒；第二列为角速度，单位为弧度每秒。

**数据类型：** `double`

### **Timestamps** — 与速度命令对应的时间戳 *N* 元列向量

与速度命令对应的时间戳，以 *N* 元列向量形式返回。

**数据类型：** `double`

### **OptPath** — 优化路径 *N*×3 矩阵

优化路径，以 *N*×3 矩阵形式返回。每一行的形式为 [*x*
*y*
*theta*]，定义了路径中某一点的 *xy* 位置和方向角 *theta*。

**数据类型：** `double`

### **SolnInfo** — 额外信息总线

额外信息，以总线形式返回。该总线包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `LastFeasibleIdx` | 指定优化路径和时间戳输出中轨迹可行的元素索引。超过此索引后，`ExitFlag` 的值将大于零。这意味着发生了一个或多个对应于 `ExitFlag` > 0 的场景。 |
| `DistanceFromStartPose` | `optPath` 中每个位姿与 `optPath` 中第一个位姿的距离。`curState` 的值始终是 `optPath` 中的第一个位姿。 |
| `HasReachedGoal` | 指示机器人是否在容差范围内成功到达 ReferencePath 中的最后一个位姿，如果成功则返回 `true`。否则，此值返回 `false`。 |
| `TrajectoryCost` | Timed Elastic Band 算法中代价函数的优化轨迹代价。 |
| `ExitFlag` | 标量值，指示 `Timed Elastic Band` 函数的退出条件。  - 0 — 指示 `Timed Elastic Band` 函数返回了可行的速度命令和轨迹。 - 1 — 指示 `Timed Elastic Band` 函数返回的轨迹输出仅在 `LastFeasibleIdx` 指定的索引值之前是无碰撞的。 - 2 — 指示 `LastFeasibleIdx` 之后索引对应的位姿违反 TEB 控制器的障碍物安全裕度约束超过 10%。 - 3 — 指示车辆从 `LastFeasibleIdx` 处的位姿移动到后续位姿时的转弯半径违反最小转弯半径约束超过 10%。 - 4 — 指示 `Timed Elastic Band` 函数返回的一个或多个时间戳早于前一个时间戳。 - 5 — 指示即使机器人以最大线速度从其当前位置行驶，也无法在指定的前瞻时间内到达参考路径。 |

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

#### Main 选项卡

### **Sample time (s)** — 控制器采样时间 1（默认）| 正标量

指定控制器的采样时间，单位为秒。此模块仅支持离散采样时间。

### **Specify lookahead time using input port** — 添加用于指定前瞻时间的输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Lookahead time (s)** 参数。

### **Lookahead time (s)** — 前瞻时间 5（默认）| 正标量

将前瞻时间指定为正标量。单位为秒。控制器会生成速度命令并优化轨迹，直到控制器达到前瞻时间。较高的前瞻时间会生成更远未来的速度命令。这使机器人能够更早地对未预见的障碍物作出反应，但会增加控制器执行时间。相反，较短的前瞻时间会减少对新未知障碍物作出反应的可利用时间，但使控制器能够以更快的速率运行。

#### 依赖关系

要启用此参数，请清除 **Specify lookahead time using input port** 复选框。

### **Specify goal tolerance using input port** — 添加用于指定目标容差的输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Goal tolerance ([m m rad])** 参数。

### **Goal tolerance ([m m rad])** — 目标位姿周围的容差 `[0.1, 0.1, 0.1]`（默认）| 三元素列向量

将目标位姿周围的容差指定为形式为 [*x*
*y*
*θ*] 的三元素向量。*x* 和 *y* 分别表示机器人在 *x* 和 *y* 方向上的位置。单位为米。*θ* 是机器人的航向角，单位为弧度。此目标容差值指定用于确定机器人是否已到达目标位姿的限值。

#### 依赖关系

要启用此参数，请清除 **Specify goal tolerance using input port** 复选框。

### **Shape** — 机器人形状 `Rectangle`（默认）| `Point`

将机器人形状指定为 `Rectangle` 或 `Point`。

### **Dimension ([m m])** — 机器人尺寸 `[1, 0.67]`（默认）| 二元素正向量

将机器人尺寸指定为形式为 [*length*
*width*] 的二元素正向量，单位为米。

### **Fixed transform ([m m rad])** — 变换矩阵 `se2`（默认）| 形式为 [*x*, *y*, *theta*] 的三元素行向量

变换矩阵，指定为定义 SE(2) 变换矩阵的 `se2` 对象，或表示机器人原点的三元素行向量。该向量形式为 [*x*,
*y*, *theta*]。当您将原点指定为
[*x*, *y*, *theta*] 时，`Timed Elastic Band` 模块会计算关联的 SE(2) 变换矩阵，并将其存储在 `FixedTransform` 字段中。

默认原点位于机器人后端中心。您可以使用此参数为机器人指定相对于默认原点的新原点。

仅当机器人形状为矩形时，此参数才有效。

### **Specify obstacle safety margin using input port** — 添加用于指定障碍物安全裕度的输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Obstacle safety margin (m)** 参数。

### **Obstacle safety margin (m)** — 机器人与障碍物之间的安全距离 0.5（默认）| 正标量

机器人与障碍物之间的安全距离，指定为正标量，单位为米。

#### 依赖关系

要启用此参数，请清除 **Specify obstacle safety margin using input port** 复选框。

#### Trajectory Tab

### **Specify max velocity using input port** — 添加用于指定最大速度的输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Maximum velocity ([m/s rad/s])** 参数。

### **Maximum velocity ([m/s rad/s])** — 线速度和角速度的最大限值 `[0.8, 1.6]`（默认）| 二元素正向量

速度命令的线速度和角速度最大限值，指定为二元素正向量。第一个元素是线速度限值，单位为米每秒；第二个元素是角速度限值，单位为弧度每秒。

#### 依赖关系

要启用此参数，请清除 **Specify max velocity using input port** 复选框。

### **Specify max reverse velocity using input port** — 为最大倒车速度添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Maximum reverse velocity (m/s)** 参数。

### **Maximum reverse velocity (m/s)** — 倒车运动的最大速度 `NaN`（默认）| 正标量

车辆在倒车方向运动时的最大速度，指定为正标量。默认值为 `NaN`。当该属性设置为 `NaN` 时，最大倒车速度的值与最大线速度相同。单位为米每秒。

#### 依赖关系

要启用此参数，请清除 **Specify max reverse velocity using input port** 复选框。

### **Specify max acceleration using input port** — 为最大加速度添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Maximum acceleration ([m/s^2 rad/s^2])** 参数。

### **Maximum acceleration ([m/s^2 rad/s^2])** — 线加速度和角加速度的最大限制 `[2.4,4.8]`（默认）| 二元素正向量

速度命令的线加速度和角加速度的最大限制，指定为二元素正向量。第一个元素是线加速度限制，单位为米每二次方秒；第二个元素是角加速度限制，单位为弧度每二次方秒。

#### 依赖关系

要启用此参数，请清除 **Specify max acceleration using input port** 复选框。

### **Specify min turning radius using input port** — 为最小转弯半径添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Minimum turning radius (m)** 参数。

### **Minimum turning radius (m)** — 车辆在优化路径上的最小转弯半径 0（默认）| 非负标量

车辆在优化路径上的最小转弯半径，指定为非负标量。该值对应于车辆在最大转向角时的转弯圆半径。单位为米。

减小该值可允许急转弯和原地旋转。增大该值可限制急转弯。当增大该值时，车辆将在受限空间中进行更多的前进和倒车运动以完成转向。

#### 依赖关系

要启用此参数，请清除 **Specify min turning radius using input port** 复选框。

### **Specify reference delta time using input port** — 为参考时间增量添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Reference delta time (s)** 参数。

### **Reference delta time (s)** — 参考时间增量 `0.3`（默认）| 正标量

参考时间增量，指定为正标量，单位为秒。它指定了连续位姿之间的行驶时间。此参数影响优化轨迹中位姿的添加和删除。增大此参数的值可减少输出路径中的位姿数量，减小该值可增加位姿数量。

#### 依赖关系

要启用此参数，请清除 **Specify reference delta time using input port** 复选框。

#### 优化选项卡

### **Specify number of iterations using input port** — 为迭代次数添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Number of iterations** 参数。

### **Number of iterations** — 优化轨迹的迭代次数 `2`（默认）| 正整数

优化轨迹的迭代次数，指定为正整数。该值是插值发生的次数，也是控制器调用求解器进行轨迹优化的次数。

#### 依赖关系

要启用此参数，请清除 **Specify number of iterations using input port** 复选框。

### **Specify time weight using input port** — 为时间权重添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Time weight** 参数。

### **Time weight** — 时间的代价函数权重 `10`（默认）| 正整数

时间的代价函数权重，指定为正标量。要降低行驶时间，请增大此权重值。

#### 依赖关系

要启用此参数，请清除 **Specify time weight using input port** 复选框。

### **Specify smoothness weight using input port** — 为平滑度权重添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Smoothness weight** 参数。

### **Smoothness weight** — 平滑运动的权重 1000（默认）| 正标量

平滑运动的代价函数权重，指定为正标量。要获得更平滑的路径，请增大此权重值。

#### 依赖关系

要启用此参数，请清除 **Specify smoothness weight using input port** 复选框。

### **Specify obstacle weight using input port** — 为障碍物权重添加输入端口 off（默认）| on

选中此复选框可添加一个输入端口，用于指定 **Obstacle weight** 参数。

### **Obstacle weight** — 与障碍物保持安全距离的权重 50（默认）| 正标量

与障碍物保持安全距离的代价函数权重，指定为正标量。要优先考虑与障碍物保持安全距离，请增大此权重值。

#### 依赖关系

要启用此参数，请清除 **Specify obstacle weight using input port** 复选框。

## 所属库

Navigation Toolbox / Control Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

规划路径以避开障碍物并生成时间最优轨迹

Timed Elastic Band (TEB) 模块计算一条避开障碍物的可行路径，同时引导车辆朝向指定的参考路径。参考路径通常使用全局路径规划器（如 `plannerRRTStar`）计算。

局部路径规划器在优化行驶时间的同时平滑路径，并与全局规划器已知或未知的障碍物保持安全距离。
