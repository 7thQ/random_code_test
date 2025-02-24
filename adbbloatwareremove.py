import subprocess

# List of carrier, Samsung, and system bloatware
packages = [
    # Metro & T-Mobile Bloat
    "com.metropcs.metrozone",
    "com.tmobile.pr.adapt",
    "com.tmobile.dm.cm",
    "com.tmobile.dm.ms.services",
    "com.applovin.array.apphub.tmobile",
    "com.ironsrc.aura.tmo",

    # Samsung Bloat
    "com.samsung.android.app.spage",  # Samsung Free (Bixby)
    "com.samsung.android.lool",  # Device care bloat
    "com.samsung.android.bixby.agent",  # Bixby
    "com.samsung.android.bixbyvision.framework",
    "com.samsung.android.visionintelligence",
    "com.samsung.android.bixby.wakeup",
    "com.samsung.android.app.shealth",
    "com.samsung.android.tvplus",
    "com.samsung.android.mdm",
    "com.samsung.android.knox.containercore",
    "com.samsung.android.knox.analytics.uploader",
    "com.samsung.klmsagent",
    "com.sec.android.app.samsungapps",  # Samsung Store
    "com.samsung.android.smartmirroring",
    "com.samsung.android.smartsuggestions",
    "com.samsung.android.mdx.kit",
    "com.samsung.android.mdx",
    "com.samsung.android.widget.pictureframe",
    "com.samsung.android.rampart",
    "com.samsung.android.forest",
    "com.samsung.android.shortcutbackupservice",
    "com.samsung.android.smartcallprovider",
    "com.samsung.android.scloud",
    "com.samsung.android.mobileservice",
    "com.samsung.android.game.gos",
    "com.samsung.android.game.gamehome",
    "com.samsung.android.dialer",
    "com.samsung.android.calendar",
    "com.samsung.android.mtp",
    "com.samsung.android.bluelightfilter",
    "com.samsung.android.dynamiclock",
    "com.samsung.android.mdx.quickboard",
    "com.samsung.android.knox.containercore",
    "com.samsung.android.knox.attestation",
    "com.samsung.android.knox.kpecore",
    "com.samsung.knox.securefolder",
    "com.samsung.android.knox.analytics.uploader",
    "com.sec.android.diagmonagent",
    "com.samsung.android.service.peoplestripe",
    "com.samsung.android.smartmirroring",
    "com.sec.android.easyMover.Agent",  # Smart Switch
    "com.samsung.android.app.clipboardedge",
    "com.samsung.android.app.appsedge",
    "com.samsung.android.themecenter",
    "com.samsung.android.bbc.bbcagent",
    "com.samsung.android.app.watchmanagerstub",
    "com.samsung.android.app.dressroom",
    "com.samsung.android.stickercenter",
    "com.samsung.android.scs",
    "com.samsung.android.samsungpositioning",
    "com.samsung.safetyinformation",
    "com.samsung.android.mdx.kit",
    "com.samsung.android.app.updatecenter",
    "com.samsung.android.rubin.app",
    "com.samsung.android.beaconmanager",
    "com.samsung.sdm",
    "com.samsung.android.smartswitchassistant",
    "com.samsung.android.settingshelper",
    "com.samsung.internal.systemui.navbar.sec_gestural",
    "com.samsung.android.providers.trash",
    "com.samsung.android.mdx",
    "com.samsung.android.allshare.service.mediashare",
    "com.samsung.android.app.soundpicker",
    "com.samsung.android.honeyboard",

    # Other Random Crap
    "com.qualcomm.qti.smq",
    "com.sec.bcservice",
    "com.sec.android.app.factorykeystring",
    "com.sec.android.app.parser",
    "com.sec.android.app.personalization",
    "com.sec.android.app.voicenote",
    "com.sec.sprextension",
    "com.sec.modem.settings",
    "com.sec.android.app.kidshome",
    "com.sec.android.app.desktoplauncher",
    "com.sec.android.app.clockpackage",
    "com.sec.android.easyMover",
    "com.sec.android.app.soundalive",
    "com.sec.hiddenmenu",
    "com.sec.android.easyMover.Agent",
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
    "com.sec.enterprise.knox.cloudmdm.smdms",
    "com.sec.android.mhs.smarttethering",
    "com.sec.android.app.chromecustomizations",
    "com.sec.android.app.launcher",
    "com.sec.android.app.qsfastpairoverlay",
    "com.sec.android.app.quicktool",
    "com.sec.imsservice"
]

# Function to uninstall packages
def uninstall_package(package):
    command = f"adb shell pm uninstall --user 0 {package}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if "Success" in result.stdout:
        print(f"[✓] Successfully removed {package}")
    else:
        print(f"[✗] Failed to remove {package}: {result.stdout.strip()} {result.stderr.strip()}")

# Run uninstallation for each package
for package in packages:
    uninstall_package(package)
