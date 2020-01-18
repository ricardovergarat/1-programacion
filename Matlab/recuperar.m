clc
archivo = fopen('2.txt');
x = 0;
y = 5;
texto_completo = "";
while x < y
    linea = fgetl(archivo);
    disp("texto completo es: " + texto_completo);
    texto_completo = texto_completo + linea + char(13);
    disp("esto es linea: " + linea);
    x = x + 1;
end
fclose(archivo);
disp("esto importa");
disp(texto_completo);