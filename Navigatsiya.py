def navig(xr,yr,x0,y0,xk,yk,sprx,spry):
    spr=[]
    for i in range(len(sprx)):
        spr.append([sprx[i],spry[i]])
    kpr=len(spr)
    err=True
    karta=[[-2 for i in range(yr)]for j in range(xr)]
    karta[x0][y0]=0
    karta[xk][yk]=-3
    for i in spr:
        karta[i[0]][i[1]]=-1
    a=[]
    a.append([x0,y0])
    for i in range((xr*yr)-kpr):
        if len(a)==0:
            err=False
            break
        l=a.pop(0)
        x,y=l[0],l[1]
        ll=[x-1,y]
        lp=[x+1,y]
        ln=[x,y+1]
        lv=[x,y-1]
        if x>-1 and x<xr and y>-2 and y<yr-1:
            if karta[x][y+1]<-1:
                karta[x][y+1]=karta[x][y]+1
                a.append([x,y+1])
        if x>-1 and x<xr and y>0 and y<yr+1:
            if karta[x][y-1]<-1:
                karta[x][y-1]=karta[x][y]+1
                a.append([x,y-1])
        if x>-2 and x<xr-1 and y>-1 and y<yr:
            if karta[x+1][y]<-1:
                karta[x+1][y]=karta[x][y]+1
                a.append([x+1,y])
        if x>0 and x<xr+1 and y>-1 and y<yr:
            if karta[x-1][y]<-1:
                karta[x-1][y]=karta[x][y]+1
                a.append([x-1,y])
        if karta[xk][yk]!=-3:
            break
    if err:
        spos=[]
        spos.append([[xk,yk]])
        kolpov=[]
        for i in range(karta[xk][yk]):
            n=karta[xk][yk]-i-1
            lenspos=len(spos)
            for j in range(lenspos):
                jspos=spos[0]
                sposi=[]
                t=jspos[i]
                x,y=t[0],t[1]
                tl=[x-1,y]
                tp=[x+1,y]
                tn=[x,y+1]
                tv=[x,y-1]
                if x>-1 and x<xr and y>-2 and y<yr-1:
                    if karta[x][y+1]==n:
                        sposi.append(tn)  
                if x>-1 and x<xr and y>0 and y<yr+1:
                    if karta[x][y-1]==n:
                        sposi.append(tv)
                if x>-2 and x<xr-1 and y>-1 and y<yr:
                    if karta[x+1][y]==n:

                        sposi.append(tp)
                if x>0 and x<xr+1 and y>-1 and y<yr:
                    if karta[x-1][y]==n:
                        sposi.append(tl)
                for c in sposi:
                    gad=[]
                    for h in jspos:
                        gad.append(h)
                    gad.append(c)
                    spos.append(gad)
                spos.pop(0)
        kolp=[0 for i in range(len(spos))]
        for i in range(len(spos)):
            for j in range(len(spos[i])-2):
                x0,y0=spos[i][j][0],spos[i][j][1]
                x1,y1=spos[i][j+1][0],spos[i][j+1][1]
                x2,y2=spos[i][j+2][0],spos[i][j+2][1]
                if (x1-x2)!=(x0-x1):
                    kolp[i]+=1
        nom=0
        for i in range(len(kolp)-1):
            if kolp[i+1]<kolp[i]:
                nom=i+1
        spos=spos[nom][::-1]
        sposok=[]
        for i in spos:
            sposok.append(i)
        return(sposok)
    else:
        return([])
def elem(m,a,b):
    return m[a][b]
def len1(m):
    return len(m)