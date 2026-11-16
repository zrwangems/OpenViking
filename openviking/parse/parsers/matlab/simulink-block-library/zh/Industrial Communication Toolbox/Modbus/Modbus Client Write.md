---
type: simulink-block
title: 'Modbus Client Write'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'Modbus'
documentation_page: 'modbusclientwrite'
documentation_source_path: 'ug/modbusclientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus Client Write

## 端口

### 输入

### **Reg\_*`x`*** — 寄存器值向量 double | array of doubles

要写入 Modbus TCP/IP 或串行服务器上指定寄存器的值。输入端口数 (*x*) 对应于您在 Registers 参数中添加的行数。当您将 N×1 值向量写入某个端口时，模块会从 **Registers** 参数的 `Address` 字段中指定的寄存器地址开始，将这些值写入 N 个连续寄存器。

#### 依赖关系

要启用此端口，请在 **Registers** 参数中指定一个或多个寄存器。

**数据类型：** `double`

## 参数

### **Client** — 选择 Modbus 客户端下拉列表

选择要与模块关联的 Modbus 客户端。选择客户端后，模块将更新 **Connection endpoint** 参数。

- 要使用 **Modbus** 窗格添加客户端，请点击 **Configure clients**。有关详细信息，请参阅在 Simulink 中配置 Modbus 客户端。
- 要更新客户端列表并显示最新的 Modbus 客户端，请点击 **Refresh**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | Modbus 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **Server ID** — 服务器的地址 1（默认）| [0, 255] 范围内的非负整数

要写入的服务器地址，指定为 [0, 255] 范围内的非负整数。默认值为 1。服务器地址指的是 Modbus TCP/IP 服务器的单元标识符。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ServerId` |
| **值：** | 1（默认） | [0, 255] 范围内的非负整数 |
| **数据类型：** | `double` |

### **Registers** — Modbus 寄存器列表表格

添加要写入指定客户端的寄存器。

- 要添加寄存器，请点击 **Add**。此操作会在 **Registers** 表格中添加一行，其中 `Name`、`Register Type` 和 `Precision` 分别设置为默认值 `Reg_1`、`Holding Register` 和 `uint16`。您必须在 `Address` 列中指定要写入的寄存器的地址。每次点击 **Add** 时，模块都会在 **Registers** 表格中添加新行，并将名称递增 1。

  - `Sl`. `no`. ：此字段不可编辑，用于指定寄存器的序列号。序列号决定模块在输入端口输入信号的顺序。
  - `Name`：这是一个可编辑文本字段，用于指定寄存器的名称。此字段还定义输入端口的名称。
  - `Address`：这是一个可编辑文本字段，用于指定 Modbus 写操作的起始地址。
  - `Register Type`：这是一个下拉列表，用于指定要写入的目标区域。您可以对两类目标执行 Modbus 写操作：线圈和保持寄存器。
  - `Precision`：这是一个下拉列表，用于指定写入寄存器的数据格式。请注意，`Precision` 字段并不指模块输入的数据类型。输入的数据类型始终为 `double`。`Precision` 指定模块如何解释寄存器数据。

    - 对于线圈，将此字段设置为 `bit`。
    - 对于保持寄存器，将此字段设置为 `int16`、`uint16`、`int32`、`uint32`、`single`、`double`、`int64` 或 `uint64`。
- 要删除寄存器，请选择这些寄存器并点击 **Delete**。
- 要导入保存为 MAT 文件的寄存器表，请点击 **Import**。此操作会为当前工作区打开“加载寄存器表”对话框。使用此浏览器，您可以选择包含寄存器信息的 MAT 文件。您选择的 MAT 文件必须包含名为 `ModbusRegisterTable` 的表。

  **注意**

  Modbus Explorer 应用会将寄存器表的内容导出为 MAT 文件。您可以将此 MAT 文件导入 Modbus Client Simulink 模块，以重用寄存器表。有关详细信息，请参阅使用 Modbus Explorer 应用。
- 要将寄存器表保存为 MAT 文件，请点击 **Export**。此操作会为当前工作区打开“保存寄存器表”对话框。使用此浏览器，您可以将寄存器表保存为 MAT 文件，并保存到您选择的位置。默认文件名为 `ModbusRegisterTable.mat`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RegisterTable` |
| **值：** | 寄存器名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **Block sample time** — 写操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块会在指定的采样时间同步地将数据写入服务器。您可以为连续模式指定 0，或指定 -1 以继承连接到 Modbus Client Write 模块输入的模块的采样时间。有关详细信息，请参阅指定采样时间 (Simulink)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | -1（默认） | 非负标量 |
| **数据类型：** | `double` |

## 所属库

Industrial Communication Toolbox / Modbus

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

限制：

- 此模块仅为主机平台生成平台特定代码（Windows®、macOS、Linux®）。
- 在一个模型中，不能有多个 Modbus Client 模块（Read 或 Write）连接到 Modbus 串行服务器的同一串行端口。

## 版本历史

**在 R2024b 中引入**

## 描述

将数据写入 Modbus 服务器

Modbus Client Write 模块将数据写入 Modbus® TCP/IP 或串行服务器上的一个或多个寄存器。

每个输入端口将数据写入该模块 **Registers** 参数中指定的对应寄存器。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink® 许可证才能使用此模块。

**注意**

您必须将 Modbus Client Write 模块连接到 Modbus TCP/IP 或串行服务器。您可以使用模型“配置参数”对话框中的 **Modbus** 窗格创建客户端，以连接到 Modbus TCP/IP 或串行服务器。您必须在模型中至少添加一个 Modbus Client Read 或 Modbus Client Write 模块才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 Modbus 客户端。

### 其他支持的功能

Modbus Client Write 模块支持使用 Simulink 加速器和快速加速器模式。您可以使用这些模式加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速 (Simulink)。
