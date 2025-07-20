# kamerge

APK payload injector and Metasploit handler launcher

## Overview
`kamerge.py` is a command-line tool for injecting Metasploit payloads into Android APK files and automating the process of decoding, recompiling, signing, and installing APKs. It also helps launch Metasploit handlers for reverse connections.

## Features
- Inject Metasploit payloads into APKs using msfvenom
- Decode APKs (decompile)
- Recompile APKs (build)
- Sign APKs with a custom keystore
- Install APKs on connected Android devices
- View Java source using jadx
- Generate keystores
- Interactive menus for all operations

## Dependencies

### Python Requirements
- Python 3.x
- rich

Install Python requirements:
```sh
pip install rich
```

### External Tools
- apktool (latest version recommended)
- apksigner (comes with Android SDK build-tools)
- keytool (comes with Java)
- adb (Android Debug Bridge)
- msfvenom & msfconsole (Metasploit Framework)
- jadx (optional, for viewing Java source)
- Android SDK Build-tools (for aapt2)

#### How to install external tools:
- **apktool**: https://github.com/iBotPeaches/Apktool
- **apksigner, aapt2**: Included in Android SDK Build-tools (https://developer.android.com/studio#downloads)
- **keytool**: Included with Java (OpenJDK or Oracle JDK)
- **adb**: Included with Android SDK Platform-tools
- **msfvenom, msfconsole**: https://www.metasploit.com/
- **jadx**: https://github.com/skylot/jadx

Add build-tools directory to your PATH:
```sh
export PATH=$PATH:/path/to/android-sdk/build-tools/30.0.3/
```

## Usage
Run the tool:
```sh
python kamerge.py
```

### Main Menu
You will see options to:
1. Inject a Metasploit payload into an APK
2. Use APKToolManager (decompile, recompile, sign, install, etc)
3. More help
0. Exit

#### Inject Payload
- Enter your IP address, port, APK path, and output name.
- The tool will run msfvenom to inject the payload.
- You can optionally launch a Metasploit handler.
- You can then use APKToolManager to manage the APK (decode, build, sign, install, etc).

#### APKToolManager
- Enter the APK path to manage.
- Choose actions: decode, build, sign, install, full process, generate keystore, view Java source.
- The build step uses `--use-aapt2` for compatibility with modern APKs.

## Troubleshooting
If you encounter errors during the build step, such as:
```
W: aapt: brut.common.BrutException: Could not extract resource: /prebuilt/linux/aapt_64 (defaulting to $PATH binary)
W: First type is not attr!
brut.androlib.AndrolibException: brut.common.BrutException: could not exec (exit code = 134): [aapt, ...]
```
- Ensure you are using the official `aapt2` from Android SDK Build-tools.
- Add the build-tools directory to your PATH:
  ```sh
  export PATH=$PATH:/path/to/android-sdk/build-tools/30.0.3/
  ```
- Try different build-tools versions if needed.
- Use the `--use-aapt2` flag (already set in the tool).
- Make sure all binaries are executable.
- If the APK uses custom or obfuscated resources, apktool may not be able to recompile it.

## Example Workflow
1. Inject payload into APK.
2. Decode APK.
3. Edit smali files if needed.
4. Build APK (with `--use-aapt2`).
5. Sign APK.
6. Install APK on device.

## Credits
Author: [0xMohammedKAM]

---

# الترجمة العربية

## نظرة عامة
`kamerge.py` هو أداة سطر أوامر لحقن حمولة Metasploit في ملفات APK لنظام أندرويد وأتمتة عملية فك وتجميع وتوقيع وتثبيت ملفات APK. كما يساعد في تشغيل معالجات Metasploit للاتصالات العكسية.

## المتطلبات
- Python 3.x
- rich
- apktool (يفضل أحدث إصدار)
- apksigner
- keytool (يأتي مع جافا)
- adb
- msfvenom و msfconsole (Metasploit)
- jadx (اختياري)
- Android SDK Build-tools (لـ aapt2)

## طريقة الاستخدام
1. شغل الأداة:
   ```sh
   python kamerge.py
   ```
2. اتبع التعليمات في القائمة الرئيسية:
   - حقن حمولة في APK
   - إدارة APK (فك، تجميع، توقيع، تثبيت، إلخ)

## حل المشاكل
إذا ظهرت أخطاء أثناء التجميع، تأكد من استخدام aapt2 الرسمي من Android SDK، وأضف مسار build-tools إلى PATH، وجرب إصدارات مختلفة إذا لزم الأمر.

## مثال سير العمل
1. حقن الحمولة في APK
2. فك APK
3. تعديل ملفات smali إذا لزم الأمر
4. تجميع APK (مع --use-aapt2)
5. توقيع APK
6. تثبيت APK على الجهاز

## المؤلف
[محمد خالد]
