<h1 align="center">
  <img align="top" width="44" src="https://raw.githubusercontent.com/udit-001/warp-linux-release/refs/heads/main/assets/warp.svg">
  <span>Warp AppImage Updater</span>
</h1>


<p align="center">
  <a href="https://github.com/udit-001/warp-linux-release/releases/latest" target="_blank"><img alt="release" src="https://img.shields.io/github/v/release/udit-001/warp-linux-release?label=release&labelColor=%231e1e2e&color=%234fa048"></a>
  <span> </span>
  <a href="https://github.com/udit-001/warp-linux-release/actions/workflows/release.yml" target="_blank"><img alt="downloads" src="https://img.shields.io/github/actions/workflow/status/udit-001/warp-linux-release/release.yml?branch=main&labelColor=%231e1e2e&color=%234fa048"></a>
  <span> </span>
</p>

## Overview

GitHub Action to fetch the latest **Warp** Linux AppImage and create a release.

## Why?

Cursor on Linux:
- ❌ Doesn’t auto-update
- ❌ Isn’t hosted at a fixed URL
- ✅ Has an API with the latest version info

This makes it hard for Linux users to keep Warp up to date & this action solves that by:
- Querying Warp’s API for the latest version
- Checking if that version already exists as a GitHub release
- If not, downloading the AppImage and publishing a release

Linux users can then update via GitHub releases, scripts, or package managers using a consistent URL.

## Setup Auto Updates with Gear Lever

To automate updates for your Warp AppImage on Linux, use [Gear Lever](https://github.com/mijorus/gearlever). It supports update sources like GitHub releases and static URLs. Configure the update URL based on your system architecture:

- **x86_64**
  ```
  https://github.com/udit-001/warp-linux-release/releases/download/*/Warp-*-x86_64.AppImage
  ```

- **ARM64**
  ```
  https://github.com/udit-001/warp-linux-release/releases/download/*/Warp-*-aarch64.AppImage
  ```


These URLs will allow automatic fetching of the latest releases. For more detailed instructions, refer to the [update guide](https://mijorus.it/posts/gearlever/update-url-info/).


## 📅 Release Status
- **⏳ Last Released On**: 2025-10-27 01:38:31 UTC
- **🔄 Last Run**: 2025-10-27 01:38:31 UTC
