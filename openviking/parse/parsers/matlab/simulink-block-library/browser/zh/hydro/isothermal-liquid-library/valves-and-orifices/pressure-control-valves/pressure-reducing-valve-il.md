---
type: simulink-block
title: 'Pressure-Reducing Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalveil'
documentation_source_path: 'ref/pressurereducingvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Reducing Valve (IL)

## 端口

### 输入

### **Ps** — 设定压力信号，Pa 物理信号

受控阀门操作的压力阈值，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **设定压力控制** 设置为 `Controlled`。

### 守恒

### **A** — 液体端口，isothermal liquid

阀门的入口或出口点。

### **B** — 液体端口，isothermal liquid

阀门的入口或出口点。

## 参数

### 参数

### **设定压力控制** — 阀门操作方法 `Constant` (默认) | `Controlled`

阀门操作方法。当将此参数设置为 `Constant` 时，阀门会在固定的压力调节范围内线性关闭，或根据提供的表列压力和开口面积数据关闭。当将此参数设置为 `Controlled` 时，阀门会根据端口 **Ps** 处的可变设定压力信号在固定压力调节范围内关闭。

### **开口参数化** — 开口参数化 `Linear - Area vs. pressure` (默认) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀门开口的建模方法。当选择 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开口面积与控制压力关联。当选择 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用减压阀的参考流量与压差曲线。

### **设定压力（表压）** — 触发阀门操作的表压 `0.1` `MPa` (默认) | 正标量

触发阀门操作的表压。当端口 **B** 处的压力达到此值时，阀门开始关闭。此参数会平移参考曲线，使减压阀在端口 **B** 处的压力等于设定压力时开始关闭。

#### 依赖关系

要启用此参数，请将 **设定压力控制** 设置为 `Constant`。

### **压力调节范围** — 阀门工作压力范围 `1` `MPa` (默认) | 正标量

阀门的工作压力范围。压力调节范围始于 **设定压力（表压）**，范围的终点是阀门最大工作压力。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure`。

### **最大开口面积** — 阀门完全打开时的面积 `1e-4` `m^2` (默认) | 正标量

阀门处于完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure`。

### **泄漏面积** — 阀门处于完全关闭位置时的间隙面积 `1e-10` `m^2` (默认) | 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此参数通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure`。

### **端口 B 处压力（表压）向量** — 用于表列面积参数化的表压值向量 `[0.2 : 0.2 : 1.2]` `MPa` (默认) | 1×*n* 向量

用于阀门开口面积表列参数化的表压值向量。向量元素必须与 **开口面积向量** 参数中的元素一一对应。元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Tabulated data - Area vs. pressure`。

### **开口面积向量** — 用于表列参数化的阀门开口面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2` (默认) | 1×*n* 向量

用于阀门开口面积表列参数化的阀门开口面积向量。向量元素必须与 **端口 B 处压力（表压）向量** 参数中的元素一一对应。元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Tabulated data - Area vs. pressure`。

### **端口 A 和 B 处的横截面积** — 阀门入口或出口处的面积 `inf` `m^2` (默认) | 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在确定通过阀门质量流量的压力-流量方程中使用这些面积。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **流量系数** — 流量系数 `0.64` (默认) | 正标量

用于考虑理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **临界雷诺数** — 层流的上限雷诺数 `150` (默认) | 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **平滑因子** — 数值平滑因子 `0.01` (默认) | 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流动响应引入一层渐变变化。将此值设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure`。

### **压力恢复** — 包含面积扩大期间压力增加的选项 `off` (默认) | `on`

是否捕获流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **开口动态** — 包含阀门开口流动响应的选项 `off` (默认) | `on`

是否近似由于阀门开口而对流体系统产生的瞬态影响。选择 **开口动态** 会通过在流动响应中引入一阶滞后来近似开口条件。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **开口时间常数** — 阀门开口时间常数 `0.1` `s` (默认) | 正标量

用于计算开口动态中滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **开口动态**，并将 **开口参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **端口 A 处参考压力（表压）** — 端口 A 处参考压力 `1.5` `MPa` (默认) | 正标量

端口 **A** 处的恒定压力，作为参考曲线的基础。此值通常对应于阀门最大工作压力。仿真期间端口 **A** 处的压力可以为任意值。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **端口 B 处参考压力（表压）向量** — 端口 B 处参考压力 `[1.2, 1, .8, .6, .4, .2]` `MPa` (默认) | 1×*n* 向量

当阀门开口面积变化时，参考曲线中端口 **B** 处单调递减的压力值向量。第一个元素是参考最大压力，即阀门完全关闭时的压力。最后一个元素是参考设定压力。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **参考体积流量向量** — 参考体积流量 `[1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028]` `m^3/s` (默认) | 1×*n* 向量

通过阀门的单调递增参考流量向量。模块使用此曲线为变化的阀门面积生成流量系数。

#### 依赖关系

要启用此参数，请将 **开口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 单向阀

### **启用单向阀** — 单向阀选项 `off` (默认) | `on`

模块是否对内部单向阀进行仿真。

### **开启压差** — 单向阀操作的设定压力 `0.1` `MPa` (默认) | 正标量

使单向阀开启的压差。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Linear - Area vs. pressure`。

### **最大开启压差** — 阀门中的最大压力 `0.2` `MPa` (默认) | 正标量

单向阀完全关闭时的压差。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Linear - Area vs. pressure`。

### **最大开口面积** — 最大打开面积 `1e-4` `m^2` (默认) | 正标量

负载管路中单向阀的最大打开面积。在内部，单向阀与减压级并联。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Linear - Area vs. pressure`。

### **压差向量** — 单向阀操作的压差 `[0.01 : 0.01 : 1]` `MPa` (默认) | 1×*n* 向量

单向阀级的压差向量。模块将单向阀压差计算为端口 **B** 处压力相对于端口 **A** 处压力的差值。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **开口面积向量** — 单向阀级开口面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2` (默认) | 1×*n* 向量

单向阀级的开口面积向量。向量元素必须与 **压差向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Tabulated data - Area vs. pressure`。

### **体积流量向量** — 单向阀级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s` (默认) | 1×*n* 向量

单向阀级的体积流量向量。此向量的元素必须与 **压差向量** 参数中的元素对应。

#### 依赖关系

要启用此参数，请将 **启用单向阀** 设置为 `On`，并将 **阀门参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 故障

### **减压阀面积故障** — 用于建模减压阀故障的选项 `Add fault`

用于启用减压阀故障参数的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，模块会将开口面积设置为 **故障时减压阀开口** 参数指定的位置。

### **故障时减压阀开口** — 减压阀故障位置 `Closed` (默认) | `Open` | `Maintain last value`

故障时减压阀位置。您可以选择阀门在打开、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请为 **减压阀面积故障** 参数单击 **Add fault** 超链接。

### **单向阀面积故障** — 用于建模单向阀故障的选项 `Add fault`

用于启用单向阀故障参数的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，模块会将开口面积设置为 **故障时单向阀开口** 参数指定的位置。

#### 依赖关系

要启用此参数，请选择 **启用单向阀**。

### **故障时单向阀开口** — 故障阀门特性 `Closed` (默认) | `Open` | `Maintain last value`

故障时单向阀位置。您可以选择阀门在打开、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请选择 **启用单向阀**，并为 **单向阀面积故障** 参数单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Pressure-Reducing Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：按体积流量与压力进行参数化

您可以将 **开口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### R2022b：访问预参数化模块选项

模块支持预参数化选项。供应商包括 Hawe Hydraulik、Rexroth Bosch Group 和 Sun Hydraulics。

## 描述

等温液体网络中的减压阀

Pressure-Reducing Valve (IL) 模块表示等温液体网络中的减压阀。当端口 **B** 处的压力小于指定压力时，阀门保持打开。当端口 **B** 处的压力达到或超过此压力时，阀门关闭。模块基于设定压力与端口 **B** 处压力之间的差值运行。模块包含一个单向阀部分，其在流动反向期间的功能与 Check Valve (IL) 模块相同。若要基于流体网络中的其他位置进行压力控制，请参阅 Pressure Compensator Valve (IL) 模块。

### 设定压力控制

模块在设定压力与最大压力之间调节压力。当您将 **设定压力控制** 设置为：

- `Controlled` — 您可以将压力信号连接到端口 **Ps**。当端口 **B** 处的压力大于参考设定压力 *Pset* 且低于 *Pmax* 时，模块调节压力。端口 **B** 处的压力充当此阀门的控制压力 *Pcontrol*。

  *Pmax* 是 *Pset* 与压力调节范围之和。
- `Constant` — **设定压力（表压）** 参数定义恒定设定压力。

模块如何确定压力调节范围取决于 **开口参数化** 参数：

- `Linear - Area vs. pressure` — **压力调节范围** 参数定义压力调节范围。
- `Tabulated data - Area vs. Pressure` — 压力调节范围是 **端口 B 处压力（表压）向量** 参数最后一个元素与第一个元素之差。
- `Tabulated data - Volumetric flow rate vs. pressure` — 压力调节范围是 **端口 B 处参考压力（表压）向量** 参数第一个元素与最后一个元素之差。

### 面积与压力参数化

当您将 **开口参数化** 设置为 `Linear - Area vs. pressure` 时，模块按如下方式计算阀面积

Avalve=p^(Aleak−Amax)+Amax,

其中归一化压力 p^ 为

p^=pcontrol−psetpmax−pset.

当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真中的数值稳健性。如果 **平滑因子** 参数非零，模块会在
*pset* 和
*pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅
数值平滑。

该图展示了使用线性面积参数化时阀的开口特性。开口面积
*Avalve* 随出口
压力 *pB,gauge* 线性下降。开口面积
范围为 *Aleak* 到
*AMax*，压力工作
范围从 *pset* 开始并到
*pmax*。

线性面积参数化的开口面积随压力变化的绘图

当您将 **开口参数化** 设置为 `Tabulated data - Area vs. Pressure` 时，模块按如下方式计算开口面积

Avalve=tablelookup(pcontrol,TLU,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol* =
  *pB,gauge* 是
  控制压力。
- *pcontrol,TLU* =
  *pB,TLU* +
  *poffset*。
- *pB,TLU* 是
  **端口 B（表压）压力向量**
  参数。
- *poffset* 是一个内部
  压力偏移量，当
  *pB,Gauge* =
  *pset* 时，它使阀开始关闭，其中
  *poffset* =
  *pset* -
  *pB,TLU(1)*。
- *ATLU* 是
  **开口面积向量** 参数。

*Amax* 和
*Aleak* 分别是
**开口面积向量** 参数的第一个和最后一个参数。
该图展示了使用
表格面积参数化时阀的开口特性。

表格面积参数化的开口面积随压力变化的绘图

**质量守恒**

当您将 **开口参数化** 设置为
`Linear - Area vs. pressure` 或
`Tabulated data - Area vs. Pressure` 时，模块
按如下方式守恒质量：

m˙A+m˙B=0.

模块按如下方式计算质量流量

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是
  **排放系数** 参数。
- *Avalve* 是
  瞬时阀开口面积。
- *Aport* 是
  **端口 A 和 B 的横截面积**
  参数。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差
  *pA* –
  *pB*。

临界压差
*Δpcrit* 是与 **临界雷诺数**
参数 *Recrit* 相关的压差，即层流和湍流之间的流态
转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*压力损失* 描述了由于面积减小而在阀中造成的压力
降低。模块按如下方式计算
*PRloss*：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*压力恢复* 描述了由于面积增大而在阀中产生的正压力变化。如果您不希望捕获这种压力
升高，请清除 **压力恢复** 复选框。在这种
情况下，*PRloss* 为 1。

模块使用阀开口动态确定开口面积
*Avalve*。

**开口动态**

对于任一种面积参数化，您都可以选择仿真阀响应的开口动态。如果您选择 **开口动态**，模块会在阀打开时向流量响应添加一个延迟，并且
*Avalve* 变为动态开口面积 *Adyn*。否则，
*Avalve* 是稳态开口面积。模块基于 **开口时间常数** 参数
*τ* 计算动态开口面积的瞬时变化：

p˙dyn=pcontrol−pdynτ.

默认情况下，模块忽略开口动态。

模块基于控制压力
*pcontrol* 计算稳态动态，并使用与阀开口相同的
参数化。

### 体积流量与压力参数化

体积流量参数化方程引用以下量：

- *⩒TLU,ref* 是
  **参考体积流量向量**
  参数。
- *PA,gauge,ref* 和
  *PB,gauge,ref* 分别是
  **端口 A（表压）参考压力向量** 和
  **端口 B（表压）参考压力向量**
  参数。
- *pset,gauge* 是
  **设定压力（表压）** 参数或
  端口 **Ps** 处的信号。
- *K* 是通过减压级的流量系数，模块会在仿真期间计算该系数。
- ρ¯ 是减压阀中的平均流体密度。
- *Δp* 是流体流过阀时的压降。
- *Δpcrit* 是流体流动的临界
  压降。
- *Cd* 是排放
  系数，模块会为体积流量
  参数化在内部设置该系数。
- *Recrit* 是临界
  雷诺数，模块会在内部设置该值。
- *ν* 是运动黏度，对于
  等温液体网络，该值为常量。

当您将 **开口参数化** 设置为
`Tabulated data - Volumetric flow rate vs. pressure` 时，
模块按如下方式计算减压阀的平滑质量流量：

m˙valve=ρ¯KΔp(Δp2+Δp2)14Δp=pA−pBΔpcrit=π2ρ¯8CdK(Recritν)2

其中模块使用
`tablelookup` 函数计算 *K*，如下所示：

K=tablelookup(Δpcontrol,TLU,Ref,KTLU,Ref,Δpcontrol,interpolation=linear,extrapolation=nearest)KTLU,Ref=V˙TLU,RefΔpTLU,Ref

模块按如下方式计算控制压力：

Δpcontrol=pB−pdrain,

其中模块将排放压力 *pdrain* 设置为 1 atm。模块按如下方式计算参考控制压力
向量：

Δpcontrol,TLU,Ref=pB,gauge,ref+poffset,

其中 *poffset* 是一个
内部计算的压力偏移量，当 *pB,gauge,ref* =
*pset,gauge* 时，它使阀开始关闭。因此，*poffset* =
*pset,gauge* -
*pB,gauge,ref*。该图展示了模块如何使用
表格体积流量参数化来控制压力。

表格体积参数化的开口面积随压力变化的绘图

### 故障

要对故障建模，请在 **故障** 部分中，
单击要建模的故障旁边的 **添加故障** 超链接。使用
故障参数来指定故障属性。有关故障建模的详细信息，
请参阅 Simscape 故障简介。

减压阀和单向阀有三种故障选项可用。对于
**故障时减压阀开口** 和 **故障时单向阀开口**
参数，您可以选择：

- `Closed` — 阀关闭到其最小
  开口值，具体取决于 **开口
  参数化** 参数。当您将
  **开口参数化** 设置为：

  - `Linear - Area vs. pressure` —
    阀面积减小到 **泄漏
    面积** 参数的值。
  - `Tabulated data - Area vs. pressure` — 阀面积减小到
    **开口面积
    向量** 参数中最后一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到
    导出的流量
    系数查找表中最后一个元素的值，
    *KTLU,Ref*。
- `Open` — 阀打开到其最大
  开口值，具体取决于 **开口
  参数化** 参数。当您将
  **开口参数化** 设置为：

  - `Linear - Area vs. pressure` —
    阀面积打开到 **最大
    开口面积** 的值。
  - `Tabulated data - Area vs. pressure` — 阀面积打开到
    **开口面积
    向量** 中第一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到
    导出的流量
    系数查找表中第一个元素的值，
    *KTLU,Ref*。
- `Maintain last value` — 阀面积
  保持为触发发生时的阀开口面积。

对于线性参数化，阀面积极值处的数值平滑会导致应用的最小面积大于
**泄漏面积** 参数，而最大值小于
**最大孔口面积** 参数。

故障触发后，阀在仿真的其余时间内保持为故障后的面积。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，这使您能够
对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **所选零件** 旁边，单击
   模块对话框设置中 **所选零件** 旁边的
   "<click to select>" 超链接。
2. 模块参数化管理器窗口打开。从菜单中选择一个零件
   并单击 **全部应用**。您可以使用
   **制造商** 下拉菜单缩小选择范围。
3. 您可以关闭 **模块参数化管理器** 菜单。
   模块现在具有您指定的参数化。
4. 您可以通过选择一个零件并查看
   **将所选零件与模块比较**
   部分中的数据，在模块参数化管理器窗口中将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数
值。模块会用工程判断和简化假设替代
缺失数据。因此，预计仿真行为与实际物理
行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，
并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。
