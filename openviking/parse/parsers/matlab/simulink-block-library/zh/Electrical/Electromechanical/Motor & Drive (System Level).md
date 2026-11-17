---
type: simulink-block
title: 'Motor & Drive (System Level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical'
documentation_page: 'motordrivesystemlevel'
documentation_source_path: 'ref/motordrivesystemlevel.html'
language: zh-CN
chinese_source: worker-translation
---

# Motor & Drive (System Level)

## 端口

### 输入

### **Tr** — 参考转矩需求 physical

与参考转矩需求关联的物理输入端口。

### **OFF** — 供电开关 physical

与供电开关关联的物理输入端口。值为
`1` 表示开关断开。值为
`0` 表示开关闭合。

#### 依赖

要启用此端口，请在 **Electrical Torque**
部分中，选择 **Enable supply switch**
参数。
### 输出

### **W** — 机械转速输出 physical

与机械转速关联的物理输出端口。
### 守恒

### **+** — 正直流电源 electrical

与正直流电源关联的电气守恒端口。

### **-** — 负直流电源 electrical

与负直流电源关联的电气守恒端口。

### **C** — 电机外壳 mechanical

与电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子 mechanical

与电机转子关联的机械旋转守恒端口。

### **H** — 热端口 thermal

热端口。

#### 依赖

要启用此端口，请将 **Modeling option**
参数设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### Electrical Torque

### **Parameterize by** — 转矩参数化方法 `Tabulate torque envelope with speed`（默认）| `Maximum torque and power` | `Tabulate torque envelope with speed and supply voltage`

用于参数化转矩的方法：

- `Tabulate torque envelope with
  speed` — 提供转速向量及对应的最大转矩
  值。
- `Maximum torque and power`
  — 通过提供最大允许转矩和电机
  功率的值来定义转矩-转速包络。
- `以转速和电源电压制表转矩包络`。
  supply voltage` — 提供
  转速向量、直流电源
  电压向量以及对应的最大转矩
  值。

### **Allow intermittent over-torque** — 间歇过转矩选项 `No`（默认）| `Yes`

是否允许间歇过转矩。有关
过转矩的更多信息，请参阅 Intermittent Over-Torque Operation。

### **Continuous operation maximum torque envelope, T\_c(w)** — 连续运行的最大转矩值向量 `[.09, .08, .07, 0]` `N*m`（默认）

允许稳态运行的最大转矩值。这些
值对应于 **Corresponding
rotational speeds, w** 参数中的转速，并定义
电机的转矩-转速包络。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
with speed`。

### **Continuous operation maximum torque envelope, T\_c(w, Vdc)** — 按转速和电压制表的连续运行最大转矩值向量 `[.09, .09, .09; .08, .08, .08; .07, .07, .07; 0, 0, 0]` `N*m`（默认）| 正值二维向量

允许稳态运行的最大转矩值。这些
值对应于 **Corresponding
rotational speeds, w** 参数中的转速，以及
**Corresponding DC supply voltage, Vdc** 参数中的电压。
此参数定义电机的转速和电源电压包络。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
以转速和电源电压`。

### **Intermittent operation maximum torque envelope, T\_i(w)** — 间歇运行的最大转矩值向量 `[.36, .32, .28, 0]` `N*m`（默认）

间歇过转矩运行期间的最大转矩值。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
with speed`，并将 **Allow intermittent
over-torque** 参数设置为
`Yes`。

### **Intermittent operation maximum torque envelope, T\_i(w,Vdc)** — 按转速和电压制表的间歇运行最大转矩值向量 `[.36, .36, .36; .32, .32, .32; .28, .28, .28; 0, 0, 0]` `N*m`（默认）| 正值二维向量

按转速和电压制表的间歇过转矩运行期间的最大转矩值。此参数的值必须
大于 **Continuous operation maximum
torque envelope, T\_c(w, Vdc**) 参数的值。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
with speed and supply voltage`，并将
**Allow intermittent over-torque** 参数设置为
`Yes`。

### **Corresponding rotational speeds, w** — 转速向量 `[0, 3750, 7500, 8000]` `rpm`（默认）

允许稳态运行的转速。为避免
因转矩-转速曲线斜率无穷大而导致性能不佳，
请指定不包含连续重复值的转速向量。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
with speed`。

### **Corresponding DC supply voltage, Vdc** — 直流电源电压向量 `[6, 12, 24]` `V`（默认）| 正标量向量

允许稳态运行的直流电源电压。此参数的值
必须严格递增。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Tabulate torque envelope
以转速和电源电压`。

### **Continuous operation maximum torque** — 连续运行的最大转矩 `0.1` `N*m`（默认）| 正标量

连续运行期间允许的最大电机转矩。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Maximum torque and
power`。

### **Continuous operation maximum power** — 连续运行的最大功率 `30` `W`（默认）| 正标量

连续运行期间允许的最大电机功率。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Maximum torque and
power`。

### **Intermittent operation maximum torque** — 间歇运行的最大转矩 `0.4` `N*m`（默认）| 正标量

间歇过转矩运行期间允许的最大电机转矩。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Maximum torque and
power`，并将 **Allow intermittent
over-torque** 参数设置为
`Yes`。

### **Intermittent operation maximum power** — 间歇运行的最大功率 `120` `W`（默认）| 正标量

间歇过转矩运行期间允许的最大电机功率。

#### 依赖

要启用此参数，请将 **Parameterize
by** 参数设置为 `Maximum torque and
power`，并将 **Allow intermittent
over-torque** 参数设置为
`Yes`。

### **Over-torque time limit** — 过转矩时间限制 `30` `s`（默认）| 正标量

可以连续施加过转矩的最长时间。

#### 依赖

要启用此参数，请将 **Allow intermittent
over-torque** 参数设置为
`Yes`。

### **Recovery time** — 恢复时间 `60` `s`（默认）| 正标量

转矩需求必须低于连续运行转矩包络的时间量，之后模块才能再次施加
过转矩。

#### 依赖

要启用此参数，请将 **Allow intermittent
over-torque** 参数设置为
`Yes`。

### **Torque control time constant, Tc** — 转矩控制时间常数 `0.02` `s`（默认）| 非负标量

电机驱动器跟踪转矩需求的时间常数。

### **Enable supply switch** — 启用供电切换的选项 `off`（默认）| `on`

启用电机接通和断开的选项。

### Electrical Losses

### **Parameterize losses by** — 电气损耗参数化 `Single efficiency measurement`（默认）| `Tabulated loss data as a function of speed and torque` | `Tabulated efficiency data as a function of speed and torque` | `Tabulated loss data as a function of speed, torque, and DC supply voltage` | `Tabulated efficiency data as a function of speed, torque, and DC supply voltage`

电气损耗参数化方法：

- `Single efficiency measurement`
  — 将损耗建模为常数项加上两个
  附加项之和，这两个附加项分别与
  转矩的平方和转速的平方成正比。
- `以转速和
  torque` — 通过使用
  基于所提供的电机转速、负载转矩和对应
  损耗的制表数据进行二维查表来确定损耗。
- `Tabulated efficiency data as a function of speed
  and torque` — 通过使用
  基于所提供的电机转速、负载转矩和对应
  效率的制表数据进行二维查表来确定损耗。
- `Tabulated loss data as a function of speed,
  torque, and DC supply voltage` —
  通过使用基于所提供的电机转速、负载
  转矩、直流电源电压和对应损耗的制表数据进行三维查表
  来确定损耗。
- `Tabulated efficiency data as a function of speed,
  torque, and DC supply voltage` —
  通过使用基于所提供的电机转速、负载
  转矩、直流电源电压和对应效率的制表数据进行三维查表
  来确定损耗。

有关详细信息，请参阅 Model Electrical Losses。

### **Motor and driver overall efficiency (percent)** — 电机和驱动器总效率 `100`（默认）

电机和驱动器的总效率。模块将总
效率定义为

η=100τ0ω0τ0ω0+P0+kτ02+kwω02

其中：

- *τ*0 是
  **Torque at which efficiency is
  measured** 参数。
- *ω*0 是
  **Speed at which efficiency is
  measured** 参数。
- *P*0 是
  **Fixed losses independent of torque or
  speed** 参数。
- kτ02 是与转矩相关的电气损耗。
- *kw**ω2*
  是与转速相关的铁耗。

在初始化时，模块求解效率
方程以得到 *k*。模块忽略与转子阻尼相关的
损耗。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Single efficiency
measurement`。

### **Speed at which efficiency is measured** — 测量效率时的转速 `3750` `rpm`（默认）

模块用于计算与转矩相关的电气
损耗的转速。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Single efficiency
measurement`。

### **Torque at which efficiency is measured** — 测量效率时的转矩 `0.08` `N*m`（默认）

模块用于计算与转矩相关的电气
损耗的转矩。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Single efficiency
measurement`。

### **Iron losses at measurement speed** — 测量转速下的铁耗 `0` `W`（默认）

在测量效率时的转速和转矩下的
铁耗。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Single efficiency
measurement`。

### **Fixed losses independent of torque and speed** — 与转矩和转速无关的固定损耗 `0` `W`（默认）

当电机电流和转矩为零时，与驱动器关联的
固定电气损耗。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Single efficiency
measurement`。

### **Vector of speeds (w) for tabulated losses** — 用于制表损耗的转速向量 `[-8000, -4000, 0, 4000, 8000]` `rpm`（默认）

计算损耗时用于查表的转速值向量。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为以下之一：

- `Tabulated loss data as a function of
  speed and torque`
- `Tabulated loss data as a function of
  speed, torque, and DC supply
  voltage`
- `Tabulated efficiency data as a function
  of speed and torque`
- `Tabulated efficiency data as a function
  of speed, torque, and DC supply
  voltage`

### **Vector of torques (T) for tabulated losses** — 用于制表损耗的转矩向量 `[0, .03, .06, .09]` `Nm`（默认）

计算损耗时用于查表的转矩值向量。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为以下之一：

- `Tabulated loss data as a function of
  speed and torque`
- `Tabulated loss data as a function of
  speed, torque, and DC supply
  voltage`
- `Tabulated efficiency data as a function
  of speed and torque`
- `Tabulated efficiency data as a function
  of speed, torque, and DC supply
  voltage`

### **Vector of DC supply voltages (v) for tabulated losses** — 用于制表损耗的直流电源电压向量 `[100, 250, 400]` `V`（默认）

计算损耗时用于查表的直流电源电压向量。

您可以将此参数指定为
行向量或列向量 *(自 R2023a 起)*。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Tabulated loss data as a
function of speed, torque, and DC supply voltage`
或 `Tabulated efficiency data as a function of speed,
torque, and DC supply voltage`。

### **Corresponding losses, P(w,T)** — 与转速和转矩对应的电气损耗 `[1.49, 1.67, 2.21, 3.1; .42, .69, 1.14, 2.03; .06, .24, .78, 1.68; .42, .69, 1.14, 2.03; 1.49, 1.67, 2.21, 3.1]` `W`（默认）

用于二维查表的、作为转速和转矩函数的电气损耗制表值。矩阵中的每个值指定
特定转速和转矩组合下的损耗。矩阵大小必须与 **Vector of
speeds (w) for tabulated losses** 和 **Vector of
torques (T) for tabulated losses** 参数中定义的维度匹配。

#### 依赖

要启用此参数，请将 **Parameterize losses
by** 参数设置为 `Tabulated loss data as a
function of speed and torque`。

### **Corresponding efficiency (percent), E(w,T)** — 对应于转速和转矩的效率 `[95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95]`（默认）

以百分比表示的表格化效率值，作为转速和转矩的函数，用于二维查表。

当热端口 **H** 处的温度等于 **Temperature Dependence** 部分中 **Measurement temperature** 参数的值时，此参数对电能与机械能之间的转换效率进行建模。如果热端口 **H** 处的温度等于 **Measurement temperature** 和 **Second measurement temperature** 之间的某个值，则此模块在每个表的数值之间对效率进行线性插值。

矩阵中的每个值指定了特定转速和转矩组合下的效率。矩阵大小必须与 **Vector of speeds (w) for tabulated losses** 和 **Vector of torques (T) for tabulated losses** 参数中定义的维度匹配。模块忽略您为零转速或零转矩提供的效率值，并假定当转矩或转速为零时损耗为零。模块使用线性插值来确定损耗。请根据需要提供低转速和低转矩的表格化数据，以获得较低功率条件下所需的精度水平。

#### 依赖关系

要启用此参数，请将 **Parameterize losses by** 参数设置为 `Tabulated efficiency data as a function of speed and torque`。

### **Corresponding losses, P(w,T,v)** — 对应于转速、转矩和电源电压的电气损耗 `ones(5, 4, 3)` `W`（默认）

作为转速、转矩和直流电源电压的函数的电气损耗表格化值，用于三维查表。矩阵中的每个值指定了特定转速、转矩和直流电源电压组合下的损耗。矩阵大小必须与 **Vector of speeds (w) for tabulated losses**、**Vector of torques (T) for tabulated losses** 和 **Vector of DC supply voltages (v) for tabulated losses** 参数定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Parameterize losses by** 参数设置为 `Tabulated loss data as a function of speed, torque, and DC supply voltage`。

### **Corresponding efficiency (percent), E(w,T,v)** — 对应于转速、转矩和电源电压的效率 `95 * ones(5, 4, 3)`（默认）

以百分比表示的表格化效率值，作为转速、转矩和直流电源电压的函数，用于三维查表。矩阵中的每个值指定了特定转速、转矩和直流电源电压组合下的效率。矩阵大小必须与 **Vector of speeds (w) for tabulated losses**、**Vector of torques (T) for tabulated losses** 和 **Vector of DC supply voltages (v) for tabulated losses** 参数定义的维度匹配。模块忽略您为零转速或零转矩提供的效率值，并假定当转矩或转速为零时损耗为零。模块使用线性插值来确定损耗。请根据需要提供低转速和低转矩的表格化数据，以获得较低功率条件下所需的精度水平。

#### 依赖关系

要启用此参数，请将 **Parameterize losses by** 参数设置为 `Tabulated efficiency data as a function of speed, torque, and DC supply voltage`。

### **External supply series resistance** — 外部电源串联电阻 `0` `Ohm`（默认）| 非负标量

与直流电源串联使用的等效电阻，用于对与驱动器电源电流成正比的电气损耗进行建模。模块假定在恒定负载条件下直流电源电流近似恒定。

### Mechanical

### **Rotor inertia** — 转子惯量 `5e-6` `kg*m^2`（默认）| 非负标量

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子阻尼 `1e-5` `N*m*s/rad`（默认）| 非负标量

转子阻尼。该值可以为零。

### **Initial rotor speed** — 初始转子转速 `0` `rpm`（默认）

仿真开始时的转子转速。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

添加开路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### Temperature Dependence

要启用这些参数，请将 **Modeling option** 参数设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

定义电阻随温度变化的方程中的参数 α，如 Thermal Model for Actuator Blocks 中所述。默认值为铜的值。

#### 依赖关系

要启用此参数，请将 **Electrical Losses** 设置中的 **Parameterize losses by** 参数设置为 `Single efficiency measurement`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

您定义电机参数时的温度。如果您通过表格化损耗数据来参数化电气损耗，则此值是您在 **Electrical Losses** 选项卡中指定 **Corresponding losses, P(w,T)** 参数值时的温度。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

您在 **Corresponding losses, P(w,T), at second measurement temperature** 参数中指定的值所对应的温度。

#### 依赖关系

要启用此参数，请在 **Electrical Losses** 部分中，将 **Parameterize losses by** 参数设置为 `Tabulated loss data as a function of speed and torque`、`Tabulated efficiency data as a function of speed and torque`、`Tabulated loss data as a function of speed, torque, and DC supply voltage` 或 `Tabulated efficiency data as a function of speed, torque, and DC supply voltage`。

### **Corresponding losses, P(w,T), at second measurement temperature** — 第二测量温度下对应于转速和转矩的电气损耗 `[1.49, 1.74, 2.49, 3.74; .42, .67, 1.42, 2.67; .06, .31, 1.06, 2.31; .42, .67, 1.42, 2.67; 1.49, 1.74, 2.49, 3.74]` `W`（默认）

第二测量温度下的铁损，对应于 **Electrical Losses** 选项卡上表格化的转速和转矩值。

#### 依赖关系

要启用此参数，请将 **Electrical Losses** 设置中的 **Parameterize losses by** 参数设置为 `Tabulated loss data as a function of speed and torque`。

### **Corresponding efficiency (percent), E(w,T), at second measurement temperature** — 第二测量温度下对应于转速和转矩的效率 `[95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95; 95, 95, 95, 95]`（默认）

以百分比表示的第二测量温度下的表格化效率值，对应于 **Electrical Losses** 选项卡上表格化的转速和转矩值。

当热端口 **H** 处的温度等于 **Second measurement temperature** 参数的值时，此参数对电能与机械能之间的转换效率进行建模。如果热端口 **H** 处的温度等于 **Measurement temperature** 和 **Second measurement temperature** 之间的某个值，则此模块在每个表的数值之间对效率进行线性插值。

#### 依赖关系

要启用此参数，请将 **Electrical Losses** 设置中的 **Parameterize losses by** 参数设置为 `Tabulated efficiency data as a function of speed and torque`。

### **Corresponding losses, P(w,T,v), at second measurement temperature** — 第二测量温度下对应于转速、转矩和电源电压的电气损耗 `ones(5, 4, 3)` `W`（默认）

第二测量温度下的铁损，对应于 **Electrical Losses** 选项卡上表格化的转速、转矩和直流电源电压值。

#### 依赖关系

要启用此参数，请将 **Electrical Losses** 设置中的 **Parameterize losses by** 参数设置为 `Tabulated loss data as a function of speed, torque, and DC supply voltage`。

### **Corresponding efficiency (percent), E(w,T,v), at second measurement temperature** — 第二测量温度下对应于转速、转矩和电源电压的效率 `95 * ones(5, 4, 3)`（默认）

以百分比表示的第二测量温度下的表格化效率值，对应于 **Electrical Losses** 选项卡上表格化的转速、转矩和直流电源电压值。

#### 依赖关系

要启用此参数，请将 **Electrical Losses** 设置中的 **Parameterize losses by** 参数设置为 `Tabulated efficiency data as a function of speed, torque, and DC supply voltage`。

### Thermal Port

要启用这些参数，请将 **Modeling option** 参数设置为 `Show thermal port`。

### **Thermal mass** — 热质量 `100` `J/K`（默认）

电绕组的质量，定义为使温度升高一度所需的能量。

### **Initial Temperature** — 初始温度 `25` `degC`（默认）

仿真开始时热端口的温度。

## 所属库

Simscape / Electrical / Electromechanical / System-Level Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024b: 捕获转子阻尼耗散的功率

如果您将 **Rotor damping** 参数设置为大于零的值，则记录的仿真数据中的 `power_dissipated` 变量现在包含转子阻尼耗散的功率。如果您还将 **Modeling option** 参数设置为 `Show thermal port`，则转子阻尼会产生热量。

### R2023a: 将向量参数指定为行向量或列向量

您现在可以将这些参数指定为行向量或列向量：

- **Continuous operation maximum torque envelope, T\_c(w)**
- **Intermittent operation maximum torque envelope, T\_i(w)**
- **Corresponding rotational speeds, w**
- **Corresponding DC supply voltage, Vdc**
- **Vector of speeds (w) for tabulated losses**
- **Vector of torques (T) for tabulated losses**
- **Vector of DC supply voltages (v) for tabulated losses**

在 R2022b 或更早版本中，您只能将这些参数指定为行向量。您可以转置存储在 MATLAB® 工作区或 Simulink 中模块参数字段中的列向量形式的输入数据。

### R2020b: 库路径和名称变更

Simplified PMSM Drive 模块已重命名为 Motor & Drive (System Level) 模块，并从 **Simscape** > **Electrical** > **Electromechanical** > **Permanent Magnet** 库移至 **Simscape** > **Electrical** > **Electromechanical** > **System-Level Modeling** 库。

如果您有依赖于该模块的库路径或 Simscape 组件路径的脚本，请更新它以反映这些变更。

## 描述

具有闭环转矩控制的通用电机和驱动器

Motor & Drive (System Level) 模块对具有闭环转矩控制的通用电机和驱动器或伺服电机进行建模。使用此模块可以在牵引和驱动系统中对各种类型的电机进行系统级建模。您可以建模的电机包括以下无刷电机：

- 永磁同步电机（PMSM）：

  - 内置式永磁（IPM）电机或内置式永磁同步电机（IPMSM）
  - 表贴式永磁（SPM）电机或表贴式永磁同步电机（SPMSM）
- 无刷直流（BLDC）电机
- 轴向磁通牵引电机

您还可以使用此模块通过模块对具有闭环转矩控制的有刷电机进行建模。

为了在系统级实现快速仿真，此模块对电机、驱动电子设备和控制器进行了抽象。

该模块仅允许转矩-转速包络所定义的转矩和转速范围。在默认模块配置中，您在模块对话框中将此数据指定为一组转速数据点和对应的最大转矩值。下图显示了笛卡尔象限定义：

无刷电机模型的表格化转矩-转速包络

下表显示了每个象限的工作区域以及转速和电磁转矩的值：

| 象限 | 描述 | 转速 | 电磁转矩 | 工作模式 |
| --- | --- | --- | --- | --- |
| 1 | 正向电动区域 | 正 | 正 | 电动模式 |
| 2 | 正向发电区域 | 正 | 负 | 发电模式 |
| 3 | 反向电动区域 | 负 | 负 | 电动模式 |
| 4 | 反向发电区域 | 负 | 正 | 发电模式 |

在此表中：

- 电动模式将电功率转换为机械功率。
- 发电模式将机械功率转换为电功率。
- 正转速意味着端口 **C** 和 **R** 之间的距离随时间增加。
- 负转速意味着端口 **C** 和 **R** 之间的距离随时间减小。
- 正转矩意味着转矩有助于转速的增加。模块产生从机械端口 **C** 到 **R** 作用的正确转矩。
- 负转矩有助于降低转速。如果转速已经为负，则负转矩会使其沿负方向加速。

仅指定正转矩区域的转矩-转速包络，即象限 1 和 4。当电机反向运行时，电机的转矩-转速包络具有相同的轮廓，由象限 2 和 3 表示。如果您仅指定正转速的包络，则模块将象限 4 的转矩包络定义为象限 1 的镜像。下图显示了转矩控制电机和驱动器的典型转矩-转速包络：

无刷电机模型的表格化转矩-转速包络

除了提供表格化的转矩-转速数据外，您还可以指定最大转矩和最大功率。下图显示了象限 1 中得到的转矩-转速包络轮廓。相同的轮廓约束其他三个工作象限。

基于最大转矩和最大功率的无刷电机模型转矩-转速包络

Visualize Four-Quadrant Operation of Electric Drive System 示例可帮助您可视化 Motor & Drive (System Level) 模块在所有四个象限中运行时的转矩-转速轨迹。

**注意**

Simscape™ Electrical™ 包含多个可以对相同类型的电机或执行器进行建模的模块。请选择具有足够建模细节的模块来回答您需要解决的工程设计问题。不要使用建模细节超出您需要的模块，因为高保真度模型会减慢仿真速度并且参数化更加复杂。

像 Motor & Drive (System Level) 这样的模块使用能量平衡或其他抽象方法。这些模型具有较低的保真度。当您需要较长的仿真时间时使用此模块，例如分析电动汽车的驾驶循环。有关选择正确的模块以适当的保真度对电机进行建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 间歇性过转矩运行

要在短时间内对电机施加过转矩，请将 **Allow intermittent over-torque** 参数设置为 `Yes`。
在这种情况下，必须同时指定 **Continuous
operation maximum torque envelope** 和 **Intermittent
operation maximum torque envelope** 参数的值。在内部，该模块根据转矩需求历史来确定应用哪个转矩包络。如果转矩需求低于连续运行转矩包络的时间超过 **Recovery time** 参数中指定的值，则可以对电机驱动器施加过转矩。如果施加过转矩的时间超过 **Over-torque time limit** 参数中指定的值，则过转矩将被禁用。

如需针对具体应用进行更精细的过转矩管理，请在 Motor & Drive 模块中禁用过转矩，并在 Simulink® 中在转矩需求和 Motor & Drive 模块的转矩参考输入端口 **Tr** 之间外部实现转矩限制。

### 电机电气损耗建模

该模块允许对电气损耗进行简化定义和表格化定义。
默认的简化行为是将损耗建模为以下四项之和：

- DC 电源与电机驱动器之间的串联电阻。
- 与转矩和转速无关的固定损耗
  *P0*。使用此项来
  考虑固定变流器损耗。
- 与转矩相关的电气损耗 *k**τ2*，其中 *τ* 是转矩，*k* 是常数。这表示
  铜绕组中的欧姆损耗。
- 与转速相关的电气损耗 *kw**ω2*，其中 *ω* 是转速，*kw* 是常数。这
  表示由涡流引起的铁耗。

这种对损耗与转矩和转速依赖关系的简化，对于早期设计工作可能已经足够，无论底层电机类型和驱动拓扑如何。

如果需要更高精度，或者在设计过程后期，可以提供作为电机转速和负载转矩函数的表格化损耗值。使用此选项时，请提供仿真将运行的所有运行象限的数据。如果只提供部分数据（例如，仅提供第 1 象限正向电动区域的数据），则假定其他象限重复相同的损耗模式。这通常对于反向电动区域是正确的，但对于制动/发电象限可能只是近似。对于超出表格范围的转速和转矩幅值，该模块不会对损耗值进行外推。

最后，可以通过使用表格化效率数据来指定电气损耗，而不是使用单一效率测量值或表格化损耗数据。使用此选项时，也请提供仿真将运行的所有运行象限的数据。如果只提供部分数据（例如，仅提供第 1 象限正向电动区域的数据），则假定其他象限重复相同的损耗模式。

最佳实践是提供作为转速和转矩函数的表格化损耗数据，而不是表格化效率数据，因为：

- 在零转速或零转矩时，效率变得定义不明确。
- 使用损耗，还可以考虑在零转速或零转矩时仍然存在的固定损耗。

如果使用表格化效率选项：

- 该模块会将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。
- 您为零转速或零转矩提供的效率值将被忽略，并且当转矩或转速为零时，假定损耗为零。
- 该模块使用线性插值来确定损耗。请根据需要提供低转速和低转矩的表格化数据，以获得较低功率条件下所需的精度水平。
- 对于超出表格范围的转速和转矩幅值，该模块不会对损耗值进行外推。

当您提供表格化损耗或效率数据时，还可以将其指定为转速、负载转矩和 DC 电源电压的函数。当电源电压未稳压并且在仿真期间可能变化时，此选项很有用。一个示例是没有在电机驱动器上游配备 DC-DC 调节器的电动汽车动力传动系统。使用 Motor & Drive (System Level) 模块对电机驱动器建模，并提供作为电机转速、负载转矩和 DC 电源电压函数的表格化损耗或效率值。

### 绘制效率图

该模块允许您可视化转矩-转速包络图以及电机和驱动器的稳态电气效率。要绘制效率图，可以任选以下一种方式：

- 在框图中双击该模块，然后在 **Description** 选项卡中点击 `Plot
  efficiency map`。
- 在框图中右键单击该模块，然后在 **Electrical** 上下文菜单中选择
  `Plot efficiency map`。

此效率图不包括由 **External supply series resistance** 和 **Rotor
damping** 参数产生的损耗。

### 热效应建模

可以暴露热端口，以对将功率转换为热量的损耗效应进行建模。
要暴露热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含一个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参见 Simulating Thermal Effects in Rotational and Translational Actuators。

### 故障建模

要对 Motor & Drive (System Level) 模块中的故障建模，请在 **Faults** 部分中，点击要建模故障旁边的 **Add fault**。有关故障建模的详细信息，请参见 Fault Behavior Modeling and Fault Triggering。

Motor & Drive (System Level) 模块允许对开路故障建模。当故障被触发时，伺服电机停止运行，从电源侧吸取的电流为零，向负载侧提供的电流也为零。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见 System Scaling by Nominal Values。
