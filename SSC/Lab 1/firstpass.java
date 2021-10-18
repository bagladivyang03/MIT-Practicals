import java.io.*;
import java.util.*;
import java.lang.*;

class OpTable {
	String s_class;
	int m_code;
	
	OpTable setupValues(String S, int m) {
		OpTable op = new OpTable();
		op.s_class = S;
		op.m_code = m;
		return op;
	}
}

class FlagTable {
	int f_code;
	
	FlagTable setupValues(int m) {
		FlagTable fp = new FlagTable();
		fp.f_code = m;
		return fp;
	}
}

class RegTable {
	int r_code;
	
	RegTable setupValues(int m) {
		RegTable rp = new RegTable();
		rp.r_code = m;
		return rp;
	}
}

class SymbolTable {
	int index;
	int address;
	int size;
	SymbolTable setupValues(int i, int m, int n) {
		SymbolTable sp = new SymbolTable();
		sp.index = i;
		sp.address = m;
		sp.size = n;
		return sp;
	}
}

class LiteralTable {
	int address;
	int index;
	LiteralTable setupValues(int i, int m) {
		LiteralTable lp = new LiteralTable();
		lp.index = i;
		lp.address = m;
		return lp;
	}
}

public class firstpass {

	static boolean isNumeric(final CharSequence cs)
	{
		final int sz = cs.length();
		for (int i = 0; i < sz; i++) {
			if(!Character.isDigit(cs.charAt(i))) {
				return false;
			}
		}
		return true;
	}

	static int instructionType(String linePart) {
		String[] is_instructions = {"STOP", "ADD", "SUB", "MULT", "MOVER", "MOVEM", "COMP", "BC", "DIV", "READ", "PRINT"};
		String[] dl_instructions = {"DC", "DS"};
		String[] ad_instructions = {"START", "END", "EQU", "ORIGIN", "LTORG"};

		if (Arrays.asList(is_instructions).contains(linePart)) {
			return 1;
		}
		if (Arrays.asList(dl_instructions).contains(linePart)) {
			return 2;
		}
		if (Arrays.asList(ad_instructions).contains(linePart)) {
			return 3;
		}
		return 0;
	}

	static int isWhat(String linePart) {
		String[] instructions = {"STOP", "ADD", "SUB", "MULT", "MOVER", "MOVEM", "COMP", "BC", "DIV", "READ", "PRINT", "DC", "DS", "START", "END", "ORIGIN", "EQU", "LTORG"};
		String[] registers = {"AREG", "BREG", "CREG", "DREG"};
		if(Arrays.asList(instructions).contains(linePart)) {
			//Is instruction
			return 1;
		}
		
		else if(Arrays.asList(registers).contains(linePart)) {
			//Is Register
			return 2;
		}

		else if (isNumeric(linePart)) {

			return 3;
		}
		
		else if (linePart.charAt(0)=='='){
			//Is Literal
			return 5;
		}

		else {
			//Is label
			return 4;
		}
	}

	static void InterCode(Map<String, OpTable> optable, Map<String, FlagTable> fptable, Map<String, RegTable> rptable, Map<String, SymbolTable> sptable, Map<String, LiteralTable> lptable) {
		
		try 
		{
			String fname = "C:\\Users\\Divyang\\Desktop\\Final Year B.Tech\\T9\\SSC\\SSC FINAL CODES\\ssc prac 1\\prog.txt";
			FileWriter f1 = new FileWriter("IC.txt");
			File f = new File(fname);
			FileReader fr;
			fr = new FileReader(f);
			BufferedReader br = new BufferedReader(fr);
			String line;
			int location_counter = 0;
			int literal_counter= 0;
			int symbol_counter = 0;
			//doy:
			while((line = br.readLine()) != null) {
				String[] lineParts = line.split(" ", 0);
				int i = 0;
				int status = isWhat(lineParts[0]);
				f1.write(location_counter+")");
				if (status == 4) {
					//Is Label
					OpTable op = optable.get(lineParts[i]);
					if(lineParts[i].equals("DC")){
						f1.write("("+op.s_class+",0"+op.m_code+")\n");
					}
					if(lineParts[i].equals("DS")){
						f1.write("("+op.s_class+",0"+op.m_code+")\n");
					}
					SymbolTable sp = new SymbolTable();
					sptable.put(lineParts[i], sp.setupValues(symbol_counter, location_counter, 1));
					f1.write("(S,"+symbol_counter+")");
					symbol_counter++;
					i++;					
				}
				status = isWhat(lineParts[i]);
				if(status == 1) {
					//Instruction
					int instructionType = instructionType(lineParts[i]);
					OpTable op = optable.get(lineParts[i]);

					if (instructionType == 1) {
						//is IS

						if(lineParts[i].equals("STOP")){
							f1.write("("+op.s_class+",0"+op.m_code+")\n");
						}

						if(lineParts[i].equals("ADD") || lineParts[i].equals("MOVER")||lineParts[i].equals("MOVEM") || lineParts[i].equals("SUB")||lineParts[i].equals("MULT") || lineParts[i].equals("DIV")||lineParts[i].equals("COMP")){
							int part1_type = isWhat(lineParts[i+1]);
							int part2_type = isWhat(lineParts[i+2]);
							String part1_text = null,part2_text = null;
							if(part1_type == 2) {
								RegTable rp = rptable.get(lineParts[i+1]);
								part1_text = "("+rp.r_code+")";
							}

							if(part1_type == 5) {
								LiteralTable lp = new LiteralTable();
								lptable.put(lineParts[i+1], lp.setupValues(literal_counter, 0));
								part1_text = "("+Integer.toString(literal_counter)+")";
								literal_counter++;
							}

							if(part1_type == 4) {
								SymbolTable sp = new SymbolTable();
								sptable.put(lineParts[i+1], sp.setupValues(symbol_counter, 0, 1));
								part1_text = "("+symbol_counter+")";
								symbol_counter++;
							}

							if(part2_type == 2) {
								RegTable rp = rptable.get(lineParts[i+2]);
								part2_text = "("+rp.r_code+")";
							}

							if(part2_type == 5) {
								LiteralTable lp = new LiteralTable();
								lptable.put(lineParts[i+2], lp.setupValues(literal_counter, 0));
								part2_text = "("+Integer.toString(literal_counter)+")";
								literal_counter++;
							}

							if(part2_type == 4) {
								SymbolTable sp = new SymbolTable();
								sptable.put(lineParts[i+2], sp.setupValues(symbol_counter, 0, 1));
								part2_text = "("+symbol_counter+")";
								symbol_counter++;
							}

							f1.write("("+op.s_class+",0"+op.m_code+")"+part1_text+part2_text+"\n");
						}

						if(lineParts[i].equals("BC")){
							f1.write("("+op.s_class+","+op.m_code+")");
							FlagTable fp = fptable.get(lineParts[i+1]);
							f1.write("("+fp.f_code+")\n");
							int part1_type = isWhat(lineParts[i+1]);
						}

						if(lineParts[i].equals("READ")){
							int part1_type = isWhat(lineParts[i+1]);
							SymbolTable sp = new SymbolTable();
							sptable.put(lineParts[i+1], sp.setupValues(symbol_counter, 0, 1));
							String part1_text = "("+symbol_counter+")";
							symbol_counter++;
							f1.write("("+op.s_class+",0"+op.m_code+")"+part1_text+"\n");
						}

						if(lineParts[i].equals("PRINT")){
							int part1_type = isWhat(lineParts[i+1]);
							SymbolTable sp = new SymbolTable();
							sptable.put(lineParts[i+1], sp.setupValues(symbol_counter, 0, 1));
							String part1_text = "("+symbol_counter+")";
							symbol_counter++;
							f1.write("("+op.s_class+",0"+op.m_code+")"+part1_text+"\n");
						}
					}

					if (instructionType == 2) {
						//is DL
						if(lineParts[i].equals("DC")){
							f1.write("("+op.s_class+",0"+op.m_code+")\n");
						}
						if(lineParts[i].equals("DS")){
							f1.write("("+op.s_class+",0"+op.m_code+")\n");
						}
					}

					if (instructionType == 3) {
						//is AD

						if(lineParts[i].equals("START")){

							f1.write("("+op.s_class+",0"+op.m_code+")"+"(C,"+lineParts[i+1]+")\n");
							location_counter = Integer.parseInt(lineParts[i+1])-1;
						}

						if(lineParts[i].equals("LTORG")){
							//process literals here
							//Internal Pool Table Tracking
							int flag = 0;
							List<String> key = new ArrayList<String>(lptable.keySet());
							//Collections.reverse(key);
							// System.out.println(key);
							for (int j = key.size()-1; j >= 0; j--){
								// System.out.println(key.get(j));
							//for (String key: keys) {
								if (flag == 1) {
									f1.write(location_counter+")");
								}
								if (lptable.get(key.get(j)).address == 0) {
									//System.out.println(lptable.get(key.get(j)));
									LiteralTable lp = new LiteralTable();
									int literal_counter_internal = lptable.get(key.get(j)).index;
									// System.out.println("Index"+literal_counter_internal);
									lptable.replace(key.get(j), lp.setupValues(literal_counter_internal,location_counter));
									location_counter++;
									flag = 1;
									f1.write("("+op.s_class+",0"+op.m_code+")"+"(DL,02)"+"(C,"+key.get(i).charAt(2)+")\n");
								}
							}
							flag = 1
;						}

						if(lineParts[i].equals("EQU")) {
							f1.write("("+op.s_class+",0"+op.m_code+")\n");
						}

						if(lineParts[i].equals("END")){
							//process literals here
							//Internal Pool table tracking
							f1.write("("+op.s_class+",0"+op.m_code+")\n");
							List<String> key = new ArrayList<String>(lptable.keySet());
							for (int j = key.size()-1; j >= 0; j--){
							//for (String key: keys) {
								if (lptable.get(key.get(j)).address == 0) {
									LiteralTable lp = new LiteralTable();
									int literal_counter_internal = lptable.get(key.get(j)).index;
									lptable.put(key.get(j), lp.setupValues(literal_counter_internal,location_counter));
									location_counter++;
								}
							}
						}

						if(lineParts[i].equals("ORIGIN")){
							f1.write("("+op.s_class+",0"+op.m_code+")"+"(C,"+lineParts[i+1]+")\n");
							location_counter = Integer.parseInt(lineParts[i+1]);
						}
					}
				}
				i = 0;
				location_counter++;
			}
			f1.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}

		System.out.println("\nSymbolTable");
		for (Map.Entry<String, SymbolTable> entry : sptable.entrySet()) {
		    System.out.println(entry.getKey() + ":" + entry.getValue().address + " " + entry.getValue().size);
		}
		System.out.println("\nLiteralTable");
		for (Map.Entry<String, LiteralTable> entry : lptable.entrySet()) {
		    System.out.println(entry.getKey() + ":" + entry.getValue().address);
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		OpTable op = new OpTable();
		Map<String, OpTable> optable = new HashMap<String, OpTable>();
		optable.put("STOP", op.setupValues("IS", 0));
		optable.put("ADD", op.setupValues("IS", 1));
		optable.put("SUB", op.setupValues("IS", 2));
		optable.put("MULT", op.setupValues("IS", 3));
		optable.put("MOVER", op.setupValues("IS", 4));
		optable.put("MOVEM", op.setupValues("IS", 5));
		optable.put("COMP", op.setupValues("IS", 6));
		optable.put("BC", op.setupValues("IS", 7));
		optable.put("DIV", op.setupValues("IS", 8));
		optable.put("READ", op.setupValues("IS", 9));
		optable.put("PRINT", op.setupValues("IS", 10));
		optable.put("DC", op.setupValues("DL", 1));
		optable.put("DS", op.setupValues("DL", 2));
		optable.put("START", op.setupValues("AD", 1));
		optable.put("END", op.setupValues("AD", 2));
		optable.put("ORIGIN", op.setupValues("AD", 3));
		optable.put("EQU", op.setupValues("AD", 4));
		optable.put("LTORG", op.setupValues("AD", 5));
		
		FlagTable fp = new FlagTable();
		Map<String, FlagTable> fptable = new HashMap<String, FlagTable>();
		fptable.put("LT", fp.setupValues(1));
		fptable.put("LE", fp.setupValues(2));
		fptable.put("EQ", fp.setupValues(3));
		fptable.put("GT", fp.setupValues(4));
		fptable.put("GE", fp.setupValues(5));
		fptable.put("ANY", fp.setupValues(6));
		
		RegTable rp = new RegTable();
		Map<String, RegTable> rptable = new HashMap<String, RegTable>();
		rptable.put("AREG", rp.setupValues(1));
		rptable.put("BREG", rp.setupValues(2));
		rptable.put("CREG", rp.setupValues(3));
		rptable.put("DREG", rp.setupValues(4));

		Map<String, SymbolTable> sptable = new LinkedHashMap<String, SymbolTable>();

		Map<String, LiteralTable> lptable = new HashMap<String, LiteralTable>();

		InterCode(optable, fptable, rptable, sptable, lptable);
				
	}
}

/*OUTPUT
E:\SSC>java firstpass
0)(AD,01)(C,400)
400)(IS,01)(1)(0)
401)(S,1)(IS,02)(2)(2)
402)(AD,03)(C,300)
301)(IS,04)(3)(3)    
302)(IS,04)(1)(0)    
303)(IS,04)(3)(1)   
304)(AD,05)(DL,02)(C,5)   
305)(AD,05)(DL,02)(C,3)   
307)(AD,03)(C,700)      
701)(IS,04)(1)(2)       
702)(IS,04)(3)(3)       
703)(S,4)(DL,01)   
704)(S,5)(DL,01)   
705)(AD,02)       

SymbolTable       
S1:703 1          
L2:401 1         
S2:704 1        

LiteralTable     
='5':304         
='3':305        
='8':705         
='7':706  
*/