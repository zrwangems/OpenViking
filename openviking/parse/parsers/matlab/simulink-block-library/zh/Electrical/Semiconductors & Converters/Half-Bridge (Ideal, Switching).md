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
```yaml
ports:
- name: G
  summary: 栅极端子矢量物理信号
  direction: input
- name: +
  summary: 正极端子电气
  direction: input
- name: '-'
  summary: 负极端子电气
  direction: input
- name: O
  summary: 输出节点电气
  direction: input
- name: G1
  summary: 栅极端子 1 电气
  direction: input
- name: G2
  summary: 栅极端子 2 电气
  direction: input
- name: H
  summary: 热端口热
  direction: input
- name: H1Switch
  summary: 上侧开关器件热端口热
  direction: input
- name: H2Switch
  summary: 下侧开关器件热端口热
  direction: input
- name: H1Diode
  summary: 上侧二极管热端口热
  direction: input
- name: H2Diode
  summary: 下侧二极管热端口热
  direction: input
```

### 输入

### **G** — 栅极端子矢量物理信号

与两个开关器件的栅极端子相关联的物理信号守恒端口，指定为包含两个物理信号的矢量。

该矢量的第一个元素控制上侧开关。该矢量的第二个元素控制下侧开关。如果在 **Diode** 设置中将 **Integral protection diode** 参数设置为 `Yes`，则该矢量的第一个和第二个元素还分别控制下侧和上侧二极管。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。
### 守恒

### **+** — 正极端子电气

与正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与负极端子相关联的电气守恒端口。

### **O** — 输出节点电气

与输出节点相关联的电气守恒端口。

### **G1** — 栅极端子 1 电气

与第一个开关器件的栅极端子相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G2** — 栅极端子 2 电气

与第二个开关器件的栅极端子相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请清除 **Separate thermal ports for upper and lower devices** 和 **Separate thermal ports for integral diodes** 参数。

### **H1Switch** — 上侧开关器件热端口热

*自 R2024a 起*

与上侧开关器件相关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal ports for upper and lower devices** 参数。

### **H2Switch** — 下侧开关器件热端口热

*自 R2024a 起*

与下侧开关器件相关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal ports for upper and lower devices** 参数。

### **H1Diode** — 上侧二极管热端口热

*自 R2024a 起*

与上侧二极管相关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal ports for upper and lower devices** 和 **Separate thermal ports for integral diodes** 参数。

### **H2Diode** — 下侧二极管热端口热

*自 R2024a 起*

与下侧二极管相关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal ports for upper and lower devices** 和 **Separate thermal ports for integral diodes** 参数。
## 参数
```yaml
parameters:
- name: 栅极控制端口
  summary: 栅极控制端口 PS（默认）| Electrical
  group: 主要
- name: 开关器件
  summary: 开关器件选项 MOSFET（默认）| IGBT | GTO
  group: 主要
- name: 阈值电压，Vth
  summary: 阈值电压 2 V | 6 V | 正标量
  group: 主要
- name: 栅极触发电压，Vgt
  summary: 栅极触发电压 6 V（默认）| 正标量
  group: 主要
- name: 栅极关断电压，Vgt_off
  summary: 栅极关断电压 -1 V（默认）| 标量
  group: 主要
- name: 维持电流
  summary: 电流阈值 1 A（默认）| 正标量
  group: 主要
- name: 导通行为与损耗
  summary: 导通行为与损耗 指定常量值（默认）| 制表
  group: 主要
- name: 漏源导通电阻，R_DS(on)
  summary: 漏源导通电阻 0.01 Ohm（默认）| 正标量
  group: 主要
- name: 导通状态电压，Vds(Tj,Ids)
  summary: 导通状态电压 [0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1, 1.15, 1.35, 1.7, 2.35, 3] V（默认）| 非负标量矩阵
  group: 主要
- name: 漏源电流向量，Ids
  summary: 漏源电流向量 [0 10 50 100 200 400 600] A（默认）| 正标量向量
  group: 主要
- name: 正向电压，Vf
  summary: 正向电压 0.8 V（默认）| 正标量
  group: 主要
- name: 导通状态电阻
  summary: 导通状态集电极-发射极电阻 0.001 Ohm（默认）| 正标量
  group: 主要
- name: 导通状态电压，Vds(Tj,Ice)
  summary: 导通状态电压 [0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8] V（默认）| 非负标量矩阵
  group: 主要
- name: 集电极-发射极电流向量，Ice
  summary: 集电极-发射极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 正标量向量
  group: 主要
- name: 导通状态电压，Vak(Tj,Iak)
  summary: 导通状态电压 [0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8] V（默认）| 非负标量矩阵
  group: 主要
- name: 阳极-阴极电流向量，Iak
  summary: 阳极-阴极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 正标量向量
  group: 主要
- name: 温度向量，Tj
  summary: 温度值 [298.15, 398.15] K（默认）| 向量
  group: 主要
- name: 断态电导
  summary: 断态集电极-发射极电导 1e-6 1/Ohm（默认）| 正标量
  group: 主要
- name: 开通损耗
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: 损耗
- name: 关断损耗
  summary: 关断损耗 17.14e-3 J（默认）| 正标量
  group: 损耗
- name: 二极管反向恢复损耗
  summary: 二极管反向恢复引起的损耗 5.70e-3 J（默认）| 正标量
  group: 损耗
- name: 损耗数据的通态电流
  summary: 输出电流 600 A（默认）| 正标量
  group: 损耗
- name: 损耗数据的断态电压
  summary: 断态电压 300 V（默认）| 正标量
  group: 损耗
- name: 将开关损耗施加到电源
  summary: 将开关损耗施加到电源的选项 关（默认）| 开
  group: 损耗
- name: 开通损耗，Eon(Tj,Ids)
  summary: 开通损耗 [0, .29, 1.43, 2.86, 5.71, 13.14, 22.86; 0, .57, 2.63, 5.14, 10.29, 20.57, 30.29] * 1e-3 J（默认）| 正标量向量
  group: 损耗
- name: 关断损耗，Eoff(Tj,Ids)
  summary: 关断损耗 [0, .21, 1.07, 2.14, 4.29, 9.86, 17.14; 0, .43, 1.97, 3.86, 7.71, 15.43, 22.71] * 1e-3 J（默认）| 正标量向量
  group: 损耗
- name: Diode reverse recovery loss, Erec(Tj,Ids)
  summary: 二极管反向恢复损耗 [0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3
    J（默认）| 正标量向量
  group: 损耗
- name: Temperature vector for losses, Tj
  summary: 损耗对应的温度 [298.15, 398.15] K（默认）| 向量
  group: 损耗
- name: Drain-source current vector for losses, Ids
  summary: 开关损耗对应的漏源电流 [0, 10, 50, 100, 200, 400, 600] A（默认）| 正标量向量
  group: 损耗
- name: Include switching loss tabulation with off-state Vds voltage
  summary: 使用关断状态 Vds 电压对开关损耗进行制表的选项 Off（默认）| On
  group: 损耗
- name: Switch-on loss, Eon(Tj,Ids,Vds)
  summary: 开通损耗 [zeros(2, 7, 3)] J（默认）| 非负标量的三维数组
  group: 损耗
- name: Switch-off loss, Eoff(Tj,Ids,Vds)
  summary: 关断损耗 [zeros(2, 7, 3)] J（默认）| 非负标量的三维数组
  group: 损耗
- name: Switch-on loss, Eon(Tj,Ice)
  summary: 开通损耗 [0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3 J（默认）|
    正标量向量
  group: 损耗
- name: Switch-off loss, Eoff(Tj,Ice)
  summary: 关断损耗 [0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3 J（默认）|
    正标量向量
  group: 损耗
- name: Diode reverse recovery loss, Erec(Tj,Ice)
  summary: 二极管反向恢复损耗 [0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3
    J（默认）| 正标量向量
  group: 损耗
- name: Collector-emitter current vector for losses, Ice
  summary: 损耗对应的集电极-发射极电流 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 正标量向量
  group: 损耗
- name: Include switching loss tabulation with off-state voltage
  summary: 使用断态电压对开关损耗进行表格化的选项 Off（默认）| On
  group: 损耗
- name: Switch-on loss, Eon(Tj,Ice,Vce)
  summary: 开通损耗 [zeros(2, 9, 3)] J（默认）| 非负标量的三维数组
  group: 损耗
- name: Switch-off loss, Eoff(Tj,Ice,Vce)
  summary: 关断损耗 [zeros(2, 9, 3)] J（默认）| 非负标量的三维数组
  group: 损耗
- name: Off-state voltage vector for switching losses, Vce
  summary: 开关损耗的断态电压向量 [0, 150, 300] V（默认）| 向量
  group: 损耗
- name: Forced commutation switch-off loss
  summary: 强制换相关断损耗 17.14e-3 J（默认）| 正标量
  group: 损耗
- name: Natural commutation rectification loss
  summary: 自然换相整流损耗 10e-3 J（默认）| 正标量
  group: 损耗
- name: Switch-on loss, Eon(Tj,Iak)
  summary: 开通损耗 [0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3 J（默认）|
    非负标量矩阵
  group: 损耗
- name: Switch-off loss, Eoff(Tj,Iak)
  summary: 关断损耗 [0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3 J（默认）|
    正标量向量
  group: 损耗
- name: Diode reverse recovery loss, Erec(Tj,Iak)
  summary: 二极管反向恢复损耗 [0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3
    J（默认）| 正标量向量
  group: 损耗
- name: Anode-cathode current vector for losses, Iak
  summary: 损耗对应的阳极-阴极电流 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 正标量向量
  group: 损耗
- name: Averaging period for switching losses
  summary: 开关损耗平均周期 1e-3 s（默认）| 正标量
  group: 损耗
- name: Integral protection diode
  summary: 保护二极管 No（默认）| Yes
  group: Integral Diode
- name: Diode model
  summary: 二极管模型 Piecewise Linear（默认）| Tabulated I-V curve
  group: Integral Diode
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）| 正标量
  group: Integral Diode
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）| 正标量
  group: Integral Diode
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认）| 正标量
  group: Integral Diode
- name: Table type
  summary: 表格函数 Table in If(Tj,Vf) form（默认）| Table in Vf(Tj,If) form
  group: Integral Diode
- name: Reverse I-V characteristics type
  summary: 反向 I-V 特性类型 Specify off conductance（默认）| Tabulate
  group: Integral Diode
- name: Forward currents, If(Tj,Vf)
  summary: 正向电流 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）| 非负向量
  group: Integral Diode
- name: Junction temperatures, Tj
  summary: 结温 [25, 125] degC（默认）| 正标量向量
  group: Integral Diode
- name: Forward voltages, Vf
  summary: 正向电压 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）| 非负向量
  group: Integral Diode
- name: Forward voltages, Vf(Tj,If)
  summary: 正向电压 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）| 非负向量
  group: Integral Diode
- name: Forward currents, If
  summary: 正向电流 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）| 非负向量
  group: Integral Diode
- name: 反向电流，Ir(Tj,Vr)
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005] A（默认）|
    非负向量
  group: Integral Diode
- name: 反向电压，Vr
  summary: 反向电压向量 [10, 20, 40, 50, 70, 80, 100] V（默认）| 非负向量
  group: Integral Diode
- name: 反向电压，Vr(Tj,Ir)
  summary: 反向电压向量 [10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320] V（默认）| 非负向量
  group: Integral Diode
- name: 反向电流，Ir
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001] A（默认）| 非负向量
  group: Integral Diode
- name: Separate thermal ports for upper and lower devices
  summary: 分离上下管热端口选项 off（默认）| on
  group: 热端口
- name: Separate thermal ports for integral diodes
  summary: 分离体二极管热端口选项 off（默认）| on
  group: 热端口
- name: Thermal network
  summary: 热网络建模选项 External（默认）| Specify junction and case thermal parameters | Cauer model | Cauer model parameterized with
    Foster coefficients
  group: 热端口
- name: Thermal mass parameterization
  summary: 热质量参数化选项 By thermal time constants（默认）| By thermal mass
  group: 热端口
- name: Junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 结-壳与壳-环境（或壳-散热器）热阻 [.03, .2] K/W（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal time constants, [t_J t_C]
  summary: 结与壳热时间常数 [.1, 5] s（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal masses, [M_J M_C]
  summary: 结与壳热质量 [3, 25] J/K（默认）| 正值向量
  group: 热端口
- name: Junction and case initial temperatures, [T_J T_C]
  summary: 结与壳初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 集成二极管结-壳与壳-环境（或壳-散热器）热阻 [.03, .2] K/W（默认）| 正值向量
  group: 热端口
- name: Thermal time constants of diode junction and case, [t_J t_C]
  summary: 集成二极管结与壳热时间常数 [.1, 5] s（默认）| 正值向量
  group: 热端口
- name: Thermal masses of diode junction and case, [M_J M_C]
  summary: 二极管结和壳的热质量 [3, 25] J/K（默认）| 正值向量
  group: 热端口
- name: Initial temperatures of diode junction and case, [T_J T_C]
  summary: 二极管结和壳的初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal resistances, [R1 R2 … Rn]
  summary: 热阻 [.03, .1, .2]K/W（默认）| [.03, .2] K/W | 正值向量
  group: 热端口
- name: Thermal time constants, [t1 t2 … tn]
  summary: 热时间常数 [.1, 1, 5] s（默认）| [1, 10] s | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [3, 10, 25] J/K（默认）| [33, 50] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode thermal resistances, [R1 R2 … Rn]
  summary: 集成二极管的热阻 [.03, .1, .2]K/W（默认）| [.03, .2] K/W | 正值向量
  group: 热端口
- name: Diode thermal time constants, [t1 t2 … tn]
  summary: 集成二极管的热时间常数 [.1, 1, 5] s（默认）| [1, 10] s | 正值向量
  group: 热端口
- name: Diode thermal masses, [M1 M2 … Mn]
  summary: 积分二极管的热质量 [3, 10, 25] J/K（默认）| [33, 50] J/K | 正值向量
  group: 热端口
- name: Initial temperatures of diode thermal masses, [T1 T2 … Tn]
  summary: 二极管热质量的初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Initial node temperatures, [T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode initial node temperatures, [T1 T2 ... Tn]
  summary: 积分二极管的初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Junction thermal mass
  summary: 结点的热质量 0.1 J/K（默认）| 正标量
  group: 热端口
- name: Diode junction thermal mass
  summary: 二极管结点的热质量 0.1 J/K（默认）| 正标量
  group: 热端口
```

### 主要

**主要**参数的可见性取决于**开关器件**和**导通行为与损耗**参数。要了解如何阅读此表，请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| 栅极控制端口 | | | | | |
| **开关器件** | | | | | |
| *`MOSFET`* | | *`IGBT`* | | *`GTO`* | |
| 阈值电压，Vth | | 阈值电压，Vth | | 栅极触发电压，Vgt | |
| 栅极关断电压，Vgt\_off | |
| 维持电流 | |
| **导通行为与损耗** | | **导通行为与损耗** | | **导通行为与损耗** | |
| *`指定常量值`* | *`制表`* | *`指定常量值`* | *`制表`* | *`指定常量值`* | *`制表`* |
| 漏源导通电阻，R\_DS(on) | 导通电压，Vds(Tj,Ids) | 正向电压，Vf | 导通电压，Vds(Tj,Ice) | 正向电压，Vf | 导通电压，Vak(Tj,Iak) |
| 温度向量，Tj | 导通电阻 | 温度向量，Tj | 导通电阻 | 温度向量，Tj |
| 漏源电流向量，Ids | 集电极-发射极电流向量，Ice | 阳极-阴极电流向量，Iak |
| 断态电导 | | | | | |

### **栅极控制端口** — 栅极控制端口 `PS`（默认）| `Electrical`

选择使用物理信号输入端口 **G** 还是电气守恒端口 **G1** 和 **G2** 作为栅极控制端口。

### **开关器件** — 开关器件选项 `MOSFET`（默认）| `IGBT` | `GTO`

半桥的开关器件。

### **阈值电压，Vth** — 阈值电压 `2` `V` | `6` `V` | 正标量

器件导通时的阈值电压。默认值取决于**开关器件**设置。

#### 依赖关系

请参阅主要参数依赖关系表。

### **栅极触发电压，Vgt** — 栅极触发电压 `6` `V`（默认）| 正标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **栅极关断电压，Vgt\_off** — 栅极关断电压 `-1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅主要参数依赖关系表。

### **维持电流** — 电流阈值 `1` `A`（默认）| 正标量

电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通行为与损耗** — 导通行为与损耗 `指定常量值`（默认）| `制表`

导通行为和开关损耗的参数化方法，指定为以下值之一：

- `指定常量值` — 使用标量值指定输出电流、开通损耗和关断损耗数据。该模块假设单次开通或关断事件期间耗散的能量与断态电压和导通电流成线性关系。该模块还假设损耗与温度无关。
- `制表` — 使用向量指定输出电流和温度数据。使用数组指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **漏源导通电阻，R\_DS(on)** — 漏源导通电阻 `0.01` `Ohm`（默认）| 正标量

器件导通时的漏源电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **导通状态电压，Vds(Tj,Ids)** — 导通状态电压 `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1, 1.15, 1.35, 1.7, 2.35, 3]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。该参数是温度和最终导通状态输出电流的函数。

#### 依赖关系

参见主参数依赖关系表。

### **漏源电流向量，Ids** — 漏源电流向量 `[0 10 50 100 200 400 600]` `A`（默认）| 正标量向量

给出导通状态电压时所对应的漏源电流。漏源电流的符号必须与对应的漏源电压符号相同。如果漏源电压为零，则对应的漏源电流也必须为零。

#### 依赖关系

参见主参数依赖关系表。

### **正向电压，Vf** — 正向电压 `0.8` `V`（默认）| 正标量

使二极管 I-V 特性梯度为 1/*R*on 所需的集电极与发射极之间或阳极与阴极模块端口之间的最小电压，其中 *R*on 是 **导通状态电阻** 参数的值。

#### 依赖关系

参见主参数依赖关系表。

### **导通状态电阻** — 导通状态集电极-发射极电阻 `0.001` `Ohm`（默认）| 正标量

器件导通时的集电极-发射极电阻。

#### 依赖关系

参见主参数依赖关系表。

### **导通状态电压，Vds(Tj,Ice)** — 导通状态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。该参数是温度和最终导通状态输出电流的函数。

#### 依赖关系

参见主参数依赖关系表。

### **集电极-发射极电流向量，Ice** — 集电极-发射极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量向量

给出导通状态电压时所对应的集电极-发射极电流。集电极-发射极电流的符号必须与对应的集电极-发射极电压符号相同。如果集电极-发射极电压为零，则对应的集电极-发射极电流也必须为零。

#### 依赖关系

参见主参数依赖关系表。

### **导通状态电压，Vak(Tj,Iak)** — 导通状态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。该参数是温度和最终导通状态输出电流的函数。

#### 依赖关系

参见主参数依赖关系表。

### **阳极-阴极电流向量，Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量向量

给出导通状态电压时所对应的阳极-阴极电流。阳极-阴极电流的符号必须与对应的阳极-阴极电压符号相同。如果阳极-阴极电压为零，则对应的阳极-阴极电流也必须为零。

#### 依赖关系

参见主参数依赖关系表。

### **温度向量，Tj** — 温度值 `[298.15, 398.15]` `K`（默认）| 向量

给出导通状态电压时所对应的温度值。

#### 依赖关系

参见主参数依赖关系表。

### **断态电导** — 断态集电极-发射极电导 `1e-6` `1/Ohm`（默认）| 正标量

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **导通状态电阻** 参数的值。

#### 依赖关系

参见主参数依赖关系表。

### 损耗

### **开通损耗** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **通态行为和损耗** 设置为 `指定常量值`。

### **关断损耗** — 关断损耗 `17.14e-3` `J`（默认）| 正标量

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `MOSFET` 或 `IGBT`，并将 **通态行为和损耗** 设置为 `指定常量值`。

### **二极管反向恢复损耗** — 二极管反向恢复引起的损耗 `5.70e-3` `J`（默认）| 正标量

二极管反向恢复事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **通态行为和损耗** 设置为 `指定常量值`，并将 **集成保护二极管** 设置为 `是`。

### **损耗数据的通态电流** — 输出电流 `600` `A`（默认）| 正标量

您据以给出开通损耗、关断损耗和通态电压的输出电流。

#### 依赖关系

要启用此参数，请将 **通态行为和损耗** 设置为 `指定常量值`。

### **损耗数据的断态电压** — 断态电压 `300` `V`（默认）| 正标量

器件关断时的输出电压。该值是您据以给出损耗的阻断电压。如果您将开关损耗指定为标量值，或在固定断态电压下指定为结温和通态电流的函数，则该模块使用此值计算开关损耗。如果您将 **集成保护二极管** 设置为 `是`，则该模块使用此值计算二极管反向恢复损耗。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **集成保护二极管** 设置为 `是`。
- 将 **通态行为和损耗** 设置为 `指定常量值`。
- 将 **开关器件** 设置为 `MOSFET`，将 **通态行为和损耗** 设置为 `制表`，并清除 **包含带断态 Vds 电压的开关损耗制表** 参数。
- 将 **开关器件** 设置为 `IGBT`，将 **通态行为和损耗** 设置为 `制表`，并清除 **包含带断态电压的开关损耗制表** 参数。
- 将 **开关器件** 设置为 `GTO`。

### **将开关损耗施加到电源** — 将开关损耗施加到电源的选项 `关`（默认）| `开`

*自 R2023b 起*

将开关损耗施加到电源的选项。

清除此参数以仅将开关损耗施加到热节点。

选择此参数以将开关损耗施加到热节点和电源。

### **开通损耗，Eon(Tj,Ids)** — 开通损耗 `[0, .29, 1.43, 2.86, 5.71, 13.14, 22.86; 0, .57, 2.63, 5.14, 10.29, 20.57, 30.29] * 1e-3` `J`（默认）| 正标量向量

单次开通事件期间耗散的能量，作为温度和最终通态漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **通态行为和损耗** 设置为 `制表`。
- 清除 **包含带断态 Vds 电压的开关损耗制表** 参数。

### **关断损耗，Eoff(Tj,Ids)** — 关断损耗 `[0, .21, 1.07, 2.14, 4.29, 9.86, 17.14; 0, .43, 1.97, 3.86, 7.71, 15.43, 22.71] * 1e-3` `J`（默认）| 正标量向量

单次关断事件期间耗散的能量，作为温度和最终通态漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **开关器件** 设置为 `MOSFET`。
- 将 **通态行为和损耗** 设置为 `制表`。
- 清除 **包含带断态 Vds 电压的开关损耗制表** 参数。

### **Diode reverse recovery loss, Erec(Tj,Ids)** — 二极管反向恢复损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J`（默认）| 正标量向量

二极管反向恢复事件期间耗散的能量，作为温度和最终导通状态漏源电流的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为 `MOSFET`。
- 将 **On-state behavior and losses** 设置为 `Tabulate`。
- 将 **Integral protection diode** 设置为 `Yes`。

### **Temperature vector for losses, Tj** — 损耗对应的温度 `[298.15, 398.15]` `K`（默认）| 向量

您给出损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Drain-source current vector for losses, Ids** — 开关损耗对应的漏源电流 `[0, 10, 50, 100, 200, 400, 600]` `A`（默认）| 正标量向量

您给出损耗时所对应的漏源电流。漏源电流的符号必须与对应漏源电压的符号相同。如果漏源电压为零，则对应的漏源电流也必须为零。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `MOSFET`，并将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Include switching loss tabulation with off-state Vds voltage** — 使用关断状态 Vds 电压对开关损耗进行制表的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用关断状态漏源电压对开关损耗进行制表的选项。

清除此参数以根据导通状态漏源电流和温度对开通损耗和关断损耗进行制表。该模块假定损耗与关断状态漏源电压成线性关系。

选择此参数以根据温度、导通状态漏源电流和关断状态漏源电压对开通损耗和关断损耗进行制表。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `MOSFET`，并将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Switch-on loss, Eon(Tj,Ids,Vds)** — 开通损耗 `[zeros(2, 7, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次开通事件期间耗散的能量，作为温度、导通状态漏源电流和关断状态漏源电压的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为 `MOSFET`。
- 将 **On-state behavior and losses** 设置为 `Tabulate`。
- 选择 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ids,Vds)** — 关断损耗 `[zeros(2, 7, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次关断事件期间耗散的能量，作为温度、导通状态漏源电流和关断状态漏源电压的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为 `MOSFET`。
- 将 **On-state behavior and losses** 设置为 `Tabulate`。
- 选择 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-on loss, Eon(Tj,Ice)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 正标量向量

单次开通事件期间耗散的能量，作为温度和最终导通状态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为 `IGBT`。
- 将 **On-state behavior and losses** 设置为 `Tabulate`。
- 清除 **Include switching loss tabulation with off-state voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ice)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 正标量向量

单次关断事件期间耗散的能量，作为温度和最终导通状态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为
  `IGBT`。
- 将 **On-state behavior and losses**
  设置为 `Tabulate`。
- 清除 **Include switching loss tabulation
  with off-state voltage** 参数。

### **Diode reverse recovery loss, Erec(Tj,Ice)** — 二极管反向恢复损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J`（默认）| 正标量向量

二极管反向恢复事件期间耗散的能量，作为温度和最终导通状态集电极-发射极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为
  `IGBT`。
- 将 **On-state behavior and losses**
  设置为 `Tabulate`。
- 将 **Integral protection diode** 设置为
  `Yes`。

### **Collector-emitter current vector for losses, Ice** — 损耗对应的集电极-发射极电流 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量向量

给出损耗时所对应的集电极-发射极电流。集电极-发射极电流的符号必须与对应集电极-发射极电压的符号相同。如果集电极-发射极电压为零，则对应的集电极-发射极电流也必须为零。

#### 依赖关系

要启用此参数，请将 **Switching
device** 设置为 `IGBT`，并将
**On-state behavior and losses** 设置为
`Tabulate`。

### **Include switching loss tabulation with off-state voltage** — 使用断态电压对开关损耗进行表格化的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用断态电压对开关损耗进行表格化的选项。

清除此参数以根据导通状态集电极-发射极电流和温度对开通损耗和关断损耗进行表格化。该模块假设损耗与断态电压成线性关系。

选择此参数以根据温度、导通状态集电极-发射极电流和断态电压对开通损耗和关断损耗进行表格化。

#### 依赖关系

要启用此参数，请将 **Switching
device** 设置为 `IGBT`，并将
**On-state behavior and losses** 设置为
`Tabulate`。

### **Switch-on loss, Eon(Tj,Ice,Vce)** — 开通损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次开通事件期间耗散的能量，作为温度、导通状态集电极-发射极电流和断态集电极-发射极电压的函数。

#### 依赖关系

- 将 **Switching device** 设置为
  `IGBT`。
- 将 **On-state behavior and losses** 设置为
  `Tabulate`。
- 选择 **Include switching loss tabulation
  with off-state voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ice,Vce)** — 关断损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次关断事件期间耗散的能量，作为温度、导通状态集电极-发射极电流和断态集电极-发射极电压的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为
  `IGBT`。
- 将 **On-state behavior and losses**
  设置为 `Tabulate`。
- 选择 **Include switching loss tabulation
  with off-state voltage** 参数。

### **Off-state voltage vector for switching losses, Vce** — 开关损耗的断态电压向量 `[0, 150, 300]` `V`（默认）| 向量

*自 R2023b 起*

给出开通损耗和关断损耗时所对应的断态集电极-发射极电压。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为
  `IGBT`。
- 将 **On-state behavior and losses**
  设置为 `Tabulate`。
- 选择 **Include switching loss tabulation
  with off-state voltage** 参数。

### **Forced commutation switch-off loss** — 强制换相关断损耗 `17.14e-3` `J`（默认）| 正标量

强制换相关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`，并将 **On-state behavior and losses** 设置为 `Specify constant values`。

### **Natural commutation rectification loss** — 自然换相整流损耗 `10e-3` `J`（默认）| 正标量

当器件因电流降至 **Holding current** 参数值以下而关断时，模块施加的整流损耗。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`。

### **Switch-on loss, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，作为温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`，并将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Switch-off loss, Eoff(Tj,Iak)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 正标量向量

单次关断事件期间耗散的能量，作为温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`，并将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Diode reverse recovery loss, Erec(Tj,Iak)** — 二极管反向恢复损耗 `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J`（默认）| 正标量向量

二极管反向恢复事件期间耗散的能量，作为温度和最终通态阳极-阴极电流的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 设置为 `GTO`。
- 将 **On-state behavior and losses** 设置为 `Tabulate`。
- 将 **Integral protection diode** 设置为 `Yes`。

### **Anode-cathode current vector for losses, Iak** — 损耗对应的阳极-阴极电流 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 正标量向量

给出损耗时所对应的阳极-阴极电流。阳极-阴极电流的符号必须与对应阳极-阴极电压的符号相同。如果阳极-阴极电压为零，则对应的阳极-阴极电流也必须为零。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`，并将 **On-state behavior and losses** 设置为 `Tabulate`。

### **Averaging period for switching losses** — 开关损耗平均周期 `1e-3` `s`（默认）| 正标量

*自 R2023b 起*

模块将开关损耗施加到电源的持续时间。

#### 依赖关系

要启用此参数，请选择 **Apply switching losses to electrical supply** 参数。

### Integral Diode

### **Integral protection diode** — 保护二极管 `No`（默认）| `Yes`

是否对模块的集成保护二极管进行建模。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

二极管模型，指定为以下之一：

- `Piecewise Linear` — 对二极管使用分段线性模型，如 Piecewise Linear Diode 中所述。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据和固定的反向偏置关断电导。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Yes`。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）| 正标量

使二极管 I-V 特性梯度为 1/*R*on 时，`+` 和 `-` 模块端口之间所需的最小电压，其中 *R*on 是 **On resistance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为
`Yes`，并将 **Diode
model** 设置为 `Piecewise linear`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）| 正标量

在 **Forward voltage** 参数值以上的电压随电流的变化率。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为
`Yes`，并将 **Diode
model** 设置为 `Piecewise linear`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）| 正标量

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为
`Yes`，并且满足以下任一条件：

- **Diode model** 设置为
  `Piecewise linear`。
- **Diode model** 设置为
  `Tabulated I-V curve`，且
  **Reverse I-V characteristics
  type** 设置为 `Specify off
  conductacne`。

### **Table type** — 表格函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表示为温度和电压的函数，还是将电压表示为温度和电流的函数。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为
`Yes`，并将 **Diode
model** 设置为 `Tabulated I-V
curve`。

### **Reverse I-V characteristics type** — 反向 I-V 特性类型 `Specify off conductance`（默认）| `Tabulate`

*自 R2024a 起*

是通过使用二极管关断电导来指定反向 I-V 特性，还是通过将电流表示为温度和电压的函数或将电压表示为温度和电流的函数来制表。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，并将
**Diode model** 设置为 `Tabulated I-V
curve`。

### **Forward currents, If(Tj,Vf)** — 正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
(*If(Tj,Vf)* = 0A)。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，
**Diode model** 设置为 `Tabulated I-V
curve`，并将 **Table type** 设置为
`Table in If(Tj,Vf) form`。

### **Junction temperatures, Tj** — 结温 `[25, 125]` `degC`（默认）| 正标量向量

结温向量。此参数必须是一个至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，并将
**Diode model** 设置为 `Tabulated I-V
curve`。

### **Forward voltages, Vf** — 正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）| 非负向量

正向电压向量。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
(*Vf* = 0V)。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，
**Diode model** 设置为 `Tabulated I-V
curve`，并将 **Table type** 设置为
`Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负向量

正向电压。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
(*Vf(Tj,If)* = 0V)。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，
**Diode model** 设置为 `Tabulated I-V
curve`，并将 **Table type** 设置为
`Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）| 非负向量

正向电流向量。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
(*If* = 0A)。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Yes`，
**Diode model** 设置为 `Tabulated I-V
curve`，并将 **Table type** 设置为
`Table in Vf(Tj,If) form`。

### **反向电流，Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数，请设置：

- **Integral protection diode** 为
  `Yes`
- **Diode model** 为
  `Tabulated I-V
  curve`
- **Table type** 为 `Table
  in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为
  `Tabulate`

### **反向电压，Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压向量。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
（*Vr* = 0V）。

#### 依赖关系

要启用此参数，请设置：

- **Integral protection diode** 为
  `Yes`
- **Diode model** 为
  `Tabulated I-V
  curve`
- **Table type** 为 `Table
  in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为
  `Tabulate`

### **反向电压，Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
（*Vr(Tj,Ir)* = 0V）。

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

### **反向电流，Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流向量。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选
（*Ir* = 0A）。

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

使用热端口来模拟产生的热量和设备温度的影响。此模块为两个晶体管和两个二极管实现了一个单一的内部热模型。任何热模型参数，例如 Cauer 模型参数，均适用于聚合后的热模型。

### **Separate thermal ports for upper and lower devices** — 分离上下管热端口选项 `off`（默认）| `on`

*自 R2024a 起*

是否分离上下管的热端口。

### **Separate thermal ports for integral diodes** — 分离体二极管热端口选项 `off`（默认）| `on`

*自 R2024a 起*

是否分离上下管体二极管的热端口。

#### 依赖关系

要启用此参数，请选择 **Separate thermal
ports for upper and lower devices** 参数，并在
**Integral Diode** 部分中，将
**Integral protection diode** 设置为
`Yes`。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

用于对模块热网络进行建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

热质量的参数化选项：

- `By thermal time constants` —
  根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定
  热质量值。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳与壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认）| 正值向量

由两个 Conductive Heat Transfer 模块表示的两个热阻值行向量 [ *R\_JC*
*R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结与壳热时间常数 `[.1, 5]` `s`（默认）| 正值向量

两个热时间常数值的行向量 [ *t\_J*
*t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结与壳热质量 `[3, 25]` `J/K`（默认）| 正值向量

两个热质量值的行向量 [ *M\_J*
*M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结与壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 集成二极管结-壳与壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认）| 正值向量

*自 R2024a 起*

由两个 Conductive Heat Transfer 模块表示的、用于集成保护二极管的两个热阻值行向量 [ *R\_JC*
*R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与二极管壳之间的热阻。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — 集成二极管结与壳热时间常数 `[.1, 5]` `s`（默认）| 正值向量

*自 R2024a 起*

用于集成保护二极管的两个热时间常数值的行向量 [ *t\_J*
*t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses of diode junction and case, [M\_J M\_C]** — 二极管结和壳的热质量 `[3, 25]` `J/K`（默认）| 正值向量

*自 R2024a 起*

用于积分保护二极管的两个热质量值的行向量 [ *M\_J* *M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — 二极管结和壳的初始温度 `[25, 25]` `degC`（默认）| 正值向量

*自 R2024a 起*

用于积分保护二极管的两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.03, .1, .2]``K/W`（默认）| `[.03, .2]` `K/W` | 正值向量

由热网络中使用的 Cauer 元件表示的 *n* 个热阻值的行向量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.1, 1, 5]` `s`（默认）| `[1, 10]` `s` | 正值向量

*n* 个热时间常数值的行向量，其中 *n* 是热网络中使用的 Cauer 元件数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化时，热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[3, 10, 25]` `J/K`（默认）| `[33, 50]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 n 是热网络中使用的 Cauer 元件数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal masses`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

由温度值组成的行向量，对应于模型中每个热容上的温度降。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Diode thermal resistances, [R1 R2 … Rn]** — 集成二极管的热阻 `[.03, .1, .2]``K/W`（默认）| `[.03, .2]` `K/W` | 正值向量

*自 R2024a 起*

由 *n* 个热阻值组成的行向量，用于集成保护二极管，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports for upper and lower devices** 参数。
  - 选中 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Diode thermal time constants, [t1 t2 … tn]** — 集成二极管的热时间常数 `[.1, 1, 5]` `s`（默认）| `[1, 10]` `s` | 正值向量

*自 R2024a 起*

由 *n* 个热时间常数值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中使用的 Cauer 元件数量。此向量的长度必须与 **Diode thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式时，热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 ith 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal ports for upper and lower devices** 参数。
  - 选中 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Diode thermal masses, [M1 M2 … Mn]** — 积分二极管的热质量 `[3, 10, 25]` `J/K`（默认）| `[33, 50]` `J/K` | 正值向量

*自 R2024a 起*

积分保护二极管的 *n* 个热质量值的行向量，其中 n 是热网络中使用的 Cauer 元件数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal masses`。

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — 二极管热质量的初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024a 起*

积分保护二极管的温度值行向量。此参数对应于模型中每个热容上的温度降。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Cauer model`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结点开始的每个节点的绝对温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Diode initial node temperatures, [T1 T2 ... Tn]** — 积分二极管的初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024a 起*

从积分保护二极管结点开始的每个节点的绝对温度值行向量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结点的热质量 `0.1` `J/K`（默认）| 正标量

结点的热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `External`。

### **Diode junction thermal mass** — 二极管结点的热质量 `0.1` `J/K`（默认）| 正标量

*自 R2024a 起*

二极管结点的热质量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Yes`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal ports for upper and lower devices** 参数。
  - 选择 **Separate thermal ports for integral diodes** 参数。
  - 将 **Thermal network** 设置为 `External`。

有关使用热端口的更多信息以及其他 **Thermal Port** 参数，请参阅 Simulating Thermal Effects in Semiconductors。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024a：上管、下管和集成二极管具有独立的热端口

现在，通过选择 **Separate thermal ports for upper and lower devices** 参数，可以将热端口 **H** 分离为分别与上管和下管开关器件关联的两个不同热端口。如果为上管和下管器件分离热端口，则还可以通过选择 **Separate thermal ports for integral diodes** 参数，进一步为每个开关器件的集成二极管分离热端口。

上管和下管开关器件共享相同的热参数。

### R2024a：对表格化的反向 I-V 特性进行建模

现在，可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来为 Half-Bridge (Ideal, Switching) 模块建模反向 I-V 特性。

在 R2024a 之前，只能通过指定反向偏置二极管的关断电导来建模反向 I-V 特性。

### R2023b：确定不连续负载电流的开关损耗

如果将 **Switching device** 参数设置为 `MOSFET` 或 `IGBT`，Half-Bridge (Ideal, Switching) 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件中测量断态电压和通态电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用此行为。如果使用定步长求解器，最短的器件导通或关断周期现在为一个步长。在 R2023b 之前，最小周期为三个步长。要报告开关损耗，最小周期仍为三个步长。

在 R2023b 之前，该模块仅在开通前测量断态电压，在关断前测量通态电流。

由于此变更，如果在早期版本中创建的模型使用了 Half-Bridge (Ideal, Switching) 模块以及建模电容或电荷的外部二极管，则必须更新该模型。最佳选择是在 Half-Bridge (Ideal, Switching) 模块内部建模二极管。要在外部建模二极管，请在不含电容或电荷的情况下对其进行建模。

### R2023b：将开关损耗施加到电源

现在，通过选择 **Apply switching losses to electrical supply** 参数，可以从电源中抽取由开关损耗引起的功率。在 R2023a 之前，该模块仅将开关损耗施加到热节点，将节点温度升高所需的值。

### R2023b：使用温度、电流和电压对开关损耗进行表格化

如果将 **Switching device** 参数设置为 `MOSFET` 或 `IGBT`，现在可以使用温度、电流和电压对开关损耗进行表格化。在早期版本中，只能使用温度和电流对开关损耗进行表格化。

## 描述

带理想开关和热端口的半桥

Half-Bridge (Ideal, Switching) 模块对带理想开关和热端口的半桥进行建模。要选择理想开关器件，请将 **Switching device** 参数设置为 `MOSFET`、`IGBT` 或 `GTO`。

可以为每个开关器件指定一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然关断向负载供电的电压时，感性负载可能产生高反向电压尖峰。

**注意**

最佳选择是在 Half-Bridge (Ideal, Switching) 模块内部建模二极管。要在外部建模二极管，请在不含电容或电荷的情况下对其进行建模。

### 开关损耗

关于模块如何建模开通和关断损耗的信息，请参阅 MOSFET (Ideal, Switching) 模块、IGBT (Ideal, Switching) 模块或 GTO 模块的文档页面，具体取决于您为 **Switching Device** 参数选择的选项。这些模块与 Half-Bridge (Ideal, Switching) 模块在损耗建模方式上的主要区别在于，对于 `MOSFET` 和 `IGBT` 选项，Half-Bridge (Ideal, Switching) 模块不使用 **Use last on-state current from previous cycle for turn-on loss** 或 **Use last off-state voltage from previous cycle for turn-off loss** 参数。造成这一区别的原因是，Half-Bridge (Ideal, Switching) 模块不建模二极管电容或引线电感，因为该模块设计用于使用理想开关进行快速仿真。通过在一个模块中建模两个开关器件，您可以避免测量二极管反向恢复的开态电流和关态电压所带来的复杂性，因此不需要基于物理的二极管电荷模型。模块在您命令互补开关器件关断的时刻测量二极管正向电流和关态电压。

默认情况下，模块仅将开关损耗施加到热节点，将节点温度升高所需的值。若要从电源汲取开关损耗所需的功率，请选择 **Apply switching losses to electrical supply** 参数。

瞬时将开关损耗施加到电源在数学上是不可能的，因此模块在等于您为 **Averaging period for switching losses** 参数指定的值的时间段内施加开关损耗。将此值设置为栅极驱动器的脉宽调制 (PWM) 周期。

**注意**

对于所有理想开关器件，记录的仿真数据将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。这些变量以脉冲形式包含损耗，其幅度等于能量损耗。如果您使用脚本对定义的仿真时间段内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录的数据中提取导通损耗和开关损耗。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。

您还可以从记录的仿真数据中各自的 `accumulatedSwitchingLosses` 变量访问两个开关器件各自的总累积开关损耗。这些变量汇总了迄今为止的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆导通损耗。

如果您使用固定步长求解器，支持捕获开关损耗的最短脉冲开启或脉冲关闭时间为三个时间步长。如果脉冲短于三个步长，模块不会报告开关损耗。

如果您使用表格数据来建模开关损耗或反向恢复损耗，请检查温度、电流和电压是否在您指定的范围内。如果您未定义真实的热模型，例如，如果结质量或从结到壳体的热导过小，温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### 参数化

半桥（理想，开关）模块支持多个预定义参数化。

使用此参数化数据来表示特定供应商的组件。这些半桥的参数化与制造商数据手册相匹配。要加载预定义参数化，请双击半桥（理想，开关）模块，单击**选定部件**参数的 **<click to select>** 超链接，然后在模块参数化管理器窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化的更多信息以及可用组件列表，请参阅预参数化组件列表。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取开关器件和集成保护二极管的器件参数，并将其导入模块中。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 或 Infineon® 支持的参数化格式。

### 热端口

使用热端口来模拟产生的热量和器件温度的影响。有关使用热端口和**热端口**参数的更多信息，请参阅半导体热效应仿真。

您还可以通过选择**为上下器件分离热端口**参数，将热端口 **H** 分离为分别与上部和下部开关器件关联的两个不同热端口。如果为上下器件分离热端口，则还可以通过选择**为集成二极管分离热端口**参数，为每个开关器件的集成二极管分离热端口。上部和下部开关器件共享相同的热参数。*（自 R2024a 起）*

下图显示了暴露所有热端口时的模块图标：

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关更多信息，请参阅设置模块变量的优先级和初始目标。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的**标称值**部分。有关更多信息，请参阅基于标称值的系统缩放。
