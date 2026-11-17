---
type: simulink-block
title: 'FEM-Parameterized Synchronous Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'femparameterizedsynchronousmachine'
documentation_source_path: 'ref/femparameterizedsynchronousmachine.html'
language: zh-CN
chinese_source: worker-translation
---

# FEM-Parameterized Synchronous Machine

## 端口

### 守恒端口

### **~** — 三相复合电气

与定子绕组关联的可扩展三相端口。有关详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *A* 相电气

与 *A* 相关联的电气守恒端口
相。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *B* 相电气

与 *B* 相关联的电气守恒端口
相。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *C* 相电气

与 *C* 相关联的电气守恒端口
相。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端关联的可扩展三相端口
连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端关联的可扩展三相端口
连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 相关联的电气守恒端口
正端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 相关联的电气守恒端口
正端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 相关联的电气守恒端口
正端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 相关联的电气守恒端口
负端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 相关联的电气守恒端口
负端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 相关联的电气守恒端口
负端连接。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Wye-wound`，并选中 **Expose neutral port** 参数。

### **fd+** — 励磁绕组正极端子电气

与励磁绕组正极端子相关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子电气

与励磁绕组负极端子相关联的电气守恒端口。

### **R** — 电机转子机械旋转

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械旋转

与电机机壳相关联的机械旋转守恒端口。

### **HA** — 绕组 *A* 热端口热

与绕组 *A* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

### **HB** — 绕组 *B* 热端口热

与绕组 *B* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

### **HC** — 绕组 *C* 热端口热

与绕组 *C* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

### **HR** — 转子热端口热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

## 参数

### 磁通与转矩

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

用于指定复合或扩展三相端口的选项。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

定子绕组的配置，指定为以下值之一：

- `Wye-wound` — 指定星形连接的定子绕组。
- `Delta-wound` — 指定三角形连接的定子绕组。*A* 相连接在端口 **a** 和 **b** 之间，*B* 相连接在端口 **b** 和 **c** 之间，*C* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组采用开路端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Number of pole pairs** — 转子极对数 `4`（默认）| 正整数

电机极对数。

### **Park's convention for tabulated data** — 表格数据的 Park 约定 `Q leads D, rotor angle measured from A-phase to D-axis`（默认）| `Q leads D, rotor angle measured from A-phase to Q-axis` | `D leads Q, rotor angle measured from A-phase to D-axis` | `D leads Q, rotor angle measured from A-phase to Q-axis`

该模块用于将 *dq* 数据映射到三个绕组的 Park 变换的顺序和参考角度。

- `Q leads D, rotor angle measured from A-phase to D-axis` — 应用交-直变换，并相对于 *D* 轴测量角度。
- `Q leads D, rotor angle measured from A-phase to Q-axis` — 应用交-直变换，并相对于 *Q* 轴测量角度。
- `D leads Q, rotor angle measured from A-phase to D-axis` — 应用直-交变换，并相对于 *D* 轴测量角度。
- `D leads Q, rotor angle measured from A-phase to Q-axis` — 应用直-交变换，并相对于 *Q* 轴测量角度。

### **Peak current magnitude vector, I** — 峰值电流幅值 `[0, 100, 200]` `A`（默认）| 非负值的行向量

该模块用于将磁链制成表格的电流幅值行向量。第一个元素必须为 `0`。第二个电流值必须相对于磁饱和开始发生时的电流值较小。此限制是必要的，因为推导出的磁通偏导数在零电流处定义不明确，而该模块改为在此第一个非零电流处计算它们。

### **Current advance angle vector, B** — 电流超前角 `[-180, -90, 0, 90, 180]` `deg`（默认）| 实数值的行向量

该模块用于计算磁链的电流超前角值行向量。电流超前角是电流超前 *Q* 轴的角度。

### **Field current vector, If** — 励磁电流 `[0, 2, 4, 6, 8, 10]` `A`（默认）| 非负值的行向量

该模块用于计算磁链的励磁电流值行向量。第一个元素必须为 `0`。

### **Rotor angle vector, theta** — 转子角度 `[0, 15, 30, 45, 60, 75, 90]` `deg`（默认）| 非负值的行向量

该模块用于将磁链制成表格的转子角度向量。此向量的第一个元素必须为 `0`。极对数为 360/*Θ*max，其中 *Θ*max 以度为单位。默认值对应于一个四极对电机。

### **A-phase flux linkage, F(I,B,If,theta)** — *A* 相磁链 `zeros(3, 5, 6, 7)` `Wb`（默认）| 4-D 数组

*A* 相磁链值的 4-D 数组，作为 **Peak current magnitude vector, I**、**Current advance angle vector, B**、**Field current vector, If** 和 **Rotor angle vector, theta** 参数的函数。

如果您的磁通数据顺序不同，请使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中的 `ee_ece_table` 函数。

### **Torque matrix, T(I,B,If,theta)** — 转矩 `zeros(3, 5, 6, 7)` `N*m`（默认）| 4-D 数组

施加到转子上的电磁转矩的 4-D 数组，作为 **Peak current magnitude vector, I**、**Current advance angle vector, B**、**Field current vector, If** 和 **Rotor angle vector, theta** 的函数。

如果您的磁通数据顺序不同，请使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中的 `ee_ece_table` 函数。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法。

- `Linear` — 使用多维插值的线性算法扩展。选择此选项以获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (4D) 模块参考页。

### **Expose neutral port** — 中性端口可见性 `Off`（默认）| `On`

用于暴露该模块中性端口的选项。

如果暴露中性端口，该模块还会对零序电流进行建模，并使用 **Stator zero-sequence inductance, L0** 参数对零序进行参数化。

#### 依赖关系

要启用此参数，请将 **Winding type** 设置为 `Wye-wound`。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）| 正标量

零序电感。

#### 依赖关系

要启用此参数，请将 **Winding type** 设置为 `Delta-Wound` 或启用 **Expose neutral port** 参数。

### 电阻

### **Stator resistance per phase** — 每相定子电阻 `0.013` `Ohm`（默认）| 正标量

定子绕组每相的电阻。

### **Field winding resistance** — 励磁绕组电阻 `0.1` `Ohm`（默认）| 正标量

励磁绕组的电阻。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 *α*。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值为铜的值。

#### 依赖关系

要启用此参数，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

### **Measurement temperature** — 电阻测量温度 `298.15` `k`（默认）| 非负标量

该模块测量励磁绕组和定子电阻时的温度。

#### 依赖关系

要启用此参数，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

### 铁耗

### **Rotor hysteresis loss coefficient, k\_hr(I,B,If)** — 转子磁滞损耗系数 `zeros(3, 5, 6)` `W/Hz`（默认）| 实数值的 3-D 数组

转子的磁滞损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### **Rotor eddy current loss coefficient, k\_Jr(I,B,If)** — 转子涡流损耗系数 `zeros(3, 5, 6)` `W/Hz^2`（默认）| 实数值的 3-D 数组

转子的涡流损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### **Rotor excess current loss coefficient, k\_er(I,B,If)** — 转子 excess current 损耗系数 `zeros(3, 5, 6)` `W/Hz^(3/2)`（默认）| 实数值的 3-D 数组

转子的 excess current 损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### **Stator hysteresis loss coefficient, k\_hs(I,B,If)** — 定子磁滞损耗系数 `zeros(3, 5, 6)` `W/Hz`（默认）| 实数值的 3-D 数组

定子的磁滞损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### **Stator eddy current loss coefficient, k\_Js(I,B,If)** — 定子涡流损耗系数 `zeros(3, 5, 6)` `W/Hz^2`（默认）| 实数值的 3-D 数组

定子的涡流损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### **Stator excess current loss coefficient, k\_es(I,B,If)** — 定子 excess current 损耗系数 `zeros(3, 5, 6)` `W/Hz^(3/2)`（默认）| 实数值的 3-D 数组

定子的 excess current 损耗系数。该值取决于电流幅值、电流相位超前角和励磁电流。该模块在 Steinmetz 方程中使用此值。

### 机械

### **Rotor inertia** — 惯量 `0` `kg*m^2`（默认）| 非负标量

连接到机械平移端口 **R** 的转子的惯量。

### **Rotor Damping** — 阻尼 `0` `N*m*s/rad`（默认）| 非负标量

旋转阻尼。

### 热端口

### **Model thermal effects** — 用于对热效应建模的选项 `Off`（默认）| `On`

用于暴露热端口并对将功率转换为热量的损耗效应进行建模的选项。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024a：定子绕组的开路端配置

要以开路端配置对电机的定子绕组进行建模，请将 **Winding type** 参数设置为 `Open-end`。然后，FEM-Parameterized Synchronous Machine 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

## 描述

以磁链定义的同步电机

FEM-Parameterized Synchronous Machine 模块对外励同步电机或混合励磁永磁同步电机（PMSM）的电气和机械特性进行建模，其磁链非线性依赖于定子电流、励磁电流和转子角度。外励同步电机和 PMSM 也分别称为同步交流电机和双励同步电机。

使用此模块对外励电动机或具有转子励磁绕组的电机进行建模。该模块通过从电机设计工具导入有限元导出的查找表，捕获饱和效应和齿槽转矩等详细行为。您还可以对永磁体和励磁绕组共同产生转子磁通的混合励磁电机进行建模。

FEM-Parameterized Synchronous Machine 模块使用磁链，您必须使用外部有限元（FE）工具计算该磁链。该模块使用 *A* 相磁链，这是一个四维表，取决于定子电流幅值、定子电流超前角、励磁绕组电流和转子角度。该模块通过从 *A* 相、*B* 相和 *C* 相磁链计算 *D* 轴磁链，并减去励磁电流为零时的磁链，来推导励磁绕组磁链。

### 方程

此方程定义定子的反电动势（EMF）：

[eAeBeC]=[dΨAdtdΨBdtdΨCdt]+P−1[00L0]di0dt,

其中

- *eA*、*eB* 和 *eC* 是定子绕组电压。
- *ΨA*、*ΨB* 和 *ΨC* 是链接每个定子绕组的磁通。
- *L0* 是 **Stator zero-sequence inductance, L0** 参数的值。
- *i0* 是零序电流。
- *P* 是 Park 变换。

为保持表维度较小，此模块不用零序电流来制表定子磁链。然后该模块使用单独的项添加零序动态。如果您将 **Winding type** 参数设置为 `Wye-wound` 并且未启用 **Expose neutral port** 参数，则零序动态为零。

此方程定义转子励磁绕组的反 EMF：

ef=dΨfdt,

其中：

- *Ψf* 是励磁绕组磁链。这些方程定义励磁绕组磁链：

  [ΨdΨqΨ0]=P(θ)[ΨA(I,B,θ,if)ΨB(I,B,θ,if)ΨC(I,B,θ,if)]Ψf(I,B,θ,if)=Ψd(I,B,θ,if)−Ψd(I,B,θ,0)
- *ef* 是励磁绕组电压。
- *Ψd*、*Ψq* 和 *Ψ0* 分别是 *d* 轴、*q* 轴和零序磁通。
- *ΨA(I,B,θ,if)*、*ΨB(I,B,θ,if)* 和 *ΨC(I,B,θ,if)* 分别是 *A* 相、*B* 相和 *C* 相磁链，相对于 *I*、*B*、*θ* 和 *if* 制表。
- *I* 是定子峰值电流幅值。
- *B* 是定子电流超前角。
- *θ* 是转子角度。
- *Ψf (I,B,θ,if)* 是相对于 *I*、*B*、*θ* 和 *if* 制表的励磁绕组磁链。

*P* 是 Park 变换，取决于您为 **Park's convention for tabulated data** 参数选择的选项。

**注意**

**Park's convention for tabulated data** 参数的 Park 变换选项必须与您在 FE 工具中用于生成磁链数据的 Park 变换版本匹配。

**选项 1：`Q leads D, rotor angle measured from A-phase to D-axis`**

Simscape™ Electrical™ 电机和电机模块内部使用此约定，并将所有其他选项转换为此格式。

- *N* 是 **Number of pole pairs** 参数的值。
- *θ*r 是转子角度。
- *i*d 和 *i*q 分别是 *D* 轴和 *Q* 轴电流。
- *i*p 是电流幅值，等于 id2+iq2。
- *β* 是电流超前角，等于 tan−1(−id/iq)。

对应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 *A* 相、*B* 相和 *C* 相电流。

**选项 2：`Q leads D, rotor angle measured from A-phase to Q-axis`**

- *N* 是 **Number of pole pairs** 参数的值。
- *θ*r 是转子角度。
- *i*d 和 *i*q 分别是 *D* 轴和 *Q* 轴电流。
- *i*p 是电流幅值，等于 id2+iq2。
- *β* 是电流超前角，等于 tan−1(−id/iq)。

对应的 Park 变换为

[idiqi0]=23[sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 *A* 相、*B* 相和 *C* 相电流。

**选项 3：`D leads Q, rotor angle measured from A-phase to D-axis`**

- *N* 是 **Number of pole pairs** 参数的值。
- *θ*r 是转子角度。
- *i*d 和 *i*q 分别是 *D* 轴和 *Q* 轴电流。
- *i*p 是电流幅值，等于 id2+iq2。
- *β* 是电流超前角，等于 tan−1(−id/iq)。

对应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 *A* 相、*B* 相和 *C* 相电流。

**选项 4：`D leads Q, rotor angle measured from A-phase to Q-axis`**

- *N* 是 **Number of pole pairs** 参数的值。
- *θ*r 是转子角度。
- *i*d 和 *i*q 分别是 *D* 轴和 *Q* 轴电流。
- *i*p 是电流幅值，等于 id2+iq2。
- *β* 是电流超前角，等于 tan−1(−id/iq)。

对应的 Park 变换为

[idiqi0]=23[−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c* 分别是 *A* 相、*B* 相和 *C* 相电流。

### 计算铁损

FEM-Parameterized Synchronous Machine 模块使用 Steinmetz 方程对铁损进行建模。Steinmetz 方程针对不同电机转速或电气频率进行缩放，因此该模块仅需要铁损数据作为电机电流的函数。

该模块使用 **Peak current magnitude vector, I**、**Current advance angle vector, B** 和 **Field current vector, If** 参数对铁损系数进行制表：

Protor(f)=khr(Ip,β,If)f+kJr(Ip,β,If)f2+ker(Ip,β,If)f1.5Pstator(f)=khs(Ip,β,If)f+kJs(Ip,β,If)f2+kes(Ip,β,If)f1.5

其中：

- *f* 是电气频率，单位为 Hz。
- *khr(Ip,β,If)* 是 **Rotor hysteresis loss coefficient, k\_hr(I,B,If)** 参数值。
- *kJr(Ip,β,If)* 是 **Rotor eddy current loss coefficient, k\_Jr(I,B,If)** 参数值。
- *ker(Ip,β,If)* 是 **Rotor excess current loss coefficient, k\_er(I,B,If)** 参数值。
- *khs(Ip,β,If)* 是 **Stator hysteresis loss coefficient, k\_hs(I,B,If)** 参数值。
- *kJs(Ip,β,If)* 是 **Stator eddy current loss coefficient, k\_Js(I,B,If)** 参数值。
- *kes(Ip,β,If)* 是 **Stator excess current loss coefficient, k\_es(I,B,If)** 参数值。

### 热效应建模

您可以暴露热端口来对将功率转换为热量的损耗效应进行建模。要暴露热端口，请在 **Thermal Ports** 部分中启用 **Model thermal effects** 参数。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
