clc
clear

Theta1m= 0.1;
Theta1M= 0.4;
Theta2m = -0.03;
Theta2M = 0.02;

matrixA0 = rand(2);
matrixA1 = rand(2);
matrixA2 = rand(2);


esom = eye(2) * 3;
A0= matrixA0 - esom;
A1= matrixA1 - esom;
A2= matrixA2 - esom;

for i=1:20
    for j=1:20
TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m);
TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m);
        
Axx= A0 +TETHA1*A1+TETHA2*A2;
%disp("axx :" + Axx);

%Re_sys(i,j)=max(abs(eig(Axx)))
ReA_sys(i,j)=max(real(eig(Axx)));
    end
end

%mesh(ReA_sys);
if ReA_sys > 0
    disp("No es cantidato");
else
    disp("es candidato");
end
