---
type: simulink-block
title: 'ePWM Type 0'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'epwmtype0'
documentation_source_path: 'ref/epwmtype0.html'
language: zh-CN
chinese_source: worker-translation
---

# ePWM Type 0

## 端口

R2025b 中未记录。

## 参数

### 定时器窗格

**Module**
:   指定要使用哪些目标 PWM 对：

    - `A` — 显示模块 A 中的 PWM
      （PWM1/PWM2、PWM3/PWM4 和 PWM5/PWM6）。
    - `B` — 显示模块 B 中的 PWM
      （PWM7/PWM8、PWM9/PWM10 和 PWM11/PWM12）。

      **注意**

      模块 A 中的 PWM 使用 Event Manager A、Timer 1，模块 B 中的 PWM 使用
      Event Manager B、Timer 3。

**Waveform period source**
:   获取波形周期值的来源。选择
    `Specify via dialog` 以在
    **Waveform period** 中输入该值，或选择 `Input
    port` 以使用来自输入端口的值。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Waveform period**
:   PWM 波形的周期，以 **Waveform period units** 中指定的时钟周期或秒为单位测量。

    **注意**

    *clock cycles* 术语指 F2812 芯片上的高速外设
    时钟。由于高速外设时钟预分频器设置为 2（150 MHz/2），此时钟默认是
    75 MHz。

**Waveform type (counting mode)**
:   PWM 对要生成的波形类型。F2812 PWM 可以生成
    两种类型的波形：`Asymmetric(Up)` 和
    `Symmetric(Up-down)`。下图显示了
    两种波形之间的差异。

**Waveform period units**
:   测量波形周期的单位。选项为 `Clock
    cycles`，指 F2812 芯片上的高速外设时钟
    （75 MHz），或 `Seconds`。更改这些单位会更改
    **Waveform period** 值和 **Duty
    cycle** 值以及 **Duty cycle units**
    选择。

**Timer prescaler**
:   对时钟输入进行分频，以产生所需的定时器计数速率。

### 输出窗格

**Enable PWM#/PWM#**
:   选中以激活 PWM 对。PWM1/PWM2 通过 Output 1 窗格激活，
    PWM3/PWM4 位于 Output 2，PWM5/PWM6 位于 Output 3。

**Duty cycle source**
:   选择 `Specify via dialog` 以使用对话框为这对 PWM 输出输入
    **Duty cycle** 值。选择
    `Input port` 以使用输入端口
    **W#** 为这对 PWM 输出输入 **Duty cycle** 值。

    输入端口 **W1** 对应 PWM1/PWM2。
    **W2** 对应 PWM3/PWM4。**W3**
    对应 PWM5/6。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Duty cycle**
:   设置 PWM 波形脉冲持续时间与 PWM **Waveform
    period** 的比率。

**Duty cycle units**
:   占空比的单位。有效选项为 `Clock
    cycles` 和 `Percentages`。更改这些
    单位会更改 **Duty cycle** 值，以及 **Waveform
    period** 值和 **Waveform period units** 选择。

    **注意**

    使用百分比可能会导致生成的
    代码中增加一些计算时间。这在您的应用中可能或可能不明显。

### 逻辑窗格

**Control logic source**
:   配置在 Outputs 选项卡上启用的所有 PWM 的控制逻辑。有效设置为 `Specify via dialog`
    （默认设置）或 `Input port`。

    `Specify via Dialog` 为每个 PWM 输出启用 **PWM control
    logic** 设置：

    - `Forced high` 使脉冲值
      为高。

      `Active high` 使脉冲值从低
      变为高。

      `Active low` 使脉冲值从高
      变为低。

      `Forced low` 使脉冲值
      为低。

    `Input port` 向 PWM 模块添加一个输入端口，用于
    设置 C2000 ACTRX 寄存器。每个 PWM 使用 2 位设置以下选项：

    - 00 Forced Low
    - 01 Active Low
    - 10 Active High
    - 11 Forced High

    模块 A 的 16 位 Compare Action Control Registers 的位 11–0 控制
    PWM1-6

    模块 B 的 16 位 Compare Action Control Registers 的位 11–0 控制
    PWM1-6

    例如：如果使用 PWM 模块 A 时在输入端口读取到十进制值 3222，
    则将采用以下 PWM 设置：

    3222 = 0C96h = 110010010110b

    因此：

    - PW1: Active High
    - PW2: Active Low
    - PW3: Active Low
    - PW4: Active High
    - PW5: Forced Low
    - PW6: Forced High

    更多信息，请参见 Texas Instruments™ 文档 “TMS320x281x DSP Event Manager
    (EV) Reference Guide”（文献编号 SPRU065）中关于 Compare Action Control Registers（ACTRA
    和 ACTRB）的部分。

### 死区窗格

**Use deadband for PWM#/PWM#**
:   在特定 PWM 对信号的开头启用无信号重叠的死区区域。下图显示了死区区域。

**Deadband prescaler**
:   时钟周期数，该数与 Deadband period 相乘后
    确定死区的大小。可选值为 1、2、4、8、16 和 32。

**Deadband period source**
:   获取死区周期的来源。选择 `Specify
    via dialog` 以在 **Deadband
    period** 字段中输入值，或选择 `Input port` 以使用
    来自输入端口的以时钟周期为单位的值。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Deadband period**
:   该值与 Deadband prescaler 相乘后确定死区的大小。
    可选值为 1 到 15。

### ADC 控制窗格

**ADC start event**
:   控制此 PWM 和与同一 EV 模块关联的 ADC 是否
    同步。选择 `None`
    以禁用同步，或选择一个事件来为关联的 ADC 生成源
    start-of-conversion (SOC) 信号。

    - `None` — ADC
      和 PWM 不同步。EV 不生成 SOC 信号，
      ADC 由软件触发（即，当 ADC
      模块在软件中执行时发生 A/D 转换）。
    - `Underflow interrupt` — 当板级
      通用 (GP) 定时器计数器达到十六进制值 FFFF 时，EV 为
      与同一 EV 模块关联的 ADC 生成 SOC 信号。
    - `Period interrupt` — 当 GP 定时器中的值
      与周期寄存器中的值匹配时，EV 为与同一 EV 模块关联的 ADC 生成
      SOC 信号。上面的 **Waveform
      period** 中设置的值决定寄存器中的值。

      **注意**

      如果选择 `Period interrupt` 并指定的
      采样时间小于指定的 **(Waveform
      period)/(Event timer clock speed)**，将发生零阶保持插值。
      （例如，如果输入 64000 作为波形周期，
      则定时器周期为 64000/75 MHz = 8.5333e-004。如果在
      C281x ADC 对话框框中输入的 **Sample time** 小于
      此结果，将导致零阶保持插值。）
    - `Compare interrupt` — 当 GP 定时器中的值
      与比较寄存器中的值匹配时，EV 为与同一 EV 模块关联的 ADC 生成
      SOC 信号。上面的
      **Duty cycle** 中设置的值决定寄存器中的
      值。

### 定时器窗格

**Module**
:   指定要使用哪些目标 PWM 对：

    - `A` — 显示模块 A 中的 PWM
      （PWM1/PWM2、PWM3/PWM4 和 PWM5/PWM6）。
    - `B` — 显示模块 B 中的 PWM
      （PWM7/PWM8、PWM9/PWM10 和 PWM11/PWM12）。

      **注意**

      模块 A 中的 PWM 使用 Event Manager A、Timer 1，模块 B 中的 PWM 使用
      Event Manager B、Timer 3。

**Waveform period source**
:   获取波形周期值的来源。选择
    `Specify via dialog` 以在
    **Waveform period** 中输入该值，或选择 `Input
    port` 以使用来自输入端口的值。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Waveform period**
:   PWM 波形的周期，以 **Waveform period units** 中指定的时钟周期或秒为单位测量。

    **注意**

    *clock cycles* 术语指 F2812 芯片上的高速外设
    时钟。由于高速外设时钟预分频器设置为 2（150 MHz/2），此时钟默认是
    75 MHz。

**Waveform type (counting mode)**
:   PWM 对要生成的波形类型。F2812 PWM 可以生成
    两种类型的波形：`Asymmetric(Up)` 和
    `Symmetric(Up-down)`。下图显示了
    两种波形之间的差异。

**Waveform period units**
:   测量波形周期的单位。选项为 `Clock
    cycles`，指 F2812 芯片上的高速外设时钟
    （75 MHz），或 `Seconds`。更改这些单位会更改
    **Waveform period** 值和 **Duty
    cycle** 值以及 **Duty cycle units**
    选择。

**Timer prescaler**
:   对时钟输入进行分频，以产生所需的定时器计数速率。

### 输出窗格

**Enable PWM#/PWM#**
:   选中以激活 PWM 对。PWM1/PWM2 通过 Output 1 窗格激活，
    PWM3/PWM4 位于 Output 2，PWM5/PWM6 位于 Output 3。

**Duty cycle source**
:   选择 `Specify via dialog` 以使用对话框为这对 PWM 输出输入
    **Duty cycle** 值。选择
    `Input port` 以使用输入端口
    **W#** 为这对 PWM 输出输入 **Duty cycle** 值。

    输入端口 **W1** 对应 PWM1/PWM2。
    **W2** 对应 PWM3/PWM4。**W3**
    对应 PWM5/6。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Duty cycle**
:   设置 PWM 波形脉冲持续时间与 PWM **Waveform
    period** 的比率。

**Duty cycle units**
:   占空比的单位。有效选项为 `Clock
    cycles` 和 `Percentages`。更改这些
    单位会更改 **Duty cycle** 值，以及 **Waveform
    period** 值和 **Waveform period units** 选择。

    **注意**

    使用百分比可能会导致生成的
    代码中增加一些计算时间。这在您的应用中可能或可能不明显。

### 逻辑窗格

**Control logic source**
:   配置在 Outputs 选项卡上启用的所有 PWM 的控制逻辑。有效设置为 `Specify via dialog`
    （默认设置）或 `Input port`。

    `Specify via Dialog` 为每个 PWM 输出启用 **PWM control
    logic** 设置：

    - `Forced high` 使脉冲值
      为高。

      `Active high` 使脉冲值从低
      变为高。

      `Active low` 使脉冲值从高
      变为低。

      `Forced low` 使脉冲值
      为低。

    `Input port` 向 PWM 模块添加一个输入端口，用于
    设置 C2000 ACTRX 寄存器。每个 PWM 使用 2 位设置以下选项：

    - 00 Forced Low
    - 01 Active Low
    - 10 Active High
    - 11 Forced High

    模块 A 的 16 位 Compare Action Control Registers 的位 11–0 控制
    PWM1-6

    模块 B 的 16 位 Compare Action Control Registers 的位 11–0 控制
    PWM1-6

    例如：如果使用 PWM 模块 A 时在输入端口读取到十进制值 3222，
    则将采用以下 PWM 设置：

    3222 = 0C96h = 110010010110b

    因此：

    - PW1: Active High
    - PW2: Active Low
    - PW3: Active Low
    - PW4: Active High
    - PW5: Forced Low
    - PW6: Forced High

    更多信息，请参见 Texas Instruments™ 文档 “TMS320x281x DSP Event Manager
    (EV) Reference Guide”（文献编号 SPRU065）中关于 Compare Action Control Registers（ACTRA
    和 ACTRB）的部分。

### 死区窗格

**Use deadband for PWM#/PWM#**
:   在特定 PWM 对信号的开头启用无信号重叠的死区区域。下图显示了死区区域。

**Deadband prescaler**
:   时钟周期数，该数与 Deadband period 相乘后
    确定死区的大小。可选值为 1、2、4、8、16 和 32。

**Deadband period source**
:   获取死区周期的来源。选择 `Specify
    via dialog` 以在 **Deadband
    period** 字段中输入值，或选择 `Input port` 以使用
    来自输入端口的以时钟周期为单位的值。

    **注意**

    所有 C281x PWM 模块的输入必须是
    标量值。

**Deadband period**
:   该值与 Deadband prescaler 相乘后确定死区的大小。
    可选值为 1 到 15。

### ADC 控制窗格

**ADC start event**
:   控制此 PWM 和与同一 EV 模块关联的 ADC 是否
    同步。选择 `None`
    以禁用同步，或选择一个事件来为关联的 ADC 生成源
    start-of-conversion (SOC) 信号。

    - `None` — ADC
      和 PWM 不同步。EV 不生成 SOC 信号，
      ADC 由软件触发（即，当 ADC
      模块在软件中执行时发生 A/D 转换）。
    - `Underflow interrupt` — 当板级
      通用 (GP) 定时器计数器达到十六进制值 FFFF 时，EV 为
      与同一 EV 模块关联的 ADC 生成 SOC 信号。
    - `Period interrupt` — 当 GP 定时器中的值
      与周期寄存器中的值匹配时，EV 为与同一 EV 模块关联的 ADC 生成
      SOC 信号。上面的 **Waveform
      period** 中设置的值决定寄存器中的值。

      **注意**

      如果选择 `Period interrupt` 并指定的
      采样时间小于指定的 **(Waveform
      period)/(Event timer clock speed)**，将发生零阶保持插值。
      （例如，如果输入 64000 作为波形周期，
      则定时器周期为 64000/75 MHz = 8.5333e-004。如果在
      C281x ADC 对话框框中输入的 **Sample time** 小于
      此结果，将导致零阶保持插值。）
    - `Compare interrupt` — 当 GP 定时器中的值
      与比较寄存器中的值匹配时，EV 为与同一 EV 模块关联的 ADC 生成
      SOC 信号。上面的
      **Duty cycle** 中设置的值决定寄存器中的
      值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

脉宽调制器 (PWM)

# ePWM Type 0

脉宽调制器 (PWM)

F2812 DSP 包含一套用于生成各种信号的脉宽调制器 (PWM)。此模块提供选项来设置 A 或 B 模块 Event Managers，以生成您所需的波形。十二个 PWM 配置为六对，每个模块中有三对。

C281x PWM 模块与其他 C281 模块共享 GP Timers。有关共享定时器的更多信息和指导，请参阅 Sharing General Purpose Timers Between C281x Peripherals。

**注意**

所有 C281x PWM 模块的输入必须是标量值。

- C281x PWM block
