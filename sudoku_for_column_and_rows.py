x = []
        
        for in_list in board:
            for i in range(0, len(board), 3):
                if(in_list[i]=='.'):
                    continue
                elif in_list.count(in_list[i])!=1:
                    return False

        
            
        for j in range(len(board)):
            value = []
            count = 0
            for i in range(0, len(board)):
                
                value.append(board[i][j])
                if(i == 3):
                    print('i am here')
                    value = remove_values_from_list(value, '.')
                    if(len(set(value))!=len(value)):
                        return False
                    else:
                        value = []
                elif(i == 6):
                    print(value, "at i value 6")
                    value = remove_values_from_list(value, '.')
                    if(len(set(value))!=len(value)):
                        return False
                    else:
                        value = []
                    
                elif(i == 8):
                    value = remove_values_from_list(value, '.')
                    if(len(set(value))!=len(value)):
                        return False
                    else:
                        value = []
                count+=1
                print(value)
                
return True
