import heapq
class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None
    def __1t__(self,other):
        return self.frequency<other.frequency
    def __eq__(self,other):
        return self.frequency==other.frequency
class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        
    def __make_frequency_dict(self):
        freq_dict={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1
        return freq_dict
    def __buildHeap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binary_tree_node=BinaryTreeNode(key,frequency)
            heapq.push(self.__heap,binary_tree_node)
    def compress(self):
        #get file from path
        #read text from file
        text="fasbsajfhbsafjhbashf"
        #make frequency dictionary using the text
        freq_dict=self.__make_frequency_dict(text)
        #construct the heap from the frequency_dict
        
        #construct the binary tree from the heap
        
        #creating the encoded text using the codes
        
        #put this encoded text into the binary file
        
        #return the binary file as output
        
        
        