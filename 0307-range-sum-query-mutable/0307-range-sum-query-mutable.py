class NumArray:

    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.arr=nums
        self.tree=[0 for _ in range(self.n *4)]
        if self.n>0:
            self.build(0,0,self.n-1)
    
    def build(self,i,l,r):
        if l==r:
            self.tree[i]=self.arr[l]
            return self.arr[l]
        
        mid=(l+r)//2
        left=self.build(2*i +1,l,mid)
        right=self.build(2*i +2 ,mid+1,r)

        self.tree[i]=left+right
        return self.tree[i]

    def update2(self,i,l,r,j,val):
        if l==r==j:
            self.tree[i]=self.arr[l]=val
            return 
        mid=(l+r)//2
        if j<=mid:
            self.update2(2*i +1,l,mid,j,val)
        else:
            self.update2(2*i +2 ,mid+1,r,j,val)
        
        self.tree[i]=self.tree[2*i +1] + self.tree[2*i +2]
        return


    def update(self, index: int, val: int) -> None:
        self.update2(0,0,self.n-1,index,val)
        return

    
    def summ(self,i,l,r,ql,qr):
        # disjoint set
        if qr<l or r<ql:
            return 0
        # fully submerginf case
        if ql<=l and r<=qr:
            return self.tree[i]
        
        # partial submerging case
        mid=(l+r)//2
        left=self.summ(2*i+1,l,mid,ql,qr)
        right=self.summ(2*i +2,mid+1,r,ql,qr)

        return left+right
        

    def sumRange(self, left: int, right: int) -> int:
        return self.summ(0,0,self.n-1,left,right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)