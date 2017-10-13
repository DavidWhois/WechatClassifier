def readdata(filename,username):
    data = []
    with open(filename) as input:
        for each_line in input:
            if each_line.startswith(username):
                print('-',end='')
            elif each_line=='\n':
                print('-',end='')
            elif each_line.startswith('—————'):
                print('-',end='')
            else:
                data.append(each_line)
    '''每5行一组，成为一个例子'''
    data1 = []
    #print(data[2])
    element=''
    for i in range(len(data)):
        #print(data[i])
        element=(element+data[i])
        if (i+1)%5==0:
            data1.append(element)
            element=''
    #print(data1)
    return data1
