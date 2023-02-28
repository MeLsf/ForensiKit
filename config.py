import os 

is_x64 = True if os.environ.get('PROGRAMFILES(X86)') else False
tools_main_dir = os.path.join(os.path.dirname(__file__), 'tools', 'x64' if is_x64 else 'x32')

output_main_dir = "C:\\Briefer\\CollectedData"
nirsoft_tools_dir = os.path.join(tools_main_dir, "Nirsoft")

basic_info_dir = os.path.join(output_main_dir, "BasicInfo")
network_info_dir = os.path.join(output_main_dir, "NetworkInfo")
persistence_info_dir = os.path.join(output_main_dir, "Persistence")
user_info_dir = os.path.join(output_main_dir, "UserInfo")


