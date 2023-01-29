class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.size = 4
        self.arr = [0] * self.size
        self.current_size = 0
        self.last_num_index = -1
        self.ordered_arr = True

    def __str__(self):
        string = ""
        for i in range(self.current_size):
            string += str(self.arr[i]) + ", "
        return string[:-2]###breyta
    
    def prepend(self, value):
        if self.current_size == self.size:
            self.add = True
            self.resize()
        
        for i in range(self.current_size, 0, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[0] = value
        self.current_size += 1
        self.last_num_index +=1
        if self.ordered_arr != False:
            self.ordered()
        
    def insert(self, value, index):
        if index < 0 or index > self.current_size:
            raise IndexOutOfBounds()
        if self.current_size == self.size:
            self.add = True
            self.resize()
        self.last_num_index += 1
        for i in range(self.current_size, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.current_size += 1
        self.ordered()
        
    def append(self, value):
        if self.current_size == self.size:
            self.add = True
            self.resize()
        self.last_num_index += 1
        self.arr[self.last_num_index] = value
        self.current_size += 1
        if self.ordered_arr != False:
            self.ordered()

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index > self.current_size -1:
            raise IndexOutOfBounds()
        self.arr[index] = value


    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.current_size == 0:
            raise Empty()
        else:
            return self.arr[0]

        

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index < 0 or index > self.current_size -1:
            raise IndexOutOfBounds()
        else:
            return self.arr[index] 

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        if self.current_size == 0:
            raise Empty()
        return self.arr[self.current_size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        if self.add == True:
            self.size *= 2
            temp_arr = [0] * self.size
            for i in range(self.current_size):
                temp_arr[i] = self.arr[i]
        else:
            self.size -= 1
            temp_arr = [0] * self.size
            index = 0
            for i in range(self.size+1):
                if self.arr[i] == None:
                    continue
                temp_arr[index] = self.arr[i]
                index += 1
        self.arr = temp_arr

        #self.size+=1 eða self.size-=1

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if index < 0 or index > self.current_size:
            raise IndexOutOfBounds()
        self.arr[index] = None
        self.current_size -= 1
        self.add = False
        self.last_num_index -= 1
        self.resize()
        self.ordered()

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        self.arr = [0] * self.size
        self.current_size = 0
        self.last_num_index = -1
        self.ordered_arr = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.ordered_arr == False:
            raise NotOrdered()
        if self.size == self.current_size:
            self.add = True
            self.resize()
        for i in range(self.current_size+1): ####Stendur að þetta a að vera O(n) veit ekki hvernig maður a að implementa þvi nema maður veit staðsetningu a value
            if value <= self.arr[i]:
                for j in range(self.current_size,i,-1):
                    self.arr[j] = self.arr[j-1]
                self.arr[i] = value
                self.current_size += 1
                self.last_num_index +=1
                break
        else:
            self.last_num_index +=1
            self.arr[self.last_num_index] = value
            self.current_size += 1
            
                
    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.ordered_arr == True:
            return self.binary_search( value, 0, self.current_size-1)
        return self.linear_search(value)

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass
    def ordered(self):
        
        for i in range(self.current_size-1):
            if not isinstance(self.arr[i], int):
                self.ordered_arr = False
                break
            if self.arr[i] > self.arr[i+1]:
                self.ordered_arr = False
                return
        
    def linear_search(self,value):
        for index in range(self.current_size):
            if self.arr[index] == value:
                return index
        raise NotFound()
    
    def binary_search(self,value,low,high):
        if high < low:
            raise NotFound()
        middle = low + (high-low) // 2
        if value == self.arr[middle]:
            return middle
        elif value > self.arr[middle]:
            return self.binary_search(value, middle+1, high)
        else:
            return self.binary_search(value, low, middle-1)


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.prepend({"23 twentythree": 23.23})
    arr_lis.prepend({"23 twentythree": 23.23})

    print(str(arr_lis))