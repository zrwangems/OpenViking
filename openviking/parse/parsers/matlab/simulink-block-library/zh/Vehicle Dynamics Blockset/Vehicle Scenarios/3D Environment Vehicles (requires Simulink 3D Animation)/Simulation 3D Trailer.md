---
type: simulink-block
title: 'Simulation 3D Trailer'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dtrailer'
documentation_source_path: 'ref/simulation3dtrailer.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Trailer

## 端口

### 输入

### **Translation** — 车辆平移 `5`-by-`3` 数组（默认）| `7`-by-`3` 数组 | `3`-by-`3` 数组

车辆和车轮平移，单位为 m。数组维度对于单轴拖车为 `3`-by-`3`，对于双轴拖车为 `5`-by-`3`，对于三轴拖车为 `7`-by-`3`，其中：

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 车辆沿惯性车辆 Z-down *X*、*Y* 和 *Z* 轴的平移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — 车轮相对于车辆沿车辆 Z-down *X*、*Y* 和 *Z* 轴的平移。

该信号包含根据轴和车轮位置的平移信息。

对于单轴拖车：

Translation=[XvYvZvXLYLZLXRYRZR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 左轮，*XL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 左轮，*YL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 左轮，*ZL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 右轮，*XR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 右轮，*YR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 右轮，*ZR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |

对于双轴拖车：

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*XFL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*YFL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*ZFL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*XFR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*YFR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*ZFR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*XRL* | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*YRL* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*ZRL* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*XRR* | `Translation(5,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*YRR* | `Translation(5,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*ZRR* | `Translation(5,3)` | 车辆 Z-down *Z* 轴 |

对于三轴拖车：

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXMLYMLZMLXMRYMRZMRXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*XFL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*YFL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*ZFL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*XFR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*YFR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*ZFR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 中左轮，*XML*（用于三轴拖车） | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 中左轮，*YML* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 中左轮，*ZML* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |
| 中右轮，*XMR* | `Translation(5,1)` | 车辆 Z-down *X* 轴 |
| 中右轮，*YMR* | `Translation(5,2)` | 车辆 Z-down *Y* 轴 |
| 中右轮，*ZMR* | `Translation(5,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*XRL* | `Translation(6,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*YRL* | `Translation(6,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*ZRL* | `Translation(6,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*XRR* | `Translation(7,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*YRR* | `Translation(7,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*ZRR* | `Translation(7,3)` | 车辆 Z-down *Z* 轴 |

### **Rotation** — 车辆旋转 `5`-by-`3` 数组（默认）| `7`-by-`3` 数组 | `3`-by-`3` 数组

车辆和车轮旋转，单位为 rad。数组维度对于单轴拖车为 `3`-by-`3`，对于双轴拖车为 `5`-by-`3`，对于三轴拖车为 `7`-by-`3`，其中：

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆绕惯性车辆 Z-down *X*、*Y* 和 *Z* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — 车轮相对于车辆绕车辆 Z-down *X*、*Y* 和 *Z* 轴的旋转。

该信号包含根据轴和车轮位置的旋转信息。

对于单轴拖车：

Rotation=[RollvPitchvYawvRollLPitchLYawLRollRPitchRYawR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 左轮，*RollL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 左轮，*PitchL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 左轮，*YawL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 右轮，*RollR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 右轮，*PitchR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 右轮，*YawR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |

对于双轴拖车：

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*RollFL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*PitchFL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*YawFL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*RollFR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*PitchFR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*YawFR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*RollRL* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*PitchRL* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*YawRL* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*RollRR* | `Rotation(5,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*PitchRR* | `Rotation(5,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*YawRR* | `Rotation(5,3)` | 车辆 Z-down *Z* 轴 |

对于三轴拖车：

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollMLPitchMLYawMLRollMRPitchMRYawMRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*RollFL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*PitchFL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*YawFL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*RollFR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*PitchFR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*YawFR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 中左轮，*RollML* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 中左轮，*PitchML* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 中左轮，*YawML* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |
| 中右轮，*RollMR* | `Rotation(5,1)` | 车辆 Z-down *X* 轴 |
| 中右轮，*PitchMR* | `Rotation(5,2)` | 车辆 Z-down *Y* 轴 |
| 中右轮，*YawMR* | `Rotation(5,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*RollRL* | `Rotation(6,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*PitchRL* | `Rotation(6,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*YawRL* | `Rotation(6,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*RollRR* | `Rotation(7,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*PitchRR* | `Rotation(7,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*YawRR* | `Rotation(7,3)` | 车辆 Z-down *Z* 轴 |

## 参数

#### 车辆参数

### **Type** — 拖车类型 `Two-axle trailer`（默认）| `Three-axle trailer` | `One-axle trailer`

拖车类型。有关拖车尺寸，请参阅：

- 单轴拖车
- 双轴拖车
- 三轴拖车

### **Name** — 车辆名称 `SimulinkVehicle1`（默认）| 字符向量

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Vehicle with Ground Following 和 Simulation 3D Vehicle 模块的数量。

#### 初始值

### **Initial array values to translate vehicle per part, Translation** — 车辆初始平移 zeros( 5, 3 )（默认）| zeros( 7, 3 ) | zeros( 3, 3 )

初始车辆和车轮平移，单位为 m。数组维度对于单轴拖车为 `3`-by-`3`，对于双轴拖车为 `5`-by-`3`，对于三轴拖车为 `7`-by-`3`，其中：

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 初始车辆沿惯性车辆 Z-down 坐标系 *X*、*Y* 和 *Z* 轴的平移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — 初始车轮相对于车辆沿车辆 Z-down *X*、*Y* 和 *Z* 轴的平移。

该信号包含根据轴和车轮位置的平移信息。

对于单轴拖车：

Translation=[XvYvZvXLYLZLXRYRZR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 左轮，*XL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 左轮，*YL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 左轮，*ZL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 右轮，*XR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 右轮，*YR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 右轮，*ZR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |

对于双轴拖车：

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*XFL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*YFL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*ZFL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*XFR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*YFR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*ZFR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*XRL* | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*YRL* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*ZRL* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*XRR* | `Translation(5,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*YRR* | `Translation(5,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*ZRR* | `Translation(5,3)` | 车辆 Z-down *Z* 轴 |

对于三轴拖车：

Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXMLYMLZMLXMRYMRZMRXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左轮，*XFL* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左轮，*YFL* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左轮，*ZFL* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右轮，*XFR* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右轮，*YFR* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右轮，*ZFR* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 中左轮，*XML*（用于三轴拖车） | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 中左轮，*YML* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 中左轮，*ZML* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |
| 中右轮，*XMR* | `Translation(5,1)` | 车辆 Z-down *X* 轴 |
| 中右轮，*YMR* | `Translation(5,2)` | 车辆 Z-down *Y* 轴 |
| 中右轮，*ZMR* | `Translation(5,3)` | 车辆 Z-down *Z* 轴 |
| 后左轮，*XRL* | `Translation(6,1)` | 车辆 Z-down *X* 轴 |
| 后左轮，*YRL* | `Translation(6,2)` | 车辆 Z-down *Y* 轴 |
| 后左轮，*ZRL* | `Translation(6,3)` | 车辆 Z-down *Z* 轴 |
| 后右轮，*XRR* | `Translation(7,1)` | 车辆 Z-down *X* 轴 |
| 后右轮，*YRR* | `Translation(7,2)` | 车辆 Z-down *Y* 轴 |
| 后右轮，*ZRR* | `Translation(7,3)` | 车辆 Z-down *Z* 轴 |

### **用于按部件旋转车辆的初始数组值，Rotation** — 车辆初始旋转 zeros( 5, 3 ) (default) | zeros( 7, 3 ) | zeros( 3, 3 )

车辆和车轮绕车辆 Z-down 的 *X*、*Y* 和 *Z* 轴的初始旋转，单位为 rad。

对于双轴挂车，数组维度为 `5`-by-`3`；对于三轴挂车，数组维度为 `7`-by-`3`，其中：

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆绕惯性车辆 Z-down 坐标系的 *X*、*Y* 和 *Z* 轴的初始旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — 车轮相对于车辆绕车辆 Z-down 的 *X*、*Y* 和 *Z* 轴的初始旋转。

该信号包含根据轴和车轮位置的平移信息。

对于单轴挂车：

Rotation=[RollvPitchvYawvRollLPitchLYawLRollRPitchRYawR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 左车轮，*RollL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 左车轮，*PitchL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 左车轮，*YawL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 右车轮，*RollR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 右车轮，*PitchR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 右车轮，*YawR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |

对于双轴挂车：

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左车轮，*RollFL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左车轮，*PitchFL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左车轮，*YawFL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右车轮，*RollFR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右车轮，*PitchFR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右车轮，*YawFR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后左车轮，*RollRL* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 后左车轮，*PitchRL* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后左车轮，*YawRL* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |
| 后右车轮，*RollRR* | `Rotation(5,1)` | 车辆 Z-down *X* 轴 |
| 后右车轮，*PitchRR* | `Rotation(5,2)` | 车辆 Z-down *Y* 轴 |
| 后右车轮，*YawRR* | `Rotation(5,3)` | 车辆 Z-down *Z* 轴 |

对于三轴挂车：

Rotation=[RollvPitchvYawvRollFLPitchFLYawFLRollFRPitchFRYawFRRollMLPitchMLYawMLRollMRPitchMRYawMRRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 前左车轮，*RollFL* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 前左车轮，*PitchFL* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 前左车轮，*YawFL* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前右车轮，*RollFR* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前右车轮，*PitchFR* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前右车轮，*YawFR* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 中左车轮，*RollML* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 中左车轮，*PitchML* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 中左车轮，*YawML* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |
| 中右车轮，*RollMR* | `Rotation(5,1)` | 车辆 Z-down *X* 轴 |
| 中右车轮，*PitchMR* | `Rotation(5,2)` | 车辆 Z-down *Y* 轴 |
| 中右车轮，*YawMR* | `Rotation(5,3)` | 车辆 Z-down *Z* 轴 |
| 后左车轮，*RollRL* | `Rotation(6,1)` | 车辆 Z-down *X* 轴 |
| 后左车轮，*PitchRL* | `Rotation(6,2)` | 车辆 Z-down *Y* 轴 |
| 后左车轮，*YawRL* | `Rotation(6,3)` | 车辆 Z-down *Z* 轴 |
| 后右车轮，*RollRR* | `Rotation(7,1)` | 车辆 Z-down *X* 轴 |
| 后右车轮，*PitchRR* | `Rotation(7,2)` | 车辆 Z-down *Y* 轴 |
| 后右车轮，*YawRR* | `Rotation(7,3)` | 车辆 Z-down *Z* 轴 |

### **采样时间** — Sample time `-1` (default) | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Trailer 模块对模型进行仿真需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现挂车

**注意**

使用 Simulation 3D Trailer 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Trailer 模块在 3D 仿真环境中实现具有单轴、双轴或三轴的挂车。

要使用 Simulation 3D Trailer 模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Trailer 模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

模块输入使用 SAE J6701 中定义的车辆 Z-down *右手* (RH) *笛卡尔* 坐标系。该坐标系为惯性坐标系，并且初始时与车辆几何中心对齐：

- *X* 轴 — 沿车辆纵轴指向前方
- *Y* 轴 — 沿车辆横轴指向右侧
- *Z* 轴 — 指向下方

**提示**

验证 Simulation 3D Trailer 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Vehicle 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡中，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Trailer — `-1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order。
