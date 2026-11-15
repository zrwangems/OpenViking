---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / System Core'
documentation_page: 'hardwareinterruptblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/hardwareinterruptblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口

### 输入

### ***`name`* Event Task** — 函数调用事件输入仿真标量

仅用于仿真的消息输入端口，当连接到 Function-Call Generator 模块时，该模块在仿真中充当直通，并在 ***`name`* Event** 端口上发出输出。

#### 依赖项

要启用此端口，请选择 **Enable simulation port** 参数。
### 输出

### ***`name`* Event** — 生成中断请求 `Scalar`

此模块的输出是函数调用。函数调用输出的数量将与在 ISR 中选择服务的事件数量相同。

## 参数

### **Interrupt group** — 选择外设 ISR `External interrupts (EXTI)`（默认）| `Analog to digital converter (ADC)` | `Pulse width modulation (PWM)` | `Direct memory access (DMA)`

**Interrupt group** 列出 **STM32 Processor Based Boards** 可用的同一类型外设的所有 ISR。选择中断组会更改 **Interrupt name** 参数中的值列表。

### **Interrupt name** — 选择 ISR `EXTI0_IRQHandler`（默认）| `ADC_IRQHandler` | `TIM1_BRK_TIM9_IRQHandler` | `DMA0_Stream0_IRQHandler`

**Interrupt name** 指定要为 Hardware Interrupt 模块生成的 ISR。**Interrupt name** 对应于处理器中断向量表中的特定条目。可用的 ISR 取决于中断组。

### **Interrupt number** — ISR 在中断表中的位置 `21`（默认）| `33` | `71` | `…`

此只读参数指示所选 ISR 在目标硬件中断向量表中的位置。

### **Events to serve** — 选择事件 `EXTI0 Event`（默认）| `ADC1 OVR` | `Stream0 TC` | `…`

从 **Events to serve** 组中选择事件或自定义事件及其各自的事件执行顺序，以便为所选 **Interrupt name** 服务事件。您可以选择自定义事件与其他所选事件一起执行。有关详细信息，请参阅限制。

### **Simulink task priority** — 设置所选 ISR 的优先级 `30`（默认）| `positive integer or nonnegative integer`

您在此参数中指定的值设置下游函数调用子系统的优先级。所选 (ISR) 的 Simulink® 任务优先级相对于模型基速率优先级。

**注意**

默认模型基本采样率优先级设置为 40，其中较低的优先级值表示较高优先级的任务。为此，必须在 **Configuration Parameters** > **Solver** 窗格中启用 **Higher priority value indicates higher task priority** 选项。

### **Run interrupt service routine as atomic unit** — 选择以禁用中断抢占 `off`（默认）| `on`

启用 Run interrupt service routine as atomic unit 以在执行所选中断服务例程时阻塞所有其他中断。

### **Clear status after servicing each event** — 选择以清除中断状态标志 `off`（默认）| `on`

选择此参数以在执行每个事件后清除中断服务例程中的事件状态。

### **Enable simulation port** — 为模块启用仿真端口 `off`（默认）| `on`

选择此参数以添加 SoC Blockset™ 兼容的仿真输入端口。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块在模型的生成代码中自动创建中断服务例程 (ISR)，以响应所选事件。ISR 执行与模块事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 优先级相同的优先级运行。

使用此模块，您可以：

- 在 STM32 Processor Based Boards 上创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。

此模块仅为指定的 ISR 和所选事件生成代码。要更改配置，请启用中断和特定触发选项，以使用所选外设的设置。

例如，要在 Hardware Interrupt 模块上为 ADC 外设创建 ISR：

- 模型必须具有 **Analog to digital Converter** (ADC) 模块。
- 要从 ADC 触发 ISR，请在 **Configuration Parameters > Hardware Implementation > Target Hardware Resources > ADC1** 中选择 **Enable Regular EoCS Interrupt** 或 **Enable Injected EoCS Interrupt** 复选框。如果您的模型没有 Analog to Digital Converter 模块，则选择此复选框不起作用。
- 从 Hardware Interrupt 模块的 **Interrupt group** 参数中选择 `Analog to digital converter (ADC)`，并在 **Interrupt name** 参数中选择 `ADCIRQ_Handler`。
- 在 **Events to serve** 参数中选择 `ADC1 Reg EoCS` 或 `ADC1 Inj EoCS` 事件名称。

当您选择必要的 Hardware Interrupt 模块设置时，会为 DMA 和 Watchdog 中断自动触发 ISR，因为在 **Configuration Parameters** > **Hardware Implementation** > **Target Hardware Resources** > **ADC** 中，**DMA transfer complete interrupt is enabled** 和 **Watchdog interrupt is enabled** 复选框默认处于选中状态。

**注意**

对于 STM32H7xx 系列处理器，STM32CubeMX 6.2.0 版本为启用外部中断生成的代码不会将所选 GPIO 引脚配置为输入模式。要在所选 GPIO 引脚上触发外部中断，请添加自定义代码以将引脚模式配置为 **input**。

您可以使用模型中的 **System Initialize** 模块来添加自定义代码。

例如，要启用引脚 **PD3** 上的 **EXTI3** 中断。

- 在 STM32CubeMX 工程中将 **PD3** 引脚配置为 **GPIO\_EXTI3**。
- 在模型中添加 **System Initialize** 模块。
- 在 System Initialize 模块的 System Initialize Function Execution Code 部分中指定以下自定义代码。这会将引脚 PD3 配置为输入模式。

  ```
  LL_GPIO_SetPinMode(GPIOD, LL_GPIO_PIN_3, LL_GPIO_MODE_INPUT);
  ```

ISR 在 `model_interrupts.c` 文件中生成。

要详细了解何时不应使用自定义事件，请参阅限制。
