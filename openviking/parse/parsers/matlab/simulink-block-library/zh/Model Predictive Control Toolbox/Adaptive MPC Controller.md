---
type: simulink-block
title: 'Adaptive MPC Controller'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'adaptivempccontroller'
documentation_source_path: 'ref/adaptivempccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive MPC Controller

## 端口
```yaml
ports:
- name: model
  summary: 更新后的被控对象模型和标称工作点总线信号
  direction: input
- name: ref
  summary: 模型输出参考值 行向量 | 矩阵
  direction: input
- name: mo
  summary: 测量输出 向量
  direction: input
- name: x[k|k]
  summary: 自定义状态估计 向量
  direction: input
- name: md
  summary: 输入 行向量 | 矩阵
  direction: input
- name: ext.mv
  summary: 上一控制区间内被控对象所使用的控制信号向量
  direction: input
- name: switch
  summary: 启用或禁用优化标量
  direction: input
- name: mv.target
  summary: 操纵变量目标向量
  direction: input
- name: ymin
  summary: 最小输出变量约束向量 | 矩阵
  direction: input
- name: ymax
  summary: 最大输出变量约束向量 | 矩阵
  direction: input
- name: umin
  summary: 被操纵变量最小值约束向量 | 矩阵
  direction: input
- name: umax
  summary: 被操纵变量最大约束向量 | 矩阵
  direction: input
- name: E
  summary: 操纵变量约束矩阵 矩阵
  direction: input
- name: F
  summary: 受控输出约束矩阵 矩阵
  direction: input
- name: G
  summary: 自定义约束向量 行向量
  direction: input
- name: S
  summary: 测量扰动约束矩阵 矩阵
  direction: input
- name: y.wt
  summary: 输出变量调整权重 行向量 | 矩阵
  direction: input
- name: u.wt
  summary: 操纵变量调整权重 行向量 | 矩阵
  direction: input
- name: du.wt
  summary: 被操纵变量速率调节权重行向量 | 矩阵
  direction: input
- name: ecr.wt
  summary: 松弛变量调节权重标量
  direction: input
- name: p
  summary: 预测时域正整数
  direction: input
- name: m
  summary: 控制时域正整数 | 向量
  direction: input
- name: mv
  summary: 最优操纵变量控制动作列向量
  direction: output
- name: cost
  summary: 目标函数代价非负标量
  direction: output
- name: qp.status
  summary: 优化状态整数
  direction: output
- name: est.state
  summary: 估计的控制器状态向量
  direction: output
- name: mv.seq
  summary: 最优操纵变量序列矩阵
  direction: output
- name: x.seq
  summary: 最优预测模型状态序列矩阵
  direction: output
- name: y.seq
  summary: 最优输出变量序列矩阵
  direction: output
```

### 输入

#### 必需输入

### **model** — 更新后的被控对象模型和标称工作点总线信号

更新后的被控对象模型和标称工作点，指定为总线信号。将总线信号连接到 `model` 输入端口。在每个控制区间开始时，此信号会修改控制器对象的 `Model.Plant` 和 `Model.Nominal` 属性。

Adaptive MPC Controller 要求被控对象模型为无延迟的 LTI 离散时间状态空间对象。以下命令提取构成此类模型的状态空间矩阵。

```
[A,B,C,D] = ssdata(mpcobj.Model.Plant)
```

`model` 输入的用途是将这些矩阵替换为具有相同维度并表示相同控制区间的新矩阵。您还必须保持输入、输出和状态变量在控制器 `Model.Plant` 属性中出现的顺序。

当运行在：

- Adaptive MPC 模式时，连接到 `model` 输入端口的总线必须包含以下信号，每个信号由指定的名称标识：

  - `A` —
    *nx*×*nx*
    矩阵信号，其中 *nx* 是
    被控对象模型状态的数量。
  - `B` —
    *nx*×*nu*
    矩阵信号，其中 *nu* 是被控对象模型输入的总数（即操纵变量、可测
    扰动和不可测扰动）。
  - `C` —
    *ny*×*nx*
    矩阵信号，其中 *ny* 是被控对象模型输出的数量。
  - `D` —
    *ny*×*nu*
    矩阵信号。
  - `X` — 长度为
    *nx* 的向量信号，替换控制器
    `Model.Nominal.X` 属性。
  - `Y` — 长度为
    *ny* 的向量信号，替换控制器
    `Model.Nominal.Y` 属性。
  - `U` — 长度为
    *nu* 的向量信号，替换控制器
    `Model.Nominal.U` 属性。
  - `DX` — 长度为
    *nx* 的向量信号，替换控制器
    `Model.Nominal.DX` 属性。它必须适合与假定控制区间的离散时间模型一起使用。有关
    更多信息，请参阅 Adaptive and Time-Varying MPC。

    要计算 `DX` 值，请使用模型的离散时间状态
    更新函数 (*f*)。这里，
    *uk* 和
    *xk* 分别是当前时间步的输入和
    状态值。

    DX=f(uk,xk)−xk
- Time-varying MPC 模式时，连接到 `model`
  输入端口的总线必须包含以下 3 维总线信号：

  - `A` —
    *nx*×*nx*×(*p*+1)
    矩阵信号
  - `B` —
    *nx*×*nu*×(*p*+1)
    矩阵信号
  - `C` —
    *ny*×*nx*×(*p*+1)
  - `D` —
    *ny*×*nu*×(*p*+1)
    矩阵信号
  - `X` —
    *nx*×(*p*+1)
    矩阵信号
  - `Y` —
    *ny*×(*p*+1)
    矩阵信号
  - `U` —
    *nu*×(*p*+1)
    矩阵信号
  - `DX` —
    *nx*×(*p*+1)
    矩阵信号

  这里，*p* 是控制器预测时域。对于每个
  信号，指定 *p*+1 个值，表示预测时域每一步的模型和标称
  条件。有关更多信息，请参阅 Time-Varying MPC。

构成总线的一种方法是使用 Bus Creator (Simulink) 模块。

#### 依赖关系

**model** 中总线元素的维度取决于控制器的运行模式。要将控制器置于：

- Adaptive MPC 模式，清除 **Linear Time-Varying (LTV)
  plants** 参数
- Time-varying MPC 模式，选中 **Linear Time-Varying (LTV)
  plants** 参数

### **ref** — 模型输出参考值 行向量 | 矩阵

被控对象输出参考值，指定为行向量信号或矩阵信号。

要在整个预测时域内使用相同的参考值，请将 **ref** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出变量的数量。每个元素指定一个输出变量的参考值。

要在预测时域内（预览）从时刻 *k*+1 到时刻 *k*+*p* 改变参考值，请将 **ref** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。此处，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的参考值。如果指定的行数少于 *p* 行，则最终参考值将用于预测时域的剩余步长。

### **mo** — 测量输出 向量

测量输出，指定为向量信号。该模块使用测量的被控对象输出来改进其状态估计。如果控制器使用默认状态估计，则必须将测量的被控对象输出连接到 **mo** 输入端口。如果控制器使用自定义状态估计，则必须将估计的被控对象状态连接到 **x[k|k]** 输入端口。

#### 依赖关系

要启用此端口，请清除 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **x[k|k]** — 自定义状态估计 向量

自定义状态估计，指定为向量信号。该模块使用连接的状态估计，而不是使用内置估计器来估计状态。如果控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

即使噪声模型状态（如果有）不用于 MPC 优化，自定义状态向量也必须包含控制器的 `mpcstate` 对象中定义的所有状态，包括被控对象、扰动和噪声模型状态。

当替代估计技术被认为优于内置估计器时，或者当状态完全可测量时，请使用自定义状态估计。

#### 依赖关系

要启用此端口，请选择 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

#### 附加输入

### **md** — 输入 行向量 | 矩阵

如果控制器预测模型具有测量扰动，则必须启用此端口，并将行向量或矩阵信号连接到该端口。

要在整个预测时域内使用相同的测量扰动值，请将 **md** 连接到具有 *Nmd* 个元素的行向量信号，其中 *Nmd* 是操纵变量的数量。每个元素指定一个测量扰动的值。

要在预测时域内（预览）从时刻 *k* 到时刻 *k*+*p* 改变扰动，请将 **md** 连接到具有 *Nmd* 列和最多 *p*+1 行的矩阵信号。此处，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的扰动。如果指定的行数少于 *p*+1 行，则最终扰动将用于预测时域的剩余步长。

#### 依赖关系

要启用此端口，请选择 **Measured disturbances** 参数。

### **ext.mv** — 上一控制区间内被控对象所使用的控制信号向量

上一控制区间内被控对象所使用的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。在以下情况下，使用此输入端口来提高状态估计精度：

- 您知道您的控制器并不总是控制被控对象。
- 施加到被控对象的实际 MV 信号可能不同于控制器生成的值，例如在控制信号饱和时。

控制器状态估计假设 MV 是分段常数。因此，在时刻 *tk*，**ext.mv** 值必须包含时刻 *tk–1* 与 *tk* 之间的有效 MV。例如，如果 MV 在此区间内实际上是变化的，您可以提供在时刻 *tk* 评估的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间内实际施加到被控对象的 MV 信号。通常，这些 MV 信号是控制器生成的值，但并非总是如此。例如，如果您的控制器离线并运行在跟踪模式（即控制器输出不驱动被控对象），则将实际控制信号馈送到 **ext.mv** 有助于在控制器重新在线时实现无扰切换。
- 当控制器驱动被控对象时，插入一个 Memory 模块或 Unit Delay 模块，以反馈上一控制区间内施加到被控对象的 MV 信号。这还可以避免从 **ext.mv** 输入端口到 **mv** 输出端口的直接馈通，从而防止 Simulink® 模型中出现代数环。

有关使用外部操纵变量输入端口进行无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **External manipulated variable** 参数。

### **switch** — 启用或禁用优化标量

要关闭控制器优化计算，请将 **switch** 连接到非零信号。

当不需要控制器输出时，例如系统手动运行或另一个控制器已接管时，禁用优化计算可减少计算工作量。但是，控制器会继续以通常方式更新其内部状态估计。因此，只要 **switch** 信号返回零，它就准备好恢复优化计算。当控制器优化关闭时，该模块会将当前 **ext.mv** 信号传递到控制器输出。如果未启用 **ext.mv** 输入端口，则控制器输出保持在禁用优化时的值。

有关使用外部操纵变量输入端口进行无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **Use external signal to enable or disable optimization** 参数。

### **mv.target** — 操纵变量目标向量

要指定操纵变量目标，请启用此输入端口，并连接一个向量信号。要使给定的操纵变量跟踪其指定的目标值，您还必须为该操纵变量指定非零的整定权重。

运行时提供的 **mv.target** 值适用于整个预测时域。

#### 依赖关系

要启用此端口，请选择 **Targets for manipulated variables** 参数。

#### 在线约束

### **ymin** — 最小输出变量约束向量 | 矩阵

要指定运行时最小输出变量约束，请启用此输入端口。如果此端口被禁用，模块将使用其 `mpc` 控制器对象的 `OutputVariables.Min` 属性中指定的下界。如果控制器对象中未为某个输出变量指定下界，则模块在运行时将忽略对应的连接信号。

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 更改边界，请将 **ymin** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*Ny* 是对象输出数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界将应用于预测时域的剩余部分。如果只有一个输出变量，并且连接了不超过 *p* 个元素的向量信号，则这些元素将用于整个预测时域。

**ymin** 信号的第 `i` 列对应于第 `i` 个对象输出，并在运行时替换 `mpc` 对象的 `OutputVariables(i).Max` 属性。替换行为取决于两个变量的维度。

**`mpc` 对象中的标量 `OutputVariables(i).Min`（第 `i` 个对象输出的常量边界，应用于所有预测步长）**

| **ymin** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymin**（单个输出，常量边界） | **ymin** 替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 列向量 **ymin**（单个输出，时变边界） | **ymin** 用时变边界替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 行向量 **ymin**（多个输出，常量边界） | **ymin** 的第 `i` 个元素替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 矩阵 **ymin**（多个输出，时变边界） | **ymin** 的第 `i` 列用时变边界替换 `OutputVariables(i).Min` 中定义的常量边界。 |

**`mpc` 对象中的向量 `OutputVariables(i).Min`（第 `i` 个对象输出的时变边界，在不同预测步长具有不同值）**

| **ymin** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymin**（单个输出，常量边界） | **ymin** 替换 `OutputVariables.Min` 中的第一个有限元素，并且 `OutputVariables.Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `OutputVariables.Min` 向量定义的轮廓。 |
| 列向量 **ymin**（单个输出，时变边界） | **ymin** 替换 `OutputVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **ymin**（多个输出，常量边界） | **ymin** 的第 `i` 个元素替换 `OutputVariables(i).Min` 中的第一个有限元素，并且 `OutputVariables(i).Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `OutputVariables(i).Min` 向量定义的轮廓。 |
| 矩阵 **ymin**（多个输出，时变边界）。 | **ymin** 的第 `i` 列替换 `OutputVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |

#### 依赖关系

要启用此端口，请选择 **Lower OV limits** 参数。

### **ymax** — 最大输出变量约束向量 | 矩阵

要指定运行时最大输出变量约束，请启用此输入端口。如果此端口被禁用，模块将使用其 `mpc` 控制器对象的 `OutputVariables.Max` 属性中指定的上界。如果控制器对象中未为某个输出变量指定上界，则模块在运行时将忽略对应的连接信号。

要在从时间 *k*+1 到时间 *k*+*p* 的预测时域内更改边界，请将 **ymax** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*Ny* 是对象输出数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界将应用于预测时域的剩余部分。如果只有一个输出变量，并且连接的是不超过 *p* 个元素的向量信号，则这些元素将用于整个预测时域。

**ymax** 信号的第 `i` 列对应于第 `i` 个对象输出，并在运行时替换 `mpc` 对象的 `OutputVariables(i).Max` 属性。替换行为取决于两个变量的维度。

**`mpc` 对象中的标量 `OutputVariables(i).Max`（第 `i` 个对象输出的常数边界，应用于所有预测步长）**

| **ymax** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymax**（单个输出，常数边界） | **ymax** 替换 `OutputVariables(i).Max` 中定义的常数边界。 |
| 列向量 **ymax**（单个输出，时变边界） | **ymax** 将 `OutputVariables(i).Max` 中定义的常数边界替换为时变边界。 |
| 行向量 **ymax**（多个输出，常数边界） | **ymax** 的第 `i` 个元素替换 `OutputVariables(i).Max` 中定义的常数边界。 |
| 矩阵 **ymax**（多个输出，时变边界） | **ymax** 的第 `i` 列将 `OutputVariables(i).Max` 中定义的常数边界替换为时变边界。 |

**`mpc` 对象中的向量 `OutputVariables(i).Max`（第 `i` 个对象输出的时变边界，在不同预测步长具有不同值）**

| **ymax** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymax**（单个输出，常数边界） | **ymax** 替换 `OutputVariables.Max` 中的第一个有限元素，并且 `OutputVariables.Max` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `OutputVariables.Max` 向量定义的轮廓。 |
| 列向量 **ymax**（单个输出，时变边界） | **ymax** 替换 `OutputVariables(i).Max` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **ymax**（多个输出，常数边界） | **ymax** 的第 `i` 个元素替换 `OutputVariables(i).Max` 中的第一个有限元素，并且 `OutputVariables(i).Max` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `OutputVariables(i).Max` 向量定义的轮廓。 |
| 矩阵 **ymax**（多个输出，时变边界）。 | **ymax** 的第 `i` 列替换 `OutputVariables(i).Max` 中定义的时变边界，并丢弃原始边界轮廓。 |

#### 依赖关系

要启用此端口，请选择 **Upper OV limits** 参数。

### **umin** — 被操纵变量最小值约束向量 | 矩阵

要指定运行时被操纵变量最小值约束，请启用此输入端口。
如果此端口被禁用，模块将使用其 `mpc` 控制器对象的
`ManipulatedVariables.Min` 属性中指定的下界。如果某个被操纵变量在控制器对象中
未指定下界，则运行时模块将忽略对应的
已连接信号。

要在预测时域内从时间 *k* 到
时间 *k*+*p*-1 更改边界，请将 **umin** 连接到
具有 *Nmv* 列且最多
*p* 行的矩阵信号。此处，*Nmv* 是
被操纵变量的数量，*k* 是当前时间，*p*
是预测时域。每一行包含一个
预测时域步长的边界。如果指定的行数少于 *p* 行，则最后一行中的边界
适用于预测时域的剩余部分。如果只有一个
被操纵变量，并且连接了不超过 *p* 个元素的向量信号，
则这些元素将在预测时域内使用。

**umin** 信号的第 `i` 列对应于
第 `i` 个被操纵变量，并在运行时替换 `mpc`
对象的 `ManipulatedVariables(i).Max` 属性。替换行为取决于
两个变量的维度。

**`mpc` 对象中的标量 `ManipulatedVariables(i).Min`（第 `i` 个被操纵变量的常量边界，
应用于所有预测步长）**

| **umin** 维度 | 替换行为 |
| --- | --- |
| 标量 **umin**（单输出，常量边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |
| 列向量 **umin**（单输出，时变边界） | **umin** 用 时变边界替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |
| 行向量 **umin**（多输出，常量边界） | **umin** 的第 `i` 个元素替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |
| 矩阵 **umin**（多输出，时变边界） | **umin** 的第 `i` 列用 时变边界替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Min`（第 `i` 个被操纵变量的时变边界，
在不同预测步长具有不同值）**

| **umin** 维度 | 替换行为 |
| --- | --- |
| 标量 **umin**（单输出，常量边界） | **umin** 替换 `ManipulatedVariables.Min` 中的第一个有限元素，并且 `ManipulatedVariables.Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `ManipulatedVariables.Min` 向量定义的轮廓。 |
| 列向量 **umin**（单输出，时变边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并且原始边界轮廓被丢弃。 |
| 行向量 **umin**（多输出，常量边界） | **umin** 的第 `i` 个分量替换 `ManipulatedVariables(i).Min` 中的第一个有限元素，并且 `ManipulatedVariables(i).Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `ManipulatedVariables(i).Min` 向量定义的轮廓。 |
| 矩阵 **umin**（多输出，时变边界）。 | **umin** 的第 `i` 列替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并且原始边界轮廓被丢弃。 |

#### 依赖关系

要启用此端口，请选择 **Lower MV limits**
参数。

### **umax** — 被操纵变量最大约束向量 | 矩阵

要指定运行时被操纵变量最大约束，请启用此输入端口。
如果此端口被禁用，模块将使用其 `mpc` 控制器对象的
`ManipulatedVariables.Max` 属性中指定的上界。如果某个被操纵变量在控制器对象中
未指定上界，则运行时模块将忽略对应的
已连接信号。

要在预测时域内从时间 *k* 到
时间 *k*+*p*-1 更改边界，请将 **umax** 连接到
一个具有 *Nmv* 列且最多
*p* 行的矩阵信号。这里，*Nmv* 是
被操纵变量的数量，*k* 是当前时间，*p*
是预测时域。每一行包含一个
预测时域步长的边界。如果指定的行数少于 *p* 行，则最后一行中的边界
将应用于预测时域的剩余部分。如果只有一个
被操纵变量，并且连接了一个不超过 *p* 个元素的向量信号，
则这些元素将用于整个预测时域。

**umax** 信号的第 `i` 列对应于
第 `i` 个被操纵变量，并在运行时替换 `mpc`
对象的 `ManipulatedVariables(i).Max` 属性。替换行为取决于
两个变量的维度。

**`mpc` 对象中的标量 `ManipulatedVariables(i).Max`（第 `i` 个被操纵变量的常量边界，
应用于所有预测步长）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单输出，常量边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 列向量 **umax**（单输出，时变边界） | **umax** 用时变边界替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 行向量 **umax**（多输出，常量边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 矩阵 **umax**（多输出，时变边界） | **umax** 的第 `i` 列用时变边界替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Max`
（第 `i` 个被操纵变量的时变边界，
在不同预测步长具有不同值）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单输出，常量边界） | **umax** 替换 `ManipulatedVariables.Max` 中的第一个有限元素，并且 `ManipulatedVariables.Max` 中的其余元素以相同的位移量向上或向下移动，以保留由原始 `ManipulatedVariables.Max` 向量定义的轮廓。 |
| 列向量 **umax**（单输出，时变边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并且原始边界轮廓将被丢弃。 |
| 行向量 **umax**（多输出，常量边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中的第一个有限元素，并且 `ManipulatedVariables(i).Max` 中的其余元素以相同的位移量向上或向下移动，以保留由原始 `ManipulatedVariables(i).Max` 向量定义的轮廓。 |
| 矩阵 **umax**（多输出，时变边界）。 | **umax** 的第 `i` 列替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并且原始边界轮廓将被丢弃。 |

#### 依赖关系

要启用此端口，请选择 **Upper MV limits**
参数。

### **E** — 操纵变量约束矩阵 矩阵

操纵变量约束矩阵，指定为 *Nc*×*Nmv* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Nmv* 是操纵变量的数量。

如果在 `mpc` 对象中定义了 `E`，则必须将信号连接到 **E** 输入端口。否则，连接一个大小正确的零矩阵。

要在运行时指定混合输入/输出约束，请将 **E** 输入端口与 **F**、**G** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `E` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **F** — 受控输出约束矩阵 矩阵

受控输出约束矩阵，指定为 *Nc*×*Ny* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Ny* 是被控对象输出的数量。如果在 `mpc` 对象中定义了 `F`，则必须将具有相同行数的信号连接到 **F** 输入端口。否则，连接一个大小正确的零矩阵。

要在运行时指定混合输入/输出约束，请将 **F** 输入端口与 **E**、**G** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `F` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **G** — 自定义约束向量 行向量

自定义约束向量，指定为长度为 *Nc* 的行向量信号，其中 *Nc* 是混合输入/输出约束的数量。如果在 `mpc` 对象中定义了 `G`，则必须将具有相同行数的信号连接到 **G** 输入端口。否则，连接一个大小正确的零矩阵。

要在运行时指定混合输入/输出约束，请将 **G** 输入端口与 **E**、**F** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `G` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **S** — 测量扰动约束矩阵 矩阵

测量扰动约束矩阵，指定为 *Nc*×*nN* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Nv* 是测量扰动的数量。如果在 `mpc` 对象中定义了 `S`，则必须将具有相同行数的信号连接到 **S** 输入端口。否则，连接一个大小正确的零矩阵。

要在运行时指定混合输入/输出约束，请将 **S** 输入端口与 **E**、**F** 和 **G** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `G` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。仅当 `mpc` 对象具有可测扰动时，才会添加此端口。

#### 在线调整权重

### **y.wt** — 输出变量调整权重 行向量 | 矩阵

要指定运行时输出变量调整权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.OutputVariables` 属性中指定的调整权重。这些调整权重用于惩罚输出参考值的偏差。

如果 MPC 控制器对象在预测时域内使用恒定的输出调整权重，则运行时只能指定恒定的输出调整权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的输出调整权重，则运行时只能指定时变输出调整权重。

要在预测时域内使用恒定调整权重，请将 **y.wt** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出数量。每个元素为输出变量指定一个非负调整权重。有关指定调整权重的更多信息，请参阅 Tune Weights。

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 变化调整权重，请将 **y.wt** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调整权重。如果指定的行数少于 *p* 行，则最后一行的调整权重适用于预测时域的剩余部分。有关在预测时域内变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **OV weights** 参数。

### **u.wt** — 操纵变量调整权重 行向量 | 矩阵

要指定运行时操纵变量调整权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariables` 属性中指定的调整权重。这些调整权重用于惩罚 MV 目标值的偏差。

如果 MPC 控制器对象在预测时域内使用恒定的操纵变量调整权重，则运行时只能指定恒定的操纵变量调整权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的操纵变量调整权重，则运行时只能指定时变操纵变量调整权重。

要在预测时域内使用相同的调整权重，请将 **u.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是操纵变量数量。每个元素为操纵变量指定一个非负调整权重。有关指定调整权重的更多信息，请参阅 Tune Weights。

要在预测时域内从时间 *k* 到时间 *k*+*p*-1 变化调整权重，请将 **u.wt** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调整权重。如果指定的行数少于 *p* 行，则最后一行的调整权重适用于预测时域的剩余部分。有关在预测时域内变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MV weights** 参数。

### **du.wt** — 被操纵变量速率调节权重行向量 | 矩阵

要指定运行时被操纵变量速率调节权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariablesRate` 属性中指定的调节权重。这些调节权重会惩罚控制量的大幅变化。

如果 MPC 控制器对象在预测时域上使用恒定的被操纵变量速率调节权重，则你在运行时只能指定恒定的被操纵变量速率调节权重。类似地，如果 MPC 控制器对象使用随预测时域变化的被操纵变量速率调节权重，则你在运行时只能指定随时间变化的被操纵变量速率调节权重。

要在预测时域上使用相同的调节权重，请将 **du.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是被操纵变量的数量。每个元素为一个被操纵变量速率指定一个非负调节权重。有关指定调节权重的更多信息，请参阅 Tune Weights。

要使调节权重在预测时域上从时间 *k* 变化到时间 *k*+*p*-1，请将 **du.wt** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调节权重。如果你指定的行数少于 *p*，则最后一行的调节权重将应用于预测时域的剩余部分。有关在预测时域上变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MVRate weights** 参数。

### **ecr.wt** — 松弛变量调节权重标量

要指定运行时松弛变量调节权重，请启用此输入端口并连接一个标量信号。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ECR` 属性中指定的调节权重。

除非你的控制器对象定义了软约束，且其关联的 ECR 值非零，否则松弛变量调节权重不起作用。如果存在软约束，增大 **ecr.wt** 值会使这些约束相对更难满足。控制器随后会更高优先级地最小化预测最坏情况约束违反的幅度。

#### 依赖关系

要启用此端口，请选择 **ECR weight** 参数。

#### 在线时域

### **p** — 预测时域正整数

预测时域，指定为正整数信号。预测时域信号值必须小于或等于 **Maximum prediction horizon** 参数。

在运行时，`p` 的值会覆盖控制器对象中指定的默认预测时域。有关更多信息，请参阅 Adjust Horizons at Run Time。

#### 依赖关系

要启用此端口，请选择 **Adjust prediction horizon and control horizon at run time** 参数。

### **m** — 控制时域正整数 | 向量

控制时域，指定为以下之一：

- 小于或等于预测时域的正整数信号。
- 指定分块区间长度的正整数向量信号。有关更多信息，请参阅 Manipulated Variable Blocking。

在运行时，`m` 的值会覆盖控制器对象中指定的默认控制时域。有关更多信息，请参阅 Adjust Horizons at Run Time。

#### 依赖关系

要启用此端口，请选择 **Adjust prediction horizon and control horizon at run time** 参数。
### 输出

#### 必需输出

### **mv** — 最优操纵变量控制动作列向量

最优操纵变量控制动作，输出为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是操纵变量的数量。

如果求解器收敛到局部最优解（**qp.status** 为正），则 **mv** 包含最优解。

如果求解器失败（**qp.status** 为负），则 **mv** 保持在其最近一次成功的解；即控制器输出冻结。

如果求解器达到最大迭代次数而未找到最优解
（**qp.status** 为零），并且控制器的
`Optimization.UseSuboptimalSolution` 属性为：

- `true`，则 **mv** 包含次优解
- `false`，则 **mv** 则 **mv** 保持在其最近一次成功的解

#### 附加输出

### **cost** — 目标函数代价非负标量

目标函数代价，输出为非负标量信号。代价量化了控制器实现其目标的程度。代价值使用缩放后的 MPC 代价函数计算，其中每一项都是无偏移且无量纲的。

仅当 **qp.status** 输出为非负时，代价值才有意义。

#### 依赖关系

要启用此端口，请选择 **Optimal cost** 参数。

### **qp.status** — 优化状态整数

优化状态，输出为整数信号。

如果控制器针对给定控制区间求解 QP 问题，则
**qp.status** 输出返回计算中使用的 QP 求解器迭代次数。该值是一个有限正整数，并且与计算所需时间成正比。因此，较大的值意味着该时间区间内模块执行相对较慢。

QP 求解器可能由于以下原因无法找到最优解：

- **qp.status** = `0` — QP 求解器无法在 `mpc` 对象中指定的最大迭代次数内找到解。在这种情况下，如果控制器的 `Optimizer.UseSuboptimalSolution` 属性为 `false`，则模块将其 **mv** 输出保持在最近一次成功的解。否则，它使用最后一次求解器迭代中找到的次优解。
- **qp.status** = `-1` — QP 求解器检测到不可行的 QP 问题。有关一个大幅、持续扰动驱动输出变量超出其指定边界的示例，请参见 Monitoring Optimization Status to Detect Controller Failures。在这种情况下，模块将其 **mv** 输出保持在最近一次成功的解。
- **qp.status** = `-2` — QP 求解器在求解严重病态的 QP 问题时遇到数值困难。在这种情况下，模块将其 **mv** 输出保持在最近一次成功的解。

在实时应用中，您可以使用 **qp.status** 设置报警或采取其他特殊操作。

#### 依赖关系

要启用此端口，请选择 **Optimization status** 参数。

### **est.state** — 估计的控制器状态向量

每个控制时刻的估计控制器状态，返回为向量信号。估计状态包括被控对象、扰动和噪声模型状态。如果使用自定义状态估计，则该输出信号与
**x[k|k]** 输入信号具有相同的值。

#### 依赖关系

要启用此端口，请选择 **Estimated controller states**
参数。

#### 最优序列

### **mv.seq** — 最优操纵变量序列矩阵

最优操纵变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nmv* 列，其中 *p* 是预测时域，*Nmv* 是操纵变量个数。

**mv.seq** 的前 *p* 行包含从当前时刻 *k* 到时刻 *k*+*p*-1 计算得到的最优操纵变量值。**mv.seq** 的第一行包含当前操纵变量值（输出 **mv**）。由于控制器在时刻 *k*+*p* 不计算最优控制量，**mv.seq** 的最后两行相同。

#### 依赖关系

要启用此端口，请选择 **Optimal control sequence** 参数。

### **x.seq** — 最优预测模型状态序列矩阵

最优预测模型状态序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nx* 列，其中 *p* 是预测时域，*Nx* 是状态个数。

**x.seq** 的第一行包含当前估计状态值，来自内置状态估计器或自定义状态估计模块输入 **x[k|k]**。**x.seq** 的接下来 *p* 行包含从时刻 *k*+1 到时刻 *k*+*p* 计算得到的最优状态值。

#### 依赖关系

要启用此端口，请选择 **Optimal state sequence** 参数。

### **y.seq** — 最优输出变量序列矩阵

最优输出变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Ny* 列，其中 *p* 是预测时域，*Ny* 是输出变量个数。

**y.seq** 的前 *p* 行包含从当前时刻 *k* 到时刻 *k*+*p*-1 计算得到的最优输出值。**y.seq** 的第一行基于当前估计状态和当前测量扰动（输入 **md** 的第一行）计算。由于控制器在时刻 *k*+*p* 不计算最优输出值，**y.seq** 的最后两行相同。

#### 依赖关系

要启用此端口，请选择 **Optimal output sequence** 参数。
## 参数
```yaml
parameters:
- name: Adaptive MPC Controller
  summary: 控制器对象 mpc 对象名称
  group: ''
  block_parameter: mpcobj
  type: string, character vector
  default: '""'
- name: Initial Controller State
  summary: 初始状态 mpcstate 对象名称
  group: ''
  block_parameter: x0
  type: string, character vector
  default: '""'
- name: Measured disturbance
  summary: 添加可测扰动输入端口 on（默认）| off
  group: ''
  block_parameter: md_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"on"'
- name: External manipulated variable
  summary: 添加外部操纵变量输入端口 off（默认）| on
  group: ''
  block_parameter: mv_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Targets for manipulated variables
  summary: 添加操纵变量目标输入端口 off（默认）| on
  group: ''
  block_parameter: uref_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Optimal cost
  summary: 添加最优代价输出端口 off（默认）| on
  group: ''
  block_parameter: return_cost
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Optimization status
  summary: 添加优化状态输出端口 off（默认）| on
  group: ''
  block_parameter: return_qpstatus
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Estimated controller states
  summary: 添加估计状态输出端口 off（默认）| on
  group: ''
  block_parameter: return_state
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Optimal control sequence
  summary: 添加最优控制序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_mvseq
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Optimal state sequence
  summary: 添加最优状态序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_xseq
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Optimal output sequence
  summary: 添加最优输出序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_ovseq
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Use custom state estimation instead of using the built-in Kalman filter
  summary: 使用自定义状态估计输入端口 off（默认）| on
  group: ''
  block_parameter: state_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Linear Time-Varying (LTV) plants
  summary: 使用自定义状态估计输入端口 off（默认）| on
  group: ''
  block_parameter: isltv_plant
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Lower OV limits
  summary: 添加最小 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymin_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Upper OV limits
  summary: 添加最大 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymax_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Lower MV limits
  summary: 添加最小 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umin_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Upper MV limits
  summary: 添加最大 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umax_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Custom constraints
  summary: 为混合输入/输出线性约束矩阵添加输入端口 off（默认）| on
  group: ''
  block_parameter: cc_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV weights
  summary: 添加 OV 调节权重输入端口 off（默认）| on
  group: ''
  block_parameter: ywt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV weights
  summary: 添加 MV 调节权重输入端口 off（默认）| on
  group: ''
  block_parameter: uwt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MVRate weights
  summary: 添加 MV 速率调节权重输入端口 off（默认）| on
  group: ''
  block_parameter: duwt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Slack variable weight
  summary: 添加 ECR 调节权重输入端口 off（默认）| on
  group: ''
  block_parameter: rhoeps_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Adjust prediction horizon and control horizon at run time
  summary: 添加预测时域和控制时域输入端口 off（默认）| on
  group: ''
  block_parameter: pm_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Maximum prediction horizon
  summary: 添加预测时域输入端口 10（默认）| 正整数
  group: ''
  block_parameter: MaximumP
  type: string, character vector
  default: '"10"'
- name: Inherit sample time
  summary: 从父子系统继承模块采样时间 off（默认）| on
  group: ''
  block_parameter: SampleTimeInherited
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: Use external signal to enable or disable optimization
  summary: 添加开关输入端口 off（默认）| on
  group: ''
  block_parameter: switch_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
```

### **Adaptive MPC Controller** — 控制器对象 `mpc` 对象名称

指定一个 `mpc` 对象来定义 MPC 控制器，方法是输入在模块标称工作点处设计的 `mpc` 对象的名称。在运行时，控制器在每个控制时刻用 **model** 输入端口指定的数据替换原始预测模型（`A`、`B`、`C` 和 `D`）和标称值（`U`、`Y`、`X` 和 `DX`）。

默认情况下，模块假定所有其他控制器对象属性（例如整定权重、约束）保持不变。您可以使用 **Online Features** 部分中的选项覆盖此假设。

以下限制适用于 `mpc` 控制器对象：

- 它必须存在于 MATLAB® 工作区中。
- 其预测模型必须是无延迟的 LTI 离散时间状态空间对象。使用 `absorbDelay` 命令将延迟转换为离散状态。预测模型中 `A`、`B`、`C` 和 `D` 矩阵的维度决定了 `model` 输入端口信号所需的维度。

#### 编程使用

|  |
| --- |
| **模块参数**：`mpcobj` |
| **类型**：string, character vector |
| **默认值**：`""` |

### **Initial Controller State** — 初始状态 `mpcstate` 对象名称

指定初始控制器状态。如果将此参数留空，模块将使用 `mpc` 对象的 `Model.Nominal` 属性中定义的标称值。要覆盖默认值，请在工作区中创建一个 `mpcstate` 对象，并在该字段中输入其名称。

使用此参数可确保控制器状态尽可能准确地反映仿真开始时被控对象的状态。此初始状态可以不同于 `mpc` 对象中定义的标称状态。

如果启用了自定义状态估计，模块将忽略 **Initial Controller State** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `x0` |
| **类型：** string, character vector |
| **默认值：** `""` |

#### 常规选项卡

### **Measured disturbance** — 添加可测扰动输入端口 `on`（默认）| `off`

如果您的控制器具有可测扰动，则必须选择此参数以将 **md** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `md_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **External manipulated variable** — 添加外部操纵变量输入端口 `off`（默认）| `on`

选择此参数以将 **ext.mv** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `mv_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Targets for manipulated variables** — 添加操纵变量目标输入端口 `off`（默认）| `on`

选择此参数以将 **mv.target** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `uref_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Optimal cost** — 添加最优代价输出端口 `off`（默认）| `on`

选择此参数以将 **cost** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_cost` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Optimization status** — 添加优化状态输出端口 `off`（默认）| `on`

选择此参数以将 **qp.status** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_qpstatus` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Estimated controller states** — 添加估计状态输出端口 `off`（默认）| `on`

选择此参数以将 **est.state** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_state` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Optimal control sequence** — 添加最优控制序列输出端口 `off`（默认）| `on`

选择此参数以将 **mv.seq** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_mvseq` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Optimal state sequence** — 添加最优状态序列输出端口 `off`（默认）| `on`

选择此参数以将 **x.seq** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_xseq` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Optimal output sequence** — 添加最优输出序列输出端口 `off`（默认）| `on`

选择此参数以将 **y.seq** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `return_ovseq` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Use custom state estimation instead of using the built-in Kalman filter** — 使用自定义状态估计输入端口 `off`（默认）| `on`

选择此参数以移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数：** `state_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 在线功能选项卡

### **Linear Time-Varying (LTV) plants** — 使用自定义状态估计输入端口 off（默认）| on

要在时变 MPC 模式下运行控制器，请选择此选项。在此模式下运行时，将三维总线信号连接到 **model** 输入端口。

有关示例，请参阅 Time-Varying MPC Control of a Time-Varying Plant。

#### 编程使用

|  |
| --- |
| **模块参数**：`isltv_plant` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Lower OV limits** — 添加最小 OV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **ymin** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ymin_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Upper OV limits** — 添加最大 OV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **ymax** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ymax_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Lower MV limits** — 添加最小 MV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **umin** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`umin_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Upper MV limits** — 添加最大 MV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **umax** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`umax_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Custom constraints** — 为混合输入/输出线性约束矩阵添加输入端口 `off`（默认）| `on`

选择此参数可将 **E**、**F**、**G** 和 **S** 输入端口添加到模块。

有关详细信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs 和 Update Mixed Input/Output Constraints at Run Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`cc_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **OV weights** — 添加 OV 调节权重输入端口 `off`（默认）| `on`

选择此参数可将 **y.wt** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ywt_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **MV weights** — 添加 MV 调节权重输入端口 `off`（默认）| `on`

选择此参数可将 **u.wt** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`uwt_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **MVRate weights** — 添加 MV 速率调节权重输入端口 `off`（默认）| `on`

选择此参数可将 **du.wt** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`duwt_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Slack variable weight** — 添加 ECR 调节权重输入端口 `off`（默认）| `on`

选择此参数可将 **ecr.wt** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`rhoeps_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Adjust prediction horizon and control horizon at run time** — 添加预测时域和控制时域输入端口 off（默认）| on

选择此参数可将 **p** 和 **m** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`pm_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Maximum prediction horizon** — 添加预测时域输入端口 `10`（默认）| 正整数

选择此参数可将 **p** 和 **m** 输入端口添加到模块。

#### 依赖关系

要启用此参数，请选择 **Adjust prediction horizon and control horizon at run time** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaximumP` |
| **类型：** string, character vector |
| **默认值：** `"10"` |

#### 其他选项卡

### **Inherit sample time** — 从父子系统继承模块采样时间 `off`（默认）| `on`

选择此参数可将父子系统的采样时间继承为模块采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

您必须按照控制器的采样率执行 Function-Call Subsystem 或 Triggered Subsystem 模块。否则，由于以下两个原因，您可能会看到意外结果。

- MV 速率向量的第一个元素（即被控变量当前值与上一次值之间的差值）通常是在假设上一次 MV 值发生在 MPC 对象中指定的采样时间的前提下进行加权和约束的，而当模块以不同的采样率执行时，此假设不再成立。
- 内置卡尔曼估计器使用 MPC 对象中指定的采样时间向 MPC 优化问题提供当前状态的估计，因此当模块以不同的采样率执行时，估计状态不再正确。

如果清除此参数（默认），则模块的采样时间继承自控制器对象。

要查看模块的采样时间，请在 Simulink 模型窗口中，在 **Debug** 选项卡上的 **Information Overlays** 下，选择 **colors** 或 **Text**。有关详细信息，请参阅 View Sample Time Information (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTimeInherited` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **Use external signal to enable or disable optimization** — 添加开关输入端口 `off`（默认）| `on`

选择此参数可将 **switch** 输入端口添加到模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `switch_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |
## 所属库

Model Predictive Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2014b 中引入**

### R2018b：MPC Simulink 模块 `mv.seq` 输出端口信号维度已更改

Adaptive MPC Controller 模块的 `mv.seq` 输出端口的信号维度已更改。以前，此信号是一个 *p*×*Nmv* 矩阵，其中 *p* 是预测时域，*Nmv* 是被控变量数量。现在，`mv.seq` 是一个 (*p*+1)×*Nmv* 矩阵，其中第 *p*+1 行重复第 *p* 行。

## 描述

仿真自适应和时变模型预测控制器

Adaptive MPC Controller 模块使用以下输入信号：

- 测量对象输出（`mo`）
- 参考或设定点（`ref`）
- 测量对象扰动（`md`），如果有

此外，所需的 `model` 输入信号指定在计算最优对象操纵变量 `mv` 时要使用的预测模型。线性预测模型可以在每个控制区间根据运行时实际对象的变化而变化。预测模型可以表示用于所有预测步的单个 LTI 对象（自适应 MPC 模式），也可以表示用于不同预测步的 LTI 对象数组（时变 MPC 模式）。修改此模型的两种常见方法如下：

- 给定非线性对象模型，在当前工作点对其进行线性化。
- 使用对象数据估计经验线性时变（LTV）模型中的参数。

默认情况下，该模块估计其预测模型状态。由于预测模型参数在运行时变化，MPC Controller 模块中使用的静态卡尔曼滤波器不适用。相反，Adaptive MPC Controller 模块使用线性时变卡尔曼滤波器（LTVKF）。有关详细信息，请参阅 Adaptive and Time-Varying MPC。

在所有其他方面，Adaptive MPC Controller 模块都模仿 MPC Controller 模块。由于自适应版本涉及额外开销，除非您需要控制一个非线性对象，且其工作条件范围很广、对象动态变化显著，否则请使用 MPC Controller 模块。

Adaptive MPC Controller 模块和 Multiple MPC Controllers 模块都能使您的控制系统在运行时适应不断变化的工作条件。下表列出了使用每个模块的优点。

| 模块 | Adaptive MPC Controller | Multiple MPC Controllers |
| --- | --- | --- |
| **自适应方法** | 随着工作条件变化，为单个控制器更新预测模型 | 在为不同工作区域设计的多个控制器之间切换 |
| **优点** | - 只需离线设计单个控制器 - 运行时计算量更少，内存占用更小 - 对对象条件中的实际变化更具鲁棒性 | - 无需在线估计对象模型 - 控制器可以具有不同的采样时间、预测时域和权重 - 预测模型可以具有不同的阶次或时间域 - 可以对有限的一组候选控制器进行全面测试 |
