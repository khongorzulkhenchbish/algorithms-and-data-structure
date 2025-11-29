class SparseVector:
    # Approach optimal: A sparse vector is a vector that has mostly zeroes, space consuming for 1 dimensional array.
    # O(N) for creating nonzeros pairs, O(L1+L2) for calculating the dot prod
    # Space: O(L) for storing the pairs for nonzeros
    def __init__(self, nums: List[int]):
        self.pairs = []
        for ind, val in enumerate(nums):
            if val != 0:
                self.pairs.append([ind, val]) # faster than hashing for larger inputs

    def dotProduct(self, vec: 'SparseVector') -> int:
        dotprod = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            # if the indes are equal
            if self.pairs[p][0] == vec.pairs[q][0]:
                dotprod += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            # if the ind of the first array is less, increment to catch up with the second
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            # if the ind of the second array is less, increment to catch up with the first
            else:
                q += 1

        return dotprod    

    
    # Approach 2: store the non-zero vals in hashmap: {"ind":"val"}
    # [1,0,0,5,0,0,0,0] => {"0":1, "3":5}
    # Time: O(N) for hashmap init, O(L) for calculating the dot prod. O(N+L)
    # Space: O(L) where L is the non zeros. O(1) for dot prod
    # cons: for larger inputs, hashing function itself takes longer time 
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for ind,val in enumerate(nums): # iterate with ind and val at the same time
            if val != 0:
                self.nonzeros[ind] = val
    
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotprod = 0

        # by this time, vec will be in format of the self.nonzeros already
        for ind, val in self.nonzeros.items():
            # v1 = [1,0,0,2,3] => {"0":1, "3":2, "4":3}
            # v2 = [0,3,0,4,0] => {"1":3, "3":4}
            # only intersection is v1=[2] and v2=[4]
            # check if the ind also exist in the vec
            if ind in vec.nonzeros:
                dotprod += val * vec.nonzeros[ind]

        return dotprod


    # Approach 1: Use the array. Time: O(n), Space: O(1)
    # You can access the vals by vectorObj.array => which will return a list
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProd = 0
        for a, b in zip(self.array, vec.array):
            dotProd += a*b
        return dotProd