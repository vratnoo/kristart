# # stt=""
# # for x in range(1,100):
# # 	if x%7==0 and x%5!=0:
# # 		stt=stt+str(x)+","
# # print(stt)

# # my own method
# # New method authentic

# # strs=[]
# # for x in range(1,100):
# # 	if (x%5==0) and (x%7!=0):
# # 		strs.append(str(x))

# # print(",".join(strs))
# # newstr=[1,2,3,4,5,6,7,8]

# # def front_back(nums):
# #   le=len(nums)
# #   for i in range(le-2):
# #     # if(nums[i:3]==[1,2,3]):
# #       # print
# #       print(i)
# #       print(nums[i:i+3])
# # print(front_back(newstr))

# # def string_match(a, b):
# #   le=len(a) if len(a)<len(b) else len(b)
# #   count=0
# #   print(le)
# #   for i in range(le):
# #     print(a[i:i+2])
# #     if(a[i:i+2]==b[i:i+2]):
# #       # print(a[i:i+2])
# #       # count=count+1
# #   return count    

# # print(string_match("vratnoo","cratnoo"))
# # def make_tags(tag, word):
# #   return "<{t}>".format(t=tag,w=word)

# # print(make_tags("w","sds"))

# # a=7
# # b=1
# # print(abs(a-b))

# # def make_bricks(small, big, goal):
# #   s=1
# #   b=5
# #   s_mod=goal%5
# #   div=goal//5
# #   return s_mod,div
# #   if(s*small+b*big==goal):
# #   	return True
# #   elif(s*small==goal):
# #   	return True
# #   elif(b*big==goal):
# #   	return True
# #   elif(s_mod<=small and div<=big):
# #   	return True
# #   else:
# #   	div=big
# #   	s_mod=goal-big*b
# #   	if(s_mod*s+div*b==goal):
# #   		return True
# #   	else:
# #   		return False
  	
# # print(make_bricks(6, 1, 11))
# # print(make_bricks(1, 4, 11))
# # print(make_bricks(3,2,8))
  
# # def end_other(a, b):
# #   a=a.lower()
# #   b=b.lower()
# #   le=len(a) if len(a)<=len(b) else len(b)
  
# #   for i in range(le-1):
# #     print(a[-(i+1):],)
# #     print(b[-(i+1):])
# #     if(a[-i:]!=b[-i:] and i!=le-1):
# #       pass
# #       # return False
# #   return True

# # end_other("vikram","rdsdsam")  

# # def sum13(nums):
# #   count=0
# #   i=0
# #   ends=True
# #   # print(len(nums))
# #   while i<len(nums):
    
# #     if(nums[i]!=13 and i<len(nums)):
# #     	count=count+nums[i]
# #     	print(nums[i])
# #     	i+=1
# #     else:
# #     	i+=2
# #   return count
# #  #    0  1  2  3  4   5   	
# # sum13([1, 3,13,2, 2, 8])

# # def sum67(nums):
# # 	sum=0
# # 	flag=False
# # 	i=0
# # 	while(i<len(nums)):

# # 		if(nums[i]!=6 and flag==False):
# # 			sum=sum+nums[i]
# # 			print(nums[i])	
			
# # 		if(nums[i]==6 and flag==False):
# # 			flag=True
			
# # 		if(flag==True):
# # 			if(nums[i]==7):
# # 				flag=False
# # 		i+=1	
# # 	return sum	
    
# # sum67([1, 1, 6, 7,5,7, 2])

# # a=[[11,2,4],[4,5,6],[10,8,-12]]
# # n=len(a)
# # pd=0
# # sd=0
# # ms=[]
# # js=[]
# # for i in range(len(a)):
# # 	# print(i)
# # 	for j in range(len(a[i])):
# # 		ids=(len(a)-1)-i 
# # 		jds=(len(a[i])-1)-j
# # 		if(i==j):
# # 			pd+=a[i][j]
			
# # 			ms.append(a[i][j])
# # 		if(ids==jds):
# # 			sd+=a[i][jds]
# # 			js.append(a[i][jds])
# # print(pd,sd)
# # print(sum(ms))
# # print(sum(js))
# #####NEW ##########
# # n=6
# # print("sssss")
# # print("sssss")
# # for i in range(n):
# # 	for j in range(n):
# # 		if(j<n-(i+1)):
# # 			print("*",end="")
# # 		else:
# # 			print("#",end="")
# # 	print("")
# ###########min max sum

# # arr=[1,2,5,8,9]
# # nr=[]
# # for i in range(len(arr)):
# # 	sum=0
# # 	for j in range(len(arr)):
		
# # 		if(j!=i):
# # 			sum+=arr[j]
# # 			print(arr[j],end="")
# # 	print("")		
# # 	nr.append(sum)	
# # print(min(nr),max(nr))

# # min max
# # ar=[3,2,1,3,4]
# # count=0
# # for i in ar:
# #     if(i==max(ar)):
# #         count+=1 
# # print(count)
# ### time conversion #####

# # st="12:45:54PM"
# # print(st[0:2])
# # print(st[3:5])
# # print(st[6:8])
# # print(st[-2:])
# # h=st[0:2]
# # m=st[3:5]
# # s=st[6:8]
# # mo=st[-2:]
# # if(mo=="PM"):
# # 	if(h!="12"):
# # 		h = int(h)+12
# # 	print("{}:{}:{}".format(h,m,s))
# # elif(mo=="AM"):
# # 	if(h=="12"):
# # 		h="00"
# # 	print("{}:{}:{}".format(h,m,s))
# ##aple and ornge problem
# # def countApplesAndOranges(s, t, a, b, apples, oranges):
# # 	ac=0
# # 	oc=0
# # 	for i in apples:
# # 		if(i+a>=s and i+a<=t):
# # 			ac+=1
# # 		print(i+a)
# # 	print(ac)
# # 	for i in oranges:
# # 		if(i+b>=s and i+b<=t):
# # 			oc+=1
# # 		print(i+b)
# # 	print(oc)
# # countApplesAndOranges(7, 11, 5, 15, [-2,3,2], [-5,6])

# ###birthday cack problem

# # def birthday(s, d, m):
# # 	count=0
# # 	for i in range(len(s)-(m-1)):
		
# # 		if(sum(s[i:i+m])==d):
# # 			count+=1
# # 	print(count)
# # birthday([1,1,1,1,1], 2, 2)

# ### breaking the record ###

# # def breakingRecords(sc):
# # 	mins=sc[0]
# # 	maxs=sc[0]
# # 	minc=0
# # 	maxc=0
# # 	for i in range(len(sc)-1):
# # 		print(sc[i+1])
# # 		if(sc[i+1]>maxs):
# # 			maxc+=1
# # 			maxs=sc[i+1]
# # 		elif(sc[i+1]<mins):
# # 			minc+=1
# # 			mins=sc[i+1]	

# # 	print(maxc,minc)		


# # breakingRecords([3,4,21,36,10,28,35,5,24,42])	


# ## dvisible sum pairs
# # def divisibleSumPairs(n, k, ar):
# # 	count=0
# # 	for i in range(len(ar)):
# # 		for j in range((n-1)-i):
			
# # 			if((ar[i]+ar[i+j+1])%k==0):
				
# # 				print([i,i+j+1],end="#")
# # 				print([ar[i],ar[i+j+1]],end="&")	

# # 	print("")		
# # 					 #0  1  2 3 4 5
# # divisibleSumPairs(5,2,[5,9,10,7,4])	

# # #### Migratory brds

# # def migratoryBirds(arr):
# # 	prv=arr[0]
# # 	for i in range(len(arr)-1):
# # 		count=0
# # 		if(prv!=arr[i+1]):
# # 			print("ok")

# # 		for j in range((len(arr)-i)-1):
# # 			if(arr[i+j+1]==arr[i]):	
# # 				count+=1
# # 		print(count)		


# # migratoryBirds([1,4,4,4,5,3])
# # #status## Failed

# # # spli bill
# # def bonAppetit(bill, k, b):
# # 	sum=0
# # 	for i in range(len(bill)):
# # 		if(i!=k):
# # 			sum+=bill[i]
# # 	if(b==sum/2):
# # 		return "Bon Appetit"
# # 	else:
# # 		return (b-sum/2)
# # bonAppetit([3,10,2,9],1,8)

# # # color stocks
# # def sockMerchant(n, ar):
# # 	for i in range(len(ar)):
# # 		for j in range((len(ar)-1)-i):
# # 			if(ar[i]==ar[i+j+1]):
# # 				print(ar[i])
# # 				print(i,i+j+1)
# # 				ar.remove(ar[i])
# # 				# ar.remove(ar[i])
# # 				break
				

# # 	print(ar)
# # sockMerchant(9,[10,20,20,10,10,30,50,10,20])

# # ##passion test
# # n=5
# # p=3
# # ar=[]
# # for i in range(n):
# # 	ar.append(i+1)

# # print(ar)
# # def pageCount(n, p):
# # 	front=p//2
# # 	if(n%2==0):
# # 		b=(n-p+1)//2

# # 	else:
# # 		b=(n-p)//2

# # 	return min(front,b)
# # print(pageCount(5,4))

# # #vally function
# # def countingValleys(n, s):
# # 	sl=0
# # 	c=0
# # 	for i in s:
# # 		if(i=="U"):
# # 			sl+=1
# # 		elif(i=="D"):
# # 			sl-=1
# # 		if(sl==0 and s.index(i)>=1):
# # 			c+=1
# # 	print(c)		

# # countingValleys(12,"DDUUDDUDUUUD")
# # ## new problem 100% win happened 
# def getMoneySpent(k, d, b):
# 	par=[]
# 	for i in k:
# 		for j in d:
# 			if(i+j<=b):
# 				par.append(i+j)
# 	if(par!=[]):
# 		return max(par)
# 	else:
# 		return -1
# getMoneySpent([4],[5],5)

# def catAndMouse(x, y, z):
# 	if(abs(x-z)<abs(y-z)):
# 		return "Cat A"
# 	elif(abs(x-z)>abs(y-z)):
# 		return "Cat B"
# 	else:
# 		return "Mouse C"

# print(catAndMouse(1,2,3))

# def pickingNumbers(a):
# 	for i in a:
# 		print(i)

# pickingNumbers([4,6,5,3,3,1])
###status Failed
# n=3
# H=1
# for i in range(1,n+1):
# 	print(i)
# 	if(i%2==0):
# 		H+=1
# 		print("["+str(H)+"]")
# 	else:
# 		H=H*2
# 		print("["+str(H)+"]")
# print(H)
##statsus :succeed

def cutTheSticks(arr):
	
	

	while(len(arr)):
		count=0
		mi=min(arr)
		for i in range(len(arr)-1):
			if(arr[i]!=0):
				
				arr[i]=arr[i]-mi
				count+=1
			print(arr)
			
			if(arr[i]==0):
				arr.remove(arr[i])
		
				
		print(count,mi)

	# print(arr)
	# print(count)			
cutTheSticks([5,4,4,2,2,8])