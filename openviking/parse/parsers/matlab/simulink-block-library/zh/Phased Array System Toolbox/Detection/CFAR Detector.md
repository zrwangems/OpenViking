---
type: simulink-block
title: 'CFAR Detector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'cfardetector'
documentation_source_path: 'ref/cfardetector.html'
language: zh-CN
chinese_source: worker-translation
---

# CFAR Detector

## 端口

### 输入

### **X** — 单元矩阵，实值 *M*×1 列向量 | 实值 *M*×*N* 矩阵

单元矩阵，指定为实值 *M*×1 列向量或实值 *M*×*N* 矩阵。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `single` | `double`

### **Idx** — 被测单元索引，实值长度为 *D* 的向量

被测单元（CUT），指定为实值长度为 *D* 的向量。索引指定要执行检测处理的输入元素或被测单元。当 `X` 为向量时，`Idx` 指定元素。当 `X` 为矩阵时，`Idx` 指定元素的行。同一索引适用于矩阵的所有列。检测沿 `Xww` 的每一列独立执行，针对 `Idx` 中指定的索引。

**数据类型：** `double`

### **K** — 阈值因子，正标量

阈值因子，用于计算检测阈值，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Threshold factor method** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 检测结果 *D*×1 向量 | *D*×*N* 矩阵 | *1*×*L* | 2×*L* 矩阵

`Y` 的格式取决于 **Output format** 属性。

- 当 **Output format** 为 `'Cut result'` 时，`Y` 为 *D*×1 向量或 *D*×*N* 矩阵，包含逻辑检测结果。*D* 是 `Idx` 的长度，*N* 是 `X` 的列数。`Y` 的行对应于 `Idx` 中的行。对于每一行，如果 `X` 的对应列中存在检测，则 `Y` 在该列中包含 `1`。否则，`Y` 包含 `0`。
- 当 **Output format** 为 `'Detection report'` 时，`Y` 为 1×*L* 向量或 2×*L* 矩阵，包含检测索引。*L* 是在输入数据中找到的检测数量。当 `X` 为列向量时，`Y` 包含 `X` 中每个检测的索引。当 `X` 为矩阵时，`Y` 包含 `X` 中每个检测的行索引和列索引。`Y` 的每一列具有 `[detrow;detcol]` 的形式。当 **Source of number of detections** 属性设置为 `'Property'` 时，*L* 等于 **Maximum number of detections** 参数的值。如果实际检测数量小于此值，则没有检测的列设置为 `NaN`。

**数据类型：** `double`

### **Th** — 检测阈值，标量

应用于被测单元的检测阈值，返回为标量。

- 当 **Output format** 为 `'CUT result'` 时，`Th` 端口在 `Y` 的某个元素为 `1` 时输出检测阈值，在 `Y` 的某个元素为 `0` 时输出 `NaN`。`Th` 的输出大小与 `Y` 相同。
- 当 **Output format** 为 `'Detection index'` 时，`Th` 端口为 `Y` 中每个对应的检测输出一个检测阈值。当 **Source of the number of detections** 参数设置为 `'Property'` 时，检测数量由 **Maximum number of detections** 参数设置。如果实际检测数量小于此值，则没有检测的列设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **Output detection threshold** 复选框。

**数据类型：** `double`

### **N** — 估计的噪声功率正标量

每个被测检测单元的估计噪声功率，以正标量形式返回。

- 当 **输出格式** 为 `'CUT result'` 时，当 `Y` 为 `1` 时，`N` 返回噪声功率估计值；当 `Y` 为零时，返回 `NaN`。端口 `N` 的输出与 `Y` 具有相同的大小。
- 当 **输出格式** 为 `'Detection index'` 时，`M` 为 `Y` 中的每个对应检测返回噪声功率估计值。当 **检测数量来源** 属性设置为 `'Property'` 时，*L* 等于 **最大检测数量** 参数的值。如果实际检测数量小于此值，则没有检测的列设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **输出估计的噪声功率** 复选框。

**数据类型：** `double`

## 参数

### **CFAR algorithm** — CFAR 算法 `CA`（默认）| `GOCA` | `SOCA` | `OS`

使用以下值之一指定 CFAR 检测算法

|  |  |
| --- | --- |
| `CA` | 单元平均 |
| `GOCA` | 最大单元平均 |
| `OS` | 有序统计 |
| `SOCA` | 最小单元平均 |

### **Number of guard cells** — 保护单元数量 `2`（默认）

将训练中使用的保护单元数量指定为偶数整数。此参数指定被测单元两侧的单元总数。

### **Number of training cells** — 训练单元数量 `2`（默认）

将训练中使用的训练单元数量指定为偶数整数。在可能的情况下，训练单元在被测单元前后等分。

### **Rank of order statistic** — 有序统计的秩 `1`（默认）

将有序统计的秩指定为正整数标量。该值必须小于或等于 **训练单元数量** 的值。

#### 依赖关系

当 **CFAR algorithm** 设置为 `OS` 时，此参数出现。

### **Threshold factor method** — 获取阈值因子的方法 `Auto`（默认）| `Input port` | `Custom`

指定阈值因子是来自自动计算、**自定义阈值因子** 参数还是输入参数。此参数的值包括：

|  |  |
| --- | --- |
| `Auto` | 应用程序根据 **虚警概率** 参数中指定的期望虚警概率自动计算阈值因子。该计算假设输入中的每个独立信号是来自平方律检测器的单脉冲，且没有脉冲积累。该计算还假设噪声为白高斯噪声。 |
| `Custom` | **自定义阈值因子** 参数指定阈值因子。 |
| `Input port` | 阈值因子使用输入端口 `K` 设置。仅当 **Threshold factor method** 设置为 `Input port` 时，此端口才会出现。 |

### **Probability of false alarm** — 期望虚警概率 `0.1`（默认）

将期望虚警概率指定为 0 到 1 之间（不含端点）的标量。

#### 依赖关系

仅当将 **Threshold factor method** 设置为 `Auto` 时，此参数才会出现。

### **Custom threshold factor** — 自定义阈值因子 `1`（默认）

将自定义阈值因子指定为正标量。

#### 依赖关系

仅当将 **Threshold factor method** 设置为 `Custom` 时，此参数才会出现。

### **Output format** — 检测结果的格式 `CUT result`（默认）| `Detection index`

指定输出端口 `Y` 中返回的检测结果格式为 `CUT result` 或 `Detection index`。

- 当设置为 `CUT result` 时，结果是每个被测单元的逻辑检测值（`1` 或 `0`）。`1` 表示被测单元的值超过检测阈值。
- 当设置为 `Detection index` 时，结果形成一个向量或矩阵，其中包含超过检测阈值的被测单元的索引。

### **Output detection threshold** — 输出检测阈值 off（默认）| on

选中此复选框可创建一个输出端口 `Th`，其中包含检测阈值。

### **Output estimated noise power** — 输出估计噪声功率 off（默认）| on

选中此复选框可创建一个输出端口 `N`，其中包含估计噪声。

### **Source of the number of detections** — 检测数量的来源 `Auto`（默认）| `Property`

将检测数量的来源指定为 `Auto` 或 `Property`。
当您选择 `Auto` 时，报告的检测索引数量为被测单元中具有检测的总数。如果选择 `Property`，则报告的检测数量由 **Maximum number of detections** 参数的值决定。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`。

### **Maximum number of detections** — 要报告的最大检测数量 `1`（默认）

将要报告的检测索引的最大数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`，并将 **Source of the number of detections** 参数设置为 `Property`。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

恒虚警率（CFAR）检测器

CFAR Detector 模块实现一维恒虚警率（CFAR）检测器。检测处理在输入数据的选定元素（称为单元）上执行。当图像单元值超过阈值时，即宣告检测到目标。为保持恒定的虚警率，阈值设置为图像噪声功率的倍数。检测器使用三种单元平均方法之一或一种顺序统计方法，从周围单元估计待测单元 *(CUT)* 的噪声功率。单元平均方法包括单元平均（CA）、最大单元平均（GOCA）或最小单元平均（SOCA）。

有关 CFAR 检测器的更多信息，请参见 [1]。

对于每个测试单元，检测器：

1. 从 CUT 单元周围训练带中的单元值估计噪声统计量。
2. 通过将噪声估计值乘以阈值因子来计算阈值。
3. 将 CUT 单元值与阈值进行比较，以确定目标是否存在。如果该值大于阈值，则目标存在。
