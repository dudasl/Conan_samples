import sys

def set_build_number(file_path, build_version):
    # Read all lines from version.txt
    file = open(file_path, 'r') 
    lines = file.readlines()  
    file.close()

    # Modify version number
    for i in range(len(lines)):
        line = lines[i]
        if not line.startswith('version: '):
            continue
        
        version = line[9:]
        version_list = version.split('.')
        if len(version_list) != 4:
            continue

        major = int(version_list[0])
        minor = int(version_list[1])
        patch = int(version_list[2])

        line = 'version: ' + str(major) + '.' + str(minor) + '.' + str(patch) + '.' + str(build_version)
        lines[i] = line

    # Write all lines to version.txt
    file = open(file_path, 'w') 
    file.writelines(lines)
    file.close()

if __name__ == "__main__":
   set_build_number(sys.argv[1], sys.argv[2])

