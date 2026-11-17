---
type: simulink-block
title: 'MCAN Interrupt Status'
family: 'f280015x'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280015x'
documentation_page: 'mcaninterruptstatus'
documentation_source_path: 'ref/mcaninterruptstatus.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Interrupt Status

## 端口

### 输出

### **MCAN\_IR** — MCAN 中断寄存器状态 uint32

输出端口，用于将整个 MCAN\_IR 寄存器状态显示为 uint32 值。

当检测到所列条件之一时（边沿敏感）会设置标志。标志保持置位，直到主机清除它们。通过向对应位位置写入 `1` 可清除标志。写入 `0` 无效。硬复位将清除该寄存器。

**MCAN\_IR 寄存器**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **位** | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31` |
| **类型** | `RF0N` | `RF0W` | `RF0F` | `RF0L` | `RF1N` | `RF1W` | `RF1F` | `RF1L` | `HPM` | `TC` | `TCF` | `TFE` | `TEFN` | `TEFW` | `TEFF` | `TEFL` | `TSW` | `MRAF` | `TOO` | `DRX` | `RESERVED` | `BEU` | `ELO` | `EP` | `EW` | `BO` | `WDI` | `PEA` | `PED` | `ARA` | `RESERVED` | `RESERVED` |

#### 依赖项

要启用此端口，请选择 **MCAN interrupt register output** 参数。

### **TEFN** — TX event FIFO 新条目状态 boolean

输出端口，用于显示发送（TX）事件先进先出（FIFO）新条目状态。状态端口输出：

- `0` - TX event FIFO 未变化
- `1` - TX 处理程序写入了 TX event FIFO 元素

#### 依赖项

要启用此端口，请选择 **TX event FIFO new element** 参数。

### **TEFW** — TX event FIFO watermark 到达状态 boolean

输出端口，用于显示 TX event FIFO watermark 到达状态。一旦该状态被清除且 FIFO 电平仍高于 watermark 电平，则该位不会使能。仅当从低到高变化时才会使能该位。状态端口输出：

- `0` - TX event FIFO 填充电平低于 watermark
- `1` - TX event FIFO 填充电平达到 watermark

#### 依赖项

要启用此端口，请选择 **TX event FIFO watermark** 参数。

### **TEFF** — TX event FIFO 满状态 boolean

输出端口，用于显示 TX event FIFO 满状态。状态端口输出：

- `0` - TX event FIFO 未满
- `1` - TX event FIFO 已满

#### 依赖项

要启用此端口，请选择 **TX event FIFO full** 参数。

### **TEFL** — TX event FIFO 元素丢失状态 boolean

输出端口，用于显示 TX event FIFO 元素丢失状态。状态端口输出：

- `0` - 无 TX event FIFO 元素丢失
- `1` - TX event FIFO 元素丢失，在尝试写入大小为 0 的 TX event FIFO 后也会置位

#### 依赖项

要启用此端口，请选择 **TX event FIFO element lost** 参数。

### **TC** — 传输完成状态 boolean

输出端口，用于显示传输完成状态。状态端口输出：

- `0` - 无传输完成
- `1` - 传输完成

#### 依赖项

要启用此端口，请选择 **Transmission complete** 参数。

### **TCF** — 传输取消完成状态 boolean

输出端口，用于显示传输取消完成状态。状态端口输出：

- `0` - 无传输取消完成
- `1` - 传输取消完成

#### 依赖项

要启用此端口，请选择 **Transmission cancellation finished** 参数。

### **TFE** — 发送 FIFO 空状态 boolean

输出端口，用于显示发送 FIFO 空状态。状态端口输出：

- `0` - TX FIFO 非空
- `1` - TX FIFO 为空

#### 依赖项

要启用此端口，请选择 **TX FIFO empty** 参数。

### **HPM** — 高优先级消息状态 boolean

输出端口，用于显示高优先级消息状态。状态端口输出：

- `0` - 未接收到高优先级消息
- `1` - 接收到高优先级消息

#### 依赖项

要启用此端口，请选择 **High priority message** 参数。

### **RF0N** — RX FIFO 0 新消息状态 boolean

输出端口，用于显示接收（RX）FIFO 0 新消息状态。状态端口输出：

- `0` - 未向 RX FIFO 0 写入新消息
- `1` - 向 RX FIFO 0 写入了新消息

#### 依赖项

要启用此端口，请选择 **RX FIFO 0 new message** 参数。

### **RF0W** — RX FIFO 0 watermark 到达状态 boolean

输出端口，用于显示接收（RX）FIFO 0 watermark 到达状态。一旦该状态被清除且 FIFO 电平仍高于 watermark 电平，则该位不会使能。仅当从低到高变化时才会使能该位。状态端口输出：

- `0` - RX FIFO 0 填充电平低于 watermark
- `1` - RX FIFO 0 填充电平达到 watermark

#### 依赖项

要启用此端口，请选择 **RX FIFO 0 watermark** 参数。

### **RF0FL** — RX FIFO 0 满状态 boolean

输出端口，用于显示接收（RX）FIFO 0 满状态。状态端口输出：

- `0` - RX FIFO 0 未满
- `1` - RX FIFO 0 已满

#### 依赖项

要启用此端口，请选择 **RX FIFO 0 full** 参数。

### **RF0ML** — RX FIFO 0 消息丢失状态 boolean

输出端口，用于显示 RX FIFO 0 消息丢失状态。状态端口输出：

- `0` - 无 RX FIFO 0 消息丢失
- `1` - RX FIFO 0 消息丢失，在尝试写入大小为 0 的 RX FIFO 0 后也会置位

#### 依赖项

要启用此端口，请选择 **RX FIFO 0 message lost** 参数。

### **DRX** — dedicated RX buffer 消息状态 boolean

消息存储到 dedicated RX buffer。只要接收到的消息已存储到 dedicated RX Buffer，就会设置该标志。

状态端口输出：

- `0` - 未更新 RX buffer
- `1` - 至少有一条接收到的消息存储到 RX buffer

#### 依赖项

要启用此端口，请选择 **Dedicated RX buffer message** 参数。

### **RF1N** — RX FIFO 1 新消息状态 boolean

输出端口，用于显示接收（RX）FIFO 1 新消息状态。状态端口输出：

- `0` - 未向 RX FIFO 1 写入新消息
- `1` - 向 RX FIFO 1 写入了新消息

#### 依赖项

要启用此端口，请选择 **RX FIFO 1 new message** 参数。

### **RF1W** — RX FIFO 1 watermark 到达状态 boolean

输出端口，用于显示接收（RX）FIFO 1 watermark 到达状态。一旦该状态被清除且 FIFO 电平仍高于 watermark 电平，则该位不会使能。仅当从低到高变化时才会使能该位。状态端口输出：

- `0` - RX FIFO 1 填充电平低于 watermark
- `1` - RX FIFO 1 填充电平达到 watermark

#### 依赖项

要启用此端口，请选择 **RX FIFO 1 watermark reached** 参数。

### **RF1FL** — RX FIFO 1 满状态 boolean

输出端口，用于显示接收（RX）FIFO 1 满状态。状态端口输出：

- `0` - RX FIFO 1 未满
- `1` - RX FIFO 1 已满

#### 依赖项

要启用此端口，请选择 **RX FIFO 1 full** 参数。

### **RF1ML** — RX FIFO 1 消息丢失状态 boolean

输出端口，用于显示 RX FIFO 1 消息丢失状态。状态端口输出：

- `0` - 无 RX FIFO 1 消息丢失
- `1` - RX FIFO 1 消息丢失，在尝试写入大小为 0 的 RX FIFO 1 后也会置位

#### 依赖项

要启用此端口，请选择 **RX FIFO 1 message lost** 参数。

### **TSW** — 时间戳回绕状态 boolean

输出端口，用于显示时间戳回绕状态。状态端口输出：

- `0` - 无 timestamp counter 回绕
- `1` - Timestamp counter 发生回绕

#### 依赖项

要启用此端口，请选择 **Timestamp wraparound** 参数。

### **TOO** — 超时发生状态 boolean

输出端口，用于显示超时发生状态。状态端口输出：

- `0` - 无超时
- `1` - 达到超时

#### 依赖项

要启用此端口，请选择 **Timeout occurred** 参数。

### **ELO** — 错误记录溢出状态 boolean

输出端口，用于显示错误记录溢出状态。状态端口输出：

- `0` - CAN error logging counter 未溢出
- `1` - 发生 CAN error logging counter 溢出

#### 依赖项

要启用此端口，请选择 **Error logging overflow** 参数。

### **EW** — 错误警告状态 boolean

输出端口，用于显示错误警告状态。状态端口输出：

- `0` - Error warning 状态未变化
- `1` - Error warning 状态已变化

#### 依赖项

要启用此端口，请选择 **Warning status** 参数。

### **WD** — watchdog 事件状态 boolean

输出端口，用于显示 watchdog 事件状态。状态端口输出：

- `0` - 未发生 Message RAM watchdog 事件
- `1` - 由于 missing ready 导致 Message RAM watchdog 事件

#### 依赖项

要启用此端口，请选择 **Watchdog event** 参数。

### **PED** — 数据阶段协议错误状态 boolean

数据阶段协议错误（使用 Data Bit Time）

输出端口，用于显示数据阶段协议错误状态。状态端口输出：

- `0` - 数据阶段无协议错误
- `1` - 检测到数据阶段协议错误

#### 依赖项

要启用此端口，请选择 **Data protocol error** 参数。

### **MRAF** — Message RAM 访问失败状态 boolean

当 RX Handler 出现以下情况时，会设置该标志：

- 在收到下一条消息的仲裁字段之前，尚未完成验收滤波或对已接受消息的存储。在这种情况下，验收滤波或消息存储会被中止，并且 RX Handler 会开始处理下一条消息。
- 无法将消息写入 Message RAM。在这种情况下，消息存储会被中止。

在这两种情况下，FIFO put index 均不会相应更新。专用 RX Buffer 的新数据标志不会被设置；当下一消息存储到该位置时，部分存储的消息会被覆盖。

当 Tx Handler 无法及时从 Message RAM 读取消息时，会设置该标志。在这种情况下，消息传输会被中止。如果发生 TX Handler 访问失败，MCAN 会切换到 Restricted Operation Mode。

输出端口，用于显示 Message RAM 访问失败状态。状态端口输出：

- `0` - 未发生 Message RAM 访问失败
- `1` - 发生 Message RAM 访问失败

#### 依赖项

要启用此端口，请选择 **Message RAM access failure** 参数。

### **BEU** — 位错误未纠正状态 boolean

位错误未纠正。检测到 Message RAM 位错误，未纠正。当连接到 Message RAM 的 ECC aggregator 检测到双位错误时，会设置该位。未纠正的 Message RAM 位错误会将 CCCR.INIT 设置为 `1`。这样做是为了避免传输损坏的数据。

输出端口，用于显示位错误未纠正状态。状态端口输出：

- `0` - 从 Message RAM 读取时未检测到位错误
- `1` - 检测到位错误，未纠正（例如 parity logic）

#### 依赖项

要启用此端口，请选择 **Bit error uncorrected** 参数。

### **EP** — error passive 状态 boolean

输出端口，用于显示 error passive 状态。状态端口输出：

- `0` - Error passive 状态未变化
- `1` - Error passive 状态已变化

#### 依赖项

要启用此端口，请选择 **Error passive status** 参数。

### **BO** — bus off 状态 boolean

输出端口，用于显示 bus off 状态。状态端口输出：

- `0` - Bus off 状态未变化
- `1` - Bus off 状态已变化

#### 依赖项

要启用此端口，请选择 **Bus off status** 参数。

### **PEA** — 仲裁协议错误状态 boolean

仲裁阶段协议错误（使用 Nominal Bit Time）

输出端口，用于显示仲裁协议错误状态。状态端口输出：

- `0` - 仲裁阶段无协议错误
- `1` - 检测到仲裁阶段协议错误

#### 依赖项

要启用此端口，请选择 **Arbitration protocol error** 参数。

### **ARA** — 保留地址访问状态 boolean

输出端口，用于显示保留地址访问状态。状态端口输出：

- `0` - 未发生对保留地址的访问
- `1` - 发生对保留地址的访问

#### 依赖项

要启用此端口，请选择 **Reversed address access** 参数。

## 参数

R2025b 中未记录。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

输出 MCAN 中断寄存器的特定位或整个寄存器

MCAN Interrupt Status 模块输出 MCAN\_IR 寄存器的特定位或整个 MCAN\_IR 寄存器。读取特定位或整个 MCAN\_IR 寄存器后，寄存器值会被清除。

选择 `MCAN interrupt register output` 参数可输出整个 MCAN 中断寄存器。

如果未选择 `MCAN interrupt register output` 参数，则该模块会根据 `Transmit sources`、`Receive sources` 和 `General sources` 中的选择，输出 MCAN\_IR 寄存器中的特定位。

在配置参数中配置接收、发送和其他中断源。有关更多信息，请参阅 Model Configuration Parameters for Texas Instruments C2000 Processors。
