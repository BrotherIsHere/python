import xlwings as xw

# app=xw.App()#没多大用,但不用好像关不了程序
# ()内为空为新建工作薄
wb = xw.Book("学籍.xlsx")
# (相对或绝对路径)为打开工作薄
# wb=xw.Book("学籍.xlsx")
# 打开对应的表[切片名称]
sht = wb.sheets[0]
# a1中插入数据
sht.range("a1").value = "jjjj"
# 读取a1,value后不加 =
print(sht.range("a1").value)
# 插入行下同
sht.range("a2").value = "a", 3, "b"
sht.range("a3").value = ["a", 8, 0]
# 插入列
sht.range("a4").value = [['b'], ["c"], ["d"]]
# 插入区域
sht.range("a7").value = [['a', 'b', 'c', 'k'], ['b', 'c', 'c', 'f'], [2, 2, 3, 4]]
# 或
sht.range("e1:s55").value = [['a', 'b', 'c', 'k'], ['b', 'c', 'c', 'f'], [2, 2, 3, 4]]
# 插入复制或使用expand()来扩展区域
# 注意expand开始行和列遇到空格就认为后面不再有数据
# 复制其它表格内容要更改sht为其它实例表格
print(sht.range("a1").expand().value)
sht.range("f6").value = sht.range("b2:c3").value
sht.range("a11").value = sht.range("a7").expand().value
# 工作表名称
sname = sht.name
print(sname)
# 工作薄名称
print(wb.name)
# 工作薄绝对路径
print(wb.fullname)
# 清除单元格内容和格式
sht.range("h11:i13").clear()
# 获取单元格列标
col = sht.range("h1").column
print(col)
# 获取单元格行标
print(sht.range("d2").row)
# 获取单元格列宽 行高
wid = sht.range("d3").column_width
print(wid)
print(sht.range("k3").row_height)
# 自适应行高 列宽
sht.range("d4").rows.autofit()
sht.range("a2:z19").columns.autofit()
# 颜色
sht.range("a2:d2").color = (22, 44, 52)
print(sht.range("a2").color)
sht.range("c2").color = None
# 公式
sht.range("m8").formula = "=sum(f8:h8)"
fl=sht.range("m8").formula
print(fl)

# 关闭工作薄
wb.save()

#wb.close()
# 退出程序
# ?还没找到


