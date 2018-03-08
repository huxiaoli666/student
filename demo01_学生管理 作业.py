import pickle,os

stuFileId = os.getcwd()

if os.path.exists('E:\\phthon基础内容年后\\20180305\\allStuInfo.txt')==False:
	f=open('accountData.txt','wb')
	f.write(pickle.dumps([]))
	f.close()
#定义展示函数
def show():
	print('	','-'*32)
	print('	|    欢迎进入学生管理系统       |')
	print("	| 	1.添加学生的信息	|")
	print("	| 	2.修改学生的信息	|")
	print("	| 	3.查询学生的信息	|")
	print("	| 	4.查询所有学生的信息	|")
	print("	| 	5.删除学生的信息	|")
	print("	| 	6.退出系统		|")
	print('	','-'*32)

class Student():
	def __init__(self,stuName,stuAge,stuAddress):
		self.stuName = stuName
		self.stuAge = stuAge
		self.stuAddress = stuAddress

	#增加	
	def addInfo(self):
		f=open('allStuInfo.txt','rb')
		content=pickle.loads(f.read())
		f.close()
		self.stuName = input('请输入添加学生的姓名:\t')
		self.stuAge = input('请输入学生的年龄：\t')
		self.stuAddress = input('请输入学生的住址：\t')
		while True:
			for i in content:
				if (self.stuName==i['keyName']) and (self.stuAge==i['keyAge']) and (self.stuAddress==i['keyAddress']):
					num=int(input("该学生信息已经存在，请选择：1.重新输入\t2.退出"))
					if num==2:
						exit()
					else:
						self.stuName = input('请输入添加学生的姓名:\t')
						self.stuAge = input('请输入学生的年龄：\t')
						self.stuAddress = input('请输入学生的住址：\t')
						break
			else:
				oneStuDict = {}
				oneStuDict['keyName'] = self.stuName
				oneStuDict['keyAge'] = self.stuAge
				oneStuDict['keyAddress'] = self.stuAddress
				content.append(oneStuDict)
				f1 = open('allStuInfo.txt','wb')
				pickle.dump(content,f1)
				f1.close()
				print('\n---提示：添加成功!---\n')
				break

	#修改
	def updataInfo(self):
		f = open('allStuInfo.txt','rb')
		updataList = pickle.loads(f.read())
		f.close()
		if len(updataList)==0:
			print('\n---提示：修改失败，文件中没有学生信息!---\n')
		else:
			flag = 1
			while flag:
				updataName = input("请输入需要修改的学生的姓名：")
				for i in updataList:
					if updataName == i['keyName']:
						flag1 = 1
						while flag1:
							num = int(input('请选择：\n1.修改学生的姓名\t2.修改学生的年龄\t3.修改学生的住址\t'))
							if num==1:
								updataName1 = input('请输入新的姓名：\t')
								f2 = open('allStuInfo.txt','rb')
								List1 = pickle.loads(f2.read())
								f2.close()
								for j in List1:
									if (updataName1==j['keyName']) and (i['keyAge']==j['keyAge']) and (i['keyAddress']==j['keyAddress']):
										num=int(input('该学生信息已经存在，请选择：1.重新输入姓名\t2.退出'))
										if num==2:
											exit()
										else:
											updataName = input('请重新输入要修改信息学生的姓名:\t')
											break
								else:
									i['keyName'] = updataName1  
									flag1=0 

							elif num==2:
								i['keyAge'] = input('请输入新的年龄：\t')
								f2 = open('allStuInfo.txt','rb')
								List1 = pickle.loads(f2.read())
								f2.close()
								for j in List1:
									if (i['keyName']==j['keyName']) and (i['keyAge']==j['keyAge']) and (i['keyAddress']==j['keyAddress']):
										num=int(input('该学生信息已经存在，请选择：1.重新输入\t2.退出'))
										if num==2:
											exit()
										else:
											updataName = input('请重新输入要修改信息学生的姓名:\t')
											break
								else:
									i['keyName'] = updataName
									flag1=0

							elif num==3:
								i['keyAddress'] = input('请输入新的住址：\t')
								f2 = open('allStuInfo.txt','rb')
								List1 = pickle.loads(f2.read())
								f2.close()
								for j in List1:
									if (i['keyName']==j['keyName']) and (i['keyAge']==j['keyAge']) and (i['keyAddress']==j['keyAddress']):
										num=int(input('该学生信息已经存在，请选择：1.重新输入\t2.退出'))
										if num==2:
											exit()
										else:
											updataName = input('请重新输入要修改信息学生的姓名:\t')
											break
								else:
									i['keyName'] = updataName
									flag1=0
							else:
								print('\n---提示：输入错误!---\n')
						f1 = open('allStuInfo.txt','wb')
						pickle.dump(updataList,f1)
						print(updataList)
						print(List1)   
						f1.close()
						print('\n---提示：修改成功!---\n')
						flag=0
						break					
				else:
					print('\n---提示：文件中没有姓名为',updataName,'的信息!---\n')


	#条件查询
	def findOne(self):
		f = open("allStuInfo.txt","rb")
		findOneList = pickle.loads(f.read())
		f.close()

		flag=1
		while flag:
			if len(findOneList)==0:
				print('\n---提示：查询失败，文件中没有学生信息!---\n')
				break
			findName = input('请输入要查询学生信息的姓名：')
			j=0  #找的是看输出第几个
			for i in findOneList:
				if findName==i['keyName']:
					print('姓名：',i['keyName'],'\t年龄：',i['keyAge'],'\t地址：',i['keyAddress'])
					flag=0
					print('\n---提示：查询成功!---\n')
					break
				j+=1
			else:
				print('\n---提示：文件中没有姓名为',findName,'的信息，查询失败!---\n')



	#查询所有
	def findAll(self):
		f = open('allStuInfo.txt','rb')
		content = pickle.loads(f.read())
		if len(content)>0:
			print('姓名','\t','年龄','\t','住址')
			for i in content:
				print(i['keyName'],'\t',i['keyAge'],'\t',i['keyAddress'])
			print('\n---提示：查询成功！---\n')
		else:
			print('\n---提示：查询失败，文件中没有学生信息!---\n')
		f.close()

	#删除
	def delInfo(self):
		f = open('allStuInfo.txt','rb')
		delList = pickle.loads(f.read())
		f.close()
		flag=1
		while flag:
			if len(delList)==0:
				print('\n---提示：删除失败，文件中没有学生信息!---\n')
				break
			delName = input('请输入要删除学生信息的姓名：')
			j=0
			for i in delList:
				if delName==i['keyName']:
					del delList[j]
					f1 = open('allStuInfo.txt','wb')
					pickle.dump(delList,f1)
					f1.close()
					flag=0
					print('\n---提示：删除成功!---\n')
					break
				j+=1
			else:
				print('\n---提示：文件中没有姓名为',delName,'的信息，删除失败!---\n')


while True:
	show()
	num=input("请输入功能序号：")
	if num.isdigit():
		num=int(num)
		if num==1:
			print('---提示：您选择的是添加学生信息的功能---')	
			addObj = Student('','','')
			addObj.addInfo()
		##修改
		elif num==2:
			print('---提示：您选择的是修改学生信息的功能---')
			updataObj = Student('','','')
			updataObj.updataInfo()	
		##查询单个
		elif num==3:
			print('---提示：您选择的是查找单个学生信息的功能---')
			findOneObj = Student('','','')
			findOneObj.findOne()
		##查询全部
		elif num==4:
			print('---提示：您选择的是查询所有学生信息的功能---')
			findAllObj = Student('','','')
			findAllObj.findAll()
		##删除
		elif num==5:
			print('---提示：您选择的是删除学生信息的功能---')
			delObj = Student('','','')
			delObj.delInfo()
		elif num==6:
			exit()
	else:
		print("您输入的不是纯数字,请重新纯数字：")