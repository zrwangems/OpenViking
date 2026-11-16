---
type: simulink-block
title: 'Memory Channel'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'memorychannel'
documentation_source_path: 'ref/memorychannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory Channel

## 端口

### 输入

### **wrData** — 写入器数据总线信号 标量 | 向量 | 矩阵

此信号包含要写入存储器的数据。

**注意**

当 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA` 时，此端口以消息形式从连接的 Stream Write 模块接收输入数据。有关消息的详细信息，请参阅 Messages。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **wrCtrlIn** — 写入器输入控制信号总线

此端口表示从数据生产者到存储器通道的协议。Memory Channel 模块在使用 **wrData** 时检查此信号。总线上的信号取决于 **Channel type** 参数。使用 SoC Bus Creator 模块创建此控制总线。有关总线类型的详细信息，请参阅 External Memory Channel Protocols。

| 通道类型配置 | 总线类型 |
| --- | --- |
| `AXI4-Stream to Software via DMA` | `StreamM2SBusObj` |
| `AXI4 Stream FIFO` | `StreamM2SBusObj` |
| `AXI4 Stream Video FIFO` | `pixelcontrol` |
| `AXI4 Stream Video Frame Buffer` | `pixelcontrol` |
| `AXI4 Random Access` | `WriteControlM2SBusObj` |

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA` 以外的值。

**数据类型：** `StreamM2SBusObj` | `pixelcontrol` | `WritecontrolM2SBusObj`

### **rdCtrlIn** — 读取器输入控制信号总线

此端口接受来自数据消费者模块的总线，指示消费者模块已准备好接受读取数据。对于流协议，**rdCtrlIn** 端口是从数据消费者到 Memory Channel 模块的反压信号。对于 `AXI4 Random Access` 协议，此输入是来自读取器的读请求。总线上的信号取决于 **Channel type** 参数。使用 SoC Bus Creator 模块创建此控制总线。

| 通道类型配置 | 总线类型 |
| --- | --- |
| `Software to AXI4-Stream via DMA` | `StreamS2MBusObj` |
| `AXI4 Stream FIFO` | `StreamS2MBusObj` |
| `AXI4 Stream Video FIFO` | `StreamVideoS2MBusObj` |
| `AXI4 Stream Video Frame Buffer` | `StreamVideoFSyncS2MBusObj` |
| `AXI4 Random Access` | `ReadControlM2SBusObj` |

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA` 以外的值。

**数据类型：** `StreamS2MBusObj` | `StreamVideoS2MBusObj` | `StreamVideoFSyncS2MBusObj` | `ReadControlM2SBusObj`

### **rdDone** — 完成读取的通知消息 标量

此消息端口从连接的 Stream Read 模块接收通知。该通知指示读事务已完成。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA`。

**数据类型：** `Boolean`

### **wrBurstDone** — 来自存储器控制器的写入器控制输入 标量

此消息端口从连接的 Memory Controller 模块接收控制消息，指示所请求的突发事务已完成。将 Memory Controller 模块的 **burstDone** 输出信号连接到此端口。有关消息的详细信息，请参阅 Messages。

**数据类型：** `BurstRequest2BusObj`

### **rdBurstDone** — 来自存储器控制器的读取器控制输入 标量

此消息端口从连接的 Memory Controller 模块接收控制消息，指示所请求的突发事务已完成。将 Memory Controller 模块的 **burstDone** 输出信号连接到此端口。有关消息的详细信息，请参阅 Messages。

**数据类型：** `BurstRequest2BusObj`
### 输出

### **rdData** — 输出到数据消费者的数据信号 标量 | 向量 | 矩阵

此信号包含从存储器读取的数据。

**注意**

当 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA` 时，此端口以消息形式将输出数据发送到连接的 Stream Read 模块。有关消息的详细信息，请参阅 Messages。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **rdEvent** — 任务读取事件信号 标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动读取。

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA`。

**数据类型：** `rteEvent`

### **wrEvent** — 任务写入事件信号 标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动写入。

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA`。

**数据类型：** `rteEvent`

### **wrDone** — 存储器中缓冲区已释放的通知 标量

此消息端口向连接的 Stream Write 模块发送通知。该通知指示读事务已完成，并且存储器中的缓冲区可用于写入。

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA`。

**数据类型：** `Boolean`

### **rdCtrlOut** — 从存储器通道到数据消费者的读取器控制信号 总线

从通道到数据消费者的控制信号。此信号的内容取决于 `Channel type` 参数。将此信号连接到数据消费者。使用 SoC Bus Selector 模块从总线中分离该信号。

| 通道类型配置 | 总线类型 |
| --- | --- |
| `Software to AXI4-Stream via DMA` | `StreamM2SBusObj` |
| `AXI4 Stream FIFO` | `StreamM2SBusObj` |
| `AXI4 Stream Video FIFO` | `pixelcontrol` |
| `AXI4 Stream Video Frame Buffer` | `pixelcontrol` |
| `AXI4 Random Access` | `ReadControlS2MBusObj` |

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA` 以外的值。

**数据类型：** `StreamM2SBusObj` | `ReadControlS2MBusObj` | `pixelcontrol`

### **wrCtrlOut** — 从存储器通道到数据生产者的写入器控制信号 总线

此总线表示从存储器通道到数据生产者的协议总线。总线上的信号取决于 **Channel type** 参数。使用 SoC Bus Selector 模块从总线中分离该信号。

| 通道类型配置 | 总线类型 |
| --- | --- |
| `AXI4-Stream to Software via DMA` | `StreamS2MBusObj` |
| `AXI4 Stream FIFO` | `StreamS2MBusObj` |
| `AXI4 Stream Video FIFO` | `StreamVideoS2MBusObj` |
| `AXI4 Stream Video Frame Buffer` | `StreamVideoS2MBusObj` |
| `AXI4 Random Access` | `WriteControlS2MBusObj` |

#### 依赖关系

要启用此端口，请将 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA` 以外的值。

**数据类型：** `StreamS2MBusObj` | `WriteControlS2MBusObj` | `StreamVideoS2MBusObj`

### **wrBurstReq** — 写突发请求 标量

此消息端口发送控制信号，请求从存储器控制器进行突发访问。将其连接到 Memory Controller 模块的 **burstReq** 输入。有关消息的详细信息，请参阅 Messages。

**数据类型：** `BurstRequestBusObj`

### **rdBurstReq** — 读突发请求 标量

此消息端口发送控制信号，请求从存储器控制器进行突发访问。将其连接到 Memory Controller 模块的 **burstReq** 输入。有关消息的详细信息，请参阅 Messages。

**数据类型：** `BurstRequestBusObj`

## 参数

### **Hardware board** — 查看或修改当前硬件设置 只读：所选硬件板的名称

此参数为只读。

此参数显示指向当前所选硬件板的链接。点击该链接以打开配置参数，调整设置，或选择其他硬件板。

要了解有关配置参数的详细信息，请参阅 FPGA design (mem channels)。

### **Show implementation info** — 查看通道信息 只读：文本窗口

此参数为只读。

此参数显示指向特定于该模型的实现信息的链接。点击该链接查看信息（在新窗口中打开）。

### **Enable memory simulation** — 控制存储器仿真精度 `on`（默认） | `off`

选择此参数可启用高精度存储器仿真。清除此参数可获得更快的仿真性能。

- `on` — 该模块以突发精度模拟存储器事务。构造突发并对其进行仲裁以访问存储器。
- `off` — 存储器事务为纯行为级，允许快速仿真。

要查看使用此功能的示例，请转到 Accelerate SoC Simulation by Varying Abstraction Levels。

### 主要

### **Channel type** — 选择通道协议 `AXI4-Stream FIFO`（默认） | `AXI4-Stream to Software via DMA` | `Software to AXI4-Stream via DMA` | `AXI4-Stream Video FIFO` | `AXI4-Stream Video Frame Buffer` | `AXI4 Random Access`

指定通道的协议。选择以下值之一：

- AXI4-Stream to Software via DMA
- Software to AXI4-Stream via DMA
- AXI4 Stream FIFO
- AXI4 Stream Video FIFO
- AXI4 Stream Video Frame Buffer
- AXI4 Random Access

**注意**

对于以下配置，可以使用简化的存储器模块（推荐）：

- AXI4-Stream to Software via DMA — 使用 AXI4-Stream to Software 模块。
- Software to AXI4-Stream via DMA — 使用 Software to AXI4-Stream 模块。
- AXI4 Stream Video Frame Buffer — 使用 AXI4 Video Frame Buffer 模块。
- AXI4 Random Access — 使用 AXI4 Random Access Memory 模块。

这些模块为每种通道类型提供预配置且简化的视图。

有关存储器通道协议的更多信息，请参阅 External Memory Channel Protocols。

### **Region size (bytes)** — 为区域分配的存储器大小，以 bytes 为单位 只读：计算结果

此参数为只读。

区域的大小，以 bytes 为单位。此值按缓冲区数量乘以缓冲区大小计算。

**示例：** 如果 Buffer size 为 1024，且缓冲区数量设置为 8，则 Region size 为 8192。

### **Buffer size (bytes)** — 缓冲区大小，以 bytes 为单位 1024（默认） | 标量

指定区域中每个缓冲区的大小，以 bytes 为单位。

设置突发和缓冲区大小时，适用以下规则。

1. 给定通道接口的 Burst Length（以 bytes 计算）必须小于 4096 bytes。要计算以 bytes 为单位的突发大小，将通道接口标量数据类型转换为 bytes，然后乘以 Burst Length。
2. Burst Length 可以设置为大于 256，但如果生成到基于 AXI 的目标平台，则会发出警告。基于 AXI 的存储器系统最大突发长度为 256。
3. Channel Length 必须是突发长度的整数倍，或者突发长度必须是 Channel Length 的整数倍。也就是说，必须能够将传入的通道数据分块为整数个突发，或者将整数个传入通道数据集中到单个突发中。
4. Buffer Size 必须是整数个突发。对于写入器的突发大小（在其 Burst Length 转换为 bytes 之后）和读取器的突发大小（在其 Burst Length 转换为 bytes 之后），这都必须成立。
5. 缓冲区中计算出的突发数量不得超过 5000。这是基于存储器模型内部事件处理的临时限制。对于具有大缓冲区大小（例如 1080p 视频帧）的共享存储器区域以及指定较小突发大小的通道接口，可能会发生这种情况。通常，对于较大的帧，必须使用接近 4096 byte 限制的突发大小。
6. 通道接口的标量数据类型转换为展平通道数据宽度（即实现中的 *tdata*）后，不得超过 128 bits。

下表提供了良好和不良参数集的示例。

**突发和缓冲区参数示例**

| 通道数据类型 | 通道维度 | Burst Length | Burst Size | 好 / 坏 | 原因？ |
| --- | --- | --- | --- | --- | --- |
| uint8 | [1 1] | 1024 | 2048 | 好 | 这是一个简单的 8 位数据事务。 |
| uint8 | [1 3] | 1024 | 4096 | 好 | 这可能表示来自 Vision HDL Toolbox 模块的 RGB 像素。它被转换为 24 位打包数据，并填充 8 位以成为到存储器的 32 位（4-Byte）*tdata* 总线。Burst size 为 1024\*4B = 4096B。 |
| fixdt(0,10,0) | [1 3] | 1024 | 4096 | 好 | 这被转换为带有 2 位填充的 30 位打包像素。 |
| fixdt(0,12,0) | [1 3] | 1024 | 8192 | 好 | 这会产生 36 位打包像素，其扩展为 64 位 *tdata*。此数据符合当前 128 位 *tdata* 的限制。 |
| fixdt(0,48,0) | [1 3] | 1024 | 8192 | 坏 | 这会产生 144 位打包像素，违反当前 128 位 *tdata* 的限制。 |
| uint8 | [120 160 3] | 1024 | 4096 | 坏 | 标量数据为 24 位，填充为 32 位 *tdata*。Channel Length 为 120\*160=19200。突发长度 1024 不能整除 19200。 |
| uint8 | [120 160 3] | 120 | 480 | 好 | 标量数据为 24 位，填充为 32 位 *tdata*。Channel Length 为 120\*160，由于突发长度为 120，Channel length 的大小为 160 个突发。缓冲区大小正好为 1 帧（120\*160\*4），以 bytes 计算。 |

### **Number of buffers** — 区域中的缓冲区数量 8（默认） | 整数

将区域划分为缓冲区。读取器和写入器之间的速率差异会减慢较快的设备。例如，慢速读取器会导致写入器耗尽缓冲区并阻塞写入器，从而实际上减慢到读取器的速率。同样，慢速写入器会导致读取器耗尽缓冲区并阻塞读取器，从而实际上减慢到写入器的速率。

- 指定 `1` – 使用单个缓冲区时，控制访问以确保先写入一个缓冲区，然后读取它，然后写入下一个缓冲区，依此类推。
- 指定 `2`：使用两个缓冲区时，存储器访问以来回模式切换。写入器写入第一个缓冲区，然后，在读取器读取它时，写入器可以写入第二个缓冲区。
- 指定 `N` – 使用 *`N`* 个缓冲区时，存储器访问具有环形缓冲区模式。只要缓冲区可用，写入器就可以持续写入。当一个缓冲区完成时，它变为可供读取器使用。写入器和读取器以循环模式遍历 N 个缓冲区。只要写入器和读取器保持相似的速率，缓冲就可以防止阻塞。

#### 限制

当将 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA` 或 `Software to AXI4-Stream via DMA` 时，**Number of buffers** 参数必须是 3 到 64 之间的整数。

### **Burst length** — 存储器事务的突发长度 1（默认） | 标量

此连接在存储器总线上的突发长度，以标量数据为单位。标量单位是打包数据类型。为通道的 **Writer** 和 **Reader** 访问指定突发大小。

无论通道类型如何，通道数据始终使用突发事务传输到存储器模型。对于 AXI4 配置，算法逻辑负责通过协议信号定义突发。

对于流数据配置，**Burst Length** 参数确定到存储器的突发大小，通道 **data** 信号定义接口上每次传输的大小。

设置突发长度时，必须考虑 Buffer size (bytes) 参数。

#### 依赖项

要启用此参数，请选择 **启用内存仿真**。

- 当 **通道类型** 参数设置为 `AXI4 Random Access` 时，此参数不可见。
- 当 **Channel Type** 参数设置为 `Software to AXI4-Stream via DMA` 时，写入器 **Burst length** 参数不可见
- 当 **Channel Type** 参数设置为 `AXI4-Stream to Software via DMA` 时，读取器 **Burst length** 参数不可见

### **使用硬件板设置** — 使用配置参数中的 Hardware Implementation 设置 on（默认）| off

要使用与配置参数中相同的模型范围设置，请选中此框。清除此框以为此通道自定义设置。使用通道特定设置时，仍会根据硬件特定约束检查这些值。要在配置参数中设置这些值，请参阅 FPGA design (mem channels)。

#### 依赖项

要启用此参数，请选择 **启用内存仿真**。

当 **通道类型** 设置为 `AXI4 Random Access` 时，此参数不可见。

### **读取器/写入器使用相同值** — 读取器和写入器使用相同值 on（默认）| off

选中此框可为此通道的读取器和写入器使用相同的互连设置。清除此框可为读取器和写入器自定义不同的设置。清除 **读取器/写入器使用相同值** 后，可为以下参数分别输入写入器侧的值和读取器侧的值：

- **FIFO 深度（突发数量）**
- **几乎满深度**
- **时钟频率 (MHz)**
- **数据宽度 (bits)**

#### 依赖项

要启用此参数，请选择 **启用内存仿真**。

当 **通道类型** 设置为 `AXI4-Stream FIFO`、`AXI4-Stream Video FIFO` 或 `AXI4-Stream Video Frame Buffer` 时，此参数可见。

### **FIFO 深度（突发数量）** — 数据的 FIFO 深度 `12`（默认）| 标量

指定数据 FIFO 的深度，以突发为单位。当写入器没有可写入的缓冲区时，FIFO 可以吸收数据，直到有缓冲区可用。此值是在数据被丢弃之前可缓冲的最大突发数。

#### 依赖项

- 要启用此参数，请清除 **使用硬件板设置** 复选框，并选择 **启用内存仿真**。

  。
- 当清除 **读取器/写入器使用相同值** 后，有两个文本框：一个用于 **写入器**，一个用于 **读取器**。
- 当 **通道类型** 参数设置为 `AXI4 Random Access` 时，此参数不可见。
- 当 **Channel Type** 参数设置为 `Software to AXI4-Stream via DMA` 时，写入器 **FIFO 深度** 参数不可见
- 当 **Channel Type** 参数设置为 `AXI4-Stream to Software via DMA` 时，读取器 **FIFO 深度** 参数不可见

### **几乎满深度** — 断言反压时的 FIFO 深度 `8`（默认）| 标量

指定一个数值，当达到该值时，通道向数据源断言反压信号。为避免丢弃数据，请设置一个高水位标记，使数据生产者有足够时间对反压做出反应。此数值必须小于 FIFO 深度。

#### 依赖项

- 要启用此参数，请清除 **使用硬件板设置** 复选框，并选择 **启用内存仿真**。
- 当清除 **读取器/写入器使用相同值** 后，有两个文本框：一个用于 **写入器**，一个用于 **读取器**。
- 当 **通道类型** 参数设置为 `AXI4 Random Access` 时，此参数不可见。
- 当 **Channel Type** 参数设置为 `Software to AXI4-Stream via DMA` 时，写入器 **几乎满深度** 参数不可见
- 当 **Channel Type** 参数设置为 `AXI4-Stream to Software via DMA` 时，读取器 **几乎满深度** 参数不可见

### **时钟频率 (MHz)** — 主数据路径的互连频率 `100`（默认）

主数据路径到互连控制器的频率，单位为 MHz。

#### 依赖项

- 要启用此参数，请清除 **使用硬件板设置** 复选框，并选择 **启用内存仿真**。
- 当清除 **读取器/写入器使用相同值** 后，有两个文本框：一个用于 **写入器**，一个用于 **读取器**。
- 当 **通道类型** 参数设置为 `AXI4 Random Access` 时，此参数不可见。
- 当 **Channel Type** 参数设置为 `Software to AXI4-Stream via DMA` 时，写入器 **时钟频率 (MHz)** 参数不可见
- 当 **Channel Type** 参数设置为 `AXI4-Stream to Software via DMA` 时，读取器 **时钟频率 (MHz)** 参数不可见

### **数据宽度 (bits)** — 主数据路径的数据宽度 `64`（默认）| 标量

主数据路径到互连控制器的数据宽度，单位为 bits。

#### 依赖项

- 要启用此参数，请清除 **使用硬件板设置** 复选框，并选择 **启用内存仿真**。
- 当清除 **读取器/写入器使用相同值** 后，有两个文本框：一个用于 **写入器**，一个用于 **读取器**。
- 当 **通道类型** 参数设置为 `AXI4 Random Access` 时，**数据宽度 (bits)** 参数设置为与 **数据类型** 参数以及 **启用样本打包** 参数对应的位宽。
- 当 **Channel Type** 参数设置为 `Software to AXI4-Stream via DMA` 时，写入器 **数据宽度 (bits)** 参数不可见
- 当 **Channel Type** 参数设置为 `AXI4-Stream to Software via DMA` 时，读取器 **数据宽度 (bits)** 参数不可见

### 信号属性

#### 写入数据信号

### **维度** — 输入数据信号的维度 标量 | 数组

**wrData** 可以是多维数组。请以整数指定数组的维度。

当 **通道类型** 设置为 `Software to AXI4-Stream via DMA` 时，**维度** 参数必须为标量。

**示例：** 1 – 一个标量样本。

**示例：** [10 1] – 十个标量的向量。

**示例：** [1080 1920 3] – 一个 1080p 帧。该帧包含 1080 行，每行 1920 个像素，每个像素由三个值表示（分别对应红色、绿色和蓝色）。

### **数据类型** — 写入器数据的数据类型 double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean | fixed point

指定 **wrData** 端口的数据类型。如需帮助，请点击 **...** 按钮。这会展开菜单并显示 **Data Type Assistant**。

当 **通道类型** 参数设置为 `Software to AXI4-Stream via DMA` 时，数据类型必须设置为 `uint16`、`uint32`、`uint64` 或 `fixdt(0,128,0)`。

### **采样时间** — 采样时间间隔 1（默认）| 正标量 | 向量

以秒为单位指定时间间隔，以定义模块更新的频率。

如果不希望输出具有时间偏移，请将 **采样时间** 参数指定为标量。要向输出添加时间偏移，请将 **采样时间** 参数指定为 `1` 乘 `2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

#### 依赖项

当 **通道类型** 参数设置为 `Software to AXI4-Stream via DMA` 时，此参数不可见。

### **启用样本打包（最后一个信号维度作为通道）** — 在信号的最后一个维度上打包数据 `off`（默认）| `on`

选择此参数以启用沿信号最后一个维度的数据打包。Memory Channel 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`，并且您选择此参数，则内存通道会生成 1024 个 128 bits 的读取或写入事务。对于此示例，如果清除此样本打包参数，则内存通道会生成 4096 个每个 32 bits 的事务。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据打包时，三个 10-bit 字会连接在一起，并扩展 2 bits 成为 32-bit 字。当数据未打包时，每个 10-bit 字会扩展为 16-bit 字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐，以构成 32 bits。底行显示未打包数据按 10 和 6 的样本对齐，以构成 16 bits。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据打包时，三个 8-bit 字会连接在一起，并扩展 8 bits 成为 32-bit 字。当数据未打包时，每个 8-bit 字表示为一个 8-bit 样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐，以构成 32 bits。底行显示未打包数据按 8 bits 的样本对齐。

展平信号的组合宽度不得超过 512 bits。

#### 依赖项

当 **通道类型** 参数设置为 `Software to AXI4-Stream via DMA` 时，此参数不可见。

#### 读取数据信号

### **输出数据信号与输入匹配** — 读取器和写入器使用相同值 on（默认）| off

选中此框可为此通道的读取器和写入器使用相同的维度和数据类型。清除此框可为读取器和写入器自定义不同的设置。清除此框可为读取器和写入器接口自定义不同的维度和数据类型。

### **维度** — 输出数据信号的维度 标量 | 数组

**rdData** 可以是多维数组。请以整数指定数组的维度。

当 **通道类型** 设置为 `AXI4-Stream to Software via DMA` 时，**维度** 参数必须为标量。

**示例：** 1 – 一个标量样本。

**示例：** [10 1] – 十个标量的向量。

**示例：** [1080 1920 3] – 一个 1080p 帧。该帧包含 1080 行，每行 1920 个像素，每个像素由三个值表示（分别对应红色、绿色和蓝色）。

#### 依赖项

要启用此参数，请清除 **输出数据信号与输入匹配** 复选框。

### **数据类型** — 读取器数据的数据类型 double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean | fixed point

指定 **rdData** 端口的数据类型。如需帮助，请点击 **...** 按钮。这会展开菜单并显示 **Data Type Assistant**。

当 **通道类型** 参数设置为 `AXI4-Stream to Software via DMA` 时，数据类型必须设置为 `uint16`、`uint32`、`uint64` 或 `fixdt(0,128,0)`。

#### 依赖项

要启用此参数，请清除 **输出数据信号与输入匹配** 复选框。

### **采样时间** — 采样时间间隔 1（默认）| 正标量 | 向量

以秒为单位指定时间间隔，以定义模块更新的频率。

如果不希望输出具有时间偏移，请将 **采样时间** 参数指定为标量。要向输出添加时间偏移，请将 **采样时间** 参数指定为 `1` 乘 `2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink 中采样时间的详细信息，请参阅 Specify Sample Time。

#### 依赖项

要启用此参数，请执行以下操作之一：

- 将 **通道类型** 设置为 `Software to AXI4-stream via DMA`。
- 将 **通道类型** 设置为 `AXI4 Random Access`，并清除 **输出数据信号与输入匹配** 复选框。

### **启用样本打包（最后一个信号维度作为通道）** — 在信号的最后一个维度上打包数据 `off`（默认）| `on`

选择此参数以启用沿信号最后一个维度的数据打包。Memory Channel 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`，并且您选择此参数，则内存通道会生成 1024 个 128 bits 的读取或写入事务。对于此示例，如果清除此样本打包参数，则内存通道会生成 4096 个每个 32 bits 的事务。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据打包时，三个 10-bit 字会连接在一起，并扩展 2 bits 成为 32-bit 字。当数据未打包时，每个 10-bit 字会扩展为 16-bit 字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐，以构成 32 bits。底行显示未打包数据按 10 和 6 的样本对齐，以构成 16 bits。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据打包时，三个 8-bit 字会连接在一起，并扩展 8 bits 成为 32-bit 字。当数据未打包时，每个 8-bit 字表示为一个 8-bit 样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐，以构成 32 bits。底行显示未打包数据按 8 bits 的样本对齐。

展平信号的组合宽度不得超过 512 bits。

#### 依赖项

要启用此参数，请清除 **输出数据信号与输入匹配** 复选框，并将 **通道类型** 设置为 `AXI4-Stream to Software via DMA` 以外的值。

### **继承采样时间偏移** — 使读取器从写入器继承采样时间 `on`（默认）| `off`

选中此框可使读取器从写入器继承采样时间偏移。清除此框可使用与写入器不同的采样时间偏移。有关采样时间偏移的详细信息，请参阅 Sample Time Offset。

#### 依赖项

要启用此参数，请清除 **输出数据信号与输入匹配** 复选框，并将 **通道类型** 设置为以下值之一：

- `AXI4-Stream FIFO`
- `AXI4-Stream Video FIFO`
- `AXI4-Stream Video Frame Buffer`

### **使用像素时钟采样时间** — 使用像素时钟采样时间 on（默认）| off

选中此框以使用像素时钟采样时间。要使用像素时钟采样时间，必须使用标量像素维度。它仅在流式传输像素时相关。如果读取器和写入器都在流式传输帧，则选中此框时会出现错误。

**注意**

如果读取器和写入器都使用成帧信号，则信号维度不是标量，并且无法推断像素时序。在这种情况下，选择 **使用像素时钟采样时间** 会产生错误。

#### 依赖项

要启用此参数，请将 **通道类型** 设置为 `AXI4-Stream Video FIFO` 或 `AXI4-Stream Video Frame Buffer`。

### **帧大小** — 帧维度 `480p SDTV (720x480p)`（默认）| ...

对于视频流应用，**帧大小** 通常可以推断出来，并且此参数显示为只读值。当无法推断时，请从下拉菜单中选择 **帧大小**。

- 当读取器或写入器使用具有已知 porch 和 blanking 时序的帧的成帧信号时，**帧大小** 会从这些时序推断出来。当读取器或写入器之一为标量，而另一个为非标准帧大小时，**帧大小** 无法推断，并且会出现错误。
- 当 **通道类型** 设置为 `AXI4-Stream Video Frame Buffer` 且读取器和写入器都使用像素流的标量维度时，**帧大小** 从 **BufferSize** 和 TDATA 推断出来，此时为只读值。
- 当 **通道类型** 设置为 `AXI4-Stream Video FIFO` 且读取器和写入器都使用像素流的标量维度时，请将 **帧大小** 选择为以下值之一：

  - `160x120p`
  - `480p SDTV (720x480p)`
  - `576p SDTV (720x576p)`
  - `720p HDTV (1280x720p)`
  - `1080p HDTV (1920x1080p)`
  - `320x240p`
  - `640x480p`
  - `800x600p`
  - `1024x768p`
  - `1280x768p`
  - `1280x1024p`
  - `1360x768p`
  - `1400x1050p`
  - `1600x1200p`
  - `1680x1050p`
  - `1920x1200p`
  - `16x12p (test mode)`

#### 依赖项

要启用此参数，请将 **通道类型** 设置为 `AXI4-Stream Video FIFO` 或 `AXI4-Stream Video Frame Buffer`，并选择 **使用像素时钟采样时间**。

### 性能

### **Launch performance plots** — 显示性能指标按钮

点击该按钮会在新窗口中打开内存通道的 Performance plots。有关性能图的更多信息，请参阅 Simulation Diagnostics。

#### 依赖项

要启用此参数，请选择 **Enable memory simulation**。

## 所属库

SoC Blockset / Memory

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

### R2023b: 支持多个 AXI 流

使用多个 AXI4-Stream to Software、Software to AXI4-Stream 或 Memory Channel 模块来建模、仿真和部署具有多个与软件之间往返的流的设计。在以前的版本中，SoC Blockset™ 仅支持多个流用于建模。此版本新增了生成二进制文件和软件并将其部署到 SoC 设备上的能力。

### R2022b: 简化的内存模块

SoC Blockset 新增四个模块，用于替换连接到 Memory Controller 模块的 Memory Channel 模块。这些新模块通过引入简单的参数集和更少的连接来简化您的模型，从而提升仿真性能。

- AXI4-Stream to Software — 使用此模块替换连接到 Memory Controller 模块且 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA` 的 Memory Channel 模块。
- Software to AXI4-Stream — 使用此模块替换连接到 Memory Controller 模块且 **Channel type** 参数设置为 `Software to AXI4-Stream via DMA` 的 Memory Channel 模块。
- AXI4 Random Access Memory — 使用此模块替换连接到 Memory Controller 模块且 **Channel type** 参数设置为 `AXI4 Random Access` 的 Memory Channel 模块。
- AXI4 Video Frame Buffer — 使用此模块替换连接到 Memory Controller 模块且 **Channel type** 参数设置为 `AXI4 Video Frame Buffer` 的 Memory Channel 模块。

### R2022a: 支持采样时间偏移

在此模块的 **Sample time** 参数中指定采样时间偏移。使用格式 `[period,offset]`。以前，您只能指定周期，而不能指定偏移。

模块掩码在 **Signal Attributes** 选项卡中还新增了 **Inherit sample time offset** 参数。当读取数据与写入数据具有相同偏移时，请选择此参数。

### R2022a: 仿真时间改进

当仿真包含 Memory Channel 模块的模型时，如果不需要高保真仿真，则可以提高仿真速度。在模块掩码中，选择 **Enable memory simulation** 以仿真准确的内存数据路径，或清除该参数，以便在调试算法时获得更快的仿真速度。有关使用此功能的示例，请参阅 Accelerate SoC Simulation by Varying Abstraction Levels。

### R2021a: 支持最高 512 bits 的向量

Memory Channel 模块支持最高 512 bits 的向量。此功能使您能够创建：

- 多通道帧
- 多通道样本
- 具有多个像素的视频帧
- 具有多个像素的视频样本
- 向量化帧
- 向量化像素

要启用样本打包，请打开模块掩码，然后在 **Signal Attributes** 选项卡上选择 **Enable sample packing (last signal dimension as channel)** 参数。

### R2021a: 流水线读取和写入操作

当您将 **Channel type** 参数设置为 `AXI4 Random Access` 时，Memory Channel 模块会仿真流水线随机访问读取和写入操作。此功能可实现更高的内存随机访问吞吐量仿真保真度。

### R2021a: 扩展数据类型

当您将 **Channel type** 参数设置为 `Software to AXI4 Stream via DMA` 或 `AXI4 Stream to Software via DMA` 时，Memory Channel 模块支持 16-bit 和 128-bit 整数数据类型。

## 描述

通过内存通道流式传输数据

Memory Channel 模块通过外部内存流式传输数据。从概念上讲，它通过共享内存对一个算法与另一个算法之间的数据传输进行建模。该算法可以是硬件逻辑 (HW)、处理器模型或 I/O 设备。写入方算法从 Memory Controller 模块请求对内存的访问。授予访问权限后，写入方算法会写入内存缓冲区。在模型中，数据存储被建模为通道中的缓冲区。在硬件上部署时，数据会被路由到外部共享内存。

此模块可配置为支持以下任一协议：

- **AXI4-Stream to Software via DMA** – 对硬件逻辑与软件任务之间通过外部内存的连接进行建模。写入方使用 MathWorks® simplified AXI stream protocol 将数据放入通道，读取方（处理器）从 DMA 驱动程序接口获取数据。该通道对该连接的数据路径和软件栈进行建模，包括 FIFO、DMA 引擎、互连和外部内存、中断、DMA 驱动程序的内核缓冲区管理，以及到软件任务的数据传输。有关 MathWorks simplified AXI stream protocol 的更多信息，请参阅 AXI4-Stream Interface。

  此图像是 Memory Channel 模块的概念视图，显示数据从 FPGA 算法流式传输到处理器算法。

  Memory Channel 模块的概念视图，显示数据从 FPGA 算法流经 FIFO 到内存。然后，处理器通过 DMA Driver 模块读取数据流。

- **Software to AXI4-Stream via DMA** – 对硬件逻辑与软件任务之间通过外部内存的连接进行建模。写入方（处理器）使用 MathWorks simplified AXI stream protocol 通过 DMA 驱动程序将数据流式传输到通道中。该通道对该连接的数据路径和软件栈进行建模，包括 FIFO、DMA 引擎、互连和外部内存、中断、DMA 驱动程序的内核缓冲区管理，以及来自软件任务的数据传输。有关 MathWorks simplified AXI stream protocol 的更多信息，请参阅 AXI4-Stream Interface。

  此图像是 Memory Channel 模块的概念视图，显示数据从处理器算法流式传输到 FPGA 算法。

  Memory Channel 模块的概念视图，显示数据从处理器算法流经 DMA 驱动程序到内存。然后，FPGA 算法读取数据流。

- **AXI4-Stream FIFO** – 对两个 FPGA 算法之间通过外部内存的连接进行建模。写入方使用 MathWorks simplified AXI stream protocol 作为主设备将数据放入通道，读取方使用相同协议作为从设备从通道接收数据。该通道的行为类似于先进先出 (FIFO) 内存。该通道对该连接的数据路径进行建模。Memory Channel 模块包含一个中间突发级 FIFO、DMA 引擎、互连和外部内存。外部内存本身作为循环缓冲区进行管理，其中必须先写入缓冲区，然后才能读取。有关 MathWorks simplified AXI stream protocol 的更多信息，请参阅 AXI4-Stream Interface。

  此图像是 Memory Channel 模块的概念视图，显示数据从一个 FPGA 算法流式传输到另一个 FPGA 算法。

  Memory Channel 模块的概念视图，显示数据从 FPGA 算法流经 FIFO 到内存。然后，接收方 FPGA 算法通过 DMA Controller 和 FIFO 从内存读取数据流。

- **AXI4-Stream Video FIFO** – 对两个硬件算法之间通过外部内存的连接进行建模。此通道结构类似于 **AXI4 Stream FIFO** 配置，但写入方和读取方使用 MathWorks streaming pixel protocol 以及背压信号。有关更多信息，请参阅 AXI4-Stream Video Interface。

- **AXI4-Stream Video Frame Buffer** – 使用完整的视频帧缓冲区，对两个硬件算法之间通过外部内存的连接进行建模。该协议是带背压的 MathWorks streaming pixel protocol。此外，读取方可以通过断言 FSYNC 协议信号来确保帧缓冲区与下游视频时序同步。数据路径包含一个 Video-DMA (VDMA) 引擎，外部内存缓冲区作为完整视频帧的循环缓冲区进行管理。该通道结构与 **AXI4 Stream FIFO** 通道类型的结构相同。

- **AXI4-Random Access** – 使用 MathWorks simplified AXI4-Master protocol，对两个硬件算法之间通过外部内存的连接进行建模。写入方和读取方都是主设备，在两种情况下该通道都是从设备。外部内存是非托管的（没有逻辑缓冲区，也没有循环缓冲区）。读取方和写入方需要协调访问时序，以确保数据完整性。有关更多信息，请参阅 Simplified AXI4 Master Interface。

  此图像是 Memory Channel 模块的概念视图，其中对内存进行随机访问以写入，并对内存进行随机访问以读取。

  Memory Channel 模块的概念视图，其中 FPGA 算法执行随机写入操作，处理器算法从内存执行随机读取操作。

有关可用协议的更多信息，请参阅 External Memory Channel Protocols。
