---
type: simulink-block
title: 'TalkBack Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'talkbackwrite'
documentation_source_path: 'supportpkg/android_ref/talkbackwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# TalkBack Write

## 端口

### 输入

### **trigger** — 用于在 TalkBack 队列中添加或删除命令的触发 `0` | `1`

触发输入，允许向 TalkBack 队列添加命令或从 TalkBack 队列中删除所有命令。

**数据类型：** `Boolean` | `Numeric`

### **command string** — 输入 TalkBack 字符串命令标量

类型为 string 的 TalkBack 命令，指定为标量。

#### 依赖项

要启用此端口，请将 **Command type** 设置为 `String`。

**数据类型：** `string`

### **ascii command** — 输入 TalkBack ASCII 命令向量

由 ASCII 字符转换得到的 `uint8` 向量 TalkBack 命令，指定为向量。

#### 依赖项

要启用此端口，请将 **Command type** 设置为 `ASCII vector`。

**数据类型：** `uint8`

### **position** — 命令在队列中的位置 整数

TalkBack 命令在 TalkBack 队列中的位置。所有先前位于该位置处或之后的命令都将下移。如果位置留空，则该命令会自动添加到队列末尾，位置编号最高。

#### 依赖项

要启用此端口，请选择 **Specify position** 参数。

**数据类型：** `uint16`

## 参数

### **TalkBack API** — 在 TalkBack 队列中添加或删除命令 `Add a command`（默认） | `Delete all commands`

选择要对 TalkBack 队列中的 TalkBack 命令执行的操作类型。

- `Add a command` – 向 TalkBack 队列添加命令
- `Delete all commands` – 从 TalkBack 队列中删除所有命令

### **TalkBack ID** — TalkBack 应用标识号 123456（默认） | 正整数

输入 TalkBack 应用的标识号。此标识号由 TalkBack 服务器自动生成。要了解你的 ThingSpeak™ TalkBack 的 TalkBack ID：

1. 在 ThingSpeak 网站中，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 **TalkBack ID**。
4. 在你的 Simulink® 模型中打开 TalkBack Write 模块，并将该值粘贴到 **TalkBack ID** 参数中。

### **API key** — ThingSpeak TalkBack 自动生成的 API key ABCDEFGHIJKLMOP（默认） | API key 字符向量 | API key 字符串标量

输入特定 TalkBack 实例的 16 位 API key，该实例允许你写入 ThingSpeak TalkBack。此 API key 由 TalkBack 服务器自动生成。此 key 允许你向 ThingSpeak TalkBack 写入命令。要了解你的 ThingSpeak TalkBack 的 API key：

1. 在 ThingSpeak 网站中，选择 **Apps** > **TalkBack**。
2. 点击 **New TalkBack**。
3. 向 TalkBack 队列添加新命令，并复制 16 位 **API key**。
4. 在你的 Simulink 模型中打开 TalkBack Write 模块，并将该值粘贴到 **API key** 参数中。

### **Command type** — 添加到 TalkBack 队列的 TalkBack 命令输入类型 `String`（默认） | `ASCII vector`

选择要添加到 TalkBack 队列的 TalkBack 命令输入类型。

- `String` – 字符串格式的 TalkBack 命令。
- `ASCII vector` – ASCII 格式的 TalkBack 命令。

### **Specify position** — 启用或禁用 position 输入端口 off（默认） | on

选择该选项以启用模块的 **position** 输入端口。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

将命令写入 ThingSpeak TalkBack 服务器上的 TalkBack ID

TalkBack Write 模块将命令写入 ThingSpeak TalkBack 服务器上的 TalkBack ID。这些命令按先进先出 (FIFO) 顺序写入 TalkBack 队列并执行，执行后将从队列中移除。
