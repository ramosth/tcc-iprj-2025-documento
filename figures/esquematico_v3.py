import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Arc, FancyArrowPatch
import numpy as np
plt.rcParams['font.family']='DejaVu Sans'
LW=1.6; C='black'
fig,ax=plt.subplots(figsize=(13,8.2)); ax.set_aspect('equal'); ax.axis('off')
def L(*pts): 
    xs,ys=zip(*pts); ax.plot(xs,ys,color=C,lw=LW,solid_capstyle='round')
def dot(x,y): ax.add_patch(plt.Circle((x,y),0.11,color=C,zorder=5))
def T(x,y,s,**k): ax.text(x,y,s,**{'fontsize':11,'ha':'center','va':'center',**k})
def box(x0,y0,x1,y1,title,ts=13):
    ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,fill=False,lw=LW,ec=C)); 
    T((x0+x1)/2,(y0+y1)/2,title,fontsize=ts,fontweight='bold')
def pin(x,y,name,side):
    # small pin stub with label inside the box
    if side=='L': L((x-0.5,y),(x,y)); T(x+0.15,y,name,ha='left',fontsize=10.5)
    else: L((x,y),(x+0.5,y)); T(x-0.15,y,name,ha='right',fontsize=10.5)
def led(x0,y,label):
    # anode at x0, cathode at x0+1.2 ; triangle pointing right
    a=x0+0.25; b=a+0.6
    L((x0,y),(a,y)); L((b,y),(x0+1.2,y))
    ax.add_patch(Polygon([(a,y-0.32),(a,y+0.32),(b,y)],closed=True,fill=False,lw=LW,ec=C))
    L((b,y-0.32),(b,y+0.32))
    for dx in (0.0,0.25):
        ax.add_patch(FancyArrowPatch((a+0.2+dx,y+0.38),(a+0.55+dx,y+0.78),arrowstyle='-|>',mutation_scale=9,lw=1.1,color=C))
    T(x0+1.45,y+0.32,label,fontsize=10,ha='left')
def ground(x,y):
    L((x,y),(x,y-0.35))
    for i,w in enumerate((0.45,0.3,0.15)): L((x-w,y-0.35-i*0.14),(x+w,y-0.35-i*0.14))

# ---------------- NodeMCU ----------------
mx0,mx1,my0,my1=10,15.5,3.2,12
box(mx0,my0,mx1,my1,'ESP8266\nNodeMCU V3',14)
yL={'USB-C':11.0,'3V3':9.2,'A0':7.4,'GND':5.6}
yR={'D1':11.0,'D2':9.5,'D3':8.0,'D4':6.5,'GND':4.4}
for n,y in yL.items(): pin(mx0,y,n,'L')
for n,y in yR.items(): pin(mx1,y,n,'R')

# ---------------- Alimentação ----------------
box(2.6,10.3,6.4,11.7,'Carregador\nUSB 5 V / 1 A',11)
L((6.4,11.0),(mx0-0.5,11.0)); T((6.4+mx0-0.5)/2+0.25,11.45,'cabo USB-C (5 V)',fontsize=10)

# ---------------- Higrômetro ----------------
hx0,hx1,hy0,hy1=3.2,7.4,0.0,4.6
ax.add_patch(Rectangle((hx0,hy0),hx1-hx0,hy1-hy0,fill=False,lw=LW,ec=C)); T(hx0+1.65,2.3,'Módulo\nhigrômetro\n(LM393)',fontsize=10.5,fontweight='bold')
hp={'VCC':4.0,'A0':3.0,'GND':2.0,'D0':0.8}
for n,y in hp.items(): pin(hx1,y,n,'R')
ax.texts[-4].set_position((hx1-0.15,4.0))
# rotas módulo -> NodeMCU (canais verticais)
for n_mod,n_mcu,xc in (('VCC','3V3',8.2),('A0','A0',8.6),('GND','GND',9.0)):
    y0=hp[n_mod]; y1=yL[n_mcu]
    L((hx1+0.5,y0),(xc,y0),(xc,y1),(mx0-0.5,y1))
L((hx1+0.5,0.8),(hx1+0.9,0.8)); T(hx1+1.25,0.8,'n.c.',fontsize=9.5)
# pinos da sonda no módulo
for n,y in (('+',3.4),('−',1.6)): 
    L((hx0-0.5,y),(hx0,y)); T(hx0+0.15,y,n,ha='left',fontsize=11)
box(-0.2,1.0,1.9,4.0,'Sonda\nFC-28',11)
for n,y in (('+',3.4),('−',1.6)):
    L((1.9,y),(hx0-0.5,y)); T(1.75,y,n,ha='right',fontsize=11)

# ---------------- LEDs ----------------
xg=26.0
for pinname,lab in (('D1','LED azul (nível VERDE)'),('D2','LED amarelo (nível AMARELO)'),('D3','LED vermelho (nível VERMELHO)')):
    y=yR[pinname]; xs=mx1+0.5
    L((xs,y),(17.6,y)); led(17.6,y,lab); L((18.8,y),(xg,y)); dot(xg,y)
# ---------------- Buzzer ----------------
y=yR['D4']; xa,xb=19.0,20.0
L((mx1+0.5,y),(xa,y)); L((xb,y),(xg,y)); dot(xg,y)
base=y-0.55
L((xa,y),(xa,base)); L((xb,y),(xb,base))
L((xa-0.45,base),(xb+0.45,base))
ax.add_patch(Arc(((xa+xb)/2,base),1.9,1.9,theta1=180,theta2=360,lw=LW,color=C))
T(xa-0.2,y-0.3,'+',fontsize=11); T(xb+0.22,y-0.3,'−',fontsize=12)
T(21.6,base-0.55,'Buzzer ativo\nTMB-12A03',fontsize=10,ha='left')
# ---------------- GND ----------------
L((mx1+0.5,yR['GND']),(xg,yR['GND']))
L((xg,yR['D1']),(xg,yR['GND'])); dot(xg,yR['GND'])
ground(xg,yR['GND'])
ax.set_xlim(-0.6,27.0); ax.set_ylim(-0.4,12.4)
plt.savefig('/tmp/sch/esquematico_v3.png',dpi=200,bbox_inches='tight',facecolor='white',pad_inches=0.15)
