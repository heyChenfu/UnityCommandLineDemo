using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

public class PythonTest
{

    [MenuItem("打包工具/打包")]
    public static void ShellBuild()
    {
        Debug.Log("调用C# ShellBuild()");
        BuildPlayerOptions buildOption = new BuildPlayerOptions();
        buildOption.target = BuildTarget.StandaloneWindows;
        buildOption.targetGroup = BuildTargetGroup.Standalone;
        buildOption.locationPathName = Path.Combine(Path.Combine(Application.dataPath, "../Build/Android"), "PythonTest.exe");
        buildOption.scenes = new List<EditorBuildSettingsScene>(EditorBuildSettings.scenes)
            .FindAll(x => x.enabled)
            .ConvertAll(x => x.path)
            .FindAll(x => !string.IsNullOrEmpty(x))
            .ToArray();
        buildOption.options = BuildOptions.AllowDebugging;
        BuildPipeline.BuildPlayer(buildOption);

    }

    public static void ShellTest()
    {
        Debug.Log("调用C# ShellTest()");

    }

    public static void ShellTest1()
    {
        Debug.Log("调用C# ShellTest1()");
    }

}
