---
type: simulink-block
title: 'Path Following Control System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'pathfollowingcontrolsystem'
documentation_source_path: 'ref/pathfollowingcontrolsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Path Following Control System

## 端口
```yaml
ports:
- name: Set velocity
  summary: 自车速度设定值 非负标量
  direction: input
- name: Time gap
  summary: 安全时间间隔 非负标量
  direction: input
- name: Relative distance
  summary: 前车与自车之间的距离 正标量
  direction: input
- name: Relative velocity
  summary: 前车与自车之间的速度差 标量
  direction: input
- name: Longitudinal velocity
  summary: 自车速度 非负标量
  direction: input
- name: Curvature
  summary: 道路曲率 标量 | 向量
  direction: input
- name: Lateral deviation
  summary: 自车横向偏差 标量
  direction: input
- name: Relative yaw angle
  summary: 相对于车道中心线的角度 标量
  direction: input
- name: Minimum longitudinal acceleration
  summary: 自车最小加速度 标量
  direction: input
- name: Maximum longitudinal acceleration
  summary: 自车最大加速度 标量
  direction: input
- name: Minimum steering angle
  summary: 最小前轮转向角 标量
  direction: input
- name: Maximum steering angle
  summary: 最大前轮转向角 标量
  direction: input
- name: Enable optimization
  summary: 控制器优化启用信号标量
  direction: input
- name: External control signal
  summary: 应用于自车的控制信号，长度为二的向量
  direction: input
- name: Vehicle dynamics matrix A
  summary: 自车预测模型的状态矩阵，方阵
  direction: input
- name: Vehicle dynamics matrix B
  summary: 自车预测模型的输入到状态矩阵，具有两列的矩阵
  direction: input
- name: Vehicle dynamics matrix C
  summary: 自车预测模型的状态到输出矩阵，具有三行的矩阵
  direction: input
- name: Longitudinal acceleration
  summary: 加速度控制信号标量
  direction: output
- name: Steering angle
  summary: 前轮转向角控制信号标量
  direction: output
```

### 输入

### **Set velocity** — 自车速度设定值 非负标量

自车速度设定值，单位为 m/s。当没有前车时，控制器跟踪该速度。

### **Time gap** — 安全时间间隔 非负标量

前车与自车之间的安全时间间隔，单位为秒。该时间间隔用于计算最小安全跟车距离约束。有关详细信息，请参阅 Safe Following Distance。

### **Relative distance** — 前车与自车之间的距离 正标量

前车与自车之间的距离，单位为米。要计算该信号，请从自车位置中减去前车位置。

### **Relative velocity** — 前车与自车之间的速度差 标量

前车与自车之间的速度差，单位为米每秒。要计算该信号，请从自车速度中减去前车速度。

### **Longitudinal velocity** — 自车速度 非负标量

自车速度，单位为 m/s。

### **Curvature** — 道路曲率 标量 | 向量

道路曲率，指定为 1/*R*，其中 *R* 是曲线半径，单位为米。

道路曲率为：

- 当道路向全局坐标系的正 Y 轴方向弯曲时为正。
- 当道路向全局坐标系的负 Y 轴方向弯曲时为负。
- 对于直道为零。

控制器将道路曲率建模为带预览的测量扰动。您可以将曲率指定为：

- 标量信号 — 指定当前控制区间的曲率。控制器在整个预测时域内使用该曲率值。
- 长度小于或等于 **Prediction Horizon** 参数的向量信号 — 指定整个预测时域内的当前和预测曲率值。如果向量长度小于预测时域，则控制器在预测时域的剩余部分使用向量中的最终曲率值。

### **Lateral deviation** — 自车横向偏差 标量

自车相对于车道中心线的横向偏差，单位为米。当自车位于中心线右侧时，横向偏差 *e*1 为正；当自车位于中心线左侧时，横向偏差为负。

### **Relative yaw angle** — 相对于车道中心线的角度 标量

自车纵轴相对于车道中心线的角度，单位为弧度，定义为：

e2=θe−θc

其中，*θe* 是自车角度，*θc* 是中心线角度，两个角度均在全局坐标系中定义。

### **Minimum longitudinal acceleration** — 自车最小加速度 标量

自车纵向加速度最小约束，单位为 m/s2。当最小加速度在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请选择相应的 **Use external source** 参数。

### **Maximum longitudinal acceleration** — 自车最大加速度 标量

自车纵向加速度最大约束，单位为 m/s2。当最大加速度在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请选择相应的 **Use external source** 参数。

### **Minimum steering angle** — 最小前轮转向角 标量

最小前轮转向角约束，单位为弧度。当最小转向角在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请选择相应的 **Use external source** 参数。

### **Maximum steering angle** — 最大前轮转向角 标量

最大前轮转向角约束，单位为弧度。当最大转向角在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请选择相应的 **Use external source** 参数。

### **Enable optimization** — 控制器优化启用信号标量

控制器优化启用信号。当此信号为：

- 非零时，控制器执行优化计算并生成 **Longitudinal acceleration** 和 **Steering angle** 控制信号。
- 零时，控制器不执行优化计算。在这种情况下，**Longitudinal acceleration** 和 **Steering angle** 输出信号保持优化禁用时的值。控制器继续更新其内部状态估计。

#### 依赖关系

要启用此端口，请选择 **Use external signal to enable or disable optimization** 参数。

### **External control signal** — 应用于自车的控制信号，长度为二的向量

应用于自车的实际控制信号。此信号的第一个元素是纵向加速度，单位为 m/s2，第二个元素是转向角，单位为弧度。控制器使用这些信号来估计自车模型状态。当应用于自车的控制信号与模型预测控制器计算的最优控制信号不匹配时，使用此输入端口。这种不匹配可能在以下情况下发生，例如：

- Path Following Control System 不是活动控制器。当控制器未激活时保持准确的状态估计，可防止控制器激活时控制信号出现突变。
- 转向或加速度执行器发生故障，无法向自车提供正确的控制信号。

#### 依赖关系

要启用此端口，请选择 **Use external control signal for bumpless transfer between PFC and other controllers** 参数。

### **Vehicle dynamics matrix A** — 自车预测模型的状态矩阵，方阵

自车预测模型的状态矩阵。状态矩阵中的行数对应于预测模型中的状态数。此矩阵必须为方阵。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。

### **Vehicle dynamics matrix B** — 自车预测模型的输入到状态矩阵，具有两列的矩阵

自车预测模型的输入到状态矩阵。此信号中的行数必须与 **Vehicle dynamics matrix A** 中的行数匹配。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。

### **Vehicle dynamics matrix C** — 自车预测模型的状态到输出矩阵，具有三行的矩阵

自车预测模型的状态到输出矩阵。此信号中的列数必须与 **Vehicle dynamics matrix A** 中的行数匹配。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。
### 输出

### **Longitudinal acceleration** — 加速度控制信号标量

由控制器生成的加速度控制信号，单位为 m/s2。

### **Steering angle** — 前轮转向角控制信号标量

由控制器生成的前轮转向角控制信号，单位为弧度。前轮转向角是前轮相对于车辆纵轴的角度。转向角朝向自车横轴正方向时为正。
## 参数
```yaml
parameters:
- name: Use vehicle parameters
  summary: 使用车辆属性定义自车模型 on（默认）| off
  group: 参数选项卡
  block_parameter: ModelType
  type: string, character vector
  default: '"Use vehicle parameters"'
- name: Use vehicle model
  summary: 使用状态空间矩阵定义自车模型 off（默认）| on
  group: 参数选项卡
  block_parameter: ModelType
  type: string, character vector
  default: '"Use vehicle parameters"'
- name: Total mass
  summary: 自车质量 1575（默认）| 正标量
  group: 参数选项卡
  block_parameter: VehicleMass
  type: string, character vector
  default: '"1575"'
- name: Yaw moment of inertia
  summary: 绕自车垂直轴的转动惯量 2875（默认）| 正标量
  group: 参数选项卡
  block_parameter: VehicleYawInertia
  type: string, character vector
  default: '"2875"'
- name: Longitudinal distance from center of gravity to front tires
  summary: 从自车质心到前轮的距离 1.2（默认）| 正标量
  group: 参数选项卡
  block_parameter: LengthToFront
  type: string, character vector
  default: '"1.2"'
- name: Longitudinal distance from center of gravity to rear tires
  summary: 从自车质心到后轮的距离 1.6（默认）| 正标量
  group: 参数选项卡
  block_parameter: LengthToRear
  type: string, character vector
  default: '"1.6"'
- name: 前轮侧偏刚度
  summary: 前轮刚度 19000（默认值）| 正标量
  group: 参数选项卡
  block_parameter: FrontTireStiffness
  type: string, character vector
  default: '"19000"'
- name: 后轮侧偏刚度
  summary: 后轮刚度 33000（默认值）| 正标量
  group: 参数选项卡
  block_parameter: RearTireStiffness
  type: string, character vector
  default: '"33000"'
- name: 纵向加速度跟踪时间常数
  summary: 加速度跟踪的时间常数 0.5（默认值）| 正标量
  group: 参数选项卡
  block_parameter: AccelTimeConstant
  type: string, character vector
  default: '"0.5"'
- name: A
  summary: 自车预测模型的初始状态矩阵 方阵
  group: 参数选项卡
  block_parameter: EgoModelMatrixA
  type: string, character vector
  default: '"[-4.4021 ,-12.4603;1.3913,-5.1868]"'
- name: B
  summary: 自车预测模型的初始输入到状态矩阵 具有两列的矩阵
  group: 参数选项卡
  block_parameter: EgoModelMatrixB
  type: string, character vector
  default: '"[24.1270;15.8609]"'
- name: C
  summary: 自车预测模型的初始状态到输出矩阵 具有三行的矩阵
  group: 参数选项卡
  block_parameter: EgoModelMatrixC
  type: string, character vector
  default: '"[1,0;0,1]"'
- name: Initial longitudinal velocity
  summary: 自车模型的初始速度 15（默认）| 非负标量
  group: 参数选项卡
  block_parameter: InitialLongVel
  type: string, character vector
  default: '"15"'
- name: Transport lag between model inputs and outputs
  summary: 自车模型中的总传输延迟 0（默认）| 非负标量
  group: 参数选项卡
  block_parameter: TransportLag
  type: string, character vector
  default: '"0"'
- name: Maintain safe distance between lead vehicle and ego vehicle
  summary: 启用间距控制 on（默认）| off
  group: 参数选项卡
  block_parameter: spaceCtrl
  type: string, character vector
  default: '"on"'
- name: Default spacing
  summary: 与前方车辆的最小间距 10（默认）| 非负标量
  group: 参数选项卡
  block_parameter: DefaultSpacing
  type: string, character vector
  default: '"10"'
- name: Minimum steering angle
  summary: 最小前轮转向角 -0.26（默认）| -pi/2 和 pi/2 之间的标量
  group: 控制器选项卡
  block_parameter: MinSteering
  type: string, character vector
  default: '"-0.26"'
- name: Maximum steering angle
  summary: 最大前轮转向角 0.26（默认）| -pi/2 和 pi/2 之间的标量
  group: 控制器选项卡
  block_parameter: MaxSteering
  type: string, character vector
  default: '"0.26"'
- name: Minimum longitudinal acceleration
  summary: 最小自车加速度 -3（默认）| 标量
  group: 控制器选项卡
  block_parameter: MinAcceleration
  type: string, character vector
  default: '"-3"'
- name: 最大纵向加速度
  summary: 自车最大加速度 2（默认）| 标量
  group: 控制器选项卡
  block_parameter: MaxAcceleration
  type: string, character vector
  default: '"2"'
- name: 采样时间
  summary: 控制器采样时间 0.1（默认）| 正标量
  group: 控制器选项卡
  block_parameter: Ts
  type: string, character vector
  default: '"0.1"'
- name: 预测时域
  summary: 控制器预测时域 10（默认）| 正整数
  group: 控制器选项卡
  block_parameter: PredictionHorizon
  type: string, character vector
  default: '"30"'
- name: 控制时域
  summary: 控制器控制时域 3（默认）| 正整数 | 正整数向量
  group: 控制器选项卡
  block_parameter: ControlHorizon
  type: string, character vector
  default: '"3"'
- name: 速度跟踪权重
  summary: 纵向速度跟踪的整定权重 0.1（默认）| 正标量
  group: 控制器选项卡
  block_parameter: LongWeight
  type: string, character vector
  default: '"0.1"'
- name: 横向误差权重
  summary: 横向误差的整定权重 1（默认）| 正标量
  group: 控制器选项卡
  block_parameter: LateralWeight
  type: string, character vector
  default: '"1"'
- name: 纵向加速度变化权重
  summary: 纵向加速度变化的整定权重 0.1（默认）| 正标量
  group: 控制器选项卡
  block_parameter: AccelRateWeight
  type: string, character vector
  default: '"0.1"'
- name: 转向角变化权重
  summary: 转向角变化的整定权重 0.1（默认）| 正标量
  group: 控制器选项卡
  block_parameter: SteerRateWeight
  type: string, character vector
  default: '"0.1"'
- name: Use suboptimal solution
  summary: 在指定迭代次数后应用次优解 off（默认）| on
  group: Block Tab
  block_parameter: suboptimal
  type: string, character vector
  default: '"off"'
- name: Maximum iteration number
  summary: 最大优化迭代次数 10（默认）| 正整数
  group: Block Tab
  block_parameter: maxiter
  type: string, character vector
  default: '"10"'
- name: Use external signal to enable or disable optimization
  summary: 添加用于启用优化的端口 off（默认）| on
  group: Block Tab
  block_parameter: optmode
  type: string, character vector
  default: '"off"'
- name: Use external signal for bumpless transfer between PFC and other controllers
  summary: 添加外部控制信号输入端口 off（默认）| on
  group: Block Tab
  block_parameter: trackmode
  type: string, character vector
  default: '"off"'
- name: Create PFC subsystem
  summary: 创建自定义控制器按钮
  group: Block Tab
```

### 参数选项卡

#### 自车

### **Use vehicle parameters** — 使用车辆属性定义自车模型 `on`（默认）| `off`

选择此参数可通过指定自车的属性来定义 MPC 控制器使用的自车模型。自车模型是从纵向加速度和前轮转向角到纵向速度、横向速度和横摆角速率的线性模型。

要定义车辆模型，请指定以下模块参数：

- **Total mass**
- **Yaw moment of inertia**
- **Longitudinal distance from center of gravity to front
  tires**
- **Longitudinal distance from center of gravity to rear
  tires**
- **Cornering stiffness of front tires**
- **Cornering stiffness of rear tires**
- **Longitudinal acceleration tracking time constant**

有关自车模型的更多信息，请参阅 Ego Vehicle Predictive Model。

选择此参数将清除 **Use vehicle model** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ModelType` |
| **类型**：string, character vector |
| **默认值**：`"Use vehicle parameters"` |

### **Use vehicle model** — 使用状态空间矩阵定义自车模型 `off`（默认）| `on`

选择此参数可定义 MPC 控制器使用的自车模型的状态空间矩阵。自车模型是从纵向加速度和前轮转向角到纵向速度、横向速度和横摆角速率的线性模型。

要定义初始内部模型，请指定 **A**、**B** 和 **C** 状态空间矩阵。内部模型必须是无直接馈通的最小实现，并且 **A**、**B** 和 **C** 的维度必须一致。

通常，自车模型依赖于速度，因此会随时间变化。要在运行时更新内部模型，请使用 **Vehicle dynamics A**、**Vehicle dynamics B** 和 **Vehicle dynamics C** 输入端口。

有关自车模型的更多信息，请参阅 Ego Vehicle Predictive Model。

选择此参数将清除 **Use vehicle parameters** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ModelType` |
| **类型**：string, character vector |
| **默认值**：`"Use vehicle parameters"` |

### **Total mass** — 自车质量 `1575`（默认）| 正标量

自车质量，单位为 kg。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`VehicleMass` |
| **类型**：string, character vector |
| **默认值**：`"1575"` |

### **Yaw moment of inertia** — 绕自车垂直轴的转动惯量 `2875`（默认）| 正标量

绕自车垂直轴的转动惯量，单位为 Kg·m2。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`VehicleYawInertia` |
| **类型**：string, character vector |
| **默认值**：`"2875"` |

### **Longitudinal distance from center of gravity to front tires** — 从自车质心到前轮的距离 `1.2`（默认）| 正标量

从自车质心到其前轮的距离，单位为米，沿车辆纵轴测量。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LengthToFront` |
| **类型**：string, character vector |
| **默认值**：`"1.2"` |

### **Longitudinal distance from center of gravity to rear tires** — 从自车质心到后轮的距离 `1.6`（默认）| 正标量

从自车质心到其后轮的距离，单位为米，沿车辆纵轴测量。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LengthToRear` |
| **类型：** string, character vector |
| **默认值：** `"1.6"` |

### **前轮侧偏刚度** — 前轮刚度 `19000`（默认值）| 正标量

前轮侧偏刚度，单位为 N/rad，定义为前轮侧向力与前轮相对于车辆纵轴夹角之间的关系。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrontTireStiffness` |
| **类型：** string, character vector |
| **默认值：** `"19000"` |

### **后轮侧偏刚度** — 后轮刚度 `33000`（默认值）| 正标量

后轮侧偏刚度，单位为 N/rad，定义为后轮侧向力与后轮相对于车辆纵轴夹角之间的关系。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RearTireStiffness` |
| **类型：** string, character vector |
| **默认值：** `"33000"` |

### **纵向加速度跟踪时间常数** — 加速度跟踪的时间常数 `0.5`（默认值）| 正标量

用于跟踪纵向加速度的时间常数，以秒为单位指定。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AccelTimeConstant` |
| **类型：** string, character vector |
| **默认值：** `"0.5"` |

### **A** — 自车预测模型的初始状态矩阵 方阵

自车预测模型的初始状态矩阵。状态矩阵的行数对应于预测模型中的状态数。此矩阵必须为方阵。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新状态矩阵，请使用 **Vehicle dynamics A** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EgoModelMatrixA` |
| **类型：** string, character vector |
| **默认值：** `"[-4.4021 ,-12.4603;1.3913,-5.1868]"` |

### **B** — 自车预测模型的初始输入到状态矩阵 具有两列的矩阵

自车预测模型的初始输入到状态矩阵。此参数的行数必须与 **A** 的行数匹配。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新输入到状态矩阵，请使用 **Vehicle dynamics B** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EgoModelMatrixB` |
| **类型：** string, character vector |
| **默认值：** `"[24.1270;15.8609]"` |

### **C** — 自车预测模型的初始状态到输出矩阵 具有三行的矩阵

自车预测模型的初始状态到输出矩阵。此参数的列数必须与 **A** 的行数匹配。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新状态到输出矩阵，请使用 **Vehicle dynamics C** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EgoModelMatrixC` |
| **类型：** string, character vector |
| **默认值：** `"[1,0;0,1]"` |

### **Initial longitudinal velocity** — 自车模型的初始速度 `15`（默认）| 非负标量

自车模型的初始速度，单位为 m/s，可以与实际自车初始速度不同。

该值用于配置模型预测控制器的初始条件。有关详细信息，请参阅初始条件。

**注意**

非常小的初始速度，例如 `eps`，可能会为控制器被控对象模型产生非最小实现，从而导致错误。为避免此错误，请将初始速度设置为较大的值，例如 `1e-3`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialLongVel` |
| **类型：** string, character vector |
| **默认值：** `"15"` |

### **Transport lag between model inputs and outputs** — 自车模型中的总传输延迟 `0`（默认）| 非负标量

自车模型中的总传输延迟，*τ*，单位为秒。该延迟包括执行器、传感器和通信延迟。对于每个输入-输出通道，传输延迟模型为：

1τs+1

#### 程序化使用

|  |
| --- |
| **模块参数：** `TransportLag` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

#### 间距控制

### **Maintain safe distance between lead vehicle and ego vehicle** — 启用间距控制 `on`（默认）| `off`

要配置安全跟车距离，请设置 **Default spacing** 参数。有关控制器使用的安全跟车距离的详细信息，请参阅安全跟车距离。

#### 程序化使用

|  |
| --- |
| **模块参数：** `spaceCtrl` |
| **类型：** string, character vector |
| **默认值：** `"on"` |

### **Default spacing** — 与前方车辆的最小间距 `10`（默认）| 非负标量

前方车辆与自车之间的最小间距，单位为米。该值对应于自车速度为零时自车与前方车辆之间的目标相对距离。

该值用于计算：

- 最小安全跟车距离。有关详细信息，请参阅安全跟车距离。
- 控制器初始条件。有关详细信息，请参阅初始条件。

#### 依赖关系

要启用此参数，请选择 **Maintain safe distance between lead vehicle and ego vehicle** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DefaultSpacing` |
| **类型：** string, character vector |
| **默认值：** `"10"` |

### 控制器选项卡

#### 路径跟随控制器约束

### **Minimum steering angle** — 最小前轮转向角 `-0.26`（默认）| `-pi/2` 和 `pi/2` 之间的标量

最小前轮转向角约束，单位为弧度。

如果最小转向角随时间变化，请通过选择 **Use external source** 将 **Minimum steering angle** 输入端口添加到模块。

#### 依赖关系

此参数必须小于 **Maximum steering angle** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MinSteering` |
| **类型：** string, character vector |
| **默认值：** `"-0.26"` |

### **Maximum steering angle** — 最大前轮转向角 `0.26`（默认）| `-pi/2` 和 `pi/2` 之间的标量

最大前轮转向角约束，单位为弧度。

如果最大转向角随时间变化，请通过选择 **Use external source** 将 **Maximum steering angle** 输入端口添加到模块。

#### 依赖关系

此参数必须大于 **Minimum steering angle** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxSteering` |
| **类型：** string, character vector |
| **默认值：** `"0.26"` |

### **Minimum longitudinal acceleration** — 最小自车加速度 `-3`（默认）| 标量

最小自车纵向加速度约束，单位为 m/s2。

如果最小加速度随时间变化，请通过选择 **Use external source** 将 **Minimum longitudinal acceleration** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MinAcceleration` |
| **类型：** string, character vector |
| **默认值：** `"-3"` |

### **最大纵向加速度** — 自车最大加速度 `2`（默认）| 标量

自车纵向加速度约束的最大值，单位为 m/s2。

如果最大加速度随时间变化，请选择 **Use external source**，为模块添加 **Maximum longitudinal acceleration** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxAcceleration` |
| **类型：** string, character vector |
| **默认值：** `"2"` |

#### 模型预测控制器设置

### **采样时间** — 控制器采样时间 `0.1`（默认）| 正标量

控制器采样时间，单位为秒。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **预测时域** — 控制器预测时域 `10`（默认）| 正整数

控制器预测时域步数。控制器预测时间为采样时间与预测时域的乘积。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PredictionHorizon` |
| **类型：** string, character vector |
| **默认值：** `"30"` |

### **控制时域** — 控制器控制时域 `3`（默认）| 正整数 | 正整数向量

控制器控制时域，指定为以下之一：

- 小于或等于 **Prediction horizon** 参数的正整数。在这种情况下，控制器计算在时刻 *k* 到 *k*+*m*-1 发生的 *m* 个自由控制移动，并在从 *k*+*m* 到 *k*+*p*-1 的剩余预测时域步数内保持控制器输出恒定。这里，*k* 是当前控制区间。
- 正整数向量 [*m*1, *m*2, …]，其中各整数之和等于 **Prediction horizon** 参数。在这种情况下，控制器计算 *M* 个自由移动块，其中 *M* 是控制时域向量的长度。第一个自由移动适用于时刻 *k* 到 *k*+*m*1-1，第二个自由移动适用于时刻 *k*+*m*1 到 *k*+*m*1+*m*2-1，依此类推。使用块移动可以提高控制器的鲁棒性。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ControlHorizon` |
| **类型：** string, character vector |
| **默认值：** `"3"` |

#### 控制器行为

### **速度跟踪权重** — 纵向速度跟踪的整定权重 `0.1`（默认）| 正标量

纵向速度跟踪的整定权重。要产生更小的速度跟踪误差，请增大此权重。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LongWeight` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **横向误差权重** — 横向误差的整定权重 `1`（默认）| 正标量

横向误差的整定权重。要产生更小的横向误差，请增大此权重。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LateralWeight` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **纵向加速度变化权重** — 纵向加速度变化的整定权重 `0.1`（默认）| 正标量

纵向加速度变化的整定权重。要产生更平缓的车辆加速度，请增大此权重。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AccelRateWeight` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **转向角变化权重** — 转向角变化的整定权重 `0.1`（默认）| 正标量

转向角变化的整定权重。要产生更平缓的转向角变化，请增大此权重。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SteerRateWeight` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### Block Tab

### **Use suboptimal solution** — 在指定迭代次数后应用次优解 `off`（默认）| `on`

将控制器配置为在指定的最大迭代次数后应用次优解，从而保证控制器的最坏情况执行时间。

有关详细信息，请参阅 Suboptimal QP Solution。

#### 依赖关系

选择此参数后，请指定 **Maximum iteration number** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`suboptimal` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Maximum iteration number** — 最大优化迭代次数 `10`（默认）| 正整数

控制器优化迭代的最大次数。

#### 依赖关系

要启用此参数，请选择 **Use suboptimal solution** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`maxiter` |
| **类型**：string, character vector |
| **默认值**：`"10"` |

### **Use external signal to enable or disable optimization** — 添加用于启用优化的端口 `off`（默认）| `on`

要向模块添加 **Enable optimization** 输入端口，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`optmode` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Use external signal for bumpless transfer between PFC and other controllers** — 添加外部控制信号输入端口 `off`（默认）| `on`

要向模块添加 **External control signal** 输入端口，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`trackmode` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Create PFC subsystem** — 创建自定义控制器按钮

生成自定义 PFC 子系统，您可以针对自己的应用对其进行修改。自定义控制器的配置数据将作为结构体导出到 MATLAB® 工作区。

您可以修改自定义控制器子系统以：

- 修改默认 MPC 设置或使用高级 MPC 功能。
- 修改默认控制器初始条件。
- 使用不同的应用设置，例如自定义安全跟车距离定义。
## 所属库

Model Predictive Control Toolbox / Automated Driving

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用自适应模型预测控制器模拟路径跟随控制

Path Following Control System 模块模拟路径跟随控制（PFC）系统，该系统使自车沿直线或弯曲道路的中心行驶，同时跟踪设定速度并与前车保持安全距离。为此，控制器同时调整自车的纵向加速度和前轮转向角。该模块使用自适应模型预测控制（MPC）计算最优控制动作，同时满足安全距离、速度、加速度和转向角约束。

此模块将 Lane Keeping Assist System 和 Adaptive Cruise Control System 模块的功能组合到单个控制器中。

要自定义控制器，例如使用高级 MPC 功能或修改控制器初始条件，请点击 **Create PFC subsystem**。
