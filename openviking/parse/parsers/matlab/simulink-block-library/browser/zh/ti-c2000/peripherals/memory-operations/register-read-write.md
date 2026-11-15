---
type: simulink-block
title: 'Register Read/Write'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Memory Operations'
documentation_page: 'registerreadwrite'
documentation_source_path: 'ref/registerreadwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Register Read/Write

## 端口

### 输出

### **All** — 选择的位域标量

输出端口取决于在使用指定位访问寄存器时选择的位域数量。在 Register bit fields 参数中，默认选择选项 **All**，它显示为输出端口。如果选择了任何其他位域，输出端口将根据所选位域而变化。

位域 **All** 将访问整个寄存器。

**注意**

在 Register bit field 参数中，您可以选择选项 All 或其他特定位域。

输出端口是动态的，取决于所选择的位域数量。当使用自定义位访问寄存器时，它取决于参数 **Bits to process** 中指定的元胞数组长度。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `Read`。

**数据类型：** `uint16` | `uint32`

### 输入

### **All** — 选择的位域数量标量

输入端口取决于在使用指定位访问寄存器时选择的位域数量。

在 Register bit fields 参数中，默认选择选项 **All**，它显示为输入端口。如果选择了任何其他位域，输入端口将根据所选位域而变化。

位域 **All** 将访问整个寄存器。

**注意**

在 Register bit field 参数中，您可以选择选项 All 或其他特定位域。

输入端口是动态的，取决于所选择的位域数量。当使用自定义位访问寄存器时，它取决于参数 **Bits to process** 中指定的元胞数组长度。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `Write`。

**数据类型：** `uint16` | `uint32`

## 参数

### **Device family** — 选择 TI C2000 器件系列 `None`（默认） | `F2804x` | `F280x` | `F281x` | `F2833x` | `F2844x` | `F280013x` | `F280015x` | `F28002x` | `F28003x` | `F28004x` | `F2802x` | `F2803x` | `F2805x` | `F2806x` | `F2807x` | `F2837xS` | `F2837xD_CPU1` | `F2837xD_CPU2` | `F2838x_CPU1` | `F2838x_CPU2` | `F2838x_CORTEXM4` | `F28M35x` | `F28M35x` | `F28M35x` | `F28p65x_CPU1` | `F28p65x_CPU2`

选择您要访问其寄存器的 TI C2000 器件系列。

### **Register group** — 选择所需寄存器组 Unspecified（默认）

选择 Register Read/Write 模块的寄存器组。

该参数的选项在您执行 C2000 HW setup 后根据所选器件系列填充。此参数将 TI C2000 寄存器分组为各种类别，即 ADC、PWM 等。

选择寄存器组会定义模块的 Register name、Register fields 和 Register bit fields 等参数。例如，如果您将 Register group 选为 ADC，则其对应的 Register name、Register fields 和 Register bit fields 会被填充。

### **Register name** — 选择寄存器名称 `Unspecified`（默认）

选择所选寄存器组的寄存器名称。选项根据所选寄存器组和器件系列填充。例如，如果 Register group 为 ADC，则 Register name 参数将填充 AdcaRegs、AdcbRegs 等选项。

### **Register field** — 选择寄存器字段 `Unspecified`（默认）

选择所选寄存器组的 Register field。选项根据所选器件系列、寄存器组和寄存器字段填充。例如，如果 Register group 为 ADC 且 Register name 为 AdcaRegs，则 Register field 参数将填充 ADCCTL1、ADCCTL2、ADCBURSTCTL 等选项。

### **Access register using** — 选择寄存器访问 `Specified bits`（默认） | `Custom bits`

选择使用指定位或自定义位访问寄存器。

- **Specified bits：** 选择指定位将以表格格式在 Register bit fields 参数中显示所有寄存器位字段。
- **Custom bit fields：** 当您想要手动访问位位置时，选择自定义位字段。

对于指定位，如果您正在使用 Register Read/Write 模块访问 AdcaRegs.ADCCTL1，则参数 Register bit fields 将以表格格式显示选项 **All** 中对应寄存器的所有位，例如 INTPULSEPOS、ADCPWDNZ、ADCBSYCHN 等。

对于自定义位，您需要以元胞数组的形式手动指定要访问的位位置。例如，当 bits to process 参数为 {[2,0],[5,3],[7,4]} 时，表示访问 3 个位范围。它根据 Operation 参数类型生成三个输入端口或输出端口。第一个端口将访问对应寄存器字段 ADCCTL1 的从位置 2 到位置 0 的位。类似地，第二个端口将访问从位置 5 到位置 3 的位，第三个端口将访问从位置 7 到位置 4 的位。

### **Operation** — 选择读或写操作 `Read`（默认） | `Write`

- **读操作** - 当您想要从寄存器读取数据时选择。读操作将在参数 **Register bit fields** 或 **Bits to process** 中选择的位字段生成为输出端口。
- **写操作** - 当您想要将数据写入寄存器时选择。写操作将在参数 **Register bit fields** 或 **Bits to process** 中选择的位字段生成为输入端口。

### **Insert code before/after** — 在之前/之后插入代码 `None`（默认） | `EALLOW/EDIS`

选择 **EALLOW/EDIS** 以访问写保护的 TI 寄存器。

### **Bit to process** — 指定自定义位 `{[15,0]}|`（默认）

Bit to process 参数接受元胞数组，其中每个元素是 `1x2` 数组，其中较小的数字表示起始位，较大的数字表示结束位。例如，当自定义位采用以下格式 **{[1], [2 3], [ 5 10 ], [11 16]}** 时，则：

- 根据提到的自定义位，您正在访问四组不同的位，即

  - 位 1
  - 位 2 和位 3
  - 位 5 到 10
  - 位 11 到 16
- 指定的自定义位将生成四个不同的端口（输入端口或输出端口）

为元胞数组的每个元素生成的相应端口将访问起始位和结束位之间的位范围。

**注意**

位位置应小于所访问寄存器字段的长度。此外，元胞数组的任何 2 个条目之间不应存在位位置重叠。

#### 依赖关系

要启用此参数，请将 **Access register using** 参数设置为 `Custom bits`。

### **Register bit fields** — 选择要访问的位字段 `All`（默认）

选择您想要访问的位字段。寄存器位字段的选项根据寄存器组、寄存器字段和寄存器名称的选择填充。

#### 依赖关系

要启用此参数，请将 **Access register using** 参数设置为 `Specified bits`。

## 所属库

C2000 Microcontroller Blockset / Memory Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从 TI C2000 寄存器的各种位字段读取或写入

您可以使用 C2000 Microcontroller Blockset 中的 Register Read/Write 模块从 TI C2000 寄存器的各种位字段读取数据，并向其写入数据。该模块依赖于硬件设置期间生成的文件，这些文件由所选处理器和 CCS 版本确定。如果模块上的参数为 **Unspecified**，请使用 `c2000setup` 配置硬件设置。

您还可以使用该模块通过自定义位指定位位置。它接受元胞数组，其中每个元素是 `1x2` 数组，用于指定起始位和结束位。

**注意**

- Register Read/Write 模块依赖于 CCS 安装以及 CCS 中存在的寄存器 xmls，以填充模块中的各种条目。某些寄存器可能不在 CCS xmls 中，因此您将无法在模块中访问它们。例如，F2803x 中的 HRCAP。
- 当您尝试修改不同 CPU 核心的外设寄存器时，请确保该 CPU 核心有权访问特定外设，否则寄存器读/写访问可能会失败。
