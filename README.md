# Eve Online Alert

## FORK INFORMATION

### This repo is forked specifically to provide solution, tested and worked on MacOS Tahoe 26.0.1 (test date: 6 July 2026). 

## Running EVE Alert on macOS

This guide explains how to run EVE Alert from source on macOS.

## Requirements

- macOS
- Python 3.10, 3.11, or 3.12
- Git

Python 3.13+ is not currently declared as supported by this project.

## Install

Clone the repository:

```sh
git clone https://github.com/georgethegreatat/EVE-Alert.git
cd EVE-Alert
```

Create and activate a virtual environment (yes, you need pre-install python12):

```sh
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the app:

```sh
python -m pip install -U pip
python -m pip install -e .
```

Run EVE Alert:

```sh
eve-alert
```

You can also run it with:

```sh
python -m evealert
```

## macOS Permissions

EVE Alert needs macOS privacy permissions for screen capture, mouse/keyboard input, and hotkeys.

Open:

```text
System Settings > Privacy & Security
```

Enable permissions for your terminal app, for example Terminal, iTerm2, or Warp:

- Screen Recording
- Accessibility
- Input Monitoring

After changing permissions, restart the terminal and run EVE Alert again.

## First Run

1. Start the app with `eve-alert`.
2. Open `Config Mode`.
3. Use the configured hotkeys to select alert and faction regions.
4. Save settings.
5. Press `Start Script`.

If the app says the settings are invalid, configure the alert and faction regions first.

## Troubleshooting

### `source: no such file or directory: .venv/bin/activate`

The virtual environment was not created successfully. Re-run:

```sh
python3.12 -m venv .venv
```

Only run `source .venv/bin/activate` after the venv command succeeds.

### `ensurepip` or `pyexpat` error when creating the venv

This is usually a local Homebrew Python issue, not an EVE Alert issue.

Try reinstalling Python:

```sh
brew reinstall python@3.12
```

Then recreate the virtual environment:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

### Keyboard warning: process is not trusted

If you see a warning like:

```text
This process is not trusted! Input event monitoring will not be possible
```

enable `Accessibility` and `Input Monitoring` permissions for your terminal app.

## Settings and Logs

On macOS, settings and logs are stored in:

```text
~/Library/Application Support/EVE Alert/
```


---

![Release](https://img.shields.io/github/v/release/Geuthur/EVE-Alert)
![Licence](https://img.shields.io/github/license/geuthur/EVE-Alert)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Geuthur/EVE-Alert-Opensource/main.svg)](https://results.pre-commit.ci/latest/github/Geuthur/EVE-Alert-Opensource/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python package](https://github.com/Geuthur/EVE-Alert-Opensource/actions/workflows/python-package.yml/badge.svg)](https://github.com/Geuthur/EVE-Alert-Opensource/actions/workflows/python-package.yml)
[![GitHub Downloads](https://img.shields.io/github/downloads/Geuthur/EVE-Alert-Opensource/total)](https://tooomm.github.io/github-release-stats/?username=Geuthur&repository=EVE-Alert-Opensource)
[![codecov](https://codecov.io/gh/Geuthur/EVE-Alert/graph/badge.svg?token=7PQ6WLXDOP)](https://codecov.io/gh/Geuthur/EVE-Alert)
[![Discord](https://img.shields.io/discord/337275567487320064?label=discord)](https://discord.gg/WrHzA4rnxA)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W810Q5J4)

EVE Alert - Check every 1-3 seconds if the Local has an Enemy or Neutral in System and play a sound if someone is there!

- [EVE Alert](#evealert)
  - [Features](#features)
  - [Download](#step1)
  - [Detection](#detection)
  - [Discord Webhook](#webhook)
  - [Showcase](#showcase)
  - [Donation](#donation)
  - [Terms](#terms)
  - [Contributing](#contributing)

## Features<a name="features"></a>

- Play Sound on Local Detection
- Easy-Use Interface
- Start/Stop System
- Monitoring Region in real-time (also possible to stream via Discord for friends)
- Faction Spawn Detection - Now you can set a Faction Spawn Detection and it will play a sound if a faction is in Site (can also used for other thing like active modules or something)
- Webhook System allows to share alarms into Discord Webhook to create a Intel System anonymous.

## Download Version<a name="step1"></a>

Go to [the releases page](https://github.com/Geuthur/EVE-Alert-Opensource/releases) to download the latest version.

## Requirements & instructions for use

- Alert/Faction Region not working correctly
  The Application only works with 100% Scaling this means your Monitor Scaling need to be 100% this can be changed in the "Display Settings"
- Issues with Sound
  Please check if you have a Sound Device installed.

### macOS

Use Python 3.10, 3.11, or 3.12. Python 3.13+ is not declared as supported by this project yet.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
eve-alert
```

On first run, macOS may ask for privacy permissions. Enable permissions for the terminal app or packaged EVE Alert app in:

- System Settings > Privacy & Security > Screen Recording
- System Settings > Privacy & Security > Accessibility
- System Settings > Privacy & Security > Input Monitoring

Settings and logs are stored in `~/Library/Application Support/EVE Alert/`.

## Detection<a name="detection"></a>

- Neutral: ![Neutral](https://i.imgur.com/SdjoIs6.png)
- Enemys: ![Red](https://i.imgur.com/O0VTT69.png)

If you want more, simply add more images to the "img/" folder with naming image_1, image_2, image_3, etc.\
Note: If you have different UI Scaling you need to add these images to the img folder like the `image_1_90%`

## Discord Webhook Usage (optinal)<a name="webhook"></a>

The webhook is responsible for sending messages to a Discord Server.

- Open The Setting Menu and put a Discord Webhook URL in the Webhook Field
- Setup a System Name: `Jita 4-4`
- You can also mute the Alarm sound by checking the Mute Alarm Checkbox

If there is a problem with the webhook, the webhook system is automatically deactivated.

## Showcase<a name="showcase"></a>

https://github.com/user-attachments/assets/89727863-538d-4846-b861-0d693a75a688

## Donation<a name="donation"></a>

I know it is simple Script, but if you want to support me here:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W810Q5J4)

## Terms<a name="terms"></a>

> [!CAUTION]
> This is an open-source project without any guarantees. Use it at your own risk.
> Please ensure that you comply with EVE Online's terms of use and policies. The use of bots or automation may violate the game's terms of service.

## Contributing<a name="contributing"></a>

Contributions are welcome! If you would like to contribute to this project and optimize the code, follow these steps:

1. Fork the repository by clicking on the "Fork" button at the top right corner of this page.
1. Clone your forked repository to your local machine.
1. Make the necessary changes and improvements to the code.
1. Commit your changes and push them to your forked repository.
1. Submit a pull request by clicking on the "New pull request" button on the original repository's page.

Please ensure that your contributions adhere to the following guidelines:

- Follow the existing code style and conventions.
- Clearly describe the changes you have made in your pull request.
- Test your changes thoroughly before submitting the pull request.

By contributing to this project, you agree to release your contributions under the MIT License.
