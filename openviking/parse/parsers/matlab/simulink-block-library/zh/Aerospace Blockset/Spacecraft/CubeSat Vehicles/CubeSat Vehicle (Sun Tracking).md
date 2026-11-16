---
type: simulink-block
title: 'CubeSat Vehicle Earth (Nadir) Pointing'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft / CubeSat Vehicles'
documentation_page: 'cubesatvehicleearthnadirpointing'
documentation_source_path: 'cubesatvehicleearthnadirpointing.html'
language: zh-CN
chinese_source: worker-translation
---

# CubeSat Vehicle Earth (Nadir) Pointing

## 端口

### 输入

### **AECEF (m/s2)** — 大小为 3 的航天器加速度矢量

用于轨道传播的航天器重力加速度（包括重力），指定为大小为 3 的矢量，单位为 m/s2。

**数据类型:** `single` | `double`

### **1st AlignmentBody** — 主对准矢量三元素矢量

主对准矢量，在本体坐标系中，用于与主约束矢量对准。

**数据类型:** `double`

### **1st ConstraintECI** — 主约束矢量三元素矢量

主约束矢量，指定主对准矢量要对准的方向。

#### 依赖项

当 **指向模式** 设置为 `Earth (Nadir) Pointing` 或 `Sun Tracking` 时，此端口不可用，因为它们具有隐含的主约束矢量。

**数据类型:** `double`

### **1st AlignmentBody** — 主对准矢量三元素矢量

主对准矢量，在本体坐标系中，用于与主约束矢量对准。

**数据类型:** `double`

### **1st ConstraintECI** — 主约束矢量三元素矢量

主约束矢量，指定主对准矢量要对准的方向。

#### 依赖项

- 方向取决于 **约束坐标系**。
- 当 **指向模式** 设置为 `Earth (Nadir) Pointing` 或 `Sun Tracking` 时，此端口不可用，因为它们具有隐含的主约束矢量。

**数据类型:** `double`

### **2nd AlignmentBody** — 次对准矢量三元素矢量

次对准矢量，在本体坐标系中，用于与次约束矢量对准。

**数据类型:** `double`

### **2nd ConstraintECI** — 次约束矢量三元素矢量

次约束矢量，指定次对准矢量要对准的方向。

#### 依赖项

方向取决于 **约束坐标系**。

**数据类型:** `double`

### 输出

### **XECEF** — CubeSat 位置三元素矢量

地心地球固连的 CubeSat 位置分量，指定为 3×1 数组。

**数据类型:** `double`

### **VECEF** — 速度分量 3×1 数组

地心地球固连的速度分量，指定为 3×1 数组。

**数据类型:** `double`

### **qECI2Body** — 四元数旋转 4×1 数组

从地心惯性坐标系到本体坐标系的四元数旋转。

**数据类型:** `double`

### **qECEF2Body** — 四元数数组 4×1 数组

从地心地球固连坐标系到本体坐标系的四元数旋转。

**数据类型:** `double`

## 参数

### **起始日期 [儒略日]** — 仿真的初始起始日期 `2458488`（默认）| 儒略日

仿真的初始起始日期。模块使用此日期定义初始条件。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

#### 编程使用

|  |
| --- |
| **模块参数:** `sim_t0` |
| **类型:** character vector |
| **值:** 儒略日 |
| **默认值:** `'2458488'` |

### CubeSat 轨道

### **输入方法** — 初始航天器 `Keplerian Orbital Elements`（默认）| `ECI Position and Velocity` | `ECEF Position and Velocity` | `Geodetic LatLonAlt and Velocity in NED`

初始航天器位置和速度输入方法。

#### 依赖项

选择 `Keplerian Orbital Elements` 输入方法会启用以下参数：

- **ECI 坐标系历元 [儒略日]**
- **半长轴 [m]**
- **偏心率**
- **倾角 [deg]**
- **升交点赤经 [deg]**
- **近地点幅角 [deg]**
- **真近点角 [deg]**
- **真经度 [deg]（圆轨道赤道）**
- **纬度幅角 [deg]（圆轨道倾斜）**
- **近地点经度 [deg]（椭圆轨道赤道）**

选择 `ECI Position and Velocity` 输入方法会启用以下参数：

- **ECI 坐标系历元 [儒略日]**
- **ECI 位置矢量 [m]**
- **ECI 速度矢量 [m/s]**

选择 `ECEF Position and Velocity` 输入方法会启用以下参数：

- **ECEF 位置矢量 [m]**
- **ECEF 速度矢量 [m/s]**

选择 `Geodetic LatLonAlt and Velocity in NED` 输入方法会启用以下参数：

- **大地纬度、经度、高度 [deg, deg, m]**
- **NED 速度矢量 [m/s]**

#### 编程使用

|  |
| --- |
| **模块参数:** `method` |
| **类型:** character vector |
| **值:** `'Keplerian Orbital Elements'` | `'ECI Position and Velocit'` | `'ECEF Position and Velocity'` | `'Geodetic LatLonAlt and Velocity in NED'` |
| **默认值:** `'Keplerian Orbital Elements'` |

### **ECI 坐标系历元 [儒略日]** — ECI 坐标系历元 `2451545`（默认）| 儒略日

ECI 坐标系历元，指定为儒略日。

**提示**

要计算特定日期的儒略日，请使用 `juliandate` 函数。

#### 编程使用

|  |
| --- |
| **模块参数:** `epoch` |
| **类型:** character vector |
| **值:** 儒略日格式 |
| **默认值:** `'2451545'` |

### **半长轴 [m]** — CubeSat 半长轴 `6878137`（默认）| 以米为单位的轴

CubeSat 半长轴（最长轨道直径的一半），以 m 为单位指定。

#### 编程使用

|  |
| --- |
| **模块参数:** `a` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'6878137'` |

### **偏心率** — 轨道偏心率 `0`（默认）| 大于或等于 0 的偏心率

CubeSat 轨道偏离完美圆形的程度。

#### 编程使用

|  |
| --- |
| **模块参数:** `ecc` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **倾角 [deg]** — CubeSat 轨道平面倾斜角 `0` | 0 到 180 之间的度

CubeSat 轨道平面倾斜角，指定为 0 到 180 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `incl` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **升交点赤经 [deg]** — 赤道面内的角距离 `0`（默认）| 0 到 360 之间的度

从 *x* 轴到升交点位置（卫星从南向北穿过赤道的点）在赤道面内的角距离，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `omega` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **近地点幅角 [deg]** — 从 CubeSat 本体升交点到近地点的角度 `0`（默认）| 0 到 360 之间的度

从 CubeSat 本体升交点到近地点（轨道距地球最近点）的角度，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `argp` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **真近点角 [deg]** — 近地点与 CubeSat 当前位置之间的角度 `0`（默认）| 0 到 360 之间的度

近地点（轨道距地球最近点）与 CubeSat 当前位置之间的角度，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `nu` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **真经度 [deg]（圆轨道赤道）** — 近地点 *x* 轴与 CubeSat 位置矢量之间的角度 `0`（默认）| 0 到 360 之间的度

近地点 *x* 轴与 CubeSat 位置矢量之间的角度，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `truelon` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **纬度幅角 [deg]（圆轨道倾斜）** — 升交点与卫星位置矢量之间的角度 `0`（默认）| 0 到 360 之间的度

升交点与卫星位置矢量之间的角度，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `arglat` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **近地点经度 [deg]（椭圆轨道赤道）** — 近地点 *x* 轴与偏心率矢量之间的角度 `0`（默认）| 0 到 360 之间的度

近地点 *x* 轴与偏心率矢量之间的角度，指定为 0 到 360 deg 之间。

#### 编程使用

|  |
| --- |
| **模块参数:** `lonper` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'0'` |

### **ECI 位置矢量 [m]** — 笛卡尔位置矢量 `[0 0 0]`（默认）| 矢量

在 **起始日期** 时卫星在 ECI 坐标系中的笛卡尔位置矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `r_eci` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **ECI 速度矢量 [m/s]** — 笛卡尔速度矢量 `[0 0 0]`（默认）| 速度矢量

在 **起始日期** 时卫星在 ECI 坐标系中的笛卡尔速度矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `v_eci` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **ECEF 位置矢量 [m]** — 笛卡尔位置矢量 `[0 0 0]`（默认）| 矢量

在 **起始日期** 时卫星在 ECEF 坐标系中的笛卡尔位置矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `r_ecef` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **ECEF 速度矢量 [m/s]** — 笛卡尔速度矢量 `[0 0 0]`（默认）| 速度矢量

在 **起始日期** 时卫星在 ECEF 坐标系中的笛卡尔速度矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `v_ecef` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **大地纬度、经度、高度 [deg, deg, m]** — 大地纬度和经度以及高度 `[0 0 0]`（默认）| 速度矢量

大地纬度和经度（以 deg 为单位），以及 WGS84 椭球上方的高度（以 m 为单位）。

#### 编程使用

|  |
| --- |
| **模块参数:** `lla` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **NED 速度矢量 [m/s]** — 本体速度 `[0 0 0]`（默认）| 速度矢量

相对于地心地球固连（ECEF）的本体速度，在北-东-地（NED）坐标系中表示，指定为矢量，单位为 m/s。

#### 编程使用

|  |
| --- |
| **模块参数:** `v_ned` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### CubeSat 姿态

### **初始欧拉角（滚转、俯仰、偏航）[deg]** — 初始欧拉旋转角 `[0 0 0]`（默认）| 矢量 | 度

本体坐标系与 NED 坐标系之间的初始欧拉旋转角（滚转、俯仰、偏航），以度为单位指定。

#### 编程使用

|  |
| --- |
| **模块参数:** `euler` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **初始本体角速率 [deg/s]** — 初始角速率 `[0 0 -0.05168]`（默认）| 矢量

相对于 NED 坐标系的初始角速率，在本体坐标系中表示，指定为矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `pqr` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'[0 0 0]'` |

### **指向模式** — CubeSat 航天器指向模式 `Earth (Nadir) Pointing`（默认）| `Sun Tracking` | `Custom Pointing` | `Standby (Off)`

CubeSat 航天器指向模式，指定为 `Earth (Nadir) Pointing`、`Sun Tracking` 或 `Custom Pointing`。CubeSat 航天器使用该指向模式进行精确姿态控制。若不进行姿态控制，请选择 `Standby (Off)`。

#### 编程使用

|  |
| --- |
| **模块参数:** `pointingMode` |
| **类型:** character vector |
| **值:** `'Earth (Nadir) Pointing'` | `'Sun Tracking'` | `'Custom Pointing'` | `'Standby (Off)'` |
| **默认值:** `'Earth (Nadir) Pointing'` |

### **主对准矢量（Body 相对于 BCM）** — 主对准矢量 `Dialog`（默认）| `Input port`

主对准矢量，在本体坐标系中，用于与主约束矢量对准。

#### 依赖项

- 选择 `Dialog` 会启用一个文本框，您可以在其中指定主对准矢量。默认值为 `[0 0 1]`。
- 选择 `Input port` 会启用 1st AlignmentBody 输入端口，您可以在该端口指定主对准矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `firstAlign` |
| **类型:** character vector |
| **值:** 矢量 |
| **默认值:** `'[0 0 1]'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `firstAlignExt` |
| **类型:** character vector |
| **值:** `'Input port'` | `'Dialog'` |
| **默认值:** `'Dialog'` |

### **次对准矢量（Body 相对于 BCM）** — 次对准矢量 `Dialog`（默认）| `Input port`

次对准矢量，在本体坐标系中，用于与次约束矢量对准。

#### 依赖项

- 选择 `Dialog` 会启用一个文本框，您可以在其中指定次对准矢量。默认值为 `[0 1 0]`。
- 选择 `Input port` 会启用 2nd AlignmentBody 输入端口，您可以在该端口指定次对准矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `secondAlign` |
| **类型:** character vector |
| **值:** 矢量 |
| **默认值:** `'[0 1 0]'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `secondAlignExt` |
| **类型:** character vector |
| **值:** `'Input port'` | `'Dialog'` |
| **默认值:** `'Dialog'` |

### **约束坐标系** — 约束坐标系 `ECI Axes`（默认）| `ECEF Axes` | `NED Axes` | `Body-Fixed Axes`

约束坐标系，指定为 `ECI Axes`、`ECEF Axes`、`NED Axes` 或 `Body-Fixed Axes`。

#### 编程使用

|  |
| --- |
| **模块参数:** `constraintCoord` |
| **类型:** character vector |
| **值:** `'ECI Axes'` | `'ECEF Axes'` | `'NED Axes'` | `'Body-Fixed Axes'` |
| **默认值:** `'ECI Axes'` |

### **主约束矢量（相对于 BCM）** — 主约束矢量 `Dialog`（默认）| `Input port`

主约束矢量，在本体坐标系中，用于与主对准矢量对准。

#### 依赖项

- 当 **指向模式** 为 `Earth (Nadir) Pointing` 或 `Sun Tracking` 时，此参数被禁用。
- 选择 `Dialog` 会启用一个文本框，您可以在其中指定主约束矢量。默认值为 `[1 0 0]`。
- 选择 `Input port` 会启用 1st constraintBody 输入端口，您可以在该端口指定主约束矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `firstRef` |
| **类型:** character vector |
| **值:** 矢量 |
| **默认值:** `'[1 0 0]'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `firstRefExt` |
| **类型:** character vector |
| **值:** `'Input port'` | `'Dialog'` |
| **默认值:** `'Dialog'` |

### **次约束矢量（相对于 BCM）** — 次约束矢量 `Dialog`（默认）| `Input port`

次约束矢量，在本体坐标系中，用于与次对准矢量对准。

#### 依赖项

- 选择 `Dialog` 会启用一个文本框，您可以在其中指定次约束矢量。默认值为 `[0 0 1]`。
- 选择 `Input port` 会启用 2nd constraintBody 输入端口，您可以在该端口指定次约束矢量。

#### 编程使用

|  |
| --- |
| **模块参数:** `secondRef` |
| **类型:** character vector |
| **值:** 矢量 |
| **默认值:** `'[0 0 1]'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `secondRefExt` |
| **类型:** character vector |
| **值:** `'Input port'` | `'Dialog'` |
| **默认值:** `'Dialog'` |

### 任务分析

### **分析运行时间源** — 任务分析实时脚本的运行时间源 `Dialog`（默认）| `Model Stop Time`

任务分析实时脚本的运行时间源，指定为：

- `Dialog` — 在 **运行时间** 参数中定义。
- `Model Stop Time` — 在模型配置参数 **停止时间** 中定义。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionRTSource` |
| **类型:** character vector |
| **值:** `'Dialog'` | `'Model StopTime'` |
| **默认值:** `'Dialog'` |

### **运行时间 [sec]** — 任务分析实时脚本的运行时间 `6*60*60`（默认）| 标量

任务分析实时脚本的运行时间，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionRT` |
| **类型:** character vector |
| **值:** 标量 |
| **默认值:** `'6*60*60'` |

### **地面站大地纬度、经度 [deg, deg]** — 地面站位置 [42, -71]（默认）| 矢量

地面站位置，指定为矢量，采用大地纬度和经度，单位为 deg、deg。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionGS` |
| **类型:** character vector |
| **值:** 矢量 |
| **默认值:** `'[42, -71]'` |

### **运行 TOI 分析** — 启用关注时间任务分析 on（默认）| off

选中此复选框以在任务分析实时脚本中启用关注时间分析。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionTOICheck` |
| **类型:** character vector |
| **值:** `'on'` | `'off'` |
| **默认值:** `'on'` |

### **关注时间 [儒略日]** — 任务分析实时脚本的关注时间 `[]`（默认）| 儒略日

关注时间任务分析，指定为儒略日。要使用仿真开始日期，请输入空数组（`[]`）。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionTOI` |
| **类型:** character vector |
| **值:** 儒略日 |
| **默认值:** `'[]'` |

### **相机视场（FOV）半角 (deg)** — 视场半角 55（默认）| `[]` | 标量

天底指向相机的视场半角。若要从分析中排除，请输入空数组（`[]`）。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionEta` |
| **类型:** character vector |
| **值:** `'[]'` | 标量 |
| **默认值:** `'55'` |

### **实时脚本文件名** — 任务分析实时脚本报告的文件名 空白项（默认）| 实时脚本文件名

任务分析实时脚本报告的文件名，生成为实时脚本。要创建格式为 `CubeSatMissionReport_currentdate.mlx` 的默认任务分析报告，请将此参数留空。要创建任务分析报告的实时脚本，请点击 **创建实时脚本报告** 按钮。

#### 依赖项

要使用指定文件名创建实时脚本，请点击 **创建实时脚本报告** 按钮。如果此参数留空，模块将创建一个具有默认文件名的实时脚本。

#### 编程使用

|  |
| --- |
| **模块参数:** `missionName` |
| **类型:** character vector |
| **值:** 空白项 | 文件名 |
| **默认值:** 空白项 |

### **创建实时脚本报告** — 分析任务并创建实时脚本报告 按钮

要以实时脚本格式分析任务并创建报告，请点击此按钮。要创建格式为 `CubeSatMissionReport_currentdate.mlx` 的默认任务分析报告，请将此参数留空。要创建任务分析报告的实时脚本，请点击 **创建实时脚本报告** 按钮。

#### 依赖项

要使用 **实时脚本文件名** 中指定的文件名创建实时脚本，请点击 **创建实时脚本报告** 按钮。如果 **实时脚本文件名** 留空，模块将创建一个具有默认文件名的实时脚本。

## 所属库

Aerospace Blockset / Spacecraft / CubeSat Vehicles

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

### R2021a: CubeSat Vehicle 现在在 ECI 坐标系中传播

CubeSat Vehicle 现在使用 `aeroiersdata.mat` 文件中的地球定向参数数据在 ECI 坐标系中传播。结果与之前版本不同，但比之前版本的模块更准确。

## 描述

对主对准矢量指向地球中心的 CubeSat 航天器建模

CubeSat Vehicle 模块对 CubeSat 航天器建模，以提供高级任务规划/快速原型选项，从而一次一个卫星地快速建模和传播卫星轨道。（要同时传播多个卫星，请参阅 Orbit Propagator 模块。）为适应星座规划工作流，您还可以在一个模型中多次使用这些模块。为航天器指定以下信息：

- 初始轨道状态
- 姿态控制（指向）模式

该库包含三个版本的 CubeSat Vehicle 模块，预配置用于这些常见姿态控制模式。要选择这些配置，请设置 **指向模式** 参数。

- CubeSat Vehicle Earth (Nadir) Pointing — 主对准矢量指向地球中心
- CubeSat Vehicle Sun Tracking — 主对准矢量指向太阳
- CubeSat Vehicle Custom Pointing — 自定义对准和约束矢量
