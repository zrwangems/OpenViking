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

当 PWM 分辨率过低时，启用 C28044 数字信号控制器上的全部 16 个高分辨率 PWM 模块 (HRPWM)。

**注意**

仅当使用 C28044 处理器时选择此参数。

例如，Spectrum Digital eZdsp™ F28044 板的系统时钟为 100 MHz（200 kHz 开关频率）。在这些频率下，传统 PWM 分辨率过低，约为 9 bits 或 10 bits。相比之下，同一板卡的 HRPWM 分辨率为 14.8 bits。

#### 依赖关系

启用此参数时：

- 使用 ePWMA 选项卡下的 HRPWM 参数进行其他配置更改。
- ePWMB 选项卡下的大部分配置参数不可用。
- 您的模型最多可包含 16 个 C280x/C2803x/C2833x ePWM 模块，前提是为每个模块配置单独的模块。（例如，**模块** 为 `ePWM1`、`ePWM2` 等。）
- 仅当使用 C28044 处理器时选择此参数。要为其他处理器启用 HRPWM，请先查阅处理器的 Texas Instruments 文档以确定可用的 HRPWM 模块数量。然后使用 ePWMA 选项卡下的 HRPWM 参数启用并配置 HRPWM。

### **模块** — 指示要使用的 ePWM 模块 `ePWM1`（默认）| `ePWM2` | `ePWM3` | `…`

选择适当的 ePWM 模块。`ePWMx`，其中 *x* 可以是 1、2、3……。

**注意**

可用的模块数量因处理器而异。

### **ePWMLink TBPRD** — 指示 ePWM 模块的 TBPRD 链接 `Not Linked`（默认）| `ePWM2` | `ePWM3` | `…`

选择要将当前 ePWM 模块链接到的 ePWM 模块以设置定时器周期。链接两个模块后，被链接 ePWM 模块中的定时器周期值将设置当前模块中 **定时器周期** 参数的值。当您选择链接到另一个 ePWM 模块时，**定时器周期单位**、**通过以下方式指定定时器周期** 和 **定时器周期** 参数不会显示。

但是，当您将 ePWM 模块链接到模型中不存在的模块时，链接无效。

**注意**

此参数仅适用于某些 TI C2000™ 处理器。

### **定时器周期单位** — 指示时间段单位 `Clock cycles`（默认）| `Seconds`

指定 **定时器周期** 或 **定时器初始周期** 参数的单位为 `Clock cycles` 或 `Seconds`。当该参数设置为 `Seconds` 时，软件会将 **定时器周期** 或 **定时器初始周期** 从以秒为单位的值转换为以时钟周期为单位的值。为获得最佳结果，请选择 `Clock cycles`。这样做可减少计算次数和舍入误差。

#### 依赖关系

- 如果将 **定时器周期单位** 设置为 `Seconds`，请启用对浮点数的支持。在模型窗口中，选择 **建模 > 模型设置**。
- 在“配置参数”对话框中，选择 **代码生成 > 接口**。在 **软件环境** 下，启用 **浮点数**。

### **通过以下方式指定定时器周期** — 配置定时器周期值的来源 `Specify via dialog`（默认）| `Input port`

当您选择 `Input port` 时，**定时器周期** 参数将变为 **定时器初始周期**，并在模块上创建一个定时器周期输入端口 **T**。

### **定时器周期** — 指示 ePWM 计数器的周期 `64000`（默认）

设置 ePWM 计数器波形的周期。生成的 ePWM 波形周期取决于 **ePWMx** 选项卡上 **当计数器=时的操作** 参数的设置。

启用 HRPWM 后，您可以输入高精度浮点值。时基周期高分辨率寄存器 (TBPRDHR) 存储定时器周期值的高分辨率部分。

定时器周期根据 **计数模式** 选择和 **定时器周期单位** 计算，如下所示。

| 计数模式 | 定时器周期单位 | 计算 | 示例 |
| --- | --- | --- | --- |
| Up or Down | Clock cycles | 在时钟周期中输入的值用于计算 ePWM 定时器寄存器的时间基准周期 (TBPRD)。ePWM 定时器周期 TCTR = (TBPRD + 1) \* TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。 | 对于 ePWM 时钟 (EPWMCLK) 频率 = 200 MHz 且 TBCLK = 5 ns。EPWMCLK 将等于 SYSCLKOUT 或 SYSCLKOUT/2，具体取决于 **EPWM 时钟分频器 (EPWMCLKDIV)** 参数设置。当定时器周期以时钟周期输入时，TBPRD = 9999，ePWM 定时器周期计算为 TCTR = 50 µs。对于 **ePWMx** 选项卡上的默认操作设置，ePWM 周期 = 50 µs。 |
| Seconds | 以秒为单位输入的值用于计算 ePWM 定时器寄存器的时间基准周期 (TBPRD)。寄存器中输入的 TBPRD 值为 TBPRD = (TCTR / TBCLK) – 1。其中，TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。对于 **ePWMx** 选项卡上的默认操作设置，ePWM 周期与输入的定时器周期（以秒为单位）相同。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以秒输入时，TCTR = 50 µs，时间基准周期计算为 TBPRD = 9999。对于 **ePWMx** 选项卡中的默认操作设置，ePWM 周期 = 50 µs。 |
| Up-Down | Clock cycles | 在时钟周期中输入的值用于计算 ePWM 定时器寄存器的时间基准周期 (TBPRD)。ePWM 定时器周期 TCTR = 2 \* TBPRD \* TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以时钟周期输入时，TBPRD = 10000，ePWM 定时器周期计算为 TCTR = 100 µs。对于 **ePWMx** 选项卡上的默认操作设置，ePWM 周期 = 100 µs。 |
| Seconds | 以秒为单位输入的值用于计算 ePWM 定时器寄存器的时间基准周期 (TBPRD)。寄存器中输入的 TBPRD 值为 TBPRD = TCTR / TBCLK。其中 TCTR 是以秒为单位的定时器周期，TBCLK 是时基时钟。对于 **ePWMx** 选项卡上的默认操作设置，ePWM 周期是输入的定时器周期（以秒为单位）的两倍。 | 对于 EPWMCLK 频率 = 200 MHz 且 TBCLK = 5 ns。当定时器周期以秒输入时，TCTR = 50 µs，时间基准周期计算为 TBPRD = 10000。对于 **ePWMx** 选项卡上的默认操作设置，ePWM 周期 = 100 µs。 |

### **定时器初始周期** — 指示波形的初始 ePWM 周期 `64000`（默认）| `0` | `...`

从 PWM 外设开始运行到 ePWM 输入端口 **T** 接收到新的周期值为止，波形的初始周期。使用 **定时器周期单位** 以时钟周期或秒为单位测量周期。定时器周期的计算方式与 **定时器周期** 参数类似。

#### 依赖关系

要启用此参数，请将 **通过以下方式指定定时器周期** 参数设置为 `Input port`。

### **活动周期寄存器加载选项 (PRDLD)** — 计数器周期寄存器重新加载时的事件 `Counter equals to zero`（默认）| `Counter equals to zero or SYNC event` | `SYNC event` | `Immediate without using shadow`

此参数提供了一个选项，用于选择适当的事件以新值更新时间段寄存器。

- `Counter equals to zero` - 当计数器的值为 0 时，计数器周期刷新。
- `Counter equals to zero or SYNC event` - 当计数器为 0 或存在同步事件时。
- `SYNC event` - 参数处于同步状态。
- `Immediate without using shadow` - 计数器周期立即刷新。

### **计数模式** — 指示 ePWM 计数器的计数模式 `Up-Down`（默认）| `Up` | `Down`

指定计数模式。此 PWM 模块可以三种不同的计数模式运行：`Up`、`Down` 和 `Up-Down`。

此图显示了与这三种模式对应的波形：

#### 依赖关系

`Down` 选项与 HRPWM 不兼容。为避免构建模型时出错，请不要将 **计数模式** 参数设置为 `Down` 并同时选择 **启用 HRPWM (周期)** 参数。

### **同步操作** — 指定相位偏移的来源 `Disable`（默认）| `Set counter to phase value specified via dialog` | `Set counter to phase value specified via input port`

指定要应用于来自 **SYNC** 输入端口的时基同步输入信号 EPWMxSYNCI 的相位偏移来源。

- `Set counter to phase value specified via dialog` - 指定此选项以创建 **相位偏移值** 参数。

  **注意**

  - ePWM 模块期望相位值在 0 到 360 deg 范围内，并按时钟周期缩放作为相位值的输入。因此，对于负值，您需要加上 360 deg 使其进入 0 到 360 deg 的相位范围。例如，对于 -90 deg 值，您必须提供 (360 - 90) = 270 deg 并按时钟周期缩放作为输入。
  - 对于大于 360 deg 的任何值，您需要考虑将值环绕到 0 到 360 deg 范围的逻辑。例如，120 + (360 - 90) = 390 应环绕为 (390 - 360) = 30 deg，然后再按时钟周期缩放并将其作为输入提供给 ePWM。
- `Set counter to phase value specified via input port` - 指定此选项以在模块上创建相位输入端口 **PHS**。
- `Disable` - 指定此选项以防止将相位偏移应用于 TB 模块。

### **相位同步后的计数方向** — 相位同步后的计数器方向 `Count down after sync`（默认）| `Count up after sync`

配置定时器在同步后向上或向下计数。此参数对应于时基控制寄存器 (TBCTL) 的相位方向 (PHSDIR) 字段。

#### 依赖关系

当 **计数模式** 为 `Up-Down` 且 **同步操作** 为 `Set counter to phase value specified via dialog` 或 `Input port` 时，将显示此参数。

### **相位偏移值 (TBPHS)** — 指定相位偏移值 (TBPHS) `0`（默认）

指定的偏移值在同步事件时加载到时基计数器中。

要启用此参数，请在 **同步操作** 参数中选择 `Set counter to phase value specified via dialog`。

在 **TBCLK** 周期中输入 `Phase offset value (TBPHS)`，范围从 0 到 65535。使用 HRPWM 时，您可以输入十进制值。

**注意**

- ePWM 模块期望相位值在 0 到 360 degrees 范围内，并按时钟周期缩放。对于负值，您需要加上 360 degrees 使其进入 0 到 360 degrees 的相位范围。例如，对于 -90 degrees 值，您必须提供 (360 - 90) = 270 degrees 并按时钟周期缩放作为输入。
- 对于大于 360 degrees 的任何值，您需要考虑将值环绕到 0 到 360 degrees 范围的逻辑。例如，120 + (360 - 90) = 390 应环绕为 (390 - 360) = 30 degrees，然后再按时钟周期缩放并将其作为输入提供。

此参数对应于时基相位寄存器 (TBPHS)。

### **通过输入端口指定软件同步 (SWFSYNC)** — 指示相位偏移值 `off`（默认）| `on`

为时基同步输入信号 EPWMxSYNCI 创建输入端口 **SYNC**。选择此参数可通过以菊花链方式连接多个时基 (TB) 子模块，实现多个 ePWM 模块之间的精确同步。

### **启用数字比较 A 事件1 同步 (DCAEVT1)** — 基于 DCAEVT1 数字比较事件同步 ePWM 时间 `off`（默认）| `on`

选择此参数可将此 PWM 模块同步到另一个 PWM 模块的时基。使用 **相位偏移值** 微调两个模块之间的同步。启用 HRPWM 会禁用此选项。

**注意**

此参数仅适用于特定的 `C28x` 设备。

### **启用数字比较 B 事件1 同步 (DCBEVT1)** — 基于 DCBEVT1 数字比较事件同步 ePWM 时间 `off`（默认）| `on`

选择此参数可将此 PWM 模块同步到另一个 PWM 模块的时基。使用 **相位偏移值** 微调两个模块之间的同步。此选项与 `HRPWM` 不兼容。启用 `HRPWM` 会禁用此选项。

**注意**

此参数仅适用于特定的 `C28x` 设备。

### **Synchronization output (SYNCO)** — 用于生成时基同步输出信号的事件 `Disable`（默认） | `Pass through (EPWMxSYNCI or SWFSYNC)` | `Counter equals to zero (CTR=Zero)` | `Counter equals to compare B (CTR=CMPB)` | `Counter equals to compare C (CTR=CMPC)` | `Counter equals to compare D (CTR=CMPD)` | `Enable DCBEVT1 sync event to SYNCO signal` | `Enable DCAEVT1 sync event to SYNCO signal` | `Enable counter equals to compare D (CTR=CMPD) event to set SYNCO signal` | `Enable counter equals to compare C (CTR=CMPC) event to set SYNCO signal` | `Enable counter equals to compare B (CTR=CMPB) event to set SYNCO signal` | `Enable counter equals to zero (CTR=ZERO) event to set SYNCO signal` | `Enable SWFSYNC event to set SYNCO signal`

时基计数器同步允许提高 ePWM 模块同步的灵活性。时钟同步方案允许 ePWM 模块在需要时作为单个系统运行。此外，该同步方案可以扩展到捕获外设子模块 (eCAP)。在 Type 4 ePWM 中，有两种可用的时基计数器同步方案。有关更多信息，请参见 Time-Base Counter Synchronization。

您可以在配置参数中配置其他 SYNCO 选项。有关更多信息，请参见 C28x-ePWM。

此参数对应于时基控制寄存器 (TBCTL) 中的 SYNCOSEL 字段。

**注意**

同步输出 (SYNCO) 的参数因所选处理器而异。

以下参数仅适用于 `F2837x`、`F2807x`、`F28004x` 和特定 `C28x` 处理器。

- `Pass through (EPWMxSYNCI or SWFSYNC)` — 分别为同步输入脉冲或软件强制同步脉冲。您可以使用此选项通过菊花链连接多个时基 (TB) 子模块，以实现多个 ePWM 模块之间的精确同步。
- `Counter equals to zero (CTR=Zero)` — 时基计数器等于零 (TBCTR = 0x0000)
- `Counter equals to compare B (CTR=CMPB)` — 时基计数器等于计数器比较 B (TBCTR = CMPB)
- `Counter equals to compare C (CTR=CMPC)` — 时基计数器等于计数器比较 C (TBCTR = CMPC)
- `Counter equals to compare D (CTR=CMPD)` — 时基计数器等于计数器比较 D (TBCTR = CMPD)
- `Disable` — 禁用 EPWMxSYNCO 输出（默认）

以下参数仅特定于 F2838x、F28002x 和 F28003x 处理器。

- `Enable DCBEVT1 sync event to SYNCO signal` - 选择将数字比较事件 B 同步到同步输出。
- `Enable DCAEVT1 sync event to SYNCO signal` - 选择将数字比较事件 A 同步到同步输出。
- `Enable counter equals to compare D (CTR=CMPD) event to set SYNCO signal` - 使计数器等于比较 D (CTR=CMPD) 事件设置 SYNCO 信号
- `Enable counter equals to compare C (CTR=CMPC) event to set SYNCO signal` - 使计数器等于比较 C (CTR=CMPC) 事件设置 SYNCO 信号
- `Enable counter equals to compare B (CTR=CMPB) event to set SYNCO signal` - 使计数器等于比较 B (CTR=CMPB) 事件设置 SYNCO 信号
- `Enable counter equals to zero (CTR=ZERO) event to set SYNCO signal` - 使计数器等于零 (CTR=ZERO) 事件设置 SYNCO 信号
- `Enable SWFSYNC event to set SYNCO signal` - 使软件强制同步脉冲 (SWFSYNC) 事件设置 SYNCO 信号

### **Peripheral synchronization event (PWMSYNCSEL)** — 时基计数器外设同步 `Counter equals to period (CTR=PRD)`（默认） | `Counter equals to zero (CTR=Zero)` | `Counter is incrementing and equals to compare C register (CTRU=CMPC)` | `Counter is decrementing and equals to compare C register (CTRD=CMPC)` | `Counter is incrementing and equals to compare D register (CTRU=CMPD)` | `Counter is decrementing and equals to compare D register (CTRD=CMPD)`

每个 ePWM 模块都有一个外设同步输出 (SYNCPER)。此输出信号用于将 CMPSS 同步到 EPWM。有关更多信息，请参见 Time-Base Counter Peripheral Synchronization。

**注意**

此参数仅适用于某些特定 `C28x` 处理器。

### **Time base clock (TBCLK) prescaler divider** — 对应 CLKDIV 的时基时钟 (TBCLK) 预分频器分频值 `1`（默认） | `2` | `4` | `…`

使用 **Time base clock (TBCLK) prescaler divider** (CLKDIV) 和 **High speed time base clock (HSPCLKDIV) prescaler divider** (HSPCLKDIV) 为 ePWM 模块配置时基时钟速度 (TBCLK)。使用以下公式计算 TBCLK：

TBCLK in Hz = PWM clock in Hz/(HSPCLKDIV \* CLKDIV)

例如，CLKDIV 和 HSPCLKDIV 的默认值均为 1，PWM 时钟的默认频率为 100 MHz，因此：

TBCLK in Hz = 100 MHz/(1 \* 1) = 100 MHz

TBCLK in seconds = 1/TBCLK in Hz = 1/100 MHz = 0.01 μs

**Time base clock (TBCLK) prescaler divider** 的选项为：`1`、`2`、`4`、`8`、`16`、`32`、`64` 和 `128`。

**Time block clock (TBCLK) prescaler divider** 参数对应于时基控制寄存器 (TBCTL) 的 CLKDIV 字段。

PWM 时钟是 SYSCLKOUT 或使用 PWM 时钟分频器从 SYSCLKOUT 派生的时钟。对于少数 TI C2000 处理器，有一个 PWM 时钟分频器，它分频 SYSCLKOUT 以派生 PWM 模块时钟。有关更多详细信息，请查看处理器的技术参考手册。

SYSCLKOUT 的频率取决于振荡器频率和基于 PLL 的时钟模块的配置。更改 SYSCLOCKOUT 的值会影响所有 ePWM 模块的时序。如果处理器中有可用的 PWM 时钟预分频器，更改其值也会影响 PWM 时序。

### **High speed time base clock (HSPCLKDIV) prescaler divider** — 高速时基时钟 (HSPCLKDIV) 预分频器分频值 `1`（默认） | `2` | `4` | `...`

**High speed time base clock (HSPCLKDIV) prescaler divider** 的选项为：`1`、`2`、`4`、`6`、`8`、`10`、`12` 和 `14`。

选择 **Enable high resolution PWM (HRPWM – period)** 会将该参数的值设置为 `1`。

此参数对应于时基控制寄存器 (TBCTL) 的 HSPCLKDIV 字段。

### **Enable swap module A and B** — 交换模块 A 和 B 的输出信号 `off`（默认） | `on`

交换 ePWMA 和 ePWMB 输出。选择此参数时，模块在 ePWMB 输出上输出 ePWMA 信号，并在 ePWMA 输出上输出 ePWMB 信号。

此参数设置 HRPWM 配置寄存器 (HRCNFG) 中的 SWAPB 字段。此选项适用于支持 HRPMW 的 ePWM，因为它使用 HRCNFG 寄存器。

**注意**

此参数仅适用于特定 `C28x` 器件。

### ePWMA 和 ePWMB

您可以在 ePWMA/ePWMB 选项卡以及 Counter compare 选项卡中执行波形生成配置。

ePWM 硬件模块可以为 A 和 B 通道生成波形，随后通过死区模块和 HRPWM 模块进行波形生成。

在波形生成期间，您可以为 ePWMA 和 ePWMB 生成波形，但这些波形选项可以被死区配置中选择的选项覆盖。例如，您可以选择不在波形生成模块中配置 eWPMB，而是使用 eWPMA 波形为 ePWMA 和 ePWMB 通道创建死区输出。

### **Enable ePWM#x** — 使能 ePWMx 输出信号 `off`（默认） | `on`

为 **General** 选项卡上选择的 ePWM 模块使能 ePWMA 和/或 ePWMB 输出信号。在此情况下，# 表示 ePWM 模块，x 表示 A 或 B。默认情况下，**Enable ePWM#A** 已启用，**Enable ePWM#B** 已禁用。

每个 ePWM 模块有两个输出：ePWMA 和 ePWMB。ePWMA 输出选项卡和 ePWMB 输出选项卡包含相同的设置，尽管默认值在某些情况下有所不同。

#### 依赖关系

当您选择 **Enable ePWM#A** 或 **Enable ePWM#B** 时，请通过浏览到 **Configuration Parameters** > **Code Generation** > **Interface** > **Software Environment** 来启用对浮点数的支持。

### **Action when counter=ZERO, Action when counter=period (PRD), Action when counter=CMPA on up-count (CAU), Action when counter=CMPA on down-count (CAD), Action when counter=CMPB on up-count (CBU), Action when counter=CMPB on down-count (CBD)** — 确定动作限定器 (AQ) 子模块行为 `Set`（默认）

**ePWMA output** 和 **ePWMB output** 选项卡上的这组参数确定动作限定器 (AQ) 子模块的行为。AQ 模块确定哪些事件被转换为各种动作类型之一，从而产生 ePWM#A 和 ePWM#B 输出信号所需的开关波形。

这些参数可以指定为 `Do nothing`、`Clear`、`Set` 或 `Toggle`。

默认值在 **ePWMA** 和 **ePWMB** 选项卡之间有所不同。

此表显示当您将 **Counting mode** 设置为 `Up` 或 `Up-Down` 时，每个选项卡的默认值：

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Set | Clear |
| period (PRD) | Clear | Set |
| CMPA on up-count (CAU) | Clear | Set |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on up-count (CBU) | Do nothing | Clear |
| CMPB on down-count (CBD) | Do nothing | Set |

此表显示当您将 **Counting mode** 设置为 `Down` 时，每个选项卡的默认值：

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Do nothing | Do nothing |
| period (PRD) | Clear | Clear |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on down-count (CBD) | Do nothing | Set |

有关 AQ 子模块的详细讨论，请参阅 Texas Instruments 网站上提供的 *TMS320x280x Enhanced Pulse Width Modulator (ePWM) Module Reference Guide* (SPRU791)。

### **Add continuous software force input port, Continuous software force logic, Reload condition for software force** — 确定动作限定器 (AQ) 子模块如何处理 S/W 强制事件 `Load on counter equals to zero (CTR=Zero)`（默认）

这些参数确定动作限定器 (AQ) 子模块如何处理 S/W 强制事件，这是一种由软件 (CPU) 通过控制寄存器位发起的异步事件。

**Compare value reload condition** 确定是否以及何时从影子寄存器重载动作限定器 S/W 强制寄存器。您可以指定以下之一：`Load on counter equals to zero (CTR=Zero)`（默认）、`Load on counter equals to period (CTR=PRD)`、`Load on either` 和 `Freeze`。

**Add continuous software force input port** 创建一个输入端口 **SFA**，您可以使用它来控制软件强制初始逻辑。将以下值之一作为无符号整数数据类型发送到 **SFA**：

- 0 = `Forcing disable`：Do nothing（默认）。
- 1 = `Forcing low`：Clear low
- 2 = `Forcing high`：Set high
- 3 = `Forcing disable`：Do nothing

**Continuous software force logic** - 如果您没有创建 **SFA** 输入端口，则可以使用它来选择要应用的软件强制初始逻辑类型。您可以指定以下之一：

- `Forcing disable`：Do nothing（默认）。
- `Forcing low`：Clear low
- `Forcing high`：Set high

**Reload condition for software force**

您可以指定以下之一：`Counter equals to zero (CTR=Zero)`（默认）、`Counter equals to period (CTR=PRD)`、`Either period or zero` 和 `Immediate`。

### **Inverted version of ePWM#A** — 反转 ePWM#A 信号 `off`（默认） | `on`

反转 ePWM#A 信号，并在 ePWM#B 输出上输出。

此参数设置 HRPWM 配置寄存器 (HRCNFG) 中的 SELOUTB 字段，并且适用于支持 HRPWM 的 ePWM，因为它使用 HRCNFG 寄存器。

**注意**

此参数仅适用于具有 HRPWM 子模块的 ePWM 模块。启用此参数会反转 ePWM#B，无论模块中是否启用了 HRPWM。

### **Enable high resolution PWM (HRPWM)** — 使能高分辨率 PWM 设置 `off`（默认） | `on`

#### 依赖关系

- 此参数仅适用于 C280x 和 C2833x 处理器的 **ePWMx** 选项卡，以及其他处理器的 **HRPWM** 选项卡。有关更多信息，请参阅 HRPWM 选项卡部分。
- 类似地，参数如 **High resolution PWM (HRPWM) loading mode**、**High resolution PWM (HRPWM) control mode**、**High resolution PWM (HRPWM) edge control mode** 以及 **Use scale factor optimizer (SFO) software** 功能，在 C280x 和 C2833x 处理器的 **ePWMx** 选项卡中以及其他处理器的 **HRPWM** 选项卡中可用。有关更多信息，请参阅 HRPWM 选项卡部分。

### 计数器比较

### **ePWMLink CMPx** — ePWM 模块的链接 `Not Linked`（默认） | `ePWM1` | `ePWM2` | `...`

在 ePWMx 中，其中 x 的范围为 1 到 12

选择一个 ePWM 模块，您希望将当前 ePWM 模块的计数值链接到该模块。在此情况下，对于 CMPx，x 表示 A、B、C 或 D。当您将一个 ePWM 模块的计数值与另一个模块链接时，链接的 ePWM 模块的 **CMPx value** 将用于当前模块。当您选择另一个 ePWM 模块进行链接时，**CMPx**、**Specify CMPx via** 和 **CMPx value** 参数不会出现。

但是，当您将 ePWM 模块链接到模型中不存在的模块时，链接无效。

**注意**

此参数仅适用于某些 TI 的 C2000 处理器。

### **CMPx Units** — 比较寄存器使用的单位 `Clock cycles`（默认） | `Percentages`

四个比较寄存器 CMPA、CMPB、CMPC 和 CMPD 与时基计数器值进行比较，以生成相应事件。CMPA 和 CMPB 事件用于通过在 **ePWMA** 和 **ePWMB** 选项卡上选择适当的动作来控制 PWM 占空比。这些事件还可用于生成到 CPU 的中断和/或到 ADC 的转换启动脉冲。您可以参考 **Event Trigger** 选项卡来选择要触发的事件。

比较寄存器 **CMPC** 和 **CMPD** 仅存在于最新处理器中。

**注意**

- 术语 *clock cycles* 指处理器上的时基时钟。有关时基时钟速度计算的说明，请参见 **TB clock prescaler divider** 主题。
- `Percentages` 在生成的代码中使用额外的计算时间，并可能降低结果的精度。

#### 依赖关系

如果您将 ***CMPx units*** 设置为 `Percentages`，请通过浏览到 **Configuration Parameters** > **Code Generation** > **Interface** > **Software Environment** 来启用对浮点数的支持。在此情况下，x 表示 A、B、C 或 D。

### **Specify CMPx Via** — 脉冲宽度源 `Specify via dialog`（默认） | `Input port`

指定脉冲宽度的源。如果您选择 `Specify via dialog`（默认），请输入 **CMPx value** 参数的值。如果您选择 `Input port`，模块将在模块上创建一个名为 WA、WB、WC 或 WD 的新输入端口。如果您选择 `Input port`，请确保设置 **CMPx initial value** 参数。在此情况下，x 表示 A、B、C 或 D。

### **CMPx Value/CMPx Initial Value** — 脉冲宽度值 `32000`（默认）

当您将 **CMPx source** 设置为 `Specify via dialog` 时，会出现 **CMPx Value** 字段。当您将 **CMPx source** 设置为 `Input port` 时，会出现 **CMPx Initial Value** 字段。输入一个值，以 **CMPx units** 中指定的单位指定脉冲宽度。在此情况下，x 表示 A、B、C 或 D。

输入 PWM 外设启动运行时使用的 CMPA 或 CMPB 的初始脉冲宽度。后续输入到 **WA** 或 **WB** 端口会更改 CMPA 或 CMPB 脉冲宽度。

### **Reload for compare x Register (SHDWxMODE)** — 计数器周期被复位的时间 `Counter equals to zero (CTR=Zero)`（默认）| `Counter equals to period (CTR=PRD)` | `Counter equals to Zero or period (CTR=Zero or CTR=PRD)` | `...`

计数器周期被复位的时间。在此情况下，x 表示 A、B、C 或 D。

- `Counter equals to zero (CTR=Zero)` — 当计数器的值为 0 时刷新计数器周期。
- `Counter equals to period (CTR=PRD)` — 当计数器的值为 period 时刷新计数器周期。
- `Counter equals to zero or period (CTR=Zero or CTR=PRD)` — 当计数器的值为 0 或 period 时刷新计数器周期。
- `Freeze` — 当计数器的值为 freeze 时刷新计数器周期。
- `Counter equals to zero or SYNC event` — 当计数器的值为 0 或发生 SYNC 事件时刷新计数器周期。
- `Counter equals to period or SYNC event` — 当计数器的值为 0 或 SYNC 时刷新计数器周期。
- `Counter equals to zero or period or SYNC event` — 当计数器的值为 0 或 period 或 SYNC 时刷新计数器周期。
- `SYNC event` — 当计数器的值为 SYNC 时刷新计数器周期。
- `Immediate without using shadow` — 立即刷新计数器周期。

### 死区单元

### **Use deadband for ePWM#A, Use deadband for ePWM#B** — 启用死区区域 `off`（默认）| `on`

启用上升沿延迟或下降沿延迟周期的死区区域，使成对的 ePWM 输出信号之间没有信号重叠。确保在 ePWMx 选项卡上启用相应的 **ePWMx (x=A or B)**，以便为同一对象生成 DB。

### **Enable half-cycle clocking** — 使死区分辨率加倍 `off`（默认）| `on`

启用半周期时钟，使死区分辨率加倍。该选项以 TBCLK\*2 对死区计数器进行时钟，也就是说，它将时钟值（以秒为单位）除以 2，从而使频率加倍。

当您禁用此选项时，死区计数器使用全周期时钟 (TBCLK\*1)。

**注意**

此参数仅适用于特定 C28x 器件。

### **Deadband Polarity** — 死区时间处的 ePWM 输出状态 `Active high (AH)`（默认）| `Active low (AL)` | `Active high complementary (AHC)` | `Active low complementary (ALC)`

当仅为死区极性启用一个 ePWM 时，您将看到选项 `Positive` 和 `Negative`。

当为死区极性启用两个 ePWM 时，您将看到选项 `Active high (AH)`、`Active low (AL)`、`Active high complementary (AHC)` 或 `Active low complementary (ALC)`。

在死区时间，ePWMA 和 ePWMB 输出都必须设置为非活动状态。根据硬件设置，非活动状态可对应高逻辑值或低逻辑值。Active high 表示当 ePWM 输出设置为高逻辑值时系统处于活动状态。Active low 表示当 ePWM 输出设置为低逻辑值时系统处于活动状态。当 B 信号需要为 A 的反相信号时，使用 Complementary 选项。有关更多信息，请参阅处理器的 ePWM 技术参考指南。

此图显示了 0% < duty < 100% 的典型情况下的波形。

### **Signal source for rising edge (RED)** — 上升沿源 `ePWMxA`（默认）| `ePWMxB`

选择要施加上升沿延迟 (RED) 的信号源。您可以为上升沿选择 ePWMxA 或 ePWMxB。

### **Signal source for falling edge (FED)** — 下降沿源 `ePWMxA`（默认）| `ePWMxB`

选择要施加下降沿延迟 (FED) 的信号源。您可以为下降沿选择 ePWMxA 或 ePWMxB。

### **Deadband period units** — 指示死区周期单位 `Clock cycles`（默认）| `Seconds`

将 **Deadband period** 的单位指定为 `Clock cycles` 或 `Seconds`。当 **Deadband period units** 设置为 `Seconds` 时，软件会将 **Deadband period** 从以秒为单位的值转换为以时钟周期为单位的值。为获得最佳结果，请选择 `Clock cycles`。这样做可以减少计算和舍入误差。

#### 依赖关系

- 如果将 **Deadband period units** 设置为 `Seconds`，请启用对浮点数的支持。在模型窗口中，选择 **Simulation > Model Configuration Parameters**。

  在 Configuration Parameters 对话框中，选择 Code Generation > Interface。在 **Software Environment** 下，启用 **floating-point numbers**。
- 此参数仅适用于某些 TI 的 C2000™ 处理器。

### **Deadband period source** — 控制逻辑源 `Specify via dialog`（默认）| `Input port`

将 **Deadband period** 的源选择为 `Specify via dialog` 或 `Input port`。

### **Deadband Rising edge (RED) period (0-16383)** — RED 延迟时间值 `0`（默认）

在字段中输入的值指定以时基时钟为单位的死区延迟。

**Deadband rising edge period (0-16383)** 参数的结果取决于 `Deadband period units` 和 `Deadband period source`。

下表说明了基于所选 `deadband unit`、`deadband source` 和 `processor` 的 deadband rising edge period 结果。

| Deadband period units | Deadband period source | Deadband rising edge(RED) period |
| --- | --- | --- |
| Clock cycles | Specify via dialog | Deadband Rising edge (RED) period (0~16383) |
| Deadband Rising edge (RED) period (0~1023) |
| Clock cycles | Input port | Deadband Rising edge (RED) initial period (0~16383) |
| Deadband Rising edge (RED) initial period (0~1023) |
| Seconds | Specify via dialog | Deadband Rising edge (RED) period |
| Deadband Rising edge (RED) period |
| Seconds | Input port | Deadband Rising edge (RED) initial period: |
| Deadband Rising edge (RED) initial period: |

### **Deadband Falling edge (FED) period** — FED 延迟时间值 `0`（默认）

在字段中输入的值指定以时基时钟为单位的死区延迟。

参数 **Deadband falling edge period** 的结果取决于 `Deadband period units` 和 `Deadband period source`。**Deadband falling edge period** 的值与 **Deadband rising edge period** 类似。有关更多信息，请参阅 deadband rising edge (RED) period 参数。

### **Reload for DBRED register (SHDWDBRED), Reload for DBFED register (SHDWDBFED)** — 影子寄存器传送到活动寄存器的事件 `Immediate without using shadow`（默认）| `Freeze` | `Counter equals to zero (CTR=Zero)` | `Counter equals to period (CTR=PRD)` | `Counter equals to either zero or period (CTR=Zero or CTR=PRD)` | `...`

影子寄存器传送到活动寄存器且计数器周期被复位的事件。

- `Immediate without using shadow` — 立即刷新计数器周期。
- `Counter equals to zero (CTR=Zero)` — 当计数器的值为 0 时刷新计数器周期。
- `Counter equals to period (CTR=PRD)` — 当计数器的值为 period 时刷新计数器周期。
- `Counter equals to zero or period (CTR=Zero or CTR=PRD)` — 当计数器的值为 0 或 period 时刷新计数器周期。
- `Freeze` — 当计数器的值为 freeze 时刷新计数器周期。

#### 依赖关系

**SHDWDBRED** 和 **SHDWDBFED** 仅在选中 **Use deadband for ePWM#A** 或 **Use deadband for ePWM#B** 时可用。

### 事件触发

### **Enable ADC start of conversion for module A** — ADC 转换启动事件 `off`（默认）| `on`

当您选择此选项时，如果 **Start of conversion for module A event selection** 参数中选择的事件发生，则生成 ADC Start of Conversion Event (ePWMSOCxA)。

### **Number of event for start of conversion for Module A (SOCA) to be generated** — 事件启动编号 `First event`（默认）| `Second event` | `Third event` | `...`

当您选择 **Enable ADC start of conversion for module A** 时，此字段指定触发 Module A 的 ADC Start of Conversion (SOCA) 的事件编号。

`First event` 在每个事件触发 ADC start of conversion（默认）。`Second event` 每第二个事件触发 ADC start of conversion。`Third event` 每第三个事件触发 ADC start of conversion。

根据所选处理器，事件触发范围从 `First event` 到 `Fifteenth event`。

### **Start of conversion for module A event selection** — 指示触发 ADC start of conversion 事件的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认）| `Digital Compare Module A Event 1 start of conversion (DCAEVT1.soc)` | `...`

此参数指定触发 ADC start of conversion 事件的计数器匹配条件。选项包括：

- `Digital Compare Module A Event 1 start of conversion (DCAEVT1.soc)(For specific C28x devices only)` - 当 ePWM 断言 DCAEVT1 或 DCBEVT1 数字比较事件时。使用此功能可将所选 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 参数微调两个模块之间的同步。
- `Counter equals to zero (CTR=Zero)` - 当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` - 当 ePWM 计数器达到 period 值时。
- `Counter equals to zero or period (CTR=Zero or CTR=PRD)` - 当时基计数器达到零 (TBCTR = 0x0000) 或时基计数器达到 period (TBCTR = TBPRD) 时。
- `Counter is incrementing and equals to the compare x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `Counter is decrementing and equals to the compare x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### **Enable ADC start of conversion for module B** — ADC 转换启动事件 `off`（默认）| `on`

当您选择此选项时，如果 **Start of conversion for module B event selection** 参数中选择的事件发生，则生成 ADC Start of Conversion Event (ePWMSOCxB)。

### **Number of event for start of conversion for Module B (SOCB) to be generated** — 事件启动编号 `First event`（默认）| `Second event` | `Third event` | `...`

当您选择 **Enable ADC start of conversion for module B** 时，此字段指定触发 Module B 的 ADC Start of Conversion (SOCB) 的事件编号。

`First event` 在每个事件触发 ADC start of conversion（默认）。`Second event` 每第二个事件触发 ADC start of conversion。`Third event` 每第三个事件触发 ADC start of conversion。

根据所选处理器，事件触发范围从 `First event` 到 `Fifteenth event`。

### **Start of conversion for module B event selection** — 指示触发 ADC start of conversion 事件的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认） |

当您选择 **Enable ADC start of conversion for module B** 时，此字段指定触发 ADC start of conversion 事件的计数器匹配条件。选项包括：

- `Digital Compare Module B Event 1 start of conversion (DCBEVT1.soc) (For specific C28x devices only)` - 当 ePWM 断言 DCAEVT1 或 DCBEVT1 数字比较事件时。使用此功能可将所选 PWM 模块同步到另一个 PWM 模块的时基。使用 **Phase offset value** 微调两个模块之间的同步。
- `Counter equals to zero (CTR=Zero)` - 当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` - 当 ePWM 计数器达到 period 值时。
- `Counter equals to zero or period (CTR=Zero or CTR=PRD)` - 当时基计数器达到零 (TBCTR = 0x0000) 或时基计数器达到 period (TBCTR = TBPRD) 时。
- `Counter is incrementing and equals to the compare x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `Counter is decrementing and equals to the compare x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### **Enable ePWM interrupt** — 生成 ePWM 中断 `Disabled`（默认）| `Enabled`

选择此选项可根据 **Number of event for interrupt to be generated** 和 **Interrupt counter match event condition** 定义的不同事件生成 ePWM 中断。默认情况下，软件会清除（禁用）此选项。

### **Number of event for interrupt to be generated** — 指定触发 ePWM 中断的事件编号 `First event`（默认）| `Second event to fifteenth event`

当您选择 ***Enable ePWM interrupt*** 时，此字段指定触发 ePWM 中断的事件编号：`First event` 在每个事件触发 ePWM 中断（默认），`Second event` 每第二个事件触发 ePWM 中断，`Third event` 每第三个事件触发 ePWM 中断。

**注意**

根据所选处理器，事件触发范围从 `First event` 到 `Fifteenth event`。

### **Interrupt counter match event condition** — 指示触发 ePWM 中断的计数器匹配条件 `Counter equals to zero (CTR=Zero)`（默认）

当您选择 ***Enable ePWM interrupt*** 时，此字段指定触发 ePWM 中断的计数器匹配条件。选项与 **Module A counter match event condition** 相同。选项包括：

- `Counter equals to zero (CTR=Zero)` - 当 ePWM 计数器达到零时（少数处理器的默认值）。
- `Counter equals to period (CTR=PRD)` - 当 ePWM 计数器达到 period 值时。
- `Counter equals to zero or period (CTR=Zero or CTR=PRD)` - 当时基计数器达到零 (TBCTR = 0x0000) 或时基计数器达到 period (TBCTR = TBPRD) 时。
- `Counter is incrementing and equals to the compare x register (CTRU=CMPx)` - ePWM 计数器在递增过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。
- `Counter is decrementing and equals to the compare x register (CTRD=CMPx)` - ePWM 计数器在递减过程中达到比较值 x。在此情况下，x 表示 A、B、C 或 D。

### HRPWM 选项卡

在为 F2837xD 处理器进行 HR（High Resolution）配置期间，ePWM 模块仅存在于 ePWM1 上，并且 SFO 仅在 CPU1 上运行。因此，如果您想使用 HRPWM，则必须将 ePWM1 分配给 CPU1；如果启用了 SFO，它必须在 CPU1 上运行。

对于 F2838xD 器件，即使 CPU 和 EWPM1 仍执行 HRPWM 的校准，每个 EPWM 模块也会对自己的 HRPWM 进行时钟控制，并使用由 SFO 计算的相同 HRMSTEP 值。这允许 HRPWM 在 CPU2 上正确运行。

### **在 ePWM#A 上启用高分辨率周期（HRPWM - period）、在 ePWM#B 上启用高分辨率周期（HRPWM - period）** — 指示常规生成 PWM 的有效分辨率 `off`（默认）| `on`

当常规生成的 PWM 的有效分辨率不足时，可考虑使用高分辨率 PWM（HRPWM）。PWM 的分辨率通常取决于 PWM 频率和底层系统时钟频率。为解决此限制，HRPWM 使用 **Micro Edge Positioner (MEP)** 技术，通过细分每个粗系统时钟来更精细地定位边沿。细分的精度约为 `150ps`。下图显示了以 **MEP** 步长表示的一个系统时钟与边沿位置之间的关系：

启用此参数后，模块接受 ePWM Module 的 timer period 的小数值。HRPWM Period 的 Extension Register（TBPRDHR）提供 **Timer period** 值小数部分的 8 位表示。此参数会启用 **Enable high resolution PWM (HRPWM - duty)** 参数，并显示 **HRPWM loading mode**、**HRPWM control mode** 和 **HRPWM edge control** 模式参数。

选择 Enable HRPWM (Period) 会将 **TB clock prescaler divider** 和 **High Speed TB clock prescaler divider** 强制为 `1`。这些设置使 HRPWM 时基时钟与 SYSCLKOUT 频率匹配。

**Counting mode** 参数中的 `Down` 选项与 HRPWM 不兼容。为避免构建模型时出错，请勿将 **Counting mode** 参数设置为 `Down`，也不要选中 **Enable HRPWM (Period)** 参数复选框。

**注意**

此参数仅适用于特定的 C28x 器件。

### **在 ePWM#A 上启用 HRPWM Duty（HRPWM - duty）** — 指示比较值的小数部分 `off`（默认）| `on`

启用此参数后，将接受 ePWM Module 的 Compare A value（CMPA）的小数值。HRPWM Compare A 的 Extension Register（CMPAHR）提供比较值小数部分的 8 位表示。

此参数还会启用 **HRPWM control mode**。

**注意**

此参数仅针对特定的 C28x 器件显示。

### **ePWM#A 上的高分辨率 PWM (HRPWM) 加载模式** — 确定何时将 CMPAHR 影子值传输到活动寄存器 `Counter equals to period (CTR=PRD)`（默认）| `Counter equals to zero (CTR=ZERO)` | `Counter equals to either zero or period (CTR=ZERO or CTR=PRD)`

当选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时，此参数出现。确定何时将 CMPAHR 影子的值传输到活动寄存器：

- `Counter equals to zero (CTR=ZERO)` — 当 time base counter 等于零（TBCTR = 0x0000）时传输该值。
- `Counter equals to period (CTR=PRD)` — 当 time base counter 等于周期（TBCTR = TBPRD）时传输该值。
- `Counter equals to either zero or period (CTR=ZERO or CTR=PRD)` — 当任一条件为真时传输该值。

此参数配置 HRPWM configuration register（HRCNFG）中的 HRLOAD shadow mode 位。

### **ePWM#A 上的高分辨率 PWM (HRPWM) 控制模式** — 指示控制模式 `Duty control mode`（默认）| `Phase control mode`

当选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时，此参数出现。选择哪个寄存器控制 Micro Edge Positioner (MEP) 步长。**高分辨率 PWM (HRPWM) 控制模式** 选项配置 CTLMODE control mode 位。

- `Duty control mode` — 使用 HRPWM Duty 的 Extension Register（CMPAHR）或 HRPWM Period 的 Extension Register（TBPRDHR）控制 MEP 边沿位置。
- `Phase control mode` — 使用 Time Base Phase High Resolution Register（TBPHSHR）控制 MEP 边沿位置。

### **高分辨率 PWM (HRPWM) 边沿控制模式** — 指示边沿控制模式 `Both Edge`（默认）| `Rising Edge` | `Falling Edge`

选择控制边沿类型上 MEP 精确定位控制的寄存器。

- `Rising Edge` — 上升沿的 MEP 控制
- `Falling Edge` — 下降沿的 MEP 控制
- `Both Edge` — 两个边沿的 MEP 控制

**高分辨率 PWM (HRPWM) 边沿控制模式** 选项配置 HRPWM configuration register（HRCNFG）中的 EDGMODE edge mode 位。

#### 依赖项

当选中 **Enable high resolution PWM (HRPWM - period)** 或 **Enable high resolution PWM (HRPWM - duty)** 时，此参数出现。

### **启用高分辨率死区上升沿（RED）、启用高分辨率死区下降沿（FED）** — 在 Deadband Rising Edge Delay 和 Falling Edge Delay 上启用 HRPWM 能力 `off`（默认）| `on`

这些参数在 Deadband Rising Edge Delay 和 Falling Edge Delay 上启用 HRPWM 能力。高分辨率死区 RED 和 FED 需要 half-cycle clocking 模式。

#### 依赖项

当选中 **Use deadband for ePWM#A** 或 **Use deadband for ePWM#B** 时，这些参数出现。

**注意**

这些参数仅适用于特定的 F28x 器件。选中这些参数时，PWM chopper module 被禁用。

### **使用比例因子优化器 (SFO) 软件** — 指示比例因子 `off`（默认）| `on`

在 HRPWM 中启用 scale factor optimizing (SFO) 软件。此软件动态确定 MEP 步长的比例因子。步长会随温度和电压等工作条件变化。SFO 软件可减少由这些条件引起的变化。更多信息，请参阅 *TMS320x2802x, 2803x Piccolo High Resolution Pulse Width Modulator (HRPWM) Reference Guide* 的 Scale Factor Optimizing Software (SFO) 部分。

#### 依赖项

- 仅当选中 **Enable auto convert** 和 **Enable high resolution PWM (HRPWM - period)** 参数时，**使用比例因子优化器 (SFO) 软件** 参数才启用、只读且可见。
- 仅当未选中 **Enable auto convert** 参数时，**使用比例因子优化器 (SFO) 软件** 参数才可编辑。

### **Enable auto convert** — 指示 auto convert `off`（默认）| `on`

将 SFO 软件计算的比例因子应用于控制 period 或 duty cycle。（使用 **HRPWM duty mode** 选择控制 period 或 duty cycle。）此参数设置 HRPWM Configuration Register（HRCNFG）中的 AUTOCONV 字段。

#### 依赖项

- **Enable auto convert** 参数仅针对特定的 C28x 器件显示。
- 仅当选中 **Enable high resolution PWM (HRPWM - period)** 参数时，**Enable auto convert** 参数才启用、只读且可见。
- 仅当选中 **Enable high resolution PWM (HRPWM - duty)** 参数时，**Enable auto convert** 参数才启用且可编辑。

### PWM Chopper Control 选项卡

### **Chopper module 使能** — 启用 chopper module `off`（默认）| `on`

选择此项以启用 chopper module。

### **Chopper 频率分频器** — 确定 chopper clock 的频率 `1`（默认）| `2` | `...`

设置用于确定 chopper clock 频率的 prescaler 值。系统时钟速度除以此值以确定 chopper clock 频率。选择 `1` 到 `8` 范围内的整数值。

### **第一个脉冲的 Chopper clock cycles 宽度** — 用于快速导通硬开关的高能量第一个脉冲 `1`（默认）| `2` | `...`

选择 `1` 到 `16` 范围内的整数值以设置第一个脉冲的宽度。此功能提供高能量第一个脉冲，以快速导通硬开关。

### **Chopper pulse 占空比** — 确定第二个及后续脉冲的占空比 `12.5%`（默认）| `25%` | `...`

第二个及后续脉冲的占空比也可编程。占空比可以 `12.5%` 为步长，从 `12.5%` 变化到 `87.5%`。

### Trip Zone 单元

### **Trip zone 源** — 确定 trip zone 信号控制逻辑的来源 `Specify via dialog`（默认）| `Input port`

指定 trip zone 信号控制逻辑的来源。选择 `Specify via dialog`（默认）以在模块对话框中启用特定 trip zone 信号。选择 `Input port` 以使用模块输入端口 **TZSEL** 启用特定 trip-zone 信号。

**Trip Zone 单元** 选项卡允许您为 Trip-zone（TZ）子模块指定参数。每个 ePWM 模块从 GPIO MUX 接收 TZ 信号。Trip zone 信号的数量因 C28x 处理器系列而异。这些信号可用于根据外部故障等事件将 ePWM 输出强制为特定状态。使用此选项卡上的设置对 ePWM 输出进行编程，以响应外部事件。

如果选择 `Input port`，请使用以下位运算确定要发送到 **TZSEL** 输入端口的 16 位整数值：

`TZSEL INPUT VALUE = (DCBEVT1*2 15
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

该软件将高 8 位用于 **One shot TZ1-TZ6**（OSHT1–6），将低 8 位用于 **Cyclic TZ1-TZ6**（CBC1–6）。您可以设置一组 TZ 源（1~6），使用位运算将它们组合为一个整数，然后将该整数馈送到 TZSEL。

例如，要将 One Shot TZ6（OSHT6）和 One Shot TZ5（OSHT5）启用为 trip zone 源，请将 OSHT6 和 OSHT5 设置为 1，其余值保留为 0。

TZSEL INPUT VALUE = (1\*215 +
1\*214 + 1\*213
+ 1\*212 + 0\*211
…)

TZSEL INPUT VALUE = (8192 + 4096 + 0 …)

TZSEL INPUT VALUE = 12288

当模块收到此值时，会将其作为二进制值 `0011000000000000` 应用到 TZSEL 寄存器。

更多信息，请参阅 TMS320x28xx, 28xxx Enhanced Pulse Width Modulator (ePWM) Module Reference Guide 的 Trip-Zone Submodule Control and Status Registers 部分。

### **启用 one-shot Trip-zone#（TZ#）** — 以 one-shot 模式启用对应的 trip zone 信号 `off`（默认）| `on`

选择此参数以 one-shot 模式启用对应的 trip zone 信号。在此模式下，当 trip 事件有效时，trip zone 模块立即对 EPWM#A/B 输出执行对应操作并锁存该条件。

当发生 one-shot trip 事件时，会设置 one-shot trip 事件标志 `TZFLG[OST]`。导致 one-shot trip 事件的事件的对应标志也会通过寄存器读/写模块在寄存器 `TZOSTFLG` 中设置。要清除 one-shot trip 条件，请使用寄存器读/写模块手动写入 `TZCLR[OST]` 位。类似地，要清除 `TZOSTFLG` 寄存器位，请使用寄存器读/写模块手动写入 `TZOSTCLR` 寄存器中的对应位。

例如，要清除 ePWM1 中的 `OST1` trip 事件，请使用寄存器读/写模块将 1 写入 `EPwm1Regs.TZCLR.bit.OST` 和 `EPwm1Regs.TZOSTCLR.bit.OST1` 位。

#### 依赖项

仅当 **Trip zone source** 为 `Specify via dialog` 时，此选项可用。

### **启用 one-shot digital compare A event 1（DCAEVT1）、启用 one-shot digital compare B event 1（DCBEVT1）** — 启用对应事件信号作为 event 1 的 OST trip 源 `off`（默认）| `on`

选择这些参数以启用对应事件信号作为 event 1 的 OST trip 源。在此模式下，如果 digital compare A 或 digital compare B event 1 有效，trip zone 模块立即对 EPWM#A/B 输出执行对应操作并锁存该条件。您可以使用 software control 解除锁存该条件。

#### 依赖项

- 仅当 **Trip zone source** 为 `Specify via dialog` 时，此选项可用。
- 此参数仅适用于特定的 C28x 处理器。

### **启用 cyclic Trip-zone#（TZ#）** — 以 cycle-by-cycle 模式启用对应的 trip zone 信号 `off`（默认）| `on`

选择此参数以 cycle-by-cycle 模式启用对应的 trip zone 信号。在此模式下，当 trip 事件有效时，trip zone 模块立即对 EPWM#A/B 输出执行对应操作并锁存该条件。在 cycle-by-cycle 模式下，当 ePWM Counter 达到零时，trip zone 模块会自动清除条件。因此，在 cycle-by-cycle 模式下，每个 ePWM 周期都会复位或清除 trip 事件。

#### 依赖项

仅当 **Trip zone source** 为 `Specify via dialog` 时，此选项可用。

### **启用 cyclic digital compare A event 2（DCAEVT2）、启用 cyclic digital compare B event 2（DCBEVT2）** — 启用对应事件信号作为 event 2 的 cyclic trip 源 `off`（默认）| `on`

选择这些参数以启用对应事件信号作为 event 2 的 cyclic trip 源。在此模式下，如果 digital compare A 或 digital compare B event 2 有效，Trip zone 模块立即对 EPWM#A/B 输出执行对应操作并锁存该条件。在 Cycle-by-Cycle Mode 下，当 ePWM Counter 达到零时，Trip zone 模块会自动清除条件。因此，在 Cycle-by-Cycle Mode 下，每个 ePWM 周期都会复位或清除 trip 事件。

#### 依赖项

- 仅当 **Trip zone source** 为 `Specify via dialog` 时，此选项可用。
- 此参数仅适用于特定的 C28x 处理器。

### **启用 trip-zone one-shot 中断（OST）** — 启用 trip zone one-shot interrupt `off`（默认）| `on`

当任何已启用的 one shot（OST）触发事件发生时生成中断。

**注意**

`TZFLG.INT` 在 ISR 后处理中被清除。但是，如果在 `CBC` 或 `OST` 置位时清除中断标志，则会生成另一个中断脉冲。清除所有标志位将阻止进一步中断。通过向 `TZCLR` 寄存器写入适当的值来清除此位。

### **启用 trip-zone cycle-by-cycle 中断（CBC）** — 启用 trip-zone cycle-by-cycle interrupt `off`（默认）| `on`

当任何已启用的 cyclic 或 cycle-by-cycle（CBC）触发事件发生时生成中断。

**注意**

`TZFLG.INT` 在 ISR 后处理中被清除。但是，如果在 `CBC` 或 `OST` 置位时清除中断标志，则会生成另一个中断脉冲。清除所有标志位将阻止进一步中断。通过向 `TZCLR` 寄存器写入适当的值来清除此位。

### **数字比较器输出 A 事件 1 中断使能（DCAEVT1）、数字比较器输出 A 事件 2 中断使能（DCAEVT2）、数字比较器输出 B 事件 1 中断使能（DCBEVT1）、数字比较器输出 B 事件 2 中断使能（DCBEVT2）** — 启用数字比较器输出 `off`（默认）| `on`

当 event 1 或 2 的 Digital Comparator Output A 或 Digital Comparator Output B 发生时生成中断。

**注意**

这些参数仅适用于特定的 C28x 处理器。

### **在以下条件下清除 cycle-by-cycle trip latch** — 选择清除 cycle by cycle trip latch `Counter equals to zero (CTR=Zero)`（默认）| `Counter equals to period (CTR=Prd)` | `Counter equals to zero or period (CTR=Zero or CTR=Prd)` | `Latch not cleared`

选择事件选项以清除 cycle by cycle trip latch。

#### 依赖项

- 要启用此参数，请将 trip zone source 参数设置为 **Input port**，或将 trip zone source 设置为 **Specify via dialog**。然后启用 **Enable cyclic trip-zine#** 或 **Enable cyclic digital compare A event 2 (DCAEVT2), Enable cyclic digital compare B event 2 (DCBEVT2)**。
- 这些参数仅适用于特定的 C28x 处理器。

### **ePWM#A forced (TZ) to, ePWM#B forced (TZ) to, ePWM#A forced (DCAEVT#) to, ePWM#B forced (DCBEVT#) to** — 确定要在 ePWM 输出上考虑的动作 `No action`（默认） | `High` | `Low` | `Hi-Z (High Impedance)`

这些参数决定在 trip zone 条件下可对 ePWM 输出执行的动作。trip zone 模块会覆盖并将 ePWM#A 和/或 ePWM#B（TZ 或 DCAEVTx）输出强制为以下状态之一：`No action`（默认）、`High`、`Low` 或 `Hi-Z (High Impedance)`。

### Digital Compare

### **Source for digital compare A high signal (DCAH), Source for digital compare B high signal (DCBH)** — 数字比较高信号源 `GPTRIP1SEL/(TZ1) for DCAH/GPTRIP1SEL/(TZ1) for DCBH`（默认） | `GPTRIP3SEL/(TZ3) for DCAH/GPTRIP7SEL for DCBH` | `...`

选择适当的 TZ 或 COMP 信号，为 Digital compare A/B 高信号生成高逻辑值。使用 **Digital compare output A event # selection**、**Digital compare output B event # selection**、**DCAEVT# source select**、**DCBEVT# source select** 参数来确定 DCAH/DCBH 对 DCAEVT# 和 DCBEVT# 的影响。

每个 digital compare (DC) 子模块从 GPIO MUX 接收三个 TZ 信号（TZ1 到 TZ3），并从 COMP 接收三个 COMP 信号（仅适用于特定 C28x 器件）。这些信号指示 ePWM 子模块外部的故障或 trip 条件。使用此选项卡中的设置来响应那些外部信号输出特定 DC 事件。这些 DC 事件直接馈入 time base、trip zone 和 event trigger 子模块。

有关更多信息，请参见 *Piccolo Enhanced Pulse Width Modulator (ePWM) Module Reference Guide* 的 *Digital Compare (DC) Submodule* 章节。

### **Source for digital compare A low signal (DCAL), Source for digital compare B low signal (DCBL)** — 数字比较低信号源 `GPTRIP1SEL/(TZ1) for DCAL/GPTRIP1SEL/(TZ1) for DCBL`（默认） | `TRIPIN1(ECCDBLERR) for DCAL/Select From DCBLTRIPSEL for DCBL` | `...`

选择适当的 TZ 或 COMP 信号，为 Digital compare A/B 低信号生成低逻辑值。使用 **Digital compare output A event # selection**、**Digital compare output B event # selection**、**DCAEVT# source select**、**DCBEVT# source select** 选项来确定 DCAL/DCBL 对 DCAEVT# 和 DCBEVT# 的影响。

### **Digital compare output A event # selection (DCAEVT#), Digital Compare output B event # selection (DCBEVT#)** — 限定生成 DC 事件的信号 `Event disabled`（默认） | `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

限定生成 DC 事件的信号，例如 DCAEVT# 或 DCBEVT#。要禁用此功能，请选择 `Event disabled` 选项。根据信号的源选择，可触发该事件。事件选择可基于 High、Low 和 Don't care 条件的组合。

### **DCAEVT# source select, DCBEVT# source select** — 数字比较事件源 `Event disabled`（默认） | `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

此参数控制触发 DC 事件的两个独立方面：

- 触发滤波或未滤波的 DC 事件

  - DC 事件可以是滤波或未滤波的信号，并可传递到其他子模块。
  - 配置 DCACTL 和 DCBCTL 寄存器中的 EVT1SRCSEL 和 EVT2SRCSEL。
  - 以 `DCAEVT# with sync` 或 `DCAEVT# with async` 开头的选项不会对 DC 事件应用滤波。经过限定的 DC 信号直接传递以触发 DC 事件，而不进行任何滤波。
  - 以 `DCEVTFILT sync` 开头的选项会对 DC 事件应用滤波。经过限定的信号在触发 DC 事件之前会通过滤波电路。有关更多信息，请参见 *Piccolo Enhanced Pulse Width Modulator (ePWM) Module Reference Guide* 的 *Event Filtering* 章节。
- 同步或异步触发 DC 事件

  - DC 事件信号可与 TBCLK 同步，也可保持异步。
  - 配置 DCACTL 和 DCBCTL 寄存器中的 EVT1SRCSEL 和 EVT2SRCSEL。
  - 以 `async` 结尾的选项会异步触发 DC 事件。当限定或滤波后的信号存在时，DC 子模块立即触发 DC 事件。
  - 以 `sync` 结尾的选项会同步触发 DC 事件。一旦限定或滤波后的信号存在，DC 子模块会与 TBCLK 信号同步触发 DC 事件。

    **Note**

    上述字段仅在相应的 DCAEVT# 使能时出现。

**Note**

当为 **DCAEVTX source select** 或 **DCBEVTX source select** 选择 `DCEVTFILT with sync` 或 `DCEVTFILT with async` 时，以下字段出现。

有关以下参数的更多详细信息，请参阅 Technical Reference Manual for Enhanced Pulse Width Modulator (ePWM) Module Reference Guide。

### **Pulse select** — 指示滤除事件发生的消隐窗口 `Counter equals to zero (CTR=Zero)`（默认） | `Counter equals to period (CTR=PRD)`

该消隐窗口在有效时滤除信号上的事件发生。设置此参数以对齐到 CTR = PRD 脉冲或 CTR = Zero 脉冲。

### **Blanking window inverted** — 指示反相消隐窗口 `off`（默认） | `on`

选择此参数以启用反相消隐窗口。

### **Blanking window offset** — 指示消隐窗口偏移 `0`（默认）

确定在 **Pulse select** 事件之后开始用于滤波的消隐窗口所需的 TBCLK 周期数

### **Blanking window width** — 指示消隐窗口宽度 `0`（默认）

确定在 **Pulse select** 事件之后开始用于滤波的消隐窗口所需的 TBCLK 周期数。

消隐窗口将基于 **Pulse select** 事件的发生而开始，并根据 **Blanking offset window** 以额外的 TBCLK 周期作为偏移。

在消隐窗口期间，所有事件都被忽略。在应用消隐窗口之前和之后，事件可以触发 sync 或 async 事件。

### **Filter output DCEVTFILT** — 指示滤波器的源选择 `Filtered version of DCAEVT1 (DCAEVT1FILT)`（默认） | `Filtered version of DCAEVT2 (DCAEVT2FILT)` | `Filtered version of DCBEVT1 (DCBEVT1FILT)` | `Filtered version of DCBEVT2 (DCBEVT2FILT)`

使用此参数选择用于滤波的源，该源形成 DCEVTFILT 信号。

### **Enable counter capture** — 指示计数器捕获 `off`（默认） | `on`

启用此选项可捕获 trip 事件的 TBCTR 值。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

生成增强型脉冲宽度调制 (ePWM) 波形

配置类型 1 到类型 4 增强型脉冲宽度调制器 (ePWM) 以生成 PWM 波形。可用的 ePWM 模块数量（ePWM1-ePWM16）因 C2000 处理器而异。有关 ePWM 类型的更多信息，请参阅 C2000 Real-Time Control Peripheral Reference Guide。

使用此模块生成 ePWM 波形。C28x 器件上有多个 ePWM 模块可用。每个模块生成两个 PWM 信号 ePWMA 和 ePWMB。

当使能高分辨率脉冲宽度调制器 (HRPWM) 时，ePWM 模块使用比例因子优化 (SFO) 软件库。SFO 库可以“动态确定每个系统时钟 (SYSCLKOUT) 周期的微边沿定位器 (MEP) 步数。”有关更多信息，请参见 `TMS320x28xx, 28xxx High-Resolution Pulse Width Modulator (HRPWM) Reference Guide`，该文档可在 Texas Instruments® 网站上获取。

此模块通用于各种 C28x 器件。可用参数因从中选择该模块的库而异。模块右上角的蓝色标签显示系列。由于该模块是不同器件上可用功能的超集，因此并非所有参数都与您的模型相关。
