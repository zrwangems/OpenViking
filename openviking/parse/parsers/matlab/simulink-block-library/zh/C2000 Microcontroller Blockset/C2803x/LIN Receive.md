---
type: simulink-block
title: 'C2803x LIN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c2803xlinreceive'
documentation_source_path: 'ref/c2803xlinreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# C2803x LIN Receive

## 端口

R2025b 中未记录。

## 参数

**数据类型**
:   选择 LIN 模块输出到模型的数据类型。可用选项为
    `single`、`int8`、
    `uint8`、`int16`、
    `uint16`、`int32` 或
    `uint32`。要解释数据，数据类型和数据
    长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 `int16`。

**Data length**
:   设置 LIN 模块输出到模型的数据长度。此值
    以 **数据类型** 的倍数计量。例如，如果
    **数据类型** 为 `int16` 且
    **Data length** 为 `int16`，则 LIN 模块
    以如下长度向模型输出数据

    1 x int16

    如果将 **Data length** 设置为大于 1 的值，
    则模块将数据作为向量输出。

    要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据
    输入相匹配。

    默认值为 1。

    **注意**

    在环回配置中，最大数据长度不能超过 8 字节。如果
    传入和传出数据的总和超过 LIN 模块的硬件缓冲区长度，
    则模块会丢弃传入的数据字节。

**Initial output**
:   设置 LIN 节点接收到数据之前 DATA 端口输出到模型的初始值。

    默认值为 `0`。

**Action taken when connection times out**
:   指定 LIN 模块在连接超时时在 DATA 端口上输出的内容。选项包括：

    - `Output the last received value` — DATA
      端口输出 LIN 节点接收到的最后一个数据值。
    - `Output custom value` — DATA 端口输出
      由 **Output value when connection times
      out** 定义的值。

    默认值为 `Output the last received
    value`。

    如果 LIN 节点尚未接收到数据，并且将此参数设置为
    `Output the last received value`，则 DATA 端口输出
    **Initial output** 值。

**连接超时时的输出值**
:   指定当 **Action taken when
    connection times out** 设置为 `Output custom
    value` 且发生连接超时时，DATA 端口输出的自定义值。

**Enable blocking mode**
:   如果启用（选中）此复选框，目标应用程序会停止并等待
    LIN 节点接收数据后再继续。如果禁用此选项，
    应用程序将继续运行，不等待数据到达。

    默认值为禁用（未选中）。

**Verify checksum**
:   如果启用（选中）此选项，LIN 节点会验证其
    接收到的校验和。

    默认值为禁用（未选中）。

**Output receiving status**
:   启用（选中）此复选框会向
    LIN Receive 模块添加一个 `status` 输出，如下图所示。

    `status` 输出针对 LIN 节点接收到的每条消息
    报告以下值：

    - `0`：无错误。
    - `-1`：模块等待接收数据时发生超时。
    - `-2`：无法接收。
    - 其他状态值表示 SCI Flags Register 的高 8 位。
      将这些值从十进制转换为二进制。然后参考
      *TMS320F2803x Piccolo Local Interconnect Network (LIN)
      Module*（文献编号 SPRUGE2，可在 Texas Instruments® 网站上获取）
      中的 Table 14. SCI Flags Register (SCIFLR) Field Descriptions
      来确定这些值的含义。

**Receive buffer interrupt**
:   如果启用此选项，SCI 节点在接收到
    完整帧后生成中断。默认值为 `Disabled`。

**Checksum error interrupt**
:   如果启用此选项，LIN 模块在传入
    消息包含无效校验和时生成中断。

    默认值为 `Disabled`。

    TXRX Error Detector Checksum Calculator 会验证传入
    消息的校验和。在经典 LIN 实现中，校验和仅覆盖数据
    字段。对于符合 LIN 2.0 的消息，校验和包括 ID 字段和
    数据字段。如果启用此选项，Checksum Calculator 在检测到校验和
    错误时生成中断，例如由 LIN 消息
    冲突引起的错误。

**Framing error interrupt**
:   如果启用此选项，LIN 模块在发生帧错误时
    生成中断。

    默认值为 `Disabled`。

**Overrun error interrupt**
:   如果启用此选项，LIN 模块在发生过载错误时
    生成中断。

    默认值为 `Disabled`。

**ID parity error interrupt**
:   如果启用此选项，LIN 模块在接收到
    无效 ID 时生成 ID-Parity 中断。

    默认值为 `Disabled`。

    如果启用此选项，还需在
    Hardware Implementation -> Target Hardware Resources 中启用 **Parity mode**。

**ID match interrupt**
:   如果启用此选项，LIN 模块在 LIN 节点
    验证其接收消息中的 ID 时生成中断。

    默认值为 `Disabled`。

**Sample time**
:   设置模块的输入采样时间，
    `Ts`。

    默认值为 `0.1` 秒。

**数据类型**
:   选择 LIN 模块输出到模型的数据类型。可用选项为
    `single`、`int8`、
    `uint8`、`int16`、
    `uint16`、`int32` 或
    `uint32`。要解释数据，数据类型和数据
    长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 `int16`。

**Data length**
:   设置 LIN 模块输出到模型的数据长度。此值
    以 **数据类型** 的倍数计量。例如，如果
    **数据类型** 为 `int16` 且
    **Data length** 为 `int16`，则 LIN 模块
    以如下长度向模型输出数据

    1 x int16

    如果将 **Data length** 设置为大于 1 的值，
    则模块将数据作为向量输出。

    要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据
    输入相匹配。

    默认值为 1。

    **注意**

    在环回配置中，最大数据长度不能超过 8 字节。如果
    传入和传出数据的总和超过 LIN 模块的硬件缓冲区长度，
    则模块会丢弃传入的数据字节。

**Initial output**
:   设置 LIN 节点接收到数据之前 DATA 端口输出到模型的初始值。

    默认值为 `0`。

**Action taken when connection times out**
:   指定 LIN 模块在连接超时时在 DATA 端口上输出的内容。选项包括：

    - `Output the last received value` — DATA
      端口输出 LIN 节点接收到的最后一个数据值。
    - `Output custom value` — DATA 端口输出
      由 **Output value when connection times
      out** 定义的值。

    默认值为 `Output the last received
    value`。

    如果 LIN 节点尚未接收到数据，并且将此参数设置为
    `Output the last received value`，则 DATA 端口输出
    **Initial output** 值。

**连接超时时的输出值**
:   指定当 **Action taken when
    connection times out** 设置为 `Output custom
    value` 且发生连接超时时，DATA 端口输出的自定义值。

**Enable blocking mode**
:   如果启用（选中）此复选框，目标应用程序会停止并等待
    LIN 节点接收数据后再继续。如果禁用此选项，
    应用程序将继续运行，不等待数据到达。

    默认值为禁用（未选中）。

**Verify checksum**
:   如果启用（选中）此选项，LIN 节点会验证其
    接收到的校验和。

    默认值为禁用（未选中）。

**Output receiving status**
:   启用（选中）此复选框会向
    LIN Receive 模块添加一个 `status` 输出，如下图所示。

    `status` 输出针对 LIN 节点接收到的每条消息
    报告以下值：

    - `0`：无错误。
    - `-1`：模块等待接收数据时发生超时。
    - `-2`：无法接收。
    - 其他状态值表示 SCI Flags Register 的高 8 位。
      将这些值从十进制转换为二进制。然后参考
      *TMS320F2803x Piccolo Local Interconnect Network (LIN)
      Module*（文献编号 SPRUGE2，可在 Texas Instruments® 网站上获取）
      中的 Table 14. SCI Flags Register (SCIFLR) Field Descriptions
      来确定这些值的含义。

**Receive buffer interrupt**
:   如果启用此选项，SCI 节点在接收到
    完整帧后生成中断。默认值为 `Disabled`。

**Checksum error interrupt**
:   如果启用此选项，LIN 模块在传入
    消息包含无效校验和时生成中断。

    默认值为 `Disabled`。

    TXRX Error Detector Checksum Calculator 会验证传入
    消息的校验和。在经典 LIN 实现中，校验和仅覆盖数据
    字段。对于符合 LIN 2.0 的消息，校验和包括 ID 字段和
    数据字段。如果启用此选项，Checksum Calculator 在检测到校验和
    错误时生成中断，例如由 LIN 消息
    冲突引起的错误。

**Framing error interrupt**
:   如果启用此选项，LIN 模块在发生帧错误时
    生成中断。

    默认值为 `Disabled`。

**Overrun error interrupt**
:   如果启用此选项，LIN 模块在发生过载错误时
    生成中断。

    默认值为 `Disabled`。

**ID parity error interrupt**
:   如果启用此选项，LIN 模块在接收到
    无效 ID 时生成 ID-Parity 中断。

    默认值为 `Disabled`。

    如果启用此选项，还需在
    Hardware Implementation -> Target Hardware Resources 中启用 **Parity mode**。

**ID match interrupt**
:   如果启用此选项，LIN 模块在 LIN 节点
    验证其接收消息中的 ID 时生成中断。

    默认值为 `Disabled`。

**Sample time**
:   设置模块的输入采样时间，
    `Ts`。

    默认值为 `0.1` 秒。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过目标上的本地互连网络 (LIN) 模块接收数据

# C2803x LIN Receive

通过目标上的本地互连网络 (LIN) 模块接收数据

本地互连网络 (LIN) 总线为分布式汽车和工业应用实现了一种串行通信协议。特别是，LIN 服务于不需要 CAN 协议所提供的带宽或鲁棒性的低成本应用。

LIN Receive 模块将目标配置为从 LINRX 或 LINTX 引脚接收标量或向量数据。

每个 C2803x 目标有一个 LIN 模块。您的模型每个模块只能包含一个 LIN Transmit 和一个 LIN Receive 模块。

C2803x LIN Transmit 模块有三个输入：

- **ID**：设置 LIN 发送节点的 LIN ID 值。
- **TX ID Mask**：设置 LIN 发送节点的 LIN ID 掩码值。
- **Data**：将此输入连接到数据源。

有关更多信息和示例，请参阅：

- Configuring LIN Communications
- LIN-Based Control of PWM Duty Cycle

**注意**

许多 LIN 特定设置位于模型的 Hardware Implementation -> Target Hardware Resources 中的 **Peripherals** >
**LIN** 下。请验证这些设置是否满足您的应用要求。

- C2803x LIN Receive 模块
