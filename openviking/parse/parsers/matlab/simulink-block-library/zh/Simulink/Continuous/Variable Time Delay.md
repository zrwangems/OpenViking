---
type: simulink-block
title: 'Variable Time Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'variabletimedelay'
documentation_source_path: 'slref/variabletimedelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Time Delay

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: t0
  summary: 时间延迟输入 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: ti
  summary: 瞬时时间延迟输入 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: Port_1
  summary: 延迟信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

当您选中 **Handle zero delay** 参数时，此端口具有直接馈通。当您选中 **Direct feedthrough of input during linearization** 参数时，此端口在修剪和线性化操作期间具有直接馈通。

**数据类型：** `double`

### **t0** — 时间延迟输入 标量 | 向量 | 矩阵

时间延迟输入，指定为标量、向量或矩阵。当模块处于 `Variable time delay` 模式时，此值指定时间延迟。有关该计算的详细信息，请参阅 Variable Time Delay。

此端口具有直接馈通。

#### 依赖关系

要启用此端口，请将 **Select delay type** 设置为 `Variable time delay`。

**数据类型：** `double`

### **ti** — 瞬时时间延迟输入 标量 | 向量 | 矩阵

瞬时时间延迟输入，指定为标量、向量或矩阵。当模块处于 `Variable transport delay` 模式时，此值用于计算传输延迟。有关该计算的详细信息，请参阅 Variable Transport Delay。

此端口具有直接馈通。

#### 依赖关系

要启用此端口，请将 **Select delay type** 设置为 `Variable transport delay`。

**数据类型：** `double`
### 输出

### **Port\_1** — 延迟信号 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Select delay type
  summary: 延迟类型 Variable time delay | Variable transport delay
  group: ''
  block_parameter: VariableDelayType
  type: 字符向量、字符串
  values: '''Variable transport delay'' | ''Variable time delay'''
- name: Maximum delay
  summary: 时间延迟输入的最大值 10（默认）| 标量 | 向量
  group: ''
  block_parameter: MaximumDelay
  type: 字符向量、字符串
  values: 标量 | 向量
- name: Initial output
  summary: 初始输出 0（默认）| 标量 | 向量
  group: ''
  block_parameter: InitialOutput
  type: 字符向量、字符串
  values: 标量 | 向量
- name: Initial buffer size
  summary: 初始内存分配 1024（默认）| 标量
  group: ''
  block_parameter: MaximumPoints
  type: 字符向量、字符串
  values: 标量 | 向量
- name: Use fixed buffer size
  summary: 使用固定大小缓冲区 off（默认）| on
  group: ''
  block_parameter: FixedBuffer
  type: 字符向量、字符串
  values: '''off'' | ''on'''
- name: Handle zero delay
  summary: 允许零延迟的选项 off（默认）| on
  group: ''
  block_parameter: ZeroDelay
  type: 字符串 | 字符向量
  values: '''off'' | ''on'''
- name: Direct feedthrough of input during linearization
  summary: 在线性化和修剪操作期间使用零延迟的选项 off（默认）| on
  group: ''
  block_parameter: TransDelayFeedthrough
  type: 字符串 | 字符向量
  values: '''off'' | ''on'''
- name: Pade order (for linearization)
  summary: Pade 近似的阶数 0（默认）| 标量
  group: ''
  block_parameter: PadeOrder
  type: 字符向量、字符串
  values: 标量
- name: Absolute tolerance
  summary: 计算模块状态的绝对容差 auto（默认）| 正实数标量或向量
  group: ''
  block_parameter: AbsoluteTolerance
  type: 字符向量、字符串
  values: '''auto'' | ''-1'' | 任何正实数标量或向量'
- name: State Name (e.g., 'position')
  summary: 每个状态的唯一名称 ' '（默认）| 字符向量、字符串
  group: ''
  block_parameter: ContinuousStateAttributes
  type: 字符向量、字符串
  values: ''' '' | 用户定义的字符向量、用户定义的字符串'
```

### **Select delay type** — 延迟类型 `Variable time delay` | `Variable transport delay`

将延迟类型指定为 `Variable time delay` 或 `Variable transport delay`。

此参数的默认值取决于模块实现：Variable Time Delay 模块为 `Variable time delay`，Variable Transport Delay 模块为 `Variable transport delay`。

#### 依赖关系

- 将此参数设置为 `Variable time delay` 会启用 **Handle zero delay** 参数。
- 将此参数设置为 `Variable transport delay` 会启用 **Absolute tolerance** 和 **State Name** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariableDelayType` |
| **类型：** 字符向量、字符串 |
| **值：** `'Variable transport delay'` | `'Variable time delay'` |

### **Maximum delay** — 时间延迟输入的最大值 `10`（默认）| 标量 | 向量

设置时间延迟输入的最大值。此值定义此模块允许的最大时间延迟输入。模块会裁剪超过此值的任何延迟。此值不能为负。如果时间延迟变为负值，模块会将其裁剪为零并发出警告消息。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaximumDelay` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 |
| **默认：** `'10'` |

### **Initial output** — 初始输出 `0`（默认）| 标量 | 向量

指定在仿真时间首次超过时间延迟输入之前模块生成的输出。

#### 依赖关系

- 此模块的初始输出不能为 `inf` 或 `NaN`。
- `Run-to-run tunable parameter` 不能在仿真运行期间更改。但是，在仿真开始之前更改它不会导致 Accelerator 或 Rapid Accelerator 重新生成代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 |
| **默认：** `'0'` |

### **Initial buffer size** — 初始内存分配 `1024`（默认）| 标量

定义要存储的输入点数的初始内存分配。输入点定义截至当前仿真时间的输入信号历史。

- 如果输入点数超过初始缓冲区大小，模块会分配额外的内存。
- 仿真结束后，如果缓冲区不足且必须分配更多内存，则会显示一条消息。

#### 提示

- 由于分配内存会减慢仿真速度，如果仿真速度是个问题，请仔细选择此值。
- 对于长时间延迟，此模块可能会使用大量内存，特别是对于维度化输入。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaximumPoints` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 |
| **默认：** `'1024'` |

### **Use fixed buffer size** — 使用固定大小缓冲区 `off`（默认）| `on`

选中此复选框会使用固定大小缓冲区来保存先前时间步的输入数据。清除此复选框时，模块不使用固定大小缓冲区。

**Initial buffer size** 参数指定缓冲区大小。如果缓冲区已满，新数据将替换缓冲区中已有的数据。Simulink 软件使用线性外推来估计不在缓冲区中的输出值。

**注意**

即使您未选中此复选框，ERT 或 GRT 代码生成也会使用固定大小缓冲区。

#### 提示

- 如果输入数据是线性的，选中此复选框可以节省内存。
- 如果输入数据是非线性的，请不要选中此复选框。这样做可能会产生不准确的结果。

#### 编程用法

|  |
| --- |
| **模块参数：** `FixedBuffer` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Handle zero delay** — 允许零延迟的选项 `off`（默认）| `on`

指定模块是否允许延迟值为 `0`。

- `off` — 模块不允许零延迟。输入信号端口不具有直接馈通。
- `on` — 模块允许零延迟。输入信号端口具有直接馈通。

#### 依赖关系

要启用此参数，请将 **Select delay type** 参数设置为 `Variable time delay`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ZeroDelay` |
| **类型：** 字符串 | 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Direct feedthrough of input during linearization** — 在线性化和修剪操作期间使用零延迟的选项 `off`（默认）| `on`

指定在修剪或线性化操作期间是否对模块使用零延迟值。

#### 提示

当您使用函数 `linmod`、`dlinmod` 或 `trim` 时，选中此参数可能会导致模型中状态顺序的变化。要提取此新状态顺序：

1. 使用此命令编译模型，其中 `model` 是模型的名称。

   ```
       [sizes,x0,x_str] = model([],[],[],'lincompile');
   ```
2. 使用以下命令终止编译。

   ```
     model([],[],[],'term');
   ```

   输出参数 `x_str` 是 Simulink 模型中状态的元胞数组，包含新的状态顺序。当您将状态向量作为输入传递给 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用此新状态顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `TransDelayFeedthrough` |
| **类型：** 字符串 | 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Pade order (for linearization)** — Pade 近似的阶数 `0`（默认）| 标量

设置线性化例程的 Pade 近似阶数。

- 默认值为 `0`，这导致单位增益且无动态状态。
- 将阶数设置为正整数 `n` 会向模型添加 `n` 个状态，但会产生更准确的传输延迟线性模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `PadeOrder` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 |
| **默认：** `'0'` |

### **Absolute tolerance** — 计算模块状态的绝对容差 `auto`（默认）| 正实数标量或向量

指定用于计算模块状态的绝对容差。

#### 依赖关系

要启用此参数，请将 **Select delay type** 设置为 `Variable transport delay`。

#### 编程用法

|  |
| --- |
| **模块参数：** `AbsoluteTolerance` |
| **类型：** 字符向量、字符串 |
| **值：** `'auto'` | `'-1'` | 任何正实数标量或向量 |
| **默认：** `'auto'` |

### **State Name (e.g., 'position')** — 每个状态的唯一名称 `' '`（默认）| 字符向量、字符串

为每个状态分配唯一名称。如果此字段为空，则不进行名称分配。

#### 提示

- 要为单个状态分配名称，请在引号之间输入名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 状态名称仅适用于所选模块。
- 状态数必须能整除状态名称数。
- 您可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，您可以在具有四个状态的系统中指定两个名称。第一个名称适用于前两个状态，第二个名称适用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符串、元胞数组或结构体。

#### 依赖关系

要启用此参数，请将 **Select delay type** 设置为 `Variable transport delay`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ContinuousStateAttributes` |
| **类型：** 字符向量、字符串 |
| **值：** `' '` | 用户定义的字符向量、用户定义的字符串 |
| **默认：** `' '` |
## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `noa, b` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块的端口具有不同的直接馈通特性。  b 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产质量代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。

通常，请考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，请在 Simulink 编辑器的 **Apps** 选项卡上，在 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 会生成近似离散化。

## 版本历史

**在 R2007a 中引入**

## 描述

按可变时间量延迟输入

Variable Transport Delay 和 Variable Time Delay 模块在 Simulink® 模块库中显示为两个模块。但是，它们是同一个 Simulink 模块，只是 **Select delay type** 参数的设置不同。使用此参数指定模块运行的模式。

### Variable Time Delay

在此模式下，模块具有数据输入、时间延迟输入和数据输出。（有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。）当前时间步的输出等于其数据输入在先前时间步的值。此时间步是当前仿真时间减去由时间延迟输入指定的延迟时间。

y(t)=u(t−t0)=u(t−τ(t))

在仿真期间，模块将时间和输入值对存储在内部缓冲区中。在仿真开始时，模块输出 **Initial output** 参数的值，直到仿真时间超过时间延迟输入。然后，在每个仿真步，模块输出对应于当前仿真时间减去延迟时间的时间处的信号。

如果您希望输出位于输入存储时间之间的时间，并且求解器是连续求解器，则模块在点之间进行线性插值。如果时间延迟小于步长，模块从前一个点外推输出点。例如，考虑步长为 `1` 且当前时间为 `t = 5` 的固定步长仿真。如果延迟为 `0.5`，模块必须生成 `t = 4.5` 处的点，但最近存储的时间值在 `t = 4`。因此，模块从 `4` 处的输入外推 `4.5` 处的输入，并使用外推值作为 `t = 5` 处的输出。

从前一个时间步向前外推可能产生比从当前时间步向后外推更不准确的结果。但是，模块无法使用当前输入来计算其输出值，因为输入端口不具有直接馈通。

如果模型指定离散求解器，模块不会在时间步之间进行插值。相反，它返回所需值之前最近的存储值。

### Variable Transport Delay

在此模式下，当前时间步的模块输出等于其数据（顶部或左侧）输入在较早时间步的值，该时间步等于当前时间减去传输延迟。

y(t)=u(t−td(t))

Simulink 软件通过求解以下方程找到传输延迟 td(t)：

∫t−td(t)t1ti(τ)dτ=1

此方程涉及由时间延迟（底部或右侧）输入给出的瞬时时间延迟 ti(t)。

假设您想使用此模块来模拟流体通过管道的流动，其中流体速度随时间变化。在这种情况下，模块的时间延迟输入为

ti(t)=Lvi(t)

其中 `L` 是管道长度，vi(t) 是流体速度。
