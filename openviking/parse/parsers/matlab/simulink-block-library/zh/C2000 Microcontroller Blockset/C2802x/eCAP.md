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

### 输入

### **SI** — 来自软件的同步输入标量

用于同步 eCAP 计数器的软件输入。当同步输入值为 1 时发生同步。

#### 依赖项

此端口仅在以下情况下出现：

- 在 **常规** 选项卡上，选择 **Operating mode** > **eCAP** 或 **APWM**。
- 在 **常规** 选项卡上，选择 **Enable counter Sync-In mode** 和 **Enable software-forced counter synchronizing input**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **RA** — One-Shot 捕获序列标量

启动 One-Shot 捕获序列。

使用 2 位停止寄存器比较 Mod4 计数器输出，当寄存器值与计数器值相等时，Mod4 计数器停止。

#### 依赖项

此端口仅在以下情况下出现：

- 在 **常规** 选项卡上，选择 **Operating mode** > **eCAP**。
- 在 **eCAP** 选项卡上，将 **Select mode control** 设置为 **One-Shot**，并选择 **Enable One-Shot re-arming control input**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **T** — APWM 周期标量

APWM 的周期。

#### 依赖项

此端口仅在以下情况下出现：

- 在 **常规** 选项卡上，选择 **Operating mode** > **APWM**。
- 在 **APWM** 选项卡上，选择 **Waveform period source** > **Input port**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **W** — APWM 宽度标量

APWM 的宽度。

#### 依赖项

此端口仅在以下情况下出现：

- 在 **常规** 选项卡上，选择 **Operating mode** > **APWM**。
- 在 **APWM** 选项卡上，选择 **Duty cycle source** > **Input port**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### 输出

输出端口仅在 eCAP 模式下出现。

### **TS** — 捕获事件输出时间戳向量

TS 是信号维度为 4 的向量，对应于 CAP1、CAP2、CAP3 和 CAP4 时间戳值，具体取决于在 **eCAP** 选项卡上的 **Stop value after** 中选择的捕获事件。使用 **Enable reset counter after capture event # time-stamp** 选项可在事件后复位计数器。此选项可用于查找事件之间的时间差。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **CF** — 捕获事件状态向量

CF 是维度为 4 的向量，对应于 CEVT1-CEVT2。捕获事件的状态。`0` 表示未发生任何事件。`1` 表示 **Stop value after** 参数指定的事件已在 eCAP 引脚上发生。

#### 依赖项

仅当你在 **eCAP** 选项卡上选择 **Enable capture event status flag output** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **OF** — 溢出状态标量

溢出的状态。`0` 表示计数器尚未溢出。`1` 表示计数器已从最高值溢出到 0。

#### 依赖项

仅当你在 **eCAP** 选项卡上选择 **Enable overflow status flag output** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Scale factor** — HRCLK cycles 比例因子标量

该因子可用于将捕获值从 HRCLK cycles 计数转换为等效的 SYSCLK cycles 计数。

#### 依赖项

仅当你在 **eCAP** 选项卡上选择 **Enable high resolution capture** 参数并将 **Output type** 设置为 **HRCLK/ SYSCLK cycles** 时，此端口才会出现。

**数据类型：** `single` | `double`

## 参数

### 常规

### **Operating mode** — 选择 eCAP 或 APWM 模式 `eCAP`（默认） | `APWM`

当你选择 `eCAP` 时，模块会针对每个捕获单元捕获并记录引脚跳变到 FIFO 缓冲区。当你选择 `APWM` 时，模块会生成非对称脉宽调制（APWM）波形，用于驱动下游系统。

### **eCAPx pin** — 选择捕获单元引脚 `eCAP1`（默认） | `eCAP2` | `eCAP3` | `eCAP4` | `eCAP5` | `eCAP6` | `eCAP7`

选择所需的 eCAP 模块，以便为捕获外部事件提供专用 eCAP 引脚。

eCAP 模块的引脚选择可通过浏览到 **Hardware Implementation** > **Target hardware resources** 完成。仅当模块有多个可为 eCAP 模块配置的引脚时，才提供该选择选项。

### **Counter phase offset value (0 ~ 4294967295)** — 事件捕获的时基 `0`（默认） | integer in [0 4294967295]

此值提供事件捕获的时基，由系统时钟提供时钟。相位寄存器用于通过软件强制或硬件强制同步与其他计数器同步。有关软件强制或硬件强制同步的信息，请参见 **Enable counter Sync-In mode** 参数。当你需要捕获模块之间存在相位偏移时，此值在 APWM 模式下很有用。将相位偏移设置为从 0 到 42949667295 (232) counts 的整数。

### **Enable counter Sync-In mode** — 使 TSCTR 计数器从 CTRPHS 寄存器加载 `off`（默认） | `on`

同步可使用 SYNCI 事件或软件完成。当发生同步时，影子寄存器 CTRPHS 会加载到当前 eCAP 模块及下游 eCAP 模块中的活动计数器 TSCTR 中。

### **Enable software-forced counter synchronizing input** — 同步一个或多个 eCAP 时基 `off`（默认） | `on`

一种用于同步一个或多个 eCAP 时基的软件方法。当同步输入值为 1 时发生同步。

#### 依赖项

此参数仅在选择 **Enable counter Sync-In mode** 时出现。

### **Sync output selection** — 将 eCAP 计数器与其他 eCAP 计数器同步 `Disabled`（默认） | `Pass through` | `CTR=PRD`

将 eCAP 计数器与其他 eCAP 计数器同步。选项包括：

- `CTR=PRD` — 当计数器值等于周期时触发同步输出信号。

- `Pass through` — 同步输入事件作为同步输出信号传递。

  **注意**

  - 对于 F2838x/002x 和 003x 处理器，Pass through 选项仅适用于 `SWSYNC input`。`ECAPSYNCIN` 信号不能传递，必须由下游 eCAP 模块在 **Hardware Implementation** > **Target hardware resources** > **eCAP** 下配置。
  - 对于 eCAP，仅当 **Operating mode** 设置为 `APWM` 时，`CTR=PRD` 的同步输出选择才适用。

- `Disabled` — 禁用同步输出信号。

### **Sample time** — 模块读取输入引脚值的频率 `0.001`（默认）

模块的采样时间，以 seconds 为单位。

### eCAP

要启用 **eCAP** 选项卡上的配置参数，请在 **常规** 选项卡上将 **Operating mode** 设置为 `eCAP`。

### **Event prescaler (integer from 0 to 31)** — 以 2 的倍数对输入信号进行预分频 `0`（默认） | scalar integer in [0 31]

输入信号按此参数值的两倍进行预分频。例如，如果你输入 `1`，则输入按 2 预分频；对于 `31`，输入按 62 预分频。输入 `0` 会绕过输入预分频器，使输入捕获信号保持不变。

### **Enable high resolution capture** — 选择以启用高分辨率捕获或 HRCAP 模式 `off`（默认） | `on`

选择 **Enable high resolution capture**（HRCAP 模式）参数以高分辨率捕获脉冲。

#### 依赖项

此参数仅适用于特定的 TI 处理器。

### **Enable continuous calibration mode** — 选择以启用连续校准模式 `off`（默认） | `on`

选择 **Enable continuous calibration mode** 参数以定期执行校准。

如果未启用连续校准模式，则校准仅发生一次（仅初始化）。高分辨率中断用于在内部监测校准状态，以获得更新后的比例因子，用于计算时间周期。因此，Hardware Interrupt 模块不能使用高分辨率中断。

校准过程提供比例因子，用于以 seconds 为单位计算高分辨率捕获值。

#### 依赖项

要启用此参数，请选择 **Enable high resolution capture** 参数。此参数仅适用于特定的 TI 处理器。

### **Calibration period in seconds** — 指定校准周期 `0.0016`（默认） | `on`

指定校准周期，以 seconds 为单位。

#### 依赖项

要启用此参数，请选择 **Enable high resolution capture** 参数和 **Enable continuous calibration mode**。此参数仅适用于特定的 TI 处理器。

### **Select mode control** — 捕获模式 `Continuous`（默认） | `One-Shot`

`Continuous` 选项使用循环缓冲区执行连续时间戳捕获（事件 1 到 4）。

`One-Shot` 选项启用 **Enable One-Shot rearming control via input port** 选项。

### **Enable One-Shot rearming control via input port** — 重新配置 One-Shot 捕获序列 `off`（默认） | `on`

选择此参数后，One-Shot 捕获序列按如下方式重新配置：

1. Mod4 计数器复位为 0。
2. Mod4 计数器解除冻结。
3. 启用捕获寄存器加载。

#### 依赖项

此参数仅在为 **Select mode control** 选择 `One-Shot` 时出现。

### **Stop value after** — 捕获停止之前的捕获事件数量 `Capture Event 1`（默认） | `Capture Event 2` | `Capture Event 3` | `Capture Event 4`

你希望捕获序列停止之前要经过的捕获事件数量。

### **Enable reset counter after capture event # time-stamp** — 在捕获事件后复位计数器 `off`（默认） | `on`

eCAP 过程在收到捕获事件时间戳后复位计数器。在此情况下，`#` 表示在 **Stop value after** 参数中设置的捕获事件编号。

### **Select capture event # polarity** — 在上升沿或下降沿启动捕获事件 `Rising Edge`（默认） | `Falling Edge`

启动捕获事件的选项。在此情况下，`#` 表示在 **Stop value after** 参数中设置的捕获事件编号。

### **Output type** — 选择 eCAP 的输出类型 `HRCLK/SYSCLK cycles`（默认） | `Microseconds`

选择 eCAP 的输出类型。

输出类型在 HRCAP 模式（高分辨率模式）下采用 HRCLK cycles 形式，在正常模式下采用 SYSCLK 形式。当你在 HRCAP 模式（高分辨率模式）下将输出类型设置为 HRCLK/SYSCLK cycles 时，会启用端口 **Scale factor**。

### **Time-Stamp counter data type** — 计数器的数据类型 `uint32`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

时间戳计数器的数据类型。

### **Enable capture event status flag output** — 输出捕获事件状态 `off`（默认） | `on`

在输出端口 **CF** 输出捕获事件状态标志。在捕获事件之前，模块输出 `0`。事件之后，标志值为 `1`。

### **Capture flag data type** — 输出端口 CF 的数据类型 `uint32`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

输出端口 **CF** 的数据类型。

#### 依赖项

此参数仅在选择 **Enable capture event status flag output** 时出现。

### **Enable overflow status flag output** — 输出 FIFO 缓冲区元素的状态 off（默认） | on

在输出端口 **OF** 输出 FIFO 缓冲区元素的状态。

### **Overflow flag data type** — 输出端口 OF 的数据类型 `uint32`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

输出端口 **OF** 的数据类型。

#### 依赖项

此参数仅在选择 **Enable overflow status flag output** 时出现。

### APWM

要启用 **APWM** 选项卡上的配置参数，请在 **常规** 选项卡上将 **Operating mode** 设置为 `APWM`。

### **Waveform period units** — 测量波形周期的单位 `Seconds`（默认） | `Clock cycles`

`Clock cycles` 使用处理器的高速外设时钟周期。

### **Waveform period source** — 获取波形周期值的来源 `Specify via dialog`（默认） | `Input port`

选择 `Specify via dialog` 可在 **Waveform period** 中输入值，或选择 `Input port` 以使用 **T** 输入端口的值。

### **Waveform period** — PWM 波形的周期 `0.001`（默认）

PWM 波形的周期，以 **Waveform period units** 中指定的 clock cycles 或 seconds 为单位。

**注意**

*clock cycles* 一词指的是 F2812 芯片上的高速外设时钟。默认情况下，该高速外设时钟为 75 MHz，因为高速外设时钟预分频器设置为 2（150 MHz/2）。

#### 依赖项

此参数仅在 **Waveform period source** 设置为 `Specify via dialog` 时出现。

### **Duty cycle units** — 测量占空比的单位 `Percentages`（默认） | `Clock cycles`

用于测量占空比的单位。

### **Duty cycle source** — 获取 PWM 波形占空比的来源 `Specify via dialog`（默认） | `Input port`

选择 `Specify via dialog` 可在 **Duty cycle** 中输入值，或选择 `Input port` 以使用 **W** 输入端口的值。

### **Duty cycle** — PWM 波形脉冲持续时间与 PWM 波形周期之比 50（默认）

PWM 波形脉冲持续时间与 PWM 波形周期之比。此比例以 **Duty cycle units** 表示。

### **Output polarity select** — 设置输出的有效电平 `Active High`（默认） | `Active Low`

当你选择 `Active High` 时，比较值（占空比）定义高电平时间。选择 `Active Low` 会使比较值定义低电平时间。

### 中断

### **Post interrupt on capture event #** — 将中断源设置为捕获事件 `off`（默认） | `on`

你可以使用 C28x Hardware Interrupt 模块响应该中断。在此情况下，`#` 表示在 **Stop value after** 参数中设置的捕获事件编号。

#### 依赖项

此参数仅在 **常规** 选项卡上将 **Operating mode** 设置为 `eCAP` 时出现。

### **Post interrupt on counter overflow** — 在计数器溢出时触发中断 `off`（默认） | `on`

当计数器溢出时触发中断。

#### 依赖项

此参数仅在 **常规** 选项卡上将 **Operating mode** 设置为 `eCAP` 时出现。

### **Post interrupt on counter equal period match** — 当计数器等于周期寄存器时发送中断 `off`（默认） | `on`

当计数器的值与周期寄存器的值相同时（CTR = PRD），发送中断。

#### 依赖项

此参数仅在 **常规** 选项卡上将 **Operating mode** 设置为 `APWM` 时出现。

### **Post interrupt on counter equal compare match** — 当计数器等于比较寄存器时发送中断 `off`（默认） | `on`

当计数器的值与比较寄存器的值相同时（CTR = CMP），发送中断。

#### 依赖项

此参数仅在 **常规** 选项卡上将 **Operating mode** 设置为 `APWM` 时出现。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

接收并记录捕获输入引脚上的跳变，或配置辅助脉冲宽度调制器

eCAP 模块捕获重要外部事件的时序，例如旋转机械速度测量中的霍尔传感器信号。当未在捕获模式下使用时，该模块可用于 APWM 模式，即单通道非对称脉冲宽度调制器（APWM）。可以为模型中的每个捕获引脚添加一个 eCAP 模块。不能将同一个 eCAP 引脚分配给模型中的两个 eCAP 模块。eCAP 和 APWM 模式使用相同的引脚。在 eCAP 模式下，这些引脚用作输入以捕获跳变。在 APWM 模式下，这些引脚用于输出 PWM 波形。

eCAP 模块中的高分辨率模式（HRCAP 模式）仅适用于特定的 TI 处理器。对于 F2803x 和 F2806x 处理器，请参阅 HRCAP 模块。
