import os
from subprocess import run
from config import nirsoft_tools_dir, basic_info_dir,network_info_dir, user_info_dir, persistence_info_dir, output_main_dir

nirsoft_utilities = [
    [os.path.join(nirsoft_tools_dir, "RegDllView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_regdllview.html")],
    [os.path.join(nirsoft_tools_dir, "AppCompatibilityView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_appcompatview.html")],
    [os.path.join(nirsoft_tools_dir, "AppCrashView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_appcrashview.html")],
    [os.path.join(nirsoft_tools_dir, "cports.exe"),"/shtml", os.path.join(network_info_dir, "Nirs_cports.html")],
    [os.path.join(nirsoft_tools_dir, "DriverView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_driverview.html")],
    [os.path.join(nirsoft_tools_dir, "ExecutedProgramsList.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_executedprogslist.html")],
    [os.path.join(nirsoft_tools_dir, "InjectedDLL.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_injecteddll.html")],
    [os.path.join(nirsoft_tools_dir, "InstalledPackagesView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_installedpackagesview.html")],
    [os.path.join(nirsoft_tools_dir, "JumpListsView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_jumplistsview.html")],
    [os.path.join(nirsoft_tools_dir, "LastActivityView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_LastActivityView.html")],
    [os.path.join(nirsoft_tools_dir, "LoadedDllsView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_loadeddllsview.html")],
    [os.path.join(nirsoft_tools_dir, "RecentFilesView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_recentfilesview.html")],
    [os.path.join(nirsoft_tools_dir, "ShellBagsView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_shellbagsview.html")],
    [os.path.join(nirsoft_tools_dir, "SimpleWMIView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_simplewmiview.html")],
    [os.path.join(nirsoft_tools_dir, "TaskSchedulerView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_taskschedulerview.html")],
    [os.path.join(nirsoft_tools_dir, "UserAssistView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_userassistview.html")],
    [os.path.join(nirsoft_tools_dir, "UserProfilesView.exe"),"/shtml", os.path.join(user_info_dir, "Nirs_userprofilesview.html")],
    [os.path.join(nirsoft_tools_dir, "WinUpdatesView.exe"),"/shtml", os.path.join(basic_info_dir, "Nirs_winupdatesview.html")]  
]



def nirsoft_collector():
    # Check if the output directory exists
    if not os.path.exists(output_main_dir):
        print(f"ERROR: {output_main_dir} does not exist. Exiting.")
    print("\n======\n:-Begin Nirsoft module\n======\n")
    for util in nirsoft_utilities:
        try:
            print(f"Success: {util[0]} executed succesfully.")
            run(util)
        except Exception as e:
            print(f"Error: {e}")
    print("\n======\n:-End Nirsoft module\n======\n")