---
type: simulink-block
title: 'Kinematic Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'kinematicsteering'
documentation_source_path: 'ref/kinematicsteering.html'
language: zh-CN
chinese_source: worker-translation
---

# Kinematic Steering

## 端口

### 输入

### **AngIn** — 转向角 `scalar`

转向角，*δin*，单位为
rad。

使用 **转向范围, StrgRng** 参数
指定转向角范围。默认情况下，该值设置为 1.25\*pi，
这会将转向角限制在 -1.25\*pi 到
1.25\*pi 的范围内。

### **PctAckIn** — Ackerman 百分比 `scalar`

Ackerman 百分比，*δin*，单位为
percent。

#### 依赖项

要创建此输入端口：

- 将 **类型** 设置为
  `Ackerman`。
- 在 **Ackerman 转向** 窗格中，
  选择 **输入百分比
  Ackerman**。
### 输出

### **Info** — 总线信号 bus

总线信号包含此模块计算。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `InstStrgRatio` | 瞬时转向比 | *γ* | NA |

### **AngLft** — 左轮角度 `scalar`

左轮角度，*δL*，单位为
rad。

### **AngRght** — 右轮角度 `scalar`

右轮角度，*δR*，单位为
rad。

## 参数

### **类型** — 选择转向类型 `Ackerman` (default) | `Rack and pinion` | `Parallel`

要指定转向
类型，请使用 **类型** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想 Ackerman 转向。车轮角度具有共同转弯圆心。 |
| `Rack and pinion` | 理想 rack-and-pinion 转向。齿轮将转向旋转转换为直线运动。 |
| `Parallel` | 平行转向。车轮角度相等。 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgType` |
| **值：** | `Ackerman` (default) | `Rack and pinion` | `Parallel` |
| **数据类型：** | `character vector` |

### **参数化方式** — 选择参数化 `Constant` (default) | `Lookup table`

要指定转向机构的
数据类型，请使用 **参数化方式**
参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常数参数数据。 |
| `Lookup table` | 转向机构为参数数据实现查找表。 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatioType` |
| **值：** | `Constant` (default) | `Lookup table` |
| **数据类型：** | `character vector` |

### **位置** — 选择位置 **Front** (default) | **Rear**

使用 **转向轴** 参数
指定是前轴还是后轴转向。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前轮转向右转的图 |
| **Rear** | 后轴转向  后轮转向右转的图 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Loc` |
| **值：** | `Front` (default) | `Rear` |
| **数据类型：** | `character vector` |

### **归一化因子, NrmlFctr** — 调整转向角 `scalar`

因子，*NrmFctr*，模块
用于调整转向比，*γ* 或小齿轮半径，
*r*。仅当将 **参数化方式** 设置为
`Constant` 时，模块才能归一化。

要调整转向比或小齿轮半径，请点击
**Normalize**。

| 转向类型 | 归一化 |
| --- | --- |
| `Ackerman`  `Parallel` | 模块将 **转向比, StrgRatio** 参数更新为由以下方程指定的归一化值 *γnrm*。  γnrm=1NrmFctr |
| `Rack and pinion` | 模块使用归一化因子 *NrmFctr* 更新 **小齿轮半径, PnnRadius** 参数。 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NrmlFctr` |
| **值：** | `scalar` |
| **数据类型：** | `double` |

#### 通用

### **轮距, TrckWdth** — 宽度 `1` (default) | `scalar`

轮距，*TW*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为
`Ackerman` 或 `Rack and
pinion`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrckWdth` |
| **值：** | `1` (default) | `scalar` |
| **数据类型：** | `double` |

### **轴距, WhlBase** — 轴距 `1.524` (default) | `scalar`

轴距，*WB*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为
`Ackerman`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlBase` |
| **值：** | `1.524` (default) | `scalar` |
| **数据类型：** | `double` |

### **死区, Db** — 死区 `0` (default) | `scalar`

在小齿轮接合齿轮之前的死区转向角，单位为 rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Db` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **转向范围, StrgRng** — 转向盘角度输入范围 `1.25*pi` (default) | `scalar`

转向盘角度输入范围，单位为 rad。模块限制转向盘
输入角度保持在转向范围内。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRng` |
| **值：** | `1.25*pi` (default) | `scalar` |
| **数据类型：** | `double` |

### **转向比, StrgRatio** — 比值 `100` (default) | `scalar`

转向比，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **类型** 设置为 `Ackerman` 或
  `Parallel`。
- 将 **参数化方式** 设置为
  `Constant`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatio` |
| **值：** | `100` (default) | `scalar` |
| **数据类型：** | `double` |

### **转向角断点, StrgAngBpts** — 断点 `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | `vector`

转向角断点，单位为 rad。

#### 依赖项

要创建此参数，请将 **参数化方式** 设置为
`Lookup table`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgAngBpts` |
| **值：** | `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | `vector` |
| **数据类型：** | `double` |

### **转向比表, StrgRatioTbl** — 表 `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]` (default) | `vector`

转向比表，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **类型** 设置为 `Ackerman` 或
  `Parallel`。
- 将 **参数化方式** 设置为 `Lookup
  table`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatioTbl` |
| **值：** | `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]` (default) | `vector` |
| **数据类型：** | `double` |

#### 齿轮齿条

### **转向臂长度, StrgArmLngth** — 长度 `0.1` (default) | `scalar`

转向臂长度，*larm*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为 `Rack and
pinion`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgArmLngth` |
| **值：** | `0.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **齿条壳体长度, RckCsLngth** — 长度 `0.5` (default) | `scalar`

齿条壳体长度，*lrack*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为 `Rack and
pinion`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RckCsLngth` |
| **值：** | `0.5` (default) | `scalar` |
| **数据类型：** | `double` |

### **横拉杆长度, TieRodLngth** — 长度 `0.248` (default) | `scalar`

横拉杆长度，*lrod*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为 `Rack and
pinion`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TieRodLngth` |
| **值：** | `0.248` (default) | `scalar` |
| **数据类型：** | `double` |

### **轴线与齿条之间的距离, D** — 距离 `0.2` (default) | `scalar`

轴线与齿条之间的距离，*D*，单位为 m。

#### 依赖项

要创建此参数，请将 **类型** 设置为 `Rack and
pinion`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `D` |
| **值：** | `0.2` (default) | `scalar` |
| **数据类型：** | `double` |

### **小齿轮半径, PnnRadius** — 半径 `0.0057` (default) | `scalar`

小齿轮半径，*r*，单位为 m。

#### 依赖项

要创建此参数：

- 将 **类型** 设置为 `Rack and
  pinion`。
- 将 **参数化方式** 设置为
  `Constant`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PnnRadius` |
| **值：** | `0.0057` (default) | `scalar` |
| **数据类型：** | `double` |

### **小齿轮半径表, PnnRadiusTbl** — 表 `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]` (default) | `vector`

小齿轮半径表，*r*，单位为 m。

#### 依赖项

要创建此参数：

- 将 **类型** 设置为 `Rack and
  pinion`。
- 将 **参数化方式** 设置为 `Lookup
  table`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PnnRadiusTbl` |
| **值：** | `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]` (default) | `vector` |
| **数据类型：** | `double` |

#### Ackerman 转向

### **输入百分比 Ackerman** — 创建 `PctAckIn` 输入端口 `off` (default) | `on`

选择以创建 `PctAckIn` 输入端口。

#### 依赖项

要启用此参数，请将 **类型** 设置为
`Ackerman`。

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `PctAckIn` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

### **百分比 Ackerman, PctAck** — 百分比 Ackerman 常数 `100` (default) | `scalar`

百分比 Ackerman 的常数值，单位为 percent。

#### 依赖项

要启用此参数：

- 将 **类型** 设置为
  `Ackerman`
- 将 **参数化方式** 设置为
  `Constant`
- 清除 **输入百分比 Ackerman**

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `PctAck` |
| **值：** | `100` (default) | `scalar` |
| **数据类型：** | `double` |

### **百分比 Ackerman 表, PctAckTbl** — 百分比 Ackerman 表 `ones(1,11)*100` (default) | `vector`

作为转向角 *δin* 函数的百分比 Ackerman 值表，
单位为 percent。

#### 依赖项

要启用此参数：

- 将 **类型** 设置为
  `Ackerman`
- 将 **参数化方式** 设置为
  `Constant`
- 清除 **输入百分比 Ackerman**

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `PctAckTbl` |
| **值：** | `ones(1,11)*100` (default) | `vector` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

用于 Ackerman、rack-and-pinion 和 parallel 转向机构的运动学转向

Kinematic Steering 模块实现转向模型，以确定
Ackerman、rack-and-pinion 和 parallel 转向机构的左、右车轮角度。该模块使用车辆坐标系。

要指定转向类型，请使用
**类型** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想 Ackerman 转向，由百分比 Ackerman 调整。车轮角度具有共同转弯圆心。 |
| `Rack and pinion` | 理想 rack-and-pinion 转向。齿轮将转向旋转转换为直线运动。 |
| `Parallel` | 平行转向。车轮角度相等。 |

要指定转向机构的
数据类型，请使用 **参数化方式**
参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常数参数数据。 |
| `Lookup table` | 转向机构为参数数据实现查找表。 |

使用 **转向轴** 参数
指定是前轴还是后轴转向。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前轮转向右转的图 |
| **Rear** | 后轴转向  后轮转向右转的图 |

### 转向类型

**Ackerman**

对于理想 Ackerman 转向，车轮转角具有共同的转向圆。

图：Ackerman 转向绕转向圆右转

为了计算理想车轮转角，该模块使用以下方程。

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

在模块计算出理想车轮转角后，它使用 Ackerman 百分比来调整外侧车轮转角。

δo=δi−pAck(δi−δAck)

外侧车轮转角取决于转向方向。

- 右转

  - 外侧转角 *δo* 是左轮转角 *δL*
  - 内侧转角 *δi* 是右轮转角 *δR*
- 左转

  - 外侧转角 *δo* 是右轮转角 *δR*
  - 内侧转角 *δi* 是左轮转角 *δL*

图示和方程使用这些变量。

|  |  |
| --- | --- |
| *δin* | 转向角 |
| *δL* | 左轮转角 |
| *δR* | 右轮转角 |
| *δo* | 外侧车轮转角 |
| *δi* | 内侧车轮转角 |
| *pAck* | Ackerman 百分比 |
| *TW* | 轮距 |
| *WB* | 轴距 |
| *γ* | 转向比 |

**Rack-and-Pinion**

对于理想 Rack-and-Pinion 转向，齿轮将转向旋转转换为直线运动。

图：Rack-and-Pinion 转向机构中的齿条、拉杆和转向臂

图：Rack-and-Pinion 转向机构中的拉杆

为了计算转向角，该模块使用以下方程。

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

图示和方程使用这些变量。

|  |  |
| --- | --- |
| *δin* | 方向盘转角 |
| *δL* | 左轮转角 |
| *δR* | 右轮转角 |
| *TW* | 轮距 |
| *r* | 小齿轮半径 |
| *ΔP* | 齿条位置的线性变化 |
| *D* | 前轴与齿条之间的距离 |
| *lrack* | 齿条壳体长度 |
| *larm* | 转向臂长度 |
| *lrod* | 横拉杆长度 |

**Parallel**

对于平行转向，车轮转角相等。

图：车轮转角相等的平行转向

为了计算转向角，该模块使用以下方程。

δR=δL=δinγ

图示和方程使用这些变量。

|  |  |
| --- | --- |
| *δin* | 方向盘转角 |
| *δL* | 左轮转角 |
| *δR* | 右轮转角 |
| *γ* | 转向比 |
