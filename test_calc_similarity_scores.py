from proj05 import calc_similarity_scores, num_in_common_between_lists

print("network: small_network_data.txt")
network=[[1, 2, 3], [0, 4, 6, 7, 9], [0, 3, 6, 8, 9], [0, 2, 8, 9], [1, 6, 7, 8], [9], [1, 2, 4, 8], [1, 4, 8], [2, 3, 4, 6, 7], [1, 2, 3, 5]]
instructor_matrix = [[3, 0, 1, 1, 1, 0, 2, 1, 2, 3], [0, 5, 3, 2, 2, 1, 1, 1, 3, 0], [1, 3, 5, 3, 2, 1, 1, 1, 2, 1], [1, 2, 3, 4, 1, 1, 2, 1, 1, 1], [1, 2, 2, 1, 4, 0, 2, 2, 2, 1], [0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [2, 1, 1, 2, 2, 0, 4, 3, 2, 2], [1, 1, 1, 1, 2, 0, 3, 3, 1, 1], [2, 3, 2, 1, 2, 0, 2, 1, 5, 2], [3, 0, 1, 1, 1, 0, 2, 1, 2, 4]]

similarity_matrix = calc_similarity_scores(network)
print("similarity matrix")
print(similarity_matrix)
print(20*"-")
print("similarity matrix printed nicely:")
for i, L in enumerate(similarity_matrix):
    print(i,":",L)
assert similarity_matrix == instructor_matrix
