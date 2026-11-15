---
type: simulink-block
title: 'Multistage Nonlinear MPC Controller'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Nonlinear MPC Design'
documentation_page: 'multistagenonlinearmpccontroller'
documentation_source_path: 'ref/multistagenonlinearmpccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Multistage Nonlinear MPC Controller

## 端口

### 输入

#### 必需输入

### **x** — 输入向量

当前预测模型状态，指定为长度为 *Nx* 的向量信号，其中 *Nx* 是预测模型状态的数量。由于非线性 MPC 控制器不执行状态估计，您必须在每个控制区间测量或估计当前预测模型状态。

### **last\_mv** — 上一控制区间在被控对象中使用的控制信号向量

上一控制区间在被控对象中使用的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。

**注意**

将 **last\_mv** 连接到上一控制区间实际施加到被控对象的 MV 信号。通常，这些 MV 信号是控制器生成的值，但有时它们可能来自其他来源。例如，如果您的控制器离线并以跟踪模式运行（即控制器输出不驱动被控对象），则将实际被控对象输入馈送到 **last\_mv** 有助于在控制器重新在线时实现无扰切换。

#### 附加输入

### **md** — 输入行向量 | 矩阵

如果您的控制器预测模型具有可测扰动，则必须启用此端口，并向其连接一个行向量或矩阵信号。

要使用相同的可测扰动值贯穿预测时域，请将 **md** 连接到具有 *Nmd* 个元素的行向量信号，其中 *Nmd* 是操纵变量的数量。每个元素指定一个可测扰动的值。

要使扰动在预测时域内从时刻 *k* 到时刻 *k*+*p* 变化（预览），请将 **md** 连接到具有 *Nmd* 列和最多 *p*+1 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的扰动。如果指定的行数少于 *p*+1，则最终扰动用于预测时域的剩余步长。

#### 依赖关系

要启用此端口，请选择 **Measured disturbances** 参数。

### **state.param** — 可选参数向量

如果您的控制器在其预测模型中使用可选参数，请启用此输入端口，并连接具有 *Npm* 个元素的向量信号，其中 *Npm* 是状态参数的数量（等于 `nlmpcMultistage` 控制器对象的 `Model.ParameterLength` 属性）。控制器将这些参数传递给其模型状态转移和状态 Jacobian 函数。

如果您的控制器不使用可选参数，则必须禁用 **state.param** 端口。

#### 依赖关系

要启用此端口，请选择 **StateFcn parameters** 参数。

### **stage.param** — 可选参数向量

如果您的控制器在任何阶段代价或约束函数中使用可选参数，请启用此输入端口，并连接具有 *Npv* 个元素的向量信号，其中 *Npv* 是所有阶段函数的参数总数，等于 `sum(Stages.ParameterLength)`。所有阶段的参数按如下方式堆叠在参数向量中。

```
[parameter vector for stage 1;
 parameter vector for stage 2;
 ...
 parameter vector for stage p+1;
]
```

在每个阶段，控制器将相关参数向量传递给该阶段激活的阶段代价和约束函数。

如果您的控制器不使用可选参数，则必须禁用 **stage.param** 端口。有关详细信息，请参阅 `nlmpcMultistage` 和 `nlmpcmove`。

#### 依赖关系

要启用此端口，请选择 **Stacked stage parameters** 参数。

#### 在线约束

### **mv.min** — 操纵变量最小约束向量 | 矩阵

要指定运行时操纵变量最小约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `ManipulatedVariables.Min` 属性中指定的下界。

要在预测时域内使用相同的边界，请将 **mv.min** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是输出的数量。每个元素指定一个操纵变量的下界。

要使边界在预测时域内从时刻 *k* 到时刻 *k*+*p*–1 变化，请将 **mv.min** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Lower MV limits** 参数。

### **mv.max** — 操纵变量最大约束向量 | 矩阵

要指定运行时操纵变量最大约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `ManipulatedVariables.Max` 属性中指定的上界。

要在预测时域内使用相同的边界，请将 **mv.max** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是输出的数量。每个元素指定一个操纵变量的上界。

要使边界在预测时域内从时刻 *k* 到时刻 *k*+*p*–1 变化，请将 **mv.max** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Upper MV limits** 参数。

### **dmv.min** — 操纵变量速率最小约束向量 | 矩阵

要指定运行时操纵变量速率最小约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `ManipulatedVariable.RateMin` 属性中指定的下界。**dmv.min** 边界必须为非正。

要在预测时域内使用相同的边界，请将 **dmv.min** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是输出的数量。每个元素指定一个操纵变量变化率的下界。

要使边界在预测时域内从时刻 *k* 到时刻 *k*+*p*–1 变化，请将 **dmv.min** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Lower MVRate limits** 参数。

### **dmv.max** — 操纵变量速率最大约束向量 | 矩阵

要指定运行时操纵变量速率最大约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `ManipulatedVariables.RateMax` 属性中指定的上界。**dmv.max** 边界必须为非负。

要在预测时域内使用相同的边界，请将 **dmv.max** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是输出的数量。每个元素指定一个操纵变量变化率的上界。

要使边界在预测时域内从时刻 *k* 到时刻 *k*+*p*–1 变化，请将 **dmv.max** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Upper MVRate limits** 参数。

### **x.min** — 状态最小约束向量 | 矩阵

要指定运行时状态最小约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `States.Min` 属性中指定的下界。

要在预测时域内使用相同的边界，请将 **x.min** 连接到具有 *Nx* 个元素的行向量信号，其中 *Nx* 是输出的数量。每个元素指定一个状态的下界。

要使边界在预测时域内从时刻 *k*+1 到时刻 *k*+*p* 变化，请将 **x.min** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Lower state limits** 参数。

### **x.max** — 状态最大约束向量 | 矩阵

要指定运行时状态最大约束，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `States.Max` 属性中指定的上界。

要在预测时域内使用相同的边界，请将 **x.max** 连接到具有 *Nx* 个元素的行向量信号，其中 *Nx* 是输出的数量。每个元素指定一个状态的上界。

要使边界在预测时域内从时刻 *k*+1 到时刻 *k*+*p* 变化，请将 **x.max** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。

#### 依赖关系

要启用此端口，请选择 **Upper state limits** 参数。

#### 其他

### **x.terminal** — 终端状态向量

终端状态，指定为长度为 *Nx* 的向量信号。要指定所需的终端状态约束，请启用此输入端口。要通过此输入端口在运行时指定所需的终端状态，您必须在作为参数传递给模块的 `nlmpcMultistage` 对象的 `Model` 属性的 `TerminalState` 字段中指定有限值。对于不需要约束到终端值的状态，请指定 `inf`。在运行时，模块会忽略输入信号中对应于对象中 `inf` 值的任何值。如果未在 `nlmpcMultistage` 对象中指定任何终端值条件，则运行时将忽略此输入端口处的信号。

如果未启用此端口，则终端状态约束（如果存在）在运行时不改变。

#### 依赖关系

要启用此端口，请选择 **Terminal state** 参数。

### **z0** — 决策变量向量的初始猜测向量

要指定决策变量向量的初始猜测，请启用此输入端口。如果禁用此端口，模块将使用上一控制区间计算出的决策变量序列作为初始猜测。良好的初始猜测很重要，因为它们有助于求解器更快地收敛到解。

**z0** 是一个列向量，其长度等于每个阶段所有决策变量向量长度之和。初始猜测必须按如下方式堆叠。

```
[state vector guess for stage 1;
 manipulated variable vector guess for stage 1;
 manipulated variable vector rate guess for stage 1; % if used
 slack variable vector guess for stage 1; % if used
 state vector guess for stage 2;
 manipulated variable vector guess for stage 2;
 manipulated variable vector rate guess for stage 2; % if used
 slack variable vector guess for stage 2; % if used
 ...
 state vector guess for stage p;
 manipulated variable vector guess for stage p;
 manipulated variable vector rate guess for stage p; % if used
 slack variable vector guess for stage p; % if used
 state vector guess for stage p+1;
 slack variable vector guess for stage p+1; % if used
]
```

有关详细信息，请参阅 `nlmpcMultistage` 和 `nlmpcmove`。

#### 依赖关系

要启用此端口，请选择 **Initial guess** 参数。
### 输出

#### 必需输出

### **mv** — 最优操纵变量控制动作列向量

最优操纵变量控制动作，输出为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是操纵变量的数量。

如果求解器收敛到局部最优解（**nlp.status** 为正），则 **mv** 包含最优解。

如果求解器达到最大迭代次数而未找到最优解（**nlp.status** 为零），并且控制器的 `Optimization.UseSuboptimalSolution` 属性为 `true`，则 **mv** 包含次优解；否则，**mv** 与 **last\_mv** 相同。

如果求解器失败（**nlp.status** 为负），则 **mv** 与 **last\_mv** 相同。

#### 附加输出

### **cost** — 目标函数代价 非负标量

目标函数代价，输出为非负标量信号。该代价量化控制器实现其目标的程度。

仅当 **nlp.status** 输出为非负时，代价值才有意义。

#### 依赖关系

要启用此端口，请选择 **Optimal cost** 参数。

### **slack** — 堆叠松弛变量向量 非负向量

堆叠松弛变量向量，用于约束软化。如果所有元素均为零，则在整个预测时域内满足所有软约束。如果任何元素大于零，则至少违反一个软约束。

所有阶段的松弛变量向量按如下方式堆叠。

```
[slack variable vector for stage 1; % if used
 slack variable vector for stage 2; % if used
 ...
 slack variable vector for stage p+1; % if used
]
```

### **nlp.status** — 优化状态标量

优化状态，输出为以下之一：

- Positive Integer — 求解器收敛到最优解
- `0` — 达到最大迭代次数但未收敛到最优解
- Negative integer — 求解器失败

#### 依赖关系

要启用此端口，请选择 **Optimization status** 参数。

#### 最优序列

### **mv.seq** — 最优操纵变量序列矩阵

最优操纵变量序列，返回为具有 *p*+1 行和 *Nmv* 列的矩阵信号，其中 *p* 是预测时域，*Nmv* 是操纵变量的数量。

**mv.seq** 的前 *p* 行包含从当前时刻 *k* 到时刻 *k*+*p*-1 计算出的最优操纵变量值。**mv.seq** 的第一行包含当前操纵变量值（输出 **mv**）。由于控制器不计算时刻 *k*+*p* 的最优控制移动，**mv.seq** 的最后两行相同。

#### 依赖关系

要启用此端口，请选择 **Optimal control sequence** 参数。

### **x.seq** — 最优预测模型状态序列矩阵

最优预测模型状态序列，返回为具有 *p*+1 行和 *Nx* 列的矩阵信号，其中 *p* 是预测时域，*Nx* 是状态的数量。

**x.seq** 的第一行包含当前估计状态值，这些值来自内置状态估计器或自定义状态估计模块输入 **x[k|k]**。**x.seq** 的接下来的 *p* 行包含从时刻 *k*+1 到时刻 *k*+*p* 计算出的最优状态值。

#### 依赖关系

要启用此端口，请选择 **Optimal state sequence** 参数。

## 参数

### **Multistage Nonlinear MPC Controller** — 控制器对象 `nlmpcMultistage` 对象名称

您必须提供一个定义非线性 MPC 控制器的 `nlmpcMultistage` 对象。为此，请在 MATLAB 工作区中输入 `nlmpc` 对象的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `nlmpcobj` |
| **类型：** string, character vector |
| **默认值：** `""` |

### **使用预测模型采样时间** — 用于使用预测模型采样时间的标志 on（默认） | off

选择此参数以使用与其预测模型相同的采样时间运行控制器。要使用不同的控制器采样时间，请清除此参数，并使用 **使模块以不同的采样时间运行** 参数指定采样时间。

为了限制决策变量数量并提高计算效率，您可以使用与预测时域不同的采样时间运行控制器。例如，考虑一个以 10 Hz 运行的非线性 MPC 控制器。如果被控对象和控制器采样时间匹配，则预测被控对象行为十秒需要长度为 100 的预测时域，这会产生大量决策变量。为了减少决策变量数量，您可以使用 1 秒的被控对象采样时间和长度为 10 的预测时域。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseObjectTs` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **使模块以不同的采样时间运行** — 控制器采样时间 正有限标量 | `-1`

指定此参数以使用与其预测模型不同的采样时间运行控制器。将此参数设置为 `-1` 允许模块从其父子系统继承采样时间。

**注意**

MV 变化率向量的第一个元素（即当前操纵变量值与上一个操纵变量值之间的差）通常会进行加权和约束，假设 MV 的上一个值发生在过去，且时间位于 MPC 对象中指定的采样时间。当模块以不同的采样率执行时，此假设不再成立，因此，在这种情况下，您必须确保控制器中定义的权重和约束正确处理 MV 变化率向量的第一个元素。

#### 依赖关系

要启用此参数，请清除 **使用预测模型采样时间** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `TsControl` |
| **类型：** string, character vector |
| **默认值：** `""` |

### **使用 MEX 加速仿真** — 用于使用 MEX 函数仿真控制器的标志 off（默认） | on

选择此参数以使用通过 `buildMEX` 生成的 MEX 函数仿真控制器。这样做可减少控制器的仿真时间。要指定 MEX 函数的名称，请使用 **指定 MEX 函数名** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseMEX` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **指定 MEX 函数名** — 控制器 MEX 函数名 string

使用此参数指定仿真期间要使用的 MEX 函数名称。要创建 MEX 函数，请使用 `buildMEX` 函数。

#### 依赖关系

要启用此参数，请选择 **使用 MEX 加速仿真** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `mexname` |
| **类型：** string, character vector |
| **默认值：** `""` |

### 常规选项卡

### **测量扰动** — 添加测量扰动输入端口 off（默认） | on

如果您的控制器具有测量扰动，则必须选择此参数以将 **md** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `md_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **StateFcn 参数** — 添加状态函数参数输入端口 off（默认） | on

如果您的预测模型使用可选参数，则必须选择此参数以将 **state.param** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `stateparam_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **堆叠阶段参数** — 添加阶段函数参数输入端口 off（默认） | on

如果您的成本或约束函数在任意阶段使用参数，则必须选择此参数以将 **stage.param** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `stageparam_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优成本** — 添加最优成本输出端口 off（默认） | on

选择此参数以将 **cost** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `cost_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优控制序列** — 添加最优控制序列输出端口 off（默认） | on

选择此参数以将 **mv.seq** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `mvseq_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优状态序列** — 添加最优状态序列输出端口 off（默认） | on

选择此参数以将 **x.seq** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `stateseq_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **松弛变量** — 添加松弛变量输出端口 off（默认） | on

选择此参数以将 **slack** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `slack_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **优化状态** — 添加优化状态输出端口 off（默认） | on

选择此参数以将 **nlp.status** 输出端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `status_enabled` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### 在线功能选项卡

### **MV 下限** — 添加最小 MV 约束输入端口 off（默认） | on

选择此参数以将 **mv.min** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `mv_min` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 上限** — 添加最大 MV 约束输入端口 off（默认） | on

选择此参数以将 **mv.max** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `mv_max` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MVRate 下限** — 添加最小 MV 变化率约束输入端口 off（默认） | on

选择此参数以将 **dmv.min** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `mvrate_min` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MVRate 上限** — 添加最大 MV 变化率约束输入端口 off（默认） | on

选择此参数以将 **dmv.max** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `mvrate_max` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **状态下限** — 添加最小状态约束输入端口 off（默认） | on

选择此参数以将 **x.min** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `state_min` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **状态上限** — 添加最大状态约束输入端口 off（默认） | on

选择此参数以将 **x.max** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `state_max` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **终端状态** — 终端状态 off（默认） | on

选择此参数以将 **x.terminal** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `terminal_state` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **初始猜测** — 添加初始猜测输入端口 off（默认） | on

选择此参数以将 **z0** 输入端口添加到模块。

**注意**

默认情况下，Nonlinar MPC Controller 模块将从一个控制区间计算出的最优状态、操纵变量和松弛变量用作下一个控制区间的初始猜测。

仅在应用需要时才启用初始猜测端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `nlp_initialize` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

## 所属库

Model Predictive Control Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法说明和限制：

- Multistage Nonlinear MPC Controller 模块仅支持为使用默认 `fmincon` 求解器和 SQP 算法的多级非线性 MPC 控制器生成代码。
- 不支持单精度或定点计算的代码生成。
- 用于代码生成时，非线性 MPC 控制器不支持将预测模型函数、阶段成本函数或约束函数表示为匿名函数。
- 在“配置参数”对话框中，在 **代码生成 > 接口** 窗格上，必须选择以下参数。

  - **支持非有限数** — 默认情况下会选择此参数。
  - **支持可变大小信号**（使用 Embedded Coder® 时） — 默认情况下不会选择此参数。

## 版本历史

**在 R2021a 中引入**

## 描述

仿真多级非线性模型预测控制器

Multistage Nonlinear MPC Controller 模块仿真多级非线性模型预测控制器。在每个控制区间，该模块通过求解非线性规划问题来计算最优控制移动，在该问题中为不同预测步（阶段）定义了不同的成本函数和约束。有关非线性 MPC 的详细信息，请参阅 Nonlinear MPC。

要使用此模块，必须首先在 MATLAB® 工作区中创建 `nlmpcMultistage` 对象。
