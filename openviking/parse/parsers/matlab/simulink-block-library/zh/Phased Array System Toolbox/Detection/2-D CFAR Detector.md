---
type: simulink-block
title: '2-D CFAR Detector'
family: 'phased'
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
```yaml
ports:
- name: X
  summary: 输入图像 实数 *M*×*N* 矩阵 | 实数 *M*×*N*×*P* 数组
  direction: input
  data_types: double
- name: idx
  summary: 测试单元的位置 *2*×*L* 正整数矩阵
  direction: input
  data_types: double
- name: K
  summary: 检测阈值因子 正标量
  direction: input
  data_types: double
- name: Y
  summary: 检测结果 逻辑矩阵（默认）| 实值矩阵
  direction: output
  data_types: double
- name: Th
  summary: 计算的检测阈值 实值矩阵
  direction: output
  data_types: double
- name: N
  summary: 估计的噪声功率实值矩阵
  direction: output
  data_types: double
```

### 输入

### **X** — 输入图像 实数 *M*×*N* 矩阵 | 实数 *M*×*N*×*P* 数组

输入图像，指定为实数 *M*×*N* 矩阵或实数 *M*×*N*×*P* 数组。*M* 和 *N* 分别表示矩阵的行数和列数。每个页是不同的二维信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **idx** — 测试单元的位置 *2*×*L* 正整数矩阵

测试单元的位置，指定为 *2*×*L* 正整数矩阵，其中 *L* 是测试单元的数量。`idx` 的每一列指定一个 CUT 单元的行索引和列索引。CUT 单元的位置受到限制，使其训练区域完全位于输入图像内。

**数据类型：** `double`

### **K** — 检测阈值因子 正标量

用于计算检测阈值的阈值因子，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Threshold factor method** 参数设置为 `'Input port'`

**数据类型：** `double`
### 输出

### **Y** — 检测结果 逻辑矩阵（默认）| 实值矩阵

检测结果，其格式取决于 `Output
Format` 属性

- 当 `OutputFormat` 为 `'Cut
  result'` 时，`Y` 是一个 *D*×*P* 矩阵，包含被测单元的逻辑检测结果。*D* 是 `cutidx` 的长度，*P* 是 `X` 的页数。`Y` 的行对应于 `cutidx` 的行。对于每一行，如果 `X` 中对应单元存在检测，则 `Y` 在相应列中包含 `1`。否则，`Y` 包含 `0`。
- 当 `OutputFormat` 为 `Detection
  index` 时，`Y` 是一个 *K*×*L* 矩阵，包含检测索引。*K* 是 `X` 的维数。*L* 是在输入数据中找到的检测数量。当 `X` 是矩阵时，`Y` 以 `[detrow;detcol]` 的形式包含 `X` 中每个检测的行索引和列索引。当 `X` 是数组时，`Y` 以 `[detrow;detcol;detpage]` 的形式包含 `X` 中每个检测的行索引、列索引和页索引。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数量小于此值，则没有检测的列设置为 `NaN`。

**数据类型：** `double`

### **Th** — 计算的检测阈值 实值矩阵

每个检测单元的计算检测阈值，以实值矩阵形式返回。`Th` 与 `Y` 具有相同的维度。

- 当 `OutputFormat` 为 `'CUT
  result'` 时，`Th` 在 `Y` 的元素为 `1` 时返回检测阈值，在 `Y` 的元素为 `0` 时返回 `NaN`。
- 当 `OutputFormat` 为 `Detection
  index` 时，`th` 为 `Y` 中每个对应检测返回检测阈值。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数量小于此值，则没有检测的列设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **Output detection threshold** 复选框。

**数据类型：** `double`

### **N** — 估计的噪声功率实值矩阵

每个检测到的单元的估计噪声功率，以实值矩阵形式返回。`noise` 的维度与 `Y` 相同。

- 当 `OutputFormat` 为 `'CUT result'` 时，`noise` 在 `Y` 的元素为 `1` 时返回噪声功率，在 `Y` 的元素为 `0` 时返回 `NaN`。
- 当 `OutputFormat` 为 `'Detection index'` 时，`noise` 为 `Y` 中的每个对应检测返回噪声功率。当 `NumDetectionsSource` 属性设置为 `'Property'` 时，*L* 等于 `NumDetections` 属性的值。如果实际检测数小于此值，则没有检测的列设置为 `NaN`。

#### 依赖关系

要启用此端口，请选中 **Output estimated noise power** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: CFAR algorithm
  summary: 噪声功率估计算法 CA（默认）| GOCA | SOCA | OS
  group: ''
- name: Rank of order statistic
  summary: 有序统计的秩 1（默认）| 正整数
  group: ''
- name: Size in cells of the guard region band
  summary: 保护带的宽度 [1,1]（默认）| 非负整数标量 | 2 元素正整数向量
  group: ''
- name: Size in cells of the training region band
  summary: 训练带的宽度 [1,1]（默认）| 非负整数标量 | 2 元素正整数向量
  group: ''
- name: Threshold factor method
  summary: 确定阈值因子的方法 Auto（默认）| Input port | Custom
  group: ''
- name: Custom threshold factor
  summary: 自定义阈值因子 1（默认）| 正标量
  group: ''
- name: Probability of false alarm
  summary: 虚警概率 0.1（默认）| 0 到 1 之间的实标量
  group: ''
- name: OutputFormat
  summary: 检测结果的格式 CUT result（默认）| Detection index
  group: ''
- name: Output threshold detection
  summary: 启用检测阈值输出 off（默认）| on
  group: ''
- name: Output estimated noise power
  summary: 启用检测阈值输出 off（默认）| on
  group: ''
- name: Source of the number of detections
  summary: 要报告的检测数量的来源 Auto（默认）| Property
  group: ''
- name: Maximum number of detections
  summary: 要报告的检测索引的最大数量 1（默认）| 正整数
  group: ''
```

### **CFAR algorithm** — 噪声功率估计算法 `CA`（默认）| `GOCA` | `SOCA` | `OS`

噪声功率估计算法，指定为 `CA`、`GOCA`、`SOCA` 或 `OS`。对于 `CA`、`GOCA`、`SOCA`，噪声功率是从训练带导出的样本均值。对于 `OS`，噪声功率是从所有训练单元值的数值排序中获得的第 *k* 个单元值。通过 **Rank of order statistic** 参数设置 *k*。参见训练单元。

| 平均方法 | 描述 |
| --- | --- |
| `CA` — 单元平均算法 | 计算 CUT 单元周围所有训练单元的样本均值。 |
| `GOCA` — 最大单元平均算法 | 将 CUT 单元周围的二维训练窗分为左右两半。然后，算法计算每一半的样本均值并选择最大的均值。 |
| `SOCA` — 最小单元平均算法 | 将 CUT 单元周围的二维训练窗分为左右两半。然后，算法计算每一半的样本均值并选择最小的均值。 |
| `OS` — 有序统计算法 | 按数值升序对训练单元进行排序。然后算法从列表中选择第 *k* 个值。*k* 是由 `Rank` 参数指定的秩。 |

### **Rank of order statistic** — 有序统计的秩 `1`（默认）| 正整数

将二维 CFAR 算法中使用的有序统计的秩指定为正整数。此参数的值必须介于 1 和 *Ntrain* 之间，其中 *Ntrain* 是训练单元的数量。值为 1 时选择训练区域中的最小值。

#### 依赖关系

要启用此参数，请将 **CFAR Algorithm** 参数设置为 `OS`。

### **Size in cells of the guard region band** — 保护带的宽度 `[1,1]`（默认）| 非负整数标量 | 2 元素正整数向量

被测单元每一侧的行和列保护单元数量，为非负整数。第一个元素指定沿行维度的保护带大小。第二个元素指定沿行维度的保护带大小。将 **Size in cells of the guard region band** 指定为标量等效于指定两个维度具有相同值的向量。例如，值 `[1 1]` 表示每个 CUT 单元周围有一个保护单元宽的区域。

### **Size in cells of the training region band** — 训练带的宽度 `[1,1]`（默认）| 非负整数标量 | 2 元素正整数向量

训练区域带的单元大小，指定为非负整数或 1×2 非负整数矩阵。第一个元素指定沿行维度的训练带大小，第二个元素指定沿列维度的训练带大小。将 **Size in cells of the training region band** 指定为标量等效于指定两个维度具有相同值的向量。例如，值 `[1 1]` 表示每个被测单元的保护区域周围有一个训练单元宽的区域。

### **Threshold factor method** — 确定阈值因子的方法 `Auto`（默认）| `Input port` | `Custom`

确定阈值因子的方法，指定为 `Auto`、`Input port` 或 `Custom`。

- 当选择 `Auto` 时，阈值因子根据估计的噪声统计量和虚警概率确定。
- 当选择 `Input Port` 时，使用 `K` 输入端口设置阈值因子。
- 当选择 `Custom` 时，使用 **Custom threshold factor** 参数设置阈值因子。

### **Custom threshold factor** — 自定义阈值因子 `1`（默认）| 正标量

自定义阈值因子，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Threshold factor method** 参数设置为 `Custom`。

### **Probability of false alarm** — 虚警概率 `0.1`（默认）| 0 到 1 之间的实标量

虚警概率，指定为 0 到 1 之间的实标量。您可以根据所需的虚警概率计算阈值因子。

#### 依赖关系

要启用此参数，请将 **Threshold factor method** 属性设置为 `Auto`。

### **OutputFormat** — 检测结果的格式 `CUT result`（默认）| `Detection index`

检测结果的格式，指定为 `CUT result` 或 `Detection index`。

- 当设置为 `'CUT result'` 时，检测结果是每个被测单元的逻辑检测值（`1` 或 `0`）。
- 当设置为 `'Detection index'` 时，结果形成一个向量或矩阵，其中包含超过检测阈值的被测单元的索引。

### **Output threshold detection** — 启用检测阈值输出 off（默认）| on

选中此复选框可通过 `Th` 输出端口启用检测阈值的输出。

### **Output estimated noise power** — 启用检测阈值输出 off（默认）| on

选中此复选框可通过 `N` 输出端口启用估计噪声功率的输出。

### **Source of the number of detections** — 要报告的检测数量的来源 `Auto`（默认）| `Property`

检测数量的来源，指定为 `Auto` 或 `Property`。当选择 `Auto` 时，报告的检测索引数量为被测单元中具有检测的总数。如果选择 `Property`，则报告的检测数量由 **Maximum number of detections** 参数的值确定。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`。

**数据类型：** `char`

### **Maximum number of detections** — 要报告的检测索引的最大数量 `1`（默认）| 正整数

要报告的检测索引的最大数量，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Detection index`，并将 **Source of the number of detections** 参数设置为 `Property`。

**数据类型：** `double`
## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

二维恒虚警率（CFAR）检测器

二维 CFAR 检测器模块为二维图像数据实现恒虚警率检测器。当图像单元值超过阈值时，即判定为检测到目标。为保持恒定的虚警率，阈值设置为图像噪声功率的倍数。检测器使用三种单元平均方法之一或一种有序统计方法，从被测单元 *(CUT)* 周围的相邻单元估计噪声功率。单元平均方法包括单元平均（CA）、最大单元平均（GOCA）或最小单元平均（SOCA）。

对于每个测试单元，检测器：

1. 从 CUT 单元周围训练带中的单元值估计噪声统计量。
2. 将噪声估计值乘以阈值因子来计算阈值。
3. 将 CUT 单元值与阈值进行比较，以确定目标存在还是不存在。如果该值大于阈值，则目标存在。
