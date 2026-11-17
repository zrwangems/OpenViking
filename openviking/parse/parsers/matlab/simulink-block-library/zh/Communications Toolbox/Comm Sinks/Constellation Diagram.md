---
type: simulink-block
title: 'Constellation Diagram'
family: 'comm-sinks'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'constellationdiagram'
documentation_source_path: 'ref/constellationdiagram.html'
language: zh-CN
chinese_source: worker-translation
---

# Constellation Diagram

## 端口

### 输入

### **In\_1, ..., In\_N** — 信号（作为单独端口）列向量 | 矩阵

信号，指定为 *N*sym-by-1 列向量或 *N*sym-by-*N*channel 矩阵的单独参数。*N*sym 是符号数量，*N*channel 是输入信号通道数量。信号可以具有不同的数据类型和维度。

必须指定 *N* 个输入端口，其中 *N* 是 **输入端口数量** 参数值。在星座图中最多可以可视化 20 个单独或集体信号通道。例如，如果为每个输入创建双通道信号，则最多可以定义 10 个输入端口。

**示例：** `[-1 + 1i; -1 - 1i; 1 + 1i; 1 - 1i]` 指定一个四符号输入信号。

**数据类型：** `double`
**复数支持：** Yes

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 上，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### 绘图

在 **Plot** 选项卡中，可以调整星座图配置的设置、仿真模型、拍摄绘图快照、复制显示内容以及打印图窗。此处描述了星座图示波器特有的参数。

### **设置** — 星座图设置按钮

在 **Plot** 选项卡中，点击 **Settings** 打开 Configuration Plot Settings 窗口。此窗口包含参数子部分，用于配置数据和坐标轴、标签以及颜色和样式。此页面描述了星座图特有的参数。

### **输入端口数量** — 示波器模块上的输入端口数量 `1` (default) | [1, 20] 范围内的整数

将示波器模块上的输入端口数量指定为 [1, 20] 范围内的整数。

输入信号通道总数不能超过 20。指定多通道输入信号时，输入信号通道总数限制输入端口数量的最大值。

### **每符号采样数** — 用于表示每个符号的采样数 `1` (default) | 正整数

将用于表示每个符号的采样数指定为正整数。绘制信号之前，按此参数的值对信号进行下采样。

### **偏移量** — 绘制点之前跳过的采样数 `0` (default) | 非负整数

将绘制点之前跳过的采样数指定为小于 **每符号采样数** 参数值的非负整数。当 **每符号采样数** 大于 1 时，此值指定要跳过的采样数。

### **要显示的符号数** — 要显示的最大符号数 `Input frame length` (default) | 正整数

通过选择 `Input frame length` 或指定正整数来指定要显示的最大符号数。要指定正整数，请选择并然后将 `<user-defined>` 替换为所需值。当输入长信号时，使用此参数限制星座图显示的最大符号数。该模块绘制最近接收到的符号。

### **AxesLimits** — *x* 和 *y* 轴限制 `[-1.375 1.375]` (default) | 二元素行向量

将 *x* 和 *y* 轴限制指定为二元素行向量。第一个元素是最小轴值，第二个元素是最大轴值。

- 如果示波器窗口为正方形，则 X 和 Y 轴将具有与 `AxesLimits` 相同的限制。
- 如果示波器窗口为矩形，则较小的轴将具有与 `AxesLimits` 相同的限制。较大的轴自动填充以保持 1:1 纵横比。

**可调：** Yes

**数据类型：** `double`

### **参考星座** — 参考星座配置按钮

在 **Plot** 选项卡或 **Measurements** 选项卡中，点击 **Reference Constellation**，打开 Reference Constellation 窗口。此窗口包含用于为每个输入端口配置参考星座的参数。

### **显示参考星座** — 显示参考星座的选项 `on` (default) | `off`

选择此参数以在绘图上显示参考星座。

### **输入** — 选择输入端口 1 (default) | 正整数

为指定的输入端口配置参考星座参数。

每个输入端口都有自己的参考星座。对于多通道输入信号，该模块对该输入端口中的所有信号应用单一参考星座。

### **参考星座** — 参考星座 `Custom` (default) | `BPSK` | `8-PSK` | `16-QAM` | `64-QAM` | `256-QAM`

通过选择 `Custom`、`BPSK`、`QPSK`、`8-PSK`、`16-QAM`、`64-QAM` 或 `256-QAM` 来指定参考星座。要指定自定义值，请先选择 `Custom`。然后在 **自定义值** 参数中，将该条目替换为自定义符号值向量。

每个输入端口都有自己的参考星座。对于多通道输入信号，该模块对该输入端口中的所有信号应用单一参考星座。

EVM/MER 测量使用指定的参考星座来计算调制输入信号的质量。有关信号质量测量的详细信息，请参阅 EVM 和 MER 测量。

### **自定义值** — 输入参考星座 `[0.7071+0.7071i -0.7071+0.7071i -0.7071-0.7071i 0.7070-0.7071i]` (default) | 向量

将输入的参考星座指定为定义自定义调制方案符号值的向量。

#### 依赖项

要启用此参数，请将 **参考星座** 参数设置为 `Custom Reference Constellation`。

### **星座归一化** — 归一化方法 `Average power` (default) | `Minimum distance` | `Peak power`

通过选择 `Average power`、`Minimum distance` 或 `Peak power`，指定该模块用于星座图的归一化方法。

#### 依赖项

要启用此参数，请将 **参考星座** 参数设置为 `16-QAM`、`64-QAM` 或 `256-QAM`。

### **平均参考功率** — 参考星座的平均功率 `1` (default) | 正标量

将参考星座的平均功率指定为正标量。平均功率以 one-ohm 负载为参考。单位为 watts。

#### 依赖项

要启用此参数，请将 **参考星座** 参数设置为 `BPSK`、`QPSK`、`8-PSK`、`16-QAM`、`64-QAM` 或 `256-QAM`。

### **参考相位偏移 (rad)** — 参考星座的相位偏移 标量

将参考星座的相位偏移指定为标量。单位为 radians。

#### 依赖项

要启用此参数，请将 **参考星座** 参数设置为 `BPSK`、`QPSK`、`8-PSK`、`16-QAM`、`64-QAM` 或 `256-QAM`。

- 对于 `BPSK`、`16-QAM`、`64-QAM` 和 `256-QAM`，默认值为 `0`。
- 对于 `8-PSK`，默认值为 `pi/4`。
- 对于 `QPSK`，默认值为 `pi/8`。

### **图例** — 显示图例的选项按钮

在 **Plot** 选项卡中，点击 **Legend** 以切换图例的显示。图例中列出的名称是模型中指定的连接到输入端口的信号名称。在模型使用输入信号运行之前，图例不会显示。

在示波器图例中，点击信号名称以切换该信号在示波器中的可见性。

### **轨迹** — 显示信号轨迹的选项按钮

在 **Plot** 选项卡中，点击 **Trajectory** 以切换轨迹的显示。选择此参数以显示所绘信号的星座点之间的轨迹。

### 测量

在 **Measurements** 选项卡中，可以选择活动通道、配置信号质量测量，并切换 **Measurements** 窗格。

有关信号质量测量的详细信息，请参阅 EVM 和 MER 测量。

#### 通道

### **通道** — 第一个端口中第一个通道的活动输入通道名称 (default) | 通道列表

从输入通道列表中选择用于测量的活动输入通道。点击 **EVM/MER** 以显示活动通道的信号质量测量。

输入信号通道总数不能超过 20。指定多通道输入信号时，输入信号通道总数限制 **输入端口数量** 参数的最大允许值。

#### 测量

### **测量间隔** — EVM 和 MER 测量的持续时间 `Current display` (default) | `All displays` | 正整数

通过选择 `Current Display` 或 `All displays`，或指定正整数，来指定 EVM 和 MER 测量的持续时间（以符号为单位）。要指定正整数，请选择并然后将 `<user-defined>` 替换为所需值。该值必须是范围 [1, **要显示的符号数**) 内的正值。当输入数据采样数超过测量间隔后，该模块计算测量值。

### **EVM 归一化** — 归一化方法 `Average constellation power` (default) | `Peak constellation power`

通过选择 `Average constellation power` 或 `Peak constellation power`，指定该模块用于 EVM 归一化的归一化方法。

### **参考星座** — 参考星座配置按钮

在 **Plot** 选项卡或 **Measurements** 选项卡中，点击 **Reference Constellation**，打开 Reference Constellation 窗口。此窗口包含用于为每个输入端口配置参考星座的参数。有关参数描述，请参阅 Plot 部分中的 **Reference Constellation** 参数。

### **EVM/MER** — 显示信号质量测量窗格的选项按钮

在 **Measurements** 选项卡中，点击 **EVM/MER** 以切换信号质量测量窗格的显示。有关详细信息，请参阅 EVM 和 MER 测量。

## 所属库

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当对包含此模块的系统执行代码生成时，此模块会从生成的代码中排除。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2013b 中引入**

### R2025a：单一坐标轴限制替代星座图模块中单独的 x 和 y 轴限制

Constellation Diagram 模块现在包含统一的坐标轴限制，替代单独的 x 和 y 轴限制。此更改确保系统将指定的限制应用到至少一个坐标轴，从而简化画布大小管理。当调整窗口大小或缩放窗口时，示波器会自动调整限制以保持 1:1 纵横比。

## 描述

在 IQ 平面中显示和分析输入信号

Constellation Diagram 模块在 IQ 平面中显示实值和复值浮点及定点信号。使用此模块对调制的单载波信号执行定性和定量分析。具体而言，IQ 平面在 xy-plot 的实轴和虚轴上显示调制信号的同相和正交分量。

显示 QPSK、16-QAM 和 8-DPSK 信号以及信号质量测量的星座图。

在 Constellation Diagram 窗口中，可以：

- 在单个星座图上输入并绘制多个信号。要为每个输入信号定义参考星座，请使用 **Reference Constellation** 参数。
- 在图例中选择信号以切换各个通道的可见性。要显示图例，请使用 **Plot** 选项卡上的 **Legend** 参数。对于多通道信号，将输入指定为矩阵，其中各个信号定义在矩阵的列中。
- 显示各个信号的计算出的误差向量幅度 (EVM) 和调制误差比 (MER) 测量值。要查看和配置测量，请在 **Measurements** 选项卡上选择 **EVM/MER**。当输入多个信号时，可以在 **Channel** 部分选择要用于测量的信号。
