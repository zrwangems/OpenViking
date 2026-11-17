---
type: simulink-block
title: 'Battery Equivalent Circuit'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells'
documentation_page: 'batteryequivalentcircuit'
documentation_source_path: 'ref/batteryequivalentcircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Equivalent Circuit

## 端口

### 守恒端口

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

与电池热质量关联的热守恒端口。

#### 依赖关系

要启用此端口，请在**主**部分中，将**热模型**参数设置为 `Lumped thermal mass`。

### **HDist** — 离散化电池热质量热节点数组

*自 R2024b 起*

与离散化电池热质量关联的热守恒端口。此列节点数组的每个元素表示热模型中沿电芯高度方向的一个离散化元素。此列向量的大小取决于**热模型数量**参数的值。

下表显示了此端口处节点数组的元素与您为电池模型选择的热选项之间的关系：

| 热选项 | 热节点连接 |
| --- | --- |
| 冷却板 | 热节点数组的第一个元素连接到顶部冷却板。热节点数组的最后一个元素连接到底部冷却板。 |
| 环境热路径 | 热节点数组中的每个元素连接到各自的热阻。数组中的所有元素还连接到一个单一的顶层节点。 |
| 冷却液热路径 |
| 电芯间热路径 | 热节点数组的每个元素连接到相邻电芯的对应元素。 |
| 电芯间辐射路径 |
| 蛇形冷却板 | 此选项提供在特定电芯边界处与电芯热节点的接口。即使对于热离散化电芯，该接口在边界处也仅提供一个热节点元素。 |
| 边界连接 |

#### 依赖关系

要启用此端口，请在**主**部分中，将**热模型**参数设置为 `Height distributed thermal mass`。

## 参数

### **Selected part** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化为表示特定供应商组件的选项。点击 **<click to select>** 超链接以打开模块参数化管理器窗口。有关模块参数化管理器的详细信息，请参阅加载预定义参数化 (Simscape Electrical)。

### 主

### **Battery capacity** — 满充电时的电池容量 `27` `A*hr`（默认）| 非负标量

电池完全充电时的容量。模块通过将累积电荷除以此值来计算 SOC。模块通过对电池电流进行积分来计算累积电荷。

### **Thermal model** — 定义电池热模型的选项 `Constant temperature`（默认）| `No temperature dependence` | `Lumped thermal mass` | `Height distributed thermal mass`

用于定义电池热模型的选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ThermalModel` |
| **值：** | `"simscape.battery.enum.cells.BatteryThermalModel.ConstantTemperature"`（默认）| `"simscape.battery.enum.cells.BatteryThermalModel.LumpedThermalMass"` | `"simscape.battery.enum.cells.BatteryThermalModel.TemperatureIndependent"` | `"simscape.battery.enum.cells.BatteryThermalModel.HeightDistributedMass"` |

### **Extrapolation method for all tables** — 表格的外推方法 `Nearest`（默认）| `Linear` | `Error`

所有基于表格的参数的外推方法：

- `Linear` — 通过在已知数据末端创建切线并将其延伸到该限制之外来估计数据之外的值。
- `Nearest` — 在查询点处外推值，该值为最近采样网格点处的值。
- `Error` — 如果值超出已知数据则返回错误。如果选择此选项，模块不使用外推。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationMethod` |
| **值：** | `"simscape.enum.extrapolation.nearest"`（默认）| `"simscape.enum.extrapolation.linear"` | `"simscape.enum.extrapolation.error"` |

### 开路电压

### **State of charge breakpoints, SOC** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围 [0, 1] 内的值向量

您在此处指定查找数据的 SOC 断点。此向量必须严格递增。模块根据**电池容量**参数中指定的标称电池容量计算 SOC 值。SOC 是可用电池电荷 *q*battery 与标称电池容量 *q*nom*(T,n)* 的比值。您必须确保，对于每个温度，SOC 值 1 表示**电池容量**参数中指定的相应电池电荷容量，假设为新电池且循环次数 *N* 等于 1 且 *δAH(n = 1, Tfade) = 0*。

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH

### **Temperature breakpoints, T** — 温度断点 `[278, 293, 313]` `K`（默认）| 正值向量

您在此处指定查找数据的温度断点。此向量必须严格递增，且每个元素必须大于 `0` `K`。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`。

### **Open-circuit voltage, OCV(SOC)** — 指定 SOC 下的开路电压查找数据 `[3.5057, 3.566, 3.6337, 3.7127, 3.9259, 4.0777, 4.1928]` `V`（默认）| 非负值向量

基本电池模型在指定 SOC 下的开路电压查找数据。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`。

### **Open-circuit voltage, OCV(SOC,T)** — 指定 SOC 和温度下的开路电压查找数据 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` `V`（默认）| 非负值矩阵

基本电池模型在指定 SOC 和温度断点下的开路电压查找数据。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`。

### **Terminal voltage operating range, [Min Max]** — 端子电压工作范围 `[0, inf]` `V`（默认）| 非负值向量

端子电压的工作范围。此参数必须是一个 1×2 向量，用于定义端子电压的最小值和最大值。

### **Hysteresis model** — 对迟滞建模的选项 `None`（默认）| `One-state model`

用于对电池迟滞建模的选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `HysteresisModel` |
| **值：** | `"simscape.battery.enum.cells.HysteresisModel.none"`（默认）| `"simscape.battery.enum.cells.HysteresisModel.oneStateModel"` |

### **Maximum dynamic hysteresis voltage, MaximumHysteresisVoltage(SOC)** — 指定 SOC 下的最大动态迟滞电压 `[0, 0, 0, 0, 0, 0, 0]` `V`（默认）| 非负值向量

指定 SOC 断点下的最大动态迟滞电压。此参数仅影响迟滞建模的动态部分。瞬时迟滞电压与此参数无关。

此参数的值必须是与**荷电状态断点，SOC**参数大小相同的向量。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**迟滞模型**设置为 `One-state model`。

### **Instantaneous hysteresis voltage, InstantaneousHysteresisVoltage(SOC)** — 指定 SOC 下的瞬时迟滞电压 `[0, 0, 0, 0, 0, 0, 0]` `V`（默认）| 非负值向量

指定 SOC 断点下的瞬时迟滞电压。此参数的值必须是与**荷电状态断点，SOC**参数大小相同的向量。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**迟滞模型**设置为 `One-state model`。

### **Hysteresis rate, HysteresisRate(SOC)** — 指定 SOC 下的迟滞率 `0.1`（默认）| 非负标量 | 非负值向量

指定 SOC 断点下的迟滞率。此参数的值必须是与**荷电状态断点，SOC**参数大小相同的标量或向量。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**迟滞模型**设置为 `One-state model`。

### **Maximum dynamic hysteresis voltage, MaximumHysteresisVoltageThermal(SOC,T)** — 指定 SOC 和温度下的最大动态迟滞电压 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` `V`（默认）| 非负值矩阵

指定 SOC 和温度断点下的最大动态迟滞电压。此参数仅影响迟滞建模的动态部分。瞬时迟滞电压与此参数无关。

此参数的值必须是一个矩阵，其行数和列数分别等于**荷电状态断点，SOC**和**温度断点，T**参数的大小。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`，并将**迟滞模型**设置为 `One-state model`。

### **Instantaneous hysteresis voltage, InstantaneousHysteresisVoltageThermal(SOC,T)** — 指定 SOC 和温度下的瞬时迟滞电压 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` `V`（默认）| 非负值矩阵

指定 SOC 和温度断点下的瞬时迟滞电压。此参数的值必须是一个矩阵，其行数和列数分别等于**荷电状态断点，SOC**和**温度断点，T**参数的大小。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`，并将**迟滞模型**设置为 `One-state model`。

### **Hysteresis rate, HysteresisRateThermal(SOC,T)** — 指定 SOC 和温度下的迟滞率 `0.1`（默认）| 非负标量 | 非负值矩阵

指定 SOC 和温度断点下的迟滞率。此参数的值必须是一个标量或矩阵，其行数和列数分别等于**荷电状态断点，SOC**和**温度断点，T**参数的大小。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`，并将**迟滞模型**设置为 `One-state model`。

### 过电位

### **State of charge breakpoints for resistance, SOC** — 电阻参数的 SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围 [0, 1] 内的值向量

您在此处为电阻参数指定查找数据的 SOC 断点。此向量必须严格递增。模块根据**电池容量**参数中指定的标称电池容量计算 SOC 值。

### **Temperature breakpoints for resistance, T** — 电阻参数的温度断点 `[278, 293, 313]` `K`（默认）| 正值向量

您在此处为电阻参数指定查找数据的温度断点。此向量必须严格递增，且其元素必须大于 `0` `K`。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`。

### **Current breakpoints for resistance, I** — 电阻参数的电流断点 `[-1, 0, 1]` `A`（默认）| 标量向量

*自 R2025a 起*

您在此处为电阻参数指定查找数据的电流断点。

#### 依赖关系

要启用此参数，请将**电阻参数的电流依赖性**设置为 `Lookup tables (current dependent)`。

### **Current dependence for resistance parameters** — 启用电阻参数电流依赖性的选项 `Disabled`（默认）| `Lookup tables (current directionality dependent)` | `Lookup tables (current dependent)`

*自 R2025a 起*

用于启用电阻参数电流依赖性的选项。如果将此参数设置为 `Lookup tables (current directionality dependent)`，则瞬时电阻和极化电阻取决于电流方向。如果将此参数设置为 `Lookup tables (current dependent)`，则瞬时电阻和极化电阻取决于电流。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CurrentDependence` |
| **值：** | `"simscape.battery.enum.cells.CurrentDependence.Disabled"`（默认）| `"simscape.battery.enum.cells.CurrentDependence.CurrentDirectionalityDependent"` | `"simscape.battery.enum.cells.CurrentDependence.CurrentDependent"` |

### **Instantaneous resistance, R0(SOC)** — 指定 SOC 下电池的瞬时电阻 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认）| 非负值向量

指定 SOC 断点下电池的瞬时电阻。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**电阻参数的电流依赖性**设置为 `Disabled`。

### **Instantaneous resistance, R0(SOC,T)** — 指定 SOC 和温度下电池的瞬时电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认）| 非负值矩阵

指定 SOC 和温度断点下电池的瞬时电阻。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `Constant temperature`、`Lumped thermal mass` 或 `Height distributed thermal mass`，并将**电阻参数的电流依赖性**设置为 `Disabled`。

### **Instantaneous resistance during discharging, R0(SOC)** — 放电阶段指定 SOC 下电池的瞬时电阻 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认）| 非负值向量

放电阶段指定 SOC 断点下电池的瞬时电阻。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**电阻参数的电流依赖性**设置为 `Lookup tables (current directionality dependent)`。

### **Instantaneous resistance during charging, R0(SOC)** — 充电阶段指定 SOC 下电池的瞬时电阻 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认）| 非负值向量

充电阶段指定 SOC 断点下电池的瞬时电阻。

#### 依赖关系

要启用此参数，请将**热模型**设置为 `No temperature dependence`，并将**电阻参数的电流依赖性**设置为 `Lookup tables (current directionality dependent)`。

### **Instantaneous resistance during charging, R0(SOC,T)** — 充电阶段在指定 SOC 和温度下的电池瞬时电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认）| 非负值矩阵

充电阶段在指定 SOC 和温度断点下的电池瞬时电阻。

#### 依赖关系

要启用此参数，请将 **Thermal model** 设置为
`Constant temperature`、
`Lumped thermal mass` 或
`Height distributed thermal mass`，并将
**Current dependence for resistance
parameters** 设置为 `Lookup tables (current
directionality dependent)`。

### **Instantaneous resistance during discharging, R0(SOC,T)** — 放电阶段在指定 SOC 和温度下的电池瞬时电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认）| 非负值矩阵

放电阶段在指定 SOC 和温度断点下的电池瞬时电阻。

#### 依赖关系

要启用此参数，请将 **Thermal model** 设置为
`Constant temperature`、
`Lumped thermal mass` 或
`Height distributed thermal mass`，并将
**Current dependence for resistance
parameters** 设置为 `Lookup tables (current
directionality dependent)`。

### **Instantaneous resistance, R0(SOC,I)** — 在指定 SOC 和电流下的电池瞬时电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认）| 非负值矩阵

*自 R2025a 起*

在指定 SOC 和电流断点下的电池瞬时电阻。

#### 依赖关系

要启用此参数，请将 **Thermal model**
设置为 `No temperature dependence`，并将
**Current dependence for resistance
parameters** 设置为 `Lookup tables (current
dependent)`。

### **Instantaneous resistance, R0(SOC,T,I)** — 在指定 SOC、温度和电流下的电池瞬时电阻 `repmat([.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089], 1, 1, 3)` `Ohm`（默认）| 非负值三维数组

*自 R2025a 起*

在指定 SOC、温度和电流断点下的电池瞬时电阻。

#### 依赖关系

要启用此参数，请将 **Thermal model**
设置为 `Constant temperature`、
`Lumped thermal mass` 或
`Height distributed thermal mass`，并将
**Current dependence for resistance
parameters** 设置为 `Lookup tables (current
dependent)`。

### **Parallel resistor capacitor pairs** — 用于对电池充电动态建模的选项 `No dynamics`（默认）| `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics`

用于对电池充电动态建模的选项。此参数确定等效电路中的并联 RC 段数。

- `No dynamics` — 等效电路不包含并联 RC 段。电池的端电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` —
  等效电路包含一个并联 RC 段。
- `Two time-constant dynamics` —
  等效电路包含两个并联 RC 段。
- `Three time-constant dynamics` —
  等效电路包含三个并联 RC 段。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCPairs` |
| **值：** | `"simscape.battery.enum.cells.RCPairs.noDynamics"`（默认）| `"simscape.battery.enum.cells.RCPairs.rc1"` | `"simscape.battery.enum.cells.RCPairs.rc2"` | `"simscape.battery.enum.cells.RCPairs.rc3"` |

### **First polarization resistance, R1(SOC)** — 在指定 SOC 下的第一并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

在指定 SOC 断点下的第一并联 RC 电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant, Tau1(SOC)** — 在指定 SOC 下的第一并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

在指定 SOC 断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant dynamics`
  、`Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second polarization resistance, R2(SOC)** — 在指定 SOC 下的第二并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

在指定 SOC 断点下的第二并联 RC 电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant, Tau2(SOC)** — 在指定 SOC 下的第二并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

在指定 SOC 断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance, R3(SOC)** — 在指定 SOC 下的第三并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

在指定 SOC 断点下的第三并联 RC 电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant, Tau3(SOC)** — 在指定 SOC 下的第三并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

在指定 SOC 断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **First polarization resistance during discharging, R1(SOC)** — 放电阶段在指定 SOC 下的第一并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第一并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant during discharging, Tau1(SOC)** — 放电阶段在指定 SOC 下的第一并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First polarization resistance during charging, R1(SOC)** — 充电阶段在指定 SOC 下的第一并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

充电阶段在指定 SOC 断点下的第一并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant during charging, Tau1(SOC)** — 充电阶段在指定 SOC 下的第一并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `Ohm`（默认）| 正值向量

充电阶段在指定 SOC 断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **Second polarization resistance during discharging, R2(SOC)** — 放电阶段在指定 SOC 下的第二并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第二并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant during discharging, Tau2(SOC)** — 放电阶段在指定 SOC 下的第二并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second polarization resistance during charging, R2(SOC)** — 充电阶段在指定 SOC 下的第二并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

充电阶段在指定 SOC 断点下的第二并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant during charging, Tau2(SOC)** — 充电阶段在指定 SOC 下的第二并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

充电阶段在指定 SOC 断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance during discharging, R3(SOC)** — 放电阶段在指定 SOC 下的第三并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第三并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant during discharging, Tau3(SOC)** — 放电阶段在指定 SOC 下的第三并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

放电阶段在指定 SOC 断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third polarization resistance during charging, R3(SOC)** — 充电阶段在指定 SOC 下的第三并联 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| 正值向量

充电阶段在指定 SOC 下的第三并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant during charging, Tau3(SOC)** — 充电阶段在指定 SOC 下的第三并联 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| 正值向量

充电阶段在指定 SOC 下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **First polarization resistance, R1(SOC,T)** — 在指定 SOC 和温度下的第一并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

在指定 SOC 和温度断点下的第一并联 RC 电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant, Tau1(SOC,T)** — 指定 SOC 和温度下的第一并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

指定 SOC 和温度断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **Second polarization resistance, R2(SOC,T)** — 指定 SOC 和温度下的第二并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

指定 SOC 和温度断点下的第二并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant, Tau2(SOC,T)** — 指定 SOC 和温度下的第二并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

指定 SOC 和温度断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance, R3(SOC,T)** — 指定 SOC 和温度下的第三并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

指定 SOC 和温度断点下的第三并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant, Tau3(SOC,T)** — 指定 SOC 和温度下的第三并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

指定 SOC 和温度断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为
  `Disabled`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **First polarization resistance during discharging, R1(SOC,T)** — 放电阶段指定 SOC 和温度下的第一并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第一并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant during discharging, Tau1(SOC,T)** — 放电阶段指定 SOC 和温度下的第一并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First polarization resistance during charging, R1(SOC,T)** — 充电阶段指定 SOC 和温度下的第一并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第一并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant during charging, Tau1(SOC,T)** — 充电阶段指定 SOC 和温度下的第一并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **Second polarization resistance during discharging, R2(SOC,T)** — 放电阶段指定 SOC 和温度下的第二并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第二并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant during discharging, Tau2(SOC,T)** — 放电阶段指定 SOC 和温度下的第二并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second polarization resistance during charging, R2(SOC,T)** — 充电阶段指定 SOC 和温度下的第二并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第二并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant during charging, Tau2(SOC,T)** — 充电阶段指定 SOC 和温度下的第二并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance during discharging, R3(SOC,T)** — 放电阶段指定 SOC 和温度断点下的第三并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第三并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant during discharging, Tau3(SOC,T)** — 放电阶段指定 SOC 和温度断点下的第三并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

放电阶段指定 SOC 和温度断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third polarization resistance during charging, R3(SOC,T)** — 充电阶段指定 SOC 和温度断点下的第三并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第三并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant during charging, Tau3(SOC,T)** — 充电阶段指定 SOC 和温度断点下的第三并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

充电阶段指定 SOC 和温度断点下的第三并联 RC 电阻。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current directionality
  dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **First polarization resistance, R1(SOC,I)** — 指定 SOC 和电流下的第一并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第一并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant, Tau1(SOC,I)** — 指定 SOC 和电流下的第一并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **Second polarization resistance, R2(SOC,I)** — 指定 SOC 和电流下的第二并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第二并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant, Tau2(SOC,I)** — 指定 SOC 和电流下的第二并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance, R3(SOC,I)** — 指定 SOC 和电流下的第三并联 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第三并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant, Tau3(SOC,I)** — 指定 SOC 和电流下的第三并联 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC 和电流断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为 `No
  temperature dependence`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **First polarization resistance, R1(SOC,T,I)** — 指定 SOC、温度和电流下的第一并联 RC 电阻 `repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm`（默认）| 正值三维数组

*自 R2025a 起*

指定 SOC、温度和电流断点下的第一并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **First time constant, Tau1(SOC,T,I)** — 指定 SOC、温度和电流下的第一并联 RC 时间常数 `repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s`（默认）| 正值三维数组

*自 R2025a 起*

指定 SOC、温度和电流断点下的第一并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `One time-constant
  dynamics`、`Two time-constant
  dynamics` 或 `Three
  time-constant dynamics`。

### **Second polarization resistance, R2(SOC,T,I)** — 指定 SOC、温度和电流下的第二并联 RC 电阻 `repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm`（默认）| 正值三维数组

*自 R2025a 起*

指定 SOC、温度和电流断点下的第二并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Second time constant, Tau2(SOC,T,I)** — 指定 SOC、温度和电流下的第二并联 RC 时间常数 `[repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s`（默认）| 正值三维数组

*自 R2025a 起*

指定 SOC、温度和电流断点下的第二并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Two time-constant dynamics`
  或 `Three time-constant
  dynamics`。

### **Third polarization resistance, R3(SOC,T,I)** — 指定 SOC、温度和电流下的第三并联 RC 电阻 `[repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm`（默认）| 正值三维数组

*自 R2025a 起*

指定 SOC、温度和电流断点下的第三并联 RC 电阻。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Third time constant, Tau3(SOC,T,I)** — 指定 SOC、温度和电流下的第三并联 RC 时间常数 `repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s`（默认）| 正值矩阵

*自 R2025a 起*

指定 SOC、温度和电流断点下的第三并联 RC 时间常数。

#### 依赖关系

要启用此参数，请设置：

- **Thermal model** 为
  `Constant temperature`、
  `Lumped thermal mass` 或
  `Height distributed thermal
  mass`。
- **Current dependence for resistance
  parameters** 为 `Lookup tables
  (current dependent)`。
- **Parallel resistor capacitor pairs**
  为 `Three time-constant
  dynamics`。

### **Self discharge** — 用于对电池自放电电阻建模的选项 `Disabled`（默认）| `Enabled`

用于对电池自放电电阻建模的选项。该模块将此效应建模为基本电池模型端子之间的一个电阻。

随着温度升高，自放电电阻减小。如果电阻减小过快，电池可能会经历热失控和数值不稳定。要解决此不稳定问题，请执行以下步骤：

- 减小热阻。
- 减小自放电电阻相对于温度的梯度。
- 增大自放电电阻。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SelfDischargeResistor` |
| **值**：| `"simscape.battery.enum.cells.BatteryEnable.Disabled"`（默认）| `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **Self-discharge resistance, SelfDischargeR** — 电池的自放电电阻 `7e3` `Ohm`（默认）| 正标量

电池的自放电电阻。该电阻作用于基本电池模型的端子之间。

#### 依赖关系

要启用此参数，请将 **Thermal model** 设置为 `No temperature dependence`，并将 **Self discharge** 设置为 `Enabled`。

### **Self-discharge resistance, SelfDischargeR(T)** — 指定温度下电池的自放电电阻 `[8000, 7000, 6000]` `Ohm`（默认）| 正值向量

指定温度断点下电池的自放电电阻。该电阻作用于基本电池模型的端子之间。

#### 依赖关系

要启用此参数，请将 **Thermal model** 设置为 `Constant temperature` 或 `Lumped thermal mass`，并将 **Self discharge** 设置为 `Enabled`。

### Cycling Aging

### **Cycling aging model** — 用于定义衰减特性的选项 `Disabled`（默认）| `Equations` | `Lookup tables (temperature independent)` | `Lookup tables (constant temperature dependent)` | `Lookup tables (temperature dependent)` | `Lookup tables (temperature and current dependent)`

用于定义衰减特性的选项：

- `Disabled` — 不对衰减特性建模。
- `Equations` — 电池容量和端子电阻与 N 成正比。开路电压与 *N* 成正比。如果启用自放电电阻或任何时间常数，其值与 N 成正比。
- `Lookup tables (temperature
  independent)` — 设置参数百分比变化作为 *N* 函数的表格数据。
- `Lookup tables (constant temperature
  dependent)` — 设置参数百分比变化作为 *N* 和恒定温度函数的表格数据。
- `Lookup
  tables (temperature dependent)` —
  设置参数百分比变化作为 *N* 和可变温度函数的表格数据。此表格数据相对于放电循环次数必须严格单调递增或递减。*（自 R2025a 起）*
- `Lookup
  tables (temperature and current dependent)`
  — 设置参数百分比变化作为 *N*、可变温度和可变电流函数的表格数据。此表格数据相对于放电循环次数必须严格单调递增或递减。*（自 R2025a 起）*

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CyclingAgingMethod` |
| **值**：| `"simscape.battery.enum.cells.CyclingAgingMethod.disabled"`（默认）| `"simscape.battery.enum.cells.CyclingAgingMethod.equations"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableN"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandT"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableT"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableTandI"` |

### **Cycle calculation method** — 用于选择模块如何计算放电循环次数的选项 `Equivalent cycles`（默认）| `Equivalent full cycles`

*自 R2025a 起*

用于选择模块如何计算放电循环次数变化的选项：

- `Equivalent cycles` — 模块使用老化后的容量来计算放电循环次数。
- `Equivalent full cycles` — 模块使用标称容量来计算放电循环次数。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`、
`Lookup tables (temperature
independent)`、`Lookup tables (constant
temperature dependent)`、`Lookup tables
(temperature dependent)` 或 `Lookup
tables (temperature and current dependent)`。

### **Number of discharge cycles, NumDisCycles** — 用于百分比变化计算的循环次数 `100`（默认）| 范围 [1, `inf`) 内的标量

发生指定百分比变化的充放电循环次数。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`。

### **Change in open-circuit voltage after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后开路电压的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后开路电压的百分比变化。

**注意**

如果为此参数指定正值，则开路电压的值增大。如果为此参数指定负值，则开路电压的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`。

### **Change in terminal resistance after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后端子电阻的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后端子电阻的百分比变化。

**注意**

如果为此参数指定正值，则端子电阻的值增大。如果为此参数指定负值，则端子电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`。

### **Change in cell capacity after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后电池容量的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后电池容量的百分比变化。

**注意**

如果为此参数指定正值，则电池容量的值增大。如果为此参数指定负值，则电池容量的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`。

### **Change in self-discharge resistance after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后自放电电阻的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后自放电电阻的百分比变化。

**注意**

如果为此参数指定正值，则自放电电阻的值增大。如果为此参数指定负值，则自放电电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`，并将
**Self discharge** 设置为
`Enabled`。

### **Change in first polarization resistance after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后第一 RC 电阻的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后第一 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第一 RC 电阻的值增大。如果为此参数指定负值，则第一 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`，并将
**Parallel resistor capacitor pairs** 设置为
`One time-constant dynamics`、
`Two time-constant dynamics` 或
`Three time-constant dynamics`。

### **Change in second polarization resistance after NumDisCycles discharge cycles (%)** — *NumDisCycles* 次循环后第二 RC 电阻的百分比变化 `0`（默认）| 标量

电池经历 *NumDisCycles* 次放电循环后第二 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第二 RC 电阻的值增大。如果为此参数指定负值，则第二 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging
model** 设置为 `Equations`，并将
**Parallel resistor capacitor pairs** 设置为
`Two time-constant dynamics` 或
`Three time-constant dynamics`。

### **Change in third polarization resistance after NumDisCycles discharge cycles (%)** — 经过 *NumDisCycles* 次循环后第三 RC 电阻的百分比变化 `0`（默认）| 标量

电池经过 *NumDisCycles* 次放电循环后第三 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第三 RC 电阻的值增加。如果为此参数指定负值，则第三 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Equations`，并将 **Parallel resistor capacitor pairs** 设置为 `Three time-constant dynamics`。

### **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** — 用于百分比变化计算的参考向量或循环次数 `[0, 100, 200, 300]`（默认）| 非负值向量

发生指定百分比变化的充放电循环次数。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`、`Lookup tables (constant temperature dependent)`、`Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`。

### **Temperatures breakpoints for cycling aging data, T** — 模块从中提取衰减查找表的温度断点 `[298.15, 323.15]` `K`（默认）| 范围 [1, `inf`] 内的条目向量

模块从中提取衰减查找表的温度断点。这些温度完全独立于 **Main** 部分中的 **Temperature breakpoints, T** 参数。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (constant temperature dependent)`、`Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`。

### **Current breakpoints for cycling aging data, I** — 模块从中提取衰减查找表的电流断点 `[-.1, -.5, -5]` `A`（默认）| 负标量向量

*自 R2025a 起*

模块从中提取衰减查找表的电流断点。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature and current dependent)`。

### **Percentage change in open-circuit voltage, OCVChange(N)** — 经过 *N* 次循环后开路电压的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后开路电压的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则开路电压的值增加。如果为此参数指定负值，则开路电压的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`。

### **Percentage change in terminal resistance, R0Change(N)** — 经过 *N* 次循环后端子电阻的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后端子电阻的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则端子电阻的值增加。如果为此参数指定负值，则端子电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`。

### **Percentage change in cell capacity, CapacityChange(N)** — 经过 *N* 次循环后电池容量的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后电池容量的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则电池容量的值增加。如果为此参数指定负值，则电池容量的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`。

### **Percentage change in self-discharge resistance, SelfDischargeRChange(N)** — 经过 *N* 次循环后自放电电阻的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后自放电电阻的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则自放电电阻的值增加。如果为此参数指定负值，则自放电电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`，并将 **Self discharge** 设置为 `Enabled`。

### **Percentage change in first polarization resistance, R1Change(N)** — 经过 *N* 次循环后第一并联 RC 电阻的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后第一并联 RC 电阻的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第一并联 RC 电阻的值增加。如果为此参数指定负值，则第一并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`，并将 **Parallel resistor capacitor pairs** 设置为 `One time-constant dynamics`、`Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **Percentage change in second polarization resistance, R2Change(N)** — 经过 *N* 次循环后第二并联 RC 电阻的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后第二并联 RC 电阻的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第二并联 RC 电阻的值增加。如果为此参数指定负值，则第二并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`，并将 **Parallel resistor capacitor pairs** 设置为 `Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **Percentage change in third polarization resistance, R3Change(N)** — 经过 *N* 次循环后第三并联 RC 电阻的百分比变化 `[0, 0, 0, 0]`（默认）| 标量向量

电池经过 *N* 次放电循环后第三并联 RC 电阻的百分比变化。

此参数的大小必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第三并联 RC 电阻的值增加。如果为此参数指定负值，则第三并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature independent)`，并将 **Parallel resistor capacitor pairs** 设置为 `Three time-constant dynamics`。

### **Percentage change in open-circuit voltage, OCVChange(N,T)** — 在指定温度下经过 *N* 次循环后开路电压的百分比变化 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后开路电压的百分比变化。

此矩阵的行数必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **Temperatures breakpoints for cycling aging data, T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则开路电压的值增加。如果为此参数指定负值，则开路电压的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (constant temperature dependent)`。

### **Percentage change in terminal resistance, R0Change(N,T)** — 在指定温度下经过 *N* 次循环后端子电阻的百分比变化 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后端子电阻的百分比变化。

此矩阵的行数必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **Temperatures breakpoints for cycling aging data, T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则端子电阻的值增加。如果为此参数指定负值，则端子电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`。

### **Initial target for percentage change in internal resistance due to cycling aging** — 由于循环老化导致的内阻百分比变化的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

由于循环老化导致的内阻百分比变化的初始目标值。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`。

### **Percentage change in cell capacity, CapacityChange(N,T)** — 在指定温度下经过 *N* 次循环后电池容量的百分比变化 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后电池容量的百分比变化。

此矩阵的行数必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **Temperatures breakpoints for cycling aging data, T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则电池容量的值增加。如果为此参数指定负值，则电池容量的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`。

### **Initial target for percentage change in capacity due to cycling aging** — 由于循环老化导致的容量百分比变化的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

由于循环老化导致的容量百分比变化的初始目标值。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`。

### **Percentage change in self-discharge resistance, SelfDischargeRChange(N,T)** — 在指定温度下经过 *N* 次循环后自放电电阻的百分比变化 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后自放电电阻的百分比变化。

此矩阵的行数必须等于 **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **Temperatures breakpoints for cycling aging data, T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则自放电电阻的值增加。如果为此参数指定负值，则自放电电阻的值减小。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`。

### **Initial target for percentage change in self-discharge resistance due to cycling aging** — 由于循环老化导致的自放电电阻百分比变化的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

由于循环老化导致的自放电电阻百分比变化的初始目标值。

#### 依赖关系

要启用此参数，请将 **Cycling aging model** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`，并将 **Self discharge** 设置为 `Enabled`。

### **首次极化电阻变化百分比，R1Change(N,T)** — 在指定温度下经过 *N* 次循环后首次并联 RC 电阻的变化百分比 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后，首次并联 RC 电阻的变化百分比。

此矩阵的行数必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **循环老化数据的温度断点，T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则首次并联 RC 电阻的值增加。如果为此参数指定负值，则首次并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`，并将 **并联电阻电容对** 设置为 `One time-constant dynamics`、`Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **循环老化导致的首次极化电阻变化百分比初始目标值** — 循环老化导致的首次极化电阻变化百分比的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

循环老化导致的首次极化电阻变化百分比的初始目标值。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `One time-constant dynamics`、`Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **第二次极化电阻变化百分比，R2Change(N,T)** — 在指定温度下经过 *N* 次循环后第二次并联 RC 电阻的变化百分比 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后，第二次并联 RC 电阻的变化百分比。

此矩阵的行数必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **循环老化数据的温度断点，T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第二次并联 RC 电阻的值增加。如果为此参数指定负值，则第二次并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`，并将 **并联电阻电容对** 设置为 `Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **循环老化导致的第二次极化电阻变化百分比初始目标值** — 循环老化导致的第二次极化电阻变化百分比的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

循环老化导致的第二次极化电阻变化百分比的初始目标值。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **第三次极化电阻变化百分比，R3Change(N,T)** — 在指定温度下经过 *N* 次循环后第三次并联 RC 电阻的变化百分比 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池在指定温度下经过 *N* 次放电循环后，第三次并联 RC 电阻的变化百分比。

此矩阵的行数必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此矩阵的列数必须等于 **循环老化数据的温度断点，T** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第三次并联 RC 电阻的值增加。如果为此参数指定负值，则第三次并联 RC 电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (constant temperature dependent)` 或 `Lookup tables (temperature dependent)`，并将 **并联电阻电容对** 设置为 `Three time-constant dynamics`。

### **循环老化导致的第三次极化电阻变化百分比初始目标值** — 循环老化导致的第三次极化电阻变化百分比的初始目标值 `0`（默认）| 标量

*自 R2025a 起*

循环老化导致的第三次极化电阻变化百分比的初始目标值。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `Three time-constant dynamics`。

### **端子电阻变化百分比，R0Change(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后端子电阻的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，端子电阻的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则端子电阻的值增加。如果为此参数指定负值，则端子电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`。

### **电芯容量变化百分比，CapacityChange(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后电芯容量的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，电芯容量的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则电芯容量的值增加。如果为此参数指定负值，则电芯容量的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`。

### **自放电电阻变化百分比，SelfDischargeRChange(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后自放电电阻的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，自放电电阻的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则自放电电阻的值增加。如果为此参数指定负值，则自放电电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`，并将 **自放电** 设置为 `Enabled`。

### **首次极化电阻变化百分比，R1Change(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后首次极化电阻的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，首次极化电阻的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则首次极化电阻的值增加。如果为此参数指定负值，则首次极化电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `One time-constant dynamics`、`Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **第二次极化电阻变化百分比，R2Change(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后第二次极化电阻的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，第二次极化电阻的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第二次极化电阻的值增加。如果为此参数指定负值，则第二次极化电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `Two time-constant dynamics` 或 `Three time-constant dynamics`。

### **第三次极化电阻变化百分比，R2Change(N,T,I)** — 在指定温度和电流下经过 *N* 次循环后第三次极化电阻的变化百分比 `repmat(0, 4, 2, 3)`（默认）| 标量三维数组

*自 R2025a 起*

电池在指定温度和电流下经过 *N* 次放电循环后，第三次极化电阻的变化百分比。

此三维数组第一维的大小必须等于 **放电循环次数断点，NumDisCyclesBreakpoints** 参数的大小。此三维数组第二维的大小必须等于 **循环老化数据的温度断点，T** 参数的大小。此三维数组第三维的大小必须等于 **循环老化数据的电流断点，I** 参数的大小。

此参数接受百分比值。例如，如果电池容量在 100 次循环后下降 2%，在 200 次循环后下降 4%，在 300 次循环后下降 8%，则将相应的百分比变化参数设置为 `[0,-2,-4,-8]`。

**注意**

如果为此参数指定正值，则第三次极化电阻的值增加。如果为此参数指定负值，则第三次极化电阻的值减小。

#### 依赖关系

要启用此参数，请将 **循环老化模型** 设置为 `Lookup tables (temperature and current dependent)`，并将 **并联电阻电容对** 设置为 `Three time-constant dynamics`。

### 日历老化

### **电阻日历老化** — 启用电阻日历老化的选项 `Disabled`（默认）| `Enabled`

启用电池电阻日历老化的选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CalendarAgeResistance` |
| **值：** | `"simscape.battery.enum.cells.BatteryEnable.Disabled"`（默认）| `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **容量日历老化** — 启用容量日历老化的选项 `Disabled`（默认）| `Enabled`

启用电池容量日历老化的选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CalendarAgeCapacity` |
| **值：** | `"simscape.battery.enum.cells.BatteryEnable.Disabled"`（默认） | `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **建模选项** — 日历老化的建模选项 `Equation-based`（默认） | `Tabulated: temperature` | `Tabulated: time and temperature`

电阻和容量日历老化的建模选项。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 或 **容量日历老化** 设置为 `Enabled`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CalendarAgingMethod` |
| **值：** | `"simscape.battery.enum.cells.CalendarAgingMethod.equation"`（默认） | `"simscape.battery.enum.cells.CalendarAgingMethod.tableT"` | `"simscape.battery.enum.cells.CalendarAgingMethod.tableTandTime"` |

### **存储条件** — 存储条件 `Specify open-circuit voltage during storage`（默认） | `Specify state-of-charge during storage`

用于指定存储期间开路电压或 SOC 的选项。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Equation-based`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StorageVariable` |
| **值：** | `"simscape.battery.enum.cells.StorageVariable.OCV"`（默认） | `"simscape.battery.enum.cells.StorageVariable.SOC"` |

### **存储期间的归一化开路电压，V/Vnom** — 存储期间的归一化开路电压 `0.9`（默认） | 标量

存储期间的归一化开路电压。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Equation-based`，并将 **存储条件** 设置为 `Specify open-circuit voltage during storage`。

### **存储期间的荷电状态** — 存储期间的 SOC 百分比 `0.6`（默认） | 范围 [0, 1] 内的标量

存储期间的 SOC 百分比。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Equation-based`，并将 **存储条件** 设置为 `Specify state-of-charge during storage`。

### **时间间隔向量** — 时间间隔 `[0]` `d`（默认） | 标量向量

时间间隔。此参数的大小必须等于 **存储温度向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Equation-based`、`Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **存储温度向量** — 存储温度 `[273]` `K`（默认） | 非负值向量

存储温度。此参数的大小必须等于 **时间间隔向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Equation-based`、`Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **端子电阻随电压的线性缩放，b** — 端子电阻的电压线性缩放系数 `2.2134e6`（默认） | 标量

端子电阻相对于开路电压的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **端子电阻随电压的常数偏移，c** — 端子电阻的电压常数偏移 `1.632e6`（默认） | 标量

端子电阻相对于开路电压的常数偏移。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **端子电阻随温度的指数增长，d** — 端子电阻随温度的指数增长 `0.515833569` `V`（默认） | 标量

端子电阻随温度的指数增长。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **端子电阻的时间指数，a** — 端子电阻中的时间指数 `0.75`（默认） | 标量

端子电阻中的时间指数。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based` 或 `Tabulated: temperature`。

### **用于端子电阻日历老化的采样温度向量，T\_ar** — 用于端子电阻日历老化的采样温度 `[273.15, 298.15, 323.15]` `K`（默认） | 正值向量

用于端子电阻日历老化的采样温度。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **用于端子电阻日历老化的采样存储时间间隔向量，t\_ar** — 用于端子电阻日历老化的采样存储时间间隔 `[90, 180, 270, 360]` `d`（默认） | 正值向量

用于端子电阻日历老化的采样存储时间间隔。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: time and temperature`。

### **由于日历老化导致的端子电阻百分比变化，dR0(T\_ar)** — 由于日历老化导致的端子电阻百分比变化 `[0,0,0]`（默认） | 标量向量

由于日历老化导致的端子电阻百分比变化。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature`。

### **端子电阻寿命开始与 dR(T\_ar) 测量之间的时间** — 端子电阻寿命开始与 *dR(Tar)* 测量之间的时间 `100` `d`（默认） | 非负标量

电池端子电阻寿命开始与 *dR(Tar)* 测量之间的时间。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature`。

### **由于日历老化导致的端子电阻百分比变化，dR0(t\_ar,T\_ar)** — 由于日历老化导致的端子电阻百分比变化 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]`（默认） | 标量矩阵

由于日历老化导致的端子电阻百分比变化。

#### 依赖关系

要启用此参数，请将 **电阻日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: time and temperature`。

### **容量随电压的线性缩放，b** — 容量的电压线性缩放 `1.5097e07`（默认） | 标量

容量相对于开路电压的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **容量随电压的常数偏移，c** — 容量的电压常数偏移 `8.3625e06`（默认） | 标量

容量相对于开路电压的常数偏移。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **容量随温度的指数下降，d** — 容量随温度的指数下降 `0.6011` `V`（默认） | 标量

容量随温度的指数下降。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based`。

### **容量的时间指数，a** — 容量中的时间指数 `0.75`（默认） | 标量

容量中的时间指数。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Equation-based` 或 `Tabulated: temperature`。

### **用于容量日历老化的采样温度向量，T\_ac** — 用于容量日历老化的采样温度 `[273.15, 298.15, 323.15]` `K`（默认） | 正值向量

用于容量日历老化的采样温度。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **用于容量日历老化的采样存储时间间隔向量，t\_ac** — 用于容量日历老化的采样存储时间间隔 `[90, 180, 270, 360]` `d`（默认） | 正值向量

用于容量日历老化的采样存储时间间隔。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: time and temperature`。

### **由于日历老化导致的容量百分比变化，dAH(T\_ac)** — 由于日历老化导致的容量百分比变化 `[0, 0, 0]`（默认） | 标量向量

由于日历老化导致的容量百分比变化。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature`。

### **容量寿命开始与 dAH(T\_ac) 测量之间的时间** — 容量寿命开始与 *dAH(Tac)* 测量之间的时间 `100` `d`（默认） | 正标量

电池容量寿命开始与 *dAH(Tac)* 测量之间的时间。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: temperature`。

### **由于日历老化导致的容量百分比变化，dAH(t\_ac,T\_ac)** — 由于日历老化导致的容量百分比变化 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]`（默认） | 标量矩阵

由于日历老化导致的容量百分比变化。

#### 依赖关系

要启用此参数，请将 **容量日历老化** 设置为 `Enabled`，并将 **建模选项** 设置为 `Tabulated: time and temperature`。

### 热

### **仿真温度** — 电池温度 `298.15` `K`（默认） | 正标量

模块在整个仿真过程中用于查找表的电池温度。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Constant temperature`。

### **电池热质量** — 与热端口关联的电池热质量 `100` `J/K`（默认） | 正标量

与热端口 **H** 或 **HDist** 关联的电池热质量。此参数表示将热端口温度升高一开尔文所需的能量。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Lumped thermal mass` 或 `Height distributed thermal mass`。

### **热模型数量** — 热模型中离散化元素的数量 `6`（默认） | 正标量

*自 R2024b 起*

热模型中离散化元素的数量。此参数的值会影响端口 **HDist** 处热节点数组的大小。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Height distributed thermal mass`。

### **Z 方向热导率** — 电芯在 *Z* 方向的热导率 `18` `W/(K*m)`（默认） | 正标量

*自 R2024b 起*

电芯在 *Z* 方向的热导率。此参数会影响热节点数组 **HDist** 的节点之间的热交换。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Height distributed thermal mass`。

### **XY 方向横截面积** — 电芯在 *XY* 方向的横截面积 `3.5e-4` `m^2`（默认） | 正标量

*自 R2024b 起*

电芯在 *XY* 方向的横截面积。此参数会影响热节点数组 **HDist** 的节点之间的热交换。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Height distributed thermal mass`。

### **电芯高度** — 电芯高度 `0.07` `m`（默认） | 正标量

*自 R2024b 起*

电池电芯的高度。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Height distributed thermal mass`。

### **可逆热模型** — 用于对可逆热建模的选项 `Disabled`（默认） | `Entropic coefficient`

用于对电池中的可逆热或熵热建模的选项。熵变会引起电池内部的可逆热。可逆热可能产生加热或冷却效应。

模块使用以下方程计算可逆热的值

Qrev=I TdOCVdT，

其中 dOCVdT 是 **熵系数** 参数的值。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Lumped thermal mass` 或 `Height distributed thermal mass`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReversibleHeatModel` |
| **值：** | `"simscape.battery.enum.cells.ReversibleHeatModel.Disabled"`（默认） | `"simscape.battery.enum.cells.ReversibleHeatModel.EntropicCoefficient"` |

### **熵系数** — 可逆热的熵系数 `[0, 0, 0, 0, 0, 0, 0]` `mV/K`（默认） | 标量向量

可逆热模型的熵系数。此向量的大小必须等于 **荷电状态断点，SOC** 参数的大小。

#### 依赖关系

要启用此参数，请将 **可逆热模型** 设置为 `Entropic coefficient`。

### 故障

### **附加电阻故障** — 用于使串联电阻发生故障的选项 `Add fault`（默认）

用于使串联电阻发生故障的选项。如果附加电阻大于 1000 欧姆，可使用此故障对开路电芯建模，或对异常内阻建模。

要添加故障，请点击 **Add fault** 超链接。

### **放热反应故障** — 用于对自热和热失控事件建模的选项 `Add fault`（默认）

用于对可能导致热失控事件的放热反应建模的选项。

当电芯中发生放热反应时，可能发生热失控事件，释放大量热量并损坏电池。当电芯温度超过 **电流中断温度** 参数的值时，电池在电气上表现为开路。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **热模型** 设置为 `Lumped thermal mass`。

### **内部短路故障** — 用于使并联电阻发生故障的选项 `Add fault`（默认）

用于使并联电阻发生故障的选项。并联电阻的范围从无穷大值到您指定的值。

要添加故障，请点击 **Add fault** 超链接。

### **故障时的附加电阻** — 模块发生故障时的附加电阻 `1e5` `Ohm`（默认）

模块处于故障状态时附加电阻的值。

#### 依赖关系

要启用此参数，请点击 **附加电阻故障** 参数的 **Add fault** 超链接。

### **Trigger type** — 附加电阻故障的故障触发类型 `Always On`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

触发类型。选择以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Additional triggers` — 故障由模块对话框中不可用的附加触发器触发。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由反映信号相关行为的条件触发。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 附加电阻故障进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Trigger Configuration** — 为附加电阻故障启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。

### **Short parallel resistance when faulted** — 模块故障时的短路并联电阻 `1e-6`（默认）

模块处于故障状态时的短路并联电阻值。

#### 依赖关系

要启用此参数，请点击 **Internal short fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 内部短路故障的故障触发类型 `Always On`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

触发类型。选择以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Additional triggers` — 故障由模块对话框中不可用的附加触发器触发。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由反映信号相关行为的条件触发。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Internal short fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 内部短路故障进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Internal short fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Trigger Configuration** — 为内部短路故障启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Internal short fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。

### **Modeling fidelity** — 放热反应建模的保真度选项 `Analytical`（默认）| `Tabulated accelerated rate calorimetry test temperature rate`

放热反应建模的保真度选项。

#### 依赖关系

要启用此参数，请将 **Thermal model** 参数设置为 `Lumped thermal mass`，并点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ExothermModel` |
| **值**：| `"simscape.battery.enum.cells.ExothermModel.analytical"`（默认）| `"simscape.battery.enum.cells.ExothermModel.acceleratedRateCalorimetryTemperature"` |

### **Tabulate with state of charge** — 将放热反应参数制表为 SOC 函数的选项 `off`（默认）| `on`

将放热反应参数制表为电池 SOC 函数的选项。

#### 依赖关系

要启用此参数，请将 **Thermal model** 参数设置为 `Lumped thermal mass`，并点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TabulateWithSOC` |
| **值**：| `false`（默认）| `true` |

### **Current interruption temperature** — 电流停止流动的温度 `420` `K`（默认）| 正标量

由于热失控导致电池电气断开且电流停止流过电池的温度。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 清除 **Tabulate with state of charge** 参数。

### **Total heat of reaction** — 反应总热量 `23e3` `J`（默认）| 正标量

反应的总热量。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 清除 **Tabulate with state of charge** 参数。

### **Exotherm onset temperature** — 放热起始温度 `350` `K`（默认）| 正标量

加速量热法（ARC）测试中自加热速率超过每分钟 0.02 摄氏度阈值的温度，在该阈值下反应热速率缓慢升高电池温度。如果温度超过此值，反应变得自持并最终产生热失控。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 清除 **Tabulate with state of charge** 参数。

### **Exotherm onset temperature rate** — 放热起始温度速率 `0.02` `K/min`（默认）| 正标量

放热起始温度速率。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。

### **Activation energy** — 活化能 `160e3` `J/mol`（默认）| 正标量

活化能。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 清除 **Tabulate with state of charge** 参数。

### **Order of reaction** — 放热反应级数 `1`（默认）| 正标量

放热反应的级数。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 清除 **Tabulate with state of charge** 参数。

### **Percent of thermal mass vented** — 电池排放到环境的热质量百分比 `40`（默认）| 正标量

电池排放到环境的热质量百分比。随着反应推进，电池中的部分材料分解为气体。电池将这些气体排放到环境中。这些材料的损失降低了电池的热质量。要对这种热质量损失建模，热质量随反应程度线性减小。要控制热质量随反应程度减小的速率，请相应地指定 **Percent of thermal mass vented** 参数。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 清除 **Tabulate with state of charge** 参数。

### **Vector of state of charge values for exothermic parameters, SOC** — 放热参数查找数据的 SOC 值 `[0,.5,1]`（默认）| 非负值向量

指定放热参数查找数据时的 SOC 值。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding current interruption temperature, Tci(SOC)** — 指定 SOC 断点处对应的电流中断温度 `[420, 420, 420]`（默认）| 非负值向量

指定 SOC 断点处对应的电流中断温度。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding total heat of reaction, heat(SOC)** — 指定 SOC 断点处对应的反应总热量 `[23000, 23000, 23000]`（默认）| 非负值向量

指定 SOC 断点处对应的反应总热量。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding exotherm onset temperature, Tex(SOC)** — 指定 SOC 断点处对应的放热起始温度 `[350, 350, 350]`（默认）| 非负值向量

指定 SOC 断点处对应的放热起始温度。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding activation energy, Ea(SOC)** — 指定 SOC 断点处对应的活化能 `[160000, 160000, 160000]`（默认）| 非负值向量

指定 SOC 断点处对应的活化能。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding order of reaction, Or(SOC)** — 指定 SOC 断点处对应的反应级数 `[1, 1, 1]`（默认）| 非负值向量

指定 SOC 断点处对应的反应级数。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Analytical`。
- 选择 **Tabulate with state of charge** 参数。

### **Vector of ARC test temperatures, T** — 查找数据的 ARC 测试温度 `[323, 373, 423, 438, 463, 483, 513, 543, 545, 547, 549, 551, 553, 573, 623, 773, 923, 943, 1003, 1063, 1113, 1123, 1133, 1153, 1173]`（默认）| 非负值向量

指定查找数据时的 ARC 测试温度。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Tabulated accelerated rate calorimetry test temperature rate`。

### **Corresponding ARC test temperature rates, dT/dt(T)** — 指定 T 断点处对应的 ARC 测试温度速率 `[.0001, .001, .025, .2, .4, .6, 1.1, 1.3, 1.9, 3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017]`（默认）| 非负值向量

指定温度断点处对应的 ARC 测试温度速率。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Tabulated accelerated rate calorimetry test temperature rate`。
- 清除 **Tabulate with state of charge** 参数。

### **Corresponding ARC test temperature rates, dT/dt(T,SOC)** — 指定温度和 SOC 断点处对应的 ARC 测试温度速率 `repmat([.0001, .001, .025, .2, .4, .6, 1.1, 1.3, 1.9, 3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017]', 1, 3)`（默认）| 非负值矩阵

指定温度和 SOC 断点处对应的 ARC 测试温度速率。

#### 依赖关系

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Modeling fidelity** 设置为 `Tabulated accelerated rate calorimetry test temperature rate`。
- 选择 **Tabulate with state of charge** 参数。

### **Corresponding percent of thermal mass vented, Mvent(SOC)** — 在指定 SOC 断点处对应的排出热质量百分比 `[40, 40, 40]`（默认）| 范围 [0, 100] 内的值向量

在指定 SOC 断点处对应的排出热质量百分比。

#### 依赖

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 选择 **Tabulate with state of charge** 参数。

### **Trigger type** — 放热反应故障的故障触发类型 `Always On`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型。选择以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障因仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障因反映信号相关行为的条件而注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖

要启用此参数，请将 **Thermal model** 参数设置为 `Lumped thermal mass`，并点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 放热反应故障进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Timed`。

### **Trigger temperature** — 触发故障的温度 `350` `K`（默认）| 非负标量

触发温度。如果温度超过此值，模块进入故障状态。

#### 依赖

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger Configuration** — 为放热反应故障启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖

要启用此参数：

- 将 **Thermal model** 参数设置为 `Lumped thermal mass`。
- 点击 **Exothermic reactions fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Additional triggers`。

## 所属库

Simscape / Battery / Cells

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：生成数字数据手册

您现在可以使用 MATLAB 实时脚本为 Battery Equivalent Circuit 模块生成数字数据手册，包括充电、放电、循环寿命和搁置寿命特性。该脚本从您在模型中选择的 Battery Equivalent Circuit 模块导入参数。

### R2025a：根据 SOC、温度和电流参数化过电位参数

您现在可以使用取决于 SOC 和电流的二维查找表或取决于 SOC、温度和电流的三维查找表来参数化 Battery Equivalent Circuit 模块的过电位参数。您可以继续参数化现有的对 SOC、温度和电流方向的依赖关系。

要启用过电位参数的电流依赖性，请将新的 **Current dependence for resistance parameters** 参数设置为 `Lookup tables (current dependent)`。

由于此更改，**Current directionality for resistance parameters** 参数已被 **Current dependence for resistance parameters** 参数替换。有关此更改的兼容性注意事项的更多信息，请参阅 Battery Equivalent Circuit block supports current dependency for overpotential parameters。

### R2025a：支持使用标称容量计算放电循环次数

Battery Equivalent Circuit 模块现在支持使用标称容量计算循环老化的放电循环次数。将 **Cycle calculation method** 参数设置为：

- `Equivalent cycles` — 模块使用老化容量计算放电循环次数。
- `Equivalent full cycles` — 模块使用标称容量计算放电循环次数。

### R2025a：根据放电循环次数、温度和电流对循环老化数据建模

您现在可以通过指定以下参数，根据放电循环次数、温度和电流为 Battery Equivalent Circuit 模块的循环老化数据建模：

- **循环老化数据的电流断点，I**
- **Percentage change in terminal resistance, R0Change(N,T,I)**
- **Initial target for percentage change in internal resistance due to cycling aging**
- **Percentage change in cell capacity, CapacityChange(N,T,I)**
- **Initial target for percentage change in capacity due to cycling aging**
- **Percentage change in self-discharge resistance, SelfDischargeRChange(N,T,I)**
- **Initial target for percentage change in self-discharge resistance due to cycling aging**
- **Percentage change in first polarization resistance, R1Change(N,T,I)**
- **Initial target for percentage change in first polarization resistance due to cycling aging**
- **Percentage change in second polarization resistance, R2Change(N,T,I)**
- **Initial target for percentage change in second polarization resistance due to cycling aging**
- **Percentage change in third polarization resistance, R3Change(N,T,I)**
- **Initial target for percentage change in third polarization resistance due to cycling aging**

由于此更改：

- **Cycling aging model** 参数的 `Lookup tables (temperature dependent)` 值已重命名为 `Lookup tables (constant temperature dependent)`。仅当您在恒定温度值下仿真电池时，此选项才有效。
- **Cycling aging model** 参数现在包含另外两个值：

  - `Lookup tables (temperature dependent)` — 将参数百分比变化的表格数据设置为 *N* 和可变温度的函数。此表格数据必须相对于放电循环次数严格单调递增或递减。
  - `Lookup tables (temperature and current dependent)` — 将参数百分比变化的表格数据设置为 *N*、可变温度和可变电流的函数。此表格数据必须相对于放电循环次数严格单调递增或递减。

### R2024b：附加内置参数化

该模块现在支持以下附加内置参数化，代表特定供应商的组件：

- CSB Battery/EVX12300
- CSB Battery/EVX12340
- CSB Battery/EVX12520
- CSB Battery/GP12340
- CSB Battery/GP1245
- CSB Battery/GPL12260
- CSB Battery/GPL12520
- CSB Battery/GPL1272
- Exide/EP10012
- Exide/EP1212
- Exide/EP16012
- Exide/EP1712
- Exide/EP3212
- Exide/EP6512
- Exide/EP912
- Panasonic/BK\_10V1S
- Panasonic/BK\_110AAO
- Panasonic/BK\_130AA
- Panasonic/BK\_200A
- Panasonic/BK\_200AAB
- Panasonic/BK\_210A
- Panasonic/BK\_250A
- Panasonic/BK\_260SCP
- Panasonic/BK\_300SCP
- Panasonic/BK\_310CH
- Panasonic/BK\_380A
- Panasonic/BK\_450A
- Panasonic/BK\_60AAAH
- Panasonic/BK\_65AAAK
- Panasonic/BK\_70AAAJ
- Panasonic/BK\_70AAH
- Panasonic/BK\_80AAAB

### R2024b：将热模型沿电芯高度离散为多个单元

为提高热建模的保真度，您现在可以沿电芯高度离散该模块的热模型。要沿电芯高度离散热模型，请将 **Thermal model** 参数设置为 `Height distributed thermal mass`。然后，模块将暴露 **HDist** 热端口，该端口是一个热节点数组，表示沿电芯高度的节点。

## 描述

具有电热动力学和可选故障的电池模型

Battery Equivalent Circuit 模块通过使用具有可变特性的电路元件和零维集中质量热方程来对电池的电热动力学进行建模。您还可以使用此模块来仿真电池在短路、开路和热失控条件下的故障动力学。要对电池的循环老化和日历老化进行建模，您可以使用查找表或经验关系。该模块将电路元件的可变特性制成表格，作为电池荷电状态 (SOC) 以及可选的电流方向性、电流和温度的函数。该模块包含以下组成模型文件：

- 电气模型

  - 开路电压和迟滞模型
  - 瞬时过电位模型
  - 动态过电位模型
- 热模型

  - 恒定温度
  - 集中热质量模型
- 循环老化模型

  - 方程
  - 温度无关查找表
  - 温度相关查找表
- 日历老化模型

  - 电阻老化模型
  - 容量老化模型
- 故障模型

  - 短路模型
  - 开路模型
  - 放热反应模型

### Electrical Model

Battery Equivalent Circuit 模块通过使用按特定电路拓扑排列的电气电路元件组合来对电池端电压进行建模。下图展示了该等效电路拓扑，它依赖于可变电阻、可变电容和可变电压源。然而，Battery Equivalent Circuit 模块的实现完全采用 Simscape 语言。

所有电路元件都具有可变特性，这些特性是其他电池状态的函数：

- **OpenCircuitVoltage** — 模块将该电路元件制表为 SOC 的函数。

  - 如果将 **Thermal model** 参数设置为 `Constant
    temperature`、`Lumped thermal
    mass` 或 `Height distributed
    thermal mass`，则该电路元件还依赖于二维查表温度。
  - 如果将 **Hysteresis model** 参数设置为 `One-state model`，则电压源值是电池先前充电或放电历史的函数。
- **R0, R1, R2, R3, Tau1, Tau2, Tau3** — 模块将该电路元件制表为 SOC 的函数。

  - 如果将 **Thermal model** 参数设置为 `Constant
    temperature`、`Lumped thermal
    mass` 或 `Height distributed
    thermal mass`，则该电路元件还依赖于二维查表温度。
  - 如果将 **Current dependence for resistance
    parameters** 参数设置为 `Lookup
    tables (current directionality dependent)`，则电阻和电容值还是瞬时电流充电或放电方向的函数。因此，如果可用，您可以使用充电和放电参数表。如果流过电池的电流为正，则模块使用充电查表参数。如果流过电池的电流为负，则模块使用放电查表参数。
  - 如果将 **Current dependence for resistance
    parameters** 参数设置为 `Lookup
    tables (current dependent)`，则电阻和电容值还是电流的函数。因此，如果可用，您可以使用电流参数表。*（自 R2025a 起）*
- **SelfDischargeResistor** — 如果将 **Thermal model** 参数设置为 `Constant temperature`、`Lumped
  thermal mass` 或 `Height distributed
  thermal mass`，则该电路元件还依赖于二维查表温度。

**注意**

对于所有基于表的参数，Battery Equivalent Circuit 模块仅支持线性插值。对于外插，请将 **Extrapolation method for all tables** 参数设置为 `Nearest`、`Linear` 或 `Error`。

对于行和列，外插遵循先行后列的约定，即先索引行再索引列。

**Terminal Voltage**

Battery Equivalent Circuit 通过求解基尔霍夫电压定律，在每个时间步计算电池的端电压

U = OCVhyst + ηinst + ηdyn，

其中：

- *U* 是电池端电压。
- OCVhyst = OCV(SOC,T)+Uhyst(SOC,T) 是经滞回修正的开路电压。软件在仿真期间每个时间步更新电池荷电状态 *SOC*、温度 *T* 以及依赖于它们的相应变量。

  - *OCV(SOC,T)* 是开路电压。
  - *U*hyst*(SOC,T)* 是滞回电压。
- ηinst=​ I R0(SOC,T,CurDir) 是瞬时过电位。软件在仿真期间每个时间步更新电池 SOC、温度、电流方向性 *CurDir* 以及依赖于它们的相应变量。

  - *I* 是电池电流。如果 *I* 的值为正，则模块使用充电查表参数。如果 *I* 的值为负，则模块使用放电查表参数。
- ηdyn = ∑i=13ΔURCi(SOC,T,CurDir) 是动态过电位。该可选项取决于并联电阻-电容对的数量。该数量可在 1 到 3 之间变化。软件在仿真期间每个时间步更新电池 SOC、温度和电流方向性，以及依赖于它们的相应变量。

  - *ΔU*RC*i* 是并联电阻-电容对 *i* 的电压降。模块使用以下常微分方程计算该电压降：

    (τi(SOC,T,CurDir)d ΔURCidt+ΔURCi)1Ri(SOC,T,CurDir)=I

对于 Battery Equivalent Circuit 模块，*I* 在放电期间为负号，在充电期间为正号。在放电期间，模块从开路电压值中减去电池过电位，从而降低电池端电压。在放电和充电情况下，过电位以热量形式耗散能量。下图展示了电池脉冲放电期间电池过电位的演变。来自电阻-电容对的动态过电位在脉冲期间缓慢增加，而瞬时过电位则在前几毫秒内增加。

**Dynamic Overpotential**

电池不会瞬时响应负载变化。它们需要一些时间才能达到稳态。这种随时间变化的特性是电池充电动态的结果。模块通过使用等效电路中的并联 RC 段来对充电动态进行建模。

要对电池充电动态进行建模，请将 **Parallel resistor
capacitor pairs** 参数设置为以下值之一：

- `No dynamics` — 等效电路不包含并联 RC 段。电池的端电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。

下图展示了仅具有两个时间常数动态且无自放电电阻的模块电路拓扑的电池等效电路。

在此图中：

- *R*1 和 *R*2 是并联 RC 电阻。如果按温度制表参数，请分别通过设置 **First
  polarization resistance, R1(SOC,T)** 和
  **Second polarization resistance, R2(SOC,T)**
  参数来指定这些值。否则，请分别通过设置 **First polarization resistance, R1(SOC)** 和
  **Second polarization resistance, R2(SOC)**
  参数来指定这些值。第一个 RC 对的电压降与电极界面处化学反应产生的活化过电位直接相关。该动态的时间常数 *τ*1 通常低于 *τ*2，这表明响应更快或动态更快。第二个 RC 对的电压降与浓差过电位相关，并且通常比活化过电位演变得更慢。
- *C*1 和 *C*2 是并联 RC 电容。每个并联段的时间常数 *τ* 通过关系 C=τ/R 将 *R* 和 *C* 值关联起来。如果按温度制表参数，请使用 **First time constant, tau1(SOC,T)** 和
  **Second time constant, tau2(SOC,T)**
  参数为每个段指定 *τ*；否则使用 **First time constant, tau1(SOC)** 和
  **Second time constant, tau2(SOC)**。
- *R*0 是瞬时电阻。如果按温度制表参数，请使用 **Instantaneous
  resistance, R0(SOC,T)** 参数指定该值；否则使用 **Instantaneous resistance,
  R0(SOC)**。

**注意**

充电动态参数也可以依赖于电流方向性和电流。如果将 **Current
dependence for resistance parameters** 设置为 `Lookup
tables (current directionality dependent` 或
`Lookup tables (current dependent)`，则 **Overpotential** 部分中的参数会相应变化。

**State of Charge**

Battery Equivalent Circuit 模块使用库仑计数法计算电池的 SOC：

SOC=1Cageddchargedt，

其中：

- *C*aged 是电芯的老化容量。
- dchargedt=I−ID,SD(T)

  - *I*D,SD 是自放电电流消耗。该方程给出了来自自放电电阻的电流消耗，您可以将其制表为温度 *T* 的函数：

    ID,SD(T)=1RSD(T)OCVinternal。
  - *R*SD*(T)* 是自放电电阻。
  - *OCV*internal 是内部开路电压。

**Heat Generation Rate**

Battery Equivalent Circuit 模块通过将以下各项相加来计算电池产热速率：

- 等效电路拓扑中所有电阻的功率耗散项。该项也称为不可逆产热。该量包含欧姆过电位和活化过电位热项。
- 来自熵的可逆产热
- 来自故障电芯行为的产热项：

  - 短路电阻（或并联附加电阻）
  - 开路电阻（或串联附加电阻）
  - 热失控反应热

该方程展示了该求和：

Q˙gen=Pdiss+Q˙rev+Qflow,exr，

其中：

- Q˙gen 是产热速率。
- Pdiss=I2 R0(SOC,T,CurDir)+(∑i=13ΔURCi(SOC,T,CurDir))I+OCVinternal2RSD(T) +Qflow,series+Qflow,parallel 是耗散功率。

  - *Q*flow,series 是串联电阻热流。
  - *Q*flow,parallel 是并联电阻热流。
- Q˙rev=I T dOCVdt(SOC) 是可逆热。
- *Q*flow,exr 是放热反应热流。有关更多信息，请参阅 Model Faults。

**Hysteresis**

电池的滞回描述了开路电压 (OCV) 对充电或放电历史的依赖性。滞回仅间接依赖于 OCV。

在完整充电或放电循环期间测量 OCV 获得的数据称为*主回路*。如果电池仅部分充电或放电，则测得的 OCV 形成*次回路*。次回路在充电延迟后趋近主回路。该效应在锂离子电池中很显著，并且对 SOC 估计有重大影响。

Battery Equivalent Circuit 模块使用单状态模型对滞回进行建模

Uhyst=M H+sgn(I)M0

其中：

- *U*hyst 是滞回电压。
- *H* 定义滞回状态。模块使用以下常微分方程计算滞回状态：

  dHdt=γCaged[I−|I| H]
- *γ* 是滞回速率。
- *C*aged 是电芯的老化容量。
- *M* 是 **Maximum dynamic
  hysteresis voltage,
  MaximumHysteresisVoltageThermal(SOC,T)** 参数的值（如果按温度制表参数），否则是 **Maximum
  dynamic hysteresis voltage,
  MaximumHysteresisVoltage(SOC)** 的值。
- *M*0 是 **Instantaneous hysteresis voltage,
  InstantaneousHysteresisVoltageThermal(SOC,T)**
  参数的值（如果按温度制表参数），否则是 **Instantaneous hysteresis voltage,
  InstantaneousHysteresisVoltage(SOC)** 的值。

有关滞回以及如何对其建模的更多信息，请参阅 Model Voltage Hysteresis in Battery 示例。

**Self-Discharge**

当电池端子开路时，内部电流仍可能使电池放电。这种行为称为自放电。要启用并对此效应进行建模，请将 **Self discharge** 参数设置为 `Enabled`。

模块使用跨基本电池模型端子的温度相关电阻 *R*SD*(T)* 来对这些内部电流进行建模。如果按温度制表参数，请使用 **Self-discharge resistance,
SelfDischargeR(T)** 参数指定该电阻的查表值；否则使用 **Self-discharge resistance, SelfDischargeR**。

### Thermal Model

将 **Thermal model** 参数设置为 `Lumped
thermal mass` 会向 Battery
Equivalent Circuit 模块添加热模型。该模型在每个时间步计算电池温度。模块将该温度用于所有温度相关查表。集总热质量添加以下常微分方程：

Mthd Tdt=Q˙gen−Q˙diss，

其中：

- *M*th 是电池热质量。
- Q˙gen=Pdiss+Q˙rev+Q˙flow,exr。
- Q˙diss 是跨 **H** 热端口的热量。

为了提高热建模的保真度并对模块内部的温度梯度进行建模，您可以沿电芯高度对热模型进行离散化。要对热模型进行高度离散化，请将 **Thermal model** 参数设置为 `Height distributed
thermal mass`。然后模块会暴露 **HDist** 热端口，该端口是一个热节点数组，表示沿电芯高度的节点。为了计算电芯的电气行为，模块使用离散化热节点的平均值。*（自 R2024b 起）*

### Cycling Aging Model

电池老化是指电池在反复充放电循环过程中性能的退化。

通过将 **Cycling aging model** 参数设置为以下选项之一，此模块允许您对电池老化进行建模：

- `Disabled` — 不对衰减特性进行建模。
- `Equations` — 电池容量和端电阻与 N 成正比。开路电压与 *N* 成正比。如果您启用自放电电阻或任何时间常数，其值将与 N 成正比。
- `Lookup tables (temperature independent)` — 基础参数百分比变化的查找表，作为放电循环次数 *N* 的函数。
- `Lookup tables (constant temperature dependent)` — 基础参数百分比变化的查找表，作为放电循环次数和当前电池温度的函数。仅当您的电池在接近恒定的温度下运行时，才使用此选项。对于温度变化的电池，请使用 `Lookup tables (temperature dependent)` 或 `Lookup tables (temperature and current dependent)`。
- `Lookup tables (temperature dependent)` — 基础参数百分比变化的查找表，作为放电循环次数和当前电池温度的函数。由于模块在下一个时间步内部计算基础参数值的方式，此表格数据必须相对于放电循环次数严格单调递增或递减。如果您的电池在变化的温度下运行，请使用此选项。对于接近恒定温度的电池，请使用 `Lookup tables (constant temperature dependent)` 以获得更好的仿真性能。*（自 R2025a 起）*
- `Lookup tables (temperature and current dependent)` — 基础参数百分比变化的查找表，作为放电循环次数、当前电池温度和当前电池单体电流的函数。由于模块在下一个时间步内部计算基础参数值的方式，此表格数据必须相对于放电循环次数严格单调递增或递减。如果您的电池在变化的温度下运行，请使用此选项。*（自 R2025a 起）*

当您将 **Cycling aging model** 参数设置为 `Equations` 时，基础电池模型的开路电压随放电循环次数 *n* 成比例衰减：

OCVfaded=OCV(1+δOCV(N,T)100nN)，

其中 *δOCV(N,T)* 是 *N* 次放电循环后开路电压的百分比变化。使用 **Change in open-circuit voltage after NumDisCycles discharge cycles (%)** 参数指定 *δOCV(N,T)*。

**注意**

Battery Equivalent Circuit 模块跟踪电流并对其随时间进行积分。放电循环次数 *n* 取决于 **Cycle calculation method** 参数的值：

- `Equivalent cycles` — 模块使用老化后的容量来计算放电循环次数。
- `Equivalent full cycles` — 模块使用 **Battery capacity** 参数的值来计算放电循环次数

模块据此计算 SOC 的标称电荷随放电循环次数的平方根衰减：

Cfaded=C(1+δC(N,T)100nN)，

其中 *C* 是初始容量，*δC(N,T)* 是 *N* 次放电循环后容量的百分比变化。使用 **Change in capacity after NumDisCycles discharge cycles (%)** 参数指定 *δC(N,T)*。

电池模型中的所有电阻也随放电循环次数的平方根衰减：

Ri,faded=Ri(1+δRi(N,T)100nN)，

其中 *δRi(N,T)* 是 *N* 次放电循环后第 *i* 个电阻的百分比变化。使用 **Change in resistance after NumDisCycles discharge cycles (%)** 参数指定 *δRi(N,T)*。

根据您配置模块的方式，电阻包括以下值：

- 瞬时电阻 — 使用 **Change in instantaneous resistance after NumDisCycles discharge cycles (%)** 参数指定 *NumDisCycles* 次循环内的百分比变化。
- 自放电电阻 — 使用 **Change in self-discharge resistance after NumDisCycles discharge cycles (%)** 参数指定 *NumDisCycles* 次循环内的百分比变化。
- 第一充电动态电阻 — 使用 **Change in first polarization resistance after NumDisCycles discharge cycles (%)** 参数指定 *NumDisCycles* 次循环内的百分比变化。
- 第二充电动态电阻 — 使用 **Change in second polarization resistance after NumDisCycles discharge cycles (%)** 参数指定 *NumDisCycles* 次循环内的百分比变化。
- 第三充电动态电阻 — 使用 **Change in third polarization resistance after NumDisCycles discharge cycles (%)** 参数指定 *NumDisCycles* 次循环内的百分比变化。

**注意**

您还可以使用温度相关、温度无关或温度与电流相关的查找表来对电池循环老化特性进行建模。选择其中任一选项将相应地更改模块参数。

### Calendar Aging Model

您可以对电池未使用时发生的电池性能退化进行建模。日历老化影响内阻和容量。特别是，电阻增加因诸如阳极和阴极处固体电解质界面（SEI）的形成以及集流体腐蚀等机制而异。这些过程主要取决于存储温度、存储 SOC 和存储时间。

要在 Battery Equivalent Circuit 模块中对日历老化进行建模，请将 **Resistance calendar aging** 或 **Capacity calendar aging** 参数之一设置为 `Enabled`，然后将 **Modeling option** 参数设置为以下值之一：

- `Equation-based`
- `Tabulated: temperature`
- `Tabulated: time and temperature`

**注意**

Battery Equivalent Circuit 模块仅在初始化期间应用日历老化。当您将 **Resistance calendar aging** 或 **Capacity calendar aging** 参数设置为 `Enabled` 时，模块会显示 **Vector of time intervals** 参数，该参数表示电池在仿真开始之前老化的时间。此选项不包括仿真期间的日历老化。

**Equation-based**

以下方程定义了由于日历老化导致的电池端电阻增加：

αR(T,Voc)=(bR Voc−cR)e−q dRk TRcalendar-aged=R0(1+∑i=1i=nαR(Ti,Voc)(tiaR−ti−1aR))

其中：

- *V*oc 是 **Normalized open-circuit voltage during storage, V/Vnom** 参数。
- *R*0 是 **Internal resistance** 参数。
- *ti* 是从 **Vector of time intervals** 参数导出的时间采样。
- *Ti* 是从 **Temperature breakpoints, T** 参数导出的。
- *b*R 是 **Terminal resistance linear scaling for voltage, b** 参数。
- *c*R 是 **Terminal resistance constant offset for voltage, c** 参数。
- *d*R 是 **Terminal resistance temperature-dependent exponential increase, d** 参数。
- *a*R 是 **Terminal resistance time exponent, a** 参数。
- *q* 是电子元电荷，单位为 C。
- *k* 是玻尔兹曼常数，单位为 J/K。

以下方程定义了由于日历老化导致的电池容量减少：

αC(T,Voc)=(bC Voc−cC)e−q dCk TCcalendar-aged=C(1+∑i=1i=nαC(Ti,Voc)(tiaC−ti−1aC))

其中：

- *C* 是初始容量。
- *b*C 是 **Capacity linear scaling for voltage, b** 参数。
- *c*C 是 **Capacity constant offset for voltage, c** 参数。
- *d*C 是 **Capacity temperature-dependent exponential increase, d** 参数。
- *a*C 是 **Capacity time constant, a** 参数。

如果您将 **Storage condition** 参数设置为 `Specify state-of-charge during storage`，模块将使用针对 SOC 和存储温度制表的电压 **V0** 将存储期间的 SOC 转换为归一化开路电压。

**Tabulated: Temperature**

老化后的端电阻是端电阻 *R*0*(SOC,T)*、电阻增加百分比 *dR*0 以及描述日历老化时间依赖性的幂律的乘积：

R0(SOC,T;tst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Tst,i)100(tast,i−tast,i−1tast,m))，

其中：

- *T* 是电池温度。如果您对参数按温度制表，请使用 **Temperature breakpoints, T** 参数指定 *T* 断点。
- *T*st 是 **Vector of storage temperatures** 参数。
- *t*st,*i* 和 *t*st,*i*-1 是从 **Vector of time intervals** 参数导出的时间采样。
- *t*0 为 0。
- *t*st,m 是软件测量电阻增加 *dR*0 的时刻。

相同的方程适用于老化电池容量的计算。

**Tabulated: Time and Temperature**

老化后的端电阻是端电阻 *R*0*(SOC,T)* 和 *dR*0 的乘积：

R0(SOC,T;Δtst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Δtst,i,Tst,i)100)。

相同的方程适用于老化电池容量的计算。

### Model Faults

要在 Battery Equivalent Circuit 模块中对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

Battery Equivalent Circuit 模块支持三种不同类型的故障：

- 附加电阻故障 — 串联连接电阻的阻值范围从 0 欧姆到您指定的值。当附加串联电阻较高（大于 1000 欧姆）时，您可以使用此故障对开路电池单体进行建模，或对异常内阻进行建模。
- 内部短路故障 — 并联连接电阻的阻值范围从无穷大到您指定的值。
- 放热反应 — 使用此故障模拟热失控事件。放热化学反应发生在电池单体级别。在低温下，反应速率较低，自加热速率不显著。在较高温度下，放热反应速率呈指数增长。电池产生的热量超过其可耗散的热量。温度开始呈指数上升，达到热失控事件，电池单体开始燃烧。在燃烧期间，电池单体的电气行为等效于开路。

  释放的热速率是反应程度和电池单体温度的函数：

  Qreaction(ξ,T)=Kscale(1−ξ)ρ e−EaRT，

  其中：

  - *K*scale 是一个常数，用于缩放方程以定义反应推进的速度。
  - *ξ* 是反应程度。如果反应程度为 0，则反应尚未开始。如果反应程度为 1，则反应已消耗所有可能的反应物并完成。
  - *ρ* 是 **Order of reaction** 参数的值，定义了反应速率相对于反应程度的多项式依赖性。
  - e−EaRT 是 Arrhenius 方程，定义了温度依赖性。*Ea* 是活化能，单位为 kJ/mol，*R* 等于 8.314 J/k/mol。

  模块使用 **Exotherm onset temperature** 参数计算 *K*scale。放热起始温度是加速量热法（ARC）测试中自加热速率超过 0.02 摄氏度/分钟阈值的温度，此时反应热速率缓慢升高电池单体温度。如果温度超过此值，反应变得自持并最终产生热失控事件。

  在 ARC 测试中，放热起始时释放的热速率等于：

  Qreaction(ξ=0,  T=TEO)=Mth,cell dTdtEO=Kscale e−EaRTEO

  其中：

  - *T*EO 是开尔文为单位的放热起始温度。
  - *M*th,cell 是电池单体的热质量。
  - *dTdt*EO 是电池单体处于放热起始温度时电池单体温度的变化率。典型值为 0.02 摄氏度/分钟。

  然后您可以将 *K*scale 计算为 *dTdt*EO、*T*EO、电池单体的热质量和活化能的函数：

  Kscale=Mth,cell∗dTdtEOe−EaRTEO。

  随着反应推进，电池中的一些材料分解为气体。这些气体消散到环境中。这些材料的损失降低了电池的热质量。为了对这种热质量损失进行建模，热质量随反应程度线性降低。要控制热质量随反应程度降低的速率，请相应地指定 **Percent of thermal mass vented** 参数。

**Fault Triggers**

您可以使用 **Trigger Type** 参数指定故障发生的方式和时间。

如果您将 **Trigger Type** 参数设置为 `Timed`，Battery Equivalent Circuit 模块将在仿真时间达到您为 **Trigger fault at time** 参数指定的值时触发故障事件。

对于放热反应故障，如果您将 **Trigger Type** 设置为 `Behavioral`，Battery Equivalent Circuit 模块将在温度超过 **Trigger temperature** 参数的值时触发故障事件。

如果您将 **Trigger Type** 设置为 `Conditional`，您可以选择 Battery Equivalent Circuit 模块中的故障是否可逆 *（自 R2025a 起）*。要对不可逆故障进行建模，请单击 **Open fault properties** 打开 Property Inspector，然后选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的其余时间内保持故障状态。要对可逆故障进行建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

**注意**

放热反应故障和内部短路故障不支持可逆故障。

有关向模块添加故障和指定故障触发器的详细信息，请参阅 Introduction to Simscape Faults。

### 预定义参数化

您可以使用代表特定供应商组件的内置参数化来参数化 Battery Equivalent Circuit 模块。

这些参数化对电池的稳态电气参数进行建模。软件根据制造商数据表中的特性曲线，对 **Open-circuit voltage (SOC)**、**Instantaneous resistance, R0(SOC, T)**、**Battery capacity**、**Percentage change in cell capacity, CapacityChange(N)** 和 **Percentage change in open-circuit voltage, OCVChangeVec(N)** 参数进行参数化。软件不会对串联电阻随电池循环寿命的变化以及动态 RC 网络参数进行参数化。相反，软件将 RC 网络电阻的净电阻加到特定参数化数据的串联电阻上。要填充 RC 参数数据，请从串联电阻数据中减去 RC 网络净电阻。软件通过假设电池比热为 900 J/kg K 来估算电池热质量。然后，热质量等于 900 乘以制造商数据表中的电池重量。

可用数据对应于不同温度下、直至数据表中最低端电压的 1 C 放电电流。软件会外推低于最低端电压的数据。**Open-circuit voltage, OCV(SOC)** 参数与温度无关。在较低温度下、低 SOC 区域中，端电阻为常数，并等于最低端电压处的电阻值。在这种情况下，电池通常会经历更高的热损耗。

要加载预定义参数化，请双击 Battery Equivalent Circuit 模块，点击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。对于缺失数据，使用工程判断和简化假设进行填补。因此，预计仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components (Simscape Electrical)。

### 生成数字数据表

*自 R2025a 起*

使用 MATLAB® 实时脚本为 Battery Equivalent Circuit 模块生成数字数据表，包括充电、放电、循环寿命、搁置寿命和迟滞特性。该脚本从您在模型中选择的 Battery Equivalent Circuit 模块导入参数。要打开 MATLAB 实时脚本：

1. 双击该模块以打开 **Block Parameters** 窗口。
2. 打开 **Description** 选项卡。
3. 点击 `Generate datasheet` 超链接。

要生成数据表，请在实时脚本中点击 `Generate Datasheet` 按钮。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。

### 公共变量（使用 Probe 模块可见）

Battery Equivalent Circuit 模块包含以下可使用 Probe 模块探测的公共变量：

- `batteryCurrent` — 通过电池端子测得的总电流。默认情况下，该变量的单位为 Amperes。
- `batteryTemperature` — 模块用于电阻和开路电压查表的电池平均温度。如果将 **Thermal model** 参数设置为 `Constant temperature`，则 `batteryTemperature` 变量等于指定的温度值。如果将 **Thermal model** 参数设置为 `Lumped thermal mass`，则 `batteryTemperature` 变量是一个在仿真期间变化的微分状态。
- `batteryVoltage` — 电池端电压，即正极端子与负极端子之间的电压差。默认情况下，该变量的单位为 Volts。
- `capacityCyclingChange` — 在指定放电循环后电池容量的百分比变化。默认情况下，该变量无单位。
- `charge` — 从电池中取出的或添加到电池中的电荷。默认情况下，该变量的单位为 A\*h。
- `heatGenerationRate` — 电池总发热率。如果您启用了放热故障，则该模块通过将所有电阻损耗、可逆发热贡献以及放热反应热相加来计算发热率。默认情况下，该变量的单位为 Watts。
- `hysteresisState` — 范围在 [-1,1] 内的迟滞状态。值 1 表示该模块在该时间步使用充电开路电压曲线。值 -1 表示该模块在该时间步使用放电开路电压曲线。默认情况下，该变量无单位。
- `isCurrentInterruptionTempExceeded` — 布尔值，指示电池在热失控事件期间是否已超过其电流中断温度。该变量仅在建模故障时相关。
- `isExothermFaulted` — 布尔值，指示电池模型是否已转变为热失控或放热模式。该模式可由高温触发，或根据故障模型规范按时间触发。该变量仅在建模故障时相关。
- `numCycles` — 电池的等效放电循环数。计数器从零开始，每当从电池中取出等效放电荷时增加一。默认情况下，该变量无单位。
- `ocv` — 根据温度、老化和荷电状态调整后的电池开路电压。默认情况下，该变量的单位为 Volts。
- `power_dissipated` — 电阻发热率或耗散功率。默认情况下，该变量的单位为 Watts。
- `r0CyclingChange` — 在指定放电循环后电池瞬时电阻的百分比变化。默认情况下，该变量无单位。
- `r1CyclingChange` — 在指定放电循环后电池第一极化电阻的百分比变化。默认情况下，该变量无单位。
- `r2CyclingChange` — 在指定放电循环后电池第二极化电阻的百分比变化。默认情况下，该变量无单位。
- `r3CyclingChange` — 在指定放电循环后电池第三极化电阻的百分比变化。默认情况下，该变量无单位。
- `reactionExtent` — 范围在 [0,1] 内的放热反应进程。初始时，该变量的值为 0。该变量仅在建模故障时相关。
- `reactionHeatRate` — 如果您启用了放热故障，则为放热反应热。默认情况下，该变量的单位为 Watts。
- `reversibleHeat` — 来自熵变化的可逆发热贡献。默认情况下，该变量的单位为 Watts。
- `selfDischargeRCyclingChange` — 在指定放电循环后电池自放电电阻的百分比变化。默认情况下，该变量无单位。
- `stateOfCharge` — 通过库仑计数获得的电池荷电状态。默认情况下，该变量无单位。
- `voltageDropRC1` — 等效电路模型第一 RC 支路引起的电压降。默认情况下，该变量的单位为 Volts。
- `voltageDropRC2` — 等效电路模型第二 RC 支路引起的电压降。默认情况下，该变量的单位为 Volts。
- `voltageDropRC3` — 等效电路模型第三 RC 支路引起的电压降。默认情况下，该变量的单位为 Volts。
