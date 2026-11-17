---
type: simulink-block
title: 'MPC Controller'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'mpccontroller'
documentation_source_path: 'ref/mpccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# MPC Controller

## 端口
```yaml
ports:
- name: mo
  summary: 测量输出向量
  direction: input
- name: x[k|k]
  summary: 自定义状态估计向量
  direction: input
- name: ref
  summary: 模型输出参考值行向量 | 矩阵
  direction: input
- name: md
  summary: 输入行向量 | 矩阵
  direction: input
- name: ext.mv
  summary: 上一控制区间内用于被控对象的控制信号向量
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
  summary: 预测时域 正整数
  direction: input
- name: m
  summary: 控制时域 正整数 | 向量
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

### **mo** — 测量输出向量

测量输出，指定为向量信号。该模块使用被控对象测量输出改进其状态估计。如果控制器使用默认状态估计，则必须将被控对象测量输出连接到 **mo** 输入端口。如果控制器使用自定义状态估计，则必须将估计的被控对象状态连接到 **x[k|k]** 输入端口。

#### 依赖

要启用此端口，请清除 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **x[k|k]** — 自定义状态估计向量

自定义状态估计，指定为向量信号。该模块使用连接的状态估计，而不是使用内置估计器估计状态。如果控制器使用自定义状态估计，则必须将当前状态估计连接到 **x[k|k]** 输入端口。如果控制器使用默认状态估计，则必须将测量输出连接到 **mo** 输入端口。

即使噪声模型状态（如果有）不用于 MPC 优化，自定义状态向量也必须包含控制器的 `mpcstate` 对象中定义的所有状态，包括被控对象、扰动和噪声模型状态。

当替代估计技术被认为优于内置估计器时，或者当状态完全可测时，请使用自定义状态估计。

#### 依赖

要启用此端口，请选择 **Use custom state estimation instead of using the built-in Kalman filter** 参数。

### **ref** — 模型输出参考值行向量 | 矩阵

被控对象输出参考值，指定为行向量信号或矩阵信号。

要在预测时域内使用相同的参考值，请将 **ref** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出变量数。每个元素指定一个输出变量的参考值。

要随时间 *k*+1 到时间 *k*+*p* 在预测时域内改变参考值（预览），请将 **ref** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的参考值。如果指定的行数少于 *p*，则最终参考值将用于预测时域的剩余步长。

#### 附加输入

### **md** — 输入行向量 | 矩阵

如果控制器预测模型具有测量扰动，则必须启用此端口，并将行向量或矩阵信号连接到该端口。

要在预测时域内使用相同的测量扰动值，请将 **md** 连接到具有 *Nmd* 个元素的行向量信号，其中 *Nmd* 是操纵变量数。每个元素指定一个测量扰动的值。

要随时间 *k* 到时间 *k*+*p* 在预测时域内改变扰动（预览），请将 **md** 连接到具有 *Nmd* 列且最多 *p*+1 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的扰动。如果指定的行数少于 *p*+1，则最终扰动将用于预测时域的剩余步长。

#### 依赖

要启用此端口，请选择 **Measured disturbances** 参数。

### **ext.mv** — 上一控制区间内用于被控对象的控制信号向量

上一控制区间内用于被控对象的控制信号，指定为长度为 *Nmv* 的向量信号，其中 *Nmv* 是操纵变量的数量。在以下情况下，使用此输入端口来提高状态估计精度：

- 您知道您的控制器并不总是控制被控对象。
- 施加到被控对象的实际 MV 信号可能不同于控制器生成的值，例如在控制信号饱和时。

控制器状态估计假设 MV 是分段常数。因此，在时刻 *tk*，**ext.mv** 值必须包含时刻 *tk–1* 与 *tk* 之间的有效 MV。例如，如果 MV 在该区间内实际变化，您可以提供在时刻 *tk* 评估的时间平均值。

**注意**

- 将 **ext.mv** 连接到上一控制区间内实际施加到被控对象的 MV 信号。通常，这些 MV 信号是控制器生成的值，但并非总是如此。例如，如果您的控制器离线并运行在跟踪模式（即控制器输出不驱动被控对象），则将实际控制信号馈送到 **ext.mv** 有助于在控制器重新在线时实现无扰切换。
- 当控制器驱动被控对象时，插入一个 Memory 模块或 Unit Delay 模块，以反馈上一控制区间内施加到被控对象的 MV 信号。这还可以避免从 **ext.mv** 输入端口到 **mv** 输出端口的直接馈通，从而防止 Simulink 模型中出现代数环。

有关使用外部操纵变量输入端口实现无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **External manipulated variable** 参数。

### **switch** — 启用或禁用优化标量

要关闭控制器优化计算，请将 **switch** 连接到非零信号。

当不需要控制器输出时，例如系统手动运行或另一个控制器已接管时，禁用优化计算可减少计算量。但是，控制器会继续以通常方式更新其内部状态估计。因此，只要 **switch** 信号返回零，它就准备好恢复优化计算。当控制器优化关闭时，模块会将当前 **ext.mv** 信号传递到控制器输出。如果未启用 **ext.mv** 输入端口，则控制器输出保持在禁用优化时的值。

有关使用外部操纵变量输入端口实现无扰切换的示例，请参阅 Switch Controller Online and Offline with Bumpless Transfer。

#### 依赖关系

要启用此端口，请选择 **Use external signal to enable or disable optimization** 参数。

### **mv.target** — 操纵变量目标向量

要指定操纵变量目标，请启用此输入端口，并连接一个向量信号。要使给定的操纵变量跟踪其指定目标值，您还必须为该操纵变量指定非零整定权重。

运行时提供的 **mv.target** 值应用于整个预测时域。

#### 依赖关系

要启用此端口，请选择 **Targets for manipulated variables** 参数。

#### 在线约束

### **ymin** — 最小输出变量约束向量 | 矩阵

要指定运行时最小输出变量约束，请启用此输入端口。如果此端口被禁用，模块将使用其 `mpc` 控制器对象的 `OutputVariables.Min` 属性中指定的下界。如果控制器对象中未为某个输出变量指定下界，则模块在运行时将忽略对应的连接信号。

要在预测时域内从时间 *k*+1 到时间 *k*+*p* 更改边界，请将 **ymin** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*Ny* 是对象输出数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界将应用于预测时域的剩余部分。如果只有一个输出变量，并且连接了一个条目数不超过 *p* 的向量信号，则这些条目将用于整个预测时域。

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
| 标量 **ymin**（单个输出，常量边界） | **ymin** 替换 `OutputVariables.Min` 中的第一个有限条目，并且 `OutputVariables.Min` 中的其余条目以相同的位移量向上或向下移动，以保留原始 `OutputVariables.Min` 向量定义的轮廓。 |
| 列向量 **ymin**（单个输出，时变边界） | **ymin** 替换 `OutputVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **ymin**（多个输出，常量边界） | **ymin** 的第 `i` 个元素替换 `OutputVariables(i).Min` 中的第一个有限条目，并且 `OutputVariables(i).Min` 中的其余条目以相同的位移量向上或向下移动，以保留原始 `OutputVariables(i).Min` 向量定义的轮廓。 |
| 矩阵 **ymin**（多个输出，时变边界）。 | **ymin** 的第 `i` 列替换 `OutputVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |

#### 依赖关系

要启用此端口，请选择 **Lower OV limits** 参数。

### **ymax** — 最大输出变量约束向量 | 矩阵

要指定运行时最大输出变量约束，请启用此输入端口。如果此端口被禁用，模块将使用其 `mpc` 控制器对象的 `OutputVariables.Max` 属性中指定的上界。如果控制器对象中未为某个输出变量指定上界，则模块在运行时将忽略对应的连接信号。

要在从时间 *k*+1 到时间 *k*+*p* 的预测时域内更改边界，请将 **ymax** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*Ny* 是对象输出数量，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的边界。如果指定的行数少于 *p*，则最后一行的边界适用于预测时域的剩余部分。如果只有一个输出变量，并且连接了不超过 *p* 个元素的向量信号，则这些元素将用于整个预测时域。

**ymax** 信号的第 `i` 列对应第 `i` 个对象输出，并在运行时替换 `mpc` 对象的 `OutputVariables(i).Max` 属性。替换行为取决于两个变量的维度。

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
连接信号。

要在预测时域内从时刻 *k* 到
时刻 *k*+*p*-1 更改边界，请将 **umin** 连接到
具有 *Nmv* 列且最多
*p* 行的矩阵信号。这里，*Nmv* 是
被操纵变量的数量，*k* 是当前时刻，*p*
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
| 标量 **umin**（单输出，常量边界） | **umin** 替换 `ManipulatedVariables.Min` 中的第一个有限元素，并且 `ManipulatedVariables.Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `ManipulatedVariables.Min` 向量定义的轮廓。 |
| 列向量 **umin**（单输出，时变边界） | **umin** 替换 `ManipulatedVariables(i).Min` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **umin**（多输出，常量边界） | **umin** 的第 `i` 个分量替换 `ManipulatedVariables(i).Min` 中的第一个有限元素，并且 `ManipulatedVariables(i).Min` 中的其余元素以相同的位移量向上或向下移动，以保留原始 `ManipulatedVariables(i).Min` 向量定义的轮廓。 |
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
具有 *Nmv* 列且最多
*p* 行的矩阵信号。这里，*Nmv* 是
被操纵变量的数量，*k* 是当前时间，*p*
是预测时域。每一行包含一个
预测时域步长的边界。如果指定的行数少于 *p* 行，则最后一行中的边界
适用于预测时域的剩余部分。如果只有一个
被操纵变量，并且连接了不超过 *p* 个元素的向量信号，
则这些元素将用于整个预测时域。

**umax** 信号的第 `i` 列对应于
第 `i` 个被操纵变量，并在运行时替换 `mpc`
对象的 `ManipulatedVariables(i).Max` 属性。替换行为取决于
两个变量的维度。

**`mpc` 对象中的标量 `ManipulatedVariables(i).Max`（第 `i` 个被操纵变量的常量边界，将
应用于所有预测步长）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单输出，常量边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 列向量 **umax**（单输出，时变边界） | **umax** 用时变边界替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 行向量 **umax**（多输出，常量边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |
| 矩阵 **umax**（多输出，时变边界） | **umax** 的第 `i` 列用时变边界替换 `ManipulatedVariables(i).Max` 中定义的常量边界。 |

**`mpc` 对象中的向量 `ManipulatedVariables(i).Max`（第 `i` 个被操纵变量的时变边界，
在不同预测步长具有不同值）**

| **umax** 维度 | 替换行为 |
| --- | --- |
| 标量 **umax**（单输出，常量边界） | **umax** 替换 `ManipulatedVariables.Max` 中的第一个有限元素，并且 `ManipulatedVariables.Max` 中的其余元素以相同的位移量上移或下移，以保留原始 `ManipulatedVariables.Max` 向量定义的轮廓。 |
| 列向量 **umax**（单输出，时变边界） | **umax** 替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并丢弃原始边界轮廓。 |
| 行向量 **umax**（多输出，常量边界） | **umax** 的第 `i` 个元素替换 `ManipulatedVariables(i).Max` 中的第一个有限元素，并且 `ManipulatedVariables(i).Max` 中的其余元素以相同的位移量上移或下移，以保留原始 `ManipulatedVariables(i).Max` 向量定义的轮廓。 |
| 矩阵 **umax**（多输出，时变边界）。 | **umax** 的第 `i` 列替换 `ManipulatedVariables(i).Max` 中定义的时变边界，并丢弃原始边界轮廓。 |

#### 依赖关系

要启用此端口，请选择 **Upper MV limits**
参数。

### **E** — 操纵变量约束矩阵 矩阵

操纵变量约束矩阵，指定为 *Nc*×*Nmv* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Nmv* 是操纵变量的数量。

如果在 `mpc` 对象中定义了 `E`，则必须将信号连接到 **E** 输入端口。否则，连接一个具有正确大小的零矩阵。

要指定运行时混合输入/输出约束，请将 **E** 输入端口与 **F**、**G** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `E` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **F** — 受控输出约束矩阵 矩阵

受控输出约束矩阵，指定为 *Nc*×*Ny* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Ny* 是被控对象输出的数量。如果在 `mpc` 对象中定义了 `F`，则必须将具有相同行数的信号连接到 **F** 输入端口。否则，连接一个具有正确大小的零矩阵。

要指定运行时混合输入/输出约束，请将 **F** 输入端口与 **E**、**G** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `F` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **G** — 自定义约束向量 行向量

自定义约束向量，指定为长度为 *Nc* 的行向量信号，其中 *Nc* 是混合输入/输出约束的数量。如果在 `mpc` 对象中定义了 `G`，则必须将具有相同行数的信号连接到 **G** 输入端口。否则，连接一个具有正确大小的零矩阵。

要指定运行时混合输入/输出约束，请将 **G** 输入端口与 **E**、**F** 和 **S** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `G` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。

### **S** — 测量扰动约束矩阵 矩阵

测量扰动约束矩阵，指定为 *Nc*×*nN* 矩阵信号，其中 *Nc* 是混合输入/输出约束的数量，*Nv* 是测量扰动的数量。如果在 `mpc` 对象中定义了 `S`，则必须将具有相同行数的信号连接到 **S** 输入端口。否则，连接一个具有正确大小的零矩阵。

要指定运行时混合输入/输出约束，请将 **S** 输入端口与 **E**、**F** 和 **G** 端口一起使用。这些约束将替换之前使用 `setconstraint` 设置的混合输入/输出约束。有关混合输入/输出约束的更多信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs。

混合输入/输出约束的数量在运行时不能更改。因此，*Nc* 必须与使用 `setconstraint` 指定的 `G` 矩阵的行数匹配。

#### 依赖关系

要启用此端口，请选择 **Custom constraints** 参数。仅当 `mpc` 对象具有可测扰动时，才会添加此端口。

#### 在线调整权重

### **y.wt** — 输出变量调整权重 行向量 | 矩阵

要指定运行时输出变量调整权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.OutputVariables` 属性中指定的调整权重。这些调整权重用于惩罚输出参考值的偏差。

如果 MPC 控制器对象在预测时域内使用恒定的输出调整权重，则运行时只能指定恒定的输出调整权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的输出调整权重，则运行时只能指定时变输出调整权重。

要在预测时域内使用恒定调整权重，请将 **y.wt** 连接到具有 *Ny* 个元素的行向量信号，其中 *Ny* 是输出个数。每个元素为某个输出变量指定一个非负调整权重。有关指定调整权重的详细信息，请参阅 Tune Weights。

要使调整权重在预测时域内从时刻 *k*+1 到时刻 *k*+*p* 变化，请将 **y.wt** 连接到具有 *Ny* 列且最多 *p* 行的矩阵信号。其中，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的调整权重。如果指定的行数少于 *p*，则最后一行的调整权重将应用于预测时域的剩余部分。有关在预测时域内变化权重的详细信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **OV weights** 参数。

### **u.wt** — 操纵变量调整权重 行向量 | 矩阵

要指定运行时操纵变量调整权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariables` 属性中指定的调整权重。这些调整权重用于惩罚 MV 目标值的偏差。

如果 MPC 控制器对象在预测时域内使用恒定的操纵变量调整权重，则运行时只能指定恒定的操纵变量调整权重。类似地，如果 MPC 控制器对象使用在预测时域内变化的操纵变量调整权重，则运行时只能指定时变操纵变量调整权重。

要在预测时域内使用相同的调整权重，请将 **u.wt** 连接到具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是操纵变量个数。每个元素为某个操纵变量指定一个非负调整权重。有关指定调整权重的详细信息，请参阅 Tune Weights。

要使调整权重在预测时域内从时刻 *k* 到时刻 *k*+*p*-1 变化，请将 **u.wt** 连接到具有 *Nmv* 列且最多 *p* 行的矩阵信号。其中，*k* 是当前时刻，*p* 是预测时域。每一行包含一个预测时域步长的调整权重。如果指定的行数少于 *p*，则最后一行的调整权重将应用于预测时域的剩余部分。有关在预测时域内变化权重的详细信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MV weights** 参数。

### **du.wt** — 被操纵变量速率调节权重行向量 | 矩阵

要指定运行时被操纵变量速率调节权重，请启用此输入端口。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ManipulatedVariablesRate` 属性中指定的调节权重。这些调节权重会惩罚控制量的大幅变化。

如果 MPC 控制器对象在预测时域上使用恒定的被操纵变量速率调节权重，则你在运行时只能指定恒定的被操纵变量速率调节权重。类似地，如果 MPC 控制器对象使用随预测时域变化的被操纵变量速率调节权重，则你在运行时只能指定随时间变化的被操纵变量速率调节权重。

要在预测时域上使用相同的调节权重，请将 **du.wt** 连接到一个具有 *Nmv* 个元素的行向量信号，其中 *Nmv* 是被操纵变量的数量。每个元素为一个被操纵变量速率指定一个非负调节权重。有关指定调节权重的更多信息，请参阅 Tune Weights。

要使调节权重在预测时域上从时间 *k* 变化到时间 *k*+*p*-1，请将 **du.wt** 连接到一个具有 *Nmv* 列且最多 *p* 行的矩阵信号。这里，*k* 是当前时间，*p* 是预测时域。每一行包含一个预测时域步长的调节权重。如果你指定的行数少于 *p*，则最后一行的调节权重将应用于预测时域的剩余部分。有关在预测时域上变化权重的更多信息，请参阅 Setting Time-Varying Weights and Constraints with MPC Designer。

#### 依赖关系

要启用此端口，请选择 **MVRate weights** 参数。

### **ecr.wt** — 松弛变量调节权重标量

要指定运行时松弛变量调节权重，请启用此输入端口并连接一个标量信号。如果此端口被禁用，模块将使用其控制器对象的 `Weights.ECR` 属性中指定的调节权重。

除非你的控制器对象定义了软约束，且其关联的 ECR 值非零，否则松弛变量调节权重不起作用。如果存在软约束，增大 **ecr.wt** 值会使这些约束相对更难满足。控制器随后会更高优先地最小化预测最坏情况约束违反的幅度。

#### 依赖关系

要启用此端口，请选择 **ECR weight** 参数。

#### 在线时域

### **p** — 预测时域 正整数

预测时域，指定为正整数信号。预测时域信号值必须小于或等于 **Maximum prediction horizon** 参数。

在运行时，`p` 的值会覆盖控制器对象中指定的默认预测时域。有关更多信息，请参阅 Adjust Horizons at Run Time。

#### 依赖关系

要启用此端口，请选择 **Adjust prediction horizon and control horizon at run time** 参数。

### **m** — 控制时域 正整数 | 向量

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

目标函数代价，输出为非负标量信号。代价量化了控制器实现其目标的程度。代价值使用
缩放后的 MPC 代价函数计算，其中每一项都是无偏移且
无量纲的。

仅当 **qp.status** 输出为非负时，代价值才有意义。

#### 依赖关系

要启用此端口，请选择 **Optimal cost** 参数。

### **qp.status** — 优化状态整数

优化状态，输出为整数信号。

如果控制器针对给定控制区间求解 QP 问题，则
**qp.status** 输出返回计算中使用的 QP 求解器迭代次数。该值是一个有限正整数，并且与
计算所需时间成正比。因此，较大的值意味着该时间区间内模块执行相对较慢。

QP 求解器可能由于以下原因而无法找到最优解：

- **qp.status** = `0` — QP 求解器无法在 `mpc` 对象中指定的最大迭代次数内找到解。在这种情况下，如果控制器的 `Optimizer.UseSuboptimalSolution` 属性为 `false`，则模块将其 **mv** 输出保持在最近一次成功的解。否则，它使用最后一次求解器迭代中找到的次优解。
- **qp.status** = `-1` — QP 求解器检测到不可行的 QP 问题。有关一个大幅、持续扰动将输出变量驱动到其指定边界之外的示例，请参见 Monitoring Optimization Status to Detect Controller Failures。在这种情况下，模块将其 **mv** 输出保持在最近一次成功的解。
- **qp.status** = `-2` — QP 求解器在求解严重病态的 QP 问题时遇到数值困难。在这种情况下，模块将其 **mv** 输出保持在最近一次成功的解。

在实时应用中，您可以使用 **qp.status** 设置报警或采取其他特殊操作。

#### 依赖关系

要启用此端口，请选择 **Optimization status** 参数。

### **est.state** — 估计的控制器状态向量

每个控制时刻的估计控制器状态，返回为向量信号。估计状态包括被控对象、扰动和噪声模型状态。如果使用自定义状态估计，则该输出信号的值与
**x[k|k]** 输入信号相同。

#### 依赖关系

要启用此端口，请选择 **Estimated controller states**
参数。

#### 最优序列

### **mv.seq** — 最优操纵变量序列矩阵

最优操纵变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nmv* 列，其中 *p* 是预测时域，*Nmv* 是操纵变量的数量。

**mv.seq** 的前 *p* 行包含从当前时刻 *k* 到时刻 *k*+*p*-1 计算得到的最优操纵变量值。**mv.seq** 的第一行包含当前操纵变量值（输出 **mv**）。由于控制器不在时刻 *k*+*p* 计算最优控制量，**mv.seq** 的最后两行相同。

#### 依赖

要启用此端口，请选中 **Optimal control sequence** 参数。

### **x.seq** — 最优预测模型状态序列矩阵

最优预测模型状态序列，以矩阵信号形式返回，具有 *p*+1 行和 *Nx* 列，其中 *p* 是预测时域，*Nx* 是状态的数量。

**x.seq** 的第一行包含当前估计的状态值，这些值来自内置状态估计器或来自自定义状态估计模块输入 **x[k|k]**。**x.seq** 的接下来 *p* 行包含从时刻 *k*+1 到时刻 *k*+*p* 计算得到的最优状态值。

#### 依赖

要启用此端口，请选中 **Optimal state sequence** 参数。

### **y.seq** — 最优输出变量序列矩阵

最优输出变量序列，以矩阵信号形式返回，具有 *p*+1 行和 *Ny* 列，其中 *p* 是预测时域，*Ny* 是输出变量的数量。

**y.seq** 的前 *p* 行包含从当前时刻 *k* 到时刻 *k*+*p*-1 计算得到的最优输出值。**y.seq** 的第一行基于当前估计状态和当前测量扰动（输入 **md** 的第一行）计算得到。由于控制器不在时刻 *k*+*p* 计算最优输出值，**y.seq** 的最后两行相同。

#### 依赖

要启用此端口，请选中 **Optimal output sequence** 参数。
## 参数
```yaml
parameters:
- name: MPC Controller
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
- name: Design
  summary: 交互式设计控制器按钮
  group: ''
- name: Review
  summary: 审查控制器的稳定性和鲁棒性问题按钮
  group: ''
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
- name: 最优输出序列
  summary: 添加最优输出序列输出端口 off（默认）| on
  group: ''
  block_parameter: return_ovseq
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 使用自定义状态估计代替内置卡尔曼滤波器
  summary: 使用自定义状态估计输入端口 off（默认）| on
  group: ''
  block_parameter: state_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 下限
  summary: 添加最小 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymin_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 上限
  summary: 添加最大 OV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: ymax_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 下限
  summary: 添加最小 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umin_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 上限
  summary: 添加最大 MV 约束输入端口 off（默认）| on
  group: ''
  block_parameter: umax_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 自定义约束
  summary: 添加混合输入/输出线性约束矩阵的输入端口 off（默认）| on
  group: ''
  block_parameter: cc_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: OV 权重
  summary: 添加 OV 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: ywt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MV 权重
  summary: 添加 MV 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: uwt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: MVRate 权重
  summary: 添加 MV 速率整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: duwt_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 松弛变量权重
  summary: 添加 ECR 整定权重输入端口 off（默认）| on
  group: ''
  block_parameter: rhoeps_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 在运行时调整预测时域和控制时域
  summary: 添加时域输入端口 off（默认）| on
  group: ''
  block_parameter: pm_inport
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 最大预测时域
  summary: 添加时域输入端口 10（默认）| 正整数
  group: ''
  block_parameter: MaximumP
  type: string, character vector
  default: '"10"'
- name: 采样时间
  summary: 默认模块采样时间 1（默认）| 正标量
  group: ''
  block_parameter: n_ts
  type: string, character vector
  default: '"1"'
- name: 预测时域
  summary: 默认预测时域 10（默认）| 正整数
  group: ''
  block_parameter: n_p
  type: string, character vector
  default: '"10"'
- name: 操纵变量数量
  summary: 默认操纵变量数量 1（默认）| 正整数
  group: ''
  block_parameter: n_mv
  type: string, character vector
  default: '"1"'
- name: 可测扰动数量
  summary: 默认可测扰动数量 1（默认）| 非负整数
  group: ''
  block_parameter: n_md
  type: string, character vector
  default: '"1"'
- name: 不可测扰动数量
  summary: 默认不可测扰动数量 0（默认）| 非负整数
  group: ''
  block_parameter: n_ud
  type: string, character vector
  default: '"0"'
- name: 被测输出数量
  summary: 被测输出的默认数量 1（默认）| 正整数
  group: ''
  block_parameter: n_mo
  type: string, character vector
  default: '"1"'
- name: 非被测输出数量
  summary: 非被测输出的默认数量 0（默认）| 非负整数
  group: ''
  block_parameter: n_uo
  type: string, character vector
  default: '"0"'
- name: 模块数据类型
  summary: 指定操纵变量的数据类型 double（默认）| single | data type expression
  group: ''
  block_parameter: BlockDataType
  type: string, character vector
  values: '"double", "single", data type expression'
  default: '"double"'
- name: 继承采样时间
  summary: 从父子系统继承模块采样时间 off（默认）| on
  group: ''
  block_parameter: SampleTimeInherited
  type: string, character vector
  values: '"off", "on"'
  default: '"off"'
- name: 使用外部信号启用或禁用优化
  summary: 添加开关输入端口 off（默认）| on
  group: ''
  block_parameter: switch_inport
  type: string, character vector
  values: '"off", "on"'
```

### **MPC Controller** — 控制器对象 `mpc` 对象名称

指定一个 `mpc` 对象来定义隐式 MPC 控制器，方法是从 MATLAB 工作区输入一个 `mpc` 对象的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`mpcobj` |
| **类型**：string, character vector |
| **默认值**：`""` |

### **Initial Controller State** — 初始状态 `mpcstate` 对象名称

指定初始控制器状态。如果将此参数留空，模块将使用 `mpc` 对象的 `Model.Nominal` 属性中定义的标称值。要覆盖默认值，请在工作区中创建一个 `mpcstate` 对象，并在该字段中输入其名称。

使用此参数可确保控制器状态尽可能准确地反映仿真开始时被控对象的状态。此初始状态可以与 `mpc` 对象中定义的标称状态不同。

如果启用了自定义状态估计，模块将忽略 **Initial Controller State** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`x0` |
| **类型**：string, character vector |
| **默认值**：`""` |

### **Design** — 交互式设计控制器按钮

要通过 **MPC Controller** 参数以交互方式修改指定的控制器，请点击 **Design** 打开 MPC Designer 应用。例如，您可以：

- 导入新的预测模型。
- 更改预测时域、约束和权重。
- 使用线性被控对象评估 MPC 性能。
- 将更新后的控制器导出到 MATLAB 工作区。

如果 MATLAB 工作区中已有 `mpc` 对象，请使用 **MPC Controller** 参数指定该对象的名称。

如果 MATLAB 工作区中没有现有的 `mpc` 对象，请将 **MPC Controller** 参数留空。在 MPC Controller 模块连接到被控对象的情况下，点击 **Design** 打开 MPC Designer。使用该应用，在指定的工作点对 Simulink 模型进行线性化，并设计您的控制器。要使用此设计方法，您必须拥有 Simulink Control Design™ 软件。有关更多信息，请参阅 Design MPC Controller in Simulink 和 Linearize Simulink Models Using MPC Designer。

### **Review** — 审查控制器的稳定性和鲁棒性问题按钮

一旦您使用 **MPC Controller** 参数指定了控制器，您可以通过点击 **Review** 来审查您的设计是否存在运行时稳定性和鲁棒性问题。有关更多信息，请参阅 Review Model Predictive Controller for Stability and Robustness Issues。

#### 常规选项卡

### **Measured disturbance** — 添加可测扰动输入端口 `on`（默认）| `off`

如果您的控制器具有可测扰动，您必须选择此参数以将 **md** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`md_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"on"` |

### **External manipulated variable** — 添加外部操纵变量输入端口 `off`（默认）| `on`

选择此参数以将 **ext.mv** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`mv_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Targets for manipulated variables** — 添加操纵变量目标输入端口 `off`（默认）| `on`

选择此参数以将 **mv.target** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`uref_inport` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Optimal cost** — 添加最优代价输出端口 `off`（默认）| `on`

选择此参数以将 **cost** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`return_cost` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Optimization status** — 添加优化状态输出端口 `off`（默认）| `on`

选择此参数以将 **qp.status** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`return_qpstatus` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Estimated controller states** — 添加估计状态输出端口 `off`（默认）| `on`

选择此参数以将 **est.state** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`return_state` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Optimal control sequence** — 添加最优控制序列输出端口 `off`（默认）| `on`

选择此参数以将 **mv.seq** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`return_mvseq` |
| **类型**：string, character vector |
| **值**：`"off"`, `"on"` |
| **默认值**：`"off"` |

### **Optimal state sequence** — 添加最优状态序列输出端口 `off`（默认）| `on`

选择此参数以将 **x.seq** 输出端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_xseq` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最优输出序列** — 添加最优输出序列输出端口 `off`（默认）| `on`

选择此参数可将 **y.seq** 输出端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `return_ovseq` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用自定义状态估计代替内置卡尔曼滤波器** — 使用自定义状态估计输入端口 `off`（默认）| `on`

选择此参数可移除 **mo** 输入端口并添加 **x[k|k]** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `state_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

#### 在线功能选项卡

### **OV 下限** — 添加最小 OV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **ymin** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymin_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 上限** — 添加最大 OV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **ymax** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ymax_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 下限** — 添加最小 MV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **umin** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umin_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 上限** — 添加最大 MV 约束输入端口 `off`（默认）| `on`

选择此参数可将 **umax** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `umax_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **自定义约束** — 添加混合输入/输出线性约束矩阵的输入端口 `off`（默认）| `on`

选择此参数可将 **E**、**F**、**G** 和 **S** 输入端口添加到模块中。

有关详细信息，请参阅 Constraints on Linear Combinations of Inputs and Outputs 和 Update Mixed Input/Output Constraints at Run Time。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cc_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **OV 权重** — 添加 OV 整定权重输入端口 `off`（默认）| `on`

选择此参数可将 **y.wt** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ywt_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MV 权重** — 添加 MV 整定权重输入端口 `off`（默认）| `on`

选择此参数可将 **u.wt** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `uwt_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **MVRate 权重** — 添加 MV 速率整定权重输入端口 `off`（默认）| `on`

选择此参数可将 **du.wt** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `duwt_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **松弛变量权重** — 添加 ECR 整定权重输入端口 `off`（默认）| `on`

选择此参数可将 **ecr.wt** 输入端口添加到模块中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rhoeps_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **在运行时调整预测时域和控制时域** — 添加时域输入端口 off（默认）| on

选择此参数可将 **p** 和 **m** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **最大预测时域** — 添加时域输入端口 `10`（默认）| 正整数

选择此参数可将 **p** 和 **m** 输入端口添加到模块。

#### 依赖关系

要启用此参数，请选择 **在运行时调整预测时域和控制时域** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaximumP` |
| **类型：** string, character vector |
| **默认值：** `"10"` |

#### 默认条件选项卡

### **采样时间** — 默认模块采样时间 `1`（默认）| 正标量

使用 MPC Designer 应用执行仿真、修剪或线性化时的默认模块采样时间。您必须指定与您的 Simulink 模型设计兼容的采样时间。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_ts` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **预测时域** — 默认预测时域 `10`（默认）| 正整数

使用 MPC Designer 应用执行仿真、修剪或线性化时的默认预测时域。您必须指定与您的 Simulink 模型设计兼容的预测时域。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_p` |
| **类型：** string, character vector |
| **默认值：** `"10"` |

### **操纵变量数量** — 默认操纵变量数量 `1`（默认）| 正整数

使用 MPC Designer 应用执行仿真、修剪或线性化时的默认操纵变量数量。您必须指定与您的 Simulink 模型设计兼容的值。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_mv` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **可测扰动数量** — 默认可测扰动数量 `1`（默认）| 非负整数

使用 MPC Designer 应用执行仿真、修剪或线性化时的默认可测扰动数量。您必须指定与您的 Simulink 模型设计兼容的值。

#### 依赖关系

- 此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。
- 要使用此参数，您必须选择 **Measured disturbance** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_md` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **不可测扰动数量** — 默认不可测扰动数量 `0`（默认）| 非负整数

使用 MPC Designer 应用执行仿真、修剪或线性化时的默认不可测扰动数量。您必须指定与您的 Simulink 模型设计兼容的值。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_ud` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

### **被测输出数量** — 被测输出的默认数量 `1`（默认）| 正整数

使用 MPC Designer 应用执行仿真、修剪或线性化时，被测输出的默认数量。您必须指定与您的 Simulink 模型设计兼容的值。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_mo` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **非被测输出数量** — 非被测输出的默认数量 `0`（默认）| 非负整数

使用 MPC Designer 应用执行仿真、修剪或线性化时，非被测输出的默认数量。您必须指定与您的 Simulink 模型设计兼容的值。

#### 依赖关系

此参数仅在 **MPC Controller** 参数为空且您使用 **Design** 按钮打开 MPC Designer 时适用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n_uo` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

#### 其他选项卡

### **模块数据类型** — 指定操纵变量的数据类型 `double`（默认）| `single` | `data type expression`

将操纵变量的模块数据类型指定为以下之一：

- `double` — 双精度浮点
- `single` — 单精度浮点

  如果您在单精度目标上实现该模块，请将输出数据类型指定为 `single`。
- `data type expression` — 一个求值为 `double` 或 `single` 的表达式。有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** string, character vector |
| **值：** `"double"`, `"single"`, `data type expression` |
| **默认值：** `"double"` |

### **继承采样时间** — 从父子系统继承模块采样时间 `off`（默认）| `on`

选择此参数以将父子系统的采样时间继承为模块采样时间。这样做允许您在 Function-Call Subsystem (Simulink) 或 Triggered Subsystem (Simulink) 模块内有条件地执行此模块。有关示例，请参阅 Using MPC Controller Block Inside Function-Call and Triggered Subsystems。

**注意**

您必须以控制器的采样率执行 Function-Call Subsystem 或 Triggered Subsystem 模块。否则，您可能会看到意外结果，原因有两个。

- MV 速率向量的第一个元素（即操纵变量的当前值与上一个值之间的差值）通常是在假设上一个 MV 值发生在 MPC 对象中指定的采样时间的过去时刻的情况下进行加权和约束的，而当模块以不同的采样率执行时，此假设不再成立。
- 内置卡尔曼估计器使用 MPC 对象中指定的采样时间来向 MPC 优化问题提供当前状态的估计，因此当模块以不同的采样率执行时，估计状态不再正确。

如果您清除此参数（默认），则模块的采样时间继承自控制器对象。

要查看模块的采样时间，请在 Simulink 模型窗口中，在 **Debug** 选项卡上的 **Information Overlays** 下，选择 **colors** 或 **Text**。有关详细信息，请参阅 View Sample Time Information (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTimeInherited` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认值：** `"off"` |

### **使用外部信号启用或禁用优化** — 添加开关输入端口 `off`（默认）| `on`

选择此参数以将 **switch** 输入端口添加到模块。

#### 程序化使用

|  |
| --- |
| **模块参数：** `switch_inport` |
| **类型：** string, character vector |
| **值：** `"off"`, `"on"` |
| **默认：** `"off"` |
## 所属库

Model Predictive Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

### R2018b：MPC Simulink 模块 `mv.seq` 输出端口信号维度已更改

MPC Controller 模块的 `mv.seq` 输出端口的信号维度已更改。以前，此信号是一个 *p*×*Nmv* 矩阵，其中 *p* 是预测时域，*Nmv* 是操纵变量个数。现在，`mv.seq` 是一个 (*p*+1)×*Nmv* 矩阵，其中第 *p*+1 行重复第 *p* 行。

## 描述

仿真模型预测控制器

MPC Controller 模块接收当前测量输出信号（`mo`）、参考信号（`ref`）以及可选的测量扰动信号（`md`）。该模块通过使用默认 KWIK 求解器或自定义 QP 求解器求解二次规划问题来计算最优操纵变量（`mv`）。有关详细信息，请参阅 QP Solvers for Linear MPC。

要在仿真和代码生成中使用该模块，必须指定一个 `mpc` 对象，该对象定义模型预测控制器。此控制器必须已经针对其所控制的被控对象设计完成。

由于 MPC Controller 模块使用 MATLAB Function 模块，因此每次更改 MPC 对象和模块时都需要编译。此外，由于 MATLAB® 不允许编译后的代码存放在任何 MATLAB 产品文件夹中，因此在使用 MPC 模块时，必须使用非 MATLAB 文件夹来处理您的 Simulink® 模型。
