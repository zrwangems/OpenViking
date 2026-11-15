---
type: simulink-block
title: 'FPGA Data Reader'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'HDL Verifier Supported Hardware / Intel FPGA Boards / FPGA Data Capture'
documentation_page: 'fpgadatareader'
documentation_source_path: 'ref/fpgadatareader.html'
language: zh-CN
chinese_source: worker-translation
---

# FPGA Data Reader

## 端口

### 输出

### **Capture\_Window** — 当前捕获窗口标量

此输出端口指示当前捕获窗口。此输出端口的值是介于 1 到 **采样深度** 参数值之间的整数。

### **Trigger\_Position** — 捕获缓冲区中触发检测时钟周期的位置 Boolean 标量

此输出端口指示捕获缓冲区中触发检测时钟周期的位置。

## 参数

#### 主要

### **采样时间** — 输出信号的速率 `double`

模块在每个时间步返回一帧数据，其中该帧是每个信号的整个捕获缓冲区。每帧包含 **采样深度** 个值，如生成时所指定。默认采样时间会将每一帧解缓冲为单个样本，从而使采样时间为 1。

#### 触发

### **采样深度** — 为每个信号捕获的样本数 integer

此参数为只读。它反映您在生成时指定的值。

### **存储类型** — 用于存储捕获数据的存储器类型 `Internal memory` | `External memory`

此参数为只读。它反映您在生成时指定的值。

### **捕获窗口数** — 数据捕获重复次数 `1` (默认) | integer power of two

指定要捕获的重复次数。此值必须是 2 的幂，且最大为 **采样深度**。*窗口深度* 定义为 **采样深度** / **捕获窗口数**。在设置 **采样深度** 时考虑 **捕获窗口数**，以便提供足够的缓冲。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **存储类型** 设置为 `Internal memory`。

### **触发阶段数** — 用于提供触发条件的触发阶段数 *M* (默认) | integer from 1 to *M*

指定触发阶段数。此值必须是 integer from 1 to *M*，其中 *M* 由 FPGA Data Capture Component Generator 工具的 **最大触发阶段数** 参数设置。当您指定 **最大触发阶段数** 参数时，请考虑您计划在其中配置触发条件以捕获数据的最大触发阶段数。

### **触发位置** — 触发检测周期在捕获缓冲区中的位置 `0` (默认) | integer up to *window depth*–1

默认情况下，检测到触发时的时钟周期是捕获缓冲区的第一个样本。您可以更改触发检测周期在捕获缓冲区中的相对位置。非默认触发位置意味着在触发发生之前会捕获一些样本。您可以将此参数设置为 0 到 *窗口深度*–1（含）之间的任意数字。当触发位置等于 *窗口深度*–1 时，最后一个样本对应于触发发生的周期。如果 **捕获窗口数** 大于一，则相同的触发位置适用于所有窗口。请参阅触发器。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **存储类型** 设置为 `Internal memory`。

### **信号** — 触发组件信号名称 character vector

此参数为只读。您在生成时指定的信号名称列在底部的下拉菜单中。单击 **+** 按钮将信号添加到触发条件。

### **运算符** — 用于在触发条件内比较信号的运算符 `==` | `!=` | `<` | `>` | `<=` | `>=`

要比较信号，请选择以下运算符之一：`==`、`!=`、`<`、`>`、`<=` 或 `>=`。要比较包含 `X` 或 `x`（无关值）的信号，请指定 `==` 或 `!=` 运算符。

### **值** — 作为整体触发条件的一部分用于与信号比较的值 decimal | binary | hexadecimal | `Low` | `High` | `Rising edge` | `Falling edge` | `Both edges`

触发条件可以由一个或多个信号的值比较组成。此参数指定每个信号要匹配的值。

对于多比特信号，请指定该信号关联数据类型范围内的十进制、二进制或十六进制值。提供十六进制或二进制值时，可以提供包含 `X` 或 `x`（无关值）组合的值以启用位掩码。比较值时，触发条件会丢弃带有 `X` 或 `x` 的位值并给出输出。

为了更便于阅读而分隔一组比特，您可以在位之间使用 `_`。例如，您可以将 32 位二进制值表示为 `0b1010_XXXX_1011_XXXX_1110_XXXX_1111XXXX`，将 32 位十六进制值表示为 `0xAB_CDEXFX`。

对于 `boolean` 信号，请选择电平或边沿条件。请参阅触发器。

### **触发组合运算符** — 用于将各个信号的比较组合成整体触发条件的逻辑运算符 `AND` (默认) | `OR`

此参数由逻辑门图标指示。单击 **更改运算符** 按钮可在 `AND` 和 `OR` 之间切换。

表示 AND 逻辑门运算符的图标

触发条件可以由一个或多个信号的值比较组成。请仅使用一种类型的逻辑运算符组合这些值比较。假设三个信号 `A`、`B` 和 `C` 构成触发条件。选项为：

```
A == 10 AND B == 'Falling edge' AND C == 0
```

或

```
A == 10 OR B == 'Falling edge' OR C == 0
```

您不能混用组合运算符。请参阅触发器。

### **触发超时** — 触发条件必须在触发阶段中发生的数据捕获 IP 核时钟周期最大数 `1` (默认) | integer from 1 to 65,536

在此数据捕获 IP 核时钟周期数内，触发条件必须在您启用此参数的触发阶段中发生。您可以根据需求指定任何 integer value from 1 to 65,536。选择此参数以在触发阶段中启用触发超时。**触发阶段 1** 中不允许触发超时。

### **超时** — 如果未满足触发条件，在中止数据捕获之前等待的秒数 `10` (默认) | positive integer

如果启用了触发条件，但 HDL IP 核未检测到该条件，则数据捕获请求会在此秒数后超时。不会向 Simulink 返回任何数据。

#### 捕获条件

### **启用捕获条件逻辑** — 启用捕获条件逻辑的选项 `off` (默认) | `on`

选择此参数以在数据捕获 IP 核中启用捕获条件逻辑。启用捕获条件逻辑以使用捕获条件控制要从 FPGA 捕获哪些数据。数据捕获 IP 核在每个时钟周期评估捕获条件，并仅捕获满足捕获条件的数据。有关捕获条件的详细信息，请参阅捕获条件。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中选择 **包括捕获条件逻辑**。

### **信号** — 捕获组件信号名称 character vector

此参数为只读。您在生成时指定为触发器的信号名称列在底部的下拉菜单中。单击 **+** 按钮将信号添加到捕获条件。

#### 依赖关系

要启用此参数，请选择 **启用捕获条件逻辑**。

### **运算符** — 用于在捕获条件内比较信号的运算符 `==` | `!=` | `<` | `>` | `<=` | `>=`

要比较信号，请选择以下运算符之一：`==`、`!=`、`<`、`>`、`<=` 或 `>=`。要比较包含 `X` 或 `x`（无关值）的信号，请指定 `==` 或 `!=` 运算符。

#### 依赖关系

要启用此参数，请选择 **启用捕获条件逻辑**。

### **值** — 作为整体捕获条件的一部分用于与信号比较的值 decimal | binary | hexadecimal | `Low` | `High` | `Rising edge` | `Falling edge` | `Both edges`

捕获条件可以由一个或多个信号的值比较组成。此参数指定每个信号要匹配的值。

对于多比特信号，请指定该信号关联数据类型范围内的十进制、二进制或十六进制值。提供十六进制或二进制值时，可以提供包含 `X` 或 `x`（无关值）组合的值以启用位掩码。比较值时，捕获条件会丢弃带有 `X` 或 `x` 的位值并给出输出。

为了更便于阅读而分隔一组比特，您可以在位之间使用 `_`。例如，您可以将 32 位二进制值表示为 `0b1010_XXXX_1011_XXXX_1110_XXXX_1111XXXX`，将 32 位十六进制值表示为 `0xAB_CDEXFX`。

对于 `boolean` 信号，请选择电平或边沿条件。请参阅捕获条件。

#### 依赖关系

要启用此参数，请选择 **启用捕获条件逻辑**。

### **捕获条件组合运算符** — 用于将各个信号的比较组合成整体捕获条件的逻辑运算符 `AND` (默认) | `OR`

此参数由逻辑门图标指示。单击 **更改运算符** 按钮可在 `AND` 和 `OR` 之间切换。

表示 AND 逻辑门运算符的图标

捕获条件可以由一个或多个信号的值比较组成。请仅使用一种类型的逻辑运算符组合这些值比较。您不能混用组合运算符。请参阅捕获条件。

#### 依赖关系

要启用此参数，请选择 **启用捕获条件逻辑**。

#### 数据类型

### **信号名称** — 输出端口的名称 character vector

此参数为只读。它反映 **Capture\_Window** 输出端口的名称、**Trigger\_Position** 输出端口的名称，以及您在生成时指定的信号名称。

### **位宽** — 信号中的位数 positive integer

此参数为只读。它反映您在生成时指定的值。

### **数据类型** — 捕获数据的数据类型 built-in type | `numerictype`

**数据类型** 菜单提供与捕获信号位宽匹配的数据类型建议。此大小是您在生成的 IP 上为端口指定的宽度。您可以在此字段中键入以指定自定义数据类型。如果信号为 8、16 或 32 位，则默认值为 `uint`。如果信号为一位，则默认值为 `boolean`。如果信号为其他宽度，则默认值为 `numerictype(0,bitWidth,0)`。

该模块支持以下数据类型，具体取决于信号位宽：`boolean`、`uint8`、`int8`、`uint16`、`int16`、`half`、`uint32`、`int32`、`single`、`uint64`、`int64`、`double` 和 `numerictype`。

如果您的开发板有多个 FPGA 或多个 JTAG 连接，则数据捕获软件无法检测您的 FPGA 在 JTAG 链中的位置。请指定这些高级参数以定位包含数据捕获 IP 核的 FPGA。

#### 高级

### **JTAG 电缆名称** — 用于数据捕获的 JTAG 电缆名称 `auto` (默认) | character vector

用于数据捕获的 JTAG 电缆名称，指定为 character vector。当开发板连接到两根相同类型的 JTAG 电缆时，请使用此参数。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **连接类型** 参数设置为 `JTAG`。

### **JTAG 电缆类型** — 用于与 FPGA 板通信的 JTAG 电缆类型（仅 AMD®） `auto` (默认) | `FTDI`

如果主机连接了多根 JTAG 电缆，请指定此参数。未指定时，FPGA Data Reader 模块将按以下顺序自动检测 JTAG 电缆类型：

- FPGA Data Reader 模块首先搜索 Digilent® 电缆。
- 如果未找到 Digilent JTAG 电缆，则搜索 FTDI 电缆。
- 如果找到两根相同类型的电缆，则该对象返回错误。设置此参数以解决该问题。
- 如果找到两根不同类型的电缆，则优先使用 Digilent 电缆。要使用 FTDI 电缆，请将此参数设置为 `FTDI`。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `JTAG`。

### **JTAG 链位置** — FPGA 在 JTAG 扫描链中的位置（仅 AMD） `0` (默认) | positive integer

FPGA 在 JTAG 扫描链中的位置，指定为 positive integer。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `JTAG`。

### **FPGA 之前的指令寄存器** — FPGA 之前的指令寄存器长度（仅 AMD） `0` (默认) | nonnegative integer

FPGA 之前的指令寄存器长度数，指定为 nonnegative integer。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `JTAG`。

### **FPGA 之后的指令寄存器** — FPGA 之后的指令寄存器长度（仅 AMD） `0` (默认) | nonnegative integer

FPGA 之后的指令寄存器长度数，指定为 nonnegative integer。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `JTAG`。

### **JTAG 时钟频率 (MHz)** — JTAG 时钟频率（仅 AMD） `15` (默认) | integer

指定 JTAG 时钟频率，以 MHz 为单位。对于 AMD FPGA，JTAG 时钟频率为 33 或 66 MHz。JTAG 频率取决于电缆类型以及 FPGA 板支持的最大时钟频率。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `JTAG`。

### **外部 DDR 存储器基地址** — 外部 DDR 存储器的基地址（仅 AMD） `8000000` (默认) | numeric value

将外部 DDR 存储器的基地址指定为 numeric value。使用此值指示您希望将捕获的数据存储在 DDR 存储器中的位置。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，将 **连接类型** 设置为 `JTAG`，并将 **存储类型** 设置为 `External memory`。

### **设备 IP 地址** — FPGA 或 SoC 板上以太网端口或 USB 以太网小工具的 IP 地址（仅 AMD） dotted-quad value

将 FPGA 或 SoC 板上以太网端口或 USB 以太网小工具的互联网协议 (IP) 地址指定为 dotted-quad value。设备 IP 地址必须是由 0 到 255 范围内整数组成的四个数字，并用三个点分隔。PL Ethernet 或 PS Ethernet 接口的默认 IP 地址为 `192.168.0.2`。USB Ethernet 接口的默认 IP 地址为 `192.168.1.2`。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `PL Ethernet`、`PS Ethernet` 或 `USB Ethernet`。

### **设备端口地址** — FPGA 板的 UDP 端口号（仅 AMD） `50101` (默认) | integer from 255 to 65,535

将 FPGA 板的用户数据报协议 (UDP) 端口号指定为 integer from 255 to 65,535。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `PL Ethernet`。

### **数据捕获 IP 核基地址** — 数据捕获 HDL IP 核的基地址（仅 AMD） `40000000` (默认) | numeric value

将数据捕获 HDL IP 核的基地址指定为 numeric value。

#### 依赖关系

要启用此参数，请在 FPGA Data Capture Component Generator 工具中将 **FPGA 供应商** 设置为 `AMD`，并将 **连接类型** 设置为 `PS Ethernet` 或 `USB Ethernet`。

## 所属库

生成的

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将实时 FPGA 中的数据捕获到 Simulink 模型中

FPGA Data Reader 模块与 FPGA 上生成的 IP core 通信，以将捕获的数据返回到 Simulink® 中。

数据捕获工作流包含三个关键步骤：生成数据捕获 IP、将其与现有 FPGA 设计集成，以及捕获数据。在数据捕获步骤中使用此模块将捕获的数据传输到 Simulink 中。

在运行此模块之前，您必须生成定制的数据捕获组件。将生成的 HDL IP core 集成到您的项目中，并将其部署到 FPGA。此模块通过 JTAG、Ethernet 或 USB Ethernet 电缆与 FPGA 通信。确保所需电缆连接在板卡和主机计算机之间。

有关工作流概述，请参阅 Data Capture Workflow。

默认情况下，FPGA Data Capture Component Generator 工具会生成一个数据捕获模型，其中包含此模块和一个 Scope 模块。捕获的数据会流式传输到 Logic Analyzer 工具。Scope 模块还会显示捕获的数据。您可以向该模型添加其他模块，以进行分析、验证和显示。

生成的数据捕获模型
