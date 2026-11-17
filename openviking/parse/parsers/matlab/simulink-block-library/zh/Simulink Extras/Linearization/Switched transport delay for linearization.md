---
type: simulink-block
title: 'Transport Delay'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Linearization'
documentation_page: 'transportdelay'
documentation_source_path: '../simulink/slref/transportdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Transport Delay

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要延迟的输入信号，指定为标量、向量或矩阵。

当 **Time delay** 参数值为 `0` 时，此端口具有直接馈通。由于 **Time delay** 参数是运行时可调的，软件将 Transport Delay 模块视为该端口始终具有直接馈通。

**数据类型：** `double`
### 输出

### **Port\_1** — 延迟信号 标量 | 向量 | 矩阵

按指定时间量延迟后的输入信号。输出具有与输入信号相同的维度和数据类型。

**数据类型：** `double`

## 参数

### **Time delay** — 时间延迟 `1`（默认）| 标量 | 向量 | 矩阵

指定在输入信号传播到输出之前延迟的仿真时间量，指定为非负标量、向量或矩阵。

#### 编程使用：

|  |
| --- |
| **模块参数：** `DelayTime` |
| **类型：** 字符向量、字符串 |
| **值：** 非负标量、向量或矩阵 |
| **默认值：** `'1'` |

### **Initial output** — 初始输出值 `0`（默认）| 标量 | 向量 | 矩阵

指定在仿真时间首次超过时间延迟输入之前模块生成的输出，指定为标量、向量或矩阵。

#### 限制

此模块的初始输出不能为 `inf` 或 `NaN`。

`Run-to-run tunable parameter` 不能在仿真运行期间更改。但是，在仿真开始之前更改它不会导致 Accelerator 或 Rapid Accelerator 重新生成代码。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

### **Initial buffer size** — 初始内存分配 `1024`（默认）| 正整数标量

定义要存储的输入点数量的初始内存分配。

- 如果输入点数量超过初始缓冲区大小，模块会分配额外的内存。
- 仿真结束后，会显示所需的总缓冲区大小。

#### 提示

- 由于分配内存会减慢仿真速度，如果仿真速度是个问题，请仔细选择此值。
- 对于长时间延迟，此模块可能会使用大量内存，特别是对于多维输入。

#### 编程使用

|  |
| --- |
| **模块参数：** `BufferSize` |
| **类型：** 字符向量、字符串 |
| **值：** 正整数标量 |
| **默认值：** `'1024'` |

### **Use fixed buffer size** — 使用固定大小缓冲区 `off`（默认）| `on`

选中此复选框以使用固定大小缓冲区保存先前时间步的输入数据。

**Initial buffer size** 参数指定缓冲区的大小。如果缓冲区已满，新数据将替换缓冲区中已有的数据。Simulink® 软件使用线性外推来估计不在缓冲区中的输出值。

**注意**

如果您拥有 Simulink
Coder™ 许可证，即使您未选中此复选框，ERT 或 GRT 代码生成也会使用固定大小缓冲区。

#### 提示

- 如果输入数据是线性的，选中此复选框可以节省内存。
- 如果输入数据是非线性的，请勿选中此复选框。这样做可能会产生不准确的结果。

#### 编程使用

|  |
| --- |
| **模块参数：** `FixedBuffer` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Direct feedthrough of input during linearization** — 启用直接馈通 `off`（默认）| `on`

使模块在线性化和 trim 期间输出其输入，这将模块模式设置为直接馈通。

#### 提示

- 当您使用函数 `linmod`、`dlinmod` 或 `trim` 时，选中此复选框可能会导致模型中状态顺序的变化。要提取此新的状态顺序：

  1. 使用以下命令编译模型，其中 `model` 是 Simulink 模型的名称。

     ```
         [sizes, x0, x_str] = model([],[],[],'lincompile');
     ```
  2. 使用以下命令终止编译。

     ```
       model([],[],[],'term');
     ```
- 输出参数 `x_str` 是 Simulink 模型中状态的元胞数组，包含新的状态顺序。当您将状态向量作为输入传递给 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用此新的状态顺序。

#### 编程使用

|  |
| --- |
| **模块参数：** `TransDelayFeedthrough` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Pade order (for linearization)** — Pade 近似阶数 `0`（默认）| 标量 | 向量 | 矩阵

将线性化例程的 Pade 近似阶数设置为非负整数的标量、向量或矩阵。

- 默认值为 `0`，这导致单位增益且无动态状态。
- 将阶数设置为正整数 `n` 会向模型添加 `n` 个状态，但会得到更准确的传输延迟线性模型。

#### 编程使用

|  |
| --- |
| **模块参数：** `PadeOrder` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产质量代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常是可以接受的，但较小的嵌入式目标通常无法支持此类代码。

通常，考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，请在 Simulink 编辑器的 **Apps** 选项卡上，在 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 会产生近似离散化。

## 版本历史

**在 R2006a 之前引入**

## 描述

按给定时间量延迟输入

Transport Delay 模块将输入延迟指定的时间量。您可以使用此模块来模拟时间延迟。此模块的输入应为连续信号。

在仿真开始时，模块输出 **Initial output** 参数值，直到仿真时间超过 **Time delay** 参数。然后，模块开始生成延迟后的输入。在仿真期间，模块将输入点和仿真时间存储在缓冲区中。您可以使用 **Initial buffer size** 参数指定此大小。

当您希望在某个时间点获得输出，而该时间点与存储的输入值的时间不对应时，模块会在点之间进行线性插值。当延迟小于步长时，模块从最后一个输出点进行外推，这可能会产生不准确的结果。由于模块没有直接馈通，它无法使用当前输入来计算输出值。例如，考虑步长为 1 且当前时间为 t = 5 的固定步长仿真。如果延迟为 0.5，模块必须在 t = 4.5 处生成一个点。由于最近存储的时间值在 t = 4，模块执行前向外推。

Transport Delay 模块不对离散信号进行插值。相反，模块返回所需时间处的离散值。

此模块与 Unit Delay 模块不同，后者仅在采样命中时延迟并保持输出。

**提示**

避免使用 `linmod` 对包含 Transport Delay 模块的模型进行线性化。有关详细信息，请参阅 Linearizing Models。
