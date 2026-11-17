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

转向角，*δin*，单位为 rad。

使用 **Steering range, StrgRng** 参数指定转向角范围。默认情况下，该值设置为 1.25\*pi，这将转向角限制在 -1.25\*pi 到 1.25\*pi 的范围内。

### **PctAckIn** — 阿克曼百分比 `scalar`

阿克曼百分比，*δin*，单位为百分比。

#### 依赖关系

要创建此输入端口：

- 将 **Type** 设置为 `Ackerman`。
- 在 **Ackerman Steering** 窗格中，选择 **Input percent Ackerman**。

### 输出

### **Info** — 总线信号 bus

总线信号包含此模块的计算结果。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `InstStrgRatio` | 瞬时转向比 | *γ* | NA |

### **AngLft** — 左轮转角 `scalar`

左轮转角，*δL*，单位为 rad。

### **AngRght** — 右轮转角 `scalar`

右轮转角，*δR*，单位为 rad。

## 参数

### **Type** — 选择转向类型 `Ackerman`（默认）| `Rack and pinion` | `Parallel`

要指定转向类型，请使用 **Type** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想阿克曼转向。车轮转角具有共同的转弯圆心。 |
| `Rack and pinion` | 理想齿轮齿条转向。齿轮将转向旋转转换为直线运动。 |
| `Parallel` | 平行转向。车轮转角相等。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgType` |
| **值：** | `Ackerman`（默认）| `Rack and pinion` | `Parallel` |
| **数据类型：** | `character vector` |

### **Parametrized by** — 选择参数化方式 `Constant`（默认）| `Lookup table`

要指定转向机构的参数数据类型，请使用 **Parametrized by** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常量参数数据。 |
| `Lookup table` | 转向机构使用查找表作为参数数据。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatioType` |
| **值：** | `Constant`（默认）| `Lookup table` |
| **数据类型：** | `character vector` |

### **Location** — 选择位置 **Front**（默认）| **Rear**

使用 **Steered axle** 参数指定转向的是前轴还是后轴。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向 前轮右转示意图 |
| **Rear** | 后轴转向 后轮右转示意图 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Loc` |
| **值：** | `Front`（默认）| `Rear` |
| **数据类型：** | `character vector` |

### **Normalization factor, NrmlFctr** — 调整转向角 `scalar`

模块用于调整转向比 *γ* 或小齿轮半径 *r* 的因子 *NrmFctr*。仅当 **Parametrized by** 设置为 `Constant` 时，模块才能进行归一化。

要调整转向比或小齿轮半径，请点击 **Normalize**。

| 转向类型 | 归一化 |
| --- | --- |
| `Ackerman`  `Parallel` | 模块将 **Steering ratio, StrgRatio** 参数更新为此方程指定的归一化值 *γnrm*。  γnrm=1NrmFctr |
| `Rack and pinion` | 模块使用归一化因子 *NrmFctr* 更新 **Pinion radius, PnnRadius** 参数。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NrmlFctr` |
| **值：** | `scalar` |
| **数据类型：** | `double` |

#### 常规

### **Track width, TrckWdth** — 宽度 `1`（默认）| `scalar`

轮距，*TW*，单位为 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Ackerman` 或 `Rack and pinion`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrckWdth` |
| **值：** | `1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Wheel base, WhlBase** — 轴距 `1.524`（默认）| `scalar`

轴距，*WB*，单位为 m。

#### 依赖项

要创建此参数，请将 **Type** 设置为 `Ackerman`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlBase` |
| **值：** | `1.524`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Deadband, Db** — 死区 `0`（默认）| `scalar`

小齿轮啮合齿轮前的转向角死区，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Db` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Steering range, StrgRng** — 方向盘角度输入范围 `1.25*pi`（默认）| `scalar`

方向盘角度输入范围，单位为 rad。该模块限制方向盘输入角度保持在转向范围内。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRng` |
| **值：** | `1.25*pi`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Steering ratio, StrgRatio** — 传动比 `100`（默认）| `scalar`

转向传动比，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Ackerman` 或 `Parallel`。
- 将 **Parametrized by** 设置为 `Constant`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatio` |
| **值：** | `100`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Steering angle breakpoints, StrgAngBpts** — 断点 `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]`（默认）| `vector`

转向角断点，单位为 rad。

#### 依赖项

要创建此参数，请将 **Parametrized by** 设置为 `Lookup table`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgAngBpts` |
| **值：** | `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Steering ratio table, StrgRatioTbl** — 表格 `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]`（默认）| `vector`

转向传动比表格，*γ*，无量纲。

#### 依赖项

要创建此参数：

- 将 **Type** 设置为 `Ackerman` 或 `Parallel`。
- 将 **Parametrized by** 设置为 `Lookup table`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgRatioTbl` |
| **值：** | `[13.5000 13.3750 13.2500 13.1250 13.0000 13.0000 13.0000 13.1250 13.2500 13.3750 13.5000]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 齿轮齿条

### **转向臂长度，StrgArmLngth** — 长度 `0.1`（默认） | `scalar`

转向臂长度，*larm*，单位为 m。

#### 依赖关系

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
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **齿条壳体长度，RckCsLngth** — 长度 `0.5`（默认） | `scalar`

齿条壳体长度，*lrack*，单位为 m。

#### 依赖关系

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
| **值：** | `0.5`（默认） | `scalar` |
| **数据类型：** | `double` |

### **横拉杆长度，TieRodLngth** — 长度 `0.248`（默认） | `scalar`

横拉杆长度，*lrod*，单位为 m。

#### 依赖关系

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
| **值：** | `0.248`（默认） | `scalar` |
| **数据类型：** | `double` |

### **轴线与齿条之间的距离，D** — 距离 `0.2`（默认） | `scalar`

轴线与齿条之间的距离，*D*，单位为 m。

#### 依赖关系

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
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **小齿轮半径，PnnRadius** — 半径 `0.0057`（默认） | `scalar`

小齿轮半径，*r*，单位为 m。

#### 依赖关系

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
| **值：** | `0.0057`（默认） | `scalar` |
| **数据类型：** | `double` |

### **小齿轮半径表，PnnRadiusTbl** — 表 `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]`（默认） | `vector`

小齿轮半径表，*r*，单位为 m。

#### 依赖关系

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
| **值：** | `[0.0055 0.0055 0.0056 0.0057 0.0057 0.0057 0.0058 0.0057 0.0056 0.0055 0.0055]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 阿克曼转向

### **输入阿克曼百分比** — 创建 `PctAckIn` 输入端口 `off`（默认） | `on`

选择以创建 `PctAckIn` 输入端口。

#### 依赖关系

要启用此参数，请将 **类型** 设置为
`Ackerman`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PctAckIn` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Percent Ackerman, PctAck** — 阿克曼百分比常数 `100`（默认） | `scalar`

阿克曼百分比的常数值，以百分比表示。

#### 依赖关系

要启用此参数：

- 将 **Type** 设置为 `Ackerman`
- 将 **Parametrized by** 设置为 `Constant`
- 清除 **Input Percent Ackerman**

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PctAck` |
| **值：** | `100`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Percent Ackerman table, PctAckTbl** — 阿克曼百分比表 `ones(1,11)*100`（默认） | `vector`

阿克曼百分比值作为转向角 *δin* 的函数表，以百分比表示。

#### 依赖关系

要启用此参数：

- 将 **Type** 设置为 `Ackerman`
- 将 **Parametrized by** 设置为 `Constant`
- 清除 **Input Percent Ackerman**

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PctAckTbl` |
| **值：** | `ones(1,11)*100`（默认） | `vector` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

用于 Ackerman、齿轮齿条和平行转向机构的运动学转向

Kinematic Steering 模块实现了一个转向模型，用于确定 Ackerman、齿轮齿条和平行转向机构的左轮和右轮角度。该模块使用车辆坐标系。

要指定转向类型，请使用 **Type** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Ackerman` | 理想 Ackerman 转向，由阿克曼百分比调整。车轮角度具有共同的转弯圆心。 |
| `Rack and pinion` | 理想齿轮齿条转向。齿轮将转向旋转转换为线性运动。 |
| `Parallel` | 平行转向。车轮角度相等。 |

要指定转向机构的数据类型，请使用 **Parametrized by** 参数。

| 设置 | 模块实现 |
| --- | --- |
| `Constant` | 转向机构使用常数参数数据。 |
| `Lookup table` | 转向机构实现参数数据的查找表。 |

使用 **Steered axle** 参数指定转向的是前轴还是后轴。

| 设置 | 实现 |
| --- | --- |
| **Front** | 前轴转向  前轮右转示意图 |
| **Rear** | 后轴转向  后轮右转示意图 |

### 转向类型

**阿克曼**

对于理想阿克曼转向，车轮转角具有共同的转弯圆。

阿克曼转向绕转弯圆右转示意图

为计算理想车轮转角，该模块使用以下方程。

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

该模块计算理想车轮转角后，使用阿克曼百分比调整外侧车轮转角。

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
    车轮转角，
    *δR*
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

**齿轮齿条**

对于理想齿轮齿条转向，齿轮将转向旋转转换为直线运动。

齿轮齿条转向机构中齿条、拉杆和转向臂示意图

齿轮齿条转向机构中拉杆示意图

为计算转向角，该模块使用以下方程。

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 方向盘转角 |
| *δL* | 左车轮转角 |
| *δR* | 右车轮转角 |
| *TW* | 轮距 |
| *r* | 小齿轮半径 |
| *ΔP* | 齿条位置的线性变化 |
| *D* | 前轴与齿条之间的距离 |
| *lrack* | 齿条壳体长度 |
| *larm* | 转向臂长度 |
| *lrod* | 横拉杆长度 |

**平行**

对于平行转向，车轮转角相等。

平行转向中车轮转角相等的示意图

为计算转向角，该模块使用以下方程。

δR=δL=δinγ

图示和方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 方向盘转角 |
| *δL* | 左车轮转角 |
| *δR* | 右车轮转角 |
| *γ* | 转向比 |
