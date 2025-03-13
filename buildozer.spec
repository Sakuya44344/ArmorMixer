[app]

title = ArmorMixer
package.name = armormixer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android specific
android.api = 29
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE

# Path SDK & NDK agar diunduh otomatis oleh Buildozer
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r23b
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
