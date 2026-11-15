---
type: simulink-block
title: 'Policy'
family: 'reinforcement-learning'
product_id: 'reinforcement-learning'
product_name: 'Reinforcement Learning Toolbox'
documentation_release: R2025b
official_category: 'Policies and Value Functions'
documentation_page: 'policy'
documentation_source_path: 'ref/policy.html'
language: zh-CN
chinese_source: worker-translation
---

# Policy

## 端口

### 输入

### **observation** — 环境观测值 scalar | vector | nonvirtual bus

此端口从环境接收观测信号。观测信号表示测量值或其他瞬时系统数据。如果有多个观测值，可以使用 Mux 模块将它们组合为 vector 信号。要使用 nonvirtual bus 信号，请使用 `bus2RLSpec` 函数。

### **update parameters** — 启用策略参数更新 scalar

当收到的 scalar 信号值大于零时，Policy 模块的参数会使用从 **parameters** 端口收到的值进行更新。

#### 依赖关系

要启用此端口，请选择 **Policy parameter inputs** 参数。

### **parameters** — 输入 bus

使用此端口提供策略参数的更新值。该端口必须接收一个 bus 信号，其结构和数据类型与启用 **Policy parameter inputs** 参数时模块创建的 bus 对象一致。当 **update parameters** 端口收到大于零的值时，Policy 模块的参数会使用从此端口收到的值进行更新。

**注意**

此端口可以接受由 `policyParameters` 函数生成的结构。

#### 依赖关系

要启用此端口，请选择 **Policy parameter inputs** 参数。

### 输出

### **action** — Policy 动作 scalar | vector | nonvirtual bus

由策略基于 observation 输入计算得到的动作。将此端口连接到系统的输入。要使用 nonvirtual bus 信号，请使用 `bus2RLSpec` 函数。

**注意**

从连续动作空间 `rlStochasticActorPolicy` 对象或连续动作空间 `rlACAgent`、`rlPGAgent` 或 `rlPPOAgent` 对象生成的 Policy 模块不强制执行由动作规范设置的约束。对于这些模块，你必须在环境内强制执行动作空间约束。

## 参数

### **Policy block data MAT file** — Policy 模块数据 MAT 文件 `blockAgentData.mat` (default) | 文件名

输入包含完整表征策略所需信息的 MAT 文件的名称。此文件由 `generatePolicyFunction` 或 `generatePolicyBlock` 生成。当你使用 `generatePolicyBlock` 生成模块并指定非默认的 `dataFileName` 参数时，生成的模块会将此参数设置为指定的文件名，从而使该模块与生成的数据文件关联。

要在条件执行的子系统（例如 Triggered Subsystem (Simulink) 或 Function-Call Subsystem (Simulink)）中使用 Policy 模块，你必须从 `SampleTime` 属性设置为 `-1` 的 agent 或 policy 对象生成其数据文件。这样做允许模块继承其父级子系统的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MATFile` |
| **类型：** string, character vector |
| **默认值：** `"blockAgentData.mat"` |

### **Policy parameter inputs** — 添加策略参数输入端口并创建 bus 对象和参数结构 `off` (default) | `on`

选择此参数以将 **update parameters** 和 **parameters** 输入端口添加到模块。选择此参数并点击 **Apply** 时，模块会在模型的全局工作区（通常是 MATLAB® 工作区）中同时创建一个 bus 对象和一个结构。

- bus 对象指定必须连接到 **parameters** 端口的 bus 的维度和数据类型。你可以使用 **Policy parameter bus name** 参数指定 bus 对象的名称。
- 该结构与 `policyParameters` 函数返回的数据一致，并包含从 **Policy block data MAT file** 中指定的 MAT 文件获取的值。

点击 **Generate IC blocks** 以自动生成引用初始策略参数的初始条件模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PolicyParamsAsInput` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Policy parameter bus name** — 策略参数 bus 对象的名称 `policy_param_bus` (default) | 文件名

输入当选择 **Policy parameter inputs** 并点击 **Apply** 时模块创建的 bus 对象的名称。模块在模型的全局工作区（通常是 MATLAB 工作区）中创建该 bus 对象。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PolicyParamsBusName` |
| **类型：** string, character vector |
| **默认值：** `"policy_param_bus"` |

### **Generate IC blocks** — 生成包含策略参数初始条件的模块按钮

点击此按钮以生成包含初始条件的 Constant 模块，这些模块连接到 **update parameters** 和 **parameters** 端口。连接到 **update parameters** 端口的模块输出 `false` logical 值。连接到 **parameters** 端口的模块输出当点击 **Apply** 按钮时在工作区中创建的包含策略参数的结构。

## 所属库

Reinforcement Learning Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

强化学习策略

使用 Policy 模块在 Simulink® 中仿真强化学习策略，并（使用 Simulink Coder™）生成用于部署的代码。此模块将 observation 作为输入，并返回 action 作为输出。将模块与一个 MAT 文件关联，该文件包含完整表征策略所需的信息。该 MAT 文件可由 `generatePolicyFunction` 或 `generatePolicyBlock` 函数生成。
