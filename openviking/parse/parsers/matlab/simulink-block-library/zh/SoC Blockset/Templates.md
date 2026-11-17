---
type: simulink-block
title: 'Use Template to Create SoC Model'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'use-templates-to-create-soc-model'
documentation_source_path: 'ug/use-templates-to-create-soc-model.html'
language: zh-CN
chinese_source: worker-translation
---

# Use Template to Create SoC Model

SoC Blockset™ 模型模板为面向仿真、HDL 代码生成或 SoC 部署的模型提供设计模式和最佳实践。从任一 SoC Blockset 模型模板创建的模型，其配置参数都已为仿真和代码生成设置好。

SoC Blockset™ 模型模板为面向仿真、HDL 代码生成或 SoC 部署的模型提供设计模式和最佳实践。从任一 SoC Blockset 模型模板创建的模型，其配置参数都已为仿真和代码生成设置好。

### 使用 SoC Blockset 模板创建 SoC 模型

为了高效地为 SoC 设计建模硬件，请使用 SoC Blockset 模板创建工程。

1. 在 MATLAB® 的 **Home** 选项卡中，选择 **Simulink** 按钮。
   或者，在命令行中输入：

   ```
   simulink
   ```
2. 在 Simulink® 起始页中，向下滚动到 **SoC
   Blockset** 部分，其中包含常见工作流的 SoC 模板链接。选择一个模板并保存工程。工作区中会打开一个工程文件夹，其中包含：

   - 名为 `soc_*_top.slx` 的模型 – SoC 工程的顶层模型。
   - `referencedmodels` – 包含顶层模型所引用模型的文件夹。某些模板包含 FPGA 模型和处理器模型。其他模板只包含一个引用模型：FPGA 模型或处理器模型。
   - `utilities` – 包含模型所用实用函数或测试平台数据的文件夹。

   要在 Simulink 中打开顶层模型，请在 **Project Shortcuts** 选项卡上点击 **Open Top model**。
3. 在每个模板中，导航到 FPGA 模型中标记为 **FPGA
   Algorithm** 的模块，或处理器模型中标记为 **Processor
   Algorithm** 的模块。这些模块会被高亮显示以便于识别。将模板模块替换为您自己的算法模型。

   **提示**

   要轻松找到算法模块，请按照整个模型层次结构中的注释进行操作。
4. 要打开 **SoC Blockset** 模块库，请选择 Library Browser 按钮，然后在左侧窗格中选择 **SoC Blockset**。或者，在命令行中输入：

   ```
   soclib
   ```

   该库包含用于创建 SoC 模型和测试平台的模块。

### 模板结构

SoC Blockset 模板中的顶层模型包含一个 FPGA 子系统，它表示用于对 FPGA 编程的逻辑。FPGA 子系统包含两个 Simulink 模型变体：

- 基于帧的 FPGA 模型 – 用于增强仿真性能（RFSoC 模板中不可用）
- 基于采样的 FPGA 模型 – 用于周期精确性和代码生成

顶层模型还包含一个处理器子系统，它表示用于在 SoC 处理器上运行的软件程序。FPGA 子系统和顶层子系统都包含标记为 FPGA Algorithm 或 Processor Algorithm 的模块。请将这些算法替换为您自己的逻辑。模板的顶层模型还包含一个内存系统，其中有内存控制器和内存通道。这些模块表示板上的物理内存系统。该模型通常还包含寄存器通道（用于实现处理器与 FPGA 之间的通信）、测试平台或 I/O 模块。

### 修改工程

#### 修改 FPGA 模型

从顶层模型，点击 FPGA 模块左下角的箭头打开 FPGA 模型：

FPGA 模型包含两个模型变体：基于帧的变体和基于采样的变体。双击要修改的模型变体。FPGA 模型通常包含两个可供修改的主要子系统：

- FPGA Algorithm Wrapper – 双击打开模型。算法包装器包含一个绿色高亮的子系统，名为 FPGA Algorithm。该模块有两个输入和一个输出，实现为乘法器。将此模块替换为您自己的 FPGA 算法。根据需要添加输入和输出。
- Test Source Wrapper – 该模块包含一个测试源，用于生成激励作为 FPGA 算法的输入。根据您的需求修改测试源，或将其替换为替代源模块。如果 FPGA 算法的输入来自 I/O 模块（如 HDMI 或 SDR），请考虑使用特定的应用模板。

  **注意**

  并非所有模板都在 FPGA 模型中包含 Test Source 模块。

#### 修改处理器模型

处理器模型包含一个 Task Manager 模块和一个处理器包装器。模板将处理器算法实现为“直通”连线。打开处理器算法包装器，将 Processor Algorithm 模块（蓝色高亮）替换为您所需的算法。

#### 修改寄存器通道

模板的顶层模型还包含一个寄存器通道，用于在处理器和 FPGA 模型之间通信。使用寄存器通道来配置 FPGA 模型，或读取和检查状态寄存器。模板中的 Register Channel 模块包含一个寄存器。要添加额外的寄存器，您必须修改寄存器通道模块参数、FPGA 算法和处理器算法：

1. 向寄存器通道添加寄存器 – 双击 Register Channel 模块打开模块掩码，根据需要添加额外的寄存器。添加寄存器会在 Register Channel 模块上创建额外的端口。有关更多信息，请参阅 Register Channel。
2. 向处理器模型添加端口 – 导航到 Processor Algorithm Wrapper 模型。要导航到处理器模型，请在 **Project Shortcuts** 选项卡上点击 **Open Processor model**。双击 Processor Algorithm Wrapper 进行修改。

   对于写寄存器，向模块添加一个输出端口，并添加逻辑以将值驱动到添加的输出端口。对于读寄存器，添加一个输入端口和逻辑以处理从读寄存器返回的信息。从顶层模型，将端口连线到 Register Channel 模块。
3. 向 FPGA 模型添加端口 – 导航到 FPGA Algorithm Wrapper 模型。要导航到 FPGA/Frame based processing 模型，请在 **Project Shortcuts** 选项卡上点击 **Open FPGA sample model**。双击 FPGA Algorithm Wrapper 进行修改。

   对于写寄存器，向模块添加一个输入端口和逻辑以处理从读寄存器返回的信息。对于读寄存器，添加一个输出端口和逻辑以将值驱动到添加的输出端口。

   要在使用 Simulink 基于采样的变体时获得等效行为，请对 FPGA 包装器中的基于采样的处理模型重复此步骤。
4. 从顶层模型，将新端口连线到 Register Channel 模块。

## 另请参阅

Task Manager | Register Channel | Memory Controller | Memory Channel

### 主题

- Stream from FPGA to Processor Template
- Stream from Processor to FPGA Template
- SDR Template
- HDMI Template
- Frame Buffer with HDMI Template
- RFSoC Template
- SoC Software Architecture Template

## MATLAB 命令

您点击了一个对应于以下 MATLAB 命令的链接：

在 MATLAB Command Window 中输入命令以运行它。
Web 浏览器不支持 MATLAB 命令。

Close

MathWorks
MathWorks

Select a Web Site

选择一个网站以获取可用的翻译内容，并查看本地活动和优惠。根据您的位置，我们建议您选择：

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太地区

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
