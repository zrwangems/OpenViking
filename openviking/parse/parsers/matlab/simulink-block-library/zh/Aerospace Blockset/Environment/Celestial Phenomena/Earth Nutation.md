---
type: simulink-block
title: 'Earth Nutation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'earthnutation'
documentation_source_path: 'earthnutation.html'
language: zh-CN
chinese_source: worker-translation
---

# Earth Nutation

## 端口

### 输入

### **TJD** — 儒略日 标量 | 正值 | 介于最小和最大儒略日之间

儒略日，指定为介于最小和最大儒略日之间的正标量。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `Julian date`，则此端口显示。

**数据类型：** `double`

### **T0JD** — 固定儒略日 标量 | 正值

特定历元的固定儒略日，该历元为插值历元当天或之前最近的午夜，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则此端口显示。

**数据类型：** `double`

### **ΔTJD** — 经过的儒略时间 标量 | 正值

固定儒略日与星历时间之间经过的儒略时间，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则此端口显示。

**数据类型：** `double`
### 输出

### **Δψ Δε (rad)** — 地球章动 向量

地球章动，以经度（Δψ）和倾角（Δε）的向量形式输出，单位为 rad。

**数据类型：** `double`

### **Δψ dot Δεdot (rad/day)** — 地球章动角速率 标量

经度（Δψ dot）和倾角（Δε dot）的地球章动角速率，指定为标量，单位为 rad/day。

#### 依赖关系

如果选中 **Calculate rates** 参数，则此端口显示。

**数据类型：** `double`

## 参数

### **Epoch** — 历元 `Julian date`（默认）| `T0 and elapsed Julian time`

历元，指定为：

- `Julian date`

  用于计算地球章动的儒略日。选择此选项时，模块具有一个输入端口 *TJD*。
- `T0 and elapsed Julian time`

  由两个模块输入指定的儒略日：

  - 表示起始历元的固定儒略日。
  - *T0JD* 与所需模型仿真时间之间经过的儒略时间。*T0JD* 与 Δ*TJD* 之和必须介于最小和最大儒略日之间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`epochflag` |
| **类型**：字符向量 |
| **值**：`Julian date` | `T0 and elapsed Julian time` |
| **默认值**：`'Julian date'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430`

从 Jet Propulsion Laboratory 定义的列表中选择星历模型：

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 于 1998 年发布。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame 1.0 版的结果。 |
| `DE421` | 于 2008 年发布。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame 1.0 版的结果。 |
| `DE423` | 于 2010 年发布。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame 2.0 版的结果。 |
| `DE430` | 于 2013 年发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame 2.0 版的结果。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® 命令窗口中键入 `aeroDataPackage`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`de` |
| **类型**：字符向量 |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**：`'DE405'` |

### **Action for out-of-range input** — 超出范围输入时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围输入时的模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 不执行任何操作。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | 在 Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`errorflag` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |

### **Calculate rates** — 计算地球章动速率 `on`（默认）| `off`

通过选中此复选框计算地球章动速率。

#### 依赖关系

选中此复选框可显示 *Δψ dot Δεdot* 端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`velflag` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` | |
| **默认值**：`'on'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

实现地球章动

Earth Nutation 模块针对给定儒略日实现 International Astronomical Union (IAU) 1980 章动序列。该模块使用 NASA Jet Propulsion Laboratory 提供的 Chebyshev 系数。

**Epoch** 参数控制模块输入的数量。如果选择 `Julian date`，则模块具有一个输入端口；如果选择 `T0 and elapsed Julian time`，则模块具有两个输入端口。

**提示**

对于模块的 `TJD` 儒略日输入：

- 使用 Julian Date Conversion 模块或 Aerospace Toolbox 的 `juliandate` 函数计算日期。
- 使用其他方法计算儒略日，并使用 Constant 模块输入。
