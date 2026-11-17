---
type: simulink-block
title: '2-D CFAR Detector'
family: 'detection'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: '2dcfardetector'
documentation_source_path: 'ref/2dcfardetector.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D CFAR Detector

## 端口

### 输入

### **X** — 输入图像 实数 *M*-by-*N* 矩阵 | 实数 *M*-by-*N*-by-*P* 数组

输入图像，指定为实数 *M*-by-*N* 矩阵或实数 *M*-by-*N*-by-*P* 数组。*M* 和 *N* 分别表示矩阵的行数和列数。每页是一个不同的 2-D 信号。

输入矩阵第一个维度的大小可以变化，以模拟不断变化的信号长度。例如，在脉冲波形具有可变脉冲重复频率的情况下，可能会发生这种大小变化。

输入矩阵第一个维度的大小可以变化，以模拟不断变化的信号长度。例如，在脉冲波形具有可变脉冲重复频率的情况下，可能会发生这种大小变化。

**数据类型：** `double`
**复数支持：** 是

### **idx** — 测试单元的位置 由正整数组成的 *2*-by-*L* 矩阵

测试单元的位置，指定为由正整数组成的 *2*-by-*L* 矩阵，其中 *L* 是测试单元的数量。`idx` 的每一列指定一个 CUT 单元的行索引和列索引。CUT 单元的位置受到限制，以使其训练区域完全位于输入图像内。

**数据类型：** `double`

### **K** — 检测阈值因子 正标量

用于计算检测阈值的阈值因子，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Threshold factor method** 参数设置为 `'Input port'`

**数据类型：** `double`

### 输出

### **Y** — 检测结果 逻辑矩阵 (默认) | 实值矩阵

检测结果，其格式取决于 `Output Format` 属性。

- 当 `OutputFormat` 为 `'Cut result'` 时，`Y` 是一个 *D*-by-*P* 矩阵，包含待测单元的逻辑检测结果。*D* 是 `cutidx` 的长度，*P* 是 `X` 的页数。`Y` 的行对应于 `cutidx` 的行。对于每一行，如果 `X` 中的对应单元有检测结果，则 `Y` 在相应列中包含 `1`；否则，`Y` 包含 `0`。
- 当 `OutputFormat` 为 `Detection index` 时，`Y` 是一个包含检测索引的 *K*-by-*L* 矩阵。*K* 是 `X` 的维度数。*L* 是在输入数据中找到的检测数量。当 `X` 是矩阵时，`Y` 以 `[detrow;detcol]` 的形式包含 `X` 中每次检测的行索引和列索引。当 `X` 是数组时，`Y` 以 `[detrow;detcol;detpage]` 的形式包含 `X` 中每次检测的行索引、列索引和页索引。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数量小于此值，则没有检测的列将设置为 `NaN`。

**数据类型：** `double`

### **Th** — 计算得到的检测阈值 实值矩阵

针对每个检测到目标的单元计算得到的检测阈值，以实值矩阵形式返回。`Th` 与 `Y` 具有相同的维度。

- 当 `OutputFormat` 为 `'CUT result'` 时，只要 `Y` 的元素为 `1`，`Th` 就返回检测阈值；只要 `Y` 的元素为 `0`，就返回 `NaN`。
- 当 `OutputFormat` 为 `Detection index` 时，`th` 针对 `Y` 中每个对应的检测返回一个检测阈值。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数量小于此值，则没有检测的列将设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **Output detection threshold** 复选框。

**数据类型：** `double`

### **N** — 估计的噪声功率 实值矩阵

针对每个检测到目标的单元估计的噪声功率，以实值矩阵形式返回。`noise` 与 `Y` 具有相同的维度。

- 当 `OutputFormat` 为 `'CUT result'` 时，只要 `Y` 的元素为 `1`，`noise` 就返回噪声功率；只要 `Y` 的元素为 `0`，就返回 `NaN`。
- 当 `OutputFormat` 为 `'Detection index'` 时，`noise` 针对 `Y` 中每个对应的检测返回一个噪声功率。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数量小于此值，则没有检测的列将设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **Output estimated noise power** 复选框。

**数据类型：** `double`

## 参数

### **CFAR algorithm** — 噪声功率估计算法 `CA` (默认) | `GOCA` | `SOCA` | `OS`

噪声功率估计算法，指定为 `CA`、`GOCA`、`SOCA` 或 `OS`。对于 `CA`、`GOCA`、`SOCA`，噪声功率是根据训练带得出的样本均值。对于 `OS`，噪声功率是通过对所有训练单元值进行数值排序而获得的第 *k* 个单元值。*k* 由 **Rank of order statistic** 参数设置。请参阅训练单元。

| 平均方法 | 描述 |
| --- | --- |
| `CA` — 单元平均算法 | 计算 CUT 单元周围所有训练单元的样本均值。 |
| `GOCA` — 取大单元平均算法 | 将 CUT 单元周围的 2-D 训练窗口分成左半部分和右半部分。然后，算法计算每半部分的样本均值，并选择较大的均值。 |
| `SOCA` — 取小单元平均算法 | 将 CUT 单元周围的 2-D 训练窗口分成左半部分和右半部分。然后，算法计算每半部分的样本均值，并选择较小的均值。 |
| `OS` — 顺序统计算法 | 按数值升序对训练单元进行排序。然后，算法从列表中选择第 *k* 个值。*k* 是由 `Rank` 参数指定的秩。 |

### **Rank of order statistic** — 顺序统计量的秩 `1` (默认) | 正整数

将 2-D CFAR 算法中使用的顺序统计量的秩指定为正整数。此参数的值必须介于 1 和 *Ntrain* 之间，其中 *Ntrain* 是训练单元的数量。值 1 选择训练区域中的最小值。

#### 依赖关系

要启用此参数，请将 **CFAR Algorithm** 参数设置为 `OS`。

### **Size in cells of the guard region band** — 保护带的宽度 `[1,1]` (默认) | 非负整数标量 | 由正整数组成的二元素向量

待测单元每侧的行和列保护单元数量，指定为非负整数。第一个元素指定沿行维度的保护带大小。第二个元素指定沿行维度的保护带大小。将 **Size in cells of the guard region band** 指定为标量，等效于指定一个两个维度具有相同值的向量。例如，值 `[1 1]` 表示每个 CUT 单元周围都有一个宽度为一个保护单元的区域。

### **Size in cells of the training region band** — 训练带的宽度 `[1,1]` (默认) | 非负整数标量 | 由正整数组成的二元素向量

训练区域带的大小（以单元数表示），指定为非负整数或由非负整数组成的 1-by-2 矩阵。第一个元素指定沿行维度的训练带大小，第二个元素指定沿列维度的训练带大小。将 **Size in cells of the training region band** 指定为标量，等效于指定一个两个维度具有相同值的向量。例如，值 `[1 1]` 表示对于每个待测单元，保护区域周围都有一个宽度为一个训练单元的区域。

### **Threshold factor method** — 确定阈值因子的方法 `Auto` (默认) | `Input port` | `Custom`

确定阈值因子的方法，指定为 `Auto`、`Input port` 或 `Custom`。

- 选择 `Auto` 时，根据估计的噪声统计量和虚警概率确定阈值因子。
- 选择 `Input Port` 时，使用 `K` 输入端口设置阈值因子。
- 选择 `Custom` 时，使用 **Custom threshold factor** 参数设置阈值因子。

### **Custom threshold factor** — 自定义阈值因子 `1` (默认) | 正标量

自定义阈值因子，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Threshold factor method** 参数设置为 `Custom`。

### **Probability of false alarm** — 虚警概率 `0.1` (默认) | 介于 0 和 1 之间的实数标量

虚警概率，指定为介于 0 和 1 之间的实数标量。您可以根据所需的虚警概率计算阈值因子。

#### 依赖关系

要启用此参数，请将 **Threshold factor method** 属性设置为 `Auto`。

### **OutputFormat** — 检测结果的格式 `CUT result` (默认) | `Detection index`

检测结果的格式，指定为 `CUT result` 或 `Detection index`。

- 设置为 `'CUT result'` 时，检测结果是每个被测试单元的逻辑检测值（`1` 或 `0`）。
- 设置为 `'Detection index'` 时，结果构成一个向量或矩阵，其中包含超过检测阈值的被测试单元的索引。

### **Output threshold detection** — 启用检测阈值输出 off (默认) | on

选中此复选框可通过 `Th` 输出端口启用检测阈值输出。

### **Output estimated noise power** — 启用检测阈值输出 off (默认) | on

选中此复选框可通过 `N` 输出端口启用估计噪声功率输出。

### **Source of the number of detections** — 要报告的检测数量的来源 `Auto` (默认) | `Property`

检测数量的来源，指定为 `Auto` 或 `Property`。选择 `Auto` 时，报告的检测索引数量等于具有检测结果的待测单元总数。如果选择 `Property`，报告的检测数量由 **Maximum number of detections** 参数的值决定。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`。

**数据类型：** `char`

### **Maximum number of detections** — 要报告的最大检测索引数量 `1` (默认) | 正整数

要报告的最大检测索引数量，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`，并将 **Source of the number of detections** 参数设置为 `Property`。

**数据类型：** `double`

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**于 R2016b 中引入**

## 描述

二维恒虚警率 (CFAR) 检测器

2-D CFAR Detector 模块针对二维图像数据实现恒虚警率检测器。当图像单元值超过阈值时，即判定为检测到目标。为保持恒定的虚警率，阈值设置为图像噪声功率的倍数。检测器使用三种单元平均方法之一或顺序统计量方法，根据待测单元 *(CUT)* 周围的邻近单元估计噪声功率。单元平均方法包括单元平均 (CA)、取大单元平均 (GOCA) 或取小单元平均 (SOCA)。

对于每个测试单元，检测器会：

1. 根据 CUT 单元周围训练带中的单元值估计噪声统计量。
2. 通过将噪声估计值乘以阈值因子来计算阈值。
3. 将 CUT 单元值与阈值进行比较，以确定目标是否存在。如果该值大于阈值，则存在目标。
