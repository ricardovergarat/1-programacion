clc
clear
warning('off','YALMIP:strict') 
load prueba1
maxAux2=1
h2 = 1

Theta1m= -0.1;
Theta1M= 0.2;
Theta2m = -0.03;
Theta2M = 0.4;
for i=0:8
    h1 = 0;
    h2 = h2+1;
    x1 = 1;
    x2 = 1;
    x3 = 1;
    while h1 < 100
        h1
        h2
        x1 = x1+1;
        x2 = x2*x1;
        x3 = x3*x1*x2;
        if x1 > 10
            x1 = 1;
        end
        if x2 > 50
            x2 = 1;
        end
        if x3 > 20
            x3 = 1;
        end
    %x = rand(1,18);
    
    
    
    A0=[rand(h2,h2)]-eye(h2);
    A0
    A1=[rand(h2,h2)]-eye(h2);
    A2=[rand(h2,h2)]-eye(h2);
    
    %%%%%%%%%%%%%%%%%%%%%%%%
    
    
    
    
 for i=1:20 
     for j=1:20
         TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m);
         TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m);
        
                
         Axx= A0 +TETHA1*A1+TETHA2*A2;

         Re_sys(i,j)=max(real(eig(Axx)));

            end
    end
        maxAux=max(max(Re_sys));
        disp("esto es el maximo");
        disp(maxAux);
        
 if  maxAux>0
        A0x=A0-eye(h2)*maxAux*0.8 ;
        A1x=A1-eye(h2)*maxAux*0.8;
        A2x=A2-eye(h2)*maxAux*0.8;
        
 for i=1:20 
      for j=1:20
        TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m);
        TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m);
        Axx2= A0x +TETHA1*A1x+TETHA2*A2x;
        Re_sys2(i,j)=max(real(eig(Axx2)));

            end
        end   
 maxAux2=max(max(Re_sys2));
 
 
 end
                
        if maxAux2<0
         An{1} = {[0 0],A0x};
         An{2} = {[1 0],A1x};
         An{3} = {[0 1],A2x};

         Arolm= rolmipvar(An,'A',[Theta1m Theta1M ;
                                  Theta2m Theta2M ]);
        % size(A1,1)
        P11 = rolmipvar(h2,h2,'P11','symmetric',[2 2],[0 0]);

        LMIx=Arolm'*P11+P11*Arolm;


            LMIs = [LMIx<0,P11>0];

            


    sol = solvesdp(LMIs, [], sdpsettings('solver', 'sedumi', 'verbose', 0));



    output.cpusec = sol.solvertime;

    output.p = min(checkset(LMIs));
output.p
    output.cpusec = sol.solvertime;

    output.p = min(checkset(LMIs));
    % checkset(LMIs)

    output.V = size(getvariables(LMIs),2);
    output.L = 0;
    for i=1:size(LMIs,1)
        output.L = output.L + size(LMIs{i},1);
    end
    output.feas = 0;

    W=double(P11);
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if (output.p > 0)
        h1 = h1+1;
        ArqCom{h2,h1}.A0=A0x;
        ArqCom{h2,h1}.A1=A1x;
        ArqCom{h2,h1}.A2=A2x;
        ArqCom{h2,h1}.Theta1m=Theta1m;
        ArqCom{h2,h1}.Theta1M=Theta1M;
        ArqCom{h2,h1}.Theta2m=Theta2m;
        ArqCom{h2,h1}.Theta2M=Theta2M;
        ArqCom{h2,h1}.output=output;
        Grafica(h2,h1)=output.cpusec;
        save prueba1 ArqCom;
    end
        end
        
        
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



    if(maxAux>-30 && maxAux<0)
         An{1} = {[0 0],A0x};
         An{2} = {[1 0],A1x};
         An{3} = {[0 1],A2x};

         Arolm= rolmipvar(An,'A',[Theta1m Theta1M ;
                              Theta2m Theta2M ]);
        % size(A1,1)
        P11 = rolmipvar(h2,h2,'P11','symmetric',[2 2],[0 0]);

        LMIx=Arolm'*P11+P11*Arolm;


        LMIs = [LMIx<0,P11>0];



        sol = solvesdp(LMIs, [], sdpsettings('solver', 'sedumi', 'verbose', 0));



        output.cpusec = sol.solvertime;

        output.p = min(checkset(LMIs));

        output.cpusec = sol.solvertime;

        output.p = min(checkset(LMIs));
        % checkset(LMIs)

        output.V = size(getvariables(LMIs),2);
        output.L = 0;
        
        
    for i=1:size(LMIs,1)
        output.L = output.L + size(LMIs{i},1);
    end
    
    
    output.feas = 0;

    W=double(P11);
    
    if (output.p > 0)
        h1 = h1+1;
        ArqCom{h2,h1}.A0=A0x;
        ArqCom{h2,h1}.A1=A1x;
        ArqCom{h2,h1}.A2=A2x;
        ArqCom{h2,h1}.Theta1m=Theta1m;
        ArqCom{h2,h1}.Theta1M=Theta1M;
        ArqCom{h2,h1}.Theta2m=Theta2m;
        ArqCom{h2,h1}.Theta2M=Theta2M;
        ArqCom{h2,h1}.output=output;
        Grafica(h2,h1)=output.cpusec;
        save prueba1 ArqCom

    end
    end
    end
    
end
%comet(Grafica)
save prueba1 ArqCom
clear
load prueba1