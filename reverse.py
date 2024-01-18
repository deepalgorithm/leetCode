def reverse(word_list):
    file = open('ilsan_test_lane_4.txt', 'w')
    word_list = word_list[::-1]
    res = " ".join(word_list)
    file.write(res)
    print(res)
    file.close()
    
def read_file(src_file):
    file = open(src_file,"r", encoding='UTF8')
    content = file.read()
    coordinate_list = content.split('\n')
    return coordinate_list

    
coordinate_list = read_file("path_ilsan_1.txt")
reverse(coordinate_list)