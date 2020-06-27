import random,copy
playerX=1
playerO=2
def ng():
    global board_pos,turn
    board_pos=['','','','','','','','','']
    turn=0
    player_select()
def player_select():
    pos=raw_input("Select the player -> 'X' or 'O': ")
    x=['x','o','X','O']
    while pos not in x:
        print "No such player, please select either 'X' or 'O'"
        pos=raw_input("Select the player -> 'X' or 'O': ")
    if pos=='x' or pos=='X':
        player=1
    else:
        player=2
    play(player)
def eligible(board_pos):
    empty_pos=[]
    eps=''
    for laddu in range(len(board_pos)):
        if board_pos[laddu]=='':
            empty_pos.append(laddu)
    for eps1 in empty_pos[:-1]:
        eps+=str(eps1+1)
        eps+=','
    eps+=str(empty_pos[-1]+1)
    print
    position_O=raw_input("Your Turn!    Enter position ("+eps+") :")
    if position_O.isdigit()==True:
        if int(position_O)>=1 and int(position_O)<=9 and (int(position_O)-1)  in empty_pos:
            position_O=int(position_O)-1
            status=True
        else:
            status=False
    else:
        status=False
    while status==False:
        position_O=raw_input("Your Turn!    Enter a valid numerical position ("+eps+") :")
        if position_O.isdigit()==True:
            if int(position_O)>=1 and int(position_O)<=9 and (int(position_O)-1)  in empty_pos:
                position_O=int(position_O)-1
                status=True
            else:
                continue
        else:
            continue
    return position_O
def play(player):
    global board_pos
    occu_pos=[] #occupied positions
    if player==2:
        start=random.randint(0,8)
        occu_pos.append(start)
        print "My Turn!"
        print
        board_pos[start]='x'
        print "Board: "
        board_print(board_pos)
        for j in range(4):
            position_O=eligible(board_pos)
            print
            print "Board: "
            board_pos[position_O]='o'
            board_print(board_pos)
            wl=check(board_pos,'o')
            if wl!='None':
                print "Hurray! You win. :)"
                break
            if j<=2:
                posswin=d_bs(board_pos,'x','w')
                if len(posswin)==1 and posswin!='None':
                    board_pos[posswin[0]]='x'
                else:
                    z=ed(board_pos,'x','x')
                    board_pos[z]='x'
                print
                print "My Turn!"
                print
                print "Board: "
                board_print(board_pos)
                wl=check(board_pos,'x')
                if wl!='None':
                    print
                    print "Yess!I win. ;)"
                    break
        else:
            for ele in range(len(board_pos)):
                if board_pos[ele]=='':
                    board_pos[ele]='X'
                else:
                    continue
            print
            print "My Turn!"
            print
            print "Board: "
            board_print(board_pos)
            wl=check(board_pos,'x')
            if wl!='None':
                print 'Yess!I win. ;)'
            else:
                print ":| Match Draw! Well played."
    elif player==1:
        print "Board: "
        board_print(board_pos)
        print
        position_X=eligible(board_pos)
        print
        print "Board: "
        board_pos[position_X]='x'
        board_print(board_pos)
        for j in range(4):
            posswin=d_bs(board_pos,'o','w')
            if len(posswin)==1 and posswin!='None':
                board_pos[posswin[0]]='o'
            else:
                z=ed(board_pos,'o','o')
                board_pos[z]='o'
            print
            print "My Turn!"
            print
            print "Board: "
            board_print(board_pos)
            wl=check(board_pos,'o')
            if wl!='None':
                print
                print "Yess!I win. ;)"
                break
            if j<=2:
                print
                position_X=eligible(board_pos)
                print
                print "Board: "
                board_pos[position_X]='x'
                board_print(board_pos)
                wl=check(board_pos,'x')
                if wl!='None':
                    print "Hurray! You win. :)"
                    break
        else:
            print
            position_X=eligible(board_pos)
            print
            print "Board: "
            board_pos[position_X]='x'
            board_print(board_pos)
            print
            wl=check(board_pos,'x')
            if wl!='None':
                print "Hurray! You win. :)"
            else:
                print ":| Match Draw! Well played."
            
def board_print(pos):
    # for empty cells give blank input
    n1=pos[0].capitalize()
    n2=pos[1].capitalize()
    n3=pos[2].capitalize()
    n4=pos[3].capitalize()
    n5=pos[4].capitalize()
    n6=pos[5].capitalize()
    n7=pos[6].capitalize()
    n8=pos[7].capitalize()
    n9=pos[8].capitalize()
    sec='---|---|---'
    div='|'
    s=" "
    if len(n1)==0:
        n1+=" "
    if len(n2)==0:
        n2+=" "
    if len(n3)==0:
        n3+=" "
    if len(n4)==0:
        n4+=" "
    if len(n5)==0:
        n5+=" "
    if len(n6)==0:
        n6+=" "
    if len(n7)==0:
        n7+=" "
    if len(n8)==0:
        n8+=" "
    if len(n9)==0:
        n9+=" "
    print s+n1+s+div+s+n2+s+div+s+n3+s
    print sec
    print s+n4+s+div+s+n5+s+div+s+n6+s
    print sec
    print s+n7+s+div+s+n8+s+div+s+n9+s
def check(l,player):
    if (l[0]==l[1]==l[2]==player):
        return 'c1'
    elif (l[3]==l[4]==l[5]==player):
        return 'c2'
    elif (l[6]==l[7]==l[8]==player):
        return 'c3'
    elif (l[0]==l[4]==l[8]==player):
        return 'd1'
    elif (l[2]==l[4]==l[6]==player):
        return 'd2'
    elif (l[0]==l[3]==l[6]==player):
        return 'r1'
    elif (l[1]==l[4]==l[7]==player):
        return 'r2'
    elif (l[2]==l[5]==l[8]==player):
        return 'r3'
    else:
        return 'None'
def d_bs(l,p,n):          # d_bs= direct best search, l= list, p=player, n=nature
    swe=[]      #sub win elements
    for i in range(0,9,3):          #for columns
        x=[]
        x.append(l[i])
        x.append(l[i+1])
        x.append(l[i+2])
        x.append('c'+str((i/3)+1))
        swe.append(x)
    for j in range(3):              #for rows
        x=[]
        x.append(l[j])
        x.append(l[j+3])
        x.append(l[j+6])
        x.append('r'+str(j+1))
        swe.append(x)
    x=[]
    x.append(l[0])
    x.append(l[4])
    x.append(l[8])
    x.append('d1')
    swe.append(x)
    x=[]
    x.append(l[2])
    x.append(l[4])
    x.append(l[6])
    x.append('d2')
    swe.append(x)
    pos_mov=[]
    if n=='w':
        if p=='x':                  #computer x ko jitana chahata h
            for se in swe:
                x=se[:-1]
                if 'o' in x:
                    continue
                else:
                    z=0
                    for u in x:
                        if u=='x':
                            z+=1
                    if z==2:
                        pos_mov.append(se)
                    else:
                        continue
        elif p=='o':                #computer o ko jitana chahata h
            for se in swe:
                x=se[:-1]
                if 'x' in x:
                    continue
                else:
                    z=0
                    for u in x:
                        if u=='o':
                            z+=1
                    if z==2:
                        pos_mov.append(se)
                    else:
                        continue
    elif n=='l':
        if p=='x':                  #computer x ko hrwana chahata h
            for se in swe:
                x=se[:-1]
                if 'o' in x:
                    continue
                else:
                    z=0
                    for u in x:
                        if u=='x':
                            z+=1
                    if z==2:
                        pos_mov.append(se)
                    else:
                        continue
        elif p=='o':                #computer o ko hrwana chahata h
            for se in swe:
                x=se[:-1]
                if 'x' in x:
                    continue
                else:
                    z=0
                    for u in x:
                        if u=='o':
                            z+=1
                    if z==2:
                        pos_mov.append(se)
                    else:
                        continue
    brumm=[]
    for o in pos_mov:
        l=o[-1]
        for z in range(3):
            if o[z]=='':
                count=z
        if l=='r1':
            count*=3
        elif l=='r2':
            count=((count*3)+1)
        elif l=='r3':
            count=((count*3)+2)
        elif l=='c1':
            count*=1
        elif l=='c2':
            count+=3
        elif l=='c3':
            count+=6
        elif l=='d1':
            count*=4
        elif l=='d2':
            count=((count+1)*2)
        brumm.append(count)
    if brumm!=[]:
        return brumm
    else:
        return 'None'
def ed(l,p,wp):
    epos=[]
    for i in range(len(l)):
        if l[i]=='':
            epos.append(i)
    data=[]
    for j in epos:
        temp=copy.copy(l)
        temp[j]=p
        if p=='x':
            p_='o'
        elif p=='o':
            p_='x'
        y=esd(temp,p_,wp)
        score=0
        for k in y:
            score+=((k[0][0])*k[1])
        f=[j,score]
        data.append(f)
    max_score=data[0][1]
    mu=data[0]
    for u in data:
        if u[1]>max_score:
            max_score=u[1]
            mu=u
    return mu[0]
def esd(l,p,wp):        #ed=exhaustive specific data, l=board_pos, p=player
    pb=[]
    pb.append(l)
    ter=[]
    step=0
    while pb!=[]:
        step+=1
        npb=[]          #new pb
        if wp=='x':
            oowp='o'
        elif wp=='o':
            oowp='x'
        for board in pb:
            rp=[]           #replacable positions
            for pos in range(len(board)):
                if board[pos]=='':
                    rp.append(pos)
                else:
                    continue
            for i in rp:
                temp=copy.copy(board)
                temp[i]=p
                s1=check(temp,wp)
                s2=check(temp,oowp)
                noneeit=0           #no of non empty elements in temp
                for k in temp:
                    if k!='':
                        noneeit+=1
                if s1!='None':
                    x=[1]
                    x.append(step)
                    ter.append(x)
                elif s2!='None':
                    x=[-1]
                    x.append(step)
                    ter.append(x)
                elif s1=='None' and s2=='None' and noneeit==9:
                    x=[0]
                    x.append(step)
                    ter.append(x)
                else:
                    npb.append(temp)
        pb=npb
        if p=='x':
            p='o'
        elif p=='o':
            p='x'
    answer=peter(ter)          #process ter
    return answer
def peter(c):
    u=[]
    for i in c:
        if i not in u:
            u.append(i)
    ans=[]
    for k in u:
        count=0
        x=[k]
        for j in c:
            if j==k:
                count+=1
            else:
                continue
        x.append(count)
        ans.append(x)
    return ans    
def pos_gen():
    n=random.randint(1,9)
    l=['','','','','','','','','']
    start=random.randint(1,2)
    if start==1:
        sp='x'
        if n%2==0:
            nx=n/2
            no=nx
        else:
            no=n/2
            nx=n-no
    else:
        sp='o'
        if n%2==0:
            nx=n/2
            no=nx
        else:
            nx=n/2
            no=n-nx
    occu_pos=[]
    for i in range(nx):
        pos=random.randint(0,8)
        while pos in occu_pos:
            pos=random.randint(0,8)
        occu_pos.append(pos)
        l[pos]='x'
    for j in range(no):
        pos=random.randint(0,8)
        while pos in occu_pos:
            pos=random.randint(0,8)
        occu_pos.append(pos)
        l[pos]='o'
    if n%2==0:
        if sp=='x':
            ep='o'
        elif sp=='o':
            ep='x'
    else:
        if sp=='x':
            ep='x'
        elif sp=='o':
            ep='o'
    d=[]
    d.append(l)
    d.append(sp)
    d.append(ep)
    return d
def run():
    for i in range(100):
        x=pos_gen()
        y=check(x[0],x[2])
        print i+1,"     ",'Starting Pos: ',x[1],',',"       ",'Ending Pos:  ',x[2]
        print
        print 'Board'
        print
        board_print(x[0])
        if y!='None':
            print
            print y
        print "-----------------------------------------------------------------------------------------------------------------------"
        
def board_print(pos):
    # for empty cells give blank input
    n1=pos[0].capitalize()
    n2=pos[1].capitalize()
    n3=pos[2].capitalize()
    n4=pos[3].capitalize()
    n5=pos[4].capitalize()
    n6=pos[5].capitalize()
    n7=pos[6].capitalize()
    n8=pos[7].capitalize()
    n9=pos[8].capitalize()
    sec='---|---|---'
    div='|'
    s=" "
    if len(n1)==0:
        n1+=" "
    if len(n2)==0:
        n2+=" "
    if len(n3)==0:
        n3+=" "
    if len(n4)==0:
        n4+=" "
    if len(n5)==0:
        n5+=" "
    if len(n6)==0:
        n6+=" "
    if len(n7)==0:
        n7+=" "
    if len(n8)==0:
        n8+=" "
    if len(n9)==0:
        n9+=" "
    print s+n1+s+div+s+n2+s+div+s+n3+s
    print sec
    print s+n4+s+div+s+n5+s+div+s+n6+s
    print sec
    print s+n7+s+div+s+n8+s+div+s+n9+s
def trial1():
    count=1
    for k in range(1000):
        y=pos_gen()
        if y[2]=='x':
            cp='o'
        else:
            cp='x'
        z=ed(y[0],cp,cp)
        scores=[]
        for i in z:
            score=0
            for j in i:
                if j[0][0]==1:
                    score+=(1*j[1])
                elif j[0][0]==-1:
                    score-=(1*j[1])
            scores.append(score)
        m=peter(scores)
        for l in m:
            if l[1]>1:
                print count,y,z
                count+=1
                print '------------------------------------------------------------------------------------------------------'
                
        
    

