import sys
import codecs
import os

def get_encoding(file):
    byte_string = file.read(2)
    if byte_string.startswith(codecs.BOM_UTF16_LE):
        return 'utf_16_le'
    if byte_string.startswith(codecs.BOM_UTF16_BE):
        return 'utf_16_be'

    return 'ascii'

def modify_line(line, find_str, build_version, delimiter='.', version_encloser=None):
    start = line.find(find_str)
    if start == -1:
        return None
        
    version = line[start + len(find_str):]
    if version_encloser != None:
        version_start = version.find(version_encloser)
        if (version_start == -1):
            return None;
        version_end = version.find(version_encloser, version_start + 1)
        if (version_end == -1):
            return None;
        version = version[version_start + 1:version_end]

    version_list = version.split(delimiter)
    if len(version_list) != 4:
        return None

    major = int(version_list[0])
    minor = int(version_list[1])
    patch = int(version_list[2])

    line = line[:start] + find_str + ' '
    if (version_encloser != None):
        line += version_encloser
    line += str(major) + delimiter + str(minor) + delimiter + str(patch) + delimiter + str(build_version)
    if (version_encloser != None):
        line += version_encloser
    line += '\r\n'
    return line

def set_txt_build_number(file_path, build_version):
    # Read byte BOM and get propriate encoding
    encoding = None
    with open(file_path, "rb") as file:
        encoding = get_encoding(file)

    # Read all lines from from txt file
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        if encoding == 'utf_16_le' or encoding == 'utf_16_be':
            file.read(1)
        lines = file.readlines()

    # Modify version number
    for i in range(len(lines)):
        line = modify_line(lines[i], 'version:', build_version)
        if line != None:
            lines[i] = line

    # Write all lines back to txt file
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        if encoding == 'utf_16_le':
            file.write('\ufeff')
        elif encoding == 'utf_16_be':
            file.write('\ufeff')
        for line in lines:
            file.write(line)

def set_rc_build_number(file_path, build_version):
    # Read byte BOM and get propriate encoding
    encoding = None
    with open(file_path, "rb") as file:
        encoding = get_encoding(file)

    # Read all lines from from rc file
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        if encoding == 'utf_16_le' or encoding == 'utf_16_be':
            file.read(1)
        lines = file.readlines()

    # Modify version number
    for i in range(len(lines)):
        line = modify_line(lines[i], 'FILEVERSION', build_version, ',')
        if line == None:
            line = modify_line(lines[i], 'PRODUCTVERSION', build_version, ',')
        if line == None:
            line = modify_line(lines[i], 'VALUE "FileVersion",', build_version, '.', '"')
        if line == None:
            line = modify_line(lines[i], 'VALUE "ProductVersion",', build_version, '.', '"')
        if line != None:
            lines[i] = line

    # Write all lines back to rc file
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        if encoding == 'utf_16_le':
            file.write('\ufeff')
        elif encoding == 'utf_16_be':
            file.write('\ufeff')
        for line in lines:
            file.write(line)

if __name__ == "__main__":
    split_path = os.path.splitext(sys.argv[1])
    if split_path[1].lower() == '.txt':
        set_txt_build_number(sys.argv[1], sys.argv[2])
    elif split_path[1].lower() == '.rc':
        set_rc_build_number(sys.argv[1], sys.argv[2])
    else:
        print('Extension of the file should be .txt or .rc')


