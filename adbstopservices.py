import subprocess

# List of packages to disable
packages = [
    "com.samsung.android.knox.containercore",
    "com.samsung.android.knox.analytics.uploader",
    "com.samsung.klmsagent",
    "com.sec.enterprise.knox.cloudmdm.smdms",
    "com.sec.android.app.samsungapps",
    "com.samsung.android.smartmirroring",
    "com.samsung.android.scloud",
    "com.samsung.android.service.peoplestripe",
    "com.sec.android.easyMover.Agent",
    "com.samsung.android.themecenter",
    "com.samsung.android.mdx.kit",
    "com.samsung.android.rubin.app",
    "com.samsung.android.beaconmanager",
    "com.samsung.sdm",
    "com.samsung.android.smartswitchassistant",
    "com.samsung.android.settingshelper",
    "com.samsung.internal.systemui.navbar.sec_gestural",
    "com.samsung.android.providers.trash",
    "com.samsung.android.app.soundpicker",
    "com.sec.android.easyMover",
    "com.sec.android.app.soundalive",
    "com.sec.hiddenmenu",
    "com.sec.android.dexsystemui",
    "com.sec.android.emergencylauncher",
    "com.sec.android.smartfpsadjuster",
    "com.sec.sve",
    "com.sec.usbsettings",
    "com.sec.automation",
    "com.sec.phone",
    "com.sec.android.gallery3d",
    "com.sec.android.mimage.photoretouching",
    "com.sec.android.provider.badge",
    "com.sec.imslogger",
    "com.sec.android.soagent",
    "com.sec.android.app.myfiles",
    "com.sec.android.desktopmode.uiservice",
    "com.sec.android.app.chromecustomizations",
    "com.sec.android.app.qsfastpairoverlay",
    "com.sec.android.app.quicktool",
    "com.sec.imsservice"
]

# Function to disable packages
def disable_package(package):
    command = f"adb shell pm disable-user --user 0 {package}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if "new state: disabled" in result.stdout:
        print(f"[✓] Successfully disabled {package}")
    else:
        print(f"[✗] Failed to disable {package}: {result.stdout.strip()} {result.stderr.strip()}")

# Run disable command for each package
for package in packages:
    disable_package(package)
