---
type: simulink-block
title: 'Model Reference Adaptive Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'modelreferenceadaptivecontrol'
documentation_source_path: 'ug/modelreferenceadaptivecontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Model Reference Adaptive Control

## 端口

### 输入

### **r** — 参考信号 标量信号 | 向量信号

提供受控系统要跟踪的参考信号。

### **state** — 受控系统状态 向量信号

提供来自受控系统的当前状态向量。

### **phi** — 扰动模型特征 向量信号 | 矩阵信号

提供自定义扰动模型特征。

#### 依赖关系

要启用此输入端口，请将 **Feature type** 参数设置为 `Use External Source for Feature`。

### 输出

### **u** — 控制输入 标量信号 | 矩阵信号

将控制输入信号连接到受控系统的输入端。控制输入是一个向量信号，其长度等于受控系统中的控制输入数量。

### **u\_ad** — 扰动和不确定性估计 标量信号 | 矩阵信号

扰动和不确定性估计是扰动模型特征与扰动模型权重向量的乘积。您可以使用此信号将估计的扰动模型与系统中的实际扰动进行比较。

#### 依赖关系

要启用此输出端口，请选择 **Output disturbance/uncertainty estimate** 参数。

### **Ahat** — 估计器状态矩阵 矩阵信号

使用此端口可输出估计器被控对象模型的估计状态矩阵。

#### 依赖关系

此输出端口用于间接 MRAC。要启用此端口，请先选择 **Indirect** 算法选项。然后，选择 **Output estimated parameters** 参数。

### **Bhat** — 估计器控制有效矩阵 向量信号 | 矩阵信号

使用此端口可输出估计器被控对象模型的估计控制有效矩阵。

#### 依赖关系

此输出端口用于间接 MRAC。要启用此端口，请先选择 **Indirect** 算法选项。然后，选择 **Output estimated parameters** 参数。

## 参数

### 系统

选择 MRAC 算法，并指定标称模型、参考模型和估计器模型动态。

### **A** — 标称模型状态矩阵 `0` (默认) | 方阵

将标称模型的状态矩阵指定为 *N*×*N* 矩阵，其中 *N* 是受控系统中的状态数量。

#### 依赖关系

此参数用于直接 MRAC。要启用此参数，请选择 **Direct** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'A'` |
| **类型：** 字符向量 |
| **值：** 方阵 |
| **默认值：** `'0'` |

### **B** — 标称模型控制有效矩阵 `1` (默认) | 向量 | 矩阵

将标称模型的控制有效矩阵指定为非零 *N*×*M* 矩阵，其中 *N* 是受控系统中的状态数量，*M* 是受控系统中的控制输入数量。

#### 依赖关系

此参数用于直接 MRAC。要启用此参数，请选择 **Direct** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'B'` |
| **类型：** 字符向量 |
| **值：** 向量 | 矩阵 |
| **默认值：** `'1'` |

### **Am** — 参考模型状态矩阵 `-1` (默认) | 矩阵

将参考模型的状态矩阵指定为与参数 **A** 具有相同维度的矩阵。对于稳定参考模型，**Am** 必须是 Hurwitz 矩阵，其每个特征值都必须具有严格负实部。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Am'` |
| **类型：** 字符向量 |
| **值：** 方阵 |
| **默认值：** `'-1'` |

### **Bm** — 参考模型控制有效矩阵 `1` (默认) | 向量 | 矩阵

将参考模型的控制有效矩阵指定为与参数 **B** 具有相同维度的非零矩阵。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Bm'` |
| **类型：** 字符向量 |
| **值：** 向量 | 矩阵 |
| **默认值：** `'[0;4]'` |

### **Ahat** — 估计器被控对象模型状态矩阵 `0` (默认) | 方阵

将估计器被控对象模型的状态矩阵指定为 *N*×*N* 矩阵，其中 *N* 是受控系统中的状态数量。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Ahat'` |
| **类型：** 字符向量 |
| **值：** 方阵 |
| **默认值：** `'0'` |

### **Adapt Ahat** — 用于调整估计器被控对象模型状态矩阵的选项 `on` (默认) | `off`

选择此参数后，控制器将调整估计器被控对象模型状态矩阵。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'ALrEnable'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Learning rate (gamma\_a)** — 用于调整估计器被控对象模型状态矩阵的学习率 `1` (默认) | 有限正标量

使用此参数可控制控制器调整估计器被控对象模型状态矩阵的速率。较大的值会增加更新幅度。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请先选择 **Indirect** 算法选项。然后，选择 **Adapt Ahat** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma_a'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** `'1'` |

### **Use learning modification** — 用于启用学习修正以更新估计器模型状态矩阵的选项 `on` (默认) | `off`

为了在较高增益下增加鲁棒性，请选择此选项以向估计器模型状态矩阵更新添加动量项。在 **Learning Modification** 选项卡上配置学习修正。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请先选择 **Indirect** 算法选项。然后，选择 **Adapt Ahat** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'ALrEnableMod'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Bhat** — 估计器被控对象模型控制有效矩阵 `1` (默认) | 向量 | 矩阵

将估计器被控对象模型的控制有效矩阵指定为非零 *N*×*M* 矩阵，其中 *N* 是受控系统中的状态数量，*M* 是受控系统中的控制输入数量。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Bhat'` |
| **类型：** 字符向量 |
| **值：** 向量 | 矩阵 |
| **默认值：** `'1'` |

### **Adapt Bhat** — 用于调整估计器被控对象模型控制有效矩阵的选项 `on` (默认) | `off`

选择此参数后，控制器将调整估计器被控对象模型控制有效矩阵。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'BLrEnable'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Learning rate (gamma\_b)** — 用于调整估计器被控对象模型控制有效矩阵的学习率 `1` (默认) | 有限正标量

使用此参数可控制控制器调整估计器被控对象模型控制有效矩阵的速率。较大的值会增加更新幅度。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请先选择 **Indirect** 算法选项。然后，选择 **Adapt Bhat** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma_a'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** `'1'` |

### **Use learning modification** — 用于启用学习修正以更新估计器模型控制有效矩阵的选项 `on` (默认) | `off`

为了在较高增益下增加鲁棒性，请选择此选项以向估计器模型控制有效矩阵更新添加动量项。在 **Learning Modification** 选项卡上配置学习修正。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请先选择 **Indirect** 算法选项。然后，选择 **Adapt Bhat** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'BLrEnableMod'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Specify estimator feedback gain** — 用于启用估计器反馈增益指定的选项 `off` (默认) | `on`

要指定估计器反馈增益，请先选择此参数。然后，指定 **Estimator feedback gain** 参数。

如果未选择此参数，估计器将使用等于 **Am** 参数的默认反馈增益。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'externalKTauEnable'` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Estimator feedback gain** — 估计器反馈增益 `-1` (默认) | 矩阵

要将 **Am** 矩阵用作默认估计器反馈增益，请将此参数指定为 `-1`。否则，将反馈增益指定为与 **Am** 具有相同维度的 Hurwitz 矩阵。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请先选择 **Indirect** 算法选项。然后，选择 **Specify estimator feedback gain** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'k_tau'` |
| **类型：** 字符向量 |
| **值：** `-1` | 矩阵 |
| **默认值：** `'-1'` |

### **Output estimated parameters** — 用于输出估计器状态矩阵和控制有效矩阵的选项 `off` (默认) | `on`

选择此参数可分别添加 **Ahat** 和 **Bhat** 输出端口，用于估计器状态矩阵值和控制有效矩阵值。

#### 依赖关系

此参数用于间接 MRAC。要启用此参数，请选择 **Indirect** 算法选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `'estParamOutput'` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 控制增益

定义使用直接 MRAC 进行模型匹配时的初始反馈增益和前馈增益。您可以配置该模块以更新这些控制增益并调整相应的学习率。要启用此选项卡上的参数，请选择 **Direct** 算法选项。

### **Feedback gains** — 用于模型匹配的反馈增益 `0` (默认) | 有限标量 | 有限值矩阵

初始反馈增益值。如果未选择 **Adapt feedback gains** 参数，则控制器将指定的反馈增益保持在这些初始值。

#### 编程用法

|  |
| --- |
| **模块参数：** `'kx'` |
| **类型：** 字符向量 |
| **值：** 有限标量 | 有限值矩阵 |
| **默认值：** `'0'` |

### **Adapt feedback gains** — 用于调整反馈增益的选项 `on` (默认) | `off`

选择此参数后，控制器将基于受控系统状态与参考模型状态之间的差异调整反馈增益。

#### 编程用法

|  |
| --- |
| **模块参数：** `'FBLrEnable'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Learning rate (gamma\_x)** — 用于调整反馈增益的学习率 `1` (默认) | 有限正标量

使用此参数可控制控制器调整反馈增益的速率。较大的值会增加增益更新幅度。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma_kx'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** `'1'` |

### **Use learning modification** — 用于启用学习修正以更新反馈增益的选项 `on` (默认) | `off`

为了在较高增益下增加鲁棒性，请选择此选项以向反馈增益更新添加动量项。在 **Learning Modification** 选项卡上配置学习修正。

#### 编程用法

|  |
| --- |
| **模块参数：** `'FBLrEnableMod'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Feedforward gains** — 用于模型匹配的前馈增益 `0` (默认) | 有限标量 | 有限值矩阵

初始前馈增益值。如果未选择 **Adapt feedforward gains** 参数，则控制器将指定的前馈增益保持在这些初始值。

#### 编程用法

|  |
| --- |
| **模块参数：** `'kr'` |
| **类型：** 字符向量 |
| **值：** 有限标量 | 有限值矩阵 |
| **默认值：** `'0'` |

### **Adapt feedforward gains** — 用于调整前馈增益的选项 `on` (默认) | `off`

选择此参数后，控制器将基于受控系统状态与参考模型状态之间的差异调整前馈增益。

#### 编程用法

|  |
| --- |
| **模块参数：** `'FFLrEnable'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Learning rate (gamma\_r)** — 用于调整前馈增益的学习率 `1` (默认) | 有限正标量

使用此参数可控制控制器调整前馈增益的速率。较大的值会增加增益更新幅度。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma_kr'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** `'1'` |

### **Use learning modification** — 用于启用学习修正以更新前馈增益的选项 `on` (默认) | `off`

为了在较高增益下增加鲁棒性，请选择此选项以向前馈增益更新添加动量项。在 **Learning Modification** 选项卡上配置学习修正。

#### 编程用法

|  |
| --- |
| **模块参数：** `'FFLrEnableMod'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### 扰动模型

配置该模块使用的扰动和不确定性模型。在操作期间，该模块会调整扰动模型参数。

### **Enable disturbance adaptation** — 用于启用对系统扰动和不确定性的自适应的选项 `on` (默认) | `off`

选择此参数后，控制器使用扰动模型来估计受控系统中的不确定性和外部扰动。控制器基于受控系统状态与参考模型状态之间的误差调整扰动模型的参数。

扰动模型的形式为 *wT**ϕ*(*x*)。

- *ϕ*(*x*) 是扰动模型特征向量。要配置特征向量，请使用 **Feature type** 参数。
- *wT* 是包含扰动模型参数的权重矩阵。控制器通过调整这些参数来调整其扰动和不确定性模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `'AdaptEnable'` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Learning rate (gamma\_w)** — 用于调整扰动模型参数的学习率 `1` (默认) | 有限正标量

使用此参数可控制控制器调整扰动模型参数的速率。较大的值会增加参数更新幅度。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma'` |
| **类型：** character vector |
| **值：** 有限正标量 |
| **默认值：** `'100'` |

### **Use learning modification** — 用于启用学习修正以更新扰动模型参数的选项 `on`（默认）| `off`

为了在更高增益下增加鲁棒性，请选择此选项以向扰动参数更新添加动量项。在 **Learning Modification** 选项卡上配置学习修正。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'WLrEnableMod'` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Channel learning rate (Q)** — 用于 Lyapunov 解的通道学习率 `1`（默认）| 有限正标量 | 长度为 *N* 且包含正有限值的向量 | 大小为 *N*×*N* 的对称正定矩阵

通道学习率 *Q* 是误差动态的 Lyapunov 函数中状态跟踪误差的加权矩阵。*Q* 的值越大，跟踪误差趋近于零的速度越快。然而，*Q* 的值越大也会产生更大的瞬态，并使系统鲁棒性降低。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Q'` |
| **类型：** character vector |
| **值：** 有限正标量 | 正值向量 | 对称正定矩阵 |
| **默认值：** `'1'` |

### **Feature type** — 扰动模型特征类型 `State`（默认）| `Radial Basis Function` | `Single Hidden Layer Network` | `Use External Source for Feature`

为扰动模型特征向量选择以下类型之一。

- `State` — 使用受控对象的状态作为扰动模型。此选项可能无法充分表示不确定性，因此性能较差。
- `Radial Basis Function` — 使用高斯径向基函数创建特征向量。
- `Single Hidden Layer Network` — 使用具有单隐藏层的神经网络。
- `Use External Source for Feature` — 将 **phi** 输入端口添加到模块。使用此端口提供您自己的自定义特征向量。

有关何时使用每种特征向量类型的详细信息，请参阅 Disturbance and Uncertainty Model。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Radial Basis Function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'FeatureTypeOptions'` |
| **类型：** character vector |
| **值：** `'Radial Basis Function'` | `'State'` | `'Single Hidden Layer Network'` | `'Use External Source for Feature'` |
| **默认值：** `'Radial Basis Function'` |

### **Number of RBF centers** — 用于扰动模型的径向基函数中心数量 `20`（默认）| 正整数

要在扰动模型中使用的径向基函数 (RBF) 中心数量。RBF 中心均匀分布在由 **Centers min** 和 **Centers max** 参数定义的范围上。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Radial Basis Function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'nCen'` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认值：** `'20'` |

### **Centers min** — 径向基函数中心的下限 `-1`（默认）| 有限标量 | 向量

指定径向基函数中心的下限。如果指定标量值，则所有基函数都使用相同的最小值。否则，必须指定长度等于 **Number of RBF centers** 参数的向量。

**Centers min** 参数必须小于 **Centers max** 参数。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Radial Basis Function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'cSpanMin'` |
| **类型：** character vector |
| **值：** 有限标量 | 向量 |
| **默认值：** `'-1'` |

### **Centers max** — 径向基函数中心的上限 `1`（默认）| 有限标量 | 向量

指定径向基函数中心的上限。如果指定标量值，则所有基函数都使用相同的最大值。否则，必须指定长度等于 **Number of RBF centers** 参数的向量。

**Centers max** 参数必须大于 **Centers min** 参数。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Radial Basis Function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'cSpanMax'` |
| **类型：** character vector |
| **值：** 有限标量 | 向量 |
| **默认值：** `'1'` |

### **Bandwidth** — 径向基函数标准差 `5`（默认）| 正标量 | 向量

指定高斯基函数核的标准差。如果指定标量值，则所有基函数都使用相同的标准差。否则，必须指定长度等于 **Number of RBF centers** 参数的向量。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Radial Basis Function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'cSig'` |
| **类型：** character vector |
| **值：** 正标量 | 向量 |
| **默认值：** `'5'` |

### **Number of neurons in hidden layer** — 神经元数量 `10`（默认）| 正整数

指定神经网络隐藏层中的神经元数量。通常，具有更多神经元的网络可以逼近更复杂的非线性扰动。不过，过多的神经元可能会产生含噪的扰动估计。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Single Hidden Layer Network`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'shlHiddenLayerSize'` |
| **类型：** character vector |
| **值：** 正标量 | 向量 |
| **默认值：** `'10'` |

### **Hidden layer learning rate (gamma\_v)** — 用于更新神经网络权重的学习率 `0.1`（默认）| 正标量

使用此参数控制控制器调整神经网络权重的速率。值越大，权重更新的幅度越大。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数，并将 **Feature type** 参数设置为 `Single Hidden Layer Network`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'gamma_V'` |
| **类型：** character vector |
| **值：** 正标量 | 向量 |
| **默认值：** `'0.1'` |

### **Output disturbance/uncertancy estimate** — 输出扰动和不确定性估计的选项 `on`（默认）| `off`

选择此参数以添加 **u\_ad** 输出端口。

#### 依赖项

要启用此参数，请选择 **Enable disturbance adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'adaptiveCntrlOutport'` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### 学习修正

为了在更高增益下增加鲁棒性，您可以修改参数更新以包含动量项。**Parameter Update Equations** 一节中的方程显示了当前模块配置的更新公式。

### **Modification Methods** — 用于更新参数的修正方法 `None`（默认）| `e-Modification` | `Sigma Modification`

选择以下选项之一，用于计算添加到参数更新中的动量项。

- `Sigma Modification` — 动量项是动量权重参数 *σ* 与当前参数值的乘积。
- `e-Modification` — 按误差值的大小缩放 sigma 修正动量项
- `None` — 不使用学习修正。

要指定 *σ*，请使用 **Sigma** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'modChoice'` |
| **类型：** character vector |
| **值：** `'Sigma Modification'` | `'e-Modification'` | `'None'` |
| **默认值：** `'Sigma Modification'` |

### **Sigma** — 参数更新的动量权重 `0.1`（默认）| 标量

指定动量权重项的值。值越大，参数更新增益和参数更新的幅度越大。

#### 依赖项

要启用此参数，请将 **Modification Methods** 参数设置为 `Sigma Modification` 或 `e-Modification`。

#### 编程用法

|  |
| --- |
| **模块参数：** `'sigma_val'` |
| **类型：** character vector |
| **值：** 有限正标量 |
| **默认值：** `'0.1'` |

### **Use discrete-time integration in adaptation** — 在自适应中使用离散时间积分 `off`（默认）| `on`

*自 R2024b 起*

选择以对参数更新使用离散时间积分。这样做允许您为需要用户指定采样时间的嵌入式系统生成代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `'DiscreteEnable'` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Sample time** — 采样时间 `0.05`（默认）| 有限正标量

*自 R2024b 起*

用于离散时间积分的采样时间，指定为有限正标量。

#### 依赖项

要启用此参数，请选择 **Use discrete-time integration in adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'Ts'` |
| **类型：** character vector |
| **值：** 有限正标量 |
| **默认值：** `'0.05'` |

### **Integration method** — 离散积分方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

*自 R2024b 起*

指定用于计算参数更新方程中积分的离散积分公式，如下之一：

- `Forward Euler` — Tsz−1
- `Backward Euler` — Tszz−1
- `Trapezoidal` — Ts2z+1z−1

#### 依赖项

要启用此参数，请选择 **Use discrete-time integration in adaptation** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'IntegrationMethods'` |
| **类型：** character vector |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

## 所属库

Simulink Control Design / Adaptive Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024b：支持嵌入式代码生成

您现在可以配置 Model Reference Adaptive Control 模块，使其对参数更新使用离散时间积分。这样做允许您为需要用户指定采样时间的嵌入式系统生成代码。要使用离散时间积分，请在 **Learning Modification** 选项卡上，启用 **Use discrete-time integration in adaptation**。然后，您可以为参数更新指定所需的采样时间和离散积分方法。

### R2023b：库位置已更改

Model Reference Adaptive Control 模块现在位于 **Simulink Control Design/Adaptive Control** 子库中。

在 R2023b 中，当您打开保存在先前版本中的模型时，Model Reference Adaptive Control 模块的库链接会自动更新。

### R2023a：单隐藏层扰动模型

现在，您可以使用单隐藏层 (SHL) 神经网络来对系统中的扰动和不确定性建模。SHL 神经网络是一种通用函数逼近器，可用于对系统中的非结构化不确定性建模。

为了学习扰动模型，MRAC 控制器会调整神经网络隐藏层和输出层的权重。您可以通过指定隐藏层中的神经元数量和学习率来配置 SHL 神经网络模型。

### R2022a：间接模型参考自适应控制

Model Reference Adaptive Control 模块现在支持间接模型参考自适应控制 (MRAC)。以前，该模块仅支持直接 MRAC。

直接 MRAC 计算控制动作，使不确定的受控系统跟踪给定参考对象模型的行为。然而，间接 MRAC 估计不确定系统的参数，并基于估计的参数推导控制信号。

## 描述

计算控制动作，使受控系统跟踪参考模型

Model Reference Adaptive Control 模块计算控制动作，使不确定的受控系统跟踪给定参考对象模型的行为。使用此模块，您可以实现以下模型参考自适应控制 (MRAC) 算法。

- 直接 MRAC — 估计以下控制器增益，并使用估计的控制器计算控制动作。
  - 将受控系统状态与控制信号关联的反馈增益。
  - 将参考信号与控制信号关联的前馈增益。
- 间接 MRAC — 估计不确定受控系统的以下矩阵，并基于估计的模型推导控制动作。
  - 状态矩阵 *A*
  - 控制有效矩阵 *B*

直接和间接 MRAC 还会估计受控系统中外部扰动和不确定性的模型，并在计算控制动作时使用该模型。

在这两种情况下，基于实时跟踪误差，控制器可以更新估计参数和扰动模型。

有关详细信息，请参阅 Model Reference Adaptive Control。
