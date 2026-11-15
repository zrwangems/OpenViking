---
type: simulink-block
title: 'Simulation 3D Dolly'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3ddolly'
documentation_source_path: 'ref/simulation3ddolly.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Dolly

## 端口

### 输入

### **Translation** — Dolly 平移 `5`-by-`3` 数组 (默认) | `8`-by-`3` 数组 | `11`-by-`3` 数组

Dolly、车轴和车轮分别沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移，单位为 m。数组维度取决于 **Type** 参数。

| Type 参数 | 数组维度 |
| --- | --- |
| `One-axle dolly` (默认) | `5`-by-`3` 数组 |
| `Two-axle dolly` | `8`-by-`3` 数组 |
| `Three-axle dolly` | `11`-by-`3` 数组 |

该信号包含根据 Dolly、车轴和车轮位置提供的平移信息。

| **信号索引** | 描述 |
| --- | --- |
| `Translation(1,1)`  `Translation(1,2)`  `Translation(1,3)` | Dolly 平移，`Vehicle`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴 |
| `Translation(2,1)`  `Translation(2,2)`  `Translation(2,3)` | 挂接插座，`HitchSocket`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(3,1)`  `Translation(3,2)`  `Translation(3,3)` | 车轴一，`Axle1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(4,1)`  `Translation(4,2)`  `Translation(4,3)` | 车轴一左轮，`Wheel_L1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(5,1)`  `Translation(5,2)`  `Translation(5,3)` | 车轴一右轮，`Wheel_R1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(6,1)`  `Translation(6,2)`  `Translation(6,3)` | 车轴二，`Axle2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(7,1)`  `Translation(7,2)`  `Translation(7,3)` | 车轴二左轮，`Wheel_L2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(8,1)`  `Translation(8,2)`  `Translation(8,3)` | 车轴二右轮，`Wheel_R2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(9,1)`  `Translation(9,2)`  `Translation(9,3)` | 车轴三，`Axle3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(10,1)`  `Translation(10,2)`  `Translation(10,3)` | 车轴三左轮，`Wheel_L3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(11,1)`  `Translation(11,2)`  `Translation(11,3)` | 车轴三右轮，`Wheel_R3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |

### **Rotation** — Dolly 旋转 `5`-by-`3` 数组 (默认) | `8`-by-`3` 数组 | `11`-by-`3` 数组

Dolly、车轴和车轮分别绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转，单位为 m。数组维度取决于 **Type** 参数。

| Type 参数 | 数组维度 |
| --- | --- |
| `One-axle dolly` (默认) | `5`-by-`3` 数组 |
| `Two-axle dolly` | `8`-by-`3` 数组 |
| `Three-axle dolly` | `11`-by-`3` 数组 |

该信号包含根据 Dolly、车轴和车轮位置提供的旋转信息。

| **信号索引** | 描述 |
| --- | --- |
| `Rotation(1,1)`  `Rotation(1,2)`  `Rotation(1,3)` | Dolly 旋转，`Vehicle`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴 |
| `Rotation(2,1)`  `Rotation(2,2)`  `Rotation(2,3)` | 挂接插座，`HitchSocket`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(3,1)`  `Rotation(3,2)`  `Rotation(3,3)` | 车轴一，`Axle1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(4,1)`  `Rotation(4,2)`  `Rotation(4,3)` | 车轴一左轮，`Wheel_L1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(5,1)`  `Rotation(5,2)`  `Rotation(5,3)` | 车轴一右轮，`Wheel_R1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(6,1)`  `Rotation(6,2)`  `Rotation(6,3)` | 车轴二，`Axle2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(7,1)`  `Rotation(7,2)`  `Rotation(7,3)` | 车轴二左轮，`Wheel_L2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(8,1)`  `Rotation(8,2)`  `Rotation(8,3)` | 车轴二右轮，`Wheel_R2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(9,1)`  `Rotation(9,2)`  `Rotation(9,3)` | 车轴三，`Axle3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(10,1)`  `Rotation(10,2)`  `Rotation(10,3)` | 车轴三左轮，`Wheel_L3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(11,1)`  `Rotation(11,2)`  `Rotation(11,3)` | 车轴三右轮，`Wheel_R3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |

## 参数

### 车辆参数

### **Type** — 类型 `One-axle dolly` (默认) | `Two-axle dolly` | `Three-axle dolly`

使用 **Type** 参数指定 Dolly 上的车轴数。下表提供了指向 Dolly 尺寸的链接。

| **Type** 设置 | Dolly 尺寸 |
| --- | --- |
| `One-axle dolly` | 单轴 Dolly |
| `Two-axle dolly` | 双轴 Dolly |
| `Three-axle dolly` | 三轴 Dolly |

### **Name** — Dolly 的名称 `SimulinkVehicle1` (默认) | character vector

Dolly 的名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Vehicle 模块的数量。

### **Sample time** — 采样时间 `-1` (默认) | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

### 初始值

### **Initial array values to translate vehicle per part, Translation** — 车辆初始平移 zeros( 5, 3 ) (默认) | zeros( 8, 3 ) | zeros( 11, 3 )

Dolly、车轴和车轮分别沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的初始平移，单位为 m。数组维度取决于 **Type** 参数。

| Type 参数 | 数组维度 |
| --- | --- |
| `One-axle dolly` (默认) | `5`-by-`3` 数组 |
| `Two-axle dolly` | `8`-by-`3` 数组 |
| `Three-axle dolly` | `11`-by-`3` 数组 |

该参数包含根据 Dolly、车轴和车轮位置提供的初始平移值。

| **信号索引** | 描述 |
| --- | --- |
| `Translation(1,1)`  `Translation(1,2)`  `Translation(1,3)` | Dolly 平移，`Vehicle`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴 |
| `Translation(2,1)`  `Translation(2,2)`  `Translation(2,3)` | 挂接插座，`HitchSocket`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(3,1)`  `Translation(3,2)`  `Translation(3,3)` | 车轴一，`Axle1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(4,1)`  `Translation(4,2)`  `Translation(4,3)` | 车轴一左轮，`Wheel_L1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(5,1)`  `Translation(5,2)`  `Translation(5,3)` | 车轴一右轮，`Wheel_R1`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(6,1)`  `Translation(6,2)`  `Translation(6,3)` | 车轴二，`Axle2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(7,1)`  `Translation(7,2)`  `Translation(7,3)` | 车轴二左轮，`Wheel_L2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(8,1)`  `Translation(8,2)`  `Translation(8,3)` | 车轴二右轮，`Wheel_R2`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(9,1)`  `Translation(9,2)`  `Translation(9,3)` | 车轴三，`Axle3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(10,1)`  `Translation(10,2)`  `Translation(10,3)` | 车轴三左轮，`Wheel_L3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |
| `Translation(11,1)`  `Translation(11,2)`  `Translation(11,3)` | 车轴三右轮，`Wheel_R3`，沿车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的平移 |

### **Initial array values to rotate vehicle per part, Rotation** — 初始旋转 zeros( 5, 3 ) (默认) | zeros( 8, 3 ) | zeros( 11, 3 )

Dolly、车轴和车轮分别绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的初始旋转，单位为 m。数组维度取决于 **Type** 参数。

| Type 参数 | 数组维度 |
| --- | --- |
| `One-axle dolly` (默认) | `5`-by-`3` 数组 |
| `Two-axle dolly` | `8`-by-`3` 数组 |
| `Three-axle dolly` | `11`-by-`3` 数组 |

该参数包含根据 Dolly、车轴和车轮位置提供的初始旋转值。

| **信号索引** | 描述 |
| --- | --- |
| `Rotation(1,1)`  `Rotation(1,2)`  `Rotation(1,3)` | Dolly 旋转，`Vehicle`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴 |
| `Rotation(2,1)`  `Rotation(2,2)`  `Rotation(2,3)` | 挂接插座，`HitchSocket`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(3,1)`  `Rotation(3,2)`  `Rotation(3,3)` | 车轴一，`Axle1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(4,1)`  `Rotation(4,2)`  `Rotation(4,3)` | 车轴一左轮，`Wheel_L1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(5,1)`  `Rotation(5,2)`  `Rotation(5,3)` | 车轴一右轮，`Wheel_R1`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(6,1)`  `Rotation(6,2)`  `Rotation(6,3)` | 车轴二，`Axle2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(7,1)`  `Rotation(7,2)`  `Rotation(7,3)` | 车轴二左轮，`Wheel_L2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(8,1)`  `Rotation(8,2)`  `Rotation(8,3)` | 车轴二右轮，`Wheel_R2`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(9,1)`  `Rotation(9,2)`  `Rotation(9,3)` | 车轴三，`Axle3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(10,1)`  `Rotation(10,2)`  `Rotation(10,3)` | 车轴三左轮，`Wheel_L3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |
| `Rotation(11,1)`  `Rotation(11,2)`  `Rotation(11,3)` | 车轴三右轮，`Wheel_R3`，绕车辆 Z-down *X* 轴、*Y* 轴和 *Z* 轴的旋转 |

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Dolly 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现 Dolly

**注意**

使用 Simulation 3D Dolly 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Dolly 模块在 3D 仿真环境中实现 Dolly。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将此模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J6701 中定义的车辆 Z-down *右手* (RH) *笛卡尔*坐标系。该坐标系为惯性坐标系，并且初始时与车辆几何中心对齐：

- *X* 轴 — 沿车辆纵轴，指向车辆前方
- *Y* 轴 — 沿车辆横轴，指向右侧
- *Z* 轴 — 指向下方

**提示**

请验证 Simulation 3D Dolly 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Dolly 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好这些数据。要检查模块执行顺序，请右键单击每个模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Dolly — `-1`

有关执行顺序的更多信息，请参阅控制和显示执行顺序。
