import heapq
class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None
    def __1t__(self,other):
        return self.freq<other.freq
    def __eq__(self,other):
        return self.freq==other.freq
class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        
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
    def __buildTree(self):
        while(len(self.__heap)>1):
            binary_tree_node1=heapq.heappop(self.__heap)
            binary_tree_node_2=heapq.heappop(self.__heap)
            freq_sum=binary_tree_node_1.freq+binary_tree_node_2.freq
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=binary_tree_node_1
            newNode.right=binary_tree_node_2
            heapq.heappush(self.__heap,newNode)
        return
    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return 
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            return
        self.__buildCodesHelper(self,root.left,curr_bits+"0")
        self.__buildCodesHelper(self,root.right,curr_bits+"1")
    def __buildCodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")
            
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
        
        
        