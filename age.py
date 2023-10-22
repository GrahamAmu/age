driving = input("請問你有沒有開過車? ")
if driving == "有" or driving == "沒有":
	age = int(input("請問你的年齡? "))
	if driving == "有" :
		if age >= 18 :
			print("恭喜你通過測試")
		else :
			print("未成年不能開車")
	else :
		if age >= 18 :
			print("你可以考駕照了")
		else :
			print("再過幾年就可以考駕照了")
else :
	print("只能輸入有/沒有")