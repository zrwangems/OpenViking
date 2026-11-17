---
type: simulink-block
title: 'C281x CAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C281x'
documentation_page: 'c281xcap'
documentation_source_path: 'ref/c281xcap.html'
language: zh-CN
chinese_source: worker-translation
---

# C281x CAP

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

### Data Format Pane

**Module**
:   选择要使用的 Event Manager (EV) 模块：

    - `A` — 使用 CAP 1、2 和 3。
    - `B` — 使用 CAP 4、5 和 6。

**Output overrun status flag**
:   选择此项可输出 FIFO 中元素的状态。状态标志的数据类型为 uint16。

**输出数据格式**
:   要输出的数据类型：

    - `Send 2 elements (FIFO Buffer)` — 发送最新的两个值。当 FIFO 中有两个元素时输出会更新，这由发送的位 13 或 11 或 9（CAP x FIFO）指示。如果在捕获的元素少于两个时轮询 CAP，则会重复旧值。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 读取 FIFO 的顶部值，并将其存储在输出的索引 0 处。
      3. 读取 FIFO 的新顶部值（先前存储的底部堆栈值），并将其存储在输出的索引 1 处。

    - `Send 1 element (oldest)` — 发送最近两个值中较旧的那个。当 FIFO 中至少有一个元素时输出会更新，这由发送的位 13:12、或 11:10、或 9:8 指示。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 读取 FIFO 的顶部值，并将其存储在输出中。

    - `Send 1 element (latest)` — 发送最近的值。当 FIFO 中至少有一个元素时输出会更新，这由发送的位 13:12、或 11:10、或 9:8 指示。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 如果 FIFO 缓冲区包含两个条目，则读取底部值并将其存储在输出中。如果 FIFO 缓冲区包含一个条目，则读取顶部值并将其存储在输出中。

**Sample time**
:   FIFO 输出之间的时间。如果没有新数据可用，则发送先前的数据。

**数据类型**
:   输出数据的数据类型。可用选项包括 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和 `boolean`。`auto` 选项使用向此模块输出数据的已连接模块的数据类型。如果此模块没有接收输入，`auto` 会将数据类型设置为 `double`。

    **注意**

    C281x CAP 模块的输出可以是向量化的。

### CAP Panes

CAP 窗格为各个 CAP 设置参数。CAP 窗格所影响的特定 CAP 取决于您选择的 EV 模块：

- **CAP1** 控制 CAP 1 或 CAP 4，分别对应 EV 模块 A 或 B。
- **CAP2** 控制 CAP 2 或 CAP 5，分别对应 EV 模块 A 或 B。
- **CAP3** 控制 CAP 3 或 CAP 6，分别对应 EV 模块 A 或 B。

**Enable CAP**
:   选择此项可使用指定的捕获单元引脚。

**Edge Detection**
:   用于此 CAP 的跳变检测类型。可用类型包括 `Rising Edge`、`Falling Edge`、`Both Edges` 和 `No transition`。

**Time Base**
:   选择 CAP 将哪个目标板 GP 定时器用作时基。CAP 1、2 和 3 可以使用 `Timer 1` 或 `Timer 2`。CAP 4、5 和 6 可以使用 `Timer 3` 或 `Timer 4`。

**Clock source**
:   此选项仅适用于 CAP 3 窗格。您可以选择 `Internal` 以使用内部时基。同时为内部时基配置 **Counting mode**、**Timer prescaler** 和 **Timer period source**。

    选择 `QEP circuit` 以从正交编码器脉冲 (QEP) 子模块生成输入时钟。

**Counting mode**
:   选择 `Up` 以生成非对称波形输出，或选择 `Up-down` 以生成对称波形输出，如下图所示。

    Counting mode 用于内部定时器设置。

    当您将 **Counting mode** 指定为 `Up`（非对称）时，波形：

    - 从低电平开始
    - 当递增周期计数值与 **Compare value** 匹配时变为高电平
    - 在周期结束时变为低电平

    当您将 **Counting mode** 指定为 `Up-down`（对称）时，波形：

    - 从低电平开始
    - 当递增周期计数值与 **Compare value** 匹配时变为高电平
    - 当递减周期计数值与 **Compare value** 匹配时变为低电平

    当您将 **Clock source** 设置为 `QEP circuit` 时，**Counting mode** 将不可用。

**Timer Prescaler**
:   用于对所选 GP 定时器进行预分频以产生所需定时器计数速率的时钟分频因子。可用选项包括 `none`、`1/2`、`1/4`、`1/8`、`1/16`、`1/32`、`1/64` 和 `1/128`。下表显示了选择每个选项后得到的速率。

    | Scaling | Resulting Rate (µs) |
    | --- | --- |
    | none | 0.01334 |
    | 1/2 | 0.02668 |
    | 1/4 | 0.05336 |
    | 1/8 | 0.10672 |
    | 1/16 | 0.21344 |
    | 1/32 | 0.42688 |
    | 1/64 | 0.85376 |
    | 1/128 | 1.70752 |

    **注意**

    这些速率假设输入时钟为 75 MHz。

**Timer period source**
:   选择 `Specify via dialog` 以启用 **Timer period** 参数。选择 `Input port` 以创建一个模块输入 **T1**，用于接受定时器周期值。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入 `0` 到 `65535` 之间的值。该值默认为 `65535`。

    如果您知道一个时钟周期的长度，就可以轻松计算出要为定时器周期设置多少个时钟周期。以下计算确定了单个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，您将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将结果值除以定时器控制输入时钟预分频器 128。得到的频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Post interrupt on CAP**
:   选中此复选框可在 CAP 上发布异步中断。

### 另请参阅

C28x Hardware Interrupt

### Data Format Pane

**Module**
:   选择要使用的 Event Manager (EV) 模块：

    - `A` — 使用 CAP 1、2 和 3。
    - `B` — 使用 CAP 4、5 和 6。

**Output overrun status flag**
:   选择此项可输出 FIFO 中元素的状态。状态标志的数据类型为 uint16。

**输出数据格式**
:   要输出的数据类型：

    - `Send 2 elements (FIFO Buffer)` — 发送最新的两个值。当 FIFO 中有两个元素时输出会更新，这由发送的位 13 或 11 或 9（CAP x FIFO）指示。如果在捕获的元素少于两个时轮询 CAP，则会重复旧值。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 读取 FIFO 的顶部值，并将其存储在输出的索引 0 处。
      3. 读取 FIFO 的新顶部值（先前存储的底部堆栈值），并将其存储在输出的索引 1 处。

    - `Send 1 element (oldest)` — 发送最近两个值中较旧的那个。当 FIFO 中至少有一个元素时输出会更新，这由发送的位 13:12、或 11:10、或 9:8 指示。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 读取 FIFO 的顶部值，并将其存储在输出中。

    - `Send 1 element (latest)` — 发送最近的值。当 FIFO 中至少有一个元素时输出会更新，这由发送的位 13:12、或 11:10、或 9:8 指示。CAP 寄存器的读取方式如下：

      1. 读取 CAP x FIFO 状态位，并将该值存储在状态标志中。
      2. 如果 FIFO 缓冲区包含两个条目，则读取底部值并将其存储在输出中。如果 FIFO 缓冲区包含一个条目，则读取顶部值并将其存储在输出中。

**Sample time**
:   FIFO 输出之间的时间。如果没有新数据可用，则发送先前的数据。

**数据类型**
:   输出数据的数据类型。可用选项包括 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和 `boolean`。`auto` 选项使用向此模块输出数据的已连接模块的数据类型。如果此模块没有接收输入，`auto` 会将数据类型设置为 `double`。

    **注意**

    C281x CAP 模块的输出可以是向量化的。

### CAP Panes

CAP 窗格为各个 CAP 设置参数。CAP 窗格所影响的特定 CAP 取决于您选择的 EV 模块：

- **CAP1** 控制 CAP 1 或 CAP 4，分别对应 EV 模块 A 或 B。
- **CAP2** 控制 CAP 2 或 CAP 5，分别对应 EV 模块 A 或 B。
- **CAP3** 控制 CAP 3 或 CAP 6，分别对应 EV 模块 A 或 B。

**Enable CAP**
:   选择此项可使用指定的捕获单元引脚。

**Edge Detection**
:   用于此 CAP 的跳变检测类型。可用类型包括 `Rising Edge`、`Falling Edge`、`Both Edges` 和 `No transition`。

**Time Base**
:   选择 CAP 将哪个目标板 GP 定时器用作时基。CAP 1、2 和 3 可以使用 `Timer 1` 或 `Timer 2`。CAP 4、5 和 6 可以使用 `Timer 3` 或 `Timer 4`。

**Clock source**
:   此选项仅适用于 CAP 3 窗格。您可以选择 `Internal` 以使用内部时基。同时为内部时基配置 **Counting mode**、**Timer prescaler** 和 **Timer period source**。

    选择 `QEP circuit` 以从正交编码器脉冲 (QEP) 子模块生成输入时钟。

**Counting mode**
:   选择 `Up` 以生成非对称波形输出，或选择 `Up-down` 以生成对称波形输出，如下图所示。

    Counting mode 用于内部定时器设置。

    当您将 **Counting mode** 指定为 `Up`（非对称）时，波形：

    - 从低电平开始
    - 当递增周期计数值与 **Compare value** 匹配时变为高电平
    - 在周期结束时变为低电平

    当您将 **Counting mode** 指定为 `Up-down`（对称）时，波形：

    - 从低电平开始
    - 当递增周期计数值与 **Compare value** 匹配时变为高电平
    - 当递减周期计数值与 **Compare value** 匹配时变为低电平

    当您将 **Clock source** 设置为 `QEP circuit` 时，**Counting mode** 将不可用。

**Timer Prescaler**
:   用于对所选 GP 定时器进行预分频以产生所需定时器计数速率的时钟分频因子。可用选项包括 `none`、`1/2`、`1/4`、`1/8`、`1/16`、`1/32`、`1/64` 和 `1/128`。下表显示了选择每个选项后得到的速率。

    | Scaling | Resulting Rate (µs) |
    | --- | --- |
    | none | 0.01334 |
    | 1/2 | 0.02668 |
    | 1/4 | 0.05336 |
    | 1/8 | 0.10672 |
    | 1/16 | 0.21344 |
    | 1/32 | 0.42688 |
    | 1/64 | 0.85376 |
    | 1/128 | 1.70752 |

    **注意**

    这些速率假设输入时钟为 75 MHz。

**Timer period source**
:   选择 `Specify via dialog` 以启用 **Timer period** 参数。选择 `Input port` 以创建一个模块输入 **T1**，用于接受定时器周期值。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入 `0` 到 `65535` 之间的值。该值默认为 `65535`。

    如果您知道一个时钟周期的长度，就可以轻松计算出要为定时器周期设置多少个时钟周期。以下计算确定了单个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，您将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将结果值除以定时器控制输入时钟预分频器 128。得到的频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Post interrupt on CAP**
:   选中此复选框可在 CAP 上发布异步中断。

### 另请参阅

C28x Hardware Interrupt
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

接收并记录捕获输入引脚的跳变

# C281x CAP

接收并记录捕获输入引脚的跳变

C281x CAP 模块为需要精确计时外部事件的系统提供输入捕获功能。C281x CAP 模块为 Event Manager (EV) 模块的捕获单元 (CAP) 设置参数。捕获单元通过将输入信号跳变的时间记录到两级深度的 FIFO 堆栈中，来记录在捕获单元引脚上检测到的跳变。您可以将捕获单元引脚设置为检测上升沿、下降沿、任一类型的跳变或不检测跳变。该模块的 `cnt` 输出给出 EV 运行定时器的捕获值。

C281x 芯片有六个捕获单元——每个 EV 模块关联三个。捕获单元 1、2 和 3 与 EVA 关联，捕获单元 4、5 和 6 与 EVB 关联。每个捕获单元都与一个捕获输入引脚关联。

每组 EV 模块捕获单元可以使用目标板上的两个通用 (GP) 定时器之一。EVA 捕获单元可以使用 GP 定时器 1 或 2。EVB 捕获单元可以使用 GP 定时器 3 或 4。当发生跳变时，模块将所选定时器的值存储到两级深度的 FIFO 堆栈中。

C281x CAP 模块与其他 C281 模块共享 GP 定时器。有关共享定时器的更多信息和指导，请参阅 Sharing General Purpose Timers Between C281x Peripherals。

**注意**

一个模型中最多可以有两个 C281x CAP 模块——每个 EV 模块一个模块。

### 输出

此模块最多有两个输出：一个 `cnt`（计数）输出和一个可选的 FIFO 状态 `flag` 输出。`cnt` 输出保存检测到的跳变期间捕获的 EV 定时器的值。`cnt` 输出根据 **输出数据格式** 参数中设置的值给出运行计数器的捕获值。状态标志输出为：

- `0` — FIFO 为空。要么没有发生捕获，要么先前存储的捕获已从堆栈中读取。（此标志的二进制版本为 `00`。）
- `1` — FIFO 在堆栈的顶部寄存器中有一个条目。（此标志的二进制版本为 `01`。）
- `2` — FIFO 在堆栈寄存器中有两个条目。（此标志的二进制版本为 `10`。）
- `3` — FIFO 在堆栈寄存器中有两个条目，并且一个或多个捕获值已丢失。发生这种情况是因为在读取 FIFO 堆栈之前又发生了一次捕获。这意味着当您按照调度方案执行模块时读取 FIFO 堆栈，如果使用采样时间则为同步读取，如果由中断或空闲任务触发则为异步读取。新值被放入底部寄存器。底部寄存器的值被推送到堆栈顶部，顶部值被推出堆栈。（此标志的二进制版本为 `11`。）

- C281x CAP 模块
