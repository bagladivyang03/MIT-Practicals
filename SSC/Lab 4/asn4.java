/*
Kartik Bhutada, PC09
problem Statement:Design  suitable  data  structure  &  implement  pass  II  of  Two  Pass  Macro processor.
*/

import java.io.*;
import java.util.HashMap;
import java.util.Vector;

public class asn4 {


    public static void main(String[] Args) throws IOException{
        BufferedReader b1 = new BufferedReader(new FileReader("intermediate.txt"));
        BufferedReader b2 = new BufferedReader(new FileReader("mnt.txt"));
        BufferedReader b3 = new BufferedReader(new FileReader("mdt.txt"));
        BufferedReader b4 = new BufferedReader(new FileReader("kpdt.txt"));
        FileWriter f1 = new FileWriter("Output-Pass2.txt");
        HashMap<Integer,String> aptab=new HashMap<Integer,String>();
        HashMap<String,Integer> aptabInverse=new HashMap<String,Integer>();
        HashMap<String,Integer> mdtpHash=new HashMap<String,Integer>();
        HashMap<String,Integer> kpdtpHash=new HashMap<String,Integer>();
        HashMap<String,Integer> kpHash=new HashMap<String,Integer>();
        HashMap<String,Integer> macroNameHash=new HashMap<String,Integer>();
        Vector<String>mdt=new Vector<String>();
        Vector<String>kpdt=new Vector<String>();
        String s,s1;
        int i,pp,kp,kpdtp,mdtp,paramNo;
        while((s=b3.readLine())!=null)
            mdt.addElement(s);
        while((s=b4.readLine())!=null)
            kpdt.addElement(s);

        while((s=b2.readLine())!=null){
            String word[]=s.split("\t");
            s1=word[0]+word[1];
            macroNameHash.put(word[0],1);
            kpHash.put(s1,Integer.parseInt(word[2]));
            mdtpHash.put(s1,Integer.parseInt(word[3]));
            kpdtpHash.put(s1,Integer.parseInt(word[4]));
        }
        while((s=b1.readLine())!=null){
            String b1Split[]=s.split("\\s");
            if(macroNameHash.containsKey(b1Split[0])){
                pp= b1Split[1].split(",").length-b1Split[1].split("=").length+1;
                kp=kpHash.get(b1Split[0]+Integer.toString(pp));
                mdtp=mdtpHash.get(b1Split[0]+Integer.toString(pp));
                kpdtp=kpdtpHash.get(b1Split[0]+Integer.toString(pp));
                String actualParams[]=b1Split[1].split(",");
                paramNo=1;
                for(int j=0;j<pp;j++){
                    aptab.put(paramNo, actualParams[paramNo-1]);
                    aptabInverse.put(actualParams[paramNo-1],paramNo);
                    paramNo++;
                }
                i=kpdtp-1;
                for(int j=0;j<kp;j++){
                    String temp[]=kpdt.get(i).split("\t");
                    aptab.put(paramNo,temp[1]);
                    aptabInverse.put(temp[0],paramNo);
                    i++;
                    paramNo++;
                }
                i=pp+1;
                while(i<=actualParams.length){
                    String initializedParams[]=actualParams[i-1].split("=");
                    aptab.put(aptabInverse.get(initializedParams[0].substring(1,initializedParams[0].length())),initializedParams[1].substring(0,initializedParams[1].length()));
                    i++;
                }
                i=mdtp-1;
                while(mdt.get(i).compareToIgnoreCase("MEND")!=0){
                    f1.write("+ ");
                    for(int j=0;j<mdt.get(i).length();j++){
                    if(mdt.get(i).charAt(j)=='#')
                        f1.write(aptab.get(Integer.parseInt("" + mdt.get(i).charAt(++j))));
                    else
                        f1.write(mdt.get(i).charAt(j));
                }
                f1.write("\n");
                i++;
                }
                aptab.clear();
                aptabInverse.clear();
            }
            else
                f1.write("+ "+s+"\n");
        }
        b1.close();
        b2.close();
        b3.close();
        b4.close();
        f1.close();

        System.out.println("------------------------------------");
        BufferedReader file1 = new BufferedReader(new FileReader("Output-Pass2.txt"));
        while((s=file1.readLine())!=null){
            System.out.println(s);
        }
        System.out.println("------------------------------------");
        file1.close();
        
    }

}


/*
Input.txt:-
MACRO M1 &x,&y,&a=AREG,&b=
MOVE &a,&x
ADD &a,='1'
MOVER &a,&y
ADD &a,='5'
MEND
MACRO M2 &p,&q,&u=CREG,&v=DREG
MOVER &u,&p
MOVER &v,&q
ADD &u,='15'
ADD &v,='10'
MEND
M1 10,20,&b=CREG
M2 100,200,&u=AREG,&v=BREG

MNT:-
M1	2	2	1	1
M2	2	2	6	3

MDT:-
MOVE #3,#1
ADD #3,='1'
MOVER #3,#2
ADD #3,='5'
MEND
MOVER #3,#1
MOVER #4,#2
ADD #3,='15'
ADD #4,='10'
MEND

Intermediate code:-
M1 10,20,&b=CREG
M2 100,200,&u=AREG,&v=BREG

Key parameter definition table:-
a	AREG
b	-
u	CREG
v	DREG


OUTPUT:-
------------------------------------
+ MOVE AREG,10
+ ADD AREG,='1'
+ MOVER AREG,20
+ ADD AREG,='5'
+ MOVER AREG,100
+ MOVER BREG,200
+ ADD AREG,='15'
+ ADD BREG,='10'
------------------------------------

*/
