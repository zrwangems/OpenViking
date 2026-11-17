---
type: simulink-block
title: 'Scattering MIMO Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'scatteringmimochannel'
documentation_source_path: 'ref/scatteringmimochannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Scattering MIMO Channel

## 端口
```yaml
ports:
- name: X
  summary: 发射的窄带信号，*M*×*Nt* 复值矩阵
  direction: input
  data_types: double
- name: XH
  summary: 发射的窄带 H 极化信号，*M*×*Nt* 复值矩阵
  direction: input
  data_types: double
- name: XV
  summary: 发射的窄带 V 极化信号，*M*×*Nt* 复值矩阵
  direction: input
  data_types: double
- name: TxPos
  summary: 发射天线阵列的位置，3×1 实值列向量
  direction: input
  data_types: double
- name: TxVel
  summary: 发射天线阵列的速度，3×1 实值列向量
  direction: input
  data_types: double
- name: TxAxes
  summary: 发射天线阵列的轴方向，3×3 实正交矩阵
  direction: input
  data_types: double
- name: RxPos
  summary: 接收天线阵列的位置 3×1 实值列向量
  direction: input
  data_types: double
- name: RxVel
  summary: 接收天线阵列的速度 3×1 实值列向量
  direction: input
  data_types: double
- name: RxAxes
  summary: 接收天线阵列的轴方向 3×3 实正交矩阵
  direction: input
  data_types: double
- name: ScatPos
  summary: 散射体的位置 3×*Ns* 实值矩阵
  direction: input
  data_types: double
- name: ScatVel
  summary: 散射体的速度 3×*Ns* 实值矩阵
  direction: input
  data_types: double
- name: ScatCoef
  summary: 散射系数 1×*Ns* 复值行向量
  direction: input
  data_types: double
- name: Y
  summary: 接收到的窄带信号 *M*×*Nr* 复值矩阵
  direction: output
  data_types: double
- name: YH
  summary: 接收到的窄带 H 极化信号 复值 *M*×*Nr* 矩阵
  direction: output
  data_types: double
- name: YV
  summary: 接收的窄带 V 极化信号复值 *M*×*Nr* 矩阵
  direction: output
  data_types: double
- name: CS
  summary: 信道响应 *Nt*×*Nr*×*Ns* 复值 MATLAB® 数组
  direction: output
  data_types: double
- name: Tau
  summary: 路径延迟 1×*Ns* 实值向量
  direction: output
  data_types: double
```

### 输入

### **X** — 发射的窄带信号，*M*×*Nt* 复值矩阵

发射的窄带信号，指定为 *M*×*Nt* 复值矩阵。*M* 为信号中的采样数，*Nt* 为发射阵列元素的数量。每一列表示对应阵列元素发射的信号。

**示例：** `[1,1;j,1;0.5,0]`

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在脉冲重复频率可变的脉冲波形情况下，大小可能发生变化。

#### 依赖关系

要启用此端口，请将 **Polarization configuration** 参数设置为 `None` 或 `Combined`。

**数据类型：** `double`
**复数支持：** 是

### **XH** — 发射的窄带 H 极化信号，*M*×*Nt* 复值矩阵

发射的窄带 *H* 极化信号，指定为 *M*×*Nt* 复值矩阵。*M* 为信号中的采样数，*Nt* 为发射阵列元素的数量。每一列表示对应阵列元素发射的信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在脉冲重复频率可变的脉冲波形情况下，大小可能发生变化。

**示例：** `[1,1;j,1;0.5,0]`

#### 依赖关系

要启用此端口，请将 **Polarization configuration** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** 是

### **XV** — 发射的窄带 V 极化信号，*M*×*Nt* 复值矩阵

发射的窄带 *V* 极化信号，指定为 *M*×*Nt* 复值矩阵。*M* 为信号中的采样数，*Nt* 为发射阵列元素的数量。每一列表示对应阵列元素发射的信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在脉冲重复频率可变的脉冲波形情况下，大小可能发生变化。

#### 依赖关系

要启用此端口，请将 **Polarization configuration** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** 是

### **TxPos** — 发射天线阵列的位置，3×1 实值列向量

发射天线阵列的位置，指定为 3×1 实值列向量，形式为 `[x;y;z]`。向量元素分别对应阵列的 *x*、*y* 和 *z* 位置。单位为米。

#### 依赖关系

要启用此端口，请将 **Source of transmit array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **TxVel** — 发射天线阵列的速度，3×1 实值列向量

发射天线阵列的速度，指定为 3×1 实值列向量，形式为 `[vx;vy;vz]`。向量元素分别对应阵列的 *x*、*y* 和 *z* 速度。单位为米每秒。

#### 依赖关系

要启用此端口，请将 **Source of transmit array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **TxAxes** — 发射天线阵列的轴方向，3×3 实正交矩阵

发射天线阵列的轴方向，指定为 3×3 实正交矩阵。该矩阵定义阵列局部坐标系相对于全局坐标的方向。矩阵列对应局部坐标系的 *x*、*y* 和 *z* 轴方向。量纲为无量纲。

#### 依赖关系

要启用此端口，请将 **Source of transmit array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxPos** — 接收天线阵列的位置 3×1 实值列向量

接收天线阵列的位置，指定为形式为 `[x;y;z]` 的 3×1 实值列向量。向量元素对应于阵列的 *x*、*y* 和 *z* 位置。单位为米。

#### 依赖

要启用此端口，请将 **Source of receive array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxVel** — 接收天线阵列的速度 3×1 实值列向量

接收天线阵列的速度，指定为形式为 `[vx;vy;vz]` 的 3×1 实值列向量。向量元素对应于阵列的 *x*、*y* 和 *z* 速度。单位为米每秒。

#### 依赖

要启用此端口，请将 **Source of receive array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxAxes** — 接收天线阵列的轴方向 3×3 实正交矩阵

接收天线阵列的轴方向，指定为 3×3 实正交矩阵。该矩阵定义阵列局部坐标系相对于全局坐标系的朝向。矩阵列对应于局部坐标系的 *x*、*y* 和 *z* 轴方向。量纲为无量纲。

#### 依赖

要启用此端口，请将 **Source of receive array motion** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatPos** — 散射体的位置 3×*Ns* 实值矩阵

散射体的位置，指定为 3×*Ns* 实值矩阵。矩阵的每一列采用 `[x;y;z]` 的形式，包含一个散射体的 *x*、*y* 和 *z* 位置。单位为米。

#### 依赖

要启用此端口，请将 **Scatterer specification** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatVel** — 散射体的速度 3×*Ns* 实值矩阵

散射体的速度，指定为 3×*Ns* 实值矩阵。矩阵的每一列采用 `[vx;vy;vz]` 的形式，包含一个散射体的 *x*、*y* 和 *z* 速度。单位为米每秒。

#### 依赖

要启用此端口，请将 **Scatterer specification** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatCoef** — 散射系数 1×*Ns* 复值行向量

散射系数，指定为 1×*Ns* 复值行向量。每个向量元素指定对应散射体的散射系数。量纲为无量纲。

#### 依赖

要启用此端口，请将 **Scatterer specification** 参数设置为 `Input port`。

**数据类型：** `double`
**复数支持：** 是
### 输出

### **Y** — 接收到的窄带信号 *M*×*Nr* 复值矩阵

接收到的窄带信号，返回为 *M*×*Nr* 复值矩阵。量 *M* 是信号中的样本数，*Nr* 是接收阵列元素的数量。每一列表示对应阵列元素接收到的信号。

#### 依赖

要启用此端口，请将 **Polarization configuration** 参数设置为 `None` 或 `Combined`。

**数据类型：** `double`
**复数支持：** 是

### **YH** — 接收到的窄带 H 极化信号 复值 *M*×*Nr* 矩阵

接收到的窄带 *H* 极化信号，返回为复值 *M*×*Nr* 矩阵。*M* 是信号中的样本数，*Nr* 是接收阵列元素的数量。每一列表示对应阵列元素接收到的信号。

#### 依赖

要启用此端口，请将 **Polarization configuration** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** 是

### **YV** — 接收的窄带 V 极化信号复值 *M*×*Nr* 矩阵

接收的窄带 *V* 极化信号，以复值 *M*×*Nr* 矩阵形式返回。*M* 是信号中的采样数，*Nr* 是接收阵列元素的数量。每一列表示对应阵列元素接收到的信号。

#### 依赖关系

要启用此端口，请将 **Polarization configuration** 参数设置为 `Dual`。

**数据类型：** `double`
**支持复数：** 是

### **CS** — 信道响应 *Nt*×*Nr*×*Ns* 复值 MATLAB® 数组

信道响应，以 *Nt*×*Nr*×*Ns* 复值 MATLAB 数组形式返回。*Nt* 是发射阵列元素的数量。*Nr* 是接收阵列元素的数量。*Ns* 是散射体的数量。数组的每一页对应特定散射体的信道响应矩阵。

#### 依赖关系

要启用此端口，请选中 **Output channel response** 复选框。

**数据类型：** `double`
**支持复数：** 是

### **Tau** — 路径延迟 1×*Ns* 实值向量

路径延迟，以 1×*Ns* 实值向量形式返回。*Ns* 是散射体的数量。每个元素对应从发射阵列相位中心到散射体再到接收阵列相位中心的路径时间延迟。

#### 依赖关系

要启用此端口，请选中 **Output channel response** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: ''
- name: Signal carrier frequency (Hz)
  summary: 信号载波频率 3e8（默认）| 正标量
  group: ''
- name: Polarization configuration
  summary: 极化配置 None（默认）| Combined | Dual
  group: ''
- name: Specify atmospheric parameters
  summary: 启用大气衰减模型 off（默认）| on
  group: ''
- name: Temperature (degrees Celsius)
  summary: 环境温度 15（默认）| 实值标量
  group: ''
- name: Dry air pressure (Pa)
  summary: 大气干空气压力 101.325e3（默认）| 正实值标量
  group: ''
- name: Water vapour density (g/m^3)
  summary: 大气水蒸气密度 7.5（默认）| 正实值标量
  group: ''
- name: Liquid water density (g/m^3)
  summary: 液态水密度 0.0（默认）| 非负实值标量
  group: ''
- name: Rain rate (mm/hr)
  summary: 降雨率 0.0（默认）| 非负实值标量
  group: ''
- name: Inherit sample rate
  summary: 从上游模块继承采样率 on（默认）| off
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认）| 正实值标量
  group: ''
- name: Simulate direct path propagation
  summary: 启用沿直接路径的传播 off（默认）| on
  group: ''
- name: Maximum delay (s)
  summary: 最大信号延迟 10e-6（默认）| 正标量
  group: ''
- name: Output channel response
  summary: 启用信道响应输出 off（默认）| on
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
- name: 将传感器阵列指定为
  summary: 指定阵列的方法 Array (no subarrays)（默认）| MATLAB expression
  group: ''
- name: 表达式
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System 对象
  group: ''
- name: 阵元类型
  summary: 阵列阵元类型 Isotropic Antenna（默认）| Cosine Antenna | Custom Antenna | Omni Microphone | Custom Microphone
  group: ''
- name: 工作频率范围 (Hz)
  summary: 天线或麦克风阵元的工作频率范围 [0,1e20]（默认）| 实值 1×2 行向量
  group: ''
- name: 工作频率向量 (Hz)
  summary: 自定义天线或麦克风阵元的工作频率范围 [0,1e20]（默认）| 实值行向量
  group: ''
- name: 阵元背面加障板
  summary: 将 Isotropic Antenna 阵元或 Omni Microphone 阵元的背面响应设置为零 关（默认）| 开
  group: ''
- name: 余弦方向图指数
  summary: 方位和俯仰余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实值 1×2 矩阵
  group: ''
- name: 频率响应 (dB)
  summary: 天线和麦克风频率响应 [0,0]（默认）| 实值行向量
  group: ''
- name: Input Pattern Coordinate System
  summary: 自定义天线方向图的坐标系 az-el（默认）| phi-theta
  group: ''
- name: Azimuth angles (deg)
  summary: 天线辐射方向图的方位角 [-180:180]（默认）| 实值行向量
  group: ''
- name: Elevation angles (deg)
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实值行向量
  group: ''
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角坐标 0:360 | 实值 1×*P* 行向量
  group: ''
- name: Theta Angles (deg)
  summary: 自定义天线辐射方向图的 Theta 角坐标 0:180 | 实值 1×*Q* 行向量
  group: ''
- name: Magnitude pattern (dB)
  summary: 组合天线辐射方向图的幅度 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: Phase pattern (deg)
  summary: 自定义天线辐射相位方向图 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: MatchArrayNormal
  summary: 将天线阵子旋转至阵列法向 on（默认）| off
  group: ''
- name: Polar pattern frequencies (Hz)
  summary: 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量
  group: ''
- name: Polar pattern angles (deg)
  summary: 极坐标方向图响应角度 [-180:180]（默认）| 实值 1×*P* 行向量
  group: ''
- name: Polar pattern (dB)
  summary: 自定义麦克风极坐标响应 zeros(1,361)（默认）| 实值 *L*×*P* 矩阵
  group: ''
- name: Geometry
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: ''
- name: Number of elements
  summary: 阵列阵元数量 ULA 阵列为 2，UCA 阵列为 5（默认）| 大于或等于 2 的整数
  group: ''
- name: Element spacing (m)
  summary: 阵列阵元之间的间距 ULA 阵列为 0.5，URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为由正值组成的 2 元素向量
  group: ''
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: ''
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 正整数向量
  group: ''
- name: Element lattice
  summary: URA 元素位置的晶格 Rectangular（默认）| Triangular
  group: ''
- name: Array normal
  summary: 阵列法线方向 URA 阵列为 x 或 UCA 阵列为 z（默认）| y
  group: ''
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: ''
- name: Element positions (m)
  summary: 共形阵列元素的位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: ''
- name: Element normals (deg)
  summary: 共形阵列单元法向量方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: ''
- name: Taper
  summary: 阵列单元锥削 1 (默认) | 复标量 | 复值行向量
  group: ''
- name: Source of transmit array motion
  summary: 指定发射阵列运动参数的来源 Property (默认) | Input port
  group: ''
- name: Position of the transmit array (m)
  summary: 发射阵列位置 [0;0;0] (默认) | 实值 3×1 向量
  group: ''
- name: Orientation of the transmit array
  summary: 设置发射阵列轴的方向 eye(3,3) (默认) | 实值 3×3 正交矩阵
  group: ''
- name: 接收阵列运动源
  summary: 指定接收阵列运动参数的来源 Property（默认）| Input port
  group: ''
- name: 接收阵列位置 (m)
  summary: 接收阵列的位置 [physconst('LightSpeed' )/1e5; 0;0]（默认）| 实值 3×1 向量
  group: ''
- name: 接收阵列朝向
  summary: 设置接收阵列轴的朝向 eye(3,3)（默认）| 实值 3×3 正交矩阵
  group: ''
- name: 散射体规格
  summary: 指定散射体参数的来源 Auto（默认）| Property | Input port
  group: ''
- name: 散射体数量
  summary: 散射体的数量 1（默认）| 非负整数
  group: ''
- name: 散射体位置边界
  summary: 将散射体位置约束在边界内 [0,1000]（默认）| 1×2 实值向量 | 3×2 实值矩阵
  group: ''
- name: Positions of scatterers (m)
  summary: 散射体位置 [physconst('LightSpeed' )*5e-6;0;0]（默认）| 实值 3×*Ns* 矩阵
  group: ''
- name: ScattererCoefficient
  summary: 散射系数 1（默认）| 复值 1×*Ns* 矩阵
  group: ''
```

#### 主选项卡

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 信号载波频率 `3e8`（默认）| 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **Polarization configuration** — 极化配置 `None`（默认）| `Combined` | `Dual`

极化配置，指定为 `None`、`Combined` 或 `Dual`。当您将此参数设置为 `None` 时，输出场被视为标量场。当您将此参数设置为 `None` 时，辐射场是极化的，并被解释为传感器固有极化中的单一信号。当您将此参数设置为 `Dual` 时，辐射场的 *H* 和 *V* 极化分量是独立信号。

**数据类型：** `char`

### **Specify atmospheric parameters** — 启用大气衰减模型 off（默认）| on

选中此参数以启用添加由大气气体、雨、雾或云引起的信号衰减。当您选中此参数时，**Temperature (degrees Celsius)**、**Dry air pressure (Pa)**、**Water vapour density (g/m^3)**、**Liquid water density (g/m^3)** 和 **Rain rate (mm/hr)** 参数将出现在对话框中。

**数据类型：** `Boolean`

### **Temperature (degrees Celsius)** — 环境温度 `15`（默认）| 实值标量

环境温度，指定为实值标量。单位为摄氏度。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Dry air pressure (Pa)** — 大气干空气压力 `101.325e3`（默认）| 正实值标量

大气干空气压力，指定为正实值标量。单位为帕斯卡（Pa）。此参数的默认值对应一个标准大气压。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Water vapour density (g/m^3)** — 大气水蒸气密度 `7.5`（默认）| 正实值标量

大气水蒸气密度，指定为正实值标量。单位为 g/m3。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `datetime`

### **Liquid water density (g/m^3)** — 液态水密度 `0.0`（默认）| 非负实值标量

雾或云的液态水密度，指定为非负实值标量。
单位为 g/m3。液态水密度的典型值为：中雾 0.05，浓雾 0.5。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Rain rate (mm/hr)** — 降雨率 `0.0`（默认）| 非负实值标量

降雨率，指定为非负实值标量。单位为
mm/hr。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选中此参数以从上游模块继承采样率。否则，
使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Simulate direct path propagation** — 启用沿直接路径的传播 off（默认）| on

选中此复选框以启用信号沿从发射阵列到接收阵列的
视距直接路径传播，且无散射。

**数据类型：** `Boolean`

### **Maximum delay (s)** — 最大信号延迟 `10e-6`（默认）| 正标量

最大信号延迟，指定为正标量。大于此值的
延迟将被忽略。

**数据类型：** `double`

### **Output channel response** — 启用信道响应输出 off（默认）| on

选中此复选框以通过输出端口 `CS` 和 `Tau` 输出信道响应和
时间延迟。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果您希望模块使用
MATLAB 解释器，请选择 `Interpreted Execution`。如果您
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行
更快。

当您在开发和调整模型时，解释执行非常有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成的代码比
解释执行运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |

#### 发射和接收阵列选项卡

### **将传感器阵列指定为** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

用于指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **表达式** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System 对象

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System 对象。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **将传感器阵列指定为** 设置为 `MATLAB expression`。

#### 阵元参数

### **阵元类型** — 阵列阵元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认）| 实值 1×2 行向量

将天线或麦克风阵元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。阵元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风阵元在此向量的最小和最大元素所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 设置这些频率处的响应。

### **阵元背面加障板** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 关（默认）| 开

选中此复选框可对阵元的背面响应加障板。加背面障板后，所有偏离视轴超过 ±90° 的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **阵元类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **余弦方向图指数** — 方位和俯仰余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **余弦方向图指数** 为 1×2 向量时，第一个元素是方位方向的指数，第二个元素是俯仰方向的指数。当将此参数设置为标量时，方位方向和俯仰方向余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Cosine Antenna`。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在 **工作频率向量 (Hz)** 参数所定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Antenna` 或
`Custom
Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为
`az-el` 或 `phi-theta`。当您
指定 `az-el` 时，使用 **Azimuth angles
(deg)** 和 **Elevations angles (deg)** 参数来
指定方向图点的坐标。当您指定
`phi-theta` 时，使用 **Phi angles (deg)**
和 **Theta angles (deg)** 参数来指定方向图点的
坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

指定用于计算天线辐射方向图的方位角，
以 1×*P* 行向量表示。*P* 必须
大于 2。方位角必须介于 –180° 和 180° 之间
（含端点），且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

指定用于计算辐射方向图的仰角，以
1×*Q* 向量表示。*Q* 必须
大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间
（含端点），且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

用于指定天线辐射方向图的点的 Phi 角，指定为
实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，且必须
严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

用于指定天线辐射方向图的点的 Theta 角，指定为
实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须介于 0° 和 360° 之间，且必须
严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (**

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵子旋转至阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵子方向图旋转至与阵列法向对齐。未选中时，阵子方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵子坐标系的 *x* 轴指向阵列法向。未选中时使用未经旋转的阵子方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵子坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量所指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风的中心拾取轴测量，且必须在 –180° 到 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元的极坐标方向图幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数量，指定为大于或等于 2 的整数。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元之间的间距 ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为由正值组成的 2 元素向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或由正值组成的 1×2 向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀间隔排列。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量具有
  形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列的每一行和每一列具有相同
  数量的元素。

对于 URA，阵列元素沿最左侧阵列列从上到下索引，然后从左到右继续到下一列。在此
图中，**Array size** 值 `[3,2]` 创建一个
具有三行两列的阵列。

#### 依赖

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 元素位置的晶格 `Rectangular`（默认）| `Triangular`

URA 元素位置的晶格，指定为 `Rectangular`
或 `Triangular`。

- `Rectangular` — 将所有元素沿
  行和列方向对齐。
- `Triangular` — 将矩形晶格的偶数行
  元素向正行轴方向偏移。
  位移为沿行维度的元素间距的一半。

#### 依赖

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Array normal** — 阵列法线方向 URA 阵列为 `x` 或 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为
`x`、
`y` 或
`z`。

平面阵列的元素位于与所选阵列法线方向正交的平面内。元素视轴
方向指向阵列法线
方向。

| Array Normal 参数值 | 元素位置和视轴方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面内。所有元素视轴向量指向 *x* 轴。 |
| `y` | 阵列元素位于 *zx* 平面内。所有元素视轴向量指向 *y* 轴。 |
| `z` | 阵列元素位于 *xy* 平面内。所有元素视轴向量指向 *z* 轴。 |

#### 依赖

要启用此参数，请将
**Geometry** 设置为
`URA` 或
`UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖

要启用此参数，请将 **Geometry** 设置为
`UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中元素的位置，指定为
3×*N* 实数值矩阵，其中 *N* 是
共形阵列中的元素数量。此矩阵的每一列表示
阵列局部坐标系中阵列元素的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位
为米。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `Conformal
Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列单元法向量方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中单元法向量方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的单元数量。如果参数值为矩阵，则每一列以 `[azimuth;elevation]` 的形式指定对应单元相对于局部坐标系的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列单元使用相同的指向方向。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意一种单元对之间通过特定变换产生差异的排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列单元锥削 1 (默认) | 复标量 | 复值行向量

将单元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的单元数量。

锥削也称为*单元权重*，用于乘以阵列单元响应。锥削修改响应的幅度和相位，以降低旁瓣或引导主响应轴。

如果 **Taper** 为标量，则对每个单元应用相同的权重。如果 **Taper** 为向量，则将向量中的权重应用于对应的传感器单元。权重数量必须与阵列的单元数量匹配。

**数据类型：** `double`

#### 运动选项卡

### **Source of transmit array motion** — 指定发射阵列运动参数的来源 `Property` (默认) | `Input port`

发射阵列运动参数的来源，指定为 `Property` 或 `Input port`。

- 当您选择 `Property` 时，使用 **Position of the transmit array (m)** 和 **Orientation of the transmit array** 参数指定阵列位置和方向。阵列是静止的。
- 当您选择 `Input port` 时，使用模块的 `TxPos`、`TxVel` 和 `TxAxes` 输入端口指定阵列位置、速度和方向。

**数据类型：** `char`

### **Position of the transmit array (m)** — 发射阵列位置 `[0;0;0]` (默认) | 实值 3×1 向量

发射阵列相位中心的位置，指定为相对于全局坐标系的笛卡尔形式 `[x;y;z]` 的实值 3×1 向量。单位为米。

#### 依赖关系

要启用此参数，请将 **Source of transmit array motion** 参数设置为 `Property`。

**数据类型：** `double`

### **Orientation of the transmit array** — 设置发射阵列轴的方向 `eye(3,3)` (默认) | 实值 3×3 正交矩阵

发射阵列的方向，指定为实值 3×3 正交矩阵。该矩阵指定定义阵列局部坐标系的三个轴相对于全局坐标系的方向。矩阵的列分别对应于 *x*、*y* 和 *z* 轴。

#### 依赖关系

要启用此参数，请将 **Source of transmit array motion** 参数设置为 `Property`。

**数据类型：** `double`

### **接收阵列运动源** — 指定接收阵列运动参数的来源 `Property`（默认）| `Input port`

接收阵列运动参数的来源，指定为 `Property` 或 `Input port`。

- 当您选择 `Property` 时，使用 **接收阵列位置 (m)** 和 **接收阵列朝向** 参数指定阵列的位置和朝向。阵列是静止的。
- 当您选择 `Input port` 时，使用模块的 `RxPos`、`RxVel` 和 `RxAxes` 输入端口指定阵列的位置、速度和朝向。

**数据类型：** `char`

### **接收阵列位置 (m)** — 接收阵列的位置 `[physconst('LightSpeed' )/1e5; 0;0]`（默认）| 实值 3×1 向量

接收阵列相位中心的位置，指定为相对于全局坐标系的笛卡尔形式 `[x;y;z]` 的实值 3×1 向量。单位为米。

#### 依赖关系

要启用此参数，请将 **接收阵列运动源** 参数设置为 `Property`。

**数据类型：** `double`

### **接收阵列朝向** — 设置接收阵列轴的朝向 `eye(3,3)`（默认）| 实值 3×3 正交矩阵

接收阵列的朝向，指定为实值 3×3 正交矩阵。该矩阵指定了定义阵列局部坐标系的三个轴相对于全局坐标系的方向。矩阵的列分别对应于 *x*、*y* 和 *z* 轴。

#### 依赖关系

要启用此参数，请将 **接收阵列运动源** 参数设置为 `Property`。

**数据类型：** `double`

### **散射体规格** — 指定散射体参数的来源 `Auto`（默认）| `Property` | `Input port`

散射体参数的来源，指定为 `Auto`、`Property` 或 `Input port`。

- 当您将此参数设置为 `Auto` 时，所有散射体位置和系数都是随机生成的。散射体速度为零。生成的位置包含在由 **散射体位置边界** 参数设置的区域内。使用 **散射体数量** 参数设置散射体的数量。
- 当您将此属性设置为 `Property` 时，使用 **散射体位置 (m)** 参数设置散射体位置。使用 **散射系数** 参数设置散射系数。散射体速度为零。
- 当您将此参数设置为 `Input port` 时，使用 `ScatPos`、`ScatVel` 和 `ScatCoef` 模块输入端口指定散射体位置、速度和散射系数。

**数据类型：** `char`

### **散射体数量** — 散射体的数量 `1`（默认）| 非负整数

散射体的数量，指定为非负整数。

#### 依赖关系

要启用此属性，请将 **散射体规格** 参数设置为 `Auto`。

**数据类型：** `double`

### **散射体位置边界** — 将散射体位置约束在边界内 `[0,1000]`（默认）| 1×2 实值向量 | 3×2 实值矩阵

散射体位置边界，指定为 1×2 实值行向量或 3×2 实值矩阵。如果边界是 1×2 行向量，则该向量包含所有三个维度的最小值和最大值 `[minbdry maxbdry]`。如果边界是 3×2 矩阵，则该矩阵以 `[x_minbdry x_maxbdry;y_minbdry y_maxbdry; z_minbdry z_maxbdry]` 的形式指定所有三个维度的边界。

#### 依赖关系

要启用此属性，请将 **散射体规格** 参数设置为 `Auto`。

**数据类型：** `double`

### **Positions of scatterers (m)** — 散射体位置 `[physconst('LightSpeed' )*5e-6;0;0]`（默认）| 实值 3×*Ns* 矩阵

散射体的位置，指定为实值 3×*Ns* 矩阵。*Ns* 是散射体的数量。每一列代表一个不同的散射体，并具有相对于全局坐标系的笛卡尔形式 `[x;y;z]`。单位为米。

#### 依赖关系

要启用此属性，请将 **Scatterer specification** 参数设置为 `Property`。

**Data Types:** `double`

### **ScattererCoefficient** — 散射系数 `1`（默认）| 复值 1×*Ns* 矩阵

散射系数，指定为复值 1×*Ns* 向量。*Ns* 是散射体的数量。单位无量纲。

#### 依赖关系

要启用此属性，请将 **Scatterer specification** 参数设置为 `Property`。

**Data Types:** `double`
**Complex Number Support:** Yes
## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

散射 MIMO 传播信道

Scattering MIMO Channel 对三维多径传播信道进行建模，其中从发射阵列辐射的信号经多个散射体反射后返回接收阵列。在该信道中，传播路径是从点到点的直接路径（视距）。该模块对距离相关的时间延迟、增益、多普勒频移、相位变化以及由气体、雨、雾和云引起的大气损耗进行建模。您可以选择通过从发射机到接收机的直接路径传播信号。

大气气体和雨的衰减模型适用于频率范围 1–1000 GHz 的电磁信号，但雾和云的衰减模型仅适用于 10–1000 GHz。在这些频率范围之外，该对象使用最近的有效值。
