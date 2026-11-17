---
type: simulink-block
title: 'TSOA Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'tsoapositionestimator'
documentation_source_path: 'ref/tsoapositionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TSOA Position Estimator

## 端口

### 输入

### **TSOAEst** — 到达时间和的估计值（秒） 实值 *J*×*L*×*K* 数组

到达时间和的估计值，输入为实值 *J*×*L*×*K* 数组，其中 *J* 是发射锚点的数量，*L* 是接收锚点的数量，*K* 是 TSOA 组的数量。每个页表示一个 TSOA 组，对应于在 *JL* 个锚点对上针对潜在目标测量得到的 TSOA。在每个页中，`TSOAEst` 的第 *j* 行第 *l* 列的元素表示从第 *j* 个发射锚点到第 *l* 个接收锚点的估计 TSOA。当 `TSOAVar` 的实际值未知时，`TSOAVar` 通常选择为每个元素均为相同实正值的矩阵。该值不影响解 `tgtposest`。单位为秒。

**数据类型：** `single` | `double`

### **TSOAVar** — TSOA 估计方差（秒的平方） 实值 *J*×*L* 矩阵 | 实值 *J*×*L*×*K* 数组

TSOA 估计方差，输入为实值 *J*×*L* 矩阵或实值 *J*×*L*×*K* 数组。表示 *JL* 个锚点对的 TSOA 估计方差。当 `TSOAVsr` 为矩阵时，*JL* 个锚点对的方差估计对于所有 *K* 个 TSOA 组相同。当 `TSOAVar` 为数组时，*JL* 个锚点对的方差估计对于不同的 TSOA 组不同。单位为秒的平方。

**数据类型：** `single` | `double`

### **TxPos** — 发射锚点位置（米） 实值 *Q*×*J* 矩阵

发射锚点位置，输入为实值 *Q*×*J* 矩阵。*J* 是发射锚点的数量。每一列表示不同锚点的位置。位置可以是二维或三维的。对于二维位置，*Q*=2；对于三维位置，*Q*=3。`txpos` 的第 *j* 列表示第 *j* 个发射机在 *Q* 维笛卡尔空间中的位置。单位为米。

**示例：** `[20 31 –16; 13 64 –44]`

**数据类型：** `single` | `double`

### **RxPos** — 接收锚点位置（米） 实值 *Q*×*L* 矩阵

接收锚点位置，输入为实值 *Q*×*L* 矩阵。*L* 是接收锚点的数量。每一列表示不同锚点的位置。位置可以是二维或三维的。对于二维位置，*Q=2*；对于三维位置，*Q=3*。`rxpos` 的第 *l* 列表示第 *l* 个接收机在 *Q* 维笛卡尔空间中的位置。单位为米。

**示例：** `[20 31 –16; 13 64 –44]`

**数据类型：** `single` | `double`
### 输出

### **TgtPosEst** — 目标位置估计 实值 *Q*×1 向量

估计的目标位置，返回为 *Q*×1 向量，表示从 TSOA 测量获得的目标位置估计。单位为米。

**数据类型：** `single` | `double`

### **TgtPosCov** — 目标位置协方差矩阵 实值半正定 *Q*×*Q* 矩阵

目标位置协方差矩阵，返回为实值半正定 *Q*×*Q* 矩阵。该协方差矩阵表示根据 TSOA 位置估计器的 Cramer-Rao 下界（CRLB）计算得到的估计目标位置协方差。计算协方差需要已知 `TSOAVar`。当 `TSOAVar` 不准确时，`TgtPosCov` 也不准确。当 `TSOAVar` 准确且较小时，`TgtPosCov` 值表示 TSOA 位置估计的 CRLB。单位为米的平方。

#### 依赖关系

要启用此输出端口，请选中 **Output covariance of TSOA position estimate** 复选框。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst("LightSpeed")`（默认）| 正实数标量

信号传播速度，指定为正实数标量。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Output covariances of TSOA position estimates (meters-squared)** — 输出 TSOA 位置估计的协方差 `false` (0)（默认）| `true` (1)

选中 **Output covariances of TSOA position estimates** 复选框以启用包含 TSOA 位置协方差的 **TgtPosCov** 输出端口。单位为米平方。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

从到达时间和估计目标位置

从到达时间和（TSOA）测量值和锚点位置估计目标位置。该模块还估计到达时间和测量值的方差。
