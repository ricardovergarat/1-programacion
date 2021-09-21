/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.entradas;

import java.util.Scanner;

/**
 *
 * @author Intel
 */
public class entrada {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int edad = Integer.parseInt(entrada.nextLine());
        System.out.println("usted tiene: " + edad);
        //Scanner entrada_2 = new Scanner(System.in);
        // TODO code application logic here
        
        
    }
    
}
