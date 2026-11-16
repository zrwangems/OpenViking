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
language: en
---

# Hardware Interrupt

## Ports

### Input

### ***`name`* Event Task** — Function-call event input simulation scalar

The simulation-only message input port, when connected to an Function-Call Generator block, the block acts as
pass-through with the output emitted on the
***`name`* Event** port
in simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter.
### Output

### ***`name`* Event** — Generate interrupt request `Scalar`

The output of this block is a function-call. The number of function
call outputs will be same as events selected to serve in an ISR.

## Parameters

### **Interrupt group** — Select a peripheral ISR `External interrupts (EXTI)` (default) | `Analog to digital converter (ADC)` | `Pulse width modulation (PWM)` | `Direct memory access (DMA)`

Interrupt group lists all the ISR for a same type of peripherals available
for **STM32 Processor Based Boards**. Selecting an
interrupt group changes the list of values in the **Interrupt name**parameter.

### **Interrupt name** — Select ISR `EXTI0_IRQHandler` (default) | `ADC_IRQHandler` | `TIM1_BRK_TIM9_IRQHandler` | `DMA0_Stream0_IRQHandler`

The **Interrupt name** specifies the ISR to be generated
for the hardware interrupt block. The **Interrupt name**
corresponds to the specific entry in the processor's interrupt vector table.
The available ISRs depend on the interrupt group.

### **Interrupt number** — Position of ISR in interrupt table `21` (default) | `33` | `71` | `…`

This read-only parameter indicates the position of the selected ISR in the
interrupt vector table of your target hardware.

### **Events to serve** — Select events `EXTI0 Event` (default) | `ADC1 OVR` | `Stream0 TC` | `…`

Select events or custom event and there respective events execution order
from the **Events to serve** group to service events for
the selected **Interrupt name**. You can select custom
events to execute along with the other selected events. For more
information, see Limitations.

### **Simulink task priority** — Set priority of selected ISR `30` (default) | `positive integer or nonnegative integer`

The value you specify in this parameter sets the priority of the
downstream function-call subsystem. The Simulink® task priority of the selected (ISR) is relative to the model
base rate priority.

**Note**

The default model base sample rate priority is set to 40 with a
lower priority value indicating a higher priority task. To achieve
this the **Higher priority value indicates higher task
priority** option must be enabled in
**Configuration Parameters** >
**Solver** pane.

### **Run interrupt service routine as atomic unit** — Select to disable interrupt preemption `off` (default) | `on`

Enable Run interrupt service routine as atomic unit to block all other
interrupts while executing the selected interrupt service routine.

### **Clear status after servicing each event** — Select to clear interrupt status flags `off` (default) | `on`

Select this parameter to clear event status in interrupt service routine
after executing each event.

### **Enable simulation port** — Enable simulation ports to block `off` (default) | `on`

Select this parameter to add an SoC Blockset™ compatible simulation input port.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Trigger downstream function-call subsystems from interrupt service routine

Use the Hardware Interrupt block to create an interrupt service routine
(ISR) automatically in the generated code of your model to react to the events selected.
The ISR executes the downstream function-call subsystem associated with event ports of
the block.

The function call subsystem associated with the event output port run at same priority
as that of ISR priority.

Using this block you can:

- Create ISRs on STM32 Processor Based Boards.
- Set ISR priority.
- Enable or disable interrupt preemption.

This block generates code only for the specified ISR and selected events. To change
the configuration, enable the interrupt and specific triggering options to use the
settings of the chosen peripheral.

For example, to create an ISR for the ADC peripheral on the Hardware Interrupt block:

- Model must have an **Analog to digital Converter** (ADC)
  block.
- To trigger an ISR from a ADC, select the **Enable Regular EoCS
  Interrupt** or **Enable Injected EoCS
  Interrupt** check box in **Configuration Parameters >
  Hardware Implementation > Target Hardware Resources > ADC1**.
  Selecting this check box has no effect if your model does not have a Analog
  to Digital Converter block.
- Select `Analog to digital converter (ADC)` in the
  **Interrupt group** parameter and
  `ADCIRQ_Handler` in the **Interrupt
  name** parameter from the hardware interrupt block.
- Select `ADC1 Reg EoCS` or `ADC1 Inj
  EoCS` event name in the **Events to serve**
  parameter.

An ISR for a DMA and Watchdog interrupt is automatically triggered when you choose the
necessary Hardware Interrupt block settings because the **DMA
transfer complete interrupt is enabled** and **Watchdog interrupt
is enabled** check box is selected by default in **Configuration
Parameters** > **Hardware Implementation** >
**Target Hardware Resources** > **ADC**.

**Note**

For STM32H7xx based processors, the code generated by STM32CubeMX 6.2.0
version for enabling external interrupt does not configure the selected GPIO pin
in input mode. To trigger the external interrupt on selected GPIO pin, add
custom code to configure the pin mode as **input**.

You can use **System Initialize** block in the model to add
the custom code.

For example, to enable the **EXTI3** interrupt on pin
**PD3**.

- Configure **PD3** pin as
  **GPIO\_EXTI3** in STM32CubeMX project.
- Add a **System Initialize** block in your
  model.
- Specify the following custom code in the System Initialize
  Function Execution Code section of the System
  Initialize block. This configures the pin PD3 in input
  mode.

  ```
  LL_GPIO_SetPinMode(GPIOD, LL_GPIO_PIN_3, LL_GPIO_MODE_INPUT);
  ```

The ISR's are generated in the `model_interrupts.c` file.

To know more about when not to use the custom event, refer to Limitations.
