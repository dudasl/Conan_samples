import sys
import codecs
import encodings

def get_encoding(file):
    byte_string = file.read(2)
    if byte_string.startswith(codecs.BOM_UTF16_LE):
        return 'utf_16_le'
    if byte_string.startswith(codecs.BOM_UTF16_BE):
        return 'utf_16_be'

    return 'ascii'

def set_build_number(file_path, build_version):
    # Read byte BOM and get propriate encoding
    encoding = None
    with open(file_path, "rb") as file:
        encoding = get_encoding(file)

    # Read all lines from version.txt
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        if encoding == 'utf_16_le' or encoding == 'utf_16_be':
            file.read(1)
        lines = file.readlines()

    # Modify version number
    for i in range(len(lines)):
        line = lines[i]
        if not line.startswith('version: '):
            continue
        
        version = line[9:]
        version_list = version.split('.')
        if len(version_list) < 4:
            continue

        major = int(version_list[0])
        minor = int(version_list[1])
        patch = int(version_list[2])

        line = 'version: ' + str(major) + '.' + str(minor) + '.' + str(patch) + '.' + str(build_version) + '\r\n'
        lines[i] = line

    # Write all lines to version.txt
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        if encoding == 'utf_16_le':
            file.write('\ufeff')
        elif encoding == 'utf_16_be':
            file.write('\ufeff')
        for line in lines:
            file.write(line)

if __name__ == "__main__":
   set_build_number(sys.argv[1], sys.argv[2])

