---
type: simulink-block
title: 'Attitude Profile (Nadir Pointing)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'attitudeprofilenadirpointing'
documentation_source_path: 'attitudeprofilenadirpointing.html'
language: zh-CN
chinese_source: worker-translation
---

# Attitude Profile (Nadir Pointing)

## 端口

### 输入

### **X** — 位置状态向量 3 元素向量

航天器在 tutc 时刻的位置状态向量。

**数据类型：** `double`

### **V** — 速度状态向量 3 元素向量

航天器在 tutc 时刻的速度状态向量，指定为 3 元素向量。

#### 依赖关系

要启用此端口，请将 **约束坐标系 (CCF)** 设置为 `LVLH`。

**数据类型：** `double`

### **q** — 航天器姿态 4 元素向量

航天器在 *tutc* 时刻的姿态，表示为从本体坐标系到端口坐标系的四元数，指定为 4 元素向量。

**数据类型：** `double`

### **tutc** — 当前日期或时间标量

当前日期或时间，指定为标量，采用儒略日。

#### 依赖关系

要启用此端口，请执行以下操作之一：

- 将 **指向模式** 设置为 `Point at celestial body` 或 `Point at LatLonAlt`
- 选中 **允许在运行期间更改指向模式** 复选框。

**数据类型：** `double`

### **μ l** — 大地纬度和经度 2 元素向量

地球兴趣点的大地纬度和经度（deg），指定为大小为 2 的一维数组。当 **指向模式** 为 `Point at LatLongAlt` 时，此端口与高度一起使用。此位置用作主约束。

#### 依赖关系

要启用此端口，请执行以下操作之一：

- 将 **指向模式** 设置为 `LatLonAlt`。
- 选中 **允许在运行期间更改指向模式** 复选框。

**数据类型：** `double`

### **h** — 高度标量

地球兴趣点的高度，指定为标量。当 **指向模式** 为 `Point at LatLongAlt` 时，此端口与大地纬度和经度一起使用。此位置用作主约束。

#### 依赖关系

要启用此端口，请执行以下操作之一：

- 将 **指向模式** 设置为 `LatLonAlt`。
- 选中 **允许在运行期间更改指向模式** 复选框。

**数据类型：** `double`

### **A1b** — 主对准向量 3 元素向量

主对准向量（在本体坐标系中），指定为 3 元素向量。

#### 依赖关系

要启用此端口，请将 **主对准（本体坐标系）** 设置为 `Port`。

**数据类型：** `double`

### **A2b** — 次对准向量 3 元素向量

次对准向量（在本体坐标系中），指定为 3 元素向量。

#### 依赖关系

要启用此端口，请将 **次对准（本体坐标系）** 设置为 `Port`。

**数据类型：** `double`

### **C1lvlh** — 主约束向量 3 元素向量

主约束向量，指定为 3 元素向量，在约束坐标系中。

#### 依赖关系

要启用此端口，请将：

- **指向模式** 设置为 `Custom`。
- **主约束 (CCF)** 设置为 `Port`。

**数据类型：** `double`

### **C2lvlh** — 次约束 3 元素向量

次约束向量，指定为 3 元素向量。

#### 依赖关系

要启用此端口，请将 **次约束 (CCF)** 设置为 `Port`。

**数据类型：** `double`

### 输出

### **qtgtb** — 四元数旋转 4 元素向量（标量在前）

用于从航天器当前姿态旋转到所需姿态的四元数旋转（在本体坐标系中），返回为 4 元素向量。

#### 依赖关系

要启用此端口，请选中 **从当前姿态到更新姿态的输出旋转** 复选框。

**数据类型：** `double`

### **qnew** — 更新后的航天器姿态 4 元素向量

按照四元数旋转更新后的航天器姿态，相对于 **端口坐标系**，返回为 4 元素向量。

#### 依赖关系

要启用此端口，请选中 **输出姿态** 复选框。

**数据类型：** `double`

## 参数

### **从当前姿态到更新姿态的输出旋转** — 输出旋转 on（默认）| off

要输出旋转，请选中此复选框。否则，清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：**  `outputError` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **输出姿态** — 输出更新后的姿态 off（默认）| on

要将更新后的航天器姿态作为从本体坐标系到 **端口坐标系** 的四元数旋转输出，请选中此复选框。否则，清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：**  `outputFinalAttitude` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **端口坐标系** — 位置、速度和姿态端口的坐标系 `ICRF`（默认）| `Fixed-frame`

位置、速度和姿态（**q**）端口的坐标系。有关坐标系的详细信息，请参阅算法。

#### 编程用法

|  |
| --- |
| **模块参数：**  `portFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认值：** `'ICRF'` |

### **指向模式** — 主向量对准指向模式 `Point at nadir`（默认）| `Point at celestial body` | `Point at LatLonAlt` | `Custom`

主向量对准指向模式，指定为 `Point at nadir`、`Point at celestial body`、`Point at LatLonAlt` 或 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：** `pointingMode` |
| **类型：** character vector |
| **值：** `'Point at nadir'` | `'Point at celestial body'` | `'Point at LatLonAlt'` | `'Custom'` |
| **默认值：** `'Point at nadir'` |

### **允许在运行期间更改指向模式** — 允许在运行期间更改指向模式 off（默认）| on

要允许在运行期间更改指向模式，请选中此复选框。否则，清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `tunablePointing` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **天体目标** — 天体 `Sun`（默认）| `Mercury` | `Venus` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

用于对准主对准向量的天体。

#### 依赖关系

要启用此参数，请将 **指向模式** 设置为 `Point at celestial body`。

#### 编程用法

|  |
| --- |
| **模块参数：** `celestialTarget` |
| **类型：** character vector |
| **值：** `'Sun'` | `'Mercury'` | `'Venus'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Pluto'` | `'Solar'` | `'Solar system barycenter'` | `'Earth-Moon barycenter'` |
| **默认值：** `'Sun'` |

### **主对准（本体坐标系）** — 主对准向量 `Dialog`（默认）| `Port`

主对准向量源，指定为 `Port` 或 `Dialog`。

- `Port` — 通过 **A1b** 端口指定端口对准数组。
- `Dialog` — 在随附文本框中指定端口对准 3 元素向量（默认值为 `[0 0 1]`）。

#### 依赖关系

要在文本框中指定端口对准数组，请将此参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `primaryAlignmentSrc` | 当 `primaryAlignmentSrc` 为 `'Dialog'` 时，使用 `primaryAlignment` 设置主对准向量 |
| **类型：** character vector |
| **值：** `'Port'` | `'Dialog'` | 主对准向量，指定为 3 元素向量 |
| **默认值：** `'Dialog'` |

### **次对准（本体坐标系）** — 次对准向量 `Dialog`（默认）| `Port`

次对准向量源，指定为 `Port` 或 `Dialog`。

- `Port` — 通过 **A2b** 端口指定端口对准数组。
- `Dialog` — 在随附文本框中指定端口对准 3 元素向量（默认值为 `[1 0 0]`）。

#### 依赖关系

要在文本框中指定端口对准数组，请将此参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `secondaryAlignmentSrc` | 当 `secondaryAlignmentSrc` 为 `'Dialog'` 时，使用 `secondaryAlignment` 设置次对准向量 |
| **类型：** character vector |
| **值：** `'Port'` | `'Dialog'` | 次对准向量，指定为 3 元素向量 |
| **默认值：** `'Dialog'` |

### **约束坐标系, CCF** — 约束坐标系 `ICRF`（默认）| `Fixed-frame` | `LVLH` | `NED` | `Body-fixed`

提供约束向量所在的坐标系，指定为 `ICRF`、`Fixed-frame`、`LVLH`、`NED` 或 `Body-fixed`。有关坐标系的详细信息，请参阅算法。

#### 编程用法

|  |
| --- |
| **模块参数：** `constraintFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` | `'LVLH'` | `'NED'` | `'Body-fixed'` |
| **默认值：** `'ICRF'` |

### **主约束 (CCF)** — 主约束 `Dialog`（默认）| `Port`

主约束向量源，指定为 `Port` 或 `Dialog`。

- `Port` — 通过 **C1b** 端口指定主约束数组。
- `Dialog` — 在随附文本框中指定端口约束 3 元素向量（默认值为 `[1 0 0]`）。

#### 依赖关系

- 要在文本框中指定端口对准数组，请将此参数设置为 `Dialog`。
- 当 **约束坐标系 (CCF)** 设置为 `Custom` 时，此参数会受影响。

#### 编程用法

|  |
| --- |
| **模块参数：**  `primaryConstraintSrc` | 当 `primaryConstraintSrc` 为 `'Dialog'` 时，使用 `primaryConstraint` 设置主约束向量 |
| **类型：** character vector |
| **值：** `'Port'` | `'Dialog'` | 主约束向量，指定为 3 元素向量 |
| **默认值：** `'Dialog'` |

### **次约束 (CCF)** — 次约束 `Dialog`（默认）| `Port`

次约束向量源，指定为 `Port` 或 `Dialog`。

- `Port` — 通过 **C1b** 端口指定次约束数组。
- `Dialog` — 在随附文本框中指定端口约束 3 元素向量（默认值为 `[0 1 0]`）。

在主对准向量与主约束向量对准后，为完整定义旋转，模块尝试将次对准向量与旋转向量对准。旋转向量应为次约束向量。

主约束仅对自定义指向模式启用，而次约束始终启用。

#### 依赖关系

要在文本框中指定端口对准数组，请将此参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：**  `secondaryConstraintSrc` | 当 `secondaryConstraintSrc` 为 `'Dialog'` 时，使用 `secondaryConstraint` 设置次约束向量 |
| **类型：** character vector |
| **值：** `'Port'` | `'Dialog'` | 次约束向量，指定为 3 元素向量 |
| **默认值：** `'Dialog'` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2020b 中引入**

### R2023a: Attitude Profile 模块更新

为支持理想化姿态控制工作流，Attitude Profile 模块新增了参数和输出端口：

- **从当前姿态到更新姿态的输出旋转**参数
- **输出姿态**参数
- **qnew** 端口

## 描述

计算最短四元数旋转

Attitude Profile 模块计算将主对准向量与主约束向量对准的最短四元数旋转。四元数采用标量在前约定定义。Aerospace Blockset™ 使用采用标量在前约定定义的四元数。

将主约束提供为以下指向模式之一：

- `Point at nadir`
- `Point at celestial body`
- `Point at LatLonAlt`

或通过自定义约束向量提供。然后，模块在不破坏主对准的前提下，尽可能对准次对准向量和约束向量。

该库包含三个版本的 Attitude Profile 模块，已针对这些常见姿态控制模式预配置：

- Attitude Profile (Nadir Pointing) — `Point at nadir`
- Attitude Profile (Geographic Pointing) — `Point at LatLonAlt`
- Attitude Profile (Sun Tracking) — `Point at celestial body`，其中 Sun 作为天体目标

有关 Attitude Profile 模块使用的坐标系的详细信息，请参阅算法。
