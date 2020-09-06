package assn7;
import java.util.*;
import java.sql.*;

public class jdbc {
	public static void main(String [] args) {
		try {
		Class.forName("com.mysql.jdbc.Driver");
		Connection c = 	DriverManager.getConnection("jdbc:mysql://localhost:3306/company","root", "yourpassword");
		Statement sm = c.createStatement();
		int ch;
		String sql;
		do {
			System.out.println("Enter Choice \n 1.Insert	\n 2.Select	\n  3.Update \n 4.Delete \n 5.Exit.");
			Scanner in = new Scanner(System.in);
			ch = in.nextInt();
			switch(ch) {
			case 1:
				sql = "Insert into dep values(25,'Testing','kuwait')";
				sm.executeUpdate(sql);
				System.out.println("New Data inserted !!");
				break;
			case 2:
				sql = "select * from dep";
				ResultSet rs = sm.executeQuery(sql);
			    while(rs.next()) {
			    	System.out.print(rs.getString(1) + "\t");
			    	System.out.print(rs.getString(2) + "\t");
			    	System.out.print(rs.getString(3) + "\t");
			    	System.out.println();
			    }
			    	break;
			case 3 :
				sql = "update dep set loc = 'LA' where depno = 10";
				sm.executeUpdate(sql);
				System.out.println("Record Updated !!");
				break;
			case 4:
				sql = "delete from dep where depno = 40";
				sm.executeUpdate(sql);
				System.out.println("Record Deleted !!");
				break;
			    }
			}while(ch!=5);
		c.close();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
