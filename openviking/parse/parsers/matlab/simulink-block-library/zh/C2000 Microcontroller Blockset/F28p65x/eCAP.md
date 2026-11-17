---
type: simulink-block
title: 'C28x eCAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xecap'
documentation_source_path: 'ref/c28xecap.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x eCAP

## 端口
```yaml
ports:
- name: SI
  summary: 来自软件的同步输入 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: RA
  summary: 单次捕获序列 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: T
  summary: APWM 周期 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: W
  summary: APWM 宽度 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: TS
  summary: 捕获事件的时间戳输出 向量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: CF
  summary: 捕获事件状态 向量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: OF
  summary: 溢出状态 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: Scale factor
  summary: HRCLK 周期缩放因子 标量
  direction: output
  data_types: single | double
```

### 输入

### **SI** — 来自软件的同步输入 标量

来自软件的输入，用于同步 eCAP 计数器。当同步输入值为 1 时发生同步。

#### 依赖

该端口仅在以下情况下出现：

- 在 **General** 选项卡上，选择 **Operating mode** > **eCAP** 或 **APWM**。
- 在 **General** 选项卡上，选择
  **Enable counter Sync-In mode**
  和 **Enable software-forced counter
  synchronizing input**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **RA** — 单次捕获序列 标量

启动单次捕获序列。

使用 2 位停止寄存器来比较 Mod4 计数器输出，当寄存器和计数器值相等时，Mod4 计数器停止。

#### 依赖

该端口仅在以下情况下出现：

- 在 **General** 选项卡上，选择 **Operating mode** > **eCAP**。
- 在 **eCAP** 选项卡上，设置 **Select mode control** > **One-Shot** 并选择 **Enable One-Shot
  re-arming control input**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **T** — APWM 周期 标量

APWM 的周期。

#### 依赖

该端口仅在以下情况下出现：

- 在 **General** 选项卡上，选择 **Operating mode** > **APWM**。
- 在 **APWM** 选项卡上，选择 **Waveform period source** > **Input port**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **W** — APWM 宽度 标量

APWM 的宽度。

#### 依赖

该端口仅在以下情况下出现：

- 在 **General** 选项卡上，选择 **Operating mode** > **APWM**。
- 在 **APWM** 选项卡上，选择 **Duty cycle source** > **Input port**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### 输出

输出端口仅在 eCAP 模式下出现。

### **TS** — 捕获事件的时间戳输出 向量

TS 是一个信号维度为 4 的向量，对应于 CAP1、CAP2、CAP3 和 CAP4 时间戳值，具体取决于在 **eCAP** 选项卡上的 **Stop value after** 中选择的捕获事件。使用 **Enable reset
counter after capture event # time-stamp** 选项可在事件后复位计数器。此选项对于查找事件之间的时间差很有用。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **CF** — 捕获事件状态 向量

CF 是一个维度为 4 的向量，对应于 CEVT1-CEVT2。捕获事件的状态。`0` 表示未发生事件。`1` 表示由 **Stop value after** 参数指定的事件已在 eCAP 引脚上发生。

#### 依赖

该端口仅在您在 **eCAP** 选项卡上选择 **Enable capture
event status flag output** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **OF** — 溢出状态 标量

溢出状态。`0` 表示计数器未溢出。`1` 表示计数器已从最高值溢出到 0。

#### 依赖

该端口仅在您在 **eCAP** 选项卡上选择 ****Enable overflow status flag
output**** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Scale factor** — HRCLK 周期缩放因子 标量

可用于将捕获值从 HRCLK 周期计数转换为等效 SYSCLK 周期计数的因子。

#### 依赖

该端口仅在您选择 ****Enable high resolution
capture**** 参数并在 **eCAP** 选项卡上将 **Output
type** 设置为 **HRCLK/ SYSCLK cycles** 时出现。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Operating mode
  summary: 选择 eCAP 或 APWM 模式 eCAP（默认）| APWM
  group: 常规
- name: eCAPx pin
  summary: 选择捕获单元引脚 eCAP1（默认）| eCAP2 | eCAP3 | eCAP4 | eCAP5 | eCAP6 | eCAP7
  group: 常规
- name: Counter phase offset value (0 ~ 4294967295)
  summary: 事件捕获的时基 0（默认）| [0 4294967295] 范围内的整数
  group: 常规
- name: Enable counter Sync-In mode
  summary: 使能 TSCTR 计数器从 CTRPHS 寄存器加载 off（默认）| on
  group: 常规
- name: Enable software-forced counter synchronizing input
  summary: 同步一个或多个 eCAP 时基 off（默认）| on
  group: 常规
- name: Sync output selection
  summary: 将 eCAP 计数器与其他 eCAP 计数器同步 Disabled（默认）| Pass through | CTR=PRD
  group: 常规
- name: Sample time
  summary: 模块读取输入引脚值的频率 0.001（默认）
  group: 常规
- name: Event prescaler (integer from 0 to 31)
  summary: 以 2 的倍数对输入信号进行预分频 0（默认）| [0 31] 范围内的标量整数
  group: eCAP
- name: Enable high resolution capture
  summary: 选择启用高分辨率捕获或 HRCAP 模式 off（默认）| on
  group: eCAP
- name: Enable continuous calibration mode
  summary: 选择启用连续校准模式 off（默认）| on
  group: eCAP
- name: Calibration period in seconds
  summary: 指定校准周期 0.0016（默认）| on
  group: eCAP
- name: Select mode control
  summary: 捕获模式 Continuous（默认）| One-Shot
  group: eCAP
- name: Enable One-Shot rearming control via input port
  summary: 重新武装单次捕获序列 off（默认）| on
  group: eCAP
- name: Stop value after
  summary: 捕获停止前经过的捕获事件数 Capture Event 1（默认）| Capture Event 2 | Capture Event 3 | Capture Event 4
  group: eCAP
- name: 'Enable reset counter after capture event # time-stamp'
  summary: 捕获事件后复位计数器 off（默认）| on
  group: eCAP
- name: 'Select capture event # polarity'
  summary: 在上升沿或下降沿启动捕获事件 Rising Edge（默认）| Falling Edge
  group: eCAP
- name: Output type
  summary: 选择 eCAP 的输出类型 HRCLK/SYSCLK cycles（默认）| Microseconds
  group: eCAP
- name: Time-Stamp counter data type
  summary: 计数器的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | boolean
  group: eCAP
- name: Enable capture event status flag output
  summary: 输出捕获事件状态 off（默认）| on
  group: eCAP
- name: Capture flag data type
  summary: 输出端口 CF 的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | boolean
  group: eCAP
- name: Enable overflow status flag output
  summary: 输出 FIFO 缓冲区元素的状态 off（默认）| on
  group: eCAP
- name: Overflow flag data type
  summary: 输出端口 OF 的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | boolean
  group: eCAP
- name: Waveform period units
  summary: 测量波形周期的单位 Seconds（默认）| Clock cycles
  group: APWM
- name: Waveform period source
  summary: 获取波形周期值的来源 Specify via dialog（默认）| Input port
  group: APWM
- name: Waveform period
  summary: PWM 波形的周期 0.001（默认）
  group: APWM
- name: Duty cycle units
  summary: 测量占空比的单位 Percentages（默认）| Clock cycles
  group: APWM
- name: Duty cycle source
  summary: 获取 PWM 波形占空比的来源 Specify via dialog（默认）| Input port
  group: APWM
- name: Duty cycle
  summary: PWM 波形脉冲持续时间与 PWM 波形周期的比率 50（默认）
  group: APWM
- name: Output polarity select
  summary: 设置输出的有效电平 Active High（默认）| Active Low
  group: APWM
- name: 'Post interrupt on capture event #'
  summary: 将中断源设置为捕获事件 off（默认）| on
  group: Interrupt
- name: Post interrupt on counter overflow
  summary: 在计数器溢出时触发中断 off（默认）| on
  group: Interrupt
- name: Post interrupt on counter equal period match
  summary: 当计数器等于周期寄存器时发送中断 off（默认）| on
  group: Interrupt
- name: Post interrupt on counter equal compare match
  summary: 当计数器等于比较寄存器时发送中断 off（默认）| on
  group: Interrupt
```

### 常规

### **Operating mode** — 选择 eCAP 或 APWM 模式 `eCAP`（默认）| `APWM`

当您选择 `eCAP` 时，该模块捕获每个捕获单元的引脚跳变并将其记录到 FIFO 缓冲区。当您选择 `APWM` 时，该模块生成非对称脉宽调制（APWM）波形以驱动下游系统。

### **eCAPx pin** — 选择捕获单元引脚 `eCAP1`（默认）| `eCAP2` | `eCAP3` | `eCAP4` | `eCAP5` | `eCAP6` | `eCAP7`

选择所需的 eCAP 模块，以获得专用的 eCAP 引脚来捕获外部事件。

eCAP 模块的引脚选择可通过浏览到 **Hardware Implementation** > **Target hardware resources** 来完成。仅当该模块具有多个可为 eCAP 模块配置的引脚时，才提供选择选项。

### **Counter phase offset value (0 ~ 4294967295)** — 事件捕获的时基 `0`（默认）| [0 4294967295] 范围内的整数

此值提供事件捕获的时基，由系统时钟计时。相位寄存器用于通过软件强制或硬件强制同步与其他计数器同步。有关软件强制或硬件强制同步的信息，请参阅 **Enable counter Sync-In mode** 参数。当您需要在捕获模块之间设置相位偏移时，此值在 APWM 模式下很有用。将相位偏移设置为 0 到 42949667295（232）个计数之间的整数。

### **Enable counter Sync-In mode** — 使能 TSCTR 计数器从 CTRPHS 寄存器加载 `off`（默认）| `on`

同步可以使用 SYNCI 事件或软件来完成。当同步发生时，影子寄存器 CTRPHS 被加载到当前 eCAP 模块和下游 eCAP 模块的活动计数器 TSCTR 中。

### **Enable software-forced counter synchronizing input** — 同步一个或多个 eCAP 时基 `off`（默认）| `on`

一种用于同步一个或多个 eCAP 时基的软件方法。当同步输入值为 1 时发生同步。

#### 依赖

此参数仅在选择 **Enable counter Sync-In
mode** 时出现。

### **Sync output selection** — 将 eCAP 计数器与其他 eCAP 计数器同步 `Disabled`（默认）| `Pass through` | `CTR=PRD`

将 eCAP 计数器与其他 eCAP 计数器同步。选项包括：

- `CTR=PRD` — 当计数器值等于周期时触发同步输出信号。

- `Pass through` — 同步输入事件作为同步输出信号传递。

  **注意**

  - 对于 F2838x/002x
    和 003x 处理器，Pass through 选项仅适用于
    `SWSYNC input`。
    `ECAPSYNCIN` 信号不能传递，
    必须由下游 eCAP 模块在 **Hardware Implementation** > **Target hardware
    resources** > **eCAP** 下配置。
  - 当 **Operating mode** 设置为
    `APWM` 时，`CTR=PRD`
    的同步输出选择仅适用于 eCAP。
- `Disabled` — 禁用同步输出信号。

### **Sample time** — 模块读取输入引脚值的频率 `0.001`（默认）

模块的采样时间，以秒为单位。

### eCAP

要启用 eCAP 选项卡上的配置参数，请在 **General** 选项卡上将 **Operating
mode** 设置为 `eCAP`。

### **Event prescaler (integer from 0 to 31)** — 以 2 的倍数对输入信号进行预分频 `0`（默认）| [0 31] 范围内的标量整数

输入信号按此参数值的两倍进行预分频。例如，如果您输入 `1`，输入被预分频 2 倍；对于 `31`，输入被预分频 62 倍。输入 `0` 会绕过输入预分频器，使输入捕获信号保持不变。

### **Enable high resolution capture** — 选择启用高分辨率捕获或 HRCAP 模式 `off`（默认）| `on`

选择 **Enable high resolution capture**（HRCAP 模式）参数以高分辨率捕获脉冲。

#### 依赖

此参数仅适用于特定的 TI 处理器。

### **Enable continuous calibration mode** — 选择启用连续校准模式 `off`（默认）| `on`

选择 **Enable continuous calibration mode** 参数以定期执行校准。

如果未启用连续校准模式，则校准仅发生一次（仅初始化）。高分辨率中断用于在内部监控校准状态，以获取更新的缩放因子用于计算时间周期。因此，Hardware Interrupt 模块不能使用高分辨率中断。

校准过程提供缩放因子，用于以秒为单位计算高分辨率捕获值。

#### 依赖

要启用此参数，请选择 **Enable high resolution
capture** 参数。此参数仅适用于特定的 TI 处理器。

### **Calibration period in seconds** — 指定校准周期 `0.0016`（默认）| `on`

以秒为单位指定校准周期。

#### 依赖

要启用此参数，请选择 **Enable high resolution
capture** 参数和 **Enable continuous
calibration mode**。此参数仅适用于特定的 TI 处理器。

### **Select mode control** — 捕获模式 `Continuous`（默认）| `One-Shot`

`Continuous` 选项使用循环缓冲区执行连续时间戳捕获（事件 1 到 4）。

`One-Shot` 选项启用 **Enable One-Shot rearming control via input port** 选项。

### **Enable One-Shot rearming control via input port** — 重新武装单次捕获序列 `off`（默认）| `on`

选择此参数后，单次捕获序列按如下方式重新武装：

1. Mod4 计数器复位为零。
2. Mod4 计数器解冻。
3. 使能捕获寄存器加载。

#### 依赖

此参数仅在您为 **Select mode
control** 选择 `One-Shot` 时出现。

### **Stop value after** — 捕获停止前经过的捕获事件数 `Capture Event 1`（默认）| `Capture Event 2` | `Capture Event 3` | `Capture Event 4`

您希望停止捕获序列之前经过的捕获事件数。

### **Enable reset counter after capture event # time-stamp** — 捕获事件后复位计数器 `off`（默认）| `on`

eCAP 过程在收到捕获事件时间戳后复位计数器。在这种情况下，`#` 表示在 **Stop value after** 参数中设置的捕获事件编号。

### **Select capture event # polarity** — 在上升沿或下降沿启动捕获事件 `Rising Edge`（默认）| `Falling Edge`

启动捕获事件的选项。在这种情况下，`#` 表示在 **Stop value after** 参数中设置的捕获事件编号。

### **Output type** — 选择 eCAP 的输出类型 `HRCLK/SYSCLK cycles`（默认）| `Microseconds`

选择 eCAP 的输出类型。

在 HRCAP 模式（高分辨率模式）下使用时，输出类型为 HRCLK 周期形式；在正常模式下使用时为 SYSCLK。当您在 HRCAP 模式（高分辨率模式）下将输出类型设置为 HRCLK/SYSCLK cycles 时，会启用 **Scale
factor** 端口。

### **Time-Stamp counter data type** — 计数器的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

时间戳计数器的数据类型。

### **Enable capture event status flag output** — 输出捕获事件状态 `off`（默认）| `on`

在输出端口 **CF** 输出捕获事件状态标志。在事件被捕获之前，该模块输出 `0`。事件之后，标志值为 `1`。

### **Capture flag data type** — 输出端口 CF 的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

输出端口 **CF** 的数据类型。

#### 依赖

此参数仅在您选择 **Enable
capture event status flag output** 时出现。

### **Enable overflow status flag output** — 输出 FIFO 缓冲区元素的状态 off（默认）| on

在输出端口 **OF** 输出 FIFO 缓冲区元素的状态。

### **Overflow flag data type** — 输出端口 OF 的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

输出端口 **OF** 的数据类型。

#### 依赖

此参数仅在您选择 **Enable
overflow status flag output** 时出现。

### APWM

要启用 APWM 选项卡上的配置参数，请在 **General** 选项卡上将 **Operating
mode** 设置为 `APWM`。

### **Waveform period units** — 测量波形周期的单位 `Seconds`（默认）| `Clock cycles`

`Clock cycles` 使用处理器的高速外设时钟周期。

### **Waveform period source** — 获取波形周期值的来源 `Specify via dialog`（默认）| `Input port`

选择 `Specify via dialog` 在 **Waveform period** 中输入值，或选择 `Input port` 使用来自 **T** 输入端口的值。

### **Waveform period** — PWM 波形的周期 `0.001`（默认）

PWM 波形的周期，以 **Waveform period units** 中指定的时钟周期或秒为单位测量。

**注意**

术语 *clock cycles* 指的是 F2812 芯片上的高速外设时钟。此高速外设时钟默认为 75 MHz，因为高速外设时钟预分频器设置为 2（150 MHz/2）。

#### 依赖

此参数仅在 **Waveform period
source** 设置为 `Specify via
dialog` 时出现。

### **Duty cycle units** — 测量占空比的单位 `Percentages`（默认）| `Clock cycles`

用于测量占空比的单位。

### **Duty cycle source** — 获取 PWM 波形占空比的来源 `Specify via dialog`（默认）| `Input port`

选择 `Specify via dialog` 在 **Duty cycle** 中输入值，或选择 `Input
port` 使用来自 **W** 输入端口的值。

### **Duty cycle** — PWM 波形脉冲持续时间与 PWM 波形周期的比率 50（默认）

PWM 波形脉冲持续时间与 PWM 波形周期的比率。此比率以 **Duty cycle units** 表示。

### **Output polarity select** — 设置输出的有效电平 `Active High`（默认）| `Active Low`

当您选择 `Active High` 时，比较值（占空比）定义高电平时间。选择 `Active
Low` 则指示比较值定义低电平时间。

### Interrupt

### **Post interrupt on capture event #** — 将中断源设置为捕获事件 `off`（默认）| `on`

您可以使用 C28x Hardware Interrupt 模块来响应此中断。在这种情况下，`#` 表示在 **Stop value
after** 参数中设置的捕获事件编号。

#### 依赖

此参数仅在您在 **General** 选项卡上将 **Operating
mode** 设置为 `eCAP` 时出现。

### **Post interrupt on counter overflow** — 在计数器溢出时触发中断 `off`（默认）| `on`

当计数器溢出时触发中断。

#### 依赖

此参数仅在您在 **General** 选项卡上将 **Operating
mode** 设置为 `eCAP` 时出现。

### **Post interrupt on counter equal period match** — 当计数器等于周期寄存器时发送中断 `off`（默认）| `on`

当计数器的值与周期寄存器的值相同时（CTR = PRD）发送中断。

#### 依赖

此参数仅在您在 **General** 选项卡上将 **Operating
mode** 设置为 `APWM` 时出现。

### **Post interrupt on counter equal compare match** — 当计数器等于比较寄存器时发送中断 `off`（默认）| `on`

当计数器的值与比较寄存器的值相同时（CTR = CMP）发送中断。

#### 依赖

此参数仅在您在 **General** 选项卡上将 **Operating
mode** 设置为 `APWM` 时出现。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

接收并记录捕获输入引脚上的跳变，或配置辅助脉冲宽度调制器

eCAP 模块捕获重要外部事件的时序，例如旋转机械速度测量中的霍尔传感器信号。当不用于捕获模式时，该模块可用于 APWM 模式，即单通道非对称脉冲宽度调制器（APWM）。您可以为模型中的每个捕获引脚添加一个 eCAP 模块。在模型中，不能将同一个 eCAP 引脚分配给两个 eCAP 模块。eCAP 和 APWM 模式使用相同的引脚。在 eCAP 模式下，这些引脚用作输入以捕获跳变。在 APWM 模式下，这些引脚用于输出 PWM 波形。

eCAP 模块中的高分辨率模式（HRCAP 模式）仅适用于特定的 TI 处理器。对于 F2803x 和 F2806x 处理器，请参见 HRCAP 模块。
