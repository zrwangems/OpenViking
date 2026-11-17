---
type: simulink-block
title: 'Spherical Harmonic Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'sphericalharmonicgravitymodel'
documentation_source_path: 'sphericalharmonicgravitymodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Spherical Harmonic Gravity Model

## 端口
```yaml
ports:
- name: Xff
  summary: 固定坐标系坐标 N×3 矩阵
  direction: input
  data_types: double
- name: gff
  summary: 重力值 N×3 矩阵
  direction: output
  data_types: double
```

### 输入

### **Xff** — 固定坐标系坐标 N×3 矩阵

从行星中心出发的固定坐标系坐标，指定为 N×3 矩阵，单位为所选单位。矩阵的每一行是一个单独的要计算的位置。*z* 轴正向指向北极。如果 **Central body model** 的值为 `EGM2008` 或 `EGM96`，则该矩阵包含地心地球固定（ECEF）坐标。

当输入较大的固定坐标系矩阵和较高的阶数值时，可能会遇到内存不足错误。有关在 MATLAB® 环境中避免内存不足错误的更多信息，请参阅 Resolve “Out of Memory” Errors。

当输入较大的固定坐标系矩阵时，可能会遇到最大矩阵大小限制。要确定在您的平台上 MATLAB 环境中可以创建的最大矩阵或数组，请参阅 Performance and Memory。

**数据类型：** `double`

### 输出

### **gff** — 重力值 N×3 矩阵

固定坐标系 *x* 轴、*y* 轴和 *z* 轴方向上的重力值数组，单位为所选长度单位每秒平方。矩阵的每一行返回输入矩阵中对应行的计算重力矢量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Action for out-of-range input
  summary: 超出范围输入的行为 Warning（默认）| Error | None
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Central body model
  summary: 行星模型 EGM2008（默认）| EGM96 | LP100K | LP165P | GMM2B | Custom | EIGENGL04C
  group: ''
  block_parameter: ptype
  type: 字符向量
  values: '''EGM2008'' | ''EGM96'' | ''LP100K'' | ''LP165P'' | ''GMM2B'' | ''Custom'' | ''EIGENGL04C'''
  default: '''EGM2008'''
- name: Degree
  summary: 谐波模型的阶数 120（默认）| 标量
  group: ''
  block_parameter: degree
  type: 字符向量
  values: scalar
  default: '''120'''
- name: Central body MAT-file
  summary: 中心天体 MAT 文件 'aerogmm2b.mat'（默认）
  group: ''
  block_parameter: datafile
  type: 字符向量
  values: '''aerogmm2b.mat'' | MAT-file'
  default: '''aerogmm2b.mat'''
```

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English`

输入和输出单位，指定为：

| Units | 输入 | 输出 |
| --- | --- | --- |
| `Metric (MKS)` | 米 (m) | 米/秒² (m/s²) |
| `English` | 英尺 (ft) | 英尺/秒² (ft/s²) |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Action for out-of-range input** — 超出范围输入的行为 `Warning`（默认）| `Error` | `None`

超出范围输入的行为，指定为：

| 值 | 描述 |
| --- | --- |
| `None` | 不采取任何操作。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` | MATLAB 返回异常，模型仿真停止。 |

球谐重力模型对于小于行星表面的径向位置是无效的。当 **Action for out-of-range input** 设置为 `None` 或 `Warning` 时，Spherical Harmonic Gravity Model 模块接受超出范围的径向位置输入（小于行星赤道半径）。但是，模块输出可能不准确或不可靠。

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### **Central body model** — 行星模型 `EGM2008`（默认）| `EGM96` | `LP100K` | `LP165P` | `GMM2B` | `Custom` | `EIGENGL04C`

行星模型，指定为：

| Central body model | 说明 |
| --- | --- |
| `EGM2008` | 地球 — 是美国国家地理空间情报局（NGA）最新的地球球谐重力模型。此模块提供该重力模型的 WGS-84 版本。如果需要使用较旧的地球标准，可以使用 EGM96 行星模型。 |
| `EGM96` | 地球 |
| `LP100K` | 月球 — 基于计算轨道所需的计算时间，最适合月球轨道确定。该行星模型与 LP165P 大约在同一年使用类似数据创建。 |
| `LP165P` | 月球 — 最适合延长月球任务轨道精度。该行星模型与 LP100K 大约在同一年使用类似数据创建。 |
| `GMM2B` | 火星 |
| `Custom` | 允许您指定自己的行星模型。此选项启用 **Central body MAT-file** 参数。 |
| `EIGENGL04C` | 地球 — 支持重力场模型 EIGEN-GL04C（`https://icgem.gfz-potsdam.de/tom_longtime`）。该模型是 EIGEN-CG03C 的升级版。 |

有关中心天体固定坐标系系的更多信息，请参阅 Algorithms。

定义自己的行星模型时，**Degree** 参数限制为 int16 的最大值。当输入较大的阶数时，可能会遇到内存不足错误。有关在 MATLAB 环境中避免内存不足错误的更多信息，请参阅 Resolve “Out of Memory” Errors。

#### 依赖关系

将此参数设置为 `Custom` 会启用 **Central body MAT-file**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：字符向量 |
| **值**：`'EGM2008'` | `'EGM96'` | `'LP100K'` | `'LP165P'` | `'GMM2B'` | `'Custom'` | `'EIGENGL04C'` |
| **默认值**：`'EGM2008'` |

### **Degree** — 谐波模型的阶数 `120`（默认）| 标量

谐波模型的阶数，指定为标量：

| Central body model | 推荐阶数 | 最大阶数 |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |

#### 编程使用

|  |
| --- |
| **模块参数**：`degree` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认值**：`'120'` |

### **Central body MAT-file** — 中心天体 MAT 文件 `'aerogmm2b.mat'`（默认）

包含自定义行星模型定义的中心天体 MAT 文件。Aerospace Blockset™ 中的 `aerogmm2b.mat` 文件是自定义行星模型的默认 MAT 文件。

此文件必须包含：

| 变量 | 描述 |
| --- | --- |
| *Re* | 行星赤道半径的标量，单位为米 (m)。 |
| *GM* | 行星引力参数的标量，单位为米的三次方每秒平方 (m³/s²) |
| *degree* | 最大阶数的标量。 |
| *C* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *C*。 |
| *S* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *S*。 |

当 **Degree** 使用较大值时，可能会遇到内存不足错误。有关在 MATLAB 环境中避免内存不足错误的更多信息，请参阅 Resolve “Out of Memory” Errors。

#### 依赖关系

要启用此参数，请将 **Central body model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`datafile` |
| **类型**：字符向量 |
| **值**：`'aerogmm2b.mat'` | MAT-file |
| **默认值**：`'aerogmm2b.mat'` |
## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

实现行星重力的球谐表示

Spherical Harmonic Gravity Model 模块基于行星引力势实现球谐行星重力的数学表示。它提供了一种便捷的方式来以球谐展开描述行星表面之外的重力场。

您可以使用球谐来修改球形重力 (-GM/r²) 的大小和方向。最重要或最大的球谐项是二阶带谐项 J2，它解释了行星的扁率。

如果您需要比球形重力模型更准确的重力值，请使用此模块。例如，非大气飞行应用可能需要更高的精度。
