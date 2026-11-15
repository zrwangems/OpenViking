---
type: simulink-block
title: 'TalkBack Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'talkbackread'
documentation_source_path: 'supportpkg/android_ref/talkbackread.html'
language: zh-CN
chinese_source: worker-translation
---

# TalkBack Read

## 端口

### 输出

### **command string** — 输入 TalkBack 字符串命令标量

类型为 string 的 TalkBack 命令，指定为标量。

#### 依赖项

要启用此端口，请将 **Command type** 设置为 `String`。

**数据类型：** `string`

### **ascii command** — 输入 TalkBack ASCII 命令向量

由 ASCII 字符组成的转换后 `uint8` 向量 TalkBack 命令，指定为向量。

#### 依赖项

要启用此端口，请将 **Command type** 设置为 `ASCII vector`。

**数据类型：** `uint8`

### **status** — TalkBack 命令的状态 `0` | `1` | `2` | `3`

最后执行的命令的状态。端口上的状态输出对应 **TalkBack API** 参数中所选的选项。例如，如果 **TalkBack API** 参数设置为 `Last executed command`，输出将指示 `Last executed command` 选项的状态。

- `0` – 表示 TalkBack 命令执行失败或队列中不存在 TalkBack 命令。
- `1` – 表示 TalkBack 命令执行成功。
- `2` – 表示命令字符串被截断。
- `3` – 表示命令字符串用零填充，仅当 Command type 参数设置为 `ASCII vector` 时。

**数据类型：** `int8`

## 参数

### **TalkBack API** — 要对 TalkBack 命令执行的操作 `Execute next command`（默认）| `Last executed command`

选择要对 TalkBack 队列中的 TalkBack 命令执行的操作。

- `Execute next command` – 指示 TalkBack 服务器执行 TalkBack 队列中的下一条命令。根据 Command type 参数中设置的选项，此值可以是 ASCII 向量或字符串。如果 TalkBack 队列中不存在命令，则对于设置为 `ASCII vector` 的 Command type 参数，模块输出零；对于设置为 `String` 的 Command type 参数，模块输出空字符串。
- `Last executed command` – 指示 TalkBack 服务器在 command 输出端口上从 TalkBack 队列输出最后执行的命令。根据 Command type 参数中设置的选项，此值可以是字符串或 ASCII 向量。如果 TalkBack 队列中不存在命令，则对于设置为 `ASCII vector` 的 Command type 参数，模块输出零；对于设置为 `String` 的 Command type 参数，模块输出空字符串。

### **TalkBack ID** — TalkBack 应用标识号 123456（默认）| 正整数

输入 TalkBack 应用的标识号。此标识号由 TalkBack 服务器自动生成。要了解你的 ThingSpeak™ TalkBack 的 TalkBack ID：

1. 在 ThingSpeak 网站中，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 **TalkBack ID**。
4. 在 Simulink® 模型中打开 TalkBack Write 模块，并将该值粘贴到 **TalkBack ID** 参数中。

### **API key** — 为 ThingSpeak TalkBack 自动生成的 API key ABCDEFGHIJKLMNOP（默认）| API key 的字符向量 | API key 的字符串标量

输入 16 位 API key，用于允许你从 ThingSpeak TalkBack 读取的特定 TalkBack 实例。此 API key 由 TalkBack 服务器自动生成。此 API key 允许你从 ThingSpeak TalkBack 读取命令。要了解你的 ThingSpeak TalkBack 的 API key：

1. 在 ThingSpeak 网站中，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 16 位 **API key**。
4. 在 Simulink 模型中打开 TalkBack Read 模块，并将该值粘贴到 **API key** 参数中。

### **Command type** — 添加到 TalkBack 队列的 TalkBack 命令输入类型 `String`（默认）| `ASCII vector`

选择要添加到 TalkBack 队列的 TalkBack 命令输出类型。

- `String` – 字符串格式的 TalkBack 命令。
- `ASCII vector` – ASCII 格式的 TalkBack 命令。

### **Command length** — 命令字符串长度 1（默认）| `255`

输入 TalkBack 队列中命令的长度。如果命令的名称小于此参数中输入的值，则命令用零填充以匹配该长度。并且，如果命令的名称大于此参数中输入的值，则长度将截断为此参数中输入的值。

### **Sample time** — 模块从 TalkBack 读取数据的时间间隔 5（默认）| 标量

输入模块从 ThingSpeak TalkBack 读取数据的时间间隔（以 seconds 为单位）。将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定为该模块的最佳采样时间。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从 ThingSpeak TalkBack 服务器上的 TalkBack ID 读取命令

TalkBack Read 模块从 ThingSpeak TalkBack 服务器上的 TalkBack ID 读取命令。命令从 TalkBack 队列按先进先出 (FIFO) 顺序读取并执行，执行后从队列中移除。
