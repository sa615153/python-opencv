import os
import sys

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from shutil import copyfile
import subprocess


job_list = [x['name'] for x in jobs]
print job_list



for job_name in job_list:
    print "----------------------------{0}---------------------------------".format(job_name)

    copyfiles = 0
    cp = 0

    # create file dir
    os.makedirs(job_name)

    # write job config
    job_config = jenkins_server.get_job_config(job_name)
    with open("./{0}/{0}_job_config.xml".format(job_name), "w") as text_file:
        text_file.write(job_config)

    # # copy scripts
    job_config = jenkins_server.get_job_config(job_name)
    _element_tree = ET.fromstring(job_config)
    if _element_tree.find('1/2/3') is not None: # linux
        command = _element_tree.find('builders/hudson.tasks.Shell/command').text
        with open("./{0}/{0}_job_config_script.txt".format(job_name), "w") as text_file:
            text_file.write(command)

        cmd_list = command.split('\n')
        print cmd_list

        for  cmd in cmd_list:
            if len(cmd.strip()) == 0:
                continue
            cmd_components = cmd.split()
            print cmd_components[0]
            # print cmd_components[1]
            print '----------------------'
            if 'cp' in cmd_components[0]:
                cp = cp +1

                if 'cp' in cmd_components[0] and 'lbjfs' in cmd_components[1]:
                    # str = cmd_components[1].split('/')
                    str = cmd_components[1][10:]
                    str2 = str.replace('/','\\')
                    path = 'M:'+str2
                    retcode = subprocess.call('copy {0} .\\{1}'.format(path,job_name),shell=True)
                    if retcode == 0:
                        copyfiles  = copyfiles + 1
                elif 'cp' in cmd_components[0] and 'lbjfs' in cmd_components[2] and 'r' in cmd_components[1]:
                    str = cmd_components[2][10:]
                    str2 = str.replace('/','\\')
                    path = 'M:'+str2

                    dirs = str2.split('\\')
                    dir = dirs[-1]
                    retcode = subprocess.call('Xcopy  /E /I {0}  .\\{1}\\{2}'.format(path,job_name,dir),shell=True)
                    print '################'
                    print 'execute  {0}'.format('Xcopy  /E /I {0}  .\\{1}\\{2}'.format(path,job_name,dir))
                    print '################'
                    if retcode == 0:
                        copyfiles  = copyfiles + 1

    elif _element_tree.find('1/2/3') is not None: # windows
        command = _element_tree.find('builders/hudson.tasks.BatchFile/command').text
        with open("./{0}/{0}_job_config_script.txt".format(job_name), "w") as text_file:
            text_file.write(command)
        cmd_list = command.split('\n')
        print cmd_list

        for cmd in cmd_list:
            if len(cmd.strip()) == 0:
                continue
            cmd_components = cmd.split()
            print cmd_components[0]
            # print cmd_components[1]
            print '----------------------'
            if 'copy' in cmd_components[0]:
                cp = cp + 1

                if 'copy' in cmd_components[0]:
                    # str = cmd_components[1].split('/')
                    cmd = cmd_components[0] + ' '+cmd_components[1]+ ' .\\{0}'.format(job_name)
                    retcode = subprocess.call(cmd,shell=True)
                    print '################'
                    print 'execute  {0}'.format(cmd)
                    print '################'
                    if retcode == 0:
                        copyfiles = copyfiles + 1

    else: # unknown
        print "-------no win or linux---------"
        pass

    print 'cp = {0}'.format(cp)
    print 'copy files= {0}'.format(copyfiles)

    if cp != copyfiles:
        sys.exit('error: {0}'.format(job_name))

print len(job_list)