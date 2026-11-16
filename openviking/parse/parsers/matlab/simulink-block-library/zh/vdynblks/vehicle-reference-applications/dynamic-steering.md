---
type: simulink-block
title: 'Dynamic Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'dynamicsteering'
documentation_source_path: 'ref/dynamicsteering.html'
language: zh-CN
chinese_source: worker-translation
---

# Dynamic Steering

## 端口

### 输入

### **TrqIn** — Torque `scalar`

扭矩，*τin*，单位 N·m。

### **TrqLft** — Left wheel torque `scalar`

左轮扭矩，*τL*，单位 N·m。

### **TrqRght** — Right wheel torque `scalar`

右轮扭矩，*τR*，单位 N·m。

### **VehSpd** — Vehicle speed `scalar`

车速，*v*，单位 m/s。

#### 依赖项

要创建 `VehSpd` 端口，请选择 **Power assist**。
### 输出

### **Info** — 总线信号 bus

总线信号包含以下模块计算结果。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `StrgWhlAng` | 方向盘角度 | rad |
| `StrgWhlSpd` | 方向盘角速度 | rad/s |
| `ShftAng` | 轴角度 | rad |
| `ShftSpd` | 轴角速度 | rad/s |
| `AngLft` | 左轮角度 | rad |
| `SpdLft` | 左轮角速度 | rad/s |
| `AngRght` | 右轮角度 | rad |
| `SpdRght` | 右轮角速度 | rad/s |
| `TrqAst` | 辅助扭矩 | N·m |
| `PwrAst` | 辅助功率 | W |
| `PwrLoss` | 功率损失 | W |
| `InstStrgRatio` | 瞬时转向比 | NA |

### **AngLft** — Left wheel angle `scalar`

左轮角度，*δL*，单位 rad。

### **AngRght** — Right wheel angle `scalar`

右轮角度，*δR*，单位 rad。

## 参数

### **Type** — 选择转向类型 `Rack and pinion`（默认）| `Ackerman` | `Parallel`

要指定转向类型，请使用 **Type** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想阿克曼转向。车轮角度具有共同的转弯圆心。 |
| `Rack and pinion` | 理想齿轮齿条转向。齿轮将转向旋转转换为线性运动。 |
| `Parallel` | 平行转向。车轮角度相等。 |

#### 依赖项

此表汇总了 **Type** 和 **Parametrized by** 参数依赖关系。

| Type | Parameterized By | 创建参数 |
| --- | --- | --- |
| `Ackerman` | `Constant` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |
| `Rack and pinion` | `Constant` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius, PnnRadius** |
| `Lookup table` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius table, PnnRadiusTbl** |
| `Parallel` | `Constant` | **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |

### **Parametrized by** — 选择参数化 `Lookup table`（默认）| `Constant`

要指定转向机构的数据类型，请使用 **Parametrized by** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常量参数数据。 |
| `Lookup table` | 转向机构实现参数数据的查找表。 |

#### 依赖项

此表汇总了 **Type** 和 **Parametrized by** 参数依赖关系。

| Type | Parameterized By | 创建参数 |
| --- | --- | --- |
| `Ackerman` | `Constant` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Track width, TrckWdth**  **Wheel base, WhlBase**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |
| `Rack and pinion` | `Constant` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius, PnnRadius** |
| `Lookup table` | **Track width, TrckWdth**  **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering arm length, StrgArmLngth**  **Rack casing length, RckCsLngth**  **Tie rod length, TieRodLngth**  **Distance between front axis and rack, D**  **Pinion radius table, PnnRadiusTbl** |
| `Parallel` | `Constant` | **Steering range, StrgRng**  **Steering ratio, StrgRatio** |
| `Lookup table` | **Steering range, StrgRng**  **Steering angle breakpoints, StrgAngBpts**  **Steering ratio table, StrgRatioTbl** |

### **Power assist** — 指定动力辅助 `on`（默认）| `off`

如果选择 **Power assist**，您可以指定一个扭矩辅助查找表 *ƒtrq*，它是车速 *v* 和方向盘输入扭矩 *τin* 的函数。

τast=ftrq(v,τin)

该模块使用方向盘输入扭矩和扭矩辅助来计算转向动力学。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Location** — 选择位置 **Front**（默认）| **Rear**

使用 **Steered axle** 参数指定转向的是前轴还是后轴。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前轮转向右转示意图 |
| **Rear** | 后轴转向  后轮转向右转示意图 |

#### 通用

### **Track width, TrckWdth** — 宽度 `1` | `scalar`

轮距，*TW*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Ackerman` 或 `Rack and pinion`。

### **Wheel base, WhlBase** — 基准 `1.524`（默认）| `scalar`

轴距，*WB*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Ackerman`。

### **Steering range, StrgRng** — 范围 `1.25*pi`（默认）| `scalar`

转向范围，单位 rad。该模块限制车轮角度以使其保持在转向范围内。

### **Steering ratio, StrgRatio** — 比率 `13.5`（默认）| `scalar`

转向比，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Ackerman` 或 `Parallel`。
- 将 **Parametrized by** 设置为 `Constant`。

### **Steering angle breakpoints, StrgAngBpts** — 断点 `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]`（默认）| `vector`

转向角断点，单位 rad。

#### 依赖项

要创建此参数，请将 **Parametrized by** 设置为 `Lookup table`。

### **Steering ratio table, StrgRatioTbl** — 表 `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]`（默认）| `vector`

转向比表，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Ackerman` 或 `Parallel`。
- 将 **Parametrized by** 设置为 `Lookup table`。

#### 齿轮齿条

### **Steering arm length, StrgArmLngth** — 长度 `0.1`（默认）| `scalar`

转向臂长度，*larm*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Rack and pinion`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `StrgArmLngth` |
| **值:** | `0.1`（默认）| `scalar` |
| **数据类型:** | `double` |

### **Rack casing length, RckCsLngth** — 长度 `0.5`（默认）| `scalar`

齿条外壳长度，*lrack*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Rack and pinion`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RckCsLngth` |
| **值:** | `0.5`（默认）| `scalar` |
| **数据类型:** | `double` |

### **Tie rod length, TieRodLngth** — 长度 `0.248`（默认）| `scalar`

横拉杆长度，*lrod*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Rack and pinion`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `TieRodLngth` |
| **值:** | `0.248`（默认）| `scalar` |
| **数据类型:** | `double` |

### **Distance between axis and rack, D** — 距离 `0.2`（默认）| `scalar`

轴与齿条之间的距离，*D*，单位 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Rack and pinion`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `D` |
| **值:** | `0.2`（默认）| `scalar` |
| **数据类型:** | `double` |

### **Pinion radius, PnnRadius** — 半径 `0.0057`（默认）| `scalar`

小齿轮半径，*r*，单位 m。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Rack and pinion`。
- 将 **Parametrized by** 设置为 `Constant`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PnnRadius` |
| **值:** | `0.0057`（默认）| `scalar` |
| **数据类型:** | `double` |

### **Pinion radius table, PnnRadiusTbl** — 表 `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]`（默认）| `vector`

小齿轮半径表，*r*，单位 m。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Rack and pinion`。
- 将 **Parametrized by** 设置为 `Lookup table`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PnnRadiusTbl` |
| **值:** | `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]`（默认）| `vector` |
| **数据类型:** | `double` |

#### 动力学

### **Steering wheel inertia, J1** — 惯量 `0.1`（默认）| `scalar`

方向盘惯量，*J1*，单位 kg\*m^2。

### **Steering mechanism inertia, J2** — 惯量 `0.01`（默认）| `scalar`

转向机构惯量，*J2*，单位 kg\*m^2。

### **Upper hysteresis modifier, beta\_u** — 上迟滞修正系数 `0.1`（默认）| `scalar`

上迟滞修正系数，*βu*，无量纲。

### **Lower hysteresis modifier, beta\_l** — 下迟滞修正系数 `0.1`（默认）| `scalar`

下迟滞修正系数，*βl*，无量纲。

### **Hysteresis viscous damping, b1** — 阻尼 `0.001`（默认）| `scalar`

迟滞阻尼，*b1*，单位 N·m·s/rad。

### **Hysteresis stiffness, k1** — 刚度 `30`（默认）| `scalar`

迟滞刚度，*k1*，单位 N·m/rad。

### **Steering wheel damping, b2** — 阻尼 `1`（默认）| `scalar`

方向盘阻尼，*b2*，单位 N·m·s/rad。

### **Steering mechanism damping, b3** — 阻尼 `0.001`（默认）| `scalar`

转向机构阻尼，*b3*，单位 N·m·s/rad。

### **Initial steering angle, theta\_o** — 角度 `0`（默认）| `scalar`

初始转向角，*θ0*，单位 rad。

### **Initial steering angular velocity, omega\_o** — 角速度 `0`（默认）| `scalar`

初始转向角速度，*ωo*，单位 rad/s。

### **Friction torque, FricTrq** — 扭矩 `0`（默认）| `scalar`

摩擦力矩，*τfric*，单位 N·m。

#### 动力辅助

### **Steering wheel torque breakpoints, TrqBpts** — 断点 `[-100 0 100]`（默认）| `1`-by-`M` vector

方向盘扭矩断点，单位 N·m。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Vehicle speed breakpoints, VehSpdBpts** — 断点 `[0 20]`（默认）| `1`-by-`N` vector

车速断点，单位 m/s。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque table, TrqTbl** — 二维扭矩表 `[0 -100;0 0;0 100]`（默认）| `M`-by-`N` matrix

辅助扭矩表，*ƒtrq*，单位 N·m。

扭矩辅助查找表是车速 *v* 和方向盘输入扭矩 *τin* 的函数。

τast=ftrq(v,τin)

该模块使用方向盘输入扭矩和扭矩辅助来计算转向动力学。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque limit, TrqLmt** — 扭矩限值 `100`（默认）| `scalar`

辅助扭矩限值，单位 N·m。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting power limit, PwrLmt** — 功率限值 `1000`（默认）| `scalar`

辅助功率限值，单位 N·m/s。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Assisting torque efficiency, Eta** — 效率 `1`（默认）| `scalar`

辅助扭矩效率，无量纲。

#### 依赖项

选择 **Power assist** 会创建 `VehSpd` 输入端口和以下参数。

| Power Assist | 参数 |
| --- | --- |
| `on` | **Steering wheel torque breakpoints, TrqBpts**  **Vehicle speed breakpoints, VehSpdBpts**  **Assisting torque table, TrqTbl**  **Assisting torque limit, TrqLmt**  **Assisting power limit, PwrLmt**  **Assisting torque efficiency, Eta**  **Cutoff frequency, omega\_c** |

### **Cutoff frequency, omega\_c** — 截止频率 `200`（默认）| `scalar`

截止频率，单位 rad/s。

#### 依赖项

选择 **动力辅助** 会创建 `VehSpd` 输入端口和以下参数。

| 动力辅助 | 参数 |
| --- | --- |
| `on` | **方向盘扭矩断点，TrqBpts**  **车速断点，VehSpdBpts**  **辅助扭矩表，TrqTbl**  **辅助扭矩限值，TrqLmt**  **辅助功率限值，PwrLmt**  **辅助扭矩效率，Eta**  **截止频率，omega\_c** |

## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a: 已删除

Dynamic Steering 已被删除。请改用 Steering System 模块。

### R2023b: 将删除

Dynamic Steering 将在未来版本中删除。请改用 Steering System 模块。

### R2023a: 不建议使用

不建议使用 Dynamic Steering。请改用 Steering System 模块来实现动态转向，包括：

- Ackerman 百分比，用于调整理想 Ackerman 外侧车轮转角。您可以使用输入端口或参数来指定 Ackerman 百分比的常量或表格。
- 单 Cardan 接头或双 Cardan 接头，用于对中间转向轴建模。
- 摩擦和柔顺效应。
- 用于动力辅助、Ackerman 转向和主销力矩的输入端口。

## 描述

（已删除）用于 Ackerman、齿轮齿条和平行转向机构的动态转向

Dynamic Steering 模块实现动态转向，以计算 Ackerman、齿轮齿条和平行转向机构的车轮转角。该模块使用方向盘输入扭矩、右轮扭矩和左轮扭矩来计算车轮转角。该模块使用车辆坐标系。

如果选择 **动力辅助**，您可以指定一个扭矩辅助查找表，该表是车速和方向盘输入扭矩的函数。该模块使用方向盘输入扭矩和扭矩辅助来计算转向动力学。

要指定转向类型，请使用 **类型** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想 Ackerman 转向。车轮转角具有共同的转弯圆心。 |
| `Rack and pinion` | 理想齿轮齿条转向。齿轮将转向旋转转换为直线运动。 |
| `Parallel` | 平行转向。车轮转角相等。 |

要指定转向机构的数据类型，请使用 **参数化方式** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常量参数数据。 |
| `Lookup table` | 转向机构实现参数数据的表格。 |

使用 **转向车轴** 参数来指定转向前轴还是后轴。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前转向右转的图 |
| **Rear** | 后轴转向  后转向右转的图 |

### 动力学

为了计算转向动力学，Dynamic Steering 模块对方向盘、转向轴、转向机构、迟滞以及可选的动力辅助进行建模。

方向盘、弹簧阻尼器和转向机构的图

| 计算 | 方程 |
| --- | --- |
| 转向柱和转向轴动力学 | J1θ¨1=τin−b2θ˙1−τhys      J2θ¨2=τeq−b3θ˙2+τhys−τfric |
| 迟滞弹簧阻尼器 | δ=θ1−θ2Δδ=δcurrent−δpreviousτhys=(b1δ˙−k1δ)(1+exp(−|Δδ|β))β={βu   when  δ>0βl    when  δ≤0 |
| 可选动力辅助 | τast=ftrq(v,τin)J1θ¨1=τin+τast−b2θ˙1−τhysJ2θ¨2=τeq+τast−b3θ˙2+τhys−τfric |

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *J1* | 方向盘惯量 |
| *J2* | 转向机构惯量 |
| θ1,θ˙1,θ¨1 | 分别为方向盘转角、角速度和角加速度 |
| θ2,θ˙2,θ¨2 | 分别为轴转角、角速度和角加速度 |
| *b1*, *k1* | 分别为迟滞弹簧和黏性阻尼系数 |
| *b2* | 方向盘黏性阻尼系数 |
| *b3* | 转向机构阻尼系数 |
| *τhys* | 迟滞弹簧阻尼扭矩 |
| *τfric* | 转向机构摩擦力矩 |
| *τeq* | 车轮等效扭矩 |
| *τast* | 扭矩辅助 |
| *βu*, *βl* | 分别为上、下迟滞修正因子 |
| *v* | 车速 |
| *ƒtrq* | 扭矩辅助查找表 |

### 转向类型

**Ackermann 转向**

对于 100%（理想）Ackermann 转向，所有车轮都沿具有同一圆心的圆弧行驶。

Ackermann 转向绕转弯圆右转的图

要计算转向车轮转角，Steering System 模块使用以下方程：

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

该表定义了方程中使用的变量：

|  |  |
| --- | --- |
| *δin* | 小齿轮转角（进入小齿轮的转向轴转角） |
| *δL* | 左轮转向角 |
| *δR* | 右轮转向角 |
| *δAck* | Ackermann 转向角 |
| *TW* | 轮距 |
| *WB* | 轴距 |
| *γ* | 转向比：小齿轮转角与 Ackermann 转角之比 |

**齿轮齿条**

对于齿轮齿条转向，小齿轮旋转引起齿条的直线运动，齿条通过横拉杆和转向臂使车轮转向。

齿轮齿条转向机构中齿条、拉杆和转向臂的图

齿轮齿条转向机构中拉杆的图

要计算转向车轮转角，该模块使用以下方程。

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 小齿轮转角（进入小齿轮的转向轴转角） |
| *δL* | 左轮转向角 |
| *δR* | 右轮转向角 |
| *TW* | 轮距 |
| *r* | 小齿轮半径 |
| *ΔP* | 齿条位置相对于“直行”位置的线性变化 |
| *D* | 齿条与转向车轴之间的纵向距离 |
| *lrack* | 齿条长度（内侧横拉杆端部之间的距离） |
| *larm* | 转向臂长度 |
| *lrod* | 横拉杆长度 |

**平行**

对于平行转向，车轮转角相等。

车轮转角相等的平行转向图

要计算转向角，该模块使用以下方程。

δR=δL=δinγ

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 方向盘转角 |
| *δL* | 左轮转角 |
| *δR* | 右轮转角 |
| *γ* | 转向比 |
