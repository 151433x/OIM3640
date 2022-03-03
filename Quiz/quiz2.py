
f=open('Data/randomwords.txt')
line=f.readline
bword=['c','o','v','i','d']
count=0
sameletter=0
def badword():
    for line in f:
        for i in line:
            if i != 0:
                if line[0] == line[-1]:
                    print(line)
                    count+=1
            elif line[i] == line[-1]:
                print(line)
                count+=1
            if i == bword:
                sameletter+=1
                if sameletter >=3:
                    print(line)
                    count+=1
    return count
print(badword())