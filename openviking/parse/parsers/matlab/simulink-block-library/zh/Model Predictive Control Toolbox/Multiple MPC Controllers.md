---
type: simulink-block
title: 'Multiple MPC Controllers'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'multiplempccontrollers'
documentation_source_path: 'ref/multiplempccontrollers.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiple MPC Controllers

## 端口

### 输入

#### 必需输入

### **ref** — 模型输出参考值 行向量 | 矩阵

被控对象输出参考值，指定为行向量信号或矩阵信号。

要在整个预测时域内使用相同的参考值，请将 **ref** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出变量的数量。每个元素指定一个输出变量的参考值。

要在预测时域内（预览）从时间 *k*+1 到时间 *k*+*p* 改变参考值，请将 **ref** 连接到具有 *Ny* 列和至多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步的参考值。如果指定的行数少于 *p*，则最终参考值用于预测时域的剩余步。

### **switch** — 控制器选择整数

使用 **switch** 输入端口选择活动控制器。**switch** 输入信号必须是范围从 `1` 到 *N*c 的标量整数，其中 *N*c 是指定的候选控制器数量。在每个控制时刻，此信号指定活动控制器。`switch` 值为 `1` 对应于候选控制器元胞数组中的第一个条目，值为 `2` 对应于第二个控制器，依此类推。

如果 `switch` 信号超出 1 到 *N*c 的范围，模块保留上一控制器输出。

### **mo** — 测量输出向量

测量输出信号，指定为向量信号。候选控制器使用被控对象测量输出来改进其状态估计。

所有候选控制器必须使用相同的状态估计选项，即默认或自定义。如果您的候选控制器使用默认状态估计，则必须将被控对象测量输出连接到 **mo** 输入端口。如果您的候选控制器使用自定义状态估计，则必须将被控对象估计状态信号连接到 **x[k|k]** 输入端口。

#### 依赖

要启用此端口，请清除 **使用自定义状态估计而不是使用内置 Kalman 滤波器** 参数。

### **x[k|k]** — 自定义状态估计向量

自定义状态估计，指定为向量信号。候选控制器使用连接的状态估计，而不是使用内置估计器估计状态。当替代估计技术被认为优于内置估计器时，或当状态完全可测时，请使用自定义状态估计。

所有候选控制器必须使用相同的状态估计选项，即默认或自定义。如果您的候选控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果您的候选控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

使用自定义状态估计时，所有候选控制器必须具有相同的维度。所有候选控制器必须为其各自的被控对象、扰动和测量噪声模型使用相同的状态定义（状态的数量和顺序）。

#### 依赖

要启用此端口，请选择 **使用自定义状态估计而不是使用内置 Kalman 滤波器** 参数。

#### 附加输入

### **md** — 输入 行向量 | 矩阵

如果您的控制器预测模型具有测量扰动，则必须启用此端口，并向其连接行向量或矩阵信号。

要在整个预测时域内使用相同的测量扰动值，请将 **md** 连接到具有 *Nmd* 个元素的行向量信号，其中 *Nmd* 是操纵变量的数量。每个元素指定一个测量扰动的值。

要在预测时域内（预览）从时间 *k* 到时间 *k*+*p* 改变扰动，请将 **md** 连接到具有 *Nmd* 列和至多 *p*+1 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步的扰动。如果指定的行数少于 *p*+1，则最终扰动用于预测时域的剩余步。

#### 依赖

要启用此端口，请选择 **测量扰动** 参数。

### **ext.mv** — 上一控制区间中用于被控对象的控制信号 向量

上一控制区间中用于被控对象的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。所有候选控制器在每个控制区间使用此信号更新其控制器状态估计。这有助于在切换驱动控制器时实现无扰切换。当被控对象中使用的操纵变量 (MV) 向量不同于模块计算的 MV 向量时（例如，由于信号饱和或超驰条件），使用此输入还可提高状态估计精度。

控制器状态估计假设 MV 向量是分段常量。因此，在时间 *tk*，**ext.mv** 值必须是时间 *tk–1* 与 *tk* 之间的有效 MV 向量。例如，如果 MV 在此区间内实际变化，您可以提供在时间 *tk* 求值的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间中实际施加到被控对象的 MV 信号。通常，这些 MV 信号是由驱动控制器模块生成的值，但并非总是如此。如果控制器模块未驱动被控对象，则将实际控制信号馈送到 **ext.mv** 也有助于在控制器重新切换到在线时实现无扰切换。
- 当控制器正在驱动被控对象时使用此选项，可能会在 Simulink® 模型中引起代数环，因为从 **ext.mv** 输入到 **mv** 输出端口存在直接馈通。要防止此类代数环，请插入 Memory 模块或 Unit Delay 模块。

有关使用外部操纵变量输入端口实现无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖

要启用此端口，请选择 **外部操纵变量** 参数。

#### 在线约束

### **ymin** — 最小输出变量约束 向量 | 矩阵

要指定运行时最小输出变量约束，请启用此输入端口。如果此端口禁用，模块使用其 `mpc` 控制器对象的 `OutputVariables.Min` 属性中指定的下界。如果某个输出变量在控制器对象中未指定下界，则在运行时模块忽略对应的连接信号。

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 改变边界，请将 **ymin** 连接到具有 *Ny* 列和至多 *p* 行的矩阵信号。这里，*Ny* 是被控对象输出的数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步的边界。如果指定的行数少于 *p*，则最后一行中的边界应用于预测时域的剩余部分。如果只有一个输出变量，并且连接了条目数不超过 *p* 的向量信号，则这些条目用于整个预测时域。

**ymin** 信号的第 `i` 列对应于第 `i` 个被控对象输出，并在运行时替换 `mpc` 对象的 `OutputVariables(i).Max` 属性。替换行为取决于这两个变量的维度。

**`mpc` 对象中的标量 `OutputVariables(i).Min`（要应用于所有预测步的第 `i` 个被控对象输出的常量边界）**

| **ymin** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymin**（单输出，常量边界） | **ymin** 替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 列向量 **ymin**（单输出，时变边界） | **ymin** 用时变边界替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 行向量 **ymin**（多输出，常量边界） | **ymin** 的第 `i` 个元素替换 `OutputVariables(i).Min` 中定义的常量边界。 |
| 矩阵 **ymin**（多输出，时变边界） | **ymin** 的第 `i` 列用时变边界替换 `OutputVariables(i).Min` 中定义的常量边界。 |

**`mpc` 对象中的向量 `OutputVariables(i).Min`（第 `i` 个被控对象输出的时变边界，在不同预测步具有不同值）**

| **ymin** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymin**（单输出，常量边界） | **ymin** 替换 `OutputVariables.Min` 中的第一个有限条目，并且 `OutputVariables.Min` 中的其余条目以相同的位移量上移或下移，以保留原始 `OutputVariables.Min` 向量定义的剖面。 |
| 列向量 **ymin**（单输出，时变边界） | **ymin** 替换 `OutputVariables(i).Min` 中定义的时变边界，并且原始边界剖面被丢弃。 |
| 行向量 **ymin**（多输出，常量边界） | **ymin** 的第 `i` 个元素替换 `OutputVariables(i).Min` 中的第一个有限条目，并且 `OutputVariables(i).Min` 中的其余条目以相同的位移量上移或下移，以保留原始 `OutputVariables(i).Min` 向量定义的剖面。 |
| 矩阵 **ymin**（多输出，时变边界）。 | **ymin** 的第 `i` 列替换 `OutputVariables(i).Min` 中定义的时变边界，并且原始边界剖面被丢弃。 |

#### 依赖

要启用此端口，请选择 **OV 下限** 参数。

### **ymax** — 最大输出变量约束 向量 | 矩阵

要指定运行时最大输出变量约束，请启用此输入端口。如果此端口禁用，模块使用其 `mpc` 控制器对象的 `OutputVariables.Max` 属性中指定的上界。如果某个输出变量在控制器对象中未指定上界，则在运行时模块忽略对应的连接信号。

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 改变边界，请将 **ymax** 连接到具有 *Ny* 列和至多 *p* 行的矩阵信号。这里，*Ny* 是被控对象输出的数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步的边界。如果指定的行数少于 *p*，则最后一行中的边界应用于预测时域的剩余部分。如果只有一个输出变量，并且连接了条目数不超过 *p* 的向量信号，则这些条目用于整个预测时域。

**ymax** 信号的第 `i` 列对应于第 `i` 个被控对象输出，并在运行时替换 `mpc` 对象的 `OutputVariables(i).Max` 属性。替换行为取决于这两个变量的维度。

**`mpc` 对象中的标量 `OutputVariables(i).Max`（要应用于所有预测步的第 `i` 个被控对象输出的常量边界）**

| **ymax** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymax**（单输出，常量边界） | **ymax** 替换 `OutputVariables(i).Max` 中定义的常量边界。 |
| 列向量 **ymax**（单输出，时变边界） | **ymax** 用时变边界替换 `OutputVariables(i).Max` 中定义的常量边界。 |
| 行向量 **ymax**（多输出，常量边界） | **ymax** 的第 `i` 个元素替换 `OutputVariables(i).Max` 中定义的常量边界。 |
| 矩阵 **ymax**（多输出，时变边界） | **ymax** 的第 `i` 列用时变边界替换 `OutputVariables(i).Max` 中定义的常量边界。 |

**`mpc` 对象中的向量 `OutputVariables(i).Max`（第 `i` 个被控对象输出的时变边界，在不同预测步具有不同值）**

| **ymax** 维度 | 替换行为 |
| --- | --- |
| 标量 **ymax**（单输出，常量边界） | **ymax** 替换 `OutputVariables.Max` 中的第一个有限条目，并且 `OutputVariables.Max` 中的其余条目以相同的位移量上移或下移，以保留原始 `OutputVariables.Max` 向量定义的剖面。 |
| 列向量 **ymax**（单输出，时变边界） | **ymax** 替换 `OutputVariables(i).Max` 中定义的时变边界，并且原始边界剖面被丢弃。 |
| 行向量 **ymax**（多输出，常量边界） | **ymax** 的第 `i` 个元素替换 `OutputVariables(i).Max` 中的第一个有限条目，并且 `OutputVariables(i).Max` 中的其余条目以相同的位移量上移或下移，以保留原始 `OutputVariables(i).Max` 向量定义的剖面。 |
| 矩阵 **ymax**（多输出，时变边界）。 | **ymax** 的第 `i` 列替换 `OutputVariables(i).Max` 中定义的时变边界，并且原始边界剖面被丢弃。 |

#### 依赖

要启用此端口，请选择 **OV 上限** 参数。

### **umin** — 最小操纵变量约束向量 | 矩阵

要指定运行时最小操纵变量约束，请启用此输入端口。
如果禁用此端口，模块将使用其 `mpc` 控制器对象的 `ManipulatedVariables.Min` 属性中指定的下界。如果控制器对象中未为某个操纵变量指定下界，则在运行时模块将忽略对应的已连接信号。

若要在预测时域内更改从时刻 *k* 到时刻 *k*+*p*-1 的边界，请将 **umin** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。其中，*Nmv* 是操纵变量的数量，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。如果只有一个操纵变量，并且连接了条目数不超过 *p* 的向量信号，则这些条目将用于整个预测时域。

**umin** 信号的第 `i` 列对应于第 `i` 个操纵变量，并在运行时替换 `mpc` 对象的 `ManipulatedVariables(i).Max` 属性。替换行为取决于这两个变量的维度。

**`mpc` 对象中的标量 `ManipulatedVariables(i).Min`（要应用于所有预测步的第 `i` 个操纵变量的常数边界）**

| **umin** 维度 | 替换行为 |
| --- | --- |
| 标量 **umin**（单个输出，常数边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的常数边界。 |
| 列向量 **umin**（单个输出，时变边界） | **umin** 将 `ManipulatedVariables(i).Min` 中定义的常数边界替换为时变边界。 |
| 行向量 **umin**（多个输出，常数边界） | **umin** 的第 `i` 个元素替换 `ManipulatedVariables(i).Min` 中定义的常数边界。 |
| 矩阵 **umin**（多个输出，时变边界） | **umin** 的第 `i` 列将 `ManipulatedVariables(i).Min` 中定义的常数边界替换为时变边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Min`（第 `i` 个操纵变量的时变边界，在不同预测步具有不同值）**

| **umin** 维度 | 替换行为 |
| --- | --- |
| 标量 **umin**（单个输出，常数边界） | **umin** 替换 `ManipulatedVariables.Min` 中第一个有限项，并且 `ManipulatedVariables.Min` 中其余项以相同位移量向上或向下移动，以保持由原始 `ManipulatedVariables.Min` 向量定义的曲线。 |
| 列向量 **umin**（单个输出，时变边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并丢弃原始边界曲线。 |
| 行向量 **umin**（多个输出，常数边界） | **umin** 的第 `i` 个分量替换 `ManipulatedVariables(i).Min` 中第一个有限项，并且 `ManipulatedVariables(i).Min` 中其余项以相同位移量向上或向下移动，以保持由原始 `ManipulatedVariables(i).Min` 向量定义的曲线。 |
| 矩阵 **umin**（多个输出，时变边界）。 | **umin** 的第 `i` 列替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并丢弃原始边界曲线。 |

#### 依赖关系

要启用此端口，请选择 **Lower MV limits** 参数。

### **umax** — 最大操纵变量约束向量 | 矩阵

要指定运行时最大操纵变量约束，请启用此输入端口。
如果禁用此端口，模块将使用其 `mpc` 控制器对象的 `ManipulatedVariables.Max` 属性中指定的上界。如果控制器对象中未为某个操纵变量指定上界，则在运行时模块将忽略对应的已连接信号。

若要在预测时域内更改从时刻 *k* 到时刻 *k*+*p*-1 的边界，请将 **umax** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。其中，*Nmv* 是操纵变量的数量，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。如果只有一个操纵变量，并且连接了条目数不超过 *p* 的向量信号，则这些条目将用于整个预测时域。

**umax** 信号的第 `i` 列对应于第 `i` 个操纵变量，并在运行时替换 `mpc` 对象的 `ManipulatedVariables(i).Max` 属性。替换行为取决于这两个变量的维度。

**`mpc` 对象中的标量 `ManipulatedVariables(i).Max`（要应用于所有预测步的第 `i` 个操纵变量的常数边界）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单个输出，常数边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的常数边界。 |
| 列向量 **umax**（单个输出，时变边界） | **umax** 将 `ManipulatedVariables(i).Max` 中定义的常数边界替换为时变边界。 |
| 行向量 **umax**（多个输出，常数边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中定义的常数边界。 |
| 矩阵 **umax**（多个输出，时变边界） | **umax** 的第 `i` 列将 `ManipulatedVariables(i).Max` 中定义的常数边界替换为时变边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Max`（第 `i` 个操纵变量的时变边界，在不同预测步具有不同值）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单个输出，常数边界） | **umax** 替换 `ManipulatedVariables.Max` 中第一个有限项，并且 `ManipulatedVariables.Max` 中其余项以相同位移量向上或向下移动，以保持由原始 `ManipulatedVariables.Max` 向量定义的曲线。 |
| 列向量 **umax**（单个输出，时变边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并丢弃原始边界曲线。 |
| 行向量 **umax**（多个输出，常数边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中第一个有限项，并且 `ManipulatedVariables(i).Max` 中其余项以相同位移量向上或向下移动，以保持由原始 `ManipulatedVariables(i).Max` 向量定义的曲线。 |
| 矩阵 **umax**（多个输出，时变边界）。 | **umax** 的第 `i` 列替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并丢弃原始边界曲线。 |

#### 依赖关系

要启用此端口，请选择 **Upper MV limits** 参数。

#### 在线整定权重

### **y.wt** — 输出变量整定权重 行向量 | 矩阵

要指定运行时输出变量整定权重，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `Weights.OutputVariables` 属性中指定的整定权重。这些整定权重惩罚与输出参考值的偏差。

如果 MPC 控制器对象在预测时域内使用常数输出整定权重，则只能在运行时指定常数输出整定权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的输出整定权重，则只能在运行时指定时变输出整定权重。

要在预测时域内使用常数整定权重，请将 **y.wt** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出数量。每个元素为输出变量指定非负整定权重。有关指定整定权重的更多信息，请参阅 Tune Weights。

若要在预测时域内使整定权重从时刻 *k*+1 到时刻 *k*+*p* 变化，请将 **y.wt** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步的整定权重。如果指定的行数少于 *p*，则最后一行的整定权重适用于预测时域的剩余部分。有关在预测时域内使权重变化的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **OV weights** 参数。

### **u.wt** — 操纵变量整定权重 行向量 | 矩阵

要指定运行时操纵变量整定权重，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `Weights.ManipulatedVariables` 属性中指定的整定权重。这些整定权重惩罚与 MV 目标值的偏差。

如果 MPC 控制器对象在预测时域内使用常数操纵变量整定权重，则只能在运行时指定常数操纵变量整定权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的操纵变量整定权重，则只能在运行时指定时变操纵变量整定权重。

要在预测时域内使用相同的整定权重，请将 **u.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是操纵变量的数量。每个元素为操纵变量指定非负整定权重。有关指定整定权重的更多信息，请参阅 Tune Weights。

若要在预测时域内使整定权重从时刻 *k* 到时刻 *k*+*p*-1 变化，请将 **u.wt** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。其中，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步的整定权重。如果指定的行数少于 *p*，则最后一行的整定权重适用于预测时域的剩余部分。有关在预测时域内使权重变化的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MV weights** 参数。

### **du.wt** — 操纵变量速率整定权重 行向量 | 矩阵

要指定运行时操纵变量速率整定权重，请启用此输入端口。如果禁用此端口，模块将使用其控制器对象的 `Weights.ManipulatedVariablesRate` 属性中指定的整定权重。这些整定权重惩罚控制作用中的大变化。

如果 MPC 控制器对象在预测时域内使用常数操纵变量速率整定权重，则只能在运行时指定常数操纵变量速率权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的操纵变量速率整定权重，则只能在运行时指定时变操纵变量速率整定权重。

要在预测时域内使用相同的整定权重，请将 **du.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是操纵变量的数量。每个元素为操纵变量速率指定非负整定权重。有关指定整定权重的更多信息，请参阅 Tune Weights。

若要在预测时域内使整定权重从时刻 *k* 到时刻 *k*+*p*-1 变化，请将 **du.wt** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。其中，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步的整定权重。如果指定的行数少于 *p*，则最后一行的整定权重适用于预测时域的剩余部分。有关在预测时域内使权重变化的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MVRate weights** 参数。

### **ecr.wt** — 松弛变量整定权重 标量

要指定运行时松弛变量整定权重，请启用此输入端口并连接一个标量信号。如果禁用此端口，模块将使用其控制器对象的 `Weights.ECR` 属性中指定的整定权重。

除非控制器对象定义了关联 ECR 值为非零的软约束，否则松弛变量整定权重无效。如果存在软约束，增大 **ecr.wt** 值会使这些约束相对更难满足。控制器随后会更高优先级地最小化预测最坏情况约束违反的幅度。

#### 依赖关系

要启用此端口，请选择 **ECR weight** 参数。

### 输出

#### 必需输出

### **mv** — 最优操纵变量控制作用 列向量

最优操纵变量控制作用，输出为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是操纵变量的数量。Multiple MPC Controllers 模块将活动控制器的输出传递到 **mv** 输出端口。

如果活动控制器的求解器收敛到局部最优解（**qp.status** 为正），则 **mv** 包含最优解。

如果求解器失败（**qp.status** 为负），则 **mv** 保持在其最近一次成功解；即控制器输出冻结。

如果求解器达到最大迭代次数仍未找到最优解（**qp.status** 为零），并且活动控制器的 `Optimization.UseSuboptimalSolution` 属性为：

- `true`，则 **mv** 包含次优解
- `false`，则 **mv** 然后 **mv** 保持在其最近一次成功解

#### 附加输出

### **cost** — 目标函数成本 非负标量

目标函数成本，输出为非负标量信号。成本量化控制器实现其目标的程度。成本值使用缩放后的 MPC 成本函数计算，其中每一项都是无偏移且无量纲的。

仅当 **qp.status** 输出为非负时，成本值才有意义。

#### 依赖关系

要启用此端口，请选择 **Optimal cost** 参数。

### **qp.status** — 优化状态整数

活动控制器的优化状态，输出为整数信号。

如果活动控制器针对给定控制区间求解 QP 问题，则 **qp.status** 输出返回计算中使用的 QP 求解器迭代次数。此值是有限正整数，并与计算所需时间成正比。因此，较大值意味着该时间区间内模块执行相对较慢。

QP 求解器可能由于以下原因无法找到最优解：

- **qp.status** = `0` — QP 求解器无法在 `mpc` 对象中指定的最大迭代次数内找到解。在这种情况下，如果活动控制器的 `Optimizer.UseSuboptimalSolution` 属性为 `false`，模块将其 **mv** 输出保持在最近一次成功解。否则，它使用最后一次求解器迭代中找到的次优解。
- **qp.status** = `-1` — QP 求解器检测到不可行的 QP 问题。有关大幅、持续扰动驱动输出变量超出其指定边界的示例，请参见 Monitoring Optimization Status to Detect Controller Failures。在这种情况下，模块将其 **mv** 输出保持在最近一次成功解。
- **qp.status** = `-2` — QP 求解器在求解严重病态的 QP 问题时遇到数值困难。在这种情况下，模块将其 **mv** 输出保持在最近一次成功解。

在实时应用中，您可以使用 **qp.status** 设置报警或采取其他特殊操作。

#### 依赖项

要启用此端口，请选择 **Optimization status** 参数。

### **est.state** — 估计的控制器状态向量

活动控制器的估计控制器状态，输出为向量信号。估计状态包括被控对象、扰动和噪声模型状态。

#### 依赖项

要启用此端口，请选择 **Estimated controller states** 参数。

#### 最优序列

### **mv.seq** — 最优操纵变量序列矩阵

最优操纵变量序列，返回为具有 *p*+1 行和 *Nmv* 列的矩阵信号，其中 *p* 是预测时域，*Nmv* 是操纵变量数量。

**mv.seq** 的前 *p* 行包含从当前时间 *k* 到时间 *k*+*p*-1 计算出的最优操纵变量值。**mv.seq** 的第一行包含当前操纵变量值（输出 **mv**）。由于控制器在时间 *k*+*p* 不计算最优控制动作，因此 **mv.seq** 的最后两行相同。

#### 依赖项

要启用此端口，请选择 **Optimal control sequence** 参数。

### **x.seq** — 最优预测模型状态序列矩阵

最优预测模型状态序列，返回为具有 *p*+1 行和 *Nx* 列的矩阵信号，其中 *p* 是预测时域，*Nx* 是状态数量。

**x.seq** 的第一行包含当前估计状态值，这些值来自内置状态估计器或自定义状态估计模块输入 **x[k|k]**。**x.seq** 的接下来 *p* 行包含从时间 *k*+1 到时间 *k*+*p* 计算出的最优状态值。

#### 依赖项

要启用此端口，请选择 **Optimal state sequence** 参数。

### **y.seq** — 最优输出变量序列矩阵

最优输出变量序列，返回为具有 *p*+1 行和 *Ny* 列的矩阵信号，其中 *p* 是预测时域，*Ny* 是输出变量数量。

**y.seq** 的前 *p* 行包含从当前时间 *k* 到时间 *k*+*p*-1 计算出的最优输出值。**y.seq** 的第一行基于当前估计状态和当前测量扰动（输入 **md** 的第一行）计算。由于控制器在时间 *k*+*p* 不计算最优输出值，因此 **y.seq** 的最后两行相同。

#### 依赖项

要启用此端口，请选择 **Optimal output sequence** 参数。

## 参数

### **MPC 控制器元胞数组** — 候选控制器 cell array of `mpc` objects | cell array of strings | cell array of character vectors

候选控制器，指定为以下之一：

- `mpc` 对象的 cell array。
- cell array of strings 或 cell array of character vectors，其中每个元素是 MATLAB® 工作区中 `mpc` 对象的名称。

指定的数组必须至少包含两个候选控制器。cell array 中的第一个条目是对应开关输入值 1 的控制器，第二个对应开关输入值 2，依此类推。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mpcobjs` |
| **类型：** string, character vector, cell array of strings, cell array of character vectors |
| **默认值：** `""` |

### **初始控制器状态元胞数组** — 初始状态 cell array of `mpcstate` objects | cell array of strings | cell array of character vectors

候选控制器的初始状态，指定为以下之一：

- `mpcstate` 对象的 cell array。
- cell array of strings 或 cell array of character vectors，其中每个元素是 MATLAB 工作区中 `mpcstate` 对象的名称。
- `{[],[],...}`、`{'[]','[]',...}` 或 `{"[]","[]",...}` — 使用每个候选控制器的 `Model.Nominal` 属性中定义的名义条件作为其初始状态。

使用此参数使控制器状态在仿真开始时尽可能反映真实被控对象环境。此初始状态可以不同于 `mpc` 对象中定义的名义状态。

如果启用了自定义状态估计，模块将忽略 **初始控制器状态元胞数组** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `x0s` |
| **类型：** string, character vector, cell array of strings, cell array of character vectors |
| **默认值：** `""` |

#### 常规选项卡

### **测量扰动** — 添加测量扰动输入端口 `on`（默认）| `off`

如果控制器具有测量扰动，必须选择此参数以将 **md** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `md_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"on"` |

### **外部操纵变量** — 添加外部操纵变量输入端口 `off`（默认）| `on`

选择此参数以将 **ext.mv** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mv_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **操纵变量目标** — 添加操纵变量目标输入端口 off（默认）| on

选择此参数以将 **mv.target** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uref_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优代价** — 添加最优代价输出端口 off（默认）| on

选择此参数以将 **cost** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_cost_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **优化状态** — 添加优化状态输出端口 off（默认）| on

选择此参数以将 **qp.status** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_qpstatus_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **估计的控制器状态** — 添加估计状态输出端口 `off`（默认）| `on`

选择此参数以将 **est.state** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_state_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优控制序列** — 添加最优控制序列输出端口 off（默认）| on

选择此参数以将 **mv.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_mvseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优状态序列** — 添加最优状态序列输出端口 off（默认）| on

选择此参数以将 **x.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_xseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优输出序列** — 添加最优输出序列输出端口 off（默认）| on

选择此参数以将 **y.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_ovseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用自定义状态估计而不是使用内置 Kalman 滤波器** — 使用自定义状态估计输入端口 `off`（默认）| `on`

选择此参数以移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `state_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 在线功能选项卡

### **OV 下限** — 添加最小 OV 约束输入端口 off（默认）| on

选择此参数以将 **ymin** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymin_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 上限** — 添加最大 OV 约束输入端口 off（默认）| on

选择此参数以将 **ymax** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymax_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 下限** — 添加最小 MV 约束输入端口 off（默认）| on

选择此参数以将 **umin** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umin_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 上限** — 添加最大 MV 约束输入端口 off（默认）| on

选择此参数以将 **umax** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umax_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **自定义约束** — 添加自定义约束输入端口 off（默认）| on

选择此参数以将 **E**、**F**、**G** 和 **S** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cc_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 权重** — 添加 OV 整定权重输入端口 off（默认）| on

选择此参数以将 **y.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ywt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 权重** — 添加 MV 整定权重输入端口 off（默认）| on

选择此参数以将 **u.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uwt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MVRate 权重** — 添加 MV rate 整定权重输入端口 off（默认）| on

选择此参数以将 **du.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `duwt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **松弛变量权重** — 添加 ECR 整定权重输入端口 off（默认）| on

选择此参数以将 **ecr.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rhoeps_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 其他选项卡

### **模块数据类型** — 指定操纵变量的数据类型 `double`（默认）| `single` | `data type expression`

将操纵变量的模块数据类型指定为以下之一：

- `double` — 双精度浮点
- `single` — 单精度浮点

  如果要在单精度目标上实现该模块，请将输出数据类型指定为 `single`。
- `data type expression` — 计算结果为 `double` 或 `single` 的表达式。有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType_multiple` |
| **类型：** string, character vector |
| **值：** `"double"`, `"single"`, `data type expression` |
| **默认值：** `"double"` |

### **继承采样时间** — 从父子系统继承模块采样时间 `off`（默认）| `on`

选择此参数以将父子系统的采样时间继承为模块采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

必须在控制器的采样率下执行 Function-Call Subsystem 或 Triggered Subsystem 模块。否则，可能会因为以下两个原因看到意外结果。

- MV rate 向量的第一个元素（即操纵变量的当前值与上一个值之差）通常会在假设上一个 MV 值是在 MPC 对象中指定的采样时间于过去发生的情况下进行加权和约束，而当模块以不同的采样率执行时，此假设不再成立。
- 内置 Kalman 估计器使用 MPC 对象中指定的采样时间向 MPC 优化问题提供当前状态的估计，因此当模块以不同的采样时间执行时，估计状态不再正确。

如果清除此参数（默认），模块的采样时间将从控制器对象继承。

要查看模块的采样时间，在 Simulink 模型窗口中，在 **Debug** 选项卡上的 **Information Overlays** 下，选择 **colors** 或 **Text**。有关详细信息，请参阅 View Sample Time Information (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTimeInherited_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

## 所属库

Model Predictive Control Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2008b 中引入**

### R2018b：MPC Simulink 模块 `mv.seq` 输出端口信号维度已更改

Multiple MPC Controllers 模块的 `mv.seq` 输出端口的信号维度已更改。以前，此信号是 *p*-by-*Nmv* 矩阵，其中 *p* 是预测时域，*Nmv* 是操纵变量数量。现在，`mv.seq` 是 (*p*+1)-by-*Nmv* 矩阵，其中第 *p*+1 行重复第 *p* 行。

## 描述

模拟在多个隐式 MPC 控制器之间切换

在每个控制时刻，Multiple MPC Controllers 模块接收当前测得的被控对象输出、参考值以及测得的被控对象扰动（如果有）。此外，它还接收一个切换信号，该信号从针对工作范围内不同工作点设计的一组候选 MPC 控制器中选择*活动控制器*。然后，活动控制器求解二次规划，以针对当前输入信号确定最优的被控对象操纵变量。

当工作条件变化时，Multiple MPC Controllers 模块使你能够实现更好的控制。利用可用的测量值，你可以在运行时检测当前工作区域，并通过 `switch` 输入端口选择合适的活动控制器。针对不同工作区域切换控制器，是使用线性控制技术解决非线性控制问题的一种常用方法。

为提高效率，非活动控制器不计算最优控制动作。但是，为在控制器之间提供无扰切换，非活动控制器继续执行状态估计。

Multiple MPC Controllers 模块缺少 MPC Controller 模块中的若干可选功能，如下所示：

- 不能禁用优化。必须始终有一个控制器处于活动状态。
- 不能在模块对话框内启动控制器设计；也就是说，没有 **Design** 按钮。在配置 Multiple MPC Controllers 模块之前，请设计所有候选控制器。
- 类似地，没有 **Review** 按钮。请改用 `review` 命令或 MPC Designer app。
- 不能在运行时更新对输入和输出的线性组合的自定义约束。

Multiple MPC Controllers 模块和 Adaptive MPC Controller 模块都使你的控制系统能够在运行时适应变化的工作条件。下表列出了使用每种模块的优势。

| 模块 | Adaptive MPC Controller | Multiple MPC Controllers |
| --- | --- | --- |
| **自适应方法** | 当工作条件变化时，更新单个控制器的预测模型 | 在不同操作区域设计的多个控制器之间切换 |
| **优势** | - 只需离线设计一个控制器 - 运行时计算量更少，内存占用更小 - 对实际被控对象条件变化更具鲁棒性 | - 无需在线估计被控对象模型 - 控制器可以具有不同的采样时间、时域和权重 - 预测模型可以具有不同的阶次或时间域 - 可以对有限的一组候选控制器进行全面测试 |
