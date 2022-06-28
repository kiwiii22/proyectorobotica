syms cq1 cq2 sq1 sq2 x1 x2 y1 y2 a3 z1 l1 l2 l3 q1 q2 q3
syms Xn1 Xn2 Xn3 Xn Yn1 Yn2 Yn3 Yn Zn1 Zn2 Zn3 Zn

"parametros del robot"
l1=0.35    
l2=0.60
l3=0.15

"punto deseado"
Xn=0.6
Yn=0
Zn=0.2

cq1=cos(q1)
cq2=cos(q2)
cq3=cos(q3)

sq1=sin(q1)
sq2=sin(q2)
sq3=sin(q3)

x2=l2*cq2 
y2=l2*sq2
x3=l3*cq3
y3=l3*sq3

    
T2 = [1 0 0 0 ;
      0 0 -1 0 ;
      0 1 0 0 ;
      0 0 0 1 ]
     
T1 = [cq1 -sq1 0 0  ;
      sq1 cq1 0 0  ;
       0 0 1 l1 ;
       0 0 0 1 ] 
  
T01=T1*T2

T12 = [ cq2 -sq2 0 x2 ;
        sq2 cq2 0 y2;
        0 0 1 0 ;
        0 0 0 1 ]
     

     
T23 = [cq3 -sq3 0 x3 ;
        sq3 cq3 0 y3 ;
        0 0 1 0 ;
        0 0 0 1 ]
    
T=simplify(T01*T12*T23)


"Matriz de simbolos"
"Xn= posicion en X deseada"
"Yn= posicion en y deseada"
"Zn= posicion en z deseada"

Tn = [ Xn1 Xn2 Xn3 Xn ;
       Yn1 Yn2 Yn3 Yn ;
       Zn1 Zn2 Zn3 Zn ;
       0 0 0 1 ]
    
"Primer paso encontrar inversas de T01 Y T01"


"Inversa de la primera transformacion"

T10=inv(T01)

"Inversa de la segunda transformacion"

T21=inv(T12)

"Pruimera igualdad entre matrices"

T1=simplify(T10*Tn)


T2=simplify(T12*T23)



"Segunda igualdad"



T3=simplify(T21*T10*Tn)




a=T1(1,4)==T2(1,4)
b=T1(2,4)==T2(2,4)
c=T1(3,4)==T2(3,4)



d=T3(1,4)==T23(1,4)
e=T3(2,4)==T23(2,4)
f=T3(3,4)==T23(3,4)


equs=[a,b,c,d,e,f];

s=solve(equs,[q1,q2,q3])

Qn1=round(s.q1*180/pi)
Qn2=round(s.q2*180/pi)
Qn3=round(s.q3*180/pi)