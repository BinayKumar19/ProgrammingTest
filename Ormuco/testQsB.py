import QsB as b


version1 = "3.0"
version2 = "3.1"
result = b.versions_compare(version1, version2)
print(result)

version1 = "2.0"
version2 = "2.0"
result = b.versions_compare(version1, version2)
print(result)

version1 = "0.5"
version2 = "0.3"
result = b.versions_compare(version1, version2)
print(result)

version1 = "0.0"
version2 = "3.0"
result = b.versions_compare(version1, version2)
print(result)

version1 = "-0.5"
version2 = "0.3"
result = b.versions_compare(version1, version2)
print(result)

