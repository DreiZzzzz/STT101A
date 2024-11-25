import java.io.FileReader;
import java.util.Scanner;

/**
 * @author DREI
 */
public class Main {

    public static void main(String[] args) {
        //
        Scanner sc = new Scanner(System.in);
        ReadFile readFile = new ReadFile();

        String fileNameCOS;
        String fileNameCCS;

        DataRecords recordHolderCOS;
        DataRecords recordHolderCCS;

        // read cos file
        // Loops until the user enters an existing and valid file name.
        do {
            System.out.print("Enter filename (COS): "); //
            fileNameCCS = sc.nextLine();
            System.out.println(); // prints a newline

            recordHolderCOS = readFile.fileReader(fileNameCCS);
            if (recordHolderCOS == null) {
                System.out.println("Error reading file. Please try again.");
            }
        } while(recordHolderCOS == null);  // re-loop until the file is read correctly

        // read ccs file
        // Loops until the user enters an existing and valid file name.
        do {
            System.out.print("Enter filename (COS): "); //
            fileNameCCS = sc.nextLine();
            System.out.println(); // prints a newline

            recordHolderCOS = readFile.fileReader(fileNameCCS);
            if (recordHolderCOS == null) {
                System.out.println("Error reading file. Please try again.");
            }
        } while(recordHolderCOS == null);  // re-loop until the file is read correctly

    }
}