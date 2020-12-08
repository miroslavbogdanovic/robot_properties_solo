import importlib.resources
import glob
import sys
from os import path, walk, mkdir, access, X_OK, environ, pathsep
import subprocess

def find_path(robot_family, robot_name):
    with importlib.resources.path(__package__, "utils.py") as p:
            package_dir = p.parent.absolute()
    
    resources_dir = package_dir/"resources"
    yaml_path = resources_dir/"dynamic_graph_manager"/("dgm_parameters_" + robot_name + ".yaml")
    urdf_path = resources_dir/(robot_name + ".urdf")
    
    if not urdf_path.exists():
        build_xacro_files(resources_dir)

    resources_dir = str(resources_dir)
    yaml_path = str(yaml_path)
    urdf_path = str(urdf_path)

    return resources_dir, yaml_path, urdf_path


def which(program):
    """ Find program. """

    def is_exe(fpath):
        return path.isfile(fpath) and access(fpath, X_OK)

    fpath, _ = path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for env_path in environ["PATH"].split(pathsep):
            exe_file = path.join(env_path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def build_xacro_files(resources_dir):
    """ Look for the xacro files and build them in the build folder. """

    build_folder = resources_dir
    xacro_files = []
    for (root, _, files) in walk(path.join(resources_dir, "xacro")):
        for afile in files:
            if afile.endswith(".urdf.xacro"):
                xacro_files.append(path.join(root, afile))

    if not path.exists(build_folder):
        mkdir(build_folder)

    for xacro_file in xacro_files:
        if which("xacro") is not None:
            for xacro_file in xacro_files:
                # Generated file name
                generated_urdf_path = path.join(
                    build_folder, path.basename(path.splitext(xacro_file)[0])
                )
                # Call xacro.
                bash_command = ["xacro", xacro_file, "-o", generated_urdf_path]
                process = subprocess.Popen(bash_command, stdout=subprocess.PIPE)
                process.communicate()


        