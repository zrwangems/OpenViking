---
type: simulink-block
title: 'Planetary Ephemeris'
family: 'aeroblks'
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
```yaml
ports:
- name: TJD
  summary: 儒略日 标量 | 正值 | 介于最小和最大儒略日之间
  direction: input
  data_types: double
- name: T0JD
  summary: 固定儒略日 标量 | 正值
  direction: input
  data_types: double
- name: ΔTJD
  summary: 经过的儒略时间 标量 | 正值
  direction: input
  data_types: double
- name: Xicrf1
  summary: 质心位置矢量
  direction: output
  data_types: double
- name: Vicrf
  summary: 速度矢量
  direction: output
  data_types: double
```

### 输入

### **TJD** — 儒略日 标量 | 正值 | 介于最小和最大儒略日之间

儒略日，指定为介于最小和最大儒略日之间的正标量。

以质心力学时（TDB）指定儒略日。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `Julian date`，则显示此端口。

**数据类型：** `double`

### **T0JD** — 固定儒略日 标量 | 正值

特定历元的固定儒略日，该历元是插值历元当天或之前最近的午夜，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

以质心力学时（TDB）指定儒略日。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`

### **ΔTJD** — 经过的儒略时间 标量 | 正值

固定儒略日与星历时间之间经过的儒略时间，指定为正标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`
### 输出

### **Xicrf1** — 质心位置矢量

**Target** 对象相对于 **Center** 对象质心的质心位置（*X*icrf1），以矢量形式输出，单位为 km 或天文单位（AU）。

**提示**

此模块输出国际天球参考框架（ICRF）坐标下的质心位置。要将这些坐标转换为地心地固（ECEF）坐标，请使用 Direction Cosine Matrix ECI to ECEF 模块。

**数据类型：** `double`

### **Vicrf** — 速度矢量

**Target** 对象质心相对于 **Center** 对象质心的速度（*V*icrf），指定为矢量，单位为 km/s 或天文单位（AU）/天。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输出单位 km,km/s（默认）| AU,AU/day
  group: ''
  block_parameter: units
  type: 字符向量
  values: m,m/s | km,km/s | AU,AU/day
  default: '''km,km/s'''
- name: Epoch
  summary: 历元 Julian date（默认）| T0 and elapsed Julian time
  group: ''
  block_parameter: epochFormat
  type: 字符向量
  values: Julian date | T0 and elapsed Julian time
  default: '''Julian date'''
- name: Ephemeris model
  summary: 星历模型 DE405（默认）| DE421 | DE423 | DE430 | DE432t
  group: ''
  block_parameter: ephemerisModel
  type: 字符向量
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Ephemeris model
  summary: 星历模型 DE405（默认）| DE421 | DE423 | DE430 | DE432t
  group: ''
  block_parameter: ephemerisModel
  type: 字符向量
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Center
  summary: 中心天体 Sun（默认）| Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system
    barycenter | Earth-Moon barycenter
  group: ''
  block_parameter: center
  type: 字符向量
  values: Sun | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system barycenter
    | Earth-Moon barycenter
  default: '''Sun'''
- name: Target
  summary: 目标天体 Sun（默认）| Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system
    barycenter | Earth-Moon barycenter
  group: ''
  block_parameter: target
  type: 字符向量
  values: Sun | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system barycenter
    | Earth-Moon barycenter
  default: '''Moon'''
- name: Limit ephemerides date range
  summary: 用于启用星历数据范围起止的选项 off（默认）| on
  group: ''
  block_parameter: useDateRange
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Start date (JD)
  summary: 星历日期范围的起始日期 juliandate(2020, 1, 1)（默认）| 儒略日
  group: ''
  block_parameter: startDate
  type: 字符向量
  values: '''juliandate(2020, 1, 1)'' | 儒略日'
  default: '''juliandate(2020, 1, 1)'''
- name: End date (JD)
  summary: 星历日期范围的结束日期 juliandate(2050, 1, 1)（默认）| 儒略日
  group: ''
  block_parameter: endDate
  type: 字符向量
  values: '''juliandate(2050, 1, 1)'' | 儒略格式日期'
  default: '''juliandate(2050, 1, 1)'''
- name: Action for out-of-range input
  summary: 超出范围时的模块行为 None（默认）| Warning | Error
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Calculate velocity
  summary: 计算目标质心速率 on（默认）| off
  group: ''
  block_parameter: outputVelocity
  type: 字符向量
  values: '''off'' | ''on'' |'
  default: '''on'''
```

### **Units** — 输出单位 `km,km/s`（默认）| `AU,AU/day`

输出单位，指定为 `km,km/s` 或 `AU,AU/day`。

| 单位 | 位置 | 速度 |
| --- | --- | --- |
| `m,m/s` | m | m/s |
| `km,km/s` | km | km/s |
| `Au,AU/day` | 天文单位（AU） | AU/day |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`m,m/s` | `km,km/s` | `AU,AU/day` |
| **默认值**：`'km,km/s'` |

### **Epoch** — 历元 `Julian date`（默认）| `T0 and elapsed Julian time`

历元，指定为：

- `Julian date`

  用于实现 **Target** 对象位置和速度的儒略日。选择此选项时，模块有一个输入端口 *TJD*。
- `T0 and elapsed Julian time`

  由两个模块输入指定的儒略日：

  - 表示起始历元的固定儒略日。
  - 固定儒略日（*T0JD*）与所需模型仿真时间之间经过的儒略时间。*T0JD* 与 Δ*TJD* 之和必须介于最小和最大儒略日之间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`epochFormat` |
| **类型**：字符向量 |
| **值**：`Julian date` | `T0 and elapsed Julian time` |
| **默认值**：`'Julian date'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择由喷气推进实验室定义的这些星历模型之一。该模块使用星历数据计算三体质点引力和太阳辐射压力所需的相对天体位置。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 1998 年发布。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块实现这些星历相对于 1998 年采用的国际天球参考框架 1.0 版。 |
| `DE421` | 2008 年发布。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块实现这些星历相对于 1998 年采用的国际天球参考框架 1.0 版。 |
| `DE423` | 2010 年发布。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |
| `DE430` | 2013 年发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |
| `DE432t` | 2014 年 4 月发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® 命令窗口中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ephemerisModel` |
| **类型**：字符向量 |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**：`'DE405'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择由喷气推进实验室定义的这些星历模型之一。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 1998 年发布。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块实现这些星历相对于 1998 年采用的国际天球参考框架 1.0 版。 |
| `DE421` | 2008 年发布。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块实现这些星历相对于 1998 年采用的国际天球参考框架 1.0 版。 |
| `DE423` | 2010 年发布。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |
| `DE430` | 2013 年发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |
| `DE432t` | 2014 年 4 月发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的国际天球参考框架 2.0 版。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB 命令窗口中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ephemerisModel` |
| **类型**：字符向量 |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**：`'DE405'` |

### **Center** — 中心天体 `Sun`（默认）| `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

中心天体（天文对象）或参考天体，指定为 **Target** 质心位置和速度测量的参考点。

#### 程序化使用

|  |
| --- |
| **模块参数**：`center` |
| **类型**：字符向量 |
| **值**：`Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **默认值**：`'Sun'` |

### **Target** — 目标天体 `Sun`（默认）| `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

目标天体（天文对象）或参考天体，指定为质心位置和速度测量的参考点。

#### 程序化使用

|  |
| --- |
| **模块参数**：`target` |
| **类型**：字符向量 |
| **值**：`Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **默认值**：`'Moon'` |

### **Limit ephemerides date range** — 用于启用星历数据范围起止的选项 `off`（默认）| `on`

控制仿真期间加载到内存中的数据量以及模块生成代码中包含的数据量：

- 选中此复选框可将星历数据的加载限制在指定的日期范围内。
- 清除此复选框可包含 **Ephemeris model** 表中定义的完整日期范围的数据。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`useDateRange` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Start date (JD)** — 星历日期范围的起始日期 `juliandate(2020, 1, 1)`（默认）| 儒略日

星历日期范围的起始日期，指定为儒略日。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 选中 **Limit ephemerides date range** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`startDate` |
| **类型**：字符向量 |
| **值**：`'juliandate(2020, 1, 1)'` | 儒略日 |
| **默认值**：`'juliandate(2020, 1, 1)'` |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)`（默认）| 儒略日

星历日期范围的结束日期，指定为儒略日。

#### 依赖关系

要启用此参数，请选中 **Limit ephemerides date range** 复选框。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 将 **Limit ephemerides date range** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`endDate` |
| **类型**：字符向量 |
| **值**：`'juliandate(2050, 1, 1)'` | 儒略格式日期 |
| **默认值**：`'juliandate(2050, 1, 1)'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 诊断查看器中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### **Calculate velocity** — 计算目标质心速率 `on`（默认）| `off`

选中此复选框可计算 **Target** 质心相对于 **Center** 质心的速度。

#### 程序化使用

|  |
| --- |
| **模块参数**：`outputVelocity` |
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

### R2023a：Planetary Ephemeris 模块控制星历数据范围

您现在可以使用以下新参数控制 Planetary Ephemeris 的星历数据范围：

- **Limit ephemerides date range** — 选中此复选框可启用星历数据范围的起始和结束。
- **Start data** — 输入星历数据范围的起始日期。**Epoch** 参数会影响此日期格式。
- **End data** — 输入星历数据范围的结束日期。**Epoch** 参数会影响此日期格式。

## 描述

实现天文对象的位置和速度

Planetary Ephemeris 模块使用切比雪夫系数实现目标对象相对于指定中心对象在给定儒略日的位置和速度。**Target** 参数指定天文对象。该模块使用 **Center** 参数指定的天文对象作为参考来实现星历。

该模块使用 NASA 喷气推进实验室提供的切比雪夫系数。

**提示**

对于 `TJD`，模块的儒略日输入：

- 使用 Julian Date Conversion 模块或 Aerospace Toolbox 的 `juliandate` 函数计算日期。
- 使用其他方法计算儒略日，并使用 Constant 模块输入。

此模块使用国际天球参考框架实现位置和速度。如果您需要地球固连（ECEF）坐标下相对于地球的行星星历位置值，请使用 Direction Cosine Matrix ECI to ECEF 模块。
