---
type: simulink-block
title: 'Planetary Ephemeris'
family: 'environment'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'planetaryephemeris'
documentation_source_path: 'planetaryephemeris.html'
language: zh-CN
chinese_source: worker-translation
---

# Planetary Ephemeris

## 端口

### 输入

### **TJD** — 儒略日标量 | 正值 | 介于最小和最大儒略日之间

儒略日，指定为介于最小和最大儒略日之间的正标量。

以质心动力学时（TDB）指定儒略日。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖项

如果 **Epoch** 参数设置为 `Julian date`，则显示此端口。

**数据类型：** `double`

### **T0JD** — 固定儒略日标量 | 正值

特定历元的固定儒略日，该历元为插值历元当天或之前最近的午夜，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

以质心动力学时（TDB）指定儒略日。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖项

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`

### **ΔTJD** — 经过的儒略时间标量 | 正值

固定儒略日与星历时间之间经过的儒略时间，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖项

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`
### 输出

### **Xicrf1** — 质心位置向量

**Target** 对象的质心位置（*X*icrf1）相对于 **Center** 对象的质心，以向量形式输出，单位为 km 或 astronomical units (AU)。

**提示**

此模块以 International Celestial Reference Frame (ICRF) 坐标输出质心位置。要将这些坐标转换为 Earth-centered Earth-fixed (ECEF)，请使用 Direction Cosine Matrix ECI to ECEF block。

**数据类型：** `double`

### **Vicrf** — 速度向量

**Target** 对象质心的速度（*V*icrf）相对于 **Center** 对象的质心，指定为向量，单位为 km/s 或 astronomical units (AU)/day。

**数据类型：** `double`

## 参数

### **Units** — 输出单位 `km,km/s`（默认）| `AU,AU/day`

输出单位，指定为 `km,km/s` 或 `AU,AU/day`。

| 单位 | 位置 | 速度 |
| --- | --- | --- |
| `m,m/s` | m | m/s |
| `km,km/s` | km | km/s |
| `Au,AU/day` | astronomical units (AU) | AU/day |

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `m,m/s` | `km,km/s` | `AU,AU/day` |
| **默认值**: `'km,km/s'` |

### **Epoch** — 历元 `Julian date`（默认）| `T0 and elapsed Julian time`

历元，指定为：

- `Julian date`

  儒略日，用于实现 **Target** 对象的位置和速度。当选择此选项时，模块有一个输入端口 *TJD*。
- `T0 and elapsed Julian time`

  儒略日，由两个模块输入指定：

  - 表示起始历元的固定儒略日。
  - 固定儒略日（*T0JD*）与所需模型仿真时间之间经过的儒略时间。*T0JD* 与 Δ*TJD* 之和必须介于最小和最大儒略日之间。

#### 程序化使用

|  |
| --- |
| **模块参数**: `epochFormat` |
| **类型**: character vector |
| **值**: `Julian date` | `T0 and elapsed Julian time` |
| **默认值**: `'Julian date'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择 Jet Propulsion Laboratory 定义的这些星历模型之一。该模块使用星历数据来计算第三体点质量引力和太阳辐射压力所需的相对天体位置。

| **Ephemeris Model** | 描述 |
| --- | --- |
| `DE405` | 1998 年发布。此星历考虑儒略日范围 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE421` | 2008 年发布。此星历考虑儒略日范围 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE423` | 2010 年发布。此星历考虑儒略日范围 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE430` | 2013 年发布。此星历考虑儒略日范围 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE432t` | 2014 年 4 月发布。此星历考虑儒略日范围 2287184.5,（1549 年 12 月 21 日）至 2688976.5,（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |

**注意**

此模块要求使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 依赖项

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ephemerisModel` |
| **类型**: character vector |
| **值**: `DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**: `'DE405'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择 Jet Propulsion Laboratory 定义的这些星历模型之一。

| **Ephemeris Model** | 描述 |
| --- | --- |
| `DE405` | 1998 年发布。此星历考虑儒略日范围 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE421` | 2008 年发布。此星历考虑儒略日范围 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE423` | 2010 年发布。此星历考虑儒略日范围 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE430` | 2013 年发布。此星历考虑儒略日范围 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE432t` | 2014 年 4 月发布。此星历考虑儒略日范围 2287184.5,（1549 年 12 月 21 日）至 2688976.5,（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |

**注意**

此模块要求使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ephemerisModel` |
| **类型**: character vector |
| **值**: `DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**: `'DE405'` |

### **Center** — 中心天体 `Sun`（默认）| `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

中心天体（天文对象）或参考天体，指定为用于 **Target** 质心位置和速度测量的参考点。

#### 程序化使用

|  |
| --- |
| **模块参数**: `center` |
| **类型**: character vector |
| **值**: `Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **默认值**: `'Sun'` |

### **Target** — 目标天体 `Sun`（默认）| `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

目标天体（天文对象）或参考天体，指定为用于质心位置和速度测量的参考点。

#### 程序化使用

|  |
| --- |
| **模块参数**: `target` |
| **类型**: character vector |
| **值**: `Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **默认值**: `'Moon'` |

### **Limit ephemerides date range** — 用于启用星历数据范围开始和结束的选项 `off`（默认）| `on`

控制在仿真期间加载到内存中的数据量以及为模块生成的代码中包含的数据量：

- 选中此复选框，以将星历数据的加载限制在指定日期范围。
- 清除此复选框，以包含 **Ephemeris model** 表中定义的完整日期范围的数据。

#### 依赖项

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `useDateRange` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **Start date (JD)** — 星历日期范围的开始日期 `juliandate(2020, 1, 1)`（默认）| Julian date

星历日期范围的开始日期，指定为儒略日。

#### 依赖项

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 选择 **Limit ephemerides date range** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数**: `startDate` |
| **类型**: character vector |
| **值**: `'juliandate(2020, 1, 1)'` | Julian date |
| **默认值**: `'juliandate(2020, 1, 1)'` |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)`（默认）| Julian date

星历日期范围的结束日期，指定为儒略日。

#### 依赖项

要启用此参数，请选中 **Limit ephemerides date range** 复选框。

#### 依赖项

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 将 **Limit ephemerides date range** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `endDate` |
| **类型**: character vector |
| **值**: `'juliandate(2050, 1, 1)'` | Julian format date |
| **默认值**: `'juliandate(2050, 1, 1)'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

### **Calculate velocity** — 计算目标质心速率 `on`（默认）| `off`

选中此复选框以计算 **Target** 质心相对于 **Center** 质心的速度。

#### 程序化使用

|  |
| --- |
| **模块参数**: `outputVelocity` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` | |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

### R2023a: Planetary Ephemeris 模块控制星历数据范围

现在可以使用以下新参数控制 Planetary Ephemeris 的星历数据范围：

- **Limit ephemerides date range** — 选中此复选框以启用星历数据范围的开始和结束。
- **Start data** — 输入星历数据范围的开始日期。**Epoch** 参数会影响此日期格式。
- **End data** — 输入星历数据范围的结束日期。**Epoch** 参数会影响此日期格式。

## 描述

实现天文对象的位置和速度

Planetary Ephemeris 模块使用 Chebyshev 系数实现给定儒略日下目标对象相对于指定中心对象的位置和速度。**Target** 参数指定一个天文对象。该模块使用 **Center** 参数指定的天文对象作为参考来实现星历。

该模块使用 NASA Jet Propulsion Laboratory 提供的 Chebyshev 系数。

**提示**

对于 `TJD`，模块的儒略日输入：

- 使用 Julian Date Conversion block 或 Aerospace Toolbox `juliandate` 函数计算日期。
- 使用其他方法计算儒略日，并使用 Constant block 输入。

此模块使用 International Celestial Reference Frame 实现位置和速度。如果需要 Earth-fixed (ECEF) 坐标中相对于地球的行星历位置值，请使用 Direction Cosine Matrix ECI to ECEF block。
