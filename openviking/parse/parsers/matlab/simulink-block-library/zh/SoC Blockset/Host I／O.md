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
chinese_source: official
---

# SoC Blockset Model Structure

An SoC Blockset™ model consists of a top model that includes at least one of these reference models.

An SoC Blockset™ model consists of a top model that includes at least one of these reference
models.

- An FPGA reference model represents the FPGA part of an SoC device. The top model
  can include at most one FPGA reference model. For information on how to set up an
  FPGA reference model, see User Logic on FPGA.
- A processor reference model represents the processor part of an SoC device. The
  top model can include one or more processor reference models. For information on how
  to set up a processor reference model, see Software and Task Management on Processor.

The processor and the FPGA subsystems communicate through a Memory Channel,
Register Channel or
Interrupt Channel
block.

In addition to FPGA and processor reference models, the top model can include additional
SoC Blockset blocks, such as the blocks listed here, for modeling interfaces and test bench
components.

- ADC
  Interface, PWM
  Interface, LED, Push
  Button
- IO Data
  Sink, IO Data
  Source, Stream Data Source

The following image shows an SoC Blockset model, with an FPGA reference model, a processor reference model,
communicating over a memory channel.

Block diagram of top model. The top model includes an FPGA model, a processor model, a memory channel connected to a memory controller, and a register channel. The processor connects to a testbench unit with a scope to display simulation output.

For an example of an SoC Blockset model, see Streaming Data from Hardware to Software.

SoC Blockset provides project templates for common SoC use-cases. Use them as a starting
point for your design.

## See Also

### Topics

- Use Template to Create SoC Model
- Create an SoC Project Application
- Build Error When FPGA or Processor Model Not Detected

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

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

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
