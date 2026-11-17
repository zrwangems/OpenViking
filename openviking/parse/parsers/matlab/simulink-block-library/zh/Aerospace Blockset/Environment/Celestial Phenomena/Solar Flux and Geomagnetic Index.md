---
type: simulink-block
title: 'Solar Flux and Geomagnetic Index'
family: 'environment'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'solarfluxandgeomagneticindex'
documentation_source_path: 'solarfluxandgeomagneticindex.html'
language: zh-CN
chinese_source: worker-translation
---

# Solar Flux and Geomagnetic Index

## 端口

### 输入

### **Year** — 年份标量

Year，指定为标量。`aeroReadSpaceWeatherData`
函数忽略 `year` 的值。

#### 依赖关系

要启用此端口，请将 **输入时间设定** 参数设置为 `Year, day, sec`。

**数据类型：** `double`

### **DOY** — 年积日标量

年积日，指定为标量。

#### 依赖关系

要启用此端口，请将 **输入时间设定** 参数设置为 `Year, day, sec`。

**数据类型：** `double`

### **UTC (sec)** — 协调世界时 (UTC) 标量

协调世界时 (UTC)，指定为以秒为单位的标量。此值是相对于 **DOY** 午夜的秒数。

#### 依赖关系

要启用此端口，请将 **输入时间设定** 参数设置为 `Year, day, sec`。

**数据类型：** `double`

### **TJD** — 协调世界时 (UTC) 标量

协调世界时 (UTC)，指定为标量儒略日。

#### 依赖关系

要启用此端口，请将 **输入时间设定** 参数设置为 `Julian date`。

**数据类型：** `double`

### 输出

### **F107A** — F10.7 通量的 81 天平均值标量

81 天 F10.7 通量平均值，以年积日 (`dayOfYear`) 为中心，指定为标量。此值对应于地球与太阳实际距离处的 10.7 cm 射电流量。该值不对应于 1 AU 处的射电流量。

**数据类型：** `double`

### **F107** — 前一日的每日 F10.7 通量标量

前一日的每日 F10.7 通量，指定为标量。此值对应于地球与太阳实际距离处的 10.7 cm 射电流量。该值不对应于 1 AU 处的射电流量。

**数据类型：** `double`

### **aph** — 磁指数信息 1×7 数组

磁指数信息，指定为 1×7 数组。此信息包括：

- 日磁指数 (AP)
- 当前时刻的 3 小时 AP
- 当前时刻前 3 小时的 3 小时 AP
- 当前时刻前 6 小时的 3 小时 AP
- 当前时刻前 9 小时的 3 小时 AP
- 当前时刻前 12 至 33 小时的八个 3 小时 AP 指数的平均值
- 当前时刻前 36 至 57 小时的八个 3 小时 AP 指数的平均值

  更多信息，请参阅限制。

**数据类型：** `double`

## 参数

### **空间天气数据文件** — 空间天气数据的 MAT 文件 `aeroSpaceWeatherData.mat`（默认） | MAT 文件名

空间天气数据的 MAT 文件。此文件是 `aeroReadSpaceWeatherData` 函数的输出。

Aerospace Blockset™ 包含默认空间天气数据文件 `aeroSpaceWeatherData.mat`。要使用可用的最新数据，请使用 `aeroReadSpaceWeatherData` 生成新的 MAT 文件，并为该参数指定文件名。更多信息，请参阅 `aeroReadSpaceWeatherData`。

如果文件不在 MATLAB® 路径上，请指定完整路径名。MAT 文件必须包含空间天气数据文件中的以下变量：

- `YEAR`
- `MONTH`
- `DAY`
- `AP1`
- `AP2`
- `AP3`
- `AP4`
- `AP5`
- `AP6`
- `AP7`
- `AP8`
- `AP_AVG`
- `F107_OBS`
- `F107_DATA_TYPE`
- `F107_OBS_CENTER81`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包括大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数**: `SpaceWeatherDataFile` |
| **类型**: character vector |
| **值**: `'aeroSpaceWeatherData.mat'` | MAT 文件名 |
| **默认值**: `'aeroSpaceWeatherData.mat'` |

### **输入时间设定** — 输入时间格式 `Year, day, sec`（默认） | `Julian date`

输入时间格式，指定为：

- `Year, day, sec` — 通过 **Year**、**DOY** 和 **UT (sec)** 输入端口输入年份、年积日和秒。
- `Julian date` — 通过 **TJD** 输入端口输入儒略日。

#### 编程使用

|  |
| --- |
| **模块参数**: `InputSpec` |
| **类型**: character vector |
| **值**: `'Year, day, sec.'` | `'Julian date'` |
| **默认值**: `'Year, day, sec.'` |

### **F10.7 外推方法** — 用于 `f107Average` 和 `f107Daily` 的外推方法 `None - clip`（默认） | `Constant` | `Least squares fit`

用于在 MAT 文件数据范围之外的时间对 `f107Average` 和 `f107Daily` 进行外推的方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将 `f107Average` 和 `f107Daily` 设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将 `f107Average` 和 `f107Daily` 设置为由 **磁指数外推方法** 参数值指定的常量值。 |
| `Least squares fit` | 使用 1957 年 10 月 1 日至 2040 年 12 月 1 日的空间天气数据的最小二乘拟合来近似 `f107Average` 和 `f107Daily`。此方法使用以下形式的三角函数：  `a + b*cos(c*t + d*sin(e*t))`，  其中：    - *a* 是 `128.2351780622538` - *b* 是 `54.3285872213434` - *c* 是 `0.0015460708364` - *d* 是 `0.2429462096495` - *e* 是 `0.0015563188188` - *t* 是 *jdCurrent* -   *jdReftime* - *jdCurrent* 是当前儒略日 - *jdRef* 是 `2436112.5` |

**注意**

对于 `f107Average` 值，如果 81 天周期的一部分落在空间天气数据的 MAT 文件范围内，则 Solar Flux and Geomagnetic Index 模块使用重叠部分的实际每日值。为计算非重叠部分的平均值，该模块使用裁剪、常量或最小二乘每日值。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包括大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数**: `F107ExtrapMethod` |
| **类型**: character vector |
| **值**: `'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **默认值**: `'None - clip'` |

### **F10.7 外推值** — 要分配给 `f107Average` 并用于计算 `f107Daily` 的外推值 `150.0`（默认） | scalar

要分配给 `f107Average` 并用于计算 `f107Daily` 的外推值，指定为标量。

**可调：** 是

#### 依赖关系

此值在以下情况下赋值：

- **F10.7 外推方法** 设置为 `Constant`。
- 由 **Year**、**DOY** 和 **UT (sec)** 端口指定的时间超出 MAT 文件中数据的范围。

#### 编程使用

|  |
| --- |
| **模块参数**: `F107ExtrapValue` |
| **类型**: character vector |
| **值**: `'150.0'` | scalar |
| **默认值**: `'150.0'` |

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包括大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。
- 将 **F10.7 外推方法** 设置为 `Constant`。

### **磁指数外推方法** — 用于磁指数信息的外推方法 `None - clip`（默认） | `Constant` | `IGRF`

用于在 MAT 文件数据范围之外的时间对磁指数信息值进行外推的方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将磁指数信息的元素设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将磁指数信息的元素设置为由 **磁指数外推方法** 参数指定的常量值。对于此范围之外的时间，磁指数元素基于这些时间界限处的水平磁场强度裁剪值。 |
| `IGRF` | 使用 International Geomagnetic Reference Field 计算磁指数信息的元素。由于此模型定义用于 1900 年 1 月 1 日 12:00 AM UTC 至 2025 年 1 月 1 日 12:00 AM UTC 之间的时间，因此此范围之外的时间的预测值会裁剪到这些时间界限处的值。 |

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包括大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数**: `MagneticIndexExtrapMethod` |
| **类型**: character vector |
| **值**: `'None - clip'` | `'Constant'` | `'IGRF'` |
| **默认值**: `'None - clip'` |

### **磁指数外推值** — 用于计算磁指数元素的外推值 `4.0`（默认） | scalar

用于计算磁指数元素的外推值，指定为标量。

**可调：** 是

#### 依赖关系

当 **磁指数外推方法** 设置为 `Constant` 时，此参数启用。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包括大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数**: `MagneticIndexExtrapValue` |
| **类型**: character vector |
| **值**: `'4.0'` | scalar |
| **默认值**: `'4.0'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

返回太阳通量和地磁指数

Solar Flux and Geomagnetic Index 模块从由 `aeroReadSpaceWeatherData` 函数生成、名为 `aeroSpaceWeatherData.mat` 的 MAT 文件中提取太阳通量和地磁指数。
