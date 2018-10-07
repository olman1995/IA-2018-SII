/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto.ii.ia;
import net.sf.clipsrules.jni.*;
/**
 *https://www.youtube.com/watch?v=YsiMFLNXrjc
 * @author olman
 */
public class ProyectoIIIA {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here}
        int numero=5;
        Environment clips;
        clips = new Environment();
        clips.load(".\\src\\proyecto\\ii\\ia\\base_conocimiento\\setup.CLP");
        clips.reset();
        clips.eval("(assert (p1 "+numero+"))");
        clips.run();
        String res=clips.getInputBuffer();
        System.out.println(res);
    }
    
}
