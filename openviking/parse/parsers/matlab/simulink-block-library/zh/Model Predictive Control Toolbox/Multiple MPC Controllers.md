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
```yaml
ports:
- name: ref
  summary: 模型输出参考值 行向量 | 矩阵
  direction: input
- name: switch
  summary: 控制器选择 整数
  direction: input
- name: mo
  summary: 测量输出 向量
  direction: input
- name: x[k|k]
  summary: 自定义状态估计 向量
  direction: input
- name: md
  summary: 输入行向量 | 矩阵
  direction: input
- name: ext.mv
  summary: 上一控制区间内用于被控对象的控制信号 向量
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
- name: y.wt
  summary: 输出变量调优权重 行向量 | 矩阵
  direction: input
- name: u.wt
  summary: 操纵变量调优权重 行向量 | 矩阵
  direction: input
- name: du.wt
  summary: 被操纵变量速率调节权重行向量 | 矩阵
  direction: input
- name: ecr.wt
  summary: 松弛变量调节权重标量
  direction: input
- name: mv
  summary: 最优被操纵变量控制作用列向量
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

### **ref** — 模型输出参考值 行向量 | 矩阵

被控对象输出参考值，指定为行向量信号或矩阵信号。

若要在预测时域内使用相同的参考值，请将 **ref** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出变量的数量。每个元素指定一个输出变量的参考值。

若要在预测时域内改变参考值（预览），从时刻 *k*+1 到时刻 *k*+*p*，请将 **ref** 连接到具有 *Ny* 列、最多 *p* 行的矩阵信号。此处，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的参考值。如果指定的行数少于 *p*，则最终参考值将用于预测时域的剩余步长。

### **switch** — 控制器选择 整数

使用 **switch** 输入端口选择活动控制器。**switch** 输入信号必须是从 `1` 到 *N*c 的标量整数，其中 *N*c 是指定的候选控制器数量。在每个控制时刻，此信号指定活动控制器。switch 值为 `1` 对应候选控制器元胞数组中的第一个条目，值为 `2` 对应第二个控制器，依此类推。

如果 `switch` 信号超出 1 到 *N*c 的范围，模块将保持先前的控制器输出。

### **mo** — 测量输出 向量

测量输出信号，指定为向量信号。候选控制器使用被控对象测量输出来改善其状态估计。

所有候选控制器必须使用相同的状态估计选项，即默认或自定义。如果候选控制器使用默认状态估计，则必须将被控对象测量输出连接到 **mo** 输入端口。如果候选控制器使用自定义状态估计，则必须将估计的被控对象状态信号连接到 **x[k|k]** 输入端口。

#### 依赖关系

要启用此端口，请清除 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **x[k|k]** — 自定义状态估计 向量

自定义状态估计，指定为向量信号。候选控制器使用连接的状态估计，而不是使用内置估计器估计状态。当替代估计技术被认为优于内置估计器时，或当状态完全可测量时，请使用自定义状态估计。

所有候选控制器必须使用相同的状态估计选项，即默认或自定义。如果候选控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果候选控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

使用自定义状态估计时，所有候选控制器必须具有相同的维度。所有候选控制器必须为其各自的被控对象、扰动和测量噪声模型使用相同的状态定义（状态的数量和顺序）。

#### 依赖关系

要启用此端口，请选择 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

#### 附加输入

### **md** — 输入行向量 | 矩阵

如果您的控制器预测模型具有可测扰动，则必须启用此端口，并将行向量或矩阵信号连接到该端口。

若要在整个预测时域内使用相同的可测扰动值，请将 **md** 连接到具有 *Nmd* 个元素的行向量信号，其中 *Nmd* 是操纵变量数。每个元素指定一个可测扰动的值。

若要使扰动在从时刻 *k* 到时刻 *k*+*p* 的预测时域内变化（预览），请将 **md** 连接到具有 *Nmd* 列且最多 *p*+1 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的扰动。如果指定的行数少于 *p*+1，则最终扰动将用于预测时域的剩余步长。

#### 依赖关系

要启用此端口，请选择 **Measured disturbances** 参数。

### **ext.mv** — 上一控制区间内用于被控对象的控制信号 向量

上一控制区间内用于被控对象的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量数。所有候选控制器在每个控制区间使用此信号更新其控制器状态估计。这有助于在切换驱动控制器时最小化无扰切换。当被控对象中使用的操纵变量 (MV) 向量与模块计算出的 MV 向量不同时（例如，由于信号饱和或超驰条件），使用此输入还可提高状态估计精度。

控制器状态估计假设 MV 向量是分段常数。因此，在时刻 *tk*，**ext.mv** 值必须是时刻 *tk–1* 与 *tk* 之间的有效 MV 向量。例如，如果 MV 在此区间内实际变化，您可以提供在时刻 *tk* 计算的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间内实际施加到被控对象的 MV 信号。通常，这些 MV 信号是驱动控制器模块生成的值，但并非总是如此。如果控制器模块未驱动被控对象，则将实际控制信号馈送到 **ext.mv** 也有助于在控制器重新上线时实现无扰切换。
- 当控制器正在驱动被控对象时使用此选项，可能会在 Simulink® 模型中导致代数环，因为从 **ext.mv** 输入到 **mv** 输出端口存在直接馈通。为防止此类代数环，请插入 Memory 模块或 Unit Delay 模块。

有关使用外部操纵变量输入端口实现无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **External manipulated variable** 参数。

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

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 更改边界，请将 **ymax** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*Ny* 是对象输出数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界将应用于预测时域的剩余部分。如果只有一个输出变量，并且连接了一个条目数不超过 *p* 的向量信号，则这些条目将用于整个预测时域。

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
| 标量 **ymax**（单个输出，常数边界） | **ymax** 替换 `OutputVariables.Max` 中的第一个有限条目，并且 `OutputVariables.Max` 中的其余条目以相同的位移量向上或向下移动，以保留原始 `OutputVariables.Max` 向量定义的轮廓。 |
| 列向量 **ymax**（单个输出，时变边界） | **ymax** 替换 `OutputVariables(i).Max` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **ymax**（多个输出，常数边界） | **ymax** 的第 `i` 个元素替换 `OutputVariables(i).Max` 中的第一个有限条目，并且 `OutputVariables(i).Max` 中的其余条目以相同的位移量向上或向下移动，以保留原始 `OutputVariables(i).Max` 向量定义的轮廓。 |
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
*p* 行的矩阵信号。这里，*Nmv* 是
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
| 列向量 **umin**（单输出，时变边界） | **umin** 用时变边界替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |
| 行向量 **umin**（多输出，常量边界） | **umin** 的第 `i` 个元素替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |
| 矩阵 **umin**（多输出，时变边界） | **umin** 的第 `i` 列用时变边界替换 `ManipulatedVariables(i).Min` 中定义的常量边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Min`（第 `i` 个被操纵变量的时变边界，
在不同预测步长具有不同值）**

| **umin** 维度 | 替换行为 |
| --- | --- |
| 标量 **umin**（单输出，常量边界） | **umin** 替换 `ManipulatedVariables.Min` 中的第一个有限元素，并且 `ManipulatedVariables.Min` 中的其余元素以相同的位移量向上或向下移动，以保留由原始 `ManipulatedVariables.Min` 向量定义的轮廓。 |
| 列向量 **umin**（单输出，时变边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **umin**（多输出，常量边界） | **umin** 的第 `i` 个分量替换 `ManipulatedVariables(i).Min` 中的第一个有限元素，并且 `ManipulatedVariables(i).Min` 中的其余元素以相同的位移量向上或向下移动，以保留由原始 `ManipulatedVariables(i).Min` 向量定义的轮廓。 |
| 矩阵 **umin**（多输出，时变边界）。 | **umin** 的第 `i` 列替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |

#### 依赖关系

要启用此端口，请选择 **Lower MV limits**
参数。

### **umax** — 被操纵变量最大约束向量 | 矩阵

要指定运行时被操纵变量最大约束，请启用此输入端口。
如果此端口被禁用，模块将使用其 `mpc` 控制器对象的
`ManipulatedVariables.Max` 属性中指定的上界。如果某个被操纵变量在控制器对象中
未指定上界，则运行时模块会忽略对应的
已连接信号。

要在预测时域内从时间 *k* 到
时间 *k*+*p*-1 更改边界，请将 **umax** 连接到
一个矩阵信号，该信号具有 *Nmv* 列，并且最多
*p* 行。这里，*Nmv* 是
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

#### 在线整定权重

### **y.wt** — 输出变量调优权重 行向量 | 矩阵

要指定运行时输出变量调优权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.OutputVariables` 属性中指定的调优权重。这些调优权重惩罚输出参考值的偏差。

如果 MPC 控制器对象在预测时域上使用恒定输出调优权重，则您只能在运行时指定恒定输出调优权重。类似地，如果 MPC 控制器对象使用随预测时域变化的输出调优权重，则您只能在运行时指定时变输出调优权重。

要在预测时域上使用恒定调优权重，请将 **y.wt** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出数量。每个元素为输出变量指定一个非负调优权重。有关指定调优权重的更多信息，请参阅 Tune Weights。

要使调优权重在预测时域上从时间 *k*+1 到时间 *k*+*p* 变化，请将 **y.wt** 连接到具有 *Ny* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调优权重。如果指定的行数少于 *p*，则最后一行的调优权重适用于预测时域的剩余部分。有关在预测时域上变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **OV weights** 参数。

### **u.wt** — 操纵变量调优权重 行向量 | 矩阵

要指定运行时操纵变量调优权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariables` 属性中指定的调优权重。这些调优权重惩罚 MV 目标值的偏差。

如果 MPC 控制器对象在预测时域上使用恒定操纵变量调优权重，则您只能在运行时指定恒定操纵变量调优权重。类似地，如果 MPC 控制器对象使用随预测时域变化的操纵变量调优权重，则您只能在运行时指定时变操纵变量调优权重。

要在预测时域上使用相同的调优权重，请将 **u.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是操纵变量数量。每个元素为操纵变量指定一个非负调优权重。有关指定调优权重的更多信息，请参阅 Tune Weights。

要使调优权重在预测时域上从时间 *k* 到时间 *k*+*p*-1 变化，请将 **u.wt** 连接到具有 *Nmv* 列和最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调优权重。如果指定的行数少于 *p*，则最后一行的调优权重适用于预测时域的剩余部分。有关在预测时域上变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MV weights** 参数。

### **du.wt** — 被操纵变量速率调节权重行向量 | 矩阵

要指定运行时被操纵变量速率调节权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariablesRate` 属性中指定的调节权重。这些调节权重会惩罚控制量的大幅变化。

如果 MPC 控制器对象在预测时域上使用恒定的被操纵变量速率调节权重，则您在运行时只能指定恒定的被操纵变量速率调节权重。类似地，如果 MPC 控制器对象使用在预测时域上变化的被操纵变量速率调节权重，则您在运行时只能指定时变的被操纵变量速率调节权重。

要在预测时域上使用相同的调节权重，请将 **du.wt** 连接到一个具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是被操纵变量的数量。每个元素为一个被操纵变量速率指定一个非负调节权重。有关指定调节权重的更多信息，请参阅 Tune Weights。

要使调节权重在预测时域上从时刻 *k* 变化到时刻 *k*+*p*-1，请将 **du.wt** 连接到一个具有 *Nmv* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的调节权重。如果您指定的行数少于 *p*，则最后一行的调节权重将应用于预测时域的剩余部分。有关在预测时域上变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MVRate weights** 参数。

### **ecr.wt** — 松弛变量调节权重标量

要指定运行时松弛变量调节权重，请启用此输入端口并连接一个标量信号。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ECR` 属性中指定的调节权重。

除非您的控制器对象定义了软约束且其关联的 ECR 值非零，否则松弛变量调节权重不起作用。如果存在软约束，增大 **ecr.wt** 值会使这些约束相对更难满足。控制器随后会更高优先级地最小化预测最坏情况约束违反的幅度。

#### 依赖关系

要启用此端口，请选择 **ECR weight** 参数。
### 输出

#### 必需输出

### **mv** — 最优被操纵变量控制作用列向量

最优被操纵变量控制作用，输出为长度为 *Nmv* 的列向量信号，其中 *Nmv* 是被操纵变量的数量。Multiple MPC Controllers 模块将活动控制器的输出传递到 **mv** 输出端口。

如果活动控制器的求解器收敛到局部最优解（**qp.status** 为正），则 **mv** 包含最优解。

如果求解器失败（**qp.status** 为负），则 **mv** 保持在其最近一次成功的解；也就是说，控制器输出冻结。

如果求解器达到最大迭代次数而未找到最优解（**qp.status** 为零），并且活动控制器的 `Optimization.UseSuboptimalSolution` 属性为：

- `true`，则 **mv** 包含次优解
- `false`，则 **mv** 保持在其最近一次成功的解

#### 附加输出

### **cost** — 目标函数代价非负标量

目标函数代价，输出为非负标量信号。代价量化了控制器实现其目标的程度。代价值使用缩放后的 MPC 代价函数计算，其中每一项都是无偏移且无量纲的。

代价值仅在 **qp.status** 输出为非负时才有意义。

#### 依赖关系

要启用此端口，请选择 **Optimal cost** 参数。

### **qp.status** — 优化状态整数

活动控制器的优化状态，以整数信号形式输出。

如果活动控制器针对给定控制区间求解了 QP 问题，则 **qp.status** 输出返回计算中使用的 QP 求解器迭代次数。该值是一个有限的正整数，并且与计算所需时间成正比。因此，较大的值意味着该时间区间内模块执行相对较慢。

QP 求解器可能由于以下原因而无法找到最优解：

- **qp.status** = `0` — QP 求解器无法在 `mpc` 对象中指定的最大迭代次数内找到解。在这种情况下，如果活动控制器的 `Optimizer.UseSuboptimalSolution` 属性为 `false`，则模块将其 **mv** 输出保持为最近一次成功求解的结果。否则，它将使用最后一次求解器迭代中找到的次优解。
- **qp.status** = `-1` — QP 求解器检测到不可行的 QP 问题。有关一个大幅、持续扰动驱动输出变量超出其指定边界的示例，请参见 Monitoring Optimization Status to Detect Controller Failures。在这种情况下，模块将其 **mv** 输出保持为最近一次成功求解的结果。
- **qp.status** = `-2` — QP 求解器在求解严重病态的 QP 问题时遇到数值困难。在这种情况下，模块将其 **mv** 输出保持为最近一次成功求解的结果。

在实时应用中，您可以使用 **qp.status** 设置报警或采取其他特殊操作。

#### 依赖关系

要启用此端口，请选择 **Optimization status** 参数。

### **est.state** — 估计的控制器状态向量

活动控制器的估计控制器状态，以向量信号形式输出。估计状态包括被控对象、扰动和噪声模型状态。

#### 依赖关系

要启用此端口，请选择 **Estimated controller states** 参数。

#### 最优序列

### **mv.seq** — 最优操纵变量序列矩阵

最优操纵变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nmv* 列，其中 *p* 是预测时域，*Nmv* 是操纵变量数量。

**mv.seq** 的前 *p* 行包含从当前时间 *k* 到时间 *k*+*p*-1 计算得到的最优操纵变量值。**mv.seq** 的第一行包含当前操纵变量值（输出 **mv**）。由于控制器不会计算时间 *k*+*p* 的最优控制增量，因此 **mv.seq** 的最后两行相同。

#### 依赖关系

要启用此端口，请选择 **Optimal control sequence** 参数。

### **x.seq** — 最优预测模型状态序列矩阵

最优预测模型状态序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nx* 列，其中 *p* 是预测时域，*Nx* 是状态数量。

**x.seq** 的第一行包含当前估计状态值，这些值来自内置状态估计器或来自自定义状态估计模块输入 **x[k|k]**。**x.seq** 接下来的 *p* 行包含从时间 *k*+1 到时间 *k*+*p* 计算得到的最优状态值。

#### 依赖关系

要启用此端口，请选择 **Optimal state sequence** 参数。

### **y.seq** — 最优输出变量序列矩阵

最优输出变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Ny* 列，其中 *p* 是预测时域，*Ny* 是输出变量数量。

**y.seq** 的前 *p* 行包含从当前时间 *k* 到时间 *k*+*p*-1 计算得到的最优输出值。**y.seq** 的第一行基于当前估计状态和当前测量扰动（输入 **md** 的第一行）计算。由于控制器不会计算时间 *k*+*p* 的最优输出值，因此 **y.seq** 的最后两行相同。

#### 依赖关系

要启用此端口，请选择 **Optimal output sequence** 参数。
## 参数
```yaml
parameters:
- name: Cell Array of MPC Controllers
  summary: 候选控制器 由 mpc 对象组成的元胞数组 | 字符串元胞数组 | 字符向量元胞数组
  group: ''
  block_parameter: mpcobjs
  type: string、character vector、cell array of strings、cell array of character vectors
  default: '""'
- name: Cell Array of Initial Controller States
  summary: 初始状态 由 mpcstate 对象组成的元胞数组 | 字符串元胞数组 | 字符向量元胞数组
  group: ''
  block_parameter: x0s
  type: string、character vector、cell array of strings、cell array of character vectors
  default: '""'
- name: Measured disturbances
  summary: 添加可测扰动输入端口 on（默认）| off
  group: ''
  block_parameter: md_inport_multiple
  type: string、character vector
  values: '"off"、"on"'
  default: '"on"'
- name: External manipulated variable
  summary: 添加外部操纵变量输入端口 off（默认）| on
  group: ''
  block_parameter: mv_inport_multiple
  type: string、character vector
  values: '"off"、"on"'
  default: '"off"'
- name: Targets for manipulated variables
  summary: 添加操纵变量目标输入端口 off（默认）| on
  group: ''
  block_parameter: uref_inport_multiple
  type: string、character vector
  values: '"off"、"on"'
  default: '"off"'
- name: Optimal cost
  summary: 添加最优代价输出端口 off（默认）| on
  group: ''
  block_parameter: return_cost_multiple
  type: string、character vector
  values: '"off"、"on"'
  default: '"off"'
- name: Optimization status
  summary: 添加优化状态输出端口 off（默认）| on
  group: ''
  block_parameter: return_qpstatus_multiple
  type: string、character vector
  values: '"off"、"on"'
  default: '"off"'
- name: Estimated controller states
  summary: 添加估计状态输出端口 off（默认）| on
  group: ''
  block_parameter: return_state_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 最优控制序列
  summary: 添加最优控制序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_mvseq_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 最优状态序列
  summary: 添加最优状态序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_xseq_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 最优输出序列
  summary: 添加最优输出序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_ovseq_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 使用自定义状态估计而非使用内置卡尔曼滤波器
  summary: 使用自定义状态估计输入端口 off（默认）| on
  group: ''
  block_parameter: state_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 下限
  summary: 添加最小 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymin_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 上限
  summary: 添加最大 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymax_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 下限
  summary: 添加最小 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umin_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 上限
  summary: 添加最大 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umax_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 自定义约束
  summary: 添加自定义约束输入端口 off（默认）| on
  group: ''
  block_parameter: cc_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 权重
  summary: 添加 OV 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: ywt_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 权重
  summary: 添加 MV 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: uwt_inport_multiple
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MVRate weights
  summary: 添加 MV 速率整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: duwt_inport_multiple
  type: string, character vector
  values: '"off", "on"'
- name: Slack variable weight
  summary: 添加 ECR 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: rhoeps_inport_multiple
  type: string, character vector
  values: '"off", "on"'
- name: Block data type
  summary: 指定操纵变量的数据类型 double（默认）| single | data type expression
  group: ''
  block_parameter: BlockDataType_multiple
  type: string, character vector
  values: '"double", "single", data type expression'
- name: Inherit sample time
  summary: 从父子系统继承模块采样时间 off（默认）| on
  group: ''
  block_parameter: SampleTimeInherited_multiple
  type: string, character vector
  values: '"off", "on"'
```

### **Cell Array of MPC Controllers** — 候选控制器 由 `mpc` 对象组成的元胞数组 | 字符串元胞数组 | 字符向量元胞数组

候选控制器，指定为以下之一：

- 由 `mpc` 对象组成的元胞数组。
- 由字符串组成的元胞数组或由字符向量组成的元胞数组，其中每个元素是 MATLAB® 工作区中某个 `mpc` 对象的名称。

指定的数组必须至少包含两个候选控制器。元胞数组中的第一个条目对应于开关输入值为 1 的控制器，第二个对应于开关输入值为 2 的控制器，依此类推。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mpcobjs` |
| **类型：** string、character vector、cell array of strings、cell array of character vectors |
| **默认值：** `""` |

### **Cell Array of Initial Controller States** — 初始状态 由 `mpcstate` 对象组成的元胞数组 | 字符串元胞数组 | 字符向量元胞数组

候选控制器的初始状态，指定为以下之一：

- 由 `mpcstate` 对象组成的元胞数组。
- 由字符串组成的元胞数组或由字符向量组成的元胞数组，其中每个元素是 MATLAB 工作区中某个 `mpcstate` 对象的名称。
- `{[],[],...}`、`{'[]','[]',...}` 或 `{"[]","[]",...}` — 使用每个候选控制器的 `Model.Nominal` 属性中定义的标称条件作为其初始状态。

使用此参数可使控制器状态在仿真开始时尽可能准确地反映真实的被控对象环境。这些初始状态可以与 `mpc` 对象中定义的标称状态不同。

如果启用了自定义状态估计，该模块将忽略 **Cell Array of Initial Controller States** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `x0s` |
| **类型：** string、character vector、cell array of strings、cell array of character vectors |
| **默认值：** `""` |

#### 常规选项卡

### **Measured disturbances** — 添加可测扰动输入端口 `on`（默认）| `off`

如果您的控制器具有可测扰动，则必须选择此参数以将 **md** 输出端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `md_inport_multiple` |
| **类型：** string、character vector |
| **值：** `"off"`、`"on"` |
| **默认值：** `"on"` |

### **External manipulated variable** — 添加外部操纵变量输入端口 `off`（默认）| `on`

选择此参数以将 **ext.mv** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mv_inport_multiple` |
| **类型：** string、character vector |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Targets for manipulated variables** — 添加操纵变量目标输入端口 off（默认）| on

选择此参数以将 **mv.target** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uref_inport_multiple` |
| **类型：** string、character vector |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Optimal cost** — 添加最优代价输出端口 off（默认）| on

选择此参数以将 **cost** 输出端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_cost_multiple` |
| **类型：** string、character vector |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Optimization status** — 添加优化状态输出端口 off（默认）| on

选择此参数以将 **qp.status** 输出端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_qpstatus_multiple` |
| **类型：** string、character vector |
| **值：** `"off"`、`"on"` |
| **默认值：** `"off"` |

### **Estimated controller states** — 添加估计状态输出端口 `off`（默认）| `on`

选择此参数以将 **est.state** 输出端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_state_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优控制序列** — 添加最优控制序列输出端口 off（默认）| on

选择此参数可将 **mv.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_mvseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优状态序列** — 添加最优状态序列输出端口 off（默认）| on

选择此参数可将 **x.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_xseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优输出序列** — 添加最优输出序列输出端口 off（默认）| on

选择此参数可将 **y.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_ovseq_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用自定义状态估计而非使用内置卡尔曼滤波器** — 使用自定义状态估计输入端口 `off`（默认）| `on`

选择此参数可移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `state_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 在线功能选项卡

### **OV 下限** — 添加最小 OV 约束输入端口 off（默认）| on

选择此参数可将 **ymin** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymin_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 上限** — 添加最大 OV 约束输入端口 off（默认）| on

选择此参数可将 **ymax** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymax_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 下限** — 添加最小 MV 约束输入端口 off（默认）| on

选择此参数可将 **umin** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umin_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 上限** — 添加最大 MV 约束输入端口 off（默认）| on

选择此参数可将 **umax** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umax_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **自定义约束** — 添加自定义约束输入端口 off（默认）| on

选择此参数可将 **E**、**F**、**G** 和 **S** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cc_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 权重** — 添加 OV 整定权重输入端口 off（默认）| on

选择此参数可将 **y.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ywt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 权重** — 添加 MV 整定权重输入端口 off（默认）| on

选择此参数可将 **u.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uwt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MVRate weights** — 添加 MV 速率整定权重输入端口 off（默认）| on

选择此参数可将 **du.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `duwt_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

### **Slack variable weight** — 添加 ECR 整定权重输入端口 off（默认）| on

选择此参数可将 **ecr.wt** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rhoeps_inport_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |

#### 其他选项卡

### **Block data type** — 指定操纵变量的数据类型 `double`（默认）| `single` | `data type expression`

将操纵变量的模块数据类型指定为以下之一：

- `double` — 双精度浮点
- `single` — 单精度浮点

  如果在单精度目标上实现该模块，请将输出数据类型指定为 `single`。
- `data type expression` — 计算结果为 `double` 或 `single` 的表达式。有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType_multiple` |
| **类型：** string, character vector |
| **值：** `"double"`, `"single"`, `data type expression` |
| **默认：** `"double"` |

### **Inherit sample time** — 从父子系统继承模块采样时间 `off`（默认）| `on`

选择此参数可将父子系统的采样时间继承为模块采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

您必须按照控制器的采样率执行 Function-Call Subsystem 或 Triggered Subsystem 模块。否则，由于以下两个原因，您可能会看到意外结果。

- MV 速率向量的第一个元素（即操纵变量当前值与上一个值之间的差值）通常是在假设上一个 MV 值发生在 MPC 对象中指定的采样时间的情况下进行加权和约束的，而当模块以不同的采样率执行时，此假设不再成立。
- 内置 Kalman 估计器使用 MPC 对象中指定的采样时间向 MPC 优化问题提供当前状态的估计，因此当模块以不同的采样时间执行时，估计状态不再正确。

如果清除此参数（默认），模块的采样时间将从控制器对象继承。

要查看模块的采样时间，请在 Simulink 模型窗口中，在 **Debug** 选项卡上的 **Information Overlays** 下，选择 **colors** 或 **Text**。有关详细信息，请参阅 View Sample Time Information (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTimeInherited_multiple` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |
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

Multiple MPC Controllers 模块的 `mv.seq` 输出端口的信号维度已更改。以前，此信号是 *p*×*Nmv* 矩阵，其中 *p* 是预测时域，*Nmv* 是操纵变量的数量。现在，`mv.seq` 是 (*p*+1)×*Nmv* 矩阵，其中第 *p*+1 行重复第 *p* 行。

## 描述

模拟多个隐式 MPC 控制器之间的切换

在每个控制时刻，Multiple MPC Controllers 模块接收当前被控对象测量输出、参考值以及被控对象测量扰动（如果有）。此外，它还接收一个切换信号，该信号从一组针对工作范围内不同工作点设计的候选 MPC 控制器中选择*活动控制器*。随后，活动控制器求解二次规划，以确定当前输入信号下的最优被控对象操纵变量。

当工作条件发生变化时，Multiple MPC Controllers 模块使您能够实现更好的控制。利用可用的测量值，您可以在运行时检测当前工作区域，并通过 `switch` 输入端口选择合适的活动控制器。针对不同工作区域切换控制器，是使用线性控制技术解决非线性控制问题的一种常见方法。

为提高效率，非活动控制器不计算最优控制动作。然而，为实现控制器之间的无扰切换，非活动控制器会继续执行状态估计。

Multiple MPC Controllers 模块缺少 MPC Controller 模块中的若干可选功能，如下所示：

- 您无法禁用优化。必须始终有一个控制器处于活动状态。
- 您无法从模块对话框内部启动控制器设计；也就是说，没有 **Design** 按钮。在配置 Multiple MPC Controllers 模块之前，请设计所有候选控制器。
- 同样，没有 **Review** 按钮。请改用 `review` 命令或 MPC Designer 应用。
- 您无法在运行时更新输入和输出线性组合的自定义约束。

Multiple MPC Controllers 模块和 Adaptive MPC Controller 模块都能使您的控制系统在运行时适应不断变化的工作条件。下表列出了使用每种模块的优势。

| 模块 | Adaptive MPC Controller | Multiple MPC Controllers |
| --- | --- | --- |
| **自适应方法** | 随着工作条件变化，为单个控制器更新预测模型 | 在为不同工作区域设计的多个控制器之间切换 |
| **优势** | - 只需离线设计单个控制器 - 运行时计算量更少，内存占用更小 - 对被控对象条件中的实际变化更具鲁棒性 | - 无需在线估计被控对象模型 - 控制器可以具有不同的采样时间、预测时域和权重 - 预测模型可以具有不同的阶次或时间域 - 可以全面测试有限的一组候选控制器 |
