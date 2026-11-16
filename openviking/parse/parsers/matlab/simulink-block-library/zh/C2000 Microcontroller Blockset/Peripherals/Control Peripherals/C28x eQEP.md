---
type: simulink-block
title: 'C28x eQEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'c28xeqep'
documentation_source_path: 'ref/c28xeqep.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x eQEP

## 端口

### 输入

### **swi** — 动态更新位置计数器初始化值的标量

如果输入为 `true`，则位置计数器初始化为 **Initialization value (0~4294967295)** 参数中的值。

#### 依赖关系

仅当在 **Position counter** 选项卡中选择 **Enable software initialization** 并将 **Software initialization source** 设置为 `Input port` 时，此端口才会出现。

**数据类型：** `Boolean`

### **cmp** — 用于比较位置的标量值

生成位置比较同步信号的输入值。

#### 依赖关系

仅当在 **Compare output** 选项卡中选择 **Enable position-compare sync signal output** 并将 **Compare value source** 设置为 `Input port` 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **iel** — 软件索引标记标量

用于锁存位置计数器的软件索引事件标记。

#### 依赖关系

仅当在 **Position counter** 选项卡中：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on index event**。
- 将 **Index event latch of position counter** 设置为 `Software index marker via input port`。

**注意**

在 **Compare output** 选项卡中，如果 **Sync output pin selection** 设置为 `Index pin is used for sync output`，则 **Index event latch of position counter** 参数不能设置为 `Software index marker via input port`。

**数据类型：** `Boolean`

### 输出

### **qposcnt** — 位置计数器信号标量

从位置计数器与控制单元 (PCCU) 接收的位置计数器信号 (PCSOUT)。

#### 依赖关系

仅当在 **Position counter** 选项卡中选择 **Output position counter** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **pcef** — 出错时的位置计数器错误标志标量

在出错时输出位置计数器错误标志。

- `0` — 在最后一次索引转换期间未发生错误。
- `1` — 位置计数器错误。

#### 依赖关系

仅当在 **Position counter** 选项卡中：

- 将 **Position counter reset mode** 设置为 `Reset on an index event`。
- 选择 **Output position counter error flag**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qdf** — 正交模块方向标志标量

正交模块的方向标志。

- `0` — 逆时针旋转（或反向移动）。
- `1` — 顺时针旋转（或正向移动）。

#### 依赖关系

仅当在 **General** 选项卡中选择 **Quadrature direction flag output port** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmr** — 捕获定时器信号标量

输出 eQEP 捕获定时器信号。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Output capture timer** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprd** — 捕获周期信号标量

输出捕获周期信号，该信号保存最近连续 eQEP 位置事件之间的周期计数值。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Output capture period timer** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **coef** — eQEP 溢出错误标志标量

在单位位置事件之间发生捕获定时器溢出时，输出溢出错误标志（COEF 标志）。

- `0` — 未发生溢出。
- `1` — eQEP 捕获定时器寄存器 (QEPCTMR) 中发生溢出。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Enable and output overflow error flag** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **cdef** — 方向变化错误标志标量

输出方向变化错误标志。

- `0` — 未发生捕获方向错误。
- `1` — 在两个捕获位置事件之间发生了方向变化。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Enable and output direction change error flag** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmrlat** — 捕获定时器锁存值标量

从 QCTMRLAT 寄存器输出捕获定时器锁存值。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Output capture timer latched value** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprdlat** — 捕获定时器周期锁存值标量

从 QCPRDLAT 寄存器输出捕获定时器周期锁存值。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Output capture timer period latched value** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposlat** — 位置计数器锁存值标量

从 QPOSLAT 寄存器输出位置计数器锁存值。

#### 依赖关系

仅当在 **Speed calculation** 选项卡中选择 **Enable eQEP capture** 和 **Output position counter latched value** 时，此端口才会出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposilat** — 在索引事件上锁存位置计数器的标量

eQEP 索引输入可配置为：当此引脚上发生确定事件时，将位置计数器寄存器 (QPOSCNT) 锁存并作为输出。

#### 依赖关系

仅当在 **Position counter** 选项卡中：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on index event**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposslat** — 在选通事件上锁存位置计数器的标量

eQEP 选通输入可配置为：当此引脚上发生确定事件时，将位置计数器寄存器 (QPOSCNT) 锁存并作为输出。

#### 依赖关系

仅当在 **Position counter** 选项卡中：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on strobe event**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### General

### **Module** — 用于获取位置、方向和速度的 eQEP 模块 `eQEP1`（默认） | `eQEP2` | `eQEP3`

用于获取位置、方向和速度信息的 eQEP 外设模块。支持的 eQEP 模块数量因不同的 C2000™ 处理器而异。

### **Position counter mode** — 与 eQEP 外设输入编码方式匹配的模式 `Quadrature-count`（默认） | `Direction-count` | `Up-count` | `Down-count`

eQEP 外设输入为 QEPA、QEPB、QEPI 和 QEPS。通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** > **eQEP** 来配置这些输入的 GPIO 引脚。

eQEP 外设的输入信号 QEPA 和 QEPB 由 eQEP 外设中的正交解码器单元 (QDU) 处理，以生成时钟 (QCLK) 和方向 (QDIR) 信号。请选择与 eQEP 模块输入编码方式匹配的位置计数器模式：

- `Quadrature-count` — 两个相位相差 90 degrees 的方波信号（A 和 B）被发送到 eQEP 外设。QDU 使用这两个输入的相位关系来生成正交时钟和方向信号。
- `Direction-count` — 方向和时钟信号直接发送到 eQEP 外设。QEPA 引脚提供时钟输入，QEPB 引脚提供方向输入。
- `Up-count` — 位置计数器用于测量 QEPA 引脚中信号的频率。在此模式下，方向硬连线为向上计数。
- `Down-count` — 位置计数器用于测量 QEPA 引脚中信号的频率。在此模式下，方向硬连线为向下计数。

### **Positive rotation** — 旋转方向 `Clockwise`（默认） | `Counterclockwise`

设置旋转方向。

如果选择 `Clockwise`，则执行正交计数操作时不会交换馈送到 QDU 的正交时钟输入。

如果选择 `Counterclockwise`，则通过交换馈送到 QDU 的正交时钟输入来执行反向计数。正交解码器会反转计数方向。

#### 依赖关系

仅当在 **General** 选项卡上将 **Position counter mode** 设置为 `Quadrature-count` 时，此参数才会出现。

### **External clock rate** — 测量分辨率 `2x resolution: Count the rising/falling edge`（默认） | `1x resolution: Count the rising edge only`

选择位置计数器用作输入的时钟发生器的分辨率，以便在 QEPA 输入的上升沿和下降沿都进行计数，或仅在上升沿进行计数。选择前者会将测量分辨率提高 2 倍。

#### 依赖关系

仅当将 **Position counter mode** 设置为 `Direction-count`、`Up-count` 或 `Down-count` 时，此参数才会出现。

### **Quadrature direction flag output port** — 创建方向标志端口 `off`（默认） | `on`

在模块上创建端口 (qdf)，用于提供正交模块的方向标志。

#### 依赖关系

仅当在 **General** 选项卡中将 **Position counter mode** 设置为 `Quadrature-count` 时，此参数才会出现。

### **Invert input QEPxX polarity** — 反转 eQEP 输入的极性 `off`（默认） | `on`

反转 eQEP 外设输入的极性。**Invert input QEPxA polarity** 复选框对应 QEPA，**Invert input QEPxB polairty** 对应 QEPB，依此类推。

### **Index pulse gating option** — 启用索引脉冲与选通输入的门控 `off`（默认） | `on`

启用外设输入索引信号与外设输入选通信号的门控。在这种情况下，仅当两个外设输入信号 eQEPxI 和 eQEPxS 均为高电平时，内部索引信号才为高电平。

### **Sample time** — 模块读取位置计数器的频率 `0.0001`（默认） | `-1` | 标量

模块的采样时间，单位为 seconds。要异步执行此模块，请将此参数设置为 `-1`。

### Position counter

### **Output position counter** — 输出位置计数器信号 `on`（默认） | `off`

从位置计数器与控制单元 (PCCU) 输出位置计数器信号 PCSOUT。位置计数器寄存器根据输入方向，在每次 eQEP 脉冲时向上或向下计数。计数值与距给定参考点的位置成比例。

### **Maximum position counter value (0~4294967295)** — 指定最大位置计数器值 `4294967295`（默认） | integer in [0, 4,294,967,295]

输入位置计数器的最大值 (QPOSMAX)。如果位置计数器达到 QPOSMAX，则在下一次计数器递增时，位置计数器设置为 `0`。如果位置计数器为 `0`，则在下一次计数器递减时，位置计数器设置为 QPOSMAX。

### **Enable set to init value on index event** — 启用将位置计数器设置为初始化值的选项 `off`（默认） | `on`

启用将位置计数器在索引事件时设置为其初始化值的选项。

### **Set to init value on index event** — 位置计数器的初始化值 `Rising edge`（默认） | `Falling edge`

在索引事件的上升沿或下降沿将位置计数器设置为其初始化值。

#### 依赖关系

仅当在 **Position counter** 选项卡中选择 **Enable set to init value on index event** 时，此参数才会出现。

### **Enable set to init value on strobe event** — 启用将位置计数器设置为初始化值的选项 `off`（默认） | `on`

启用将位置计数器在选通事件时设置为其初始化值的选项。

### **Set to init value on strobe event** — 设置位置计数器的初始化值 `Rising edge`（默认） | `Depending on direction`

`Rising edge` 选项在选通输入的上升沿将位置计数器设置为其初始化值。`Depending on direction` 选项在以下情况下将位置计数器设置为其初始化值：

- 在正方向上，选通输入的上升沿。
- 在反方向上，选通输入的下降沿。

#### 依赖关系

仅当在 **Position counter** 选项卡中选择 **Enable set to init value on strobe event** 时，此参数才会出现。

### **Enable software initialization** — 启用将位置计数器设置为初始化值的选项 `off`（默认） | `on`

允许使用软件将位置计数器设置为其初始化值。

### **Software initialization source** — 指定位置计数器的初始化源 `Input port`（默认） | `Set to init value at start up`

选择 `Set to init value at start up` 选项，以在程序开始执行时将位置计数器初始化为 **Initialization value** 中输入的值。选择 `Input port` 选项，以基于输入初始化信号（输入端口 **swi**）动态更新初始化值。如果输入 **swi** 为 `true`，则位置计数器初始化为 **Initialization value**。

#### 依赖关系

仅当在 **Position counter** 选项卡中选择 **Enable software initialization** 时，此参数才会出现。

### **Initialization value (0~4294967295)** — 位置计数器的初始化值 `2147483648` | integer in [0, 4,294,967,295]

输入位置计数器的初始化值。

#### 依赖关系

仅当选择 **Enable set to init value on index event**、**Enable set to init value on strobe event** 或 **Enable software initialization** 时，此参数才会出现。

### **位置计数器复位模式** — 复位位置计数器 `Reset on an index event`（默认）| `Reset on the maximum position` | `Reset on the first index event` | `Reset on a time unit event`

位置计数器复位模式，取决于 eQEP 模块所处理的系统性质。

- `Reset on an index event` — 如果索引事件在正向期间发生，则位置计数器在下一个 eQEP 时钟复位为 0。如果索引事件在反向期间发生，则位置计数器在下一个 eQEP 时钟复位为 QPOSMAX 寄存器中的值。
- `Reset on the maximum position` — 在正向期间，当位置计数器等于 QPOSMAX 时，位置计数器在下一个 eQEP 时钟复位为 0，并设置位置计数器溢出标志。在反向期间，当位置计数器等于 0 时，位置计数器在下一个 QEP 时钟复位为 QPOSMAX，并设置位置计数器下溢标志。
- `Reset on the first index event` — 如果索引事件在正向期间发生，位置计数器在下一个 eQEP 时钟复位为 0。如果索引事件在反向期间发生，位置计数器在下一个 eQEP 时钟复位为 QPOSMAX 寄存器中的值。仅当第一次出现索引事件时，才会使用 `Reset on the first index event` 选项复位位置计数器。第一次出现索引事件后，位置计数器基于最大位置进行复位。
- `Reset on a unit time event` — 在单位时间事件上，QPOSCNT 值锁存到 QPOSLAT 寄存器。然后，对于正向，QPOSCNT 寄存器复位为 0；对于反向，复位为 QPOSMAX。您可以将此选项用于频率测量。

### **输出位置计数器错误标志** — 出错时输出位置计数器错误标志 `off`（默认）| `on`

出错时输出位置计数器错误标志。选择此选项后，将创建输出端口 **pcef**。

#### 依赖项

仅当在 **位置计数器** 选项卡中将 **位置计数器复位模式** 设置为 `Reset on an index event` 时，此参数才会出现。

### **在索引事件时输出锁存位置计数器** — 在索引事件时锁存位置计数器 `off`（默认）| `on`

启用此选项后，选通引脚上发生事件时，位置计数器 QPOSCNT 会锁存到 QPOSLAT 中。

#### 依赖项

仅当在 **位置计数器** 选项卡中将 **位置计数器复位模式** 设置为 `Reset on the maximum position` 或 `Reset on the first index event` 时，此参数才会出现。

### **位置计数器的索引事件锁存** — 将位置计数器配置为在事件上锁存 `Rising edge`（默认）| `Falling edge` | `Software index marker via input port`

将 eQEP 位置计数器配置为在所选的索引事件上锁存。

#### 依赖项

仅当在 **位置计数器** 选项卡中满足以下条件时，此参数才会出现：

- 将 **位置计数器复位模式** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **在索引事件时输出锁存位置计数器**。

### **在选通事件时输出锁存位置计数器** — 在选通事件时锁存位置计数器 `off`（默认）| `on`

eQEP 选通输入可配置为在该引脚上发生确定事件时将位置计数器（QPOSCNT）锁存到 QPOSSLAT 中。此选项在每次选通事件时锁存位置计数器。

#### 依赖项

仅当在 **位置计数器** 选项卡中将 **位置计数器复位模式** 设置为 `Reset on the maximum position` 或 `Reset on the first index event` 时，此参数才会出现。

### **锁存位置计数器的选通事件** — 将位置计数器配置为在选通上锁存 `Rising edge`（默认）| `Depending on direction`

`Rising edge` 在选通事件输入的上升沿锁存。`Depending on direction` 在正向时于上升沿锁存，在反向时于下降沿锁存。

#### 依赖项

仅当在 **位置计数器** 选项卡中满足以下条件时，此参数才会出现：

- 将 **位置计数器复位模式** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **在选通事件时输出锁存位置计数器**。

### 速度计算

要查看此选项卡的其他参数，请选择 **启用 QEP 捕获** 选项。

### **启用 QEP 捕获** — 启用边沿捕获单元 `off`（默认）| `on`

eQEP 外设包含一个集成边沿捕获单元，用于测量单位位置事件之间经过的时间。此选项启用边沿捕获单元。

### **输出捕获定时器** — 输出捕获定时器 `off`（默认）| `on`

从 QCTMR 寄存器输出捕获定时器值。

### **输出捕获周期定时器** — 输出捕获周期 `off`（默认）| `on`

从 QCPRD 寄存器输出最近连续 eQEP 位置事件之间的周期计数值。

### **eQEP 捕获定时器预分频器** — 预分频捕获定时器时钟频率 `128`（默认）| `1` | `2` | `4` | `8` | `16` | `32` | `64`

eQEP 捕获定时器由预分频后的 SYSCLKOUT 运行。捕获定时器时钟频率为 SYSCLKOUT 的频率除以您为此参数选择的值。

### **单位位置事件预分频器** — 预分频正交时钟 `128`（默认）| `1` | `2` | `4` | `8` | `16` | `32` | `64` | `256` | `512` | `1024` | `2048`

单位位置事件的时序通过预分频正交时钟（QCLK）确定。QCLK 除以您为此参数选择的预分频值。

### **启用并输出溢出错误标志** — 当捕获定时器溢出时输出溢出错误标志 `off`（默认）| `on`

在单位位置事件之间发生捕获定时器溢出时，启用并输出 eQEP 溢出错误标志（COEF）。

### **启用并输出方向变化错误标志** — 输出方向变化错误标志 `off`（默认）| `on`

在单位位置事件之间发生方向变化时，启用并输出方向变化错误标志（CDEF）。

### **捕获定时器和位置** — QEP 捕获锁存模式 `On position counter read`（默认）| `On unit time-out event`

触发捕获定时器和捕获周期寄存器锁存的事件：

- `On position counter read` — 在处理器读取位置计数器时锁存。当处理器读取 QPOSCNT 寄存器时，捕获定时器和捕获周期值会锁存到 QCTMRLAT 和 QCPRDLAT 寄存器中。
- `On unit time-out event` — 在单位超时事件时锁存。在单位超时事件时，位置计数器、捕获定时器和捕获周期值会锁存到 QPOSLAT、QCTMRLAT 和 QCPRDLAT 寄存器中。

### **单位定时器周期（0~4294967295）** — 设置单位定时器周期 `100000000`（默认）| 值在 [0, 4,294,967,295] 范围内

设置单位定时器周期。

#### 依赖项

仅当将 **捕获定时器和位置** 设置为 `On unit time-out event` 时，此参数才会出现。

### **输出捕获定时器锁存值** — 输出捕获定时器锁存值 `off`（默认）| `on`

从 QCTMRLAT 寄存器在输出端口 **qctmrlat** 输出捕获定时器锁存值。

### **输出捕获定时器周期锁存值** — 输出捕获定时器周期锁存值 `off`（默认）| `on`

从 QCPRDLAT 寄存器在输出端口 **qcprdlat** 输出捕获定时器周期锁存值。

### **输出位置计数器锁存值** — 输出位置计数器锁存值 `off`（默认）| `on`

从 QPOSLAT 寄存器在输出端口 **qposlat** 输出位置计数器锁存值。

### 比较输出

要查看此选项卡的其他参数，请选择 **启用位置比较同步信号输出** 选项。

### **启用位置比较同步信号输出** — 启用位置比较同步信号输出 `off`（默认）| `on`

eQEP 外设包含一个位置比较单元，当位置计数器寄存器（QPOSCNT）和位置比较寄存器（QPOSCMP）值匹配时，会生成位置比较同步信号。此选项启用位置比较同步信号输出。同步信号可以使用 eQEP 外设的索引引脚或选通引脚输出。

### **同步输出引脚选择** — 用于同步信号的 GPIO 引脚 `Index pin is used for sync output`（默认）| `Strobe pin is used for sync output`

用于同步信号输出的 GPIO 引脚。使用 eQEP 外设的索引引脚或选通引脚输出位置比较同步信号。

### **比较值来源** — 位置比较的值来源 `Specify via dialog`（默认）| `Input port`

要用于位置比较寄存器（QPOSCMP）的值的来源。当此参数设置为 `Input port` 时，将创建输入端口 **cmp**。

### **位置比较影子加载模式** — 生成位置比较同步信号的影子模式 `Load on QPOSCNT=0`（默认）| `Shadow disabled(load immediate)` | `Load on QPOSCNT=QPOSCMP`

此参数允许您启用或禁用用于更新位置比较（QPOSCMP）寄存器的影子模式。启用影子模式时，您还可以选择触发将影子寄存器值加载到活动寄存器中的事件。禁用影子模式时，处理器会直接将值加载到活动寄存器中。

`Load on QPOSCNT=0` 在位置计数器为零事件时加载，`Load on QPOSCNT=QPOSCMP` 在 QPOSCNT 和 QPOSCMP 值匹配时加载。选择这些选项时，影子模式会启用。

### **位置比较值（0~4294967295）** — 用于比较位置的值 `4294967295`（默认）| 值在 [0, 4,294,967,295] 范围内

此值会加载到位置比较寄存器（QPOSCMP）中。

#### 依赖项

仅当将 **比较值来源** 设置为 `Specify via dialog` 时，此参数才会出现。

### **同步输出脉冲宽度（1~4096）** — 位置比较同步输出信号的脉冲宽度 `1`（默认）| 值在 [0, 4,096] 范围内

位置比较单元中的脉冲展宽逻辑在位置比较匹配时生成可编程的位置比较同步脉冲输出。

从 `1` 到 `4096` 的值，用于确定位置比较同步输出信号的脉冲宽度。输出脉冲的宽度以 SYSCKOUT cycles 为单位测量，是输入值的四倍。

### **同步输出极性** — 同步输出极性 `Active high`（默认）| `Active low`

选择所生成同步输出信号的极性。

### 看门狗单元

### **看门狗定时器使能** — 使能看门狗超时标志 `off`（默认）| `on`

eQEP 外设包含一个看门狗定时器，用于监视正交时钟以指示运动控制系统正在运行。该定时器在正交时钟的边沿跳变时复位。看门狗单元会生成中断，您可以在 **中断** 选项卡中启用该中断。

### **看门狗定时器** — 看门狗定时器的超时值 `65535`（默认）| 值在 [0, 65,535] 范围内

看门狗单元生成中断之后的时间段。

#### 依赖项

仅当选择 **看门狗定时器使能** 时，此参数才会出现。

### 信号数据类型

当您在其他选项卡中选择信号作为输出时，对应信号会出现在此选项卡中。例如，当您在 **位置计数器** 选项卡上选择 **输出位置计数器** 选项时，**位置计数器值数据类型** 选项会出现在此选项卡上。使用此选项卡，您可以选择信号的数据类型。

有效数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和 `boolean`。

下表总结了可在 **信号数据类型** 选项卡中设置数据类型的选项：

| 窗格 | 选项 |
| --- | --- |
| 常规 | 正交方向标志输出端口 |
| 位置计数器 | 输出位置计数器（默认选中） |
| 输出位置计数器错误标志 |
| 在索引事件时输出锁存位置计数器 |
| 在选通事件时输出锁存位置计数器 |
| 速度计算 | 输出捕获定时器 |
| 输出捕获周期定时器 |
| 启用并输出溢出错误标志 |
| 启用并输出方向变化错误标志 |
| 输出捕获定时器锁存值 |
| 输出捕获定时器周期锁存值 |
| 输出位置计数器锁存值 |

### 中断

根据此选项卡中的设置，启用或禁用与特定事件对应的中断。生成的中断与 C28x Hardware Interrupt 一起使用。

### **位置计数器错误中断使能** — 使能位置计数器错误中断 `off`（默认）| `on`

使能位置计数器错误中断。位置计数器中断仅在索引事件复位模式下生成。当 eQEP 配置为此模式时，位置计数器值会锁存到 QPOSILAT 寄存器，并且每次索引事件标记时都会记录方向信息。如果锁存值不等于 0 或 QPOSMAX，则生成位置计数器错误中断。

### **正交相位错误中断使能** — 使能正交相位错误中断 `off`（默认）| `on`

使能正交相位错误中断。在正交计数模式下，预期正交输入 QEPA 和 QEPB 相位相差 90 degrees。当在 QEPA 和 QEPB 信号上同时检测到边沿跳变时，会生成正交相位错误中断。

### **正交方向变化中断使能** — 使能正交方向变化中断 `off`（默认）| `on`

当计数方向变化时，会生成正交方向变化中断。

### **看门狗超时中断使能** — 使能看门狗超时中断 `off`（默认）| `on`

eQEP 外设包含一个监视正交时钟的看门狗定时器。如果在看门狗定时器达到看门狗周期之前未检测到正交时钟事件，则发生超时并生成看门狗超时中断。

### **位置计数器下溢中断使能** — 使能位置计数器下溢中断 `off`（默认）| `on`

使能位置计数器下溢中断。在反向期间，如果位置计数器达到 0，则位置计数器在下一个 QEP 时钟复位为 QPOSMAX，并生成位置计数器下溢中断。

### **位置计数器溢出中断使能** — 使能位置计数器溢出中断 `off`（默认）| `on`

使能位置计数器溢出中断。在正向期间，如果位置计数器达到 QPOSMAX，则位置计数器在下一个 QEP 时钟复位为 0，并生成位置计数器溢出中断。

### **位置比较就绪中断使能** — 使能位置比较就绪中断 `off`（默认）| `on`

使能位置比较就绪中断。当位置比较寄存器配置为影子模式时，在影子寄存器值加载到活动寄存器后，会生成位置比较就绪中断。

### **位置比较匹配中断使能** — 使能位置比较匹配中断 `off`（默认）| `on`

使能位置比较匹配中断。当位置计数器值 QPOSCNT 与活动位置比较寄存器 QPOSCMP 匹配时，会生成位置比较匹配中断。

### **选通事件锁存中断使能** — 使能选通事件锁存中断 `off`（默认）| `on`

使能选通事件锁存中断。在选通事件锁存期间，当位置计数器锁存到 QPOSSLAT 寄存器时，会生成选通事件锁存中断。

### **索引事件锁存中断使能** — 启用索引事件锁存中断 `off`（默认）| `on`

启用索引事件锁存中断。当位置计数器在索引事件锁存期间锁存到 QPOSILAT 寄存器时，会生成选通事件锁存中断。

### **单元超时中断使能** — 启用单元超时中断 `off`（默认）| `on`

启用单元超时中断。当单元定时器与单元周期匹配时，会生成单元超时中断。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

正交编码器脉冲模块用于推导位置、方向和速度

增强型正交编码器脉冲 (eQEP) 模块与线性或旋转增量编码器一起使用，以从旋转机械获取位置、方向和速度信息。

eQEP 外设模块输入包括 QEPA、QEPB、QEPI（索引）和 QEPS（选通）。

要将设备配置为与该模块一起使用，请导航到 **模型配置参数** > **硬件实现**，在 **硬件板** 处选择您的设备，并展开 **目标硬件资源**。
