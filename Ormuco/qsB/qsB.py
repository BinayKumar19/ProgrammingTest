# This function will receive 2 version numbers in string format, It will compare them and return the relation of first
# version number with the other
def versions_compare(version1_str, version2_str):
    version1 = float(version1_str)
    version2 = float(version2_str)

    if version1 < 0 or version2 < 0:
        result = "version number should be greater than 0"
    elif version1 > version2:
        result = "version " + version1_str + " is greater than version " + version2_str
    elif version1 < version2:
        result = "version " + version1_str + " is smaller than version " + version2_str
    else:
        result = "version " + version1_str + " is equals to version " + version2_str

    return result
