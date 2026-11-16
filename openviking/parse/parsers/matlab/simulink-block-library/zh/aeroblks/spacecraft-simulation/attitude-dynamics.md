---
type: simulink-block
title: 'Attitude Dynamics'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'attitudedynamics'
documentation_source_path: 'attitudedynamics.html'
language: zh-CN
chinese_source: worker-translation
---

# Attitude Dynamics

## 端口

### 输入

### **X** — 航天器位置 3 元素向量 | *numSat*-by-3 数组

航天器相对于状态向量坐标系的位置，在当前时间步指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

- 要更改此端口的坐标系，请设置 **State vector output coordinate frame** 参数。
- **质量** 或 **姿态** 选项卡中提供的初始条件的大小控制端口维度。

**数据类型：** `double`

### **V** — 航天器速度 3 元素向量 | *numSat*-by-3 数组

航天器相对于状态向量坐标系的速度，在当前时间步指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

- 要更改此端口的坐标系，请设置 **State vector output coordinate frame** 参数。
- **质量** 或 **姿态** 选项卡中提供的初始条件的大小控制端口维度。

**数据类型：** `double`

### **Mb** — 外部力矩 3 元素向量 | *numSat*-by-3 数组

在体坐标系中施加到航天器的力矩，在当前时间步指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口，请选中 **Input body moments** 复选框。

**数据类型：** `double`

### **dm/dt** — 质量变化率 标量 | 大小为 *numSat* 的一维数组

当前时间步的质量变化率（累积为正，烧蚀为负），指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **m** — 航天器质量 标量 | 大小为 *numSat* 的一维数组

当前时间步的航天器质量。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **I** — 航天器惯性张量 3-by-3 数组 | 3-by-3-by-*numSat* 数组

当前时间步的航天器惯性张量，指定为 3-by-3 数组或 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵变化率 3-by-3 数组 | 3-by-3-by-*numSat* 数组

当前时间步的惯性张量矩阵变化率，指定为 3-by-3 数组或 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **Vre** — 相对速度 3 元素向量 | *numSat*-by-3 数组

在体固联轴中，质量累积到或烧蚀自本体的相对速度，指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Custom Variable` 或 `Simple Variable`。
- 选中 **Include mass flow relative velocity** 复选框。

**数据类型：** `double`

### **φθψ** — 月球天平动角 3 元素向量

用于在国际天球参考系 (ICRF) 和月心固定坐标系之间进行变换的月球天平动角，使用月心主轴 (PA) 系统，指定为 3 元素向量。要获取这些值，请使用 Moon Libration 模块。

**注意**

当 **Central body** 设置为 `Moon` 时，此模块使用的固定坐标系是平地球/极轴 (ME) 系统。有关详细信息，请参阅算法。

#### 依赖关系

要启用此端口：

- 将 **Central body** 设置为 `Moon`。
- 选中 **Input Moon libration angles** 复选框。

**数据类型：** `double`

### **αδW** — 赤经、赤纬和旋转角 3 元素向量

中心天体自旋轴的瞬时赤经、赤纬和旋转角，指定为 3 元素向量。此端口仅适用于自定义中心天体。

#### 依赖关系

要启用此端口：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Port`。

**数据类型：** `double`

### 输出

### **qbody2icrf** — 航天器姿态四元数 4 元素四元数 | *numSat*-by-4 数组

航天器姿态四元数，返回为从体轴到输出端口坐标系的标量在前的 4 元素四元数旋转，或当前时间步的标量在前的 *numSat*-by-4 数组。*numSat* 是航天器数量。

#### 依赖关系

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Quaternion`。

**数据类型：** `double`

### **DCM** — 航天器姿态方向余弦矩阵 3-by-3 数组 | *numSat*-by-3-by-3 数组

航天器姿态方向余弦矩阵 (DCM)，返回为 3-by-3 数组或 *numSat*-by-3-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `DCM`。

**数据类型：** `double`

### **R1,R2,R3** — 航天器姿态欧拉角 3 元素向量 | *numSat*-by-3 数组

航天器姿态欧拉角，返回为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Euler angles`。

**数据类型：** `double`

### **ω** — 航天器角速率 3 元素向量 | *numSat*-by-3 数组

航天器相对于姿态参考坐标系的角速率，返回为 3 元素向量或 *numSat*-by-3 数组，表示为体轴角速率 PQR。*numSat* 是航天器数量。

#### 依赖关系

姿态参考坐标系取决于 **Attitude reference coordinate frame** 参数。

**数据类型：** `double`

### **qicrf2ff** — 坐标系变换 4 元素数组

当前时间步 ICRF 和固定坐标系之间的坐标系变换，返回为 4 元素数组。

#### 依赖关系

要启用此端口，请选中 **Output quaternion (ICRF to Fixed-frame)** 复选框。

**数据类型：** `double`

### **tutc** — 当前时间步的时间 标量 | 6 元素数组

当前时间步的时间，返回为：

- 标量 — 如果将 **Start data/time** 参数指定为儒略日期。
- 6 元素数组 — 如果将 **Start data/time** 参数指定为具有六个元素的公历日期：年、月、日、小时、分钟、秒。

此值等于 **Start date/time** 参数值加上经过的仿真时间。

#### 依赖关系

要启用此参数，请选中 **Output current date/time (UTC Julian date)** 复选框。

**数据类型：** `double`

### **Fuel Status** — 燃料状态 标量 | *numSat* 元素数组

当前时间步的燃料箱状态，返回为标量或 *numSat* 元素数组：

- `1` — 燃料箱已满。
- `0` — 燃料箱未满或为空。
- `-1` — 燃料箱为空。

*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable`。
- 选中 **Output fuel tank status** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **Input body moments** — 启用外部力矩的选项 on（默认）| off

要将外部力矩包含在体坐标系中航天器运动方程的积分中，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `momentsIn` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **State vector coordinate frame** — 位置和速度状态端口坐标系 `ICRF`（默认）| `Fixed-frame`

位置和速度状态端口坐标系设置，指定为 `ICRF` 或 `Fixed-frame`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outportFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认值：** `'ICRF'` |

### **Start date/time (UTC Julian date)** — 仿真的初始开始时间 `juliandate (2020, 1, 1, 12, 0, 0)`（默认）| 有效的标量儒略日期 | 有效的公历日期

仿真的初始开始日期和时间，指定为儒略日期或公历日期。有效的公历日期必须包含年、月、日、小时、分钟和秒，以 1D 或 6 元素数组形式给出。模块使用此值定义初始条件。

**提示**

要计算儒略日期，请使用 `juliandate` 函数。

**可调：** 是

#### 依赖关系

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **模块参数：** `startDate` |
| **类型：** character vector |
| **值：** `'juliandate(2020, 1, 1, 12, 0, 0)'` | 有效的标量儒略日期 | 有效的公历日期 |
| **默认值：**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — 添加输出端口 tutc 的选项 on（默认）| off

要输出当前日期或时间，请选中此复选框。否则，清除此复选框。

#### 依赖关系

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dateOut` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `Warning`（默认）| `Error` | `None`

超出范围时的模块行为操作。指定以下选项之一。

| 操作 | 说明 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error` (default) | 在诊断查看器中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**： character vector |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认值**： `'Warning'` |

### 质量

### **Mass type** — 航天器质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

航天器质量类型，指定为：

- `Fixed` — 质量和惯性在整个仿真过程中保持恒定。
- `Simple Variable` — 质量和惯性随质量变化率线性变化。
- `Custom Variable` — 瞬时质量、惯性和惯性变化率是模块的输入。

#### 程序化使用

|  |
| --- |
| **模块参数**： `massType` |
| **类型**： character vector |
| **值**： `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认值**： `'Fixed'` |

### **Mass** — 刚体航天器的初始质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

刚体航天器的初始质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 参数设置为 **Fixed** 或 **Simple variable**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** character vector |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认值：** `'4.0'` |

### **Empty mass** — 航天器空质量 `3.5`（默认）| 标量 | 大小为 *numSat* 的向量

航天器空（干）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `emptyMass` |
| **类型：** character vector |
| **值：** 大小为 *numSat* 的一维数组 | 大小为 *numSat* 的一维数组 |
| **默认值：** `'3.5'` |

### **Full mass** — 航天器满质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

航天器满（湿）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fullMass` |
| **类型：** character vector |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认值：** `'4.0'` |

### **Inertia tensor** — 惯性张量矩阵 `[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

航天器的初始惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` | 3-by-3 数组 | 3-by-3-by-*numSat* 数组 |
| **默认值：** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` |

### **Empty inertia tensor** — 空惯性张量矩阵 `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

空（干）惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `emptyInertia` |
| **类型：** character vector |
| **值：** 3-by-3 数组 | 3-by-3-by-*numSat* 数组 |
| **默认值：** `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]` |

### **Full inertia tensor** — 满惯性张量矩阵 `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

满（湿）惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fullInertia` |
| **类型：** character vector |
| **值：** 3-by-3 数组 | 3-by-3-by-*numSat* 数组 |
| **默认值：** `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]` |

### **Include mass flow relative velocity** — 启用质量流速度的选项 off（默认）| on

要启用质量流速度到模块，请选中此复选框。质量流速度是质量在体坐标系中累积或烧蚀时的相对速度。要禁用质量流速度到模块，请清除此复选框。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable` 或 `Custom variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useMassFlowRelativeVelocity` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **Limit mass flow when mass is empty or full** — 限制质量流的选项 on（默认）| off

要在航天器质量满或空时限制质量流，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `limitMassFlow` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Output fuel tank status** — 启用燃料箱状态的选项 on（默认）| off

要启用燃料箱状态，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outputFuelStatus` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### 姿态

### **Attitude reference coordinate frame** — 姿态和角速率坐标系 `ICRF`（默认）| `Fixed-frame` | `NED` | `LVLH`

相对于姿态和角速率初始条件的姿态和角速率坐标系，指定为：

- `ICRF`
- `Fixed-frame`
- `NED`
- `LVLH`

#### 程序化使用

|  |
| --- |
| **模块参数：** `attitudeFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` | `'NED'` | `'LVLH'` |
| **默认值：** `'ICRF'` |

### **Attitude representation** — 方向格式 `Quaternion`（默认）| `DCM` | `Euler angles`

航天器姿态的方向格式（初始条件和输出端口），指定为 `Quaternion`、`DCM` 或 `Euler angles`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `attitudeFrame` |
| **类型：** character vector |
| **值：** `'Quaternion'` | `'DCM'` | `'Euler angles'` |
| **默认值：** `'Quaternion'` |

### **Initial body attitude** — 航天器初始姿态 `[1, 0, 0, 0]`（默认）| 4 元素向量 | *numSat*-by-4 数组 | 3-by-3 数组 | *numSat*-by-3-by-3 数组 | 3 元素向量 | *numSat*-by-3 数组

航天器的初始姿态（方向），根据 **Attitude representation** 提供为四元数、DCM 或欧拉角集。

**可调：** 是

#### 依赖关系

此参数名称和值格式取决于 **Attitude representation** 参数。

| 参数名称 | 姿态表示设置 | 值格式 |
| --- | --- | --- |
| **Initial quaternion** | `Quaternion` | - 4 元素向量 - *numSat*-by-4 数组 |
| **Initial DCM** | `DCM` | - 3-by-3 数组 - *numSat*-by-3-by-3 数组 |
| **Initial Euler angles** | `Euler angles` | - 3 元素向量 - *numSat*-by-3 数组 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `attitude` |
| **类型：** character vector |
| **值：** 4 元素向量 | *numSat*-by-4 数组 | 3-by-3 数组 | *numSat*-by-3-by-3 数组 | 3 元素数组 | *numSat*-by-3 数组 |
| **默认值：** `'[1, 0, 0, 0]'` |

### **Angle rotation order** — 角度旋转顺序 `ZYX`（默认）| `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

用于欧拉角姿态表示的旋转角顺序。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Attitude representation** 设置为 `Euler angles`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `rotationOrder` |
| **类型**： character vector |
| **值**： `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认值**： `'ZYX'` |

### **Initial body angular rates PQR** — 初始体固联角速率 `[0, 0, 0]`（默认）| 3 元素向量 | *numSat*-by-3 数组

相对于 **Attitude reference coordinate frame** 的初始体固联角速率 (PQR)。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `attitudeRate` |
| **类型：** character vector |
| **值：** | 3 元素向量 | *numSat*-by-3 数组 |
| **默认值：** `[0, 0, 0]` |

### **Include gravity gradient torque** — 启用重力梯度力矩的选项 on（默认）| off

选中此复选框以启用模块旋转动力学方程中的重力梯度力矩。否则，清除此复选框。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `angAccelOut` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### 中心天体

### **Central body** — 航天器环绕运行的天体 `Earth`（默认）| `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

航天器环绕运行的天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune` 或 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `centralBody` |
| **类型：** character vector |
| **值：** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` | |
| **默认值：** `'Earth'` |

### **Rotational rate** — 旋转速率 `4.06124975e-3`（默认）| 标量

自定义中心天体的旋转速率，指定为标量。

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'customOmega'` |
| **类型：** character vector |
| **值：** `'4.06124975e-3'` | 标量 |
| **默认值：** `'4.06124975e-3'` |

### **Use Earth orientation parameters (EOPs)** — 使用地球定向参数的选项 on（默认）| off

选中此复选框以使用地球定向参数进行 ICRF 和固定坐标系之间的变换。否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Earth`。

此外，还必须满足以下条件之一：

- **State vector output coordinate frame** 设置为 `Fixed-frame`。
- **Attitude reference coordinate frame** 设置为 `Fixed-frame` 或 `NED`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useEOPs` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **IERS EOP data file** — 地球定向数据 `aeroiersdata.mat`（默认）| MAT-file

自定义地球定向数据列表，在 MAT 文件中指定。

#### 依赖关系

要启用此参数：

- 选中 **Use Earth orientation parameters (EOPs)** 复选框。
- 将 **Central body** 设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eopFile` |
| **类型：** character vector |
| **值：** `'aeroiersdata.mat'` | MAT-file |
| **默认值：** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — 月球天平动欧拉角速率 off（默认）| on

要为月球定向指定欧拉天平动角 (φ θ ψ)，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Moon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useMoonLib` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Output quaternion (ICRF to Fixed-frame)** — 添加输出变换四元数端口的选项 off（默认）| on

要添加从 ICRF 到固定坐标系的四元数变换的输出变换四元数端口，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outputTransform` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Central body spin axis source** — 中心天体自旋源 `Port`（默认）| `Dialog`

中心天体自旋轴来源，指定为 `Port` 或 `Dialog`。模块使用自旋轴计算自定义中心天体从 ICRF 到固定坐标系的变换。

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbPoleSrc` |
| **类型：** character vector |
| **值：** `'Port'` | `'Dialog'` |
| **默认值：** `'Port'` |

### **Spin axis right ascension (RA) at J2000** — 中心天体自旋轴在 J2000 的赤经 `317.68143`（默认）| double 标量

中心天体自旋轴在 J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT) 的赤经，指定为 double 标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRA` |
| **类型：** character vector |
| **值：** `'317.68143'` | double 标量 |
| **默认值：** `'317.68143'` |

### **Spin axis RA rate (deg/century)** — 中心天体自旋轴的赤经变化率 `-0.1061`（默认）| double 标量

中心天体自旋轴的赤经变化率，指定为 double 标量，单位为指定的角度单位/世纪。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRARate` |
| **类型：** character vector |
| **值：** `'-0.1061'` | double 标量 |
| **默认值：** `'-0.1061'` |

### **Spin axis declination (Dec) at J2000** — 中心天体自旋轴在 J2000 的赤纬 `52.88650`（默认）| double 标量

中心天体自旋轴在 J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT) 的赤纬，指定为 double 标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDec` |
| **类型：** character vector |
| **值：** `'52.88650'` | double 标量 |
| **默认值：** `'52.88650'` |

### **Spin axis Dec rate (deg/century)** — 中心天体自旋轴的赤纬变化率 `-0.0609`（默认）| double 标量

中心天体自旋轴的赤纬变化率，指定为 double 标量，单位为指定的角度单位/世纪。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDecRate` |
| **类型：** character vector |
| **值：** `'-0.0609'` | double 标量 |
| **默认值：** `'-0.0609'` |

### **Initial rotation angle at J2000** — 中心天体 *x* 轴的旋转角 `176.630`（默认）| double 标量

中心天体 *x* 轴相对于 ICRF *x* 轴在 J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT) 的旋转角，指定为 double 标量，采用指定的角度单位。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotAngle` |
| **类型：** character vector |
| **值：** `'176.630'` | double 标量 |
| **默认值：** `'176.630'` |

### **Rotation rate (deg/day)** — 中心天体 *x* 轴的旋转速率 `350.89198226`（默认）| double 标量

中心天体 *x* 轴相对于 ICRF *x* 轴 (2451545.0 JD, 2000 Jan 1 12:00:00 UTC) 的旋转速率，指定为 double 标量，采用角度单位/天。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotRate` |
| **类型：** character vector |
| **值：** `'350.89198226'` | double 标量 |
| **默认值：** `'350.89198226'` |

### **Equatorial radius** — 赤道半径 `3396200`（默认）| double 标量

自定义中心天体的赤道半径，指定为 double 标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Central Body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customR` |
| **类型：** character vector |
| **值：** `'3396200'` | double 标量 |
| **默认值：** `'3396200'` |

### **Flattening** — 行星扁率 `0.00589`（默认）| double 标量

自定义中心天体的行星扁率，指定为 double 标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customF` |
| **类型：** character vector |
| **值：** `'0.00589'` | double 标量 |
| **默认值：** `'0.00589'` |

### **Gravitational parameter** — 引力参数 `4.305e13`（默认）| double 标量

自定义中心天体的引力参数，指定为 double 标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customMu` |
| **类型：** character vector |
| **值：** `'4.305e13'` | double 标量 |
| **默认值：** `'4.305e13'` |

### 单位

### **Units** — 参数和端口单位 `Metric (m/s)`（默认）| `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

参数和端口单位，如下表所示。

| 单位 | 力矩 | 质量 | 惯性 | 距离 | 速度 | 加速度 |
| --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | Newton-meter | Kilograms | Kilogram m2 | meters | meters/sec | meters/sec2 |
| `Metric (km/s)` | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/sec | kilometers/sec2 |
| `Metric (km/h)` | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/hour | kilometers/hour2 |
| `English (ft/s)` | Foot-pound | Slugs | Slug ft2 | feet | feet/sec | feet/sec2 |
| `English (kts)` | Foot-pound | Slugs | Slug ft2 | nautical mile | knots | knots/sec |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **默认值：** `'Metric (m/s)'` |

### **Angle units** — 角度单位 `Degrees`（默认）| `Radians`

角度参数和端口单位，指定为 `Degrees` 或 `Radians`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `angleUnits` |
| **类型：** character vector |
| **值：** `'Degrees'` | `'Radians'` |
| **默认值：** `'Degrees'` |

### **Time format** — 开始日期和时间输出的时间格式 `Julian date`（默认）| `Gregorian`

**Start date/time (UTC Julian date)** 和输出端口 **tutc** 的时间格式，指定为 `Julian date` 或 `Gregorian`。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `timeFormat` |
| **类型：** character vector |
| **值：** `'Julian date'` | `'Gregorian'` |
| **默认值：** `'Julian date'` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

为一个或多个航天器建模姿态动力学

Attitude Dynamics 模块使用数值积分对航天器的旋转动力学建模。该模块使用提供的位置和速度状态，计算一个或多个航天器随时间的姿态和角速度。为获得最准确的结果，请使用具有低容差设置（小于 1e-8）的变步长求解器。要根据任务需求在精度和速度之间进行权衡，可使用较大的容差。

有关 Attitude Dynamics 模块使用的坐标系以及平移和旋转动力学的详细信息，请参阅算法。
