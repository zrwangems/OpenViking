---
type: simulink-block
title: 'Modbus Client Read'
family: 'icomm'
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
```yaml
ports:
- name: Reg_*x*
  summary: 寄存器的当前值向量
  direction: output
  data_types: double
```

### 输出

### **Reg\_*`x`*** — 寄存器的当前值向量

从 Modbus TCP/IP 或串行服务器读取的值。输出端口数量（*x*）对应于您在 Registers 参数中添加的行数。每个端口的数据大小为 1×*N*，其中 *N* 对应于要读取的连续寄存器数量。*N* 的值在 **Registers** 参数的 `Count` 字段中指定。该模块从 *N* 个连续寄存器中读取值，起始地址为 **Registers** 参数的 `Address` 字段中指定的寄存器地址。

#### 依赖关系

要启用此端口，请在 **Registers** 参数中指定一个或多个寄存器。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Client
  summary: 选择 Modbus 客户端 下拉列表
  group: ''
  block_parameter: ClientList
  values: Modbus 客户端名称
- name: Server ID
  summary: 服务器地址 1 （默认） | [0, 255] 范围内的非负整数
  group: ''
  block_parameter: ServerId
  values: 1 （默认） | [0, 255] 范围内的非负整数
- name: Registers
  summary: Modbus 寄存器列表表格
  group: ''
  block_parameter: RegisterTable
  values: register name and information
- name: Block sample time
  summary: 读取操作的采样时间 -1（默认）| 非负标量
  group: ''
  block_parameter: SampleTime
  values: -1 (default) | nonnegative scalar
```

### **Client** — 选择 Modbus 客户端 下拉列表

选择要与该模块关联的 Modbus 客户端。选择客户端后，该模块会更新 **Connection endpoint** 参数。

- 要使用 **Modbus** 窗格添加客户端，请点击 **Configure clients**。有关详细信息，请参阅 Configure Modbus Client in Simulink。
- 要更新客户端列表并显示最新的 Modbus 客户端，请点击 **Refresh**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | Modbus 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **Server ID** — 服务器地址 1 （默认） | [0, 255] 范围内的非负整数

要读取的服务器地址，指定为 [0, 255] 范围内的非负整数。默认值为 1。服务器地址指的是 Modbus TCP/IP 服务器的单元标识符。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ServerId` |
| **值：** | 1 （默认） | [0, 255] 范围内的非负整数 |
| **数据类型：** | `double` |

### **Registers** — Modbus 寄存器列表表格

将寄存器添加到要从指定客户端读取的列表中。

- 要添加寄存器，请点击 **Add**。此操作会在 **Registers** 表格中添加一行，其中 `Name`、`Register Type`、`Precision` 和 `Count` 分别设置为默认值 `Reg_1`、`Holding Register`、`uint16` 和 `1`。您必须在 `Address` 列中为要读取的寄存器指定地址。每次点击 **Add** 时，模块都会在 **Registers** 表格中添加新行，并将名称递增 1。

  - `Sl`. `no`.：此字段不可编辑，用于指定寄存器的序列号。序列号决定了模块在输出端口输出信号的顺序。
  - `Name`：这是一个可编辑的文本字段，用于指定寄存器的名称。此字段还定义了输出端口的名称。
  - `Address`：这是一个可编辑的文本字段，用于指定 Modbus 读取操作的起始地址。
  - `Register Type`：这是一个下拉列表，用于指定要读取的目标区域。您可以对四种类型的目标执行 Modbus 读取操作：线圈、输入、输入寄存器和保持寄存器。
  - `Precision`：这是一个下拉列表，用于指定读取寄存器的数据格式。请注意，`Precision` 字段并不指代模块输出的数据类型。输出的数据类型始终为 `double`。`Precision` 指定模块如何解释寄存器数据。

    - 对于线圈和输入，将此字段设置为 `bit`。
    - 对于保持寄存器和输入寄存器，将此字段设置为 `int16`、`uint16`、`int32`、`uint32`、`single`、`double`、`int64` 或 `uint64`。
  - `Count`：这是一个可编辑的文本字段，用于指定从对应 `Address` 字段中指定的地址开始读取的寄存器数量。
- 要删除寄存器，请选择这些寄存器并点击 **Delete**。
- 要导入保存为 MAT 文件的寄存器表格，请点击 **Import**。此操作会为当前工作区打开 Load register table 对话框。使用此浏览器，您可以选择包含寄存器信息的 MAT 文件。您选择的 MAT 文件必须包含一个名为 `ModbusRegisterTable` 的表格。

  **注意**

  Modbus Explorer 应用会将寄存器表格的内容导出为 MAT 文件。您可以将此 MAT 文件导入 Modbus Client Simulink 模块，以复用该寄存器表格。有关详细信息，请参阅 Use the Modbus Explorer App。
- 要将寄存器表格保存为 MAT 文件，请点击 **Export**。此操作会为当前工作区打开 Save register table 对话框。使用此浏览器，您可以将寄存器表格保存为 MAT 文件并存放在您选择的位置。默认文件名为 `ModbusRegisterTable.mat`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RegisterTable` |
| **值**：| register name and information |
| **Data Types:** | `character vector` | `string` |

### **Block sample time** — 读取操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步读取来自服务器的数据。有关详细信息，请参阅 Specify Sample Time (Simulink)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| -1 (default) | nonnegative scalar |
| **Data Types:** | `double` |
## 所属库

Industrial Communication Toolbox / Modbus

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

限制：

- 此模块仅为主机平台（Windows®、macOS、Linux®）生成平台特定的代码。
- 在一个模型中，不能有多个 Modbus Client 模块（读或写）连接到 Modbus 串行服务器的同一串行端口。

## 版本历史

**在 R2024b 中引入**

## 描述

从 Modbus 服务器读取数据

Modbus Client Read 模块从 Modbus® TCP/IP 或串行服务器上的一个或多个寄存器读取数据。

每个输出端口返回模块的 **Registers** 参数中指定的对应寄存器的数据。输出端口的数据大小为 1×*N*，其中 *N* 对应于 **Registers** 表中指定的要读取的连续寄存器数量。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink® 许可证才能使用此模块。

**注意**

您必须将 Modbus Client Read 模块连接到 Modbus TCP/IP 或串行服务器。您可以使用模型的配置参数对话框中的 **Modbus** 窗格创建客户端以连接到 Modbus TCP/IP 或串行服务器。您必须在模型中添加至少一个 Modbus Client Read 或 Modbus Client Write 模块才能启用此窗格。有关详细信息，请参阅 Configure Modbus Client in Simulink。

### 其他支持的功能

Modbus Client Read 模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration (Simulink)。
