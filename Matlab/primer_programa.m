clc
disp("ahora abriremos el archivo");
archivo = fopen('2.txt');
y = 0
el_texto = "";
while y < 3
    linea = fgetl(archivo);
    display("estamos en la linea: " + y + " y su texto es: " + linea)
    el_texto = el_texto + "\n" + linea;
    y = y + 1;
end
disp("el texto completo es: " + el_texto);

fclose(archivo);
disp("todo salio bien");