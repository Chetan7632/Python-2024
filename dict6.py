d={"om":"55.77","dada":"77.88","aman":"66.77","sai":"46"}
print("All keys:")
for val in d.keys():
    print(val)
print("All Sorted Ascending Keys:")
for val in sorted (d.keys()):
    print(val)
print("All Sorted Descending Keys:")
for val in sorted (d.keys(),reverse=True):
    print(val)
    
