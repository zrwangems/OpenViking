---
type: simulink-block
title: 'Thyristor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'thyristor'
documentation_source_path: 'ref/thyristor.html'
language: zh-CN
chinese_source: worker-translation
---

# Thyristor

## 端口

### 守恒

### **G** — 栅极端口（电气）

与栅极关联的电气守恒端口。

### **A** — 阳极端口（电气）

与阳极关联的电气守恒端口。

### **K** — 阴极端口（电气）

与阴极关联的电气守恒端口。

### **H** — 热端口（热）

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并模拟生成热量和器件温度的影响。

### 主要

### **I-V characteristics defined by** — 晶闸管表示形式 `Fundamental nonlinear equations`（默认） | `Lookup table`

使用基于 NPN 和 PNP 双极晶体管的等效电路表示晶闸管，或使用通态 I-V 曲线的查找表近似表示晶闸管。

### **On-state voltage, V\_T** — 通态阳极-阴极静态电压 `1.2` `V`（默认）

通态时的阳极-阴极静态电压降，此时流过的电流等于通态电流 *IT*。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **On-state current, I\_T** — 通态静态负载电流 `1` `A`（默认）

当阳极-阴极电压等于通态电压 *VT* 时流过的静态负载（或等效阳极）电流。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **Vector of on-state voltages, V\_T** — 通态电压向量 `[.75, 1, 1.25, 1.5, 1.75, 2, 2.25]` `V`（默认）

用于表查找的通态电压向量。向量值必须严格递增，且第一个值必须大于零。这些值可以非均匀间隔。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### **Vector of corresponding currents, I\_T** — 对应电流向量 `[.015, .22, .75, 1.4, 2, 2.75, 3.45]` `A`（默认）

与通态电压向量值对应的电流向量，用于一维表查找。两个向量的大小必须相同。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### **Off-state current, I\_DRM** — 断态阳极电流 `0.01` `mA`（默认）

当阳极-阴极电压等于断态电压 *VDRM* 时流过的断态阳极电流 *IDRM*。

### **Corresponding off-state voltage, V\_DRM** — 断态阳极-阴极电压 `400` `V`（默认）

在给出断态电流 *IDRM* 时，晶闸管处于断态所施加的阳极-阴极电压 *VDRM*。

### **Holding current** — 维持电流 `1` `mA`（默认）

这是晶闸管保持通态所需的最小电流。对于 Lookup table 选项，闩锁电流假定等于维持电流，因此这也是晶闸管保持断态的最大电流。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### **Measurement temperature** — 器件仿真温度 `25` `degC`（默认）

器件仿真温度。必须为该温度指定所有模块参数值。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### 栅极触发

### **Gate trigger current, I\_GT** — 临界栅极电流 `3` `uA`（默认）

使晶体管导通所需的临界栅极电流 *iGT*，此时栅极电压等于对应的栅极电压 *vGT*。必须设置 **高级** 选项卡上的 **Internal shunt resistor, Rs** 参数值，以确保栅极在 *iGT* 时触发，而不是在小于 *iGT* 的电流时触发。

### **Corresponding gate voltage, V\_GT** — 栅极-阴极电压 `0.6` `V`（默认）

当栅极电流等于栅极触发电流 *iGT* 时的栅极-阴极电压 *vGT*。

### **Test voltage, V\_D** — 测试电源电压 `12` `V`（默认）

给出 *vGT* 和 *iGT* 值时使用的电源电压。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **Test load resistor** — 测试负载电阻 `120` `Ohm`（默认）

给出 *vGT* 和 *iGT* 值时使用的负载电阻。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### dV/dt 触发

### **Critical rate of rise of off-state voltage, dV/dt** — 断态电压临界上升率 `150` `V/us`（默认）

如果阳极-阴极电压上升快于该速率，晶闸管将由于电容效应而发生寄生导通。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **Test gate-cathode resistor, R\_GK** — 测试栅极-阴极电阻 `1000` `Ohm`（默认）

给出断态电压临界上升率时使用的栅极-阴极电阻。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### 时间常数

### **NPN device forward transit time parameterization** — NPN 器件正向渡越时间参数化 `Derive approximate value from gate-controlled turn-on time`（默认） | `Specify directly`

选择以下选项之一：

- `Derive approximate value from gate-controlled turn-on time` — 模块根据您指定的栅极控制导通时间和对应栅极电流值计算 NPN 器件正向渡越时间。
- `Specify directly` — 使用 **NPN device forward transit time** 参数直接提供该值。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **Gate-controlled turn-on time** — 栅极控制导通时间 `2` `us`（默认）

施加栅极电流时，栅极从断态转到通态所需的时间。

### **Corresponding gate current** — 测试栅极电流 `10` `mA`（默认）

给出栅极控制导通时间时使用的栅极电流。假定所有输入电荷都用于将栅极电压升高到对应的栅极电压 *vGT*，则使用该栅极电流和导通时间计算 NPN 器件正向渡越时间的近似值。默认值为 `10` mA。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations`，并且为 **NPN device forward transit time parameterization** 选择 `Derive approximate value from gate-controlled turn-on time` 时，此参数才可见。

### **NPN device forward transit time** — 平均正向渡越时间 `0.3` `us`（默认）

少数载流子从 NPN 器件的发射极穿过基区到达集电极的平均时间 [1]。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations`，并且为 **NPN device forward transit time parameterization** 选择 `Specify directly` 时，此参数才可见。

### **PNP device forward transit time parameterization** — PNP 器件正向渡越时间参数化 `Set equal to NPN device forward transit time`（默认） | `Specify directly`

选择以下选项之一：

- `Set equal to NPN device forward transit time` — 模块使用 NPN 器件正向渡越时间值。
- `Specify directly` — 使用 **PNP device forward transit time** 参数直接提供该值。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **PNP device forward transit time** — 平均正向渡越时间 `0.3` `us`（默认）

少数载流子从 PNP 器件的发射极穿过基区到达集电极的平均时间 [1]。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations`，并且为 **PNP device forward transit time parameterization** 选择 `Specify directly` 时，此参数才可见。

### **Turn-on delay time** — 时间延迟 `0` `s`（默认）

在栅极电流从零阶跃到 **Gate current for turn-on delay time** 参数指定的值后，器件开始导通之前的时间延迟。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### **Gate current for turn-on delay time** — 导通延迟时间用栅极电流 `1` `mA`（默认）

测量导通延迟时间时使用的栅极电流。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### **Turn-on rise time** — 导通上升时间 `0` `s`（默认）

在导通延迟事件之后，晶闸管完全导通所需的时间。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Lookup table` 时，此参数才可见。

### 高级

### **Internal shunt resistor, Rs** — 栅极-阴极分流电阻 `87` `kOhm`（默认）

栅极-阴极分流电阻。设置此参数值以确保栅极在 *iGT* 时触发，而不是在小于 *iGT* 的电流时触发，这一点很重要。有关详细信息，请参阅 Thyristor Static Behavior Validation 示例。如果在存在外部栅极-阴极电阻 RGK 的电路中使用晶闸管，则通常 Rs 的影响很小，可将其设置为 `inf`。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

### **Internal series gate resistor, Rg** — 与栅极连接关联的电阻 `10` `Ohm`（默认）

与栅极连接关联的电阻。典型值为几欧姆量级，其对静态和动态特性的影响很小。因此，其精确值并不重要，但如果栅极直接由电压源驱动，它的存在有助于避免数值仿真问题。可以指定任何正值。

### **Product of NPN and PNP forward current gains** — NPN 和 PNP 正向电流增益的乘积 `10`（默认）

这是 NPN 正向增益 *BFNPN* 和 PNP 正向增益 *BFPNP* 的乘积。该值必须大于一才能发生闩锁。该值越小，闩锁电流越大。但是，闩锁电流主要由其他模块参数设定，总增益仅具有很小的影响。

#### 依赖关系

仅当为 **I-V characteristics defined by** 参数选择 `Fundamental nonlinear equations` 时，此参数才可见。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010b 中引入**

### R2019b：热网络 simlog 路径

从 R2019b 开始，可以在内部或外部对该模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您有一个以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

使用 NPN 和 PNP 晶体管的 Thyristor

Thyristor 模块提供两种晶闸管建模方式：

- 作为基于 NPN 和 PNP 双极晶体管的等效电路
- 通过通态 I-V（电流-电压）曲线的查找表近似

### 等效电路表示

等效电路包含一对 NPN 和 PNP 双极型晶体管，如下图所示。

晶闸管的 P-N-P-N 结构对应于双极型晶体管的 P-N-P 和 N-P-N 结构，每个器件的基极连接到另一个器件的集电极。为确保该电路表现得像晶闸管，必须选择 NPN 和 PNP 器件以及外部电阻的合适参数值。例如，为了使电路在被合适的栅极电流触发后锁存到通态，两个晶体管的总增益必须大于 1。该模型结构复现了晶闸管在典型应用电路中的行为，同时向求解器呈现最少数量的方程，以提高仿真速度。

**注意**

在模型中使用晶闸管组件之前，正确设置其参数极其重要。为帮助你完成此操作，Simscape™ Electrical™ 示例中有两个测试框架：Thyristor Static Behavior Validation 和 Thyristor Dynamic Behavior Validation。按照这两个示例的帮助文本以及你所使用器件的数据手册，重新设置晶闸管组件的参数，使其复现所需行为。然后，你可以将参数化后的组件复制到你的模型中。请注意正确建模栅极驱动电路，包括电路串联电阻。将受控电压源直接连接到晶闸管栅极会产生非物理结果，因为当栅极需求为零时，它会将栅极钳位到阴极电压。

该模型捕获以下晶闸管行为：

- 断态电流 *IDRM* 和 *IRRM*。这些电流通常针对最大断态电压 *VDRM* 和 *VRRM* 给出。假设 *IDRM* = *IRRM* 且 *VDRM* = *VRRM*，这与大多数晶闸管的情况相同。
- 当栅极电流等于 **栅极触发电流，I\_GT** 参数值时，栅极触发电压等于 **对应的栅极电压，V\_GT** 参数值。
- 当栅极电流等于 **栅极触发电流，I\_GT** 时，晶闸管锁存到通态。晶闸管在栅极电流达到该值之前不会锁存到通态。为确保如此，你必须正确设置 **内部分流电阻，Rs** 参数。如果该电阻过高，则栅极会在栅极电流达到 *iGT* 之前触发。如果该电阻过小，则栅极不会触发。

  你可以通过运行仿真来确定内部分流电阻 Rs 的值。要了解如何操作，请参阅 Thyristor Static Behavior Validation 示例。或者，如果你在电路中使用晶闸管，并且从栅极到阴极连接了一个外部电阻 RGK，则 Rs 的影响通常非常小，可以将其设置为 `inf`。
- 当晶闸管处于通态时，如果移除栅极电流，只要负载电流高于维持电流，晶闸管就保持在通态。你不直接指定维持电流，因为其值主要由其他模块参数决定。

  但是，维持电流可能受到 **高级** 选项卡上的 **NPN 和 PNP 正向电流增益的乘积** 参数影响。降低增益会增加维持电流。
- 当负载电流等于 **通态电流，I\_T** 参数值时，通态电压等于 **通态电压，V\_T** 参数值。这由 R\_on 电阻值确保，该值考虑了 PNP 和 NPN 器件上的电压降。
- 由断态电压上升率触发。阳极-阴极电压的快速变化会在基极-集电极电容项中感应出电流。如果该电流足够大，则会将晶闸管触发到通态。晶闸管初始化例程会计算基极-集电极电容的合适值，使得当电压变化率等于 **断态电压临界上升率，dV/dt** 参数值时，晶闸管触发导通。该计算基于这样的近似：所需电流为 *vGT* / *RGK*，其中 *RGK* 是引用临界 *dV/dt* 值时使用的栅极-阴极电阻值。
- 非零的栅控开通时间，主要受 **NPN 器件正向渡越时间，TF** 影响。你可以直接指定此参数，也可以根据开通时间计算 TF 的近似值。
- 非零的换向关断时间，主要受 **PNP 器件正向渡越时间，TF** 影响。你可以直接指定此参数，也可以将其设置为等于 NPN 晶体管的正向渡越时间。

电阻 Gmin1 和 Gmin2 提高了大正向和反向电压下的数值稳健性。在最大断态正向和反向电压下，它们的值对断态电流的影响不超过 1%。

**注意**

由于此模块实现包含电荷模型，你必须对驱动栅极的电路阻抗进行建模，以获得具有代表性的开通和关断动态。因此，如果你通过将栅极驱动电路表示为受控电压源来简化它，则必须在电压源和栅极之间包含一个合适的串联电阻。

### 查表表示

如果使用查表表示，你需要提供通态时阳极-阴极电流作为阳极-阴极电压函数的表格值。使用此选项的主要优点是仿真速度和参数化简便性。为了进一步简化底层模型，此表示不对以下内容建模：

- 由于断态电压上升率引起的器件触发
- 换向关断时间

开通延迟由输入栅极-阴极电容表示，其值经过计算，使得栅极电压上升与器件开始开通之间的延迟等于 **开通延迟时间** 参数指定的值。负载电流的开通上升时间通过在由 **开通上升时间** 参数值指定的时间段内，在零和由通态电流-电压曲线确定的电流之间进行非线性斜坡变化来实现。请注意，所得的开通电流曲线是对实际器件的近似。

### 热端口

你可以暴露热端口，以对产生的热量和器件温度的影响进行建模。要暴露热端口，请将 **建模选项** 参数设置为以下任一值：

- `No thermal port` — 该模块不包含热端口，也不仿真器件中的热量生成。
- `Show thermal port` — 该模块包含一个热端口，允许你对传导损耗产生的热量进行建模。出于数值效率考虑，热状态不会影响模块的电气行为。

有关使用热端口以及 **热端口** 参数的详细信息，请参阅《半导体中的热效应仿真》。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅《为模块变量设置优先级和初始目标》。

使用标称值指定模型中变量的预期量级。基于标称值使用系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅《按标称值进行系统缩放》。
