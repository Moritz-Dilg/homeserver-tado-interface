# Homeserver Tado Interface

This logic node for the Gira Homeserver and Facilityserver enables you to control Tado Smart Thermostats. 

## Overview

The Homeserver Tado Interface provides the functionality to read the *target temperatur*, *actual temperature* and *humidity* of Thermostats in up to 20 zones. Additionally you can set new target temperatures.

Unfortunately, Tado does not provide an official API documentation and does not guarantee any backward compatability in the event of an change of their API. This means, that this logic node can suddenly stop working, if Tado decides to change their API.

## Installation and Usage

### Use the precompiled logic node

In this github repository you can find all published releases. It is recommended to always use the latest version. \
If you want to update your already installed logic node, just import it again.

### Compile it yourself

In order to compile a logic node yourself you need the `hsl2` SDK and Framework from Gira. It can be found on Giras [developer website](https://partner.gira.com/en/service/software-tools/developer.html) under `Gira HomeServer Logic 2.0`.

In order to compile a logic node yourself you first need to add the project in the `/HSL/HSL2 SDK 2.0.7/framework/projects/` directory. Then, run the compilation script with **pyhton 2.7**:
```sh
pyhton2 /HSL/HSL2 SDK 2.0.7/framework/generator.pyc [project_name]
```
Where `[project_name]` is the folder name of your project inside the `projects` directory.

### Usage

To use the logic node, import the compiled or downloaded `.hsl` file by clicking `File` -> `Import` -> `Logic node` in the menu of the HS Expert. After restarting the Expert, you can use it like any other logic node.

## Error codes

| Code           | Reason                                                    |
|----------------|-----------------------------------------------------------|
| I-00           | Internal Exception                                        |
| I-01: [reason] | Unknown Exception - a Reason is stated after the code     |
| E-11           | No Credentials provided                                   |
| I-12           | Authentication Exception: User could not be authenticated |
| E-13           | Unauthorized Request: Incorrect Credentials               |
| I-21           | Zone States could not be retrieved                        |
| I-22           | User Information could not be retrieved                   |
| I-23           | Zone Names could not be retrieved                         |
| I-24           | Error setting Zone Temperature                            |