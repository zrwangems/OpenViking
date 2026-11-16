---
type: simulink-block
title: 'Half-Bridge (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'halfbridgeidealswitching'
documentation_source_path: 'ref/halfbridgeidealswitching.html'
language: zh-CN
chinese_source: worker-translation
---

# Half-Bridge (Ideal, Switching)

## 端口

### 输入

### **G** — 栅极端子向量物理信号

与两个开关器件的栅极端子关联的物理信号守恒端口，指定为两个物理信号的向量。

向量的第一个元素控制上侧开关。向量的第二个元素控制下侧开关。如果在 **二极管** 设置中，将 **集成保护二极管** 参数设置为 `Yes`，则向量的第一个和第二个元素还分别控制下侧和上侧二极管。

#### 依赖关系

要启用此端口，请将 **栅极控制端口** 设置为 `PS`。

### 守恒

### **+** — 正极端子电气

与正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与负极端子关联的电气守恒端口。

### **O** — 输出节点电气

与输出节点关联的电气守恒端口。

### **G1** — 栅极端子 1 电气

与第一个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **栅极控制端口** 设置为 `Electrical`。

### **G2** — 栅极端子 2 电气

与第二个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **栅极控制端口** 设置为 `Electrical`。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖关系

要启用此端口，请清除 **上下器件分离热端口** 和 **集成二极管分离热端口** 参数。

### **H1Switch** — 上开关器件的热端口 thermal

*自 R2024a 起*

与上开关器件关联的热守恒端口。

#### 依赖关系

要启用此端口，请选择 **上下器件分离热端口** 参数。

### **H2Switch** — 下开关器件的热端口 thermal

*自 R2024a 起*

与下开关器件关联的热守恒端口。

#### 依赖关系

要启用此端口，请选择 **上下器件分离热端口** 参数。

### **H1Diode** — 上二极管的热端口 thermal

*自 R2024a 起*

与上二极管关联的热守恒端口。

#### 依赖关系

要启用此端口，请选择 **上下器件分离热端口** 和 **集成二极管分离热端口** 参数。

### **H2Diode** — 下二极管的热端口 thermal

*自 R2024a 起*

与下二极管关联的热守恒端口。

#### 依赖关系

要启用此端口，请选择 **上下器件分离热端口** 和 **集成二极管分离热端口** 参数。

## 参数

### 主要

**主要** 参数的可视性取决于 **开关器件** 和 **导通行为与损耗** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| 栅极控制端口 | | | | | |
| **开关器件** | | | | | |
| *`MOSFET`* | | *`IGBT`* | | *`GTO`* | |
| 阈值电压, Vth | | 阈值电压, Vth | | 栅极触发电压, Vgt | |
| 栅极关断电压, Vgt\_off | |
| 保持电流 | |
| **导通行为与损耗** | | **导通行为与损耗** | | **导通行为与损耗** | |
| *`Specify constant values`* | *`Tabulate`* | *`Specify constant values`* | *`Tabulate`* | *`Specify constant values`* | *`Tabulate`* |
| 漏源导通电阻, R\_DS(on) | 导通电压, Vds(Tj,Ids) | 正向电压, Vf | 导通电压, Vds(Tj,Ice) | 正向电压, Vf | 导通电压, Vak(Tj,Iak) |
| 温度向量, Tj | 导通电阻 | 温度向量, Tj | 导通电阻 | 温度向量, Tj |
| 漏源电流向量, Ids | 集电极-发射极电流向量, Ice | 阳极-阴极电流向量, Iak |
| 断态电导 | | | | | |

### **栅极控制端口** — 栅极控制端口 `PS` (默认) | `Electrical`

选择使用物理信号输入端口 **G** 还是电气守恒端口 **G1** 和 **G2** 作为栅极控制端口的选项。

### **开关器件** — 开关器件选项 `MOSFET` (默认) | `IGBT` | `GTO`

半桥的开关器件。

### **阈值电压, Vth** — 阈值电压 `2` `V` | `6` `V` | positive scalar

器件导通时的阈值电压。默认值取决于 **开关器件** 设置。

#### 依赖关系

请参阅主要参数依赖关系表。

### **栅极触发电压, Vgt** — 栅极触发电压 `6` `V` (默认) | positive scalar

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **栅极关断电压, Vgt\_off** — 栅极关断电压 `-1` `V` (默认) | scalar

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅主要参数依赖关系表。

### **保持电流** — 电流阈值 `1` `A` (默认) | positive scalar

电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通行为与损耗** — 导通行为与损耗 `Specify constant values` (默认) | `Tabulate`

导通行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。该模块假设单次开通或关断事件期间耗散的能量与断态电压和导通电流成线性关系。该模块还假设损耗与温度无关。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用数组指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **漏源导通电阻, R\_DS(on)** — 漏源导通电阻 `0.01` `Ohm` (默认) | positive scalar

器件导通时的漏源电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通电压, Vds(Tj,Ids)** — 导通电压 `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1, 1.15, 1.35, 1.7, 2.35, 3]` `V` (默认) | matrix of nonnegative scalars

器件在触发导通状态下的电压降。此参数是温度和最终导通输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **漏源电流向量, Ids** — 漏源电流向量 `[0 10 50 100 200 400 600]` `A` (默认) | vector of positive scalars

引用导通电压时所对应的漏源电流。漏源电流的符号必须与对应漏源电压的符号相同。如果漏源电压为零，则对应的漏源电流也必须为零。

#### 依赖关系

请参阅主要参数依赖关系表。

### **正向电压, Vf** — 正向电压 `0.8` `V` (默认) | positive scalar

使二极管 I-V 特性斜率为 1/*R*on 所需的集电极与发射极之间或阳极与阴极之间模块端口的最小电压，其中 *R*on 是 **导通电阻** 参数的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通电阻** — 导通集电极-发射极电阻 `0.001` `Ohm` (默认) | positive scalar

器件导通时的集电极-发射极电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通电压, Vds(Tj,Ice)** — 导通电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (默认) | matrix of nonnegative scalars

器件在触发导通状态下的电压降。此参数是温度和最终导通输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **集电极-发射极电流向量, Ice** — 集电极-发射极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (默认) | vector of positive scalars

引用导通电压时所对应的集电极-发射极电流。集电极-发射极电流的符号必须与对应集电极-发射极电压的符号相同。如果集电极-发射极电压为零，则对应的集电极-发射极电流也必须为零。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通电压, Vak(Tj,Iak)** — 导通电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (默认) | matrix of nonnegative scalars

器件在触发导通状态下的电压降。此参数是温度和最终导通输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **阳极-阴极电流向量, Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (默认) | vector of positive scalars

引用导通电压时所对应的阳极-阴极电流。阳极-阴极电流的符号必须与对应阳极-阴极电压的符号相同。如果阳极-阴极电压为零，则对应的阳极-阴极电流也必须为零。

#### 依赖关系

请参阅主要参数依赖关系表。

### **温度向量, Tj** — 温度值 `[298.15, 398.15]` `K` (默认) | vector

引用导通电压时所对应的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **断态电导** — 断态集电极-发射极电导 `1e-6` `1/Ohm` (默认) | positive scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **导通电阻** 参数的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### 损耗

### **开通损耗** — 开通损耗 `22.86e-3` `J` (默认) | positive scalar

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **导通行为与损耗** 设置为 `Specify constant values`。

### **关断损耗** — 关断损耗 `17.14e-3` `J` (默认) | positive scalar

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `MOSFET` 或 `IGBT`，并将 **导通行为与损耗** 设置为 `Specify constant values`。

### **二极管反向恢复损耗** — 二极管反向恢复的损耗 `5.70e-3` `J` (默认) | positive scalar

二极管反向恢复事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **导通行为与损耗** 设置为 `Specify constant values`，并将 **集成保护二极管** 设置为 `Yes`。

### **用于损耗数据的导通电流** — 输出电流 `600` `A` (默认) | positive scalar

引用开通损耗、关断损耗和导通电压时所对应的输出电流。

#### 依赖关系

要启用此参数，请将 **导通行为与损耗** 设置为 `Specify constant values`。

### **用于损耗数据的断态电压** — 断态电压 `300` `V` (默认) | positive scalar

器件关断时的输出电压。此值是引用损耗时的阻断电压。如果将开关损耗指定为标量值，或在固定断态电压下指定为结温和导通电流的函数，则该模块使用此值计算开关损耗。如果将 **集成保护二极管** 设置为 `Yes`，则该模块使用此值计算二极管反向恢复损耗。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **集成保护二极管** 设置为 `Yes`。
- 将 **导通行为与损耗** 设置为 `Specify constant values`。
- 将 **开关器件** 设置为 `MOSFET`，将 **导通行为与损耗** 设置为 `Tabulate`，并清除 **包含使用断态 Vds 电压的开关损耗表格化** 参数。
- 将 **开关器件** 设置为 `IGBT`，将 **导通行为与损耗** 设置为 `Tabulate`，并清除 **包含使用断态电压的开关损耗表格化** 参数。
- 将 **开关器件** 设置为 `GTO`。

### **将开关损耗施加到电源** — 将开关损耗施加到电源的选项 `Off` (默认) | `On`

*自 R2023b 起*

将开关损耗施加到电源的选项。

清除此参数以仅将开关损耗施加到热节点。

选择此参数以将开关损耗施加到热节点和电源。

### **开通损耗, Eon(Tj,Ids)** — 开通损耗 `[0, .29, 1.43, 2.86, 5.71, 13.14, 22.86; 0, .57, 2.63, 5.14, 10.29, 20.57, 30.29] * 1e-3` `J` (默认) | vector of positive scalars

单次开通事件期间耗散的能量，是温度和最终导通漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **导通行为与损耗** 设置为 `Tabulate`。
- 清除 **包含使用断态 Vds 电压的开关损耗表格化** 参数。

### **关断损耗, Eoff(Tj,Ids)** — 关断损耗 `[0, .21, 1.07, 2.14, 4.29, 9.86, 17.14; 0, .43, 1.97, 3.86, 7.71, 15.43, 22.71] * 1e-3` `J` (默认) | vector of positive scalars

单次关断事件期间耗散的能量，是温度和最终导通漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **导通行为与损耗** 设置为 `Tabulate`。
- 清除 **包含使用断态 Vds 电压的开关损耗表格化** 参数。

### **二极管反向恢复损耗, Erec(Tj,Ids)** — 二极管反向恢复的损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J` (默认) | vector of positive scalars

二极管反向恢复事件期间耗散的能量，是温度和最终导通漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **导通行为与损耗** 设置为 `Tabulate`。
- 将 **集成保护二极管** 设置为 `Yes`。

### **损耗温度向量, Tj** — 损耗温度 `[298.15, 398.15]` `K` (默认) | vector

引用损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将 **导通行为与损耗** 设置为 `Tabulate`。

### **损耗漏源电流向量, Ids** — 开关损耗的漏源电流 `[0, 10, 50, 100, 200, 400, 600]` `A` (默认) | vector of positive scalars

引用损耗时所对应的漏源电流。漏源电流的符号必须与对应漏源电压的符号相同。如果漏源电压为零，则对应的漏源电流也必须为零。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `MOSFET`，并将 **导通行为与损耗** 设置为 `Tabulate`。

### **包含关态 Vds 电压的开关损耗表格** — 使用关态 Vds 电压来表格化开关损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

用于使用关态漏源电压来表格化开关损耗的选项。

清除此参数以使用通态漏源电流和温度来表格化开通损耗和关断损耗。模块假设损耗与关态漏源电压成线性关系。

选择此参数以使用温度、通态漏源电流和关态漏源电压来表格化开通损耗和关断损耗。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `MOSFET`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **开通损耗, Eon(Tj,Ids,Vds)** — 开通损耗 `[zeros(2, 7, 3)]` `J`（默认）| 非负标量的 3-D 数组

*自 R2023b 起*

在单次开通事件期间耗散的能量，是温度、通态漏源电流和关态漏源电压的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 选择 **包含关态 Vds 电压的开关损耗表格** 参数。

### **关断损耗, Eoff(Tj,Ids,Vds)** — 关断损耗 `[zeros(2, 7, 3)]` `J`（默认）| 非负标量的 3-D 数组

*自 R2023b 起*

在单次关断事件期间耗散的能量，是温度、通态漏源电流和关态漏源电压的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 选择 **包含关态 Vds 电压的开关损耗表格** 参数。

### **开通损耗, Eon(Tj,Ice)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 正标量的向量

在单次开通事件期间耗散的能量，是温度和最终通态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 清除 **包含关态电压的开关损耗表格** 参数。

### **关断损耗, Eoff(Tj,Ice)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 正标量的向量

在单次关断事件期间耗散的能量，是温度和最终通态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 清除 **包含关态电压的开关损耗表格** 参数。

### **二极管反向恢复损耗, Erec(Tj,Ice)** — 二极管反向恢复损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J`（默认）| 正标量的向量

在二极管反向恢复事件期间耗散的能量，是温度和最终通态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 将 **集成保护二极管** 设置为 `Yes`。

### **损耗用集电极-发射极电流向量, Ice** — 损耗用集电极-发射极电流 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量的向量

给出损耗所对应的集电极-发射极电流。集电极-发射极电流的符号必须与相应的集电极-发射极电压的符号相同。如果集电极-发射极电压为零，则相应的集电极-发射极电流也必须为零。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `IGBT`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **包含关态电压的开关损耗表格** — 使用关态电压来表格化开关损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

用于使用关态电压来表格化开关损耗的选项。

清除此参数以使用通态集电极-发射极电流和温度来表格化开通损耗和关断损耗。模块假设损耗与关态电压成线性关系。

选择此参数以使用温度、通态集电极-发射极电流和关态电压来表格化开通损耗和关断损耗。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `IGBT`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **开通损耗, Eon(Tj,Ice,Vce)** — 开通损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的 3-D 数组

*自 R2023b 起*

在单次开通事件期间耗散的能量，是温度、通态集电极-发射极电流和关态集电极-发射极电压的函数。

#### 依赖关系

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 选择 **包含关态电压的开关损耗表格** 参数。

### **关断损耗, Eoff(Tj,Ice,Vce)** — 关断损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的 3-D 数组

*自 R2023b 起*

在单次关断事件期间耗散的能量，是温度、通态集电极-发射极电流和关态集电极-发射极电压的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 选择 **包含关态电压的开关损耗表格** 参数。

### **开关损耗用关态电压向量, Vce** — 开关损耗数据用关态电压向量 `[0, 150, 300]` `V`（默认）| 向量

*自 R2023b 起*

给出开通损耗和关断损耗所对应的关态集电极-发射极电压。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `IGBT`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 选择 **包含关态电压的开关损耗表格** 参数。

### **强制换相关断损耗** — 强制换相关断损耗 `17.14e-3` `J`（默认）| 正标量

在强制换相关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `GTO`，并将 **通态行为和损耗** 设置为 `Specify constant values`。

### **自然换相整流损耗** — 自然换相整流损耗 `10e-3` `J`（默认）| 正标量

当器件因电流降至 **保持电流** 参数值以下而关断时，模块施加的整流损耗。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `GTO`。

### **开通损耗, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量的矩阵

在单次开通事件期间耗散的能量，是温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `GTO`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **关断损耗, Eoff(Tj,Iak)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 正标量的向量

在单次关断事件期间耗散的能量，是温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `GTO`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **二极管反向恢复损耗, Erec(Tj,Iak)** — 二极管反向恢复损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J`（默认）| 正标量的向量

在二极管反向恢复事件期间耗散的能量，是温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `GTO`。
- 将 **通态行为和损耗** 设置为 `Tabulate`。
- 将 **集成保护二极管** 设置为 `Yes`。

### **损耗用阳极-阴极电流向量, Iak** — 损耗用阳极-阴极电流 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量的向量

给出损耗所对应的阳极-阴极电流。阳极-阴极电流的符号必须与相应的阳极-阴极电压的符号相同。如果阳极-阴极电压为零，则相应的阳极-阴极电流也必须为零。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `GTO`，并将 **通态行为和损耗** 设置为 `Tabulate`。

### **开关损耗平均周期** — 开关损耗平均周期 `1e-3` `s`（默认）| 正标量

*自 R2023b 起*

模块将开关损耗施加到电源的持续时间。

#### 依赖关系

要启用此参数，请选择 **将开关损耗施加到电源** 参数。

### 集成二极管

### **集成保护二极管** — 保护二极管 `No`（默认）| `Yes`

是否对模块的集成保护二极管建模。

### **二极管模型** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

二极管模型，指定为以下选项之一：

- `Piecewise Linear` — 使用二极管的分段线性模型，如 Piecewise Linear Diode 中所述。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据和固定的反向偏置关断电导。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`。

### **正向电压** — 正向电压 `0.8` `V`（默认）| 正标量

为使二极管 I-V 特性的梯度为 1/*R*on，在 `+` 和 `-` 模块端口两端所需的最小电压，其中 *R*on 是 **导通电阻** 参数的值。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并将 **二极管模型** 设置为 `Piecewise linear`。

### **导通电阻** — 导通电阻 `0.001` `Ohm`（默认）| 正标量

高于 **正向电压** 参数值时，电压相对于电流的变化率。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并将 **二极管模型** 设置为 `Piecewise linear`。

### **关断电导** — 关断电导 `1e-5` `1/Ohm`（默认）| 正标量

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并满足以下任一条件：

- **二极管模型** 设置为 `Piecewise linear`。
- **二极管模型** 设置为 `Tabulated I-V curve`，且 **反向 I-V 特性类型** 设置为 `Specify off conductacne`。

### **表格类型** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是将电压表格化为温度和电流的函数。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并将 **二极管模型** 设置为 `Tabulated I-V curve`。

### **反向 I-V 特性类型** — 反向 I-V 特性的类型 `Specify off conductance`（默认）| `Tabulate`

*自 R2024a 起*

是通过使用二极管关断电导来指定反向 I-V 特性，还是通过将电流表格化为温度和电压的函数或将电压表格化为温度和电流的函数来指定反向 I-V 特性。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并将 **二极管模型** 设置为 `Tabulated I-V curve`。

### **正向电流, If(Tj,Vf)** — 正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*If(Tj,Vf)* = 0A）。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，将 **二极管模型** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in If(Tj,Vf) form`。

### **结温, Tj** — 结温 `[25, 125]` `degC`（默认）| 正标量的向量

结温向量。此参数必须为至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，并将 **二极管模型** 设置为 `Tabulated I-V curve`。

### **正向电压, Vf** — 正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）| 非负向量

正向电压向量。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*Vf* = 0V）。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，将 **二极管模型** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in If(Tj,Vf) form`。

### **正向电压, Vf(Tj,If)** — 正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负向量

正向电压。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*Vf(Tj,If)* = 0V）。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，将 **二极管模型** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in Vf(Tj,If) form`。

### **正向电流, If** — 正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）| 非负向量

正向电流向量。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*If* = 0A）。

#### 依赖关系

要启用此参数，请将 **集成保护二极管** 设置为 `Yes`，将 **二极管模型** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in Vf(Tj,If) form`。

### **反向电流, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数，请设置：

- **集成保护二极管** 为 `Yes`
- **二极管模型** 为 `Tabulated I-V curve`
- **表格类型** 为 `Table in If(Tj,Vf) form`
- **反向 I-V 特性** 为 `Tabulate`

### **反向电压, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压向量。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*Vr* = 0V）。

#### 依赖关系

要启用此参数，请设置：

- **集成保护二极管** 为 `Yes`
- **二极管模型** 为 `Tabulated I-V curve`
- **表格类型** 为 `Table in If(Tj,Vf) form`
- **反向 I-V 特性** 为 `Tabulate`

### **反向电压, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压。此参数必须为至少包含三个非负元素的向量，且按升序排列。零点可选（*Vr(Tj,Ir)* = 0V）。

#### 依赖关系

要启用此参数，请设置：

- **Integral protection diode** 为
  `Yes`
- **Diode model** 为
  `Tabulated I-V
  curve`
- **Table type** 为 `Table
  in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为
  `Tabulate`

### **Reverse currents, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流向量。此参数必须是一个包含至少三个非负元素的向量，且按升序排列。零点为可选（*Ir* = 0A）。

#### 依赖关系

要启用此参数，请设置：

- **Integral protection diode** 为
  `Yes`
- **Diode model** 为
  `Tabulated I-V
  curve`
- **Table type** 为 `Table
  in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为
  `Tabulate`

### 热端口

使用热端口来模拟产生的热量和设备温度的影响。此模块为两个晶体管和两个二极管实现了一个单一的内部热模型。任何热模型参数（如 Cauer 模型参数）均适用于聚合后的热模型。

### **Separate thermal ports for upper and lower devices** — 为上下管分开热端口的选项 `off`（默认）| `on`

*自 R2024a 起*

是否为上管和下管分开热端口。

### **Separate thermal ports for integral diodes** — 为集成二极管分开热端口的选项 `off`（默认）| `on`

*自 R2024a 起*

是否为上管和下管的集成二极管分开热端口。

#### 依赖关系

要启用此参数，请选中 **Separate thermal
ports for upper and lower devices** 参数，并在
**Integral Diode** 部分中，将
**Integral protection diode** 设置为
`Yes`。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

热质量的参数化选项：

- `By thermal time constants` —
  用热时间常数来参数化热质量。
- `By thermal mass` — 直接指定
  热质量值。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结到外壳以及外壳到环境（或外壳到散热器）的热阻 `[.03, .2]` `K/W`（默认）| 正数值向量

包含两个热阻值的行向量 [ *R\_JC*
*R\_CA* ]，由两个 Conductive Heat Transfer 模块表示。第一个值
*R\_JC* 是结到外壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与设备外壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和外壳的热时间常数 `[.1, 5]` `s`（默认）| 正数值向量

包含两个热时间常数值的行向量 [ *t\_J*
*t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值
*t\_C* 是外壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`，并将 **Thermal mass
parameterization** 设置为 `By thermal time
constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和外壳的热质量 `[3, 25]` `J/K`（默认）| 正数值向量

包含两个热质量值的行向量 [ *M\_J*
*M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值
*M\_C* 是外壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`，并将 **Thermal mass
parameterization** 设置为 `By thermal
mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和外壳的初始温度 `[25, 25]` `degC`（默认）| 正数值向量

包含两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是外壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`。

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 集成二极管的结到外壳以及外壳到环境（或外壳到散热器）的热阻 `[.03, .2]` `K/W`（默认）| 正数值向量

*自 R2024a 起*

集成保护二极管的包含两个热阻值的行向量 [ *R\_JC*
*R\_CA* ]，由两个 Conductive Heat Transfer 模块表示。第一个值
*R\_JC* 是结到外壳之间的热阻。第二个值
*R\_CA* 是端口 **H** 与二极管外壳之间的热阻。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Specify junction and case thermal
    parameters`。

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — 集成二极管的结和外壳热时间常数 `[.1, 5]` `s`（默认）| 正数值向量

*自 R2024a 起*

集成保护二极管的包含两个热时间常数值的行向量 [ *t\_J*
*t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是外壳时间常数。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Specify junction and case thermal
    parameters`。
  - 将 **Thermal mass
    parameterization** 设置为 `By
    thermal time constants`。

### **Thermal masses of diode junction and case, [M\_J M\_C]** — 二极管结和外壳的热质量 `[3, 25]` `J/K`（默认）| 正数值向量

*自 R2024a 起*

集成保护二极管的包含两个热质量值的行向量 [ *M\_J*
*M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是外壳热质量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Specify junction and case thermal
    parameters`。
  - 将 **Thermal mass
    parameterization** 设置为 `By
    thermal mass`。

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — 二极管结和外壳的初始温度 `[25, 25]` `degC`（默认）| 正数值向量

*自 R2024a 起*

集成保护二极管的包含两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值
*T\_J* 是结初始温度。第二个值 *T\_C* 是外壳初始温度。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Specify junction and case thermal
    parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.03, .1, .2]``K/W`（默认）| `[.03, .2]` `K/W` | 正数值向量

包含 *n* 个热阻值的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[.03, .1,
.2]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[.03,
.2]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster
coefficients`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.1, 1, 5]` `s`（默认）| `[1, 10]` `s` | 正数值向量

包含 *n* 个热时间常数值的行向量，其中
*n* 是热网络中使用的 Cauer 元件数量。此向量的长度必须与
**Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式时，热质量计算为
`Mi =
ti/Ri`，
其中 `Mi`、
`ti` 和
`Ri` 分别是第
i 个 Cauer 元件（如果将
**Thermal network** 设置为 `Cauer
model`）或 Foster 元件（如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[.1, 1,
5]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[1,
10]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster coefficients`，并将
**Thermal mass parameterization** 设置为
`By thermal time constants`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[3, 10, 25]` `J/K`（默认）| `[33, 50]` `J/K` | 正数值向量

包含 *n* 个热质量值的行向量，其中 n 是热网络中使用的 Cauer 元件数量。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[3, 10,
25]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[33,
50]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster coefficients`，并将
**Thermal mass parameterization** 设置为
`By thermal masses`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正数值向量

对应于模型中每个热容两端温降的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model`。

### **Diode thermal resistances, [R1 R2 … Rn]** — 集成二极管的热阻 `[.03, .1, .2]``K/W`（默认）| `[.03, .2]` `K/W` | 正数值向量

*自 R2024a 起*

集成保护二极管的包含 *n* 个热阻值的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[.03, .1,
.2]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[.03,
.2]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Cauer model` 或
    `Cauer model parameterized with Foster
    coefficients`。

### **Diode thermal time constants, [t1 t2 … tn]** — 集成二极管的热时间常数 `[.1, 1, 5]` `s`（默认）| `[1, 10]` `s` | 正数值向量

*自 R2024a 起*

集成保护二极管的包含 *n* 个热时间常数值的行向量，其中 *n* 是热网络中使用的 Cauer 元件数量。此向量的长度必须与 **Diode thermal resistances, [R1 R2 …
Rn]** 的长度匹配。使用此参数化方式时，热质量计算为 `Mi =
ti/Ri`，
其中 `Mi`、
`ti` 和
`Ri` 分别是第
i 个 Cauer 元件（如果将
**Thermal network** 设置为 `Cauer
model`）或 Foster 元件（如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[.1, 1,
5]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[1,
10]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Cauer model` 或
    `Cauer model parameterized with Foster
    coefficients`。
  - 将 **Thermal mass
    parameterization** 设置为 `By
    thermal time constants`。

### **Diode thermal masses, [M1 M2 … Mn]** — 集成二极管的热质量 `[3, 10, 25]` `J/K`（默认）| `[33, 50]` `J/K` | 正数值向量

*自 R2024a 起*

集成保护二极管的包含 *n* 个热质量值的行向量，其中 n 是热网络中使用的 Cauer 元件数量。

如果将 **Thermal network** 设置为 `Cauer
model`，则默认值为 `[3, 10,
25]`。如果将 **Thermal network** 设置为
`Cauer model parameterized with Foster
coefficients`，则默认值为 `[33,
50]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Cauer model` 或
    `Cauer model parameterized with Foster
    coefficients`。
  - 将 **Thermal mass
    parameterization** 设置为 `By
    thermal masses`。

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — 二极管热质量的初始温度 `[25, 25, 25]` `degC`（默认）| 正数值向量

*自 R2024a 起*

集成保护二极管的温度值行向量。此参数对应于模型中每个热容两端的温降。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，
  将 **Integral protection diode** 设置为
  `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports
    for upper and lower devices** 参数。
  - 选中 **Separate thermal ports
    for integral diodes** 参数。
  - 将 **Thermal network** 设置为
    `Cauer model`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正数值向量

从结开始每个节点的绝对温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model parameterized with Foster
coefficients`。

### **Diode initial node temperatures, [T1 T2 ... Tn]** — 集成二极管的初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正数值向量

*自 R2024a 起*

从集成保护二极管结开始每个节点的绝对温度值行向量。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分中，
  将 **集成保护二极管** 设置为
  `Yes`。
- 在 **热端口** 部分中：

  - 选择 **为上部与下部器件
    分离热端口** 参数。
  - 选择 **为集成二极管
    分离热端口** 参数。
  - 将 **热网络** 设置为
    `Cauer model parameterized with Foster
    coefficients`。

### **结热质量** — 结的热质量 `0.1` `J/K`（默认） | positive scalar

结的热质量。

#### 依赖项

要启用此参数，请将 **热网络**
设置为 `External`。

### **二极管结热质量** — 二极管结的热质量 `0.1` `J/K`（默认） | positive scalar

*自 R2024a 起*

二极管结的热质量。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分中，
  将 **集成保护二极管** 设置为
  `Yes`。
- 在 **热端口** 部分中：

  - 选择 **为上部与下部器件
    分离热端口** 参数。
  - 选择 **为集成二极管
    分离热端口** 参数。
  - 将 **热网络** 设置为
    `External`。

有关使用热端口以及其他 **热端口**
参数的更多信息，请参阅在半导体中模拟热效应。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024a：为上部器件、下部器件和集成二极管分离热端口

您现在可以通过选择 **为上部与下部器件分离热端口** 参数，将热端口 **H** 分离为分别与上部与下部开关器件关联的两个不同热端口。如果您为上部与下部器件分离热端口，则还可以通过选择 **为集成二极管分离热端口** 参数，为每个开关器件的集成二极管分离热端口。

上部与下部开关器件共享相同的热参数。

### R2024a：对表格化的反向 I-V 特性建模

您现在可以通过将电流表格化为温度和电压的函数，或将电压表格化为温度和电流的函数，为 Half-Bridge (Ideal, Switching) 模块对反向 I-V 特性建模。

在 R2024a 之前，您只能通过指定反向偏置二极管的断态电导来对反向 I-V 特性建模。

### R2023b：确定不连续负载电流的开关损耗

如果您将 **开关器件** 参数设置为
`MOSFET` 或 `IGBT`，则
Half-Bridge (Ideal, Switching) 模块现在支持
不连续负载电流。

该模块通过在所有开通和关断事件中测量断态电压和导通电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用此行为。如果您使用固定步长求解器，最短的器件导通或关断周期现在为一个步长。在 R2023b 之前，最小周期为三个步长。要报告开关损耗，最小周期仍为三个步长。

在 R2023b 之前，该模块仅在开通前测量断态电压，并在关断前测量导通电流。

由于此更改，如果您在早期版本中创建了使用
Half-Bridge (Ideal, Switching) 模块以及对外部二极管
建模电容或电荷的模型，则必须更新该模型。最佳选项是在
Half-Bridge (Ideal, Switching) 模块内部对二极管建模。
要在外部对二极管建模，请在不带电容或电荷的情况下对它们建模。

### R2023b：将开关损耗施加到电源

您现在可以通过选择 **将开关损耗施加到电源**
参数，从电源抽取因开关损耗产生的功率。在 R2023a 之前，该模块仅将开关损耗施加到热节点，将节点温度升高所需值。

### R2023b：使用温度、电流和电压表格化开关损耗

如果您将 **开关器件** 参数设置为
`MOSFET` 或 `IGBT`，您现在
可以使用温度、电流和电压表格化开关损耗。在早期版本中，您只能使用温度和电流
表格化开关损耗。

## 描述

带理想开关和热端口的半桥

Half-Bridge (Ideal, Switching) 模块对带理想开关和热端口的半桥建模。要选择理想开关器件，请将
**开关器件** 参数设置为
`MOSFET`、`IGBT` 或
`GTO`。

您可以为每个开关器件指定一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然关断向负载的电压供应时，感性负载可能产生高反向电压尖峰。

**注意**

最佳选项是在 Half-Bridge (Ideal,
Switching) 模块内部对二极管建模。要在外部对二极管建模，请在不带电容
或电荷的情况下对它们建模。

### 开关损耗

有关模块如何对开通和关断损耗建模的信息，请参阅
MOSFET (Ideal, Switching) 模块、IGBT (Ideal, Switching) 模块或 GTO 模块的文档页面，具体取决于您为
**开关器件** 参数选择的选项。这些模块与
Half-Bridge (Ideal, Switching)
模块对损耗建模方式的主要区别在于，对于 `MOSFET` 和
`IGBT` 选项，Half-Bridge (Ideal,
Switching) 模块不使用 **使用上一周期的最后导通电流计算开通损耗** 或 **使用上一周期的最后断态电压计算关断损耗** 参数。
造成此区别的原因是 Half-Bridge (Ideal,
Switching) 模块不对二极管电容或引线
电感建模，因为该模块设计用于使用理想开关进行快速仿真。
通过在一个模块中对两个开关器件建模，您可以避免测量二极管
反向恢复的导通电流和断态电压相关的复杂性，因此不需要基于物理的二极管电荷模型。该模块
在您命令互补开关器件关断的时刻测量二极管正向电流和断态电压。

默认情况下，模块仅将开关损耗施加到热节点，将节点温度升高所需值。要从电源抽取因开关
损耗产生的所需功率，请选择 **将开关损耗施加到
电源** 参数。

将开关损耗瞬时施加到电源在数学上是不可能的，因此模块在等于您为
**开关损耗平均周期**
参数指定的值的时间段内施加开关损耗。将此值设置为栅极驱动器的脉冲宽度调制 (PWM) 周期。

**注意**

对于所有理想开关器件，记录的仿真数据将
热损耗报告为 `lastTurnOffLoss`、
`lastTurnOnLoss` 和
`lastReverseRecoveryLoss`。这些变量将损耗
包含为脉冲，其幅度等于能量损耗。如果您使用脚本对定义的仿真时间段内的总损耗求和，则必须在每个脉冲上升沿对脉冲
值求和。或者，您可以使用 `ee_getPowerLossSummary` 和
`ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和
开关损耗。要了解如何记录和绘制仿真数据，请参阅记录和绘制仿真数据示例。

您还可以从记录的仿真数据中相应的
`accumulatedSwitchingLosses` 变量访问两个
开关器件各自的总累计开关损耗。这些变量对迄今为止的所有开关损耗求和，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量
不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告
欧姆导通损耗。

如果您使用固定步长求解器，支持捕获开关损耗的最短导通脉冲或关断脉冲为三个时间步长。如果脉冲
短于三个步长，模块不报告开关损耗。

如果您使用表格数据对开关损耗或反向恢复损耗建模，请检查温度、电流和电压是否在您指定的范围内。如果您未定义实际的热模型，例如，如果结质量或从结到外壳的电导过小，温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### 参数化

Half-Bridge (Ideal, Switching) 模块支持多个
预定义参数化。

使用此参数化数据表示特定供应商的组件。这些半桥的参数化与制造商数据表匹配。要加载
预定义参数化，请双击 Half-Bridge (Ideal, Switching)
模块，单击 **所选部件** 参数的
**<click to select>** 超链接，然后在模块参数化
管理器窗口中，从可用组件列表中选择您要使用的部件。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要改进组件模型。

有关预定义参数化以及可用组件列表的更多信息，请参阅预参数化组件列表。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取开关器件和集成保护二极管的器件参数，并将其导入模块。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 或 Infineon® 支持的参数化格式。

### 热端口

使用热端口模拟产生的热量和器件温度的影响。有关使用热端口以及 **热端口**
参数的更多信息，请参阅在半导体中模拟热效应。

您还可以通过选择 **为上部与下部器件分离热端口** 参数，将热端口
**H** 分离为分别与上部与
下部开关器件关联的两个不同热端口。如果您为
上部与下部器件分离热端口，则还可以通过选择
**为集成二极管分离热端口** 参数，为每个开关器件的集成二极管分离热端口。
上部与下部开关器件共享相同的热参数。*(自 R2024a 起)*

下图显示了当您公开所有热端口时的模块图标：

### 变量

要在仿真前设置模块变量的优先级和初始目标值，
请使用模块对话框或属性检查器中的 **初始目标** 部分。有关更多信息，请参阅设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量值。使用基于标称值的系统缩放可提高仿真稳健性。标称值
可以来自不同来源。其中一种来源是模块对话框或属性检查器中的 **标称值** 部分。有关
更多信息，请参阅按标称值进行系统缩放。
