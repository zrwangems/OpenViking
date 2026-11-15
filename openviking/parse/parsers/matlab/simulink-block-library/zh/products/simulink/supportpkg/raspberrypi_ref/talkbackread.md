---
type: simulink-block
title: 'TalkBack Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'talkbackread'
documentation_source_path: 'supportpkg/raspberrypi_ref/talkbackread.html'
language: zh-CN
chinese_source: worker-translation
---

# TalkBack Read

## 端口

### 输出

### **Command string** — 由模块读取的字符串命令标量

模块从 TalkBack 服务器读取的字符串命令，以 string scalar 形式返回。

#### 依赖关系

要启用此端口，请将 **Command Type** 设置为 `String`。

**数据类型：** `string`

### **Ascii command** — 由模块读取的 ASCII 命令向量

模块从 TalkBack 服务器读取的 ASCII 命令，以向量形式返回。

#### 依赖关系

要启用此端口，请将 **Command Type** 设置为 `ASCII vector`。

**数据类型：** `uint8`

### **Status** — TalkBack 命令的状态 `0` | `1` | `2` | `3`

TalkBack 服务器执行的最后一条命令的状态。模块根据你在 **TalkBack API** 参数中选择的选项，在 **Status** 上输出状态。例如，如果 **TalkBack API** 参数设置为 `Last executed command`，输出将指示 `Last executed command` 选项的状态。

- `0` — 指示 TalkBack 命令执行失败或 TalkBack 队列为空。
- `1` — 指示 TalkBack 命令执行成功。
- `2` — 指示命令字符串被截断。
- `3` — 仅当 **Command Type** 参数设置为 `ASCII vector` 时，指示命令已用零填充。

**数据类型：** `int8`

## 参数

### **TalkBack API** — 要对 TalkBack 命令执行的操作 `Execute next command`（默认）| `Last executed command`

选择要对 TalkBack 队列中的 TalkBack 命令执行的操作。

- `Execute next command` — 模块请求 TalkBack 服务器执行 TalkBack 队列中的下一条命令。模块读取此命令，并根据你在 **Command Type** 参数中设置的选项输出字符串或 ASCII 向量。如果 TalkBack 队列中没有命令，则当你将 **Command Type** 参数设置为 `ASCII vector` 时，模块输出零；当你将 **Command Type** 参数设置为 `String` 时，模块输出 null。
- `Last executed command` — 模块请求 TalkBack 服务器输出 TalkBack 队列中最后执行的命令。模块读取此命令，并根据你在 **Command Type** 参数中设置的选项，将其输出为字符串或 ASCII 向量。如果 TalkBack 队列中没有命令，则当你将 **Command Type** 参数设置为 `ASCII vector` 时，模块输出零；当你将 **Command Type** 参数设置为 `String` 时，模块输出 null。

### **TalkBack ID** — TalkBack 应用标识号 123456（默认）| 正整数

输入 TalkBack 应用的标识号。此标识号由 TalkBack 服务器自动生成。要为你的 TalkBack 通道查找 TalkBack ID：

1. 在 ThingSpeak 网站上，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 **TalkBack ID**。
4. 在你的 Simulink® 模型中打开 TalkBack Read 模块，并将该值粘贴到 **TalkBack ID** 参数中。

### **API key** — 为 TalkBack 通道自动生成的 API key ABCDEFGHIJKLMNOP（默认）| character vector | string scalar

输入 TalkBack 特定实例的 16 位 API key，该 API key 允许你从 TalkBack 通道读取。此 API key 由 TalkBack 服务器自动生成。要为你的 TalkBack 通道查找 API key：

1. 在 ThingSpeak 网站上，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 16 位 **API key**。
4. 在你的 Simulink 模型中打开 TalkBack Read 模块，并将该值粘贴到 **API key** 参数中。

### **Command Type** — 添加到 TalkBack 队列的命令输出类型 `String`（默认）| `ASCII vector`

选择要添加到 TalkBack 队列的 TalkBack 命令输出类型。

- `String` — 字符串格式的 TalkBack 命令。
- `ASCII vector` — ASCII 格式的 TalkBack 命令。

### **Command Length** — 命令长度 1（默认）| `255`

输入 TalkBack 队列中命令的长度。如果命令名称小于此参数中输入的值，则用零填充该命令以匹配该长度。如果命令名称大于此参数中输入的值，则将该长度截断为此参数中输入的值。

### **Print diagnostic messages** — 将 TalkBack 服务器响应保存到日志文件 off（默认）| on

选择此参数可将每次读取请求的 TalkBack 服务器响应保存到日志文件。使用名为 `TALKBACK_DIAG_MSG:` 的标头标识此请求。日志文件的名称格式为 `<model_name>.log`。

### **Sample time** — 模块读取数据的时间间隔 5（默认）| 标量

输入模块从 TalkBack 通道读取数据的时间间隔（以秒为单位）。当你将此参数设置为 `-1` 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从 ThingSpeak TalkBack 服务器上的 TalkBack ID 读取命令

TalkBack Read 模块从 ThingSpeak TalkBack 服务器上的 TalkBack ID 读取命令。该模块按先进先出（FIFO）顺序读取 TalkBack 服务器队列中的命令，命令执行后即从队列中移除。
