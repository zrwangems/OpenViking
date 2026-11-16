---
type: simulink-block
title: 'C281x Timer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / CLA, Watchdog, Timer'
documentation_page: 'c281xtimer'
documentation_source_path: 'ref/c281xtimer.html'
language: zh-CN
chinese_source: worker-translation
---

# C281x Timer

## 端口

未在 R2025b 中记录。

## 参数

**Module**, **Timer no**
:   选择要配置的四个可能定时器中的哪一个。将 **Module** 设置为 `A` 允许你在 **Timer no** 中选择 `Timer 1` 或 `Timer 2`。将 **Module** 设置为 `B` 允许你在 **Timer no** 中选择 `Timer 3` 或 `Timer 4`。

**Clock source**
:   当 **Timer no** 的值为 `Timer 2` 或 `Timer 4` 时，使用此参数选择事件定时器的时钟源。你可以选择 `Internal` 或 `QEP circuit`。选择 `Internal` 时，你可以配置其他选项，如 **Timer period source**、**Counting mode** 和 **Timer prescaler**。

**Timer period source**
:   选择事件定时器周期的来源。使用 `Specify via dialog` 通过 **Timer period** 设置周期。选择 `Input port` 可创建输入 **T**，它接受以时钟周期为单位的定时器周期值，范围为 `0` 到 `65535`。当 **Clock source** 设置为 `QEP circuit` 时，**Timer period source** 变为不可用。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入 `0` 到 `65535` 之间的值。该值默认为 `10000`。

    如果你知道一个时钟周期的长度，就可以轻松计算要为定时器周期设置多少个时钟周期。以下计算确定一个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以高速时钟预分频器 2。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Compare value source**
:   选择比较值的来源。使用 `Specify via dialog` 通过 **Compare value** 参数设置周期。选择 `Input port` 可创建模块输入 **W**，它接受比较值的值，范围为 `0` 到 `65535`。

**Compare value**
:   输入一个常量值，用于与运行中的定时器值进行比较以生成中断。输入 `0` 到 `65535` 之间的值。该值默认为 `5000`。仅当启用 **Post interrupt on compare match** 时，定时器才会生成中断。

**Counting mode**
:   选择 `Up` 生成非对称波形输出，或选择 `Up-down` 生成对称波形输出，如下图所示。

    当将 **Counting mode** 指定为 `Up`（非对称）时，波形：

    - 以低电平开始
    - 当递增的周期计数值与 **Compare value** 匹配时变为高电平
    - 在周期结束时变为低电平

    当将 **Counting mode** 指定为 `Up-down`（对称）时，波形：

    - 以低电平开始
    - 当递增的周期计数值与 **Compare value** 匹配时变为高电平
    - 当递减的周期计数值与 **Compare value** 匹配时变为低电平

    当 **Clock source** 设置为 `QEP circuit` 时，**Counting mode** 变为不可用。

**Timer prescaler**
:   对时钟输入进行分频，以产生所需的定时器计数速率。

    当 **Clock source** 设置为 `QEP circuit` 时，**Timer prescaler** 变为不可用。

**Post interrupt on period match**
:   当定时器的值达到 **Timer period** 中指定的最大值时生成中断。

**Post interrupt on underflow**
:   当定时器的值循环回 `0` 时生成中断。

**Post interrupt on overflow**
:   当定时器的值达到其最大值 `65535` 时生成中断。要使此参数生效，还需将 **Timer period** 设置为 `65535`。

**Post interrupt on compare match**
:   当定时器的值等于 **Compare value** 时生成中断。

**Module**, **Timer no**
:   选择要配置的四个可能定时器中的哪一个。将 **Module** 设置为 `A` 允许你在 **Timer no** 中选择 `Timer 1` 或 `Timer 2`。将 **Module** 设置为 `B` 允许你在 **Timer no** 中选择 `Timer 3` 或 `Timer 4`。

**Clock source**
:   当 **Timer no** 的值为 `Timer 2` 或 `Timer 4` 时，使用此参数选择事件定时器的时钟源。你可以选择 `Internal` 或 `QEP circuit`。选择 `Internal` 时，你可以配置其他选项，如 **Timer period source**、**Counting mode** 和 **Timer prescaler**。

**Timer period source**
:   选择事件定时器周期的来源。使用 `Specify via dialog` 通过 **Timer period** 设置周期。选择 `Input port` 可创建输入 **T**，它接受以时钟周期为单位的定时器周期值，范围为 `0` 到 `65535`。当 **Clock source** 设置为 `QEP circuit` 时，**Timer period source** 变为不可用。

**Timer period**
:   以时钟周期为单位设置定时器周期的长度。输入 `0` 到 `65535` 之间的值。该值默认为 `10000`。

    如果你知道一个时钟周期的长度，就可以轻松计算要为定时器周期设置多少个时钟周期。以下计算确定一个时钟周期的长度：

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    在此计算中，将 150 MHz 的系统时钟频率除以高速时钟预分频器 2。然后，将所得值除以定时器控制输入时钟预分频器 128。所得频率为 0.586 MHz。因此，一个时钟周期为 1/.586 MHz，即 1.706 µs。

**Compare value source**
:   选择比较值的来源。使用 `Specify via dialog` 通过 **Compare value** 参数设置周期。选择 `Input port` 可创建模块输入 **W**，它接受比较值的值，范围为 `0` 到 `65535`。

**Compare value**
:   输入一个常量值，用于与运行中的定时器值进行比较以生成中断。输入 `0` 到 `65535` 之间的值。该值默认为 `5000`。仅当启用 **Post interrupt on compare match** 时，定时器才会生成中断。

**Counting mode**
:   选择 `Up` 生成非对称波形输出，或选择 `Up-down` 生成对称波形输出，如下图所示。

    当将 **Counting mode** 指定为 `Up`（非对称）时，波形：

    - 以低电平开始
    - 当递增的周期计数值与 **Compare value** 匹配时变为高电平
    - 在周期结束时变为低电平

    当将 **Counting mode** 指定为 `Up-down`（对称）时，波形：

    - 以低电平开始
    - 当递增的周期计数值与 **Compare value** 匹配时变为高电平
    - 当递减的周期计数值与 **Compare value** 匹配时变为低电平

    当 **Clock source** 设置为 `QEP circuit` 时，**Counting mode** 变为不可用。

**Timer prescaler**
:   对时钟输入进行分频，以产生所需的定时器计数速率。

    当 **Clock source** 设置为 `QEP circuit` 时，**Timer prescaler** 变为不可用。

**Post interrupt on period match**
:   当定时器的值达到 **Timer period** 中指定的最大值时生成中断。

**Post interrupt on underflow**
:   当定时器的值循环回 `0` 时生成中断。

**Post interrupt on overflow**
:   当定时器的值达到其最大值 `65535` 时生成中断。要使此参数生效，还需将 **Timer period** 设置为 `65535`。

**Post interrupt on compare match**
:   当定时器的值等于 **Compare value** 时生成中断。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

未在 R2025b 中记录。

## 描述

在 Event Manager 模块中配置通用定时器

# C281x Timer

在 Event Manager 模块中配置通用定时器

C281x 包含两个事件管理器（EV）模块。每个模块包含两个通用（GP）定时器。你可以将这些定时器用作各种应用的独立时基。

使用 C281x Timer 模块设置一个 GP 定时器的周期性以及它发出中断的条件。每个模型最多可包含四个 C281x Timer 模块。

C281x Timer 模块配置其他 C281 模块共享的 GP 定时器。有关共享定时器的更多信息和指导，请参阅 Sharing General Purpose Timers Between C281x Peripherals。

- C281x Timer 模块
