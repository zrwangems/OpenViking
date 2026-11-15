---
type: simulink-block
title: 'eSpeak Text to Speech'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'espeaktexttospeech'
documentation_source_path: 'supportpkg/raspberrypi_ref/espeaktexttospeech.html'
language: en
---

# eSpeak Text to Speech

## Ports

### Input

### **ASCII text** — Input ASCII text character vector

The block accepts an array that is converted into its ASCII equivalent in the
format: `uint8('character vector')`. For
example, you can send `uint8('Hello world')` or `uint8('1 2
3')` to the input port of the block. However, if you send `[1 2
3]` to the input, the block does nothing.

**Data Types:** `uint8`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Convert text into speech on default audio device

Use the eSpeak Text to Speech block to convert text into speech using the
eSpeak speech synthesizer. The block outputs the synthesized speech through the default audio
device connected to your Raspberry Pi® board.

If you simulate a model on your host computer that contains an eSpeak Text to Speech block
without running it on your Raspberry Pi board, the block produces zeros (or no output). For more information, see Block Produces Zeros or Does Nothing in Simulation. You must use this block in
external mode (Monitor & Tune) or deploy the model on your Raspberry Pi board to listen to the output of the speech synthesizer.

When you run a model in external mode that contains the block, the block automatically
launches a background process that converts the input text to its corresponding ASCII values.
Once the conversion is over, the block is ready to convert another array of input text. If the
input text overlaps the text currently being converted, the block launches multiple background
processes that run concurrently. Although the Linux® sound driver mixes the sound from those processes, the resulting output is
unsatisfactory. Running too many processes concurrently produces errors.
