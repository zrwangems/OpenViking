---
type: simulink-block
title: 'Linear Sliding Mode Controller (State Feedback)'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Sliding Mode'
documentation_page: 'linearslidingmodecontrollerstatefeedback'
documentation_source_path: 'ug/linearslidingmodecontrollerstatefeedback.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Sliding Mode Controller (State Feedback)

## 端口
```yaml
ports:
- name: x
  summary: 系统状态 标量 | 向量
  direction: input
  data_types: single | double
- name: r
  summary: 参考信号 标量 | 向量
  direction: input
  data_types: single | double
- name: r.dot
  summary: 参考信号的导数 标量 | 向量
  direction: input
  data_types: single | double
- name: u
  summary: 控制作用 标量 | 向量
  direction: output
  data_types: single | double
- name: s(x)
  summary: 切换函数值 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **x** — 系统状态 标量 | 向量

系统状态，指定为 *nx*×1 的信号，其中 *nx* 是状态的数量。

**数据类型：** `single` | `double`

### **r** — 参考信号 标量 | 向量

跟踪模式下要跟随的参考轨迹，指定为 *ny*×1 的信号，其中 *ny* 是输出的数量。

参考信号必须是可微的。

#### 依赖关系

要启用此端口，请将 **Task Mode** 设置为 **Reference Tracking** 或 **Model-Reference Tracking**。

**数据类型：** `single` | `double`

### **r.dot** — 参考信号的导数 标量 | 向量

参考信号的导数，指定为 *ny*×1 的信号，其中 *ny* 是输出的数量。

当您希望从外部输入提供参考信号的导数时，请使用此端口。否则，模块将在仿真期间计算导数。

#### 依赖关系

要启用此端口：

- 将 **Switching Function** 设置为 **Reference Tracking**。
- 启用 **Include derivative reference signal**。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制作用 标量 | 向量

计算得到的控制作用，返回为 *nu*×1 的信号，其中 *nu* 是输入的数量。

**数据类型：** `single` | `double`

### **s(x)** — 切换函数值 标量 | 向量

切换函数值，返回为 *nu*×1 的信号，其中 *nu* 是输入的数量。

#### 依赖关系

要启用此端口，请启用 **Output Switching Function** 参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: A
  summary: 状态矩阵 [0 1; 0 0]（默认）| 方阵
  group: 模型参数
  block_parameter: A
  values: '"[0 1; 0 0]"（默认）| 方阵'
- name: B
  summary: 输入矩阵 [0; 1]（默认）| 矩阵
  group: 模型参数
  block_parameter: B
  values: '"[0; 1]"（默认）| 矩阵'
- name: C
  summary: 输出矩阵 [1 0]（默认）| 矩阵
  group: 模型参数
  block_parameter: C
  values: '"[1 0]"（默认）| 矩阵'
- name: Am
  summary: 参考模型状态矩阵 [0 1; 0 0]（默认）| 矩阵
  group: 参考模型参数
  block_parameter: Am
  values: '"[0 1; 0 0]"（默认）| 方阵'
- name: Bm
  summary: 参考模型输入矩阵 [0; 1]（默认）| 矩阵
  group: 参考模型参数
  block_parameter: Bm
  values: '"[0; 1]"（默认）| 矩阵'
- name: Task Mode
  summary: 运行模式 Regulation（默认）| Reference Tracking | Model-Reference Tracking
  group: Sliding Surface Tab
  block_parameter: TaskMode
  values: '"Regulation"（默认）| "Reference Tracking" | "Model-Reference Tracking"'
- name: Output Switching Function
  summary: 输出切换函数 off（默认）| on
  group: Sliding Surface Tab
  block_parameter: EnableSwitchingFunction
  values: '"off"（默认）| "on"'
- name: Include derivative reference signal
  summary: 在外部指定参考信号的导数 off（默认）| on
  group: Sliding Surface Tab
  block_parameter: EnableTrackingDerivative
  values: '"off"（默认）| "on"'
- name: Sr
  summary: 参考跟踪的设计矩阵 0.1（默认）| 标量 | 矩阵
  group: Sliding Surface Tab
  block_parameter: Sr
  values: '"0.1"（默认）| 带引号的标量或矩阵'
- name: Tuning Method
  summary: 滑模面设计方法 Pole Placement（默认）| Quadratic Minimization | User-Defined Matrix (S)
  group: Sliding Surface Tab
  block_parameter: Tuning
  values: '"Pole Placement"（默认）| "Quadratic Minimization" | "User-defined Matrix (S)"'
- name: Pole Location
  summary: 极点配置方法的极点位置 -1（默认）| 列向量
  group: Sliding Surface Tab
  block_parameter: PoleLocation
  values: '"-1"（默认）| 带引号的列向量'
- name: Weighted Matrix
  summary: 二次性能指标的加权矩阵 eye(2)（默认）| 方阵
  group: Sliding Surface Tab
  block_parameter: WeightedMatrix
  values: '"eye(2)"（默认）| 带引号的矩阵'
- name: Export Hyperplane Matrix S
  summary: 将设计好的超平面矩阵发送到 MATLAB® 工作区按钮
  group: Sliding Surface Tab
- name: S
  summary: 用户定义的超平面矩阵 [1 1]（默认）| 矩阵
  group: Sliding Surface Tab
  block_parameter: S
  values: '"[0; 1]"（默认）| 矩阵'
- name: Reaching Law
  summary: 趋近律 Constant Rate（默认）| Exponential | Power Rate | Unit Vector
  group: Reaching Law Tab
  block_parameter: ReachingLaw
  values: '"Constant Rate"（默认）| "Exponential" | "Power Rate" | "Unit Vector"'
- name: Reaching Rate (η)
  summary: 趋近速率 0.01（默认）| 正标量 | 列向量
  group: Reaching Law Tab
  block_parameter: ReachingRate
  values: '"0.01"（默认）| 带引号的正标量 | 带引号的列向量'
- name: Control Gain (K)
  summary: 控制增益 0.01（默认）| 正标量 | 列向量
  group: Reaching Law Tab
  block_parameter: ControlGain
  values: '"0.01"（默认） | 带引号的正标量 | 带引号的列向量'
- name: Power Rate Exponent (α)
  summary: 幂次趋近律指数 0.01（默认） | 0 到 1 之间的正标量 | 0 到 1 之间的正数值列向量
  group: Reaching Law Tab
  block_parameter: PowerRate
  values: '"0.01"（默认） | 带引号的 0 到 1 之间的正标量 | 带引号的 0 到 1 之间的正数值列向量'
- name: Select Boundary Layer
  summary: 边界层函数 Sign（默认） | Relay | Hyperbolic Tangent | Saturation
  group: Reaching Law Tab
  block_parameter: BoundaryLayer
  values: '"Sign"（默认） | "Relay" | "Hyperbolic Tangent" | "Saturation"'
- name: Phi
  summary: 边界层厚度 0.01（默认） | 正标量 | 列向量
  group: Reaching Law Tab
  block_parameter: Phi
  values: '"0.01"（默认） | 带引号的正标量 | 带引号的列向量'
- name: Enable zero-crossing detection
  summary: 启用过零检测 off（默认） | on
  group: Reaching Law Tab
  block_parameter: ZeroCross
  values: '"off"（默认） | "on"'
- name: Time domain
  summary: 控制器时域 Continuous-Time（默认）| Discrete-Time
  group: 模块选项卡
  block_parameter: TimeDomain
  values: '"Continuous-Time"（默认）| "Discrete-Time"'
- name: Sample time
  summary: 采样时间 -1（默认）| 有限正标量
  group: 模块选项卡
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的正标量'
- name: Integrator method
  summary: 离散时间积分方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: 模块选项卡
  block_parameter: IntegratorMethod
  values: '"Forward Euler"（默认）| "Backward Euler" | "Trapezoidal"'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 模型参数

### **A** — 状态矩阵 `[0 1; 0 0]`（默认）| 方阵

系统的状态矩阵，指定为大小为 *nx*×*nx* 的方阵，其中 *nx* 是状态的数量。此处，系统是一类不确定线性系统，其标称模型定义为：

x˙(t)=Ax(t)+Bu(t)

对 (*A*，*B*) 必须是可控的。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `A` |
| **值：** | `"[0 1; 0 0]"`（默认）| 方阵 |

**示例：** `set_param(gcb,"A","[1 2; 3 1]")`

### **B** — 输入矩阵 `[0; 1]`（默认）| 矩阵

系统的输入矩阵，指定为大小为 *nx*×*nu* 的矩阵，其中 *nx* 是状态的数量，*nu* 是输入的数量。此处，系统是一类不确定线性系统，其标称模型定义为：

x˙(t)=Ax(t)+Bu(t)

对 (*A*，*B*) 必须是可控的。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `B` |
| **值：** | `"[0; 1]"`（默认）| 矩阵 |

**示例：** `set_param(gcb,"B","[2; 3]")`

### **C** — 输出矩阵 `[1 0]`（默认）| 矩阵

系统的输出矩阵，指定为大小为 *ny*×*nx* 的矩阵，其中 *nx* 是状态的数量，*ny* 是输出的数量。此处，系统是一类不确定线性系统，其标称模型定义为：

x˙(t)=Ax(t)+Bu(t)y(t)=Cx(t)

系统 (*A*，*B*，*C*) 必须完全可控，并且在原点处没有不变零点。

#### 依赖关系

要启用此参数，请将 **Task Mode** 设置为 **Reference Tracking**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `C` |
| **值：** | `"[1 0]"`（默认）| 矩阵 |

**示例：** `set_param(gcb,"C","[2 3]")`

### 参考模型参数

### **Am** — 参考模型状态矩阵 `[0 1; 0 0]`（默认）| 矩阵

参考模型的状态矩阵，指定为大小为
*nx*×*nx* 的方阵，
其中 *nx* 是状态数。在模型参考跟踪模式下，指定的系统
状态 *x*(*t*) 跟踪参考
模型状态
*xm*(*t*)。

x˙(t)=Ax(t)+Bu(t)x˙m(t)=Amxm(t)+Bmr(t)

对
(*Am*,*Bm*)
必须可控，且参考模型必须稳定，即
*Am* 的特征值具有
负实部。

#### 依赖关系

要启用此参数，请将 **Task Mode** 设置为
**Model-Reference Tracking**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Am` |
| **值：** | `"[0 1; 0 0]"`（默认）| 方阵 |

**示例：** `set_param(gcb,"Am","[1 2; 3
1]")`

### **Bm** — 参考模型输入矩阵 `[0; 1]`（默认）| 矩阵

参考模型的输入矩阵，指定为大小为
*nx*×*nu* 的方阵，
其中 *nx* 是状态数，*nu* 是
输入数。在模型参考跟踪模式下，指定的系统
状态 *x*(*t*) 跟踪参考
模型状态
*xm*(*t*)。

x˙(t)=Ax(t)+Bu(t)x˙m(t)=Amxm(t)+Bmr(t)

#### 依赖关系

要启用此参数，请将 **Task Mode** 设置为
**Model-Reference Tracking**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Bm` |
| **值：** | `"[0; 1]"`（默认）| 矩阵 |

**示例：** `set_param(gcb,"Bm","[2;
3]")`

### Sliding Surface Tab

### **Task Mode** — 运行模式 **Regulation**（默认）| **Reference Tracking** | **Model-Reference Tracking**

模块运行模式，指定为以下之一：

- **Regulation** — 当您
  希望将系统状态
  *x*(*t*) 驱动到零时，使用此模式。

  x˙(t)=Ax(t)+Bu(t)
- **Reference Tracking** — 当您
  希望系统输出
  *y*(*t*) 跟随
  指定的参考信号
  *r*(*t*) 时，使用此模式。

  x˙(t)=Ax(t)+Bu(t)y(t)=Cx(t)
- **Model-Reference Tracking** — 当您
  希望系统状态
  *x*(*t*) 跟踪
  预定义的参考模型状态
  *xm*(*t*) 时，使用此
  模式。

  x˙(t)=Ax(t)+Bu(t)x˙m(t)=Amxm(t)+Bmr(t)

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TaskMode` |
| **值：** | `"Regulation"`（默认）| `"Reference Tracking"` | `"Model-Reference Tracking"` |

**示例：** `set_param(gcb,"TaskMode","Reference
Tracking")`

### **Output Switching Function** — 输出切换函数 `off`（默认）| `on`

选择以在输出端口
**s(x)** 返回滑模面值。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableSwitchingFunction` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb,"EnableSwitchingFunction","on")`

### **Include derivative reference signal** — 在外部指定参考信号的导数 `off`（默认）| `on`

选择以在输入端口 **r.dot** 外部指定状态参考信号的
导数。

#### 依赖关系

要启用此参数，请将 **Task Mode** 设置为
**Reference Tracking**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EnableTrackingDerivative` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb,"EnableTrackingDerivative","on")`

### **Sr** — 参考跟踪的设计矩阵 `0.1`（默认）| 标量 | 矩阵

用于在参考跟踪模式下控制降阶运动的设计矩阵，指定为大小为
*ny*×*ny* 的标量或矩阵，
其中 *ny* 是输出数量。

在参考跟踪模式下，切换函数定义为：

s(x)=Sx˜(t)−Srr(t)x˜(t)=[xr(t)x(t)],x˙r(t)=r(t)−y(t)

#### 依赖关系

要启用此参数，请设置：**Task Mode** 为
**Reference Tracking**，并启用
**Include derivative reference signal**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sr` |
| **值：** | `"0.1"`（默认）| 带引号的标量或矩阵 |

**示例：** `set_param(gcb,"Sr","eye(2)")`

### **Tuning Method** — 滑模面设计方法 **Pole Placement**（默认）| **Quadratic Minimization** | **User-Defined Matrix (S)**

用于设计滑模面 *S* 的整定方法，
指定为以下之一：

- **Pole Placement** — 此方法将
  滑模阶段闭环系统的特征值配置到期望的动态特性。要指定
  极点位置，请使用 **Pole Location**
  参数。
- **Quadratic Minimization** — 此方法
  设计矩阵 *S*，使系统
  最小化二次性能指标，表示为：

  J=12∫ts∞x(t)TQx(t)dt

  要指定矩阵 *Q*，请使用
  **Weighted Matrix** 参数。
- **User-Defined Matrix (S)** — 显式
  定义滑模面矩阵。要指定该矩阵，请使用
  模块参数 **S**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tuning` |
| **值：** | `"Pole Placement"`（默认）| `"Quadratic Minimization"` | `"User-defined Matrix (S)"` |

**示例：** `set_param(gcb,"Tuning","Quadratic
Minimization")`

### **Pole Location** — 极点配置方法的极点位置 `-1`（默认）| 列向量

使用极点配置方法设计滑模面 *S* 时的
极点位置，指定为以下大小之一的列向量：

- (*nx* –
  *nu*)×1，当
  **Task Mode** 设置为
  **Regulation** 或
  **Model-Reference Tracking** 时。
- (*nx* –
  *nu* +
  *ny*)×1，当
  **Task Mode** 设置为
  **Reference Tracking** 时。

#### 依赖关系

要启用此参数，请将 **Tuning Method**
设置为 **Pole Placement**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PoleLocation` |
| **值：** | `"-1"`（默认）| 带引号的列向量 |

**示例：** `set_param(gcb,"PoleLocation","[-2;-3]")`

### **Weighted Matrix** — 二次性能指标的加权矩阵 `eye(2)`（默认）| 方阵

使用二次最小化方法设计滑模面 *S* 时
二次性能指标的加权矩阵，
指定为以下大小之一的方阵：

- *nx*×*nx*，
  当 **Task Mode** 设置为
  **Regulation** 或
  **Model-Reference Tracking** 时。
- (*nx* +
  *ny*)×(*nx*
  + *ny*)，当
  **Task Mode** 设置为
  **Reference Tracking** 时。

使用加权矩阵根据指定的权重惩罚状态偏差。这与 LQR 设计中的
*Q* 矩阵概念相同。

#### 依赖关系

要启用此参数，请将 **Tuning Method**
设置为 **Quadratic Minimization**。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WeightedMatrix` |
| **值：** | `"eye(2)"`（默认）| 带引号的矩阵 |

**示例：** `set_param(gcb,"WeightedMatrix","[3 0; 0
1]")`

### **Export Hyperplane Matrix S** — 将设计好的超平面矩阵发送到 MATLAB® 工作区按钮

当您点击此按钮时，该模块会在 MATLAB 工作区中创建一个变量，其中包含设计好的超平面矩阵 *S*。

#### 依赖关系

要启用此参数，请将 **Tuning Method** 设置为 **Pole Placement** 或 **Quadratic Minimization**。

### **S** — 用户定义的超平面矩阵 `[1 1]`（默认）| 矩阵

用户定义的超平面矩阵（*S*），指定为具有以下尺寸之一的矩阵：

- 当 **Task Mode** 设置为 **Regulation** 或 **Model-Reference Tracking** 时，为 *nu*×*nx* 矩阵。
- 当 **Task Mode** 设置为 **Reference Tracking** 时，为 *nu*×(*nx* + *ny*) 矩阵。

矩阵 *S* 决定了滑模控制将系统状态驱动到的超平面。

#### 依赖关系

要启用此参数，请将 **Tuning Method** 设置为 **User-defined Matrix (S)**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `S` |
| **值：** | `"[0; 1]"`（默认）| 矩阵 |

**示例：** `set_param(gcb,"Bm","[2; 3]")`

### Reaching Law Tab

### **Reaching Law** — 趋近律 `Constant Rate`（默认）| `Exponential` | `Power Rate` | `Unit Vector`

滑动面的趋近律 *h*(*s*(*x*))，指定为以下之一。

- `Constant Rate` — h(s(x))=−ηiθ(si)

  该律提供到达滑动面的恒定速率。此处，*θ*(*si*) 是边界层，*ηi* 是第 *i* 个控制输入的趋近速率。
- `Exponential` — h(s(x))=−ηiθ(si)−Kisi

  该律添加了一个与滑动变量成比例的项，并在状态偏差显著时提供更激进的收敛。此处，*Ki* 是控制增益项，用于缩放与第 *i* 个滑动变量相关的控制作用。
- `Power Rate` — h(s(x))i=−ηi|si|αθ(si)

  该律在状态远离滑动面时提供快速趋近速度，但在状态接近时降低速度。这确保了减少抖振并提供快速收敛。
- `Unit Vector` — h(s(x))=−ηθ(P2s)−Ks

  此处，*P2* 是 Lyapunov 方程 P2K+KTP2=−I 的解。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingLaw` |
| **值：** | `"Constant Rate"`（默认）| `"Exponential"` | `"Power Rate"` | `"Unit Vector"` |

**示例：** `set_param(gcb,"ReachingLaw","Power Rate")`

### **Reaching Rate (η)** — 趋近速率 `0.01`（默认）| 正标量 | 列向量

趋近速率（*η*），指定为正标量或长度等于控制输入数量的正数值列向量。

趋近速率决定了系统轨迹接近滑动面的速率。较大的 *η* 值会导致更快的滑动面收敛，但也可能导致更高的控制作用，这在所有情况下都不理想，因为可能存在执行器饱和或抖振增加等问题。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReachingRate` |
| **值：** | `"0.01"`（默认）| 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"ReachingRate","0.05")`

### **Control Gain (K)** — 控制增益 `0.01`（默认）| 正标量 | 列向量

指数趋近律中比例项的控制增益，指定为正标量或长度等于控制输入数量的列向量。在指数趋近律中，该项根据与滑动面的偏差成比例地增加控制作用。

#### 依赖关系

要启用此参数，请将 **Reaching Law** 设置为 `Exponential` 或 `Unit Vector`。

#### 编程用法

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ControlGain` |
| **值：** | `"0.01"`（默认） | 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"ControlGain","2")`

### **Power Rate Exponent (α)** — 幂次趋近律指数 `0.01`（默认） | 0 到 1 之间的正标量 | 0 到 1 之间的正数值列向量

幂次趋近律中的指数值，指定为 0 到 1 之间的正标量或长度等于控制输入数量的列向量。该参数决定了控制作用相对于距滑模面距离的非线性程度。具体而言，它调整控制努力随滑模变量幅值的缩放方式。*α* 的值影响趋近滑模面的平滑度。较低的值导致更柔和的趋近，并可能减少抖振。

#### 依赖关系

要启用此参数，请将 **Reaching Law** 设置为 `Power Rate`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PowerRate` |
| **值：** | `"0.01"`（默认） | 带引号的 0 到 1 之间的正标量 | 带引号的 0 到 1 之间的正数值列向量 |

**示例：** `set_param(gcb,"PowerRate","0.02")`

### **Select Boundary Layer** — 边界层函数 `Sign`（默认） | `Relay` | `Hyperbolic Tangent` | `Saturation`

边界层函数，指定为以下之一：

- `Sign` — θ(s)=sgn(s(x))

  此选项使用默认符号函数，并在 –1 和 1 之间不连续切换。
- `Relay` — θ(s)=s|s|+ϕ

  此选项使用继电器函数来定义滑模面周围的切换边界。
- `Hyperbolic Tangent` — θ(s)=tanh(sϕ)

  此选项使用双曲正切函数来定义滑模面周围的切换边界。
- `Saturation` — θ(s)={1s>ϕkss≤ϕ−1s<−ϕk=1ϕ

  此选项使用饱和函数，当滑模变量在边界层 [*–ϕ*,*ϕ*] 内时，在 –1 和 1 之间平滑插值，从而减少高频切换。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BoundaryLayer` |
| **值：** | `"Sign"`（默认） | `"Relay"` | `"Hyperbolic Tangent"` | `"Saturation"` |

**示例：** `set_param(gcb,""BoundaryLayer,"Saturation")`

### **Phi** — 边界层厚度 `0.01`（默认） | 正标量 | 列向量

边界层厚度参数，指定为正标量或长度等于控制输入数量的列向量。

该参数定义滑模面周围的边界层厚度。较大的 **Phi** 值导致较少的抖振，但可能增加稳态误差。相反，较小的 **Phi** 值可以减少稳态误差，但会增加抖振。

#### 依赖关系

要启用此参数，请将 **Select Boundary Layer** 设置为以下任一值：

- `Relay`
- `Hyperbolic Tangent`
- `Saturation`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Phi` |
| **值：** | `"0.01"`（默认） | 带引号的正标量 | 带引号的列向量 |

**示例：** `set_param(gcb,"Phi","0.05")`

### **Enable zero-crossing detection** — 启用过零检测 `off`（默认） | `on`

选择以启用过零检测。有关详细信息，请参阅过零检测。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ZeroCross` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"ZeroCross","on")`

### 模块选项卡

### **Time domain** — 控制器时域 **Continuous-Time**（默认）| **Discrete-Time**

指定控制器时域。

当您选择 **Discrete-Time** 时，使用 **Sample time** 参数指定采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TimeDomain` |
| **值**：| `"Continuous-Time"`（默认）| `"Discrete-Time"` |

**Example:** `set_param(gcb,""TimeDomain,"Discrete-Time")`

### **Sample time** — 采样时间 `-1`（默认）| 有限正标量

模块的采样时间，指定为正标量。模块使用此值对输入输出数据进行采样。

#### 依赖关系

要启用此参数，请将 **Time domain** 属性设置为 **Discrete-Time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的正标量 |

**Example:** `set_param(gcb,"DiscreteTs","0.5")`

### **Integrator method** — 离散时间积分方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

您可以为离散时间积分器选择以下积分方法之一。

- `Forward Euler`：

  y(n)=y(n−1)+Ts⋅u(n−1)
- `Backward Euler`：

  y(n)=y(n−1)+Ts⋅u(n)
- `Trapezoidal`：

  y(n)=y(n−1)+Ts⋅[u(n)+u(n−1)]/2

其中：

- *y* 是积分器输出
- *u* 是输入
- *n* 是当前采样时间
- *Ts* 是采样时间

有关离散时间积分的详细信息，请参阅 Discrete-Time Integrator。

#### 依赖关系

要启用此参数，请将 **Time domain** 设置为 **Discrete-Time**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `IntegratorMethod` |
| **值**：| `"Forward Euler"`（默认）| `"Backward Euler"` | `"Trapezoidal"` |

**Example:** `set_param(gcb,"IntegratorMethod","Trapezoidal")`
## 所属库

Simulink Control Design / Sliding Mode

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用状态反馈，基于已知线性系统设计滑模控制

使用 Linear Sliding Mode Controller (State Feedback) 模块，基于一类不确定线性系统，使用状态反馈方法实现滑模控制 (SMC)。该模块的主要优势在于，它提供了两种基于线性被控对象模型自动设计滑模面的方法。你可以使用 Sliding Mode Controller (Reaching Law) 模块来支持通用的非线性被控对象模型 (x˙=f(x)+g(x)u)，不过你需要自行设计滑模面 *C*。相比之下，对于基于标称线性被控对象模型的 Linear Sliding Mode Controller (State Feedback) 模块，你可以使用所提供的方法自动设计滑模面。

使用该模块，你可以在以下运行模式下实现 SMC：

- 调节模式 — 当你希望将系统状态 *x*(*t*) 驱动到零时，使用此模式。

  x˙(t)=Ax(t)+Bu(t)
- 参考跟踪模式 — 当你希望系统输出 *y*(*t*) 跟随指定参考信号 *r*(*t*) 时，使用此模式。

  x˙(t)=Ax(t)+Bu(t)y(t)=Cx(t)
- 模型参考跟踪模式 — 当你希望系统状态 *x*(*t*) 跟踪预定义的参考模型状态 *xm*(*t*) 时，使用此模式。

  x˙(t)=Ax(t)+Bu(t)x˙m(t)=Amxm(t)+Bmr(t)

对于每种模式，你都可以显式指定滑模矩阵 *S*，或者使用以下两种方法之一设计该矩阵：

- 极点配置 — 该方法配置滑模期间闭环系统的特征值，以实现期望的动态特性。
- 二次最小化 — 该方法设计矩阵 *S*，使系统最小化一个二次性能指标，表示为：

  J=12∫ts∞x(t)TQx(t)dt

此外，你可以选择一种趋近律来控制到达滑模面的收敛速率，并选择一个边界层来最小化抖振效应。有关 SMC 的更多信息，请参阅 Sliding Mode Control。
