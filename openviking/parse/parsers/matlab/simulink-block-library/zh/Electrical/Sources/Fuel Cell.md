---
type: simulink-block
title: 'Fuel Cell'
family: 'sources'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fuelcell'
documentation_source_path: 'ref/fuelcell.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuel Cell

## 端口

### 输入

### **pfuel** — 燃料的供应绝对压力，bar 物理信号

与燃料的供应绝对压力关联的物理信号端口，单位为 `bar`，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **pair** — 空气的供应表压，bar 物理信号

与空气的供应表压关联的物理信号端口，单位为 `bar`，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **qfuel** — 燃料流量，l/min 物理信号

与燃料流量关联的物理信号端口，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **qair** — 空气流量，l/min 物理信号

与空气流量关联的物理信号端口，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### 守恒

### **+** — 正端子 电气

与燃料电池正端子关联的电气守恒端口。

### **-** — 负端子 电气

与燃料电池负端子关联的电气守恒端口。

### **H** — 热端口 热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

## 参数

### 主

### **Model fidelity** — 燃料电池保真度 `Detailed with physical inputs`（默认）| `Simplified - nominal conditions`

燃料电池模型的保真度级别。

### **Open-circuit voltage** — 开路电压 `65` `V`（默认）| 正标量

开路电压。

当流量非常低或接近零且燃料和空气压力值等于其标称值时，燃料电池的输出电压等于开路电压乘以模块单元数。流出燃料电池的电流可忽略不计。此图显示如何设置开路测试：

### **Tafel slope** — Tafel 斜率 `0.23` `V`（默认）| 正标量

使反应速率增加十倍所需的过电位量。

### **Internal resistance** — 内阻 `0.05` `Ohm`（默认）| 正标量

内阻。

### **Nominal exchange current** — 标称交换电流 `80` `A`（默认）| 正标量

标称温度下的交换电流。

在标称交换电流下，燃料电池离开活化极化区域并进入欧姆极化区域。

### **Collapse current** — 崩溃电流 `200` `A`（默认）| 正标量

燃料电池电压变为零时的电流值。当燃料电池进入浓差极化区域且电流继续增加时，电压开始以更快速率下降。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Number of cells per module** — 每模块电池数 `65`（默认）| 正标量

每模块的电池数。

此模块中的电池计数值与燃料电池在指定的流量和 H2 压力设定点下提供其最大输出功率一致。

### **Module units (Series)** — 串联模块单元堆栈 `10`（默认）| 正标量

串联的模块单元堆栈。

将模块串联堆叠以提升电压。例如，10 个开路电压为 65 V 的串联模块单元提供 650V 电压。

### 供应

要启用这些参数，请在 **Main** 选项卡中，将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Nominal H2 pressure** — 标称氢气压力 `1.5e5` `Pa`（默认）| 正标量

标称温度下的氢气表压。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Nominal O2 pressure** — 标称氧气压力 `1.0e5` `Pa`（默认）| 正标量

标称温度下的氧气表压。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Concentration H2 in fuel (%)** — 燃料中的氢气浓度 `99`（默认）| `0` 到 `100` 之间的整数

燃料中氢气的摩尔分数浓度，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Concentration O2 in air (%)** — 燃料中的氧气浓度 `21`（默认）| `0` 到 `100` 之间的整数

燃料中氧气的摩尔分数浓度，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Concentration vapor in air (%)** — 空气中的蒸气浓度 `1`（默认）| `0` 到 `100` 之间的整数

空气中蒸气的摩尔分数浓度，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### 动态

### **Model activation delay** — 激活延迟建模选项 `No`（默认）| `Yes`

是否对燃料电池的激活延迟建模。

### **Sum of activation and concentration resistance** — 活化电阻与浓差电阻之和 `0.005` `Ohm`（默认）| 正标量

活化电阻和浓差电阻之和。

#### 依赖关系

要启用此参数，请将 **Model activation delay** 设置为 `Yes`。

### **Time constant** — 时间常数 `10` `s`（默认）| 正标量

时间常数。

#### 依赖关系

要启用此参数，请将 **Model activation delay** 设置为 `Yes`。

### 热

要启用这些参数，请在 **Main** 选项卡中，将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Nominal temperature** — 标称温度 `293.15` `K`（默认）| 标量

测量标称参数时的温度。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

### **Thermal mass** — 与热端口 H 关联的热质量 `30000` `J/K`（默认）| 正标量

与热端口 **H** 关联的热质量。此值表示将热端口温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请将 **Model fidelity** 设置为 `Detailed with physical inputs`。

## 所属库

Simscape / Electrical / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

燃料电池电气系统

Fuel Cell 模块对将氢气的化学能转换为电能的燃料电池进行建模。

此化学反应定义电气转换：

H2+12O2→H2O+heat

其发生是由于以下阳极和阴极半反应：

H2→2H++2e−12O2+2H++2e−→H2O

燃料电池堆包括若干串联连接的燃料电池。此图显示此模块使用的单个燃料电池的等效电路

其中：

- *VFC* 是电池电压。
- *Ri* 是 **Internal resistance**。
- *Rd* 是 **Sum of activation and concentration resistances**。
- *Cdl* 是并联 RC 电容，用于考虑电池中的时间动态。

### 方程

您可以使用 **Model fidelity** 参数将 Fuel Cell 模块设置为两个不同的保真度级别：

- `Simplified - nominal conditions` — 模块在标称温度和压力条件下计算 Nernst 电压。
- `Detailed with physical inputs` — 模块通过考虑燃料和空气的压力和流量来计算 Nernst 电压。

**简化电气模型**

当 **Model fidelity** 设置为 `Simplified - nominal conditions` 时，Fuel Cell 模块在标称温度和压力条件下计算 Nernst 电压 *E*，由以下方程定义：

E=Eoc−NAln(iFCi0)vFC=NunitE−RiiFC−vd1Rd(τdvddt+vd)=iFC

其中：

- *Eoc* 是 **Open-circuit voltage**。
- *N* 是 **Number of cells per module**。
- *iFC* 是燃料电池生成的电流。
- *vFC* 是燃料电池端子两端的电压。
- *Nunit* 是 **Module units (Series)**。
- *vd* 是考虑燃料电池动态的电压降。
- *A* 是 **Tafel slope**，单位为 volts。
- *i0* 是 **Nominal exchange current**。
- τ=RdCdl。

**详细电气模型**

当 **Model fidelity** 设置为 `Detailed with physical inputs` 时，Fuel Cell 模块通过考虑燃料和空气的压力和流量来计算 Nernst 电压 *E*。

这些方程确定氢气利用率 *UH2* 和氧气利用率 *UO2*

UH2=60000NiFCVepfuelqfuelxH2UO2=60000NiFCVe2pairqairxO2

其中：

- *Ve* 是室温下的热电压。
- *pfuel* 是燃料的供应压力，单位为 `bar`。
- *qfuel* 是燃料流量。
- *xH2* 是燃料中氢气的浓度，以百分比表示。
- *pair* 是空气的供应压力，单位为 `bar`。
- *qair* 是空气流量。
- *xO2* 是空气中氧气的浓度，以百分比表示。

这些方程定义分压：

pH2=pfuelxH2−UH2pO2=pairxO2−UO2pH2O=pairxH2O−2UO2

其中 *xH2O* 是空气中蒸气的浓度，以百分比表示。

然后，模块计算 Nernst 电压为

其中：

- Kz=Eoc\_admKcN−1.229(Tnom−298)−44.43z0F+RTnomz0Fln(pnH2pnO212).
- ETafel=NATln(iFCi0) 是活化的电化学动力学项。
- Econc=VeT298ln(ilimilim−iFC) 是浓差的电化学动力学项。
- Eoc\_adm=max(Eoc,N(1.229+RTnom2Fln(pnH2pnO212))).
- *Kc* 是标称操作条件下的电压常数。
- *T* 是燃料电池的工作温度。
- *Tnom* 是 **Nominal temperature** 参数的值。
- *z* 是每秒移动电子数。
- *z0* 是 **Nominal exchange current** 参数值处每秒移动电子数。
- *F* 是法拉第常数。
- *R* 是通用气体常数。
- *pnH2* 是标称氢气压力，单位为 `bar`。
- *pnO2* 是标称氧气压力，单位为 `bar`。
- AT=ATln(10)∗298 是作为温度函数的 Tafel 斜率。
- *ilim* 是 **Collapse current** 参数的值。
- 电压 `1.229` 表示 Nernst 方程的标准电池电势。

模块使用以下方程计算燃料电池中耗散的功率或释放的热量

Pdissipated=Ze\_agg(TΔS)+RiiFC+vd21Rd

其中：

- Ze\_agg=(NunitE−RiiFC−vd)iFC2ΔG 是总电子循环速率，单位为 `mol/s`。
- *TΔS* 是燃料电池反应在燃料电池工作温度下的熵变，单位为 `kJ/(mol*K)`。
- *ΔG* 是完整燃料电池反应在燃料电池工作温度下的吉布斯自由能变化，单位为 `kJ/mol`。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
