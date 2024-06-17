def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)

    return data 
    

def read_file_into_list(file_name):
    data =  []
    with open(file_name, 'r') as file:
        for x in file:
            data.append(x)
            print(x)

    return data
    

def write_first_line_to_file(file_contents, output_filename):
    line = file_contents.split('\n')[0] 
    print(line)

    with open(output_filename, 'w') as file:
        file.write(line)



def read_even_numbered_lines(file_name):
    data =  []
    count = 1
    with open(file_name, 'r') as file:
        for x in file:
            if count % 2 == 0:
                data.append(x)
            count += 1
    
    return data

def read_file_in_reverse(file_name):
    data =  []
    with open(file_name, 'r') as file:
        for x in file:
            data.append(x)
    
    data.reverse()

    print(data)

    return data

def main():
    #file_contents = read_file("lorem.txt")
     #print(read_file_into_list("lorem.txt"))
     write_first_line_to_file("hello world we are very happy\nOur job is to make yours easier", "online.txt")
     #print(read_even_numbered_lines("sampletext.txt"))
     #print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
