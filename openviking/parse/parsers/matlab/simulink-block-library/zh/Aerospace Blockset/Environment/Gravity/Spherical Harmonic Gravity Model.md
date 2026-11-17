---
type: simulink-block
title: 'Spherical Harmonic Gravity Model'
family: 'environment'
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

### 输入

### **Xff** — 固定坐标系坐标 N×3 矩阵

来自行星中心的固定坐标系坐标，指定为 N×3 矩阵，采用所选单位。矩阵的每一行是要计算的单独位置。*z* 轴正向指向北极。如果 **中心天体模型** 的值为 `EGM2008` 或 `EGM96`，则此矩阵包含地心地球固定 (ECEF) 坐标。

当输入大型固定坐标系矩阵和高阶数值时，可能会收到内存不足错误。有关在 MATLAB® 环境中避免内存不足错误的详细信息，请参阅“解决‘内存不足’错误”。

当输入大型固定坐标系矩阵时，可能会受到最大矩阵大小限制。要确定在您的平台上可以在 MATLAB 环境中创建的最大矩阵或数组，请参阅“性能和内存”。

**数据类型：** `double`
### 输出

### **gff** — 重力值 N×3 矩阵

固定坐标系坐标的 *x* 轴、*y* 轴和 *z* 轴方向上的重力值数组，采用所选长度单位每秒平方。矩阵的每一行返回输入矩阵中对应行的计算重力矢量。

**数据类型：** `double`

## 参数

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English`

输入和输出单位，指定为：

| 单位 | 输入 | 输出 |
| --- | --- | --- |
| `Metric (MKS)` | Meters (m) | Meters/sec2 (m/s2) |
| `English` | Feet (ft) | Feet/sec2 (ft/s2) |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **超出范围输入的操作** — 超出范围输入行为 `Warning` (默认) | `Error` | `None`

超出范围输入行为，指定为：

| 值 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error` | MATLAB 返回异常，模型仿真停止。 |

对于小于行星表面的径向位置，球谐重力模型无效。当 **超出范围输入的操作** 设置为 `None` 或 `Warning` 时，Spherical Harmonic Gravity Model 模块接受超出范围的径向位置输入（小于行星赤道半径）。但是，模块输出可能不准确或不可靠。

#### 编程使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

### **中心天体模型** — 行星模型 `EGM2008` (默认) | `EGM96` | `LP100K` | `LP165P` | `GMM2B` | `Custom` | `EIGENGL04C`

行星模型，指定为：

| 中心天体模型 | 说明 |
| --- | --- |
| `EGM2008` | 地球 — 是来自 National Geospatial-Intelligence Agency (NGA) 的最新地球球谐重力模型。此模块提供此重力模型的 WGS-84 版本。如果需要使用较旧的地球标准，可以使用 EGM96 行星模型。 |
| `EGM96` | 地球 |
| `LP100K` | 月球 — 基于计算轨道所需的计算时间，最适合月球轨道确定。此行星模型的创建年份与 LP165P 大致相同，数据相似。 |
| `LP165P` | 月球 — 最适合扩展月球任务的轨道精度。此行星模型的创建年份与 LP100K 大致相同，数据相似。 |
| `GMM2B` | 火星 |
| `Custom` | 使您能够指定自己的行星模型。此选项启用 **中心天体 MAT 文件** 参数。 |
| `EIGENGL04C` | 地球 — 支持重力场模型 EIGEN-GL04C (`https://icgem.gfz-potsdam.de/tom_longtime`)。此模型是 EIGEN-CG03C 的升级。 |

有关中心天体的固定坐标系的详细信息，请参阅算法。

定义自己的行星模型时，**阶数** 参数限制为 int16 的最大值。输入较大的阶数时，可能会收到内存不足错误。有关在 MATLAB 环境中避免内存不足错误的详细信息，请参阅“解决‘内存不足’错误”。

#### 依赖关系

将此参数设置为 `Custom` 会启用 **中心天体 MAT 文件**。

#### 编程使用

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'EGM2008'` | `'EGM96'` | `'LP100K'` | `'LP165P'` | `'GMM2B'` | `'Custom'` | `'EIGENGL04C'` |
| **默认值**: `'EGM2008'` |

### **阶数** — 谐波模型的阶数 `120` (默认) | scalar

谐波模型的阶数，指定为标量：

| 中心天体模型 | 建议阶数 | 最大阶数 |
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
| **模块参数**: `degree` |
| **类型**: character vector |
| **值**: `scalar` |
| **默认值**: `'120'` |

### **中心天体 MAT 文件** — 中心天体 MAT 文件 `'aerogmm2b.mat'` (默认)

中心天体 MAT 文件，包含自定义行星模型的定义。Aerospace Blockset™ 中的 `aerogmm2b.mat` 文件是自定义行星模型的默认 MAT 文件。

此文件必须包含：

| 变量 | 描述 |
| --- | --- |
| *Re* | 行星赤道半径的标量，单位为 meters (m)。 |
| *GM* | 行星引力参数的标量，单位为 meters cubed per second squared (m3/s2) |
| *degree* | 最大阶数的标量。 |
| *C* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *C*。 |
| *S* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *S*。 |

使用较大的 **阶数** 值时，可能会收到内存不足错误。有关在 MATLAB 环境中避免内存不足错误的详细信息，请参阅“解决‘内存不足’错误”。

#### 依赖关系

要启用此参数，请将 **中心天体模型** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**: `datafile` |
| **类型**: character vector |
| **值**: `'aerogmm2b.mat'` | MAT-file |
| **默认值**: `'aerogmm2b.mat'` |

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

Spherical Harmonic Gravity Model 模块基于行星引力势实现球谐行星重力的数学表示。它提供了一种便捷方式，以球谐展开描述行星表面外的行星引力场。

您可以使用球谐来修改球面重力 (-GM/r2) 的大小和方向。最重要或最大的球谐项是二阶带谐项 J2，它考虑了行星的扁率。

如果您需要比球面重力模型更准确的重力值，请使用此模块。例如，非大气飞行应用可能需要更高精度。
