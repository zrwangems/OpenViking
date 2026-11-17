---
type: simulink-block
title: 'Steering System'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'steeringsystem'
documentation_source_path: 'ref/steeringsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Steering System

## 端口
```yaml
ports:
- name: VehSpd
  summary: 车辆速度标量
  direction: input
- name: CstrAng
  summary: 车轮主销后倾角 1×2 向量
  direction: input
- name: WhlAngFdk
  summary: 车轮转向角反馈 1×2 向量
  direction: input
- name: AngIn
  summary: 方向盘角度输入标量
  direction: input
- name: TrqIn
  summary: 转向力矩输入标量
  direction: input
- name: PwrAstTrq
  summary: 助力力矩标量
  direction: input
- name: PctAck
  summary: 阿克曼百分比值标量
  direction: input
- name: TireFdk
  summary: 轮胎力和力矩反馈 1×12 向量
  direction: input
- name: LftKpM
  summary: 左主销力矩标量
  direction: input
- name: RghtKpM
  summary: 右主销力矩标量
  direction: input
- name: Info
  summary: 车辆动力学信息总线
  direction: output
- name: AngLft
  summary: 左车轮转向角 scalar
  direction: output
- name: AngRght
  summary: 右车轮转向角 scalar
  direction: output
```

### 输入

### **VehSpd** — 车辆速度标量

车辆速度，*v*，单位为 m/s，指定为标量。
这是车辆质心纵向速度矢量的大小。

#### 依赖关系

要启用此参数，请选择 **Power
assist** 模块选项。

### **CstrAng** — 车轮主销后倾角 1×2 向量

车轮主销后倾角，*τL*，单位为弧度，指定为 1×2 向量。第一个元素是左轮的角度，第二个元素是右轮的角度。

#### 依赖关系

要启用此端口，请清除 **Input signals** > **Kingpin moment**。

### **WhlAngFdk** — 车轮转向角反馈 1×2 向量

车轮转向角反馈，单位为弧度，指定为 1×2 向量。第一个元素是来自左轮的角度反馈，第二个元素是来自右轮的角度反馈：

- **AngLft**
- **AngRght**

您可以使用来自车辆被控对象模型的转向角响应或此模块的车轮角度输出指定车轮转向角反馈。

#### 依赖关系

要启用此端口，请清除 **Input signals** > **Kingpin moment**。

### **AngIn** — 方向盘角度输入标量

来自驾驶员的方向盘角度输入，单位为弧度，指定为标量。

#### 依赖关系

要启用此端口，请选择 **Steering inputs** > **Angle**。

### **TrqIn** — 转向力矩输入标量

来自驾驶员的方向盘力矩输入，单位为 N\*m，指定为标量。

#### 依赖关系

要启用此端口，请选择 **Steering inputs** > **Torque**。

### **PwrAstTrq** — 助力力矩标量

转向轴上助力的力矩值，单位为 N\*m，指定为标量。该值从外部提供给此端口。

#### 依赖关系

要启用此端口，请选择 **Input signals** > **Power assist**。

### **PctAck** — 阿克曼百分比值标量

阿克曼值，以百分比表示，指定为标量。该值从外部提供给此端口。

#### 依赖关系

要启用此端口，请选择 **Input signals** > **Ackerman steering**。

### **TireFdk** — 轮胎力和力矩反馈 1×12 向量

来自右轮胎和左轮胎的轮胎力和力矩反馈，指定为 1×12 向量，包含下表中按指定顺序排列的以下值：

| 描述 | 单位 |
| --- | --- |
| *x* 方向力，左 | N |
| *x* 方向力，右 | N |
| *y* 方向力，左 | N |
| *y* 方向力，右 | N |
| *z* 方向力，左 | N |
| *z* 方向力，右 | N |
| *x* 方向力矩，左 | N\*m |
| *x* 方向力矩，右 | N\*m |
| *y* 方向力矩，左 | N\*m |
| *y* 方向力矩，右 | N\*m |
| *z* 方向力矩，左 | N\*m |
| *z* 方向力矩，右 | N\*m |

#### 依赖关系

要启用此端口，请清除 **Input signals** > **Kingpin moment**。

### **LftKpM** — 左主销力矩标量

左主销力矩，单位为 N\*m，指定为标量。

#### 依赖关系

要启用此端口，请选择 **Input signals** > **Kingpin moment**。

### **RghtKpM** — 右主销力矩标量

右主销力矩，单位为 N\*m，指定为标量。

#### 依赖关系

要启用此端口，请选择 **Input signals** > **Kingpin moment**。
### 输出

### **Info** — 车辆动力学信息总线

车辆动力学信息，以总线信号形式返回，包含以下信号：

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `StrWhlAngFdk` | 方向盘角度 | rad |
| `AstTrq` | 助力施加的扭矩 | N·m |
| `AstPwr` | 助力施加的功率 | W |
| `LftTieRodForce` | 左转向横拉杆轴向力 | N |
| `RghtTieRodForce` | 右转向横拉杆轴向力 | N |
| `LftKpM` | 左主销力矩 | N·m |
| `RghtKpM` | 右主销力矩 | N·m |
| `LftWhlAng` | 左车轮转向角 | rad |
| `RghtWhlAng` | 右车轮转向角 | rad |
| `LftWhlSpd` | 左车轮转向角速度 | rad/s |
| `RghtWhlSpd` | 右车轮转向角速度 | rad/s |
| `TrqIn` | 驾驶员施加在方向盘上的扭矩 | N·m |

### **AngLft** — 左车轮转向角 `scalar`

左车轮转向角，*δL*，以弧度为单位，以标量形式返回。

### **AngRght** — 右车轮转向角 `scalar`

右车轮转向角，*δR*，以弧度为单位，以标量形式返回。
## 参数
```yaml
parameters:
- name: Type
  summary: 转向类型 Rack and pinion（默认）
  group: ''
  block_parameter: StrgType
  values: Rack and pinion（默认）
- name: Intermediate shaft type
  summary: 中间轴类型 Single Cardan joint（默认） | Double Cardan joints
  group: ''
  block_parameter: IntmdShaftType
  values: Single Cardan joint（默认） | Double Cardan joints
- name: Power assist
  summary: 助力建模选项 on（默认） | off
  group: ''
  block_parameter: PwrAst
  values: on（默认） | off
- name: Ackerman steering
  summary: 使用阿克曼转向的选项 on（默认） | off
  group: ''
  block_parameter: AckStr
  values: on（默认） | off
- name: Power assist
  summary: 外部助力扭矩 off（默认） | on
  group: ''
  block_parameter: PwrAstOverride
  values: off（默认） | on
- name: Ackerman steering
  summary: 外部阿克曼百分比 off（默认） | on
  group: ''
  block_parameter: AckStrOverride
  values: off（默认） | on
- name: Kingpin moment
  summary: 左右主销力矩 off（默认） | on
  group: ''
  block_parameter: KingpinOverride
  values: off（默认） | on
- name: Steered axle
  summary: 转向系统位置 Front（默认） | Rear
  group: ''
  block_parameter: Loc
  values: Front（默认） | Rear
- name: Steering inputs
  summary: 方向盘转角或力矩 Angle（默认） | Torque
  group: ''
  block_parameter: StrIn
  values: Angle（默认） | Torque
- name: Track width, TrckWdth
  summary: 轮距 1（默认） | 标量
  group: ''
  block_parameter: TrckWdth
  values: 1（默认） | 标量
- name: Steering angle input range, StrRng
  summary: 方向盘范围 1.25*pi（默认） | 标量
  group: ''
  block_parameter: StrRng
  values: 1.25*pi（默认） | 标量
- name: Steering angle input deadband width, DbWdth
  summary: 转向角输入死区宽度 0（默认） | 标量
  group: ''
  block_parameter: DbWdth
  values: 0（默认） | 标量
- name: Steering wheel inertia, StrWhlInert
  summary: 方向盘惯量 0.1（默认） | 标量
  group: ''
  block_parameter: StrWhlInert
  values: 0.1（默认） | 标量
- name: Steering shaft inertia, StrColInert
  summary: 转向轴惯量 0.01（默认） | 标量
  group: ''
  block_parameter: StrCollnert
  values: 0.01（默认）| 标量
- name: Kingpin offset, KngpnOfst
  summary: 主销偏移距 0.075（默认）| 标量
  group: ''
  block_parameter: KngpnOfst
  values: 0.075（默认）| 标量
- name: Kingpin inclination angle, Lambda
  summary: 主销内倾角 0.2094（默认）| 标量
  group: ''
  block_parameter: Lambda
  values: 0.2094（默认）| 标量
- name: Hub lead, HbLead
  summary: 轮毂前束 4.00E-05（默认）| 标量
  group: ''
  block_parameter: HbLead
  values: 4.00E-05（默认）| 标量
- name: Static loaded radius, StcLdRadius
  summary: 静态加载半径 0.4（默认）| 标量
  group: ''
  block_parameter: StcLdRadius
  values: 0.4（默认）| 标量
- name: Overall steering ratio, OvrlStrRatio
  summary: 总转向比 17.42（默认）| 标量
  group: ''
  block_parameter: OvrlStrRatio
  values: 17.42（默认）| 标量
- name: Steering angle breakpoints, StrgAngBpts
  summary: 方向盘转角断点 [-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]（默认）| 1×11 向量
  group: ''
  block_parameter: StrgAngBpts
  values: '[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]（默认）| 1×11 向量'
- name: CstrAng
  summary: 主销后倾角 0（默认）| 标量
  group: ''
  block_parameter: CstrAng
  values: 0（默认） | 标量
- name: 齿条增益参数化方式
  summary: 齿条增益参数化 Constant（默认） | Lookup table
  group: ''
  block_parameter: StrgRatioType
  values: Constant（默认） | Lookup table
- name: 齿条增益，RckGn
  summary: 齿条增益 0.062（默认） | 标量
  group: ''
  block_parameter: RckGn
  values: 0.062（默认） | 标量
- name: 齿条增益表，RckGnTbl
  summary: 齿条增益表 ones(1,11)*0.0057*2*pi（默认） | 1×11 向量
  group: ''
  block_parameter: RckGnTbl
  values: ones(1,11)*0.0057*2*pi（默认） | 1×11 向量
- name: 转向臂长度，StrgArmLngth
  summary: 转向臂长度 0.1（默认） | 标量
  group: ''
  block_parameter: StrgArmLngth
  values: 0.1（默认） | 标量
- name: 齿条壳体长度，RckCsLngth
  summary: 齿条长度 0.5（默认） | 标量
  group: ''
  block_parameter: RckCsLngth
  values: 0.5（默认） | 标量
- name: 横拉杆长度，TieRodLngth
  summary: 横拉杆长度 0.248（默认） | 标量
  group: ''
  block_parameter: TieRodLngth
  values: 0.248（默认） | 标量
- name: 轴线与齿条之间的距离，Dst
  summary: 车轴与齿条之间的距离 0.2（默认） | 标量
  group: ''
  block_parameter: Dst
  values: 0.2（默认） | 标量
- name: Efficiency of gears, Epsilon
  summary: 齿轮效率 0.9（默认）| 标量
  group: ''
  block_parameter: Epsilon
  values: 0.9（默认）| 标量
- name: Pinion inertia, PnInert
  summary: 小齿轮惯量 0.1（默认）| 标量
  group: ''
  block_parameter: PnInert
  values: 0.1（默认）| 标量
- name: Spatial angle for the single Cardan joint, SptlAng
  summary: 单万向节的空间角 2.6178（默认）| 标量
  group: ''
  block_parameter: SptlAng
  values: 2.6178（默认）| 标量
- name: Spatial angle for the upper Cardan joint, Alpha_b
  summary: 上万向节的空间角 2.6178（默认）| 标量
  group: ''
  block_parameter: Alpha_b
  values: 2.6178（默认）| 标量
- name: Spatial angle for the lower Cardan joint, Alpha_c
  summary: 下万向节的空间角 2.7051（默认）| 标量
  group: ''
  block_parameter: Alpha_c
  values: 2.7051（默认）| 标量
- name: Edge view angle between the planes of the two joints, Sigma_bc
  summary: 两个万向节平面之间的边缘视角 0.2618（默认）| 标量
  group: ''
  block_parameter: Sigma_bc
  values: 0.2618（默认）| 标量
- name: Phase angle, Gamma
  summary: 相位角 0.2618（默认）| 标量
  group: ''
  block_parameter: Gamma
  values: 0.2618（默认）| 标量
- name: 方向盘扭矩断点，TrqBpts
  summary: 方向盘扭矩断点 [-100 0 100]（默认）| 1×*M* 向量
  group: ''
  block_parameter: TrqBpts
  values: '[-100 0 100]（默认）| 1×*M* 向量'
- name: 车速断点，VehSpdBpts
  summary: 车速断点 [0 20]（默认）| 1×*N* 向量
  group: ''
  block_parameter: VehSpdBpts
  values: '[0 20]（默认）| 1×*N* 向量'
- name: 辅助扭矩表，TrqTbl
  summary: 扭矩辅助表 [0 -100;0 0;0 100]（默认）| *M*×*N* 矩阵
  group: ''
  block_parameter: TrqTbl
  values: '[0 -100;0 0;0 100]（默认）| *M*×*N* 矩阵'
- name: 辅助扭矩限值，TrqLmt
  summary: 扭矩辅助限值 100（默认）| 标量
  group: ''
  block_parameter: TrqLmt
  values: 100（默认）| 标量
- name: 辅助功率限值，PwrLmt
  summary: 辅助功率限值 1000（默认）| 标量
  group: ''
  block_parameter: PwrLmt
  values: 1000（默认）| 标量
- name: 辅助扭矩效率，Eta
  summary: 扭矩辅助效率 1（默认）| 标量
  group: ''
  block_parameter: Eta
  values: 1（默认）| 标量
- name: 截止频率，CutOmege [rad/s]
  summary: 截止频率 200（默认）| 标量
  group: ''
  block_parameter: omega_c
  values: 200（默认）| 标量
- name: Percent Ackerman parameterized by
  summary: Ackermann 参数化方式 Constant（默认）| Lookup table
  group: ''
  block_parameter: AckParamType
  values: Constant（默认）| Lookup table
- name: Percent Ackerman, PctAck
  summary: 百分比 Ackermann 100（默认）| 标量
  group: ''
  block_parameter: PctAck
  values: 100（默认）| 标量
- name: Percent Ackerman table, PctAckTbl
  summary: 百分比 Ackermann 表 ones(1,11)*100（默认）| 1×11 向量
  group: ''
  block_parameter: PctAckTbl
  values: ones(1,11)*100（默认）| 1×11 向量
- name: 密封刚度，SlgStf
  summary: 密封刚度 1.5e4（默认）| 标量
  group: ''
  block_parameter: SlgStf
  values: 1.5e4（默认）| 标量
- name: 上边界摩擦力，UpprFric
  summary: 上边界摩擦力 1（默认）| 标量
  group: ''
  block_parameter: UpprFric
  values: 1（默认）| 标量
- name: 摩擦边界增加引起的压力变化，PrsFric
  summary: 摩擦边界增加引起的压力变化 1e-5（默认）| 标量
  group: ''
  block_parameter: PrsFric
  values: 1e-5（默认） | 标量
- name: Maxwell 单元刚度，MaxStf
  summary: Maxwell 单元刚度 10000（默认） | 标量
  group: ''
  block_parameter: MaxStf
  values: 10000（默认） | 标量
- name: Maxwell 单元上边界摩擦力，MaxUpprFric
  summary: Maxwell 单元上边界摩擦力 0.2（默认） | 标量
  group: ''
  block_parameter: MaxUpprFric
  values: 0.2（默认） | 标量
- name: Maxwell 线性阻尼系数，MaxDamp
  summary: Maxwell 线性阻尼系数 1（默认） | 标量
  group: ''
  block_parameter: MaxDamp
  values: 1（默认） | 标量
- name: 扭杆刚度系数，TorStf
  summary: 转向轴扭转刚度 30（默认） | 标量
  group: ''
  block_parameter: TorStf
  values: 30（默认） | 标量
- name: 扭杆阻尼系数，TorDamp
  summary: 转向轴中的扭转粘性阻尼 1（默认） | 标量
  group: ''
  block_parameter: TorDamp
  values: 1（默认） | 标量
- name: 积分抗饱和增益，A []
  summary: 积分抗饱和增益 0（默认） | 标量
  group: ''
  block_parameter: A
  values: 0（默认） | 标量
- name: 微分增益，D []
  summary: 微分增益 0.1（默认） | 标量
  group: ''
  block_parameter: D
  values: 0.1（默认） | 标量
- name: 积分增益，I []
  summary: 积分增益 5（默认）| 标量
  group: ''
  block_parameter: I
  values: 5（默认）| 标量
- name: 转向扭矩输出饱和下限，OutSatLowLmt [Nm]
  summary: 输出饱和下限 -500（默认）| 标量
  group: ''
  block_parameter: OutSatLowLmt
  values: -500（默认）| 标量
- name: 转向扭矩输出饱和上限，OutSatUpLmt [Nm]
  summary: 转向扭矩输出饱和上限 500（默认）| 标量
  group: ''
  block_parameter: OutSatUpLmt
  values: 500（默认）| 标量
- name: 比例增益，P []
  summary: 比例增益 150（默认）| 标量
  group: ''
  block_parameter: P
  values: 150（默认）| 标量
```

#### 模块选项

### **Type** — 转向类型 `Rack and pinion`（默认）

设置转向系统的转向类型。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `StrgType` |
| **值**：| `Rack and pinion`（默认） |
| **Data Types:** | `character vector` |

### **Intermediate shaft type** — 中间轴类型 `Single Cardan joint`（默认） | `Double Cardan joints`

选择使用单万向节还是双万向节对中间轴类型进行建模。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `IntmdShaftType` |
| **值**：| `Single Cardan joint`（默认） | `Double Cardan joints` |
| **Data Types:** | `character vector` |

### **Power assist** — 助力建模选项 `on`（默认） | `off`

选择此参数以在转向系统中对助力进行建模。

#### 依赖关系

要启用此参数，请在 **Input signals** 部分中清除 **Power assist**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PwrAst` |
| **值**：| `on`（默认） | `off` |
| **Data Types:** | `character vector` |

### **Ackerman steering** — 使用阿克曼转向的选项 `on`（默认） | `off`

选择此参数以在 Steering System 模块中设置阿克曼转向百分比。

#### 依赖关系

要启用此参数，请在 **Input signals** 部分中清除 **Ackerman steering**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AckStr` |
| **值**：| `on`（默认） | `off` |
| **Data Types:** | `character vector` |

#### 输入信号

### **Power assist** — 外部助力扭矩 `off`（默认） | `on`

选择此参数以启用 **PwrAstTrq** 端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PwrAstOverride` |
| **值**：| `off`（默认） | `on` |
| **Data Types:** | `character vector` |

### **Ackerman steering** — 外部阿克曼百分比 `off`（默认） | `on`

选择此参数以启用 **PctAck** 端口。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AckStrOverride` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Kingpin moment** — 左右主销力矩 `off`（默认） | `on`

选择此参数以启用 **LftKpM** 和 **RghtKpM** 端口。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KingpinOverride` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Steered axle** — 转向系统位置 `Front`（默认） | `Rear`

选择前轴或后轴作为转向系统的位置。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Loc` |
| **值：** | `Front`（默认） | `Rear` |
| **数据类型：** | `character vector` |

### **Steering inputs** — 方向盘转角或力矩 `Angle`（默认） | `Torque`

选择 **AngIn** 或 **TrqIn** 端口作为驾驶员输入。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrIn` |
| **值：** | `Angle`（默认） | `Torque` |
| **数据类型：** | `character vector` |

#### 常规

### **Track width, TrckWdth** — 轮距 `1`（默认） | 标量

轮距，*TW*，单位为 m，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrckWdth` |
| **值：** | `1`（默认） | 标量 |
| **数据类型：** | `double` |

### **Steering angle input range, StrRng** — 方向盘范围 `1.25*pi`（默认） | 标量

方向盘从正前方到左锁止或右锁止的转角，单位为 rad，指定为标量。此参数使两个转向车轮保持在其设计的转向范围内。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrRng` |
| **值：** | `1.25*pi`（默认） | 标量 |
| **数据类型：** | `double` |

### **Steering angle input deadband width, DbWdth** — 转向角输入死区宽度 `0`（默认） | 标量

方向盘死区角度，单位为弧度，从左侧啮合到右侧啮合。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DbWdth` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **Steering wheel inertia, StrWhlInert** — 方向盘惯量 `0.1`（默认） | 标量

方向盘转动惯量，单位为 kg\*m2，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrWhlInert` |
| **值：** | `0.1`（默认） | 标量 |
| **数据类型：** | `double` |

### **Steering shaft inertia, StrColInert** — 转向轴惯量 `0.01`（默认） | 标量

转向轴转动惯量，单位为 kg\*m2，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrCollnert` |
| **值：** | `0.01`（默认）| 标量 |
| **数据类型：** | `double` |

### **Kingpin offset, KngpnOfst** — 主销偏移距 `0.075`（默认）| 标量

主销偏移距，单位为 m，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KngpnOfst` |
| **值：** | `0.075`（默认）| 标量 |
| **数据类型：** | `character vector` |

### **Kingpin inclination angle, Lambda** — 主销内倾角 `0.2094`（默认）| 标量

主销内倾角，单位为 rad，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lambda` |
| **值：** | `0.2094`（默认）| 标量 |
| **数据类型：** | `double` |

### **Hub lead, HbLead** — 轮毂前束 `4.00E-05`（默认）| 标量

轮毂前束，单位为 m，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `HbLead` |
| **值：** | `4.00E-05`（默认）| 标量 |
| **数据类型：** | `double` |

### **Static loaded radius, StcLdRadius** — 静态加载半径 `0.4`（默认）| 标量

静态加载轮胎半径，单位为 m，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StcLdRadius` |
| **值：** | `0.4`（默认）| 标量 |
| **数据类型：** | `double` |

### **Overall steering ratio, OvrlStrRatio** — 总转向比 `17.42`（默认）| 标量

总转向比，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OvrlStrRatio` |
| **值：** | `17.42`（默认）| 标量 |
| **数据类型：** | `double` |

### **Steering angle breakpoints, StrgAngBpts** — 方向盘转角断点 `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]`（默认）| 1×11 向量

方向盘转角断点，单位为 rad，指定为 1×11 向量。
这些断点用于参数化阿克曼值或齿条增益。

#### 依赖关系

要启用此参数，请将以下参数之一设置为
`Lookup table`：

- **Rack and pinion** > **Rack gain parameterized by**
- **Ackerman steering** > **Percent Ackerman parameterized by**

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgAngBpts` |
| **值：** | `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]`（默认）| 1×11 向量 |
| **数据类型：** | `double` |

### **CstrAng** — 主销后倾角 `0`（默认）| 标量

主销后倾角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Input signals** > **Kingpin moment**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CstrAng` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

#### 齿条和小齿轮

### **齿条增益参数化方式** — 齿条增益参数化 `Constant`（默认） | `Lookup table`

是将齿条增益参数化为常量值，还是通过查找表进行参数化。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatioType` |
| **值：** | `Constant`（默认） | `Lookup table` |
| **数据类型：** | `character vector` |

### **齿条增益，RckGn** — 齿条增益 `0.062`（默认） | 标量

齿条增益，单位为 m/rev，指定为标量。

#### 依赖关系

要启用此参数，请将 **齿条增益参数化方式** 设置为 `Constant`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RckGn` |
| **值：** | `0.062`（默认） | 标量 |
| **数据类型：** | `double` |

### **齿条增益表，RckGnTbl** — 齿条增益表 `ones(1,11)*0.0057*2*pi`（默认） | 1×11 向量

齿条增益表，单位为 m/rev，指定为 1×11 向量。

#### 依赖关系

要启用此参数，请将 **齿条增益参数化方式** 设置为 `Lookup table`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RckGnTbl` |
| **值：** | `ones(1,11)*0.0057*2*pi`（默认） | 1×11 向量 |
| **数据类型：** | `double` |

### **转向臂长度，StrgArmLngth** — 转向臂长度 `0.1`（默认） | 标量

转向臂长度，单位为 m，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgArmLngth` |
| **值：** | `0.1`（默认） | 标量 |
| **数据类型：** | `double` |

### **齿条壳体长度，RckCsLngth** — 齿条长度 `0.5`（默认） | 标量

齿条长度（内侧横拉杆端部之间的距离），单位为 m，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RckCsLngth` |
| **值：** | `0.5`（默认） | 标量 |
| **数据类型：** | `double` |

### **横拉杆长度，TieRodLngth** — 横拉杆长度 `0.248`（默认） | 标量

横拉杆长度，*lrod*，单位为 m，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TieRodLngth` |
| **值：** | `0.248`（默认） | 标量 |
| **数据类型：** | `double` |

### **轴线与齿条之间的距离，Dst** — 车轴与齿条之间的距离 `0.2`（默认） | 标量

转向轴与齿条中心线之间的纵向距离，*D*，单位为 m，指定为标量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Dst` |
| **值：** | `0.2`（默认） | 标量 |
| **数据类型：** | `double` |

### **Efficiency of gears, Epsilon** — 齿轮效率 `0.9`（默认）| 标量

齿条和小齿轮机构的效率 *ɛ*，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Epsilon` |
| **值：** | `0.9`（默认）| 标量 |
| **数据类型：** | `double` |

### **Pinion inertia, PnInert** — 小齿轮惯量 `0.1`（默认）| 标量

小齿轮惯量，单位为 kg\*m2，指定为标量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PnInert` |
| **值：** | `0.1`（默认）| 标量 |
| **数据类型：** | `double` |

#### 单万向节

### **Spatial angle for the single Cardan joint, SptlAng** — 单万向节的空间角 `2.6178`（默认）| 标量

单万向节的空间角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请将 **Intermediate shaft type** 设置为 `Single Cardan joint`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SptlAng` |
| **值：** | `2.6178`（默认）| 标量 |
| **数据类型：** | `double` |

#### 双万向节

### **Spatial angle for the upper Cardan joint, Alpha\_b** — 上万向节的空间角 `2.6178`（默认）| 标量

上万向节的空间角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请将 **Intermediate shaft type** 设置为 `Double Cardan joints`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Alpha_b` |
| **值：** | `2.6178`（默认）| 标量 |
| **数据类型：** | `double` |

### **Spatial angle for the lower Cardan joint, Alpha\_c** — 下万向节的空间角 `2.7051`（默认）| 标量

下万向节的空间角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请将 **Intermediate shaft type** 设置为 `Double Cardan joints`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Alpha_c` |
| **值：** | `2.7051`（默认）| 标量 |
| **数据类型：** | `double` |

### **Edge view angle between the planes of the two joints, Sigma\_bc** — 两个万向节平面之间的边缘视角 `0.2618`（默认）| 标量

两个万向节平面之间的边缘视角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请将 **Intermediate shaft type** 设置为 `Double Cardan joints`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sigma_bc` |
| **值：** | `0.2618`（默认）| 标量 |
| **数据类型：** | `double` |

### **Phase angle, Gamma** — 相位角 `0.2618`（默认）| 标量

两个万向节之间的旋转相位角，单位为 rad，指定为标量。

#### 依赖关系

要启用此参数，请将 **Intermediate shaft type** 设置为 `Double Cardan joints`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Gamma` |
| **值：** | `0.2618`（默认）| 标量 |
| **数据类型：** | `double` |

#### 动力辅助

### **方向盘扭矩断点，TrqBpts** — 方向盘扭矩断点 `[-100 0 100]`（默认）| 1×*M* 向量

方向盘扭矩断点，单位为 N·m，指定为 1×*M* 向量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqBpts` |
| **值：** | `[-100 0 100]`（默认）| 1×*M* 向量 |
| **数据类型：** | `double` |

### **车速断点，VehSpdBpts** — 车速断点 `[0 20]`（默认）| 1×*N* 向量

车速断点，单位为 m/s，指定为 1×*N* 向量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VehSpdBpts` |
| **值：** | `[0 20]`（默认）| 1×*N* 向量 |
| **数据类型：** | `double` |

### **辅助扭矩表，TrqTbl** — 扭矩辅助表 `[0 -100;0 0;0 100]`（默认）| *M*×*N* 矩阵

扭矩辅助表，*ƒtrq*，单位为 N·m，指定为 *M*×*N* 矩阵。

扭矩辅助查找表是车速 *v* 和方向盘输入扭矩 *τin* 的函数：

τast=ftrq(v,τin)。

该模块将方向盘输入扭矩和扭矩辅助施加到小齿轮上。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqTbl` |
| **值：** | `[0 -100;0 0;0 100]`（默认）| *M*×*N* 矩阵 |
| **数据类型：** | `double` |

### **辅助扭矩限值，TrqLmt** — 扭矩辅助限值 `100`（默认）| 标量

扭矩辅助限值，单位为 N·m，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqLmt` |
| **值：** | `100`（默认）| 标量 |
| **数据类型：** | `double` |

### **辅助功率限值，PwrLmt** — 辅助功率限值 `1000`（默认）| 标量

辅助功率限值，单位为瓦特，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PwrLmt` |
| **值：** | `1000`（默认）| 标量 |
| **数据类型：** | `double` |

### **辅助扭矩效率，Eta** — 扭矩辅助效率 `1`（默认）| 标量

扭矩辅助效率，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Eta` |
| **值：** | `1`（默认）| 标量 |
| **数据类型：** | `double` |

### **截止频率，CutOmege [rad/s]** — 截止频率 `200`（默认）| 标量

截止频率，以 rad/s 为单位，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Power assist** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_c` |
| **值：** | `200`（默认）| 标量 |
| **数据类型：** | `double` |

#### Ackerman 转向

### **Percent Ackerman parameterized by** — Ackermann 参数化方式 `Constant`（默认）| `Lookup table`

是将 Ackermann 值参数化为常量值还是通过查找表参数化。

#### 依赖关系

要启用此参数，请选择 **Ackerman steering** 模块选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AckParamType` |
| **值：** | `Constant`（默认）| `Lookup table` |
| **数据类型：** | `character vector` |

### **Percent Ackerman, PctAck** — 百分比 Ackermann `100`（默认）| 标量

百分比 Ackermann，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Ackerman steering** 模块选项，并将 **Percent Ackerman parameterized by** 设置为 `Constant`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PctAck` |
| **值：** | `100`（默认）| 标量 |
| **数据类型：** | `double` |

### **Percent Ackerman table, PctAckTbl** — 百分比 Ackermann 表 `ones(1,11)*100`（默认）| 1×11 向量

百分比 Ackermann 表，指定为 1×11 向量。

#### 依赖关系

要启用此参数，请选择 **Ackerman steering** 模块选项，并将 **Percent Ackerman parameterized by** 设置为 `Lookup table`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PctAckTbl` |
| **值：** | `ones(1,11)*100`（默认）| 1×11 向量 |
| **数据类型：** | `double` |

#### 摩擦与柔度

### **密封刚度，SlgStf** — 密封刚度 `1.5e4`（默认）| 标量

密封刚度，以 N\*m/rad 为单位，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SlgStf` |
| **值：** | `1.5e4`（默认）| 标量 |
| **数据类型：** | `double` |

### **上边界摩擦力，UpprFric** — 上边界摩擦力 `1`（默认）| 标量

上边界摩擦力，以 N 为单位，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `UpprFric` |
| **值：** | `1`（默认）| 标量 |
| **数据类型：** | `double` |

### **摩擦边界增加引起的压力变化，PrsFric** — 摩擦边界增加引起的压力变化 `1e-5`（默认）| 标量

摩擦边界增加引起的压力变化，以 N/bar 为单位，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PrsFric` |
| **值：** | `1e-5`（默认） | 标量 |
| **数据类型：** | `double` |

### **Maxwell 单元刚度，MaxStf** — Maxwell 单元刚度 `10000`（默认） | 标量

Maxwell 单元刚度，单位为 N\*m/rad，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxStf` |
| **值：** | `10000`（默认） | 标量 |
| **数据类型：** | `double` |

### **Maxwell 单元上边界摩擦力，MaxUpprFric** — Maxwell 单元上边界摩擦力 `0.2`（默认） | 标量

Maxwell 单元上边界摩擦力，单位为 N，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxUpprFric` |
| **值：** | `0.2`（默认） | 标量 |
| **数据类型：** | `double` |

### **Maxwell 线性阻尼系数，MaxDamp** — Maxwell 线性阻尼系数 `1`（默认） | 标量

Maxwell 线性阻尼系数，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDamp` |
| **值：** | `1`（默认） | 标量 |
| **数据类型：** | `double` |

### **扭杆刚度系数，TorStf** — 转向轴扭转刚度 `30`（默认） | 标量

转向轴扭转刚度，单位为 N\*m/rad，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TorStf` |
| **值：** | `30`（默认） | 标量 |
| **数据类型：** | `double` |

### **扭杆阻尼系数，TorDamp** — 转向轴中的扭转粘性阻尼 `1`（默认） | 标量

转向轴中的扭转粘性阻尼，单位为 N\*m\*s/rad，指定为标量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TorDamp` |
| **值：** | `1`（默认） | 标量 |
| **数据类型：** | `double` |

#### 转向扭矩控制器

### **积分抗饱和增益，A []** — 积分抗饱和增益 `0`（默认） | 标量

积分抗饱和增益，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `A` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **微分增益，D []** — 微分增益 `0.1`（默认） | 标量

微分增益，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `D` |
| **值：** | `0.1`（默认） | 标量 |
| **数据类型：** | `double` |

### **积分增益，I []** — 积分增益 `5`（默认）| 标量

积分增益，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `I` |
| **值：** | `5`（默认）| 标量 |
| **数据类型：** | `double` |

### **转向扭矩输出饱和下限，OutSatLowLmt [Nm]** — 输出饱和下限 `-500`（默认）| 标量

转向扭矩输出饱和下限，指定为标量，单位为 Nm。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutSatLowLmt` |
| **值：** | `-500`（默认）| 标量 |
| **数据类型：** | `double` |

### **转向扭矩输出饱和上限，OutSatUpLmt [Nm]** — 转向扭矩输出饱和上限 500（默认）| 标量

转向扭矩输出饱和上限，指定为标量，单位为 Nm。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutSatUpLmt` |
| **值：** | 500（默认）| 标量 |
| **数据类型：** | `double` |

### **比例增益，P []** — 比例增益 `150`（默认）| 标量

比例增益，指定为标量。

#### 依赖关系

要启用此参数，请选择 **Steering inputs** > **Angle**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `P` |
| **值：** | `150`（默认）| 标量 |
| **数据类型：** | `double` |
## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024a：新增转向扭矩控制器参数

从 R2024a 开始，Steering System 模块包含以下参数，您可以指定这些参数来定义转向扭矩控制器：

- **积分抗饱和增益**
- **微分增益**
- **积分增益**
- **输出饱和下限**
- **输出饱和上限**
- **比例增益**

## 描述

用于阿克曼和齿轮齿条式转向机构的转向系统

Steering System 模块实现动态转向，用于计算具有摩擦[4]、柔顺性和阿克曼转向特性的齿轮齿条机构的车轮转向角。该模块使用方向盘输入角度或力矩输入、车速、主销后倾角以及左右车轮反馈来计算车轮转向角。该模块使用车辆坐标系。

如果选择 **Power assist** 参数，则可以指定一个作为车速和方向盘输入力矩函数的力矩辅助查找表。该模块使用方向盘输入力矩和力矩辅助来计算转向动力学。如果选择 **Ackerman steering** 参数，则可以指定一个阿克曼百分比值的查找表来计算阿克曼转向效应，或指定一个常数阿克曼百分比，其中 100% 表示完美阿克曼转向。

如果在 **Input signals** 部分选择 **Power assist**、**Ackerman steering** 或 **Kingpin moment**[5] 参数，则可以为外部动力辅助力矩、阿克曼百分比值或主销力矩指定附加输入。

使用 **Steered axle** 参数指定转向的是前轴还是后轴。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前转向右转示意图 |
| **Rear** | 后轴转向  后转向右转示意图 |

### 转向类型

**齿轮齿条式**

对于齿轮齿条式转向，小齿轮旋转引起齿条的直线运动，齿条通过横拉杆和转向臂使车轮转向。

齿轮齿条式转向机构中齿条、拉杆和转向臂示意图

齿轮齿条式转向机构中拉杆示意图

为计算转向车轮角度，该模块使用以下方程。

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 小齿轮角度（输入小齿轮的转向轴角度） |
| *δL* | 左轮转向角 |
| *δR* | 右轮转向角 |
| *TW* | 轮距 |
| *r* | 小齿轮半径 |
| *ΔP* | 齿条位置相对于“正前方”位置的线性变化 |
| *D* | 齿条与转向轴之间的纵向距离 |
| *lrack* | 齿条长度（内侧横拉杆端部之间的距离） |
| *larm* | 转向臂长度 |
| *lrod* | 横拉杆长度 |

### 转向效应

**阿克曼**

对于理想的阿克曼转向，车轮转角具有共同的转弯圆。

阿克曼转向绕转弯圆右转示意图

为计算理想车轮转角，该模块使用以下方程。

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

在计算出理想车轮转角后，该模块使用阿克曼百分比来调整外侧车轮转角。

δo=δi−pAck(δi−δAck)

外侧车轮转角取决于转向方向。

- 右转

  - 外侧转角，
    *δo*，为左车轮
    转角，
    *δL*
  - 内侧转角，
    *δi*，为右车轮
    转角，*δR*
- 左转

  - 外侧转角，
    *δo*，为右
    车轮转角，*δR*
  - 内侧转角，
    *δi*，为左车轮
    转角，*δL*

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 转向角 |
| *δL* | 左车轮转角 |
| *δR* | 右车轮转角 |
| *δo* | 外侧车轮转角 |
| *δi* | 内侧车轮转角 |
| *pAck* | 阿克曼百分比 |
| *TW* | 轮距 |
| *WB* | 轴距 |
| *γ* | 转向比 |

**主销力矩与转向横拉杆力**

如果未在**输入信号**部分选择**主销力矩**参数来指定右和左主销力矩输入，则该模块使用以下方程实现总主销力矩：

Mkp=Mkpfx+Mkpfy+Mkpfz+Mkpmx+Mkpmy+MkpmzwhereMkpfx=0Mkpfy=−Fy(nTcos(ν))cos(δ)nT=Hl+(rsltan(ν))Mkpfz=−(Fzsin(λ)rssin(δ))+(Fzsin(ν)rscos(δ))rs=Kpoffset−(rsltan(λ))Mkpmx=0Mkpmy=0Mkpmz=Mzcos((λ2+ν2)0.5)

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *Mkp* | 总主销力矩 |
| *Mkpfx* | 驱动力产生的力矩 |
| *Mkpfy* | 侧向力产生的力矩 |
| *Mkpfz* | 垂直力产生的力矩 |
| *Mkpmx* | 轮胎翻转力矩 |
| *Mkpmy* | 轮胎滚动阻力力矩 |
| *Mkpmz* | 轮胎回正力矩 |
| *Fy* | *Fy* 轮胎输入 |
| *nT* | 主销后倾拖距 |
| *ν* | 动态主销后倾角输入 |
| *δ* | 动态转向角 |
| *ƛ* | 主销内倾角 |
| *Fz* | *Fz* 轮胎输入 |
| *rs* | 主销偏移距 |
| *Mz* | *Mz* 轮胎输入 |
| *Kpoffset* | 主销偏移量 |
| *Hl* | 轮毂前伸量 |
| *rsl* | 静态加载半径 |

该模块使用以下方程实现转向横拉杆力：

Ftie=MkpLsacos(λ)cos(δ)whereLsa=(rskrcos(λ)cos(ν)π)

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *Ftie* | 转向横拉杆力 |
| *Mkp* | 主销力矩 |
| *Lsa* | 齿轮齿条转向的摆臂长度 |
| *ƛ* | 主销内倾角 |
| *δ* | 动态转向角 |
| *rs* | 总转向比 |
| *kr* | 齿条增益 |
| *ν* | 动态主销后倾角输入 |
