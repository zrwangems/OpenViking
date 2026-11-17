---
type: simulink-block
title: 'ePWM Type 1-4'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'epwmtype14'
documentation_source_path: 'ref/epwmtype14.html'
language: zh-CN
chinese_source: worker-translation
---

# ePWM Type 1-4

## 端口

R2025b 中未记录。

## 参数

### 常规

### **Allow use of 16 HRPWMs (for C28044) instead of 6 PWMs** — 当 PWM 分辨率过低时启用 HRPWM `off`（默认）| `on`

当 PWM 分辨率过低时，在 C28044 数字信号控制器上启用全部 16 个高分辨率 PWM 模块（HRPWM）。

**注意**

仅当您使用 C28044 处理器时才选择此参数。

例如，Spectrum Digital eZdsp™ F28044 板的系统时钟为 100 MHz（200 kHz 开关频率）。在这些频率下，传统 PWM 分辨率过低，约为 9 位或 10 位。相比之下，同一块板的 HRPWM 分辨率为 14.8 位。

#### 依赖关系

当您启用此参数时：

- 使用 ePWMA 选项卡下的 HRPWM 参数进行其他配置更改。
- ePWMB 选项卡下的大部分配置参数不可用。
- 您的模型最多可包含 16 个 C280x/C2803x/C2833x ePWM 模块，前提是您将每个模块配置为单独的模块。（例如，**Module** 为 `ePWM1`、`ePWM2` 等。）
- 仅当您使用 C28044 处理器时才选择此参数。要为其他处理器启用 HRPWM，请先查阅处理器的 Texas Instruments 文档以确定可用的 HRPWM 模块数量。然后使用 ePWMA 选项卡下的 HRPWM 参数来启用和配置 HRPWM。

### **Module** — 指示要使用的 ePWM 模块 `ePWM1`（默认）| `ePWM2` | `ePWM3` | `…`

选择适当的 ePWM 模块。`ePWMx`，其中 *x* 可以是 1、2、3……

**注意**

可用模块的数量因处理器而异。

### **ePWMLink TBPRD** — 指示 ePWM 模块的 TBPRD 链接 `Not Linked`（默认）| `ePWM2` | `ePWM3` | `…`

选择一个 ePWM 模块，将当前 ePWM 模块链接到该模块以共享定时器周期。当您链接两个模块时，被链接的 ePWM 模块中的定时器周期值将设置当前模块中 **Timer period** 参数的值。当您选择链接到另一个 ePWM 模块时，**Timer period units**、**Specify timer period via** 和 **Timer period** 参数不会显示。

但是，当您将一个 ePWM 模块链接到模型中不存在的模块时，链接不会生效。

**注意**

此参数仅适用于某些 TI C2000™ 处理器。

### **Timer period units** — 指示时间周期单位 `Clock cycles`（默认）| `Seconds`

以 `Clock cycles` 或 `Seconds` 指定 **Timer period** 或 **Timer initial period** 参数的单位。当该参数设置为 `Seconds` 时，软件会将 **Timer period** 或 **Timer initial period** 从以秒为单位的值转换为以时钟周期为单位的值。为获得最佳结果，请选择 `Clock cycles`。这样做可以减少计算次数和舍入误差。

#### 依赖关系

- 如果将 **Timer period units** 设置为 `Seconds`，请启用对浮点数的支持。在模型窗口中，选择 **Modeling > Model Settings**。
- 在“配置参数”对话框中，选择 **Code Generation > Interface**。在 **Software Environment** 下，启用 **floating-point numbers**。

### **Specify timer period via** — 配置定时器周期值的来源 `Specify via dialog`（默认）| `Input port`

当您选择 `Input port` 时，**Timer period** 参数将变为 **Timer initial period**，并在模块上创建一个定时器周期输入端口 **T**。

### **Timer period** — 指示 ePWM 计数器的周期 `64000`（默认）

设置 ePWM 计数器波形的周期。生成的 ePWM 波形周期取决于 **ePWMx** 选项卡上 **Action when counter=** 参数的设置。

当您启用 HRPWM 时，可以输入高精度浮点值。时基周期高分辨率寄存器（TBPRDHR）存储定时器周期值的高分辨率部分。

定时器周期根据 **Counting mode** 选择和 **Timer period units** 计算，如下所示。

| 计数模式 | 定时器周期单位 | 计算 | 示例 |
| --- | --- | --- | --- |
| Up 或 Down | Clock cycles | 以时钟周期输入的值用于计算 ePWM 定时器寄存器的时基周期（TBPRD）。ePWM 定时器周期 TCTR = (TBPRD + 1) \* TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。 | 对于 ePWM 时钟（EPWMCLK）频率 = 200 MHz 且 TBCLK = 5 ns。EPWMCLK 将等于 SYSCLKOUT 或 SYSCLKOUT/2，具体取决于 **EPWM clock divider (EPWMCLKDIV)** 参数设置。当定时器周期以时钟周期输入时 TBPRD = 9999，ePWM 定时器周期计算为 TCTR = 50 µs。对于 **ePWMx** 选项卡上的默认动作设置，ePWM 周期 = 50 µs。 |
| Seconds | 以秒输入的值用于计算 ePWM 定时器寄存器的时基周期（TBPRD）。寄存器中输入的 TBPRD 值为 TBPRD = (TCTR / TBCLK) – 1。其中，TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。对于 **ePWMx** 选项卡上的默认动作设置，ePWM 周期与输入的定时器周期（以秒为单位）相同。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以秒输入时 TCTR = 50 µs，时基周期计算为 TBPRD = 9999。对于 **ePWMx** 选项卡中的默认动作设置，ePWM 周期 = 50 µs。 |
| Up-Down | Clock cycles | 以时钟周期输入的值用于计算 ePWM 定时器寄存器的时基周期（TBPRD）。ePWM 定时器周期 TCTR = 2 \* TBPRD \* TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以时钟周期输入时，TBPRD = 10000，ePWM 定时器周期计算为 TCTR = 100 µs。对于 **ePWMx** 选项卡上的默认动作设置，ePWM 周期 = 100 µs。 |
| Seconds | 以秒输入的值用于计算 ePWM 定时器寄存器的时基周期（TBPRD）。寄存器中输入的 TBPRD 值为 TBPRD = TCTR / TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。对于 **ePWMx** 选项卡上的默认动作设置，ePWM 周期是输入的定时器周期（以秒为单位）的两倍。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以秒输入时 TCTR = 50 µs，时基周期计算为 TBPRD = 10000。对于 **ePWMx** 选项卡上的默认动作设置，ePWM 周期 = 100 µs。 |

### **Timer initial period** — 指示波形的初始 ePWM 周期 `64000`（默认）| `0` | `...`

从 PWM 外设开始运行到 ePWM 输入端口 **T** 接收到新的周期值为止，波形的初始周期。使用 **Timer period units** 以时钟周期或秒为单位测量周期。定时器周期的计算方式与 **Timer period** 参数类似。

#### 依赖关系

要启用此参数，请将 **Specify timer period via** 参数设置为 `Input port`。

### **Active period register load option (PRDLD)** — 计数器周期寄存器重新加载的事件 `Counter equals to zero`（默认）| `Counter equals to zero or SYNC event` | `SYNC event` | `Immediate without using shadow`

此参数提供选项以选择适当的事件来用新值更新时间周期寄存器。

- `Counter equals to zero` - 当计数器值为 0 时，计数器周期刷新。
- `Counter equals to zero or SYNC event` - 当计数器为 0 或存在同步事件时。
- `SYNC event` - 参数处于同步状态。
- `Immediate without using shadow` - 计数器周期立即刷新。

### **Counting mode** — 指示 ePWM 计数器的计数模式 `Up-Down`（默认）| `Up` | `Down`

指定计数模式。此 PWM 模块可以以三种不同的计数模式运行：`Up`、`Down` 和 `Up-Down`。

此图显示了与这三种模式对应的波形：

#### 依赖关系

`Down` 选项与 HRPWM 不兼容。为避免在构建模型时出错，请勿将 **Counting mode** 参数设置为 `Down` 并选择 **Enable HRPWM (Period)** 参数。

### **Synchronization action** — 指定相位偏移的来源 `Disable`（默认）| `Set counter to phase value specified via dialog` | `Set counter to phase value specified via input port`

指定要应用于来自 **SYNC** 输入端口的时基同步输入信号 EPWMxSYNCI 的相位偏移的来源。

- `Set counter to phase value specified via dialog` - 指定此选项以创建 **Phase offset value** 参数。

  **注意**

  - ePWM 模块期望相位值在 0 到 360 度范围内，并按时钟周期缩放后作为相位值的输入。因此对于负值，您需要加上 360 度使其进入 0 到 360 度的相位范围。例如，对于 -90 度的值，您需要提供 (360 - 90) = 270 度并按时钟周期缩放后作为输入。
  - 对于任何大于 360 度的值，您需要考虑将其回绕到 0 到 360 度范围的逻辑。例如，120 + (360 - 90) = 390 应在按时钟周期缩放并作为 ePWM 输入之前回绕为 (390 - 360) = 30 度。
- `Set counter to phase value specified via input port` - 指定此选项以在模块上创建相位输入端口 **PHS**。
- `Disable` - 指定此选项以防止对 TB 模块应用相位偏移。

### **Counting direction after phase synchronization** — 相位同步后的计数器方向 `Count down after sync`（默认）| `Count up after sync`

配置定时器在同步后向上计数还是向下计数。此参数对应于时基控制寄存器（TBCTL）的相位方向（PHSDIR）字段。

#### 依赖关系

当 **Counting mode** 为 `Up-Down` 且 **Synchronization action** 为 `Set counter to phase value specified via dialog` 或 `Input port` 时，此参数出现。

### **Phase offset value (TBPHS)** — 指定相位偏移值（TBPHS） `0`（默认）

指定的偏移值在同步事件时加载到时基计数器中。

要启用此参数，请在 **Synchronization action** 参数中选择 `Set counter to phase value specified via dialog`。

以 **TBCLK** 周期为单位输入 `Phase offset value (TBPHS)`，范围为 0 到 65535。使用 HRPWM 时，您可以输入十进制值。

**注意**

- ePWM 模块期望相位值在 0 到 360 度范围内，并按时钟周期缩放。对于负值，您需要加上 360 度使其进入 0 到 360 度的相位范围。例如，对于 -90 度的值，您需要提供 (360 - 90) = 270 度并按时钟周期缩放后作为输入。
- 对于任何大于 360 度的值，您需要考虑将其回绕到 0 到 360 度范围的逻辑。例如，120 + (360 - 90) = 390 应在按时钟周期缩放并作为输入提供之前回绕为 (390 - 360) = 30 度。

此参数对应于时基相位寄存器（TBPHS）。

### **Specify software synchronization via input port (SWFSYNC)** — 指示相位偏移值 `off`（默认）| `on`

为时基同步输入信号 EPWMxSYNCI 创建输入端口 **SYNC**。选择此参数可通过菊花链连接多个时基（TB）子模块，从而实现多个 ePWM 模块之间的精确同步。

### **Enable digital compare A event1 synchronization (DCAEVT1)** — 基于 DCAEVT1 数字比较事件同步 ePWM 时基 `off`（默认）| `on`

选择此参数以将此 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 微调两个模块之间的同步。启用 HRPWM 会禁用此选项。

**注意**

此参数仅适用于特定的 `C28x` 器件。

### **Enable digital compare B event1 synchronization (DCBEVT1)** — 基于 DCBEVT1 数字比较事件同步 ePWM 时基 `off`（默认）| `on`

选择此参数以将此 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 微调两个模块之间的同步。此选项与 `HRPWM` 不兼容。启用 `HRPWM` 会禁用此选项。

**注意**

此参数仅适用于特定的 `C28x` 器件。

### **Synchronization output (SYNCO)** — 生成时基同步输出信号的事件 `Disable`（默认）| `Pass through (EPWMxSYNCI or SWFSYNC)` | `Counter equals to zero (CTR=Zero)` | `Counter equals to compare B (CTR=CMPB)` | `Counter equals to compare C (CTR=CMPC)` | `Counter equals to compare D (CTR=CMPD)` | `Enable DCBEVT1 sync event to SYNCO signal` | `Enable DCAEVT1 sync event to SYNCO signal` | `Enable counter equals to compare D (CTR=CMPD) event to set SYNCO signal` | `Enable counter equals to compare C (CTR=CMPC) event to set SYNCO signal` | `Enable counter equals to compare B (CTR=CMPB) event to set SYNCO signal` | `Enable counter equals to zero (CTR=ZERO) event to set SYNCO signal` | `Enable SWFSYNC event to set SYNCO signal`

时基计数器同步允许提高 ePWM 模块同步的灵活性。时钟同步方案允许 ePWM 模块在需要时作为单一系统运行。此外，该同步方案还可以扩展到捕获外设子模块（eCAP）。在 Type 4 ePWM 中，有两种类型的时基计数器同步方案可用。有关更多信息，请参阅 Time-Base Counter Synchronization。

您可以在 Configuration Parameters 中配置额外的 SYNCO 选项。有关更多信息，请参阅 C28x-ePWM。

此参数对应于时基控制寄存器（TBCTL）中的 SYNCOSEL 字段。

**注意**

同步输出（SYNCO）的参数因所选处理器而异。

以下参数仅适用于 `F2837x`、`F2807x`、`F28004x` 和特定的 `C28x` 处理器。

- `Pass through (EPWMxSYNCI or SWFSYNC)` — 分别为同步输入脉冲或软件强制同步脉冲。您可以使用此选项通过菊花链连接多个时基（TB）子模块，从而实现多个 ePWM 模块之间的精确同步。
- `Counter equals to zero (CTR=Zero)` — 时基计数器等于零（TBCTR = 0x0000）
- `Counter equals to compare B (CTR=CMPB)` — 时基计数器等于计数器比较 B（TBCTR = CMPB）
- `Counter equals to compare C (CTR=CMPC)` — 时基计数器等于计数器比较 C（TBCTR = CMPC）
- `Counter equals to compare D (CTR=CMPD)` — 时基计数器等于计数器比较 D（TBCTR = CMPD）
- `Disable` — 禁用 EPWMxSYNCO 输出（默认）

以下参数仅特定于 F2838x、F28002x 和 F28003x 处理器。

- `Enable DCBEVT1 sync event to SYNCO signal` - 选择将数字比较事件 B 同步到同步输出。
- `Enable DCAEVT1 sync event to SYNCO signal` - 选择将数字比较事件 A 同步到同步输出。
- `Enable counter equals to compare D (CTR=CMPD) event to set SYNCO signal` - 使能计数器等于比较 D（CTR=CMPD）事件来置位 SYNCO 信号
- `Enable counter equals to compare C (CTR=CMPC) event to set SYNCO signal` - 使能计数器等于比较 C（CTR=CMPC）事件来置位 SYNCO 信号
- `Enable counter equals to compare B (CTR=CMPB) event to set SYNCO signal` - 使能计数器等于比较 B（CTR=CMPB）事件来置位 SYNCO 信号
- `Enable counter equals to zero (CTR=ZERO) event to set SYNCO signal` - 使能计数器等于零（CTR=ZERO）事件来置位 SYNCO 信号
- `Enable SWFSYNC event to set SYNCO signal` - 使能软件强制同步脉冲（SWFSYNC）事件来置位 SYNCO 信号

### **Peripheral synchronization event (PWMSYNCSEL)** — 时基计数器外设同步 `Counter equals to period (CTR=PRD)`（默认）| `Counter equals to zero (CTR=Zero)` | `Counter is incrementing and equals to compare C register (CTRU=CMPC)` | `Counter is decrementing and equals to compare C register (CTRD=CMPC)` | `Counter is incrementing and equals to compare D register (CTRU=CMPD)` | `Counter is decrementing and equals to compare D register (CTRD=CMPD)`

每个 ePWM 模块都有一个外设同步输出（SYNCPER）。该输出信号用于将 CMPSS 同步到 EPWM。有关更多信息，请参阅 Time-Base Counter Peripheral Synchronization。

**注意**

此参数仅适用于某些特定的 `C28x` 处理器。

### **Time base clock (TBCLK) prescaler divider** — 对应于 CLKDIV 的时基时钟（TBCLK）预分频器 `1`（默认）| `2` | `4` | `…`

使用 **Time base clock (TBCLK) prescaler divider**（CLKDIV）和 **High speed time base clock (HSPCLKDIV) prescaler divider**（HSPCLKDIV）来配置 ePWM 模块的时基时钟速度（TBCLK）。使用以下公式计算 TBCLK：

TBCLK（Hz）= PWM 时钟（Hz）/(HSPCLKDIV \* CLKDIV)

例如，CLKDIV 和 HSPCLKDIV 的默认值均为 1，PWM 时钟的默认频率为 100 MHz，因此：

TBCLK（Hz）= 100 MHz/(1 \* 1) = 100 MHz

TBCLK（秒）= 1/TBCLK（Hz）= 1/100 MHz = 0.01 μs

**Time base clock (TBCLK) prescaler divider** 的可选值为：`1`、`2`、`4`、`8`、`16`、`32`、`64` 和 `128`。

**Time block clock (TBCLK) prescaler divider** 参数对应于时基控制寄存器（TBCTL）的 CLKDIV 字段。

PWM 时钟是 SYSCLKOUT 或使用 PWM 时钟分频器从 SYSCLKOUT 派生的时钟。对于少数 TI C2000 处理器，有一个 PWM 时钟分频器可以对 SYSCLKOUT 进行分频以派生 PWM 模块时钟。有关更多详细信息，请查阅您处理器的技术参考手册。

SYSCLKOUT 的频率取决于振荡器频率和基于 PLL 的时钟模块的配置。更改 SYSCLOCKOUT 的值会影响所有 ePWM 模块的时序。如果处理器中有可用的 PWM 时钟预分频，更改其值也会影响 PWM 时序。

### **High speed time base clock (HSPCLKDIV) prescaler divider** — 高速时基时钟（HSPCLKDIV）预分频器 `1`（默认）| `2` | `4` | `...`

**High speed time base clock (HSPCLKDIV) prescaler divider** 的可选值为：`1`、`2`、`4`、`6`、`8`、`10`、`12` 和 `14`。

选择 **Enable high resolution PWM (HRPWM – period)** 会将此参数的值设置为 `1`。

此参数对应于时基控制寄存器（TBCTL）的 HSPCLKDIV 字段。

### **Enable swap module A and B** — 交换模块 A 和 B 的输出信号 `off`（默认）| `on`

交换 ePWMA 和 ePWMB 输出。当您选择此参数时，模块在 ePWMB 输出上输出 ePWMA 信号，在 ePWMA 输出上输出 ePWMB 信号。

此参数设置 HRPWM 配置寄存器（HRCNFG）中的 SWAPB 字段。此选项适用于支持 HRPMW 的 ePWM，因为它使用 HRCNFG 寄存器。

**注意**

此参数仅适用于特定的 `C28x` 器件。

### ePWMA 和 ePWMB

您可以在 ePWMA/ePWMB 选项卡以及 Counter compare 选项卡中执行波形生成配置。

ePWM 硬件模块可以为 A 和 B 通道生成波形，随后通过 Deadband 模块和 HRPWM 模块进行波形生成。

在波形生成期间，您可以为 ePWMA 和 ePWMB 生成波形，但这些波形选项可以被 Deadband 配置中选择的选项覆盖。例如，您可以选择不在波形生成模块中配置 eWPMB，而是使用 eWPMA 波形为 ePWMA 和 ePWMB 两个通道创建 Deadband 输出。

### **Enable ePWM#x** — 使能 ePWMx 输出信号 `off`（默认）| `on`

使能在 **General** 选项卡上选择的 ePWM 模块的 ePWMA 和/或 ePWMB 输出信号。在此情况下，# 表示 ePWM 模块，x 表示 A 或 B。默认情况下，**Enable ePWM#A** 已使能，**Enable ePWM#B** 已禁用。

每个 ePWM 模块有两个输出：ePWMA 和 ePWMB。ePWMA 输出选项卡和 ePWMB 输出选项卡包含相同的设置，尽管在某些情况下默认值有所不同。

#### 依赖关系

当您选择 **Enable ePWM#A** 或 **Enable ePWM#B** 时，请通过浏览到 **Configuration Parameters** > **Code Generation** > **Interface** > **Software Environment** 来使能浮点数支持。

### **Action when counter=ZERO, Action when counter=period (PRD), Action when counter=CMPA on up-count (CAU), Action when counter=CMPA on down-count (CAD), Action when counter=CMPB on up-count (CBU), Action when counter=CMPB on down-count (CBD)** — 确定动作限定器（AQ）子模块的行为 `Set`（默认）

**ePWMA output** 和 **ePWMB output** 选项卡上的这组参数确定动作限定器（AQ）子模块的行为。AQ 模块确定哪些事件被转换为各种动作类型之一，从而产生 ePWM#A 和 ePWM#B 输出信号所需的开关波形。

这些参数可以指定为 `Do nothing`、`Clear`、`Set` 或 `Toggle`。

默认值在 **ePWMA** 和 **ePWMB** 选项卡之间有所不同。

下表显示了当您将 **Counting mode** 设置为 `Up` 或 `Up-Down` 时，每个选项卡的默认值：

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Set | Clear |
| period (PRD) | Clear | Set |
| CMPA on up-count (CAU) | Clear | Set |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on up-count (CBU) | Do nothing | Clear |
| CMPB on down-count (CBD) | Do nothing | Set |

下表显示了当您将 **Counting mode** 设置为 `Down` 时，每个选项卡的默认值：

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Do nothing | Do nothing |
| period (PRD) | Clear | Clear |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on down-count (CBD) | Do nothing | Set |

有关 AQ 子模块的详细讨论，请参阅 *TMS320x280x Enhanced Pulse Width Modulator (ePWM) Module Reference Guide*（SPRU791），可在 Texas Instruments 网站上获取。

### **Add continuous software force input port, Continuous software force logic, Reload condition for software force** — 确定动作限定器（AQ）子模块如何处理软件强制事件 `Load on counter equals to zero (CTR=Zero)`（默认）

这些参数确定动作限定器（AQ）子模块如何处理软件强制事件，这是一种由软件（CPU）通过控制寄存器位发起的异步事件。

**Compare value reload condition** 确定是否以及何时从影子寄存器重新加载动作限定器软件强制寄存器。您可以指定以下之一：`Load on counter equals to zero (CTR=Zero)`（默认）、`Load on counter equals to period (CTR=PRD)`、`Load on either` 和 `Freeze`。

**Add continuous software force input port** 创建一个输入端口 **SFA**，您可以使用它来控制软件强制初始逻辑。将以下值之一作为无符号整数数据类型发送到 **SFA**：

- 0 = `Forcing disable`：不执行任何操作（默认）。
- 1 = `Forcing low`：清零为低电平
- 2 = `Forcing high`：置位为高电平
- 3 = `Forcing disable`：不执行任何操作

**Continuous software force logic** - 如果您没有创建 **SFA** 输入端口，可以使用它来选择应用哪种类型的软件强制初始逻辑。您可以指定以下之一：

- `Forcing disable`：不执行任何操作（默认）。
- `Forcing low`：清零为低电平
- `Forcing high`：置位为高电平

**Reload condition for software force**

您可以指定以下之一：`Counter equals to zero (CTR=Zero)`（默认）、`Counter equals to period (CTR=PRD)`、`Either period or zero` 和 `Immediate`。

### **Inverted version of ePWM#A** — 反转 ePWM#A 信号 `off`（默认）| `on`

反转 ePWM#A 信号并将其输出到 ePWM#B 输出上。

此参数设置 HRPWM 配置寄存器（HRCNFG）中的 SELOUTB 字段，适用于支持 HRPWM 的 ePWM，因为它使用 HRCNFG 寄存器。

**注意**

此参数仅适用于具有 HRPWM 子模块的 ePWM 模块。使能此参数会反转 ePWM#B，无论模块中是否使能了 HRPWM。

### **Enable high resolution PWM (HRPWM)** — 使能高分辨率 PWM 设置 `off`（默认）| `on`

#### 依赖关系

- 此参数仅适用于 C280x 和 C2833x 处理器的 **ePWMx** 选项卡，以及其余处理器的 **HRPWM** 选项卡。有关更多信息，请参阅 HRPWM 选项卡部分。
- 类似地，**High resolution PWM (HRPWM) loading mode**、**High resolution PWM (HRPWM) control mode**、**High resolution PWM (HRPWM) edge control mode** 和 **Use scale factor optimizer (SFO) software** 等参数在 C280x 和 C2833x 处理器的 **ePWMx** 选项卡中以及其余处理器的 **HRPWM** 选项卡中可用。有关更多信息，请参阅 HRPWM 选项卡部分。

### Counter Compare

### **ePWMLink CMPx** — ePWM 模块的链接 `Not Linked`（默认）| `ePWM1` | `ePWM2` | `...`

在 ePWMx 中，x 的范围为 1 到 12

选择一个 ePWM 模块，您希望将当前 ePWM 模块链接到该模块以获取计数器值。在此情况下，对于 CMPx，x 表示 A、B、C 或 D。当您将一个 ePWM 模块的计数器值链接到另一个模块时，链接的 ePWM 模块的 **CMPx value** 将在当前模块中使用。当您选择另一个 ePWM 模块进行链接时，**CMPx**、**Specify CMPx via** 和 **CMPx value** 参数不会出现。

但是，当您将一个 ePWM 模块链接到模型中不存在的模块时，链接没有效果。

**注意**

此参数仅适用于某些 TI C2000 处理器。

### **CMPx Units** — 比较寄存器使用的单位 `Clock cycles`（默认）| `Percentages`

四个比较寄存器 CMPA、CMPB、CMPC 和 CMPD 与时基计数器值进行比较以生成相应的事件。CMPA 和 CMPB 事件用于通过在 **ePWMA** 和 **ePWMB** 选项卡上选择适当的动作来控制 PWM 占空比。这些事件还可以用于生成到 CPU 的中断和/或到 ADC 的转换启动脉冲。您可以参考 **Event Trigger** 选项卡来选择要触发的事件。

比较寄存器 **CMPC** 和 **CMPD** 仅存在于最新的处理器中。

**注意**

- 术语 *clock cycles* 指的是处理器上的时基时钟。有关时基时钟速度计算的说明，请参阅 **TB clock prescaler divider** 主题。
- 百分比在生成的代码中使用额外的计算时间，可能会降低结果的精度。

#### 依赖关系

如果您将 ***CMPx units*** 设置为 `Percentages`，请通过浏览到 **Configuration Parameters** > **Code Generation** > **Interface** > **Software Environment** 来使能浮点数支持。在此情况下，x 表示 A、B、C 或 D。

### **Specify CMPx Via** — 脉冲宽度来源 `Specify via dialog`（默认）| `Input port`

指定脉冲宽度的来源。如果您选择 `Specify via dialog`（默认），请为 **CMPx value** 参数输入一个值。如果您选择 `Input port`，模块将在模块上创建一个名为 WA、WB、WC 或 WD 的新输入端口。如果您选择 `Input port`，请确保设置 **CMPx initial value** 参数。在此情况下，x 表示 A、B、C 或 D。

### **CMPx Value/CMPx Initial Value** — 脉冲宽度值 `32000`（默认）

当您将 **CMPx source** 设置为 `Specify via dialog` 时，会出现 **CMPx Value** 字段。当您将 **CMPx source** 设置为 `Input port` 时，会出现 **CMPx Initial Value** 字段。输入一个值来指定脉冲宽度，单位在 **CMPx units** 中指定。在此情况下，x 表示 A、B、C 或 D。

输入 PWM 外设在开始运行时使用的 CMPA 或 CMPB 的初始脉冲宽度。后续输入到 **WA** 或 **WB** 端口会更改 CMPA 或 CMPB 脉冲宽度。

### **Reload for compare x Register (SHDWxMODE)** — 计数器周期复位的时间 `Counter equals to zero (CTR=Zero)`（默认）| `Counter equals to period (CTR=PRD)` | `Counter equals to Zero or period (CTR=Zero or CTR=PRD)` | `...`

计数器周期复位的时间。在此情况下，x 表示 A、B、C 或 D。

- `Counter equals to zero
  (CTR=Zero)` — 当计数器的值为 0 时刷新计数器周期。
- `Counter equals to period
  (CTR=PRD)` — 当计数器的值为 period 时刷新计数器周期。
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` — 当计数器的值为 0 或 period 时刷新计数器周期。
- `Freeze` — 当计数器的值为 freeze 时刷新计数器周期。
- `Counter equals to zero or SYNC
  event` — 当计数器的值为 0 或 SYNC 时刷新计数器周期。
- `Counter equals to period or SYNC
  event` — 当计数器的值为 0 或 SYNC 时刷新计数器周期。
- `Counter equals to zero or period or SYNC
  event` — 当计数器的值为 0 或 period 或 SYNC 时刷新计数器周期。
- `SYNC event` — 当计数器的值为 SYNC 时刷新计数器周期。
- `Immediate without using shadow`
  — 立即刷新计数器周期。

### Deadband Unit

### **Use deadband for ePWM#A, Use deadband for ePWM#B** — 使能死区区域 `off`（默认）| `on`

使能上升沿延迟或下降沿延迟周期的死区区域，且 ePWM 输出信号对之间无信号重叠。确保在 ePWMx 选项卡上使能相应的 **ePWMx (x=A or B)** 以生成对应的 DB。

### **Enable half-cycle clocking** — 死区分辨率加倍 `off`（默认）| `on`

使能半周期时钟以将死区分辨率加倍。此选项以 TBCLK\*2 对死区计数器进行时钟控制，即将以秒为单位的时钟值除以 2，从而使频率加倍。

禁用此选项时，死区计数器使用全周期时钟（TBCLK\*1）。

**注意**

此参数仅适用于特定的 C28x 器件。

### **Deadband Polarity** — 死区时间时的 ePWM 输出状态 `Active high (AH)`（默认）| `Active low (AL)` | `Active high complementary (AHC)` | `Active low complementary (ALC)`

仅为一个 ePWM 使能死区极性时，将看到 `Positive` 和 `Negative` 选项。

为两个 ePWM 使能死区极性时，将看到 `Active high (AH)`、`Active low (AL)`、`Active high complementary (AHC)` 或 `Active low complementary (ALC)` 选项。

在死区时间，ePWMA 和 ePWMB 输出都必须设置为非活动状态。根据硬件设置，非活动状态可能对应高逻辑值或低逻辑值。Active high 表示当 ePWM 输出设置为高逻辑值时系统处于活动状态。Active low 表示当 ePWM 输出设置为低逻辑值时系统处于活动状态。当 B 信号需要为 A 的反相时，使用 Complementary 选项。有关更多信息，请参阅处理器的 ePWM 技术参考指南。

此图显示了 0% < 占空比 < 100% 的典型情况下的波形。

### **Signal source for rising edge (RED)** — 上升沿源 `ePWMxA`（默认）| `ePWMxB`

选择需要施加上升沿延迟（RED）的信号源。可以选择 ePWMxA 或 ePWMxB 作为上升沿。

### **Signal source for falling edge (FED)** — 下降沿源 `ePWMxA`（默认）| `ePWMxB`

选择需要施加下降沿延迟（FED）的信号源。可以选择 ePWMxA 或 ePWMxB 作为下降沿。

### **Deadband period units** — 指示死区周期单位 `Clock cycles`（默认）| `Seconds`

将 **Deadband period** 的单位指定为 `Clock cycles` 或 `Seconds`。当 **Deadband period units** 设置为 `Seconds` 时，软件将 **Deadband period** 从以秒为单位的值转换为以时钟周期为单位的值。为获得最佳结果，请选择 `Clock cycles`。这样做可以减少计算和舍入误差。

#### 依赖关系

- 如果将 **Deadband period units** 设置为 `Seconds`，请使能对浮点数的支持。在模型窗口中，选择 **Simulation > Model Configuration Parameters**。

  在 Configuration Parameters 对话框中，选择 Code Generation > Interface。在 **Software Environment** 下，使能 **floating-point numbers**。
- 此参数仅适用于某些 TI 的 C2000™ 处理器。

### **Deadband period source** — 控制逻辑源 `Specify via dialog`（默认）| `Input port`

将 **Deadband period** 的来源选择为 `Specify via dialog` 或 `Input port`。

### **Deadband Rising edge (RED) period (0-16383)** — RED 延迟时间值 `0`（默认）

在字段中输入的值指定以时基时钟为单位的死区延迟。

**Deadband rising edge period (0-16383)** 参数的结果取决于 `Deadband period units` 和 `Deadband period source`。

下表说明了基于所选的 `deadband unit`、`deadband source` 和 `processor` 的死区上升沿周期结果。

| Deadband period units | Deadband period source | Deadband rising edge(RED) period |
| --- | --- | --- |
| Clock cycles | Specify via dialog | Deadband Rising edge (RED) period (0~16383) |
| Deadband Rising edge (RED) period (0~1023) |
| 时钟周期 | 输入端口 | 死区上升沿（RED）初始周期（0~16383） |
| Deadband Rising edge (RED) initial period (0~1023) |
| Seconds | Specify via dialog | Deadband Rising edge (RED) period |
| Deadband Rising edge (RED) period |
| 秒 | 输入端口 | 死区上升沿（RED）初始周期： |
| Deadband Rising edge (RED) initial period: |

### **Deadband Falling edge (FED) period** — FED 延迟时间值 `0`（默认）

在字段中输入的值指定以时基时钟为单位的死区延迟。

参数 **Deadband falling edge period** 的结果取决于 `Deadband period units` 和 `Deadband period source`。**Deadband falling edge period** 的值与 **Deadband rising edge period** 类似。有关更多信息，请参阅 deadband rising edge (RED) period 参数。

### **Reload for DBRED register (SHDWDBRED), Reload for DBFED register (SHDWDBFED)** — 影子寄存器传送到活动寄存器的事件 `Immediate without using shadow`（默认）| `Freeze` | `Counter equals to zero (CTR=Zero)` | `Counter equals to period (CTR=PRD)` | `Counter equals to either zero or period (CTR=Zero or CTR=PRD)` | `...`

影子寄存器传送到活动寄存器且计数器周期复位的事件。

- `Immediate without using shadow`
  — 立即刷新计数器周期。
- `Counter equals to zero
  (CTR=Zero)` — 当计数器的值为 0 时刷新计数器周期。
- `Counter equals to period
  (CTR=PRD)` — 当计数器的值为 period 时刷新计数器周期。
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` — 当计数器的值为 0 或 period 时刷新计数器周期。
- `Freeze` — 当计数器的值为 freeze 时刷新计数器周期。

#### 依赖关系

**SHDWDBRED** 和 **SHDWDBFED** 仅在选中 **Use deadband for ePWM#A** 或 **Use deadband for ePWM#B** 时可用。

### Event Trigger

### **Enable ADC start of conversion for module A** — ADC 转换启动事件 `off`（默认）| `on`

选中此选项时，当 **Start of conversion for module A event selection** 参数中选择的事件发生时，将生成 ADC 转换启动事件（ePWMSOCxA）。

### **Number of event for start of conversion for Module A (SOCA) to be generated** — 事件启动编号 `First event`（默认）| `Second event` | `Third event` | `...`

选中 **Enable ADC start of conversion for module A** 时，此字段指定触发模块 A 的 ADC 转换启动（SOCA）的事件编号。

`First event` 在每个事件时触发 ADC 转换启动（默认）。`Second event` 在每第二个事件时触发 ADC 转换启动。`Third event` 在每第三个事件时触发 ADC 转换启动。

事件触发范围从 `First event` 到 `Fifteenth event`，具体取决于所选的处理器。

### **Start of conversion for module A event selection** — 指示触发 ADC 转换启动事件的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认）| `Digital Compare Module A Event 1 start of conversion (DCAEVT1.soc)` | `...`

此参数指定触发 ADC 转换启动事件的计数器匹配条件。选项包括：

- `Digital Compare Module A Event 1 start of
  conversion (DCAEVT1.soc)(For specific C28x devices
  only)` - 当 ePWM 断言 DCAEVT1 或 DCBEVT1 数字比较事件时。使用此功能可将所选 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 参数微调两个模块之间的同步。
- `Counter equals to zero (CTR=Zero)` -
  当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` -
  当 ePWM 计数器达到周期值时。
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - 当时基计数器达到零（TBCTR = 0x0000）或当时基计数器达到周期（TBCTR = TBPRD）时。
- `计数器正在递增且等于比较值
  x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `计数器正在递减且等于比较值
  x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### **Enable ADC start of conversion for module B** — ADC 转换启动事件 `off`（默认）| `on`

选中此选项时，当 **Start of conversion for module B event selection** 参数中选择的事件发生时，将生成 ADC 转换启动事件（ePWMSOCxB）。

### **Number of event for start of conversion for Module B (SOCB) to be generated** — 事件启动编号 `First event`（默认）| `Second event` | `Third event` | `...`

选中 **Enable ADC start of conversion for module B** 时，此字段指定触发模块 B 的 ADC 转换启动（SOCB）的事件编号。

`First event` 在每个事件时触发 ADC 转换启动（默认）。`Second event` 在每第二个事件时触发 ADC 转换启动。`Third event` 在每第三个事件时触发 ADC 转换启动。

事件触发范围从 `First event` 到 `Fifteenth event`，具体取决于所选的处理器。

### **Start of conversion for module B event selection** — 指示触发 ADC 转换启动事件的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认）|

选中 **Enable ADC start of conversion for module B** 时，此字段指定触发 ADC 转换启动事件的计数器匹配条件。选项包括：

- `Digital Compare Module B Event 1 start of
  conversion (DCBEVT1.soc) (For specific C28x devices
  only)` - 当 ePWM 断言 DCAEVT1 或 DCBEVT1 数字比较事件时。使用此功能可将所选 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 微调两个模块之间的同步。
- `Counter equals to zero (CTR=Zero)` -
  当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` -
  当 ePWM 计数器达到周期值时。
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - 当时基计数器达到零（TBCTR = 0x0000）或当时基计数器达到周期（TBCTR = TBPRD）时。
- `计数器正在递增且等于比较值
  x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `计数器正在递减且等于比较值
  x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### **Enable ePWM interrupt** — 生成 ePWM 中断 `Disabled`（默认）| `Enabled`

选择此选项以基于 **Number of event for interrupt to be generated** 和 **Interrupt counter match event condition** 定义的不同事件生成 ePWM 中断。默认情况下，软件清除（禁用）此选项。

### **Number of event for interrupt to be generated** — 指定触发 ePWM 中断的事件编号 `First event`（默认）| `Second event to fifteenth event`

选中 ***Enable ePWM interrupt*** 时，此字段指定触发 ePWM 中断的事件编号：`First event` 在每个事件时触发 ePWM 中断（默认），`Second event` 在每第二个事件时触发 ePWM 中断，`Third event` 在每第三个事件时触发 ePWM 中断。

**注意**

事件触发范围从 `First event` 到 `Fifteenth event`，具体取决于所选的处理器。

### **Interrupt counter match event condition** — 指示触发 ePWM 中断的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认）

选中 ***Enable ePWM interrupt*** 时，此字段指定触发 ePWM 中断的计数器匹配条件。选项与 **Module A counter match event condition** 相同。选项包括：

- `Counter equals to zero (CTR=Zero)` -
  当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` -
  当 ePWM 计数器达到周期值时。
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - 当时基计数器达到零（TBCTR = 0x0000）或当时基计数器达到周期（TBCTR = TBPRD）时。
- `计数器正在递增且等于比较值
  x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `计数器正在递减且等于比较值
  x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### HRPWM Tab

在 F2837xD 处理器的 HR（高分辨率）配置期间，ePWM 模块仅存在于 ePWM1 上，且 SFO 仅在 CPU1 上运行。因此，如果要使用 HRPWM，则 ePWM1 必须分配给 CPU1，并且如果使能了 SFO，它必须在 CPU1 上运行。

对于 F2838xD 器件，尽管 CPU 和 EWPM1 仍然执行 HRPWM 的校准，但每个 EPWM 模块对自己的 HRPWM 进行时钟控制，并使用由 SFO 计算的相同 HRMSTEP 值。这使得 HRPWM 能够在 CPU2 上正确运行。

### **Enable High Resolution Period on ePWM#A (HRPWM - period), Enable High Resolution Period on ePWM#B (HRPWM - period)** — 指示常规生成 PWM 的有效分辨率 `off`（默认）| `on`

当常规生成 PWM 的有效分辨率不足时，考虑使用高分辨率 PWM (HRPWM)。PWM 的分辨率通常取决于 PWM 频率和底层系统时钟频率。为解决此限制，HRPWM 使用 **Micro Edge Positioner (MEP)** 技术，通过细分每个粗系统时钟来更精细地定位边沿。细分的精度约为 `150ps`。下图展示了以一个系统时钟与以 **MEP** 步进表示的边沿位置之间的关系：

当启用此参数时，模块接受 ePWM 模块定时器周期的十进制值。HRPWM 周期扩展寄存器 (TBPRDHR) 提供 **Timer period** 值小数部分的 8 位表示。此参数会启用 **Enable high resolution PWM (HRPWM - duty)** 参数，并显示 **HRPWM loading mode**、**HRPWM control mode** 和 **HRPWM edge control** 模式参数。

选择 Enable HRPWM (Period) 会将 **TB clock prescaler divider** 和 **High Speed TB clock prescaler divider** 强制为 `1`。这些设置使 HRPWM 时基时钟与 SYSCLKOUT 频率匹配。

**Counting mode** 参数中的 `Down` 选项与 HRPWM 不兼容。为避免在构建模型时出错，请勿将 **Counting mode** 参数设置为 `Down` 并选中 **Enable HRPWM (Period)** 参数复选框。

**注意**

此参数仅适用于特定的 C28x 器件。

### **Enable HRPWM Duty on ePWM#A(HRPWM - duty)** — 指示比较值的小数部分 `off`（默认）| `on`

当启用此参数时，ePWM 模块的比较 A 值 (CMPA) 将接受十进制值。HRPWM 比较 A 扩展寄存器 (CMPAHR) 提供比较值小数部分的 8 位表示。

此参数还会启用 **HRPWM control mode**。

**注意**

此参数仅出现在特定的 C28x 器件上。

### **High resolution PWM (HRPWM) Load mode on ePWM#A** — 确定何时将 CMPAHR 影子值传输到活动寄存器 `Counter equals to period (CTR=PRD)`（默认）| `Counter equals to zero (CTR=ZERO)` | `Counter equals to either zero or period (CTR=ZERO or CTR=PRD)`

此参数在选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时出现。确定何时将 CMPAHR 影子值传输到活动寄存器：

- `Counter equals to zero (CTR=ZERO)` — 当时基计数器等于零 (TBCTR = 0x0000) 时传输该值。
- `Counter equals to period (CTR=PRD)` — 当时基计数器等于周期 (TBCTR = TBPRD) 时传输该值。
- `Counter equals to either zero or period (CTR=ZERO or CTR=PRD)` — 当任一条件为真时传输该值。

此参数配置 HRPWM 配置寄存器 (HRCNFG) 中的 HRLOAD 影子模式位。

### **High resolution PWM (HRPWM) control mode on ePWM#A** — 指示控制模式 `Duty control mode`（默认）| `Phase control mode`

此参数在选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时出现。选择哪个寄存器控制 Micro Edge Positioner (MEP) 步长。**High resolution PWM (HRPWM) control mode** 选项配置 CTLMODE 控制模式位。

- `Duty control mode` — 使用 HRPWM 占空比扩展寄存器 (CMPAHR) 或 HRPWM 周期扩展寄存器 (TBPRDHR) 来控制 MEP 边沿位置。
- `Phase control mode` — 使用时基相位高分辨率寄存器 (TBPHSHR) 来控制 MEP 边沿位置。

### **High resolution PWM (HRPWM) edge control mode** — 指示边沿控制模式 `Both Edge`（默认）| `Rising Edge` | `Falling Edge`

选择控制边沿类型上 MEP 精确位置控制的寄存器。

- `Rising Edge` — 上升沿的 MEP 控制
- `Falling Edge` — 下降沿的 MEP 控制
- `Both Edge` — 两个边沿的 MEP 控制

**High resolution PWM (HRPWM) edge control mode** 选项配置 HRPWM 配置寄存器 (HRCNFG) 中的 EDGMODE 边沿模式位。

#### 依赖关系

此参数在选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时出现。

### **Enable high resolution deadband rising edge (RED), Enable high resolution deadband falling edge (FED)** — 在死区上升沿延迟和下降沿延迟上启用 HRPWM 功能 `off`（默认）| `on`

这些参数在死区上升沿延迟和下降沿延迟上启用 HRPWM 功能。高分辨率死区 RED 和 FED 需要半周期时钟模式。

#### 依赖关系

这些参数在选中 **Use deadband for ePWM#A** 或 **Use deadband for ePWM#B** 时出现。

**注意**

这些参数仅适用于特定的 F28x 器件。选中这些参数时，PWM 斩波器模块被禁用。

### **Use scale factor optimizer (SFO) software** — 指示比例因子 `off`（默认）| `on`

在 HRPWM 中启用比例因子优化 (SFO) 软件。此软件动态确定 MEP 步长的比例因子。步长随温度和电压等工作条件而变化。SFO 软件减少了这些条件引起的变异性。有关更多信息，请参阅 *TMS320x2802x, 2803x Piccolo High Resolution Pulse Width Modulator (HRPWM) Reference Guide* 的 Scale Factor Optimizing Software (SFO) 部分。

#### 依赖关系

- **Use scale factor optimizer (SFO) software** 参数仅在选中 **Enable auto convert** 和 **Enable high resolution PWM (HRPWM - period)** 参数时启用、只读且可见。
- **Use scale factor optimizer (SFO) software** 参数仅在取消选中 **Enable auto convert** 参数时可编辑。

### **Enable auto convert** — 指示自动转换 `off`（默认）| `on`

将 SFO 软件计算的比例因子应用于控制周期或占空比。（使用 **HRPWM duty mode** 选择控制周期或占空比。）此参数设置 HRPWM 配置寄存器 (HRCNFG) 中的 AUTOCONV 字段。

#### 依赖关系

- **Enable auto convert** 参数仅出现在特定的 C28x 器件上。
- **Enable auto convert** 参数仅在选中 **Enable high resolution PWM (HRPWM - period)** 参数时启用、只读且可见。
- **Enable auto convert** 参数仅在选中 **Enable high resolution PWM (HRPWM - duty)** 参数时启用且可编辑。

### PWM Chopper Control Tab

### **Chopper module enable** — 启用斩波器模块 `off`（默认）| `on`

选择以启用斩波器模块。

### **Chopper frequency divider** — 确定斩波器时钟频率 `1`（默认）| `2` | `...`

设置确定斩波器时钟频率的预分频器值。系统时钟速度除以此值以确定斩波器时钟频率。选择 `1` 到 `8` 范围内的整数值。

### **Chopper clock cycles width of first pulse** — 用于快速开启硬开关功率开关的高能量第一脉冲 `1`（默认）| `2` | `...`

选择 `1` 到 `16` 范围内的整数值来设置第一脉冲的宽度。此功能提供高能量第一脉冲以快速开启硬开关功率开关。

### **Chopper pulse duty cycle** — 确定第二及后续脉冲的占空比 `12.5%`（默认）| `25%` | `...`

第二及后续脉冲的占空比也是可编程的。占空比可以以 `12.5%` 为步长从 `12.5%` 变化到 `87.5%`。

### Trip Zone Unit

### **Trip zone source** — 确定跳闸区信号控制逻辑的来源 `Specify via dialog`（默认）| `Input port`

指定跳闸区信号控制逻辑的来源。选择 `Specify via dialog`（默认）以在模块对话框中启用特定的跳闸区信号。选择 `Input port` 以使用模块输入端口 **TZSEL** 启用特定的跳闸区信号。

**Trip Zone unit** 选项卡允许您指定跳闸区 (TZ) 子模块的参数。每个 ePWM 模块从 GPIO MUX 接收 TZ 信号。跳闸区信号的数量因 C28x 处理器系列而异。这些信号可用于根据外部故障等事件将 ePWM 输出强制到特定状态。使用此选项卡上的设置来编程 ePWM 输出以响应外部事件。

如果选择 `Input port`，请使用此位操作来确定发送到 **TZSEL** 输入端口的 16 位整数值：

`TZSEL 输入值 = (DCBEVT1*2 15
+ DCAEVT1*2 14 +
OSHT6*213 +
OSHT5*212 +
OSHT4*211 +
OSHT3*210 +
OSHT2*29 +
OSHT1*28 + DCBEVT2*2
7 + DCAEVT2*2
6 +
CBC6*25 +
CBC5*24 +
CBC4*23 +
CBC3*22 +
CBC2*21 +
CBC1*20)`

软件使用高 8 位用于 **One shot TZ1-TZ6** (OSHT1–6)，低 8 位用于 **Cyclic TZ1-TZ6** (CBC1–6)。您可以设置一组 TZ 源 (1~6)，使用位操作将它们组合成一个整数，然后将该整数馈送到 TZSEL。

例如，要启用 One Shot TZ6 (OSHT6) 和 One Shot TZ5 (OSHT5) 作为跳闸区源，将 OSHT6 和 OSHT5 设置为 1，其余值保持为 0。

TZSEL 输入值 = (1\*215 +
1\*214 + 1\*213
+ 1\*212 + 0\*211
…)

TZSEL 输入值 = (8192 + 4096 + 0 …)

TZSEL 输入值 = 12288

当模块接收到此值时，它会将其作为二进制值应用到 TZSEL 寄存器：`0011000000000000`。

有关更多信息，请参阅 TMS320x28xx, 28xxx Enhanced Pulse Width Modulator (ePWM) Module Reference Guide 的 Trip-Zone Submodule Control and Status Registers 部分。

### **Enable one-shot Trip-zone# (TZ#)** — 以单次模式启用相应的跳闸区信号 `off`（默认）| `on`

选择此参数以单次模式启用相应的跳闸区信号。在此模式下，当跳闸事件有效时，跳闸区模块立即对 EPWM#A/B 输出执行相应操作并锁存该条件。

当单次跳闸事件发生时，单次跳闸事件标志 `TZFLG[OST]` 被置位。导致单次跳闸事件的事件的相应标志也会通过寄存器读/写模块在寄存器 `TZOSTFLG` 中置位。要清除单次跳闸条件，请使用寄存器读/写模块手动写入 `TZCLR[OST]` 位。类似地，要清除 `TZOSTFLG` 寄存器位，请使用寄存器读/写模块手动写入 `TZOSTCLR` 寄存器中的相应位。

例如，要清除 ePWM1 中的 `OST1` 跳闸事件，请使用寄存器读/写模块将 1 写入 `EPwm1Regs.TZCLR.bit.OST` 和 `EPwm1Regs.TZOSTCLR.bit.OST1` 位。

#### 依赖关系

此选项仅在 **Trip zone source** 为 `Specify via dialog` 时可用。

### **Enable one-shot digital compare A event 1 (DCAEVT1), Enable one-shot digital compare B event 1 (DCBEVT1)** — 启用相应事件信号作为事件 1 的 OST 跳闸源 `off`（默认）| `on`

选择这些参数以启用相应事件信号作为事件 1 的 OST 跳闸源。在此模式下，如果数字比较 A 或数字比较 B 事件 1 有效，跳闸区模块立即对 EPWM#A/B 输出执行相应操作并锁存该条件。您可以使用软件控制解锁该条件。

#### 依赖关系

- 此选项仅在 **Trip zone source** 为 `Specify via dialog` 时可用。
- 此参数仅适用于特定的 C28x 处理器。

### **Enable cyclic Trip-zone# (TZ#)** — 以逐周期模式启用相应的跳闸区信号 `off`（默认）| `on`

选择此参数以逐周期模式启用相应的跳闸区信号。在此模式下，当跳闸事件有效时，跳闸区模块立即对 EPWM#A/B 输出执行相应操作并锁存该条件。在逐周期模式下，当 ePWM 计数器达到零时，跳闸区模块自动清除条件。因此，在逐周期模式下，每个 ePWM 周期都会复位或清除跳闸事件。

#### 依赖关系

此选项仅在 **Trip zone source** 为 `Specify via dialog` 时可用。

### **Enable cyclic digital compare A event 2 (DCAEVT2), Enable cyclic digital compare B event 2 (DCBEVT2)** — 启用相应事件信号作为事件 2 的循环跳闸源 `off`（默认）| `on`

选择这些参数以启用相应事件信号作为事件 2 的循环跳闸源。在此模式下，如果数字比较 A 或数字比较 B 事件 2 有效，跳闸区模块立即对 EPWM#A/B 输出执行相应操作并锁存该条件。在逐周期模式下，当 ePWM 计数器达到零时，跳闸区模块自动清除条件。因此，在逐周期模式下，每个 ePWM 周期都会复位或清除跳闸事件。

#### 依赖关系

- 此选项仅在 **Trip zone source** 为 `Specify via dialog` 时可用。
- 此参数仅适用于特定的 C28x 处理器。

### **Enable trip-zone one-shot interrupt (OST)** — 启用跳闸区单次中断 `off`（默认）| `on`

当任何已启用的单次 (OST) 触发事件发生时生成中断。

**注意**

`TZFLG.INT` 在 ISR 的后处理中被清除。但是，如果在 `CBC` 或 `OST` 被置位时清除中断标志，则会生成另一个中断脉冲。清除所有标志位将防止进一步的中断。此位通过向 `TZCLR` 寄存器写入适当的值来清除。

### **Enable trip-zone cycle-by-cycle interrupt (CBC)** — 启用跳闸区逐周期中断 `off`（默认）| `on`

当任何已启用的循环或逐周期 (CBC) 触发事件发生时生成中断。

**注意**

`TZFLG.INT` 在 ISR 的后处理中被清除。但是，如果在 `CBC` 或 `OST` 被置位时清除中断标志，则会生成另一个中断脉冲。清除所有标志位将防止进一步的中断。此位通过向 `TZCLR` 寄存器写入适当的值来清除。

### **Digital comparator output A event 1 interrupt enable (DCAEVT1), Digital comparator output A event 2 interrupt enable (DCAEVT2), Digital comparator output B event 1 interrupt enable (DCBEVT1), Digital comparator output B event 2 interrupt enable (DCBEVT2)** — 启用数字比较器输出 `off`（默认）| `on`

当数字比较器输出 A 或数字比较器输出 B 的事件 1 或 2 发生时生成中断。

**注意**

这些参数仅适用于特定的 C28x 处理器。

### **Clear cycle-by-cycle trip latch at** — 选择清除逐周期跳闸锁存器 `Counter equals to zero (CTR=Zero)`（默认）| `Counter equals to period (CTR=Prd)` | `Counter equals to zero or period (CTR=Zero or CTR=Prd)` | `Latch not cleared`

选择事件选项以清除逐周期跳闸锁存器。

#### 依赖关系

- 要启用此参数，请将 trip zone source 参数设置为 **Input port** 或将 trip zone source 设置为 **Specify via dialog**。然后启用 **Enable cyclic trip-zine#** 或 **Enable cyclic digital compare A event 2 (DCAEVT2), Enable cyclic digital compare B event 2 (DCBEVT2)**。
- 这些参数仅适用于特定的 C28x 处理器。

### **ePWM#A forced (TZ) to, ePWM#B forced (TZ) to, ePWM#A forced (DCAEVT#) to, ePWM#B forced (DCBEVT#) to** — 确定在 ePWM 输出上要考虑的动作 `No action`（默认）| `High` | `Low` | `Hi-Z (High Impedance)`

这些参数决定在触发区条件下可对 ePWM 输出执行的动作。触发区模块会覆盖并强制将
ePWM#A 和/或 ePWM#B（TZ 或 DCAEVTx）输出设置为以下状态之一：
`No action`
（默认）、`High`、
`Low` 或 `Hi-Z (High
Impedance)`。

### Digital Compare

### **Source for digital compare A high signal (DCAH), Source for digital compare B high signal (DCBH)** — 数字比较高信号源 `GPTRIP1SEL/(TZ1) for DCAH/GPTRIP1SEL/(TZ1) for DCBH`（默认）| `GPTRIP3SEL/(TZ3) for DCAH/GPTRIP7SEL for DCBH` | `...`

选择适当的 TZ 或 COMP 信号，为数字比较 A/B 高信号生成高逻辑值。使用 **Digital
compare output A event # selection**、**Digital
compare output B event # selection**、**DCAEVT#
source select**、**DCBEVT# source select**
参数来确定 DCAH/DCBH 对 DCAEVT# 和 DCBEVT# 的影响。

每个数字比较（DC）子模块从 GPIO MUX 接收三个 TZ 信号（TZ1 到
TZ3），并从 COMP 接收三个 COMP 信号（仅适用于特定的 C28x 器件）。这些信号表示
ePWM 子模块外部的故障或触发条件。使用此选项卡中的设置来输出响应那些外部
信号的特定 DC 事件。这些 DC 事件直接馈入时基、触发区和事件触发子模块。

有关更多信息，请参阅 *Piccolo Enhanced Pulse
Width Modulator (ePWM) Module Reference Guide* 的 *Digital Compare (DC)
Submodule* 部分。

### **Source for digital compare A low signal (DCAL), Source for digital compare B low signal (DCBL)** — 数字比较低信号源 `GPTRIP1SEL/(TZ1) for DCAL/GPTRIP1SEL/(TZ1) for DCBL`（默认）| `TRIPIN1(ECCDBLERR) for DCAL/Select From DCBLTRIPSEL for DCBL` | `...`

选择适当的 TZ 或 COMP 信号，为数字比较 A/B 低信号生成低逻辑值。使用 **Digital
compare output A event # selection**、**Digital
compare output B event # selection**、**DCAEVT#
source select**、**DCBEVT# source select**
选项来确定 DCAL/DCBL 对 DCAEVT# 和 DCBEVT# 的影响。

### **Digital compare output A event # selection (DCAEVT#), Digital Compare output B event # selection (DCBEVT#)** — 限定生成 DC 事件的信号 `Event disabled`（默认）| `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

限定生成 DC 事件（例如 DCAEVT# 或
DCBEVT#）的信号。要禁用此功能，请选择 `Event
disabled` 选项。根据信号的源选择，可以触发该事件。事件选择可以基于
High、Low 和 Don't care 条件的组合。

### **DCAEVT# source select, DCBEVT# source select** — 数字比较事件源 `Event disabled`（默认）| `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

此参数控制触发 DC
事件的两个独立方面：

- 触发滤波或未滤波的 DC 事件

  - DC 事件可以是滤波或未滤波的信号，
    可以传递到其他子模块。
  - 配置 DCACTL
    和 DCBCTL 寄存器中的 EVT1SRCSEL 和 EVT2SRCSEL。
  - 以 `DCAEVT# with
    sync` 或 `DCAEVT# with
    async` 开头的选项不对 DC
    事件应用滤波。合格的 DC 信号直接传递以触发 DC
    事件，不进行任何滤波。
  - 以 `DCEVTFILT
    sync` 开头的选项对 DC 事件应用滤波。
    合格信号在触发 DC 事件之前通过滤波电路。有关更多信息，请参阅
    *Piccolo Enhanced Pulse Width Modulator
    (ePWM) Module Reference Guide* 的
    *Event Filtering* 部分。
- 同步或异步触发 DC 事件

  - DC 事件信号可以与 TBCLK 同步，或
    保持异步。
  - 配置 DCACTL
    和 DCBCTL 寄存器中的 EVT1SRCSEL 和 EVT2SRCSEL。
  - 以 `async` 结尾的选项
    异步触发 DC 事件。当合格或
    滤波信号存在时，DC 子模块立即触发 DC
    事件。
  - 以 `sync` 结尾的选项
    同步触发 DC 事件。一旦合格或
    滤波信号存在，DC 子模块将与 TBCLK 信号同步触发 DC
    事件。

    **注意**

    上述字段仅在
    相应的 DCAEVT# 启用时出现。

**注意**

当您为 **DCAEVTX source select** 或 **DCBEVTX
source select** 选择 `DCEVTFILT with
sync` 或 `DCEVTFILT with async`
时，以下字段会出现。

有关以下参数的更多详细信息，请参阅 Enhanced Pulse Width Modulator (ePWM) Module Reference
Guide 的技术参考手册。

### **Pulse select** — 指示消隐窗口，用于滤除事件发生 `Counter equals to zero (CTR=Zero)`（默认）| `Counter equals to period (CTR=PRD)`

消隐窗口在激活期间滤除
信号上的事件发生。将此参数设置为与 CTR = PRD 脉冲或 CTR = Zero 脉冲对齐。

### **Blanking window inverted** — 指示反转消隐窗口 `off`（默认）| `on`

选择此参数以启用反转消隐窗口。

### **Blanking window offset** — 指示偏移消隐窗口 `0`（默认）

用于确定 **Pulse select** 事件之后开始消隐窗口
以进行滤波的点的 TBCLK 周期数

### **Blanking window width** — 指示消隐窗口持续时间 `0`（默认）

用于确定 **Pulse select** 事件之后开始消隐窗口
以进行滤波的点的 TBCLK 周期数。

消隐窗口将根据 **Pulse
select** 事件的发生开始，并按照 **Blanking offset window**
附加 TBCLK 周期作为偏移。

在消隐窗口期间，所有事件都被忽略。事件可以在消隐窗口应用之前和之后
触发同步或异步事件。

### **Filter output DCEVTFILT** — 指示滤波器的源选择 `Filtered version of DCAEVT1 (DCAEVT1FILT)`（默认）| `Filtered version of DCAEVT2 (DCAEVT2FILT)` | `Filtered version of DCBEVT1 (DCBEVT1FILT)` | `Filtered version of DCBEVT2 (DCBEVT2FILT)`

使用此参数选择用于滤波的源，从而形成
DCEVTFILT 信号。

### **Enable counter capture** — 指示计数器捕获 `off`（默认）| `on`

启用此选项允许捕获触发
事件的 TBCTR 值。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

生成增强型脉宽调制（ePWM）波形

配置 Type 1 至 Type 4 增强型脉宽调制器（ePWM）以生成 PWM
波形。可用的 ePWM 模块数量（ePWM1-ePWM16）因 C2000
处理器而异。有关 ePWM 类型的更多信息，请参阅 C2000 Real-Time Control
Peripheral Reference Guide。

使用此模块生成 ePWM 波形。C28x 器件上有多个 ePWM 模块
可用。每个模块生成两个 PWM 信号 ePWMA 和 ePWMB。

当您启用高分辨率脉宽调制器（HRPWM）时，ePWM 模块使用
比例因子优化（SFO）软件库。SFO 库可以
“动态确定每个系统
时钟（SYSCLKOUT）周期的微边沿定位器（MEP）步数。”有关更多信息，请参阅 `TMS320x28xx, 28xxx
High-Resolution Pulse Width Modulator (HRPWM) Reference Guide`，可在
Texas Instruments® 网站上获取。

此模块通用于各种 C28x 器件。可用参数因您选择模块的
库而异。模块右上角的蓝色标签显示
系列。由于该模块是不同器件上可用功能的超集，并非所有参数都与您的模型相关。
