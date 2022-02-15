import subprocess
import os

CONFIG_UNITY_PATH = r'F:/Unity/Editor/Unity'

def get_project_dir() :
    if get_project_dir.path is None :
        print(f'__file__:{__file__}！')
        script_dir = os.path.realpath(__file__)
        print(f'script_dir:{get_project_dir.path}！')
        get_project_dir.path = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
        print(f'get_project_dir.path:{get_project_dir.path}！')
    return get_project_dir.path
get_project_dir.path = None

def get_output_info_path() :
    proj_dir = get_project_dir()
    return os.path.join(proj_dir, f"output.txt")

def run_text():
    #-logFile <pathname>|指定 Unity 写入 Editor 或 Windows/Linux/OSX 独立日志文件的位置。要输出到控制台，请为路径名指定 -。
    # 在 Windows 上，指定 - 选项将使输出进入 stdout，这在默认情况下不是控制台
	cmd = [
		CONFIG_UNITY_PATH,
        "-batchmode",
		"-logFile", get_output_info_path(),
		"-projectPath", get_project_dir(), 
		"-executeMethod", "PythonTest.ShellBuild",
		"-quit"
	]
	assert subprocess.call(cmd) == 0, "Unity 执行失败！"
	#subprocess.run(cmd, check = True)

	print("执行完毕")

if __name__ == "__main__":
    run_text()
    pass