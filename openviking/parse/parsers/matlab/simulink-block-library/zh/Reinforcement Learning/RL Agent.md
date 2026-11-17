---
type: simulink-block
title: 'RL Agent'
family: 'reinforcement-learning'
product_id: 'reinforcement-learning'
product_name: 'Reinforcement Learning'
documentation_release: R2025b
official_category: ''
documentation_page: 'rlagent'
documentation_source_path: 'ref/rlagent.html'
language: zh-CN
chinese_source: worker-translation
---

# RL Agent

## 端口
```yaml
ports:
- name: observation
  summary: 环境观测值 标量 | 向量 | 非虚拟总线
  direction: input
- name: reward
  summary: 来自环境的奖励 标量
  direction: input
- name: isdone
  summary: 终止回合模拟的标志 逻辑值
  direction: input
- name: external action
  summary: 外部动作信号 标量 | 向量
  direction: input
- name: last action
  summary: 应用于环境的上一动作 信号 标量 | 向量
  direction: input
- name: use external action
  summary: 使用外部动作信号 0 | 1
  direction: input
- name: action
  summary: 智能体动作 标量 | 向量 | 非虚拟总线
  direction: output
- name: cumulative reward
  summary: 累积未折扣奖励标量
  direction: output
```

### 输入

### **observation** — 环境观测值 标量 | 向量 | 非虚拟总线

此端口接收来自环境的观测信号。观测信号表示测量值或其他瞬时系统数据。如果有多个观测值，可以使用 Mux 模块将它们组合为向量信号。要使用非虚拟总线信号，请使用 `bus2RLSpec`。

### **reward** — 来自环境的奖励 标量

此端口接收奖励信号，该信号基于观测数据计算得出。奖励信号在智能体训练期间用于最大化长期奖励的期望值。

### **isdone** — 终止回合模拟的标志 逻辑值

使用此信号指定终止训练回合的条件。必须根据系统配置适当的逻辑来确定回合终止条件。一个应用场景是终止明显进展顺利或进展不佳的回合。例如，可以在智能体达到目标或不可恢复地远离目标时终止回合。

### **external action** — 外部动作信号 标量 | 向量

使用此信号向模块提供外部动作。此信号可以是来自人类专家的控制动作，可用于安全学习或模仿学习应用。当 **use external action** 信号的值为 `1` 时，RL Agent 模块通过 **action** 输出端口将 **external action** 信号传递给环境。模块还使用外部动作根据产生的观测值和奖励来更新智能体策略。

#### 依赖关系

要启用此端口，请选择 **External action inputs** 参数。

### **last action** — 应用于环境的上一动作 信号 标量 | 向量

对于某些应用，应用于环境的动作可能与 RL Agent 模块输出的动作不同。例如，Simulink 模型可能在动作输出信号上包含饱和模块。

在这种情况下，为了改善离策略智能体的学习结果，可以启用此输入端口，并连接实际应用于环境的实际动作信号，延迟一个采样时间。有关示例，请参见 Custom Training Loop with Simulink Action Noise。

**注意**

**last action** 端口仅应与离策略智能体一起使用，否则训练可能产生意外结果。

#### 依赖关系

要启用此端口，请选择 **Last action input** 参数。

### **use external action** — 使用外部动作信号 `0` | `1`

使用此信号将 **external action** 信号传递给环境。

当 **use external action** 信号的值为 `1` 时，模块将 **external action** 信号传递给环境。模块还使用外部动作来更新智能体策略。

当 **use external action** 信号的值为 `0` 时，模块不将 **external action** 信号传递给环境，也不使用外部动作更新策略。此时，模块的动作使用来自智能体策略的动作。

#### 依赖关系

要启用此端口，请选择 **External action inputs** 参数。

### 输出

### **action** — 智能体动作 标量 | 向量 | 非虚拟总线

智能体基于观测值和奖励输入计算的动作。将此端口连接到环境的输入。要使用非虚拟总线信号，请使用 `bus2RLSpec`。

**注意**

连续动作空间智能体（如 `rlACAgent`、`rlPGAgent` 或 `rlPPOAgent`，即使用 `rlContinuousGaussianActor` 对象的智能体）不强制执行动作规范设置的约束。在这些情况下，必须在环境内强制执行动作空间约束。

### **cumulative reward** — 累积未折扣奖励标量

这是从仿真开始到当前时刻的奖励信号的累积未折扣总和。观察或记录此信号，以跟踪累积奖励随时间的变化。

#### 依赖关系

要启用此端口，请选择 **Cumulative reward output** 参数。
## 参数
```yaml
parameters:
- name: Agent object
  summary: 要训练的智能体 agentObj（默认）| 智能体对象
  group: ''
  block_parameter: Agent
  type: string, character vector
  default: '"agentObj"'
- name: Generate greedy policy block
  summary: 生成贪婪策略模块控制器按钮
  group: ''
- name: External action inputs
  summary: 为外部动作添加输入端口 off（默认）| on
  group: ''
  block_parameter: ExternalActionAsInput
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Last action input
  summary: 为应用于环境的上一动作添加输入端口 off（默认）| on
  group: ''
  block_parameter: ProvideLastAction
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Cumulative reward output
  summary: 添加累积奖励输出端口 off（默认）| on
  group: ''
  block_parameter: ProvideCumRwd
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Use strict observation data types
  summary: 强制观测使用严格数据类型 off（默认）| on
  group: ''
  block_parameter: UseStrictObservationDataTypes
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
```

### **Agent object** — 要训练的智能体 `agentObj`（默认）| 智能体对象

输入存储在 MATLAB 工作区或数据字典中的智能体对象的名称，例如 `rlACAgent` 或 `rlDDPGAgent` 对象。有关智能体对象的信息，请参阅 Reinforcement Learning Agents。

如果 RL Agent 模块位于条件执行子系统中，例如 Triggered Subsystem (Simulink) 或 Function-Call Subsystem (Simulink)，则必须将智能体对象的采样时间指定为 `-1`，以便该模块可以继承其父子系统的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`Agent` |
| **类型**：string, character vector |
| **默认值**：`"agentObj"` |

### **Generate greedy policy block** — 生成贪婪策略模块控制器按钮

通过调用 `generatePolicyBlock` 模块函数，为 **Agent object** 中指定的智能体生成一个实现贪婪策略的 Policy 模块。要生成贪婪策略，该模块在生成策略模块之前将智能体的 `UseExplorationPolicy` 属性设置为 `false`。

生成的模块将添加到新的 Simulink 模型中，策略数据保存在当前工作文件夹的 MAT 文件中。

### **External action inputs** — 为外部动作添加输入端口 `off`（默认）| `on`

通过选择此参数，启用 **external action** 和 **use external action** 模块输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalActionAsInput` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Last action input** — 为应用于环境的上一动作添加输入端口 `off`（默认）| `on`

通过选择此参数，启用 **last action** 模块输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ProvideLastAction` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Cumulative reward output** — 添加累积奖励输出端口 `off`（默认）| `on`

通过选择此参数，启用 **cumulative reward** 模块输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`ProvideCumRwd` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Use strict observation data types** — 强制观测使用严格数据类型 `off`（默认）| `on`

选择此参数以强制观测数据类型。在这种情况下，如果连接到 **observation** 输入端口的信号的数据类型与智能体的 `ObservationInfo` 属性中的数据类型不匹配，则该模块会尝试将信号转换为正确的数据类型。如果无法转换数据类型，则该模块会生成错误。

强制严格数据类型：

- 允许您验证模块是否获取了正确的数据类型。
- 允许其他模块从 **observation** 端口继承其数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseStrictObservationDataTypes` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |
## 所属库

Reinforcement Learning Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

强化学习智能体

使用 RL Agent 模块在 Simulink® 中仿真和训练强化学习智能体。将该模块与存储在 MATLAB® 工作区或数据字典中的智能体相关联，例如 `rlACAgent` 或 `rlDDPGAgent` 对象。连接该模块，使其接收观测值和计算得到的奖励。例如，考虑以下 `rlSimplePendulumModel` 模型的框图。

RL Agent 模块的 **observation** 输入端口接收一个信号，该信号来源于摆的瞬时角度和角速度。**reward** 端口接收由相同的两个值以及所施加的动作计算得到的奖励。您需要配置适合您系统的观测值和奖励计算。

该模块使用智能体根据您提供的观测值和奖励生成动作。将 **action** 输出端口连接到您系统的相应输入。例如，在 `rlSimplePendulumModel` 中，**action** 输出端口是施加到摆系统的力矩。有关此模型的更多信息，请参阅 Train DQN Agent to Swing Up and Balance Pendulum。

要在 Simulink 中训练强化学习智能体，您需要从 Simulink 模型生成环境。然后创建并配置智能体，针对该环境进行训练。有关更多信息，请参阅 Create Custom Simulink Environments。当您使用该环境调用 `train` 时，`train` 会仿真模型并更新与该模块关联的智能体。
