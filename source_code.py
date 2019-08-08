def sort_by_month(filename,Month):
    """ filename(str),Month(int) --> make csv file sorted by month with name, 'filename+month'"""
    import csv
    content_list = []
    with open(filename+'.csv','r',encoding = 'utf-8') as file:
        contents = file.readline()
        header_list = (contents.strip('\n')).strip('\ufeff').split(',')
        contents = file.readline()
        while contents != '':
            contents = contents.strip('\n').split(',')
            month = int(contents[0])%100
            if month == Month:
                content_list.append(contents)
            contents = file.readline()
    with open(filename+str(Month)+'월.csv','w',newline = '') as file:
        mywriter = csv.writer(file)
        mywriter.writerow(header_list)
        for i in range(len(content_list)):
            mywriter.writerow(content_list[i])


def sort_by_address(filename):
    with open(filename+'.csv','r') as file:
        contents = file.readline()
        contents = file.readlines()
        in_address = []
        for i in contents:
            i = i.strip('\n').split(',')
            for x in range(10):
                if str(x) in i[2]:
                    i[2] = i[2].replace(str(x),'')
            in_address.append(i)
        return in_address


def ranking_by_address_in_ascending_order(filename):
    """get sum by address """
    in_address = sort_by_address(filename) #[['201808',1744',희우정로길','5955','69941'],['201808','1743','휘경로길','10483',143839']]
    address_dict = {}
    for i in in_address:
        if i[2] not in address_dict:
            address_dict[i[2]] = int(i[-1])
        else:
            address_dict[i[2]] += int(i[-1]) #주소별로 데이터합산 후 딕셔너리 형태로 저장
            
    address_dict_items = sorted(address_dict.items()) #데이터정렬후 튜플 in 리스트로 저장
    y = []
    for i in address_dict_items:
        y.append(list(i)) #튜플 in 리스트 형태를 리스트 in 리스트 형태로 변환
    for i in range(len(y)):
        k = y[i][0]
        y[i][0] = y[i][1]
        y[i][1] = k #리스트 안에 있는 리스트의 순서를 바꿈 (ex. [행당로,3] -> [3,행당로])
    rank = []
    count = 0
    for i in range(len(y)):
        s = 0
        x = y[i][0]
        for j in range(len(y)):
            z = y[j][0]
            if x>z:
                s += 1
        rank.append([y[i][1],s+1])
        count += 1
        if count == len(y):
            break #같은 크기의 데이터에 대해 같은 순위를 부여한다
    result_list = []
    for i in range(len(rank)):
        result_list.append([str(rank[i][1])+'위',rank[i][0]])
    return result_list


def ranking_by_address_in_descending_order(filename):
    """get sum by address """
    in_address = sort_by_address(filename)
    address_dict = {}
    for i in in_address:
        if i[2] not in address_dict:
            address_dict[i[2]] = int(i[-1])
        else:
            address_dict[i[2]] += int(i[-1])
    address_dict_items = sorted(address_dict.items())
    y = []
    for i in address_dict_items:
        y.append(list(i))
    for i in range(len(y)):
        k = y[i][0]
        y[i][0] = y[i][1]
        y[i][1] = k
    rank = []
    count = 0
    for i in range(len(y)):
        s = 0
        x = y[i][0]
        for j in range(len(y)):
            z = y[j][0]
            if x<z:
                s += 1
        rank.append([y[i][1],s+1])
        count += 1
        if count == len(y):
            break #같은 크기의 데이터에 대해 같은 순위를 부여한다
    result_list = []
    for i in range(len(rank)):
        result_list.append([str(rank[i][1])+'위',rank[i][0]])
    return result_list


def address_shop_index_in_list(filename): 
    """make a list with elements like [address, shop, index]"""
    data = sort_by_address(filename)
    address_list = []
    for i in data:
        address_list.append([i[2],i[4],i[-1]])
    return address_list


def ranking_by_address(filename):
    a = address_shop_index_in_list(filename)
    
    address_list = set()  
    for i in a:
        address_list.add(i[0]) #주소들의 셋

    address_list = list(address_list) #주소들의 리스트(중복제거)
    
    
    rank_by_address = [] # rank_by_address = [['희우정로길',['1위',화장품],['2위',PC방]],['행당로길'],['1위',PC방],['2위',노래방]]
    for k in address_list:
        result = []
        for i in a:
            if i[0] == k:
                result.append(i[1:]) #address_list의 데이터(ex.['희우정로길', '화장품', '1'])를 ['화장품', '1'])형태로 변환
                
        result_elements = {}
        for i in result:
            if i[0] not in result_elements:
                result_elements[i[0]] = int(i[-1])
            else:
                result_elements[i[0]] += int(i[-1]) #같은 업종의 데이터들을 합산 (ex.{화장품: 11})
        result_elements = sorted(result_elements.items()) #정렬
        
        y = []
        for i in result_elements:
            y.append(list(i)) #딕셔너리 형태인 result_elements를 리스트 형태로 변환
            
        for i in range(len(y)): 
            s = y[i][0]
            y[i][0] = y[i][1]
            y[i][1] = s #위치 바꾸기(ex.[화장품,11] -> [11,화장품])
        if '점포' in filename:     
            rank = []
            count = 0
            for i in range(len(y)):
                s = 0
                x = y[i][0]
                for j in range(len(y)):
                    z = y[j][0]
                    if x>z:
                        s += 1
                rank.append([y[i][1],s+1])
                count += 1
                if count == len(y):
                    break #같은 크기의 데이터에 대해 같은 순위를 부여한다
            result_list = []
            for i in range(len(rank)):
                result_list.append([str(rank[i][1])+'위',rank[i][0]])            
        elif '추정매출' in filename:
            rank = []
            count = 0
            for i in range(len(y)):
                s = 0
                x = y[i][0]
                for j in range(len(y)):
                    z = y[j][0]
                    if x<z:
                        s += 1
                rank.append([y[i][1],s+1])
                count += 1
                if count == len(y):
                    break #같은 크기의 데이터에 대해 같은 순위를 부여한다
            result_list = [] # ex) result_list = [['1위','PC방'],['2위','노래방']]
            for i in range(len(rank)):
                result_list.append([str(rank[i][1])+'위',rank[i][0]])
        rank_by_address.append([k,result_list])      
    return rank_by_address

def A_Result_Dictionary():
    a = ranking_by_address_in_ascending_order('점포10월')
    b = ranking_by_address_in_descending_order('추정매출10월')
    c = ranking_by_address_in_descending_order('추정유동인구10월')

    reverse_a = []
    for i in a:
        reverse_a.append([i[1],int(i[0].strip('위'))])
    reverse_b = []
    for i in b:
        reverse_b.append([i[1],int(i[0].strip('위'))])
    reverse_c = []
    for i in c:
        reverse_c.append([i[1],int(i[0].strip('위'))])
    reverse_a = sorted(reverse_a)
    reverse_b = sorted(reverse_b)
    reverse_c = sorted(reverse_c)
    adding_data = []
    for i in range(len(reverse_a)):
        if reverse_a[i][0] == reverse_b[i][0]:
            if reverse_a[i][0] == reverse_c[i][0]:
                reverse_b[i][1] += reverse_c[i][1]
                reverse_a[i][1] += reverse_b[i][1]
                adding_data.append(reverse_a[i])
    rank = []
    count = 0
    for i in range(len(adding_data)):
        s = 0
        x = adding_data[i][1]
        for j in range(len(adding_data)):
            z = adding_data[j][1]
            if x>z:
                s += 1
        rank.append([adding_data[i][0],s+1])
        count += 1
        if count == len(adding_data):
            break
    result_list = []
    for i in range(len(rank)):
        result_list.append([str(rank[i][1])+'위',rank[i][0]])

    for i in result_list:
        i[0] = int(i[0].strip("위"))
    result_list = sorted(result_list)

    SortedDictionary = {}
    for i in result_list:
        if str(i[0]) + '위' not in SortedDictionary.keys():
            SortedDictionary[str(i[0])+'위'] = i[1]
        else:
            SortedDictionary[str(i[0])+'위'] += ","+i[1]
    return SortedDictionary

def A_Result():
    import pandas as pd
    x = A_Result_Dictionary()
    return pd.Series(x)
    

    #FinalResult = pd.Series(SortedDictionary)
    #return print("<어느 주소에서 장사를 해야할지 보여주는 지표>",FinalResult, sep = '\n')

def GetAddressRank():
    x = input("어느 주소의 순위를 보고 싶으신가요? ")
    y = A_Result_Dictionary()
    NewDict = {}
    for i,j in y.items():
        j = j.split(',')
        for items in j:
            NewDict[items] = i
    return NewDict[x]

def B_Result_DataFrame():
    import pandas as pd
    p = ranking_by_address('점포10월')
    q = ranking_by_address('추정매출10월')

    reverse_p = [] #[3,골프연습장] -> [골프연습장,3]
    for j in range(len(p)):
        address_name = p[j][0]
        data_list = []
        for i in range(len(p[j][1])):
            data_list.append([p[j][1][i][1],int(p[j][1][i][0].strip('위'))])
        reverse_p.append([address_name,data_list])

    reverse_q = [] #[31,골프연습장] -> [골프연습장, 31]
    for j in range(len(q)):
        address_name = q[j][0]
        data_list = []
        for i in range(len(q[j][1])):
            data_list.append([q[j][1][i][1],int(q[j][1][i][0].strip('위'))])
        reverse_q.append([address_name,data_list])
        
    reverse_p = sorted(reverse_p)
    reverse_q = sorted(reverse_q) # reverse_p리스트와 reverse_q리스트를 주소를 기준으로 가나다순으로 정렬


    for num in range(len(reverse_p)):
        same_list = []
        new_list = []
        for i in range(len(reverse_p[num][1])):
            same_list.append(reverse_p[num][1][i][0])
        for i in range(len(reverse_q[num][1])):
            if reverse_q[num][1][i][0] in same_list:
                new_list.append(reverse_q[num][1][i])
                
        reverse_q[num][1] = new_list #'점포'와 '추정매출' 둘 다 존재하는 데이터에 대해서만 비교
        
        a_list = []
        new_list = []
        for i in range(len(reverse_q[num][1])):
            a_list.append(reverse_q[num][1][i][0])
        for i in range(len(reverse_p[num][1])):
            if reverse_p[num][1][i][0] in a_list:
                new_list.append(reverse_p[num][1][i]) 
                
        reverse_p[num][1] = new_list #'점포'와 '추정매출' 둘 다 존재하는 데이터에 대해서만 비교

    #reverse_p = [[가락로길,[골프연습장,3],[노래방,8]...],[가로공원로길,[과일채소,18],[한의원,10]...]]
    #reverse_q도 reverse_p와 같은형태
    result_rank = []
    for num in range(len(reverse_p)): # len(reverse_p) : 주소의 갯수
        address_name = reverse_p[num][0]
        adding_data = [] #address_name별 데이터 ex.) [골프연습장,3]
        for i in range(len(reverse_p[num][1])):
            if reverse_p[num][1][i][0] == reverse_q[num][1][i][0]:
                reverse_p[num][1][i][1] += reverse_q[num][1][i][1]
                adding_data.append(reverse_p[num][1][i]) #같은 업소에 대하여 데이터를 합산 ex.) <가락로길> reverse_p의 골프연습장:3 reverse_q의 골프연습장:2 -> 골프연습장:5
        
        rank = [] #데이터들의 순위 매기기
        count = 0
        for i in range(len(adding_data)):
            s = 0
            x = adding_data[i][1]
            for j in range(len(adding_data)):
                z = adding_data[j][1]
                if x>z:
                    s += 1
            rank.append([adding_data[i][0],s+1])
            count += 1
            if count == len(adding_data):
                break
                
        result_list = []
        for i in range(len(rank)):
            result_list.append([str(rank[i][1])+'위',rank[i][0]])
        for i in result_list:
            i[0] = int(i[0].strip("위"))
        result_list = sorted(result_list)
        SortedDictionary = {}
        for i in result_list:
            if str(i[0]) not in SortedDictionary.keys():
                SortedDictionary[str(i[0])] = i[1]
            else:
                SortedDictionary[str(i[0])] += "," + i[1]
                
        result_rank.append([address_name,SortedDictionary])

    FirstAddress = result_rank[0][0] #result_rank의 첫번째 주소(가락로길)
    FirstAddressRank = [] #result_rank의 첫번째 주소의 순위목록
    FirstAddressShop = [] #result_rank의 첫번째 주소의 순위목록에 대응하는 업소목록

    for i in result_rank[0][1]:
        FirstAddressRank.append(i)
        FirstAddressShop.append(result_rank[0][1][i])
    FinalDataFrame = pd.DataFrame(data = FirstAddressShop, index = FirstAddressRank, columns = [FirstAddress]) #첫번째 주소를 표로 변환

    for i in range(1,len(result_rank)):
        NextAddress = result_rank[i][0]
        NextRank = []
        NextShop = []
        for j in result_rank[i][1]:
            NextRank.append(j)
            NextShop.append(result_rank[i][1][j])
        FinalDataFrame.loc[:,NextAddress] = pd.Series(NextShop, index = NextRank) #다음 주소들의 데이터들을 추가
        
    return FinalDataFrame

def B_Result():
    from IPython.display import display
    x = B_Result_DataFrame()
    return display(x)

def GetAddressInfo():
    from IPython.display import display
    x = input("주소를 입력하세요: ")
    y = B_Result_DataFrame()
    return display([y[x]])