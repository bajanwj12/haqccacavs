#！/bin/python3
"""
Buildozer动作
================

它设置一些环境变量，安装Buildozer，运行Buildozer并查找
输出文件。

您可以自上而下地读取此文件，因为函数是按其执行顺序排列的。
顺序。
"""

进口 os
进口子流程
进口sys
从……起os进口environ作为env


定义main()定义main()定义main()定义main()定义main()定义main()：
repository_root=os。路径.aspath(环境["INPUT_REPOSITORY_ROOT"])aspath(环境["INPUT_REPOSITORY_ROOT"])aspath(环境["INPUT_REPOSITORY_ROOT"])aspath(aspath(环境["INPUT_REPOSITORY_ROOT"])["INPUT_REPOSITORY_ROOT"])aspath(环境["INPUT_REPOSITORY_ROOT"])
变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者)(变更拥有者(变更拥有者)(变更拥有者(变更拥有者)(_O)(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R))(环境)["用户"]，存储库根目录(_R)
修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点(修复原点)修复原点(修复原点(修复原点)(_H)())())())())())())())())())())())())())())())()
install_buildozer(install_buildozer(install_buildozer(install_buildozer(install_buildozer(install_buildozer(install_buildozer(环境["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])["INPUT_Buildozer_VERSION"])
apply_buildozer_settings()
更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录(更改目录)(_D)(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"]))(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])
应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序(应用修补程序 (_P)())())())())())())())())())())())())())())())()
run_command(run_command(run_command(run_command(环境["INPUT_COMMAND"]))["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])(run_command(run_command(run_command(run_command(环境["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])["INPUT_COMMAND"])
set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(set_output(env["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])["INPUT_REPOSITORY_ROOT"]，env["INPUT_WORKDIR"])
变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(变更拥有者(_O)("根"，repository_root))("根"，存储库根目录(_R))("根"，存储库根目录(_R)))("根"，存储库根目录(_R)))("根"，存储库根目录(_R)))("根"，存储库根目录(_R))("根"，存储库根目录(_R)))("根"，存储库根目录(_R)))("根"，repository_root))("根"，存储库根目录(_R))("根"，存储库根目录(_R)))("根"，存储库根目录(_R)))("根"，存储库根目录(_R)))("根"，存储库根目录(_R))("根"，存储库根目录(_R)))("根"，存储库根目录(_R))


定义变更拥有者(定义变更拥有者(定义变更拥有者(定义变更拥有者(_O)(用户，存储库根目录)：)(用户，存储库根目录)：(定义变更拥有者(定义变更拥有者(定义变更拥有者(_O)(用户，存储库根目录)：)(用户，存储库根目录)：)(用户，存储库根目录)：)(用户，存储库根目录)：
#GitHub将根目录设置为存储库目录的所有者。将其更改为用户
#并在所有命令后返回到root
子流程。check_call(["sudo"，"chown"，"-R"，用户，存储库根])


定义修复原点(_H)()：
#GitHub将HOME设置为/GitHub/home，但Buildozer安装到/主页/用户。将主页更改为用户的主页
env["主页"]=env["HOME_DIR"]


定义安装Buildozer(Buildozer版本)(_V)：
#安装所需的Buildozer版本
打印("：：组：：安装Buildozer”)
PIP_install=[sys.可执行的]+"-m pip安装--用户--升级"".分离()
如果Buildozer_version=="稳定"：
#从PyPI安装稳定的Buildozer
子流程.check_call([*pip_install，"buildozer"])
Elif os.路径.存在(Buildozer_version)和操作系统。路径.存在(
操作系统。路径.参加(buildozer_version，"buildozer"，"__init__.py")
    ):
#从本地目录安装
子流程.check_call([*pip_install，buildozer_version])
Elif buildozer_version.startswith("git+")：
#从指定git+链接安装
子流程.check_call([*pip_install，buildozer_version])
Elif buildozer_version==""：
#什么都不做
打印(
"：：警告：：未安装Buildozer，原因是"
"指定的Buildozer_version为空。"
        )
其他:
#从资源库安装指定的ref
子流程.check_call(
            [
*pip_install，
F"git+https://github.com/kivy/buildozer.git@{Buildozer_version}"，
            ]
        )
打印(“：：endgroup：：”)


定义apply_buildozer_settings()：
#Buildozer设置禁用交互
env["Buildozer_WARN_ON_ROOT"]="0"
env["APP_ANDROID_ACCEPT_SDK_LICENSE"]="1"
#不允许更改目录
env["Buildozer_BUILD_DIR"]="./.buildozer"
env["Buildozer_BIN"]="./bin"


Def更改目录(_D)(repository_root，workdir)：
directory=os.路径.参加(repository_root，workdir)
#更改目录为workir
如果不os.path.存在(目录)：
打印("：：错误：：指定的工作目录不存在。" )
出口(1)
    os.chdir(directory)


def apply_patches():
    # Apply patches
    print("::group::Applying patches to Buildozer")
    try:
        import importlib
        import site

        importlib.reload(site)
        globals()["buildozer"] = importlib.import_module("buildozer")
    except ImportError:
        print(
            "::error::Cannot apply patches to buildozer (ImportError). "
            "Update buildozer-action to new version or create a Bug Request"
        )
        print("::endgroup::")
        return

    print("Changing global_buildozer_dir")
    source = open(buildozer.__file__, "r", encoding="utf-8").read()
    new_source = source.replace(
        """
    @property
    def global_buildozer_dir(self):
        return join(expanduser('~'), '.buildozer')
""",
        f"""
    @property
    def global_buildozer_dir(self):
        return '{env["GITHUB_WORKSPACE"]}/{env["INPUT_REPOSITORY_ROOT"]}/.buildozer_global'
""",
    )
    if new_source == source:
        print(
            "::warning::Cannot change global buildozer directory. "
            "Update buildozer-action to new version or create a Bug Request"
        )
    open(buildozer.__file__, "w", encoding="utf-8").write(new_source)
    print("::endgroup::")


def run_command(command):
    # Run command
    retcode = subprocess.check_call(command, shell=True)
    if retcode:
        print(f'::error::Error while executing command "{command}"')
        exit(1)


def set_output(repository_root, workdir):
    if not os.path.exists("bin"):
        print(
            "::error::Output directory does not exist. See Buildozer log for error"
        )
        exit(1)
    filename = [
        file
        for file in os.listdir("bin")
        if os.path.isfile(os.path.join("bin", file))
    ][0]
    path = os.path.normpath(
        os.path.join(repository_root, workdir, "bin", filename)
    )
    # Run with sudo to have access to GITHUB_OUTPUT file
    subprocess.check_call(
        [
            "sudo",
            "bash",
            "-c",
            f"echo 'filename={path}' >> {os.environ['GITHUB_OUTPUT']}",
        ]
    )


if __name__ == "__main__":
    main()
