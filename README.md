# coop-app

Business app for coopbusinesses-cloud that automatically installs to Micro SD card.

### Feature
- Auto-install to Micro SD Card using `android:installLocation="preferExternal"`
- For Coop Businesses Cloud

### Requirements
- Android 6.0+
- Micro SD card inserted
- Fast SD card (Class 10 / A1 / A2 recommended)

### How it works
The app manifest has `preferExternal` so Android will try to install it to external storage first. If no SD card, it installs to internal.

### Build
Build APK with Android Studio or via GitHub Actions.

### Install
Download APK from Releases > Install on device with SD card.