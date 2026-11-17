---
type: simulink-block
title: 'Simulation 3D Probabilistic Radar Configuration'
family: 'driving'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Radar targets
  summary: 与雷达目标对应的标识符 []（默认）| 正整数 | *L* 长度唯一正整数向量
  group: ''
- name: Radar cross sections (dBsm)
  summary: 雷达散射截面 {}（默认）| 实值 *Q*×*P* 矩阵 | *L* 长度元胞数组，包含实值 *Q*1×*P*1、…、*Q*L×*P*L 矩阵
  group: ''
- name: Default radar cross section (dBsm)
  summary: 默认雷达散射截面 -20（默认）| 实标量
  group: ''
```

### **Radar targets** — 与雷达目标对应的标识符 `[]`（默认）| 正整数 | *L* 长度唯一正整数向量

与雷达目标对应的标识符，指定为正整数或 *L* 长度唯一正整数向量。*L* 等于您要为其指定非默认雷达散射截面（RCS）的雷达目标数量。

下表提供了雷达在默认场景中可检测到的标识符及对应对象类型，这些默认场景可从 Simulation 3D Scene Configuration 模块中选择。例如，要为建筑物和道路指定非默认 RCS，请将 **Radar targets** 设置为 `[1,7]`。如果您使用的是自定义场景，可以在 Unreal® Editor 中为未使用的 ID 分配新的对象类型。更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景中包含未分配 ID 的对象，则该对象被分配 ID `0`。不支持车道标线的检测。

| ID | 类型 |
| --- | --- |
| `0` | 无/默认 |
| `1` | 建筑物 |
| `2` | *未使用* |
| `3` | 其他 |
| `4` | 行人 |
| `5` | 杆 |
| `6` | 车道标线 |
| `7` | 道路 |
| `8` | 人行道 |
| `9` | 植被 |
| `10` | 车辆 |
| `11` | *未使用* |
| `12` | 通用交通标志 |
| `13` | 停车标志 |
| `14` | 让行标志 |
| `15` | 限速标志 |
| `16` | 限重标志 |
| `17-18` | *未使用* |
| `19` | 左右箭头警告标志 |
| `20` | 左箭头警告标志 |
| `21` | 右箭头警告标志 |
| `22` | *未使用* |
| `23` | 右侧单行道标志 |
| `24` | *未使用* |
| `25` | 仅校车标志 |
| `26-38` | *未使用* |
| `39` | 人行横道标志 |
| `40` | *未使用* |
| `41` | 交通信号灯 |
| `42` | 右弯警告标志 |
| `43` | 左弯警告标志 |
| `44` | 右上箭头警告标志 |
| `45-47` | *未使用* |
| `48` | 铁路道口标志 |
| `49` | 街道标志 |
| `50` | 环岛警告标志 |
| `51` | 消防栓 |
| `52` | 出口标志 |
| `53` | 自行车道标志 |
| `54-56` | *未使用* |
| `57` | 天空 |
| `58` | 路缘 |
| `59` | 立交匝道 |
| `60` | 道路护栏 |
| 61 | 骑自行车者 |
| `62-66` | *未使用* |
| `67` | 鹿 |
| `68-70` | *未使用* |
| `71` | 路障 |
| `72` | 摩托车 |
| `73-255` | *未使用* |

### **Radar cross sections (dBsm)** — 雷达散射截面 `{}`（默认）| 实值 *Q*×*P* 矩阵 | *L* 长度元胞数组，包含实值 *Q*1×*P*1、…、*Q*L×*P*L 矩阵

目标对象的雷达散射截面，以分贝每平方米为单位，指定为矩阵或矩阵的元胞数组。每个矩阵定义由 **Radar targets** 指定的对应目标对象的 RCS。

如果 **Radar targets** 是标量（即单个目标对象），则将 **Radar cross sections (dBsm)** 指定为实值 *Q*×*P* 矩阵，其中：

- *Q* 是该对象的仰角采样数。
- *P* 是该对象的方位角采样数。

如果 **Radar targets** 是向量（即多个目标对象），则将 **Radar cross sections (dBsm)** 指定为 *L* 长度元胞数组，包含实值 *Q*1×*P*1、…、*Q*L×*P*L 矩阵，其中：

- *L* 是对象数量。
- *Q*1、…、*Q*L 是每个对象的仰角采样数。
- *P*1、…、*P*L 是每个对象的方位角采样数。

*Q* 和 *P* 可以因对象而异。对于每个 RCS 矩阵：

- 行对应于在区间 [0, 180] 上均匀采样的仰角。
- 列对应于在区间 [0, 360] 上均匀采样的方位角。

例如，RCS 矩阵 `RCS` 的仰角和方位角采样数如下：

```
el = linspace(0,180,size(RCS,1));
az = linspace(0,360,size(RCS,2));
```

### **Default radar cross section (dBsm)** — 默认雷达散射截面 `-20`（默认）| 实标量

默认雷达散射截面，以分贝每平方米为单位，指定为实标量。该模块将此 RCS 值用于未通过 **Radar cross sections (dBsm)** 指定 RCS 的对象。如果模型不包含 Simulation 3D Scene Configuration 模块，则 Unreal Engine 场景中分配给对象的默认 RCS 为 –20 dBsm。

**示例：** `-10`
## 所属库

Automated Driving Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Probabilistic Radar Configuration 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 仿真环境中配置概率雷达特征

**注意**

使用 Simulation 3D Probabilistic Radar Configuration 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Probabilistic Radar Configuration 模块为 3D 仿真环境中的对象配置概率雷达特征。此环境使用 Epic Games® 的 Unreal Engine® 渲染。要对概率雷达进行建模，请使用 Simulation 3D Probabilistic Radar 模块。所配置的雷达特征适用于模型中的所有 Simulation 3D Probabilistic Radar 模块。
