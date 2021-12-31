#sudoku problem ... not optimal solution 
class Solution(object):
    
    def isValidSudoku(self, board):
        def remove_values_from_list(the_list, val):
            return [value for value in the_list if value != val]
        """
        :type board: List[List[str]]
        :rtype: bool
        """ 
        def check_boxes():
            val = []
            for element in board:
                val.append(element[:3])
                
            val1 = val[0]+val[1]+val[2]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[3]+val[4]+val[5]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[6]+val[7]+val[8]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            
            ##########################
            val = []
            for element in board:
                val.append(element[3:6])
                
            val1 = val[0]+val[1]+val[2]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[3]+val[4]+val[5]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[6]+val[7]+val[8]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            
            ##########################
            val = []
            for element in board:
                val.append(element[6:9])
                
            val1 = val[0]+val[1]+val[2]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[3]+val[4]+val[5]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            val1 = val[6]+val[7]+val[8]
            val1 = remove_values_from_list(val1, '.')
            if(len(set(val1))!= len(val1)):
                return False
            
            return True
                
        
        
        def check_rows():
            for in_list in board:
                in_list = remove_values_from_list(in_list, '.')
                if(len(in_list)!=len(set(in_list))):
                    return False
            return True
        
        def check_columns():
            for j in range(len(board)):
                value = []
                for i in range(0, len(board)):
                    value.append(board[i][j])
                    
                value = remove_values_from_list(value, '.')
                if(len(value)!=len(set(value))):
                    return False
            return True
                
        
        
        if(check_rows() and check_boxes() and check_columns()):
            return True
        
        else:
            False

        
        
                
            
               
