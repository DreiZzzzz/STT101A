/**
 * @author DREI
 * */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile {
    private int numRecords;
    private DataRecords tempHolder;

    private String desc;
    private int num;

    public DataRecords fileReader(String fileName){
        try {
            Scanner scanner = new Scanner(new File(fileName));

            desc = scanner.nextLine(); // scans the string
            numRecords = scanner.nextInt();

            tempHolder = new DataRecords(desc); // Instantiates recordHolder with the number of nodes and connections

            for (int i = 0; i < numRecords; i++) {
                num = scanner.nextInt();
                tempHolder.addRecord(num);
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("\nFILE DOES NOT EXIST: " + fileName + "\n");
            return null;
        } catch (Exception e) {
            System.out.println("Error while reading the file. Please check the file format."); // Handle other potential exceptions like NoSuchElementException, etc.
            return null;
        }

        return tempHolder;
    }

}
