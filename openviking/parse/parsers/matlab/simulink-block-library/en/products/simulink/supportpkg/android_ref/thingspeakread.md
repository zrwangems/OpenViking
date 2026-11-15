---
type: simulink-block
title: 'ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'thingspeakread'
documentation_source_path: 'supportpkg/android_ref/thingspeakread.html'
language: en
---

# ThingSpeak Read

## Ports

### Output

### **Field1** — Data read from specified field of ThingSpeak channel scalar

At each time step, the port outputs the data read from the field specified in the
**Field Number** parameter. If the data received is null, the port
outputs `0`.

**Data Types:** `single`

### **Status** — ThingSpeak server response for each read request scalar

The port outputs the ThingSpeak server response for the read request at each time step. The response is
received as an HTTP status code. An HTTP status code of `200`
indicates that the read request is successfully completed. For more information on
HTTP status codes, see `matlab.net.http.StatusCode`.

If the data received is null, the port outputs `0`.

**Data Types:** `single`

## Parameters

### **Channel ID** — Channel ID from which block reads data `12397` (default) | any positive integer

Specify the channel ID from which the block reads data.

If you do not know the channel ID of your channel:

1. Sign In to
   ThingSpeak using your MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel from which to read data.
4. Click the **Channel Settings** tab.
5. Copy the channel ID from the **Channel ID** parameter.
6. Open the ThingSpeak Read block in your model and paste the copied
   ID to the **Channel ID** parameter.

### **Channel Access** — Sharing settings of channel `Public` (default) | `Private`

Specify if your channel is private or public.

If you do not know the sharing settings of your channel:

1. Sign In to
   ThingSpeak using your MathWorks Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the sharing status.
4. Click the **Sharing** tab. Use the option selected in the tab
   to set **Channel Access**.

   - **Keep channel view private**: Set **Channel
     Access** to `Private`. Only you can view the
     channel data.
   - **Share channel view with everyone**: Set **Channel
     Access** to `Public`. Anyone browsing the
     ThingSpeak website can view the channel data.
   - **Share channel view only with the following users**: Set
     **Channel Access** to `Private`.
     Users who have access to shared channels can see only the private view of a
     channel; they cannot add channels, see alerts, or see license
     information.

### **Read API Key** — Key to read data from a private or shared channel `ABCDEFGHIJK` (default) | any valid Read API Key

When you read data from your channel using the ThingSpeak API or MATLAB code, you need an appropriate read permission. The 16-digit API key allows
you to read data from a private or a shared channel. You do not need an API key to read
from a public ThingSpeak channel.

If you do not know the read API key of your channel:

1. Sign In to
   ThingSpeak using your The MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the read API key.
4. Click the **API Keys** tab.
5. Copy the key from the **Read API Keys** parameter.
6. Open the ThingSpeak Read block in your model and paste the copied
   API key into the **Read API Key** parameter.

#### Dependencies

The **Read API Key** parameter appears only when you set the
**Channel Access** parameter to
`Private`.

### **Field Number** — Field from which block reads data `1` (default) | any integer between 1 and 8

Select a field of the ThingSpeak channel from which the block reads data.

### **Sample time** — Interval at which block reads data from ThingSpeak channel `60` (default) | `-1` | any nonnegative value

Specify how often this block reads data from the ThingSpeak channel.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read data stored in ThingSpeak channel

The ThingSpeak Read block reads data from the ThingSpeak™ channel on ThingSpeak.com
website.

ThingSpeak is an open Internet of Things (IoT) platform with MATLAB® analytics that allows you to collect and store sensor data in the cloud and
develop IoT applications. The ThingSpeak IoT platform provides applications that allow you to analyze and visualize your
data in MATLAB and then act on the data. For errors related to connection, channel ID, fields,
and success logs, see the **Log** tab in the generated application on the
Android® device.
