# qsB.py
# Binay Kumar
# May 12, 2019

"""
==========
qsB
==========
This module contains functions to compare 2 version numbers received in a string format

Contents
--------
* versions_compare()  - This function will compare the 2 version numbers

"""


def versions_compare(version1_str, version2_str):
    """
    Returns: the relation of first version number with the second version number
    ===========
    Description
    ===========
    This function will receive 2 version numbers in string format and compare them
    """
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


if __name__ == '__main__':
    # compare two positive version numbers (second version number is greater than the first version number)
    version1 = "3.0"
    version2 = "3.1"
    result = versions_compare(version1, version2)
    print(result)

    # compare two equal positive version numbers
    version1 = "2.0"
    version2 = "2.0"
    result = versions_compare(version1, version2)
    print(result)

    # compare two positive version numbers (first version number is greater than the second version number)
    version1 = "0.5"
    version2 = "0.3"
    result = versions_compare(version1, version2)
    print(result)

    # compare two positive version numbers (first version number is 0.0 and second version number is a positive)
    version1 = "0.0"
    version2 = "3.0"
    result = versions_compare(version1, version2)
    print(result)

    # compare two version numbers (first version number is negative and second version number is positive )
    version1 = "-0.5"
    version2 = "0.3"
    result = versions_compare(version1, version2)
    print(result)
