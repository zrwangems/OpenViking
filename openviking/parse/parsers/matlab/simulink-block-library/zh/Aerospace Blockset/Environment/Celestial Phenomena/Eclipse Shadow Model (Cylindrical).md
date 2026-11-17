---
type: simulink-block
title: 'Eclipse Shadow Model (Dual Cone)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'eclipseshadowmodeldualcone'
documentation_source_path: 'eclipseshadowmodeldualcone.html'
language: zh-CN
chinese_source: worker-translation
---

# Eclipse Shadow Model (Dual Cone)

## 端口

### 输入

### **Xicrf** — 航天器位置 三元素向量 | *M*×3 数组

航天器相对于 ICRF 坐标系的位置，指定为三元素向量或 *M*×3 数组，其中 *M* 是航天器数量。**Units** 参数控制单位指定。

**数据类型：** `double`

### **TJD** — 儒略日 标量

儒略日，指定为标量。

#### 依赖关系

要启用此端口，请将 **Dialog** 设置为 `Port (Julian date)`。

**数据类型：** `double`

### **T0JD** — 儒略日历元 标量

用于计算经过儒略时间基准的儒略日历元，指定为标量。

#### 依赖关系

要启用此端口，请将 **Dialog** 设置为 `Port (T0 and elapsed Julian time)`。

**数据类型：** `double`

### **ΔTJD** — 相对于 T0JD 的经过儒略时间 标量

相对于 **ΔT**JD 的经过儒略时间，指定为标量经过时间。

#### 依赖关系

要启用此端口，请将 **Dialog** 设置为 `Port (T0 and elapsed Julian time)`。

**数据类型：** `double`

### **Rssbary,cb** — 自定义中心天体位置 3×1 数组

自定义中心天体相对于太阳系质心的位置，在 ICRF 坐标系中。

#### 依赖关系

要启用此端口，请将 **Central body** 设置为 `Custom`。

**数据类型：** `double`
### 输出

### **Fraction** — 可见太阳比例 标量 | *M* 元素向量

可见太阳比例（食），返回为标量或大小为 *M* 的向量。*M* 是输入航天器的数量。

#### 依赖关系

- 当 **Shadow model** 参数设置为 `Dual cone` 时，值为 `0`（本影）、介于 `0` 和 `1` 之间（半影或伪本影）或 `1`（日照）。
- 当 **Shadow model** 参数设置为 `Cylindrical` 时，值为 `0`（本影）或 `1`（日照）。

**数据类型：** `double`

### **Region** — 区域 标量 | *M* 元素向量 | 整数

取决于 **Shadow model** 值的区域，返回为标量或 *M* 元素整数向量。*M* 是航天器数量。

- 当 **Shadow model** 参数设置为 `Dual cone` 时，区域可以为 `0`（本影）、介于 `0` 和 `1` 之间（半影或伪本影）或 `1`（日照）。
- 当 **Shadow model** 参数设置为 `Cylindrical` 时，区域可以为 `0`（本影）或 `1`（日照）。

#### 依赖关系

要启用此端口：

- 选中 **Output index of shadow region** 复选框。

**数据类型：** `int32`

### **Secondary Region** — 次要区域 标量 | *M* 元素向量 | 整数

取决于 **Shadow model** 值的区域，返回为标量或 *M* 元素整数向量。*M* 是航天器数量。

- 当 **Shadow model** 参数设置为 `Dual cone` 时，区域可以为 `0`（本影）、介于 `0` 和 `1` 之间（半影或伪本影）或 `1`（日照）。
- 当 **Shadow model** 参数设置为 `Cylindrical` 时，区域可以为 `0`（本影）或 `1`（日照）。

#### 依赖关系

要启用此端口，请选中 **Output index of shadow region** 复选框以及以下设置之一：

- - 将 **Central body** 设置为 `Earth`。
  - 选中 **Include Moon**。

或：

- - 将 **Central body** 设置为 `Moon`。
  - 选中 **Include Earth**。

**数据类型：** `int32`

## 参数

### **Units** — 位置端口单位 `Metric (m)`（默认）| `Metric (km)` | `English (ft)` | `English (M)`

位置端口单位，指定为以下值之一：

| 单位 | 距离 |
| --- | --- |
| `Metric (m)` | 米 |
| `Metric (km)` | 千米 |
| `English (ft)` | 英尺 |
| `English (M)` | 英里 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (m)'` | `'Metric (km)'` | `'English (ft)'` | `'English (M)'` |
| **默认值**：`'Metric (m)'` |

### **Shadow model** — 阴影模型 `Dual cone`（默认）| `Cylindrical`

用于食计算的阴影模型，指定为以下值之一。

- `Cylindrical` — Fraction 可以为 0.0（本影）或 1.0（日照）。
- `Dual cone` — Fraction 可以为 0.0（本影）、介于 0.0 和 1.0 之间（半影或伪本影）或 1.0（日照）。

#### 编程使用

|  |
| --- |
| **模块参数**：`shadowModel` |
| **类型**：character vector |
| **值**：`'Dual cone'` | `'Cylindrical'` |
| **默认值**：`'Dual cone'` |

### **Output index of shadow region** — 阴影区域索引输出 `on`（默认）| `off`

要启用阴影区域索引端口，请选中此复选框。否则，清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`outputShadowRegion` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Time source** — 时间源方法 `Dialog`（默认）| `Port (Julian date)` | `Port (T0 and elapsed Julian time)`

时间源方法，指定为以下值之一：

- `Dialog` — 模块对话框参数。
- `Port (Julian date)` — **T**JD 端口。
- `Port (T0 and elapsed Julian time)` — **T**JD 和 **ΔT**JD 端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`timeSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Port (Julian date)'` | `'Port (T0 and elapsed Julian time)'` |
| **默认值**：`'Dialog'` |

### **Start date/time (JD)** — 仿真的初始开始日期和时间 `juliandate(2020, 1, 1)`（默认）| 有效标量儒略日

仿真的初始开始日期和时间，指定为有效标量儒略日。为确定每个仿真时间步的当前时间，模块将经过的仿真时间添加到此值。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

#### 依赖关系

要启用此参数，请将 **Time source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`startDate` |
| **类型**：character vector |
| **值**：`'juliandate(2020, 1, 1)'` | valid scalar Julian date |
| **默认值**：`'juliandate(2020, 1, 1)'` |

### **Central body** — 用于食计算的遮蔽天体 `Earth`（默认）| `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

用于食计算的遮蔽天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune` 或 `Custom`。

位置输入参考中心天体的原点。

#### 编程使用

|  |
| --- |
| **模块参数**：`centralBody` |
| **类型**：character vector |
| **值**：`'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` | |
| **默认值**：`'Earth'` |

### **Equatorial radius** — 自定义中心天体半径 `3396200`（默认）| double 标量

自定义中心天体的赤道半径，指定为以 **Units** 参数中指定的单位表示的 double 标量。

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`customR` |
| **类型**：character vector |
| **值**：`'3396200'` | double scalar |
| **默认值**：`'3396200'` |

### **Include Moon** — 包含 Moon 的选项 `on`（默认）| `off`

当中心天体为 Earth 时，在食计算中将 Moon 作为次要遮蔽天体的选项。

#### 依赖关系

将 **Central body** 参数设置为 `Earth`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeMoon` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Include Earth** — 包含 Earth 的选项 `on`（默认）| `off`

当中心天体为 Moon 时，在食计算中将 Earth 作为次要遮蔽天体的选项。

#### 依赖关系

将 **Central body** 参数设置为 `Moon`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeEarth` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择由 Jet Propulsion Laboratory 定义的这些星历模型之一。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 1998 年发布。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame 1.0 版本。 |
| `DE421` | 2008 年发布。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame 1.0 版本。 |
| `DE423` | 2010 年发布。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame 2.0 版本。 |
| `DE430` | 2013 年发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame 2.0 版本。 |
| `DE432t` | 2014 年 4 月发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame 2.0 版本。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® 命令窗口中键入 `aeroDataPackage`。在 MATLAB 桌面工具栏中，点击 **Add-Ons**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ephemerisModel` |
| **类型**：character vector |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**：`'DE405'` |

### **Limit ephemerides date range** — 打开以启用星历数据的范围开始和结束 `on`（默认）| `off`

控制仿真期间加载到内存中的数据量以及为模块生成的代码中包含的数据量：

- 清除此复选框以包含星历模型表中定义的完整日期范围的数据。
- 选中此复选框以将星历数据的加载限制在指定的日期范围内。

#### 编程使用

|  |
| --- |
| **模块参数**：`useDateRange` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` | |
| **默认值**：`'on'` |

### **Start date (JD)** — 星历日期范围的开始日期 `juliandate(2020, 1, 1)`（默认）| 儒略日

星历日期范围的开始日期，指定为儒略日。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 选中 **Limit ephemerides date range** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`startDate` |
| **类型**：character vector |
| **值**：`'juliandate(2020, 1, 1)'` | Julian date |
| **默认值**：`'juliandate(2020, 1, 1)'` |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)`（默认）| 儒略日

星历日期范围的结束日期，指定为儒略日。

#### 依赖关系

要启用此参数，请选中 **Limit ephemerides date range** 复选框。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 将 **Limit ephemerides date range** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`endDate` |
| **类型**：character vector |
| **值**：`'juliandate(2050, 1, 1)'` | Julian format date |
| **默认值**：`'juliandate(2050, 1, 1)'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `Error`（默认）| `Warning` | `None`

超出范围时的模块行为，指定为以下值之一：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `off`（默认）| `on`

选择以启用零交叉检测，允许 Eclipse Shadow Model (Dual Cone) 在进入和退出食时识别零交叉。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **Parameter:** `zeroCrossing` |
| **类型**：character vector, string |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：`Eclipse Shadow Model (Dual Cone)` 模块变更

Eclipse Shadow Model (Dual Cone) 和 Eclipse Shadow Model (Cylindrical) 模块现在支持零交叉检测。此变更使模块能够识别零交叉进入和退出食的时间。

## 描述

计算惯性位置处可见太阳圆盘的比例

Eclipse Shadow Model (Dual Cone) 模块计算从提供的惯性位置可见的太阳圆盘比例，假设被遮蔽天体和太阳均为球形。该模块使用两种阴影模型：

双锥模型 — 该模块区分偏食、环食和全食，这意味着航天器可以处于日照、半影、伪本影或本影中。在半影中食为偏食，在伪本影中为环食，在本影中为全食。总结如下：

- 本影，无日照 — 0
- 半影或伪本影，部分日照 — 0 到 1
- 全日照 — 1

圆柱模型 — 该模块仅区分全食（本影）和全日照。有关详细信息，请参阅 Alternative Configurations 部分。

- 本影，无日照 — 0
- 全日照 — 1
