---
type: simulink-block
title: 'Battery (Table-Based)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Electrochemical Cell Modeling'
documentation_page: 'batterytablebased'
documentation_source_path: 'ref/batterytablebased.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery (Table-Based)

## 端口

### 输出

### **SOC** — 电池荷电水平，C 物理信号

物理信号端口，输出内部荷电状态。使用此输出端口可根据荷电状态更改负载行为，而无需构建荷电状态估计器的复杂性。荷电状态是根据当前电荷与标称电池容量 *qnom(T,n)* 的比值估计的归一化值。该模块通过对电池端子输出电流进行积分来估计当前电池电荷。要将荷电状态转换为实际电荷，必须为每个温度使用正确的标称电池容量。

#### 依赖关系

要启用此端口，请在 **主要** 设置中，将 **公开 SOC 测量端口** 参数设置为 `Yes`。

### 守恒

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

表示电池热质量的热守恒端口。

#### 依赖关系

要启用此端口，请在 **热** 设置中，将 **热端口** 参数设置为 `Yes`。

## 参数

### **所选部件** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商提供的组件的选项。单击 **<click to select>** 超链接以打开 Block Parameterization Manager 窗口。有关 Block Parameterization Manager 的详细信息，请参阅 Load Predefined Parameterizations (Simscape Electrical)。

### 主要

### **荷电状态值向量, SOC** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认） | 范围 [0,1] 内的标量向量

用于定义指定查找数据点的荷电状态断点向量。此向量必须严格递增。荷电状态值相对于 **电芯容量, AH** 参数中指定的标称电池容量计算。`SOC` 是可用电池电荷 *qbattery* 与标称电池容量 *qnom(T,n)* 的比值。必须确保对于每个温度，`SOC = 1` 表示 **电芯容量, AH** 参数中指定的相应电池电荷容量，假设电池是新的，循环次数 *N* 等于 1，且 *δAH(n = 1, Tfade) = 0*。

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH

### **按温度将参数制成表格** — 选择是否按温度将电池参数制成表格 `Yes`（默认） | `No`

选择是否按温度将电池参数制成表格。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_dependence` |
| **取值：** | `"yes"`（默认） | `"no"` |

### **电流方向性** — 启用电流方向 `Disabled`（默认） | `Enabled`

是否启用电流方向性。如果将此参数设置为 `Enabled`，则端子电阻取决于电流方向。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_dir` |
| **取值：** | `"currentDirectionality"`（默认） | `"noCurrentDirectionality"` |

### **端子电压工作范围 [Min Max]** — 端子电压工作范围 `[0, inf]` `V`（默认） | 正数向量

端子电压的工作范围。此参数必须是大小为 `1`-by-`2` 的向量，用于定义端子电压的最小值和最大值。

### **温度向量, T** — *T* 断点 `[278, 293, 313]` `K`（默认） | 正数向量

用于定义指定查找数据点的温度断点向量。此向量必须严格递增且大于 `0` `K`。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `Yes` 时，此参数可见。

### **开路电压, V0(SOC,T)** — 带温度断点的 *V0* 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` `V`（默认） | 非负数矩阵

在指定 SOC 和温度断点处的基本电池模型开路电压查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `Yes` 时，此参数可见。

### **开路电压, V0(SOC)** — *V0* 查找表 `[3.5057, 3.566, 3.6337, 3.7127, 3.9259, 4.0777, 4.1928]` `V`（默认） | 非负数矩阵

在指定 SOC 处的基本电池模型开路电压查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `No` 时，此参数可见。

### **端子电阻, R0(SOC,T)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认） | 非负数矩阵

在指定 SOC 和温度断点处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `Yes` 且 **电流方向性** 参数设置为 `Disabled` 时，此参数可见。

### **放电期间的端子电阻, R0(SOC,T)** — 放电阶段带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认） | 非负数矩阵

放电阶段在指定 SOC 和温度断点处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `Yes` 且 **电流方向性** 参数设置为 `Enabled` 时，此参数可见。

### **充电期间的端子电阻, R0(SOC,T)** — 充电阶段带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm`（默认） | 非负数矩阵

充电阶段在指定 SOC 和温度断点处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `Yes` 且 **电流方向性** 参数设置为 `Enabled` 时，此参数可见。

### **端子电阻, R0(SOC)** — R0 查找表 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认） | 非负数矩阵

在指定 SOC 处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `No` 且 **电流方向性** 参数设置为 `Disabled` 时，此参数可见。

### **放电期间的端子电阻, R0(SOC)** — 放电阶段 R0 查找表 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认） | 非负数矩阵

放电阶段在指定 SOC 处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `No` 且 **电流方向性** 参数设置为 `Enabled` 时，此参数可见。

### **充电期间的端子电阻, R0(SOC)** — 充电阶段 R0 查找表 `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm`（默认） | 非负数矩阵

充电阶段在指定 SOC 处的电池串联电阻查找数据。

#### 依赖关系

仅当 **按温度将参数制成表格** 参数设置为 `No` 且 **电流方向性** 参数设置为 `Enabled` 时，此参数可见。

### **电芯容量, AH** — 完全充电时的电池容量 `27` `hr*A`（默认） | 非负标量

电池的电芯容量。该模块通过将累积电荷除以此值来计算荷电状态。该模块通过对电池电流进行积分来计算累积电荷。

### **自放电** — 选择是否对电池的自放电电阻建模 `Disabled`（默认） | `Enabled`

选择是否对电池的自放电电阻建模。该模块将此效应建模为基本电池模型端子两端的一个电阻。

随着温度升高，自放电电阻减小，导致自放电增加。如果电阻下降过快，可能会发生电池热失控和数值不稳定性。您可以通过进行以下任一更改来解决此不稳定性：

- 减小热阻
- 减小自放电电阻相对于温度的梯度
- 增大自放电电阻

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_leak` |
| **取值：** | `"disabled"`（默认） | `"enabled"` |

### **自放电电阻, Rleak(T)** — 表示温度断点处电池自放电的电阻 `[8000, 7000, 6000]` `Ohm`（默认） | 正数向量

在指定温度断点处的电池自放电电阻查找数据。此电阻作用在基本电池模型的端子两端。

#### 依赖关系

当 **自放电** 参数设置为 `Enabled` 且 **按温度将参数制成表格** 设置为 `Yes` 时启用。

### **自放电电阻, Rleak** — 表示电池自放电的电阻 `7e3` `Ohm`（默认） | 正标量

电池自放电电阻查找数据。此电阻作用在基本电池模型的端子两端。

#### 依赖关系

仅当 **自放电** 参数设置为 `Enabled` 且 **按温度将参数制成表格** 参数设置为 `No` 时，此参数可见。

### **所有表格的外插方法** — 表格的外插方法 `Nearest`（默认） | `Linear` | `Error`

所有基于表格的参数的外插方法：

- `Linear` — 通过在已知数据末端创建切线并将其延伸到该限制之外来估计数据集之外的值。
- `Nearest` — 在查询点处外插出的值为最接近样本网格点处的值。
- `Error` — 如果值超出已知数据集，则返回错误。如果选择此选项，模块不使用外插。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extrapolation_option` |
| **取值：** | `"nearest"`（默认） | `"linear"` | `"error"` |

### **公开 SOC 测量端口** — 表格的外插方法 `No`（默认） | `Yes`

是否公开荷电状态测量端口。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOC_port` |
| **取值：** | `"no"`（默认） | `"yes"` | `"error"` |

### 动态特性

### **电荷动态特性** — 电池电荷动态特性模型 `No dynamics`（默认） | `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics` | `Four time-constant dynamics` | `Five time-constant dynamics`

选择如何对电池电荷动态特性建模。此参数确定等效电路中的并联 RC 段数量：

- `No dynamics` — 等效电路不包含并联 RC 段。电池的端子电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。如果按温度将参数制成表格，则使用 **第一时间常数, tau1(SOC,T)** 参数指定时间常数；否则使用 **第一时间常数, tau1(SOC)**。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。如果按温度将参数制成表格，则使用 **第一时间常数, tau1(SOC,T)** 和 **第二时间常数, tau2(SOC,T)** 参数指定时间常数；否则使用 **第一时间常数, tau1(SOC)** 和 **第二时间常数, tau2(SOC)**。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。如果按温度将参数制成表格，则使用 **第一时间常数, tau1(SOC,T)**、**第二时间常数, tau2(SOC,T)** 和 **第三时间常数, tau3(SOC,T)** 参数指定时间常数；否则使用 **第一时间常数, tau1(SOC)**、**第二时间常数, tau2(SOC)** 和 **第三时间常数, tau3(SOC)**。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 段。如果按温度将参数制成表格，则使用 **第一时间常数, tau1(SOC,T)**、**第二时间常数, tau2(SOC,T)**、**第三时间常数, tau3(SOC,T)** 和 **第四时间常数, tau4(SOC,T)** 参数指定时间常数；否则使用 **第一时间常数, tau1(SOC)**、**第二时间常数, tau2(SOC)**、**第三时间常数, tau3(SOC)** 和 **第四时间常数, tau4(SOC)**。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 段。如果按温度将参数制成表格，则使用 **第一时间常数, tau1(SOC,T)**、**第二时间常数, tau2(SOC,T)**、**第三时间常数, tau3(SOC,T)**、**第四时间常数, tau4(SOC,T)** 和 **第五时间常数, tau5(SOC,T)** 参数指定时间常数；否则使用 **第一时间常数, tau1(SOC)**、**第二时间常数, tau2(SOC)**、**第三时间常数, tau3(SOC)**、**第四时间常数, tau4(SOC)** 和 **第五时间常数, tau5(SOC)**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_dyn` |
| **取值：** | `"off"`（默认） | `"rc1"` | `"rc2"` | `"rc3"` | `"rc4"` | `"rc5"` |

### **第一极化电阻, R1(SOC,T)** — 温度断点处的第一 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认） | 正数矩阵

在指定 SOC 和温度断点处的第一并联 RC 电阻查找数据。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态特性** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度将参数制成表格** 设置为 `Yes`。

### **第一极化电阻, R1(SOC)** — 第一 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认） | 正数矩阵

在指定 SOC 处的第一并联 RC 电阻查找数据。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态特性** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度将参数制成表格** 设置为 `No`。

### **第一时间常数, tau1(SOC,T)** — 温度断点处的第一 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第一并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第一时间常数, tau1(SOC)** — 第一 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| matrix of positive numbers

指定 SOC 处第一并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第二极化电阻, R2(SOC,T)** — 温度断点处的第二 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第二并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第二极化电阻, R2(SOC)** — 第二 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 处第二并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第二时间常数, tau2(SOC,T)** — 温度断点处的第二 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第二并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第二时间常数, tau2(SOC)** — 第二 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| matrix of positive numbers

指定 SOC 处第二并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第三极化电阻, R3(SOC,T)** — 温度断点处的第三 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第三并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第三极化电阻, R3(SOC)** — 第三 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 处第三并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第三时间常数, tau3(SOC,T)** — 温度断点处的第三 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第三并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第三时间常数, tau3(SOC)** — 第三 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| matrix of positive numbers

指定 SOC 处第三并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第四极化电阻, R4(SOC,T)** — 温度断点处的第四 RC 电阻 `[.014, .382, .407; .028, .006, .007; .014, .007, .006; .333, .956, .912]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第四并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第四极化电阻, R4(SOC)** — 第四 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 处第四并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第四时间常数, tau4(SOC,T)** — 温度断点处的第四 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第四并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第四时间常数, tau4(SOC)** — 第四 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| matrix of positive numbers

指定 SOC 处第四并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第五极化电阻, R5(SOC,T)** — 温度断点处的第五 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第五并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第五极化电阻, R5(SOC)** — 第五 RC 电阻 `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm`（默认）| matrix of positive numbers

指定 SOC 处第五并联 RC 电阻的查找数据。此参数主要影响 RC 部分的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### **第五时间常数, tau5(SOC,T)** — 温度断点处的第五 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s`（默认）| matrix of positive numbers

指定 SOC 和温度断点处第五并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `Yes`。

### **第五时间常数, tau5(SOC)** — 第五 RC 时间常数 `[36, 45, 105, 29, 77, 33, 39]` `s`（默认）| matrix of positive numbers

指定 SOC 处第五并联 RC 时间常数的查找数据。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Five time-constant dynamics`，并将 **按温度制表参数** 设置为 `No`。

### 衰减

### **衰减特性** — 选择如何定义衰减特性 `Disabled`（默认）| `Equations` | `Lookup tables (temperature independent)` | `Lookup tables (constant temperature dependent)`

选择如何定义衰减特性：

- `Disabled` — 模块不对衰减特性建模。
- `Equations` — 电池容量和端子电阻将与 N 成正比，而开路电压将与 *N* 成正比。如果启用了自放电电阻或任意数量的时间常数，则其值将与 N 成正比。
- `Lookup tables (temperature independent)` — 设置参数百分比变化作为 *N* 的函数的表格数据。
- `Lookup tables (constant temperature dependent)` — 设置参数百分比变化作为 *N* 和温度的函数的表格数据。仅当使用恒定温度值仿真电池时，此选项有效。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_fade` |
| **值：** | `"disabled"`（默认） | `"equations"` | `"tableN"` | `"tableNandT"` |

### **放电循环次数, N** — 用于百分比变化计算的参考循环次数 `100`（默认）| 从 `1` 到 `Inf` 的数字

发生指定百分比变化所经历的充放电循环次数。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后开路电压的变化 (%)** — 经过 *N* 次循环后开路电压的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后开路电压的百分比变化。

**注意**

如果为此参数指定正值，则开路电压值增加。如果为此参数指定负值，则开路电压值降低。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后端子电阻的变化 (%)** — 经过 *N* 次循环后串联电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后串联电阻的百分比变化。

**注意**

如果为此参数指定正值，则端子电阻值增加。如果为此参数指定负值，则端子电阻值降低。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后电池容量的变化 (%)** — 经过 *N* 次循环后电池容量的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后电池容量的百分比变化。

**注意**

如果为此参数指定正值，则电池容量值增加。如果为此参数指定负值，则电池容量值降低。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后自放电电阻的变化 (%)** — 经过 *N* 次循环后自放电电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后自放电电阻的百分比变化。

**注意**

如果为此参数指定正值，则自放电电阻值增加。如果为此参数指定负值，则自放电电阻值降低。

#### 依赖关系

要启用此参数，请将 **自放电** 设置为 `Enabled`，并将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后第一极化电阻的变化 (%)** — 经过 *N* 次循环后第一 RC 电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后第一 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第一 RC 电阻值增加。如果为此参数指定负值，则第一 RC 电阻值降低。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后第二极化电阻的变化 (%)** — 经过 *N* 次循环后第二 RC 电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后第二 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第二 RC 电阻值增加。如果为此参数指定负值，则第二 RC 电阻值降低。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后第三极化电阻的变化 (%)** — 经过 *N* 次循环后第三 RC 电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后第三 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第三 RC 电阻值增加。如果为此参数指定负值，则第三 RC 电阻值降低。

#### 依赖关系

要启用此参数，请将 **充电动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Equations`。

### **经过 N 次放电循环后第四极化电阻的变化 (%)** — 经过 *N* 次循环后第四 RC 电阻的百分比变化 `0`（默认）| scalar

经过 *N* 次放电循环后第四 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第四 RC 电阻值增加。如果为此参数指定负值，则第四 RC 电阻值降低。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Four time-constant dynamics`，或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Equations`。

### **N 次放电循环后第五极化电阻的变化 (%)** — 经过 *N* 次循环后第五 RC 电阻的百分比变化 `0`（默认） | 标量

经过 *N* 次放电循环后电池第五 RC 电阻的百分比变化。

**注意**

如果为此参数指定正值，则第五 RC 电阻的值会增加。如果为此参数指定负值，则第五 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Equations`。

### **放电循环值向量, N** — 用于百分比变化计算的参考向量或循环次数 `[0, 100, 200, 300]`（默认） | 从 `0` 到 `Inf` 的数

指定的百分比变化发生时所对应的充放电循环次数向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (temperature independent)` 或 `Lookup tables (constant temperature dependent)`。

### **衰减数据温度向量, Tfade** — 已提取衰减查找表时的温度向量 `[298.15, 323.15]` `K`（默认） | 从 `1` 到 `Inf` 的数

已提取衰减查找表时的温度向量。这些温度完全独立于 **Main** 选项卡中的 **温度向量, T** 参数。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **开路电压百分比变化, dV0(N)** — 经过 *N* 次循环后开路电压的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池开路电压的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则开路电压的值会增加。如果为此参数指定负值，则开路电压的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **端子电阻百分比变化, dR0(N)** — 经过 *N* 次循环后串联电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池串联电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则端子电阻的值会增加。如果为此参数指定负值，则端子电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **电芯容量百分比变化, dAH(N)** — 经过 *N* 次循环后电芯容量的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池电芯容量的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则电芯容量的值会增加。如果为此参数指定负值，则电芯容量的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **自放电电阻百分比变化, dRleak(N)** — 经过 *N* 次循环后自放电电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池自放电电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则自放电电阻的值会增加。如果为此参数指定负值，则自放电电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **自放电** 设置为 `Enabled`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **第一极化电阻百分比变化, dR1(N)** — 经过 *N* 次循环后第一 RC 电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池第一 RC 电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第一 RC 电阻的值会增加。如果为此参数指定负值，则第一 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **第二极化电阻百分比变化, dR2(N)** — 经过 *N* 次循环后第二 RC 电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池第二 RC 电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第二 RC 电阻的值会增加。如果为此参数指定负值，则第二 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **第三极化电阻百分比变化, dR3(N)** — 经过 *N* 次循环后第三 RC 电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池第三 RC 电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第三 RC 电阻的值会增加。如果为此参数指定负值，则第三 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **第四极化电阻百分比变化, dR4(N)** — 经过 *N* 次循环后第四 RC 电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池第四 RC 电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第四 RC 电阻的值会增加。如果为此参数指定负值，则第四 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Four time-constant dynamics`，或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **第五极化电阻百分比变化, dR5(N)** — 经过 *N* 次循环后第五 RC 电阻的百分比变化向量 `[0, 0, 0, 0]`（默认） | 标量向量

经过 *N* 次放电循环后电池第五 RC 电阻的百分比变化向量。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第五 RC 电阻的值会增加。如果为此参数指定负值，则第五 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (temperature independent)`。

### **开路电压百分比变化, dV0(N, Tfade)** — 经过 *N* 次循环后开路电压的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池开路电压的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则开路电压的值会增加。如果为此参数指定负值，则开路电压的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **端子电阻百分比变化, dR0(N, Tfade)** — 经过 *N* 次循环后串联电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池串联电阻的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则端子电阻的值会增加。如果为此参数指定负值，则端子电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **电芯容量百分比变化, dAH(N, Tfade)** — 经过 *N* 次循环后电芯容量的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池电芯容量的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则电芯容量的值会增加。如果为此参数指定负值，则电芯容量的值会减小。

#### 依赖关系

要启用此参数，请将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **自放电电阻百分比变化, dRleak(N, Tfade)** — 经过 *N* 次循环后自放电电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池自放电电阻的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则自放电电阻的值会增加。如果为此参数指定负值，则自放电电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **自放电** 设置为 `Enabled`，并将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **第一极化电阻百分比变化, dR1(N, Tfade)** — 经过 *N* 次循环后第一 RC 电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池第一 RC 电阻的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第一 RC 电阻的值会增加。如果为此参数指定负值，则第一 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **充电动态特性** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`，并将 **衰减特性** 设置为 `Lookup tables (constant temperature dependent)`。

### **第二极化电阻百分比变化, dR2(N, Tfade)** — 经过 *N* 次循环后第二 RC 电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认） | 标量矩阵

经过 *N* 次放电循环后电池第二 RC 电阻的百分比变化矩阵。

当放电循环次数为零时，模块支持为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外插选项，可能会出现意外行为。

**注意**

如果为此参数指定正值，则第二 RC 电阻的值会增加。如果为此参数指定负值，则第二 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two
time-constant dynamics`、`Three
time-constant dynamics`、`Four
time-constant dynamics` 或 `Five
time-constant dynamics`，并将 **Fade
characteristic** 设置为 `Lookup tables
(constant temperature dependent)`。

### **Percent change in third polarization resistance, dR3(N, Tfade)** — 经过 *N* 次循环后第三 RC 电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池经过 *N* 次放电循环后，第三 RC 电阻的百分比变化矩阵。

该模块支持在放电循环次数为零时为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外推选项，可能会发生意外行为。

**注意**

如果为此参数指定正值，则第三 RC 电阻的值会增加。如果为此参数指定负值，则第三 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three
time-constant dynamics`、`Four
time-constant dynamics` 或 `Five
time-constant dynamics`，并将 **Fade
characteristic** 设置为 `Lookup tables
(constant temperature dependent)`。

### **Percent change in fourth polarization resistance, dR4(N, Tfade)** — 经过 *N* 次循环后第四 RC 电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池经过 *N* 次放电循环后，第四 RC 电阻的百分比变化矩阵。

该模块支持在放电循环次数为零时为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外推选项，可能会发生意外行为。

**注意**

如果为此参数指定正值，则第四 RC 电阻的值会增加。如果为此参数指定负值，则第四 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four
time-constant dynamics` 或 `Five
time-constant dynamics`，并将 **Fade
characteristic** 设置为 `Lookup tables
(constant temperature dependent)`。

### **Percent change in fifth polarization resistance, dR5(N, Tfade)** — 经过 *N* 次循环后第五 RC 电阻的百分比变化矩阵 `[0, 0; 0, 0; 0, 0; 0, 0]`（默认）| 标量矩阵

电池经过 *N* 次放电循环后，第五 RC 电阻的百分比变化矩阵。

该模块支持在放电循环次数为零时为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外推选项，可能会发生意外行为。

**注意**

如果为此参数指定正值，则第五 RC 电阻的值会增加。如果为此参数指定负值，则第五 RC 电阻的值会减小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five
time-constant dynamics`，并将 **Fade
characteristic** 设置为 `Lookup tables
(constant temperature dependent)`。

### 日历老化

### **Internal resistance calendar aging** — 内阻的日历老化 `Disabled`（默认）| `Enabled`

是否启用电池内阻的日历老化。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_age_resistance` |
| **值：** | `"disabled"`（默认）| `"enabled"` |

### **Capacity calendar aging** — 容量的日历老化 `Disabled`（默认）| `Enabled`

是否启用电池容量的日历老化。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_age_capacity` |
| **值：** | `"disabled"`（默认）| `"enabled"` |

### **Modeling option** — 日历老化选项 `Equation-based`（默认）| `Tabulated: temperature` | `Tabulated: time and temperature`

内阻和容量日历老化的建模选项。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 或 **Capacity calendar aging** 设置为 `Enabled`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_age_modeling` |
| **值：** | `"equation"`（默认）| `"tableT"` | `"tableTandTime"` |

### **Vector of time intervals** — 时间间隔 `[0]` `d`（默认）| 标量向量

时间间隔。此参数的大小必须与 **Vector of storage temperatures** 相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Equation-based`、`Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **Vector of storage temperatures** — 存储温度 `[273]` `K`（默认）| 标量向量

存储温度集。此参数的大小必须与 **Vector of time intervals** 相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Equation-based`、`Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **Storage condition** — 存储条件 `Specify open-circuit voltage during storage`（默认）| `Specify state-of-charge during storage`

指定存储期间的开路电压还是荷电状态。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Equation-based`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `prm_age_OCV` |
| **值：** | `"OCV"`（默认）| `"SOC"` |

### **Normalized open-circuit voltage during storage, V/Vnom** — 存储期间的归一化开路电压 `0.9`（默认）| 标量

存储期间的归一化开路电压。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Equation-based`，并将 **Storage condition** 设置为 `Specify open-circuit voltage during storage`。

### **State of charge during storage** — 存储期间的荷电状态百分比 `60`（默认）| 正数

存储期间的荷电状态，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Equation-based`，并将 **Storage condition** 设置为 `Specify state-of-charge during storage`。

### **Terminal resistance linear scaling for voltage, b** — 端子电阻中电压的线性缩放 `2.2134e6`（默认）| 标量

开路电压在端子电阻中的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Terminal resistance constant offset for voltage, c** — 端子电阻中电压的恒定偏移 `1.632e6`（默认）| 标量

开路电压在端子电阻中的恒定偏移。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Terminal resistance temperature-dependent exponential increase, d** — 端子电阻中与温度相关的指数增长 `0.515833569` `V`（默认）| 标量

端子电阻中与温度相关的指数增长。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Terminal resistance time exponent, a** — 端子电阻中的时间指数 `0.75`（默认）| 标量

端子电阻中的时间指数。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based` 或 `Tabulated: temperature`。

### **Capacity linear scaling for voltage, b** — 容量中电压的线性缩放 `1.5097e07`（默认）| 标量

开路电压在容量中的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Capacity constant offset for voltage, c** — 容量中电压的恒定偏移 `8.3625e06`（默认）| 标量

开路电压在容量中的恒定偏移。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Capacity temperature-dependent exponential increase, d** — 容量中与温度相关的指数增长 `0.6011` `V`（默认）| 标量

容量中与温度相关的指数增长。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based`。

### **Capacity time exponent, a** — 容量中的时间指数 `0.75`（默认）| 标量

容量中的时间指数。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Equation-based` 或 `Tabulated: temperature`。

### **Vector of sampled temperatures for terminal resistance calendar aging, T\_ar** — 端子电阻日历老化的采样温度 `[273.15, 298.15, 323.15]` `K`（默认）| 标量向量

端子电阻日历老化的采样温度向量。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **Percentage change in terminal resistance due to calendar aging, dR0(T\_ar)** — 由日历老化引起的端子电阻百分比变化 `[0,0,0]`（默认）| 标量向量

由日历老化引起的端子电阻百分比变化。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature`。

### **Time between terminal resistance beginning of life and dR(T\_ar) measurement** — 端子电阻寿命开始与 dR(T\_ar) 测量之间的时间 `100` `d`（默认）| 标量

端子电阻寿命开始与 dR(T\_ar) 测量之间的时间。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature`。

### **Vector of sampled temperatures for capacity calendar aging, T\_ac** — 容量日历老化的采样温度 `[273.15, 298.15, 323.15]` `K`（默认）| 标量向量

容量日历老化的采样温度向量。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature` 或 `Tabulated: time and temperature`。

### **Percentage change in capacity due to calendar aging, dAH(T\_ac)** — 由日历老化引起的容量百分比变化 `[0,0,0]`（默认）| 标量向量

由日历老化引起的容量百分比变化。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature`。

### **Time between capacity beginning of life and dAH(T\_ac) measurement** — 容量寿命开始与 dAH(T\_ac) 测量之间的时间 `100` `d`（默认）| 标量

容量寿命开始与 dR(T\_ac) 测量之间的时间。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: temperature`。

### **Vector of sampled storage time intervals for terminal resistance calendar aging, t\_ar** — 端子电阻日历老化的采样存储时间间隔 `[0, 90, 180, 270, 360]` `d`（默认）| 标量向量

端子电阻日历老化的采样存储时间间隔向量。

该模块支持在时间间隔数为零时为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外推选项，可能会发生意外行为。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: time and temperature`。

### **Percentage change in terminal resistance due to calendar aging, dR0(t\_ar,T\_ar)** — 由日历老化引起的端子电阻百分比变化 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]`（默认）| 标量矩阵

由日历老化引起的端子电阻百分比变化。

#### 依赖关系

要启用此参数，请将 **Internal resistance calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: time and temperature`。

### **Vector of sampled storage time intervals for capacity calendar aging, t\_ac** — 容量日历老化的采样存储时间间隔 `[0, 90, 180, 270, 360]` `d`（默认）| 标量向量

容量日历老化的采样存储时间间隔向量。

该模块支持在时间间隔数为零时为衰减和日历老化选项定义断点值。如果未定义零断点值，则根据外推选项，可能会发生意外行为。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: time and temperature`。

### **Percentage change in capacity due to calendar aging, dAH(t\_ac,T\_ac)** — 由日历老化引起的容量百分比变化 `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]`（默认）| 标量矩阵

由日历老化引起的容量百分比变化。

#### 依赖关系

要启用此参数，请将 **Capacity calendar aging** 设置为 `Enabled`，并将 **Modeling option** 设置为 `Tabulated: time and temperature`。

### 热

### **Thermal port** — 热端口可见性 `Omit`（默认）| `Model`

是否公开热端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `thermal_port` |
| **值：** | `"omit"`（默认）| `"model"` |

### **Simulation temperature** — 电池温度 `298.15` `K`（默认）| 正数

整个仿真期间查找表中使用的电池温度。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Omit`，并将 **Tabulate parameters over temperature** 设置为 `Yes`，或将 **Fade characteristic** 设置为 `Lookup tables (constant temperature dependent)`。有关详细信息，请参阅热效应建模。

### **Thermal mass** — 与热端口关联的热质量 `100` `J/K`（默认）

与热端口 H 关联的热质量。它表示将热端口温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。有关详细信息，请参阅热效应建模。

## 所属库

Simscape / Electrical / Sources Simscape / Battery / Cells

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023b: 当放电循环次数或时间间隔为零时，为衰减和日历老化选项定义断点值

当放电循环次数或时间间隔为零时，您可以为衰减和日历老化选项定义断点值。

如果您未定义零断点值：

- 如果将 **Extrapolation method for all tables** 参数设置为 `Linear`，则根据表数据，该模块可能外插出不正确的值。例如，外插得到的容量可能升到 1 以上，这意味着该点处电池单体的容量大于电池单体的标称容量。
- 如果将 **Extrapolation method for all tables** 参数设置为 `Nearest`，则该模块外插最近的值。对于全新的电池，这意味着衰减和日历老化已经发生。
- 如果将 **Extrapolation method for all tables** 参数设置为 `Error`，则当放电循环次数或存储持续时间低于此表数据的最低断点时，软件会抛出错误。

## 描述

表格式电池模型

Battery (Table-Based) 模块表示高保真电池模型。该模块使用查找表将开路电压计算为荷电水平和可选温度的函数，并包含若干建模选项：

- 自放电
- 电池衰减
- 充电动态
- 日历老化

**注意**

对于所有基于表的参数，Battery (Table-Based) 模块仅支持线性插值。对于外插，将 **Extrapolation method for all tables** 参数设置为 `Nearest`、`Linear` 或 `Error`。

对于行和列，它遵循行列约定，即先索引行，随后索引列。

该图显示了一个电池，其性能随温度和荷电状态的变化而变化，这通常见于数据表。

使用此模块可基于数据表或实验结果对具有复杂开路电压行为的电池进行参数化。要获得更简单的电池表示，请参阅 Battery (Simscape Electrical) 模块。

Battery (Table-Based) 模块有两个可选端口，您可以通过设置相应参数来公开这些端口。额外的物理信号端口 **SOC** 输出内部荷电状态。使用此功能可根据荷电状态改变负载行为，而无需构建荷电状态估计器的复杂性。要公开 **SOC** 端口，请在 **Main** 设置中将 **Expose SOC measurement port** 参数设置为 `Yes`。

要公开热端口，请在 **Thermal** 设置中将 **Thermal port** 参数设置为 `Model`。热端口表示电池热质量。

您还可以为此模块选择不同的内置参数化。有关详细信息，请参阅 Predefined Parameterization 部分。

电池等效电路由基础电池模型、自放电电阻 *RSD*、充电动态模型和串联电阻 *R0* 组成。

### 电池模型

该模块通过插值计算开路电压，即基础电池模型两端的电压：

v0=v0(SOC,T)

其中：

- *v0* 是电池的开路电压。如果沿温度对参数制表，则使用 **Open-circuit voltage, V0(SOC,T)** 参数指定查找值网格；否则使用 **Open-circuit voltage, V0(SOC)**。
- `SOC` 是当前电荷量与标称电池容量之比，该标称电池容量由 **Cell capacity, AH** 参数指定，并包含由 **Percentage change in cell capacity, dAH(N, Tfade)** 参数指定的温度相关衰减导致的单体容量百分比变化 *δAH(n, Tfade)* 的影响。使用 **Vector of state-of-charge values, SOC** 参数指定 SOC 断点。该模块通过插值指定的温度相关衰减特性和 **Cell capacity, AH** 参数，基于循环次数和电池温度估计标称电池容量。

  `SOC` 表示相对于 *qnom* 的归一化数据。

  对于基于查找表的衰减特性选项，

  qnom(T,n)=(1+δAH(n,Tfade)100)\*AH Ah.

  对于基于方程的衰减特性选项，

  qnom(T,n)=(1+δAH100nN)\*AH Ah.

  最后，`SOC` 由以下方程得到。

  SOC(t)=1qnom(T,n)∫(i(t)−Vopen(T,n,t)RSD(T,n))dt

  其中：

  - *qnom* 是电池的单体容量。使用 **Cell capacity, AH** 参数指定此值。
  - *N* 是参考放电循环次数，在该次数上您指定多个电池参数的百分比变化。使用 **Number of discharge cycles, N** 参数设置此值。
  - *n* 是电池的当前循环次数。
  - *δAH* 是电池在 *N* 次放电循环后单体容量的百分比变化。
- *T* 是电池温度。如果沿温度对参数制表，则使用 **Vector of temperatures, T** 参数指定 *T* 断点。

该模块还将串联电阻 *R0* 建模为荷电状态和可选温度的函数。如果沿温度对参数制表，则使用 **Terminal resistance, R0(SOC,T)** 参数指定串联电阻的查找值网格；否则使用 **Terminal resistance, R0(SOC)**。

### 对自放电建模

当电池端子开路时，内部电流仍可能使电池放电。此行为称为自放电。要启用此效应，将 **Self-discharge** 参数设置为 `Enabled`。

该模块使用跨接在基础电池模型端子上的温度相关电阻 *RSD(T)* 对这些内部电流建模。如果沿温度对参数制表，则可以使用 **Self-discharge resistance, Rleak(T)** 参数指定此电阻的查找值；否则使用 **Self-discharge resistance, Rleak**。

### 对充电动态建模

电池无法瞬时响应负载变化。它们需要一些时间才能达到稳态。这种时变特性是电池充电动态的结果，并在等效电路中使用并联 RC 段建模。

您可以使用 **Charge dynamics** 参数对电池充电动态建模：

- `No dynamics` — 等效电路不包含并联 RC 段。电池的端子电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。如果沿温度对参数制表，则使用 **First time constant, tau1(SOC,T)** 参数指定时间常数；否则使用 **First time constant, tau1(SOC)**。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。如果沿温度对参数制表，则使用 **First time constant, tau1(SOC,T)** 和 **Second time constant, tau2(SOC,T)** 参数指定时间常数；否则使用 **First time constant, tau1(SOC)** 和 **Second time constant, tau2(SOC)**。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。如果沿温度对参数制表，则使用 **First time constant, tau1(SOC,T)**、**Second time constant, tau2(SOC,T)** 和 **Third time constant, tau3(SOC,T)** 参数指定时间常数；否则使用 **First time constant, tau1(SOC)**、**Second time constant, tau2(SOC)** 和 **Third time constant, tau3(SOC)**。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 段。如果沿温度对参数制表，则使用 **First time constant, tau1(SOC,T)**、**Second time constant, tau2(SOC,T)**、**Third time constant, tau3(SOC,T)** 和 **Fourth time constant, tau4(SOC,T)** 参数指定时间常数；否则使用 **First time constant, tau1(SOC)**、**Second time constant, tau2(SOC)**、**Third time constant, tau3(SOC)** 和 **Fourth time constant, tau4(SOC)**。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 段。如果沿温度对参数制表，则使用 **First time constant, tau1(SOC,T)**、**Second time constant, tau2(SOC,T)**、**Third time constant, tau3(SOC,T)**、**Fourth time constant, tau4(SOC,T)** 和 **Fifth time constant, tau5(SOC,T)** 参数指定时间常数；否则使用 **First time constant, tau1(SOC)**、**Second time constant, tau2(SOC)**、**Third time constant, tau3(SOC)**、**Fourth time constant, tau4(SOC)** 和 **Fifth time constant, tau5(SOC)**。

此图显示了配置为 two time-constant dynamics 的模块的等效电路。

图中：

- *R1* 和 *R2* 是并联 RC 电阻。如果沿温度对参数制表，则分别使用 **First polarization resistance, R1(SOC,T)** 和 **Second polarization resistance, R2(SOC,T)** 参数指定这些值；否则使用 **First polarization resistance, R1(SOC)** 和 **Second polarization resistance, R2(SOC)**。
- *C1* 和 *C2* 是并联 RC 电容。每个并联段的时间常数 *τ* 通过关系 C=τ/R 关联 *R* 和 *C* 值。如果沿温度对参数制表，则分别使用 **First time constant, tau1(SOC,T)** 和 **Second time constant, tau2(SOC,T)** 参数为每个段指定 *τ*；否则使用 **First time constant, tau1(SOC)** 和 **Second time constant, tau2(SOC)**。
- *R0* 是串联电阻。如果沿温度对参数制表，则使用 **Terminal resistance, R0(SOC,T)** 参数指定此值；否则使用 **Terminal resistance, R0(SOC)**。

### 对电池衰减建模

电池衰减是电池性能在重复充电和放电循环后的劣化。当 **Fade characteristic** 参数设置为 `Equations` 时，电池衰减按如下方式建模。

基础电池模型两端的开路电压随放电循环次数 *n* 成比例衰减：

v0,fade=v0(1+δv0100nN)

其中 *δv0* 是 *N* 次放电循环后开路电压的百分比变化。使用 **Change in open-circuit voltage after N discharge cycles (%)** 参数指定 *δv0*。

**注意**

Battery (Table-Based) 模块跟踪电流并对其随时间积分。每当提取出一个等效单体放电容量时，放电循环次数 *n* 增加 1。

用于计算荷电状态的标称电荷随放电循环次数的平方根衰减：

qnom,fade=qnom(1+δAH100nN)

电池模型中的所有电阻也随放电循环次数的平方根衰减：

Ri,fade=Ri(1+δRi100nN)

其中：

- *Ri* 是第 *i* 个电阻
- *δRi* 是此电阻在 *N* 次循环内的百分比变化

根据您配置模块的方式，电阻可能包括：

- 串联电阻 — 使用 **Change in terminal resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 自放电电阻 — 使用 **Change in self-discharge resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 第一个充电动态电阻 — 使用 **Change in first polarization resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 第二个充电动态电阻 — 使用 **Change in second polarization resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 第三个充电动态电阻 — 使用 **Change in third polarization resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 第四个充电动态电阻 — 使用 **Change in fourth polarization resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。
- 第五个充电动态电阻 — 使用 **Change in fifth polarization resistance after N discharge cycles (%)** 参数指定在 *N* 次循环内的百分比变化。

**注意**

您还可以使用查找表（temperature independent）或查找表（constant temperature dependent）对电池衰减特性建模。选择这两个选项中的任意一个都会相应地更改模块参数。有关详细信息，请参阅 Fade parameters 选项卡。

### 对热效应建模

电池温度由模型中包含的所有欧姆损耗之和确定：

MthT˙=∑iVT,i2/RT,i

其中：

- *M*th 是电池热质量。
- *i* 对应于第 *i* 个欧姆损耗贡献项。根据您配置模块的方式，损耗可能包括：

  - 串联电阻
  - 自放电电阻
  - 第一个充电动态段
  - 第二个充电动态段
  - 第三个充电动态段
  - 第四个充电动态段
  - 第五个充电动态段
- *VT,i* 是电阻 *i* 上的电压降。
- *RT,i* 是电阻 *i*。

### 电池老化建模

您可以对电池不使用时发生的电池性能劣化进行建模。日历老化同时影响内阻和容量。特别地，电阻增加取决于多种机制，例如在阳极和阴极形成固体电解质界面 (SEI) 以及集流体腐蚀。这些过程主要取决于存储温度、存储荷电状态和时间。

您可以通过将 Battery (Table-Based) 模块中的 **Modeling option** 参数设置为以下值来对日历老化建模：

- `Equation-based`
- `Tabulated: temperature`
- `Tabulated: time and temperature`

**注意**

Battery (Table-Based) 模块仅在初始化期间应用日历老化。当您将 **Internal resistance calendar aging** 或 **Capacity calendar aging** 参数设置为 `Enabled` 时，该模块会显示 **Vector of time intervals** 参数，该参数表示电池在仿真开始前已老化的时间。此选项不涵盖仿真期间的日历老化。

**Equation-based**

以下方程定义由于日历老化导致的电池端子电阻增加：

αr(T,Voc)=(bVoc−c)e−qdkT,R=R0(1+∑i=1i=nαr(Ti,Voc)(tia−ti−1a)),

其中：

- *Voc* 是 **Normalized open-circuit voltage during storage, V/Vnom**。
- *R0* 是 **Internal resistance**。
- *ti* 是从 **Vector of time intervals** 参数导出的时间采样。
- *Ti* 从 **Vector of temperatures, T** 参数导出。
- *b* 是 **Terminal resistance linear scaling for voltage, b**。
- *c* 是 **Terminal resistance constant offset for voltage, c**。
- *d* 是 **Terminal resistance temperature-dependent exponential increase, d**。
- *a* 是 **Terminal resistance time exponent, a**。
- *q* 是电子的基本电荷，单位为 C。
- *k* 是玻尔兹曼常数，单位为 J/K。

以下方程定义由于日历老化导致的电池容量下降：

αc(T,Voc)=(bVoc−c)e−qdkT,C=C0(1−∑i=1i=nαc(Ti,Voc)(tia−ti−1a)),

其中：

- *C0* 是 **initial capacity**。
- *b* 是 **Capacity linear scaling for voltage, b**。
- *c* 是 **Capacity constant offset for voltage, c**。
- *d* 是 **Capacity temperature-dependent exponential increase, d**。
- *a* 是 **Capacity time constant, a**。

如果您将 **Storage condition** 参数设置为 `Specify state-of-charge during storage`，该模块会使用根据荷电状态和存储期间温度制表的电压 **V0**，将存储期间的荷电状态转换为归一化开路电压。

**Tabulated: temperature**

老化后的端子电阻是端子电阻 *R0(SOC,T)*、电阻增加百分比 *dR0* 以及描述日历老化时间依赖性的幂律之间的乘积：

R0(SOC,T;tst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Tst,i)100(tast,i−tast,i−1tast,m)),

其中：

- *T* 是电池温度。如果在温度上对参数制表，请使用 **Vector of temperatures, T** 参数指定 *T* 断点。
- *Tst* 是 **Vector of storage temperatures**。
- *tst,i* 和 *tst,i-1* 是从 **Vector of time intervals** 导出的时间采样。
- *t0* 假定为零。
- *tst,m* 是测量电阻增加 *dR0* 的时间点。

同一方程适用于老化电池容量的计算。

**Tabulated: time and temperature**

老化后的端子电阻是端子电阻 *R0(SOC,T)* 与 *dR0* 的乘积：

R0(SOC,T;Δtst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Δtst,i,Tst,i)100).

同一方程适用于老化电池容量的计算。

### 预定义参数化

Battery (Table-Based) 模块有多个可用的内置参数化。

此预参数化数据允许您设置该模块以表示特定供应商的组件。这些电池的参数化与制造商数据表中的放电曲线匹配。要加载预定义参数化，请双击 Battery (Table-Based) 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

可用的预参数化数据对锂离子电池的稳态电气参数进行建模。**Open-circuit voltage, V0(SOC)**、**Terminal resistance, R0(SOC, T)**、**Cell capacity, AH**、**Percentage change in cell capacity, dAH** 和 **Percentage change in Open-circuit voltage, dV0(N)** 参数是根据制造商数据表中的特性曲线参数化的。串联电阻随电池循环寿命的变化、热质量以及动态 RC 网络参数未进行参数化。相反，RC 网络电阻器的净电阻会加到特定预参数化数据的串联电阻中。如果需要填充 RC 参数数据，请从串联电阻数据中减去 RC 网络净电阻。

可用数据是针对不同温度下、直至数据表中最低端子电压的 1C 放电电流进行参数化的。低于最低端子电压的数据是外推得到的。**Open-circuit voltage, V0(SOC)** 参数近似为与温度无关。在较低温度下、低 SOC 区域中，端子电阻恒定，并等于最低端子电压处的电阻值。这可能导致更高的热损耗。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。使用工程判断和简化假设来填补缺失数据。因此，预计仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

有关预参数化以及可用组件列表的详细信息，请参阅预参数化组件列表 (Simscape Electrical)。

### 绘制基本电压-电荷特性

您无需构建完整模型即可绘制 Battery (Table-Based) 模块的基本电压-电荷特性。使用这些图可探究参数选择对器件特性的影响。如果您根据数据表对模块进行参数化，可以将图与数据表进行比较，以检查是否正确参数化了模块。如果您有完整的工作模型但不知道使用哪个制造部件，可以将图与数据表进行比较以帮助决策。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Battery** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅绘制电池模块的基本电压-电荷特性 (Simscape Electrical)。
