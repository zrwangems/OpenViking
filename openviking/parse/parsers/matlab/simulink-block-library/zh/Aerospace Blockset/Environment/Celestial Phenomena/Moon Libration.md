---
type: simulink-block
title: 'Moon Libration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'moonlibration'
documentation_source_path: 'moonlibration.html'
language: zh-CN
chinese_source: worker-translation
---

# Moon Libration

## 端口

### 输入

### **TJD** — 儒略日标量 | 正值 | 介于最小和最大儒略日之间

儒略日，指定为介于最小和最大儒略日之间的正值标量。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `Julian date`，则显示此端口。

**数据类型：** `double`

### **T0JD** — 固定儒略日标量 | 正值

特定历元的固定儒略日，该历元为在插值历元当天或之前的最接近午夜，指定为正值标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`

### **ΔTJD** — 经过的儒略时间标量 | 正值

固定儒略日与星历时间之间经过的儒略时间，指定为正值标量。*T0JD* 与 *ΔTJD* 之和必须介于最小和最大儒略日之间。

有关最小和最大儒略日，请参阅 **Ephemeris model** 参数。

#### 依赖关系

如果 **Epoch** 参数设置为 `T0 and elapsed Julian time`，则显示此端口。

**数据类型：** `double`
### 输出

### **φ θ ψ (rad)** — 欧拉角向量

月球姿态的欧拉角 (φ θ ψ)，单位为 rad。

**数据类型：** `double`

### **ω (rad/day)** — 月球天平动欧拉角速率向量

月球天平动欧拉角速率 (ω)，单位为 rad/day。

**数据类型：** `double`

## 参数

### **Epoch** — 历元 `Julian date` (默认) | `T0 and elapsed Julian time`

历元，指定为：

- `Julian date`

  用于计算月球天平动的儒略日。选择此选项时，模块有一个输入端口 *TJD*。
- `T0 and elapsed Julian time`

  儒略日，由两个模块输入指定：

  - 表示起始历元的固定儒略日。
  - 固定儒略日 (*T0JD*) 与所需模型仿真时间之间经过的儒略时间。*T0JD* 与 Δ*TJD* 之和必须介于最小和最大儒略日之间。

#### 程序化使用

|  |
| --- |
| **模块参数**: `epochflag` |
| **类型**: character vector |
| **值**: `Julian date` | `T0 and elapsed Julian time` |
| **默认值**: `'Julian date'` |

### **Ephemeris model** — 星历模型 `DE405` (默认) | `DE421` | `DE423` | `DE430` | `DE432t`

从 Jet Propulsion Laboratory 定义的这些星历模型中选择一个。该模块使用星历数据计算第三体点质量引力和太阳辐射压力所需的相对天体位置。

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | 发布于 1998 年。该星历考虑儒略日范围 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。该模块按照 1998 年采用的国际天球参考框架 1.0 版实现这些星历。 |
| `DE421` | 发布于 2008 年。该星历考虑儒略日范围 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。该模块按照 1998 年采用的国际天球参考框架 1.0 版实现这些星历。 |
| `DE423` | 发布于 2010 年。该星历考虑儒略日范围 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。该模块按照 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |
| `DE430` | 发布于 2013 年。该星历考虑儒略日范围 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。该模块按照 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |
| `DE432t` | 发布于 2014 年 4 月。该星历考虑儒略日范围 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。该模块按照 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ephemerisModel` |
| **类型**: character vector |
| **值**: `DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**: `'DE405'` |

### **Action for out-of-range input** — 越界模块行为 `None` (默认) | `Warning` | `Error`

越界模块行为，指定如下。

| Action | Description |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` (默认) | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `errorflag` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Error'` |

### **Calculate rates** — 计算月球天平动速率 `on` (默认) | `off`

选择以计算月球天平动速率。

#### 依赖关系

选中此复选框以显示 *ω* 端口。

#### 程序化使用

|  |
| --- |
| **模块参数**: `velflag` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` | |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

实现月球天平动

Moon Libration 模块使用切比雪夫系数或给定儒略日实现月球天平动。该模块使用 NASA Jet Propulsion Laboratory 提供的切比雪夫系数。

**提示**

对于 `TJD`（模块的儒略日输入）：

- 使用 Julian Date Conversion 模块或 Aerospace Toolbox 的 `juliandate` 函数计算日期。
- 使用其他方法计算儒略日，并使用 Constant 模块输入该儒略日。
