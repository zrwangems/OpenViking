---
type: simulink-block
title: 'Receiver Accumulator (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Tanks & Accumulators'
documentation_page: 'receiveraccumulator2p'
documentation_source_path: 'ref/receiveraccumulator2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Receiver Accumulator (2P)

## 端口

### 输出

### **L** — 液位物理信号

储罐中的液位。使用此端口监测内部剩余的液体量。
### 守恒

### **AV** — 储罐开口两相流体

流体流入或流出储罐的开口。液体和蒸气均可通过此端口进入。但是，只有蒸气可以通过此端口流出——直到储罐中的蒸气耗尽，此时液体也可以通过此端口流出。

### **BV** — 储罐开口两相流体

流体流入或流出储罐的开口。液体和蒸气均可通过此端口进入。但是，只有蒸气可以通过此端口流出——直到储罐中的蒸气耗尽，此时液体也可以通过此端口流出。

### **AL** — 储罐开口两相流体

流体流入或流出储罐的开口。液体和蒸气均可通过此端口进入。但是，只有液体可以通过此端口流出——直到储罐中的液体耗尽，此时蒸气也可以通过此端口流出。

### **BL** — 储罐开口两相流体

流体流入或流出储罐的开口。液体和蒸气均可通过此端口进入。但是，只有液体可以通过此端口流出——直到储罐中的液体耗尽，此时蒸气也可以通过此端口流出。

### **H** — 储罐壁热

流体体积与储罐壁之间的热边界。使用此端口捕获流体与储罐外部环境之间的各种热交换——例如传导、对流或辐射。

## 参数

### 主要

### **Total tank volume** — 储罐中液相和气相的总容积 `1 m^3`（默认）| 正标量

储罐中液相和气相的总容积。

### **Tank cross-sectional area** — 储罐横截面积 `0.5 m^2`（默认）| 正标量

储罐的横截面积。

### **Cross-sectional area at port AV** — 端口 AV 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

端口 **AV** 处垂直于流动方向的面积。

### **Cross-sectional area at port BV** — 端口 BV 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

端口 **BV** 处垂直于流动方向的面积。

### **Cross-sectional area at port AL** — 端口 AL 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

端口 **AL** 处垂直于流动方向的面积。

### **Cross-sectional area at port BL** — 端口 BL 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

端口 **BL** 处垂直于流动方向的面积。

### **Liquid volume fraction out of range** — 当体积分数超出范围时的行为 `No error`（默认）| `Error` | `Warning`

选择当模块的体积分数低于 **Minimum liquid volume fraction** 参数或高于 **Maximum liquid volume fraction** 参数时的行为。选择 `Warning` 以在体积分数超出指定范围时收到通知。选择 `Error` 以在此类事件发生时停止仿真。

### **Minimum liquid volume fraction** — 触发警告或错误的下限值 `0.05`（默认）| 0 到 1 之间的正标量

储罐中液体体积分数有效范围的下限。低于此值的分数将触发仿真警告或错误（取决于 **Liquid volume fraction out of range** 模块参数的设置）。

#### 依赖关系

要启用此参数，请将 **Liquid volume fraction out of range** 设置为 `Warning` 或 `Error`。

### **Maximum liquid volume fraction** — 触发警告或错误的上限值 `0.95`（默认）| 0 到 1 之间的正标量

储罐中液体体积分数有效范围的上限。高于此值的分数将触发仿真警告或错误（取决于 **Liquid volume fraction out of range** 模块参数的设置）。

#### 依赖关系

要启用此参数，请将 **Liquid volume fraction out of range** 设置为 `Warning` 或 `Error`。

### **Volume fraction threshold for transition to pure liquid or pure vapor** — 过渡到纯液体或纯蒸气的相体积分数阈值 `0.05`（默认）| 0 到 1 之间的正标量

任一相的体积分数低于此值时过渡到单相储罐——要么是过冷液体，要么是过热蒸气。此参数决定过渡的平滑程度。其值越大，过渡越平滑，因此仿真越快（但代价是精度较低）。

### 传热

### **Vapor heat transfer coefficient** — 蒸气与储罐壁之间热交换的系数 `20 W/(m^2*K)`（默认）| 正标量

蒸气区域与其对应的储罐壁部分之间热交换的系数。此参数用于计算此热交换的速率。

### **Liquid heat transfer coefficient** — 液体与储罐壁之间热交换的系数 `100 W/(m^2*K)`（默认）| 正标量

液体区域与其对应的储罐壁部分之间热交换的系数。此参数用于计算此热交换的速率。

### 效应和初始条件

### **Initial pressure** — 仿真开始时的绝对压力 `0.101325 MPa`（默认）| 标量

仿真开始时储罐中的压力。

### **Initial liquid fraction specification** — 初始液体分数的类型 `Liquid mass fraction`（默认）| `Liquid volume fraction`

是将初始液体体积分数指定为质量分数还是体积分数。

### **Initial liquid mass fraction** — 储罐中液体的初始质量分数 `0.5`（默认）| 0 到 1 之间的无量纲标量

仿真开始时储罐中液体的质量分数。

#### 依赖关系

要启用此参数，请将 **Initial liquid fraction specification** 设置为 `Liquid mass fraction`。

### **Initial liquid volume fraction** — 储罐中液体的初始体积分数 `0.5`（默认）| 0 到 1 之间的无量纲标量

仿真开始时储罐中液体的体积分数。

#### 依赖关系

要启用此参数，请将 **Initial liquid fraction specification** 设置为 `Liquid volume fraction`。

### **Initial liquid and vapor volumes fully saturated** — 将液体和蒸气指定为完全饱和的选项 `on`（默认）| `off`

是否将储罐中的液体和蒸气初始化为完全饱和状态。如果清除此复选框，则可以指定液体和蒸气体积的初始能量。

### **Initial fluid energy specification** — 用于定义初始流体能量的热力学变量 `Degree of subcooling and superheating`（默认）| `Temperature` | `Specific enthalpy` | `Specific internal energy`

模块用于定义初始流体能量的热力学变量。如果选中此复选框，则液体和蒸气均为饱和状态。如果清除此复选框，则模块使用初始流体能量规格参数分别计算液体和蒸气的过冷度或过热度。

#### 依赖关系

要启用此参数，请清除 **Initial liquid and vapor volumes fully saturated** 复选框。

### **Initial liquid subcooling** — 仿真开始时的液体过冷度 `5 deltaK`（默认）| 正标量

仿真开始时储罐中的液体过冷度。模块将初始液体温度初始化为 *Tsat
(pinit)-ΔTsub,init*，其中 *Tsat
(pinit)* 是 **Initial pressure** 参数值下的饱和温度，*ΔTsub,init* 是此参数的值。

#### 依赖关系

要启用此参数，请清除 **Initial liquid and vapor volumes fully saturated** 复选框，并将 **Initial fluid energy specification** 设置为 `Degree of subcooling and superheating`。

### **初始蒸气过热度** — 仿真开始时的蒸气过热度 `5 deltaK`（默认）| 正标量

仿真开始时储罐中的蒸气过热度。该模块将初始液体温度初始化为
*Tsat
(pinit)+ΔTsup,init*，
其中 *Tsat
(pinit)* 是 **初始压力**
参数值下的饱和温度，*ΔTsup,init* 是该参数的值。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`过冷度和
过热度`。

### **初始液体温度** — 仿真开始时的液体温度 `368.15 K`（默认）| 标量

仿真开始时储罐中的液体温度。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`温度`。

### **初始蒸气温度** — 仿真开始时的蒸气温度 `378.15 K`（默认）| 标量

仿真开始时储罐中的蒸气温度。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`温度`。

### **初始液体比焓** — 仿真开始时的液体比焓 `400 kJ/kg`（默认）| 标量

仿真开始时储罐中的液体比焓。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`比焓`。

### **初始蒸气比焓** — 仿真开始时的蒸气比焓 `2700 kJ/kg`（默认）| 标量

仿真开始时储罐中的蒸气比焓。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`比焓`。

### **初始液体比内能** — 仿真开始时的液体比内能 `400 kJ/kg`（默认）| 标量

仿真开始时储罐中的液体比内能。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`比内能`。

### **初始蒸气比内能** — 仿真开始时的蒸气比内能 `2700 kJ/kg`（默认）| 标量

仿真开始时储罐中的蒸气比内能。

#### 依赖关系

要启用此参数，请清除 **初始液体和
蒸气体积完全饱和** 复选框，并将
**初始流体能量指定** 设置为
`比内能`。

### **汽化和冷凝时间常数** — 相变事件的特征持续时间 `0.1 s`（默认）| 正标量

储罐中发生的相变事件达到平衡的特征时间。增大此参数可减慢相变速率，减小此参数可加快相变速率。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2024b：为液体和蒸气体积指定初始条件

现在，您可以使用 Receiver Accumulator (2P) 模块中的初始条件来指定未饱和的液体和蒸气体积。以前，如果您将液体体积初始化为过冷状态，或将蒸气初始化为过热状态，则该模块无法同时分别对蒸气或液体进行建模。现在，您可以指定初始液体或蒸气体积。清除 **Initial liquid and vapor volumes fully saturated** 参数，以指定液体体积和蒸气体积的初始能量。

如果您更新包含 Receiver Accumulator (2P) 模块的模型，而升级工具无法识别连接到网络的 Two-Phase Fluid Properties (2P) 或 Two-Phase Fluid Predefined Properties (2P) 模块，则会发出错误，指出初始液体分数未更新。要手动更新初始条件，您可能需要计算 *pinit* 处的初始饱和边界，即 **Initial pressure** 参数的值，其中：

- *Tsat (pinit)* 是 *pinit* 处的初始饱和温度。
- *hsat,liq (pinit)* 是 *pinit* 处的初始液体饱和比焓。
- *hsat,vap (pinit)* 是 *pinit* 处的初始蒸气饱和比焓。
- *usat,liq (pinit)* 是 *pinit* 处的初始液体饱和比内能。
- *usat,vap (pinit)* 是 *pinit* 处的初始蒸气饱和比内能。

按下表所示更新参数：

| 以前的初始条件参数 | 新的初始条件参数 |
| --- | --- |
| - **Initial fluid energy specification** 为 `Temperature` - *Tinit* 是 **Initial temperature** 参数的值 | - 将 **Initial fluid fraction specification** 设置为 `Liquid mass fraction`。 - 清除 **Initial liquid and vapor volumes fully saturated** 复选框。 - 将 **Initial fluid energy specification** 设置为 `Temperature`。 - 如果 *Tinit ≤ Tsat (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `1`。 - 将 **Initial liquid temperature** 参数的值设置为 *Tinit*。 - 如果 *Tinit > Tsat (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `0`。 - 将 **Initial vapor temperature** 参数的值设置为 *Tinit*。 |
| - **Initial fluid energy specification** 为 `Liquid mass fraction` - *Mfrac,init* 是 **Initial liquid mass fraction** 参数的值 | - 将 **Initial fluid fraction specification** 设置为 `Liquid mass fraction`。 - 选择 **Initial liquid and vapor volumes fully saturated**。 - 将 **Initial liquid mass fraction** 参数的值设置为 *Mfrac,init*。 |
| - **Initial fluid energy specification** 为 `Liquid volume fraction` - *Vfrac,init* 是 **Initial liquid volume fraction** 参数的值 | - 将 **Initial fluid fraction specification** 设置为 `Liquid volume fraction`。 - 选择 **Initial liquid and vapor volumes fully saturated**。 - 将 **Initial liquid volume fraction** 参数的值设置为 *Vfrac,init*。 |
| - **Initial fluid energy specification** 为 `Specific enthalpy` - *hinit* 是 **Initial specific enthalpy** 参数的值 | - 将 **Initial fluid fraction specification** 设置为 `Liquid mass fraction`。 - 清除 **Initial liquid and vapor volumes fully saturated** 复选框。 - 将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。 - 如果 *hinit ≤ hsat,liq (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `1`。 - 将 **Initial liquid specific enthalpy** 参数的值设置为 *hinit*。 - 如果 *hinit ≥ hsat,vap (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `0`。 - 将 **Initial vapor specific enthalpy** 参数的值设置为 *hinit*。 - 如果 *hsat,liq (pinit) < hinit < hsat,vap (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 hinit−hsat,liq(pinit)hsat,vap(pinit)−hsat,liq(pinit)。 - 将 **Initial liquid specific enthalpy** 参数的值设置为 *hsat,liq (pinit)*。 - 将 **Initial vapor specific enthalpy** 参数的值设置为 *hsat,vap (pinit)*。 |
| - **Initial fluid energy specification** 为 `Specific internal energy` - *uinit* 是 **Initial specific internal energy** 参数的值 | - 将 **Initial fluid fraction specification** 设置为 `Liquid mass fraction`。 - 清除 **Initial liquid and vapor volumes fully saturated** 复选框。 - 将 **Initial fluid energy specification** 设置为 `Specific internal energy`。 - 如果 *uinit ≤ usat,liq (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `1`。 - 将 **Initial liquid specific internal energy** 参数的值设置为 *uinit*。 - 如果 *uinit ≥ usat,vap (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 `0`。 - 将 **Initial vapor specific internal energy** 参数的值设置为 *uinit*。 - 如果 *usat,liq (pinit) < uinit < usat,vap (pinit)*： - 将 **Initial liquid mass fraction** 参数的值设置为 uinit−usat,liq(pinit)usat,vap(pinit)−usat,liq(pinit)。 - 将 **Initial liquid specific internal energy** 参数的值设置为 *usat,liq (pinit)*。 - 将 **Initial vapor specific internal energy** 参数的值设置为 *usat,vap (pinit)*。 |

## 描述

具有可变比例液体和蒸气体积的储罐

Receiver-Accumulator (2P) 模块表示一个流体可发生相变的储罐。液相和蒸气相（称为*区域*）被建模为在仿真期间尺寸可以变化但不会混合的独立体积。区域在系统中所占的相对空间量称为*区域分数*，其范围为 `0` 到 `1`。不建模蒸气-液体混合物相。

在 HVAC 系统中，当该储罐放置在冷凝器和膨胀阀之间时，它充当储液器。与模块的液体连接在端口 **AL** 和 **BL** 处进行。当储罐放置在蒸发器和压缩机之间时，它充当储液器。与模块的蒸气连接在端口 **AV** 和 **BV** 处进行。任一相的流体均可连接到任一端口，但从 V 端口流出的流体位于蒸气区域，从 L 端口流出的流体位于液体区域。未连接的端口没有质量流量。

储罐壁的温度在端口 **H** 处设置。

储罐的液位以端口 **L** 处的区域分数形式报告。如果液位报告为 `0`，则储罐完全充满蒸气。储罐永远不会为空。

### 传热

总传热量 *QH* 是液相和气相传热量之和：

QH=QL+QV。

传递给液体体积的传热量部分 *QL* 考虑了液体与壁面之间以及液体与蒸气之间的传热，

QL=(Sc+zLSs)αL(TH−TL)+ScαLV(TV−TL)

其中：

- *z*L 是储罐的液体体积分数。
- *S*c 是 **储罐横截面积** 参数。
- *S*s 是储罐侧表面积，模块根据体积和储罐横截面积计算该值，假设储罐为圆柱形。
- *α*L 是 **液体传热系数** 参数。
- *TH* 是储罐壁面的温度。
- *TL* 是液体的温度。

模块计算液体与蒸气之间的传热系数为

αLV=11αL+1αV。

传递给蒸气体积的传热量部分 *QV* 考虑了蒸气与壁面之间以及液体与蒸气之间的传热，

QV=(Sc+(1−zL)Ss)αV(TH−TV)+ScαLV(TL−TV)，

其中：

- *α*V 是 **蒸气传热系数**。
- *TV* 是蒸气的温度。

液体体积分数由液体质量分数确定：

zL=fM,LνLfM,LνL+(1−fM,L)νV，

其中：

- *fM,L* 是液体的质量分数。
- *νL* 是液体的比体积。
- *νV* 是蒸气的比体积。

### 相变引起的能量流率

当液体比焓大于或等于饱和液体比焓时，汽化流体的质量流率为：

m˙Vap=ML(hL−hL,Sat)/(hV−hL,Sat)τ。

其中：

- *ML* 是液体总质量。
- *τ* 是 **汽化和冷凝时间常数** 参数。
- *hL* 是内部节点处液体的比焓。
- *hL,Sat* 是内部节点处的饱和液体比焓。
- *hV* 是蒸气的比焓。
- *hV,Sat* 是饱和蒸气比焓。

与汽化相关的能量流为：

ϕVap=m˙VaphV,Sat，

当液体比焓低于饱和液体比焓时，不发生汽化，且 *ṁVap = 0*。

类似地，当蒸气比焓小于或等于饱和蒸气比焓时，冷凝流体的质量流率为：

m˙Con=MV(hV−hV,Sat)/(hV−hL,Sat)τ。

其中 *MV* 是蒸气总质量。

与冷凝相关的能量流为：

ϕCon=m˙ConhL,Sat，

当蒸气比焓高于饱和蒸气比焓时，不发生冷凝，且 *ṁCon = 0*。

### 质量平衡

储罐总体积恒定。由于相变，流体的体积分数和质量会发生变化。液体区域的质量平衡为：

dMLdt=m˙L,In−m˙L,Out+m˙Con−m˙Vap，

其中：

- m˙L,In 是所有 L 和 V 端口处的入口液体质量流率。
- m˙L,Out 是出口液体质量流率：

  m˙L,Out=−(m˙AL+m˙BL)，
- m˙Con 是冷凝流体的质量流率。
- m˙Vap 是汽化流体的质量流率。

蒸气区域的质量平衡为：

dMVdt=m˙V,In−m˙V,Out−m˙Con+m˙Vap，

其中：

- *MV* 是蒸气总质量。
- m˙V,In 是所有 L 和 V 端口处的入口蒸气质量流率。
- m˙V,Out 是出口蒸气质量流率：

  m˙V,Out=−(m˙AV+m˙BV)。

如果储罐中仅存在一个区域，则流体的出口质量流率为所有端口流率之和：

m˙phase,Out=−(m˙AL+m˙BL+m˙AV+m˙BV)。

其中 m˙phase,Out 在流体完全为液体时为 m˙L,Out，在流体完全为蒸气时为 m˙V,Out。

### 能量平衡

流体可以根据储罐与壁面之间的传热进行加热或冷却，该传热由端口 **H** 处的温度设定。

液体区域的能量平衡为：

MLduLdt+dMLdtuL=ϕL,In−ϕL,Out+ϕCon−ϕVap+QL。

其中：

- *uL* 是液体的比内能。
- *ϕL,In* 是所有 L 和 V 端口处的入口液体能量流率。
- *ϕL,Out* 是出口液体能量流率：

  ϕL,Out=−(ϕAL+ϕBL)。
- *ϕCon* 是冷凝蒸气的能量流率。
- *ϕVap* 是汽化液体的能量流率。
- *QL* 是储罐壁面与液体之间的传热。

蒸气区域的能量平衡为：

MVduVdt+dMVdtuV=ϕV,In−ϕV,Out−ϕCon+ϕVap+QV。

- *uV* 是蒸气的比内能。
- *ϕV,In* 是所有 L 和 V 端口处的入口蒸气能量流率。
- *ϕV,Out* 是出口蒸气能量流率：

  ϕV,Out=−(ϕAV+ϕBV)。
- *QV* 是储罐壁面与蒸气之间的传热。

如果储罐中仅存在一个区域，则出口能量流率为所有端口流率之和：

ϕphase,Out=−(ϕAL+ϕBL+ϕAV+ϕBV)。

其中 *ϕphase,Out* 在流体完全为液体时为 *ϕL,Out*，在流体完全为蒸气时为 *ϕV,Out*。

### 动量平衡

储罐中不建模任何压力变化，包括静水压力。任何端口处的压力等于储罐内部压力。

Receiver Accumulator 模块分别对蒸气和液体体积进行建模。如果快速输入蒸气或液体，模块可能会压缩蒸气体积，压力可能会比预期上升得更快。压力上升是因为当存在高蒸气或液体质量流率输入时，压缩导致的温升比冷却蒸气的传热更快。如果缓慢添加蒸气，蒸气与液体之间的传热会降低蒸气温度，使其能够冷凝为液体，压力就不会出现尖峰。此外，如果等到模块达到平衡，添加蒸气或液体会改变质量分数，不会引起压力尖峰。

### 假设和限制

- 压力必须保持低于临界压力。
- 不建模静水压力。
- 容器壁面为刚性，因此流体的总体积恒定。
- 不建模储罐壁面的热质量。
- 不建模通过出口的流动阻力。要对与出口相关的压力损失进行建模，请将 Local Restriction (2P) 模块或 Flow Resistance (2P) 模块连接到 Receiver-Accumulator (2P) 模块的端口。
- 不建模液-气混合物。
