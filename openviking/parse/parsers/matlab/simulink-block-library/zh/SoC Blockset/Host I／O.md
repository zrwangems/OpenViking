---
type: simulink-block
title: 'SoC Blockset Model Structure'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'soc-blockset-model-structure'
documentation_source_path: 'ug/soc-blockset-model-structure.html'
language: zh-CN
chinese_source: worker-translation
---

# SoC Blockset Model Structure

一个 SoC Blockset™ 模型由一个顶层模型组成，该顶层模型包含至少一个以下参考模型。

一个 SoC Blockset™ 模型由一个顶层模型组成，该顶层模型包含至少一个以下参考模型。

- 一个 FPGA 参考模型表示 SoC 器件的 FPGA 部分。顶层模型最多可以包含一个 FPGA 参考模型。有关如何设置 FPGA 参考模型的信息，请参阅 User Logic on FPGA。
- 一个处理器参考模型表示 SoC 器件的处理器部分。顶层模型可以包含一个或多个处理器参考模型。有关如何设置处理器参考模型的信息，请参阅 Software and Task Management on Processor。

处理器和 FPGA 子系统通过 Memory Channel、Register Channel 或 Interrupt Channel 模块进行通信。

除了 FPGA 和处理器参考模型之外，顶层模型还可以包含其他 SoC Blockset 模块，例如此处列出的用于建模接口和测试平台组件的模块。

- ADC Interface、PWM Interface、LED、Push Button
- IO Data Sink、IO Data Source、Stream Data Source

下图展示了一个 SoC Blockset 模型，其中包含一个 FPGA 参考模型、一个处理器参考模型，并通过内存通道进行通信。

顶层模型的框图。顶层模型包含一个 FPGA 模型、一个处理器模型、一个连接到内存控制器的内存通道，以及一个寄存器通道。处理器连接到一个带有示波器的测试平台单元，用于显示仿真输出。

有关 SoC Blockset 模型的示例，请参阅 Streaming Data from Hardware to Software。

SoC Blockset 为常见的 SoC 用例提供了项目模板。可将它们用作设计的起点。

## 另请参阅

### 主题

- 使用模板创建SoC模型
- Create an SoC Project Application
- 未检测到FPGA或处理器模型时出现构建错误

## MATLAB 命令

您点击了一个对应于以下 MATLAB 命令的链接：

在 MATLAB Command Window 中输入该命令以运行它。
Web 浏览器不支持 MATLAB 命令。

关闭

MathWorks
MathWorks

选择网站

选择网站以获取翻译内容（如可用），并查看本地活动和优惠。根据您的位置，我们建议您选择：

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站

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
