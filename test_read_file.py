from proj05 import read_file
instructor_net = [[1, 2, 3], [0, 4, 6, 7, 9], [0, 3, 6, 8, 9], [0, 2, 8, 9], [1, 6, 7, 8], [9], [1, 2, 4, 8], [1, 4, 8], [2, 3, 4, 6, 7], [1, 2, 3, 5]]
print(instructor_net)

fp = open("small_network_data.txt")
network = read_file(fp)
print("network:")
print(network)
print(20*"-")
print("network printed nicely:")
for i, L in enumerate(network):
    print(i,":",L)
assert network == instructor_net
