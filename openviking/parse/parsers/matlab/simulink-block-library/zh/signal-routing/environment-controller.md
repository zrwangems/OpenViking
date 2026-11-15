---
type: simulink-block
title: 'Environment Controller'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'environmentcontroller'
language: zh-CN
chinese_source: worker-translation
---

# Environment Controller

## 端口

### 输入

### **Sim** — 仿真输入 标量 | 向量 | 矩阵

仿真输入值，指定为标量、向量或矩阵。输入信号必须与 **Coder** 端口的输入具有相同的宽度。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Coder** — 代码生成输入 标量 | 向量 | 矩阵

代码生成输入值，指定为标量、向量或矩阵。输入信号必须与 **Sim** 端口的输入具有相同的宽度。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **Out** — 来自仿真或代码生成输入端口的值 标量 | 向量 | 矩阵

来自 **Sim** 或 **Coder** 输入端口的值，具体取决于当前环境。有关该模块在各种仿真和代码生成模式下输出的详细信息，请参阅描述。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。涉及嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然代码在功能上有效，并且在资源丰富的环境中通常可接受，但较小的嵌入式目标往往无法支持此类代码。通常，模块会逐渐演变为适合生产代码。因此，适合生产代码的模块仍然适合。

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2021b：Environment Controller 模块已被移除

Environment Controller 模块已从 Signal Routing 库中移除。使用此模块的现有模型将继续工作，但会发出警告。请改用 Variant Source 模块，并将 **Variant control mode** 参数设置为 `sim codegen switching`。您可以使用 Model Advisor 或 Upgrade Advisor 自动识别所有 Environment Controller 模块实例，并将其替换为 Variant Source 模块。有关 Model Advisor 检查的信息，请参阅识别 Environment Controller 模块并将其替换为 Variant Source 模块。

Variant 模块相比 Environment Controller 模块具有以下优势：

- 将 Variant Source 模块的 **Variant control mode** 参数设置为 `sim codegen switching`，可让您在仿真和代码生成工作流之间自动切换。在此模式下，Variant Source 模块支持以下激活时间：

  | Variant 激活时间 | 行为 |
  | --- | --- |
  | `update diagram` | Simulink 在更新图期间、信号属性传播之前设置活动选择。非活动选择在信号属性传播之前被移除，因此生成的代码仅包含活动选择。 |
  | `update diagram analyze all choices` | Simulink 在更新图期间、信号属性传播之后设置活动选择。信号属性会传播到活动选择和非活动选择，以检查一致性。非活动选择在模型启动之前、更新图结束时被移除。生成的代码仅包含活动选择。 |

- Variant Sink 模块支持在输出侧（信号的目标）进行分支。
- Variant 模块在仿真和代码生成期间高亮显示活动 variant 选择的路径。
- 与 Environment Controller 模块相比，Variant Source 模块提供最优的代码生成。Environment Controller 模块可能会在生成的代码中保留连接到 **Sim** 端口的模块。
- 可以使用 Variant Manager 工具集中管理 Variant 模块，该工具提供以下关键功能：

  - 可视化 variant 模型层次结构。
  - 定义并验证模型的多个 variant 配置。
  - 使用 Variant Reducer 工具为某个 variant 配置生成简化模型。对于将 **Variant control mode** 参数设置为 `sim codegen switching` 的 variant 模块，您可以选择在简化模型中保留仿真分支或代码生成分支。
  - 使用 Variant Configuration Analysis 工具比较 variant 配置。

  有关详细信息，请参阅 Variant Manager for Simulink。

## 描述

（已移除）创建仅适用于仿真或仅适用于代码生成的框图分支

Environment Controller 模块仅当包含它的模型正在仿真时，才在其 **Sim** 端口输出信号。仅当从该模型生成代码时，才在其 **Coder** 端口输出信号。此选项使您能够创建仅适用于仿真或代码生成的框图分支。下表描述了 **Sim** 或 **Coder** 端口适用的各种场景。

| 场景 | 输出 |
| --- | --- |
| 正常模式仿真 | **Sim** |
| 加速模式仿真 | **Sim** |
| 快速加速模式仿真 | **Sim** |
| 在正常或加速模式下仿真被引用模型 | **Sim** |
| 在 processor-in-the-loop (PIL) 模式下仿真被引用模型 | **Coder**（使用为被引用模型生成的相同代码） |
| 外部模式仿真 | **Coder** |
| 标准代码生成 | **Coder** |
| 被引用模型的代码生成 | **Coder** |

Simulink® Coder™ 软件在满足以下条件时，不会为连接到 **Sim** 端口的模块生成代码：

- 在 Configuration Parameters 对话框的 **Code Generation > Optimization** 窗格中，将 **Default parameter behavior** 设置为 `Inlined`。
- 连接到 **Sim** 端口的模块没有外部信号。
- **Sim** 端口输入路径不包含 S-function 或 Interpreted MATLAB Function 模块。

如果启用 Block reduction 优化，Simulink 在为仿真编译模型时会消除连接到 **Coder** 端口的分支中的模块。有关详细信息，请参阅 Block reduction。

**注意**

Simulink Coder 代码生成仅当仿真分支与代码生成分支具有相同的信号维度时，才会消除连接到仿真分支的模块。无论是否消除仿真分支，Simulink Coder 都会使用仿真分支以及代码生成分支上的采样时间来确定生成代码的基本采样时间，并且在某些情况下，可能会生成仅适用于仿真分支上指定的采样时间的采样时间处理代码。
