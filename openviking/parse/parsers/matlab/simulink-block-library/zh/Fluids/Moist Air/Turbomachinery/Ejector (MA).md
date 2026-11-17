---
type: simulink-block
title: 'Ejector (MA)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 一次入口湿空气
  direction: conserving
- name: B
  summary: 出口湿空气
  direction: conserving
- name: S
  summary: 二次入口湿空气
  direction: conserving
```

### 守恒端口

### **A** — 一次入口湿空气

与一次喷嘴入口关联的湿空气守恒端口。

### **B** — 出口湿空气

与扩压器出口关联的湿空气守恒端口。

### **S** — 二次入口湿空气

与二次入口关联的湿空气守恒端口。
## 参数
```yaml
parameters:
- name: Primary nozzle throat area
  summary: 一次喷嘴喉部面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Area ratio of nozzle exit to throat
  summary: 喷嘴出口与喉部面积比 3（默认）| 正标量
  group: ''
- name: Area ratio of mixing chamber to throat
  summary: 混合室与喉部面积比 8（默认）| 正标量
  group: ''
- name: Minimum area ratio of secondary throat to primary throat
  summary: 二次喉部与一次喉部气动面积比的下限 0.1（默认）| 正标量
  group: ''
- name: Report when secondary throat area falls below minimum
  summary: 二次喉部面积低于最小值时的通知方式 Warning（默认）| None | Error
  group: ''
- name: Efficiency for primary flow through nozzle
  summary: 一次流通过喷嘴的效率因子 0.95（默认）| 正标量
  group: ''
- name: Efficiency for secondary suction flow
  summary: 二次引射流的效率因子 0.85（默认）| 正标量
  group: ''
- name: Efficiency for primary flow expansion
  summary: 一次流膨胀的效率因子 0.88（默认）| 正标量
  group: ''
- name: Efficiency for mixing
  summary: 混合导致的混合流速度效率因子 0.84（默认）| 正标量
  group: ''
- name: Cross-sectional area at port A
  summary: 端口 A 的横截面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at port B
  summary: 端口 B 的横截面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at port S
  summary: 端口 S 的横截面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Primary nozzle throat area** — 一次喷嘴喉部面积 `1e-4` `m^2`（默认）| 正标量

一次流喷嘴的喉部面积。

### **Area ratio of nozzle exit to throat** — 喷嘴出口与喉部面积比 `3`（默认）| 正标量

喷嘴出口面积与喷嘴喉部面积之比。该参数限制了二次气动喉部可以达到的最大尺寸。

### **Area ratio of mixing chamber to throat** — 混合室与喉部面积比 `8`（默认）| 正标量

混合室面积与喉部面积之比。混合室面积与一次流膨胀射流面积之间的差值形成了二次流的虚拟气动喉部。

### **Minimum area ratio of secondary throat to primary throat** — 二次喉部与一次喉部气动面积比的下限 `0.1`（默认）| 正标量

二次喉部与一次喉部的最小气动面积比。该模块不允许虚拟气动喉部的面积低于此值。为避免触及此最小值，请增大 **Area ratio of mixing chamber to throat** 参数的值。

### **Report when secondary throat area falls below minimum** — 二次喉部面积低于最小值时的通知方式 `Warning`（默认）| `None` | `Error`

当二次喉部面积低于 **Minimum area ratio of secondary throat to primary throat** 参数指定的最小值时，模块是不执行任何操作、生成警告还是生成错误。

### **Efficiency for primary flow through nozzle** — 一次流通过喷嘴的效率因子 `0.95`（默认）| 正标量

经验因子，用于修正因一次喷嘴中的损失而导致的一次质量流率降低。

### **Efficiency for secondary suction flow** — 二次引射流的效率因子 `0.85`（默认）| 正标量

经验因子，用于修正因二次流引射中的损失而导致的二次质量流率降低。

### **Efficiency for primary flow expansion** — 一次流膨胀的效率因子 `0.88`（默认）| 正标量

经验因子，用于修正因混合损失而导致的一次流射流膨胀的降低。

### **Efficiency for mixing** — 混合导致的混合流速度效率因子 `0.84`（默认）| 正标量

经验因子，用于修正因混合室中的损失而导致的混合流速度降低。

### **Cross-sectional area at port A** — 端口 A 的横截面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Cross-sectional area at port B** — 端口 B 的横截面积 `0.01` `m^2`（默认）| 正标量

端口 **B** 的横截面积。

### **Cross-sectional area at port S** — 端口 S 的横截面积 `0.01` `m^2`（默认）| 正标量

端口 **S** 的横截面积。
## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的喷射器

Ejector (MA) 模块对湿空气网络中的喷射器进行建模。喷射器迫使高压一次流通过具有特定喉部面积的喷嘴，从而产生低压射流，引射二次流。一次射流的膨胀为二次流形成了一个喉部。该模块假设两股流在均匀压力下混合，混合后的流通过扩压器排出以恢复压力。一次流和二次流必须包含相同的湿空气组分，但可以具有不同的组成。

您可以将喷射器用作泵或压缩机来驱动二次流体。与泵或压缩机不同，喷射器没有外部机械能源，高压一次流体是驱动二次流体的能量来源。

### 喷射器几何结构

高压一次流在位置 p 处进入喷射器，并流过喉部面积为 *Spt* 的收敛-扩张喷嘴，该面积为 **Primary nozzle throat area** 参数的值。喷射器在喉部（位置 pt）处对一次流进行壅塞，并将流加速为一次喷嘴出口（位置 pn）处的低压超声速射流。超声速一次流射流的低压在位置 s 处围绕喷嘴引射二次流。

超声速一次流射流在离开喷嘴后继续膨胀并降低压力，直到在膨胀一次流射流（位置 pe）处达到其最大面积。超声速一次流射流的膨胀在位置 st 处为二次流形成了一个虚拟气动喉部，该位置与 pe 相同。二次流也在气动喉部处壅塞。通过气动喉部后，一次流和二次流在均匀压力下混合（位置 m）。如果混合流仍为超声速，则流动会在混合室中的位置 s 处产生激波，扩压器（位置 d）使混合流减速以提高出口压力。

该示意图描述了喷射器，其中：

- 位置 p 是一次入口。
- 位置 s 是二次入口。
- 位置 pt 是一次喷嘴喉部。
- 位置 pn 是一次喷嘴出口。
- 位置 pe 是膨胀一次流射流。
- 位置 st 是二次气动喉部。
- 位置 m 是混合流。
- 位置 ms 是混合室中的激波。
- 位置 d 是扩压器出口。

喷射器示意图，显示了一次流和二次流、入口、喉部、混合和激波的位置。

### 质量流率

喷射器使一次湿空气流通过喷嘴加速。一次流的质量流率为

m˙p=Spt(2γγ−1)ηpppρp[(pmpp)2γ−(pmpp)γ+1γ],

其中：

- *Spt* 是 **Primary nozzle throat area** 参数的值。
- γ=cpcv 是热容比，其中 *cp* 是定压比热，*cv* 是定容比热。
- *ηp* 是 **Efficiency for primary flow through nozzle** 参数的值。
- *pp* 是一次流入口处的压力。
- *pm* 是一次流和二次流混合后的压力。
- *ρp* 是一次流入口处的密度。

一次流将二次湿空气流引入吸入室，并使其朝膨胀一次射流形成的虚拟气动喉部加速。二次流的质量流率为

m˙s=Sst(2γγ−1)ηspsρs[(pmps)2γ−(pmps)γ+1γ],

其中：

- *Sst* 是虚拟气动喉部的面积。该模块根据一次流射流的膨胀计算该值。
- *ηs* 是 **Efficiency for secondary suction flow** 参数的值。
- *ps* 是二次流入口处的压力。
- *ρs* 是二次流入口处的密度。

当 pmpp<Bcrit 时，其中 Bcrit=(2γ+1)γγ−1，一次流发生壅塞，质量流率达到最大值

m˙p\*=Sptηpppρpγ(2γ+1)γ+1γ−1。

当 pmps<Bcrit 时，二次流发生壅塞，质量流率达到最大值

m˙s\*=Sstηspsρsγ(2γ+1)γ+1γ−1。

### 一次流与二次流关系

超声速一次流射流的流通面积膨胀由以下关系式给出

SpeSpt=Ψpe(γ−12)(2γ+1)γ+1γ−1(pmpp)2γ−(pmpp)γ+1γ,

其中 *ψpe* 是 **Efficiency for primary flow expansion** 参数的值。

该模块使用膨胀超声速一次流射流的面积 *Spe* 来计算虚拟二次流气动喉部的流通面积 *Sst*

SstSpt=SmSpt−max{SpeSpt,SpmSpt},

其中：

- SmSpt 是 **Area ratio of mixing chamber to throat** 参数的值。
- SpnSpt 是 **Area ratio of nozzle exit to throat** 参数的值。

膨胀射流的一次流速度为

vpe=2γγ−1(ppρp)[1−(pmpp)γ−1γ]。

气动喉部处的二次流速度为

vst=2γγ−1(psρs)[1−(pmps)γ−1γ]。

二次流速度受限于壅塞值。当 pmps<Bcrit 时，二次流达到最大值

vst\*=2γγ+1(psρs)。

### 混合模型

在虚拟气动喉部之后，一次流和二次流在均匀压力下混合。混合流温度为

Tm=m˙pTp+m˙sTsm˙m−γ−12γRvm2,

其中：

- *Tp* 是一次流入口温度。该模块假设此值等于一次流滞止温度，因为入口处的动能相对于喷射器内部而言可以忽略不计。
- *Tm* 是混合流温度。
- *Ts* 是二次流入口温度。该模块假设此值等于二次流滞止温度，因为入口处的动能相对于喷射器内部而言可以忽略不计。
- *R* 是比气体常数。
- *vm* 是一次流和二次流混合后的流速。
- m˙m 是一次流和二次流混合后的质量流率，即 m˙m=m˙p+m˙s。

混合区域中的动量平衡为

pmSm+m˙mvm=pmSpe+m˙pvpe+pmSst+m˙svst,

其中 *Sm* 是一次流和二次流混合后的横截面积。

由于均匀压力混合假设，压力项相互抵消，混合流速度为

vm=ψmm˙pvpe+m˙svstm˙m,

其中 *ψm* 是 **Efficiency for mixing** 参数的值。

混合流马赫数为

Mm=vmγRTm。

### 混合扩压器流动关系

如果混合后流动为超声速，即 *MM* > 1，则会产生激波。激波后的压力升高为

pmspm=1+2γγ+1(Mm2−1),

其中 *Mm* 是一次流和二次流混合后的马赫数。

激波后的马赫数为

Mms2=γ−1γ+1(Mm2−1)+12γγ+1(Mm2−1)+1。

激波后，扩压器使流动减速以提高压力。该模块假设扩压器出口处的动能可以忽略不计，并将流动减速至 *pd* 处的滞止压力：

pdpms=(1+γ−12Mms2)γγ−1。

如果 *MM* ≤ 1，则没有激波，且

pmspm=1Mms2=Mm2。

混合压力 *pm* 与扩压器出口压力 *pd* 之间的关系为

pdpm={[γ+12Mm2]γγ−1[2γγ+1(Mm2−1)+1]1γ−1,Mm>1(1+γ−12Mm2)γγ−1,Mm≤1

### 临界模式运行

在正常运行中，一次流为高压并在运行期间发生壅塞。当二次流发生壅塞时，该模块也可以运行。如果一次流和二次流均发生壅塞，则该模块在临界模式下运行。

临界混合压力 *pm\** 是导致一次流和二次流均发生壅塞的低压阈值：

pm\*=min{pp,ps}(2γ+1)γγ−1。

该模块使用与上述相同的方程，将 *pm* 替换为 *pm\**，来计算临界扩压器出口压力 *pd\**。如果实际出口压力大于临界扩压器出口压力，则喷射器处于亚临界状态，该模块将混合压力与扩压器出口压力关联。如果实际出口压力小于临界扩压器出口压力，则喷射器处于临界状态，该模块将混合压力限制为临界混合压力。这意味着：

pm={pd(pdpm)pd≥pd\*pm\*pd<pd\*

### 假设与限制

- 该模块使用等熵理想气体关系式推导模型方程。
- 该模块使用经验损失系数来考虑摩擦、混合以及喷嘴出口处的膨胀波和激波造成的损失。
- 在一次流离开喷嘴后，直到一次流完全膨胀之前，两股流不会混合。
- 膨胀后，两股流在均匀压力下混合。
- 与喷射器内部流动的动能相比，一次流入口、二次流入口和扩压器出口处的动能可以忽略不计。
- 流动为稳态且一维。
- 流动为绝热。
- 存在反向流动时，模型结果可能不准确。
