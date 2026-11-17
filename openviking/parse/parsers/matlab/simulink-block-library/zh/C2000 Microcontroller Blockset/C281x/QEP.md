---
type: simulink-block
title: 'C281x QEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C281x'
documentation_page: 'c281xqep'
documentation_source_path: 'ref/c281xqep.html'
language: zh-CN
chinese_source: worker-translation
---

# C281x QEP

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Module**
:   指定要使用哪些 QEP 引脚：

    - `A` — 使用 QEP1 和 QEP2 引脚。
    - `B` — 使用 QEP3 和 QEP4 引脚。

**Counting mode**
:   指定如何对 QEP 脉冲进行计数：

    - `Counter` — 基于 GP Timer 2（对于 EVB 为 GP Timer 4）对脉冲进行计数。
    - `RPM` — 计算每分钟转数。

**Positive rotation**
:   定义将 `Clockwise` 还是 `Counterclockwise` 用作正旋转方向。仅当选择 `RPM` 时，此字段才会出现。

**Initial count**
:   计数器的初始值。该值默认为 `0`。

**Encoder resolution (pulse/revolution)**
:   每转的 QEP 脉冲数。仅当选择 `RPM` 时，此字段才会出现。

**Enable QEP index**
:   当 CAP3\_QEPI1 上的 QEP index 输入从低电平转换为高电平时，将 QEP 计数器复位为零。

**Enable index qualification mode**
:   对 CAP3\_QEPI1 上的 QEP index 输入进行限定。在将 index 信号判定为有效之前，检查 CAP1\_QEP1 和 CAP2\_QEP2 上的电平是否为高电平。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入从 `0` 到 `65535` 的值。该值默认为 `65535`。

    如果知道一个时钟周期的长度，就可以轻松计算出要为定时器周期设置多少个时钟周期。以下计算确定一个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Sample time**
:   从 QEP 引脚连续读取之间的时间间隔，以秒为单位。

**数据类型**
:   QEP 引脚数据的数据类型。电路将数据读取为 16 位数据，然后将其转换为所选数据类型。有效数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

**Module**
:   指定要使用哪些 QEP 引脚：

    - `A` — 使用 QEP1 和 QEP2 引脚。
    - `B` — 使用 QEP3 和 QEP4 引脚。

**Counting mode**
:   指定如何对 QEP 脉冲进行计数：

    - `Counter` — 基于 GP Timer 2（对于 EVB 为 GP Timer 4）对脉冲进行计数。
    - `RPM` — 计算每分钟转数。

**Positive rotation**
:   定义将 `Clockwise` 还是 `Counterclockwise` 用作正旋转方向。仅当选择 `RPM` 时，此字段才会出现。

**Initial count**
:   计数器的初始值。该值默认为 `0`。

**Encoder resolution (pulse/revolution)**
:   每转的 QEP 脉冲数。仅当选择 `RPM` 时，此字段才会出现。

**Enable QEP index**
:   当 CAP3\_QEPI1 上的 QEP index 输入从低电平转换为高电平时，将 QEP 计数器复位为零。

**Enable index qualification mode**
:   对 CAP3\_QEPI1 上的 QEP index 输入进行限定。在将 index 信号判定为有效之前，检查 CAP1\_QEP1 和 CAP2\_QEP2 上的电平是否为高电平。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入从 `0` 到 `65535` 的值。该值默认为 `65535`。

    如果知道一个时钟周期的长度，就可以轻松计算出要为定时器周期设置多少个时钟周期。以下计算确定一个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Sample time**
:   从 QEP 引脚连续读取之间的时间间隔，以秒为单位。

**数据类型**
:   QEP 引脚数据的数据类型。电路将数据读取为 16 位数据，然后将其转换为所选数据类型。有效数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

正交编码器脉冲电路

# C281x QEP

正交编码器脉冲电路

每个 F2812 Event Manager 都有三个捕获单元，可记录其捕获单元引脚上的跳变。Event Manager A (EVA) 使用捕获单元 1、2 和 3。Event Manager B (EVB) 使用捕获单元 4、5 和 6。

正交编码器脉冲 (QEP) 电路对这些捕获单元引脚上的正交编码输入脉冲进行解码和计数。QEP 脉冲是两个脉冲序列，其频率可变，并具有固定的 90 度（或四分之一周期）相移。该电路对 QEP 脉冲的两个边沿都进行计数，因此 QEP 时钟的频率是输入序列频率的四倍。

QEP 与光学编码器结合使用，可用于从旋转机械获取速度和位置信息。QEP 电路中的逻辑通过哪个序列领先来确定旋转方向。对于模块 A，如果 QEP1 序列领先，则通用 (GP) Timer 向上计数；如果 QEP2 序列领先，则定时器向下计数。脉冲计数和频率决定角位置和速度。

C281x QEP 模块与其他 C281 模块共享 GP Timer。有关共享定时器的更多信息和指导，请参阅 Sharing General Purpose Timers Between C281x Peripherals。

- C281x QEP 模块
