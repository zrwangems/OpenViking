---
type: simulink-block
title: 'C28x eQEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c28xeqep'
documentation_source_path: 'ref/c28xeqep.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x eQEP

## 端口
```yaml
ports:
- name: swi
  summary: 动态更新位置计数器初始化值 标量
  direction: input
  data_types: Boolean
- name: cmp
  summary: 用于比较位置的值 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: iel
  summary: 软件索引标记 标量
  direction: input
  data_types: Boolean
- name: qposcnt
  summary: 位置计数器信号 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: pcef
  summary: 错误时的位置计数器错误标志 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qdf
  summary: 正交模块方向标志 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qctmr
  summary: 捕获定时器信号 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qcprd
  summary: 捕获周期信号 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: coef
  summary: eQEP 溢出错误标志 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: cdef
  summary: 方向变化错误标志 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qctmrlat
  summary: 捕获定时器锁存值 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qcprdlat
  summary: 捕获定时器周期锁存值 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposlat
  summary: 位置计数器锁存值 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposilat
  summary: 在索引事件上锁存位置计数器 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposslat
  summary: 在选通事件上锁存位置计数器 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
```

### 输入

### **swi** — 动态更新位置计数器初始化值 标量

如果输入为 `true`，位置计数器将初始化为 **Initialization value (0~4294967295)** 参数中的值。

#### 依赖

此端口仅在 **Position counter** 选项卡中，选择 **Enable software initialization** 并将 **Software initialization source** 设置为 `Input port` 时出现。

**数据类型：** `Boolean`

### **cmp** — 用于比较位置的值 标量

生成位置比较同步信号的输入值。

#### 依赖

此端口仅在 **Compare output** 选项卡中，选择 **Enable position-compare sync signal output** 并将 **Compare value source** 设置为 `Input port` 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **iel** — 软件索引标记 标量

用于锁存位置计数器的软件索引事件标记。

#### 依赖

此端口仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on index event**。
- 将 **Index event latch of position counter** 设置为 `Software index marker via input port`。

**注意**

在 **Compare output** 选项卡中，如果 **Sync output pin selection** 设置为 `Index pin is used for sync output`，则 **Index event latch of position counter** 参数不能设置为 `Software index marker via input port`。

**数据类型：** `Boolean`
### 输出

### **qposcnt** — 位置计数器信号 标量

从位置计数器与控制单元（PCCU）接收的位置计数器信号（PCSOUT）。

#### 依赖

此端口仅在 **Position counter** 选项卡中，选择 **Output position counter** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **pcef** — 错误时的位置计数器错误标志 标量

在发生错误时输出位置计数器错误标志。

- `0` — 上次索引转换期间未发生错误。
- `1` — 位置计数器错误。

#### 依赖

此端口仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on an index event`。
- 选择 **Output position counter error flag**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qdf** — 正交模块方向标志 标量

正交模块的方向标志。

- `0` — 逆时针旋转（或反向运动）。
- `1` — 顺时针旋转（或正向运动）。

#### 依赖

此端口仅在 **General** 选项卡中，选择 **Quadrature direction flag output port** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmr** — 捕获定时器信号 标量

输出 eQEP 捕获定时器信号。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Output capture timer** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprd** — 捕获周期信号 标量

输出捕获周期信号，该信号保存最近连续 eQEP 位置事件之间的周期计数值。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Output capture period timer** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **coef** — eQEP 溢出错误标志 标量

在单位位置事件之间捕获定时器溢出时输出溢出错误标志（COEF 标志）。

- `0` — 未发生溢出。
- `1` — eQEP 捕获定时器寄存器（QEPCTMR）中发生溢出。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Enable and output overflow error flag** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **cdef** — 方向变化错误标志 标量

输出方向变化错误标志。

- `0` — 未发生捕获方向错误。
- `1` — 在两个捕获位置事件之间发生方向变化。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Enable and output direction change error flag** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmrlat** — 捕获定时器锁存值 标量

输出来自 QCTMRLAT 寄存器的捕获定时器锁存值。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Output capture timer latched value** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprdlat** — 捕获定时器周期锁存值 标量

输出来自 QCPRDLAT 寄存器的捕获定时器周期锁存值。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Output capture timer period latched value** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposlat** — 位置计数器锁存值 标量

输出来自 QPOSLAT 寄存器的位置计数器锁存值。

#### 依赖

此端口仅在 **Speed calculation** 选项卡中，选择 **Enable eQEP capture** 和 **Output position counter latched value** 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposilat** — 在索引事件上锁存位置计数器 标量

eQEP 索引输入可配置为在该引脚上发生确定事件时锁存位置计数器寄存器（QPOSCNT）作为输出。

#### 依赖

此端口仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on index event**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposslat** — 在选通事件上锁存位置计数器 标量

eQEP 选通输入可配置为在该引脚上发生确定事件时锁存位置计数器寄存器（QPOSCNT）作为输出。

#### 依赖

此端口仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on strobe event**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
## 参数
```yaml
parameters:
- name: Module
  summary: 用于获取位置、方向和速度的 eQEP 模块 eQEP1（默认）| eQEP2 | eQEP3
  group: 常规
- name: Position counter mode
  summary: 与 eQEP 外设输入编码方式匹配的模式 Quadrature-count（默认）| Direction-count | Up-count | Down-count
  group: 常规
- name: Positive rotation
  summary: 旋转方向 Clockwise（默认）| Counterclockwise
  group: 常规
- name: External clock rate
  summary: '测量分辨率 2x resolution: Count the rising/falling edge（默认）| 1x resolution: Count the rising edge only'
  group: 常规
- name: Quadrature direction flag output port
  summary: 为方向标志创建端口 off（默认）| on
  group: 常规
- name: Invert input QEPxX polarity
  summary: 反转 eQEP 输入极性 off（默认）| on
  group: 常规
- name: Index pulse gating option
  summary: 使能索引脉冲与选通输入的门控 off（默认）| on
  group: 常规
- name: Sample time
  summary: 模块读取位置计数器的频率 0.0001（默认）| -1 | 标量
  group: 常规
- name: Output position counter
  summary: 输出位置计数器信号 on（默认）| off
  group: Position counter
- name: Maximum position counter value (0~4294967295)
  summary: 指定最大位置计数器值 4294967295（默认）| [0, 4,294,967,295] 范围内的整数
  group: Position counter
- name: Enable set to init value on index event
  summary: 使能在索引事件上将位置计数器设置为初始化值的选项 off（默认）| on
  group: Position counter
- name: Set to init value on index event
  summary: 位置计数器的初始化值 Rising edge（默认）| Falling edge
  group: Position counter
- name: Enable set to init value on strobe event
  summary: 使能在选通事件上将位置计数器设置为初始化值的选项 off（默认）| on
  group: Position counter
- name: Set to init value on strobe event
  summary: 设置位置计数器的初始化值 Rising edge（默认）| Depending on direction
  group: Position counter
- name: Enable software initialization
  summary: 使能通过软件设置位置计数器初始化值的选项 off（默认）| on
  group: Position counter
- name: Software initialization source
  summary: 指定位置计数器的初始化来源 Input port（默认）| Set to init value at start up
  group: Position counter
- name: Initialization value (0~4294967295)
  summary: 位置计数器的初始化值 2147483648 | [0, 4,294,967,295] 范围内的整数
  group: Position counter
- name: Position counter reset mode
  summary: 复位位置计数器 Reset on an index event（默认）| Reset on the maximum position | Reset on the first index event | Reset on
    a time unit event
  group: Position counter
- name: Output position counter error flag
  summary: 在错误时输出位置计数器错误标志 off（默认）| on
  group: Position counter
- name: Output latch position counter on index event
  summary: 在索引事件时锁存位置计数器 off（默认）| on
  group: Position counter
- name: Index event latch of position counter
  summary: 配置位置计数器在事件时锁存 Rising edge（默认）| Falling edge | Software index marker via input port
  group: Position counter
- name: Output latch position counter on strobe event
  summary: 在选通事件时锁存位置计数器 off（默认）| on
  group: Position counter
- name: Strobe event of latched position counter
  summary: 配置位置计数器在选通时锁存 Rising edge（默认）| Depending on direction
  group: Position counter
- name: Enable QEP capture
  summary: 启用边沿捕获单元 off（默认）| on
  group: Speed calculation
- name: Output capture timer
  summary: 输出捕获定时器 off（默认）| on
  group: Speed calculation
- name: Output capture period timer
  summary: 输出捕获周期 off（默认）| on
  group: Speed calculation
- name: eQEP capture timer prescaler
  summary: 预分频捕获定时器时钟频率 128（默认）| 1 | 2 | 4 | 8 | 16 | 32 | 64
  group: Speed calculation
- name: Unit position event prescaler
  summary: 预分频正交时钟 128（默认）| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 256 | 512 | 1024 | 2048
  group: Speed calculation
- name: Enable and output overflow error flag
  summary: 当捕获定时器溢出时输出溢出错误标志 off（默认）| on
  group: Speed calculation
- name: Enable and output direction change error flag
  summary: 输出方向变化错误标志 off（默认）| on
  group: Speed calculation
- name: Capture timer and position
  summary: QEP 捕获锁存模式 On position counter read（默认）| On unit time-out event
  group: Speed calculation
- name: Unit timer period (0~4294967295)
  summary: 设置单位定时器周期 100000000（默认）| 范围 [0, 4,294,967,295] 内的值
  group: Speed calculation
- name: Output capture timer latched value
  summary: 输出捕获定时器锁存值 off（默认）| on
  group: Speed calculation
- name: Output capture timer period latched value
  summary: 输出捕获定时器周期锁存值 off（默认）| on
  group: Speed calculation
- name: Output position counter latched value
  summary: 输出位置计数器锁存值 off（默认）| on
  group: Speed calculation
- name: Enable position-compare sync signal output
  summary: 启用位置比较同步信号输出 off（默认）| on
  group: Compare output
- name: Sync output pin selection
  summary: 用于同步信号的 GPIO 引脚 Index pin is used for sync output（默认）| Strobe pin is used for sync output
  group: Compare output
- name: Compare value source
  summary: 位置比较值的来源 Specify via dialog（默认）| Input port
  group: Compare output
- name: Position compare shadow load mode
  summary: 生成位置比较同步信号的影子模式 Load on QPOSCNT=0（默认）| Shadow disabled(load immediate) | Load on QPOSCNT=QPOSCMP
  group: Compare output
- name: Position compare value (0~4294967295)
  summary: 用于比较位置的值 4294967295（默认）| 范围 [0, 4,294,967,295] 内的值
  group: Compare output
- name: Sync output pulse width (1~4096)
  summary: 位置比较同步输出信号的脉冲宽度 1（默认）| 范围 [0, 4,096] 内的值
  group: Compare output
- name: Polarity of sync output
  summary: 同步输出的极性 Active high（默认）| Active low
  group: Compare output
- name: Watchdog timer enable
  summary: 启用看门狗超时标志 off（默认）| on
  group: Watchdog unit
- name: Watchdog timer
  summary: 看门狗定时器的超时值 65535（默认）| 范围 [0, 65,535] 内的值
  group: Watchdog unit
- name: Position counter error interrupt enable
  summary: 启用位置计数器错误中断 off（默认）| on
  group: Interrupt
- name: Quadrature phase error interrupt enable
  summary: 启用正交相位错误中断 off（默认）| on
  group: Interrupt
- name: Quadrature direction change interrupt enable
  summary: 启用正交方向变化中断 off（默认）| on
  group: Interrupt
- name: Watchdog timeout interrupt enable
  summary: 启用看门狗超时中断 off（默认）| on
  group: Interrupt
- name: Position counter underflow interrupt enable
  summary: 启用位置计数器下溢中断 off（默认）| on
  group: Interrupt
- name: Position counter overflow interrupt enable
  summary: 启用位置计数器溢出中断 off（默认）| on
  group: Interrupt
- name: Position-compare ready interrupt enable
  summary: 启用位置比较就绪中断 off（默认）| on
  group: Interrupt
- name: Position-compare match interrupt enable
  summary: 启用位置比较匹配中断 off（默认）| on
  group: Interrupt
- name: Strobe event latch interrupt enable
  summary: 启用选通事件锁存中断 off（默认）| on
  group: Interrupt
- name: 索引事件锁存中断使能
  summary: 使能索引事件锁存中断 off（默认）| on
  group: Interrupt
- name: 单元超时中断使能
  summary: 使能单元超时中断 off（默认）| on
  group: Interrupt
```

### 常规

### **Module** — 用于获取位置、方向和速度的 eQEP 模块 `eQEP1`（默认）| `eQEP2` | `eQEP3`

用于获取位置、方向和速度信息的 eQEP 外设模块。不同 C2000™ 处理器支持的 eQEP 模块数量不同。

### **Position counter mode** — 与 eQEP 外设输入编码方式匹配的模式 `Quadrature-count`（默认）| `Direction-count` | `Up-count` | `Down-count`

eQEP 外设输入为 QEPA、QEPB、QEPI 和 QEPS。通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** > **eQEP** 来配置这些输入的 GPIO 引脚。

eQEP 外设的输入信号 QEPA 和 QEPB 由 eQEP 外设中的正交解码单元（QDU）处理，以产生时钟（QCLK）和方向（QDIR）信号。选择与 eQEP 模块输入编码方式匹配的位置计数器模式：

- `Quadrature-count` — 两个相位相差 90 度的方波信号（A 和 B）发送到 eQEP 外设。QDU 使用这两个输入的相位关系生成正交时钟和方向信号。
- `Direction-count` — 方向和时钟信号直接发送到 eQEP 外设。QEPA 引脚提供时钟输入，QEPB 引脚提供方向输入。
- `Up-count` — 位置计数器用于测量 QEPA 引脚上信号的频率。在此模式下方向硬连线为向上计数。
- `Down-count` — 位置计数器用于测量 QEPA 引脚上信号的频率。在此模式下方向硬连线为向下计数。

### **Positive rotation** — 旋转方向 `Clockwise`（默认）| `Counterclockwise`

设置旋转方向。

如果选择 `Clockwise`，则执行正交计数操作时不交换馈送到 QDU 的正交时钟输入。

如果选择 `Counterclockwise`，则通过交换馈送到 QDU 的正交时钟输入来执行反向计数。正交解码器反转计数方向。

#### 依赖

此参数仅在 **General** 选项卡中将 **Position counter mode** 设置为 `Quadrature-count` 时出现。

### **External clock rate** — 测量分辨率 `2x resolution: Count the rising/falling edge`（默认）| `1x resolution: Count the rising edge only`

选择位置计数器用作输入的时钟发生器分辨率，使计数在 QEPA 输入的上升沿和下降沿发生，或仅在上升沿发生。选择前者可将测量分辨率提高 2 倍。

#### 依赖

此参数仅在将 **Position counter mode** 设置为 `Direction-count`、`Up-count` 或 `Down-count` 时出现。

### **Quadrature direction flag output port** — 为方向标志创建端口 `off`（默认）| `on`

在模块上创建一个端口（qdf），用于给出正交模块的方向标志。

#### 依赖

此参数仅在 **General** 选项卡中，**Position counter mode** 设置为 `Quadrature-count` 时出现。

### **Invert input QEPxX polarity** — 反转 eQEP 输入极性 `off`（默认）| `on`

反转 eQEP 外设输入的极性。**Invert input QEPxA polarity** 复选框对应 QEPA，**Invert input QEPxB polairty** 对应 QEPB，依此类推。

### **Index pulse gating option** — 使能索引脉冲与选通输入的门控 `off`（默认）| `on`

使能外设输入索引信号与外设输入选通信号的门控。在这种情况下，仅当外设输入信号 eQEPxI 和 eQEPxS 均为高电平时，内部索引信号才为高电平。

### **Sample time** — 模块读取位置计数器的频率 `0.0001`（默认）| `-1` | 标量

模块的采样时间，以秒为单位。要异步执行此模块，请将此参数设置为 `-1`。

### Position counter

### **Output position counter** — 输出位置计数器信号 `on`（默认）| `off`

输出位置计数器与控制单元（PCCU）的位置计数器信号 PCSOUT。位置计数器寄存器根据输入方向在每个 eQEP 脉冲上递增或递减计数。计数值与距给定参考点的位置成正比。

### **Maximum position counter value (0~4294967295)** — 指定最大位置计数器值 `4294967295`（默认）| [0, 4,294,967,295] 范围内的整数

输入位置计数器的最大值（QPOSMAX）。如果位置计数器达到 QPOSMAX，则在计数器下一次递增时位置计数器设置为 `0`。如果位置计数器为 `0`，则在计数器下一次递减时位置计数器设置为 QPOSMAX。

### **Enable set to init value on index event** — 使能在索引事件上将位置计数器设置为初始化值的选项 `off`（默认）| `on`

使能在索引事件上将位置计数器设置为其初始化值的选项。

### **Set to init value on index event** — 位置计数器的初始化值 `Rising edge`（默认）| `Falling edge`

在索引事件的上升沿或下降沿将位置计数器设置为其初始化值。

#### 依赖

此参数仅在 **Position counter** 选项卡中，选择 **Enable set to init value on index event** 时出现。

### **Enable set to init value on strobe event** — 使能在选通事件上将位置计数器设置为初始化值的选项 `off`（默认）| `on`

使能在选通事件上将位置计数器设置为其初始化值的选项。

### **Set to init value on strobe event** — 设置位置计数器的初始化值 `Rising edge`（默认）| `Depending on direction`

`Rising edge` 选项在选通输入的上升沿将位置计数器设置为其初始化值。`Depending on direction` 选项在以下情况将位置计数器设置为其初始化值：

- 正向运动时，在选通输入的上升沿。
- 反向运动时，在选通输入的下降沿。

#### 依赖

此参数仅在 **Position counter** 选项卡中，选择 **Enable set to init value on strobe event** 时出现。

### **Enable software initialization** — 使能通过软件设置位置计数器初始化值的选项 `off`（默认）| `on`

允许使用软件将位置计数器设置为其初始化值。

### **Software initialization source** — 指定位置计数器的初始化来源 `Input port`（默认）| `Set to init value at start up`

选择 `Set to init value at start up` 选项可在程序开始执行时将位置计数器初始化为 **Initialization value** 中输入的值。选择 `Input port` 选项可根据输入初始化信号（输入端口 **swi**）动态更新初始化值。如果输入 **swi** 为 `true`，则位置计数器初始化为 **Initialization value**。

#### 依赖

此参数仅在 **Position counter** 选项卡中，选择 **Enable software initialization** 时出现。

### **Initialization value (0~4294967295)** — 位置计数器的初始化值 `2147483648` | [0, 4,294,967,295] 范围内的整数

输入位置计数器的初始化值。

#### 依赖

此参数仅在选择 **Enable set to init value on index event**、**Enable set to init value on strobe event** 或 **Enable software initialization** 时出现。

### **Position counter reset mode** — 复位位置计数器 `Reset on an index event`（默认）| `Reset on the maximum position` | `Reset on the first index event` | `Reset on a time unit event`

位置计数器复位模式，取决于 eQEP 模块所配合工作的系统性质。

- `Reset on an index event` — 如果索引事件在正向方向上发生，则位置计数器在下一个 eQEP 时钟时复位为 0。如果索引事件在反向方向上发生，则位置计数器在下一个 eQEP 时钟时复位为 QPOSMAX 寄存器中的值。
- `Reset on the maximum position` — 在正向方向上，当位置计数器等于 QPOSMAX 时，位置计数器在下一个 eQEP 时钟时复位为 0，并置位位置计数器溢出标志。在反向方向上，当位置计数器等于 0 时，位置计数器在下一个 QEP 时钟时复位为 QPOSMAX，并置位位置计数器下溢标志。
- `Reset on the first index event` — 如果索引事件在正向方向上发生，位置计数器在下一个 eQEP 时钟时复位为 0。如果索引事件在反向方向上发生，位置计数器在下一个 eQEP 时钟时复位为 QPOSMAX 寄存器中的值。仅在首次索引事件发生时，使用 `Reset on the first index event` 选项复位位置计数器。在首次索引事件发生之后，位置计数器基于最大位置进行复位。
- `Reset on a unit time event` — 在单位时间事件时，QPOSCNT 值锁存到 QPOSLAT 寄存器。然后，QPOSCNT 寄存器在正向方向上复位为 0，在反向方向上复位为 QPOSMAX。您可以将此选项用于频率测量。

### **Output position counter error flag** — 在错误时输出位置计数器错误标志 `off`（默认）| `on`

在错误时输出位置计数器错误标志。当您选择此选项时，将创建输出端口 **pcef**。

#### 依赖关系

此参数仅在 **Position counter** 选项卡中将 **Position counter reset mode** 设置为 `Reset on an index event` 时出现。

### **Output latch position counter on index event** — 在索引事件时锁存位置计数器 `off`（默认）| `on`

当启用此选项时，位置计数器 QPOSCNT 在选通引脚上发生事件时锁存到 QPOSLAT 中。

#### 依赖关系

此参数仅在 **Position counter** 选项卡中将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event` 时出现。

### **Index event latch of position counter** — 配置位置计数器在事件时锁存 `Rising edge`（默认）| `Falling edge` | `Software index marker via input port`

配置 eQEP 位置计数器在所选索引事件时锁存。

#### 依赖关系

此参数仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on index event**。

### **Output latch position counter on strobe event** — 在选通事件时锁存位置计数器 `off`（默认）| `on`

eQEP 选通输入可配置为在此引脚上发生确定事件时将位置计数器（QPOSCNT）锁存到 QPOSSLAT 中。此选项在每次选通事件时锁存位置计数器。

#### 依赖关系

此参数仅在 **Position counter** 选项卡中将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event` 时出现。

### **Strobe event of latched position counter** — 配置位置计数器在选通时锁存 `Rising edge`（默认）| `Depending on direction`

`Rising edge` 在选通事件输入的上升沿锁存。`Depending on direction` 在正向方向的上升沿和反向方向的下降沿锁存。

#### 依赖关系

此参数仅在 **Position counter** 选项卡中满足以下条件时出现：

- 将 **Position counter reset mode** 设置为 `Reset on the maximum position` 或 `Reset on the first index event`。
- 选择 **Output latch position counter on strobe event**。

### Speed calculation

要查看此选项卡的其他参数，请选择 **Enable QEP capture** 选项。

### **Enable QEP capture** — 启用边沿捕获单元 `off`（默认）| `on`

eQEP 外设包含一个集成的边沿捕获单元，用于测量单位位置事件之间经过的时间。此选项启用边沿捕获单元。

### **Output capture timer** — 输出捕获定时器 `off`（默认）| `on`

从 QCTMR 寄存器输出捕获定时器值。

### **Output capture period timer** — 输出捕获周期 `off`（默认）| `on`

从 QCPRD 寄存器输出最近连续 eQEP 位置事件之间的周期计数值。

### **eQEP capture timer prescaler** — 预分频捕获定时器时钟频率 `128`（默认）| `1` | `2` | `4` | `8` | `16` | `32` | `64`

eQEP 捕获定时器由预分频后的 SYSCLKOUT 驱动。捕获定时器时钟频率为 SYSCLKOUT 的频率除以您为此参数选择的值。

### **Unit position event prescaler** — 预分频正交时钟 `128`（默认）| `1` | `2` | `4` | `8` | `16` | `32` | `64` | `256` | `512` | `1024` | `2048`

单位位置事件的时序由正交时钟（QCLK）预分频确定。QCLK 除以您为此参数选择的预分频值。

### **Enable and output overflow error flag** — 当捕获定时器溢出时输出溢出错误标志 `off`（默认）| `on`

在单位位置事件之间发生捕获定时器溢出时，启用并输出 eQEP 溢出错误标志（COEF）。

### **Enable and output direction change error flag** — 输出方向变化错误标志 `off`（默认）| `on`

在单位位置事件之间发生方向变化时，启用并输出方向变化错误标志（CDEF）。

### **Capture timer and position** — QEP 捕获锁存模式 `On position counter read`（默认）| `On unit time-out event`

触发捕获定时器和捕获周期寄存器锁存的事件：

- `On position counter read` — 在处理器读取位置计数器时锁存。当处理器读取 QPOSCNT 寄存器时，捕获定时器和捕获周期值锁存到 QCTMRLAT 和 QCPRDLAT 寄存器中。
- `On unit time-out event` — 在单位超时时锁存。在单位超时时，位置计数器、捕获定时器和捕获周期值锁存到 QPOSLAT、QCTMRLAT 和 QCPRDLAT 寄存器中。

### **Unit timer period (0~4294967295)** — 设置单位定时器周期 `100000000`（默认）| 范围 [0, 4,294,967,295] 内的值

设置单位定时器周期。

#### 依赖关系

此参数仅在将 **Capture timer and position** 设置为 `On unit time-out event` 时出现。

### **Output capture timer latched value** — 输出捕获定时器锁存值 `off`（默认）| `on`

在输出端口 **qctmrlat** 输出 QCTMRLAT 寄存器中的捕获定时器锁存值。

### **Output capture timer period latched value** — 输出捕获定时器周期锁存值 `off`（默认）| `on`

在输出端口 **qcprdlat** 输出 QCPRDLAT 寄存器中的捕获定时器周期锁存值。

### **Output position counter latched value** — 输出位置计数器锁存值 `off`（默认）| `on`

在输出端口 **qposlat** 输出 QPOSLAT 寄存器中的位置计数器锁存值。

### Compare output

要查看此选项卡的其他参数，请选择 **Enable position-compare sync signal output** 选项。

### **Enable position-compare sync signal output** — 启用位置比较同步信号输出 `off`（默认）| `on`

eQEP 外设包含一个位置比较单元，当位置计数器寄存器（QPOSCNT）和位置比较寄存器（QPOSCMP）的值匹配时，该单元生成位置比较同步信号。此选项启用位置比较同步信号输出。同步信号可以使用 eQEP 外设的索引引脚或选通引脚输出。

### **Sync output pin selection** — 用于同步信号的 GPIO 引脚 `Index pin is used for sync output`（默认）| `Strobe pin is used for sync output`

用于同步信号输出的 GPIO 引脚。使用 eQEP 外设的索引引脚或选通引脚输出位置比较同步信号。

### **Compare value source** — 位置比较值的来源 `Specify via dialog`（默认）| `Input port`

用于位置比较寄存器（QPOSCMP）的值的来源。当此参数设置为 `Input port` 时，将创建输入端口 **cmp**。

### **Position compare shadow load mode** — 生成位置比较同步信号的影子模式 `Load on QPOSCNT=0`（默认）| `Shadow disabled(load immediate)` | `Load on QPOSCNT=QPOSCMP`

此参数允许您启用或禁用更新位置比较（QPOSCMP）寄存器的影子模式。当启用影子模式时，您还可以选择触发将影子寄存器值加载到活动寄存器的事件。当禁用影子模式时，处理器直接将值加载到活动寄存器中。

`Load on QPOSCNT=0` 在位置计数器为零事件时加载，`Load on QPOSCNT=QPOSCMP` 在 QPOSCNT 和 QPOSCMP 值匹配时加载。当您选择这些选项时，影子模式被启用。

### **Position compare value (0~4294967295)** — 用于比较位置的值 `4294967295`（默认）| 范围 [0, 4,294,967,295] 内的值

此值被加载到位置比较寄存器（QPOSCMP）中。

#### 依赖关系

此参数仅在将 **Compare value source** 设置为 `Specify via dialog` 时出现。

### **Sync output pulse width (1~4096)** — 位置比较同步输出信号的脉冲宽度 `1`（默认）| 范围 [0, 4,096] 内的值

位置比较单元中的脉冲展宽逻辑在位置比较匹配时生成可编程的位置比较同步脉冲输出。

一个从 `1` 到 `4096` 的值，用于确定位置比较同步输出信号的脉冲宽度。输出脉冲的宽度以 SYSCKOUT 周期为单位，是输入值的四倍。

### **Polarity of sync output** — 同步输出的极性 `Active high`（默认）| `Active low`

选择所生成同步输出信号的极性。

### Watchdog unit

### **Watchdog timer enable** — 启用看门狗超时标志 `off`（默认）| `on`

eQEP 外设包含一个看门狗定时器，用于监视正交时钟以指示运动控制系统正在运行。该定时器在正交时钟的边沿跳变时复位。看门狗单元生成一个中断，您可以在 **Interrupt** 选项卡中启用该中断。

### **Watchdog timer** — 看门狗定时器的超时值 `65535`（默认）| 范围 [0, 65,535] 内的值

看门狗单元生成中断之后的时间段。

#### 依赖关系

此参数仅在您选择 **Watchdog timer enable** 时出现。

### 信号数据类型

当您在其他选项卡中选择信号作为输出时，相应的信号会出现在此选项卡中。例如，当您在 **Position counter** 选项卡上选择 **Output position counter** 选项时，**Position counter value data type** 选项会出现在此选项卡上。使用此选项卡，您可以选择信号的数据类型。

有效的数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和 `boolean`。

下表总结了您可以在 **Signal data types** 选项卡中设置数据类型的选项：

| Pane | Option |
| --- | --- |
| 通用 | 正交方向标志输出端口 |
| Position counter | Output position counter（默认选中） |
| Output position counter error flag |
| Output latch position counter on index event |
| Output latch position counter on strobe event |
| Speed calculation | Output capture timer |
| Output capture period timer |
| 启用并输出溢出错误标志 |
| 启用并输出方向变化错误标志 |
| 输出捕获定时器锁存值 |
| 输出捕获定时器周期锁存值 |
| 输出位置计数器锁存值 |

### Interrupt

与此选项卡中的设置相对应，特定事件的中断被启用或禁用。所生成的中断与 C28x Hardware Interrupt 配合使用。

### **Position counter error interrupt enable** — 启用位置计数器错误中断 `off`（默认）| `on`

启用位置计数器错误中断。位置计数器中断仅在索引事件复位模式下生成。当 eQEP 配置为此模式时，位置计数器值锁存到 QPOSILAT 寄存器，并且在每个索引事件标记上记录方向信息。如果锁存值不等于 0 或 QPOSMAX，则生成位置计数器错误中断。

### **Quadrature phase error interrupt enable** — 启用正交相位错误中断 `off`（默认）| `on`

启用正交相位错误中断。在正交计数模式下，正交输入 QEPA 和 QEPB 预期相位相差 90 度。当在 QEPA 和 QEPB 信号上同时检测到边沿跳变时，生成正交相位错误中断。

### **Quadrature direction change interrupt enable** — 启用正交方向变化中断 `off`（默认）| `on`

当计数方向变化时，生成正交方向变化中断。

### **Watchdog timeout interrupt enable** — 启用看门狗超时中断 `off`（默认）| `on`

eQEP 外设包含一个监视正交时钟的看门狗定时器。如果在看门狗定时器达到看门狗周期之前未检测到正交时钟事件，则发生超时并生成看门狗超时中断。

### **Position counter underflow interrupt enable** — 启用位置计数器下溢中断 `off`（默认）| `on`

启用位置计数器下溢中断。在反向方向上，如果位置计数器达到 0，则位置计数器在下一个 QEP 时钟时复位为 QPOSMAX，并生成位置计数器下溢中断。

### **Position counter overflow interrupt enable** — 启用位置计数器溢出中断 `off`（默认）| `on`

启用位置计数器溢出中断。在正向方向上，如果位置计数器达到 QPOSMAX，则位置计数器在下一个 QEP 时钟时复位为 0，并生成位置计数器溢出中断。

### **Position-compare ready interrupt enable** — 启用位置比较就绪中断 `off`（默认）| `on`

启用位置比较就绪中断。当位置比较寄存器配置为影子模式时，在影子寄存器值加载到活动寄存器之后，生成位置比较就绪中断。

### **Position-compare match interrupt enable** — 启用位置比较匹配中断 `off`（默认）| `on`

启用位置比较匹配中断。当位置计数器值 QPOSCNT 与活动位置比较寄存器 QPOSCMP 匹配时，生成位置比较匹配中断。

### **Strobe event latch interrupt enable** — 启用选通事件锁存中断 `off`（默认）| `on`

启用选通事件锁存中断。当在选通事件锁存期间位置计数器锁存到 QPOSSLAT 寄存器时，生成选通事件锁存中断。

### **索引事件锁存中断使能** — 使能索引事件锁存中断 `off`（默认）| `on`

使能索引事件锁存中断。当位置计数器在索引事件锁存期间锁存到 QPOSILAT 寄存器时，将生成选通事件锁存中断。

### **单元超时中断使能** — 使能单元超时中断 `off`（默认）| `on`

使能单元超时中断。当单元定时器与单元周期匹配时，将生成单元超时中断。
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

增强型正交编码器脉冲（eQEP）模块与线性或旋转增量式编码器配合使用，从旋转电机获取位置、方向和速度信息。

eQEP 外设模块的输入包括 QEPA、QEPB、QEPI（索引）和 QEPS（选通）。

要将您的设备配置为与该模块配合使用，请导航至 **Model Configuration Parameters** > **Hardware Implementation**，在 **Hardware board** 处选择您的设备，然后展开 **Target hardware resources**。
