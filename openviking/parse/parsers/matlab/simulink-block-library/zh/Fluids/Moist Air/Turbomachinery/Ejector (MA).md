---
type: simulink-block
title: 'Ejector (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'ejectorma'
documentation_source_path: 'ref/ejectorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Ejector (MA)

## 端口

### 守恒

### **A** — 主流入口湿空气

与主喷嘴入口关联的湿空气守恒端口。

### **B** — 出口湿空气

与扩压器出口关联的湿空气守恒端口。

### **S** — 二次流入口湿空气

与二次流入口关联的湿空气守恒端口。

## 参数

### **Primary nozzle throat area** — 主流喷嘴喉部的面积 `1e-4` `m^2` (默认) | positive scalar

主流喷嘴的喉部面积。

### **Area ratio of nozzle exit to throat** — 喷嘴出口面积与喷嘴喉部面积之比 `3` (默认) | positive scalar

喷嘴出口面积与喷嘴喉部面积之比。此参数限制二次气动喉部可以有多大。

### **Area ratio of mixing chamber to throat** — 混合室面积与喉部面积之比 `8` (默认) | positive scalar

混合室面积与喉部面积之比。混合室面积与主流膨胀射流面积之间的差值为二次流形成虚拟气动喉部。

### **Minimum area ratio of secondary throat to primary throat** — 二次喉部与一次喉部的气动面积比下限 `0.1` (默认) | positive scalar

二次喉部与一次喉部的最小气动面积比。该模块不允许虚拟气动喉部的面积低于此值。为避免达到该最小值，请增大 **Area ratio of mixing chamber to throat** 参数的值。

### **Report when secondary throat area falls below minimum** — 当二次喉部面积低于最小值时的通知 `Warning` (默认) | `None` | `Error`

当二次喉部面积低于由 **Minimum area ratio of secondary throat to primary throat** 参数指定的最小值时，该模块是不执行任何操作、生成警告还是生成错误。

### **Efficiency for primary flow through nozzle** — 主流通过喷嘴的效率因子 `0.95` (默认) | positive scalar

用于考虑由于主喷嘴中的损失导致主流质量流量减少的经验因子。

### **Efficiency for secondary suction flow** — 二次抽吸流的效率因子 `0.85` (默认) | positive scalar

用于考虑由于二次流抽吸中的损失导致二次流质量流量减少的经验因子。

### **Efficiency for primary flow expansion** — 主流膨胀的效率因子 `0.88` (默认) | positive scalar

用于考虑由于混合损失导致主流射流膨胀减少的经验因子。

### **Efficiency for mixing** — 混合导致的混合流速度的效率因子 `0.84` (默认) | positive scalar

用于考虑由于混合室中的损失导致混合流速度降低的经验因子。

### **Cross-sectional area at port A** — 端口 A 的横截面积 `0.01` `m^2` (默认) | positive scalar

端口 **A** 的横截面积。

### **Cross-sectional area at port B** — 端口 B 的横截面积 `0.01` `m^2` (默认) | positive scalar

端口 **B** 的横截面积。

### **Cross-sectional area at port S** — 端口 S 的横截面积 `0.01` `m^2` (默认) | positive scalar

端口 **S** 的横截面积。

## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的喷射器

Ejector (MA) 模块对湿空气网络中的喷射器进行建模。喷射器迫使高压主流通过具有特定喉部面积的喷嘴，从而产生低压射流并吸入二次流。主流射流的膨胀为二次流形成喉部。该模块假设两股流动在均匀压力下混合，并且合并后的流动通过扩压器排出以恢复压力。主流和二次流必须包含相同的湿空气组分，但可以具有不同的组成。

您可以将喷射器用作泵或压缩机来驱动二次流体。与泵或压缩机不同，没有外部机械能来源，高压主流体是驱动二次流体的能量来源。

### 喷射器几何结构

高压主流在位置 p 进入喷射器，并流经喉部面积为 *Spt* 的收敛-扩张喷嘴，该面积是 **Primary nozzle throat area** 参数的值。喷射器在喉部（位置 pt）使主流壅塞，并将流动加速为主喷嘴出口（位置 pn）处的低压超声速射流。超声速主流射流的低压在喷嘴周围的位置 s 吸入二次流。

超声速主流射流在离开喷嘴出口后继续膨胀并降压，直到在膨胀后的主流射流（位置 pe）处达到最大面积。超声速主流射流的膨胀在位置 st 为二次流形成虚拟气动喉部，该位置与 pe 相同。二次流也在该气动喉部处壅塞。通过气动喉部后，主流和二次流在均匀压力下混合（位置 m）。如果混合流仍为超声速，则流动会在位置 s 的混合室中引起激波，并且扩压器（位置 d）使混合流减速以提高出口压力。

此示意图描述了该喷射器，其中：

- 位置 p 是主流入口。
- 位置 s 是二次流入口。
- 位置 pt 是主喷嘴喉部。
- 位置 pn 是主喷嘴出口。
- 位置 pe 是膨胀后的主流射流。
- 位置 st 是二次流气动喉部。
- 位置 m 是混合流。
- 位置 ms 是混合室中的激波。
- 位置 d 是扩压器出口。

显示主流和二次流、入口、喉部、混合和激波位置的喷射器示意图。

### 质量流量

喷射器使主流湿空气通过喷嘴加速。主流的质量流量为

m˙p=Spt(2γγ−1)ηpppρp[(pmpp)2γ−(pmpp)γ+1γ],

其中：

- *Spt* 是 **Primary nozzle throat area** 参数的值。
- γ=cpcv 是热容比，其中 *cp* 是定压比热容，*cv* 是定容比热容。
- *ηp* 是 **Efficiency for primary flow through nozzle** 参数的值。
- *pp* 是主流入口处的压力。
- *pm* 是主流和二次流混合后的压力。
- *ρp* 是主流入口处的密度。

主流将二次湿空气流吸入抽吸室，并将其加速至由膨胀的主流射流形成的虚拟气动喉部。二次流的质量流量为

m˙s=Sst(2γγ−1)ηspsρs[(pmps)2γ−(pmps)γ+1γ],

其中：

- *Sst* 是虚拟气动喉部的面积。该模块根据主流射流的膨胀计算该值。
- *ηs* 是 **Efficiency for secondary suction flow** 参数的值。
- *ps* 是二次流入口处的压力。
- *ρs* 是二次流入口处的密度。

当 pmpp<Bcrit，其中 Bcrit=(2γ+1)γγ−1，时，主流发生壅塞，质量流量达到最大值

m˙p\*=Sptηpppρpγ(2γ+1)γ+1γ−1.

当 pmps<Bcrit 时，二次流发生壅塞，质量流量达到最大值

m˙s\*=Sstηspsρsγ(2γ+1)γ+1γ−1.

### 主流和二次流关系

超声速主流射流的流通面积膨胀由以下关系给出

SpeSpt=Ψpe(γ−12)(2γ+1)γ+1γ−1(pmpp)2γ−(pmpp)γ+1γ,

其中 *ψpe* 是 **Efficiency for primary flow expansion** 参数的值。

该模块使用膨胀后的超声速主流射流的面积 *Spe* 来计算二次流虚拟气动喉部的流通面积 *Sst*

SstSpt=SmSpt−max{SpeSpt,SpmSpt},

其中：

- SmSpt 是 **Area ratio of mixing chamber to throat** 参数的值。
- SpnSpt 是 **Area ratio of nozzle exit to throat** 参数的值。

膨胀射流的主流速度为

vpe=2γγ−1(ppρp)[1−(pmpp)γ−1γ].

气动喉部处的二次流速度为

vst=2γγ−1(psρs)[1−(pmps)γ−1γ].

二次流速度受限于壅塞值。当 pmps<Bcrit 时，二次流达到最大值

vst\*=2γγ+1(psρs).

### 混合模型

在虚拟气动喉部之后，主流和二次流在均匀压力下混合。混合流温度为

Tm=m˙pTp+m˙sTsm˙m−γ−12γRvm2,

其中：

- *Tp* 是主流入口温度。该模块假设该值等于主流滞止温度，因为入口处的动能相对于喷射器内部可忽略不计。
- *Tm* 是混合流温度。
- *Ts* 是二次流入口温度。该模块假设该值等于二次流滞止温度，因为入口处的动能相对于喷射器内部可忽略不计。
- *R* 是比气体常数。
- *vm* 是主流和二次流混合后的流速。
- m˙m 是主流和二次流混合后的质量流量，即 m˙m=m˙p+m˙s。

混合区域中的动量平衡为

pmSm+m˙mvm=pmSpe+m˙pvpe+pmSst+m˙svst,

其中 *Sm* 是主流和二次流混合后的横截面积。

由于均匀压力混合假设，压力项消去，混合流速度为

vm=ψmm˙pvpe+m˙svstm˙m,

其中 *ψm* 是 **Efficiency for mixing** 参数的值。

混合流马赫数为

Mm=vmγRTm.

### 混合扩压器流动关系

如果混合后流动为超声速，即 *MM* > 1，则发生激波。激波后的压力升高为

pmspm=1+2γγ+1(Mm2−1),

其中 *Mm* 是主流和二次流混合后的马赫数。

激波后的马赫数为

Mms2=γ−1γ+1(Mm2−1)+12γγ+1(Mm2−1)+1.

激波后，扩压器使流动减速以提高压力。该模块假设扩压器出口处的动能可忽略不计，并将流动减速至 *pd* 处的滞止压力：

pdpms=(1+γ−12Mms2)γγ−1.

如果 *MM* ≤ 1，则没有激波，并且

pmspm=1Mms2=Mm2.

混合压力 *pm* 与扩压器出口压力 *pd* 之间的关系为

pdpm={[γ+12Mm2]γγ−1[2γγ+1(Mm2−1)+1]1γ−1,Mm>1(1+γ−12Mm2)γγ−1,Mm≤1

### 临界模式运行

在正常运行中，主流为高压，并在运行期间壅塞。如果二次流壅塞，该模块也可以运行。如果主流和二次流均壅塞，则该模块在临界模式下运行。

临界混合压力 *pm\** 是导致主流和二次流均发生壅塞的低压阈值：

pm\*=min{pp,ps}(2γ+1)γγ−1.

该模块使用与上文相同的方程，并将 *pm* 替换为 *pm\**，以计算临界扩压器出口压力 *pd\**。如果实际出口压力大于临界扩压器出口压力，则喷射器为亚临界，该模块将混合压力与扩压器出口压力关联。如果实际出口压力小于临界扩压器出口压力，则喷射器为临界，该模块将混合压力限制为临界混合压力。这意味着：

pm={pd(pdpm)pd≥pd\*pm\*pd<pd\*

### 假设和限制

- 该模块使用等熵理想气体关系推导模型方程。
- 该模块使用经验损失系数来考虑由于摩擦、混合以及喷嘴出口处的膨胀波和激波造成的损失。
- 在主流离开喷嘴后，直到主流完全膨胀之前，两股流动不混合。
- 膨胀后，两股流动在均匀压力下混合。
- 与喷射器内部流动的动能相比，主流入口、二次流入口和扩压器出口处的动能可忽略不计。
- 流动为稳态且一维。
- 流动为绝热。
- 存在反向流时，模型结果可能不准确。
