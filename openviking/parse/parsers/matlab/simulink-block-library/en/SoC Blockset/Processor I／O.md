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
language: en
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

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

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

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
