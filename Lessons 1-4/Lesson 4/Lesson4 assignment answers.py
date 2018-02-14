
from writeXL_method import writeXL_method

csvlist1 = ['header1','a2','a3', 'a4']
csvlist2 = ['header2','b2','b3', 'b4']
csvlist3 = ['header3','c2','c3']
toplist = [csvlist1,csvlist2,csvlist3]



writeXL_method(toplist,'less4answerWS','less4answerWB') #supply our custom-made function its arguments (ie inputs)
