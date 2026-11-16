---
type: simulink-block
title: 'Line of Sight Access'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'lineofsightaccess'
documentation_source_path: 'lineofsightaccess.html'
language: zh-CN
chinese_source: worker-translation
---

# Line of Sight Access

## 端口

### 输入

### **TJD** — 儒略日标量

以 UTC（Universal Coordinated Time）表示的儒略日，指定为标量。

#### 依赖项

要启用此端口，请将 **Time source** 设置为 `Port
(Julian date)`。

**数据类型：** `double`

### **T0JD** — 儒略日历元标量

用作经过的儒略时间基准的儒略日历元，以 UTC（Universal Coordinated Time）表示，指定为标量。

#### 依赖项

要启用此端口，请将 **Time source** 设置为 `Port
(T0 and elapsed Julian time)`。

**数据类型：** `double`

### **ΔTJD** — 相对于 T0JD 的经过儒略时间标量

相对于 **ΔT**JD 的经过儒略时间，以 UTC（Universal Coordinated Time）表示，指定为经过时间的标量。

#### 依赖项

要启用此端口，请将 **Time source** 设置为 `Port
(Julian date)`。

**数据类型：** `double`

### **Src *`position`*** — 源位置 3 元素向量 | 4 元素向量 | *M*×3 数组 | *M*×4 数组

源位置（例如航天器的位置）相对于源中心天体，指定为 3 元素向量或 *M*×3 数组。*`position`* 可以是 **Xicrf**、**Xff** 或 **LLA**，具体取决于 **Source** 选项卡上的 **Position coordinate frame** 设置。

#### 依赖项

当将源位置指定为 *M*×3 数组时，还必须将目标位置指定为 *M*×3 数组。

**数据类型：** `double`

### **Src *`attitude`*** — 源姿态 3 元素向量 | *M*×3 数组

源姿态，定义为从 **Source** 选项卡上的 **Attitude reference coordinate frame** 参数到本体坐标系在当前时间步的旋转，指定为以下值之一：

- 4 元素向量 — **Attitude representation** 设置为 `Quaternion`。
- 3 元素向量 — **Attitude representation** 设置为 `Euler angles`。

*`attitude`* 可以是 **q** 或 **[R1, R2, R3]**，具体取决于 **Source** 选项卡上的 **Attitude representation** 设置。

#### 依赖项

- 要启用此端口，请在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。
- 当将源姿态指定为 *M*×3 数组时，还必须将目标姿态指定为 *M*×3 数组。

**数据类型：** `double`

### **Src FOV *`orientation`*** — 源视场方向 4 元素向量 | 3 元素向量

源视场方向，定义为从本体坐标系到传感器坐标系的旋转，指定为以下值之一：

- 4 元素向量 — **Attitude representation** 设置为 `Quaternion`。
- 3 元素向量 — **Attitude representation** 设置为 `Euler angles`。

*`orientation`* 可以是 **q** 或 **[R1, R2, R3]**，具体取决于 **Source** 选项卡上的 **Attitude representation** 设置。

#### 依赖项

要启用此端口，

- 在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。
- 将 **Source FOV orientation source** 设置为 `Port`。

当将源 FOV 方向指定为 *M*×3 数组时，还必须将目标 FOV 方向指定为 *M*×3 数组。

### **Tgt *`position`*** — 目标位置 3 元素向量 | *M*×3 数组

一个或多个目标位置，指定为 3 元素向量或 *M*×3 数组。*`position`* 可以是 **Xicrf**、**Xff** 或 **LLA**，具体取决于 **Source** 选项卡上的 **Position coordinate frame** 设置。

#### 依赖项

当将源位置指定为 *M*×3 数组时，还必须将目标位置指定为 *M*×3 数组。但是，如果源位置是 3 元素向量，则目标位置可以具有任意行数（*M*×3）。

**数据类型：** `double`

### **Tgt *`attitude`*** — 目标姿态 3 元素向量 | *M*×3 数组

一个或多个目标姿态，指定为 3 元素向量或 *M*×3 数组。*`attitude`* 可以是 **q** 或 **[R1, R2, R3]**，具体取决于 **Source** 选项卡上的 **Attitude representation** 设置。

#### 依赖项

当将源姿态指定为 *M*×3 数组时，还必须将目标姿态指定为 *M*×3 数组。

**数据类型：** `double`

### **Tgt FOV *`orientation`*** — 目标视场方向 4 元素向量 | 3 元素向量

目标视场方向，定义为从本体坐标系到传感器坐标系的旋转，指定为以下之一：

- 4 元素向量 — **Attitude representation** 设置为 `Quaternion`。
- 3 元素向量 — **Attitude representation** 设置为 `Euler angles`。

*`orientation`* 可以是 **q** 或 **[R1, R2, R3]**，具体取决于 **Source** 选项卡上的 **Attitude representation** 设置。

#### 依赖项

要启用此端口，

- 在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。
- 将 **Source FOV orientation source** 设置为 `Port`。

当将源姿态指定为 *M*×3 数组时，还必须将目标中心天体指定为 *M*×3 数组。

### **Rssbary,cb** — 自定义中心天体位置 3×1 数组

自定义中心天体相对于太阳系质心的位置，在 ICRF 坐标系中。**cb** 可以是 **cb**src 或 **cb**tgt，具体取决于 **Source** 或 **Target** 选项卡上的 **Central body** 是否设置为 `Custom`。

#### 依赖项

要在 **Source** 或 **Target** 选项卡上启用此端口，请将 **Central body** 设置为 `Custom`。

**数据类型：** `double`

### **φθψ** — Moon 天平动角 3 元素向量

用于在国际天球参考系 (ICRF) 与以 Moon 为中心的固定坐标系之间转换的 Moon 天平动角，指定为 3 元素向量。要获取这些值，请使用 Moon Libration 模块。

**注意**

当 **Source** 或 **Target** 选项卡上的 **Central body** 设置为 `Moon` 时，此模块使用的固定坐标系是平地球/极轴 (ME) 系统。有关详细信息，请参阅算法。

#### 依赖项

要启用此端口：

- 在 **Source** 或 **Target** 选项卡上，将 **Central body** 设置为 `Moon`。
- 选择 **Input Moon libration angles** 参数。

**数据类型：** `double`

### 输出

### **Access** — 总组合视线访问状态 `0` (false) | `1` (true)

所有启用的遮挡或约束的总组合视线访问状态。

- `0` (false) — 无视线。
- `1` (true) — 已建立视线。

#### 依赖项

- 要将此端口显示为 **Access**，请清除 **Output access status for each occulting body** 参数。
- 要将此端口显示为 **Access**total，请选择 **Output access status for each occulting body** 参数。

**数据类型：** `Boolean`

### **AccesssourceCB** — 源中心天体的视线访问状态 `0` (false) | `1` (true)

仅针对源中心天体的从源到目标的视线访问状态。如果源与目标之间的视线访问未被源中心天体阻挡，则此状态为 `1` (true)。*source* 取决于 **Source** 选项卡上设置的 **Central body** 选项。

- `0` (false) — 无视线。
- `1` (true) — 已建立视线。

#### 依赖项

要启用此端口，请选择 **Output access status for each occulting body** 参数。

**数据类型：** `Boolean`

### **AccessEarth/Moon** — Earth 或 Moon 的视线访问状态 `0` (false) | `1` (true)

当 Earth 或 Moon 其中之一为源中心天体或目标中心天体启用时，从源到目标针对 Earth 或 Moon 的视线访问状态。如果 Earth 或 Moon 未阻挡源与目标之间的视线访问，则此状态为 1 (true)。

- `1` (true) — 如果 Earth 或 Moon 未阻挡源与目标之间的视线访问。
- `0` (false) — 如果 Earth 或 Moon 阻挡源与目标之间的视线访问。

#### 依赖项

要启用此端口：

- 选择 **Output access status for each occulting body** 参数。
- 为源或目标中心天体选择 **Include Moon** 或 **Include Earth** 参数。

**数据类型：** `Boolean`

### **AccesstargetCB** — 目标中心天体的视线访问状态 `0` (false) | `1` (true)

仅针对目标中心天体的从源到目标的视线访问状态。如果目标中心天体未阻挡源与目标之间的视线访问，则此状态为 `1` (true)。

- `0` (false) — 无视线。
- `1` (true) — 已建立视线。

#### 依赖项

要启用此端口：

- 选择 **Output access status for each occulting body** 参数。
- 清除 **Use same central body as Source** 参数。

**数据类型：** `Boolean`

### **AccessSrc FOV** — 源视场的从源到目标视线访问状态 `0` (false) | `1` (true)

仅针对源视场 (FOV) 的从源到目标视线访问状态。当目标位于源 FOV 内部时，此状态为 `1` (true)。

- `0` (false) — 无视线。
- `1` (true) — 已建立视线。

#### 依赖项

要启用此端口：

- 选择 **Output access status for each occulting body** 参数。
- 在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

**数据类型：** `Boolean`

### **AccessTgt FOV** — 目标视场的从源到目标视线访问状态 `0` (false) | `1` (true)

仅针对目标视场 (FOV) 的从源到目标视线访问状态。当源位于目标 FOV 内部时，此状态为 `1` (true)。

- `0` (false) — 无视线。
- `1` (true) — 已建立视线。

#### 依赖项

要启用此端口：

- 选择 **Output access status for each occulting body** 参数。
- 在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

**数据类型：** `Boolean`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### Main

### **Units** — 参数和端口单位 `Metric (m)` (default) | `Metric (km)` | `English (ft)` | `English (M)`

参数和端口单位，指定为 `Metric (m)`、`Metric (km)`、`English (ft)` 或 `English (M)`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Units` |
| **值：** | `Metric (m)` (default) | `Metric (km)` | `English (ft)` | `English (M)` |

### **Time source** — 时间源方法 `Dialog` (default) | `Port (Julian date)` | `Port (T0 and elapsed Julian time)`

时间源方法，指定为以下值之一：

- `Dialog` — 模块对话框参数
- `Port (Julian date)` — **T**JD 端口
- `Port (T0 and elapsed Julian time)` — **T**JD 和 **ΔT**JD 端口

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `timeSource` |
| **值：** | `Dialog` (default) | `Port (Julian date)` | `Port (T0 and elapsed Julian time)` |

### **Start date/time (JD)** — 仿真的初始开始日期和时间 `juliandate(2020, 1, 1)` (default) | 有效标量儒略日

仿真的初始开始日期和时间，指定为有效标量儒略日。为了确定每个仿真时间步的当前时间，模块会将经过的仿真时间添加到此值。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

#### 依赖项

要启用此参数，请将 **Time source** 设置为 `Dialog`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `startDate` |
| **值：** | `juliandate(2020, 1, 1)` (default) | 有效标量儒略日 |

### **Access calculation type** — 控制访问类型的方法 `Cumulative` (default) | `Element-wise`

控制如何在源和目标之间计算访问的方法。

- `Cumulative`

  - 标量源和 *M* 个目标 — 如果源可以看到每个目标，则模块建立访问（例如，如果 `Src` 可以看到 `Tgt 1` 和 `Tgt 2`，则 **Access** 端口为 `1` (true)）。访问状态输出为标量。
  - *M* 个源和 *M* 个目标 — 如果源和目标的全部对应索引之间存在视线访问，则模块建立访问（例如，如果 `Src 1` 可以看到 `Tgt 1` 且 `Src 2` 可以看到 `Tgt 2`，则 **Access** 为 true）。访问状态输出为标量。
- `Element-wise`

  - 标量源和 *M* 个目标 — 模块单独建立并报告源与每个目标之间的访问（例如，如果 `Src` 可以看到 `Tgt 1`，则 `Access 1` 元素为 `1` (true)；如果 `Src` 可以看到 `Tgt 2`，则 `Access 2` 为 true）。访问状态输出大小为 *M*。`Access 1` 和 `Access 2` 分别是 **Access** 端口的第一和第二个元素。
  - *M* 个源和 *M* 个目标 — 模块针对源和目标的对应索引单独建立并报告访问（例如，如果 `Src 1` 可以看到 `Tgt 1`，则 `Access 1` 为 `1` (true)；如果 `Src 2` 可以看到 `Tgt 2`，则 `Access 2` 为 `1` (true)）。访问状态输出大小为 *M*。`Access 1` 和 `Access 2` 分别是 **Access** 端口的第一和第二个元素。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetType` |
| **值：** | `Cumulative` (default) | `Element-wise` |

### **Output access status for each occulting body** — 为每个遮挡天体输出访问状态 `off` (default) | `on`

为源中心天体、目标中心天体以及 Earth、Moon 或两者的遮挡输出访问状态。默认情况下，模块仅输出组合的总访问。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `outputIndividualAccess` |
| **值：** | `off` (default) | `on` |

### **Ephemeris model** — 星历模型 `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t`

选择 Jet Propulsion Laboratory 定义的以下星历模型之一。模块使用星历数据来计算视线访问计算所需中心天体的相对天体位置。

| **Ephemeris Model** | 描述 |
| --- | --- |
| `DE405` | 于 1998 年发布。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE421` | 于 2008 年发布。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。此模块相对于 1998 年采用的 International Celestial Reference Frame version 1.0 实现这些星历。 |
| `DE423` | 于 2010 年发布。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE430` | 于 2013 年发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |
| `DE432t` | 于 2014 年 4 月发布。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。此模块相对于 2010 年采用的 International Celestial Reference Frame version 2.0 实现这些星历。 |

Line of Sight Access 模块在以下情况下加载 Jet Propulsion Laboratory 行星星历数据：

- 源中心天体不同于目标中心天体。
- 你定义源或目标自定义中心天体相对于太阳系质心。

**注意**

此模块要求你使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB® Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条上，单击 **Add-Ons**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ephemerisModel` |
| **值：** | `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t` |

### **Limit ephemerides date range** — 启用星历数据日期范围开始和结束的选项 `on` (default) | `off`

控制仿真期间加载到内存中的数据量以及模块生成代码中包含的数据量：

- 清除此参数以包含 Ephemeris model 表中定义的完整日期范围的数据。
- 选择此参数以将星历数据的加载限制为指定日期范围。

#### 依赖项

要启用此参数，请选择 **Limit ephemerides date range** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `useDateRange` |
| **值：** | `on` (default) | `off` |

### **Start date (JD)** — 星历日期范围的开始日期 `juliandate(2020, 1, 1)` (default) | 儒略日

星历日期范围的开始日期，指定为儒略日。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ephemerisStartDate` |
| **值：** | `juliandate(2020, 1, 1)` (default) | 儒略日 |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2035, 1, 1)` (default) | 儒略日

星历日期范围的结束日期，指定为儒略日。

#### 依赖项

要启用此参数，请选择 **Limit ephemerides date range** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ephemerisEndDate` |
| **值：** | `juliandate(2035, 1, 1)` (default) | 儒略日 |

### **Action for out-of-range input** — 超出范围输入的模块行为 `Warning` (default) | `Error` | `None`

超出范围输入的模块行为，指定为以下值之一。

| Action | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` (default) | Diagnostic Viewer 中显示警告。模型仿真继续。 |
| `Error` | Diagnostic Viewer 中显示错误。模型仿真停止。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `action` |
| **值：** | `Warning` (default) | `Error` | `None` |

### **Enable zero-crossing detection** — 启用零交叉检测 `off` (default) | `on`

选择以启用零交叉检测，使 Line of Sight Access 能够在进出视线时识别零交叉。有关详细信息，请参阅 Zero-Crossing Detection。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zeroCrossing` |
| **值：** | `off` (default) | `on` |

### Source

### **Central body** — 源位置的天体中心天体 `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

源位置的天体中心天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune`、`Sun` 或 `Custom`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceCentralBody` |
| **值：** | `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom` |

### **Include Moon** — 包含 Moon 的选项 `off` (default) | `on`

当源中心天体为 Earth 时，在访问计算中包括 Moon 作为次要遮挡天体的选项。

#### 依赖项

要启用此参数，请将 **Source** 选项卡的 **Central body** 参数设置为 `Earth`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceIncludeMoon` |
| **值：** | `off` (default) | `on` |

### **Include Earth** — 包含 Earth 的选项 `off` (default) | `on`

当源中心天体为 Moon 时，在访问计算中包括 Earth 作为次要遮挡天体的选项。

#### 依赖项

要启用此参数，请将 **Source** 选项卡的 **Central body** 参数设置为 `Moon`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceIncludeEarth` |
| **值：** | `off` (default) | `on` |

### **Position coordinate frame** — 位置坐标系 `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude`

位置坐标系，指定为 `ICRF`、`Fixed-frame` 或 `Latitude, Longitude, Altitude`。有关详细信息，请参阅算法。

#### 依赖项

要启用此参数，请将 **Source** 选项卡中的 **Central body** 参数设置为 `Custom` 以外的任何选项。当中心天体为 `Custom` 时，位置坐标系始终为 International Celestial Reference Frame (ICRF)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceFrame` |
| **值：** | `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude` |

### **Minimum elevation angle (deg)** — 最小仰角 `0` (default) | double scalar | vector

最小仰角，

计算源对象访问时要使用的最小仰角，指定为 double 标量或向量。

- 如果源与目标之间的仰角小于最小仰角，则模块不建立访问。值必须在 `[–90, 90]` 范围内。
- 如果提供了多个源，并且将 **Minimum Elevation Angle** 指定为标量，则模块将该值分配给每个源输入。
- 如果提供了多个源，并且将 **Minimum Elevation Angle** 指定为向量，则向量长度必须等于提供给模块的源输入数量。

#### 依赖项

要启用此参数，请将 **Source** 选项卡上的 **Position coordinate frame** 参数设置为 `Latitude, Longitude, Altitude`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceFrame` |
| **值：** | `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude` |

**数据类型：** `double`

### **Input Moon libration angles** — Moon 天平动 off (default) | on

要指定用于 Moon 方向的 Moon 天平动角 (φ θ ψ)，请选择此参数。否则，清除此参数。

#### 依赖项

要启用此参数，请将 **Source** 选项卡上的 **Central body** 设置为 `Moon`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceUseMoonLib` |
| **值：** | `'off'` (default) | `'on'` |

### **Use Earth orientation parameters (EOPs)** — 使用地球定向参数的选项 on (default) | off

选择此复选框以在 ICRF 与固定坐标系之间的转换中使用地球定向参数。否则，清除此复选框。

#### 依赖项

要启用此参数，请将 **Source** 选项卡上的 **Central body** 设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useEOPs` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **IERS EOP data file** — 地球定向数据 `aeroiersdata.mat` (default) | MAT file

地球定向数据的自定义列表，在 MAT 文件中指定。要创建此文件，请参阅 `aeroReadIERSData`。

#### 依赖项

要启用此参数：

- 选择 **Use Earth orientation parameters (EOPs)** 参数。
- 将 **Source** 选项卡上的 **Central body** 设置为 `Earth`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceEOPFile` |
| **值：** | `aeroiersdata.mat` (default) | MAT file |

### **Equatorial radius** — 自定义赤道半径 `3.3962e6` (default) | double scalar

自定义中心天体的自定义赤道半径，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数，请将 **Source** 选项卡上的 **Central body** 设置为 `Custom`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceCustomR` |
| **值：** | `3.3962e6` (default) | double scalar |

### **Use field of view (FOV)** — 指定视场的选项 `off` (default) | `on`

用于指定是否将访问计算约束到圆锥视场的选项。此选项模拟传感器或相机的行为。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceUseFOV` |
| **值：** | `off` (default) | `on` |

### **FOV half angle (deg)** — 视场半角 `22.5` (default) | double scalar

视场半角，指定为 double 标量。

#### 依赖项

要启用此参数，请在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceFOVHalfAngle` |
| **值：** | `22.5` (default) | double scalar |

### **Attitude representation** — 姿态表示 `Quaternion` (default) | `Euler angles`

源姿态和 FOV 方向的姿态表示，指定为 `Quaternion` 或 `Euler angles`。

#### 依赖项

要启用此参数，请在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceRotationFormat` |
| **值：** | `Quaternion` (default) | `Euler angles` |

### **FOV orientation source** — 视场方向源方法 `Dialog` (default) | `Port`

视场方向源，指定为以下值之一：

- `Dialog` — 模块对话框参数。
- `Port` — **Src FOV** 端口

#### 依赖项

要启用此参数，请在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceFOVOrientationSrc` |
| **值：** | `Dialog` (default) | `Port` |

### **FOV orientation** — 视场方向 4 元素向量 | 3 元素向量

FOV 视轴相对于源本体坐标系的方向，指定为 4 元素向量（四元数）或 3 元素向量（欧拉角）。

- 4 元素向量 — **Attitude representation** 设置为 `Quaternion`。
- 3 元素向量 — **Attitude representation** 设置为 `Euler angles`。

#### 依赖项

要启用此参数：

- 将 **FOV orientation source** 设置为 `Dialog`。
- 在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceRotationFormat` |
| **值：** | `Quaternion` (default) | `Euler angles` |

### **Attitude reference coordinate frame** — 姿态参考坐标系 `ICRF` | `Fixed-frame` | `NED`

用于源姿态定义的坐标系，指定为 `ICRF`、`Fixed-frame` 或 `NED`。*Attitudes* 是从姿态参考坐标系到本体坐标系的旋转。

#### 依赖项

要启用此参数，请在 **Source** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceRotationFormat` |
| **值：** | `ICRF` | `Fixed-frame` | `NED` |

### **Angle rotation order** — 角度旋转顺序 `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

欧拉角姿态表示的旋转角顺序。

**可调：** 是

#### 依赖项

要启用此参数，请在 **Source** 选项卡上：

- 选择 **Use field of view (FOV)** 参数。
- 将 `Attitude Representation` 参数设置为 `Euler Angles`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sourceRotationOrder` |
| **值：** | `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |

### Target

### **Use same central body as Source** — 使用与源本体指定相同中心天体的选项 `on` (default) | `off`

使用与源指定相同目标中心天体的选项。

Line of Sight Access 模块允许你定义源和目标中心天体。不能使用 **Central body** 参数为两个中心天体设置相同的行星。如果要对源和目标使用相同的中心天体，请在 **Target** 选项卡中选择 **Use same central body as Source** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `useTargetCentralBodyForTarget` |
| **值：** | `on` (default) | `off` |

### **Central body** — 目标位置的天体中心天体 `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

目标位置的天体中心天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune`、`Sun` 或 `Custom`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetCentralBody` |
| **值：** | `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom` |

### **Include Moon** — 包含 Moon 的选项 `off` (default) | `on`

当目标中心天体为 Earth 时，在访问计算中包括 Moon 作为次要遮挡天体的选项。

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Central body** 参数设置为 `Earth`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetIncludeMoon` |
| **值：** | `off` (default) | `on` |

### **Include Earth** — 包含 Earth 的选项 `off` (default) | `on`

当目标中心天体为 Moon 时，在访问计算中包括 Earth 作为次要遮挡天体的选项。

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Central body** 参数设置为 `Moon`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetIncludeEarth` |
| **值：** | `off` (default) | `on` |

### **Position coordinate frame** — 位置坐标系 `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude`

位置坐标系，指定为 `ICRF`、`Fixed-frame` 或 `Latitude, Longitude, Altitude`。有关详细信息，请参阅算法。

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Central body** 参数设置为 `Custom` 以外的任何选项。当中心天体为 `Custom` 时，位置坐标系始终为 International Celestial Reference Frame (ICRF)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetCustomR` |
| **值：** | `ICRF` (default) | double scalar |

### **Minimum elevation angle (deg)** — 最小仰角 `0` (default) | double scalar | vector

最小仰角，

计算目标对象访问时要使用的最小仰角，指定为 double 标量或向量。

- 如果源与目标之间的仰角小于最小仰角，则模块不建立访问。值必须在 `[–90, 90]` 范围内。
- 如果提供了多个目标，并且将 **Minimum Elevation Angle** 指定为标量，则模块将该值分配给每个源输入。
- 如果提供了多个目标，并且将 **Minimum Elevation Angle** 指定为向量，则向量长度必须等于提供给模块的源输入数量。

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Position coordinate frame** 参数设置为 `Latitude, Longitude, Altitude`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetMinimumElevationAngle` |
| **值：** | `0` (default) | double scalar |

**数据类型：** `double`

### **Input Moon libration angles** — Moon 天平动角 off (default) | on

要指定用于 Moon 方向的 Moon 天平动角 (φ θ ψ)，请选择此复选框。否则，清除此复选框。

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Central body** 参数设置为 `Moon`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetUseMoonLib` |
| **值：** | `'off'` (default) | `'on'` |

### **IERS EOP data file** — 地球定向数据 `aeroiersdata.mat` (default) | MAT file

地球定向数据的自定义列表，在 MAT 文件中指定。要创建此文件，请参阅 `aeroReadIERSData`。

#### 依赖项

要启用此参数，请在 **Target** 选项卡上：

- 选择 **Use Earth orientation parameters (EOPs)** 参数。
- 将 **Central body** 设置为 `Earth`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetEOPFile` |
| **值：** | `aeroiersdata.mat` (default) | MAT file |

### **Equatorial radius** — 自定义赤道半径 `3.3962e6` (default) | double scalar

自定义中心天体的自定义赤道半径，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数，请将 **Target** 选项卡上的 **Central body** 参数设置为 `Custom`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetCustomR` |
| **值：** | `3.3962e6` (default) | double scalar |

### **Use field of view (FOV)** — 指定视场的选项 `off` (default) | `on`

用于指定是否在访问计算中为目标准使用视场的选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetUseFOV` |
| **值：** | `off` (default) | `on` |

### **FOV half angle (deg)** — 视场半角 `22.5` (default) | double scalar

视场半角，指定为 double 标量。

#### 依赖项

要启用此参数，请在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetFOVHalfAngle` |
| **值：** | `22.5` (default) | double scalar |

### **Attitude representation** — 姿态表示 `Quaternion` (default) | `Euler angles`

姿态表示，指定为 `Quaternion` 或 `Euler angles`。

#### 依赖项

要启用此参数，请在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetRotationFormat` |
| **值：** | `Quaternion` (default) | `Euler angles` |

### **FOV orientation source** — 视场方向源方法 `Dialog` (default) | `Port`

视场方向源方法，指定为以下值之一：

- `Dialog` — 模块对话框参数
- `Port` — **Tgt FOV** 端口

#### 依赖项

要启用此参数，请在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetFOVOrientationSrc` |
| **值：** | `Dialog` (default) | `Port` |

### **FOV orientation** — 视场方向 4 元素向量 | 3 元素向量

FOV 视轴相对于目标本体坐标系的方向，表示为 4 元素向量（四元数）或 3 元素向量（欧拉角）。

- 4 元素向量 — **Attitude representation** 设置为 `Quaternion`。
- 3 元素向量 — **Attitude representation** 设置为 `Euler angles`。

#### 依赖项

要启用此参数，请在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetRotationFormat` |
| **值：** | `Quaternion` (default) | `Euler angles` |

### **Attitude reference coordinate frame** — 姿态参考坐标系 `ICRF` (default) | `Fixed-frame` | `NED`

用于目标姿态定义的坐标系，指定为 `ICRF`、`Fixed-frame` 或 `NED`。Attitudes 是从姿态参考坐标系到本体坐标系的旋转。

#### 依赖项

要启用此参数，请在 **Target** 选项卡上选择 **Use field of view (FOV)** 参数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetRotationFormat` |
| **值：** | `ICRF` | `Fixed-frame` | `NED` |

### **Angle rotation order** — 角度旋转顺序 `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

欧拉角姿态表示的旋转角顺序。

**可调：** 是

#### 依赖项

要启用此参数，请在 **Target** 选项卡上：

- 选择 **Use field of view (FOV)** 参数。
- 将 `Attitude Representation` 参数设置为 `Euler Angles`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `targetRotationOrder` |
| **值：** | `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: `Line of Sight Access` 模块变更

Line of Sight Access 模块现在支持零交叉检测。此更改使模块能够识别零交叉何时进出视线。

## 描述

确定一个或多个源位置与一个或多个目标位置之间的视线 (LOS) 访问

Line of Sight Access 模块确定在当前时间步，从一个或多个源位置到一个或多个目标位置是否存在视线 (LOS) 访问。

### 源和目标中心天体

Line of Sight Access 模块允许你相对于不同的中心天体定义源和目标。不能为源和目标的 **Central body** 参数设置相同的中心天体。如果要对源和目标使用相同的中心天体，请在 **Target** 选项卡中选择 **Use same central body as Source** 参数。
