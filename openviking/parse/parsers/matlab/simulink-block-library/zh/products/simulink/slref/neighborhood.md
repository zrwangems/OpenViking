---
type: simulink-block
title: 'Neighborhood'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'neighborhood'
documentation_source_path: 'slref/neighborhood.html'
language: zh-CN
chinese_source: worker-translation
---

# Neighborhood

## 端口

在 R2025b 中未记录。

## 参数

### **邻域大小** — 邻域窗口的维度 `[3 3]` (默认) | 正标量数组

配置子系统在每次迭代中接收的邻域窗口的维度。邻域的维度不能超过通过 **处理宽度** 和 **处理偏移量** 参数指定的感兴趣区域的维度。

例如，考虑以下输入矩阵：

[12345678910111213141516171819202122232425].

.

如果将 **邻域大小** 设置为 `[3 3]`，则在第七次迭代中，Neighborhood Processing Subsystem 模块会接收围绕第七个元素的以下 3×3 窗口：

[123678111213].

.

#### 编程用法

|  |
| --- |
| **模块参数**: `NeighborhoodSize` |
| **类型**: array |
| **取值**: `[3 3]` | `'<array>'` |
| **默认值**: `[3 3]` |

### **步长** — 迭代之间要跳过的输入矩阵元素数 `[1 1]` (默认) | 正标量数组

配置 Neighborhood Processing Subsystem 模块在每次迭代之间跳过输入矩阵中的一定数量的元素。例如，值 `[1 2]` 将子系统配置为在输入矩阵中隔列进行迭代，值 `[3 1]` 将子系统配置为在输入矩阵中每三行取一行进行迭代。较大的 **步长** 值会产生较小的输出矩阵，因为 Neighborhood Processing Subsystem 模块处理的元素更少。

查看 **步长** 参数值 `[1 1]` 和 `[2 3]` 之间的区别。

一个模型将常量传递通过两个 Neighborhood Processing Subsystem 模块，每个模块都输出到 Display 模块。该常量是包含从 1 到 25 的值的 5×5 矩阵。每个 Neighborhood Processing Subsystem 模块使用 1×1 邻域，并将其 Inport 直接馈送到其 Outport。一个 Neighborhood Processing Subsystem 模块使用步长参数值 [1 1]，并返回输入矩阵不变。另一个 Neighborhood Processing Subsystem 模块使用步长参数值 [2 3]，并返回输入矩阵的 3×2 子区域，其中包含输入矩阵中每三列取一列以及每隔一行取一行的值。

#### 编程用法

|  |
| --- |
| **模块参数**: `Stride` |
| **类型**: array |
| **取值**: `[1 1]` | `'<array>'` |
| **默认值**: `[1 1]` |

### **处理偏移量** — 每次迭代的偏移 `[0 0]` (默认) | 正标量数组

配置算法每次迭代的偏移距离。此距离定义输入矩阵内 ROI 的左上边界。

例如，考虑以下输入矩阵：

[12345678910111213141516171819202122232425].

.

如果使用默认 **处理偏移量** 参数值 `[0 0]`，则第一次迭代使用元素 `1` 周围的邻域，第二次迭代以元素 `2` 为中心，依此类推。如果将 **处理偏移量** 参数值设置为 `[1 2]`，则 Neighborhood Processing Subsystem 模块沿垂直轴将每次迭代的中心偏移 1，沿水平轴偏移 2。第一次迭代以元素 `8` 为中心，第二次迭代以元素 `9` 为中心，依此类推。由于感兴趣区域不能延伸到输入矩阵之外，因此输出矩阵小于输入矩阵。

一个模型将常量传递通过两个 Neighborhood Processing Subsystem 模块，每个模块都输出到 Display 模块。该常量是包含从 1 到 25 的值的 5×5 矩阵。每个 Neighborhood Processing Subsystem 模块使用 1×1 邻域，并将其 Inport 直接馈送到其 Outport。一个 Neighborhood Processing Subsystem 模块使用处理偏移量参数值 -1，并返回输入矩阵不变。另一个 Neighborhood Processing Subsystem 模块使用处理偏移量参数值 [1 2]，并返回输入矩阵中从第 8 个元素到第 25 个元素的子区域。

将 **处理偏移量** 和 **处理宽度** 参数一起使用，以仅处理输入矩阵的子区域。有关示例，请参阅为邻域处理指定感兴趣区域。

#### 编程用法

|  |
| --- |
| **模块参数**: `ProcessingOffset` |
| **类型**: array |
| **取值**: `[0 0]` | `'<array>'` |
| **默认值**: `[0 0]` |

### **处理宽度** — 要处理的输入矩阵子区域 `-1` (默认) | 标量数组

配置要处理的输入矩阵 ROI 的维度。**处理宽度** 参数的维度不能超过输入矩阵的维度。

例如，考虑以下输入矩阵：

[12345678910111213141516171819202122232425].

.

如果使用默认 **处理宽度** 参数值 `-1`，则 Neighborhood Processing Subsystem 模块遍历整个输入矩阵。在此示例中，此行为等效于 **处理宽度** 参数值 `[5 5]`。如果使用 **处理宽度** 参数值 `[3 4]`，则 Neighborhood Processing Subsystem 模块仅遍历输入矩阵左上角的 3×4 区域。

可以在 **处理宽度** 参数向量值内使用值 `-1`，以将 Neighborhood Processing Subsystem 模块配置为遍历特定维度的整个长度。在前面的示例中，如果使用 **处理宽度** 参数值 `[2 -1]`，则 Neighborhood Processing Subsystem 模块遍历输入矩阵顶部的 2×5 区域。

一个模型将常量传递通过两个 Neighborhood Processing Subsystem 模块，每个模块都输出到 Display 模块。该常量是包含从 1 到 25 的值的 5×5 矩阵。每个 Neighborhood Processing Subsystem 模块使用 1×1 邻域，并将其 Inport 直接馈送到其 Outport。一个 Neighborhood Processing Subsystem 模块使用处理宽度参数值 -1，并返回输入矩阵不变。另一个 Neighborhood Processing Subsystem 模块使用处理偏移量参数值 [3 4]，并返回输入矩阵左上角的 3×4 子区域。

将 **处理偏移量** 和 **处理宽度** 参数一起使用，以定义感兴趣区域的左上边界和右下边界。有关示例，请参阅为邻域处理指定感兴趣区域。

#### 编程用法

|  |
| --- |
| **模块参数**: `ProcessingWidth` |
| **类型**: array |
| **取值**: `-1` | `'<array>'` |
| **默认值**: `-1` |

### **输出大小** — 输出矩阵的维度 `Same` (默认) | `Full` | `Valid`

通过选择值 `Same`、`Full` 或 `Valid`，配置希望 Neighborhood Processing Subsystem 模块遍历哪些 ROI 元素。这决定了输出矩阵的维度。

每个示例图都显示一个 5×5 感兴趣区域，其中突出显示三个子区域。

- 蓝色左上方子区域表示 Neighborhood Processing Subsystem 模块在第一次迭代中处理的邻域。
- 橙色右下方子区域表示最后一次迭代的邻域。
- 绿色中心子区域表示输出矩阵的维度，该矩阵跨越第一次和最后一次迭代的中心。

对于使用填充值的设置，示例图将填充值表示为 `?`。

每个示例图都假定 **邻域大小** 参数值为 `[3 3]`，它定义 3×3 邻域。由于每个示例图都假定 **处理偏移量** 参数的默认值 `[0 0]` 和 **处理宽度** 参数的默认值 `-1`，因此感兴趣区域为整个输入矩阵。有关在配置感兴趣区域时 Neighborhood Processing Subsystem 模块如何填充值的信息，请参阅将 Neighborhood Processing Subsystem 模块填充选项与感兴趣区域一起使用。

- `Same` –– 输出矩阵的维度与感兴趣区域相同。对于靠近边缘的元素，邻域会延伸到输入矩阵之外。使用 **填充选项** 参数配置如何填充输入矩阵外部的元素。

  包含从 1 到 25 的值的 5×5 矩阵，周围有一层灰色问号。标有“第一次迭代”的蓝色 3×3 框围绕第一个元素，向左上延伸到问号层中。标有“最后一次迭代”的橙色 3×3 框围绕最后一个元素，向右下延伸到问号层中。绿色 5×5 框围绕原始 5×5 矩阵。
- `Full` –– 输出矩阵大于感兴趣区域。该矩阵为每个至少包含感兴趣区域中一个元素的邻域都包含一个元素，即使邻域中心在感兴趣区域之外也是如此。使用 **填充选项** 参数配置如何填充输入矩阵外部的元素。

  包含从 1 到 25 的值的 5×5 矩阵，周围有两层灰色问号。标有“第一次迭代”的蓝色 3×3 框围绕左上角 3×3 窗口，其中包括八个问号和值 1。标有“最后一次迭代”的橙色 3×3 框围绕右下角 3×3 窗口，其中包括值 25 和八个问号。绿色 7×7 框围绕原始 5×5 矩阵和问号的内层。
- `Valid` –– 输出矩阵小于感兴趣区域。输出矩阵仅包含其邻域完全落在感兴趣区域内的元素。

  包含从 1 到 25 的值的 5×5 矩阵。标有“第一次迭代”的蓝色 3×3 框围绕左上角 3×3 窗口，以元素 7 为中心。标有“最后一次迭代”的橙色 3×3 框围绕右下角 3×3 窗口，以元素 19 为中心。绿色 3×3 框围绕中心 3×3 窗口，以元素 13 为中心。

#### 编程用法

|  |
| --- |
| **模块参数**: `OutputSize` |
| **类型**: character vector |
| **取值**: `'Same'` | `'Full'` | `'Valid'` |
| **默认值**: `'Same'` |

### **填充选项** — 在输入矩阵外部使用的值 `Constant` (默认) | `Replicate` | `Symmetric` | `Circular`

配置如何填充输入矩阵外部的值。当为 **输出大小** 参数选择值 `Full` 或 `Same` 时，某些邻域会延伸到输入矩阵之外，并使用填充后的矩阵元素值。

为了完整说明每个填充选项的逻辑，每个示例图都显示用 5×5 矩阵填充后的 5×5 输入矩阵。在实践中，并非每个填充值都必然是邻域的一部分，具体取决于 **邻域大小** 和 **输出大小** 参数。例如，如果将 **邻域大小** 设置为 `[3 3]` 并将 **输出大小** 设置为 `Same`，则子系统仅使用最内层的填充值。

- `Constant` –– 对输入矩阵外部的元素使用可配置的常量值。例如，此矩阵使用常量值 `0`。

  包含从 1 到 25 的整数的 5×5 矩阵。矩阵外部的每个值都设置为 0。
- `Replicate` –– 扩展边缘元素的值。

  包含从 1 到 25 的整数的 5×5 矩阵。矩阵外部的每个值都设置为输入矩阵中最近的值。
- `Symmetric` –– 镜像输入矩阵。

  包含从 1 到 25 的整数的 5×5 矩阵。矩阵外部的值镜像输入矩阵中的值。
- `Circular` –– 以平铺模式重复输入矩阵。

  包含从 1 到 25 的整数的 5×5 矩阵。矩阵外部的值重复输入矩阵中的模式。

  有关 **填充选项** 参数如何与 **处理偏移量** 和 **处理宽度** 参数交互的信息，请参阅将 Neighborhood Processing Subsystem 模块填充选项与感兴趣区域一起使用。

#### 编程用法

|  |
| --- |
| **模块参数**: `PaddingOption` |
| **类型**: character vector |
| **取值**: `'Constant'` | `'Replicate'` | `'Symmetric'` | `'Circular'` |
| **默认值**: `'Constant'` |

#### 依赖关系

要启用此参数，请将 **输出大小** 设置为 `Same` 或 `Full`。

### **填充常量** — 在输入矩阵外部使用的值 `0` (默认) | 标量

配置用于 `Constant` 填充选项的值。

#### 依赖关系

要启用此参数，请将 **填充选项** 设置为 `Constant`。

#### 编程用法

|  |
| --- |
| **模块参数**: `PaddingConstant` |
| **类型**: scalar |
| **取值**: `0` | `'<scalar>'` |
| **默认值**: `0` |

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

## 版本历史

**在 R2022b 中引入**

## 描述

Neighborhood Processing Subsystem 的控制模块

Neighborhood 模块用作 Neighborhood Processing Subsystem 模块的控制模块。Neighborhood Processing Subsystem 模块遍历输入矩阵。在每次迭代中，子系统内部的 inport 接收一个小矩阵，该矩阵表示输入矩阵中某个元素周围的可配置元素窗口。使用 Neighborhood 模块参数配置 Neighborhood Processing Subsystem 模块的行为，例如窗口维度、输出矩阵的大小以及要遍历的感兴趣区域 (ROI)。
