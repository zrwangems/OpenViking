---
type: simulink-block
title: 'Policy'
family: 'reinforcement-learning'
product_id: 'reinforcement-learning'
product_name: 'Reinforcement Learning'
documentation_release: R2025b
official_category: ''
documentation_page: 'policy'
documentation_source_path: 'ref/policy.html'
language: zh-CN
chinese_source: worker-translation
---

# Policy

## 端口
```yaml
ports:
- name: observation
  summary: 环境观测值 标量 | 向量 | 非虚拟总线
  direction: input
- name: update parameters
  summary: 启用策略参数更新 标量
  direction: input
- name: parameters
  summary: 输入总线
  direction: input
- name: action
  summary: 策略动作 标量 | 向量 | 非虚拟总线
  direction: output
```

### 输入

### **observation** — 环境观测值 标量 | 向量 | 非虚拟总线

此端口接收来自环境的观测信号。观测信号表示测量值或其他瞬时系统数据。如果有多个观测值，可以使用 Mux 模块将它们组合为向量信号。要使用非虚拟总线信号，请使用 `bus2RLSpec` 函数。

### **update parameters** — 启用策略参数更新 标量

当接收到的标量信号值大于零时，Policy 模块的参数将使用从 **parameters** 端口接收到的值进行更新。

#### 依赖关系

要启用此端口，请选择 **Policy parameter inputs** 参数。

### **parameters** — 输入总线

使用此端口提供策略参数的更新值。该端口必须接收一个总线信号，其结构和数据类型与启用 **Policy parameter inputs** 参数时模块创建的 bus 对象一致。当 **update parameters** 端口接收到大于零的值时，Policy 模块的参数将使用从此端口接收到的值进行更新。

**注意**

此端口可以接受由 `policyParameters` 函数生成的结构体。

#### 依赖关系

要启用此端口，请选择 **Policy parameter inputs** 参数。
### 输出

### **action** — 策略动作 标量 | 向量 | 非虚拟总线

策略基于观测输入计算出的动作。将此端口连接到系统的输入。要使用非虚拟总线信号，请使用 `bus2RLSpec` 函数。

**注意**

从连续动作空间 `rlStochasticActorPolicy` 对象或连续动作空间 `rlACAgent`、`rlPGAgent` 或 `rlPPOAgent` 对象生成的 Policy 模块不会强制执行由动作规范设置的约束。对于这些模块，必须在环境内强制执行动作空间约束。
## 参数
```yaml
parameters:
- name: Policy block data MAT file
  summary: 策略模块数据 MAT 文件 blockAgentData.mat（默认）| 文件名
  group: ''
  block_parameter: MATFile
  type: string, character vector
  default: '"blockAgentData.mat"'
- name: Policy parameter inputs
  summary: 添加策略参数输入端口并创建 bus 对象和参数结构体 off（默认）| on
  group: ''
  block_parameter: PolicyParamsAsInput
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 策略参数总线名称
  summary: 策略参数总线对象的名称 policy_param_bus（默认值）| 文件名
  group: ''
  block_parameter: PolicyParamsBusName
  type: string, character vector
  default: '"policy_param_bus"'
- name: 生成 IC 模块
  summary: 生成包含策略参数初始条件的模块 按钮
  group: ''
```

### **Policy block data MAT file** — 策略模块数据 MAT 文件 `blockAgentData.mat`（默认）| 文件名

输入包含完整描述策略所需信息的 MAT 文件名。此文件由 `generatePolicyFunction` 或 `generatePolicyBlock` 生成。当使用 `generatePolicyBlock` 生成模块并指定非默认的 `dataFileName` 参数时，生成的模块将此参数设置为指定的文件名，以便模块与生成的数据文件关联。

要在条件执行子系统（如 Triggered Subsystem (Simulink) 或 Function-Call Subsystem (Simulink)）中使用 Policy 模块，必须从 `SampleTime` 属性设置为 `-1` 的智能体或策略对象生成其数据文件。这样做可以使模块继承其父子系统的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MATFile` |
| **类型：** string, character vector |
| **默认值：** `"blockAgentData.mat"` |

### **Policy parameter inputs** — 添加策略参数输入端口并创建 bus 对象和参数结构体 `off`（默认）| `on`

选择此参数以将 **update parameters** 和 **parameters** 输入端口添加到模块。当选择此参数并点击 **Apply** 时，模块会在模型的全局工作区（通常是 MATLAB® 工作区）中创建 bus 对象和结构体。

- bus 对象指定必须连接到 **parameters** 端口的总线的维度和数据类型。可以使用 **Policy parameter bus name** 参数指定 bus 对象的名称。
- 结构体与 `policyParameters` 函数返回的数据一致，并包含从 **Policy block data MAT file** 中指定的 MAT 文件获取的值。

点击 **Generate IC blocks** 以自动生成引用初始策略参数的初始条件模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PolicyParamsAsInput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **策略参数总线名称** — 策略参数总线对象的名称 `policy_param_bus`（默认值）| 文件名

输入当您选择**策略参数输入**并点击**应用**时该模块创建的 bus 对象的名称。该模块在模型的全局工作区（通常是 MATLAB 工作区）中创建该 bus 对象。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PolicyParamsBusName` |
| **类型：** string, character vector |
| **默认值：** `"policy_param_bus"` |

### **生成 IC 模块** — 生成包含策略参数初始条件的模块 按钮

点击此按钮可生成包含初始条件的 Constant 模块，这些模块连接到 **update parameters** 和 **parameters** 端口。连接到 **update parameters** 端口的模块返回 `false` 逻辑值作为输出。连接到 **parameters** 端口的模块返回包含策略参数的结构体作为输出，该结构体在您点击**应用**按钮时在工作区中创建。
## 所属库

Reinforcement Learning Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

强化学习策略

使用 Policy 模块在 Simulink® 中仿真强化学习策略，并生成代码（使用 Simulink Coder™）用于部署目的。该模块将观测值作为输入，并返回动作作为输出。您将该模块与一个 MAT 文件关联，该文件包含完整表征策略所需的信息。该 MAT 文件可由 `generatePolicyFunction` 或 `generatePolicyBlock` 函数生成。
