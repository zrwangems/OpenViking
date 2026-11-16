---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'pwmoutput'
documentation_source_path: 'freedomboard/ref/pwmoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Output

## 端口

### 输入

### **Port\_1** — 占空比值标量

有效输入值的范围为 `0` 到 `100`。
该输入控制方波的占空比（方波的宽度）。

输入值 `0` 产生 0% 占空比，输入值 `100` 产生 100% 占空比。模块输入端口处任何超出范围的值（例如 `500` 或 `-500`）与最大或最小输入值具有相同的效果。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Pin** — 输出引脚，模块在该引脚上生成方波脉冲波形 `PTA5 (D5)`（默认） | `LED_RED` | `LED_GREEN` | `LED_BLUE` | `PTA1 (D0)` | `PTA2 (D1)` | `PTD4 (D2)` | `PTA12 (D3)` | `PTA4 (D4)` | `PTC8 (D6)` | `PTC9 (D7)` | `PTA13 (D8)` | `PTD5 (D9)` | `PTD0 (D10)` | `PTD2 (D11)` | `PTD3 (D12)` | `PTD1 (D13)` | `PTB0 (A0)` | `PTB1 (A1)` | `PTB2 (A2)` | `PTB3 (A3)` | `PTC2 (A4)` | `PTC1 (A5)` | `PTE20` | `PTE21` | `PTE22` | `PTE23` | `PTE29` | `PTE30` | `PTE31` | `PTC3` | `PTC4`

要查看板上的引脚映射，请点击 **View Pin Map**。在板上，每个 PWM 引脚连接到三个定时器 TPM0（Timer PWM Module）、TPM1 或 TPM2 中的一个。要了解定时器通道引脚组合，请参阅 **Timer/PWM module** 参数描述部分中的 Timer to Pin Mapping 表。

### **Timer/PWM module** — 生成 PWM 信号的定时器 `TPM0`（默认） | `TPM1` | `TPM2`

该板有三个定时器：TPM0、TPM1 和 TPM2。每个 PWM 引脚连接到这三个定时器之一。当您在 **Pin** 列表中选择一个引脚时，此参数将填充为该引脚连接到的定时器。例如，如果您选择 `PTA1 (D0)` 引脚，此参数将设置为 `TPM2`。

下表显示了定时器到引脚的映射。

在您的模型中，如果 PWM Output 模块有多个实例，请为每个模块实例使用不同的定时器通道组合。否则，您将收到一条错误消息，指示您为所有模块实例使用来自不同定时器通道组合的 GPIO 引脚。

例如，假设在一个 PWM Output 模块实例中，您选择 `PTC3` 引脚来生成输出。`PTC3` 引脚连接到 TPM0 定时器的 CH2 通道。在为 PWM Output 模块的其他实例选择引脚时，请选择属于 TPM0 CH2 以外的定时器通道组合的引脚。

#### 依赖项

此参数显示为灰显。

### **Initial duty cycle (0 - 100)** — 初始占空比 `0`（默认） | `integer between 0 and 100`

初始化时，模块将其占空比设置为您在此参数中指定的值。

### 示例

此示例说明如何使用 PWM Output 模块控制板上连接到 `D13` 引脚的蓝色 LED 的亮度。

1. 将 FRDM-KL25Z 硬件连接到您的计算机。
2. 在 Simulink® Editor 中，打开一个新的模型窗口。
   从 Library Browser 中，复制一个 Constant 模块和一个 PWM Output 模块，并将它们连接起来。
3. 将 Constant 模块的值设置为 `50`。此值表示输出方波的占空比，以百分比为单位。
4. 在 Block Parameter 对话框中，将 Pin 设置为 `D13`，并将 Initial duty cycle 设置为 `0`。
5. 在 Simulink Editor 中，选择 **Simulation** > **Model Configuration Parameters**。
6. 在 Configuration Parameters 对话框中，点击 **Hardware Implementation**。
7. 将 **Hardware board** 参数设置为 NXP FRDM-KL25Z。
8. 要设置输出信号的频率，请确定 `D13` 引脚连接到的定时器。

   要确定该定时器，请在 Block Parameter 对话框中点击 **View Pin Map**。在引脚图中，搜索 `D13` 引脚及其旁边的定时器名称。`D13` 引脚连接到 `TMP0` 引脚。
9. 在 Configuration Parameters 对话框中，将 **TPM0 Frequency (in Hz)** 设置为 `50`。使用该频率值，模块计算方波的周期。

   Period = 1/50 = 0.02 seconds

当您构建模型并将其加载到硬件上时，PWM Output 模块会生成脉冲宽度为 (50\* 0.02)/100 = 0.01 seconds 的方波脉冲。蓝色 LED 点亮 0.01 seconds，然后在接下来的 0.01 seconds 内熄灭。您可以使用 PWM Output 模块快速使 LED 亮灭，以控制其亮度。

## 所属库

Simulink Coder Support Package for NXP FRDM-KL25Z Board/FRDM-KL25Z

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

在指定输出引脚上生成方波

PWM Output 模块生成方波脉冲，并输出到板上指定的引脚。您可以将 0–100 之间的值作为模块输入。您提供的输入值控制脉冲波形的占空比。输入值 `0` 产生 0% 占空比，输入值 `100` 产生 100% 占空比。
