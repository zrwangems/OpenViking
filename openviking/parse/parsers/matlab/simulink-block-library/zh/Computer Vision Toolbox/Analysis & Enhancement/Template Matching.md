---
type: simulink-block
title: 'Template Matching'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'templatematching'
documentation_source_path: 'ref/templatematching.html'
language: zh-CN
chinese_source: worker-translation
---

# Template Matching

## 端口

### 输入

### **I** — 图像 image

要与模板一起使用的输入图像。该模块不对输入数据进行填充。因此，它只能计算输入图像与模板之间的匹配度量值，其中模板的位置使其完全落在输入图像上。模板的所有此类位置的集合称为输入图像的*有效*区域。有效区域的大小是输入图像与模板图像大小之差加一。

|  |  |
| --- | --- |
| sizevalid=sizeinput – sizetemplate+1 | **(1)** |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **T** — 模板 *M*×*N* 矩阵

模板，指定为 *M*×*N* 矩阵

Template Matching 模块不对输入数据进行填充。因此，它只能计算输入图像与模板之间的匹配度量值，其中模板的位置使其完全落在输入图像上。模板的所有此类位置的集合称为输入图像的*有效*区域。有效区域的大小是输入图像与模板图像大小之差加一。

|  |  |
| --- | --- |
| sizevalid=sizeinput – sizetemplate+1 | **(2)** |

**数据类型：** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **ROI** — 感兴趣区域 四元素向量

感兴趣区域向量，格式为 (*x*,*y*,*width*,*height*)，其中 (*x*,*y*) 是区域左上角的基于一的坐标。该模块输出相对于输入图像左上角的最佳匹配位置索引。

**数据类型：** `single` | `double` | `uint8` | `Boolean` | `fixed point`
### 输出

### **Metric** — 匹配度量值矩阵

匹配度量值矩阵。匹配度量的矩阵始终实现单步穷举窗口迭代。因此，该模块计算每个像素处的度量值。

#### 依赖关系

当您将 **Output** 参数设置为 `Metric matrix` 时，该模块输出有效图像大小。

**数据类型：** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **Loc** — 最佳匹配位置 二元素向量

最佳模板匹配位于基于一的 (*x*,*y*) 坐标处。在 ROI 处理模式下，该模块将 ROI 周围的图像视为 ROI 子区域的延伸。因此，它计算与 ROI 实际边界一致的最佳匹配位置。该模块输出相对于图像左上角的最佳匹配坐标。位置的基于一的 [x y] 坐标对应于模板的中心。下表显示了该模块如何输出奇数模板和偶数模板的中心坐标：

| 模板中像素数为奇数 | 模板中像素数为偶数 |
| --- | --- |
|  |  |

**数据类型：** `uint32`

### **NMetric** — 最佳匹配邻域内的度量值 *N*×*N* 矩阵

最佳匹配邻域内的度量值，以 *N*×*N* 矩阵形式返回。*N* 在掩膜中指定，必须为奇数。当您选择 **Best match location** 以返回最佳匹配周围邻域的度量矩阵时，穷举循环会计算 *N*×*N* 邻域的所有度量值。此输出对于执行亚像素精度的模板匹配特别有用。

**数据类型：** `single` | `double` | `uint8` | `Boolean` | `fixed point`

### **NValid** — 有效邻域 off | on

启用以跟踪有效邻域区域。度量值的邻域矩阵在 ROI 内部有效。该模块按如下方式设置 **NValid** 输出：

- `1` — 包含最佳匹配的邻域完全位于感兴趣区域内。
- `0` — 包含最佳匹配的邻域完全或部分位于感兴趣区域外。

#### 依赖关系

当您启用 **Output NxN matrix of metric values around best match** 参数时，此端口出现。

**数据类型：** `Boolean`

### **ROIValid** — 有效感兴趣区域 off | on

启用以跟踪有效感兴趣区域。如果 ROI 部分位于有效图像外，该模块仅处理 ROI 与有效图像的交集。该模块按如下方式设置 **ROIValid** 输出：

- `1` — ROI 完全位于输入图像的有效部分内。
- `0` — ROI 完全或部分位于输入图像的有效部分外。

#### 依赖关系

当您启用 **Output flag indicating if ROI is valid** 参数时，此端口出现。

**数据类型：** `Boolean`

## 参数

**Main Tab**

### **Match metric** — 匹配度量 `Sum of absolute differences`（默认）| `Sum of squared differences` | `Maximum absolute difference`

选择匹配度量为以下之一：

- `Sum of absolute differences` (SAD)
- `Sum of squared differences` (SSD)
- `Maximum absolute difference` (MaxAD)

该模块在迭代的每一步计算匹配度量。选择最适合您应用的匹配度量。该模块计算最佳度量值的全局最优值。它使用与 ROI（如果提供）相交的输入图像的有效子区域。

### **Output** — 匹配度量 `Match metric`（默认）| `Best match location`

选择输出类型为以下之一：

- `Match metric` — 输出匹配度量矩阵。此选项将 **Metric** 输出端口添加到该模块。
- `Best match location` — 输出最佳匹配位置的 [*x*,*y*] 坐标。此选项将 **Loc** 输出端口添加到该模块。它还使 **Search method**、**Output NxN matrix of metric values around best match** 和 **Enable ROI processing** 参数可用。

  Data Types 窗格上的 **Output** 参数在您将 **Main tab** 上的 **Output** 参数设置为 `Metric matrix` 时出现，或者当您将其设置为 `Best match location` 并启用 **Output NxN matrix of metric values around best match** 参数时出现。

### **Search method** — 搜索方法 `Exhaustive`（默认）| `Three-step`

将搜索方法指定为 `Exhaustive` 或 `Three-step`。`Exhaustive` 搜索方法计算量大，因为它在图像的每个像素位置进行搜索。但是，此方法提供更精确的结果。

`Three-step` 搜索方法是一种快速搜索，使用邻域方法而非在每个像素处搜索。搜索以等于或略大于最大搜索范围一半的步长开始，然后采用以下步骤：

1. 该模块在每一步比较九个搜索点。有一个中心点和位于搜索区域边界上的八个搜索点。
2. 该模块在每一步后将步长减一，以一步像素的步长结束搜索。
3. 在每个新步骤中，该模块将搜索中心移动到前一步骤产生的最佳匹配点。下图中数字一蓝色圆圈表示起始步长为三的搜索。数字二绿色圆圈表示下一次搜索，步长为二，以前一次搜索找到的最佳匹配为中心。最后，数字三橙色圆圈表示最终搜索，步长为一，以前一次最佳匹配为中心。

#### 依赖关系

当您将 **Output** 参数设置为 `Best match location` 时，此参数出现。

### **Output NxN matrix of metric values around best match** — 输出 *N*×*N* 矩阵 on（默认）| off

启用以添加 **NMetric** 和 **NValid** 端口。

#### 依赖关系

当您将 **Output** 参数设置为 `Best match location` 时，此参数出现。

### **N** — 输出矩阵大小 `3`（默认）| 整数

输出矩阵大小。此值确定以最佳匹配位置索引为中心的 *N*×*N* 输出矩阵的大小。*N* 必须为奇数。

#### 依赖关系

当您启用 **Output NxN matrix of metric values around best match** 参数时，此参数出现。

### **Enable ROI processing** — 启用 ROI 处理 on（默认）| off

启用 ROI 处理。

#### 依赖关系

- 当您将 **Output** 参数设置为 `Best match location` 时，此参数出现。
- 当您启用此参数时，该模块添加 **ROI** 输入端口，并且 **Output flag indicating if ROI is valid** 参数出现。

### **Output flag indicating if ROI is valid** — 有效 ROI off（默认）| on

启用以添加 **ROIValid** 端口。

#### 依赖关系

当您启用 **Enable ROI processing** 参数时，此参数出现。

**Data Types Tab**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2009b 中引入**

## 描述

在图像中定位模板

Template Matching 模块在输入图像中查找模板的最佳匹配。该模块通过在感兴趣区域或整个图像上移动模板来计算匹配度量值，然后找到最佳匹配位置。

该模块输出匹配度量值或最佳模板匹配的基于一的 (*x*,*y*) 坐标。该模块可选地输出以最佳匹配位置为中心的 *N*×*N* 匹配度量值矩阵。
