---
type: simulink-block
title: 'RL Agent'
family: 'reinforcement-learning'
product_id: 'reinforcement-learning'
product_name: 'Reinforcement Learning'
documentation_release: R2025b
official_category: 'Reinforcement Learning'
documentation_page: 'rlagent'
documentation_source_path: 'ref/rlagent.html'
language: zh-CN
chinese_source: worker-translation
---

# RL Agent

## 端口

### 输入

### **observation** — 环境观测 scalar | vector | nonvirtual bus

此端口从环境接收 observation 信号。observation 信号表示测量值或其他瞬时系统数据。如果有多个 observation，可以使用 Mux 模块将它们组合为 vector 信号。要使用 nonvirtual bus 信号，请使用 `bus2RLSpec`。

### **reward** — 来自环境的奖励 scalar

此端口接收 reward 信号，该信号由您根据 observation 数据计算。reward 信号在代理训练期间用于最大化长期奖励的期望。

### **isdone** — 用于终止回合仿真的标志 logical

使用此信号指定终止训练回合的条件。您必须配置适合您系统的逻辑，以确定回合终止条件。一个应用是终止明显进展顺利或进展不佳的回合。例如，如果代理达到目标或不可恢复地远离目标，则可以终止回合。

### **external action** — External action 信号 scalar | vector

使用此信号向模块提供 external action。此信号可以是来自人类专家的控制动作，可用于安全或模仿学习应用。当 **use external action** 信号的值为 `1` 时，RL Agent 模块通过 **action** 输出端口将 **external action** 信号传递给环境。该模块还使用 external action 根据生成的 observation 和 reward 更新代理策略。

#### 依赖关系

要启用此端口，请选择 **External action inputs** 参数。

### **last action** — 应用于环境的 last action 信号 scalar | vector

对于某些应用，应用于环境的 action 可能不同于 RL Agent 模块输出的 action。例如，Simulink 模型可以在 action 输出信号上包含一个 Saturation 模块。

在这种情况下，为改进 off-policy 代理的学习结果，您可以启用此输入端口，并连接实际应用于您的环境的实际 action 信号，并将其延迟一个采样时间。有关示例，请参见 Custom Training Loop with Simulink Action Noise。

**注意**

**last action** 端口应仅与 off-policy 代理一起使用，否则训练可能产生意外结果。

#### 依赖关系

要启用此端口，请选择 **Last action input** 参数。

### **use external action** — Use external action 信号 `0` | `1`

使用此信号将 **external action** 信号传递给环境。

当 **use external action** 信号的值为 `1` 时，该模块将 **external action** 信号传递给环境。该模块还使用 external action 更新代理策略。

当 **use external action** 信号的值为 `0` 时，该模块不将 **external action** 信号传递给环境，也不使用 external action 更新策略。相反，该模块的 action 使用来自代理策略的 action。

#### 依赖关系

要启用此端口，请选择 **External action inputs** 参数。

### 输出

### **action** — 代理 action scalar | vector | nonvirtual bus

代理基于 observation 和 reward 输入计算的 action。将此端口连接到环境的输入。要使用 nonvirtual bus 信号，请使用 `bus2RLSpec`。

**注意**

连续 action 空间代理（例如 `rlACAgent`、`rlPGAgent` 或 `rlPPOAgent`（使用 `rlContinuousGaussianActor` 对象的代理））不会强制实施 action 规范设置的约束。在这些情况下，您必须在环境内强制实施 action 空间约束。

### **cumulative reward** — 累积未折扣 reward scalar

这是从仿真开始到当前时间的 reward 信号的累积未折扣总和。观察或记录此信号，以跟踪 cumulative reward 随时间的变化。

#### 依赖关系

要启用此端口，请选择 **Cumulative reward output** 参数。

## 参数

### **Agent object** — 要训练的代理 `agentObj`（默认） | agent object

输入存储在 MATLAB 工作区或数据字典中的代理对象的名称，例如 `rlACAgent` 或 `rlDDPGAgent` 对象。有关代理对象的信息，请参阅 Reinforcement Learning Agents。

如果 RL Agent 模块位于条件执行子系统（例如 Triggered Subsystem (Simulink) 或 Function-Call Subsystem (Simulink)）内，则必须将代理对象的采样时间指定为 `-1`，以便该模块可以继承其父子系统的采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `Agent` |
| **类型：** string, character vector |
| **默认值：** `"agentObj"` |

### **Generate greedy policy block** — 生成贪心策略模块控件按钮

通过调用 `generatePolicyBlock` 模块函数，为 **Agent object** 中指定的代理生成一个实现贪心策略的 Policy 模块。为生成贪心策略，该模块在生成策略模块之前将代理的 `UseExplorationPolicy` 属性设置为 `false`。

生成的模块会添加到新的 Simulink 模型中，策略数据保存在当前工作文件夹中的 MAT 文件中。

### **External action inputs** — 为 external action 添加输入端口 `off`（默认） | `on`

通过选择此参数，启用 **external action** 和 **use external action** 模块输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ExternalActionAsInput` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Last action input** — 为应用于环境的 last action 添加输入端口 `off`（默认） | `on`

通过选择此参数，启用 **last action** 模块输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ProvideLastAction` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Cumulative reward output** — 添加 cumulative reward 输出端口 `off`（默认） | `on`

通过选择此参数，启用 **cumulative reward** 模块输出。

#### 编程用法

|  |
| --- |
| **模块参数：** `ProvideCumRwd` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Use strict observation data types** — 强制实施 observation 的严格数据类型 `off`（默认） | `on`

选择此参数以强制实施 observation 数据类型。在这种情况下，如果连接到 **observation** 输入端口的信号的数据类型与代理的 `ObservationInfo` 属性中的数据类型不匹配，该模块会尝试将信号转换为正确的数据类型。如果无法转换数据类型，该模块会生成错误。

强制实施严格数据类型：

- 允许您验证模块获取的数据类型是否正确。
- 允许其他模块从 **observation** 端口继承其数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseStrictObservationDataTypes` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

## 所属库

Reinforcement Learning Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

强化学习代理

使用 RL Agent 模块在 Simulink® 中仿真和训练强化学习代理。您可以将该模块与存储在 MATLAB® 工作区或数据字典中的代理相关联，例如 `rlACAgent` 或 `rlDDPGAgent` 对象。您连接该模块，使其接收 observation 和计算得到的 reward。例如，考虑 `rlSimplePendulumModel` 模型的以下框图。

RL Agent 模块的 **observation** 输入端口接收派生自摆的瞬时角度和角速度的信号。**reward** 端口接收根据相同的两个值和应用的 action 计算的 reward。您可以配置适合您系统的 observation 和 reward 计算。

该模块使用代理基于您提供的 observation 和 reward 生成 action。将 **action** 输出端口连接到系统的相应输入。例如，在 `rlSimplePendulumModel` 中，**action** 输出端口是施加到摆系统的扭矩。有关此模型的更多信息，请参阅 Train DQN Agent to Swing Up and Balance Pendulum。

要在 Simulink 中训练强化学习代理，您从 Simulink 模型生成环境。然后创建并配置代理以针对该环境进行训练。有关更多信息，请参阅 Create Custom Simulink Environments。当您使用该环境调用 `train` 时，`train` 会仿真模型并更新与该模块关联的代理。
