clc
cantidad = 97;
x = 0;
intento = 66;
while x < 3
	%matrix = rand(2);
	%string_matrix = mat2str(matrix);
	%string_intento = num2str(intento);
	archivo = fopen('3.txt');
	y = 0;
	texto_archivo = "";
	while y < ( (100 - cantidad))
		linea = fgetl(archivo);
        disp("linea: " + linea);
		texto_archivo = texto_archivo  + linea + char(13);
		y = y + 1;
    end
    fclose(archivo);
    disp("---------------------");
    disp("texto completo: " + texto_archivo);
    disp("---------------------");
    %nueva_linea = texto_archivo + "intento: " + string_intento + " " + string_matrix;
    %disp("este es el texto acumulado");
    %disp(nueva_linea);
	%archivo = fopen('3.txt',"w");
	%fprintf(archivo,'%s',nueva_linea);
	%fclose(archivo);
	intento = intento + 1;
	x = x + 1;
end
disp("100%");