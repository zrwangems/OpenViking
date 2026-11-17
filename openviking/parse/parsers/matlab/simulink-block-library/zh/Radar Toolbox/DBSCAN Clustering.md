---
type: simulink-block
title: 'DBSCAN Clusterer'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'dbscanclusterer'
documentation_source_path: 'ref/dbscanclusterer.html'
language: zh-CN
chinese_source: worker-translation
---

# DBSCAN Clusterer

## 端口

### 输入

### **X** — 输入数据 *N*×*P* 实值矩阵

输入数据，指定为实值 *N*×*P* 矩阵，其中 *N* 是要聚类的数据点数量。*P* 是特征维度数量。DBSCAN 算法可以通过适当的 **Minimum number of points in a cluster** 和 **Cluster threshold epsilon** 设置对任何类型的数据进行聚类。

**数据类型：** `double`

### **Update** — 启用 epsilon 自动更新 `false`（默认）| `true`

启用 epsilon 估计值的自动更新，指定为 `false` 或 `true`。

- 当为 `true` 时，epsilon 阈值首先估计为 *k-NN* 搜索曲线拐点的平均值。然后将该估计值添加到大小为 *L* 的缓冲区中，该大小由 **Length of cluster threshold epsilon history** 参数设置。epsilon 的最终值计算为 *L* 长度 epsilon 历史缓冲区的平均值。如果 **Length of cluster threshold epsilon history** 设置为 1，则估计值是无记忆的。无记忆意味着每个 epsilon 估计值立即被使用，不进行移动平均平滑。
- 当为 `false` 时，使用先前的 epsilon 估计值。估计 epsilon 计算量大，不推荐用于大型数据集。

#### 依赖

要启用此端口，请将 **Source of cluster threshold epsilon** 参数设置为 `Auto`，并设置 **Maximum number of points for 'Auto' epsilon** 参数。

**数据类型：** `Boolean`

### **AmbLims** — 模糊度限制 1×2 实值向量（默认）| 2×2 实值矩阵

模糊度限制，指定为 1×2 实值向量或 2×2 实值矩阵。对于单个模糊度维度，将限制指定为 1×2 向量 *[MinAmbiguityLimitDimension1,MaxAmbiguityLimitDimension1]*。对于两个模糊度维度，将限制指定为 2×2 矩阵 *[MinAmbiguityLimitDimension1, MaxAmbiguityLimitDimension1; MinAmbiguityLimitDimension2,MaxAmbiguityLimitDimension2]*。

聚类可以跨边界进行，以确保模糊检测在最多两个维度上被适当地聚类。输入端口数据 `X` 的模糊列使用 **Indices of ambiguous dimensions** 参数定义。**AmbLims** 参数定义最小和最大模糊度限制，使用的单位与输入数据 `X` 的 **Indices of ambiguous dimensions** 列中使用的单位相同。

#### 依赖

要启用此端口，请选中 **Enable disambiguation of dimensions** 复选框。

**数据类型：** `double`
### 输出

### **Idx** — 聚类索引 *N*×1 整值列向量

聚类索引，返回为 *N*×1 整值列向量。聚类 ID 表示 DBSCAN 算法的聚类结果。值等于 '-1' 表示 DBSCAN 噪声点。正的 `Idx` 值对应于满足 DBSCAN 聚类标准的聚类。

#### 依赖

要启用此端口，请将 **Define outputs for Simulink block** 参数设置为 `Index` 或 `Index and ID`。

**数据类型：** `double`

### **Clusters** — 替代聚类 ID 1×*N* 整值行向量

替代聚类 ID，返回为 1×*N* 正整数行向量。每个值是表示假设目标聚类的唯一标识符。此参数包含所有点（包括噪声）的唯一正聚类 ID。相比之下，`Idx` 输出参数将噪声点标记为 '–1'。将此输出用作 Phased Array System Toolbox™ 模块（如 Range Estimator 和 Doppler Estimator）的输入。

#### 依赖

要启用此端口，请将 **Define outputs for Simulink block** 参数设置为 `Cluster ID` 或 `Index and ID`。

**数据类型：** `double`

## 参数

### **Define outputs for Simulink block** — 聚类数据输出的类型 `Index and ID`（默认）| `Cluster ID` | `Index`

聚类数据输出的类型，指定为：。

- `Index and ID` –- 启用 `Idx`
  和 `Clusters` 输出端口。
- `Cluster ID` –- 仅启用
  `Clusters` 输出端口。
- `Index` –- 仅启用 `Idx` 输出
  端口。

### **Source of cluster threshold epsilon** — Epsilon 来源 `Property`（默认）| `Auto`

聚类阈值的 Epsilon 来源：

- `Property` — Epsilon 从
  **Cluster threshold epsilon** 参数获取。
- `Auto` — Epsilon 使用
  k-近邻（*k*-NN）搜索自动估计。搜索计算时，*k* 的范围从
  **Minimum number of points in a cluster** 的值减一到
  **Maximum number of points for 'Auto' epsilon** 的值减一。需要减一是
  因为一个点的邻域包含该点本身。

### **Cluster threshold epsilon** — 聚类邻域大小 `10.0`（默认）| 正标量 | 正实值 1×*P* 行向量

用于搜索查询的聚类邻域大小，指定为正标量或
实值 1×*P* 行向量。*P* 是输入数据 `X` 中的
聚类维度数。

Epsilon 定义了围绕某个点的半径，在该半径内统计
检测数量。当 epsilon 为标量时，相同的值适用于所有聚类特征
维度。你可以通过指定实值 1×*P* 行向量，为不同聚类维度指定不同的 epsilon 值。使用行向量
会创建多维椭圆搜索区域，当数据列
具有不同的物理含义（例如距离和多普勒）时，这很有用。

### **Minimum number of points in a cluster** — 聚类所需的最小点数 `3`（默认）| 正整数

聚类所需的最小点数，指定为正整数。
该参数定义了在判断一个点是否为核心点时，聚类中的最小点数。

### **Maximum number of points for 'Auto' epsilon** — 聚类所需的最大点数 `10`（默认）| 正整数

聚类中的最大点数，指定为正整数。当对象执行 *k*-NN
搜索时，该属性用于估计 epsilon。

#### 依赖关系

要启用此参数，请将 **Source of cluster threshold
epsilon** 参数设置为 `Auto`。

### **Length of cluster threshold epsilon history** — 聚类阈值 epsilon 历史长度 `10`（默认）| 正整数

存储的聚类阈值 epsilon 历史长度，指定为正
整数。当设置为 1 时，历史是无记忆的。此时，每个 epsilon 估计值都会
立即使用，并且不会进行移动平均平滑。当大于 1 时，
epsilon 值会在指定的历史长度上进行平均。

**Example:** `5`

**Data Types:** `double`

### **Enable disambiguation of dimensions** — 打开维度解模糊 `off`（默认）| `on`

用于启用维度解模糊的复选框，指定为
`false` 或 `true`。选中时，聚类会在执行时由输入端口 `AmbLims`
中的值所定义的边界之间进行。模糊检测会被适当地聚类。使用
**Indices of ambiguous dimensions** 参数来指定 `X` 中可能发生
模糊的那些列索引。最多允许两个模糊
维度。对于大型数据集，不建议打开解模糊。

**Data Types:** `Boolean`

### **模糊维度索引** — 模糊维度的索引 `1`（默认）| 正整数 | 正整数的 1×2 向量

模糊维度的索引，指定为正整数或正整数的 1×2 向量。此属性指定输入端口数据 `X` 中可以进行消歧的列索引。正整数对应于输入数据矩阵 `X` 中的单个模糊维度。1×2 长度的索引行向量对应于两个模糊维度。**模糊维度索引**的大小和顺序必须与 `AmbLims` 输入端口值一致。

**示例：** `[3 4]`

#### 依赖关系

要启用此参数，请选中 **启用维度消歧** 复选框。

**数据类型：** `double`

### **仿真方式** — 模块仿真方法 `解释执行`（默认）| `代码生成`

模块仿真方式，指定为 `解释执行` 或 `代码生成`。如果希望模块使用 MATLAB® 解释器，请选择 `解释执行`。如果希望模块作为编译代码运行，请选择 `代码生成`。编译代码需要时间进行编译，但通常运行更快。

在开发和调优模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `代码生成` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `解释执行` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `代码生成` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

对检测进行聚类

使用基于密度的带噪声应用空间聚类 (DBSCAN) 算法对数据进行聚类。DBSCAN Clusterer 模块可以对任何类型的数据进行聚类。该模块还可以求解聚类阈值 (epsilon)，并可以在两个维度上执行数据消歧。
