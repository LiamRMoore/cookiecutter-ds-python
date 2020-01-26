""" post_gen_project.py
    post-creation hooks to remove unnecessary files
"""
import os
import shutil
import warnings

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_aws_scripts = '{{cookiecutter.use_aws_ec2_instance}}' == 'y'

if not create_aws_scripts:
    # remove relative file nested inside the generated folder
    remove(os.path.join('{{cookiecutter.repo_name}}', 'bin', 'connect_to_aws'))
    remove(os.path.join('{{cookiecutter.repo_name}}', 'bin', 'connect_to_notebook'))
    remove(os.path.join('{{cookiecutter.repo_name}}', 'bin', 'update_ssh_config'))
else:
    # sanity check
    if not os.path.isfile('{{ cookiecutter.aws_ec2_ssh_key }}'):
        warnings.warn("SSH key not found at {{ cookiecutter.aws_ec2_ssh_key }}!")
    # remove absolute path to file nested inside the generated folder
    #remove(os.path.join(os.getcwd(), '{{cookiecutter.repo_name}}', 'file_one.py'))
