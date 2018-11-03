#with open('C:\Users\gedonglai\Desktop\\art1.txt', 'a') as f:
# num = 0
# for arg,jufa in zip(open('C:\Users\gedonglai\Desktop\\test2.txt', 'r'),open('C:\Users\gedonglai\Desktop\\testf.txt', 'r')):
#     arg = arg.strip().split()
#     jufa = jufa.strip().split()
#     for ii,i in enumerate(arg):
#         if i not in jufa :
#             num+=1
# print num
class node:
    def __init__(self):
        self.word =''
        self.child = []
        self.parent = []
        self.srl=''
        self.num=None
        self.parent_num= ''
    def givenum(self,tok):
        if self.parent !=[]:
            #print 'hh'
            child_tmp = self.parent.child
            for i,children in enumerate(child_tmp):
                if children.child ==[]:
                    #print 'hh'
                    if isinstance(children.num,int) and children.word in tok:
                        if i-1>=0:
                            #print'hh'
                            if self.parent.child[i-1].num ==None:
                                #print 'hh'
                                self.parent.child[i-1].num = children.num -0.1
    def getmin(self):
        if self.child!=[] and self.num ==None:
            num_tmp =[]
            for i,children in enumerate(self.child):
                num_tmp.append(children.num)
            num_tmp.sort()
            #print num_tmp
            self.num = num_tmp[0]





    # def getmax(self):
    #     if self.child ==[]:
    #         self.max = self.num
    #     else:
    #         maxnum=[]
    #         for children in self.child:
    #             if children.num !=None :
    #                 maxnum.append(children.num)
    #         if maxnum!=[]:
    #             self.max = max(maxnum)
    #         else:
    #             self.max = None
    def sort_children(self):
        if self.child !=[]:
            num = True
            for children in self.child:
                if children.num == None:
                    num = False
            if num == True:
                child_tmp = []
                num_tmp = []
                for i,ch in enumerate(self.child):
                    num_tmp.append(ch.num)
                num_tmp.sort()
                for j in range(len(num_tmp)):
                    for h,child in enumerate(self.child):
                        if num_tmp[j] == child.num:
                            child_tmp.append(child)
                self.child= child_tmp
                #print child_tmp
        # if self.child !=[]:
        #     num = False
        #     for children in self.child:
        #         if children.num !=None:
        #             num = True
        #     if num ==True:
        #         child_tmp=[]
        #         num_tmp=[]
        #         for i,children in enumerate(self.child):
        #             child_tmp.append(children)
        #             if children.word not in tok :
        #                 print children.word
        #                 if i+1 < len(self.child):
        #                     print self.child[i+1].num
        #                     children.num = self.child[i+1].num-0.1
        #             num_tmp.append(children.num)
        #         self.child=[]
        #         num_tmp.sort()
        #         for i in range(len(num_tmp)):
        #             for j,childrenj in enumerate(child_tmp):
        #                 if childrenj.num == num_tmp[i]:
        #                     self.child.append(childrenj)

    def prin(self,tok,e):

        if self.srl=='':
            e.append(self.word)
        else:
            if self.word not in tok :
                if self.child ==[]:
                    e.append(self.word)
                else:
                #print self.word+self.srl
                    e.append(self.word+self.srl)
            else:
                e.append(self.word)
        if self.child !=[]:
            for i in self.child:
                if i not in tok :
                    i.prin(tok,e)
    def all_parent(self,tmp):
        a= self.parent

        tmp.append(a.parent_num)
        while a.parent !=[]:
            a = a.parent

            tmp.append(a.parent_num)
ww=0
with open('C:\Users\gedonglai\Desktop\\tc1025.txt', 'a') as f:
    #for jufa,srl,tok in zip(open('C:\Users\gedonglai\Desktop\\testjufa.txt', 'r'),open('C:\Users\gedonglai\Desktop\\test515.txt', 'r'),open('C:\Users\gedonglai\Desktop\\testtok.txt', 'r')):
    for jufa, tok,bpe in zip(open('C:\Users\gedonglai\Desktop\\tjufa1.txt', 'r'),open('C:\Users\gedonglai\Desktop\\ttok1.txt', 'r'),open('C:\Users\gedonglai\Desktop\\tbpe1.txt', 'r')):
        if jufa.strip() !='':
            parent_num=0
            chlength = 0
            #srl =srl.strip().split()
            tok = tok.strip().split()
            bpe = bpe.strip().split()
            jufa = jufa.strip().split()
            #bpe.pop()
            tmp_bpe = []
            for t_bpe in bpe:
                tmp_bpe.append(t_bpe)
            allin = True
            #stok = stok.strip().split()
            for token in tok:
                if token not in jufa :
                    allin = False
            if allin == True:

                e = []
                list = []
                all_node =[]
                all_node2=[]
                for jufa_word in jufa:
                    tmp = []
                    ttmp=[]
                    if jufa_word not in ['(',')']:
                        a =node()
                        a.word = jufa_word
                        pp = False
                        # for p,stok_word in enumerate(stok):
                        #     if jufa_word == stok_word and pp ==False:
                        #         a.num = p
                        #         pp = True
                        #         stok[p]=''

                        #print a.word,a.num
                        # flag=False
                        # for j,srl_word in enumerate(srl):
                        #     if len(srl_word.split('**'))>1:
                        #         if a.word == srl_word.split('**')[-1] and flag ==False:
                        #             for i in range(len(srl_word.split('**'))-1):
                        #
                        #                 a.srl=a.srl+srl_word.split('**')[i]
                        #             #print a.srl
                        #
                        #             srl[j]=''
                        #             flag=True
                        list.append(a)
                        all_node.append(a)
                    elif jufa_word=='(':

                        list.append(jufa_word)
                    elif jufa_word==')':
                        if len(list)>0:
                            b =list.pop()
                            if b != '(':
                                tmp.append(b)
                            while b!='(':
                                b= list.pop()
                                if b!='(':
                                    tmp.append(b)
                        # for iii in tmp:
                        #     print iii.word
                        # print'______'
                        if len(tmp)>1:
                            hh=''
                            for oo in tmp:
                                if oo.srl!='':
                                    hh=oo.srl

                            for ooo in tmp:
                                if ooo.word not in tok:
                                    if ooo.srl =='':
                                        ooo.srl = hh

                        if len(list)>=1:
                            end_node = list.pop()
                            while len(tmp)>0:
                                ttmp.append(tmp.pop())
                            parent_num+=1

                            for ttt,tt in enumerate(ttmp):
                                #print ttt,tt.word

                                if tt not in tok and ttt % 2 == 0:

                                    # no bpe path
                                    end_node.child.append(tt)
                                    end_node.parent_num=end_node.word+'_'+str(parent_num)
                                    tt.parent = end_node
                                if ttt %2 != 0 :
                                    #print tt.word
                                    s_bpe = []
                                    #print chlength
                                    chlength+=len(tt.word)
                                    #print chlength
                                    fullword = ''
                                    full = False
                                    chlength1 = 0
                                    for (bb, bbpe) ,(bbb,bbbpe) in zip(enumerate(tmp_bpe),enumerate(bpe)):
                                        # print bbpe,tt.word
                                        # fullword = ''
                                        chlength1+=len(bbbpe.strip().rstrip('_').lstrip('_').strip())
                                        #print chlength1
                                        if bbpe.strip().rstrip('_').lstrip('_').strip()!=''and bbpe.strip().rstrip('_').lstrip('_').strip() in tt.word and bbpe.strip().rstrip('_').lstrip('_').strip() != tt.word :
                                            #print 'hh'
                                        #     s_bpe.append(bbpe)
                                        #     for ss_bpe in s_bpe:
                                        #         fullword = fullword+ss_bpe.rstrip('_').lstrip('_').strip()
                                        #     print fullword
                                        #     if fullword == tt.word:
                                        #         print 'hh'
                                        #         full = True
                                        #         fullword = ''
                                        #     else:
                                        #         full = False
                                        #     tmp_bpe[bb]=''
                                            if bb == 0 and (bbpe.strip().rstrip('_').lstrip('_').strip() in tt.word )and bbpe.strip().rstrip('_').lstrip('_').strip() != tt.word and full == False :
                                                #print 'hh'
                                                s_bpe.append(bbpe)

                                            elif bb>0 and tt.word.startswith(bbpe.strip().rstrip('_').lstrip('_').strip()) == True and full==False:
                                                #print 'hh'
                                                smallword =''
                                                for sss in s_bpe:
                                                    smallword = smallword+sss.strip().rstrip('_').lstrip('_').strip()
                                                #print smallword
                                                smallword = smallword+bbpe.strip().rstrip('_').lstrip('_').strip()
                                                if smallword in tt.word:
                                                    s_bpe.append(bbpe)
                                                    fullword = ''
                                                    if tt.word.startswith(s_bpe[0].strip().lstrip('_').rstrip('_').strip()) == True:
                                                        for ss_bpe in s_bpe:
                                                            fullword = fullword + ss_bpe.strip().rstrip('_').lstrip('_').strip()
                                                        #print fullword, tt.word, chlength, chlength1
                                                        if fullword.strip() == tt.word.strip() and chlength == chlength1:
                                                            # print chlength,chlength1
                                                            # print fullword,tt.word
                                                            full = True
                                                            fullword = ''
                                                            for i in range(bb):
                                                                tmp_bpe[i] = ''
                                                            tmp_bpe[bb] = ''

                                                        else:
                                                            full = False
                                                    else:
                                                        s_bpe = []
                                                else:
                                                        index = 0
                                                        while smallword not in tt.word and s_bpe[-1] != '':
                                                            # print index
                                                            smallword = ''
                                                            if s_bpe[index] != '':
                                                                s_bpe[index] = ''
                                                                for ssss in s_bpe:
                                                                    smallword = smallword + ssss.strip().lstrip(
                                                                        '_').rstrip('_').strip()
                                                            else:
                                                                if index < len(s_bpe):
                                                                    s_bpe[index + 1] = ''
                                                                for sssss in s_bpe:
                                                                    smallword = smallword + sssss.strip().lstrip(
                                                                        '_').rstrip('_').strip()
                                                            index += 1
                                                        s_bpe.append(bbpe)
                                                # for ss_bpe in s_bpe:
                                                #     fullword = fullword + ss_bpe.rstrip('_').lstrip('_').strip()
                                                # print fullword,tt.word
                                                # if fullword.strip() == tt.word.strip() :
                                                #     print fullword ,tt.word
                                                #
                                                #     full = True
                                                #     fullword = ''
                                                # else:
                                                #     full = False
                                                #tmp_bpe[bb] = ''
                                            elif bb > 0 and (tmp_bpe[bb - 1].strip().rstrip('_').lstrip('_').strip() in tt.word )and tmp_bpe[bb - 1].strip().rstrip('_').lstrip('_').strip() != tt.word and full == False:
                                                smallword =''
                                                for sss in s_bpe:
                                                    smallword = smallword+sss.strip().rstrip('_').lstrip('_').strip()
                                                smallword = smallword + bbpe.strip().rstrip('_').lstrip('_').strip()
                                                if smallword in tt.word:
                                                    s_bpe.append(bbpe)
                                                    #print s_bpe
                                                    fullword = ''
                                                    if tt.word.startswith(s_bpe[0].strip().lstrip('_').rstrip('_').strip())==True:

                                                        for ss_bpe in s_bpe:
                                                            fullword = fullword + ss_bpe.strip().rstrip('_').lstrip('_').strip()
                                                        #print fullword,tt.word ,chlength,chlength1
                                                        if fullword.strip() == tt.word.strip() and chlength == chlength1:
                                                            #print chlength,chlength1
                                                            #print fullword,tt.word
                                                            full = True
                                                            fullword = ''
                                                            for i in range(bb):
                                                                tmp_bpe[i]=''
                                                            tmp_bpe[bb] =''

                                                        else:
                                                            full = False
                                                    else:
                                                        s_bpe=[]
                                                else:
                                                    index=0
                                                    while smallword not in tt.word and s_bpe[-1]!='':
                                                        #print index
                                                        smallword=''
                                                        if s_bpe[index]!='':
                                                            s_bpe[index]=''
                                                            for ssss in s_bpe:
                                                                smallword = smallword+ssss.strip().lstrip('_').rstrip('_').strip()
                                                        else:
                                                            if index < len(s_bpe):
                                                                s_bpe[index+1]=''
                                                            for sssss in s_bpe:
                                                                smallword = smallword+sssss.strip().lstrip('_').rstrip('_').strip()
                                                        index += 1
                                                    s_bpe.append(bbpe)
                                                #tmp_bpe[bb] = ''
                                    #print s_bpe
                                    if s_bpe != [] and full ==True:
                                        #print s_bpe
                                        for bbb, b_bpe in enumerate(s_bpe):
                                            b = node()
                                            b.word = b_bpe
                                            c = node()
                                            c.word = bbb
                                            ttmp[ttt - 1].child.append(c)
                                            ttmp[ttt - 1].parent_num = ttmp[ttt - 1].word + '_' + str(parent_num)
                                            c.parent = ttmp[ttt - 1]
                                            c.child.append(b)
                                            c.parent_num = str(c.word) + '_' + str(parent_num)
                                            b.parent = c


                                            all_node.append(b)
                                            for nnn,nn in enumerate(all_node):
                                                if nn ==tt:
                                                    all_node[nnn]=''
                                    else:
                                        ttmp[ttt - 1].child.append(tt)
                                        ttmp[ttt - 1].parent_num = ttmp[ttt - 1].word + '_' + str(parent_num)
                                        tt.parent = ttmp[ttt - 1]
                                    parent_num+=1
                                    #print 'hh'
                                    # no bpe path
                                    # ttmp[ttt-1].child.append(tt)
                                    # ttmp[ttt-1].parent_num=ttmp[ttt-1].word+'_'+str(parent_num)
                                    # tt.parent = ttmp[ttt-1]

                            #print end_node.word
                            list.append(end_node)
                syntax = []
                for nod in all_node:
                    #f.write(nod.parent_num+' ')
                    # if nod.word not in tok:
                    # if nod.parent !=[]:
                    #     print nod.word,nod.parent.word,nod.parent.parent_num
                    #print nod.word
                    # if nod !='':
                    #     print nod.word
                    if nod !='' and nod.child ==[]:
                        #print nod.word
                        syntax.append(nod)
                        #print len(syntax)
                final =[]
                for tok_word in bpe:
                    #print tok_word
                    only = False
                    for ssy,syntax_word in enumerate(syntax):
                        #print syntax_word.word
                        if syntax_word !='':
                            #print syntax_word.word
                            if tok_word.strip().lstrip('_').rstrip('_').strip() ==syntax_word.word.strip().lstrip('_').rstrip('_').strip() and only==False:
                                #print tok_word,syntax_word.word
                                final.append(syntax_word)
                                syntax[ssy]=''
                                only=True
                    #exit()
                # for iiiii in final:
                #     print iiiii.word
                if len(final)!= len(bpe):
                    print len(final),len(bpe)
                    ww +=1
                    length2 = len(bpe)**2
                    for i in range(length2):
                        f.write('0' + ' ')
                    f.write('\n')
                else:
                # for ff in final:
                #         f.write(ff.word+' ')
                    all_pn=''
                    for num_1,tok_word_1 in enumerate(final):
                    #     if tok_word_1.parent != []:
                    #         tmp_1 = []
                    #         tok_word_1.all_parent(tmp_1)
                    #         #print tmp_1
                    #         end_1 =[]
                    #         end_2 =''
                    #         for tt in tmp_1:
                    #             if tt.split('_')[0] not in end_1:
                    #                 end_1.append(tt.split('_')[0])
                    #         for ee in end_1:
                    #             end_2 = end_2+str(ee)+'+'
                    #         #print end_2
                    #         if end_2.strip() !='':
                    #             f.write(end_2.strip().rstrip('+')+' ')
                    #         else:
                    #             f.write('None'+' ')
                    #     else:
                    #         f.write('None'+' ')
                    # f.write('\n')
                        for num_2,tok_word_2 in enumerate(final):
                            if num_1<num_2:
                                all_pn="+"
                            elif num_1>num_2:
                                all_pn="-"
                            if tok_word_1.parent!=[] and tok_word_2.parent !=[]:
                                if tok_word_1.word == tok_word_2.word and tok_word_1.parent.parent_num == tok_word_2.parent.parent_num:
                                    f.write( "0"+ ' ')
                                else:
                                    if tok_word_1.parent !=[] and tok_word_2.parent !=[]:
                                        tmp_1 =[]
                                        tmp_2 =[]
                                        tok_word_1.all_parent(tmp_1)
                                        #print tmp_1
                                        tok_word_2.all_parent(tmp_2)
                                        nowrite = False
                                        first = False
                                        end_parent=''
                                        end_index=10000
                                        end_path=''
                                        #print tmp_1,tmp_2
                                        for index1,tmp1_parent in enumerate(tmp_1):

                                                #print type(tmp_parent)
                                                if (tmp1_parent in tmp_2 )and (first == False):
                                                    end_parent=tmp1_parent
                                                    end_index=index1
                                                    #f.write(tmp_parent.split('_')[0]+' ')
                                                    first = True
                                                    #nowrite=True
                                        if end_index !=10000:
                                            for small_index in range(end_index):
                                                tt_path = end_path
                                                tt_path=tt_path.replace('+',' ')
                                                tt_path = tt_path.replace('-', ' ')
                                                if tt_path.strip()!='':

                                                    tt_path = tt_path.strip().split()[-1]
                                                if tmp_1[small_index].split('_')[0] != tt_path:
                                                    end_path = end_path+tmp_1[small_index].split('_')[0]+'+'
                                                else:
                                                    end_path = end_path
                                            #end_path = end_path+tmp_1[0].split('_')[0]+'+'
                                            tt_path = end_path
                                            tt_path = tt_path.replace('+', ' ')
                                            tt_path = tt_path.replace('-', ' ')
                                            if tt_path.strip() != '':
                                                tt_path = tt_path.strip().split()[-1]
                                            if tmp_1[end_index].split('_')[0] != tt_path:
                                                end_path = end_path+tmp_1[end_index].split('_')[0]
                                            else:
                                                end_path = end_path
                                            second = False
                                            end2_index =10000
                                            for index2,tmp2_parent in enumerate(tmp_2):
                                                if tmp2_parent == end_parent and second==False:
                                                    second=True
                                                    end2_index=index2
                                            for small2_index in range(end2_index):
                                                #print end_path
                                                tt_path = end_path.rstrip('+')
                                                tt_path = tt_path.replace('+', ' ')
                                                tt_path = tt_path.replace('-', ' ')
                                                if tt_path.strip()!='':

                                                    tt_path = tt_path.strip().split()[-1]
                                                if tmp_2[end2_index-1-small2_index].split('_')[0] != tt_path:
                                                    end_path =end_path.rstrip('+')+'-'+ tmp_2[end2_index-1-small2_index].split('_')[0]
                                                else:
                                                    end_path = end_path
                                            #end_path = end_path+'-'+tmp_2[0].split('_')[0]
                                            #select fixed length path


                                            f.write(all_pn+str(len(end_path.strip().replace('+',' ').replace('-',' ').strip().split()))+' ')
                                            nowrite=True

                                        if nowrite== False:
                                                f.write('0'+' ')
                                    else:
                                        f.write('0' + ' ')
                            else:
                                f.write('0' + ' ')
                    f.write('\n')
                            # if the same word :None
                            # if tok_word_1.parent!=[] and tok_word_2.parent !=[]:
                            #     if tok_word_1.word == tok_word_2.word and tok_word_1.parent.parent_num ==tok_word_2.parent.parent_num:
                            #         f.write('None'+' ')
                            #     else:
                            #         #print tok_word_1.parent.word, tok_word_2.parent.word
                            #         if tok_word_1.parent!=[] and tok_word_2.parent !=[]:
                            #             if tok_word_1.parent.parent_num ==tok_word_2.parent.parent_num:
                            #                 f.write(tok_word_1.parent.word+' ')
                            #                 #print 'hh'
                            #
                            #             else:
                            #                 tmp_1=[]
                            #                 tmp_2=[]
                            #
                            #                 tok_word_1.all_parent(tmp_1)
                            #                 tok_word_2.all_parent(tmp_2)
                            #                 nowrite= False
                            #                 first = False
                            #                 for tmp_parent in tmp_1:
                            #
                            #                     #print type(tmp_parent)
                            #                     if (tmp_parent in tmp_2 )and (first == False):
                            #
                            #                         f.write(tmp_parent.split('_')[0]+' ')
                            #                         first = True
                            #                         nowrite=True
                            #                 if nowrite== False:
                            #                     f.write('None'+' ')
                            #         else:
                            #             f.write('None'+' ')
                            # else:
                            #     f.write('None' + ' ')
            else:
                length1 = len(bpe)**2
                for i in range(length1):
                    f.write('0' + ' ')
                f.write('\n'+' ')
                #     if nod.child !=[]:
                #         keyi = False
                #         wo = False
                #         for children in nod.child:
                #             if children.srl !='' and wo == False:
                #                 tmpsrl=nod.child[0].srl
                #                 wo = True
                #             else:
                #                 tmpsrl = ''
                #         for children in nod.child:
                #             #if children.srl !='':
                #                 if tmpsrl != children.srl:
                #                     tmpsrl =''
                #         nod.srl=tmpsrl
                            #if children.word in tok :
                                # if nod.srl=='':
                                #     nod.srl=children.srl
                                # else:
                                #     if nod.srl !=children.srl:
                                #         nod.srl=''
            # for nod in all_node:
            #     if len(nod.child)>0:
            #         print nod.word,nod.srl
            #         print '+++++'
            #         for i in nod.child:
            #             print i.word,i.srl
            #     print '--------'

            # re = []
            # while len(all_node)>0:
            #     re.append(all_node.pop())
            # for ree in re:
            #     #ree.getmin()
            #     #print ree.word,ree.num
            #     #f.write(ree.word)
            #     if ree.word not in tok:
            #         if ree.child !=[]:
            #             tmpsrl2=ree.child[0].srl
            #             for children in ree.child:
            #                 if tmpsrl2 != children.srl:
            #                     tmpsrl2 = ''
            #             ree.srl = tmpsrl2
            # for ree in re:
            #     ree.sort_children()
            # for ree in re:
            #     if ree.word not in tok:
            #         if ree.parent !=[]:
            #             if ree.parent.srl == ree.srl:
            #                 ree.srl = ''
                            #if children.word in tok :
                                # if ree.srl=='':
                                #     ree.srl=children.srl
                                # else:
                                #     if ree.srl !=children.srl:
                                #         ree.srl='_'

            # for r in re:
            #     if r.parent ==[]:
            #         r.prin(tok,e)

            #f.write(str(e))
        else:
            tok = tok.strip().split()
            length = len(bpe)**2
            for i in range(length):
                f.write('0'+' ')
            f.write('\n')
print ww






