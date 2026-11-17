---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'hardwareinterruptblock'
documentation_source_path: 'ref/hardwareinterruptblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口
```yaml
ports:
- name: '*name* Event Task'
  summary: 函数调用事件输入仿真标量
  direction: input
- name: '*name* Event'
  summary: 生成中断请求 Scalar
  direction: output
```

### 输入

### ***`name`* Event Task** — 函数调用事件输入仿真标量

仅用于仿真的消息输入端口，当连接到 Function-Call Generator 模块时，该模块在仿真中作为直通模块，输出通过 ***`name`* Event** 端口发出。

#### 依赖

要启用此端口，请选择 **Enable simulation port** 参数。

### 输出

### ***`name`* Event** — 生成中断请求 `Scalar`

该模块的输出是函数调用。函数调用输出的数量将与选择在 ISR 中服务的事件数量相同。
## 参数
```yaml
parameters:
- name: Number of events to serve
  summary: 指定要服务的事件数量 1（默认）| 2 | 3 | <32
  group: ''
- name: Simulink task priority
  summary: 设置所选 ISR 的优先级 50（默认）| 正整数或非负整数
  group: ''
- name: Disable interrupt pre-emption
  summary: 选择以禁用中断抢占 off（默认）| on
  group: ''
- name: Enable simulation port
  summary: 启用仿真端口以进行阻塞 off（默认）| on
  group: ''
```

### **Number of events to serve** — 指定要服务的事件数量 `1`（默认）| `2` | `3` | `<32`

指定 Hardware Interrupt 模块要服务的事件数量。此参数将指定数量的事件启用为输出端口 `event#`

### **Simulink task priority** — 设置所选 ISR 的优先级 `50`（默认）| `正整数或非负整数`

在此参数中指定的值用于设置下游函数调用子系统的优先级。所选（ISR）的 Simulink 任务优先级相对于模型基础速率优先级。

**注意**

默认模型基础采样率优先级设置为 40，较低的优先级值表示较高的优先级任务。要实现这一点，必须在 **Configuration Parameters** > **Solver** 窗格中启用 **Higher priority value indicates higher task priority** 选项。

### **Disable interrupt pre-emption** — 选择以禁用中断抢占 `off`（默认）| `on`

默认情况下，中断可以被更高优先级的中断抢占。选择此选项允许低优先级中断完成其执行而不被其他中断抢占。

### **Enable simulation port** — 启用仿真端口以进行阻塞 `off`（默认）| `on`

选择此参数以添加兼容的仿真输入端口。
## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块在模型的生成代码中自动创建中断服务例程（ISR）。ISR 执行与该模块事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 优先级相同的优先级运行。

使用此模块，您可以：

- 创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。
- 使用 Hardware Mapping 工具配置所需的事件或中断。

**Hardware Mapping** 工具允许您为所选硬件板配置硬件中断任务。使用此工具，您可以将软件模型中的任务映射到可用的事件源和中断：

- 在 **Mapping Browser** > **Tasks** > **`CPU name`** 中手动选择任务。选择所需的事件或中断源。更多信息，请参阅 Configure Interrupts and Events Using Hardware Mapping
