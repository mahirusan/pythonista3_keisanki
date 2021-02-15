import ui

inputnum = '' 
prevnum = ''
operation = ''

#数字ボタンをタップした時の処理
def on_numtap(sender):
	global inputnum
	#sender→クリックしたボタンの要素が入る
	v = sender.superview #タップしたボタン(sender)の親要素
	#文字列連結で最初先頭に0が付いたままになるので対策
	inputnum = str(int(inputnum+sender.title) if float(inputnum+sender.title).is_integer() else float(inputnum+sender.title))
	v['label1'].text = inputnum


#clearボタンを押した時の処理
def on_clearbtn(sender):
	global inputnum,prevnum,operation
	v = sender.superview #タップしたボタン(sender)の親要素
	v['label1'].text = '0'
	inputnum = ''
	prevnum = ''
	operation = ''

#delボタンを押した時の処理
def on_delbtn(sender):
	global inputnum
	v = sender.superview #タップしたボタン(sender)の親要素
	#label1が空でなければ1文字削除する
	if len(inputnum) >= 1:
		inputnum = inputnum[0:-1]
		v['label1'].text = inputnum
	elif len(inputnum) == 1:
		inputnum = ''
		v['label1'].text = ''
    
#演算子ボタンを押した時
def on_opebtn(sender):
	global inputnum,prevnum,operation
	v = sender.superview #タップしたボタン(sender)の親要素
	#前回何か演算子を入れていたら
	if operation != '':
		if len(inputnum) == 0:
			operation = sender.title
		else:
			#計算処理(inputnum,prevnum,operation)
			prevnum = calc(inputnum,prevnum,operation)
			operation = sender.title
			inputnum = ''
			v['label1'].text = prevnum
	else:
		if len(inputnum) == 0 and len(prevnum) != 0:
			operation = sender.title
		elif len(inputnum) == 0 and len(prevnum) == 0:
			pass
		else:
			#演算子をoparationに退避
			operation = sender.title
			#現在のラベルにある入力値を退避
			prevnum = inputnum
			inputnum = ''

#=ボタンを押した時
def on_equalbtn(sender):
	global inputnum,prevnum,operation
	v = sender.superview #タップしたボタン(sender)の親要素
	if len(inputnum) != 0:
		prevnum = calc(inputnum,prevnum,operation)
		inputnum = ''
		operation = ''
		v['label1'].text = prevnum

#.ボタンを押した時
def on_dotbtn(sender):
	global inputnum
	v = sender.superview #タップしたボタン(sender)の親要素
	if len(inputnum) == 0:
		inputnum = '0.'
		v['label1'].text = '0.'
	else:
		if '.' not in inputnum:
			inputnum += '.'
			v['label1'].text = inputnum

#計算処理(計算して結果を返す)
def calc(inp,prev,ope):
	if ope == '+':
		retval = float(prev)+float(inp)
	elif ope == '-':
		retval = float(prev)-float(inp)
	elif ope == '÷':
		retval = float(prev)/float(inp)
	elif ope == '×':
		retval = float(prev)*float(inp)
	return str(int(retval)) if retval.is_integer() else str(retval)

#pyuiの部品の情報を読み込み
v = ui.load_view()
#画面を描画する
v.present('sheet')
