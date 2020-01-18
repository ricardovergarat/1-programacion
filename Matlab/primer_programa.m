clc
archivo = fopen('2.txt',"w");
fprintf(archivo,'%s',char(13));
fclose(archivo);
x = 0;
intento = 1;
while x < 60
	matrix = rand(2);
	string_matrix = mat2str(matrix);
	string_intento = num2str(intento);
	archivo = fopen('2.txt');
	y = 0;
	texto_archivo = "";
	while y < x + 1
		linea = fgetl(archivo);
		texto_archivo = texto_archivo  + linea + char(13);
		y = y + 1;
    end
    fclose(archivo);
    nueva_linea = texto_archivo + "intento: " + string_intento + " " + string_matrix;
	archivo = fopen('2.txt',"w");
	fprintf(archivo,'%s',nueva_linea);
	fclose(archivo);
	intento = intento + 1;
	x = x + 1;
end
disp("100%");