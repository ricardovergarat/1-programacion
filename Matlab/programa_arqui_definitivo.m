clc           %---------> esto limpia los mostrado por consola anteriormente
orden = 2;
intentos = 604; %---------> poner el ultimo intento del archivo, si es el primero poner 1
cantidad = 40;  %---------> cuantas matrices quieres agregar al archivo, este programa esta hecho de tal forma que impleca que usted tiene 100 - cantidad  de matricez en el archivo 
Theta1m = 0.25;
Theta1M = 0.4;
Theta2m = 1;
Theta2M = 3;
string_orden = num2str(orden);
nombre_archivo = string_orden + ".txt";
x = 0;
while x < cantidad
    matrix_A0 = rand(orden);
    matrix_A1 = rand(orden);
    matrix_A2 = rand(orden);
    %-----------------------------
    % candidatos
    
    su_matrix_simetrica = eye(orden) * 2; % por si no recuerdan la simetrica es cuando SOLO la diagional es 1
    A0= matrix_A0 - su_matrix_simetrica;
    A1= matrix_A1 - su_matrix_simetrica;
    A2= matrix_A2 - su_matrix_simetrica;
    
    for i=1:20
        for j=1:20
    TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m);
    TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m);
    
    Axx= A0 +TETHA1*A1+TETHA2*A2;
    ReA_sys(i,j)=max(real(eig(Axx)));
        end
    end
    
    if ReA_sys > 0
        disp("No es candidato");
        intentos  = intentos + 1;
    else
        % operacion isaic
        disp("Es candidato");
        
        algo = 1;
        
        if algo == 1
            %|||||||||||||||||||||||||||||
            % aqui trataremos de determinar la estabilidad del sistema
        
            An{1} = {[0 0],A0}; % exponente a cada alfa
            An{2} = {[1 0],A1};
            An{3} = {[0 1],A2};
        
            Arolm= rolmipvar(An,'A',[Theta1m Theta1M ; % creacion de caja con sus valores en los vertices
                                    Theta2m Theta2M ]);
                      
            P11 = rolmipvar(2,2,'P11','symmetric',[2 2],[0 0]); % sin punto

            LMIx = Arolm'*P11+P11*Arolm; % sin punto
        
                LMIs = [LMIx<0,P11>0];
        
            sol = solvesdp(LMIs, [], sdpsettings('solver', 'sedumi', 'verbose', 0));
        
            cpusec = sol.solvertime; % -------> esto se supone que es el tiempo

            p = min(checkset(LMIs)); % esto es lo bueno  si es positvo es estable

            % checkset(LMIs)

            V = size(getvariables(LMIs),2); % -------> ni puta idea 
            L = 0; % --------------------------------> que mierda esto siempre sera 0
        
            for i=1:size(LMIs,1)
                L = L + size(LMIs{i},1);
            end
            feas = 0; % --------------------------------> esta igual sera 0, que wea
        
            W=double(P11);
        
            disp("esto es P: " + p);
            %|||||||||||||||||||||||||||||
        
            %
            if p > 0
                disp("Es estable");
                disp("Esta es la matrix: " + W);
                disp("el sistema se demoro: " + cpusec);
                disp("Estamos en el intento: " + intentos);
                y = 0;
                archivo = fopen(nombre_archivo);
                texto_archivo = "";
                while y < (100 - cantidad)
                    linea = fgetl(archivo);
                    texto_archivo = texto_archivo  + linea + char(13);
                    y = y + 1;
                end
                fclose(archivo);
                disp("texto completo: " + texto_archivo);
                string_matrix = mat2str(W);
                string_intento = num2str(intentos);
                %disp(string_matrix);
                nueva_linea = texto_archivo + "intento: " + string_intento + " " + string_matrix;
                archivo = fopen(nombre_archivo,"w");
                fprintf(archivo,'%s',nueva_linea);
                fclose(archivo);
                intentos = intentos + 1;
                x = x + 1;
            else
                disp("No es estable");
                intentos = intentos + 1;
            end
          
        else
            disp("proceso isaic determino que no es candidato");
        end
        
    end
end
disp("100 %");