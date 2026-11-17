---
type: simulink-block
title: 'IM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'imcontroller'
documentation_source_path: 'ref/imcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# IM Controller

## 端口
```yaml
ports:
- name: SpdReq
  summary: 转子机械转速指令 scalar
  direction: input
- name: TrqCmd
  summary: 转矩指令 scalar
  direction: input
- name: BusVolt
  summary: 直流母线电压 scalar
  direction: input
- name: PhaseCurrA
  summary: 电流 scalar
  direction: input
- name: PhaseCurrB
  summary: 电流 scalar
  direction: input
- name: SpdFdbk
  summary: 转子机械转速 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: BusCurr
  summary: 母线电流 scalar
  direction: output
- name: PhaseVolt
  summary: 定子端电压 array
  direction: output
```

### 输入

### **SpdReq** — 转子机械转速指令 `scalar`

转子机械转速指令，
*ω\*m*，单位为 rad/s。

#### 依赖

要创建此端口，请将 **Control Type** 参数设置为 `Speed
Control`。

### **TrqCmd** — 转矩指令 `scalar`

转矩指令，*T\**，单位为 N·m。

#### 依赖

要创建此端口，请将 **Control Type** 参数设置为 `Torque
Control`。

### **BusVolt** — 直流母线电压 `scalar`

直流母线电压 *vbus*，单位为
V。

### **PhaseCurrA** — 电流 `scalar`

定子电流 a 相，*ia*，
单位为 A。

### **PhaseCurrB** — 电流 `scalar`

定子电流 b 相，*ib*，
单位为 A。

### **SpdFdbk** — 转子机械转速 `scalar`

转子机械转速，*ωm*，
单位为 rad/s。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算结果的总线信号。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `SrcPwr` | 源功率 | W |
| `LdPwr` | 负载功率 | W |
| `PwrLoss` | 功率损耗 | W |
| `MtrTrqEst` | 估计的电机转矩 | N·m |

### **BusCurr** — 母线电流 `scalar`

估计的直流母线电流，
*ibus*，单位为 A。

### **PhaseVolt** — 定子端电压 `array`

定子端电压，
*Va*、
*Vb* 和
*Vc*，单位为 V。
## 参数
```yaml
parameters:
- name: Control Type
  summary: 选择控制方式 Speed Control（默认）| Torque Control
  group: ''
  block_parameter: control_type
  values: Speed Control（默认）| Torque Control
- name: Stator resistance, Rs
  summary: 电阻 1.77（默认）| scalar
  group: ''
  block_parameter: Rs
  values: 1.77（默认）| scalar
- name: Stator leakage inductance, Lls
  summary: 电感 0.0139（默认）| scalar
  group: ''
  block_parameter: Lls
  values: 0.0139（默认）| scalar
- name: Rotor resistance, Rr
  summary: 电阻 1.34（默认）| scalar
  group: ''
  block_parameter: Rr
  values: 1.34（默认） | scalar
- name: 转子漏电感，Llr
  summary: 电感 0.0121（默认） | scalar
  group: ''
  block_parameter: Llr
  values: 0.0121（默认） | scalar
- name: 转子励磁电感，Lm
  summary: 电感 0.3687（默认） | scalar
  group: ''
  block_parameter: Lm
  values: 0.3687（默认） | scalar
- name: 极对数，PolePairs
  summary: 极数 2（默认） | scalar
  group: ''
  block_parameter: PolePairs
  values: 2（默认） | scalar
- name: 物理惯量、粘性阻尼、静摩擦，Mechanical
  summary: 电机机械特性 [0.025, 0, 0]（默认） | vector
  group: ''
  block_parameter: Mechanical
  values: '[0.025, 0, 0]（默认） | vector'
- name: Rated synchronous speed, Frate
  summary: 电机频率 60（默认）| scalar
  group: ''
  block_parameter: Frate
  values: 60（默认）| scalar
- name: Rated line to line voltage RMS, Vrate
  summary: 电机电压 460（默认）| scalar
  group: ''
  block_parameter: Vrate
  values: 460（默认）| scalar
- name: Rated slip, Srate
  summary: 电机转差速度 0.0172（默认）| scalar
  group: ''
  block_parameter: Srate
  values: 0.0172（默认）| scalar
- name: Calculate Rated Stator Flux Current
  summary: 推导参数按钮
  group: ''
- name: D-axis rated current, Isd_0
  summary: 推导值 3.1004（默认）| scalar
  group: ''
  block_parameter: Isd_0
  values: 3.1004（默认） | scalar
- name: Q-axis rated current, Isq_0
  summary: 派生 5.7131（默认） | scalar
  group: ''
  block_parameter: Isq_0
  values: 5.7131（默认） | scalar
- name: Torque at rated current, Tem
  summary: 派生 12.6467（默认） | scalar
  group: ''
  block_parameter: Tem
  values: 12.6467（默认） | scalar
- name: Bandwidth of the current regulator, EV_current
  summary: 带宽 200（默认） | scalar
  group: ''
  block_parameter: EV_current
  values: 200（默认） | scalar
- name: Sample time for the torque control, Tst
  summary: 时间 5e-5（默认）| scalar
  group: ''
  block_parameter: Tst
  values: 5e-5（默认）| scalar
- name: Calculate Current Regulator Gains
  summary: 推导参数按钮
  group: ''
- name: D and Q axis proportional gain, Kp
  summary: 推导 32.1894（默认）| scalar
  group: ''
  block_parameter: Kp
  values: 32.1894（默认）| scalar
- name: D and Q axis integral gain, Ki
  summary: 推导 2224.2476（默认）| scalar
  group: ''
  block_parameter: Ki
  values: 2224.2476（默认）| scalar
- name: Bandwidth of the motion controller, EV_motion
  summary: 带宽 [20, 4, 0.8]（默认）| vector
  group: ''
  block_parameter: EV_motion
  values: '[20, 4, 0.8]（默认）| vector'
- name: Bandwidth of the state filter, EV_sf
  summary: 带宽 200（默认）| scalar
  group: ''
  block_parameter: EV_sf
  values: 200（默认）| scalar
- name: Calculate Speed Regulator Gains
  summary: 派生参数按钮
  group: ''
- name: Proportional gain, ba
  summary: 派生 3.7477（默认）| scalar
  group: ''
  block_parameter: ba
  values: 3.7477（默认）| scalar
- name: Angular gain, Ksa
  summary: 派生 94.0877（默认）| scalar
  group: ''
  block_parameter: Ksa
  values: 94.0877（默认）| scalar
- name: Rotational gain, Kisa
  summary: 派生 381.7822（默认）| scalar
  group: ''
  block_parameter: Kisa
  values: 381.7822（默认）| scalar
- name: Speed regulation time constant, Ksf
  summary: 派生 1217.9727（默认）| scalar
  group: ''
  block_parameter: Ksf
  values: 1217.9727（默认） | scalar
- name: 惯性补偿，Jcomp
  summary: 派生 0.025（默认） | scalar
  group: ''
  block_parameter: Jcomp
  values: 0.025（默认） | scalar
- name: 粘性阻尼补偿，Fv
  summary: 派生 0（默认） | scalar
  group: ''
  block_parameter: Fv
  values: 0（默认） | scalar
- name: 静摩擦，Fs
  summary: 派生 0（默认） | scalar
  group: ''
  block_parameter: Fs
  values: 0（默认） | scalar
- name: Parameterize losses by
  summary: 选择类型 Single efficiency measurement（默认）| Tabulated loss data | Tabulated efficiency data
  group: ''
  block_parameter: param_loss
  values: Single efficiency measurement（默认）| Tabulated loss data | Tabulated efficiency data
- name: Overall inverter efficiency, eff
  summary: 常量 98（默认）| scalar
  group: ''
  block_parameter: eff
  values: 98（默认）| scalar
- name: Vector of speeds (w) for tabulated loss, w_loss_bp
  summary: 断点 [0 200 400 600 800 1000]（默认）| 1×M 向量
  group: ''
  block_parameter: w_loss_bp
  values: '[0 200 400 600 800 1000]（默认）| 1×M 向量'
- name: Vector of torques (T) for tabulated loss, T_loss_bp
  summary: 断点 [0 25 50 75 100]（默认）| 1×N 向量
  group: ''
  block_parameter: T_loss_bp
  values: '[0 25 50 75 100]（默认）| 1×N 向量'
- name: Corresponding losses, losses_table
  summary: 表 [100 100 100 100 100;100 150 200 250 300;100 200 300 400 500;100 250 400 550 700;100 300 500 700 900;100 350
    600 850 1100]（默认）| M×N 数组
  group: ''
  block_parameter: losses_table
  values: M×N 数组
- name: Vector of speeds (w) for tabulated efficiency, w_eff_bp
  summary: 断点 [200 400 600 800 1000]（默认）| 1×M 向量
  group: ''
  block_parameter: w_eff_bp
  values: '[200 400 600 800 1000]（默认）| 1×M 向量'
- name: Vector of torques (T) for tabulated efficiency, T_eff_bp
  summary: 断点 [25 50 75 100]（默认）| 1×N 向量
  group: ''
  block_parameter: T_eff_bp
  values: '[25 50 75 100]（默认）| 1×N 向量'
- name: Corresponding efficiency, efficiency_table
  summary: 表 [96.2 98.1 98.7 99;98.1 99 99.4 99.5;98.7 99.4 99.6 99.7;99 99.5 99.7 99.8;99.2 99.6 99.7 99.8]（默认）| M×N 数组
  group: ''
  block_parameter: efficiency_table
  values: M×N 数组
```

#### 模块选项

### **Control Type** — 选择控制方式 `Speed Control`（默认）| `Torque Control`

如果选择 `Torque Control`，该模块
不实现速度控制器。

下表总结了端口配置。

| 端口配置 | 创建的端口 |
| --- | --- |
| `Speed Control` | `SpdReq` |
| `Torque Control` | `TrqCmd` |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `control_type` |
| **值**：| `Speed Control`（默认）| `Torque Control` |
| **Data Types:** | `character vector` |

#### 电机

### **Stator resistance, Rs** — 电阻 `1.77`（默认）| `scalar`

定子相绕组电阻，
*Rs*，单位为欧姆。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **值**：| `1.77`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Stator resistance, Rs** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis integral gain, Ki** | **Current Controller** |

### **Stator leakage inductance, Lls** — 电感 `0.0139`（默认）| `scalar`

定子漏电感，*Lls*，
单位为 H。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Lls` |
| **值**：| `0.0139`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Stator leakage inductance, Lls** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |
| **D and Q axis proportional gain, Kp**  **D and Q axis integral gain, Ki** | **Current Controller** |

### **Rotor resistance, Rr** — 电阻 `1.34`（默认）| `scalar`

转子电阻，*Rr*，单位为
欧姆。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rr` |
| **值：** | `1.34`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转子电阻，Rr** | **D 轴额定电流，Isd\_0**  **Q 轴额定电流，Isq\_0**  **额定电流下的转矩，Tem** | **Id 和 Iq 计算** |

### **转子漏电感，Llr** — 电感 `0.0121`（默认） | `scalar`

转子漏电感，*Llr*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Llr` |
| **值：** | `0.0121`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转子漏电感，Llr** | **D 轴额定电流，Isd\_0**  **Q 轴额定电流，Isq\_0**  **额定电流下的转矩，Tem** | **Id 和 Iq 计算** |
| **D 和 Q 轴比例增益，Kp** | **电流控制器** |

### **转子励磁电感，Lm** — 电感 `0.3687`（默认） | `scalar`

转子励磁电感，*Lm*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lm` |
| **值：** | `0.3687`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转子漏电感，Llr** | **D 轴额定电流，Isd\_0**  **Q 轴额定电流，Isq\_0**  **额定电流下的转矩，Tem** | **Id 和 Iq 计算** |
| **D 和 Q 轴比例增益，Kp** | **电流控制器** |

### **极对数，PolePairs** — 极数 `2`（默认） | `scalar`

电机极对数，*P*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PolePairs` |
| **值：** | `2`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转子漏电感，Llr** | **额定电流下的转矩，Tem** | **Id 和 Iq 计算** |

### **物理惯量、粘性阻尼、静摩擦，Mechanical** — 电机机械特性 `[0.025, 0, 0]`（默认） | `vector`

电机的机械特性：

- 电机惯量，*F*v**，单位为 kgm^2
- 粘性摩擦转矩常数，*F*v**，单位为 N·m/(rad/s)
- 静摩擦转矩常数，*Fs*，单位为 N·m

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Mechanical` |
| **值：** | `[0.025, 0, 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数设置为 `Speed Control`。

对于增益计算，模块使用 **Motor Parameters** 选项卡上 **Physical inertia, viscous damping, static friction** 参数值中的惯量。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Physical inertia, viscous damping, static friction, Mechanical** | **Proportional gain, ba**  **Angular gain, Ksa**  **Rotational gain, Kisa**  **Inertia compensation, Jcomp**  **Viscous damping compensation, Fv**  **Static friction, Fs** | **Speed Controller** |

#### Id and Iq Calculation

### **Rated synchronous speed, Frate** — 电机频率 `60`（默认）| `scalar`

电机额定电气频率，*Frate*，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Frate` |
| **值：** | `60`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Rated synchronous speed, Frate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Rated line to line voltage RMS, Vrate** — 电机电压 `460`（默认）| `scalar`

电机额定线电压，*Vrate*，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vrate` |
| **值：** | `460`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Rated synchronous speed, Frate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Rated slip, Srate** — 电机转差速度 `0.0172`（默认）| `scalar`

电机额定转差速度，*Srate*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Srate` |
| **值：** | `0.0172`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Rated slip, Srate** | **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Id and Iq Calculation** |

### **Calculate Rated Stator Flux Current** — 推导参数按钮

点击以推导参数。

#### 依赖关系

在 **Id and Iq Calculation** 选项卡上，当您选择 **Calculate Rated Stator Flux Current** 时，模块会计算推导参数。下表总结了依赖于其他模块参数的推导参数。

| **Id and Iq Calculation** 选项卡上的推导参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D-axis rated current, Isd\_0** — 推导值 `3.1004`（默认）| `scalar`

推导的 d 轴额定电流，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Isd_0` |
| **值：** | `3.1004`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

在 **Id and Iq Calculation** 选项卡上，当您选择 **Calculate Rated Stator Flux Current** 时，模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Id and Iq Calculation** 选项卡上的派生参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **Q-axis rated current, Isq\_0** — 派生 `5.7131`（默认） | `scalar`

派生的 q 轴额定电流，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Isq_0` |
| **值：** | `5.7131`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

在 **Id and Iq Calculation** 选项卡上，当您选择 **Calculate Rated Stator Flux Current** 时，模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Id and Iq Calculation** 选项卡上的派生参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **Torque at rated current, Tem** — 派生 `12.6467`（默认） | `scalar`

额定电流下的转矩，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tem` |
| **值：** | `12.6467`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

在 **Id and Iq Calculation** 选项卡上，当您选择 **Calculate Rated Stator Flux Current** 时，模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Id and Iq Calculation** 选项卡上的派生参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D-axis rated current, Isd\_0**  **Q-axis rated current, Isq\_0**  **Torque at rated current, Tem** | **Rated synchronous speed, Frate**  **Rated line to line voltage RMS, Vrate**  **Rated slip, Srate** | **Id and Iq Calculation** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

#### 电流控制器

### **Bandwidth of the current regulator, EV\_current** — 带宽 `200`（默认） | `scalar`

电流调节器带宽，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_current` |
| **值：** | `200`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

此表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **电流调节器的带宽，EV\_current** | **D 轴和 Q 轴积分增益，Ki**  **D 轴和 Q 轴比例增益，Kp** | **电流控制器** |

### **Sample time for the torque control, Tst** — 时间 `5e-5`（默认）| `scalar`

转矩控制采样时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tst` |
| **值：** | `5e-5`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

此表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转矩控制的采样时间，Tst** | **速度调节时间常数，Ksf** | **速度控制器** |

### **Calculate Current Regulator Gains** — 推导参数按钮

点击以推导参数。

#### 依赖关系

在 **Current Controller** 选项卡上，当您
选择 **Calculate Current Regulator Gains** 时，
模块会计算推导参数。该表汇总了依赖于其他模块参数的
推导参数。

| **Current Controller** 选项卡上的推导参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴和 Q 轴比例增益，Kp**  **D 轴和 Q 轴积分增益，Ki** | **电流调节器的带宽，EV\_current** | **电流控制器** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D and Q axis proportional gain, Kp** — 推导 `32.1894`（默认）| `scalar`

推导的比例增益，单位为 V/A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp` |
| **值：** | `32.1894`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

在 **Current Controller** 选项卡上，当您
选择 **Calculate Current Regulator Gains** 时，
模块会计算推导参数。该表汇总了依赖于其他模块参数的
推导参数。

| **Current Controller** 选项卡上的推导参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴和 Q 轴比例增益，Kp**  **D 轴和 Q 轴积分增益，Ki** | **电流调节器的带宽，EV\_current** | **电流控制器** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

### **D and Q axis integral gain, Ki** — 推导 `2224.2476`（默认）| `scalar`

推导的积分增益，单位为 V/A\*s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki` |
| **值：** | `2224.2476`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

在 **Current Controller** 选项卡上，当您选择 **Calculate Current Regulator Gains** 时，该模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Current Controller** 选项卡上的派生参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴和 Q 轴比例增益，Kp**  **D 轴和 Q 轴积分增益，Ki** | **电流调节器的带宽，EV\_current** | **电流控制器** |
| **Stator resistance, Rs**  **Stator leakage inductance, Lls**  **Rotor resistance, Rr**  **Rotor leakage inductance, Llr**  **Rotor magnetizing inductance, Lm** | **Motor Parameters** |

#### 速度控制器

### **Bandwidth of the motion controller, EV\_motion** — 带宽 `[20, 4, 0.8]`（默认）| `vector`

运动控制器带宽，单位为 Hz。将向量的第一个元素设置为所需的截止频率。将向量的第二个和第三个元素设置为更高阶的截止频率。您可以将下一个元素的值设置为前一个元素值的 `1/5`。例如，如果所需截止频率为 `20` Hz，请指定 `[20 4 0.8]`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_motion` |
| **值：** | `[20, 4, 0.8]`（默认）| `vector` |
| **数据类型：** | `double` |

#### 依赖关系

当 **Control Type** 参数设置为 `Speed Control` 时，该参数启用。

| 参数 | 用于派生 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Bandwidth of the motion controller, EV\_motion** | **Proportional gain, ba**  **Angular gain, Ksa**  **Rotational gain, Kisa** | **Speed Controller** |

### **Bandwidth of the state filter, EV\_sf** — 带宽 `200`（默认）| `scalar`

状态滤波器带宽，单位为 Hz。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_sf` |
| **值：** | `200`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

当 **Control Type** 参数设置为 `Speed Control` 时，该参数启用。

| 参数 | 用于派生 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Bandwidth of the state filter, EV\_sf** | **Speed regulation time constant, Ksf** | **Speed Controller** |

### **Calculate Speed Regulator Gains** — 派生参数按钮

点击以派生参数。

#### 依赖关系

在 **Speed Controller** 选项卡上，当您选择 **Calculate Speed Regulator Gains** 时，模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Speed Controller** 选项卡上的派生参数 | | 依赖于 | |
| --- | --- | --- | --- |
| 参数 | 选项卡 |
| **Proportional gain, ba** | ba=Jp−Jpp1p2p3Tsm | **Bandwidth of the motion controller, EV\_motion**  **Bandwidth of the state filter, EV\_sf** | **Speed Controller** |
| **角度增益，Ksa** | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 | **转矩控制的采样时间，Tst** | **电流控制器** |
| **Rotational gain, Kisa** | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Speed regulation time constant, Ksf** | Ksf=1−exp(−Tsm2πEVsf)Tsm |
| **Inertia compensation, Jcomp** | *Jcomp* = *Jp* | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Viscous damping compensation, Fv** | *F*v** |
| **Static friction, Fs** | *Fs* |

公式使用以下变量。

|  |  |
| --- | --- |
| *P* | 电机极对数 |
| *ba* | 速度调节器比例增益 |
| *Ksa* | 速度调节器积分增益 |
| *Kisa* | 速度调节器双积分增益 |
| *Ksf* | 速度调节器时间常数 |
| *Jp* | 电机惯量 |
| *EVsf* | 状态滤波器带宽 |
| *EVmotion* | 运动控制器带宽 |

### **Proportional gain, ba** — 派生 `3.7477`（默认）| `scalar`

派生的比例增益，单位为 N·m/(rad/s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ba` |
| **值：** | `3.7477`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Proportional gain, ba** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Angular gain, Ksa** — 派生 `94.0877`（默认）| `scalar`

派生的角增益，单位为 N·m/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ksa` |
| **值：** | `94.0877`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Angular gain, Ksa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Rotational gain, Kisa** — 派生 `381.7822`（默认）| `scalar`

派生的旋转增益，单位为 N·m/(rad\*s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kisa` |
| **值：** | `381.7822`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Rotational gain, Kisa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Speed regulation time constant, Ksf** — 派生 `1217.9727`（默认）| `scalar`

派生的速度调节时间常数，单位为 1/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ksf` |
| **值：** | `1217.9727`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **速度调节时间常数，Ksf** | **转矩控制的采样时间，Tst** | **电流控制器** |
| **状态滤波器带宽，EV\_sf** | **速度控制器** |

### **惯性补偿，Jcomp** — 派生 `0.025`（默认） | `scalar`

派生的惯性补偿，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jcomp` |
| **值：** | `0.025`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **惯性补偿，Jcomp** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

### **粘性阻尼补偿，Fv** — 派生 `0`（默认） | `scalar`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fv` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **粘性阻尼补偿，Fv** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

### **静摩擦，Fs** — 派生 `0`（默认） | `scalar`

派生的静摩擦，单位为 N·m/(rad/s)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fs` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **静摩擦，Fs** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

#### 电气损耗

### **Parameterize losses by** — 选择类型 `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 根据电机转速和负载转矩的函数关系计算电气损耗。 |
| `Tabulated efficiency data` | 使用作为电机转速和负载转矩函数的逆变器效率计算电气损耗。    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要为低转速和低转矩提供表格化数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速和转矩幅值，不进行损耗值外推。 |

最佳实践是使用 `Tabulated loss data` 而非 `Tabulated efficiency data`：

- 效率在零转速或零转矩时变得不确定。
- 您可以考虑在零转速或零转矩时仍然存在的固定损耗。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **值**：| `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data` |
| **Data Types:** | `character vector` |

### **Overall inverter efficiency, eff** — 常量 `98`（默认）| `scalar`

整体逆变器效率 *Eff*，以 % 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **值**：| `98`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Vector of speeds (w) for tabulated loss, w\_loss\_bp** — 断点 `[0 200 400 600 800 1000]`（默认）| `1`×`M` 向量

计算损耗时查找表的转速断点，以 rad/s 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `w_loss_bp` |
| **值**：| `[0 200 400 600 800 1000]`（默认）| `1`×`M` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Vector of torques (T) for tabulated loss, T\_loss\_bp** — 断点 `[0 25 50 75 100]`（默认）| `1`×`N` 向量

计算损耗时查找表的转矩断点，以 N·m 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `T_loss_bp` |
| **值**：| `[0 25 50 75 100]`（默认）| `1`×`N` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Corresponding losses, losses\_table** — 表 `[100 100 100 100 100;100 150 200 250 300;100 200 300 400 500;100 250 400 550 700;100 300 500 700 900;100 350 600 850 1100]`（默认）| `M`×`N` 数组

作为 `M` 个转速和 `N` 个转矩函数的电气损耗值数组，单位为 W。每个值指定特定转速和转矩组合下的损耗。矩阵大小必须与转速和转矩向量定义的维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `M`×`N` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated loss data`。

### **Vector of speeds (w) for tabulated efficiency, w\_eff\_bp** — 断点 `[200 400 600 800 1000]`（默认）| `1`×`M` 向量

计算效率时查找表的转速断点，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[200 400 600 800 1000]`（默认）| `1`×`M` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。

### **Vector of torques (T) for tabulated efficiency, T\_eff\_bp** — 断点 `[25 50 75 100]`（默认）| `1`×`N` 向量

计算效率时查找表的转矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[25 50 75 100]`（默认）| `1`×`N` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。

### **Corresponding efficiency, efficiency\_table** — 表 `[96.2 98.1 98.7 99;98.1 99 99.4 99.5;98.7 99.4 99.6 99.7;99 99.5 99.7 99.8;99.2 99.6 99.7 99.8]`（默认）| `M`×`N` 数组

作为 `M` 个转速和 `N` 个转矩函数的效率数组，单位为 %。每个值指定特定转速和转矩组合下的效率。矩阵大小必须与转速和转矩向量定义的维度匹配。

模块忽略零转速或零转矩时的效率值。当转矩或转速为零时，损耗为零。模块使用线性插值。

为了在低功率条件下获得所需的精度水平，您可以为低转速和低转矩提供表格数据。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `M`×`N` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。
## 所属库

Powertrain Blockset / Propulsion / Electric Motor Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

用于感应电机的基于内部转矩的磁场定向控制器，带有可选的外环速度控制器

IM Controller 模块为感应电机（IM）实现了一个基于内部转矩的磁场定向控制器，并带有可选的外环速度控制器。转矩控制实现了一种控制电机磁通的策略。您可以指定速度控制或转矩控制。

IM Controller 实现了速度控制、转矩确定、调节器、变换和电机的方程。

该图展示了模块中的信息流。

该模块实现的方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 转子速度 |
| *ω\** | 转子速度指令 |
| *T\** | 转矩指令 |
| *id*  *i\*d* | d 轴电流  d 轴电流指令 |
| *iq*  *i\*q* | q 轴电流  q 轴电流指令 |
| *vd*,  *v\*d* | d 轴电压  d 轴电压指令 |
| *vq*  *v\*q* | q 轴电压  q 轴电压指令 |
| *va*, *vb*, *vc* | 定子 a、b、c 相电压 |
| *ia*, *ib*, *ic* | 定子 a、b、c 相电流 |

### Speed Controller

要实现速度控制器，请选择 **Control Type** 参数 `Speed Control`。如果选择 **Control Type** 参数 `Torque Control`，则该模块不实现速度控制器。

速度控制器通过实现状态滤波器，并计算前馈和反馈指令来确定转矩指令。如果不实现速度控制器，则向 IM Controller 模块输入转矩指令。

**状态滤波器**

状态滤波器是一种低通滤波器，它根据速度指令生成加速度指令。在 **Speed Controller** 选项卡上：

- 若要使速度指令滞后时间可忽略不计，请指定 **Bandwidth of the state filter** 参数。
- 若要基于状态滤波器带宽计算 **Speed regulation time constant, Ksf** 增益，请选择 **Calculate Speed Regulator Gains**。

特征方程的离散形式为：

z+KsfTsm−1

该滤波器使用此方程计算增益。

Ksf=1−exp(−Tsm2πEVsf)Tsm

该方程使用以下变量。

|  |  |
| --- | --- |
| *EVsf* | 速度指令滤波器的带宽 |
| *Tsm* | 运动控制器采样时间 |
| *Ksf* | 速度调节器时间常数 |

**状态反馈**

为了生成状态反馈转矩，该模块使用来自状态滤波器的滤波后速度误差信号。反馈转矩计算还需要速度调节器的增益。

在 **Speed Controller** 选项卡上，选择 **Calculate Speed Regulator Gains** 以计算：

- **Proportional gain, ba**
- **Angular gain, Ksa**
- **Rotational gain, Kisa**

对于增益计算，该模块使用 **Motor Parameter** 选项卡上 **Physical inertia, viscous damping, static friction** 参数值中的惯量。

状态反馈的增益使用以下方程计算。

| 计算 | 方程 |
| --- | --- |
| 特征方程的离散形式 | z3+(−3Jp+Tsba+ Ts2Ksa+Ts3Kisa)Jpz2+(3Jp− 2Tsba− Ts2Ksa)Jpz+−Jp+TsbaJp  (z−p1)(z−p2)(z−p3)=z3+(p1+p2+p3)z2+(p1p2+p2p3+p13)z2−p1p2p3 |
| 速度调节器比例增益 | ba=Jp−Jpp1p2p3Tsm |
| 速度调节器积分增益 | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 |
| 速度调节器双积分增益 | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *P* | 电机极对数 |
| *ba* | 速度调节器比例增益 |
| *Ksa* | 速度调节器积分增益 |
| *Kisa* | 速度调节器双积分增益 |
| *Jp* | 电机惯量 |
| *Tsm* | 运动控制器采样时间 |

**指令前馈**

为了生成状态前馈转矩，该模块使用来自状态滤波器的滤波后速度和加速度。此外，前馈转矩计算使用惯量、粘性阻尼和静摩擦。为了实现零跟踪误差，转矩指令是前馈和反馈转矩指令之和。

在 **Speed Controller** 选项卡上选择 **Calculate Speed Regulator Gains** 会使用 **Motor Parameter** 选项卡上的 **Physical inertia, viscous damping, static friction** 参数值更新惯量、粘性阻尼和静摩擦。

前馈转矩指令使用此方程。

Tcmd\_ff= Jpω˙m+Fvωm+Fs ωm|ωm|

该方程使用以下变量。

|  |  |
| --- | --- |
| *Jp* | 电机惯量 |
| *Tcmd\_ff* | 转矩指令前馈 |
| *Fs* | 静摩擦转矩常数 |
| *F*v** | 粘性摩擦转矩常数 |
| *Fs* | 静摩擦转矩常数 |
| *ωm* | 转子机械速度 |

### Torque Determination

该模块使用交轴电流来确定基速和电流指令。电机额定值决定额定电气速度。

| Calculation | Equations |
| --- | --- |
| Current commands | iqref=Tcmdisq\_0⋅P⋅(L2mLr)  ``` If |ωe|≤ωrated 		idref= isd_0	 Else 		idref= isd_0⋅ωrated|ωe| End ``` |
| Inductance | Lr=Llr+LmLs=Lls+Lm |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *idref* | d 轴参考电流 |
| *iqref* | q 轴参考电流 |
| *isd\_0* | d 轴额定电流 |
| *isq\_0* | q 轴额定电流 |
| *ωe* | 转子电气速度 |
| *ωrated* | 额定电气速度 |
| *Llr* | 转子漏电感 |
| *Lr* | 转子绕组电感 |
| *Lls* | 定子漏电感 |
| *Ls* | 定子绕组电感 |
| *Lm* | 电机励磁电感 |
| *P* | 电机极对数 |
| *Tcmd* | 指令电机最大转矩 |

### Current Regulators

该模块通过抗积分饱和功能调节电流。经典比例积分（PI）电流调节器不考虑 d 轴和 q 轴耦合或反电动势（EMF）耦合。因此，瞬态性能会变差。为考虑耦合，该模块以转子参考坐标系的标量形式实现复矢量电流调节器（CVCR）。CVCR 解耦：

- d 轴和 q 轴电流交叉耦合
- 反电动势交叉耦合

电流频率响应是一阶系统，带宽为 *EVcurrent*。

该模块实现以下方程。

| Calculation | Equations |
| --- | --- |
| Motor voltage, in the stator reference frame | σ=1−L2mLsLrvsd=Rsisd+σLsdisddt+LmLrdλrddt−PωmσLsisqvsq=Rsisq+σLsdisqdt+ωdLmLrdλrddt+PωmσLsisd |
| Current regulator gains | ωb=2πEVcurrentKp=σLdωbKi=Rsωb |
| Transfer functions | ididref= ωbs+ωbiqiqref= ωbs+ωb |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EVcurrent* | 电流调节器带宽 |
| *id* | d 轴电流 |
| *iq* | q 轴电流 |
| *isq* | 定子 q 轴电流 |
| *isd* | 定子 d 轴电流 |
| *vsd* | 定子 d 轴电压 |
| *vsq* | 定子 q 轴电压 |
| *Kp* | 电流调节器 d 轴增益 |
| *Ki* | 电流调节器积分增益 |
| *Ls* | 定子绕组电感 |
| *Lm* | 电机励磁电感 |
| *Lr* | 转子绕组电感 |
| *Rs* | 定子相绕组电阻 |
| *λrd* | 转子 d 轴磁通 |
| *σ* | 漏磁系数 |
| *p* | 电机极对数 |

### Transforms

为计算平衡三相（*a*、*b*）量、正交两相（*α*、*β*）量和旋转（*d*、*q*）参考坐标系中的电压和电流，该模块使用 Clarke 和 Park 变换。

在变换方程中。

ωe=Pωmdθedt= ωe

| Transform | Description | Equations |
| --- | --- | --- |
| Clarke | 将平衡三相信号（*a*、*b*）转换为平衡两相正交信号（*α*、*β*）。 | xα= 23xa− 13xb −13xcxβ= 32xb− 32xc |
| Park | 将平衡两相正交静止信号（*α*、*β*）转换为正交旋转参考坐标系（*d*、*q*）。 | xd= xαcosθe+ xβsinθexq= −xαsinθe+ xβcosθe |
| Inverse Clarke | 将平衡两相正交信号（*α*、*β*）转换为平衡三相信号（*a*、*b*）。 | xa= xaxb= −12xα+ 32xβxc= −12xα− 32xβ |
| Inverse Park | 将正交旋转参考坐标系（*d*、*q*）转换为平衡两相正交静止信号（*α*、*β*）。 | xα= xdcosθe− xqsinθexβ= xdsinθe+ xqcosθe |

这些变换使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子机械速度 |
| *P* | 电机极对数 |
| *ωe* | 转子电气速度 |
| *Θe* | 转子电角度 |
| *x* | 相电流或电压 |

### Motor

该模块使用相电流和相电压来估算直流母线电流。正电流表示电池放电。负电流表示电池充电。该模块使用以下方程。

|  |  |
| --- | --- |
| 负载功率 | LdPwr=va ia+ vb ib+ vc ic |
| 源功率 | SrcPwr= LdPwr+PwrLoss |
| 直流母线电流 | ibus= SrcPwrvbus |
| 估算的转子转矩 | MtrTrqest=PλrdisqLmLr |
| 单一效率源到负载的功率损耗 | PwrLoss=100−EffEff⋅LdPwr |
| 单一效率负载到源的功率损耗 | PwrLoss=100−Eff100⋅|LdPwr| |
| 表格化效率的功率损耗 | PwrLoss= f(ωm,MtrTrqest) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *va*、*vb*、*vc* | 定子 a、b、c 相电压 |
| *vbus* | 估算的直流母线电压 |
| *ia*、*ib*、*ic* | 定子 a、b、c 相电流 |
| *ibus* | 估算的直流母线电流 |
| *Eff* | 逆变器总效率 |
| *ωm* | 转子机械转速 |
| *Lr* | 转子绕组电感 |
| *Lm* | 电机励磁电感 |
| *λrd* | 转子 d 轴磁通 |
| *isq* | q 轴电流 |
| *P* | 电机极对数 |

### Electrical Losses

要指定电气损耗，请在 **Electrical Losses** 选项卡中，对于 **Parameterize losses by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 根据电机转速和负载转矩的函数计算电气损耗。 |
| `Tabulated efficiency data` | 使用作为电机转速和负载转矩函数的逆变器效率计算电气损耗。    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，假定损耗为零。 - 使用线性插值确定损耗。根据需要提供低转速和低转矩的表格化数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速和转矩幅值，不外推损耗值。 |

作为最佳实践，请使用 `Tabulated loss data` 而不是 `Tabulated efficiency data`：

- 当转速或转矩为零时，效率变得定义不明确。
- 您可以考虑在转速或转矩为零时仍然存在的固定损耗。
