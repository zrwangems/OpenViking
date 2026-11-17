---
type: simulink-block
title: 'Simulation 3D Probabilistic Radar Configuration'
family: 'simulation-3d'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dprobabilisticradarconfiguration'
documentation_source_path: 'ref/simulation3dprobabilisticradarconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Probabilistic Radar Configuration

## 端口

未在 R2025b 中记录。

## 参数

### **Radar targets** — 对应于雷达目标的标识符 `[]`（默认）| positive integer | *L*-length vector of unique positive integers

对应于雷达目标的标识符，指定为 positive integer 或 *L*-length vector of unique positive integers。*L* 等于您要为其指定非默认雷达散射截面（RCS）的雷达目标数。

此表提供了雷达可在默认场景中检测到的标识符和对应对象类型，这些默认场景可从 Simulation 3D Scene Configuration 模块中选择。例如，要为建筑物和道路指定非默认 RCS，请将 **Radar targets** 设置为 `[1,7]`。如果您使用自定义场景，可以在 Unreal® Editor 中将新的对象类型分配给未使用的 ID。有关更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景包含未分配 ID 的对象，则为该对象分配 ID `0`。不支持检测车道标线。

| ID | 类型 |
| --- | --- |
| `0` | None/default |
| `1` | Building |
| `2` | *Not used* |
| `3` | Other |
| `4` | Pedestrians |
| `5` | Pole |
| `6` | Lane Markings |
| `7` | Road |
| `8` | Sidewalk |
| `9` | Vegetation |
| `10` | Vehicle |
| `11` | *Not used* |
| `12` | Generic traffic sign |
| `13` | Stop sign |
| `14` | Yield sign |
| `15` | Speed limit sign |
| `16` | Weight limit sign |
| `17-18` | *Not used* |
| `19` | Left and right arrow warning sign |
| `20` | Left chevron warning sign |
| `21` | Right chevron warning sign |
| `22` | *Not used* |
| `23` | Right one-way sign |
| `24` | *Not used* |
| `25` | School bus only sign |
| `26-38` | *Not used* |
| `39` | Crosswalk sign |
| `40` | *Not used* |
| `41` | Traffic signal |
| `42` | Curve right warning sign |
| `43` | Curve left warning sign |
| `44` | Up right arrow warning sign |
| `45-47` | *Not used* |
| `48` | Railroad crossing sign |
| `49` | Street sign |
| `50` | Roundabout warning sign |
| `51` | Fire hydrant |
| `52` | Exit sign |
| `53` | Bike lane sign |
| `54-56` | *Not used* |
| `57` | Sky |
| `58` | Curb |
| `59` | Flyover ramp |
| `60` | Road guard rail |
| 61 | Bicyclist |
| `62-66` | *Not used* |
| `67` | Deer |
| `68-70` | *Not used* |
| `71` | Barricade |
| `72` | Motorcycle |
| `73-255` | *Not used* |

### **Radar cross sections (dBsm)** — 雷达散射截面 `{}`（默认）| real-valued *Q*-by-*P* matrix | *L*-length cell array of real-valued *Q*1-by-*P*1, …, *Q*L-by-*P*L matrices

目标对象的雷达散射截面，以 decibels per square meter 为单位，指定为 matrix 或 cell array of matrices。每个矩阵定义由 **Radar targets** 指定的对应目标对象的 RCS。

如果 **Radar targets** 是 scalar（即单个目标对象），则将 **Radar cross sections (dBsm)** 指定为 real-valued *Q*-by-*P* matrix，其中：

- *Q* 是该对象的仰角采样数。
- *P* 是该对象的方位角采样数。

如果 **Radar targets** 是 vector（即多个目标对象），则将 **Radar cross sections (dBsm)** 指定为 *L*-length cell array of real-valued *Q*1-by-*P*1, …, *Q*L-by-*P*L matrices，其中：

- *L* 是对象数。
- *Q*1, …, *Q*L 是每个对象的仰角采样数。
- *P*1, …, *P*L 是每个对象的方位角采样数。

*Q* 和 *P* 可以随每个对象而变化。对于每个 RCS 矩阵：

- 行对应于在区间 [0, 180] 上均匀采样的仰角。
- 列对应于在区间 [0, 360] 上均匀采样的方位角。

例如，RCS 矩阵 `RCS` 的仰角和方位角采样数如下：

```
el = linspace(0,180,size(RCS,1));
az = linspace(0,360,size(RCS,2));
```

### **Default radar cross section (dBsm)** — 默认雷达散射截面 `-20`（默认）| real scalar

默认雷达散射截面，以 decibels per square meter 为单位，指定为 real scalar。对于未由 **Radar cross sections (dBsm)** 指定 RCS 的对象，该模块使用此 RCS 值。如果模型不包含 Simulation 3D Scene Configuration 模块，则分配给 Unreal Engine 场景中对象的默认 RCS 为 –20 dBsm。

**示例：** `-10`

## 所属库

Automated Driving Toolbox / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Probabilistic Radar Configuration 模块仿真模型需要 Simulink 3D Animation。

## 描述

配置 3D 仿真环境中的概率雷达签名

**注意**

使用 Simulation 3D Probabilistic Radar Configuration 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Probabilistic Radar Configuration 模块配置 3D 仿真环境中对象的概率雷达签名。此环境使用 Epic Games® 的 Unreal Engine® 渲染。要对概率雷达建模，请使用 Simulation 3D Probabilistic Radar 模块。配置的雷达签名应用于模型中的所有 Simulation 3D Probabilistic Radar 模块。
