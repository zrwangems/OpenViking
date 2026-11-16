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

### 输入

### **X** — 发射窄带信号 *M*×*Nt* 复值矩阵

发射窄带信号，指定为 *M*×*Nt* 复值矩阵。量 *M* 是信号中的样本数，*Nt* 是发射阵列元素数。每一列表示对应阵列元素发射的信号。

**示例：** `[1,1;j,1;0.5,0]`

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `None` 或 `Combined`。

**数据类型：** `double`
**复数支持：** Yes

### **XH** — 发射窄带 H 极化信号 *M*×*Nt* 复值矩阵

发射窄带 *H* 极化信号，指定为 *M*×*Nt* 复值矩阵。量 *M* 是信号中的样本数，*Nt* 是发射阵列元素数。每一列表示对应阵列元素发射的信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**示例：** `[1,1;j,1;0.5,0]`

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** Yes

### **XV** — 发射窄带 V 极化信号 *M*×*Nt* 复值矩阵

发射窄带 *V* 极化信号，指定为 *M*×*Nt* 复值矩阵。量 *M* 是信号中的样本数，*Nt* 是发射阵列元素数。每一列表示对应阵列元素发射的信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** Yes

### **TxPos** — 发射天线阵列的位置 3×1 实值列向量

发射天线阵列的位置，指定为 3×1 实值列向量，形式为 `[x;y;z]`。向量元素对应于阵列的 *x*、*y* 和 *z* 位置。单位为 meters。

#### 依赖关系

要启用此端口，请将 **发射阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **TxVel** — 发射天线阵列的速度 3×1 实值列向量

发射天线阵列的速度，指定为 3×1 实值列向量，形式为 `[vx;vy;vz]`。向量元素对应于阵列的 *x*、*y* 和 *z* 速度。单位为 meters per second。

#### 依赖关系

要启用此端口，请将 **发射阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **TxAxes** — 发射天线阵列的轴方向 3×3 实正交矩阵

发射天线阵列的轴方向，指定为 3×3 实正交矩阵。该矩阵定义阵列局部坐标系相对于全局坐标的姿态。矩阵列对应于局部坐标系的 *x*、*y* 和 *z* 轴方向。单位无量纲。

#### 依赖关系

要启用此端口，请将 **发射阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxPos** — 接收天线阵列的位置 3×1 实值列向量

接收天线阵列的位置，指定为 3×1 实值列向量，形式为 `[x;y;z]`。向量元素对应于阵列的 *x*、*y* 和 *z* 位置。单位为 meters。

#### 依赖关系

要启用此端口，请将 **接收阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxVel** — 接收天线阵列的速度 3×1 实值列向量

接收天线阵列的速度，指定为 3×1 实值列向量，形式为 `[vx;vy;vz]`。向量元素对应于阵列的 *x*、*y* 和 *z* 速度。单位为 meters per second。

#### 依赖关系

要启用此端口，请将 **接收阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **RxAxes** — 接收天线阵列的轴方向 3×3 实正交矩阵

接收天线阵列的轴方向，指定为 3×3 实正交矩阵。该矩阵定义阵列局部坐标系相对于全局坐标的姿态。矩阵列对应于局部坐标系的 *x*、*y* 和 *z* 轴方向。单位无量纲。

#### 依赖关系

要启用此端口，请将 **接收阵列运动源** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatPos** — 散射体的位置 3×*Ns* 实值矩阵

散射体的位置，指定为 3×*Ns* 实值矩阵。矩阵的每一列形式为 `[x;y;z]`，包含一个散射体的 *x*、*y* 和 *z* 位置。单位为 meters。

#### 依赖关系

要启用此端口，请将 **散射体指定** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatVel** — 散射体的速度 3×*Ns* 实值矩阵

散射体的速度，指定为 3×*Ns* 实值矩阵。每个矩阵列的形式为 `[vx;vy;vz]`，包含一个散射体的 *x*、*y* 和 *z* 速度。单位为 meters per second。

#### 依赖关系

要启用此端口，请将 **散射体指定** 参数设置为 `Input port`。

**数据类型：** `double`

### **ScatCoef** — 散射系数 1×*Ns* 复值行向量

散射系数，指定为 1×*Ns* 复值行向量。每个向量元素指定对应散射体的散射系数。单位无量纲。

#### 依赖关系

要启用此端口，请将 **散射体指定** 参数设置为 `Input port`。

**数据类型：** `double`
**复数支持：** Yes

### 输出

### **Y** — 接收窄带信号 *M*×*Nr* 复值矩阵

接收窄带信号，返回为 *M*×*Nr* 复值矩阵。量 *M* 是信号中的样本数，*Nr* 是接收阵列元素数。每一列表示对应阵列元素接收的信号。

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `None` 或 `Combined`。

**数据类型：** `double`
**复数支持：** Yes

### **YH** — 接收窄带 H 极化信号 复值 *M*×*Nr* 矩阵

接收窄带 *H* 极化信号，返回为复值 *M*×*Nr* 矩阵。*M* 是信号中的样本数，*Nr* 是接收阵列元素数。每一列表示对应阵列元素接收的信号。

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** Yes

### **YV** — 接收窄带 V 极化信号 复值 *M*×*Nr* 矩阵

接收窄带 *V* 极化信号，返回为复值 *M*×*Nr* 矩阵。*M* 是信号中的样本数，*Nr* 是接收阵列元素数。每一列表示对应阵列元素接收的信号。

#### 依赖关系

要启用此端口，请将 **极化配置** 参数设置为 `Dual`。

**数据类型：** `double`
**复数支持：** Yes

### **CS** — 信道响应 *Nt*×*Nr*×*Ns* 复值 MATLAB® 数组

信道响应，返回为 *Nt*×*Nr*×*Ns* 复值 MATLAB 数组。*Nt* 是发射阵列元素数。*Nr* 是接收阵列元素数。*Ns* 是散射体数。数组的每一页对应于特定散射体的信道响应矩阵。

#### 依赖关系

要启用此端口，请选中 **输出信道响应** 复选框。

**数据类型：** `double`
**复数支持：** Yes

### **Tau** — 路径延迟 1×*Ns* 实值向量

路径延迟，返回为 1×*Ns* 实值向量。*Ns* 是散射体数。每个元素对应于从发射阵列相位中心到散射体再到达接收阵列相位中心的路径时间延迟。

#### 依赖关系

要启用此端口，请选中 **输出信道响应** 复选框。

**数据类型：** `double`

## 参数

#### 主选项卡

### **传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (default) | positive scalar

信号传播速度，指定为实值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **信号载波频率 (Hz)** — 信号载波频率 `3e8` (default) | positive scalar

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **极化配置** — 极化配置 `None` (default) | `Combined` | `Dual`

极化配置，指定为 `None`、`Combined` 或 `Dual`。当您将此参数设置为 `None` 时，输出场被视为标量场。当您将此参数设置为 `None` 时，辐射场被极化，并解释为传感器固有极化中的单个信号。当您将此参数设置为 `Dual` 时，辐射场的 *H* 和 *V* 极化分量是独立信号。

**数据类型：** `char`

### **指定大气参数** — 启用大气衰减模型 off (default) | on

选择此参数可启用以添加由大气气体、雨、雾或云引起的信号衰减。当您选择此参数时，**温度 (degrees Celsius)**、**干空气压力 (Pa)**、**水汽密度 (g/m^3)**、**液态水密度 (g/m^3)** 和 **降雨率 (mm/hr)** 参数将出现在对话框中。

**数据类型：** `Boolean`

### **温度 (degrees Celsius)** — 环境温度 `15` (default) | real-valued scalar

环境温度，指定为实值标量。单位为 degrees Celsius。

#### 依赖关系

要启用此参数，请选中 **指定大气参数** 复选框。

**数据类型：** `double`

### **干空气压力 (Pa)** — 大气干空气压力 `101.325e3` (default) | positive real-valued scalar

大气干空气压力，指定为正实值标量。单位为 pascals (Pa)。此参数的默认值对应于一个标准大气压。

#### 依赖关系

要启用此参数，请选中 **指定大气参数** 复选框。

**数据类型：** `double`

### **水汽密度 (g/m^3)** — 大气水汽密度 `7.5` (default) | positive real-valued scalar

大气水汽密度，指定为正实值标量。单位为 g/m3。

#### 依赖关系

要启用此参数，请选中 **指定大气参数** 复选框。

**数据类型：** `datetime`

### **液态水密度 (g/m^3)** — 液态水密度 `0.0` (default) | nonnegative real-valued scalar

雾或云的液态水密度，指定为非负实值标量。单位为 g/m3。液态水密度的典型值为：中等雾为 0.05，浓雾为 0.5。

#### 依赖关系

要启用此参数，请选中 **指定大气参数** 复选框。

**数据类型：** `double`

### **降雨率 (mm/hr)** — 降雨率 `0.0` (default) | non-negative real-valued scalar

降雨率，指定为非负实值标量。单位为 mm/hr。

#### 依赖关系

要启用此参数，请选中 **指定大气参数** 复选框。

**数据类型：** `double`

### **继承采样率** — 从上游模块继承采样率 on (default) | off

选择此参数以从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **采样率 (Hz)** — 信号采样率 `1e6` (default) | positive real-valued scalar

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **继承采样率** 复选框。

**数据类型：** `double`

### **仿真直接路径传播** — 启用沿直接路径传播 off (default) | on

选中此复选框可启用以无散射方式沿从发射阵列到接收阵列的视距直接路径传播信号。

**数据类型：** `Boolean`

### **最大延迟 (s)** — 最大信号延迟 `10e-6` (default) | positive scalar

最大信号延迟，指定为正标量。大于此值的延迟将被忽略。

**数据类型：** `double`

### **输出信道响应** — 启用信道响应输出 off (default) | on

选中此复选框可通过输出端口 `CS` 和 `Tau` 输出信道响应和时间延迟。

**数据类型：** `Boolean`

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (default) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

下表显示了 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### 发射和接收阵列选项卡

### **将传感器阵列指定为** — 指定阵列的方法 `Array (no subarrays)` (default) | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建数组的 MATLAB 表达式 Phased Array System Toolbox™ array System object

用于创建数组的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox array System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，将 **Specify sensor array as** 设置为
`MATLAB expression`。

#### 元素参数

### **Element type** — 阵列元素类型 `Isotropic Antenna` (default) | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风元素的工作频率范围 `[0,1e20]` (default) | real-valued 1-by-2 row vector

将天线或麦克风元素的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1-by-2
行向量。该元素在此频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Isotropic Antenna`、`Cosine Antenna` 或
`Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风元素的工作频率范围 `[0,1e20]` (default) | real-valued row vector

将设置天线和麦克风频率响应的频率指定为
由递增实数值组成的 1-by-*L* 行向量。天线或
麦克风元素在此向量的最小
和最大元素所指定的频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。使用
**Frequency responses (dB)** 设置这些
频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元素或 `Omni Microphone` 元素的后向响应设置为零 off (default) | on

选中此复选框以遮挡元素的后向响应。当后向被遮挡时，所有偏离宽边方向超过 ±90° 的方位角处的响应均设置为零。宽边方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，将
**Element type** 设置为
`Isotropic Antenna` 或
`Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和俯仰角余弦方向图的指数 `[1.5 1.5]` (default) | 非负标量 | 由非负值组成的 real-valued 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或
由非负值组成的 real-valued 1-by-2 矩阵。当
**Exponent of cosine pattern** 是
1-by-2 向量时，第一个元素是方位角
方向的指数，第二个元素是
俯仰角方向的指数。将此参数设置为标量时，
方位角方向和俯仰角方向余弦
方向图均升到相同的幂。

#### 依赖关系

要启用此参数，将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]` (default) | real-valued row vector

自定义天线或自定义
麦克风在 **Operating frequency vector (Hz)** 参数所定义频率处的频率响应。
**Frequency responses (dB)** 的维度必须
与 **Operating frequency vector (Hz)** 参数指定的向量的维度匹配。

#### 依赖关系

要启用此参数，将
**Element type** 设置为
`Custom Antenna` 或
`Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el` (default) | `phi-theta`

自定义天线方向图的坐标系，指定为
`az-el` 或 `phi-theta`。指定
`az-el` 时，使用 **Azimuth angles
(deg)** 和 **Elevations angles (deg)** 参数
指定方向图点的坐标。指定
`phi-theta` 时，使用 **Phi angles (deg)**
和 **Theta angles (deg)** 参数指定
方向图点的坐标。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]` (default) | real-valued row vector

将计算天线辐射方向图的方位角指定为
1-by-*P* 行向量。*P* 必须
大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的俯仰角 `[-90:90]` (default) | real-valued row vector

将计算辐射方向图的俯仰角指定为
1-by-*Q* 向量。*Q* 必须
大于 2。角度单位是 degrees。俯仰角必须介于
–90° 和 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | real-valued 1-by-*P* row vector

指定天线辐射方向图的点的 Phi 角，指定为
real-valued 1-by-*P* 行向量。*P* 必须
大于 2。角度单位是 degrees。Phi 角必须介于 0° 和 360° 之间，并且
严格递增。

#### 依赖关系

要启用此参数，将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | real-valued 1-by-*Q* row vector

指定天线辐射方向图的点的 Theta 角，指定为
real-valued 1-by-*Q* 行向量。*Q* 必须
大于 2。角度单位是 degrees。Theta 角必须介于 0° 和 360° 之间，并且
严格递增。

#### 依赖关系

要启用此参数，将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

组合天线辐射方向图的幅度，指定为
*Q*-by-*P* 矩阵或
*Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数
  设置为 `az-el` 时，*Q* 等于
  由 **Elevation angles
  (deg)** 参数指定的向量的长度，*P* 等于
  由 **Azimuth angles (deg)**
  参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数
  设置为 `phi-theta` 时，*Q* 等于
  由 **Theta Angles
  (deg)** 参数指定的向量的长度，*P* 等于
  由 **Phi Angles (deg)**
  参数指定的向量的长度。

量 *L* 等于
**Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P*
  矩阵，则同一方向图应用于
  **Operating frequency vector (Hz)**
  参数中指定的 *所有* 频率。
- 如果该值是
  *Q*-by-*P*-by-*L*
  数组，则数组的每个 *Q*-by-*P* 页
  为 **Operating frequency vector (Hz)**
  参数中指定的 *对应* 频率指定一个方向图。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)` (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

组合天线辐射方向图的相位，指定为
*Q*-by-*P* 矩阵或
*Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数
  设置为 `az-el` 时，*Q* 等于
  由 **Elevation angles
  (deg)** 参数指定的向量的长度，*P* 等于
  由 **Azimuth angles (deg)**
  参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数
  设置为 `phi-theta` 时，*Q* 等于
  由 **Theta Angles
  (deg)** 参数指定的向量的长度，*P* 等于
  由 **Phi Angles (deg)**
  参数指定的向量的长度。

量 *L* 等于
**Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P*
  矩阵，则同一方向图应用于
  **Operating frequency vector (Hz)**
  参数中指定的 *所有* 频率。
- 如果该值是
  *Q*-by-*P*-by-*L*
  数组，则数组的每个 *Q*-by-*P* 页
  为 **Operating frequency vector (** 中指定的
  *对应* 频率指定一个方向图。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Antenna`。

### **MatchArrayNormal** — 将天线元素旋转到阵列法线 `on` (default) | `off`

选中此复选框以旋转天线元素方向图，使其与阵列法线对齐。未选中时，元素方向图不旋转。

当天线用于天线阵列并且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使元素坐标系的 *x* 轴沿阵列法线指向。未选中时使用未旋转的元素方向图。

当天线用于天线阵列并且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使元素坐标系的 *z* 轴沿阵列法线指向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖关系

要启用此参数，将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3 (default) | real scalar | real-valued 1-by-*L* row vector

极坐标方向图麦克风响应频率，指定为 real scalar，或
real-valued、1-by-*L* 向量。响应频率位于
**Operating frequency vector (Hz)**
向量指定的频率范围内。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角 `[-180:180]` (default) | real-valued -by-*P* row vector

将极坐标方向图响应角指定为 1-by-*P* 向量。角度
从麦克风的中心拾取轴测量，并且必须介于
–180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)` (default) | real-valued *L*-by-*P* matrix

将自定义麦克风元素极坐标方向图的幅度指定为
*L*-by-*P* 矩阵。*L* 是
**Polar pattern frequencies (Hz)** 中指定的频率数。
*P* 是 **Polar pattern
angles (deg)** 中指定的角度数。矩阵的每一行表示
在 **Polar
pattern frequencies (Hz)** 中指定的对应频率以及 **Polar
pattern angles (deg)** 中指定的所有角度处测量的
极坐标方向图幅度。方向图在方位平面中测量。在
方位平面中，俯仰角为 0°，中心拾取轴为 0°
degrees 方位角和 0° degrees 俯仰角。极坐标方向图围绕
中心轴对称。你可以根据
极坐标方向图构造 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，将 **Element type** 设置为
`Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA` (default) | `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意元素
  位置

### **Number of elements** — 阵列元素数 对于 ULA 阵列，`2`；对于 UCA 阵列，`5` (default) | 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列元素数，指定为大于
或等于 2 的整数。

#### 依赖关系

要启用此参数，将 **Geometry** 设置为
`ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列元素之间的间距 对于 ULA 阵列，`0.5`；对于 URA 阵列，`[0.5,0.5]` (default) | 对于 ULA 或 URA 阵列，正标量 | 对于 URA 阵列，由正值组成的 2 元素向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距
  指定为正标量。
- URA — 将间距指定为正标量或由正值组成的 1-by-2 向量。
  如果 **Element spacing (m)** 是标量，
  则行间距和列间距相等。如果 **Element spacing
  (m)** 是向量，则该向量的形式为
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，将 **Geometry** 设置为
`ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y` (default) | `x` | `z`

ULA 的线性轴方向，指定为 `y`、
`x` 或 `z`。所有 ULA 阵列
元素在本地阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，将 **Geometry** 设置为
  `ULA`。
- 当模块仅支持 ULA
  阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]` (default) | 正整数 | 由正整数组成的 1-by-2 向量

URA 阵列的维度，指定为正整数或由
正整数组成的 1-by-2 向量。

- 如果 **Array size** 是 1-by-2 向量，则该向量的
  形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列每行和每列具有相同
  数量的元素。

对于 URA，阵列元素沿最左侧阵列列从上到下索引，
然后从左到右继续到下一列。在此
图中，**Array size** 值 `[3,2]` 创建
具有三行两列的阵列。

#### 依赖关系

要启用此参数，将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 元素位置的栅格 `Rectangular` (default) | `Triangular`

URA 元素位置的栅格，指定为 `Rectangular`
或 `Triangular`。

- `Rectangular` — 将
  行和列方向上的所有元素对齐。
- `Triangular` — 将矩形栅格的偶数行
  元素向正行轴方向偏移。
  位移为沿行维度元素间距的一半。

#### 依赖关系

要启用此参数，将 **Geometry** 设置为
`URA`。

### **Array normal** — 阵列法线方向 对于 URA 阵列，`x`；对于 UCA 阵列，`z` (default) | `y`

阵列法线方向，指定为
`x`、
`y` 或
`z`。

平面阵列的元素位于与
所选阵列法线方向正交的平面内。元素视轴
方向沿阵列法线
方向。

| Array Normal 参数值 | 元素位置和视轴方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面。所有元素视轴向量沿 *x* 轴指向。 |
| `y` | 阵列元素位于 *zx* 平面。所有元素视轴向量沿 *y* 轴指向。 |
| `z` | 阵列元素位于 *xy* 平面。所有元素视轴向量沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，将
**Geometry** 设置为
`URA` 或
`UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5 (default) | 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，将 **Geometry** 设置为
`UCA`。

### **阵元位置 (m)** — 共形阵列阵元的位置 `[0;0;0]`（默认） | 3×*N* 实值矩阵

共形阵列中阵元的位置，指定为 3×*N* 实值矩阵，其中 *N* 是共形阵列中阵元的数量。此矩阵的每一列表示阵列局部坐标系中一个阵元的位置 `[x;y;z]`。局部坐标系的原点是 *(0,0,0)*。单位为 meters。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **阵元法线 (deg)** — 共形阵列阵元法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中阵元的数量。如果参数值是矩阵，则每一列以 `[azimuth;elevation]` 形式指定对应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值是 2×1 列向量，则所有阵列阵元使用相同的指向方向。

您可以使用 **阵元位置 (m)** 和 **阵元法线 (deg)** 参数来表示任意排列，其中阵元对之间通过某些变换有所不同。这些变换可以组合平移、方位角旋转和仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列阵元锥削 1（默认） | 复标量 | 复值行向量

将阵元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中阵元的数量。

锥削也称为 *阵元权重*，它会乘以阵列阵元响应。锥削会修改响应的幅度和相位，以减少旁瓣或控制主响应轴的方向。

如果 **Taper** 是标量，则对每个阵元应用相同的权重。如果 **Taper** 是向量，则向量中的权重会应用到对应的传感器阵元。权重的数量必须与阵列的阵元数量匹配。

**数据类型：** `double`

#### 运动选项卡

### **发射阵列运动的来源** — 指定发射阵列运动参数的来源 `Property`（默认） | `Input port`

发射阵列运动参数的来源，指定为 `Property` 或 `Input port`。

- 当您选择 `Property` 时，使用 **发射阵列的位置 (m)** 和 **发射阵列的朝向** 参数指定阵列的位置和朝向。阵列是静止的。
- 当您选择 `Input port` 时，使用模块的 `TxPos`、`TxVel` 和 `TxAxes` 输入端口指定阵列的位置、速度和朝向。

**数据类型：** `char`

### **发射阵列的位置 (m)** — 发射阵列的位置 `[0;0;0]`（默认） | 实值 3×1 向量

发射阵列相位中心的位置，指定为相对于全局坐标系的笛卡尔形式 `[x;y;z]` 的实值 3×1 向量。单位为 meters。

#### 依赖关系

要启用此参数，请将 **发射阵列运动的来源** 参数设置为 `Property`。

**数据类型：** `double`

### **发射阵列的朝向** — 设置发射阵列轴的朝向 `eye(3,3)`（默认） | 实值 3×3 正交矩阵

发射阵列的朝向，指定为实值 3×3 正交矩阵。该矩阵指定定义阵列局部坐标系的三个轴相对于全局坐标系的方向。矩阵的列分别对应 *x*、*y* 和 *z* 轴。

#### 依赖关系

要启用此参数，请将 **发射阵列运动的来源** 参数设置为 `Property`。

**数据类型：** `double`

### **接收阵列运动的来源** — 指定接收阵列运动参数的来源 `Property`（默认） | `Input port`

接收阵列运动参数的来源，指定为 `Property` 或 `Input port`。

- 当您选择 `Property` 时，使用 **接收阵列的位置 (m)** 和 **接收阵列的朝向** 参数指定阵列的位置和朝向。阵列是静止的。
- 当您选择 `Input port` 时，使用模块的 `RxPos`、`RxVel` 和 `RxAxes` 输入端口指定阵列的位置、速度和朝向。

**数据类型：** `char`

### **接收阵列的位置 (m)** — 接收阵列的位置 `[physconst('LightSpeed' )/1e5; 0;0]`（默认） | 实值 3×1 向量

接收阵列相位中心的位置，指定为相对于全局坐标系的笛卡尔形式 `[x;y;z]` 的实值 3×1 向量。单位为 meters。

#### 依赖关系

要启用此参数，请将 **接收阵列运动的来源** 参数设置为 `Property`。

**数据类型：** `double`

### **接收阵列的朝向** — 设置接收阵列轴的朝向 `eye(3,3)`（默认） | 实值 3×3 正交矩阵

接收阵列的朝向，指定为实值 3×3 正交矩阵。该矩阵指定定义阵列局部坐标系的三个轴相对于全局坐标系的方向。矩阵的列分别对应 *x*、*y* 和 *z* 轴。

#### 依赖关系

要启用此参数，请将 **接收阵列运动的来源** 参数设置为 `Property`。

**数据类型：** `double`

### **散射体设定** — 指定散射体参数的来源 `Auto`（默认） | `Property` | `Input port`

散射体参数的来源，指定为 `Auto`、`Property` 或 `Input port`。

- 当您将此参数设置为 `Auto` 时，所有散射体位置和系数都会随机生成。散射体速度为零。生成的位置包含在由 **散射体位置边界** 参数设置的区域内。使用 **散射体数量** 参数设置散射体数量。
- 当您将此属性设置为 `Property` 时，使用 **散射体位置 (m)** 参数设置散射体位置。使用 **散射系数** 参数设置散射系数。散射体速度为零。
- 当您将此参数设置为 `Input port` 时，使用模块的 `ScatPos`、`ScatVel` 和 `ScatCoef` 输入端口指定散射体位置、速度和散射系数。

**数据类型：** `char`

### **散射体数量** — 散射体数量 `1`（默认） | 非负整数

散射体的数量，指定为非负整数。

#### 依赖关系

要启用此属性，请将 **散射体设定** 参数设置为 `Auto`。

**数据类型：** `double`

### **散射体位置边界** — 将散射体位置约束在边界内 `[0,1000]`（默认） | 1×2 实值向量 | 3×2 实值矩阵

散射体位置边界，指定为 1×2 实值行向量或 3×2 实值矩阵。如果边界是 1×2 行向量，则该向量包含所有三个维度的最小值和最大值，`[minbdry maxbdry]`。如果边界是 3×2 矩阵，则该矩阵以 `[x_minbdry x_maxbdry;y_minbdry y_maxbdry; z_minbdry z_maxbdry]` 形式指定所有三个维度中的边界。

#### 依赖关系

要启用此属性，请将 **散射体设定** 参数设置为 `Auto`。

**数据类型：** `double`

### **散射体位置 (m)** — 散射体的位置 `[physconst('LightSpeed' )*5e-6;0;0]`（默认） | 实值 3×*Ns* 矩阵

散射体的位置，指定为实值 3×*Ns* 矩阵。*Ns* 是散射体的数量。每一列表示一个不同的散射体，并采用相对于全局坐标系的笛卡尔形式 `[x;y;z]`。单位为 meters。

#### 依赖关系

要启用此属性，请将 **散射体设定** 参数设置为 `Property`。

**数据类型：** `double`

### **ScattererCoefficient** — 散射系数 `1`（默认） | 复值 1×*Ns* 矩阵

散射系数，指定为复值 1×*Ns* 向量。*Ns* 是散射体的数量。单位无量纲。

#### 依赖关系

要启用此属性，请将 **散射体设定** 参数设置为 `Property`。

**数据类型：** `double`
**复数支持：** Yes

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

Scattering MIMO Channel 模块对三维多径传播信道进行建模，其中来自发射阵列的辐射信号经多个散射体反射后返回接收阵列。在此信道中，传播路径是从点到点的直接路径（视距）。该模块对距离相关时延、增益、多普勒频移、相位变化以及由气体、雨、雾和云引起的大气损耗进行建模。您可以选择让信号通过从发射机到接收机的直接路径传播。

大气气体和雨的衰减模型适用于频率范围 1–1000 GHz 的电磁信号，但雾和云的衰减模型仅适用于 10–1000 GHz。在这些频率范围之外，该对象使用最近的有效值。
