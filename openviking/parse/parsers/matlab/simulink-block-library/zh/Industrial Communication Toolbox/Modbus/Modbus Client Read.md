---
type: simulink-block
title: 'Modbus Client Read'
family: 'modbus'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'Modbus'
documentation_page: 'modbusclientread'
documentation_source_path: 'ug/modbusclientread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus Client Read

## 端口

### 输出

### **Reg\_*`x`*** — 寄存器向量的当前值

从 Modbus TCP/IP 或串行服务器读取的值。输出端口 (*x*) 的数量对应于您在 Registers 参数中添加的行数。每个端口的数据大小为 1-by-*N*，其中 *N* 对应于要读取的连续寄存器数量。*N* 的值在 **Registers** 参数的 `Count` 字段中指定。模块从 *N* 个连续寄存器读取值，起始地址为 **Registers** 参数的 `Address` 字段中指定的寄存器地址。

#### 依赖关系

要启用此端口，请在 **Registers** 参数中指定一个或多个寄存器。

**数据类型：** `double`

## 参数

### **Client** — 选择 Modbus 客户端下拉列表

选择要与该模块关联的 Modbus 客户端。选择客户端后，模块会更新 **Connection endpoint** 参数。

- 要使用 **Modbus** 窗格添加客户端，请点击 **配置客户端**。有关详细信息，请参阅在 Simulink 中配置 Modbus 客户端。
- 要更新客户端列表并显示最新的 Modbus 客户端，请点击 **刷新**。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | Modbus 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **Server ID** — 服务器的地址 1（默认） | [0, 255] 范围内的非负整数

要读取的服务器地址，指定为 [0, 255] 范围内的非负整数。默认值为 1。服务器地址指 Modbus TCP/IP 服务器的单元标识符。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ServerId` |
| **值：** | 1（默认） | [0, 255] 范围内的非负整数 |
| **数据类型：** | `double` |

### **Registers** — Modbus 寄存器列表表格

添加要从指定客户端读取的寄存器。

- 要添加寄存器，请点击 **添加**。此操作会在 **Registers** 表中添加一行，其中 `Name`、`Register Type`、`Precision` 和 `Count` 分别设置为默认值 `Reg_1`、`Holding Register`、`uint16` 和 `1`。您必须在 `Address` 列中指定要读取的寄存器的地址。每次点击 **添加** 时，模块都会在 **Registers** 表中添加一个新行，并将名称递增 1。

  - `Sl`. `no`.：此字段不可编辑，用于指定寄存器的序号。序号决定模块在输出端口输出信号的顺序。
  - `Name`：这是一个可编辑文本字段，用于指定寄存器的名称。此字段还定义输出端口的名称。
  - `Address`：这是一个可编辑文本字段，用于指定 Modbus 读取操作的起始地址。
  - `Register Type`：这是一个下拉列表，用于指定要读取的目标区域。您可以在四类目标上执行 Modbus 读取操作：线圈、输入、输入寄存器和保持寄存器。
  - `Precision`：这是一个下拉列表，用于指定所读取寄存器的数据格式。请注意，`Precision` 字段并不指模块输出的数据类型。输出的数据类型始终为 `double`。`Precision` 指定模块如何解释寄存器数据。

    - 对于线圈和输入，将此字段设置为 `bit`。
    - 对于保持寄存器和输入寄存器，将此字段设置为 `int16`、`uint16`、`int32`、`uint32`、`single`、`double`、`int64` 或 `uint64`。
  - `Count`：这是一个可编辑文本字段，用于指定从相应 `Address` 字段中指定的地址开始要读取的寄存器数量。
- 要删除寄存器，请选择这些寄存器并点击 **删除**。
- 要导入保存为 MAT 文件的寄存器表，请点击 **导入**。此操作会打开当前工作区的“加载寄存器表”对话框。使用此浏览器，您可以选择包含寄存器信息的 MAT 文件。您选择的 MAT 文件必须包含名为 `ModbusRegisterTable` 的表。

  **注意**

  Modbus Explorer 应用会将寄存器表的内容导出为 MAT 文件。您可以将此 MAT 文件导入 Modbus Client Simulink 模块，以重用寄存器表。有关详细信息，请参阅使用 Modbus Explorer 应用。
- 要将寄存器表保存为 MAT 文件，请点击 **导出**。此操作会打开当前工作区的“保存寄存器表”对话框。使用此浏览器，您可以将寄存器表保存为 MAT 文件并将其保存在您选择的位置。默认文件名为 `ModbusRegisterTable.mat`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RegisterTable` |
| **值：** | 寄存器名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **Block sample time** — 读取操作的采样时间 -1（默认） | 非负标量

定义模块的采样时间，单位为 seconds。模块在指定的采样时间同步从服务器读取数据。有关详细信息，请参阅指定采样时间 (Simulink)。

#### 以编程方式使用

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

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

限制：

- 此模块仅为宿主机平台（Windows®、macOS、Linux®）生成特定于平台的代码。
- 在模型中，不能有多个 Modbus Client 模块（Read 或 Write）连接到 Modbus 串行服务器的同一串行端口。

## 版本历史

**在 R2024b 中引入**

## 描述

从 Modbus 服务器读取数据

Modbus Client Read 模块从 Modbus® TCP/IP 或串行服务器上的一个或多个寄存器读取数据。

每个输出端口返回来自模块 **Registers** 参数中指定的对应寄存器的数据。输出端口的数据大小为 1-by-*N*，其中 *N* 对应于 **Registers** 表中指定的要读取的连续寄存器数量。

**注意**

使用此模块需要 Industrial Communication Toolbox™ 和 Simulink® 许可证。

**注意**

您必须将 Modbus Client Read 模块连接到 Modbus TCP/IP 或串行服务器。您可以使用模型“配置参数”对话框中的 **Modbus** 窗格创建用于连接到 Modbus TCP/IP 或串行服务器的客户端。您必须在模型中添加至少一个 Modbus Client Read 或 Modbus Client Write 模块才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 Modbus 客户端。

### 其他支持的功能

Modbus Client Read 模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅加速 (Simulink)。
