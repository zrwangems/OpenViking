---
type: simulink-block
title: 'Geoid Height'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'geoidheight'
documentation_source_path: 'geoidheight.html'
language: zh-CN
chinese_source: worker-translation
---

# Geoid Height

## 端口

### 输入

### **μ (deg)** — 大地纬度标量

大地纬度，指定为标量，单位为度，北纬为正，南纬为负。输入纬度必须为 single 或 double 类型。如果纬度不在 –90 到 90 的范围内，该模块会将其环绕到该范围内。

**数据类型：** `double` | `single`

### **l (deg)** — 经度标量

经度，指定为标量，单位为度，东经为正，范围为 0 到 360。输入经度必须为 single 或 double 类型。如果经度不在 0 到 360 的范围内，当 **Action for out-of-range input** 设置为 `None` 或 `Warning` 时，该模块会将其环绕到该范围内。当 **Action for out-of-range input** 设置为 `Error` 时，它不会环绕。

**数据类型：** `double` | `single`
### 输出

### **N** — 大地水准面高度标量

大地水准面高度，以所选长度单位返回为标量。数据类型与第一个输入中的纬度相同。

**数据类型：** `double` | `single`

## 参数

### **Units** — 参数和输出单位 `Metric (MKS)`（默认）| `English`

参数和输出单位，指定为：

| Units | Height |
| --- | --- |
| `Metric (MKS)` | 米 |
| `English` | 英尺 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Geopotential model** — 重力位模型 `EGM96`（默认）| `EGM2008` | `Custom`

重力位模型，指定为：

| Geopotential Model | Description |
| --- | --- |
| `EGM96 (Earth)` | 默认值。EGM96 重力位模型，阶次为 360。该模型使用无潮系统中的 15 分钟点值网格。对于该模型，此模块计算大地水准面高度的精度为 0.01 m。 |
| `EGM2008 (Earth)` | EGM2008 重力位模型，阶次为 2159。该模型使用无潮系统中的 2.5 分钟点值网格。对于该模型，此模块计算大地水准面高度的精度为 0.001 m。  **注意**  此模块要求您使用 Add-On Explorer 下载 EGM2008 重力位模型的大地水准面数据。点击 **Get data** 按钮以启动 Add-On Explorer。有关详细信息，请参阅 `aeroDataPackage`。如果数据已安装，则不会显示 **Get data** 按钮。 |
| `Custom` | 在 **Geopotential mat-file** 中定义的自定义重力位模型。对于自定义模型，此模块计算大地水准面高度的精度为 0.01 m。选择 `Custom` 会启用 **Geopotential mat-file** 参数。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`gtype` |
| **类型**：字符向量 |
| **值**：`'EGM96'` | `'EGM2008'` | `'Custom'` |
| **默认值**：`'Earth'` |

### **Geopotential mat-file** — 重力位 MAT 文件 `'geoidegm96grid'`（默认）| MAT 文件

定义自定义重力位模型的重力位 MAT 文件。

#### 依赖关系

要启用此参数，请将 **Geopotential model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`datafile` |
| **类型**：字符向量 |
| **值**：`'geoidegm96grid'` | MAT 文件 |
| **默认值**：`'geoidegm96grid'` |

### **Data type** — 输入和输出信号的数据类型 `double`（默认）| `single`

输入和输出信号的数据类型，指定为 `double` 或 `single`。

#### 编程使用

|  |
| --- |
| **模块参数**：`dtype` |
| **类型**：字符向量 |
| **值**：`'double'` | `'single'` |
| **默认值**：`'double'` |

### **Action for out-of-range input** — 超出范围输入的行为 `Warning`（默认）| `Error` | `None`

超出范围输入的行为（纬度超出 –90 到 90 度，经度超出 0 到 360 度），指定如下。

| Action | Description |
| --- | --- |
| `None` | 不执行任何操作。 |
| `Warning` | 在 Diagnostic Viewer 中发出警告。 |
| `Error`（默认） | MATLAB® 返回异常，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010b 中引入**

## 描述

计算起伏/高度

Geoid Height 模块使用 **Geopotential model** 参数计算大地水准面高度。该模块从无潮系统中的点值网格插值大地水准面高度。它使用指定的重力位模型，达到该模型的阶次和次数。大地水准面起伏相对于 WGS84 椭球体。

插值方案在极点处进行环绕，以允许在这些位置及其附近计算大地水准面高度。
