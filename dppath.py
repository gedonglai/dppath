#coding= utf-8
# import re
# with open ('/home/gedonglai/桌面/t528.txt','a')as f:
#     for i in open('/home/gedonglai/桌面/ttok.txt','r'):
#         i=i.replace('"','') 
#         i = i.replace('\\','')
#         f.write('{"sentence": "'+i.strip()+'"}'+'\n')
class node:
    def __init__(self, row,num):
        self.word = row[1]
	if row[6]=='_':
		self.parentnum = row[6]
	else:
        	self.parentnum = int(row[6])
        self.parent=[]
        if row[7] != 'ROOT':
	  
            self.relation = row[7]
            self.parent=[]
        else:
            self.relation = ''
            self.parent.append('ROOT')
        self.children = []
        #self.parent=[]
        self.index=num
    def get_allpath(self,tmp):
        a = self
        tmp.append(a.relation)
        #print type(a),a.word
        while a.parent !=[] and a.parent[0]!='ROOT':
            a = a.parent[0]
            tmp.append(a.relation)
    def get_allparent(self,tmp_p):
        a = self
        flag =False
        tmp_p.append(a)
        while  a.parent !=[] and flag == False:
            if a.parent[0]=='ROOT':
                #print 'hh'
                flag = True
                tmp_p.append('ROOT')
            else:
                #print 'hh'
                a = a.parent[0]
                tmp_p.append(a)
            #print 'hh'
bpesent =[]
with open('testbpe1.txt','r')as y:
    for yy in y:
        bpesent.append(yy.strip())
with open('test.r', 'a')as f:
  
    num = 0
    all_word = []
    line =0
    for i in open('pretest.txt', 'r'):
        #all_path=[]
        if i.strip() != '':
            num+=1
            row = i.split()
            a= node(row,num)
            all_word.append(a)

        else:
            #print 'hh'
                
            bpe=bpesent[line]
            bpe=bpe.strip().split()
            tmp_bpe =[]
            for t_bpe in bpe:
                tmp_bpe.append(t_bpe)
            #print (all_word[0].word)
            #print (bpesent[line])
            line +=1
            num=0
            chlength=0
            #print len(all_word)
            # creat tree
            for word1 in all_word:
                for word2 in all_word:
                    #print word1.parentnum,word2.index
                    if word1.parentnum==word2.index :

                        word1.parent.append(word2)
                        word2.children.append(word1)
            eos = ['_','<EOS>','_','_','_','_','_','E','_','_']
            for j, word in enumerate(all_word):
                if word.parent==['ROOT']:
                    eos[6]=str(j+1)
                    e = node(eos,-1)
                    word.children.append(e)
                    e.parent.append(word)
                    all_word.append(e)
                s_bpe =[]
                chlength+=len(word.word)
                fullword=''
                full=False
                chlength1 =0
                for (bb,bbpe),(bbb,bbbpe) in zip(enumerate(tmp_bpe),enumerate(bpe)):
                    chlength1+=len(bbbpe.strip())
                    if bbpe.strip()!='' and bbpe.strip() in word.word and bbpe.strip() != word.word:
                        if bb==0 and bbpe.strip() in word.word and bbpe.strip()!= word.word and full== False:
                            s_bpe.append(bbpe)
                        elif bb>0 and word.word.startswith(bbpe.strip())== True and full ==False:
                            smallword =''
                            for sss in s_bpe:
                                smallword = smallword+ sss.strip()
                            smallword = smallword+bbpe.strip()
                            if smallword in word.word:
                                s_bpe.append(bbpe)
                                fullword = ''
                                if word.word.startswith(s_bpe[0].strip()) == True:
                                    for ss_bpe in s_bpe:
                                        fullword = fullword + ss_bpe.strip()
                                    if fullword.strip() == word.word.strip() and chlength ==chlength1:
                                        full=True
                                        fullword=''
                                        for i in range(bb):
                                            tmp_bpe[i]=''
                                        tmp_bpe[bb]=''
                                    else:
                                        full = False
                                else:
                                    s_bpe=[]
                            else:
                                    index=0
                                    while smallword not in word.word and s_bpe[-1]!='':
                                        smallword=''
                                        if s_bpe[index]!='':
                                            s_bpe[index]=''
                                            for ssss in s_bpe:
                                                smallword=smallword+ssss.strip()
                                        else:
                                            if index < len(s_bpe):
                                                s_bpe[index+1]=''
                                            for sssss in s_bpe:
                                                smallword = smallword+sssss.strip()
                                        index+=1
                                    s_bpe.append(bbpe)
                        elif bb>0 and tmp_bpe[bb-1].strip() in word.word and tmp_bpe[bb-1].strip()!=word.word and full==False:
                            smallword =''
                            for sss in s_bpe:
                                smallword = smallword + sss.strip()
                            smallword = smallword + bbpe.strip()
                            if smallword in word.word:
                                s_bpe.append(bbpe)
                                fullword = ''
                                if word.word.startswith(s_bpe[0].strip())==True:
                                    for ss_bpe in s_bpe:
                                        fullword=fullword + ss_bpe.strip()
                                    if fullword.strip() == word.word.strip() and chlength == chlength1:
                                        full = True
                                        fullword =''
                                        for i in range(bb):
                                            tmp_bpe[i]=''
                                        tmp_bpe[bb]=''
                                    else:
                                        full = False
                                else:
                                    s_bpe=[]
                            else:
                                index =0
                                while smallword not in word.word and s_bpe[-1]!='':
                                    smallword=''
                                    if s_bpe[index]!='':
                                        s_bpe[index]=''
                                        for ssss in s_bpe:
                                            smallword = smallword+ssss.strip()
                                    else:
                                        if index < len(s_bpe):
                                            s_bpe[index+1]=''
                                        for sssss in s_bpe:
                                            smallword = smallword + sssss.strip()
                                    index +=1
                                s_bpe.append(bbpe)
                if s_bpe !=[] and full == True:
                    #eos = ['_','<EOS>','_','_','_','_','_','E','_','_']

                    for bbb,b_bpe in enumerate(s_bpe):
                        b_line = ['_',b_bpe,'_','_','_','_','_','_','_','_']
                        
                        #b_line[6]=word.parentnum
                        b_line[6]=word.index 
                        b_line[7]=str(bbb)
                        #b_line[7]=str(bbb)+'_'+word.relation
                        small_num =str(word.index)+'_'+str(bbb)  
                        b=node(b_line,small_num)
                        #b.word = b_bpe
                        #b.relation =bbb
                        #print (b.word,b.relation,b.parentnum,word.parentnum)
                        #if word.parent!=[] and word.parent[0] !='ROOT':
                            
                            #all_word[j].parent[0].children.append(b)
                        
                            #b.parent.append(all_word[j].parent[0])
                        #elif word.parent!=[] and word.parent[0] =='ROOT':
                            
                            #b.parent=['ROOT']
                        #else:
                            #b.parent=[]
                        word.children.append(b)
                        b.parent.append(word)
                        all_word.append(b)
            final=[]
            for tok_word in bpe:
                only = False
                for a ,a_word in enumerate(all_word):
                    if a_word !='':
                        if tok_word.strip() == a_word.word.strip() and only==False:
                            final.append(a_word)
                            all_word[a]=''
                            only=True
            #all_false_path=[]
            if len(final)!=len(bpe):
                
                for i in final:
                    print (i.word+' ')
                all_false_path=[]
                print (len(final),len(bpe))
                #for i in range(len(bpe)**2):
                for i in range(len(bpe)):
                    all_false_path.append('None')
                for ll in all_false_path:
                    f.write(ll+' ')
                f.write('\n')
                all_word=[]
            else:
                all_path =[]
                for word3 in final:
                    #for word4 in final:
                        tmp1=[]
                        tmp2=[]
                        tmp_p1 = []
                        tmp_p2 = []
                        word3.get_allpath(tmp1)
                        #word4.get_allpath(tmp2)
                        word3.get_allparent(tmp_p1)
                        #print (tmp_p1)
                        hh =''
                        for pp in tmp_p1:
                            if pp !='ROOT':
                                hh =hh+ str(pp.relation)+'+'
                            else:
                                hh =hh+'ROOT'
                        if hh.strip() !='':
                            f.write(hh.replace('++','+').strip().rstrip('+')+' ')
                        else:
                            f.write('None'+' ')
                            
                        #word4.get_allparent(tmp_p2)
                        #if word3.word == word4.word and word3.parent ==word4.parent and word3.index == word4.index:
                            #all_path.append('None')
                        #elif word3 in word4.children:
                            #all_path.append('+'+word3.relation)
                        #elif word3 in word4.parent:
                            #all_path.append('-'+word4.relation)
                        #elif tmp1 !=[] and tmp2 !=[]:
                            #first = False
                            #end_path = ''
                            #end_index=10000
                            #end_all_path = ''
                            #for index1,tmp1_parent in enumerate(tmp_p1):
                                #if (tmp1_parent in tmp_p2) and (first == False):
                                    #end_parent = tmp1_parent
                                    #end_index = index1
                                    #first = True
                            #if end_index !=10000:
                                #for small_index in range(end_index):
                                    #end_all_path =end_all_path+tmp1[small_index]+'+'
                                #second = False
                                #end2_index = 10000
                                #for index2,tmp2_parent in enumerate(tmp_p2):
                                    #if tmp2_parent == end_parent and second == False:
                                        #second = True
                                        #end2_index= index2
                                #for small2_index in range(end2_index):
                                    #end_all_path = end_all_path+'-'+tmp2[end2_index-1-small2_index]

                            #if (end_all_path.startswith('-') is False) and (end_all_path.startswith('+') is False):
                            # print 'hh'
                                #end_all_path = '+' + end_all_path
                            #all_path.append(end_all_path.rstrip('+'))
                        #else:
                            #all_path.append('None')
                #for all_path_word in all_path:
                    #f.write(all_path_word.replace('+-','-').replace('+-','-').replace('++','+').replace('--','-')+' ')
                f.write('\n')
                all_word=[]

