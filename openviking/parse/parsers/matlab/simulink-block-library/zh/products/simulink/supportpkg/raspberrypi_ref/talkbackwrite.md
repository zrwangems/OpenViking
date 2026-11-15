---
type: simulink-block
title: 'TalkBack Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'talkbackwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/talkbackwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# TalkBack Write

## 端口

### 输入

### **Trigger** — 用于在 TalkBack 队列中添加或删除命令的触发 `0` | 大于 `0` 的任意值

向 TalkBack 队列输入，或删除 TalkBack 队列中的所有命令。

**数据类型：** `Boolean` | `Numeric`

### **Command string** — 要由模块添加的字符串命令，标量

要由模块添加的字符串命令，指定为标量。

#### 依赖关系

要启用此端口，请将 **Command type** 设置为 `String`，并将 **TalkBack API** 设置为 `Add a command`。

**数据类型：** `string`

### **Ascii command** — 要由模块添加的 ASCII 命令，向量

要由模块添加的 ASCII 命令，指定为向量。

#### 依赖关系

要启用此端口，请将 **Command type** 设置为 `ASCII vector`，并将 **TalkBack API** 设置为 `Add a command`。

**数据类型：** `uint8`

### **Position** — 命令在队列中的位置，整数

TalkBack 命令在 TalkBack 队列中的位置。位于此位置处或之后的任何先前命令都会在队列中向下移动。如果未指定位置，模块会将命令添加到队列末尾，即最高位置。

#### 依赖关系

要启用此端口，请将 **TalkBack API** 参数设置为 `Add a command`，并选中 **Specify position** 参数。

**数据类型：** `uint16`

## 参数

### **TalkBack API** — 在 TalkBack 队列中添加或删除命令 `Add a command`（默认）| `Delete all commands`

选择要对 TalkBack 队列执行的操作类型。

- `Add a command` — 向 TalkBack 队列添加一条命令
- `Delete all commands` — 从 TalkBack 队列删除所有命令

### **TalkBack ID** — TalkBack 应用标识号 123456（默认）| 正整数

输入 TalkBack 应用的标识号。此标识号由 TalkBack 服务器自动生成。要查找 TalkBack 通道的 TalkBack ID：

1. 在 ThingSpeak 网站上，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 **TalkBack ID**。
4. 在 Simulink® 模型中打开 TalkBack Write 模块，并将该值粘贴到 **TalkBack ID** 参数中。

### **API key** — 为 TalkBack 通道自动生成的 API key ABCDEFGHIJKLMNOP（默认）| character vector | string scalar

输入用于特定 TalkBack 实例的 16 位 API key，该密钥允许您写入 TalkBack 通道。此 API key 由 TalkBack 服务器自动生成。要查找 TalkBack 通道的 API key：

1. 在 ThingSpeak 网站上，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 16 位 **API key**。
4. 在 Simulink 模型中打开 TalkBack Write 模块，并将该值粘贴到 **API key** 参数中。

### **Command type** — 添加到 TalkBack 队列的命令类型 `String`（默认）| `ASCII vector`

选择您希望模块添加到 TalkBack 队列的 TalkBack 命令类型。

- `String` — 字符串格式的 TalkBack 命令。
- `ASCII vector` — ASCII 格式的 TalkBack 命令。

#### 依赖关系

要启用此端口，请将 **TalkBack API** 参数设置为 `Add a command`。

### **Specify position** — 启用或禁用 position 输入端口 off（默认）| on

选择此选项以启用模块的 **position** 输入端口。

#### 依赖关系

要启用此端口，请将 **TalkBack API** 参数设置为 `Add a command`。

### **Print diagnostic messages** — 将 TalkBack 服务器响应保存到日志文件 off（默认）| on

选择此参数可将来自 TalkBack 服务器的响应保存到日志文件，每个读取请求一个。使用名为 `TALKBACK_DIAG_MSG:` 的标头标识此请求。日志文件的名称格式为 `<model_name>.log`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

将命令写入 ThingSpeak TalkBack 服务器上的 TalkBack ID

TalkBack Write 模块将命令写入 ThingSpeak TalkBack 服务器上的 TalkBack ID。该模块按先进先出 (FIFO) 顺序将命令写入 TalkBack 队列，并且命令一旦执行便会从队列中移除。
