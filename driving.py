country = input('請問你是哪國人：')
age = input('請輸入你的年齡：')
if country == '台灣':
	if int(age) >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if int(age) >= 16:
			print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('目前僅對應台灣及美國')