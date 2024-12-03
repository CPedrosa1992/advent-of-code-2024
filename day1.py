def read_text_file(filename):
    with open(filename, "r") as file:
        return file.read()


def process_input(input_text):

    values = [int(x) for x in input_text.split()]
    list1 = sorted(values[i] for i in range(len(values)) if i % 2 == 0)
    list2 = sorted(values[i] for i in range(len(values)) if i % 2 != 0)
    return list1, list2

def calculate_distances(list1, list2):

    distances = [b - a for a, b in zip(list1, list2)]
    total_distance = sum(abs(d) for d in distances)
    return distances, total_distance

#part2
def calculate_similarity(list1, list2):
    similarity = 0
    for num in list1:
        similarity += num * list2.count(num)
    return similarity
    

    

if __name__ == "__main__":
    input_text = read_text_file("inputday1.txt")

    list1, list2 = process_input(input_text)
    
    distances, total_distance = calculate_distances(list1, list2)
    similarity = calculate_similarity(list1, list2)
    # print(f"List 1: {list1}")
    # print(f"List 2: {list2}")
    # print(f"Distances: {distances}")
    print(f"Total Distance: {total_distance}")
    print(f"Total Similarity: {similarity}")
