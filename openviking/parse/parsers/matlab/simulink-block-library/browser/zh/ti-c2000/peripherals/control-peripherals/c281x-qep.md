---
type: simulink-block
title: 'C281x QEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'c281xqep'
documentation_source_path: 'ref/c281xqep.html'
language: zh-CN
chinese_source: worker-translation
---

# C281x QEP

## 端口

在 R2025b 中未记录。

## 参数

**模块**
:   指定要使用的 QEP 引脚：

    - `A` — 使用 QEP1 和 QEP2 引脚。
    - `B` — 使用 QEP3 和 QEP4 引脚。

**计数模式**
:   指定如何计数 QEP 脉冲：

    - `Counter` — 基于 GP Timer 2（对于 EVB 为 GP Timer 4）对脉冲进行计数。
    - `RPM` — 计数每分钟转数。

**正向旋转**
:   定义使用 `Clockwise` 还是 `Counterclockwise` 作为正旋转方向。仅当选择 `RPM` 时显示此字段。

**初始计数**
:   计数器的初始值。默认值为 `0`。

**编码器分辨率 (pulse/revolution)**
:   每转的 QEP 脉冲数。仅当选择 `RPM` 时显示此字段。

**使能 QEP 索引**
:   当 CAP3\_QEPI1 上的 QEP 索引输入从低电平跳变到高电平时，将 QEP 计数器复位为零。

**使能索引限定模式**
:   限定 CAP3\_QEPI1 上的 QEP 索引输入。在将索引信号确认为有效之前，检查 CAP1\_QEP1 和 CAP2\_QEP2 上的电平是否为高。

**定时器周期**
:   设置定时器周期的长度，以 clock cycles 为单位。输入从 `0` 到 `65535` 的值。默认值为 `65535`。

    如果知道一个 clock cycle 的长度，就可以轻松计算应为定时器周期设置多少个 clock cycles。以下计算确定一个 clock cycle 的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个 clock cycle 为 1/.586 MHz，即 1.706 µs。

**采样时间**
:   从 QEP 引脚连续读取之间的时间间隔，以 seconds 为单位。

**数据类型**
:   QEP 引脚数据的数据类型。电路将数据读取为 16-bit 数据，然后将其转换为所选数据类型。有效数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

**模块**
:   指定要使用的 QEP 引脚：

    - `A` — 使用 QEP1 和 QEP2 引脚。
    - `B` — 使用 QEP3 和 QEP4 引脚。

**计数模式**
:   指定如何计数 QEP 脉冲：

    - `Counter` — 基于 GP Timer 2（对于 EVB 为 GP Timer 4）对脉冲进行计数。
    - `RPM` — 计数每分钟转数。

**正向旋转**
:   定义使用 `Clockwise` 还是 `Counterclockwise` 作为正旋转方向。仅当选择 `RPM` 时显示此字段。

**初始计数**
:   计数器的初始值。默认值为 `0`。

**编码器分辨率 (pulse/revolution)**
:   每转的 QEP 脉冲数。仅当选择 `RPM` 时显示此字段。

**使能 QEP 索引**
:   当 CAP3\_QEPI1 上的 QEP 索引输入从低电平跳变到高电平时，将 QEP 计数器复位为零。

**使能索引限定模式**
:   限定 CAP3\_QEPI1 上的 QEP 索引输入。在将索引信号确认为有效之前，检查 CAP1\_QEP1 和 CAP2\_QEP2 上的电平是否为高。

**定时器周期**
:   设置定时器周期的长度，以 clock cycles 为单位。输入从 `0` 到 `65535` 的值。默认值为 `65535`。

    如果知道一个 clock cycle 的长度，就可以轻松计算应为定时器周期设置多少个 clock cycles。以下计算确定一个 clock cycle 的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以 2 的高速时钟预分频器。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个 clock cycle 为 1/.586 MHz，即 1.706 µs。

**采样时间**
:   从 QEP 引脚连续读取之间的时间间隔，以 seconds 为单位。

**数据类型**
:   QEP 引脚数据的数据类型。电路将数据读取为 16-bit 数据，然后将其转换为所选数据类型。有效数据类型为 `auto`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

正交编码器脉冲电路

# C281x QEP

正交编码器脉冲电路

每个 F2812 事件管理器都有三个捕获单元，可记录其捕获单元引脚上的跳变。事件管理器 A (EVA) 使用捕获单元 1、2 和 3。事件管理器 B (EVB) 使用捕获单元 4、5 和 6。

正交编码器脉冲 (QEP) 电路对这些捕获单元引脚上的正交编码输入脉冲进行解码和计数。QEP 脉冲是两个频率变化且具有固定 90 degrees 相移（或周期的四分之一）的脉冲序列。该电路对 QEP 脉冲的两个边沿都进行计数，因此 QEP 时钟的频率是输入序列频率的四倍。

QEP 与光学编码器结合使用时，可用于从旋转机械获取速度和位置信息。QEP 电路中的逻辑通过哪个序列领先来确定旋转方向。对于模块 A，如果 QEP1 序列领先，则通用 (GP) 定时器向上计数；如果 QEP2 序列领先，则定时器向下计数。脉冲计数和频率确定角位置和速度。

C281x QEP 模块与其他 C281 模块共享 GP 定时器。有关共享定时器的更多信息和指南，请参阅《在 C281x 外设之间共享通用定时器》。

- C281x QEP 模块
