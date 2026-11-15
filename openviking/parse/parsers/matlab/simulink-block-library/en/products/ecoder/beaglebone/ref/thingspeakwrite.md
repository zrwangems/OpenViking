---
type: simulink-block
title: 'ThingSpeak Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'beaglebone/ref/thingspeakwrite.html'
language: en
---

# ThingSpeak Write

## Ports

### Input

### **varn** — Data published to nth variable of ThingSpeak channel [`1` x *N*] vector, where *N* ranges from `1` to `8`

The block publishes the data to the nth variable in the ThingSpeak channel at each time step. The number of data channels at the block
input depends on the number of variables that you select in the **Number of variables to send** parameter. For example, if you set the
**Number of variables to send** parameter to
`3`, the block enables three input port with port names **var1**, **var2**, and **var3**.

**Data Types:** `single`

### **location** — Send location data three-element numeric vector

The block sends the location data that is specified as a three-element numeric
vector of the form [*latitude*, *longitude*,
*altitude*].

#### Dependencies

- To enable this port, on the **Optional** tab, select
  **Send location information** and set the
  **Coordinate source** parameter to `Input
  port`.

**Data Types:** `single` | `double`

## Parameters

### Main

### **Update URL** — Add URL from ThingSpeak website https://api.thingspeak.com/update (default) | char vector

Enter the URL from the **Add data by sending a POST or GET
to** parameter in ThingSpeak.com. To know the URL:

1. In the ThingSpeak.com website, select **Channels** > **My Channels**.
2. Under the channel that you created for this target hardware, click
   **Settings**.
3. Click the **Data Import/Export** tab.
4. Copy the URL from **Add data by sending a POST or GET
   to** parameter.
5. Open the ThingSpeak Write block in your Simulink® model and paste the URL in the **Update URL**
   parameter.

### **Write API key** — Write API key of ThingSpeak channel no default (default) | character vector

Enter the 16-digit write API key of the ThingSpeak channel.

Follow these steps to know the API key for your ThingSpeak channel.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the write API key.
4. Click the **API Keys** tab and copy the key from the
   **Write API Keys** parameter.Write API Key
5. Open the ThingSpeak Write block in your model and paste the
   copied API key into the **Write API key** parameter.

### **Number of variables to send** — Number of ThingSpeak variables to publish data `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8`

Select the number of ThingSpeak variables to publish data from the block.

### **Update interval (seconds)** — Data update interval `60` (default) | nonnegative scalar

Specify the time interval at which the input data is updated on the ThingSpeak channel.

### **Print diagnostic messages** — Save ThingSpeak server response to log file Off (default) | On

Select this parameter to save the response from the ThingSpeak server to a log file for each write request. The name of the log file
has the format `<model_name>.log`.

### Optional

### **Send location information** — Send location information Off (default) | On

Select this parameter to send the location information to the ThingSpeak channel.

### **Coordinate source** — Source of location data `Block dialog` (default) | `Input port`

Select the source of the location data.

- `Block dialog` — Specify the location using the
  **Location (latitude, longitude, altitude)**
  parameter.
- `Input port` — Specify the location using the
  **location** input port.

Use decimal degrees notation to specify *latitude* and
*longitude* whereas, use meters to specify
*altitude*. For example,

- The lowest human-sized point underground, the TauTona Mine in Carletonville,
  South Africa, is [`-26.416111,27.4275,-3900`].
- The highest point measured from sea level, the summit of Mount Everest in
  Nepal, is [`27.988056,86.925278,8848`].

### **Coordinates (latitude, longitude, altitude)** — Location information [`42.29971`, `-71.350719`, `69.29`] (default) | three-element numeric vector

Enter the location information as a three-element numeric vector of the form
[*latitude*, *longitude*,
*altitude*] to update the ThingSpeak channel.

#### Dependencies

- To enable this parameter, set **Coordinate source** to
  `Block dialog`.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Publish data to Internet of Things using ThingSpeak

The ThingSpeak Write block publishes input data from target hardware to the
Internet of Things (IoT) using ThingSpeak™.

ThingSpeak is an open Internet
of Things (IoT) platform with MATLAB® analytics that allows you to collect and store the sensor data in the cloud and
develop IoT applications. The ThingSpeak IoT platform provides applications that allow you to analyze and visualize your
data in MATLAB and then act on the data. For more information on how to use ThingSpeak, see ThingSpeak
Apps, Plugins, and Tutorials.
