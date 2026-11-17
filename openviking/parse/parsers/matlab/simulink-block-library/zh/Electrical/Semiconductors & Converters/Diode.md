---
type: simulink-block
title: 'Diode'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: zh-CN
chinese_source: worker-translation
---

# Diode

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与阳极关联的电气守恒端口。

### **-** — 负极端子电气

与阴极关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Selected part
  summary: 预定义参数化选项 <click to select>（默认）
  group: ''
- name: Fidelity level
  summary: 保真度级别 Include capacitance and charge dynamics（默认）| Ideal switching
  group: 主
- name: Diode model
  summary: 二极管模型 Piecewise Linear（默认）| Exponential | Tabulated I-V curve
  group: 主
- name: Table type
  summary: 表格化函数 Table in If(Tj,Vf) form（默认）| Table in Vf(Tj,If) form
  group: 主
- name: Forward voltage
  summary: 正向电压 0.6 V（默认）
  group: 主
- name: On resistance
  summary: 导通电阻 0.3 Ohm（默认）
  group: 主
- name: Off conductance
  summary: 关断电导 1e-8 1/Ohm（默认）
  group: 主
- name: Parameterization
  summary: 模型参数化 Use two I-V curve data points（默认）| Use parameters IS and N | Use an I-V data point and IS | Use an I-V data
    point and N
  group: 主
- name: Currents [I1 I2]
  summary: 两个点处的电流值向量 [.0137, .545] A（默认）
  group: 主
- name: Voltages [V1 V2]
  summary: 两个点处的电压值向量 [.6, .7] V（默认）
  group: 主
- name: Saturation current, IS
  summary: 饱和电流 1e-12 A（默认）
  group: 主
- name: Emission coefficient, N
  summary: 二极管发射系数 1（默认）
  group: 主
- name: Current I1
  summary: 电流值 0.0137 A（默认）
  group: 主
- name: Voltage V1
  summary: 电压值 0.6 V（默认）
  group: 主
- name: Ohmic resistance, RS
  summary: 欧姆电阻 0 Ohm（默认）
  group: 主
- name: Measurement temperature
  summary: 测量温度 298.15 K（默认）
  group: 主
- name: Forward currents, If(Tj,Vf)
  summary: 正向电流向量 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）| 非负向量
  group: 主
- name: Forward voltages, Vf(Tj,If)
  summary: 正向电压向量 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）| 非负向量
  group: 主
- name: Junction temperatures, Tj
  summary: 结温向量 [25, 125] degC（默认）
  group: 主
- name: Forward voltages, Vf
  summary: 正向电压向量 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）
  group: 主
- name: Forward currents, If
  summary: 正向电流向量 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）
  group: 主
- name: Reverse currents, Ir(Tj,Vr)
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005] A（默认）|
    非负向量
  group: 主
- name: Reverse voltages, Vr
  summary: 反向电压向量 [10, 20, 40, 50, 70, 80, 100] V（默认）
  group: 主
- name: Reverse voltages, Vr(Tj,Ir)
  summary: 反向电压向量 [10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320] V（默认）| 非负向量
  group: 主
- name: Reverse currents, Ir
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001] A（默认）
  group: 主
- name: Number of series diodes
  summary: 串联连接的二极管数量 1（默认）
  group: 主
- name: Number of parallel diodes
  summary: 并联二极管数量 1（默认）
  group: 主
- name: Model Zener diode
  summary: 建模齐纳二极管的选项 Off（默认）| On
  group: 主
- name: Zener resistance
  summary: 齐纳电阻 0.3 Ohm（默认）| 正标量
  group: 击穿
- name: Reverse breakdown voltage
  summary: 反向击穿电压 inf V（默认）| 正标量
  group: 击穿
- name: Parameterization
  summary: 建模结电容 Fixed or zero junction capacitance（默认）| Use C-V curve data points | Use parameters CJ0, VJ, M & FC
  group: 电容
- name: Junction capacitance
  summary: 结电容 0 pF（默认）
  group: 电容
- name: Reverse bias voltages [VR1 VR2 VR3]
  summary: 反向偏置电压值向量 [.1, 10, 100] V（默认）
  group: 电容
- name: Corresponding capacitances [C1 C2 C3]
  summary: 电容值向量 [3.5, 1, .4] pF（默认）
  group: 电容
- name: Zero-bias junction capacitance, CJ0
  summary: 零偏结电容 5 pF（默认）
  group: 电容
- name: Junction potential, VJ
  summary: 结电势 1 V（默认）
  group: 电容
- name: Grading coefficient, M
  summary: 梯度系数 0.5（默认）
  group: 电容
- name: Capacitance coefficient, FC
  summary: 电容系数 0.5（默认）
  group: 电容
- name: Charge dynamics
  summary: 电荷动态参数化 Do not model charge dynamics（默认）| Use peak reverse current and stretch factor | Use peak reverse current
    and reverse recovery time | Use peak reverse current and reverse recovery charge | Use peak reverse current and reverse
    recovery energy | Use transit time and carrier lifetime
  group: 电容
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -7.15 A（默认）| 负标量
  group: 电容
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 4 A（默认）| 正标量
  group: 电容
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -750 A/μs（默认）| 负标量
  group: 电容
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）
  group: 电容
- name: Reverse recovery time, trr
  summary: 反向恢复时间 115（默认）
  group: 电容
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 s*μA（默认）
  group: 电容
- name: Diode turn-off voltage when measuring Erec
  summary: 测量 Erec 时的二极管关断电压 -600 V（默认）
  group: 电容
- name: Stray inductance when measuring Erec
  summary: 测量 Erec 时的杂散电感 150 nH（默认）
  group: 电容
- name: Reverse recovery energy, Erec
  summary: 反向恢复能量 0.03 J（默认）
  group: 电容
- name: Transit time, TT
  summary: 渡越时间 50 ns（默认）
  group: 电容
- name: Carrier lifetime, tau
  summary: 载流子寿命 100 ns（默认）
  group: 电容
- name: Reverse recovery loss model
  summary: 反向恢复损耗模型 Fixed loss（默认）| Tabulated loss
  group: Reverse Recovery Loss
- name: Reverse recovery loss
  summary: 反向恢复损耗 0 J（默认）| 非负标量
  group: Reverse Recovery Loss
- name: Scale reverse recovery loss with current and voltage
  summary: 按电流和电压缩放反向恢复损耗的选项 On（默认）| Off
  group: Reverse Recovery Loss
- name: Forward current when measuring recovery loss, Irec
  summary: 模块测量恢复损耗时的正向电流 10 A（默认）| 正标量
  group: Reverse Recovery Loss
- name: Turn-off voltage when measuring recovery loss, Vrec
  summary: 测量恢复损耗时的关断电压 10 V（默认）| 正标量
  group: Reverse Recovery Loss
- name: Filter time constant for voltage and current values
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认）| 正标量
  group: Reverse Recovery Loss
- name: Reverse recovery loss table, Erec(Tj, If)
  summary: 反向恢复损耗表 zeros(2, 3) J（默认）| 非负标量向量
  group: Reverse Recovery Loss
- name: Temperature vector for recovery loss table, Tj
  summary: 恢复损耗表的温度向量 [298.15, 398.15] K（默认）| 向量
  group: Reverse Recovery Loss
- name: Forward current vector for recovery loss table, If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] A（默认）| 非负标量向量
  group: Reverse Recovery Loss
- name: Parameterization
  summary: 温度依赖性参数化 None - Use characteristics at parameter measurement temperature（默认）| Use an I-V data point at second measurement
    temperature | Specify saturation current at second measurement temperature | Specify the energy gap EG
  group: Temperature Dependence
- name: Current I1 at second measurement temperature
  summary: 第二测量温度下的电流 I1 0.0245 A（默认）
  group: Temperature Dependence
- name: Voltage V1 at second measurement temperature
  summary: 第二测量温度下的电压 V1 0.5 V（默认）
  group: Temperature Dependence
- name: Saturation current, IS, at second measurement temperature
  summary: 第二测量温度下的饱和电流 IS 1.25e-7 A（默认）
  group: Temperature Dependence
- name: Second measurement temperature
  summary: 第二测量温度 125 °C（默认）
  group: Temperature Dependence
- name: Energy gap parameterization
  summary: 能隙参数化 Use nominal value for silicon (EG=1.11eV)（默认）| Use nominal value for 4H-SiC silicon carbide (EG=3.23eV) |
    Use nominal value for 6H-SiC silicon carbide (EG=3.00eV) | Use nominal value for germanium (EG=0.67eV) | Use nominal value
    for gallium arsenide (EG=1.43eV) | Use nominal value for selenium (EG=1.74eV) | Use nominal value for Schottky barrier
    diodes (EG=0.69eV) | Specify a custom value
  group: Temperature Dependence
- name: Energy gap, EG
  summary: 能隙 1.11 eV（默认）
  group: Temperature Dependence
- name: Saturation current temperature exponent parameterization
  summary: 饱和电流温度指数参数化 Use nominal value for pn-junction diode (XTI=3)（默认）| Use nominal value for Schottky barrier diode (XTI=2)
    | Specify a custom value
  group: Temperature Dependence
- name: Saturation current temperature exponent, XTI
  summary: 饱和电流温度指数 3（默认）
  group: Temperature Dependence
- name: Reverse breakdown voltage temperature coefficient, dBV/dT
  summary: 反向击穿电压温度系数 0 V/K（默认）
  group: Temperature Dependence
- name: Device simulation temperature
  summary: 器件仿真温度 25 °C（默认）
  group: Temperature Dependence
- name: Diode fault
  summary: 对二极管中的故障进行建模的选项 Add fault（默认）
  group: 故障
- name: Failure mode
  summary: 故障类别 Open（默认）| Short | Parameter shift
  group: 故障
- name: Fault transition time constant
  summary: 故障过渡时间常数 1e-3 s（默认）| 正标量
  group: 故障
- name: Faulted series resistance
  summary: 故障串联电阻 1000 Ohm（默认）| 有限非负标量
  group: 故障
- name: Faulted parallel conductance
  summary: 故障并联电导 1000 1/Ohm（默认）| 有限非负标量
  group: 故障
- name: Faulted forward voltage
  summary: 故障正向电压 0.6 V（默认）| 正标量
  group: 故障
- name: Faulted on resistance
  summary: 故障导通电阻 0.3 Ohm（默认）| 正标量
  group: 故障
- name: Faulted off conductance
  summary: 故障关断电导 1e-8 S（默认）| 正标量
  group: 故障
- name: Faulted zener resistance
  summary: 故障齐纳电阻 0.3 Ohm（默认）| 正标量
  group: 故障
- name: Faulted reverse breakdown voltage
  summary: 故障反向击穿电压 inf V（默认）| 正标量
  group: 故障
- name: Faulted currents, [I1 I2]
  summary: 故障电流 [.0137, .545] A（默认）| 正标量的二维向量
  group: 故障
- name: Faulted voltages, [V1 V2]
  summary: 故障电压 [.6, .7] V（默认）| 正标量的二维向量
  group: 故障
- name: Faulted ohmic resistance, RS
  summary: 故障电压 0 Ohm（默认）| 非负标量
  group: 故障
- name: Faulted saturation current, IS
  summary: 故障饱和电流 1e-12 A（默认）| 正标量
  group: 故障
- name: Faulted emission coefficient, N
  summary: 故障发射系数 1（默认）| 正标量
  group: 故障
- name: Faulted current, I1
  summary: 故障电流 0.0137 A（默认）| 正标量
  group: 故障
- name: Faulted voltage, V1
  summary: 故障电压 0.6 V（默认）| 正标量
  group: 故障
- name: Faulted forward currents, If(Tj,Vf)
  summary: 故障正向电流 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）| 非负标量矩阵
  group: 故障
- name: Faulted forward voltages, Vf
  summary: 故障正向电压 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）| 非负标量向量
  group: 故障
- name: Faulted reverse currents, Ir(Tj,Vr)
  summary: 故障反向电流 [1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005] A（默认）|
    非负标量矩阵
  group: 故障
- name: Faulted reverse voltages, Vr
  summary: 故障反向电压 [1, 2, 4, 5, 7, 8, 10] V（默认）| 非负标量向量
  group: 故障
- name: Faulted forward voltages, Vf(Tj,If)
  summary: 故障正向电压 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）| 非负标量矩阵
  group: 故障
- name: Faulted forward currents, If
  summary: 故障正向电流 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）| 非负标量向量
  group: 故障
- name: Faulted reverse voltages, Vr(Tj,Ir)
  summary: 故障反向电压 [1, 10, 20, 25, 30, 32.5, 35; 1, 5, 10, 20, 25, 30, 32] V（默认）| 非负标量矩阵
  group: 故障
- name: Faulted reverse currents, Ir
  summary: 故障反向电流 [1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001] A（默认）| 非负标量向量
  group: 故障
- name: Faulted capacitance and charge as percentage of unfaulted
  summary: 故障电容和电荷占未故障状态的百分比 100（默认）| 有限正标量
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible reverse voltage
  summary: 最大允许反向电压 inf V（默认）| 正标量
  group: 故障
- name: Number of events to fail when exceeding voltage
  summary: 超过电压时失效的事件数 1（默认）| 正整数标量
  group: 故障
- name: Maximum permissible current
  summary: 故障转换的电流阈值 inf A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding current
  summary: 电流超过阈值的最大持续时间 1 s（默认）| 非负标量
  group: 故障
- name: Maximum diode recovery, dV/dt
  summary: 二极管恢复阈值 inf V/s（默认）| 正标量
  group: 故障
- name: Maximum permissible temperature
  summary: 故障转换的温度阈值 inf K（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding temperature
  summary: 超过温度时失效的时间 1 s（默认）| 正标量
  group: 故障
- name: Thermal network
  summary: 热网络建模选项 External（默认）| Specify junction and case thermal parameters | Cauer model | Cauer model parameterized with
    Foster coefficients
  group: 热端口
- name: Thermal mass parameterization
  summary: 热质量参数化选项 By thermal time constants（默认）| By thermal mass
  group: 热端口
- name: Junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 结-壳和壳-环境（或壳-散热器）热阻 [0, 10] K/W（默认）| 非负值向量
  group: 热端口
- name: Junction and case thermal time constants, [t_J t_C]
  summary: 结和壳热时间常数 [0, 10] s（默认）| 非负值向量
  group: 热端口
- name: Junction and case thermal masses, [M_J M_C]
  summary: 结和壳热质量 [0, 1] J/K（默认）| 正值向量
  group: 热端口
- name: Junction and case initial temperatures, [T_J T_C]
  summary: 结和壳初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal resistances, [R1 R2 … Rn]
  summary: 热阻 [1, 3, 10] K/W | [4, 6] K/W | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [.1, .3, 1] J/K | [1.5, 3] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal time constants, [t1 t2 … tn]
  summary: 热时间常数 [1, 3, 10] s | [6, 18] s | 正值向量
  group: 热端口
- name: Initial node temperatures, [T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Junction thermal mass
  summary: 结的热质量 0.01 J/K（默认）| 正标量
  group: 热端口
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并建模所产生的热量和设备温度的影响。

### **Selected part** — 预定义参数化选项 `<click to select>`（默认）

将模块参数化以表示特定供应商的组件的选项。点击
**<click to select>** 超链接以打开 Block
Parameterization Manager 窗口。有关 Block Parameterization
Manager 的详细信息，请参阅 Load Predefined Parameterizations。

### 主

### **Fidelity level** — 保真度级别 `Include capacitance and charge dynamics`（默认）| `Ideal switching`

二极管动态模型的详细程度。如果选择 `Ideal
switching`，模块仅建模反向恢复损耗。如果选择
`Include capacitance and charge dynamics`，模块同时建模
结电容和电荷动态。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show
thermal port`。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Exponential` | `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用二极管的分段线性模型，
  如 Piecewise Linear Diode 中所述。这是默认方法。
- `Exponential` — 使用二极管的标准指数模型，
  如 Exponential Diode 中所述。
- `Tabulated I-V curve` — 使用表格化的正向偏置
  I-V 数据加上固定的反向偏置关断电导，如 Tabulated Diode 中所述。

### **Table type** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是将电压
表格化为温度和电流的函数。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Tabulated I-V curve`。

### **Forward voltage** — 正向电压 `0.6` `V`（默认）

使二极管变为正向偏置所需施加的最小电压。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Piecewise linear`。

### **On resistance** — 导通电阻 `0.3` `Ohm`（默认）

二极管正向偏置时的电阻。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Piecewise linear`。

### **Off conductance** — 关断电导 `1e-8` `1/Ohm`（默认）

二极管反向偏置时的电导。当 **Model Zener diode**
参数被清除时，模块使用此值来确定反向 I-V 特性。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Piecewise linear` 或 `Tabulated I-V
curve`。

### **Parameterization** — 模型参数化 `Use two I-V curve data points`（默认）| `Use parameters IS and N` | `Use an I-V data point and IS` | `Use an I-V data point and N`

选择以下模型参数化方法之一：

- `Use two I-V curve data points` — 指定二极管 I-V 曲线上两个点的测量
  数据。这是默认方法。
- `Use parameters IS and N` — 指定饱和电流
  和发射系数。
- `Use an I-V data point and IS` — 指定二极管 I-V 曲线上单个点的测量数据
  并结合饱和电流。
- `Use an I-V data point and N` — 指定二极管 I-V 曲线上单个点的测量数据
  并结合发射系数。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`。

### **Currents [I1 I2]** — 两个点处的电流值向量 `[.0137, .545]` `A`（默认）

模块用于计算 *IS* 和 *N* 的二极管 I-V 曲线上两个点处的
电流值向量。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use two I-V curve data points`。

### **Voltages [V1 V2]** — 两个点处的电压值向量 `[.6, .7]` `V`（默认）

模块用于计算 *IS* 和 *N* 的二极管 I-V 曲线上两个点处的
电压值向量。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use two I-V curve data points`。

### **Saturation current, IS** — 饱和电流 `1e-12` `A`（默认）

理想二极管方程在非常大的反向偏置水平下渐近逼近的
电流幅值。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use parameters IS and N` 或 `Use an I-V data point
and IS`。

### **Emission coefficient, N** — 二极管发射系数 `1`（默认）

二极管发射系数或理想因子。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use parameters IS and N` 或 `Use an I-V data point
and N`。

### **Current I1** — 电流值 `0.0137` `A`（默认）

模块用于计算的二极管 I-V 曲线上该点处的电流值。
根据 **Parameterization** 的值，模块使用此参数
计算 *N* 或 *IS*。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use an I-V data point and IS` 或 `Use an I-V data
point and N`。

### **Voltage V1** — 电压值 `0.6` `V`（默认）

模块用于计算的二极管 I-V 曲线上该点处的电压值。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`，并将 **Parameterization** 设置为
`Use an I-V data point and IS` 或 `Use an I-V data
point and N`。

### **Ohmic resistance, RS** — 欧姆电阻 `0` `Ohm`（默认）

串联二极管连接电阻。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Exponential`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认）

测量 IS 或 I-V 曲线时的温度 *Tm1*。

### **Forward currents, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*If(Tj,Vf)* = 0A）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负向量

正向电压。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Vf(Tj,If)* = 0V）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
Vf(Tj,If) form`。

### **Junction temperatures, Tj** — 结温向量 `[25, 125]` `degC`（默认）

结温向量。

如果向量的大小等于 `1`，则二极管特性
不依赖于温度。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Tabulated I-V curve`。

### **Forward voltages, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压向量。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Vf* =
0V）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
If(Tj,Vf) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*If* =
0A）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
Vf(Tj,If) form`。

### **Reverse currents, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
If(Tj,Vf) form` 并选中 **Model Zener diode**
参数。

### **Reverse voltages, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认）

*自 R2024a 起*

反向电压向量。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Vr* =
0V）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
If(Tj,Vf) form` 并选中 **Model Zener diode**
参数。

### **Reverse voltages, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Vr(Tj,Ir)* = 0V）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
Vf(Tj,If) form` 并选中 **Model Zener diode**
参数。

### **Reverse currents, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）

*自 R2024a 起*

反向电流向量。此参数必须是至少包含三个非负元素的向量，
且按升序排列。零点可选（*Ir* =
0A）。

#### 依赖关系

要启用此参数，请将 **Table type** 设置为 `Table in
Vf(Tj,If) form` 并选中 **Model Zener diode**
参数。

### **Number of series diodes** — 串联连接的二极管数量 `1`（默认）

在 **+** 和 **–** 模块端口之间串联连接的二极管数量。
不会建模多个二极管。而是每个二极管的所有电压相关量都按
您指定的因子进行缩放。

### **Number of parallel diodes** — 并联二极管数量 `1`（默认）

在 **+** 和 **–** 模块端口之间的并联二极管数量，或由串联连接
的二极管形成的并联路径数量。不会建模多个
二极管。而是每个二极管的所有电流相关量都按
您指定的因子进行缩放。

### **Model Zener diode** — 建模齐纳二极管的选项 `Off`（默认）| `On`

*自 R2023b 起*

建模齐纳二极管的选项。

选择此参数以建模在正向和反向偏置方向上均导通的齐纳二极管。模块图标显示齐纳二极管的电子符号，并且您
启用 **Breakdown** 选项卡中的参数。您必须为 **Reverse breakdown voltage** 参数指定一个有限
值。

当您选择此选项时，您可以通过指定新的 **Reverse
voltages, Vr(Tj,Ir)**、**Reverse currents, Ir(Tj,Vr)**、
**Reverse voltages, Vr** 和 **Reverse currents, Ir**
参数来为 Diode 模块建模反向 I-V 特性。*（自 R2024a 起）*

清除此参数以建模仅在单一方向上导通的标准二极管。
模块假定反向击穿电压为无穷大，这实际上从模型中省略了
反向击穿。模块图标显示标准二极管的电子符号。

### 击穿

要启用这些参数，请选中 **Model Zener diode**
参数。

### **Zener resistance** — 齐纳电阻 `0.3` `Ohm`（默认）| 正标量

当电压小于 **Reverse breakdown
voltage** 值时二极管的电阻。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Piecewise linear`。

### **Reverse breakdown voltage** — 反向击穿电压 `inf` `V`（默认）| 正标量

低于该反向电压时建模二极管击穿时发生的电导快速增加。

#### 依赖关系

要启用此参数，请将 **Diode model** 设置为
`Piecewise linear` 或
`Exponential`。

### 电容

要启用这些参数，请将 **Modeling option** 设置为 `No
thermal port` 或将 **Fidelity level** 设置为 `Include
capacitance and charge dynamics`。

### **Parameterization** — 建模结电容 `Fixed or zero junction capacitance`（默认）| `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

建模结电容的方法：

- `Fixed or zero junction capacitance` — 将
  结电容建模为固定值。
- `Use C-V curve data points` — 指定二极管 C-V 曲线上三个点的测量数据。
- `Use parameters CJ0, VJ, M & FC` — 指定
  零偏结电容、结电势、梯度系数和正向偏置
  耗尽电容系数。

### **Junction capacitance** — 结电容 `0` `pF`（默认）

固定结电容值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Fixed or zero junction capacitance`。

### **Reverse bias voltages [VR1 VR2 VR3]** — 反向偏置电压值向量 `[.1, 10, 100]` `V`（默认）

模块用于计算 *CJ0*、*VJ* 和
*M* 的二极管 C-V 曲线上三个点处的反向偏置电压值
向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
C-V curve data points`。

### **Corresponding capacitances [C1 C2 C3]** — 电容值向量 `[3.5, 1, .4]` `pF`（默认）

模块用于计算 *CJ0*、*VJ* 和
*M* 的二极管 C-V 曲线上三个点处的电容值
向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
C-V curve data points`。

### **Zero-bias junction capacitance, CJ0** — 零偏结电容 `5` `pF`（默认）

与传导电流项并联放置的电容值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **Junction potential, VJ** — 结电势 `1` `V`（默认）

结电势。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **Grading coefficient, M** — 梯度系数 `0.5`（默认）

梯度系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **Capacitance coefficient, FC** — 电容系数 `0.5`（默认）

量化耗尽电容随施加电压降低的拟合系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **Charge dynamics** — 电荷动态参数化 `Do not model charge dynamics`（默认）| `Use peak reverse current and stretch factor` | `Use peak reverse current and reverse recovery time` | `Use peak reverse current and reverse recovery charge` | `Use peak reverse current and reverse recovery energy` | `Use transit time and carrier lifetime`

选择以下电荷动态参数化方法之一：

- `Do not model charge dynamics` — 不包含电荷动态建模。这是默认方法。
- `Use peak reverse current and stretch factor` — 通过提供峰值反向电流 *iRM* 和拉伸因子 *λ* 的值，以及在测量 *iRM* 和 *trr* 时测试电路中使用的初始正向电流和电流变化率信息，来对电荷动态进行建模。
- `Use peak reverse current and reverse recovery time` — 通过提供峰值反向电流 *iRM* 和反向恢复时间 *trr* 的值，以及在测量 *iRM* 和 *trr* 时测试电路中使用的初始正向电流和电流变化率信息，来对电荷动态进行建模。如果制造商数据手册未提供渡越时间 *TT* 和载流子寿命 *τ* 的值，请使用此选项。
- `Use peak reverse current and reverse recovery charge` — 通过提供峰值反向电流 *iRM* 和反向恢复电荷 *Qrr* 的值，以及在测量 *iRM* 和 *trr* 时测试电路中使用的初始正向电流和电流变化率信息，来对电荷动态进行建模。
- `Use peak reverse current and reverse recovery energy` — 通过提供峰值反向电流 *iRM* 和反向恢复能量 *Erec* 的值，以及在测量 *iRM* 时测试电路中使用的初始正向电流和电流变化率信息，来对电荷动态进行建模。
- `Use transit time and carrier lifetime` — 通过提供渡越时间 *TT* 和载流子寿命 *τ* 的值，来对电荷动态进行建模。

### **Peak reverse current, iRM** — 峰值反向电流 `-7.15` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `4` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-750` `A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。此值必须大于 `1`。默认值为 `3`。

指定拉伸因子是比指定反向恢复电荷更简便的反向恢复时间参数化方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and stretch factor`。

### **Reverse recovery time, trr** — 反向恢复时间 `115`（默认）

从二极管关断时电流初始降至零的点，到电流降至峰值反向电流的百分之十以下的点之间的时间。默认值为 `115` `ns`。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and reverse recovery time`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*μA`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管器件数据手册指定了反向恢复电荷的值而非反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and reverse recovery charge`。

### **Diode turn-off voltage when measuring Erec** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

二极管处于稳态时的电压。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and reverse recovery energy`。

### **Stray inductance when measuring Erec** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值来计算 **Reverse recovery energy, Erec**。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and reverse recovery energy`。

### **Reverse recovery energy, Erec** — 反向恢复能量 `0.03` `J`（默认）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use peak reverse current and reverse recovery energy`。

### **Transit time, TT** — 渡越时间 `50` `ns`（默认）

载流子穿过二极管结所需时间的度量。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use transit time and carrier lifetime`。

### **Carrier lifetime, tau** — 载流子寿命 `100` `ns`（默认）

二极管不再导通后载流子消散所需时间的度量。默认值为 `100` `ns`。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Use transit time and carrier lifetime`。

### Reverse Recovery Loss

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`，并将 **Fidelity level** 设置为 `Ideal switching`。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

选择对固定反向恢复损耗还是表格化反向恢复损耗进行建模。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

每次关断事件中耗散的能量，无论开关事件前后二极管的状态如何。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 按电流和电压缩放反向恢复损耗的选项 `On`（默认）| `Off`

*自 R2023b 起*

按电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2023b 起*

模块用于测量恢复损耗的反向恢复事件之前通过二极管的正向电流。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

用于测量恢复损耗的反向恢复事件之后二极管两端的电压。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。请将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Reverse recovery loss table, Erec(Tj, If)** — 反向恢复损耗表 `zeros(2, 3)` `J`（默认）| 非负标量向量

作为开关事件之前正向电流 *If* 以及二极管处于关断状态后最终关态电压的函数的耗散能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15, 398.15]` `K`（默认）| 向量

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `A`（默认）| 非负标量向量

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Tabulated loss`。

### Temperature Dependence

本节仅适用于 `Exponential` 和 `Tabulated I-V curve` 二极管模型。

此表显示了 **Temperature Dependence** 设置的可见性如何取决于您在 **Main** 设置中配置 **Diode model** 参数的方式以及是否暴露热端口。要了解如何阅读此表，请参阅参数依赖关系

**Temperature Dependence 设置的可见性**

| 参数、选项和设置的可见性 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Diode model** | | | | | | | |
| *`Piecewise linear`* | | | | *`Exponential`* | | *`Tabulated I-V curve`* | |
| **Thermal Port** | | | | **Thermal Port** | | **Thermal Port** | |
| *`Not exposed`* | *`Exposed`* | | | *`Not exposed`* | *`Exposed`* | *`Not exposed`* | *`Exposed`* |
| 隐藏 | 隐藏 | | | 可见 | 可见 | 可见 | 隐藏 |

### **Parameterization** — 温度依赖性参数化 `None - Use characteristics at parameter measurement temperature`（默认）| `Use an I-V data point at second measurement temperature` | `Specify saturation current at second measurement temperature` | `Specify the energy gap EG`

选择以下温度依赖性参数化方法之一：

- `None - Use characteristics at parameter measurement temperature` — 不对温度依赖性进行建模，或者模型在测量温度 *T*m1（由 **Main** 选项卡上的 **Measurement temperature** 参数指定）下仿真。这是默认方法。
- `Use an I-V data point at second measurement temperature T2` — 如果选择此选项，您需要指定第二个测量温度 *T*m2，以及该温度下的电流和电压值。模型使用这些值以及第一个测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify saturation current at second measurement temperature T2` — 如果选择此选项，您需要指定第二个测量温度 *T*m2，以及该温度下的饱和电流值。模型使用这些值以及第一个测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify the energy gap EG` — 直接指定能隙值。

### **Current I1 at second measurement temperature** — 第二测量温度下的电流 I1 `0.0245` `A`（默认）

指定在第二测量温度下电压为 *V1* 时的二极管电流 *I1* 值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use an I-V data point at second measurement temperature`。

### **Voltage V1 at second measurement temperature** — 第二测量温度下的电压 V1 `0.5` `V`（默认）

指定在第二测量温度下电流为 *I1* 时的二极管电压 *V1* 值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use an I-V data point at second measurement temperature`。

### **Saturation current, IS, at second measurement temperature** — 第二测量温度下的饱和电流 IS `1.25e-7` `A`（默认）

指定第二测量温度下的饱和电流 *IS* 值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify saturation current at second measurement temperature`。

### **Second measurement temperature** — 第二测量温度 `125` `°C`（默认）

指定第二测量温度的值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use an I-V data point at second measurement temperature` 或 `Specify saturation current at second measurement temperature`。

### **Energy gap parameterization** — 能隙参数化 `Use nominal value for silicon (EG=1.11eV)`（默认）| `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

从预定选项列表中选择能隙值，或指定自定义值：

- `Use nominal value for silicon (EG=1.11eV)` — 这是默认值。
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — 如果选择此选项，对话框中会出现 **Energy gap, EG** 参数，以便您为 *EG* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify the energy gap EG`。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

为能隙 *EG* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **Energy gap parameterization** 设置为 `Specify a custom value`。

### **Saturation current temperature exponent parameterization** — 饱和电流温度指数参数化 `Use nominal value for pn-junction diode (XTI=3)`（默认）| `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

选择以下选项之一来指定饱和电流温度指数值：

- `Use nominal value for pn-junction diode (XTI=3)` —
  这是默认值。
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — 如果选择此选项，
  对话框中会出现 **Saturation current temperature exponent, XTI** 参数，
  以便您为 *XTI* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

为饱和电流温度指数 *XTI* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`，并将 **Saturation current temperature exponent
parameterization** 设置为 `Specify a custom value`。

### **Reverse breakdown voltage temperature coefficient, dBV/dT** — 反向击穿电压温度系数 `0` `V/K`（默认）

调制反向击穿电压 *BV*。如果将反向击穿电压 *BV* 定义为正值，
则 *TCV* 的正值意味着反向击穿电压的幅值随温度降低而减小。

#### 依赖关系

要启用此参数，请选中 **Model Zener diode** 参数，
并将 **Parameterization** 设置为 `Use an I-V data point at
second measurement temperature`、`Specify saturation current at
second measurement temperature` 或 `Specify the energy gap,
EG`。

### **Device simulation temperature** — 器件仿真温度 `25` `°C`（默认）

指定器件仿真时的温度 *T*s 的值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`。

### 故障

### **Diode fault** — 对二极管中的故障进行建模的选项 `Add fault`（默认）

对 Diode 模块中的故障进行建模的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Failure mode** — 故障类别 `Open`（默认）| `Short` | `Parameter shift`

指定 Diode 模块的故障模式：

- `Open` — 一旦触发故障，串联电阻会瞬时增大。您可以使用此类故障来对因金属化烧毁而失效的二极管进行建模。
- `Short` — 一旦触发故障，并联电导会瞬时增大。您可以使用此选项来对因穿通而失效的二极管进行建模。
- `Parameter shift` — 从触发故障的时刻起，模块参数随时间变化。您可以使用此选项来对因老化而失效的二极管进行建模。

#### 依赖关系

要启用此参数，请通过点击 **Diode fault** 参数中的
**Add fault** 超链接向 Diode 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Fault transition time constant** — 故障过渡时间常数 `1e-3` `s`（默认）| 正标量

过渡到故障状态的时间常数。

#### 依赖关系

要启用此参数，请通过点击 **Diode fault** 参数中的
**Add fault** 超链接向 Diode 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted series resistance** — 故障串联电阻 `1000` `Ohm`（默认）| 有限非负标量

故障状态下的串联电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Failure mode** 设置为 `Open`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted parallel conductance** — 故障并联电导 `1000` `1/Ohm`（默认）| 有限非负标量

故障状态下的并联电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Failure mode** 设置为 `Short`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted forward voltage** — 故障正向电压 `0.6` `V`（默认）| 正标量

故障状态下的正向电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Piecewise
  linear`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted on resistance** — 故障导通电阻 `0.3` `Ohm`（默认）| 正标量

故障状态下的导通电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Piecewise
  linear`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted off conductance** — 故障关断电导 `1e-8` `S`（默认）| 正标量

故障状态下的关断电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Piecewise
  linear`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted zener resistance** — 故障齐纳电阻 `0.3` `Ohm`（默认）| 正标量

故障状态下的关断电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Piecewise
  linear`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted reverse breakdown voltage** — 故障反向击穿电压 `inf` `V`（默认）| 正标量

故障状态下的反向击穿电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Piecewise
  linear`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted currents, [I1 I2]** — 故障电流 `[.0137, .545]` `A`（默认）| 正标量的二维向量

故障状态下的 *I1* 和 *I2* 电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use two I-V curve data
  points`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted voltages, [V1 V2]** — 故障电压 `[.6, .7]` `V`（默认）| 正标量的二维向量

故障状态下的 *V1* 和 *V2* 电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use two I-V curve data
  points`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted ohmic resistance, RS** — 故障电压 `0` `Ohm`（默认）| 非负标量

故障状态下的欧姆电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted saturation current, IS** — 故障饱和电流 `1e-12` `A`（默认）| 正标量

故障状态下的饱和电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use parameters IS and
  N` 或 `Use an I-V data point and IS`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted emission coefficient, N** — 故障发射系数 `1`（默认）| 正标量

故障状态下的发射系数。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use parameters IS and
  N` 或 `Use an I-V data point and N`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted current, I1** — 故障电流 `0.0137` `A`（默认）| 正标量

故障状态下的电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use an I-V data point and
  IS` 或 `Use an I-V data point and N`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted voltage, V1** — 故障电压 `0.6` `V`（默认）| 正标量

故障状态下的电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为
  `Exponential`。
- 将 **Parameterization** 设置为 `Use an I-V data point and
  IS` 或 `Use an I-V data point and N`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted forward currents, If(Tj,Vf)** — 故障正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负标量矩阵

故障状态下的正向电流 *If(Tj,Vf)*。此参数必须是
至少包含三个非负元素且按升序排列的向量。零点为
可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode fault** 参数中的 **Add fault**
  超链接向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in If(Tj,Vf)
  form`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，
**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted forward voltages, Vf** — 故障正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）| 非负标量向量

故障状态下的正向电压 *Vf*。此参数必须是
至少包含三个非负元素且按升序排列的向量。零点为可选
（*Vf* = 0V）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in If(Tj,Vf)
  form`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted reverse currents, Ir(Tj,Vr)** — 故障反向电流 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负标量矩阵

*自 R2024a 起*

故障状态下的反向电流 *Ir(Tj,Vr)*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in If(Tj,Vf)
  form`。
- 选中 **Model Zener diode** 参数。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted reverse voltages, Vr** — 故障反向电压 `[1, 2, 4, 5, 7, 8, 10]` `V`（默认）| 非负标量向量

*自 R2024a 起*

故障状态下的反向电压 *Vr*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*Vr* = 0V）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in If(Tj,Vf)
  form`。
- 选中 **Model Zener diode** 参数。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted forward voltages, Vf(Tj,If)** — 故障正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负标量矩阵

故障状态下的正向电压 *Vf(Tj,If)*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*Vf(Tj,If)* = 0V）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in Vf(Tj,If)
  form`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted forward currents, If** — 故障正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）| 非负标量向量

故障状态下的正向电流 *If*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*If* = 0A）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in Vf(Tj,If)
  form`。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted reverse voltages, Vr(Tj,Ir)** — 故障反向电压 `[1, 10, 20, 25, 30, 32.5, 35; 1, 5, 10, 20, 25, 30, 32]` `V`（默认）| 非负标量矩阵

*自 R2024a 起*

故障状态下的反向电压 *Vr(Tj,Ir)*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*Vr(Tj,ir)* = 0V）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in Vf(Tj,If)
  form`。
- 选中 **Model Zener diode** 参数。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted reverse currents, Ir** — 故障反向电流 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负标量向量

*自 R2024a 起*

故障状态下的反向电流 *Vr*。此参数必须是一个至少包含三个非负元素的向量，且按升序排列。零点可选（*Ir* = 0A）。

#### 依赖关系

要启用此参数：

- 在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。
- 将 **Diode model** 设置为 `Tabulated I-V
  curve`。
- 将 **Table type** 设置为 `Table in Vf(Tj,If)
  form`。
- 选中 **Model Zener diode** 参数。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted capacitance and charge as percentage of unfaulted** — 故障电容和电荷占未故障状态的百分比 `100`（默认）| 有限正标量

故障状态下的电容和电荷占未故障状态的百分比。

#### 依赖关系

要启用此参数，请在 **Diode fault** 参数中点击 **Add fault** 超链接，向 Diode 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个带有故障的模块时，**Open Fault Inspector** 超链接会取代 **Add fault** 超链接出现。有关包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible reverse voltage** — 最大允许反向电压 `inf` `V`（默认）| 正标量

可能触发故障的最大反向电压。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Number of events to fail when exceeding voltage** — 超过电压时失效的事件数 `1`（默认）| 正整数标量

在触发故障之前，二极管必须超过反向电压阈值的次数。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible current** — 故障转换的电流阈值 `inf` `A`（默认）| 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding current** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding current** — 电流超过阈值的最大持续时间 `1` `s`（默认）| 非负标量

电流可以超过最大允许值而不触发故障的最大持续时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum diode recovery, dV/dt** — 二极管恢复阈值 `inf` `V/s`（默认）| 正标量

最大二极管恢复。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible temperature** — 故障转换的温度阈值 `inf` `K`（默认）| 正标量

最大允许温度值。如果温度超过此值的时间长于 **Time to fail when exceeding temperature** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。
- 将 **Diode model** 设置为 `Piecewise
  Linear`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。

### **Time to fail when exceeding temperature** — 超过温度时失效的时间 `1` `s`（默认）| 正标量

在触发行故障之前，温度必须持续超过最大允许温度的时间量。

#### 依赖关系

要启用此参数：

- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。
- 将 **Diode model** 设置为 `Piecewise
  Linear`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show
thermal port`。

有关使用热端口和 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

用于对模块热网络建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

热质量的参数化选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer
model` 或 `Cauer model parameterized with Foster
coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[0, 10]` `K/W`（默认）| 非负值向量

由两个 Conductive Heat Transfer 模块表示的两个热阻值的行向量 [ *R\_JC*
*R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[0, 10]` `s`（默认）| 非负值向量

两个热时间常数值的行向量 [ *t\_J*
*t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time
constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[0, 1]` `J/K`（默认）| 正值向量

两个热质量值的行向量 [ *M\_J*
*M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal
mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[1, 3, 10]` `K/W` | `[4, 6]` `K/W` | 正值向量

由热网络中使用的 Cauer 元件表示的 *n* 个热阻值的行向量。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为 `[1, 3, 10]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[4, 6]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with
Foster coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.1, .3, 1]` `J/K` | `[1.5, 3]` `J/K` | 正值向量

*n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为 `[.1, .3, 1]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[1.5, 3]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with
Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

对应于模型中每个热容两端温降的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[1, 3, 10]` `s` | `[6, 18]` `s` | 正值向量

*n* 个热时间常数值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式，模块将热质量计算为 `Mi =
ti/Ri`，其中 `Mi`、`ti`
和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model
parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为 `[1, 3, 10]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[6, 18]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为
`Cauer model` 或 `Cauer model parameterized with
Foster coefficients`，并将 **Thermal mass parameterization** 设置为
`By thermal time constants`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结开始每个节点的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为
`Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结的热质量 `0.01` `J/K`（默认）| 正标量

结的热质量。

#### 依赖关系

要启用此参数，请将 **Fidelity level** 设置为 `Ideal
switching`，并将 **Thermal network** 设置为
`External`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024a：对表格化反向 I-V 特性进行建模

您现在可以对 Diode 模块的表格化反向 I-V 特性进行建模。

要对反向 I-V 特性进行建模，请选择 **Model Zener diode**
参数，然后指定新的 **Reverse voltages, Vr(Tj,Ir)**、
**Reverse currents, Ir(Tj,Vr)**、**Reverse voltages, Vr** 和
**Reverse currents, Ir** 参数。

在 R2024a 之前，您只能通过指定反向偏置二极管的关断电导来对反向 I-V 特性进行建模。

### R2024a：**Junction capacitance voltage** 变量替换为 **Charge of junction capacitance** 变量

如果在 **Capacitance** 部分中，将
**Parameterization** 设置为 `Use C-V curve data points`
或 `Use parameters Cj0, VJ, M & FC`，您现在使用 **Charge of junction capacitance** 变量来指定电容和电荷建模的 **Initial Targets** 和 **Nominal Values**。**Junction capacitance voltage** 变量不再启用。

如果您在较早版本中创建的模型使用这些值进行
**Parameterization**，并为 **Junction capacitance voltage**
变量指定了 **Initial Targets** 或 **Nominal Values**，则必须更新该模型。有关如何计算结电容电荷的详细信息，请参阅 Junction Capacitance。

### R2023b：在模块图标中显示齐纳二极管的电子符号

Diode 模块图标现在根据您建模的是标准二极管还是齐纳二极管显示不同的电子符号。要对齐纳二极管进行建模，请选择 **Model a Zener diode** 参数，并为 **Reverse breakdown voltage** 参数指定一个有限值。

在 R2023b 之前，您可以通过为 **Reverse breakdown voltage** 参数指定一个有限值来对齐纳二极管进行建模，但模块图标显示的是标准二极管的电子符号。要启用 **Reverse breakdown
voltage** 参数，请将 **Diode model** 设置为 `Piecewise
linear` 或 `Exponential`。

如果您在 R2023b 之前创建了一个模型，并为 **Reverse
breakdown voltage** 参数指定了一个有限值，则模块现在默认启用 **Model a Zener
diode** 参数以实现向后兼容性。

### R2023b：随电流和电压缩放反向恢复损耗

您现在可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **Scale reverse recovery loss with current and
voltage** 参数。

在 R2023a 或更早版本中创建的模型默认不缩放，以实现向后兼容性。

### R2023b：使用内置参数化对特定二极管进行建模

您现在可以使用代表特定供应商组件的内置参数化来参数化 Diode 模块。这些二极管的参数化与制造商数据手册相匹配。使用这些参数化来设置此模块，以复现特定供应商数据手册中正向电压的 V-I 曲线。要加载预定义的参数化，请双击 Diode 模块，单击 **Selected part** 参数的 **<click to select>**
超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择您要使用的部件。

### R2023a：使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并替换为 **Fault
trigger** 参数。您可以将 **Fault trigger**
参数设置为 `Temporal` 或 `Behavioral`。
您只能启用一个触发器。

如果您在较早版本中创建了一个模型并同时启用了时间触发器和行为触发器，现在只有时间触发器被启用。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您想在特定时间触发故障，请将 **Fault trigger**
参数设置为 `Temporal`。如果您想确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为
`Behavioral`。

## 描述

分段线性、指数或表格化二极管

Diode 模块可以表示分段线性二极管、指数二极管或具有表格化 I-V 曲线的二极管。使用 **Fidelity
level** 参数选择动力学模型的详细程度。

### 分段线性二极管

分段线性二极管模型与 **Simscape™** > **Foundation Library** > **Electrical** > **Electrical Elements** > **Diode** 模块相同，但增加了固定结电容和可选的电荷动力学。如果二极管正向电压超过 **Forward
voltage** 参数中指定的值，二极管表现为线性电阻，其阻值为 **On resistance** 参数中指定的值。否则，二极管表现为线性电阻，其小电导为 **Off conductance**
参数中指定的值。二极管两端电压为零时，流过二极管的电流为零。

有关 Simscape Foundation 库中 Diode 模块的更多信息，请参阅 Diode。

### 指数二极管

指数二极管模型表示二极管电流
*I* 和二极管电压 *V* 之间的以下关系：

I=IS⋅(eqVNkTm1−1)   V>−BVI=−IS⋅(e−q(V+Vz)kTm1−eqVNkTm1)  V≤−BV

其中：

- *q* 是电子的基本电荷（1.602176e–19
  库仑）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *BV* 是 **Reverse breakdown voltage** 参数值。
- *N* 是发射系数。
- *IS* 是饱和电流。
- *Tm1* 是指定二极管参数时的温度，由 **Measurement temperature**
  参数值定义。

当 (*q**V* /
*N**k**Tm1*) >
80 时，模块将 eqVNkTm1 替换为 (*q**V* /
*N**k**Tm1* –
79)e80，这与 (*q**V* /
*N**k**Tm1*) =
80 处二极管电流的梯度相匹配，并进行线性外推。当 (*q**V* /
*N**k**Tm1*) <
–79 时，模块将 eqVNkTm1 替换为 (*q**V* /
*N**k**Tm1* +
80)e–79，这也匹配梯度并进行线性外推。典型电路不会达到这些极端值。模块提供此线性外推以帮助在仿真期间求解约束时收敛。

当您为 **Parameterization** 参数选择 `Use parameters IS and N` 时，您通过 **Saturation current IS** 和 **Emission coefficient N**
参数来指定二极管。当您为 **Parameterization** 参数选择 `Use two I-V curve data points` 时，您指定二极管 I-V 曲线上的两个电压和电流测量点，模块推导出 *IS* 和
*N* 值。然后模块按如下方式计算 *IS* 和
*N*：

- N=((V1−V2)/Vt)/(log(I1)−log(I2))
- IS=(I1/(exp(V1/(NVt))−1)+I2/(exp(V2/(NVt))−1))/2

其中：

- *Vt* =
  *k**Tm1* /
  *q*。
- *V1* 和
  *V2* 是 **Voltages [V1
  V2]** 向量中的值。
- *I1* 和
  *I2* 是 **Currents [I1
  I2]** 向量中的值。

当您为 **Parameterization** 参数选择 `Use an I-V data point and IS` 时，模块按如下方式计算 *N*：

N=V1/(Vtlog(I1IS+1))

当您为 **Parameterization** 参数选择 `Use an I-V data point and N` 时，模块按如下方式计算
*IS*：

IS=I1/(exp(V1/(NVt)−1))

### 表格化二极管

要对表格化二极管进行建模，请将 **Diode model** 参数设置为
`Tabulated I-V curve`。下图显示了表格化二极管选项的实现：

如果您选择 **Model Zener
Diode** 参数，您还可以对表格化反向 I-V 特性进行建模。*（自 R2024a 起）*

如果您不选择 **Model Zener Diode** 参数，模块使用 **Off conductance** 参数对反向特性进行建模：

- 如果电压小于 -1 V，模块使用等于 **Off conductance**
  参数值的恒定关断电导来建模 I-V 关系。您指定的值必须小于小正电压下正向 I-V 曲线的梯度。
- 如果电压在 -1 V 和 0 V 之间，模块使用 makima 插值，使正向和反向偏置的 I-V 曲线平滑重叠。

模块使用 `makima` 插值来查找中间值。如果电压或电流超出表格化数据范围，模块在最后一个电压-电流数据点之后使用线性外推。

### 结电容

Diode 模块仅在您将 **Modeling option** 参数设置为 `No thermal
port` 或将 **Fidelity level** 参数设置为 `Include
capacitance and charge dynamics` 时才对结电容进行建模。要包含结电容：

- 为 **Parameterization** 参数选择 `Include fixed or zero junction capacitance`。电容是固定的。
- 为 **Parameterization** 参数选择 `Use parameters CJO, VJ, M & FC`。模块使用系数
  *CJO*、*VJ*、*M* 和
  *FC* 来计算取决于结电压的结电容。
- 为 **Parameterization** 参数选择 `Use C-V curve data points`。模块使用 C-V 电容曲线上的三个电容值来估计 *CJO*、*VJ* 和
  *M*，并将这些值与指定的 *FC* 值一起使用来计算取决于结电压的结电容。模块按如下方式计算 *CJO*、*VJ* 和 *M*：

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  其中：

  - *VR1*、
    *VR2* 和 *VR3* 是 **Reverse
    bias voltages [VR1 VR2 VR3]** 向量中的值。
  - *C1*、
    *C2* 和 *C3* 是
    **Corresponding capacitances [C1 C2 C3]** 向量中的值。

  反向偏置电压（定义为正值）应满足
  *VR3* >
  *VR2* >
  *VR1*。这意味着电容应满足 *C1* >
  *C2* >
  *C3*，因为反向偏置使耗尽区变宽，从而降低电容。违反这些不等式会导致错误。电压
  *VR2* 和
  *VR3* 应远离结电势 *VJ*。电压 *VR1* 应小于结电势 *VJ*，*VR1* 的典型值为 0.1 V。

电压相关结电容以结电容电荷 *Qj* 定义为：

- 对于 *V* <
  *FC*·*VJ*：

  Qj=CJ0⋅(VJ/(M−1))⋅((1−V/VJ)1−M−1)
- 对于 *V* ≥
  *FC*·*VJ*：

  Qj=CJ0⋅F1+(CJ0/F2)⋅(F3⋅(V−FC⋅VJ)+0.5(M/VJ)⋅(V2−(FC⋅VJ)2))

其中：

- F1=(VJ/(1−M))⋅(1−(1−FC)1−M))
- F2=(1−FC)1+M))
- F3=1−FC⋅(1+M)
- *V* 是结电容电压。

这些方程与 [2] 中使用的相同，不同之处在于未对 *VJ* 和 *FC* 的温度依赖性进行建模。

### Charge Dynamics

仅当您将 **Modeling option** 参数设置为 `No thermal port`，或将 **Fidelity level** 参数设置为 `Include capacitance and charge dynamics` 时，Diode 模块才会对电荷动态进行建模。对于换流二极管等应用，对二极管电荷动态进行建模可能很重要。当正向偏置的二极管两端施加反向电压时，电荷需要时间耗散，因此二极管需要时间关断。二极管关断所需的时间主要由渡越时间参数决定。一旦二极管关断，任何剩余电荷随后耗散，其发生速率由载流子寿命决定。

Diode 模块使用 Lauritzen 和 Ma [3] 的模型来捕捉这些效应。以下是定义方程。

|  |  |
| --- | --- |
| i=qE−qMTM | **(1)** |

|  |  |
| --- | --- |
| dqMdt+qMτ−qE−qMTM=0 | **(2)** |

|  |  |
| --- | --- |
| qE=(τ+TM)i | **(3)** |

其中：

- *i* 是二极管电流。
- *qE* 是结电荷。
- *qM* 是总存储电荷。
- *TM* 是渡越时间。
- *τ* 是载流子寿命。
- *vD* 是二极管两端电压。
- *vF* 是二极管正向电压。
- *R* 是二极管导通电阻。
- *G* 是二极管关断电导。

下图显示了二极管器件的典型反向模式电流特性。

其中：

- *iRM* 是峰值反向电流。
- *iF* 是测量 *iRM* 时的起始正向电流。
- *a* 是测量 *iRM* 时的电流变化率。
- *trr* 是反向恢复时间。

二极管的数据手册会给出在初始正向电流和稳定电流变化率下的峰值反向电流值。数据手册还可能提供反向恢复时间和总恢复电荷的值。

**模块如何计算 *TM* 和 Tau**

模块根据您为 **Charge Dynamics** 参数输入的值来计算渡越时间 *TM* 和载流子寿命 *τ*。模块使用 *TM* 和 *τ* 来求解电荷动态方程 1、2 和 3。

在反向模式的初始电流下降期间，二极管仍处于导通状态，电流变化率由外部测试电路决定。

首先，模块使用方程 1 执行此计算。

|  |  |
| --- | --- |
| iF+at=qE−qMTM | **(4)** |

然后，它将方程 4 代入方程 2。

|  |  |
| --- | --- |
| dqMdt+qMτ=iF+at | **(5)** |

然后，它求解方程 5 得到 *qM*，

|  |  |
| --- | --- |
| qM=iFτ−aτ2+kexp(tτ)+aτt, | **(6)** |

其中 *k* 是常数。

当 *t* 为零时，*i* = *iF* 且 *qM* = *τiF*，因为系统处于稳态。

将这些关系代入方程 6 并求解该方程得到 *k* = *aτ2*。

因此，

|  |  |
| --- | --- |
| qM=iFτ+aτ2(1exp(tτ)−1)+aτt. | **(7)** |

在时间 *t* = *ts* 时，电流为 *iRM*，结电荷 *qE* 为零。

模块将这些值代入方程 1。

|  |  |
| --- | --- |
| iRM=−qMTM | **(8)** |

模块重新整理方程 8 以求解 *qM*，并将结果代入方程 7。

|  |  |
| --- | --- |
| −TMiRM=iFτ+aτ2(1exp(tsτ)−1)+aτts | **(9)** |

然后，模块用 *iRM*、*iF* 和 *a* 表示时间 *ts*。

|  |  |
| --- | --- |
| ts=iRM−iFa | **(10)** |

考虑二极管恢复，即当 *t* > *ts* 时。二极管处于反向偏置，电流和结电荷实际上为零。

电流由以下方程定义。

|  |  |
| --- | --- |
| i=iRMexp[−(t−ts)τrr], | **(11)** |

其中：

|  |  |
| --- | --- |
| 1τrr=1τ+1TM. | **(12)** |

模块现在将方程 12 中的表达式与反向恢复时间 *trr* 关联起来。

当 t=iFa+trr 时，电流为 iRM10。

因此，

|  |  |
| --- | --- |
| exp(−t−tsτrr)=0.1 | **(13)** |

并且

|  |  |
| --- | --- |
| trr=τrrlog(10)+iRMa. | **(14)** |

模块使用方程 9 和 14 来计算 *TM* 和 *τ* 的值。由于方程 9 中的指数项，该计算使用迭代方案。

**直接指定 *trr* 的替代方法**

除了允许您直接指定反向恢复时间 *trr* 之外，模块还支持三种替代参数化方式。模块可以从以下任一参数推导出 *trr*：

- 反向恢复时间拉伸因子 *λ*
- 反向恢复电荷 *Qrr*，当数据手册指定此值而不是反向恢复时间时。
- 反向恢复能量 *Erec*，当数据手册指定此值而不是反向恢复时间时。

反向恢复时间拉伸因子 *λ* 与 *trr* 之间的关系由以下方程表示

λ=trraiRM。

反向恢复时间必须大于 iRMa，典型值为 3(iRMa)。

因此，*λ* 的典型值为 3。*λ* 必须大于 1。

反向恢复电荷 *Qrr* 是反向电流从电流变为负值的点开始直到衰减回零的时间积分。

初始电荷，到时间 ts（如图所示），由以下方程表示：

|  |  |
| --- | --- |
| Qs=12(−iRM)iRMa. | **(15)** |

对公式 11 积分得到时间 ts 到无穷大之间的电荷。该电荷等于

τrriRM。

因此，总反向恢复电荷由以下方程给出：

|  |  |
| --- | --- |
| Qrr=−iRM22a−τrriRM. | **(16)** |

重新整理方程 16 以求解 *τrr*，并将结果代入方程 14，得到一个用 *Qrr* 表示 *trr* 的方程：

trr=(QrriRM+iRM2a)log(10)+iRMa。

或者，模块使用反向恢复能量 *Erec* 计算 *τrr*。此方程定义二极管电压曲线：

|  |  |
| --- | --- |
| vd=vR−(vR−vRM)exp(−(t−t1)/τrr), | **(17)** |

其中 vRM=vR−iRM(R−Lτrr) 是最大二极管反向电压。

如果 Lτrr≫R，这是反向恢复测试电路的常见条件，模块将最大二极管反向电压计算为：

vRM=vR+iRMLτrr。

由于下降时间值很小，模块假设二极管电流下降是线性的：

|  |  |
| --- | --- |
| iF+didt · t = qE−qMTM. | **(18)** |

然后，它将方程 18 代入方程 5：

|  |  |
| --- | --- |
| dqMd+qMτ=iF+didt · t. | **(19)** |

为了获得总存储电荷，它求解方程 19：

|  |  |
| --- | --- |
| qM=iFτ+didt · τ2(1exp(tτ)−1)+didt · τt, | **(20)** |

其中 *didt* 是电流的梯度。

当 t=t1=iRM−iFdidt 时，峰值反向电流为：

|  |  |
| --- | --- |
| iRM=−qMTM. | **(21)** |

模块现在将方程 21 代入方程 20：

|  |  |
| --- | --- |
| −iRMTM=iFτ+ didt · τ2(exp(−iRM−iFdidt · τ)−1)+τ(iRM−iF)−(TM+τ)iRM=didt · τ2(exp(−iRM−iFdidt · τ)−1)iRM=F(didt,iF,TM,τ). | **(22)** |

最后，模块求解方程 22 以获得反向恢复能量：

|  |  |
| --- | --- |
| Erec=∫t1t2idvddtErec=τrriRM(vR+vRM)2Erec=iRM(2vRτrr+iRML)2. | **(23)** |

**带故障的电荷动态**

当器件发生故障时，Diode 模块将结电荷计算为

qE=(τ+TM)idiode，

其中：

- *idiode* 是不含电荷模型的二极管电流。
- *qE* 是结电荷。
- *TM* 是渡越时间。
- *τ* 是载流子寿命。

此方程随后定义二极管电流的值：

dqMdt+qMτ−qE−qMTM=0i=qE−qMTMQscale−(Qscale−1)idiode

其中：

- *i* 是二极管电流。
- *qM* 是总存储电荷。
- *Qscale* 是电荷比的当前值。

### Temperature Dependence

Diode 模块的默认行为是不对温度依赖性进行建模，器件在您提供模块参数的温度下进行仿真。指数二极管模型包含若干选项，用于在仿真期间对二极管电流-电压关系的温度依赖性进行建模。不对结电容的温度依赖性进行建模，因为其影响要小得多。

当包含温度依赖性时，二极管定义方程保持不变。测量温度值 *Tm1* 被替换为仿真温度 *Ts*。饱和电流 *IS* 根据以下方程成为温度的函数：

ISTs=ISTm1⋅(Ts/Tm1)XTI/N⋅exp(−EGNkTs(1−Ts/Tm1))

其中：

- *Tm1* 是指定二极管参数时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是当对温度依赖性建模时，标准二极管方程中使用的饱和电流值。
- *EG* 是半导体类型的能隙，单位为焦耳(J)。硅的值通常取为 1.11 eV，其中 1 eV 为 1.602e-19。
- *XTI* 是饱和电流温度指数。对于 pn 结二极管，通常设置为 3.0；对于肖特基势垒二极管，通常设置为 2.0。
- *N* 是发射系数。
- *k* 是玻尔兹曼常数 (1.3806503e–23 J/K)。

*XTI* 和 *EG* 的适当值取决于二极管的类型和所使用的半导体材料。特定材料类型和二极管类型的默认值可捕捉随温度的近似行为。模块为常见类型的二极管提供默认值。

在实践中，需要调整 *XTI* 和 *EG* 的值，以对特定二极管的确切行为进行建模。一些制造商在 SPICE 网表中给出这些调整后的值，您可以读取相应的值。否则，您可以使用数据手册定义的较高温度下的电流-电压数据点来确定 *EG* 的改进估计值。模块为此提供了参数化选项。它还提供了直接指定较高温度下饱和电流 *ISTm2* 的选项。

您也可以自行调整 *XTI* 和 *EG* 的值，以匹配您特定器件的实验室数据。您可以使用 Simulink® Design Optimization™ 软件来帮助调整 *XTI* 和 *EG* 的值。

**注意**

器件温度行为还取决于发射系数。发射系数的不适当值可能导致错误的温度依赖性，因为饱和电流是 *EG* 与 *N* 之比的函数。

如果定义有限的反向击穿电压 (*BV*)，则反向 *BV* 的值由反向击穿温度系数 *TCV* 调制（使用 **Reverse breakdown voltage temperature coefficient, dBV/dT** 参数指定）：

|  |  |
| --- | --- |
| *BVTs* = *BVTm1* – *TCV*· (*Ts* – *Tm1*) | **(24)** |

### Ideal Switching

您可以将理想开关选项与以下理想开关半导体模块一起使用：

- GTO
- Half-Bridge (Ideal, Switching)
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

您可以在这些模块内部对二极管进行建模，也可以使用单独的 Diode 模块在外部对二极管进行建模。

要启用理想开关选项，请将 **Fidelity level** 参数设置为 `Ideal Switching`。

下图显示了半桥内部开关状态下二极管的电压和电流。

反向恢复损耗是二极管热损耗的主要来源之一。二极管每次从导通状态关断到开路状态时都会耗散能量。

对于理想开关，模块不使用基于物理的电荷模型。模块将电荷在反向恢复期间产生的损耗表示为瞬时损耗。

模块通过将结温升高一个等于反向恢复损耗除以结处总热质量的值来施加反向恢复损耗。

如果您将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定了作为结温和开关事件前正向电流函数的耗散能量。关断电压相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果您将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定了每次关断事件期间耗散的能量。如果您选择 **Scale reverse recovery loss with current and voltage** 参数，则模块会按导通状态电流和关断状态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

**注意**

记录的仿真数据中的 `lastReverseRecoveryLoss` 变量将反向恢复损耗包含为幅度等于能量损耗的脉冲。如果您使用脚本对指定仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆导通状态损耗。

### 故障

要在 Diode 模块中对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Diode 模块允许您对三种类型的故障进行建模：

- `Open` — 一旦触发故障，串联电阻立即增加。您可以使用此类型的故障来对因金属化烧毁而失效的二极管进行建模。
- `Short` — 一旦触发故障，并联电导立即增加。您可以使用此选项来对因穿通而失效的二极管进行建模。
- `Parameter shift` — 模块参数从触发故障的时刻开始随时间偏移。您可以使用此选项来对因老化而失效的二极管进行建模。

模块可以触发故障事件：

- 在特定时间。
- 当电流限值、电压限值或温度限值超过特定时间间隔时。

如果您想在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果您想确定系统是否发生故障以及何时发生故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

如果您选择行为触发，则组件会在其中一个触发条件为真时立即失效。

**Parameter Shift Fault**

如果在 **Faults** 设置中，您将 **Failure mode** 参数设置为 `Parameter shift`，则二极管因其组件老化而失效。此方程定义偏移参数的值：

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ)，

其中 *tth* 是触发故障时的时间阈值，*τ* 是 **Fault transition time constant** 参数的值。

### 热效应建模

您可以暴露热端口来对产生的热量和设备温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口，也不模拟设备中的热量产生。
- `Show thermal port` — 模块包含一个热端口，允许您对传导损耗产生的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 齐纳二极管建模

*从 R2023b 开始*

要对在正向和反向偏置方向均导通的齐纳二极管进行建模，请选择 **Model Zener diode** 参数，并为 **Reverse breakdown voltage** 参数指定一个有限值。

当您选择此选项时，您可以通过指定新的 **Reverse voltages, Vr(Tj,Ir)**、**Reverse currents, Ir(Tj,Vr)**、**Reverse voltages, Vr** 和 **Reverse currents, Ir** 参数来为 Diode 模块建模反向 I-V 特性。*（从 R2024a 开始）*

Diode 模块图标取决于您是否对齐纳二极管进行建模以及是否暴露热端口。有关暴露热端口的详细信息，请参阅热效应建模。

| **Modeling option** 参数值 | **Model a Zener diode** 参数值 | 模块图标 |
| --- | --- | --- |
| `No thermal port` | `Off` |  |
| `On` |  |
| `Show thermal port` | `Off` |  |
| `On` |  |

### 参数化

*从 R2023b 开始*

Diode 模块支持多种预定义参数化。

使用此参数化数据来复现特定供应商数据手册中正向电压的 V-I 曲线。要加载预定义参数化，请双击 Diode 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择您要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化及可用组件列表的详细信息，请参阅 List of Pre-Parameterized Components。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取设备参数并将其导入模块。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 或 Infineon® 支持的参数化格式。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**注意**

为满足所有初始目标，请勿将 **Initial Targets** 部分中超过模块方程中微分变量总数的初始目标优先级设置为 `High`。

- 如果在 **Capacitance** 部分中，您将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 设置为 `0`，则模块方程中的微分变量总数为零。请勿将 **Initial Targets** 部分中任何变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分中，您将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 参数设置为非零值，则模块方程中的微分变量总数为 1。将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分中，您将 **Parameterization** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，则模块方程中的微分变量总数为 1。将 **Initial Targets** 部分中不超过一个变量的优先级设置为 `High`。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您无需构建完整模型即可绘制 Diode 模块的基本 I-V 特性。使用这些图来探索参数选择对设备特性的影响。如果您从数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查模块参数化是否正确。如果您有一个完整的工作模型但不知道使用哪个制造部件，可以将图与数据手册进行比较以帮助您做出决定。

要启用此选项，请将 Diode 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
